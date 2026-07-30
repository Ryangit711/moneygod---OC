# s05 — Intraday Market Structure

## Part 1: The Session Architecture

Every trading day has a consistent macro structure that repeats. Understanding this is your first edge — knowing where you are in the day tells you what kind of price action to expect.

### The Three-Session Framework (FX)

| Session | GMT (Winter) | EST | Character |
|---------|-------------|-----|-----------|
| **Asia/Tokyo** | 00:00–09:00 | 7pm–4am | Low volatility, range-bound, no major news, manipulative moves stick |
| **London** | 07:00–16:00 | 2am–11am | High volatility, most FX volume, trend begins here, liquidity hunts into NY open |
| **New York** | 13:00–22:00 | 8am–4pm | 2nd highest volume, news-driven, often continuation/reversal of London trend |

**The overlap zones** (London–NY overlap, 8am–11am EST) = highest volatility, widest spreads, fastest moves. Most retail blow-ups happen here.

### The Four-Session Framework (Futures)

For /ES and /NQ, the session structure maps differently:

| Session | EST | Character |
|---------|-----|-----------|
| **Overnight** | 6pm–9:30am | Lower volume, gap risk, algorithmic, often one-directional |
| **Opening Drive** | 9:30–10:00am | Highest volume of the day, most volatility, OPEX-level activity |
| **Midday Lull** | 10:00am–2:00pm | Slower, range-bound, mean reversion common |
| **Closing Auction** | 2:00–4:00pm | Volume picks up, market positioning for next day, institutional flows |

**The opening range** (first 15–30 min) defines the high and low for most of the day. ~65% of all daily ranges establish within the first 30 minutes (statistically, this holds across many years of ES data).

---

## Part 2: Daily Structure Patterns

### The Opening Drive (9:30–10:00 EST)

Two common templates:

| Template | Description | Frequency |
|----------|-------------|-----------|
| **Trend Day** | Price opens, finds liquidity, then trends in one direction all day. No significant pullback beyond the opening balance. | ~20% of days |
| **Range Day** | Price opens, establishes a range, oscillates within it. The rest of the day is a series of failed breakouts. | ~50% of days |
| **Reversal Day** | Price opens in one direction, fails at a key level, reverses across the opening range and trends opposite. | ~20% of days |
| **Inside Day** | Price stays within previous day's range. Low volatility, usually before a major event. | ~10% of days |

**How to use this:** By 10:15 AM EST, you can classify the day. If it's a range day, stop trying to trend-trade. If it's a trend day, stop trying to fade the edges.

### The Lunch Lull (10:00–14:00 EST)

Volume drops ~60% from opening drive levels. Price action becomes noise. The lunch lull is:
- A good time for mean reversion scalps
- A bad time for breakout trades (false breaks are common here)
- The best time to study — no reason to be in a trade for most people

**Your edge:** Knowing that moves during the lunch lull have a high probability of failing. The real move comes between 14:00–15:30 EST when the closing auction begins.

### The Closing Auction (14:00–16:00 EST)

The most important period for understanding the NEXT DAY. Volume picks up as institutions position themselves for the following day's open.

The closing hour is when the big money decides what happens tomorrow. If the day's trend continues into the close, expect continuation at the next session start. If the trend reverses in the final hour, expect a gap open against the trend.

---

## Part 3: Key Price Levels During the Day

### Types of Intraday Levels (Strongest to Weakest)

1. **Previous Day's VAH and VAL** — volume profile reference levels (from s03)
2. **Previous Day's High / Low** — structural levels, especially when combined with volume
3. **Session Open (00:00 GMT / 9:30 EST)** — the most important level of the day. Price above = bullish bias, below = bearish bias.
4. **Session High / Low** — levels that, if broken, signify a shift in session character
5. **Opening Range High/Low** — the range of the first 15–30 minutes
6. **Round Numbers** — psychological levels ($100, 1.1000, etc.)

### How Levels Interact

Levels don't work in isolation. A previous day low + session open + round number at the same price? That's a fortress. A single level with no confluence? It's a suggestion, not a plan.

Your job: at the start of each session, draw the levels that have 2+ sources of confluence. Trade only at those levels. Ignore all others.

---

## Part 4: Regime Detection

Before you trade intraday, answer:

**Is today trending or ranging?**

