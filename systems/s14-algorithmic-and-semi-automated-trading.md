# s14 — Algorithmic and Semi-Automated Trading

Code is a force multiplier for a discretionary trader. Use it to sharpen your edge, not replace your judgment.

---

## Part 1: Why Code (for a Discretionary Trader)

Automation is not about letting a robot trade for you. A black-box bot is a fast way to blow up. The purpose of code is narrower:

- **Backtesting setups faster** — run 500 historical simulations in 2 seconds instead of flipping charts (cross-ref s04)
- **Scanning across pairs** — monitor 28 FX + 6 futures for your conditions and only look at charts that trigger
- **Alerting when conditions align** — Telegram push when your confluence appears, no screen-staring
- **Journaling automatically** — broker CSV → Python → metrics dashboard, no manual entry (cross-ref s09)
- **Eliminating entry hesitation** — execution script enters faster and more precisely than you can click

**What NOT to automate:** your judgment. You assess context — volume confirmation, upcoming news, market structure feel. Code handles the mechanical layer. You handle the discretionary layer.

---

## Part 2: Semi-Automation Frameworks

Semi-automated = code alerts you + you decide. This is the sweet spot.

```
Market Data → Scanner Script → Alert → You Review → Manual Entry (or 1-Click API)
```

### Example Workflow

1. Python script runs every 5 minutes via cron, scanning 28 FX pairs for an ORB breakout on the 5M chart
2. It sends a Telegram message:
   ```
   EUR/USD ORB | Breakout at 1.1045 | Stop: 1.1030 (15 ticks) | Target: 1.1085 (40 ticks) | R:R = 2.67
   ```
3. You open the chart, check volume profile, check economic calendar, confirm the level
4. If it passes your judgment, click to send the pre-filled order

### What to Semi-Automate First

| Task | Priority | Effort |
|------|----------|--------|
| Trade journal auto-parser | P0 | 1 hour |
| Daily session timer + alerts | P1 | 30 min |
| Multi-pair Pine scanner | P1 | 2 hours |
| R:R calculator CLI | P2 | 15 min |
| Weekly performance report | P2 | 2 hours |

---

## Part 3: Pine Script (TradingView)

Pine Script runs in-browser on TradingView. Zero setup, instant results. Fastest path from idea → working script.

### What Pine Is Good For

Custom indicators, alerts, simple backtesting (`strategy()` framework), multi-instrument scanning (Pine Scanner), multi-timeframe analysis via `request.security()`

### What Pine Is NOT Good For

