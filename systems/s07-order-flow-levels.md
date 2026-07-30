# s07 — Order Flow Levels

## Part 1: What Makes a Level "Real"

Not all levels are created equal. Most levels drawn on a chart (random horizontal lines, Fibonacci retracements drawn from a swing low to swing high, etc.) are noise. The levels described here come from **actual trading activity** — where volume transacted, where orders sat waiting, where participants used limit orders.

### Level Types by Source of Strength

| Rank | Level Type | Source | Why It's Strong |
|------|-----------|--------|-----------------|
| 1 | **Volume Point of Control (POC)** | VWAP + Volume Profile | Highest transaction volume — the "fair price" consensus. Price returns to POC like gravity. |
| 2 | **High Volume Node (HVN)** | Volume Profile | Price spent significant time here, many transactions. Natural support/resistance. |
| 3 | **Low Volume Node (LVN)** | Volume Profile | Little transaction time. Price crosses these quickly — when returning, they become support/resistance because of the "gap" in activity. |
| 4 | **Previous Day VAH / VAL** | Volume Profile | High-volume edge of value area — institutional reference not retail levels. |
| 5 | **Delta Pivot** | Order Flow | Price level where cumulative delta changed direction (shift from aggressive buying to aggressive selling). |
| 6 | **Stopped Volume** | Volume Profile | Level where a trend stopped — high volume at trend exhaustion. Opposite of POC. |
| 7 | **Sweep Level** | Order Flow | Price beyond an obvious liquidity level (previous high/low) that got "swept" (wicked through) before reversing. |
| 8 | **Round Number** | Psychology | Everyone sees it. Only strong with VBPC (volume-by-price cluster at the round number). |
| 9 | **Fib Retracement** | Geometry | Only valid if it aligns with a volume level. Alone, means nothing. |
| 10 | **Trendline** | Geometry | Only valid if price respects it 3+ times AND it aligns with a volume level. |

---

## Part 2: Finding Levels (TradingView Method)

### Volume Profile Setup (Free / Lite)

1. Open TradingView (free account minimum)
2. Apply `Volume Profile` indicator (available in Lite plan for most pairs)
3. Set period to: Session (for intraday), Day (for daily), or Weeks (for swing)
4. Value Area %: 70% (standard — represents the 70th percentile of volume)
5. Number of rows: 24 (default is fine)

**What you're looking at:**
- **POC** = the longest horizontal bar (highest volume at a specific price)
- **VAH** = top of the value area (price level above which only 15% of volume occurred)
- **VAL** = bottom of the value area (price level below which only 15% of volume occurred)
- **HVN** = clusters of long bars (high volume price range)
- **LVN** = empty space or short bars (low volume price range — price is quick here)

### Delta and Cumulative Delta

Delta = aggressive buys minus aggressive sells at the market price.

- **Positive delta** (+500 contracts): More aggressive buying than selling at this price
- **Negative delta** (−300 contracts): More aggressive selling than buying at this price
- **Cumulative delta divergences**: Price makes a new high, but cumulative delta makes a lower high → exhaustion (potential reversal)
- **Cumulative delta convergence**: Price and cumulative delta move together → trend is healthy

**Free delta setup on TradingView:**
- Use the "Depth of Market" or Footprint chart feature if available
- Alternative: `Volume Delta` indicator on TradingView (Lite plan or above)

---

## Part 3: How to Trade Off These Levels

### Scenario A: Price Returns to POC

| What happens | Your trade |
|-------------|------------|
| Price returns to POC with decreasing volume | Mean reversion trade in direction of daily trend (from s06). Enter at POC, stop below POC range, target VAH or VAL. |
| Price returns to POC with INCREASING volume | POC is breaking. Do NOT mean-revert. Wait for price to establish new POC. |

**Key question:** Is volume increasing or decreasing at POC? If volume is higher at POC than when the level was originally established, the level is failing. If volume is lower, the level is holding.

### Scenario B: Price Approaches HVN

| What happens | Your trade |
|-------------|------------|
| Price enters HVN zone with decreasing momentum | Expect reversal at the nearest edge. Look for reversal candle + delta divergence. |
| Price enters HVN zone with high momentum and high delta | HVN zone may break. Look for continuation setup. |

### Scenario C: Price Approaches LVN

| What happens | Your trade |
|-------------|------------|
| Price approaches LVN from above | Expect quick move through — do NOT short at LVN top. Wait for the sweep. |
| Price approaches LVN from below | Expect quick move through — do NOT buy at LVN bottom. Wait for the sweep. |
| Price returns to LVN after sweep | NOW LVN becomes a level. Place reversal trade at the LVN edge. |

### Scenario D: Delta Divergence at a Level

| Signal | What it means | Trade |
|--------|---------------|-------|
| Price higher high, delta lower high | Exhaustion — buying power drying up | Short at level. Stop above wick. Target POC. |
| Price lower high, delta higher low | Accumulation — selling power drying up | Long at level. Stop below wick. Target POC. |

---

## Part 4: The Level-Trading Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  IDENTIFY LEVELS (pre-market, 3 min)                             │
│  • Draw POC, VAH, VAL for daily                                 │
│  • Draw POC, VAH, VAL for current session                       │
│  • Mark nearest round number                                    │
│  • Mark any pending LVN (gap that hasn't been filled)           │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  ASSESS (using s06 TDA framework)                                │
│  • Which direction is the daily bias?                           │
│  • Which levels align with the bias? (trade WITH the bias)      │
│  • Which levels are counter-trend? (smaller size, scalps only)  │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  WATCH (during the session)                                      │
│  • Set alerts at key levels (POC, VAH, VAL)                     │
│  • Watch delta behavior as price approaches                     │
│  • Watch volume behavior at the level                           │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  EXECUTE (when 2+ conditions align)                              │
│  • Price at level + delta divergence aligned = entry ✅          │
│  • Price at level + increasing volume = WARNING — wait          │
│  • Price at level + mid-session (low vol) = SKIP                │
│  • Price at level + strong trend (ADX > 30) = respect trend    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s03-volume-profile-and-order-flow.md` | s03 defines the concepts (POC, HVN, LVN, delta, cumulative delta). s07 operationalizes them as TRADEABLE LEVELS. s03 = theory, s07 = application. | Converting volume profile concepts to trade setup |
| `systems/s06-top-down-analysis.md` | s06 tells you which levels matter today (biased by daily/weekly trend). s07 finds those levels. You can't have s07 without s06's directional context. | Pre-market routine; filtering levels by bias |
| `systems/s05-intraday-market-structure.md` | A level's behavior differs by session: opening drive breaks are real, lunch lull breaks are false. s05's session knowledge filters s07's level signals. | Evaluating a level break during the session |
| `systems/s10-execution-and-trade-management.md` | Once a level-triggered trade is taken, s10 handles execution — limit vs. market entry, stop placement, trailing. s07 is the trigger, s10 is the management. | Executing a level-based setup |
| `systems/s04-backtesting-and-system-development.md` | Level-based setups (POC bounce, delta divergence at HVN) can be backtested using s04's methodology. Most profitable systems are level-based. | Backtesting a level-based trading system |
| `systems/s01-mathematics.md` | Stop distance from a level determines R. The shorter the stop (tight level), the better the R:R. s01's R-multiple calculations integrate directly. | Computing position size for a level trade |