| Metric | Trending | Ranging |
|--------|----------|---------|
| ADX (>25 trending, <20 ranging) | >25 | <20 |
| Boilinger Bands (width) | Expanding | Contracting |
| Moving averages (separation) | Separated (20 vs 50) | Coiled / close together |
| Consecutive same-color candles >2R range | Yes — strong trend | No |
| Reversals at MAs fail? | Yes | No (reversals hold) |

Trade the regime, not your bias. If it's a ranging day, your pivot-level mean reversion system is active and your trend-following system is OFF.

---

## Part 5: Time-Based Edges (Minute-Level Patterns)

Beyond the broad session structure (Part 1), there are predictable minute-level patterns that repeat with statistical consistency. These are your most actionable edges because they are specific enough to script.

### The Daily Clock (EST, /ES /NQ)

| Time (EST) | Pattern | Edge |
|-----------|---------|------|
| **9:30-9:50** | Initial drive — the first 20 min establishes the opening range. ~65% of all daily ranges establish within the first 30 min. | Trade the FIRST 15-min candle break. If it holds, the opening direction often persists. |
| **9:50-10:10** | First reversal window — the opening drive exhausts, first pullback occurs. | Fade the extreme of the opening range at the first sign of delta divergence. |
| **10:10-11:15** | Morning continuation or range build — trend continues OR range establishes. | If trending: ride it. If ranging: buy VAL, sell VAH. |
| **11:15-11:30** | European close inflection — London traders flatten positions. Often creates a sharp 15-min reversal. | Watch for liquidity grab into the close, then fade. |
| **12:00-14:00** | Lunch lull — volume drops ~60%. Moves are noise. | Do not trade breakouts. Mean reversion only. Or don't trade. |
| **14:00-15:30** | Closing auction begins — institutional positioning for next day. Real volume returns. | Trade WITH the closing direction. If the trend continues into close, expect continuation tomorrow. |
| **15:30-15:50** | MOC (Market on Close) imbalance window — MOC orders hit the tape to match closing imbalances. | Sharp move in the direction of the imbalance. Scalpable but don't hold through 16:00. |
| **16:00** | Close surge — last-minute positioning, rebalancing, stop runs. | Watch only. Trading the close is for institutions. |

### Weekly/Monthly Calendar Edges

| Event | Timing | Edge |
|-------|--------|------|
| **OPEX (Option Expiry)** | 3rd Friday of each month | Gamma pinning toward max pain strike. Expect range contraction into expiry, then expansion after. |
| **Month-end rebalancing** | Last trading day of month | Pension/ETF rebalancing creates artificial flows. Trade the rebalancing direction, fade the extreme. |
| **Quarter-end** | Last 3 days of quarter | Institutional window dressing. Expect larger moves as managers adjust positions. |
| **CPI / NFP / FOMC** | Scheduled release times | Do NOT trade 30 min before. Wait 15 min after for the second move (see s10 Part 6). |
| **FOMC decision (8 weeks)** | 8 meetings/year, 2:00 PM EST | Flat 1 hour before. Wait 30 min after for the initial spike to settle, then trade the retest. |
| **Rollover (futures)** | 1 week before expiry | Volume shifts to next contract. Watch for spread distortions. |

### The 80% Rule (Value Area Re-Entry)

If price opens OUTSIDE the prior day's value area (above VAH or below VAL) and then RE-ENTERS the value area within 1-2 hours, there is an ~80% probability that price will rotate to the OPPOSITE side of the value area.

**Trade rule:**
1. Identify previous day's VAH and VAL (from s07).
2. If price opens above VAH and then closes a 15-min candle BELOW VAH → short with target at VAL.
3. If price opens below VAL and then closes a 15-min candle ABOVE VAL → long with target at VAH.
4. Stop: beyond the initial opening extreme.
5. Best when the re-entry happens within the first 90 minutes.

---

## Part 6: Market Internal Dashboard (Futures)

For /ES and /NQ traders, the internals tell you whether the move is real before price confirms. These are not available for FX — if trading FX, skip this section.

### The Three Core Internals

