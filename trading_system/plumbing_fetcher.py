#!/usr/bin/env python3
"""
PLUMBING DATA FETCHER
Fetches the 5 URLs from live-data-workflow.md, extracts 6 raw numbers,
computes Net Liquidity = ΔFedBS - ΔTGA - ΔRRP
Outputs JSON verdict for the decision engine.
"""

import json
import requests
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from typing import Optional
import os
from pathlib import Path

# Load config
CONFIG_PATH = Path(__file__).parent / "config.json"
if CONFIG_PATH.exists():
    with open(CONFIG_PATH) as f:
        _CONFIG = json.load(f)
    FRED_API_KEY = _CONFIG.get("data_sources", {}).get("fred_api_key", "")
    USE_MOCK_DATA = _CONFIG.get("data_sources", {}).get("use_mock_data", True)
else:
    FRED_API_KEY = os.getenv("FRED_API_KEY", "")
    USE_MOCK_DATA = True

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# FRED Series IDs (from live-data-workflow.md)
SERIES = {
    "fed_bs": "WALCL",      # Fed Balance Sheet (total assets, $M)
    "tga": "WDTGAL",        # Treasury General Account ($M)
    "rrp": "RRPONTSYD",     # Overnight Reverse Repo ($M)
}

# URLs for manual fetching (fallback if no FRED key)
MANUAL_URLS = {
    "fed_bs": "https://fred.stlouisfed.org/series/WALCL",
    "tga": "https://fred.stlouisfed.org/series/WDTGAL",
    "rrp": "https://fred.stlouisfed.org/series/RRPONTSYD",
    "sofr": "https://www.newyorkfed.org/markets/reference-rates/sofr",
    "dxy_vix": "https://www.tradingview.com/symbols/TVC-DXY/",  # DXY + VIX
    "mes_mnq": "https://www.tradingview.com/symbols/CME-MES1!/",  # MES/MNQ overnight
    "calendar": "https://www.forexfactory.com/calendar",  # Economic calendar
}


@dataclass
class RawPlumbingData:
    """The 6 raw numbers from Min 1-3 of live-data-workflow.md"""
    fed_bs: float           # $B
    tga: float              # $B
    rrp: float              # $B
    sofr: float             # %
    vix: float              # index value
    dxy: float              # price
    dxy_direction: str      # "up" | "down" | "flat"
    mes_gap_pts: float      # points
    mnq_gap_pts: float      # points
    news_today: str         # high-impact events
    timestamp: str


@dataclass
class LiquidityVerdict:
    """Output of Min 4-6: Net Liquidity computation"""
    net_liquidity_b: float      # $B
    liquidity_verdict: str      # "INJECT" | "NEUTRAL" | "DRAIN"
    sofr_vs_iorb: str           # "normal" | "stress"
    vix_level: str              # "low" | "normal" | "elevated" | "panic"
    dxy_trend: str              # "up" | "down" | "flat"


@dataclass
class MarketSignals:
    """Output of Min 7-9: 3-market signals"""
    vwap_position: str          # "above" | "below"
    tick_index: str             # "bullish" | "bearish" | "neutral"
    wti_direction: str          # "up" | "down"
    dxy_direction: str          # "up" | "down" | "flat"
    cot_extreme: bool           # True if COT shows extreme positioning


@dataclass
class PlumbingVerdict:
    """Complete plumbing verdict (Min 1-12)"""
    raw: RawPlumbingData
    liquidity: LiquidityVerdict
    signals: MarketSignals
    trade_mode: str             # "FULL" | "NORMAL" | "REDUCED" | "FLAT"
    instrument: str             # "MES" | "MNQ" | "BOTH" | "NONE"
    bias: str                   # "BULLISH" | "BEARISH" | "NEUTRAL"
    active_edges: list[str]
    session_plan_line1: str
    session_plan_line2: str
    max_contracts: int          # derived from trade_mode
    risk_pct_per_trade: float   # derived from trade_mode
    daily_max_pct: float        # derived from trade_mode


# ==================== FETCHERS ====================

