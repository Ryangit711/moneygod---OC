# PLATFORM SETUP — MT5 + TRADINGVIEW
## Your workspace: install, configure, place first trade

---

## TOOLS YOU NEED

| Tool | Purpose | Download |
|------|---------|----------|
| **TradingView** | Charting, analysis, alerts, paper trade | tradingview.com (web, no install needed) |
| **MetaTrader 5 (MT5)** | Forex/CFD execution via broker | metatrader5.com or broker's site |
| **MT5 Demo Account** | Practice with virtual money | Get from broker or prop firm site |

---

## TRADINGVIEW SETUP (Do This First)

### 1. Create Free Account
- Go to tradingview.com → Sign up (email/Google)
- Free tier is sufficient for basic charting

### 2. Set Up Your Workspace
- **Layout:** SuperD1 layout (Single chart, large)
- **Indicators to add:**
  - Volume (built-in)
  - EMA 9 and 21 (or SMA 20, 50, 200)
- **Remove everything else.** Clean chart = clear mind.

### 3. Set Your Watchlist
```
USD/CAD     — your home pair
EUR/USD     — most traded pair
GBP/USD     — London sentiment
AUD/USD     — China proxy
USD/JPY     — carry trade
WTI Crude   — drives CAD
Gold (XAU/USD) — safe haven
```

### 4. Set Alerts
- Right-click on chart → "Add Alert"
- Set alerts at key levels (support/resistance, round numbers)
- Get notified on your phone for free

### 5. Paper Trade on TradingView
- Click "Paper Trading" button (bottom of chart)
- $100,000 virtual balance
- Practice placing trades, setting stops, taking profits

---

## MT5 SETUP

### 1. Install MT5
- Go to your broker's website (or metatrader5.com)
- Download MT5 for desktop
- Install (Windows/Mac)

### 2. Get Demo Account
- Open MT5 → File → Open Account
- Select your broker (or search for "Goat Funded Trader Demo")
- Account type: Demo
- Fill in your details → Get free demo with $10,000-$100,000 virtual

### 3. Configure MT5 for Trading
- View → Market Watch (Ctrl+M) — shows all pairs
- View → Navigator (Ctrl+N) — shows your accounts, indicators
- Charts → New Chart (Ctrl+N) — open a new chart

### 4. Set Your Defaults
- Tools → Options → Charts:
  - "Show grid" — OFF (cleaner chart)
  - "Show OHLC" — ON
  - "One click trading" — ON (fast execution)
- Tools → Options → Trade:
  - "Show confirmation" — ON (double-check before placing)
  - "Max deviation" — 10 pips (slippage protection)

---

## YOUR FIRST TRADE (On Demo)

### Step 1: Choose a pair → USD/CAD
- Find USD/CAD in Market Watch
- Drag it to a chart

### Step 2: Identify the direction
- Is price making higher highs? → Look to buy (Long)
- Is price making lower lows? → Look to sell (Short)
- Not sure? → Don't trade. Wait.

### Step 3: Place a Market Order

**To Buy (Long):**
```
1. Click "New Order" (F9)
2. Type: Market Execution
3. Volume: 0.01 (micro lot = 1,000 units)
4. Place Buy
5. Set Stop Loss: below recent low OR 20 pips below entry
6. Set Take Profit: 20-30 pips above entry (1:1 or 1:2 RR)
7. Confirm
```

**To Sell (Short):**
```
1. Click "New Order" (F9)
2. Type: Market Execution
3. Volume: 0.01 (micro lot)
4. Place Sell
5. Set Stop Loss: above recent high OR 20 pips above entry
6. Set Take Profit: 20-30 pips below entry (1:1 or 1:2 RR)
7. Confirm
```

### Step 4: Manage the Trade
- Do NOT move your stop loss further away (widen)
- DO move stop to breakeven once price moves 1R in your favor
- Let the trade run to your take profit

### Step 5: Close the Trade
- Right-click on trade in "Trade" tab → Close Order
- Or set Take Profit to auto-close

---

## ORDER TYPES CHEAT SHEET

| Order Type | When to Use |
|-----------|-------------|
| **Market Order** | Enter RIGHT NOW at current price |
| **Limit Order** | Enter at a SPECIFIC BETTER price (below current for buy, above for sell) |
| **Stop Order** | Enter at a SPECIFIC WORSE price (above for buy, below for sell) — used for breakouts |
| **Stop Loss** | Get out at a specific bad price — always set this |
| **Take Profit** | Get out at a specific good price — always set this |
| **OCO (One Cancels Other)** | Two orders, one fills, other cancels — used for breakouts |
| **Trailing Stop** | Stop that moves with price — locks in profit |

---

## YOUR DAILY SETUP CHECKLIST

```
BEFORE ANY TRADE:
  [ ] Do I know the direction? (bias from global flow check)
  [ ] Did I set a stop loss? (always)
  [ ] Did I set a take profit? (always)
  [ ] Is this 0.01 lot size? (micro, always for now)
  [ ] Can I articulate: "I'm trading because [reason]"
```

---

## COMMON MISTAKES (Avoid These)

| Mistake | Why It's Bad | Fix |
|---------|-------------|-----|
| **No stop loss** | One bad move can wipe your account | Always set SL |
| **Too big size** | 1 lot = $10/pip move = too much for demo | Use 0.01 micro lots |
| **Chasing price** | Buy at the top, sell at the bottom | Wait for pullback |
| **Overtrading** | 10 bad trades > 1 good trade | Max 2-3 trades/day |
| **Ignoring time** | Trading during low liquidity | Only trade NY session (5am-2pm PT) |
| **No journal** | Can't learn without records | Log every trade |

---

## NEXT STEPS

```
Day 1: Set up TradingView + MT5 demo
Day 2: Place 1-2 demo trades using this guide
Day 3: Read 03-demo-path.md for your 30-day plan
```

---

## REFERENCES

- [01-broker-canada.md] — Open your accounts first
- [03-demo-path.md] — 30-day demo plan
- [first-setup-orb.md] — Your first real strategy
- [pip-calculator.md] — Pip values and position sizing
