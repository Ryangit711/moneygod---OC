# s08 — Advanced Risk and Position Sizing

## Part 1: The Fundamental Law of Risk

**The single most important number in trading is NOT your win rate or your R:R. It's your risk per trade as a percentage of account.**

Everything else (strategy, edge, discipline) is secondary to this number. Because if you risk 10% per trade, you will blow up — no matter how good your system. Math doesn't care about your edge.

### The Blow-Up Table (from s01 — repeated here for emphasis)

| Risk/Trade | Win Rate | Consecutive Losses to Blow Up (50% drawdown) |
|-----------|----------|----------------------------------------------|
| 0.5% | 50% | ~139 |
| 1% | 50% | ~69 |
| 2% | 50% | ~34 |
| 3% | 50% | ~23 |
| 5% | 50% | ~13 |
| 10% | 50% | ~7 |

A 2% risk/trade means you blow up (50% drawdown) after 34 consecutive losses. If you trade daily, that's about 7 weeks of losing. Is that possible? Yes. Every system has drawdown periods of 20+ consecutive losses. Especially in choppy markets.

---

## Part 2: Position Sizing Methods

### Method 1: Fixed Fractional (Standard)

**Formula:** `Position Size = (Account × Risk%) ÷ Stop Distance in Dollars`

Example: $10,000 account, 1% risk ($100), stop is 20 pips on EUR/USD ($10/pip)
- Position size = $100 ÷ $20 = 0.05 lots (5 micro lots)

This is the baseline. Use this until you have a consistent edge.

### Method 2: Kelly Criterion (Optimal)

**Formula:** `Kelly% = (W × (R+1) − 1) ÷ R`
- W = win rate (decimal)
- R = win/loss ratio (R:R)

Example: Win rate 55% (0.55), R:R = 2:1
- Kelly% = (0.55 × 3 − 1) ÷ 2 = 0.325 = 32.5%

**Full Kelly is too aggressive. Use quarter-Kelly or eighth-Kelly.**
- Quarter-Kelly: 32.5% ÷ 4 = 8.125% → still too high for most people
- Eighth-Kelly: 32.5% ÷ 8 = 4.06% → actually useable (treat as max-per-trade cap)

**When Kelly breaks:**
- Your win rate is not stable over time (it changes with market regime)
- Overlapping trades (correlation) violates Kelly's independence assumption
- Kelly assumes you know the exact edge, which you don't (sampling error)

### Method 3: Volatility-Adjusted (Fixed Ratio with ATR)

**Formula:** `Position Size = (Account × Risk%) ÷ (ATR × 1.5)`

Stop distance is proportional to volatility. When volatility expands, position size shrinks. When volatility contracts, position size grows. Same risk %, variable stop.

This is superior for:
- Systems with stop distances that vary (e.g., structural stops, not fixed pips)
- Markets with changing volatility (most of them)
- Any system where you want risk % to remain consistent across regimes

### Method 4: Drawdown-Modulated

Start with Method 1. But when in a drawdown (account below previous equity peak):

| Drawdown | Risk % Modifier | Example (1% base) |
|----------|----------------|--------------------|
| 0–5% | Normal | 1% |
| 5–10% | Halve | 0.5% |
| 10–15% | Quarter | 0.25% |
| 15–20% | Stop trading | 0% |
| >20% | STOP. Account review required. | N/A |

This is the only way to survive. Your edge stays the same, you just temporarily reduce exposure. When you return to previous equity peak, resume 1%.

---

## Part 3: Correlation Sizing

### The Invisible Killer

You have a $10,000 account. You risk 1% ($100) on EUR/USD. You risk 1% ($100) on GBP/USD. You risk 1% ($100) on USD/JPY.

That's 3% total risk — because these pairs are highly correlated. When EUR/USD moves, GBP/USD and USD/JPY move with it. Your 3% realized risk is actually ~2.5% effective risk.

**Correlation pairs (FX):**
| Pair | Correlated With | Correlation Strength |
|------|----------------|---------------------|
| EUR/USD | GBP/USD | 0.7–0.85 (very high) |
| EUR/USD | USD/CHF | −0.7 to −0.85 (inverse) |
| USD/JPY | USD/CHF | 0.6–0.7 (high) |
| USD/JPY | GBP/USD | −0.6 to −0.7 (inverse) |
| AUD/USD | NZD/USD | 0.7–0.8 (high) |
| EUR/USD | EUR/JPY | 0.5–0.6 (moderate) |

