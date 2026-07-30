# Candlestick Anatomy

## What You're Actually Looking At

A candlestick is a visual representation of price movement over a specific time period. Each candle tells a story: where price opened, where it closed, and how far it traveled in between.

---

## The Parts of a Candlestick

```
        │
        │  ← Upper Wick (Shadow)
        │
    ┌───┴───┐
    │       │
    │       │  ← Body
    │       │
    └───┬───┘
        │
        │  ← Lower Wick (Shadow)
        │
```

| Part | What It Is |
|------|-----------|
| **Body** | The rectangle between the open and close prices |
| **Upper Wick (Shadow)** | The thin line above the body — shows the highest price reached |
| **Lower Wick (Shadow)** | The thin line below the body — shows the lowest price reached |
| **Open** | The price when the candle's time period started |
| **Close** | The price when the candle's time period ended |
| **High** | The highest price during the period (top of upper wick) |
| **Low** | The lowest price during the period (bottom of lower wick) |

---

## Green vs Red (Bullish vs Bearish)

| Candle Color | Direction | Meaning |
|-------------|-----------|---------|
| **Green / White / Hollow** | Price went UP | Close > Open (bulls won) |
| **Red / Black / Filled** | Price went DOWN | Close < Open (bears won) |

**Bullish candle:**
```
        High
        │
    ┌───┴───┐
    │       │  Close (top of body)
    │       │
    │       │  Open (bottom of body)
    └───┬───┘
        Low
```

**Bearish candle:**
```
        High
        │
    ┌───┴───┐
    │       │  Open (top of body)
    │       │
    │       │  Close (bottom of body)
    └───┬───┘
        Low
```

---

## Body Size = Strength

| Body Size | Meaning | Example |
|-----------|---------|---------|
| **Long body** | Strong conviction — one side dominated | Big green candle = buyers in control |
| **Short body** | Indecision — neither side won | Small body = consolidation |
| **No body (Doji)** | Perfect indecision — open = close | Cross shape = market is thinking |

**The rule:** Bigger body = stronger move. Smaller body = weaker move.

---

## Wick Size = Rejection

| Wick Size | Meaning | Example |
|-----------|---------|---------|
| **Long upper wick** | Price tried to go up but was rejected | Sellers pushed back |
| **Long lower wick** | Price tried to go down but was rejected | Buyers pushed back |
| **Short wicks** | Price stayed close to the body's range | Clean move, little rejection |
| **No wicks** | Price never strayed far from open/close | Maximum conviction |

**The rule:** Long wick = rejection. Price tested a level and got pushed back.

---

## Common Candlestick Patterns (You'll Learn These)

### Doji (Indecision)
```
    │
    │  (open = close, tiny body)
    │
```
Market is thinking. Often precedes a reversal.

### Hammer (Bullish Reversal)
```
    │
    │  (small body at top)
    │
    │
    │  (long lower wick)
    │
```
Price dropped hard, buyers pushed it back up. Bullish at support.

### Shooting Star (Bearish Reversal)
```
        │
        │  (long upper wick)
        │
        │
        │  (small body at bottom)
        │
```
Price spiked up, sellers pushed it back down. Bearish at resistance.

### Engulfing (Strong Reversal)
```
   Red    Green
   ┌─┐    ┌───┐
   │█│    │   │
   │█│    │   │  ← Green body completely
   │█│    │   │     covers previous red body
   └─┘    └───┘
```
The new candle completely overwhelms the previous one. Strong signal.

---

## Timeframes

Each candle represents a specific time period. You choose the timeframe:

| Timeframe | One Candle = | Used For |
|-----------|-------------|----------|
| 1-min (M1) | 1 minute | Scalping (not recommended for beginners) |
| 5-min (M5) | 5 minutes | Day trading entries |
| 15-min (M15) | 15 minutes | Day trading entries + structure |
| 1-hour (H1) | 1 hour | Intraday bias |
| 4-hour (H4) | 4 hours | Daily bias |
| Daily (D1) | 1 day | Weekly chart context |
| Weekly (W1) | 1 week | Monthly bias |

**The hierarchy:** Daily → 4H → 1H → 15M → 5M. Higher timeframes set the direction. Lower timeframes give the entry.

**Rule:** Never trade on a timeframe lower than 5-min until you're consistently profitable.

---

## How to Read a Candle — Step by Step

1. **Look at the body color** — green or red? Which side won?
2. **Look at the body size** — how strong was the move?
3. **Look at the wicks** — where was rejection?
4. **Look at the candle's position** — is it at support, resistance, or mid-range?
5. **Look at the candle's neighbors** — what happened before and after?

**Example reading:**
```
EUR/USD 1H candle at 1.0850:
- Green body (bulls won)
- Long lower wick (price dipped to 1.0835, buyers rejected it)
- Short upper wick (clean move up)
- At daily support level
= Bullish rejection candle at support → likely reversal up
```

---

## Quick Reference Card

```
BODY      = open-to-close range (green = up, red = down)
WICK      = price rejection (long wick = strong rejection)
DOJI      = indecision (open = close)
HAMMER    = bullish reversal (long lower wick at support)
SHOOTING STAR = bearish reversal (long upper wick at resistance)
ENGULFING = new candle covers previous one (strong reversal)
TIMEFRAME = which candle to use depends on what you're doing
```

---

*Open TradingView. Look at EUR/USD 1-hour chart. Read 10 candles aloud: "This candle is [color], body is [size], wicks are [long/short], price was rejected from [level]." Do this until it's automatic.*

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `core/tri-region-flow-map.md` | Wick rejection marks liquidity boundaries between Tri-Region zones | Candle wick at key level |
| `core/liquidity-equation.md` | Body size quantifies the liquidity imbalance during a price move | Reading candle strength |
| `trading/complete-strategy-orb-eurusd.md` | ORB entry triggered by candle close above/below opening-range high/low | ORB entry candle forms |
| `core/plumbing-esoterica.md` | Multi-timeframe candle structure shows how liquidity pools drain across timeframes | Stacking timeframes |
| `systems/weekly-flow-checklist.md` | Weekly candle structure sets the flow context for position sizing | Monday candle review |
