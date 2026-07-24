# What Is VWAP, EMA, and Volume?

## The Three Indicators You Actually Need

Most traders drown in indicators. You need exactly three. These are the ones institutions watch.

---

## VWAP — Volume Weighted Average Price

**What it is:** The average price of an asset, weighted by how much volume occurred at each price level. It tells you where the "smart money" is positioned for the day.

**Think of it as:** The fair price for today. If price is above VWAP, buyers are in control. Below VWAP, sellers are in control.

**How to read it:**
```
Price above VWAP → Bullish bias (buyers paying more than average)
Price below VWAP → Bearish bias (sellers accepting less than average)
Price at VWAP     → Neutral / decision point
```

**VWAP as support/resistance:**
- Price often bounces off VWAP
- First touch of VWAP = often holds as support/resistance
- Multiple touches = stronger level

**Trading rule:**
- Only look for LONG trades when price is above VWAP
- Only look for SHORT trades when price is below VWAP
- Avoid trading when price is oscillating around VWAP (choppy)

**How to add to chart:**
- TradingView: search "VWAP" in indicators → add it
- MT5: Insert → Indicators → Volume → VWAP
- Tradovate: Indicators → VWAP

---

## EMA — Exponential Moving Average

**What it is:** A line on the chart that shows the average price over a specific number of periods, but it gives MORE weight to recent prices (unlike a simple moving average).

**Think of it as:** The trend direction. If the EMA is sloping up, the trend is up. Down = downtrend.

**The EMAs you need:**
| EMA | Period | What It Shows |
|-----|--------|---------------|
| **20 EMA** | 20 periods | Short-term trend (intraday momentum) |
| **50 EMA** | 50 periods | Medium-term trend (daily bias) |
| **200 EMA** | 200 periods | Long-term trend (weekly/monthly bias) |

**How to read them:**
```
Price above 20 EMA → Short-term bullish
Price below 20 EMA → Short-term bearish

20 EMA above 50 EMA → Bullish trend
20 EMA below 50 EMA → Bearish trend

Price above 200 EMA → Long-term bullish
Price below 200 EMA → Long-term bearish
```

**EMA crossover signals:**
- **Golden Cross:** 20 EMA crosses above 50 EMA → bullish
- **Death Cross:** 20 EMA crosses below 50 EMA → bearish
- These are NOT entry signals by themselves — they confirm trend direction

**Trading rule:**
- Trade in the direction of the 20 EMA slope
- Use 50 EMA as dynamic support/resistance
- Use 200 EMA to determine long-term bias (don't fight it)

**How to add to chart:**
- TradingView: search "EMA" → add it twice → set one to 20, one to 50
- MT5: Insert → Indicators → Trend → Moving Average → set to Exponential, period 20
- Tradovate: Indicators → Moving Average → set to EMA, period 20

---

## Volume — How Much Trading Activity Occurred

**What it is:** The number of contracts/shares/lots traded during a specific time period. It shows how much participation there was at each price level.

**Think of it as:** The conviction behind a move. High volume = strong move. Low volume = weak move.

**How to read it:**
```
High volume + Price up    = Strong bullish move (real buying)
High volume + Price down  = Strong bearish move (real selling)
Low volume + Price up     = Weak move (likely to reverse)
Low volume + Price down   = Weak move (likely to reverse)
```

**Volume confirms everything:**
- A breakout on high volume = real
- A breakout on low volume = trap
- A reversal on high volume = strong reversal
- A reversal on low volume = weak reversal

**Volume climax:**
- Extremely high volume at a swing point = potential reversal
- "Exhaustion volume" — the last buyers/sellers have entered
- After a climax, expect a reversal

**Volume at support/resistance:**
- High volume at support = buyers defending the level → likely to hold
- Low volume at support = weak defense → likely to break
- Same logic for resistance (sellers defending vs. not)

**How to add to chart:**
- TradingView: "Volume" indicator → adds bars at bottom of chart
- MT5: already shows volume by default (if not: Insert → Indicators → Volume)
- Tradovate: already shows volume by default

---

## How They Work Together

**The setup:**
```
1. VWAP: Is price above or below? (Bias direction)
2. 20 EMA: Is it sloping up or down? (Momentum confirmation)
3. 50 EMA: Where is price relative to it? (Trend confirmation)
4. Volume: Is the move supported by volume? (Conviction)
```

**Example long trade:**
```
- Price is above VWAP ✓ (bullish bias)
- 20 EMA is sloping up ✓ (momentum up)
- Price just bounced off 50 EMA ✓ (trend support)
- Volume spike on the bounce ✓ (conviction)
= LONG trade with SL below 50 EMA, TP above VWAP
```

**Example short trade:**
```
- Price is below VWAP ✓ (bearish bias)
- 20 EMA is sloping down ✓ (momentum down)
- Price just rejected from 50 EMA ✓ (trend resistance)
- Volume spike on the rejection ✓ (conviction)
= SHORT trade with SL above 50 EMA, TP below VWAP
```

**If indicators conflict:** Don't trade. Wait for alignment.

---

## Quick Reference Card

```
VWAP   = fair price for today. Above = bullish, below = bearish.
20 EMA = short-term trend. Slope up = bullish momentum.
50 EMA = medium-term trend. Support/resistance in trend.
VOLUME = conviction. High volume confirms the move.
ALL THREE ALIGNED = high-probability trade. No alignment = no trade.
```

---

## Practice Drill

Open TradingView with EUR/USD 15-minute chart:
1. Add VWAP, 20 EMA, 50 EMA, and Volume
2. Find 3 moments where all 4 indicators aligned
3. For each: mark where you'd enter, where your SL would be, where your TP would be
4. Calculate R:R for each
5. If all 3 have R:R ≥ 1:2, those are A+ setups

*Open TradingView right now. Add VWAP, 20 EMA, 50 EMA, and Volume to EUR/USD 15-min. Find one setup where all four agree. You just read the chart like a pro.*
