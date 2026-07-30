# s03 — Volume Profile and Order Flow

## The Missing Microstructure Layer

This file fills the single biggest gap in the repo. The existing
plumbing-hierarchy-master.md (3,307 lines) is strong on macro but
silent on tape reading. The 06-day-trading-tap-the-flow.md file
references "liquidity sweeps" and "absorption" but never explains
the volume/delta mechanics behind them. This file does.

---

## Part 1: The Hierarchy of Price Discovery

### Every Market Is an Auction

Price moves because buyers and sellers cannot agree on value at
the current price. The auction moves price until buyers and
sellers ARE matched.

**Auction theory rules:**
- Price moves UP when buyers are more aggressive (willing to pay higher ask)
- Price moves DOWN when sellers are more aggressive (willing to accept lower bid)
- Price stays FLAT when buyers and sellers are balanced
- Volume tells you WHICH scenario is happening (trend vs. balance)

### The Two Phases of Every Auction

1. **Trend phase:** Price moves in one direction as one side
   (buyers or sellers) is clearly dominant. Volume is typically
   ABOVE average during trend phases.
2. **Balance phase:** Price oscillates in a range as buyers and
   sellers are evenly matched. The edges of the range are where
   the auction "fails" — one side rejects price at that level.

### Timeframes of the Auction

| Timeframe | What's Being Auctioned |
|-----------|----------------------|
| Monthly | Long-term institutional positioning |
| Weekly | Swing-level positioning |
| Daily | Day traders + intraday institions |
| 1H | Session-level positioning |
| 15m | The driver of intraday direction |
| 5m | Where most retail traders get chopped |
| 1m | Pure HFT/algo noise — do NOT trade off this |

**Heuristic:** The 5m and 1m charts are where retail gets bled.
The 1H and 15m charts are where intraday decisions are made.
The daily and weekly charts set the bias. Match your timeframe
to the auction you're trying to read.

---

## Part 2: Volume Profile — The Map of Where Price Spends Time

### What Volume Profile Shows

Volume profile is NOT the same as the volume bars at the bottom
of your chart. Those show volume PER TIME. Volume profile shows
volume PER PRICE — vertical histogram on the right of the chart.

### The Components

```
                    ┃▓▓  ←  Value Area High (VAH) — top of 70% range
                    ┃▓▓▓▓
                    ┃▓▓▓▓▓▓
                    ┃▓▓▓▓▓▓▓▓ ← Point of Control (POC) — highest volume price
                    ┃▓▓▓▓▓▓
                    ┃▓▓▓▓
                    ┃▓▓ ←  Value Area Low (VAL) — bottom of 70% range
```

- **POC (Point of Control):** The price with the most volume in
  the profile. Price gravitates back to POC like a magnet.
- **Value Area (VA):** The price range where 70% of volume traded.
  VAH (high) and VAL (low) form the edges.
- **High-Volume Nodes (HVNs):** Prices with abnormally high volume
  — institutional interest. These act as **support/resistance**.
- **Low-Volume Nodes (LVNs):** Prices with abnormally low volume
  — price moves through these quickly (no interest). LVNs act as
  **magnets** — price is uncomfortable spending time there.

### How to Read Profile

| Pattern | Interpretation | Trade Response |
|---------|----------------|-----------------|
| Price is in Value Area | Balanced auction. Both sides comfortable here. | Range-trade the edges. Buy VAL, sell VAH. |
| Price breaks above VAH with volume | Buyers stepping up. Trend up probable. | Long break, target = next HVN above. |
| Price breaks below VAL with volume | Sellers stepping down. Trend down probable. | Short break, target = next HVN below. |
| Price at POC | Equilibrium. Both sides matched. | Don't trade. Wait for a break either way. |
| Price in LVN | Auction moving. No agreement yet. | Don't trade. Wait for it to settle at an HVN. |
| Price rejects an extreme and returns to VA | Failed auction. Range continues. | Fade the extreme. Target POC. |

### Free Tool for Volume Profile

- **TradingView (free tier):** Has "Fixed Range Volume Profile"
  — drag it across any chart, shows the profile for that range
- **TradingView (paid tier):** "Session Volume Profile" — auto-draws
  for each session
