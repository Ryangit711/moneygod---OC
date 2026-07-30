# s06 — Top-Down Analysis

## Part 1: The One Golden Principle

**Higher timeframes control lower timeframes.**

A bullish divergence on the 1-minute chart means nothing if the 1-hour chart is in a downtrend, below all MAs, and at a resistance level. The H4 chart will eat the 1-minute chart for breakfast. Every time.

Traders who don't respect this are called "retail." They found a pretty pattern on the 5-min and went long into a daily downtrend, then wonder why they got stopped out.

### The Rule of Dominance

| If Higher TF says | You on Lower TF |
|-------------------|-----------------|
| Strong uptrend | Take longs only. Shorts are swing trades at best. |
| Strong downtrend | Take shorts only. Longs are bounce scalps at best. |
| Range (no clear direction) | Trade both sides at range boundaries. No trend trades — they fail. |
| Consolidation (coil / triangle) | Wait for breakout. Do NOT anticipate. |
| Reversal pattern (double top, divergence) | Start looking for lower-TF entries in the reversal direction. Do NOT fade the trend until H4 confirms. |

---

## Part 2: The Three-Step Top-Down Process

### Step 1: Weekly (or Monthly) — The Destination

- Look at the weekly chart first. You're not looking for entries here.
- Determine one thing: **Weekly bias** — are we going up, down, or nowhere?
- Monthly chart is reference only. Use it to identify your major structural support/resistance levels.

Questions to answer:
1. Where is price relative to the weekly EMA 21?
2. Has price made a higher high / higher low sequence (uptrend), or lower high / lower low (downtrend)?
3. What is the nearest weekly support/resistance?
4. Are we in a trending week or a ranging week?

**Your weekly bias:**
- Price above weekly EMA 21 with HH/HL sequence = bullish week, look for longs
- Price below weekly EMA 21 with LH/LL sequence = bearish week, look for shorts
- Price crossing weekly EMA 21 = no clear weekly bias, trade as range until price commits

### Step 2: Daily — The Context

- Look at the daily chart next. You're looking for: **regime, structure, and key levels**.
- The daily chart gives you your trading day framework — will today be a trend day or a range day (s05)?

Questions to answer:
1. Where is price relative to the daily EMA 21 and VWAP?
2. Is there a pending liquidity sweep (below previous low / above previous high)?
3. What's the nearest HVN from s03? Am I trading at an HVN (support/resistance) or an LVN (likely to break)?
4. What's the ADX? (Trending or ranging day — s05 Part 4)

**Your daily plan:**
- Trend day (ADX > 25) → bias with the trend, no counter-trend trades
- Range day (ADX < 20) → mean reversion at daily HVN / previous day VAH/VAL
- Pending sweep → prepare for the sweep if intraday price reaches that level, then look for reversal signal

### Step 3: Intraday (4H, 1H, 15m, 5m) — The Execution

- Now you look at the charts you actually trade from.
- Intraday, you are ONLY looking for entries that align with your weekly bias and daily plan.

Questions to answer:
1. Is the intraday structure aligned with the daily bias? (If daily says up, is 1H making higher lows?)
2. Where is the nearest intraday POC/VAH/VAL (from volume profile)?
3. What session are we in? (Opening drive, lunch lull, closing auction — s05)
4. Does the setup have confluence from 2+ timeframe levels?

---

## Part 3: The TDA Framework (Timeframe Discrepancy Analysis)

### What to Do When Timeframes Conflict

| Scenario | Your Move |
|----------|-----------|
| Weekly up, Daily up, 1H up | Strong directional trend. Full-size entries in direction. |
| Weekly up, Daily up, 1H down | Normal pullback. Look for 1H reversal to enter in trend direction (best setup). |
| Weekly up, Daily down, 1H down | Daily-level correction. Wait for daily reversal to align with weekly. Do NOT trade 1H — wait. |
| Weekly down, Daily down, 1H up | Normal pullback in downtrend. Look for 1H reversal to enter short. |
| Weekly down, Daily up, 1H up | Daily-level counter-trend rally. Do NOT trade the rally — wait for daily to resume downtrend. |
| Weekly flat, Daily up, 1H up | Range within daily uptrend. Trade the 1H but expect it to revert at weekly range boundaries. |

### The Money-Generating Scenario

The best trades happen when:
- Weekly = directional
- Daily = pullback in the opposite direction from weekly
- 1H = reversal back toward weekly direction

This is the "pullback in a trend" — the most predictable, repeatable trading setup in existence. It produces a 4:1+ R:R with >60% win rate when executed correctly.

### The Avoid-At-All-Costs Scenario

Worst trades happen when:
- Weekly range (no clear direction)
- Daily range (no clear direction)
- 1H choppy (no clear direction)
- AND you take a trade anyway

This is gambling. Close the charts. Go do something else. 50% of days are this.

---

## Part 4: Practical Workflow

### Pre-Market Routine (10 min)

1. **Weekly bias** (1 min): Check weekly HTF structure
2. **Daily plan** (3 min): Check daily — ADX, key levels, pending sweeps
3. **Intraday for session** (3 min): Check 1H and 15m — session phase, within-day structure
4. **Watchlist** (2 min): Mark 2-3 scenarios you're watching for (e.g., "if price sweeps below W low then closes above daily open, go long")
5. **State check** (1 min): Are you calm, focused, ready? Run the s02 pre-trade scan.

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s05-intraday-market-structure.md` | s06's daily/weekly bias determines WHICH session regime to expect. s05 provides the intraday execution layer within that bias. | Pre-market routine; classifying the day |
| `systems/s03-volume-profile-and-order-flow.md` | The HVN/LVN levels on the daily (from s03) are the key levels in s06's Step 2. Volume confirmation in s03 validates s06's directional bias. | Identifying key daily levels; confirming bias |
| `systems/s09-journaling-and-performance-analysis.md` | Record your pre-market TDA analysis (bias, key levels) so you can compare it to what actually happened. s06's plan vs. reality is your main learning loop. | Journaling the trade day; reviewing performance |
| `systems/s02-trading-psychology.md` | When multiple timeframes conflict (s06 Part 3), frustration + forcing trades spikes. Recognizing TDA conflict preemptively prevents psychology errors. | Pre-trade state check; feeling uncertain |
| `trading/complete-strategy-orb-eurusd.md` AND `trading/mes-mnq-playbook.md` | These existing playbooks become entries within s06's TDA framework. The playbook entry conditions are intraday; s06 tells you WHEN they're valid. | Preparing playbook entries; filtering playbook by bias |
| `systems/s07-order-flow-levels.md` | The levels in s07 are derived from volume profile — s06 is where you decide which levels matter for today based on higher timeframe bias. | Building the daily plan; marking key zones |
