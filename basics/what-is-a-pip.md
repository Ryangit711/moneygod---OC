# What Is a Pip?

## The Smallest Move That Matters

A **pip** (Percentage in Point) is the smallest standard price movement in a currency pair.

### Forex Pips

For most pairs (EUR/USD, GBP/USD, AUD/USD, NZD/USD):
- 1 pip = the **4th decimal place**
- EUR/USD moves from 1.0850 to 1.0851 = **1 pip**

For JPY pairs (USD/JPY, EUR/JPY, GBP/JPY):
- 1 pip = the **2nd decimal place**
- USD/JPY moves from 149.50 to 149.51 = **1 pip**

**Exception:** Some brokers show 5 decimal places (fractional pips / pipettes).
- EUR/USD at 1.08507 → the "7" is a pipette (1/10 of a pip)
- For trading purposes, you care about the 4th decimal place

### Pip Value

Pip value depends on lot size and the quote currency.

**For USD-quoted pairs (EUR/USD, GBP/USD):**
| Lot Size | Units | Pip Value |
|----------|-------|-----------|
| 0.01 (micro) | 1,000 | $0.10/pip |
| 0.1 (mini) | 10,000 | $1.00/pip |
| 1.0 (standard) | 100,000 | $10.00/pip |

**For non-USD pairs (USD/CAD, AUD/USD, etc.):**
- Same pip values, but converted at current exchange rate
- Example: USD/CAD at 1.3600, 0.01 lot → 1 pip = $0.10 / 1.36 = ~$0.074 CAD
- Approximate: multiply USD pip value by 0.7-0.8 for CAD pairs

---

## Spread

The **spread** is the difference between the Bid price and the Ask price. It is your COST of trading.

- **Bid** = price you can SELL at
- **Ask** = price you can BUY at
- **Spread** = Ask − Bid

**Example:**
```
EUR/USD: Bid 1.0849, Ask 1.0851
Spread = 1.0851 - 1.0849 = 2 pips
```

If you buy EUR/USD at 1.0851, price must move to 1.0853 before you break even. The spread is the toll you pay to enter the trade.

**Typical spreads:**
| Pair | Normal Spread | Stressed Spread |
|------|--------------|-----------------|
| EUR/USD | 0.8-1.5 pips | 3-5+ pips |
| USD/CAD | 1.5-2.5 pips | 4-8+ pips |
| USD/JPY | 0.8-1.5 pips | 3-6+ pips |
| GBP/USD | 1.2-2.0 pips | 4-10+ pips |

Wider spreads = more cost. Avoid trading during low-liquidity hours when spreads blow out.

---

## Lot Size

A **lot** is the unit of measurement for a trade size.

| Lot Type | Units | Lot Value (EUR/USD) |
|----------|-------|---------------------|
| Standard | 100,000 | $10/pip |
| Mini | 10,000 | $1/pip |
| Micro | 1,000 | $0.10/pip |
| Nano | 100 | $0.01/pip |

**You will trade micro lots (0.01)** until you're consistently profitable. This means:
- 10 pip win on EUR/USD = $1
- 10 pip loss = -$1
- Your entire day's risk = a cup of coffee

**The math:**
```
Pip Value = (Lot Size × Pip Size) / Exchange Rate
For EUR/USD: Pip Value = (1,000 × 0.0001) / 1.0850 = $0.092 ≈ $0.10
```

---

## Leverage

Leverage lets you control a large position with a small amount of capital.

**How it works:**
- Broker offers 1:100 leverage
- You deposit $1,000
- You can control up to $100,000 (1 standard lot)

**The catch:** Leverage multiplies BOTH wins AND losses.

| Leverage | Your Capital | Max Position | 10 Pip Move |
|----------|-------------|--------------|-------------|
| 1:100 | $1,000 | $100,000 | ±$100 |
| 1:50 | $1,000 | $50,000 | ±$50 |
| 1:20 | $1,000 | $20,000 | ±$20 |
| 1:10 | $1,000 | $10,000 | ±$10 |

**Key insight:** Higher leverage = more risk per pip. You don't need high leverage. You need small lot sizes.