- **Sierra Chart / Quantower:** Paid platforms with full footprint charts
  (recommended once you're funded)

---

## Part 3: Delta and Cumulative Delta — Buying vs. Selling Pressure

### What Delta Is

Delta = (Volume of market buys) − (Volume of market sells)

A single candle has positive delta if buyers were more aggressive
(more market buy orders hit the ask) than sellers (market sell
orders hit the bid).

Cumulative Delta = the running sum of delta across all candles
in the session. Shows you who is in control: net buyers or net sellers.

### Delta Divergence — The Strongest Signal in Microstructure

**The setup:**
- Price makes a new high (or higher high)
- Cumulative delta does NOT confirm — it is flat or falling
- This means: price is rising on thin buying. Sellers are absorbing
  the buyers. The move is weak.

**Trade rule:**
- If price breaks above an obvious resistance level (HVN or session high)
  BUT the cumulative delta is flat OR falling → SHORT the retest
  of the broken level.
- Stop: just above the breakout high
- Target: POC or the nearest HVN below
- Probability of success: ~60-65% inMES/NQ intraday

### The Reverse: Confirmation

If price breaks out AND delta confirms (rising strongly):
- The breakout is REAL — institutional buyers are pushing
- Long the retest with confidence
- Target: 2R or the next HVN above

### Realistic Free Tools

- **Jigsaw Daytradr:** Paid, ~$250 lifetime, pro tools
- **NinjaTrader + free volume indicator:** Covers delta basics
- **TradingView "Volume Profile Visible Range" (free):** Limited,
  but lets you see profile
- **Quantower:** Has free trial, full footprint

Don't wait until you have a paid tool. Use TradingView's free
volume profile to start. The patterns are the same — only the
precision differs.

---

## Part 4: Order Flow Basics — Market Orders, Limit Orders, Icebergs

### Market Orders (Aggressive)

A market buy order = "I want to buy NOW and pay whatever the ask is."
A market sell order = "I want to sell NOW and accept whatever the bid is."

Market orders take liquidity. They move price. When a flood of
market buys hit, the ask gets lifted (price rises fast).

### Limit Orders (Passive)

A limit buy at $100 = "I want to buy at $100 or better." The order
sits in the book at $100. If price drops to $100, the order fills.

Limit orders PROVIDE liquidity. They form the bid-ask spread.
But limit orders DO NOT move price — they wait for price to come.

### Iceberg Orders

An iceberg is a large limit order that shows only a small portion
of its size. When the visible portion is filled, more is revealed.

- Why icebergs exist: large institutions want to hide their interest
  so they don't push price away from their target entry.
- How to spot them: the same price level absorbs multiple small fills
  without breaking. Price seems "stuck" on a level for many candles.
- Why you care: the "sticky" level is institutional absorption. A
  breakout attempt at that level will likely fail.

### Stop-Run Mechanics (Re_actual microstructure, not just ICT theory)

A 'liquidity sweep' (ICT concept) is concrete at the book level:

1. There is a known level (e.g., yesterday's low)
2. Stop-loss orders from longs sit just below it (sell stops)
3. An aggressive buyer pushes price down to that level
4. The sell stops trigger → market sell orders flood the book
5. Price wicks below the level momentarily
6. The aggressive buyer absorbs all those sell orders at cheap prices
7. Price snaps back up — the buyer now has a large long position at a discount

**Reading this on the chart:**
- Wicks below a key level that snap back within 1-3 candles
- High delta at the wick (buying absorbed the selling)
- Population stops got run

---

## Part 5: Footprint Charts — What Each Candle Reveals

### The Footprint View

A footprint chart shows volume at EACH PRICE LEVEL inside a single
candle. You see WHO is winning inside the candle, not just that the
candle was green or red.

```
Footprint of a 5-min candle on /ES:
                        BID     ASK      Δ
5400.25  ┃              120  :  85    → +35   ↑ buyers control top
5400.50  ┃              180  :  240   → -60
5400.75  ┃              250  :  320   → -70
5401.00  ┃              90   :  150   → +60   ↑ absorption at highs
5401.25  ┃              200  :  180   → +20
                       (close)
```

### Reading Footprint

| Pattern | What It Means | Trade |
|---------|--------------|-------|
| **Imbalance at the high** (more buys than sells at the top of the candle) | Buyers confidently holding the high. Move likely continues up. | Long bias |
| **Imbalance at the low** (more sells than buys at the bottom) | Sellers confidently pressing lows. Move likely continues down. | Short bias |
| **Absorption** (large volume at a price that doesn't break) | A big limit order soaking up the aggression. The breaking side is failing. | Fade the breakout |
| **Stacked imbalances** (3+ consecutive prices with same-side imbalance) | Strong directional pressure. Trend continuation likely. | Trade with the imbalance |
| **Delta reversal** (positive delta then negative delta in the same candle) | Control shifted mid-candle. Reversal at the close probable. | Fade the open direction |

### Free Practical Use

Footprint charts typically require paid platforms ($50-150/month).
You can simulate this conceptually with free tools:
- Watch volume-at-price in TradingView's volume profile
- Watch delta via free NinjaTrader indicators
- Compare candle wicks to identify absorption: long wick at a
  "should break" level + the next candle reverses = absorption

Don't get stuck waiting for paid tools. Train your eye with what's
free, then upgrade only when funded.

---

## Part 6: Integration with the Existing ICT Framework

The repo already references ICT concepts (liquidity sweep, fair
value gap, order block) in plumbing-hierarchy-master.md Part 9.2
and 06-day-trading-tap-the-flow.md. Here's how volume profile and
order flow map to those concepts:

| ICT Concept | Volume Profile / Order Flow Translation |
|-------------|---------------------------------------|
| **Liquidity void** | An LVN (Low-Volume Node). Price moved through this zone fast, leaving no footprint. It usually gets re-visited and filled. |
| **Order block** | An HVN (High-Volume Node) where an institutional player accumulated a position. Price returns to this level because the institution defends it. |
| **Fair Value Gap (FVG)** | The low-volume "void" left between two candles in a strong move. Volume profile shows the void as a thin zone between two HVN clusters. |
| **Liquidity grab / sweep** | A wick below an HVN that triggers stops. Confirmation via positive delta at the wick (buying absorbed the stop-triggered selling). |
| **Displacement** | A high-volume candle with strong stacked imbalance. In footprint, multiple prices show same-side control. |
| **Premium / Discount** | Above POC = premium (expensive, expecting reversion). Below POC = discount (cheap, expecting rally back to POC). |
| **Change of Character (CHoCH)** | A break of the session's structural high/low WITH a delta flip. (Price broke AND control shifted.) Without delta confirmation, it's a fakeout. |
| **Optimal Trade Entry (OTE)** | A retracement to the value area edge (VAH or VAL) within a trend direction. The 62-79% OTE zone maps roughly to a key HVN within the trend. |

### Practical Workflow (combining ICT + volume)

1. **Daily check:** Where are the daily HVN levels above and below current price? These are your "key levels."
2. **Session open:** Mark the OR high/low. Wait for a break.
3. **Breakout:** Check delta on the break. If delta confirms → continuation. If delta diverges → fade.
4. **Retracement:** Price comes back to the broken level. Is it holding as support/resistance? Check delta again — are buyers/sellers defending?
5. **Entry:** At the level, with stop below/above the wick that tests the level. Target the next HVN.

This is the full execution loop tying s03 microstructure to the existing ICT framework in the repo.

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `06-day-trading-tap-the-flow.md` | The existing file references "5 esoteric principles" (liquidity, footprint, divergence, absorption, exhaustion) but never defines them mechanically. s03 provides the mechanical definitions; 06 provides the strategic context. Read together. | Reading 06 and hitting a concept that felt vague |
| `systems/s05-intraday-market-structure.md` | s05 shows WHERE the volume appears in the day (sessions, opening drive). s03 shows WHAT that volume means (profile, delta, footprint). Read together when planning an intraday session. | Planning an intraday session |
| `systems/s04-backtesting-and-system-development.md` | Every backtest should record volume profile context: was the setup at an HVN or LVN? Was delta confirming or diverging? Without s03 patterns logged in your backtest, you can't separate A-grade from B-grade setups. | Building a backtest; tagging setups by quality |
| `trading/mes-mnq-playbook.md` AND `trading/complete-strategy-orb-eurusd.md` | Both playbooks should be re-read after s03. The MES/MNQ ORB and the FX London breakout both have volume-profile variants — confirmation via delta makes them A-grade. Otherwise they're B-grade. | Refining entry quality on existing strategies |
| `plumbing-hierarchy-master.md` Part 9.2 (ICT Concepts) | Part 9.2 lists ICT concepts as one-liners. s03 provides the FULL microstructure explanation for each. The hierarchy-master brief mentions, s03 elaborates. | Wanting the "why" behind each ICT concept |
| `systems/s10-institutional-plumbing-and-eurodollar.md` | s10 covers MACRO institutional flow (Eurodollar, repo). s03 covers MICRO institutional flow (footprint, delta, absorption). Both together = complete institutional literacy. | Studying how institutions actually trade |
| `systems/s13-options-mechanics-for-futures-traders.md` | Options dealer hedging is itself an order flow event (gamma-driven buying/selling). s13 explains the WHY; s03 explains the HOW (it shows up in delta). | Studying gamma/0DTE movements |
