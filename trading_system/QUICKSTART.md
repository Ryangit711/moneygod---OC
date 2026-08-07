# TRADING SYSTEM — QUICK START GUIDE

## What This Is
A **self-sustaining automated trading system** built from your existing repos:
- **moneygod---OC** → Decision framework (plumbing → bridge → trade)
- **mt5_bot.py** → Execution engine (FX)
- **DeepTutor** → Research/backtest/visualization
- **ABHIMANYU-2.0** → Skill-based orchestration model

---

## Directory Structure
```
/home/aryan/trading_system/
├── plumbing_fetcher.py       # 5 URLs → 6 numbers → Net Liquidity verdict
├── orchestrator.py           # Chains: fetch → decide → execute → journal
├── mt5_bot_enhanced.py       # MT5 bot accepting trade_mode/bias from orchestrator
├── config.json               # All settings (mode, accounts, risk, schedule)
├── requirements.txt          # Python dependencies
├── setup_cron.sh             # Install daily cron jobs
├── plumbing_verdict.json     # Daily verdict (machine-readable)
├── trade_journal.csv         # Combined journal (multi-account format)
└── logs/                     # Cron job logs
```

---

## The Daily Pipeline (Automated via Cron)

| Time (PT) | Step | Script | Output |
|-----------|------|--------|--------|
| **05:30** | Plumbing Check | `orchestrator.py --step plumbing` | `plumbing_verdict.json` |
| **06:30-09:00** | Execution | `orchestrator.py --step execute` | Trades via MT5/Tradovate |
| **09:05** | Journal Close | `orchestrator.py --step journal` | `trade_journal.csv` entry |
| **Mon 04:30** | Weekly Deep Dive | `weekly_deep_dive.py` | Regime updates |

---

## Quick Test (Manual Run)

```bash
cd /home/aryan/trading_system

# 1. Test plumbing pipeline (shows full 15-min workflow)
python3 plumbing_fetcher.py

# 2. Test full orchestrator (demo mode - no real trades)
python3 orchestrator.py --step full --demo

# 3. Check outputs
cat plumbing_verdict.json
cat trade_journal.csv
```

---

## Configuration

Edit `config.json`:
```json
{
  "mode": "paper",           // "paper" or "live"
  "accounts": {
    "fx": {"enabled": true, "symbol": "BTCUSD"},
    "futures": {"enabled": false, "symbol": "MES"}
  },
  "notifications": {
    "telegram_enabled": false,
    "telegram_token": "YOUR_BOT_TOKEN",
    "telegram_chat_id": "YOUR_CHAT_ID"
  }
}
```

**For live trading:**
1. Set `"mode": "live"` and `"dry_run": false` in mt5_bot_enhanced.py config
2. Add Telegram credentials for alerts
3. Ensure MT5 terminal is running with your broker credentials

---

## Install Cron Jobs (Automation)

```bash
cd /home/aryan/trading_system
chmod +x setup_cron.sh
./setup_cron.sh
```

This installs:
- Daily plumbing check at 05:30 AM (Mon-Fri)
- Daily execution at 06:30 AM (Mon-Fri)
- Daily journal close at 09:05 AM (Mon-Fri)
- Weekly deep dive Monday 04:30 AM

---

## What Each Component Does

### plumbing_fetcher.py
Implements **live-data-workflow.md** (Min 1-15):
- Fetches 5 data sources (FRED, NY Fed, TradingView, Forex Factory)
- Computes **Net Liquidity = ΔFedBS - ΔTGA - ΔRRP**
- Runs **4 Decision Trees** from plumbing-to-trade-bridge.md
- Outputs: Trade Mode (FULL/NORMAL/REDUCED/FLAT), Instrument, Bias, Size, Session Plan

### orchestrator.py
Chains the pipeline:
1. Runs plumbing check
2. Checks circuit breakers (multi-account-gateway.md rules)
3. Executes bots with verdict parameters
4. Updates combined journal

### mt5_bot_enhanced.py
Your existing MT5 bot **modified to accept orchestrator parameters**:
- `--trade-mode` → adjusts risk_pct (FULL=1.5%, NORMAL=1.0%, REDUCED=0.25%, FLAT=0%)
- `--bias` → filters setups (BULLISH=longs only, BEARISH=shorts only, NEUTRAL=both)
- `--max-contracts` → caps position size
- Respects execution window (06:30-09:00 PT)
- Enforces max 2 trades/session

---

## Missing Pieces (To Complete the System)

| Component | Status | Effort |
|-----------|--------|--------|
| **Real data APIs** | Mock data in fetcher | Low (add FRED key, Twelve Data, etc.) |
| **Tradovate bot** | Not built | Medium (mirror mt5_bot_enhanced.py) |
| **Strategy signals** | Basic RSI/MACD/SMA | Medium (code ORB, VWAP, Gap plays) |
| **Weekly deep dive** | Not built | Low (COT, auctions, balance sheets) |
| **Backtest framework** | Use DeepTutor | Low (deep_research + visualize) |

---

## Study Path (From Your Repos)

Start with these files in **moneygod---OC** (in order):

1. **README.md** → System overview
2. **ASSIMILATION_PROTOCOL.md** → How to learn the system
3. **CURRICULUM.md** → 6-phase learning path
4. **systems/live-data-workflow.md** → The 15-min daily routine (what plumbing_fetcher.py automates)
5. **systems/plumbing-to-trade-bridge.md** → 4 Decision Trees (what orchestrator.py runs)
6. **trading/mes-mnq-playbook.md** → MES/MNQ execution plays
7. **trading/complete-strategy-orb-eurusd.md** → ORB FX strategy
8. **trading/multi-account-gateway.md** → Scaling path & circuit breakers
9. **systems/position-sizing-by-flow.md** → Risk sizing by regime
10. **plumbing-hierarchy-master.md** → Master reference (12 parts, 3,342 lines)

---

## Next Steps for You

1. **Study the source docs** (moneygod---OC) — understand the *why* behind each decision
2. **Get a FRED API key** (free) → add to config.json → real plumbing data
3. **Paper trade for 2 weeks** — verify the pipeline works end-to-end
4. **Build tradovate_bot.py** — mirror mt5_bot_enhanced.py for futures
5. **Code the playbook strategies** — ORB, VWAP Reversion, Gap Play as Python signals
6. **Add backtest validation** — use DeepTutor's `deep_research` + `visualize` capabilities

---

## Files Created Today

| File | Purpose |
|------|---------|
| `plumbing_fetcher.py` | Complete Min 1-15 workflow automation |
| `orchestrator.py` | Daily pipeline orchestration |
| `mt5_bot_enhanced.py` | MT5 bot accepting plumbing verdict params |
| `config.json` | Central configuration |
| `setup_cron.sh` | Automation installer |
| `requirements.txt` | Dependencies |

Run `python3 plumbing_fetcher.py` anytime to see today's verdict.