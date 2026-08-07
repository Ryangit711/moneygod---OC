#!/usr/bin/env python3
"""
FREE DATA FEEDS MODULE
Unified interface for all free market data sources.
Add your API keys to environment variables or config.json.
"""

import os
import json
import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, List, Any
from pathlib import Path

# Load config for API keys
CONFIG_PATH = Path(__file__).parent / "config.json"
if CONFIG_PATH.exists():
    with open(CONFIG_PATH) as f:
        _CONFIG = json.load(f)
    FRED_API_KEY = _CONFIG.get("data_sources", {}).get("fred_api_key", "")
    ALPHAVANTAGE_KEY = _CONFIG.get("data_sources", {}).get("alphavantage_key", os.getenv("ALPHAVANTAGE_KEY", ""))
    FINNHUB_KEY = _CONFIG.get("data_sources", {}).get("finnhub_key", os.getenv("FINNHUB_KEY", ""))
    TWELVE_DATA_KEY = _CONFIG.get("data_sources", {}).get("twelvedata_key", os.getenv("TWELVE_DATA_KEY", ""))
else:
    FRED_API_KEY = os.getenv("FRED_API_KEY", "")
    ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY", "")
    FINNHUB_KEY = os.getenv("FINNHUB_KEY", "")
    TWELVE_DATA_KEY = os.getenv("TWELVE_DATA_KEY", "")

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# ==================== FRED MACRO DATA ====================

def fetch_fred_series(series_id: str, weeks_back: int = 4) -> List[Dict]:
    """Fetch observations from FRED API. Returns list of {date, value} in billions."""
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
        "limit": 20,
    }
    
    try:
        resp = requests.get(FRED_BASE, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        obs = data.get("observations", [])
        # FRED returns values in millions, convert to billions
        return [{"date": o["date"], "value": float(o["value"]) / 1000} for o in obs if o["value"] != "."]
    except Exception as e:
        print(f"[WARN] FRED fetch failed for {series_id}: {e}")
        return []


def get_latest_two_values(series_id: str) -> tuple[Optional[float], Optional[float]]:
    """Get (latest, previous) values in $B from FRED."""
    obs = fetch_fred_series(series_id)
    if len(obs) >= 2:
        return obs[0]["value"], obs[1]["value"]
    elif len(obs) == 1:
        return obs[0]["value"], None
    return None, None


# ==================== ALPHA VANTAGE (FREE TIER: 25 req/day) ====================

def av_get_cpi() -> Optional[float]:
    """Get latest CPI YoY % from Alpha Vantage."""
    if not ALPHAVANTAGE_KEY:
        return None
    url = f"https://www.alphavantage.co/query?function=INFLATION&apikey={ALPHAVANTAGE_KEY}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        # Returns list of dicts with 'value' and 'date'
        if "data" in data and data["data"]:
            return float(data["data"][0]["value"])
    except Exception as e:
        print(f"[WARN] Alpha Vantage CPI failed: {e}")
    return None


def av_get_gdp() -> Optional[float]:
    """Get latest GDP QoQ % from Alpha Vantage."""
    if not ALPHAVANTAGE_KEY:
        return None
    url = f"https://www.alphavantage.co/query?function=REAL_GDP&interval=quarterly&apikey={ALPHAVANTAGE_KEY}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if "data" in data and data["data"]:
            return float(data["data"][0]["value"])
    except Exception as e:
        print(f"[WARN] Alpha Vantage GDP failed: {e}")
    return None


def av_get_unemployment() -> Optional[float]:
    """Get latest unemployment rate from Alpha Vantage."""
    if not ALPHAVANTAGE_KEY:
        return None
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_KEY}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if "data" in data and data["data"]:
            return float(data["data"][0]["value"])
    except Exception as e:
        print(f"[WARN] Alpha Vantage Unemployment failed: {e}")
    return None


