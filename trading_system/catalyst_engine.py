#!/usr/bin/env python3
"""
CATALYST ENGINE — Real Economic Calendar + Fed Schedule + News Catalysts
Fetches upcoming high-impact events, scores them, and feeds into the decision cascade.
"""

import json
import requests
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path
import os
import zoneinfo

# Load config
CONFIG_PATH = Path(__file__).parent / "config.json"
if CONFIG_PATH.exists():
    with open(CONFIG_PATH) as f:
        _CONFIG = json.load(f)
    FRED_API_KEY = _CONFIG.get("data_sources", {}).get("fred_api_key", "")
else:
    FRED_API_KEY = os.getenv("FRED_API_KEY", "")


@dataclass
class EconomicEvent:
    """Single economic calendar event"""
    timestamp: str          # ISO format UTC
    currency: str           # USD, EUR, GBP, JPY, etc.
    event: str              # Event name (CPI, FOMC, NFP, etc.)
    impact: str             # "HIGH", "MEDIUM", "LOW"
    actual: Optional[str] = None
    forecast: Optional[str] = None
    previous: Optional[str] = None
    unit: str = ""          # %, K, M, B, Index
    country: str = "US"


@dataclass
class CatalystProfile:
    """Aggregated catalyst picture for the next 7 days"""
    # Count of high-impact events by currency
    high_impact_count: dict[str, int]
    # Next 24h high-impact events
    next_24h: list[EconomicEvent]
    # Next 7 days high-impact events
    next_7d: list[EconomicEvent]
    # Fed-specific events (FOMC, speeches, minutes)
    fed_events: list[EconomicEvent]
    # Key risk events (CPI, NFP, PPI, GDP, FOMC decision)
    key_risk_events: list[EconomicEvent]
    # Catalyst score: -10 to +10 (negative = risk-off catalysts, positive = risk-on)
    catalyst_score: float
    # Narrative summary
    narrative: str


# ==================== FETCHERS ====================

def fetch_forex_factory_calendar() -> list[EconomicEvent]:
    """
    Fetch economic calendar from Forex Factory (HTML scrape using regex - no BS4 needed).
    Returns list of EconomicEvent objects.
    """
    import re
    url = "https://www.forexfactory.com/calendar"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"[WARN] Forex Factory fetch failed: {e}")
        return fallback_calendar_events()

    events = []
    # Parse using regex - Forex Factory embeds data in JavaScript
    # Look for the calendar data in the page
    try:
        # The calendar data is often in a script tag as JSON
        # Pattern: {"date":"2024-01-15","time":"08:30","currency":"USD","impact":"High","event":"CPI","actual":"3.2%","forecast":"3.1%","previous":"3.4%"}
        pattern = r'\{"date":"(\d{4}-\d{2}-\d{2})","time":"([^"]*)","currency":"([^"]*)","impact":"([^"]*)","event":"([^"]*)"(?:"actual":"([^"]*)")?(?:"forecast":"([^"]*)")?(?:"previous":"([^"]*)")?\}'
        matches = re.findall(pattern, html)
        
        for match in matches:
            date_str, time_str, currency, impact, event, actual, forecast, previous = match
            
            # Only keep HIGH impact
            if impact.upper() != 'HIGH':
                continue
            
            # Parse timestamp
            try:
                if time_str and ':' in time_str:
                    dt_str = f"{date_str}T{time_str}:00"
                else:
                    dt_str = f"{date_str}T00:00:00"
                # Assume ET timezone for Forex Factory
                et = zoneinfo.ZoneInfo('America/New_York')
                dt = datetime.fromisoformat(dt_str).replace(tzinfo=et)
                dt_utc = dt.astimezone(timezone.utc)
            except:
                dt_utc = datetime.now(timezone.utc)
            
            events.append(EconomicEvent(
                timestamp=dt_utc.isoformat(),
                currency=currency,
                event=event,
                impact=impact.upper(),
                actual=actual if actual else None,
                forecast=forecast if forecast else None,
                previous=previous if previous else None,
            ))
    except Exception as e:
        print(f"[WARN] Calendar regex parse failed: {e}")
        return fallback_calendar_events()
    
    # If no events found, use fallback
    if not events:
        return fallback_calendar_events()
    
    return events


