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

## REFERENCES

- **Tradovate demo signup:** tradovate.com → Free Trial
- **Vancouver timezone reference:** https://time.is/PT
- **Per-session risk:** `systems/position-sizing-by-flow.md` (size per trade mode)
- **Full daily OS:** `systems/3hr-daily-schedule.md`
- **Journal template:** `systems/trade-journal-template.md`
- **Sunday prep:** `systems/sunday-prep-ritual.md`
- **Morning workflow:** `systems/live-data-workflow.md`
