# THE MASTER SYLLABUS — Day by Day, ABC to First Funded Trade

## "From 'What is money?' to 'I am a funded trader.' 20 weeks. Zero assumptions."

---

## ORIENTATION COMPLETE. CLASS STARTS TOMORROW.

---

## THE STRUCTURE

```
PRE-NURSERY (Weeks 1-3)     ← ABC mode. What money is. What a pip is.
NURSERY (Weeks 4-5)         ← Chart literacy. The machine's hidden layer.
PRIMARY (Weeks 6-17)        ← Demo trades. Patterns. Integration. Bridge.
GRADUATION (Weeks 18-20)    ← Eval. Funded. Repeat.
```

---

## GAP ANALYSIS — What Was Missing Before This Syllabus

| Gap | Severity | What's Missing |
|-----|----------|---------------|
| **No "What is a pip?" file** | CRITICAL | Every file uses "pip" but nowhere is it defined for a total beginner. Same for lot, spread, leverage, margin, drawdown, R:R. |
| **No candlestick explanation** | CRITICAL | The 12-week syllabus assumes you know what a candlestick is. Week 1 talks about "close back inside range" — but what IS a close? What IS a wick? |
| **No order types file** | CRITICAL | Market order, limit order, stop loss, take profit — used everywhere, never explained. |
| **No "how to place a trade on MT5"** | CRITICAL | CURRICULUM.md Day 40 says "place your first demo trade" — but doesn't show the clicks. |
| **No "how to place a trade on Tradovate"** | HIGH | Same for futures. |
| **No VWAP/EMA/Volume explanation** | HIGH | Used in chart templates but never defined. |
| **CURRICULUM.md and 12-week syllabus overlap** | MEDIUM | Both cover similar ground but don't align. One says "Phase 0 Week 1," the other says "Week 0 Foundation Source Read." |
| **No "what happens when you click buy"** | HIGH | The mechanics of order routing, fill, P&L calculation — never explained. |

**Bottom line:** The repo was built for someone who already knows what a pip is. A true beginner (ABC mode) hits a wall on Day 1. This syllabus fixes that.

---

## NEW FILES NEEDED (6 files, all under 100 lines, pure basics)

| New File | What It Covers | Phase |
|----------|---------------|-------|
| **`basics/what-is-a-pip.md`** | Pip, lot, spread, leverage, margin, drawdown, R:R — all defined with examples | Pre-Nursery W2 |
| **`basics/candlestick-anatomy.md`** | What is a candlestick? Body, wick, open, close, high, low. Green vs red. Timeframes. | Pre-Nursery W2 |
| **`basics/order-types.md`** | Market order, limit order, stop loss, take profit, trailing stop. When to use each. | Nursery W4 |
| **`basics/how-to-place-a-trade-mt5.md`** | Step-by-step: open MT5 → select instrument → set lot size → click buy/sell → set SL/TP. | Primary W7 |
| **`basics/how-to-place-a-trade-tradovate.md`** | Same for Tradovate (futures). | Primary W7 |
| **`basics/what-is-vwap-ema-volume.md`** | VWAP, EMA, volume — what they are, why they matter, how to read them. | Nursery W4 |

---

---

# PRE-NURSERY — WEEK 1: "What IS Money?"

*You've heard the word your whole life. You've never thought about what it actually is.*

| Day | Read | Do | Time |
|-----|------|-----|------|
| **1** | `01-origins-of-money-and-debt.md` | Write in journal: "Money is not what I thought. It is actually _______" | 45 min |
| **2** | `02-the-real-meaning-of-economy.md` | Write: "The economy is not GDP. It is _______" | 45 min |
| **3** | `03-money-as-debt-modern-system.md` | Write: "Banks don't lend money. They _______" | 45 min |
| **4** | `04-what-the-powerful-understand.md` | Write: "The 5 things most people believe that are wrong: _______" | 45 min |
| **5** | `07-what-money-actually-is-no-bs.md` | Write: "My job as a trader is to _______" | 45 min |
| **6** | Re-read all 5 journal entries | Write 1 page: "What I Now Know About Money" — explain to an imaginary friend | 60 min |
| **7** | Watch: Ray Dalio — "How the Economic Machine Works" (YouTube, 30 min) | Write: "How does Dalio's model differ from what I believed?" | 45 min |