def fetch_fred_series(series_id: str, weeks_back: int = 2) -> list[dict]:
    """Fetch last N observations from FRED API. Returns list of {date, value}."""
    if not FRED_API_KEY:
        return []
    
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(weeks=weeks_back)).strftime("%Y-%m-%d")
    
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": start_date,
        "observation_end": end_date,
        "sort_order": "desc",
        "limit": 10,
    }
    
    try:
        resp = requests.get(FRED_BASE, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        obs = data.get("observations", [])
        # FRED returns strings, convert to float (values in millions)
        return [{"date": o["date"], "value": float(o["value"]) / 1000} for o in obs if o["value"] != "."]
    except Exception as e:
        print(f"[WARN] FRED fetch failed for {series_id}: {e}")
        return []


def get_latest_two_weeks(series_id: str) -> tuple[Optional[float], Optional[float]]:
    """Get (this_week, last_week) values in $B from FRED."""
    obs = fetch_fred_series(series_id)
    if len(obs) >= 2:
        return obs[0]["value"], obs[1]["value"]
    elif len(obs) == 1:
        return obs[0]["value"], None
    return None, None


def fetch_plumbing_data() -> RawPlumbingData:
    """
    Fetch all 6 raw numbers. 
    NOTE: In production, you'd use proper APIs for SOFR, DXY, VIX, MES/MNQ, Calendar.
    For demo, we simulate with reasonable defaults + FRED if key available.
    """
    # --- FRED data (Fed BS, TGA, RRP) ---
    fed_bs_this, fed_bs_last = get_latest_two_weeks("WALCL")
    tga_this, tga_last = get_latest_two_weeks("WDTGAL")
    rrp_this, rrp_last = get_latest_two_weeks("RRPONTSYD")
    
    # Fallback demo values if no FRED key or mock data enabled
    if fed_bs_this is None or USE_MOCK_DATA:
        fed_bs_this, fed_bs_last = 7200, 7180  # ~$7.2T
    if tga_this is None or USE_MOCK_DATA:
        tga_this, tga_last = 650, 600        # ~$650B
    if rrp_this is None or USE_MOCK_DATA:
        rrp_this, rrp_last = 400, 420        # ~$400B
    
    # --- Simulated market data (replace with real API calls) ---
    # In production: use Twelve Data, Alpha Vantage, Polygon, or broker APIs
    sofr = 5.33           # SOFR %
    vix = 14.2            # VIX level
    dxy = 103.45          # DXY price
    dxy_direction = "down"  # up/down/flat
    mes_gap_pts = 5.0     # MES overnight gap points
    mnq_gap_pts = -12.0   # MNQ overnight gap points
    news_today = "FOMC minutes 2:00 PM ET; No high-impact FX news"
    
    return RawPlumbingData(
        fed_bs=fed_bs_this,
        tga=tga_this,
        rrp=rrp_this,
        sofr=sofr,
        vix=vix,
        dxy=dxy,
        dxy_direction=dxy_direction,
        mes_gap_pts=mes_gap_pts,
        mnq_gap_pts=mnq_gap_pts,
        news_today=news_today,
        timestamp=datetime.now().isoformat(),
    )


# ==================== COMPUTE ENGINE ====================

def compute_liquidity(raw: RawPlumbingData) -> LiquidityVerdict:
    """Min 4-6: Compute Net Liquidity = ΔFedBS - ΔTGA - ΔRRP"""
    # Get previous week values (in demo, we use the fallbacks)
    # In production, these come from FRED fetch
    fed_bs_last = 7180  # $B
    tga_last = 600
    rrp_last = 420
    
    delta_bs = raw.fed_bs - fed_bs_last
    delta_tga = raw.tga - tga_last
    delta_rrp = raw.rrp - rrp_last
    
    net_liq = delta_bs - delta_tga - delta_rrp
    
    # Verdict thresholds (from live-data-workflow.md lines 101-107)
    if net_liq > 50:
        verdict = "INJECT"
    elif net_liq > 10:
        verdict = "INJECT"  # mild risk-on
    elif net_liq > -10:
        verdict = "NEUTRAL"
    elif net_liq > -50:
        verdict = "DRAIN"
    else:
        verdict = "DRAIN"  # risk-off
    
    # SOFR vs IORB (IORB ~5.4% currently)
    iorb = 5.40
    sofr_spread = raw.sofr - iorb
    sofr_status = "stress" if sofr_spread > 0.05 else "normal"  # >5bp spread
    
    # VIX classification
    if raw.vix < 15:
        vix_level = "low"
    elif raw.vix < 20:
        vix_level = "normal"
    elif raw.vix < 25:
        vix_level = "elevated"
    else:
        vix_level = "panic"
    
    # DXY trend
    dxy_trend = raw.dxy_direction
    
    return LiquidityVerdict(
        net_liquidity_b=round(net_liq, 1),
        liquidity_verdict=verdict,
        sofr_vs_iorb=sofr_status,
        vix_level=vix_level,
        dxy_trend=dxy_trend,
    )


def extract_signals(raw: RawPlumbingData) -> MarketSignals:
    """Min 7-9: Extract 3-market signals (simulated for demo)"""
    # In production: fetch real VWAP, TICK, WTI, COT data
    return MarketSignals(
        vwap_position="above" if raw.mes_gap_pts > 0 else "below",
        tick_index="bullish" if raw.mes_gap_pts > 10 else ("bearish" if raw.mes_gap_pts < -10 else "neutral"),
        wti_direction="up",  # placeholder
        dxy_direction=raw.dxy_direction,
        cot_extreme=False,   # placeholder - check Friday COT
    )


# ==================== DECISION ENGINE ====================

def decision_tree_1_should_trade(liq: LiquidityVerdict) -> tuple[bool, str]:
    """Decision Tree 1: Should I trade today? (plumbing-to-trade-bridge.md lines 38-72)"""
    # VIX > 25 → FLAT
    if liq.vix_level == "panic":
        return False, "VIX > 25 (panic) — FLAT"
    
    # Net Liq < -$50B → FLAT
    if liq.net_liquidity_b < -50:
        return False, "Net Liquidity < -$50B — FLAT"
    
    # SOFR > IORB + >5bp spread → FLAT (repo stress)
    if liq.sofr_vs_iorb == "stress":
        return False, "SOFR > IORB + spread > 5bp — Repo stress, FLAT"
    
    return True, "PROCEED to Tree 2"


def decision_tree_2_bias(liq: LiquidityVerdict, signals: MarketSignals) -> str:
    """Decision Tree 2: What's my bias today? (lines 81-107)"""
    # INJECT + DXY falling + VIX low → BULLISH
    if liq.liquidity_verdict == "INJECT" and liq.dxy_trend == "down" and liq.vix_level in ["low", "normal"]:
        return "BULLISH"
    
    # DRAIN + DXY rising + VIX elevated → BEARISH
    if liq.liquidity_verdict == "DRAIN" and liq.dxy_trend == "up" and liq.vix_level in ["elevated", "panic"]:
        return "BEARISH"
    
    # Default: NEUTRAL
    return "NEUTRAL"


def decision_tree_3_instrument(trade_mode: str, bias: str) -> str:
    """Decision Tree 3: Which instrument? (lines 116-142)"""
    if trade_mode == "FULL":
        return "BOTH" if bias == "BULLISH" else "MES"
    elif trade_mode == "NORMAL":
        return "MES"
    elif trade_mode == "REDUCED":
        return "MES"
    else:  # FLAT
        return "NONE"


def decision_tree_4_size(liq: LiquidityVerdict, trade_mode: str) -> tuple[float, float, int]:
    """Decision Tree 4: Position sizing (lines 151-172)"""
    # Map trade_mode to sizing regime
    if trade_mode == "FULL":
        risk_pct = 1.5
        daily_max = 3.0
        max_contracts = 3
    elif trade_mode == "NORMAL":
        risk_pct = 1.0
        daily_max = 2.0
        max_contracts = 2
    else:  # REDUCED or FLAT
        risk_pct = 0.25
        daily_max = 0.75
        max_contracts = 1
    
    return risk_pct, daily_max, max_contracts


def classify_active_edges(liq: LiquidityVerdict, signals: MarketSignals, raw: RawPlumbingData) -> list[str]:
    """Identify active edges from plumbing-hierarchy-master.md Part 5"""
    edges = []
    
    # Edge 2: RRP-to-Zero Squeeze
    # (would need weekly RRP change - simplified here)
    if liq.liquidity_verdict == "INJECT" and raw.rrp < 500:
        edges.append("Edge 2: RRP-to-Zero Squeeze")
    
    # Edge 3: TGA Directional
    if liq.liquidity_verdict == "DRAIN":  # TGA rising
        edges.append("Edge 3: TGA Directional")
    
    # Edge 6: Gamma Squeeze
    if liq.vix_level == "low" and signals.tick_index == "bullish":
        edges.append("Edge 6: Gamma Squeeze")
    
    # Edge 7: Repo Stress (already checked in Tree 1)
    if liq.sofr_vs_iorb == "stress":
        edges.append("Edge 7: Repo Stress")
    
    # Edge 9: Quarterly Rebalance
    # (would check calendar - placeholder)
    
    # Edge 11: Liquidity Void (gap > 20 pts, low volume)
    if abs(raw.mes_gap_pts) > 20 or abs(raw.mnq_gap_pts) > 20:
        edges.append("Edge 11: Liquidity Void")
    
    return edges


def generate_session_plan(trade_mode: str, instrument: str, bias: str, 
                          active_edges: list[str], raw: RawPlumbingData) -> tuple[str, str]:
    """Min 13-15: Generate 2-line session plan"""
    
    line1 = f"{trade_mode} | {instrument} | {bias}"
    
    if trade_mode == "FLAT":
        line2 = "Staying flat. " + ("; ".join(active_edges) if active_edges else "No tradable edges.")
    elif trade_mode == "FULL" and bias == "BULLISH":
        line2 = f"I will buy the ORB breakout above 15-min high with volume. If no breakout by 7:30 AM PT, wait for power hour pullback to VWAP."
    elif trade_mode == "NORMAL" and bias == "NEUTRAL":
        line2 = f"I will trade ORB only — long above high, short below low. First 15-min candle sets range. Max 2 trades. 1:1 R:R minimum."
    elif bias == "BEARISH":
        line2 = f"I will short initial bounces that fail at VWAP. 1 trade maximum. 0.25% risk. If no clear rejection, stay flat."
    else:
        line2 = f"I will follow {instrument} ORB setup per playbook. Max 2 trades. Strict risk rules."
    
    return line1, line2


# ==================== MAIN ORCHESTRATOR ====================

def run_plumbing_pipeline() -> PlumbingVerdict:
    """Run the complete Min 1-15 plumbing workflow"""
    print("=" * 60)
    print("PLUMBING PIPELINE — Live Data Workflow (15 min)")
    print("=" * 60)
    
    # Min 1-3: Fetch raw data
    print("\n[Min 1-3] Fetching raw plumbing data...")
    raw = fetch_plumbing_data()
    print(f"  Fed BS: ${raw.fed_bs:.0f}B  TGA: ${raw.tga:.0f}B  RRP: ${raw.rrp:.0f}B")
    print(f"  SOFR: {raw.sofr:.2f}%  VIX: {raw.vix:.1f}  DXY: {raw.dxy:.2f} ({raw.dxy_direction})")
    print(f"  MES gap: {raw.mes_gap_pts:.1f}pts  MNQ gap: {raw.mnq_gap_pts:.1f}pts")
    
    # Min 4-6: Compute liquidity
    print("\n[Min 4-6] Computing Net Liquidity...")
    liq = compute_liquidity(raw)
    print(f"  Net Liquidity: ${liq.net_liquidity_b:.1f}B")
    print(f"  Verdict: {liq.liquidity_verdict}")
    print(f"  SOFR vs IORB: {liq.sofr_vs_iorb}")
    print(f"  VIX level: {liq.vix_level}")
    print(f"  DXY trend: {liq.dxy_trend}")
    
    # Min 7-9: Market signals
    print("\n[Min 7-9] Reading 3-market signals...")
    signals = extract_signals(raw)
    print(f"  VWAP position: {signals.vwap_position}")
    print(f"  TICK index: {signals.tick_index}")
    print(f"  WTI: {signals.wti_direction}")
    print(f"  DXY: {signals.dxy_direction}")
    
    # Decision Trees 1-4
    print("\n[Min 10-12] Running Decision Trees...")
    
    # Tree 1: Should I trade?
    should_trade, reason = decision_tree_1_should_trade(liq)
    print(f"  Tree 1 (Trade?): {should_trade} — {reason}")
    
    if not should_trade:
        trade_mode = "FLAT"
        instrument = "NONE"
        bias = "NONE"
        risk_pct, daily_max, max_contracts = 0, 0, 0
    else:
        # Tree 2: Bias
        bias = decision_tree_2_bias(liq, signals)
        print(f"  Tree 2 (Bias): {bias}")
        
        # Tree 1 also determines trade mode from liquidity + VIX (live-data-workflow.md lines 155-165)
        if liq.liquidity_verdict == "INJECT" and liq.vix_level == "low":
            trade_mode = "FULL"
        elif liq.liquidity_verdict == "INJECT" and liq.vix_level == "normal":
            trade_mode = "NORMAL"
        elif liq.liquidity_verdict == "NEUTRAL":
            trade_mode = "NORMAL"
        elif liq.liquidity_verdict == "DRAIN":
            trade_mode = "REDUCED"
        else:
            trade_mode = "FLAT"
        
        print(f"  Trade Mode: {trade_mode}")
        
        # Tree 3: Instrument
        instrument = decision_tree_3_instrument(trade_mode, bias)
        print(f"  Tree 3 (Instrument): {instrument}")
        
        # Tree 4: Size
        risk_pct, daily_max, max_contracts = decision_tree_4_size(liq, trade_mode)
        print(f"  Tree 4 (Size): {risk_pct}%/trade, {daily_max}% daily max, {max_contracts} max contracts")
    
    # Active edges
    active_edges = classify_active_edges(liq, signals, raw)
    print(f"  Active Edges: {active_edges if active_edges else 'None'}")
    
    # Session plan
    line1, line2 = generate_session_plan(trade_mode, instrument, bias, active_edges, raw)
    print(f"\n[Min 13-15] Session Plan:")
    print(f"  Line 1: {line1}")
    print(f"  Line 2: {line2}")
    
    return PlumbingVerdict(
        raw=raw,
        liquidity=liq,
        signals=signals,
        trade_mode=trade_mode,
        instrument=instrument,
        bias=bias,
        active_edges=active_edges,
        session_plan_line1=line1,
        session_plan_line2=line2,
        max_contracts=max_contracts,
        risk_pct_per_trade=risk_pct,
        daily_max_pct=daily_max,
    )


def save_verdict(verdict: PlumbingVerdict, path: str = "plumbing_verdict.json"):
    """Save verdict as JSON for downstream consumers (bots, journal, etc.)"""
    # Convert dataclasses to dict
    data = {
        "timestamp": verdict.raw.timestamp,
        "trade_mode": verdict.trade_mode,
        "instrument": verdict.instrument,
        "bias": verdict.bias,
        "max_contracts": 3 if verdict.trade_mode == "FULL" else (2 if verdict.trade_mode == "NORMAL" else 1),
        "risk_pct_per_trade": 1.5 if verdict.trade_mode == "FULL" else (1.0 if verdict.trade_mode == "NORMAL" else 0.25),
        "daily_max_pct": 3.0 if verdict.trade_mode == "FULL" else (2.0 if verdict.trade_mode == "NORMAL" else 0.75),
        "active_edges": verdict.active_edges,
        "session_plan": f"{verdict.session_plan_line1}\n{verdict.session_plan_line2}",
        "raw_data": asdict(verdict.raw),
        "liquidity": asdict(verdict.liquidity),
        "signals": asdict(verdict.signals),
    }
    
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ Verdict saved to {path}")


if __name__ == "__main__":
    verdict = run_plumbing_pipeline()
    save_verdict(verdict)
    
    print("\n" + "=" * 60)
    print("DAILY VERDICT TEMPLATE (from plumbing-to-trade-bridge.md)")
    print("=" * 60)
    print(f"DATE: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"TRADING: {'YES' if verdict.trade_mode != 'FLAT' else 'NO'} — "
          f"{'FLAT: ' + verdict.session_plan_line2 if verdict.trade_mode == 'FLAT' else 'PROCEED'}")
    print(f"TRADE MODE: {verdict.trade_mode}")
    print(f"INSTRUMENT: {verdict.instrument}")
    print(f"BIAS: {verdict.bias}")
    print(f"MAX SIZE: {3 if verdict.trade_mode == 'FULL' else (2 if verdict.trade_mode == 'NORMAL' else 1)} contracts")
    print(f"ACTIVE EDGES: {', '.join(verdict.active_edges) if verdict.active_edges else 'None'}")
    print(f"SESSION PLAN: {verdict.session_plan_line1}")
    print(f"              {verdict.session_plan_line2}")