# WEEK 1 READINESS — Before Your First Trade

## "The demo is not practice. It's the proving ground. Treat it like live capital."

---

## 1. DEMO ACCOUNT SETUP

### Recommended: Tradovate (fastest path)

| Step | Action | Time |
|------|--------|------|
| 1 | Go to tradovate.com → Sign up for Free Trial | 2 min |
| 2 | Select "Futures" → choose Paper Trading (demo) account | 1 min |
| 3 | Fund demo with **$50,000 simulated balance** | 1 min |
| 4 | Set up chart templates (save as workspace) | 5 min |

### Chart Templates to Save

You need charts before you can see any setup. Save these as a workspace:

| Timeframe | Indicators | Purpose |
|-----------|-----------|---------|
| **5-min** | VWAP, Volume, 20 EMA, 50 EMA | Primary entry chart |
| **15-min** | VWAP, Volume, 20 EMA, 50 EMA | Confirmation / structure |
| **1H** | VWAP, 20 EMA, 50 EMA | Intraday bias frame |
| **4H** | 20 EMA, 50 EMA, 200 EMA | Medium-term trend |
| **Daily** | 20 EMA, 50 EMA, 200 EMA | Weekly bias + key levels |

Also save these drawing tools for quick access:
- **Fibonacci retracement tool** (for OTE zones in Week 4)
- **Rectangle tool** (for marking order blocks in Week 6)
- **Ray tool** (for extending key levels across the session)

### Alternative Platforms

| Platform | Setup Time | Pros | Cons |
|----------|-----------|------|------|
| **NinjaTrader** | 15 min | Better charting, free demo | Desktop-only, heavier |
| **Thinkorswim** | 10 min | Integrated with Schwab, good scanner | Futures demo needs a funded account |
| **TradingView + broker** | 5 min | Best UX, web-based | Paper trading depends on broker connection |

**Rule:** Pick one. Don't switch during the 12 weeks. The platform is infrastructure, not an edge.

---

## 2. VANCOUVER KILLZONE MAP (PT)

This is the most important gap in the syllabus. London open is 11PM PT — you're sleeping. Kill it from your expectations.

### The 3 Killzones, Mapped to PT

| Killzone | ET Time | PT Time | Tradeable? | Why |
|----------|---------|---------|------------|-----|
| **London Open** | 2:00-5:00 AM ET | 11:00 PM - 2:00 AM PT | NO | Sleep window |
| **NY AM** | 7:00-10:00 AM ET | 4:00-7:00 AM PT | YES | Best session for PT traders |
| **NY PM** | 10:00 AM - 12:00 PM ET | 7:00-9:00 AM PT | YES | Power hour + close |

### Killzone: Use These Only

| Local Time (PT) | Killzone | What Happens | Notes |
|----------------|----------|-------------|-------|
| 4:00-5:00 AM | NY Pre-market | First prints, gap fills, initial VWAP calculation | Lowest volume of the day — be patient |
| 5:00-6:00 AM | NY Open (first hour) | Highest volume. ORB forms in first 15-60 min. | THIS is where the week's patterns form most reliably |
| 6:00-7:00 AM | NY AM continuation | Trend or range established. Liquidity sweeps of ORB high/low. | Second-best hour |
| 7:00-9:00 AM | NY PM / Power Hour | MOC imbalances, position squaring. Often re-sweeps NY AM levels. | Can be trend extension or reversal |

### What This Means for the Syllabus

- **You get 2-3 hours per day max** (5-7 AM PT or 7-9 AM PT)
- **If you wake up at 4:00 AM PT:** you can trade NY AM full session (4-7 AM)
- **If you wake up at 6:30 AM PT:** you catch the tail end of NY AM and the NY PM power hour
- **London-based setups (weeks 1-4):** Your sweep will happen at NY open, not London open. Adjust your expectation accordingly.
- **Sunday prep (weekly chart):** This is for the H1/H4/D1 context, not for finding entries in your sleep window.

### Session Selection by Wake Time

| Wake Time | Available Session | What to Focus On | What to Ignore |
|-----------|-----------------|------------------|----------------|
| 4:00 AM PT | Full NY AM + PM | ORB, VWAP, all patterns | London session entirely |
| 5:30 AM PT | NY AM tail + PM | Sweeps of ORB, continuation | Pre-market moves |
| 7:00 AM PT | NY PM only | Power hour, MOC | Morning range, trend days |
| 9:00 AM PT | None | Study session only | Do not trade |

