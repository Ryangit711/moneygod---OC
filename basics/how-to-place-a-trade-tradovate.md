# How to Place a Trade on Tradovate (Futures)

## Step-by-Step: From Open Screen to Live Futures Trade

Tradovate is the platform used by MyFundedFutures, TradeDay, Apex (optional), and Tradeify. It's different from MT5 — futures trade on CME, not OTC.

---

## Key Differences: Tradovate vs MT5

| Feature | MT5 (Forex) | Tradovate (Futures) |
|---------|-------------|---------------------|
| Market | OTC (over-the-counter) | CME (centralized exchange) |
| Instrument | EUR/USD, USD/CAD | /ES, /NQ, /MES, /MNQ |
| Lot sizing | 0.01, 0.10, 1.00 | 1 contract, 2 contracts, etc. |
| Spreads | Variable (broker-dependent) | Tight (exchange-competitive) |
| Commissions | Usually built into spread | Explicit per contract |
| Trading hours | 24/5 | CME hours (Sun 5 PM – Fri 4 PM CT) |
| Stop loss | Set in order window | Set in order window |

---

## Setup (Do This Once)

### 1. Get a Tradovate Account
- Sign up through your prop firm (MFF, TradeDay, etc.)
- You'll get login credentials via email
- Go to `app.tradovate.com` in your browser

### 2. Log In
- Open `app.tradovate.com`
- Enter username and password
- Select your account (demo or live)

### 3. Familiarize Yourself with the Interface
```
┌─────────────────────────────────────────────┐
│  Top Bar: Account info, balance, margin      │
├──────────┬──────────────────────┬────────────┤
│          │                      │            │
│  Watch   │      CHART           │  Order     │
│  List    │                      │  Entry     │
│          │                      │  Panel     │
│          │                      │            │
├──────────┴──────────────────────┴────────────┤
│  Bottom: Positions | Orders | Fills | Account│
└─────────────────────────────────────────────┘
```

- **Watchlist (left):** Your instruments
- **Chart (center):** Price visualization
- **Order Entry (right):** Where you place trades
- **Bottom tabs:** Open positions, pending orders, fill history, account summary

---

## Placing a Market Order (Buy or Sell Now)

### Step 1: Select Your Instrument
- In the Watchlist, find your instrument:
  - **/MES** — Micro E-mini S&P 500 (most popular for beginners)
  - **/MNQ** — Micro E-mini Nasdaq 100
  - **/ES** — E-mini S&P 500 (bigger, more volatile)
  - **/NQ** — E-mini Nasdaq 100
  - **/CL** — Crude Oil
  - **/GC** — Gold
- Click the instrument to load it in the chart and order panel

### Step 2: Set Number of Contracts
- In the Order Entry panel, find the "Qty" field
- Enter **1 contract** (for /MES or /MNQ)
- **For beginners: use micro contracts only** (/MES or /MNQ)

### Step 3: Choose Order Type
- Ensure "Order Type" is set to **"Market"**
- This fills immediately at the best available price

### Step 4: Set Stop Loss
- In the Order Entry panel, find "Stop" or "Stop Loss"
- Check the box to enable
- Enter your stop price:
  - **For a LONG (buy) trade:** enter a price BELOW current price
  - **For a SHORT (sell) trade:** enter a price ABOVE current price
- Example: If /MES is at 5,450.00, and you want 10 points risk → Stop at 5,440.00

### Step 5: Set Take Profit
- Find "Limit" or "Take Profit"
- Check the box to enable
- Enter your target price:
  - **For a LONG trade:** enter a price ABOVE current price
  - **For a SHORT trade:** enter a price BELOW current price
- Example: If /MES is at 5,450.00, and you want 20 points reward → Limit at 5,470.00

### Step 6: Click Buy or Sell
- **BUY (Long):** Click the "Buy" button → you profit if price goes UP
- **SELL (Short):** Click the "Sell" button → you profit if price goes DOWN
- A confirmation dialog appears → confirm

### Step 7: Verify Your Position
- Look at the "Positions" tab at the bottom
- You should see:
  - Instrument (/MES)
  - Quantity (1)
  - Entry Price
  - Current Price
  - Unrealized P&L (fluctuating)

---

## Placing a Limit Order (Pending)

### Steps 1-2: Same as Market Order

### Step 3: Change Order Type
- Change "Order Type" from "Market" to **"Limit"**

### Step 4: Set Limit Price
- Enter the price you want to buy at (for a long limit order, this must be BELOW current price)
- For a short limit order, enter a price ABOVE current price

