# s01 — Trading Mathematics from First Principles

## Part 1: Arithmetic of P&L

### Pip Value — The Fundamental Unit

A pip (Percentage in Point) is the smallest standard price movement
in most currency pairs.

- Most pairs (EUR/USD, GBP/USD, AUD/USD): 4th decimal = 1 pip
- JPY pairs (USD/JPY, EUR/JPY): 2nd decimal = 1 pip
- CAD pairs (USD/CAD, EUR/CAD): 4th decimal = 1 pip
- Gold (XAU/USD): 2nd decimal = 1 pip (also called 1 cent)

**Pip value formula:**

```
Pip Value (in quote currency) = (0.0001 or 0.01) × Lot Size
```

For EUR/USD:
- 0.01 lot = 1,000 units → 1 pip = 0.0001 × 1,000 = $0.10
- 0.10 lot = 10,000 units → 1 pip = 0.0001 × 10,000 = $1.00
- 1.00 lot = 100,000 units → 1 pip = 0.0001 × 100,000 = $10.00

For USD/JPY (different — 2 decimals):
- 0.01 lot = 1,000 units → 1 pip = 0.01 × 1,000 = ¥10
- Convert to USD: ¥10 ÷ USD/JPY rate. If USD/JPY = 150, then ¥10 = $0.067

**Futures tick value (MES, MNQ):**
- MES: 1 tick (0.25 index points) = $1.25
- MNQ: 1 tick (0.25 index points) = $0.50
- MES: 1 point (4 ticks) = $5.00
- MNQ: 1 point (4 ticks) = $2.00

### Position Sizing — The Risk Formula

```
Risk $ = Account Size × Risk %
Lot Size = Risk $ ÷ (Stop Distance in Pips × Pip Value per Lot)
```

**Worked example (EUR/USD):**
- Account: $5,000
- Risk: 1% = $50
- Stop distance: 15 pips
- Pip value at 1.00 lot: $10
- Lot size = $50 ÷ (15 × $10) = 0.333 → round down to 0.30 lots

**Worked example (MES):**
- Account: $5,000
- Risk: 1% = $50
- Stop distance: 5 points (20 ticks)
- Point value: $5
- Contracts = $50 ÷ (5 × $5) = 2 contracts

### Margin and Leverage

**Margin** = the cash your broker holds while you have an open position.
**Leverage** = how much bigger a position you can take vs. your cash.

- 1:100 leverage: $1,000 cash controls $100,000 of currency
- 1:30 leverage (EU/UK cap): $1,000 controls $30,000
- 1:50 leverage (US Forex cap): $1,000 controls $50,000

**The trap:** Leverage multiplies both wins AND losses.
- 1.00 lot EUR/USD, 100-pip move = $1,000 gain OR loss
- On $1,000 account with 1:100 leverage, that's a 100% gain or 100% loss in one trade

**Required margin formula:**
```
Required Margin = (Lot Size × Contract Size) ÷ Leverage
```
For EUR/USD, 0.10 lot at 1:100 leverage:
- Margin = (10,000) ÷ 100 = $100 held while the position is open

### Drawdown — The Reality of Losing

Drawdown is how much your account has fallen from its peak.

**What retail misses:** Drawdown is non-linear. A 50% drawdown requires
a 100% gain to recover. A 90% drawdown requires a 900% gain.

| Drawdown | Gain Needed to Recover |
|----------|----------------------|
| 10% | 11% |
| 25% | 33% |
| 50% | 100% |
| 75% | 300% |
| 90% | 900% |

**The rule:** Your max drawdown target is 10%. After that, halve position
size until you recover. (See s08 — Advanced Risk.)

---

## Part 2: Probability for Traders

### Expected Value (EV) — The Only Number That Matters

```
EV = (Win Probability × Average Win) − (Loss Probability × Average Loss)
```

If EV > 0 → the system is profitable over time.
If EV < 0 → the system is losing over time.

**Example:**
- Win rate = 40% (you lose more than you win)
- Average win = $200 (2R where R = $100)
- Average loss = $100 (1R)
- EV = (0.40 × $200) − (0.60 × $100) = $80 − $60 = **+$20 per trade**