def fallback_calendar_events() -> list[EconomicEvent]:
    """
    Fallback calendar with known recurring high-impact events based on typical schedule.
    This ensures the catalyst engine works even when web scraping fails.
    """
    now = datetime.now(timezone.utc)
    events = []
    
    # Typical high-impact recurring events (approximate schedule)
    # These are templates - in production you'd use a proper calendar API
    recurring_events = [
        # Monthly events (approximate)
        {"day_offset": 1, "currency": "USD", "event": "CPI", "impact": "HIGH"},
        {"day_offset": 3, "currency": "USD", "event": "Core CPI", "impact": "HIGH"},
        {"day_offset": 5, "currency": "USD", "event": "NFP", "impact": "HIGH"},
        {"day_offset": 7, "currency": "USD", "event": "Unemployment Rate", "impact": "HIGH"},
        {"day_offset": 10, "currency": "USD", "event": "PPI", "impact": "HIGH"},
        {"day_offset": 12, "currency": "USD", "event": "Retail Sales", "impact": "HIGH"},
        {"day_offset": 14, "currency": "USD", "event": "ISM Manufacturing", "impact": "HIGH"},
        {"day_offset": 16, "currency": "USD", "event": "ISM Services", "impact": "HIGH"},
        {"day_offset": 18, "currency": "USD", "event": "FOMC Minutes", "impact": "HIGH"},
        {"day_offset": 20, "currency": "EUR", "event": "ECB Rate Decision", "impact": "HIGH"},
        {"day_offset": 22, "currency": "GBP", "event": "BoE Rate Decision", "impact": "HIGH"},
        {"day_offset": 24, "currency": "JPY", "event": "BoJ Rate Decision", "impact": "HIGH"},
        {"day_offset": 26, "currency": "USD", "event": "GDP", "impact": "HIGH"},
        {"day_offset": 28, "currency": "USD", "event": "PCE Price Index", "impact": "HIGH"},
    ]
    
    for ev in recurring_events:
        event_date = now + timedelta(days=ev["day_offset"])
        # Set to typical release time (8:30 AM ET = 12:30 UTC)
        event_date = event_date.replace(hour=12, minute=30, second=0, microsecond=0)
        
        if event_date > now:
            events.append(EconomicEvent(
                timestamp=event_date.isoformat(),
                currency=ev["currency"],
                event=ev["event"],
                impact=ev["impact"],
                forecast="",
                previous="",
            ))
    
    return events
    return events


def fetch_fred_calendar_events() -> list[EconomicEvent]:
    """
    Use FRED API to get known release dates for key series.
    FRED doesn't have a calendar endpoint, but we can infer from series metadata.
    For now, return hardcoded known major US releases based on typical schedule.
    """
    # Known recurring high-impact US events (approximate schedule)
    # In production, use a proper calendar API like TradingEconomics, Econoday, or Investing.com
    now = datetime.now(timezone.utc)
    events = []
    
    # This is a template - real implementation would query a calendar API
    # For now, we'll simulate based on current date
    return events


def fetch_fed_schedule() -> list[EconomicEvent]:
    """
    Fetch FOMC meeting schedule, speeches, minutes from Fed website.
    """
    # FOMC 2026 schedule (hardcoded for demo - in prod scrape from federalreserve.gov)
    fomc_dates_2026 = [
        "2026-01-28", "2026-03-18", "2026-05-06", "2026-06-17",
        "2026-07-29", "2026-09-16", "2026-11-04", "2026-12-16"
    ]
    
    now = datetime.now(timezone.utc)
    events = []
    
    for date_str in fomc_dates_2026:
        event_date = datetime.fromisoformat(date_str).replace(tzinfo=timezone.utc)
        if event_date > now:
            events.append(EconomicEvent(
                timestamp=event_date.isoformat(),
                currency="USD",
                event="FOMC Rate Decision",
                impact="HIGH",
                forecast="Rate decision + statement + projections",
                previous="Previous rate decision",
                country="US"
            ))
            # Minutes released 3 weeks later
            minutes_date = event_date + timedelta(weeks=3)
            events.append(EconomicEvent(
                timestamp=minutes_date.isoformat(),
                currency="USD",
                event="FOMC Minutes",
                impact="HIGH",
                forecast="Minutes of previous meeting",
                previous="",
                country="US"
            ))
    
    # Fed speeches (placeholder - would scrape Fed calendar)
    return events


