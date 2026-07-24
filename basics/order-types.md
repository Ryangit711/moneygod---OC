# Order Types

## The 5 Ways to Enter and Exit a Trade

Every trade you place uses one of these order types. Know them cold.

---

## 1. Market Order (Instant Execution)

**What it is:** You buy or sell RIGHT NOW at the current price.

**When to use:** You want in immediately. The setup is live. You don't care about getting a slightly better price — you care about getting in.

**How it works:**
```
EUR/USD is trading at 1.0850 (Bid) / 1.0852 (Ask)
You click BUY → you enter at 1.0852 (the Ask price)
Spread cost = 2 pips
```

**Pros:**
- Instant fill — you're in the trade NOW
- No slippage risk (usually fills at displayed price)

**Cons:**
- You pay the spread
- In fast-moving markets, price may have moved by the time your order reaches the server

**Use in prop firms:** YES — primary execution method during eval and funded

---

## 2. Limit Order (Pending — Better Price)

**What it is:** You place an order to buy BELOW current price or sell ABOVE current price. It only fills if price reaches your level.

**When to use:** You have a specific entry price in mind. You're patient. You want a better price than what's available now.

**How it works:**
```
EUR/USD is at 1.0850
You place BUY LIMIT at 1.0830
→ Order sits waiting
→ If price drops to 1.0830, it fills you there
→ If price never reaches 1.0830, order stays unfilled
```

**Buy Limit:** placed BELOW current price (you want to buy cheaper)
**Sell Limit:** placed ABOVE current price (you want to sell higher)

**Pros:**
- Better entry price = better R:R
- No spread cost (you enter at your price)
- Set and forget — no need to watch the screen

**Cons:**
- Price may never reach your level
- You miss the trade entirely if it moves without you

**Use in prop firms:** YES — excellent for OTE entries, FVG fills, and order block entries

---

## 3. Stop Loss (Risk Management — NON-NEGOTIABLE)

**What it is:** An order that CLOSES your trade if price moves against you by a set amount. It is your seatbelt.

**When to use:** EVERY. SINGLE. TRADE. No exceptions. No excuses.

**How it works:**
```
You BUY EUR/USD at 1.0850
You set STOP LOSS at 1.0840 (10 pips below entry)
→ If price drops to 1.0840, your trade closes automatically
→ You lose $1 on 0.01 lot (10 pips × $0.10)
→ Your account is protected
```

**For a short position:**
```
You SELL USD/CAD at 1.3650
You set STOP LOSS at 1.3665 (15 pips above entry)
→ If price rises to 1.3665, your trade closes automatically
```

**Stop Loss Placement Rules:**
- Place behind structure (below support for longs, above resistance for shorts)
- Place beyond the recent swing high/low
- Place where your trade idea is INVALIDATED
- Never move your stop loss further away from entry

**Prop firm rules:**
- FTMO: stop loss required on every trade
- Funding Pips: stop loss required
- Apex: trailing drawdown acts as automatic stop

**NEVER trade without a stop loss. Ever. Not once.**

---

## 4. Take Profit (Exit — Lock In Gains)

**What it is:** An order that CLOSES your trade when price reaches your profit target.

**When to use:** Every trade. You set both SL and TP before entering.

**How it works:**
```
You BUY EUR/USD at 1.0850
Stop Loss: 1.0840 (10 pips risk)
Take Profit: 1.0880 (30 pips reward)
R:R = 1:3

→ If price hits 1.0880, trade closes automatically
→ You book $3 profit on 0.01 lot
```

**Pros:**
- Removes emotion — you don't need to decide when to exit
- Ensures you actually take profits (greed kills)
- Set-and-forget execution

**Cons:**
- Price may reverse just before your TP
- Sometimes you leave money on the table

**Pro tip:** You can partially close — take half off at first TP, let the rest run with a trailing stop.

**Prop firms:**
- FTMO: no specific TP rule, but having one is mandatory for discipline
- MFF: same
- Apex: use trailing stop instead of fixed TP

---

## 5. Trailing Stop (Dynamic Exit)

**What it is:** A stop loss that automatically moves in your favor as price moves in your favor.

**When to use:** You're in a trending market. You want to let winners run but protect gains.

**How it works:**
```
You BUY EUR/USD at 1.0850
Initial Stop Loss: 1.0840 (10 pips)
Trailing Stop: 10 pips behind current price

Price moves to 1.0860 → Stop moves to 1.0850 (break even)
Price moves to 1.0870 → Stop moves to 1.0860 (locked in +10 pips)
Price moves to 1.0880 → Stop moves to 1.0870 (locked in +20 pips)
Price reverses to 1.0870 → Trade closes, you profit +20 pips
```

**Pros:**
- Lets winners run
- Automatically locks in profits
- No need to manually adjust your stop

**Cons:**
- Can close you out on normal pullbacks in a trend
- Tighter trailing = more likely to get stopped out early

**MT5 trailing stop:** Right-click your open trade → Trailing Stop → set distance in pips.

**Prop firms:**
- Apex: trailing stop built into the rules ($3,000 trailing on $25K)
- FTMO: you set it manually
- Most evals: use fixed SL, consider trailing for funded phase

---

## Order Type Decision Tree

```
Am I entering NOW or waiting for a level?
├── NOW → Market Order
└── WAITING → Limit Order

Do I have a stop loss?
├── NO → STOP. Go back. Set one.
└── YES → Good. What else do I need?
    ├── Profit target set? → Take Profit
    ├── Want to let it run? → Trailing Stop
    └── Neither? → At minimum, have the SL.
```

---

## Order Combination Example

```
You BUY EUR/USD at 1.0850 (Market Order)
Stop Loss: 1.0840 (10 pips, $1 risk on 0.01 lot)
Take Profit: 1.0880 (30 pips, $3 reward on 0.01 lot)
R:R: 1:3

Total risk: 0.2% of account ($1 on $500 demo)
Potential reward: 0.6% of account ($3 on $500 demo)
```

This is how every trade should look. Entry. SL. TP. Before you click anything.

---

## Quick Reference Card

```
MARKET ORDER    = buy/sell now at current price
LIMIT ORDER     = buy below / sell above (pending, better price)
STOP LOSS       = auto-close if price moves against you (ALWAYS USE)
TAKE PROFIT     = auto-close when price hits your target
TRAILING STOP   = stop loss that moves with price
```

---

*Open MT5. Place a demo market order on EUR/USD with a stop loss and take profit. Then place a limit order 10 pips below current price with SL and TP. Get comfortable with both.*