Even with a 40% win rate, you profit. This is why R:R matters more than win rate.

**Example (the loser most retail traders run):**
- Win rate = 60%
- Average win = $50 (small take-profits)
- Average loss = $150 (letting losers run)
- EV = (0.60 × $50) − (0.40 × $150) = $30 − $60 = **−$30 per trade**

You win 60% of the time and still bleed out.

### R-Multiples — The Universal Language

R = your risk on a trade. Everything is measured in multiples of R.

- A "2R winner" = you made 2× what you risked
- A "1R loser" = you lost exactly what you risked
- A "5R runner" = you made 5× what you risked

**Why R matters:** It decouples performance from absolute dollars. A $200 win
is meaningless until you know the risk was $100 (2R) or $400 (0.5R).

| Outcome | Frequency | Size | EV Contribution |
|---------|-----------|------|-----------------|
| Big winner | 10% | +5R | +0.5R per trade |
| Standard winner | 35% | +2R | +0.7R per trade |
| Scratch (breakeven) | 15% | 0R | 0R |
| Standard loser | 35% | −1R | −0.35R per trade |
| Big loser (rare) | 5% | −2R | −0.10R per trade |

**EV per trade = +0.75R**. Over 100 trades, +75R. If R = $50, that's $3,750.

### The Win Rate × Risk-Reward Matrix

| Win Rate / R:R | 1:1 | 1:1.5 | 1:2 | 1:3 |
|----------------|-----|-------|-----|-----|
| 30% | −0.40R | −0.25R | −0.10R | +0.05R |
| 40% | −0.20R | −0.10R | 0 | +0.20R |
| 50% | 0 | +0.25R | +0.50R | +1.00R |
| 55% | +0.10R | +0.325R | +0.65R | +1.30R |
| 60% | +0.20R | +0.40R | +0.80R | +1.60R |

**Read this table. Tattoo it.** At 30% win rate and 1:1 R:R, you bleed.
At 30% and 1:3, you profit. The question is never "is my win rate good?"
The question is "is my win rate × R:R positive?"

### Kelly Criterion — The Optimal Bet Size

John Kelly, 1956. The formula that tells you the maximum theoretical
size you should bet on each trade, given your edge.

```
Kelly % = W − (L ÷ R)

where:
  W = win rate (decimal, e.g., 0.55)
  L = loss rate (1 − W, e.g., 0.45)
  R = average win ÷ average loss (e.g., 2 if you win 2R and lose 1R)
```

**Example:**
- Win rate = 55%, average win = 2R, average loss = 1R → R = 2
- Kelly % = 0.55 − (0.45 ÷ 2) = 0.55 − 0.225 = **0.325 = 32.5%**

**The Kelly CRITIQUE — why the textbook version is dangerous:**
- Kelly assumes you know your true win rate and R:R with certainty. You don't.
- Kelly assumes no correlation between trades. In reality, your losses cluster.
- Full Kelly sizing produces drawdowns that no human can sit through (40–60%).

**Practical use:**
- **Half-Kelly**: 0.5 × 32.5% = 16.25% (still too aggressive for retail)
- **Quarter-Kelly**: 0.25 × 32.5% = 8% (still too aggressive)
- **Eighth-Kelly**: 0.125 × 32.5% = 4% (top of practical range for retail)
- **Tenth-Kelly or 1% rule**: Robust against model error. You will not blow up.

**The takeaway:** Kelly tells you the ceiling. You should trade a fraction of it.
The default 1% rule is roughly 1/30th of Kelly for most retail parameters — 
deliberately conservative.

---

## Part 3: Statistics That Matter

### Standard Deviation ≈ Volatility

Standard deviation measures how spread out returns are.
High σ = high volatility = wider stops needed.

```
σ (sample) = √[ Σ(x − x̄)² ÷ (n − 1) ]
```

**Practical:** Don't calculate this by hand. Use TradingView's "Standard Deviation"
indicator (built-in, free). A reading of 2.0 on the daily means the typical
daily move is 2.0 of whatever unit the indicator is set to (pips, %, points).