**The rule:** Total correlated risk per direction must not exceed 2.5% of account.

If you're long EUR/USD and long GBP/USD at the same time:
- Total risk = 1% + 1% = 2%, but effective risk = ~1.7% (because they don't move perfectly together)
- Still: don't risk more than 2.5% on correlated pairs in the same direction

**For futures:**
- /ES and /NQ are correlated (~0.6). Don't double-up directionally.
- /ES and /YM are correlated (~0.8). Same rule.
- Metals (/GC, /SI) are correlated (~0.5). Caution.

---

## Part 4: Scaling In and Out

### Scaling In

Adding to a position as it moves in your favor.

| Approach | How | When |
|----------|-----|------|
| **Pyramid (aggressive)** | 1 unit at entry, 2 at +1R, 3 at +2R | Strong trends with conviction |
| **Pyramid (conservative)** | 1 unit at entry, 1 at +1R, 0.5 at +2R | Moderate conviction |
| **Scale into pullback** | 1 unit at entry, 1 unit at −0.5R, 0.5 at −1R | Strong trend, careful averaging (risky!) |

Pyramiding works IF your stop moves with each add. The average entry price improves, but the total position size grows. Move stop to breakeven or to the previous entry point.

**Danger of scaling in without moving stop:** Your average entry worsens (you buy at higher price = average entry is higher than first entry). If the trend reverses, your loss is larger than if you took a single entry. Never scale into a position without moving your stop.

### Scaling Out

Exiting a portion of a position at different targets.

| Approach | How | Why |
|----------|-----|-----|
| **50/50** | 50% at +1R, 50% at +3R | Capture profits early, let remainder run |
| **1/3, 1/3, 1/3** | 33% at +1R, 33% at +2R, 33% at +3R | Higher probability, lower profit per trade |
| **Trailing stop + partial** | Exit 25% at each R target, trail stop on remainder | Capture full trend when it runs |

**The math of scaling out:**
- 1-lot position, +2R target: Profit = 2R
- 50/50 scale: 0.5 lot at +1R (0.5R) + 0.5 lot at +3R (1.5R) = 2R total

Same total profit, but with scaling out you get a psychological benefit (pride of hitting targets) and the second target has a higher probability of being hit because the first target reduces your risk. The downside: you cap the max gain of a massive trend (the 5R+ moves).

**Verdict:** Scale out if you're starting out. Full-sized exits are for experienced traders with tested systems.

---

## Part 5: The Risk Decision Tree

```
Are you risking more than 2% on this single trade?
├── YES → Reduce size. 2% max as a starting trader.
└── NO → Continue.

Do you have correlated trades open in the same direction?
├── YES → Combined risk must be ≤ 2.5%.
├── YES → And combined risk > 2.5%? → Reduce the smaller trade.
└── NO → Continue.

Is your stop at a valid structural level?
├── YES → Continue (the stop is "real").
├── NO, it's a random pip level → Move stop to the nearest HVN/structural level.
└── YES, but it's way too far (risk is >5% even at minimum size) → Skip the trade. Level is too far away.

Are you in a drawdown?
├── NO → Full risk (1% or whatever your base is).
├── YES, 5-10% → Halve risk.
├── YES, 10-15% → Quarter risk.
└── YES, 15-20% → No trades. Review.

Is the trade in the direction of the daily/weekly trend? (from s06)
├── YES → Normal risk.
└── NO (counter-trend) → Halve risk. Scalp only.
```

---

## Part 6: Anti-Fragile Position Architecture

Most position sizing (Parts 1-4) treats every entry as a single bet. Anti-fragile architecture treats a position as a PROCESS — a sequence of bets that adapts as the market reveals information.

### The Probe → Confirmation → Conviction Framework

| Phase | Size (% of intended max) | Trigger | Stop | Psychology |
|-------|--------------------------|--------|------|------------|
| **Probe** | 10-20% | First indication of setup. Level is near, structure is set-up. | Wide — structural level below/above. | "I'm paying to learn." The probe is tuition, not conviction. |
| **Confirmation** | 30-40% | Price reaches the level, shows absorption/acceptance, first target hit. | Move to breakeven on full position. | "The market confirmed my thesis at the level." |
| **Conviction** | Remaining 40-50% | Structure break — price breaks the range, delta confirms, session in your favor. | Breakeven on full position or trail. | "Flow has committed." Size accordingly. |

### How It Works in Practice

**Example: Long EUR/USD at support level**

**Step 1 — Probe (0.05 lots, $5 risk in a $1000 account):**
- Entry at 1.0950, stop at 1.0920 (30 pip stop)
- Thesis: "Weekly support + HVN at this level + bullish delta divergence on 15m"
- If stopped: loss = $5. You paid $5 for information: "This level is not holding."

**Step 2 — Confirmation (add 0.15 lots, total 0.2 lots, $7.50 additional risk):**
- Trigger: Price touched 1.0950, bounced to 1.0970 (20 pips), shows buying at the level
- Move stop on entire 0.2 lots to 1.0940 (breakeven from here)
- If stopped now: loss = $0 (the probe's profit covers the new add's stop distance)
- You are paying nothing more for this information

**Step 3 — Conviction (add 0.2 lots, total 0.4 lots):**
- Trigger: Price breaks above 1.1000 (resistance, structural break) with delta confirmation
- Move all stops to breakeven
- Target: 1.1080 (next major level)
- If reversed to breakeven: $0 loss. You tested the thesis for free.
- If hits target: profit = (0.05 x $50) + (0.15 x $110) + (0.2 x $80) = $2.50 + $16.50 + $16.00 = $35 on what started as a $5 risk trade

### The "Buy Information" Philosophy

Every probe is a SMALL payment for information. If the probe loses, you learned: "this level is not valid today." That information is worth the probe cost. If the probe wins, you get confirmation and size up.

**Rule:** If you are not willing to lose the probe, you should not take the trade. The probe IS the cost of learning. If the probe feels too expensive, the trade is too big.

### When NOT to Use This Framework

| Situation | Why | Alternative |
|-----------|-----|-------------|
| High-volatility news event | The probe can get stopped before confirmation arrives | Either full-size after second move (s10 Part 6) or skip |
| Gap openings | Multiple entries impossible / unreliable | Single entry at post-gap level |
| Scalping (1-2 tick targets) | No time for multiple entries | Single entry, full size |
| 0DTE options | Time decay destroys the probe | Single entry or skip |
| Account < $500 | Commission costs eat the probe structure | Single entry, reduced size |

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s01-mathematics.md` | The Kelly formula, R-multiples, drawdown non-linearity, and position sizing math are defined in s01. s08 applies them. You must know s01 first. | Computing position size; calculating Kelly fraction |
| `systems/s04-backtesting-and-system-development.md` | Backtest results produce the inputs for s08: win rate, R:R, MaxDD. Without s04, you're guessing your edge. s08 assumes you know it. | Determining base risk %; choosing sizing method |
| `systems/s06-top-down-analysis.md` | Counter-trend trades (s06 Part 3) require halved risk. s08's risk decision tree uses s06's directional bias as input. | Adjusting size by trade direction strength |
| `systems/s10-execution-and-trade-management.md` | Scaling in/out (s08 Part 4) is executed via s10's entry/exit mechanics. s08 decides the plan, s10 executes it. | Executing a scale-in or scale-out plan |
| `systems/s02-trading-psychology.md` | Over-sizing is the #1 cause of emotional trading. s02's revenge state (Dangerous State #2) usually expresses as "increase size to get back to even." s08 prevents this mechanically. | Pre-trade state check; feeling urge to oversize |
| `systems/s12-capital-management-and-scaling.md` | s12 uses the methodology from s08 to decide when to scale up (after 3+ months of positive expectancy, the risk % can increase). s08 is the daily sizing tool, s12 is the growth planner. | Planning account growth targets |
| `systems/s10-execution-and-trade-management.md` | Anti-fragile position architecture (Part 6) relies on s10's execution mechanics for the multiple entries. s08 plans the sequence; s10 places each entry. | Executing a probe → confirmation → conviction sequence |
| `mental-models/information-half-life.md` | "Buy information" philosophy (Part 6) aligns with the information decay curve: early probes in high-information moments are worth more than late entries. | Deciding whether to probe or skip a marginal setup |