**Week 1 Proof Gate:** Can you explain to someone what money is, where it comes from, and why the system needs perpetual growth? YES → proceed. NO → re-read Days 1-5.

---

# PRE-NURSERY — WEEK 2: "What IS a Pip, Lot, Spread, Candle?"

*The vocabulary of trading. Without this, every other file is gibberish.*

| Day | Topic | Read / Watch | Do | Time |
|-----|-------|-------------|-----|------|
| **8** | **What is a currency pair?** | `14-forex-clock-resources.md` (first 30 lines) | Open TradingView. Type "EURUSD". See the price (e.g., 1.0850). Write: "EUR/USD at 1.0850 means _______ USD to buy 1 EUR." | 45 min |
| **9** | **What is a pip?** | `basics/what-is-a-pip.md` + `quickstart/pip-calculator.md` (first 50 lines) | A pip is the 4th decimal place in most pairs. EUR/USD moves from 1.0850 to 1.0851 = 1 pip. Write: "1 pip on EUR/USD at 0.01 lot = $0.10. At 0.1 lot = $1. At 1.0 lot = $10." Calculate pip values for USD/CAD too. | 45 min |
| **10** | **What is a candlestick?** | `basics/candlestick-anatomy.md` | Open TradingView. Switch to "Candles" view. Each candle = 4 prices in a time period. Green/white = price went UP. Red/black = price went DOWN. Body = open-to-close. Wick = high and low. Draw 5 candles on paper. Label: open, close, high, low, body, wick. | 45 min |
| **11** | **What is bid/ask spread?** | `basics/what-is-a-pip.md` (spread section) | Every price has TWO numbers: Bid (what you can sell at) and Ask (what you can buy at). The difference = spread. On EUR/USD: Bid 1.0849, Ask 1.0851 = 2 pip spread. This is your COST of trading. | 30 min |
| **12** | **What is a lot?** | `basics/what-is-a-pip.md` (lot section) + `quickstart/pip-calculator.md` (full) | Standard lot = 100,000 units. Mini = 10,000. Micro = 1,000. Nano = 100. You'll trade micro (0.01 lot) to start. Write the math: "0.01 lot EUR/USD, 10 pip move = $1 profit/loss." | 45 min |
| **13** | **What is leverage?** | `basics/what-is-a-pip.md` (leverage section) | Leverage lets you control $100,000 with $1,000. It multiplies BOTH wins AND losses. 1:100 leverage = $1,000 controls $100,000. Write: "Leverage is a magnifier. It doesn't create money. It creates risk." | 30 min |
| **14** | **Vocabulary test — self quiz** | Write from memory: pip, lot, spread, candle, body, wick, bid, ask, leverage, margin, drawdown, R:R | If you can define all 12 without looking → proceed. If not → re-read the day you're weak on. | 30 min |

**Week 2 Proof Gate:** Can you look at a TradingView chart, see EUR/USD at 1.0850, and explain: what a pip is, what the candle means, what the spread costs, and how much you'd make/lose at 0.01 lot? YES → proceed. NO → repeat the weak day.

---

# PRE-NURSERY — WEEK 3: "How Does Money Actually MOVE?"

*Now you know what money is and what a pip is. Time to see how the machine works.*

