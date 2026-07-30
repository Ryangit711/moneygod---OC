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

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s03-volume-profile-and-order-flow.md` | Session VAH/VAL levels (defined in s03) are the most important intraday levels. s05 tells you WHEN they matter (opening drive / closing auction). | Drawing daily levels; classifying day type |
| `systems/s06-top-down-analysis.md` | The higher timeframe context (daily/weekly) from s06 tells you which direction to expect within each session. s05 is the execution layer below s06's framing. | Starting top-down analysis; determining bias for the session |
| `systems/s07-order-flow-levels.md` | s07's levels (HVN, LVN, POC) are the WHERE. s05's session timing is the WHEN. Together: a complete intraday framework. | Building watchlist before session; planning trades |
| `systems/s04-backtesting-and-system-development.md` | Session-based filtering is a key s04 filter condition. You backtest a system differently in London vs Asia vs NY. | Filtering backtest trades by session; evaluating system performance by session |
| `systems/s02-trading-psychology.md` | The lunch lull (10-14 EST) is when boredom-based mistakes happen (s02's #1 dangerous state). Knowing the session regime heads off psychological errors. | Pre-trade state check; recognizing urge to trade during low-volume periods |
| `systems/s10-execution-and-trade-management.md` | Intraday execution (limit vs market, trailing stops) depends on which session phase you're in. Opening drive = aggressive fills. Lunch lull = tight spreads, slow fills. | Choosing entry type; managing position during a session |