Complex logic (no classes, 500-line limit), large data processing (max ~20K bars), external API calls, real automation (can't place live orders outside TradingView paper trading), precision backtesting (basic slippage/fill models)

### Pine Template: Multi-Timeframe Scanner with Alerts

```pinescript
//@version=5
indicator("S14 Scanner", overlay=true)

htf = input.timeframe("D", "Higher TF")
lb = input.int(10, "Pivot Lookback")

dHigh = request.security(syminfo.tickerid, htf, ta.pivothigh(high, lb, lb))
dLow  = request.security(syminfo.tickerid, htf, ta.pivotlow(low, lb, lb))
atRes = dHigh != 0 and math.abs(high - dHigh) / dHigh < 0.002
atSup = dLow  != 0 and math.abs(low - dLow)  / dLow  < 0.002
volUp = volume > ta.sma(volume, 20) * 1.5

plotshape(atRes and volUp, style=shape.triangledown, location=location.abovebar, color=color.red, size=size.small)
plotshape(atSup and volUp, style=shape.triangleup, location=location.belowbar, color=color.green, size=size.small)

alertcondition(atRes and volUp, "Resistance Vol", "{{ticker}} at resistance + vol spike @ {{close}}")
alertcondition(atSup and volUp, "Support Vol", "{{ticker}} at support + vol spike @ {{close}}")
```

### Key Pine Patterns

| Pattern | Code |
|---------|------|
| Pull HTF data | `request.security(syminfo.tickerid, "D", close)` |
| Pivot high/low | `ta.pivothigh(high, 10, 10)` |
| Volume spike | `volume > ta.sma(volume, 20) * 1.5` |
| ATR for stops | `ta.atr(14)` |
| Alert on condition | `alertcondition(cond, title, msg)` |

---

## Part 4: Python (For Serious Work)

Python does everything Pine can't: file I/O, API calls, complex math, scheduling, running 24/7.

### What Python Is Good For

Custom backtesting (vectorbt, backtrader, or custom loops), trade journal analysis (pandas), Telegram/Discord alert bots, scheduled multi-pair scanning, risk monitoring, Kelly and position sizing calculations

### What Python Is NOT Good For

Low-latency execution (10-100ms+ due to GIL). Python should not be your order router. For a manual trader this is irrelevant — your reaction time dominates. Only use Python for analysis and alerts, not bot execution.

### Starter Script: Trade Journal Analyzer

```python
"""
s14 journal.py — Run weekly: python journal.py trades.csv
"""
import pandas as pd, numpy as np, sys, json

df = pd.read_csv(sys.argv[1])
df['R'] = df['pnl'] / df['risk']

wins = df[df['R'] > 0]
losses = df[df['R'] <= 0]
wr = len(wins) / len(df)
aw = wins['R'].mean() if len(wins) else 0
al = losses['R'].mean() if len(losses) else 0
pf = abs(wins['pnl'].sum() / losses['pnl'].sum()) if len(losses) and losses['pnl'].sum() != 0 else float('inf')
cum, rm = df['pnl'].cumsum(), df['pnl'].cumsum().cummax()
mdd = (cum - rm).min()
b = abs(aw / al) if al != 0 else 0
kelly = (wr * b - (1 - wr)) / b if b and wr * b - (1 - wr) > 0 else 0

print(json.dumps({
    'trades': len(df), 'win_rate': f'{wr:.2%}',
    'avg_r': f'{df["R"].mean():.2f}', 'profit_factor': f'{pf:.2f}',
    'max_dd': f'${mdd:.2f}', 'kelly': f'{kelly:.2%}',
    'total_pnl': f'${df["pnl"].sum():.2f}'
}, indent=2))
```

### Project Structure Template

```
trading-tools/
├── journal/journal.py        # Trade analysis
├── scanner/scanner.py        # Multi-pair scanner
├── scanner/config.yaml       # Pairs, TFs, conditions
├── alerts/telegram_bot.py    # Alert dispatcher
├── utils/rr_calculator.py    # R:R calculator
└── utils/position_sizer.py   # Size by risk %
```

---

## Part 5: Broker APIs

Do NOT touch APIs until 6+ months of consistent manual profitability. Start with read-only access, progress to execution.

### Tradovate API (Futures — Primary)

REST + WebSocket. OAuth 2.0. Place/cancel orders, get quotes, manage positions. Official Python SDK. 20 req/s REST limit. Best path for futures semi-automation.

### MetaTrader MQL (FX)

MQL4/MQL5 — proprietary C-like language. Massive ecosystem of EAs and indicators. Requires VPS for 24/7. Old architecture (MQL4 from 2005). Only use if you're committed to full FX automation.

### cTrader cAlgo (FX — Modern)

C#-based with proper debugger and .NET ecosystem. REST API available. Better than MT5 for everything. If you automate FX, use cTrader.

### API Progression

| Phase | Timeline | What You Do |
|-------|----------|-------------|
| 0 | Month 0-6 | Manual trading only. Export CSV from broker. |
| 1 | Month 6-8 | Tradovate REST — read account, pull trade history, auto-journal |
| 2 | Month 8-10 | Tradovate WebSocket — real-time alerts when conditions hit |
| 3 | Month 10-12 | Tradovate order entry — 1-click from script (manual confirm) |
| 4 | Month 12+ | Full semi-auto: scanner → alert → you review → script sends |

---

## Part 6: The Key Code Snippets (Reference Section)

### Snippet #1: R:R Calculator CLI

```python
import argparse
p = argparse.ArgumentParser()
for arg in ['--entry', '--stop', '--target']:
    p.add_argument(arg, type=float, required=True)
args = p.parse_args()
risk, rwd = abs(args.entry - args.stop), abs(args.target - args.entry)
print(f"R:R = 1:{rwd/risk:.2f} | Risk: {risk} | Reward: {rwd}")
```

### Snippet #2: Position Sizer

```python
def size_futures(balance, risk_pct, stop_ticks, tick_value):
    return max(int(balance * risk_pct / (stop_ticks * tick_value)), 1)

def size_fx(balance, risk_pct, stop_pips, pip_per_lot):
    return round(balance * risk_pct / (stop_pips * pip_per_lot) * 100) / 100

print(f"MES: {size_futures(10000, 0.01, 20, 1.25)} contracts")
print(f"EUR/USD: {size_fx(10000, 0.01, 15, 10.0)} lots")
```

### Snippet #3: Session Timer

```python
from datetime import datetime, time
import pytz
et, now = pytz.timezone('US/Eastern'), datetime.now(pytz.timezone('US/Eastern'))
sessions = [('Asia/London', time(0,0), time(9,0)), ('London', time(3,0), time(12,0)),
            ('Overlap', time(8,0), time(12,0)), ('NY', time(8,0), time(17,0))]
for name, s, e in sessions:
    if s <= now.time() <= e:
        rem = (datetime.combine(now.date(), e, et) - now).seconds // 60
        print(f"{name} ({rem} min left)")
        break
else:
    print("No major session active — check volume")
```

### Snippet #4: Inline Trade Journal

```python
import pandas as pd, sys
df = pd.read_csv(sys.argv[1]); df['R'] = df['pnl']/df['risk']
w = df[df['R']>0]; l = df[df['R']<=0]
print(f"{len(df)} trades | WR: {len(w)/len(df):.2%} | Avg R: {df['R'].mean():.2f} | "
      f"PF: {abs(w['pnl'].sum()/l['pnl'].sum()):.2f} | PnL: ${df['pnl'].sum():.2f}")
```

### Snippet #5: Calendar Filter (Scraper Skeleton)

```python
import requests
from bs4 import BeautifulSoup
# FXStreet calendar — parse table rows, filter importance=high
# Placeholder: check forexfactory.com or use their API
print("High-impact events: see forexfactory.com or fxstreet.com/calendar")
```

---

## Part 7: Quick Start — Your First Automation

### Step 1: Setup

```bash
pip install pandas numpy requests pytz
mkdir -p ~/trading-tools/{journal,scanner,alerts,utils}
```

### Step 2: Export trades from Tradovate (`Reports → Trade Reports → Export CSV`), save to `~/trading-tools/journal/trades.csv`

### Step 3: Run analysis

```bash
cd ~/trading-tools/journal && python journal.py trades.csv
# → { "trades": 45, "win_rate": "57.78%", "avg_r": "0.68R", ... }
```

### Step 4: Run weekly (cross-ref sunday-prep-ritual.md). Compare win rate, avg R, max DD against prior weeks.

### Step 5: Monthly expansion

| Month | Script | Purpose |
|-------|--------|---------|
| 1 | `journal.py` | Auto-analyze trades |
| 2 | `session_timer.py` | Active session + time remaining |
| 3 | Pine scanner | Scan 28 pairs → TradingView alert |
| 4 | `telegram_bot.py` | Forward Pine alerts to phone |
| 5 | `rr_calculator.py` | CLI R:R check before entry |
| 6 | Tradovate API read | Auto-pull history (no CSV export) |

**Do not build a trading bot in month 1.** Start with analysis automation. Move to execution only after 6+ months of verified edge.

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `s04-backtesting-and-system-development.md` | Pine + Python execute s04's methodology — backtest a defined system with code instead of flipping charts | Writing a backtest script or validating a system from s04 |
| `s09-journaling-and-performance-analysis.md` | Python journal automator computes s09's template metrics — replaces manual spreadsheet entry | Running `journal.py` for weekly review instead of filling forms by hand |
| `s10-execution-and-trade-management.md` | Semi-automated execution (Part 5) and broker APIs (Part 2) implement s10's order management rules via code | Designing API-based 1-click entry that respects s10's entry/exit rules |
| `s01-mathematics.md` | Every snippet computes math from s01 — pip value, R:R, Kelly %, position sizing | Implementing any s01 formula in Python/Pine |
| `s07-order-flow-levels.md` | Automated level detection (POC, HVN scan across timeframes) integrates s07 with Pine's multi-TF capability | Writing a Pine script that draws s07 levels automatically |
| `quickstart/02-platform-setup.md` | Broker API access requires account setup — Tradovate credentials, Rithmic connection, data subscriptions | Generating API keys or configuring Tradovate access |
| `08-forex-trading-the-purest-flow.md` | MT5/cTrader are FX automation platforms; MQL4/MQL5 and cAlgo in Part 5 are the FX execution options | Choosing between MT5/cTrader for FX automation |
| `09-futures-trading-energy-and-receipts.md` | Tradovate API (Part 5) is the futures automation path — directionally consistent with /ES, /NQ, /CL via code | Writing Python to trade futures via Tradovate API |