**For prop firms:**
- FTMO: max 1:100 leverage
- Funding Pips: max 1:100 leverage
- TradeDay: no leverage (futures, margin-based)

**Rule of thumb:** Use the lowest leverage that lets you place your intended lot size. If you're trading 0.01 lot, you barely need any leverage at all.

---

## Margin

**Margin** is the collateral you put up to open a trade. It is NOT a fee — it's held while the trade is open and returned when you close.

**Free Margin** = Your Balance − Used Margin

If your free margin drops too low, your broker will close your trade (margin call / stop out).

**Example:**
- Account balance: $1,000
- Open 0.1 lot EUR/USD (requires ~$100 margin at 1:100)
- Free margin: $900
- If trade goes against you by $800 → free margin = $100 → danger zone

**Prop firm note:** Prop firms enforce daily loss limits and total drawdown limits. You won't get a margin call — you'll get an account closure if you breach limits.

---

## Drawdown

**Drawdown** = how much your account has fallen from its peak.

**Example:**
- Account peaks at $52,000
- Drops to $48,000
- Drawdown = $4,000 / $52,000 = **7.7%**

**Drawdown types:**
| Type | What It Means | Prop Firm Limit |
|------|--------------|-----------------|
| **Maximum drawdown** | Total account loss from peak | FTMO: 10%, Funding Pips: 5-10% |
| **Daily drawdown** | Loss in a single day | FTMO: 5%, Funding Pips: 3-5% |
| **Trailing drawdown** | Drawdown from peak, resets on new equity high | Apex: $3,000 on $25K |

**Why it matters:** A 50% drawdown requires a 100% gain just to break even. Keep drawdown small. This is why risk per trade is 0.5-1% max.

**The math of ruin:**
```
Drawdown → Required Gain to Recover
10% → 11.1%
20% → 25%
30% → 42.9%
50% → 100%
```

Small drawdowns are survivable. Large ones are death.

---

## R:R (Risk-to-Reward Ratio)

**R:R** = how much you stand to lose vs. how much you stand to gain.

```
Risk:Reward = Potential Loss : Potential Win
```

**Example:**
- You buy EUR/USD at 1.0850
- Stop loss at 1.0840 (10 pips risk)
- Take profit at 1.0880 (30 pips reward)
- R:R = 1:3

**Why it matters:** With 1:3 R:R, you only need to win 1 out of 4 trades to break even. With 1:1 R:R, you need to win 50% just to break even (before spread costs).

**Minimum R:R for prop firms:** 1:1.5 (better if 1:2 or 1:3)

**The math:**
```
With 1:2 R:R (win 50% of trades):
  10 trades × $100 risk = $500 max risk
  5 wins × $200 = $1,000
  5 losses × $100 = -$500
  Net = +$500

With 1:3 R:R (win 40% of trades):
  10 trades × $100 risk = $1,000 max risk
  4 wins × $300 = $1,200
  6 losses × $100 = -$600
  Net = +$600
```

**Rule:** Never take a trade with R:R below 1:1.5. Prefer 1:2 or better.

---

## Quick Reference Card

```
PIP        = smallest move (4th decimal, or 2nd for JPY pairs)
SPREAD     = Ask − Bid (your cost)
LOT        = trade size (use 0.01 micro to start)
LEVERAGE   = magnifier (use low, trade small)
MARGIN     = collateral held (not a fee)
DRAWDOWN   = account decline from peak (keep <5% daily)
R:R        = risk vs reward (aim for 1:2 or better)
```

---

*This file is your vocabulary. Read it until you can define every term without looking.*

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `quickstart/pip-calculator.md` | Pip values from this file are the direct inputs to the pip calculator tool | Opening pip calculator |
| `core/liquidity-equation.md` | Pip value × SL distance × lot size = the numeric risk in the liquidity equation | Computing dollar risk |
| `systems/position-sizing-by-flow.md` | Pip value is the measurement unit that converts flow regime into lot size | Sizing position by flow |
| `basics/order-types.md` | SL and TP distances defined in pips are entered as the stop and limit on every order | Setting SL/TP in pips |
| `trading/prop-firm-architecture.md` | Prop firm drawdown limits are tracked in pips-equivalent and enforced per trade | Checking prop firm rules |