def av_get_retail_sales() -> Optional[float]:
    """Get latest retail sales MoM % from Alpha Vantage."""
    if not ALPHAVANTAGE_KEY:
        return None
    url = f"https://www.alphavantage.co/query?function=RETAIL_SALES&apikey={ALPHAVANTAGE_KEY}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if "data" in data and data["data"]:
            return float(data["data"][0]["value"])
    except Exception as e:
        print(f"[WARN] Alpha Vantage Retail Sales failed: {e}")
    return None


# ==================== FINNHUB (FREE: 60 req/min) ====================

def fh_get_economic_calendar() -> List[Dict]:
    """Get economic calendar events from Finnhub."""
    if not FINNHUB_KEY:
        return []
    url = f"https://finnhub.io/api/v1/calendar/economic?token={FINNHUB_KEY}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        return data.get("economic", [])
    except Exception as e:
        print(f"[WARN] Finnhub calendar failed: {e}")
    return []


def fh_get_quote(symbol: str) -> Optional[Dict]:
    """Get real-time quote from Finnhub (works for stocks, forex, crypto)."""
    if not FINNHUB_KEY:
        return None
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_KEY}"
    try:
        r = requests.get(url, timeout=5)
        return r.json()
    except Exception as e:
        print(f"[WARN] Finnhub quote failed for {symbol}: {e}")
    return None


# ==================== TWELVE DATA (FREE: 800 req/day) ====================

def td_get_price(symbol: str, interval: str = "1day", outputsize: int = 30) -> Optional[pd.DataFrame]:
    """Get price history from Twelve Data."""
    if not TWELVE_DATA_KEY:
        return None
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&outputsize={outputsize}&apikey={TWELVE_DATA_KEY}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if "values" in data:
            df = pd.DataFrame(data["values"])
            df["datetime"] = pd.to_datetime(df["datetime"])
            for col in ["open", "high", "low", "close", "volume"]:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
            df = df.sort_values("datetime").reset_index(drop=True)
            return df
    except Exception as e:
        print(f"[WARN] Twelve Data failed for {symbol}: {e}")
    return None


# ==================== YAHOO FINANCE (NO KEY, UNOFFICIAL) ====================

def yf_get_price(symbol: str, period: str = "1mo", interval: str = "1d") -> Optional[pd.DataFrame]:
    """Get price history using yfinance (no API key needed)."""
    try:
        import yfinance as yf
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)
        if not df.empty:
            df = df.reset_index()
            df.columns = [c.lower().replace(" ", "_") for c in df.columns]
            return df
    except Exception as e:
        print(f"[WARN] yfinance failed for {symbol}: {e}")
    return None


def yf_get_multiple(symbols: List[str], period: str = "1mo") -> Dict[str, pd.DataFrame]:
    """Get multiple symbols at once."""
    result = {}
    for sym in symbols:
        result[sym] = yf_get_price(sym, period=period)
    return result


# ==================== VIX / DXY / FUTURES QUICK SNAPSHOTS ====================

def get_vix_dxy_quick() -> tuple[float, float, str]:
    """
    Quick snapshot of VIX and DXY using free endpoints.
    Returns (vix, dxy, dxy_direction)
    """
    vix = 14.2
    dxy = 103.45
    dxy_dir = "flat"
    
    # Try Finnhub for VIX (symbol: VIX)
    vix_data = fh_get_quote("VIX")
    if vix_data and "c" in vix_data:
        vix = float(vix_data["c"])
    
    # Try Finnhub for DXY (symbol: DXY)
    dxy_data = fh_get_quote("DXY")
    if dxy_data and "c" in dxy_data and "pc" in dxy_data:
        dxy = float(dxy_data["c"])
        prev = float(dxy_data["pc"])
        dxy_dir = "up" if dxy > prev else ("down" if dxy < prev else "flat")
    
    return vix, dxy, dxy_dir