| Indicator | What It Shows | How to Use |
|-----------|---------------|------------|
| **$TICK (NYSE Tick)** | Number of stocks trading on an uptick minus a downtick. Range -2000 to +2000. | Extremes predict reversals. $TICK > +1000 = overbought (fade). $TICK < -1000 = oversold (buy). Readings between -500 and +500 = neutral. |
| **$ADD (NYSE Advance/Decline)** | Number of advancing stocks minus declining stocks. | Confirms breadth. If /ES is up but $ADD is negative, the rally is narrow (AI/AI halo only) and likely to fail. If both are up, broad participation = real rally. |
| **$VOLD (NYSE Volume)** | Volume of advancing issues minus declining issues. | Breadth with weight. A strong $VOLD confirms the move. Divergence between $VOLD and price = reversal signal. |

### How to Read the Dashboard

| Price Action | $TICK | $ADD | $VOLD | Verdict |
|-------------|-------|------|-------|---------|
| /ES making new highs | >+1000 | Positive | Positive | Healthy rally. Let it run. |
| /ES making new highs | <+500 | Flat/negative | Negative | Narrow rally. Expect reversal. |
| /ES making new lows | <-1000 | Negative | Negative | Healthy sell-off. Let it run. |
| /ES making new lows | >-500 | Flat/positive | Positive | Selling exhausted. Bounce coming. |
| /ES breaking out | +800 to +1000 | Positive | Positive | Real breakout. Add to position. |
| /ES breaking out | +300 to +600 | Negative | Negative | Fakeout. Fade it. |

### Sector Rotation (For /ES Traders)

The market rotates through sectors in a predictable sequence during a risk-on cycle. Knowing where you are in the cycle tells you how long the move will last.

| Phase | Leading Sectors | What It Means |
|-------|----------------|---------------|
| **Early cycle** | Tech (XLK), Consumer Discretionary (XLY) | Risk appetite returning. Long /NQ. |
| **Mid cycle** | Industrials (XLI), Materials (XLB), Energy (XLE) | Broadening participation. Long /ES. |
| **Late cycle** | Utilities (XLU), Consumer Staples (XLP), Healthcare (XLV) | Defensive rotation. Risk-off. Short /ES or flat. |
| **Recession** | Gold (GLD), Treasuries (TLT), USD | Flight to safety. Long /GC, short /ES. |

Check sector performance daily on finviz.com or TradingView's stock screener (free). Which sectors led yesterday? Which ones are leading today? Rotation from tech to utilities in 3 days = cycle is late.

### Free Sources for Internals

- **Finviz (free):** S&P 500 heatmap, sector performance
- **TradingView (free):** $TICK, $ADD, $VOLD tickers available
- **Barchart (free):** Market internals page
- **Thinkorswim (free with TD account):** Full internal dashboard
- **TradingView paid:** $TICK + $ADD as indicators on chart

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s03-volume-profile-and-order-flow.md` | Session VAH/VAL levels (defined in s03) are the most important intraday levels. s05 tells you WHEN they matter (opening drive / closing auction). | Drawing daily levels; classifying day type |
| `systems/s06-top-down-analysis.md` | The higher timeframe context (daily/weekly) from s06 tells you which direction to expect within each session. s05 is the execution layer below s06's framing. | Starting top-down analysis; determining bias for the session |
| `systems/s07-order-flow-levels.md` | s07's levels (HVN, LVN, POC) are the WHERE. s05's session timing is the WHEN. Together: a complete intraday framework. | Building watchlist before session; planning trades |
| `systems/s04-backtesting-and-system-development.md` | Session-based filtering is a key s04 filter condition. You backtest a system differently in London vs Asia vs NY. | Filtering backtest trades by session; evaluating system performance by session |
| `systems/s02-trading-psychology.md` | The lunch lull (10-14 EST) is when boredom-based mistakes happen (s02's #1 dangerous state). Knowing the session regime heads off psychological errors. | Pre-trade state check; recognizing urge to trade during low-volume periods |
| `systems/s10-execution-and-trade-management.md` | Intraday execution (limit vs market, trailing stops) depends on which session phase you're in. Opening drive = aggressive fills. Lunch lull = tight spreads, slow fills. | Choosing entry type; managing position during a session |
| `systems/s10-execution-and-trade-management.md` | Time-based edges (Part 5) and the "second move" news protocol (s10 Part 6) are designed to work together. s05 identifies WHEN the edge exists; s10 executes the HOW. | Planning trades around specific clock windows |
| `systems/s00-concept-registry.md` | Market internals ($TICK, $ADD, $VOLD) added to registry as new concepts. Cross-reference with s03 (volume) and s06 (top-down). | Learning internals; checking market health |