### Step 5: Set SL and TP
- Same as market order — enter stop loss and take profit prices

### Step 6: Click Buy or Sell
- The order is now pending
- It will fill when price reaches your limit level
- You'll see it in the "Orders" tab with status "Working"

---

## Futures-Specific Concepts

### Point Value (Not Pip Value)
Futures use **points**, not pips:
- /MES: 1 point = $5 per contract (tick size = 0.25 points = $1.25)
- /MNQ: 1 point = $2 per contract (tick size = 0.25 points = $0.50)
- /ES: 1 point = $50 per contract (tick size = 0.25 points = $12.50)
- /NQ: 1 point = $20 per contract (tick size = 0.25 points = $5.00)

**Example:**
```
Buy 1 /MES at 5,450.00
Price moves to 5,460.00 (10 points)
Profit = 10 × $5 = $50

Price drops to 5,440.00 (10 points)
Loss = 10 × $5 = $50
```

### Margin
- /MES: ~$1,320 maintenance margin per contract
- /MNQ: ~$1,870 maintenance margin per contract
- Prop firms provide simulated margin — you don't need real capital

### Trading Hours
- CME opens Sunday 5:00 PM CT (6:00 PM ET, 3:00 PM PT)
- Closes Friday 4:00 PM CT (5:00 PM ET, 2:00 PM PT)
- Closed Saturday
- **Best hours:** 9:30 AM – 11:30 AM ET (6:30 AM – 8:30 AM PT) — NY open
- **Also good:** 2:00 PM – 4:00 PM ET (11:00 AM – 1:00 PM PT) — power hour

### Rollover
- Futures contracts expire (usually quarterly)
- /MES March → /MES June → /MES September, etc.
- Prop firms handle rollover automatically
- You just trade the current active contract

---

## Modifying and Closing Trades

### Modifying Stop Loss or Take Profit
1. Go to "Orders" tab
2. Find your working order
3. Click "Modify"
4. Change the price
5. Click "Submit"

### Closing a Position Manually
1. Go to "Positions" tab
2. Find your open position
3. Click "Close" (or the X button)
4. Confirm

**Or:** Place an opposite order (if you're long, sell to close).

---

## Tradovate Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Buy Market** | Click "Buy" in order panel |
| **Sell Market** | Click "Sell" in order panel |
| **Ctrl+Click on chart** | Place limit order at that price |
| **Alt+Click on chart** | Place stop order at that price |

---

## Practice Drill

Before going live, do this 10 times on Tradovate demo:

1. Open `app.tradovate.com`
2. Select /MES from the watchlist
3. Set quantity to 1
4. Set stop loss 10 points below current price (for long)
5. Set take profit 15 points above current price (for long)
6. Click BUY (market order)
7. Verify in Positions tab
8. Watch for 5 minutes
9. Close the position
10. Journal: entry, exit, P&L, what you learned

Repeat 10 times. You should be clicking through the interface without hesitation.

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Confusing point value with dollar value | /MES 10 points = $50, not $10. Know your contract specs |
| Trading during low-liquidity hours | Avoid 4 PM – 6 PM CT (closes/opens) — spreads widen |
| Forgetting contract rollover | Check active contract month — your prop firm usually tells you |
| Using /ES instead of /MES | /ES is 10× bigger — start with /MES or /MNQ |
| Not setting stop loss | Futures move FAST — always set SL before entering |
| Overleveraging with multiple contracts | Start with 1 contract. Add contracts only after consistent profits |

---

*Open Tradovate right now. Place a demo trade. /MES, 1 contract, 10 point SL, 15 point TP. Close it after 5 minutes. You just placed your first futures trade.*

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `trading/mes-mnq-playbook.md` | Tradovate is the execution interface for the /MES + /MNQ strategies | Placing /MES or /MNQ trade |
| `basics/how-to-place-a-trade-mt5.md` | Parallel mechanics: MT5 lots ↔ Tradovate contracts, SL/TP entry identical | Comparing forex to futures |
| `trading/prop-firm-architecture.md` | Tradovate login credentials and account rules are defined by the prop firm | Setting up prop firm account |
| `quickstart/pip-calculator.md` | Futures point value ($5 for /MES, $2 for /MNQ) replaces pip calculations | Calculating futures risk |
| `systems/position-sizing-by-flow.md` | Number of contracts entered in Tradovate is sized by flow regime | Entering contract quantity |