def get_futures_gaps() -> tuple[float, float]:
    """Get MES and MNQ overnight gaps using yfinance."""
    mes_gap = 0.0
    mnq_gap = 0.0
    
    # MES=F for E-mini S&P 500, NQ=F for Nasdaq 100
    mes_data = yf_get_price("ES=F", period="2d", interval="1d")
    if mes_data is not None and len(mes_data) >= 2:
        prev_close = mes_data.iloc[-2]["close"]
        curr_open = mes_data.iloc[-1]["open"]
        mes_gap = round((curr_open - prev_close) * 10, 1)  # ES points (1 point = $50)
    
    nq_data = yf_get_price("NQ=F", period="2d", interval="1d")
    if nq_data is not None and len(nq_data) >= 2:
        prev_close = nq_data.iloc[-2]["close"]
        curr_open = nq_data.iloc[-1]["open"]
        mnq_gap = round((curr_open - prev_close) * 5, 1)  # NQ points (1 point = $20)
    
    return mes_gap, mnq_gap


# ==================== COMBINE ALL FOR PLUMBING ====================

def fetch_all_plumbing_raw() -> Dict[str, Any]:
    """
    Fetch all raw data needed for plumbing pipeline.
    Returns dict with all fields for RawPlumbingData.
    """
    # FRED macro data
    fed_bs_latest, fed_bs_prev = get_latest_two_values("WALCL")
    tga_latest, tga_prev = get_latest_two_values("WDTGAL")
    rrp_latest, rrp_prev = get_latest_two_values("RRPONTSYD")
    
    # Fallback values if FRED fails
    if fed_bs_latest is None:
        fed_bs_latest, fed_bs_prev = 7200, 7180
    if tga_latest is None:
        tga_latest, tga_prev = 650, 600
    if rrp_latest is None:
        rrp_latest, rrp_prev = 400, 420
    
    # Market data
    vix, dxy, dxy_dir = get_vix_dxy_quick()
    mes_gap, mnq_gap = get_futures_gaps()
    
    # SOFR - use FRED or fallback
    sofr_latest, _ = get_latest_two_values("SOFR")
    if sofr_latest is None:
        sofr_latest = 5.33
    
    # Economic calendar for news
    econ_events = fh_get_economic_calendar()
    high_impact_today = []
    now = datetime.now(timezone.utc)
    today = now.date()
    for ev in econ_events:
        if ev.get("impact") == "high":
            try:
                ev_date = datetime.fromisoformat(ev["date"].replace("Z", "+00:00")).date()
                if ev_date == today:
                    high_impact_today.append(f"{ev['country']}: {ev['event']}")
            except:
                pass
    
    news_today = "; ".join(high_impact_today[:3]) if high_impact_today else "No high-impact events today"
    
    return {
        "fed_bs": fed_bs_latest,
        "tga": tga_latest,
        "rrp": rrp_latest,
        "fed_bs_prev": fed_bs_prev,
        "tga_prev": tga_prev,
        "rrp_prev": rrp_prev,
        "sofr": sofr_latest,
        "vix": vix,
        "dxy": dxy,
        "dxy_direction": dxy_dir,
        "mes_gap_pts": mes_gap,
        "mnq_gap_pts": mnq_gap,
        "news_today": news_today,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


# ==================== CORRELATION / HEATMAP DATA ====================

def get_correlation_basket(symbols: List[str] = None, period: str = "3mo") -> pd.DataFrame:
    """Get correlation matrix for a basket of symbols."""
    if symbols is None:
        symbols = ["ES=F", "NQ=F", "BTC-USD", "GC=F", "CL=F", "EURUSD=X", "JPY=X", "ZN=F"]
    
    data = yf_get_multiple(symbols, period=period)
    closes = {}
    for sym, df in data.items():
        if df is not None and not df.empty and "close" in df.columns:
            closes[sym] = df.set_index("date")["close"]
    
    if not closes:
        return pd.DataFrame()
    
    price_df = pd.DataFrame(closes).dropna()
    returns = price_df.pct_change().dropna()
    return returns.corr()


if __name__ == "__main__":
    # Quick test
    print("Testing data feeds...")
    raw = fetch_all_plumbing_raw()
    for k, v in raw.items():
        print(f"  {k}: {v}")
    
    print("\nTesting correlation basket...")
    corr = get_correlation_basket()
    print(corr.round(2))