---

## 3. PER-SESSION RISK CAP (HARD RULES)

These apply EVERY session. Not negotiable.

### Hard Stops

| Rule | Detail |
|------|--------|
| **Max loss per session** | **2% of demo account** ($1,000 on $50K) — if you hit this, stop trading and close all positions |
| **Max loss per week** | **4% of demo account** ($2,000 on $50K) — if you hit this, no more trades until Monday |
| **Max consecutive loss days** | **3 days** — if you lose 3 days in a row, take 1 FULL day off. No charts, no analysis. Resume the day after. |
| **Max trades per session** | **3** — no matter how good the setups look. After 3, you're done. |
| **Min R:R per trade** | **1:1.5** — no trade below this (unless it's a scale-in on an existing winner) |

### Position Sizing (Demo, $50K)

| Trade Mode | Risk per Trade | Max Contracts MES | Daily Loss Limit |
|-----------|---------------|-------------------|------------------|
| FULL | 0.5% ($250) | 5 contracts | $1,000 |
| NORMAL | 0.33% ($165) | 3 contracts | $1,000 |
| REDUCED | 0.2% ($100) | 2 contracts | $500 |
| FLAT | 0% | 0 | Do not trade |

**MES tick value:** $1.25 per tick (0.25 point). 1 point = $5.
**MNQ tick value:** $0.50 per tick (0.25 point). 1 point = $2.

### The Session Kill Switch

If any of these happen DURING a session, flatten everything and stop:

| Trigger | Action |
|---------|--------|
| Two consecutive losses in the same session | Stop. Close everything. No revenge trade. |
| A loss greater than 2x your planned risk (slippage, gap) | Stop. Session is done. Review the setup tomorrow. |
| You break any of the hard rules above | Stop. The rule exists because you wrote it. Breaking it means you're not ready. |
| You feel emotional (anger, frustration, euphoria) and recognize it | Stop. The feeling is the signal. The trade can wait. |

---

## 4. THE FULL WEEKLY CYCLE (Updated)

With the gaps closed, the week looks like this:

```
SUNDAY EVENING (20 min) — systems/sunday-prep-ritual.md
├── Open weekly charts → mark key levels
├── Check unfilled FVGs on 4H / Daily
├── Note any plumbing events (opex, FOMC, NFP) for the coming week
└── Set the week's bias frame

TRADING DAYS (Mon/Wed/Fri or Tue/Thu)
├── 15 min: systems/live-data-workflow.md (plumbing → verdict)
├── Session: execute per concept + per-session risk cap
└── 5 min: systems/trade-journal-template.md (post-session record)

FRIDAY CLOSE (15 min) — systems/trade-journal-template.md (weekly review)
├── Concept performance this week
├── Edge × concept cross-tracking
├── Discipline score
├── Advance or repeat?
└── Aha insights captured
```

---

## 5. THE 4-WEEK BRIDGE — Demo → Prop Firm Eval

**This is the gap most traders ignore.** Demo execution is not the same as prop firm execution. The fills are different, the spreads are different, the psychology is different. Walk this stairway before you buy your first eval.

### The Paper-to-Live Execution Gap (Quick Summary)

| What Demo Gives You | What Prop Firm Gives You |
|---------------------|-------------------------|
| Zero slippage | 1-10 ticks slippage on volatility |
| Fixed tight spreads | Variable spreads (widen at rollover, news) |
| No commissions | $3-$7/lot or $0.62/contract |
| Instant fills | 5-200ms latency |
| Stop at exact price | Stop becomes market order → fill at available price |

**Full breakdown:** `trading/paper-vs-live-gap.md`

### Week 1: Realistic Demo

Trade your retail demo, but manually subtract realistic costs:

| Day | Activity | Purpose |
|-----|----------|---------|
| 1-2 | Trade demo, mentally subtract 1 pip from every win | Simulates slippage |
| 3-4 | Trade demo, use limit entries only (never market) | Learn queue behavior |
| 5-7 | Trade demo, subtract $5 from every winning trade | Factor in commissions |

### Week 2: Prop Firm's Own Demo

| Day | Activity | Purpose |
|-----|----------|---------|
| 1 | Sign up for FTMO free 14-day demo OR Goat Funded free demo | Get on their actual price feed |
| 2-3 | Trade 1-2 sessions. Compare fills to TradingView. | Identify their execution quality |
| 4-7 | Full sessions on their demo. Journal every fill. | Build your slippage profile |

### Week 3: Eval Rehearsal

| Day | Activity | Purpose |
|-----|----------|---------|
| 1-3 | Same demo, but treat it like live: 0.25% risk max, 1 trade/day | Build eval-mode discipline |
| 4-5 | Only A+ setups. Flat if no A+. | Prove you can wait |
| 6-7 | Full pre-session ritual + 1 trade + journal | Rehearse the exact eval routine |

### Week 4: Pre-Eval Checklist

```
- [ ] 30+ demo trades on prop firm's own feed (not retail demo)
- [ ] Average slippage documented per instrument
- [ ] Execution cost calculated (spread + slippage + commission)
- [ ] Win rate after execution costs is still positive
- [ ] R:R maintained at 1:1.5 minimum after costs
- [ ] Pre-session ritual is habitual (not something you think about)
- [ ] Journal entries for every trade
- [ ] Max 2 consecutive losses in any 5-trade stretch
- [ ] No overtrading: 1-2 trades/day for 5+ consecutive days
```

**All boxes checked → you're ready to buy your first eval.**

### Which Platform to Practice On (By Firm)

| If Your First Eval Is... | Practice On... | Why |
|--------------------------|---------------|-----|
| FTMO (FX) | MT5 demo from FTMO's site | Same platform, same feed |
| Funding Pips (FX) | MT5 demo from their site | Same platform, same feed |
| Goat Funded (FX/CFD) | MT5 demo from their site | Same platform, same feed |
| MyFundedFutures (futures) | Tradovate paper trading | Same platform, same feed |
| Apex (futures) | Tradovate or NinjaTrader paper | Same platform, same feed |
| TradeDay (futures) | Tradovate paper trading | Same platform, same feed |

**Rule:** Never practice on a retail demo and then buy an eval. Practice on THE FIRM'S OWN DEMO FIRST. The feeds are different. The fills are different. The experience must match.

---

## 6. PROP FIRM ARCHITECTURE — Quick Reference

**Full details:** `trading/prop-firm-architecture.md`

### Forex/CFD Firms (MT4/MT5/cTrader)
- FTMO — Gold standard, $79 entry, 14-day free demo
- Funding Pips — Best value, $29 entry, weekly payouts
- The5ers — Best scaling, up to $4M, milestone-based
- FundedNext — Best multi-strategy, up to $4M, 24h payouts

### Futures Firms (NinjaTrader/Tradovate/Rithmic)
- MyFundedFutures — Highest trust (4.9★), EOD drawdown, $54.50
- Apex — Cheapest ($19.90), 100% split first $25K, trailing DD
- TradeDay — Commission-free, $43.50, EOD drawdown
- Tradeify — Simple 1-step, $42.25, 90% split

### Multi-Asset (FX + Futures)
- FXIFY — #1 for Canada, MT5 + FFX, $59, Canadian privacy policy

### Paper vs Live Gap
- Full execution gap analysis: `trading/paper-vs-live-gap.md`
- 6 execution gaps, cost math, 4-week bridge protocol

### Multi-Account Gateway
- Managing multiple prop accounts: `trading/multi-account-gateway.md`
- 4-layer architecture, risk rules, scaling path

---

## REFERENCES

- **Paper vs live gap:** `trading/paper-vs-live-gap.md` — execution differences, cost math, bridging protocol
- **Prop firm architecture:** `trading/prop-firm-architecture.md` — every firm categorized by market
- **Prop firm specs:** `trading/prop-firm-playbook.md` — detailed comparison with promo codes
- **Multi-account gateway:** `trading/multi-account-gateway.md` — managing multiple funded accounts
- **Tradovate demo signup:** tradovate.com → Free Trial
- **FTMO free demo:** ftmo.com → Free Trial (14 days)
- **Vancouver timezone reference:** https://time.is/PT
- **Per-session risk:** `systems/position-sizing-by-flow.md` (size per trade mode)
- **Full daily OS:** `systems/3hr-daily-schedule.md`
- **Journal template:** `systems/trade-journal-template.md`
- **Sunday prep:** `systems/sunday-prep-ritual.md`
- **Morning workflow:** `systems/live-data-workflow.md`
