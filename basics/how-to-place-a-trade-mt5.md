# How to Place a Trade on MetaTrader 5 (MT5)

## Step-by-Step: From Open Screen to Live Trade

This is the mechanical process. You will do this hundreds of times. Get comfortable with the clicks.

---

## Setup (Do This Once)

### 1. Download and Install MT5
- Go to your broker's website (FTMO, Funding Pips, etc.)
- Download MT5 (Windows, Mac, or mobile)
- Install and open

### 2. Log In to Your Demo Account
- Open MT5
- File → Login to Trade Account
- Enter your account number and password
- Select the correct server (e.g., "FTMO-Demo" or "FundingPips-Demo")
- Click OK

### 3. Set Up Your Workspace
- View → Symbols → Show the pairs you want (EUR/USD, USD/CAD, GBP/USD, USD/JPY)
- Right-click each chart → Properties → set to your preferred colors
- Save your workspace: File → Profiles → Save As

### 4. Add Indicators to Chart
- Navigator panel (Ctrl+N) → Indicators
- Drag VWAP onto chart
- Drag Moving Average → set to period 20, method Exponential
- Drag Moving Average → set to period 50, method Exponential
- Drag Volume onto chart (separate window)
- Save template: right-click chart → Template → Save Template

---

## Placing a Market Order (Buy or Sell Now)

### Step 1: Open the Order Window
- **Method A:** Click the "New Order" button in the toolbar (top of screen)
- **Method B:** Press F9
- **Method C:** Right-click the chart → Trading → New Order
- **Method D:** Single-click the current price on the chart

### Step 2: Select Your Instrument
- In the Symbol field, select your pair (e.g., EURUSD)
- Make sure you're on the right chart (don't accidentally trade the wrong pair)

### Step 3: Set Volume (Lot Size)
- In the Volume field, enter your lot size
- **For prop firms: 0.01 lot** (micro) to start
- MT5 shows volume in lots: 0.01 = micro, 0.10 = mini, 1.00 = standard
- Your pip value will show in the "Tick Value" field at the bottom

### Step 4: Set Stop Loss and Take Profit (BEFORE ENTERING)
- Click the checkbox next to "Stop Loss" → enter your SL price
- Click the checkbox next to "Take Profit" → enter your TP price
- **SL must be below current price for a buy, above for a sell**
- **TP must be above current price for a buy, below for a sell**

### Step 5: Choose Order Type
- Ensure "Type" is set to **"Market Execution"**

### Step 6: Click Buy or Sell
- **BUY (Long):** You profit if price goes UP
- **SELL (Short):** You profit if price goes DOWN
- Click the appropriate button
- A confirmation dialog appears → click OK

### Step 7: Verify Your Trade
- Open the "Trade" tab at the bottom of MT5
- You should see your open position with:
  - Symbol (EURUSD)
  - Volume (0.01)
  - Entry Price
  - Stop Loss
  - Take Profit
  - Current Profit/Loss (fluctuating in real time)

---

## Placing a Limit Order (Pending — Better Price)

### Steps 1-3: Same as Market Order

### Step 4: Change Order Type
- Change "Type" from "Market Execution" to **"Pending Order"**

### Step 5: Select Pending Order Type
- **Buy Limit:** buy BELOW current price
- **Sell Limit:** sell ABOVE current price
- **Buy Stop:** buy ABOVE current price (breakout)
- **Sell Stop:** sell BELOW current price (breakout)

### Step 6: Set Entry Price
- In the "at price" field, enter your desired entry price
- **For Buy Limit:** enter a price BELOW current market price
- **For Sell Limit:** enter a price ABOVE current market price

### Step 7: Set SL and TP
- Same as market order — enter your stop loss and take profit prices

### Step 8: Set Expiry (Optional)
- Check "Expiry" to set a time limit on the pending order
- The order cancels automatically if not filled by the expiry time

### Step 9: Click Place
- The order is now pending — it will fill when price reaches your level
- You'll see it in the "Trade" tab with status "plugged"

---

## Modifying a Trade

### Moving Your Stop Loss or Take Profit
1. Go to the "Trade" tab (bottom of MT5)
2. Right-click your open position
3. Select "Modify or Delete Order"
4. Change the SL or TP price
5. Click "Modify"

**Never move your stop loss FURTHER from entry** (widening your risk). Only move it CLOSER (reducing risk or locking in profit).

### Closing a Trade Manually
1. Go to the "Trade" tab
2. Right-click your position
3. Select "Close Position"
4. Confirm

**Or:** Click the X button next to your position in the Trade tab.

---

## MT5 Keyboard Shortcuts (Memorize These)

| Shortcut | Action |
|----------|--------|
| **F9** | New Order |
| **Ctrl+T** | Toolbox (Trade tab) |
| **Ctrl+N** | Navigator |
| **Ctrl+M** | Market Watch |
| **Ctrl+Y** | Grid |
| **Ctrl+G** | Show/Hide Grid |
| **Spacebar** | Refresh chart |
| **Page Up/Down** | Scroll chart |

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Forgetting to set SL/TP before entering | Set SL/TP in the order window BEFORE clicking Buy/Sell |
| Wrong lot size (1.0 instead of 0.01) | Double-check volume field every single time |
| Wrong instrument (EURUSD instead of USDCAD) | Check symbol name at top of chart |
| Moving stop loss further away | NEVER do this. Only move SL closer or leave it |
| Trading without checking spread | Look at Bid/Ask in Market Watch before entering |
| Placing order on wrong chart timeframe | The trade executes on the CURRENT timeframe, not the chart's TF |

---

## Prop Firm Specific Notes

### FTMO
- Stop loss is required on every trade
- Position size must be reasonable (they review your trading)
- Daily loss limit: 5% of initial balance
- Maximum loss: 10% of initial balance

### Funding Pips
- Similar rules to FTMO
- Stop loss required
- Some accounts allow "no time limit" — trade at your own pace

### TradeDay (Futures — Tradovate/NinjaTrader)
- Uses Tradovate, not MT5
- Different platform, different order flow (see tradovate guide)

---

## Practice Drill

Before going live, do this 10 times on demo:

1. Open MT5
2. Press F9
3. Select EUR/USD
4. Set volume to 0.01
5. Set SL 10 pips below current price
6. Set TP 15 pips above current price
7. Click BUY
8. Verify in Trade tab
9. Right-click → Close Position (after 5 minutes, regardless of P&L)
10. Journal the trade

Repeat 10 times. The clicks should be automatic by then.

---

*Open MT5 right now. Place a demo trade. EUR/USD, 0.01 lot, 10 pip SL, 15 pip TP. Close it after 5 minutes. You just placed your first trade.*