### Normal Distribution vs. Fat Tails — Why Stops Blow Up

Textbook statistics assume returns are normally distributed (bell curve).
Real markets are NOT. They have **fat tails** — extreme moves happen
much more often than the normal distribution predicts.

| Model prediction (normal) | Reality (fat tails) |
|---------------------------|-------------------|
| 3σ move: 0.3% probability (1 in 370 days) | ~5% probability (~1 in 20 days) |
| 4σ move: 0.01% probability (1 in 15,000 days) | ~1% probability (~1 in 100 days) |
| 6σ move: 1 in 1 billion days | ~1 in 1,000 days |

**Implication for stops:**
- A "3-sigma stop" is not safe. It will hit ~1 in 20 days.
- A "5-sigma stop" is the realistic "safe" stop for fat-tail awareness
- Use of options (long puts/calls as a hedge) is the only true protection against 6σ+

### Correlation — Why "Two Trades" Can Be One Trade

Correlation measures how two assets move together. Range −1 to +1.

| Correlation | What it means | Example |
|-------------|--------------|---------|
| +1.0 | Always move same direction | EUR/USD & GBP/USD (~0.85) |
| +0.7 | Usually same direction | S&P 500 & Nasdaq (~0.90) |
| 0 | Independent | EUR/USD & Gold (≈0) |
| −0.7 | Usually opposite | USD & Gold (~−0.40) |
| −1.0 | Always opposite | USD/JPY & Gold (sometimes) |

**The risk rule:** If you are long EUR/USD and long GBP/USD,
you are not "diversified" — you are double-long EUR. If EUR
drops, both positions lose. Total risk = 2 × single risk.

**Practical check:** Use TradingView's correlation indicator
or check MYFXbook's correlation matrix (free).

---

## Part 4: Metrics — What Each Tells You (and Lies to You)

### Profit Factor (PF)

```
PF = Gross Profits ÷ Gross Losses
```

- PF > 1.5 → profitable
- PF > 2.0 → very profitable
- PF < 1.0 → losing system
- PF > 3.0 → suspiciously good — likely curve-fit. Re-test on out-of-sample data.

### Sharpe Ratio

```
Sharpe = (Return − Risk-Free Rate) ÷ σ (standard deviation of returns)
```

- Sharpe > 1.0 → decent
- Sharpe > 2.0 → excellent
- Sharpe > 3.0 → hedge-fund-grade (or fake backtest)

**The lie:** Sharpe penalizes upside spikes. A system that occasionally
catches big wins looks worse on Sharpe than a system that grinds small wins.

### Sortino Ratio

Same as Sharpe but only counts downside volatility. Fixes the Sharpe lie.

```
Sortino = (Return − Risk-Free Rate) ÷ σ-downside
```

Sortino is always ≥ Sharpe. Use Sortino over Sharpe for trading evaluation.

### Maximum Drawdown (MaxDD)

The largest peak-to-trough decline in your equity curve.

- MaxDD < 10% → professional
- MaxDD 10–20% → aggressive but acceptable
- MaxDD > 25% → likely a blow-up in progress

### Recovery Factor

```
Recovery Factor = Net Profit ÷ Max Drawdown
```

- > 3 → strong system
- < 1 → your drawdown is bigger than your annual profit. Reconsider.

---

## Part 5: Geometric vs. Arithmetic Returns — Why Compounding Is Non-Linear

### The Difference

- **Arithmetic return:** Average of returns. (10% + −20% + 30%) ÷ 3 = 6.67%
- **Geometric return:** What you actually experience. ∛(1.10 × 0.80 × 1.30) − 1 = 4.6%

Geometric return is always ≤ arithmetic return when volatility > 0.

### The Volatility Drag

```
Geometric Return ≈ Arithmetic Return − (σ² ÷ 2)
```

Example: If your arithmetic average trade is +2% with σ = 10% per trade:
- Volatility drag = (0.10² ÷ 2) = 0.5% per trade
- Your true per-trade geometric return = 2% − 0.5% = 1.5%