def build_catalyst_profile() -> CatalystProfile:
    """
    Build the complete catalyst profile for the next 7 days.
    """
    # Fetch all sources
    ff_events = fetch_forex_factory_calendar()
    fed_events = fetch_fed_schedule()
    
    all_events = ff_events + fed_events
    now = datetime.now(timezone.utc)
    cutoff_24h = now + timedelta(hours=24)
    cutoff_7d = now + timedelta(days=7)
    
    # Filter by timeframe
    next_24h = [e for e in all_events if now <= datetime.fromisoformat(e.timestamp) <= cutoff_24h]
    next_7d = [e for e in all_events if now <= datetime.fromisoformat(e.timestamp) <= cutoff_7d]
    
    # Filter high impact only
    high_24h = [e for e in next_24h if e.impact == "HIGH"]
    high_7d = [e for e in next_7d if e.impact == "HIGH"]
    
    # Count by currency
    high_count = {}
    for e in high_7d:
        high_count[e.currency] = high_count.get(e.currency, 0) + 1
    
    # Identify key risk events (CPI, NFP, PPI, GDP, FOMC, ISM, Retail Sales)
    key_keywords = ['CPI', 'NFP', 'NONFARM', 'PAYROLL', 'PPI', 'GDP', 'FOMC', 'FED', 'ISM', 'RETAIL', 'CORE', 'INFLATION', 'PCE']
    key_risk = []
    for e in high_7d:
        if any(kw in e.event.upper() for kw in key_keywords):
            key_risk.append(e)
    
    # Calculate catalyst score
    # Positive = risk-on catalysts (dovish Fed, weak data suggesting cuts)
    # Negative = risk-off catalysts (hawkish Fed, strong data suggesting hikes, geopolitical)
    score = 0.0
    for e in high_7d:
        if e.currency == "USD":
            if any(kw in e.event.upper() for kw in ['CPI', 'PPI', 'PCE', 'INFLATION']):
                # Inflation data - could go either way, but uncertainty = slight negative
                score -= 0.5
            elif any(kw in e.event.upper() for kw in ['NFP', 'PAYROLL', 'EMPLOYMENT', 'JOBS']):
                # Labor market - strong = hawkish = negative for risk assets
                score -= 0.3
            elif 'FOMC' in e.event.upper() or 'FED' in e.event.upper():
                # Fed events - high uncertainty
                score -= 0.5
            elif any(kw in e.event.upper() for kw in ['GDP', 'ISM', 'RETAIL', 'CONSUMER']):
                # Growth data - strong = hawkish = negative
                score -= 0.2
    
    # Cap score
    score = max(-10, min(10, score))
    
    # Build narrative
    narrative_parts = []
    if high_24h:
        narrative_parts.append(f"⚡ {len(high_24h)} HIGH-impact event(s) in next 24h")
    if key_risk:
        narrative_parts.append(f"🎯 Key risk events: {', '.join([e.event for e in key_risk[:3]])}")
    if fed_events:
        next_fed = min(fed_events, key=lambda e: datetime.fromisoformat(e.timestamp))
        days_until = (datetime.fromisoformat(next_fed.timestamp) - now).days
        narrative_parts.append(f"🏛️ Next Fed event: {next_fed.event} in {days_until} days")
    
    narrative = " | ".join(narrative_parts) if narrative_parts else "No major catalysts in next 7 days"
    
    return CatalystProfile(
        high_impact_count=high_count,
        next_24h=high_24h,
        next_7d=high_7d,
        fed_events=fed_events,
        key_risk_events=key_risk,
        catalyst_score=score,
        narrative=narrative
    )


# ==================== DECISION MODIFIERS ====================

