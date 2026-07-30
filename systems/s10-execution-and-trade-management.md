# s10 — Execution and Trade Management

## Part 1: Entry Types — Market Orders vs. Limit Orders

### Market Order
You buy at the current ask price (or sell at the current bid). Immediate execution.

| Pros | Cons |
|------|------|
| Guaranteed entry | Worst price in the moment (pay spread) |
| No slippage (in liquid markets) | Slippage in low-volume markets |
| Simple — click and done | No control over execution price |

**Use market orders when:**
- The setup is time-sensitive (e.g., price is rapidly approaching your level and you fear missing the entry)
- The market is highly liquid (EUR/USD, /ES, /NQ during high volume)
- You're entering at a structural level that's already being tested
- The spread is tight (1-2 pips for FX, 1 tick for futures)

**Don't use market orders when:**
- The market is slow / low volume (spread widens, you'll pay more)
- You're trading illiquid pairs or off-hours
- You're entering a breakout (wait for confirmation first)

### Limit Order
You instruct the broker to buy/sell at a specified price or better. The order sits in the book until filled.

| Pros | Cons |
|------|------|
| Better price (you set the price) | May not get filled |
| No slippage | Miss moves if price doesn't reach your limit |
| Works well at structural levels | Gaps can bypass your limit |

**Use limit orders when:**
- You're trading at a structural level (POC, HVN, previous day high/low)
- The market is pulling back toward your entry zone
- You want to enter with a tight stop and you can wait for the pullback
- You're scaling into a position

### The Rule of Thumb

| Context | Entry Type |
|---------|-----------|
| Sweep + reversal (price already at the level and reversing) | Market order (immediate) |
| Anticipated pullback to a level (price hasn't reached it yet) | Limit order (patient) |
| Breakout above resistance | Market order AFTER confirmed candle close above (not limit — you'll get stopped out) |
| Fading the first touch of a level | Limit order at the level |
| News event | Avoid both — no trade during news |

---

## Part 2: Stop Loss Placement

### Good Stops vs. Bad Stops

| Type | Example | Verdict |
|------|---------|---------|
| **Structural stop** | Below the wick of the sweep candle, below the HVN | Good — real level |
| **Fixed pip stop** | 20-pip stop on EUR/USD with no rationale | Bad — arbitrary |
| **ATR-based stop** | 1.5 × ATR below entry | Acceptable — volatility-adjusted |
| **MAE-based stop** | Where your backtest's worst 10% of trades show the MAE peak | Good — data-driven |
| **Round number** | Stop 5 pips above 1.1000 | Crap — everyone else has it there, hunted easily |

### Where NOT to Put Your Stop

1. **Exactly at the obvious level.** If everyone is looking at 1.1000 support, their stops are at 1.0995. Big money knows this. They will push price to 1.0990 to trigger those stops, then reverse. Your stop should be 10-15 pips below the obvious level (if you're a positional trader) or you should wait for the sweep and then enter (if you're a reversal trader).

2. **Inside the spread.** Don't put your stop 1 pip away from entry. You're giving the market noise room to stop you out.

3. **At a random Fibonacci level.** Unless it's confirmed by volume profile, this is noise.

### Breakeven Stop — When and When Not

**When to move to breakeven:**
- After price reaches +1R (you've paid for the trade — now it's risk-free)
- When the structure changes (e.g., price breaks above a resistance level that was your original target)
- Before a high-impact event that could cause a gap (but consider exiting entirely)

**When NOT to:**
- Immediately after entry (price needs room to breathe — you'll get stopped out on normal noise)
- In a trending market (let the trend run, don't exit prematurely at breakeven)
- When your system doesn't call for it (backtest your target rules — if BE doesn't improve results, don't use it)

---

## Part 3: Trailing Stops

### Methods

| Method | How | Best For |
|--------|-----|----------|
| **Fixed distance** | Trail stop by a fixed amount (e.g., 20 pips below price) | High-volatility swing trends with clear momentum |
| **Parabolic SAR** | Indicators. Not recommended for manual trading — lag too much. | Automated systems |
| **Moving average** | Trail stop at MA (e.g., 20-EMA on 15m chart) | Trend days where price stays above MA |
| **Structure-based** | Trail stop at the last swing low/high | Range days and slower trends |
| **Volatility-based** | Trail stop at 1.5 × ATR below/above price | Adaptive — good for varying volatility |
| **Time stop** | Exit if trade hasn't hit target by a certain time | Lunch-lul trades, fade trades |

### When and How Much to Trail

**Conservative (AVOID early exits):**
- Let price reach +1R first
- Then trail by 0.5R from the highest price reached
- If price goes to +2R, trail by 1R from the highest price

**Aggressive (MAX capture of trend):**
- Trail at 1 × ATR below the highest price reached
- Only good for strong trend days (ADX > 30)
- Will give back more profits but catches massive moves (5-10R)

**For your first 6 months:**
- Let target hit. Don't trail.
- Trailing adds complexity and decision-making overhead.
- Once you're consistently profitable, you can experiment with trailing to enhance returns.

---

## Part 4: Exit Management

### When to Exit Early

| Scenario | Early Exit? | Why |
|----------|------------|-----|
| News event approaching | YES | Gaps can destroy your profit. Take what's there. |
| End-of-session (lunch lull) | YES | The move is over. Take profit or get out. |
| MFE hit 3R+ but target is 4R | NO — unless structure has reversed | Let the trade run to its target. |
| Delta divergence appears while in profit | YES (partial) | Take partial at +2R, trail the rest. |
| Price reversed 50% of your profit | YES | You gave back too much. Be more disciplined with trailing. |

### The "Let It Run" Mentality

Most traders exit too early. They take +1R when the setup was targeting +3R. This is called "leaving money on the table" and it's the #1 destroyer of expectancy.

**The fix:** Backtest your exit rules. If your data shows that 30% of trades hit +3R and the rest hit stop at -1R, your EV is:
(0.30 × 3R) - (0.70 × 1R) = 0.9 - 0.7 = 0.2R per trade EV

If you keep exiting at +1R because "profit is profit":
(0.30 × 1R) - (0.70 × 1R) = 0.3 - 0.7 = -0.4R per trade EV

That's the difference between a profitable system and a loser — just from exit discipline.

---

## Part 5: Execution Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  PRE-ENTRY (verify your plan)                                    │
│  • Check: is the setup aligned with daily bias? (s06)           │
│  • Check: is the level valid? (s07)                             │
│  • Check: position size computed? (s08)                         │
│  • Check: pre-trade record filled? (s09)                        │
│  • Check: state is Calm? (s02)                                  │
│  • Stop placed 10-15 pips below the obvious level               │
│  • Entry type chosen (market or limit)                          │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  ENTRY                                                            │
│  • If market order: click immediately (don't hesitate)          │
│  • If limit order: set it and walk away (let it come to you)    │
│  • Take note of exact entry price and time in journal            │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  IN-TRADE (monitor, don't micro-manage)                          │
│  • Set alert at +1R (consider partial exit)                     │
│  • Set alert at stop level (so you don't forget to check)       │
│  • Don't watch the 1-minute chart. Watch the 5-15 min.          │
│  • If price reaches +1R: consider moving stop to breakeven      │
│  • If structure fully reverses: exit (manual override)          │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  EXIT                                                             │
│  • If target hit: exit (don't get greedy)                       │
│  • If stop hit: exit without hesitation                         │
│  • If time stop (no movement): exit — capital is wasted here    │
│  • Post-trade: fill out journal immediately (while memory fresh) │
└─────────────────────────────────────────────────────────────────┘
```

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s07-order-flow-levels.md` | s07's levels (POC, HVN, LVN) define WHERE to enter. s10's limit/market order decision depends on whether price is AT the level or APPROACHING it. | Choosing entry type by level proximity |
| `systems/s08-advanced-risk-and-position-sizing.md` | s08's scaling in/out plans are executed via s10. s08 plans the "how much," s10 executes "how and when." | Executing a scale-in or scale-out |
| `systems/s05-intraday-market-structure.md` | Session timing affects execution: market orders better in opening drive (slippage acceptable), limits better in lunch lull (patience rewarded). | Adapting execution to session phase |
| `systems/s09-journaling-and-performance-analysis.md` | MFE/MAE data from s09 feeds back into s10's stop placement decision. s10's execution quality is the main input for s09's analysis. | Reviewing exits; adjusting stop placement |
| `systems/s06-top-down-analysis.md` | The exit decision depends on TDA alignment: in a strong trend (s06), let trades run. In a range (s06), take profits early. | Deciding whether to trail or take target |
| `systems/s04-backtesting-and-system-development.md` | Execution rules (market vs. limit, trailing methods, BE rules) should be backtested in s04 before being used live. s10 puts theory into live practice. | Testing entry/exit rules in backtester |
| `systems/s02-trading-psychology.md` | Hesitation at entry, greed at exit, fear of losing profitable trades — all s02 territory. s10 provides the process that overrides emotional interference. | Pre-trade state check; post-trade emotion management |
