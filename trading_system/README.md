# Trading System - Complete Setup & Operation Guide

## Overview

This is a **fully automated macro-driven trading system** that:
1. **Fetches real macro data** (Fed balance sheet, TGA, RRP, SOFR, VIX, DXY) from free APIs
2. **Computes Net Liquidity** = ΔFedBS - ΔTGA - ΔRRP
3. **Scans economic calendar** for high-impact events (CPI, NFP, FOMC, etc.)
4. **Scores catalysts** and adjusts trade mode/bias/size
5. **Runs decision trees** to determine: Trade? Bias? Instrument? Size?
6. **Executes trades** via MT5 (paper/live) or Tradovate (futures)
7. **Logs everything** to CSV journal + Telegram alerts

All using **FREE data sources** - no paid subscriptions needed.

---

## Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Data Feeds     │────▶│  Plumbing        │────▶│  Catalyst Engine │
│  (FRED, AV,     │     │  Pipeline        │     │  (Calendar +     │
│   Finnhub,      │     │  (Liquidity +    │     │   Scoring)       │
│   Yahoo, etc.)  │     │   Decision)      │     └────────┬─────────┘
└─────────────────┘     └────────┬─────────┘              │
                                 │                       │
                                 ▼                       ▼
                        ┌──────────────────┐     ┌──────────────────┐
                        │  Orchestrator    │◀────│  Apply Modifiers │
                        │  (Chains Steps)  │     │  (Mode/Bias/Size)│
                        └────────┬─────────┘     └──────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
       ┌─────────────┐   ┌─────────────┐    ┌─────────────┐
       │  MT5 Bot    │   │  Tradovate  │    │  Journal    │
       │  (FX/Crypto)│   │  (Futures)  │    │  (CSV + TG) │
       └─────────────┘   └─────────────┘    └─────────────┘
```

---

## Quick Start

### 1. Prerequisites
- Linux (Debian/Ubuntu) or WSL2
- Python 3.11+
- MetaTrader 5 terminal (for live FX/crypto) OR Tradovate account (for futures)

### 2. Setup (run once)

```bash
cd /home/aryan/trading_system

# Create virtual environment
python3 -m venv trading_venv
source trading_venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your API keys to config.json (or use environment variables)
# Required: FRED_API_KEY (already set)
# Optional: ALPHAVANTAGE_KEY, FINNHUB_KEY, TWELVE_DATA_KEY

# Install cron jobs
chmod +x setup_cron.sh
./setup_cron.sh
```

### 3. Test Run (manual)

```bash
# Quick plumbing check only
python run_pilot.py --mode=quick

# Full pipeline (demo mode - no real trades)
python run_pilot.py --mode=full --retries=1