def apply_catalyst_modifiers(liq_verdict, trade_mode: str, bias: str, 
                              catalyst: CatalystProfile) -> tuple[str, str, dict]:
    """
    Apply catalyst profile to modify trade mode, bias, and sizing.
    Returns (new_trade_mode, new_bias, modifier_details)
    """
    modifiers = {
        "catalyst_score": catalyst.catalyst_score,
        "catalyst_narrative": catalyst.narrative,
        "trade_mode_change": None,
        "bias_change": None,
        "size_multiplier": 1.0,
        "warnings": []
    }
    
    # 1. HIGH-IMPACT EVENT TODAY/TOMORROW → Reduce size / go FLAT
    if catalyst.next_24h:
        modifiers["warnings"].append(f"HIGH-impact event(s) in 24h: {[e.event for e in catalyst.next_24h]}")
        if trade_mode in ["FULL", "NORMAL"]:
            modifiers["trade_mode_change"] = "REDUCED"
            trade_mode = "REDUCED"
        elif trade_mode == "REDUCED":
            modifiers["trade_mode_change"] = "FLAT"
            trade_mode = "FLAT"
        modifiers["size_multiplier"] *= 0.5
    
    # 2. KEY RISK EVENT (CPI, NFP, FOMC) → Further reduction
    if catalyst.key_risk_events:
        next_key = min(catalyst.key_risk_events, key=lambda e: datetime.fromisoformat(e.timestamp))
        hours_until = (datetime.fromisoformat(next_key.timestamp) - datetime.now(timezone.utc)).total_seconds() / 3600
        modifiers["warnings"].append(f"KEY RISK: {next_key.event} in {hours_until:.1f}h")
        if trade_mode == "FULL":
            modifiers["trade_mode_change"] = "NORMAL"
            trade_mode = "NORMAL"
        elif trade_mode == "NORMAL":
            modifiers["trade_mode_change"] = "REDUCED"
            trade_mode = "REDUCED"
        modifiers["size_multiplier"] *= 0.7
    
    # 3. FOMC WEEK → Extra caution
    fed_this_week = [e for e in catalyst.fed_events 
                     if (datetime.fromisoformat(e.timestamp) - datetime.now(timezone.utc)).days <= 5]
    if fed_this_week:
        modifiers["warnings"].append("FOMC/Fed event this week")
        if trade_mode == "FULL":
            modifiers["trade_mode_change"] = "NORMAL"
            trade_mode = "NORMAL"
        modifiers["size_multiplier"] *= 0.8
    
    # 4. CATALYST SCORE BIAS ADJUSTMENT
    if catalyst.catalyst_score <= -3:
        # Strong risk-off catalysts
        if bias == "BULLISH":
            modifiers["bias_change"] = "NEUTRAL"
            bias = "NEUTRAL"
        elif bias == "NEUTRAL":
            modifiers["bias_change"] = "BEARISH"
            bias = "BEARISH"
        modifiers["warnings"].append(f"Catalyst score {catalyst.catalyst_score:.1f} → risk-off bias")
    elif catalyst.catalyst_score >= 3:
        # Strong risk-on catalysts (rare)
        if bias == "BEARISH":
            modifiers["bias_change"] = "NEUTRAL"
            bias = "NEUTRAL"
        elif bias == "NEUTRAL":
            modifiers["bias_change"] = "BULLISH"
            bias = "BULLISH"
        modifiers["warnings"].append(f"Catalyst score {catalyst.catalyst_score:.1f} → risk-on bias")
    
    # 5. CURRENCY-SPECIFIC HIGH IMPACT
    if catalyst.high_impact_count.get("USD", 0) >= 3:
        modifiers["warnings"].append("Heavy USD calendar this week — expect elevated volatility")
        modifiers["size_multiplier"] *= 0.8
    
    if catalyst.high_impact_count.get("EUR", 0) >= 2:
        modifiers["warnings"].append("EUR heavy calendar — EUR pairs may see gaps")
    
    if catalyst.high_impact_count.get("JPY", 0) >= 2:
        modifiers["warnings"].append("JPY calendar active — watch USDJPY, Nikkei")
    
    # Cap size multiplier
    modifiers["size_multiplier"] = max(0.25, min(1.5, modifiers["size_multiplier"]))
    
    return trade_mode, bias, modifiers


# ==================== MAIN ====================

def run_catalyst_engine() -> CatalystProfile:
    """Run the full catalyst engine and print summary."""
    print("=" * 60)
    print("CATALYST ENGINE — Economic Calendar + Fed Schedule")
    print("=" * 60)
    
    catalyst = build_catalyst_profile()
    
    print(f"\n📅 Next 24h HIGH-impact events: {len(catalyst.next_24h)}")
    for e in catalyst.next_24h:
        dt = datetime.fromisoformat(e.timestamp)
        print(f"  • {dt.strftime('%a %H:%M UTC')} | {e.currency} | {e.event}")
    
    print(f"\n📅 Next 7d HIGH-impact count by currency:")
    for curr, cnt in catalyst.high_impact_count.items():
        print(f"  {curr}: {cnt}")
    
    print(f"\n🎯 Key risk events ({len(catalyst.key_risk_events)}):")
    for e in catalyst.key_risk_events[:5]:
        dt = datetime.fromisoformat(e.timestamp)
        print(f"  • {dt.strftime('%a %b %d')} | {e.currency} | {e.event}")
    
    print(f"\n🏛️ Fed events upcoming:")
    for e in catalyst.fed_events[:3]:
        dt = datetime.fromisoformat(e.timestamp)
        print(f"  • {dt.strftime('%a %b %d')} | {e.event}")
    
    print(f"\n📊 Catalyst Score: {catalyst.catalyst_score:+.1f} / 10")
    print(f"📝 Narrative: {catalyst.narrative}")
    
    # Save to JSON
    out_path = Path(__file__).parent / "catalyst_profile.json"
    with open(out_path, "w") as f:
        json.dump(asdict(catalyst), f, indent=2, default=str)
    print(f"\n✅ Catalyst profile saved to {out_path}")
    
    return catalyst


if __name__ == "__main__":
    run_catalyst_engine()