| Day | Read | Do | Time |
|-----|------|-----|------|
| **15** | `14-monetary-plumbing-global.md` | Draw the two-layer engine on paper: CB reserves → commercial bank credit. | 45 min |
| **16** | `core/repo-plumbing.md` | Write: "Repo is _______. SOFR tells me _______." | 45 min |
| **17** | `05-how-money-flows-in-the-system.md` | Draw the three-pool model: Banks → Government → Markets. Label the flows. | 45 min |
| **18** | `core/liquidity-equation.md` | Write the formula 10 times: **Net Liq = ΔCB BS − ΔTGA − ΔRRP**. Go to fred.stlouisfed.org. Look up WRESBAL, RRPONTSYD, WTREGEN. Compute today's Net Liq. | 60 min |
| **19** | `core/tri-region-flow-map.md` | Draw the simplified US→CA→EU flow. Mark: where does CAD get its value? (Oil → exports → CAD strength.) | 45 min |
| **20** | `core/global-flow-map.md` (US + Canada sections only) | Find Canada in the transmission table. Write: "When the Fed does X, Canada experiences Y, and my trade should be Z." | 60 min |
| **21** | Re-read `core/liquidity-equation.md` | Compute Net Liq again. Has it changed from Day 18? Write the verdict: NET LIQ IN / NET LIQ OUT / NEUTRAL | 30 min |

**Week 3 Proof Gate:** Can you compute Net Liq from FRED data and say whether liquidity is expanding or contracting? YES → proceed. NO → repeat Days 18-21.

---

# NURSERY — WEEK 4: "The Machine's Hidden Layer + Your First Chart"

*Esoteric plumbing + the moment you first open a chart as an observer.*

| Day | Read / Do | Time |
|-----|-----------|------|
| **22** | `core/plumbing-esoterica.md` Sections 1-3 (Eurodollar, XCCY, FRA-OIS) | Find today's EUR/USD XCCY basis. Is dollar availability normal or stressed? | 60 min |
| **23** | `core/plumbing-esoterica.md` Sections 4-6 (Primary dealers, FX swaps, CCP) | Write: "The FX swap market is _______. It is bigger than _______." | 60 min |
| **24** | `core/plumbing-esoterica.md` Sections 7-12 (CP, IOER, China, BIS, SDR, NBFI) | Write: "The biggest plumbing change happening right now is _______" | 60 min |
| **25** | Open TradingView. Type "EURUSD". Set to 1-hour candles. | **Just watch.** Mark the London open (11 PM PT), NY open (6:30 AM PT). Note: what happens at each open? Write 3 sentences. | 45 min |
| **26** | `14-forex-clock-resources.md` (full) | Draw a timeline of your day (PT). Mark: when can you trade? When are the killzones? Write your available windows. | 30 min |
| **27** | `08-forex-trading-the-purest-flow.md` (sections 1-3) | Open USD/CAD on TradingView. Watch during NY session. Note how it moves. Write: "CAD is _______ when oil is _______" | 45 min |
| **28** | `09-futures-trading-energy-and-receipts.md` | Open `/ES` (S&P 500 futures) on TradingView. Watch the NY open (9:30 AM ET). Write: "First 15 min is _______. Direction shows at _______" | 45 min |

**Week 4 Proof Gate:** Can you look at a chart and say "this is the NY open, this is what typically happens here"? YES → proceed.

---

# NURSERY — WEEK 5: "The Rules + The Rhythm + The Mind"

*Before you place a single trade, you need three things: rules, a daily rhythm, and the right mindset.*