### The 50% Drawdown Problem

To recover from 50% drawdown, you need +100% return. Why?
- Start: $100
- Lose 50%: $50
- Gain 50%: $75 (not $100)
- Gain 100%: $100

Most retail traders blow accounts not because they can't make money,
but because they take 50% drawdowns and can't dig out.

### Scaling Is Non-Linear

Doubling your risk per trade does NOT double your returns. It also
doubles your drawdowns, and drawdowns are geometric — they hurt more
than the equivalent gain helps.

| Risk per trade | Avg expected return | Avg expected drawdown | % chance of blow-up |
|----------------|--------------------|-----------------------|---------------------|
| 0.5% | +30%/yr | 5% | <1% |
| 1.0% | +50%/yr | 10% | ~2% |
| 2.0% | +75%/yr | 25% | ~15% |
| 5.0% | +120%/yr | 60% | ~50% |
| 10.0% | +200%/yr | 100% | ~95% |

**Read this table.** Five-percent risk per trade has a 50% blow-up rate.
Most "gurus" recommend 5%. They are selling hope, not edge.

---

## Part 6: Reference Card — All Formulas

| Formula | Equivalent Plain-English |
|---------|-------------------------|
| Pip Value = (0.0001 or 0.01) × Lot | How much one pip is worth |
| Risk $ = Account × Risk % | How much you can lose on a trade |
| Lots = Risk $ ÷ (Stop Pips × Pip Value) | How big your position should be |
| EV = (W% × Avg Win) − (L% × Avg Loss) | If positive, you win over time |
| Kelly % = W − (L ÷ R) | The mathematically optimal bet size |
| Quarter-Kelly = practical bet size | What you should actually trade |
| σ = sqrt(Σ(x-mean)² / (n-1)) | How volatile your returns are |
| Sortino = (Return − RF) ÷ σ-downside | Sharpe without the upside penalty |
| MaxDD = max peak-to-trough decline | How deep your worst dip is |
| Geometric Return ≈ Arithmetic − σ²/2 | What you actually live with |
| PF = Gross Profit / Gross Loss | >1.5 = profitable, >3 = suspicious |
| Recovery = Net Profit / MaxDD | >3 = strong, <1 = rethink |

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s08-advanced-risk-and-position-sizing.md` | s01 gives you the math; s08 gives you the dynamic rules for when to break from 1% defaults. Read both together when sizing positions. | Sizing any live position; evaluating drawdown protocols |
| `systems/s04-backtesting-and-system-development.md` | All metrics (PF, Sharpe, Sortino, MaxDD, Recovery Factor) feed directly into backtest analysis. Cannot evaluate a backtest without s01's formulas. | Running backtests; deciding if a strategy is tradeable |
| `00-background-edge.md` | Your "real P&L management" edge (Section 1 of 00) lets you feel these numbers without panic. Most retail traders freeze the first time they see a $500 drawdown — you have managed clinics. | When drawdown math feels abstract |
| `systems/s09-journaling-and-performance-analysis.md` | The journal template uses R-multiples (defined here in s01 Part 2). Every journaled trade should be tagged with R result. | Filling out the journal; weekly review |
| `quickstart/pip-calculator.md` | The pip calculator is the practical tool for s01 Part 1. Use both — math here, calculator there for speed. | Quickly sizing a position without manual math |
| `systems/position-sizing-by-flow.md` | s01 defines the static math (size = risk ÷ stop × pip value). The existing position-sizing-by-flow file teaches you to vary by liquidity regime — that's dynamic, layered on top of this static foundation. | Adjusting size based on Net Liq state |
| `trading/trading-trading-commandments.md` WAIT → actually `trading/trading-commandments.md` | Commandment #2 (risk only what you can afford to lose) and #5 (R:R minimum 1:1.5) — both rules only make sense after reading s01 Part 2. | Reading commandments before each session |
| `plumbing-hierarchy-master.md` Part 5 (15 Trading Edges) | Each of the 15 edges has an EV. Without s01, you can't compute it. With s01, each edge becomes a computable bet. | Evaluating which edges are worth trading |
