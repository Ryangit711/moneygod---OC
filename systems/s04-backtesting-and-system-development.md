# s04 — Backtesting and System Development

## Part 1: What a Trading System Actually Is

A trading system is NOT a setup. A setup is "liquidity sweep + FVG."
A trading system is a fully specified set of rules that covers:

1. **Entry conditions** — exactly what must be true to enter
   (e.g., "ES sweeps below prior session low with negative delta, then
   closes back above — and is at a 4H HVN")
2. **Stop loss conditions** — where and why you get out when wrong
   (price stop, time stop, or thesis break)
3. **Take profit conditions** — where and why you get out when right
   (fixed R target, structural target, or trailing)
4. **Filter conditions** — when NOT to take the trade even if entry triggers
   (e.g., "no trades 30 min before/bafter high-impact news")
5. **Position sizing rules** — how many units based on account size and risk %
6. **Session rules** — when this system is valid (e.g., "London + NY
   overlap only. Never Asia.")

**Without all 6, you do not have a system. You have an idea.**
An idea is not tradeable. A system is.

**The mistake most retail makes:** They have an entry rule ("buy when
RSI is oversold") and NO OTHER RULES. They have no idea where to stop,
when to take profit, how much to risk, or what to avoid. They have an
opinion, not a system.

---

## Part 2: Manual Backtesting Methodology

### The Basic Process

1. Open a chart with at least 6 months of historical data (more = better)
2. Set timeframe to your trading horizon (5m for intraday, 1H for swing)
3. Scroll back to a starting date
4. Walk forward candle by candle — DO NOT PEEK AHEAD
5. At each candle, ask: "Does my system trigger here?"
6. If yes → record a virtual trade: entry, stop, target, size, date
7. Continue until you have 30-100 trades
8. Calculate metrics (Part 3)

### Sample Size Requirements

| Sample Size | Statistical Significance | Action |
|-------------|-------------------------|--------|
| < 20 trades | None. Pure noise. | Keep backtesting. |
| 20-30 trades | Directional. Good enough to start demo-test. | Move to demo forward testing. |
| 30-60 trades | Useable. ~10% margin of error on your true win rate. | Live demo with 0.01 lots. |
| 60-100 trades | Statistical. ~5% margin of error. | Ready for small live. |
| 100+ trades | Solid. Real edge detection. | Eval/trainable consistently. |

**Why 30-60 is the magic zone:** Below 30, you can have a 50% win rate just
from luck. Below 60, your true win rate could be anywhere ±10%. Above 60,
your real edge (or lack of it) becomes clear.

### The Forward Bias Trap

The single biggest backtesting mistake: knowing what happened next.

**The fix:** Use a tool that hides forward candles:
- TradingView Bar Replay (free) — scroll back, then step forward
- Forex Tester 4 (~$200 lifetime) — proper simulator, no peeking
- Or: print 6 months of charts on paper and tape over the right side

If you've EVER accidentally looked 1 candle ahead and thought "well,
I would have entered there anyway" — that trade is contaminated.
Skip it. Don't include it in your numbers. The bias compounds.

### The Survivorship Bias Trap

You only backtest symbols that still exist. The ones that went bankrupt
got delisted. Your backtest misses the worst outcomes.

**The fix:**
- For FX: trade major pairs only — they don't go to zero
- For futures: trade /ES and /NQ — they reflect the index, not an underlying
- For stocks: include delisted names in your backtest data but expect them to underperform
- For crypto: be aware BTC's history makes any strategy look great — the
  macro regime masks the edge

---

## Part 3: Metrics That Matter

### Core System Metrics

| Metric | Calculation | What It Tells You |
|--------|-------------|-------------------|
| **Win rate** | wins ÷ total trades | Hit frequency (NOT edge — see EV in s01) |
| **Risk:Reward** | avg win ÷ avg loss | The symmetry of the system |
| **Profit factor** | gross profit ÷ gross loss | >1.5 profitable, >2 strong, >3 suspicious |
| **Expectancy (EV)** | (W% × avg win) − (L% × avg loss) | Money made per trade (in R) |
| **Max drawdown** | worst peak-to-trough equity decline | Worst pain to sit through |
| **Recovery factor** | net profit ÷ max drawdown | Quality of returns vs. pain |
| **Sharpe** | (return − RF) ÷ σ | Risk-adjusted return (penalizes upside — use Sortino) |
| **Sortino** | (return − RF) ÷ σ-downside | Better — only penalizes downside |
| **Avg trade duration** | how long a trade is open | Quality-of-life metric (5-day avg = swing; 5 min = scalp) |
| **Max consecutive losses** | worst losing streak | Prepare for psychological stress |
| **Trade frequency** | trades per week/month | Whether the system matches your schedule |

### Optimization vs. Monitoring

| Metric | Optimize for | Just Monitor |
|--------|--------------|-------------|
| Win rate | NO — false goal | YES — check it's not drifting |
| R:R | NO — depends on market regime | YES — check it remains congruent with system |
| Profit factor | YES to a degree (>2 means healthy) | Don't chase >3 — usually means curve fit |
| Expectancy | YES in R per trade | Monitor — if it drops > 25% from initial, the system is degrading |
| Max drawdown | YES — minimize | NO — every system has a natural DD |
| Average trade time | Match your schedule | Don't chase shorter |
| Trade frequency | Match your bandwidth | Don't chase more trades (overtrading) |

**The cardinal warning:** If you optimize for win rate, you will
end up with 90% win rate and a 1:0.1 R:R — small wins, occasional
huge losses. Net negative EV. Win rate is vanity; EV is sanity.

---

## Part 4: The Curve-Fitting Danger — How Backtests Lie

### What Curve-Fitting Is

Your system has parameters: stop distance, take profit R, time-of-day
filter, RSI threshold, etc. If you tune these parameters to maximize
backtest performance on YOUR historical dataset, you have likely
curve-fit: you found parameters that happen to work on the past
but have NO predictive power for the future.

### The Test: Out-of-Sample

Save 30% of your historical data BEFORE backtesting. Backtest on the
other 70%. Then test on the 30%.

If performance on the 30% is within 25% of the 70% → not curve-fit (probably).
If performance drops >50% → curve-fit. Your parameters don't generalize.
Worst case: positive on 70%, negative on 30% → totally curve-fit. Abandon.

### Walk-Forward Analysis

A more rigorous version: backtest on rolling windows.
- Backtest 2023 → test 2024-Q1
- Then add Q1 to backtest → test Q2
- And so on.
- If the system holds up across each window, it's robust.

This is what pro quants do. Retail can simulate by just backtesting
in 3-month chunks and comparing metrics.

### Monte Carlo Simulation

Take your backtest's trade list (entry, exit, R-result of each trade).
Randomly shuffle the order of trades 1,000 times. Each shuffle creates
a different equity curve. Look at the WORST of these 1,000.

If the worst case is a >30% drawdown in your shuffle, your real-world
drawdown will probably exceed your backtest drawdown. The order
matters — clustered losses (which tend to happen when regimes shift)
kill accounts in ways mean-variance can't predict.

Free tool: https://www.montecarlosimulations.org/ (basic)
Paid: Monte Carlo tools in MetaTrader, TradeStation, Quantower.

### The Tell-Tale Signs of Curve-Fitting

| Symptom | Likely Diagnosis |
|--------|------------------|
| PF > 3 in backtest | Suspicious. Most real edges are PF 1.5-2.5. |
| Win rate > 75% | Suspicious unless you're a market maker. |
| Max drawdown < 5% | Likely curve fit or over-tight stops. |
| Returns spike on entry parameters (e.g., "use RSI=67 instead of 65") | Noise-driven. Use parameters that are within ±20% of each other performance-wise. |
| Best results at a single time of day | Likely real — regime-based. |
| Results change wildly with small parameter changes | Curve-fit. |

---

## Part 5: Automated Backtesting — Basic Pine Script and Python

### When to Automate

| Situation | Automate? |
|-----------|-----------|
| Backtesting 100+ trades manually | YES — automation lets you scale sample size |
| Testing variations of a system (different R targets, different stops) | YES — quickly iterate |
| Studying the intraday behavior of one setup | YES |
| Testing market regime filters | YES — too tedious to do manually |
| Trying to find an edge in the first month | NO — you don't know what you're looking for; manual observation comes first |
| Backtesting news-based strategies | NO — historical news data is unreliable |

### Pine Script Starter (TradingView)

```pinescript
//@version=5
strategy("ORB Long Backtest", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=1)

// 9:30 ET OR high definition (sample, conceptual)
tradetime = time(timeframe.period, "0930-1000:1234567", "America/New_York")
isORBPeriod = ta.barssince(tradetime[0] != tradetime[1]) == 0  // first bar of ORB
orbHigh = isORBPeriod ? high : na

// Track ORB high
var float orbHighLevel = na
if isORBPeriod
    orbHighLevel := high
plot(orbHighLevel, color=color.green)

// Enter on breakout
breakoutCondition = close > orbHighLevel and not isORBPeriod
if breakoutCondition
    strategy.entry("ORB Long", strategy.long)

// Exit at +2R or last bar of day
riskInPrice = orbHighLevel - (orbHighLevel - ta.lowest(low, 5))  // arbitrary risk proxy
targetPrice = orbHighLevel + 2 * riskInPrice
if high >= targetPrice
    strategy.close("ORB Long", comment="Take Profit")
if hour == 16
    strategy.close_all(comment="Close of Session")
```

**Use this as a template.** It will produce ~20-50 trades on a year of
5-min data. From there, refine entry logic, add a stop, compare different
R targets. Pine Script v5 manual on TradingView's website — ~2 hours to
become functional.

### Python Starter

For more serious backtesting, learn the `backtrader` library or
`vectorbt`. Free, open-source, allows for walk-forward analysis,
Monte Carlo, and full metrics calculation. Takes longer to learn
but unlocks any analysis you can think of.

**Key libraries:**
- `backtrader` — backtest framework
- `pandas`, `numpy` — data manipulation
- `yfinance` — free historical data
- `matplotlib` — visualize equity curves

A simple backtest in Python:

```python
import backtrader as bt

class ORBStrategy(bt.Strategy):
    def __init__(self):
        self.orb_high = None
    def next(self):
        if self.datas[0].datetime.time() == dt.time(9, 30):
            self.orb_high = self.datas[0].high
        elif self.datas[0].high > self.orb_high and not self.position:
            self.buy()
        elif self.datas[0].high >= self.orb_high * 1.002:
            self.close()
```

(Pseudocode — learn from backtrader docs for full template.)

---

## Part 6: The Development Loop

```
┌─────────────────────────────────────────────────────────────────┐
│  OBSERVE: Watch live data for a recurring phenomenon             │
│  "I notice /ES often wicks below the prior session low and     │
│   snaps back in the first hour of NY open."                    │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  HYPOTHESIZE: Form a rule-based guess about the pattern         │
│  "If price wicks 5+ pips below prior session low AND closes    │
│   back above within 3 candles, then buy with stop below wick." │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  TEST: Backtest on 6+ months of data. 60+ trades minimum.      │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  ANALYZE: Compute metrics. Check PF, EV, MaxDD, win rate.      │
│  If PF < 1.5 → reject hypothesis.                              │
│  If MaxDD > 25% → adjust stops or sizing, re-test.             │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  REFINE: Try 3 variations of the rule (tighter/looser stops,  │
│  different filter, different session). Pick the variation     │
│  that is STABLE across parameter changes (robust, not optimal). │
└──────────────────────────────────┬──────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  FORWARD-TEST ON DEMO: Trade the system with 0.01 lots for 30 │
│  trades. Compare demo win rate/EV to backtest.                 │
│  Within 25% → ready for eval.                                  │
│  Outside 25% → re-examine for forward bias in backtest.        │
└─────────────────────────────────────────────────────────────────┘
```

### The Loop in Practice

Most "strategies" fail this loop. That's normal. You will try 10 ideas
and find 1 that survives. That 1, on demo, becomes your system. The other
9 are learning — they refine your hypotheses for the next iteration.

**The number that matters:** 1 working system you understand the WHY of
is worth 100 "profitable backtests" you don't understand. Always be able
to explain why your system works in plain English. If you can't, you've
curve-fit.

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s01-mathematics.md` | Every metric in s04 Part 3 (PF, EV, MaxDD, Sortino, Recovery Factor) is defined formulaically in s01. You cannot evaluate a backtest without s01's reference card. | Computing backtest metrics |
| `systems/s09-journaling-and-performance-analysis.md` | The journal template records trades the SAME WAY you backtest them — making your live record directly comparable to backtest results. Without that congruence, you can't compare. | Defining journal fields; comparing live vs. backtest |
| `systems/s03-volume-profile-and-order-flow.md` | Every backtest should record volume/flow context of each setup entry. s03's concepts (HVN, delta divergence) become categorization tags in s04's trade log. | Categorizing setups by quality in backtest |
| `trading/complete-strategy-orb-eurusd.md` AND `trading/mes-mnq-playbook.md` | These existing playbooks can be backtested using s04's methodology. They're prime candidates for the first system you develop through the loop. | Building first backtestable system |
| `systems/s08-advanced-risk-and-position-sizing.md` | Backtest results dictate your live sizing protocol (Kelly fraction, drawdown halving). s04 produces the inputs for s08's sizing decisions. | Choosing Kelly fraction; setting drawdown rules |
| `systems/s05-intraday-market-structure.md` | The session patterns in s05 (opening drive, lunch lull) are filter conditions for s04. Backtesting intraday strategies requires recording session timing — the why is in s05. | Filtering backtest trades by session |
| `plumbing-hierarchy-master.md` Part 9.2 (ICT Concepts) | Each ICT concept (liquidity sweep, FVG, order block, CHoCH) can be backtested using s04's methodology. ICT files alone are theory; s04 turns them into testable hypotheses. | Converting ICT concepts to testable systems |
| `systems/s12-capital-management-and-scaling.md` | The metrics produced by s04 (expectancy, MaxDD) feed directly into s12's scaling plan — your "3 consecutive months of positive expectancy" criterion is what s04 measures. | Determining readiness to scale |