| Day | Read / Do | Time |
|-----|-----------|------|
| **29** | `trading/trading-commandments.md` | Print it. Read it aloud. Pin it next to your screen. This is law from now on. | 15 min |
| **30** | `13-weekly-flow-tapping-operating-system.md` | Run the Monday checklist TODAY (even if it's not Monday). It takes 15 min. | 30 min |
| **31** | `systems/weekly-flow-checklist.md` | Same checklist, different format. Repeat it. | 15 min |
| **32** | `systems/daily-pre-session.md` | Tomorrow morning: do the 5-min pre-session before you open anything. | 15 min |
| **33** | `systems/position-sizing-by-flow.md` | Calculate: if you had a $50K demo, what's your position size for EUR/USD in each liquidity regime? | 45 min |
| **34** | `mental-models/pipe-theory.md` | Write: "Sit in the pipe means _______. Flow > prediction means _______." Read twice. | 45 min |
| **35** | `mental-models/wealth-code-synthesis.md` + `mental-models/10-level-mastery-path.md` | Write: "I am at level _______. My next level requires _______." Then write 1 page: "My Trading Philosophy (Before I've Made a Single Trade)" | 60 min |

**Week 5 Proof Gate:** Can you run the daily pre-session from memory? Can you say "sit in the pipe" and know what it means? YES → proceed to PRIMARY.

---

# PRIMARY — WEEK 6: "Chart Literacy + Demo Setup"

*You know the plumbing. You know the rules. Now learn to read the chart like a book.*

| Day | Read / Do | Time |
|-----|-----------|------|
| **36** | `quickstart/01-broker-canada.md` | Open a Tradovate demo account ($50K simulated). OR FTMO free 14-day demo. | 30 min |
| **37** | `quickstart/02-platform-setup.md` | Set up chart templates: 5-min, 15-min, 1H, 4H, Daily. Add VWAP, 20 EMA, 50 EMA, Volume. Save as workspace. | 45 min |
| **38** | Watch 5-min EUR/USD for 1 hour during NY open | **No trading.** Just watch. Where does price go first? What happens at the open? Write 3 observations. | 60 min |
| **39** | Watch 5-min /MES for 1 hour during NY open | Same. Write: "The difference between forex and futures at the open is _______" | 60 min |
| **40** | `systems/live-data-workflow.md` | Run the full workflow. Compute Net Liq. Get the verdict. Write it down. Don't trade it. | 30 min |
| **41** | `systems/plumbing-to-trade-bridge.md` | Run all 4 decision trees with today's data. Write the output: Trade? Bias? Instrument? Size? | 30 min |
| **42** | `systems/gangotri-protocol.md` | Read the Combined Edge Matrix. Match today's signals. Write your 3-question gate. | 30 min |

**Week 6 Proof Gate:** Can you run the full pre-session workflow (live-data → bridge → gangotri → commandments) in under 20 minutes? YES → proceed.

---

# PRIMARY — WEEK 7: "Your First Demo Trades"

*The moment. You click buy or sell for the first time. On demo. But it's real.*

| Day | Read / Do | Time |
|-----|-----------|------|
| **43** | `quickstart/pip-calculator.md` (full) | Calculate pip values: EUR/USD 0.01 lot, USD/CAD 0.01 lot, MES 1 contract. Know your risk per pip. | 30 min |
| **44** | `trading/complete-strategy-orb-eurusd.md` (full) | Read the ORB strategy. Understand: first 15-30 min = ORB range. Breakout above = long. Breakout below = short. | 45 min |
| **45** | **PLACE YOUR FIRST DEMO TRADE** | EUR/USD, 0.01 lot. Set stop loss (10 pips). Set take profit (15 pips). Enter. Journal it. Screenshot it. | 60 min |
| **46** | Review yesterday's trade | Did you follow the plan? Write: "What I did right: _______. What I'd change: _______." | 30 min |
| **47** | Watch. Wait for ORB setup. | If ORB triggers → take the trade (0.01 lot). If not → watch and journal. Max 1 trade today. | 60 min |
| **48** | `06-day-trading-tap-the-flow.md` (layers + principles) | On a 5-min chart, identify 3 liquidity sweeps and 3 absorptions. Draw them. | 45 min |
| **49** | Weekly review | Count: trades taken, wins, losses, R:R. Write: "My first week of trading: _______" | 30 min |

**Week 7 Proof Gate:** Have you placed at least 2 demo trades? Did you follow your rules on both? YES → proceed.

---

# PRIMARY — WEEKS 8-9: "Foundation Patterns"

*Learn the patterns that institutions leave behind.*

| Day | Concept | Read | Do | Time |
|-----|---------|------|-----|------|
| **50-51** | **Liquidity Sweep** | `plumbing-hierarchy-master.md` Part 9.2 (Liquidity Sweep row) | Find 3 examples on EUR/USD 5-min. Mark: where were the stops? Who swept them? | 60 min × 2 |
| **52-53** | | | Take 2 demo trades on sweeps (0.01 lot). Journal. | 60 min × 2 |
| **54-55** | **Fair Value Gap** | `plumbing-hierarchy-master.md` Part 9.2 (FVG row) | Find 3 FVGs on EUR/USD 15-min. Mark the gap. Watch: does price return to fill it? | 60 min × 2 |
| **56-57** | | | Take 2 demo trades on FVG retracements. Journal. | 60 min × 2 |
| **58-59** | **Displacement** | `plumbing-hierarchy-master.md` Part 9.2 (Displacement row) | Find 3 displacement candles. Mark: the large candle, the FVG it created, the retracement zone. | 60 min × 2 |
| **60-61** | | | Take 2 demo trades on displacement retracements. Journal. | 60 min × 2 |
| **62-63** | **Optimal Trade Entry** | `plumbing-hierarchy-master.md` Part 9.2 (OTE row) | Draw Fibonacci on 3 clean legs. Mark 62-79% zone. Watch: does price respect the zone? | 60 min × 2 |
| **64-65** | | | Take 2 demo trades at OTE zones. Journal. | 60 min × 2 |

**Weeks 8-9 Proof Gate:** 6+ demo trades taken. ≥50% win rate. Can you identify sweeps, FVGs, displacement, and OTE on a live chart? YES → proceed.

---

# PRIMARY — WEEKS 10-11: "Timing & Context"

*When to trade matters as much as what to trade.*

| Day | Concept | Read | Do | Time |
|-----|---------|------|-----|------|
| **66-67** | **Killzone Timing** | `systems/gangotri-protocol.md` (Killzone section) | Trade ONLY within killzones this week. Track: how many setups did you SKIP because they were outside? | 60 min × 2 |
| **68-69** | **Order Blocks** | `plumbing-hierarchy-master.md` Part 9.2 (Order Block row) | Find 3 order blocks on 15-min chart. Mark: consolidation candle → displacement → return to OB. | 60 min × 2 |
| **70-71** | | | Take 2 demo trades at order block boundaries. Journal. | 60 min × 2 |
| **72-73** | **Change of Character** | `plumbing-hierarchy-master.md` Part 9.2 (CHoCH row) | Find 3 CHoCH events. Mark: the structure break, the confirmation candle, the entry. | 60 min × 2 |
| **74-75** | | | Take 2 demo trades on CHoCH. Journal. | 60 min × 2 |
| **76-77** | **Premium/Discount** | `plumbing-hierarchy-master.md` Part 9.2 (Premium/Discount row) | Mark 50% of the day's range. Above = premium (sell). Below = discount (buy). | 60 min × 2 |
| **78-79** | | | Take 2 demo trades from discount/premium. Journal. | 60 min × 2 |

**Weeks 10-11 Proof Gate:** 6+ demo trades. Can you identify killzones, order blocks, CHoCH, and premium/discount on a live chart? YES → proceed.

---

# PRIMARY — WEEKS 12-13: "Synthesis + Integration"

*All the pieces come together. Start running the full system.*

| Day | Concept | Read | Do | Time |
|-----|---------|------|-----|------|
| **80-81** | **Interbank FVG** | `plumbing-hierarchy-master.md` Part 9.2 (IFC row) | Open weekly chart. Find unfilled weekly FVGs. Mark them as targets. | 60 min × 2 |
| **82-83** | **Liquidity Pyramid** | Combine: sweep on daily + 4H + 1H at same level | Find 3 examples of multi-timeframe confluence. | 60 min × 2 |
| **84-85** | **Forward Testing** | Run the full system: workflow → bridge → gangotri → playbook → journal | Take 2 demo trades using ALL pieces. No shortcuts. | 60 min × 2 |
| **86-87** | | Same. | 2 more trades. Journal everything. | 60 min × 2 |
| **88-89** | | Same. | 2 more trades. Total: 6 forward-test trades. | 60 min × 2 |
| **90-91** | Weekly review | Review all 6 forward-test trades. Write: "My system's strengths: _______. Weaknesses: _______." | 60 min × 2 |

**Weeks 12-13 Proof Gate:** 6+ forward-test trades taken with full system. Can you run workflow → bridge → gangotri → execute → journal without checking files? YES → proceed.

---

# PRIMARY — WEEKS 14-15: "Final Integration + Eval Prep"

*The syllabus's final weeks with real context. Paper-to-live gap. Prop firm selection.*

| Day | Concept | Read | Do | Time |
|-----|---------|------|-----|------|
| **92-93** | **Forward Testing (continued)** | `systems/accumulation-distribution-syllabus.md` Week 11 | 10 more trades using the full system. Journal with concept tags. | 60 min × 2 |
| **94-95** | | | 10 more. Total forward test: 20+ trades. | 60 min × 2 |
| **96-97** | **Eval Prep** | `systems/accumulation-distribution-syllabus.md` Week 12 + `trading/eval-mode-protocol.md` | Switch to eval-mode sizing: 0.25% risk, 1 trade/day max. Run 5 sessions. | 60 min × 2 |
| **98-99** | | | 5 more eval-mode sessions. Total: 10. | 60 min × 2 |
| **100-101** | **Paper-vs-Live Gap** | `trading/paper-vs-live-gap.md` (full) | Read the 6 execution gaps. Understand: slippage, spreads, commissions, rollover, stop gap, queue position. | 60 min × 2 |
| **102-103** | **Prop Firm Architecture** | `trading/prop-firm-architecture.md` (full) | Choose your first firm. Decision: FX (FTMO/Funding Pips) or Futures (MFF/Apex)? Write: "My first eval will be _______ because _______" | 60 min × 2 |

**Weeks 14-15 Proof Gate:** 10 eval-mode sessions with zero rule breaches. You've chosen your first firm. YES → proceed.

---

# PRIMARY — WEEKS 16-17: "The 4-Week Bridge"

*Demo is not live. Bridge the gap.*

| Day | Activity | Reference | Time |
|-----|----------|-----------|------|
| **104-110** | **Week 1 of Bridge:** Trade your demo but manually subtract costs (1 pip from every win, $5 from every profit) | `trading/paper-vs-live-gap.md` Week 1 protocol | 60 min/day |
| **111-117** | **Week 2 of Bridge:** Switch to your chosen firm's own demo (FTMO free 14-day or MFF demo) | `trading/paper-vs-live-gap.md` Week 2 protocol | 60 min/day |
| **118-124** | **Week 3 of Bridge:** Eval rehearsal — 0.25% risk, 1 trade/day, A+ setups only | `trading/paper-vs-live-gap.md` Week 3 protocol | 60 min/day |
| **125-131** | **Week 4 of Bridge:** Pre-eval checklist — verify all boxes | `trading/paper-vs-live-gap.md` Week 4 checklist | 60 min/day |

**Week 16-17 Proof Gate (Pre-Eval Checklist):**
```
- [ ] 30+ trades on firm's own demo (not retail demo)
- [ ] Average slippage documented
- [ ] Win rate after costs still positive
- [ ] R:R ≥ 1:1.5 after costs
- [ ] Pre-session ritual is habitual
- [ ] Journal entries for every trade
- [ ] Max 2 consecutive losses in any 5-trade stretch
- [ ] No overtrading: 1-2 trades/day for 5+ consecutive days
```

**All checked → BUY YOUR FIRST EVAL.**

---

# GRADUATION — WEEKS 18-20: "From Student to Trader"

*You've graduated from the classroom. Now you trade.*

| Day | Activity | Reference | Time |
|-----|----------|-----------|------|
| **132** | Buy your first eval | `trading/prop-firm-playbook.md` | — |
| **133-138** | Trade the eval. 1 contract MES or 0.01 lot EUR/USD. Slow and boring. | `trading/eval-mode-protocol.md` | 60-90 min/day |
| **139** | Weekly review | Did you pass? Did you breach rules? What happened? | 30 min |
| **140** | If passed → `trading/fill-your-cup.md` (Prove It phase) | Read. Internalize. This is the beginning of the real game. | 45 min |
| **141-147** | Trade funded account. Same routine. Same rules. Same size. | All system files. Daily. | 60-90 min/day |

---

## THE COMPLETE MAP — 20 Weeks, Every Day, Every File

```
PRE-NURSERY (Weeks 1-3)  │ DAYS 1-21  │ 14 files │ "What is this?"
NURSERY (Weeks 4-5)      │ DAYS 22-35  │ 10 files │ "How do I read it?"
PRIMARY (Weeks 6-17)     │ DAYS 36-131 │ ALL files│ "How do I do it?"
GRADUATION (Weeks 18-20) │ DAYS 132+   │ ALL files│ "I am doing it."
```

---

## CROSS-REFERENCE — Every File Used in This Syllabus

### Pre-Nursery (Weeks 1-3)
| File | Day(s) | Phase |
|------|--------|-------|
| `01-origins-of-money-and-debt.md` | 1 | Pre-Nursery |
| `02-the-real-meaning-of-economy.md` | 2 | Pre-Nursery |
| `03-money-as-debt-modern-system.md` | 3 | Pre-Nursery |
| `04-what-the-powerful-understand.md` | 4 | Pre-Nursery |
| `07-what-money-actually-is-no-bs.md` | 5 | Pre-Nursery |
| `basics/what-is-a-pip.md` | 9, 11, 12, 13 | Pre-Nursery |
| `basics/candlestick-anatomy.md` | 10 | Pre-Nursery |
| `14-forex-clock-resources.md` | 8, 26 | Pre-Nursery |
| `quickstart/pip-calculator.md` | 9, 12 | Pre-Nursery |
| `14-monetary-plumbing-global.md` | 15 | Pre-Nursery |
| `core/repo-plumbing.md` | 16 | Pre-Nursery |
| `05-how-money-flows-in-the-system.md` | 17 | Pre-Nursery |
| `core/liquidity-equation.md` | 18, 21 | Pre-Nursery |
| `core/tri-region-flow-map.md` | 19 | Pre-Nursery |
| `core/global-flow-map.md` | 20 | Pre-Nursery |

### Nursery (Weeks 4-5)
| File | Day(s) | Phase |
|------|--------|-------|
| `core/plumbing-esoterica.md` | 22, 23, 24 | Nursery |
| `08-forex-trading-the-purest-flow.md` | 27 | Nursery |
| `09-futures-trading-energy-and-receipts.md` | 28 | Nursery |
| `basics/order-types.md` | (referenced throughout) | Nursery |
| `basics/what-is-vwap-ema-volume.md` | (referenced throughout) | Nursery |
| `trading/trading-commandments.md` | 29 | Nursery |
| `13-weekly-flow-tapping-operating-system.md` | 30 | Nursery |
| `systems/weekly-flow-checklist.md` | 31 | Nursery |
| `systems/daily-pre-session.md` | 32 | Nursery |
| `systems/position-sizing-by-flow.md` | 33 | Nursery |
| `mental-models/pipe-theory.md` | 34 | Nursery |
| `mental-models/wealth-code-synthesis.md` | 35 | Nursery |
| `mental-models/10-level-mastery-path.md` | 35 | Nursery |

### Primary (Weeks 6-17)
| File | Day(s) | Phase |
|------|--------|-------|
| `quickstart/01-broker-canada.md` | 36 | Primary |
| `quickstart/02-platform-setup.md` | 37 | Primary |
| `systems/live-data-workflow.md` | 40 | Primary |
| `systems/plumbing-to-trade-bridge.md` | 41 | Primary |
| `systems/gangotri-protocol.md` | 42, 66-67 | Primary |
| `quickstart/pip-calculator.md` | 43 | Primary |
| `trading/complete-strategy-orb-eurusd.md` | 44 | Primary |
| `06-day-trading-tap-the-flow.md` | 48 | Primary |
| `plumbing-hierarchy-master.md` Part 9.2 | 50-79 | Primary |
| `systems/accumulation-distribution-syllabus.md` | 92-97 | Primary |
| `trading/eval-mode-protocol.md` | 96-97, 133-138 | Primary |
| `trading/paper-vs-live-gap.md` | 100-131 | Primary |
| `trading/prop-firm-architecture.md` | 102-103 | Primary |
| `trading/prop-firm-playbook.md` | 132 | Primary |
| `trading/mes-mnq-playbook.md` | (during sessions) | Primary |
| `systems/3hr-daily-schedule.md` | (daily from Week 6) | Primary |
| `systems/sunday-prep-ritual.md` | (every Sunday from Week 6) | Primary |
| `systems/trade-journal-template.md` | (every trade from Week 7) | Primary |
| `systems/gangotri-protocol.md` | (every session from Week 6) | Primary |

### Graduation (Weeks 18-20)
| File | Day(s) | Phase |
|------|--------|-------|
| `trading/prop-firm-playbook.md` | 132 | Graduation |
| `trading/eval-mode-protocol.md` | 133-138 | Graduation |
| `trading/fill-your-cup.md` | 140+ | Graduation |
| `trading/trading-commandments.md` | Every day | Graduation |
| `trading/multi-account-gateway.md` | When scaling | Graduation |
| `10-investing-and-compounding.md` | After first payout | Graduation |
| `11-escaping-the-rat-race.md` | After 3 months funded | Graduation |

---

## THE DAILY RHYTHM (Once You're in Primary — Day 36+)

```
┌─────────────────────────────────────────────────────────────┐
│                  DAILY 3-HOUR BLOCK                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ☐ Pre-session (30 min)                                      │
│      15 min — Live data workflow                              │
│       5 min — Chart prep (ORB, VWAP, levels)                 │
│       5 min — Commandments read aloud                         │
│       5 min — Session plan written                            │
│                                                              │
│  ☐ Trading session (60-90 min)                                │
│      Watch 6:30-7:00 AM PT (no trades)                        │
│      Execute 7:00-9:00 AM PT (1-2 trades max)                 │
│      STOP by 9:00 AM PT unless Power Hour at 10:30            │
│                                                              │
│  ☐ Post-session (15 min)                                      │
│      Journal every trade                                      │
│      Session summary: follow plan? bias match?                │
│      Update P&L tracker                                       │
│                                                              │
│  ☐ Study time (45-75 min)                                     │
│      Focus on one topic — plumbing, mental models,            │
│      or strategy refinement. No charts.                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## THE RULES

1. **Do not advance until proof is met.** Each week has a Proof Gate. If you can't pass it, repeat the week.
2. **If you repeat a week, change your approach.** Same concept, different lens.
3. **Journal every trade. Tag every trade with the concept name.** Even skipped trades.
4. **When the tracker fills up, you're ready.** 20 weeks of structured learning, ~120 journaled trades, eval-ready risk habits.
5. **The syllabus is not the teacher. The screen is.** Every line is a suggestion. The only real curriculum is price.
6. **Per-session risk cap is law.** Max 2% loss per session. Max 3 trades per session. Max 3 consecutive loss days before forced flat day.
7. **Sunday prep is not optional.** The weekly chart frames every intraday trade.
8. **Flat is a win.** Every day you wanted to trade but didn't because the signal wasn't there is a WIN.
9. **If you open a trade without doing the pre-session, you are gambling.**
10. **If you open a trade without a journal entry planned, you are gambling.**

---

## RECOVERY PROTOCOL — When Life Happens

| Missed | Resume With |
|--------|-------------|
| 1 day | Skip it. Resume next day. No catch-up. |
| 2 days | Study day first. Run workflow 3 days without trading. |
| 1 week | 3 study days in a row. Re-read pipe-theory.md. Demo 5 sessions before live. |
| 1 month | Restart from Week 29 (Systems & Ritual). Do not skip. |

---

## THE ENDGAME

```
Week 1:   "What is money?"
Week 7:   "I just placed my first trade."
Week 13:  "I can run the full system."
Week 17:  "I'm ready for real money."
Week 20:  "I am a funded trader."
Week 30:  "I am free."
```

---

*"The map is not the territory. But without the map, you're lost in the territory. This is your map. Follow it. Then burn it when you can navigate by heart."*

---

*git add -A && git commit -m "syllabus — THE MASTER SYLLABUS — day by day, ABC to first funded trade — 2026-07-23" && git push*