# Full pipeline (background mode for cron)
python run_pilot.py --mode=background
```

### 4. Switch to Live Trading

Edit `config.json`:
```json
{
  "mode": "live",  // Change from "paper" to "live"
  "accounts": {
    "fx": {
      "enabled": true,
      "bot": "mt5_bot.py",
      "symbol": "BTCUSD"
    }
  }
}
```

Add MT5 credentials to `~/.mt5_credentials` (or environment variables).

---

## Free Data Sources Used

| Source | What It Provides | Free Tier Limits |
|--------|------------------|------------------|
| **FRED** | Fed BS, TGA, RRP, SOFR, macro series | Unlimited (with key) |
| **Alpha Vantage** | CPI, GDP, Unemployment, Retail Sales | 25 req/day |
| **Finnhub** | Economic calendar, real-time quotes | 60 req/min |
| **Twelve Data** | Price history for any symbol | 800 req/day |
| **Yahoo Finance (yfinance)** | Price data, futures, crypto | No limit (unofficial) |
| **Forex Factory** | Economic calendar (HTML scrape) | No limit |

---

## Daily Schedule (Automated via Cron)

| Time (PT) | Job | Purpose |
|-----------|-----|---------|
| **05:30** | Full Pipeline | Main daily run: plumbing → catalyst → execution → journal |
| **06:00-13:00** (every 30 min) | Quick Check | Monitor liquidity regime changes during market hours |
| **Sunday 02:00** | Cleanup | Remove logs older than 7 days |

---

## Key Files

| File | Purpose |
|------|---------|
| `run_pilot.py` | **Main entry point** - robust runner with retries, logging, state |
| `orchestrator.py` | Chains plumbing → catalyst → execution → journal |
| `plumbing_fetcher.py` | Fetches macro data, computes liquidity, runs decision trees |
| `catalyst_engine.py` | Fetches calendar, scores events, adjusts mode/bias/size |
| `data_feeds.py` | **Unified API layer** for all free data sources |
| `mt5_bot_enhanced.py` | MT5 execution bot (paper/live) |
| `config.json` | All settings (mode, risk, accounts, API keys, schedule) |
| `setup_cron.sh` | Installs automated cron jobs |
| `cleanup_logs.py` | Weekly log rotation |

---

## Output Files (Generated Daily)

| File | Description |
|------|-------------|
| `plumbing_verdict.json` | Complete verdict with all raw data, liquidity, signals, decisions |
| `catalyst_profile.json` | Calendar events, catalyst score, narrative |
| `trade_journal.csv` | One row per day: mode, instrument, bias, edges, PnL |
| `verdict_YYYYMMDD.txt` | Human-readable daily summary |
| `logs/pilot_YYYYMMDD.log` | Detailed execution log |
| `pilot_state.json` | Persistent state (run count, failures, last success) |

---

## Telegram Alerts

Set in `config.json`:
```json
{
  "notifications": {
    "telegram_enabled": true,
    "telegram_token": "YOUR_BOT_TOKEN",
    "telegram_chat_id": "6766010191"
  }
}
```

You'll receive:
- **05:30 AM**: Daily verdict (mode, bias, instrument, size, catalyst narrative, session plan)
- **Regime change alerts**: If quick check detects liquidity shift

---

## Trade Modes Explained

| Mode | When | Max Contracts | Risk/Trade | Daily Max |
|------|------|---------------|------------|-----------|
| **FULL** | Net Liq > +50B, VIX low, no catalysts | 3 | 1.5% | 3.0% |
| **NORMAL** | Net Liq +10 to +50B, or INJECT + normal VIX | 2 | 1.0% | 2.0% |
| **REDUCED** | Net Liq -10 to -50B, or catalysts present | 1 | 0.25% | 0.75% |
| **FLAT** | Net Liq < -50B, VIX panic, SOFR stress | 0 | 0% | 0% |

**Catalyst modifiers** (applied automatically):
- High-impact event in 24h → halve size, step down mode
- Key risk (CPI/NFP/FOMC) → further reduce
- Fed meeting this week → extra caution
- Heavy USD calendar → reduce size 20%

---

## Decision Trees (The Logic)

1. **Tree 1 - Should I trade?**
   - VIX > 25 → FLAT
   - Net Liquidity < -$50B → FLAT
   - SOFR > IORB + 5bp → FLAT (repo stress)
   - Else → PROCEED

2. **Tree 2 - Bias?**
   - INJECT + DXY down + VIX low → BULLISH
   - DRAIN + DXY up + VIX elevated → BEARISH
   - Else → NEUTRAL

3. **Tree 3 - Instrument?**
   - FULL + BULLISH → BOTH (MES + MNQ)
   - FULL/NORMAL/REDUCED → MES
   - FLAT → NONE

4. **Tree 4 - Size?**
   - FULL: 1.5%/trade, 3% daily, 3 contracts
   - NORMAL: 1.0%/trade, 2% daily, 2 contracts
   - REDUCED: 0.25%/trade, 0.75% daily, 1 contract
   - FLAT: 0

---

## Monitoring & Debugging

### View logs
```bash
# Today's full run log
tail -f logs/cron_full.log

# Pilot runner log
tail -f logs/pilot_$(date +%Y%m%d).log

# Quick check logs
tail -f logs/cron_quick.log
```

### Check state
```bash
cat pilot_state.json
```

### Manual override (force FLAT for a day)
```bash
python -c "
import json
with open('config.json') as f: c = json.load(f)
c['mode'] = 'paper'  # Forces paper mode
with open('config.json', 'w') as f: json.dump(c, f, indent=2)
print('Set to paper mode')
"
```

### Force re-run today
```bash
python run_pilot.py --mode=full --retries=3
```

---

## Adding More Data Sources

Edit `data_feeds.py` - add new functions following the same pattern:
```python
def new_source_get_data() -> Dict:
    # Your API call here
    return {"key": value}
```

Then call it from `fetch_all_plumbing_raw()` or `plumbing_fetcher.py`.

---

## Risk Controls (Built-in)

1. **Daily loss limit** - Stops all trading if daily PnL < -3% (configurable)
2. **Max accounts in drawdown** - Circuit breaker if 2+ accounts losing
3. **Consecutive failure alert** - Telegram alert after 3 failed runs
4. **Catalyst overrides** - Automatically reduces size before major events
5. **Paper mode default** - Safe by default, explicit switch to live

---

## Next Steps (When Ready to Scale)

1. **Add paid data** - Bloomberg, Refinitiv, Koyfin for cleaner macro
2. **Intraday pipeline** - Run plumbing every 30 min, execute on signals
3. **ML catalyst scoring** - Train on historical event reactions
4. **Portfolio optimization** - Multi-asset, correlation-based sizing
5. **Tradovate integration** - Enable futures account
6. **Web dashboard** - Flask/FastAPI + React for real-time monitoring

---

## Support

- **Logs**: `logs/` directory
- **State**: `pilot_state.json`
- **Config**: `config.json`
- **Telegram**: Daily alerts at 05:30 AM PT

The system is designed to **run unattended** and **fail safely**. If anything breaks, it logs the error, retries 3x, alerts you, and stays in paper mode.

Good luck! 🚀