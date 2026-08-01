# s00 — Concept Registry (The Hippocampus)

## What This Is

The concept registry is the hippocampus of the Moneygod brain. It indexes every distinct trading/finance concept across all 93+ files in this repo. When a new piece of information arrives (from Arena chat, personal journal, book, AI conversation), the ASSIMILATION_PROTOCOL.md taxonomy table routes it to the correct file — but the concept registry connects all files by CONCEPT, not by file location.

Use this registry when:
- You read a term in one file and want to find all related files
- You learn a new concept and need to place it in the existing map
- You want to study a concept across all its dimensions (math → psychology → execution)
- You need to know if a concept is already covered before creating a new file

## How to Use

1. Look up the concept alphabetically
2. Note the Primary and Secondary files
3. Read the Primary file first (it has the core treatment)
4. Read the Secondary files for cross-dimension understanding

## The Registry

### 0DTE (Zero Days to Expiration)
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`
- **Neuron:** Options that expire the same day — gamma approaches infinity near the close, forcing dealers to hedge violently.
- **Synapse:** 40-50% of all SPX option volume is now 0DTE; the Friday power hour (3:30-4:00 PM) is the most mechanically tradeable window of the week.

### 10-Level Mastery Path
- **Primary:** `CURRICULUM.md`
- **Secondary:** `GROWTH_PROTOCOL.md`, `systems/s12-capital-management-and-scaling.md`
- **Neuron:** The progression from Phase 0 (self-assessment) through Phase 10 (mastery) — each phase has specific skill gates, risk rules, and capital targets.
- **Synapse:** Prevents skipping stages; the path is the protection against blowing up by trying to skip from beginner to funded in one leap.

### 18-Region Flow Map
- **Primary:** `core/global-flow-map.md`
- **Secondary:** `core/tri-region-flow-map.md`, `plumbing-hierarchy-master.md`
- **Neuron:** The complete map of 18 financial regions organized by flow power — US (engine) → Tier 1 (EU, China, Japan, UK) → Tier 2 (Canada, Australia, etc.).
- **Synapse:** Shows exactly how dollar liquidity cascades from the Fed through every region; tells you which markets to watch for transmission.

### 4% Rule
- **Primary:** `systems/s12-capital-management-and-scaling.md`
- **Secondary:** `systems/s11-trading-business-and-tax.md`
- **Neuron:** The withdrawal rate that historically preserves capital indefinitely — withdraw 4% of portfolio annually, adjust for inflation.
- **Synapse:** Defines the "Freedom Number" — the capital required to replace earned income with portfolio withdrawals.

### Absorption
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A large limit order soaks up aggressive market orders without the price breaking — the aggressor is failing to move the market.
- **Synapse:** Absorption at a key level is the strongest fade signal in microstructure; the breakout attempt will likely fail and reverse.

### ADX (Average Directional Index)
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`
- **Neuron:** A 0-100 oscillator measuring trend strength: >25 = trending, <20 = ranging. Does not indicate direction, only strength.
- **Synapse:** Before every session, check ADX — determines whether your trend-following or mean-reversion system should be active.

### Arithmetic vs. Geometric Returns
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`
- **Neuron:** Arithmetic return = average of returns; geometric return = what you actually compound to. Geometric ≤ arithmetic when volatility > 0.
- **Synapse:** The gap between them is the volatility drag — the reason 50% drawdowns require 100% gains to recover.

### ATR Stop
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`, `systems/s01-mathematics.md`
- **Neuron:** Stop distance set as a multiple of average true range (e.g., 1.5×ATR) — adapts to current volatility.
- **Synapse:** Volatility-adjusted stops keep risk constant across market regimes; tight in low vol, wide in high vol.

### Auction Theory
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `06-day-trading-tap-the-flow.md`, `plumbing-hierarchy-master.md`
- **Neuron:** Every market is an auction — price moves up when buyers are more aggressive, down when sellers are more aggressive, and stays flat when balanced.
- **Synapse:** Understanding the two phases (trend and balance) tells you whether to trend-trade or range-trade.

### Backtesting
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`, `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Neuron:** Simulating a trading system on historical data to estimate its statistical properties (win rate, EV, drawdown) before risking live capital.
- **Synapse:** The only way to separate an edge from luck; 60+ trades minimum for a statistically usable sample.

### Backtrader (Python Library)
- **Primary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`
- **Neuron:** Python backtesting framework that supports walk-forward analysis, Monte Carlo, and custom strategy logic.
- **Synapse:** When Pine Script limits are hit, Backtrader unlocks any backtest analysis you can think of.

### Behavioral Metrics
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`
- **Neuron:** Quantified psychological health: % of impulse trades, % of trades that deviated from plan, % of premature breakeven exits.
- **Synapse:** Behavioral metrics catch deterioration before P&L does — a red flag in behavior predicts a red month in equity.

### BIS (Bank for International Settlements)
- **Primary:** `plumbing-hierarchy-master.md`
- **Secondary:** `14-monetary-plumbing-global.md`
- **Neuron:** The "central bank of central banks" — coordinates global monetary policy, sets Basel capital standards, operates in Basel, Switzerland.
- **Synapse:** BIS capital requirements (Basel III) determine how much leverage banks can use, which directly constrains market liquidity.

### Boredom State
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`
- **Neuron:** The urge to trade when no setup exists — driven by dopamine starvation, not edge detection.
- **Synapse:** Boredom is the #1 destroyer of accounts; "no trade" is always a winning trade.

### Breakeven Stop
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** Moving a stop to the entry price after price reaches +1R — the trade becomes risk-free.
- **Synapse:** Do NOT move to breakeven immediately after entry; price needs room to breathe. Wait for +1R.

### Business Income vs. Capital Gains (CRA)
- **Primary:** `systems/s11-trading-business-and-tax.md`
- **Secondary:** `01-origins-of-money-and-debt.md`
- **Neuron:** CRA determines if you are a trader (business income — 100% taxable) or an investor (capital gains — 50% inclusion rate) based on frequency, holding period, intent.
- **Synapse:** Day traders are automatically business income; a $100k gain is $100k taxable, not $50k. Incorporate or use RRSP/FHSA to mitigate.

### Call Wall
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A strike price with massive open interest in calls — dealers hedging those calls buy futures as price rises, accelerating the move upward.
- **Synapse:** Acts as a liquidity ceiling; if price reaches it and rejects, short. If price blows through, let the gamma squeeze run.

### Cantillon Effect
- **Primary:** `03-money-as-debt-modern-system.md`
- **Secondary:** `core/liquidity-equation.md`, `plumbing-hierarchy-master.md`
- **Neuron:** New money enters the economy at specific points (banks, dealers); those closest to the spigot benefit first, before inflation reaches the broader economy.
- **Synapse:** Explains why QE primarily inflates asset prices (stocks, real estate) before CPI — the first receivers capture the new money.

### Carried Interest
- **Primary:** `04-what-the-powerful-understand.md`
- **Secondary:** `12-who-knows-this-level.md`
- **Neuron:** The profit share paid to fund managers (typically 20% of returns above a hurdle) — taxed as capital gains, not ordinary income, due to a carried-interest tax loophole.
- **Synapse:** Illustrates how the wealthy structure income through tax-advantaged vehicles that are unavailable to retail traders.

### Closing Auction
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s13-options-mechanics-for-futures-traders.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** The 2:00-4:00 PM EST window when volume picks up as institutions position for the next day — the most important period for understanding tomorrow's direction.
- **Synapse:** If the day's trend continues into the close, expect continuation at next session's open. If it reverses, expect a gap.

### Compound vs. Withdraw 50% Rule
- **Primary:** `systems/s12-capital-management-and-scaling.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** After 3 consecutive months of positive expectancy in Phase 2, withdraw up to 50% of monthly gains — reward yourself while keeping the account compounding.
- **Synapse:** Prevents two failure modes: never withdrawing (resentment) and withdrawing too much (killing compounding).

### Correlation
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** A measure (-1 to +1) of how two assets move together. EUR/USD and GBP/USD correlate at ~0.85; being long both is not diversification.
- **Synapse:** Total correlated risk per direction must not exceed 2.5% of account — otherwise one move wipes the book.

### Correlation Sizing
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** Adjusting position sizes to account for correlation between instruments — if EUR/USD and GBP/USD are both long, their combined effective risk is ~1.7× single risk.
- **Synapse:** Prevents the invisible killer: having 3% total risk across correlated pairs when you think you have 1%.

### Cross-Currency Basis
- **Primary:** `core/plumbing-esoterica.md`
- **Secondary:** `14-monetary-plumbing-global.md`
- **Neuron:** The deviation from covered interest rate parity — a measure of dollar funding stress in the global banking system.
- **Synapse:** Negative cross-currency basis = dollar shortage = stress in global markets; this is the canary in the coal mine for liquidity crises.

### Cumulative Delta
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** The running sum of delta (market buys minus market sells) across all candles in a session — shows who is in net control.
- **Synapse:** When cumulative delta diverges from price (price up, delta flat), the move is weak and likely to reverse.

### Curve-Fitting
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** Over-optimizing a system's parameters to fit historical data, producing a backtest that looks great but has zero predictive power.
- **Synapse:** A profit factor > 3 in backtest is the classic tell — real edges are PF 1.5-2.5. Always test on out-of-sample data.

### Dealer Hedging (Options)
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** When dealers sell options, they hedge by buying/selling the underlying futures as delta changes — creating mechanical, predictable order flow.
- **Synapse:** Dealer hedging is the "why" behind gamma squeezes, pinning, and the power hour; you are riding mandatory institutional flow.

### Delta (Option Greek)
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** The rate of change of an option's price per $1 move in the underlying (0 to 1 for calls, 0 to -1 for puts). Tells dealers how much to hedge.
- **Synapse:** ATM call delta ≈ 0.50 means the dealer buys 0.50 futures per option sold — multiply by open interest to estimate hedging pressure.

### Delta (Order Flow)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** The difference between market buy volume and market sell volume at a given price level or within a candle.
- **Synapse:** Positive delta + rising price = healthy trend. Positive delta + flat price = absorption (strong sellers meeting buyers).

### Delta Divergence
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** Price makes a new high but cumulative delta is flat or falling — buying pressure is drying up even as price rises.
- **Synapse:** The strongest single signal in microstructure; probability of reversal ~60-65% in ES/NQ intraday.

### Delta Pivot
- **Primary:** `systems/s07-order-flow-levels.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** A price level where cumulative delta changed direction — the exact point where aggressive buying flipped to aggressive selling (or vice versa).
- **Synapse:** Ranks #5 in level strength hierarchy; acts as a micro-level support/resistance line drawn from actual order flow.

### Despair (Psychological State)
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`
- **Neuron:** A losing streak drains self-efficacy — you start identifying as a loser rather than a trader who lost. Often leads to blowing up.
- **Synapse:** The protocol is NOT to stop trading; reduce to 0.25% risk and rebuild confidence through small wins over 3-5 sessions.

### Development Loop
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Neuron:** Observe → Hypothesize → Test → Analyze → Refine → Forward-Test. The systematic cycle for converting market observations into tradeable systems.
- **Synapse:** Most ideas fail the loop; finding 1 working system out of 10 attempts is normal. The 9 failures refine your hypotheses.

### Drawdown
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`, `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** The peak-to-trough decline in account equity. Non-linear: a 50% drawdown requires 100% gain to recover.
- **Synapse:** Max drawdown target is 10% — after that, halve position size until recovery. 50% of retail blow-ups start with ignoring a 10% drawdown.

### Drawdown-Modulated Sizing
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`, `systems/s01-mathematics.md`
- **Neuron:** A sizing method that reduces risk percentage as drawdown deepens: 0-5% DD = normal, 5-10% = halve, 10-15% = quarter, >15% = stop.
- **Synapse:** The only way to survive long enough for your edge to play out — your edge stays the same, but you temporarily reduce exposure.

### EMI Coverage
- **Primary:** `systems/s12-capital-management-and-scaling.md`
- **Secondary:** `00-background-edge.md`, `systems/s02-trading-psychology.md`
- **Neuron:** Using trading income to service the ~$1,000/month EMI — the first milestone in Phase 2 that proves the account can cover a real expense.
- **Synapse:** The EMI Buffer variant in s12 turns the account into a debt-servicing machine: every 2× EMI growth → withdraw 1× EMI.

### Emotional Decision Log
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`
- **Neuron:** A separate log tracking deviations from your trading plan: trigger, deviation, emotional state before/after, dollar cost.
- **Synapse:** The pattern becomes visible after 20 entries — your specific triggers become predictable, and prediction is prevention.

### Euphoria State
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** Dopamine-driven invulnerability after a winning streak — the state where the largest losses occur because you size up right before reversion to the mean.
- **Synapse:** Bank the win, take 24 hours off, and re-read your trailing 30-trade stats before the next session.

### Eurodollar
- **Primary:** `14-monetary-plumbing-global.md`
- **Secondary:** `systems/s10-institutional-plumbing-and-eurodollar.md`, `core/plumbing-esoterica.md`
- **Neuron:** US dollars held in banks outside the US — a $13T+ offshore market not subject to Fed reserve requirements or FDIC insurance.
- **Synapse:** Eurodollar rates (LIBOR, SOFR) reflect the TRUE cost of dollar funding; the Eurodollar futures curve predicts global liquidity conditions.

### Excursion Analysis (MFE/MAE)
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Max Favorable Excursion (how far price went in your favor) vs. Max Adverse Excursion (how far it went against you) for every trade.
- **Synapse:** If MFE consistently exceeds realized exit, your exit strategy is leaving money on the table — tighten targets or add trailing logic.

### Exit Management
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** The complete set of rules for when and how to exit: target hits, stop hits, time stops, early exits, and the "let it run" mentality.
- **Synapse:** Most traders exit too early; exiting at +1R when the target is +3R can turn a positive-EV system into a negative one.

### Expectancy (EV)
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`, `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** (Win Probability × Average Win) − (Loss Probability × Average Loss). The only number that determines whether a system makes or loses money over time.
- **Synapse:** A system with 40% win rate and 2:1 R:R has positive EV (+0.2R/trade). A system with 60% win rate and 1:3 R:R has negative EV (−0.2R/trade). Win rate is vanity; EV is sanity.

### Fat Tails
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Real market returns have fatter tails than the normal distribution predicts — extreme moves (3σ+) happen 10-20× more often than textbook statistics suggest.
- **Synapse:** A "3-sigma stop" will hit ~1 in 20 trading days, not 1 in 370. Use 5-sigma stops or options hedges for true tail protection.

### Fixed Fractional Sizing
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** Position size = (Account × Risk%) ÷ Stop Distance. The baseline sizing method — risk a fixed percentage of account per trade.
- **Synapse:** Use this until you have a consistent edge. 1% is the default for most traders; 0.5% for Survival Phase.

### Flow vs. Prediction
- **Primary:** `plumbing-hierarchy-master.md`
- **Secondary:** `06-day-trading-tap-the-flow.md`, `00-background-edge.md`
- **Neuron:** The difference between reading where money is currently flowing (flow) and guessing where it will go (prediction). Trading flow is probabilistic; trading predictions is gambling.
- **Synapse:** "Feel, don't predict" — the antidote to overconfidence from plumbing understanding. Read flow, don't forecast price.

### FOMO (Fear of Missing Out)
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** The anxiety-driven urge to enter a trade because price is moving and you're not in it — the emotional state most likely to produce an entry without a setup.
- **Synapse:** If you feel FOMO, the trade is already gone. FOMO entries are always at the worst price. Wait for the next setup.

### Footprint Charts
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A chart type that shows volume at each price level within a single candle — reveals who is winning inside the candle, not just the open/close.
- **Synapse:** Imbalance at the high = buyers confident, trend continues. Absorption at a level = breakout likely fails. Stacked imbalances = strong directional pressure.

### Forward Bias
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Neuron:** The single biggest backtesting mistake: knowing what happened next contaminates your entry/exit decisions, inflating backtest performance.
- **Synapse:** Fix with bar replay tools (TradingView, Forex Tester 4) or paper charts. One peek-ahead candle contaminates the trade; skip it.

### Freedom Number
- **Primary:** `systems/s12-capital-management-and-scaling.md`
- **Secondary:** `11-escaping-the-rat-race.md`
- **Neuron:** The capital required to replace all essential monthly expenses using the 4% rule: Freedom Number = Monthly Expenses × 12 ÷ 0.04.
- **Synapse:** Defines the destination — at $2,500/mo expenses, Freedom Number = $750,000. The three-phase model is the step-by-step path to reach it.

### FREEFALL (All Sectors)
- **Primary:** `FREEFALL_360.md`
- **Secondary:** `FREEFALL_LIFE.md`, `FREEFALL_PHILOSOPHY.md`, `MAP_360.md`
- **Neuron:** The complete 360° mapping of the system as a living organism — connects monetary plumbing, geopolitics, psychology, life strategy, and exit planning into one unified model.
- **Synapse:** FREEFALL is the meta-map that shows how every concept in this registry connects; drop in anywhere and follow threads to everywhere.

### Gamma (Option Greek)
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** The rate of change of delta per $1 move in the underlying. High gamma = delta changes rapidly = dealers must hedge aggressively.
- **Synapse:** Gamma is highest ATM and at expiration. Gamma flips from positive (mean-reverting) to negative (trending) when strike is breached — this is the options signal for regime change.

### Gamma Squeeze
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** A self-reinforcing cycle where dealer hedging (buying futures as delta increases) pushes price higher, increasing delta further, forcing more buying.
- **Synapse:** Not optional — dealers MUST hedge. Gamma squeezes are the most explosive moves in the market; ride them, don't fight them.

### Geometric vs. Arithmetic Returns
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`
- **Neuron:** Arithmetic = average return; geometric = compounded return. Geometric is always ≤ arithmetic when volatility > 0.
- **Synapse:** The gap is the volatility drag (σ²/2). Doubling risk doesn't double returns — it squares drawdowns and extends the recovery timeline.

### Gatherer vs Converger
- **Primary:** `00-background-edge.md`
- **Secondary:** `systems/s02-trading-psychology.md`, `conversations/2026-07-29_arena-analysis-catalyst.md`
- **Neuron:** The distinction between gathering knowledge broadly (which feels like progress but doesn't compound) and converging on one catalyst pathologically (which feels risky but is the only path to leverage). Most intelligent people stay in gather mode forever.
- **Synapse:** At every phase, ask: "Am I gathering or converging?" The feeling of needing "just one more book/file/course before I start" is the gatherer protecting itself from the risk of failure.

### Higher Timeframe Dominance
- **Primary:** `systems/s06-top-down-analysis.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`
- **Neuron:** The golden principle: higher timeframes control lower timeframes. A bullish 1-min divergence means nothing if the 1H chart is in a downtrend.
- **Synapse:** 80% of retail losses come from fighting the higher timeframe trend. Determine weekly bias first, then find intraday entries in that direction.

### High Volume Node (HVN)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s05-intraday-market-structure.md`
- **Neuron:** A price level where abnormally high volume traded — institutional interest zone that acts as natural support or resistance.
- **Synapse:** Ranks #2 in level strength hierarchy. Price approaching an HVN with decreasing momentum = expect reversal; with high momentum = expect breakout.

### HST/GST Registration (Canada)
- **Primary:** `systems/s11-trading-business-and-tax.md`
- **Secondary:** `06-day-trading-tap-the-flow.md`
- **Neuron:** If gross revenue from non-security services exceeds $30k/quarter, you must register for GST/HST. Trading your own capital is exempt; prop payouts may not be.
- **Synapse:** Most traders don't know this threshold exists. Exceeding it without registering triggers penalties and back-tax.

### Iceberg Orders
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A large limit order that shows only a small portion of its true size — institutions hide their interest to avoid pushing price away.
- **Synapse:** Price "stuck" on a level for many candles that absorbs multiple fills without breaking = iceburg. The breakout attempt at that level will likely fail.

### Imbalance (Order Flow)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** When one side of the market (buys vs. sells) dominates at a specific price within a candle. Stacked imbalances show strong directional pressure.
- **Synapse:** Imbalance at the candle's high = buyers in control, trend continues. Imbalance at the candle's low = sellers in control, trend continues.

### Inside Day
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`
- **Neuron:** A day where price stays entirely within the previous day's range — low volatility, usually before a major event.
- **Synapse:** ~10% of days. Expect a breakout the following day. Inside days compress energy; the release is directional.

### Kelly Criterion
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** Kelly% = W − (L/R). The formula that gives the mathematically optimal bet size given your win rate and R:R.
- **Synapse:** Full Kelly is too dangerous (40-60% drawdowns). Use Quarter-Kelly or Eighth-Kelly (4% for typical retail parameters). The 1% rule is ~1/30th Kelly — deliberately conservative.

### Kelly Fraction (Quarter/Eighth)
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** Practical fractions of full Kelly that reduce drawdown risk while capturing most of the compounding benefit: full Kelly ÷ 4 or ÷ 8.
- **Synapse:** Eighth-Kelly (4%) is the practical max for retail. If that feels too large, use 1% — the most important thing is not blowing up.

### Legal Fiction (Sovereign)
- **Primary:** `01-origins-of-money-and-debt.md`
- **Secondary:** `04-what-the-powerful-understand.md`, `plumbing-hierarchy-master.md`
- **Neuron:** The legal construction that the sovereign (King, state, government) has the authority to create money and define what counts as legal tender for discharging debts.
- **Synapse:** Understanding that money is a legal fiction, not a natural resource, removes the mystique and reveals the plumbing underneath.

### Level Confluence
- **Primary:** `systems/s07-order-flow-levels.md`
- **Secondary:** `systems/s06-top-down-analysis.md`, `systems/s05-intraday-market-structure.md`
- **Neuron:** When multiple level types (POC + round number + previous day high) align at the same price — creating a "fortress" level with much higher probability.
- **Synapse:** Trade only at levels with 2+ sources of confluence. A single level with no confluence is a suggestion, not a plan.

### Leverage
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** The multiplier between your cash and your position size — 1:100 leverage means $1,000 controls $100,000. Multiplies both wins AND losses equally.
- **Synapse:** Leverage is not edge. 1:100 leverage on a $1k account with a 100-pip move = 100% gain or 100% loss. Use leverage to size appropriately, not to amplify returns.

### Leverage Types (Labor / Capital / Code / Media)
- **Primary:** `00-background-edge.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`, `conversations/2026-07-29_arena-analysis-catalyst.md`
- **Neuron:** The four forms of leverage that multiply output without multiplying hours: labor (people working for you), capital (money working for you), code (software working for you), media (content working for you). Smart people sell time; rich people build machines.
- **Synapse:** Most intelligent people default to selling time (consulting, job, trading with their hands). The shift to wealth is building one of the four leverages. The prop firm + algo trading path targets capital + code leverage.

### Limit Order
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** An order to buy/sell at a specified price or better — PROVIDES liquidity, sits in the book until filled.
- **Synapse:** Use limit orders at structural levels (POC, HVN) where you can wait for price to come to you. Use market orders only for time-sensitive entries.

### Low Volume Node (LVN)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A price level where abnormally low volume traded — price moves through these quickly. After being swept, LVNs become support/resistance.
- **Synapse:** Do NOT trade at an LVN — wait for the sweep, then the LVN edge becomes a level. Ranks #3 in strength hierarchy.

### Lunch Lull
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s02-trading-psychology.md`
- **Neuron:** The 10:00 AM-2:00 PM EST window where volume drops ~60% from opening drive — price action becomes noise, breakout trades fail more often.
- **Synapse:** The lunch lull is when boredom-based mistakes happen (Dangerous State #1). Best used for study, not trading.

### MAE (Max Adverse Excursion)
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** The furthest price went against your position before the trade closed — the actual worst moment of the trade.
- **Synapse:** Compare MAE to your stop distance; if MAE consistently falls short of your stop, your stop is too wide. If MAE exceeds stop, your stop placement is poor.

### MAE-Based Stop
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** A stop placed where your backtest's worst 10% of trades show the MAE peak — data-driven, not arbitrary.
- **Synapse:** The most robust stop placement method; it's based on actual trade data rather than chart geometry.

### Margin
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** The cash your broker holds while a position is open — required margin = (Lot Size × Contract Size) ÷ Leverage.
- **Synapse:** Margin is NOT the same as risk. Margin is collateral; risk is the actual loss if stop is hit. Never confuse margin usage with risk exposure.

### Market Order
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** An order to buy/sell at the current market price — TAKES liquidity, guarantees execution but at the worst current price (pays spread).
- **Synapse:** Use for time-sensitive entries (sweep + reversal) or when the market is highly liquid. Do NOT use in low-volume markets or for breakout entries.

### Max Pain
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** The strike price where total value of all options at expiration is lowest — the level where most options expire worthless, maximizing market maker profit.
- **Synapse:** Market makers have incentive to push price toward Max Pain; acts as broad gravitational force over the week. Gamma pin (last hour) usually wins if they diverge.

### MFE (Max Favorable Excursion)
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** The furthest price went in favor of your position before the trade closed — the maximum profit that was available.
- **Synapse:** Compare MFE to actual exit; if MFE is consistently 2× your realized profit, you are leaving money on the table. Tighten exits or add trailing.

### Minsky Cycle
- **Primary:** `04-what-the-powerful-understand.md`
- **Secondary:** `plumbing-hierarchy-master.md`, `core/plumbing-esoterica.md`
- **Neuron:** Hyman Minsky's model of financial instability: Hedge → Speculative → Ponzi financing stages lead to inevitable crisis as debt outruns cash flows.
- **Synapse:** The Minsky Cycle explains why bull markets always end in crashes — stability is destabilizing because it breeds leverage. Markets are not mean-reverting; they are cycle-reverting.

### Money as Debt
- **Primary:** `03-money-as-debt-modern-system.md`
- **Secondary:** `01-origins-of-money-and-debt.md`, `07-what-money-actually-is-no-bs.md`
- **Neuron:** Money in the modern system is created as a debt contract — a bank issues a loan, creating a deposit (money) and a liability (debt) simultaneously.
- **Synapse:** 95% of broad money is bank-created credit, not government-issued cash. Understanding this demystifies inflation, deflation, and liquidity cycles.

### Money-Generating Scenario
- **Primary:** `systems/s06-top-down-analysis.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** The highest-probability trade setup: Weekly = directional, Daily = pullback opposite to weekly, 1H = reversal back toward weekly direction.
- **Synapse:** Produces 4:1+ R:R with >60% win rate. This single concept is worth more than any indicator. Find it, trade it, compound it.

### Monte Carlo Simulation
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** Randomly shuffling the order of trade results 1,000 times to generate many possible equity curves — tests whether your system survives clustered losses.
- **Synapse:** If the worst-case simulation shows >30% drawdown, your real-world drawdown will probably exceed your backtest drawdown. The order of outcomes matters.

### The Negatives (8 Flagged)
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `00-background-edge.md`, `systems/s12-capital-management-and-scaling.md`
- **Neuron:** Eight specific psychological risks flagged by AI models for this trader: totalizing worldview, compression risk, spiritual bypass, family financial pressure, being right vs. making money, intellectual escapism, over-optimization, isolation.
- **Synapse:** Each negative has an antidote protocol. Review the 8 negatives before every phase transition or when you feel any of them activating.

### Net Liquidity Equation
- **Primary:** `core/liquidity-equation.md`
- **Secondary:** `core/global-flow-map.md`, `plumbing-hierarchy-master.md`
- **Neuron:** Net Liquidity = Δ Central Bank Balance Sheet − Δ TGA − Δ RRP. The single metric that drives ~90% of asset price direction.
- **Synapse:** Positive Net Liquidity = buy risk assets. Negative Net Liquidity = sell risk assets. Check weekly — it's the tide that lifts or sinks all boats.

### Norbert's Gambit
- **Primary:** `systems/s11-trading-business-and-tax.md`
- **Secondary:** `quickstart/01-broker-canada.md`
- **Neuron:** A method to convert CAD to USD (or vice versa) at near-spot rates by buying a dual-listed ETF (DLR.TO), journaling it to the USD side, and selling the USD shares.
- **Synapse:** Saves 2-3% vs. bank FX spreads. Use IBKR for cheapest execution (FX is already cheap there). Use with other brokers for meaningful savings on large conversions.

### Oikonomia vs. Chrematistike
- **Primary:** `02-the-real-meaning-of-economy.md`
- **Secondary:** `07-what-money-actually-is-no-bs.md`
- **Neuron:** Aristotle's distinction: Oikonomia = household management (sustainable, use-value focused); Chrematistike = wealth acquisition for its own sake (extractive, unlimited).
- **Synapse:** Trading is chrematistike. Understanding this prevents moral guilt about "not adding value" — the system allows it; you are responsible for your family, not the system's design.

### Opening Drive
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** The first 15-30 minutes after the NY open (9:30-10:00 AM EST) — highest volume and volatility of the day. ~65% of daily ranges establish in this window.
- **Synapse:** The opening range high and low define the day's structure. If price breaks the OR with volume + delta confirmation, the day's trend is set.

### Order Flow
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s10-execution-and-trade-management.md`
- **Neuron:** The real-time measurement of aggressive buying vs. selling — market orders hitting the ask vs. market orders hitting the bid.
- **Synapse:** Price action without order flow is a silent movie. Order flow gives you the sound: who is winning, who is losing, and whether the move has conviction.

### Out-of-Sample Testing
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Neuron:** Saving 30% of historical data before backtesting — test the system on unseen data after optimizing on the first 70%.
- **Synapse:** If performance drops >50% on out-of-sample data, the system is curve-fit. If it drops >25%, it may still be fragile. This is the only real curve-fitting test.

### Overconfidence
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** The belief after a winning streak that "you figured it out" — leads to increasing size, skipping checks, and ignoring risk rules right before reversion.
- **Synapse:** Overconfidence is the stealthiest killer because it feels good. The antidote: re-read your 30-trade rolling stats after every win streak.

### Performance Metrics
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`, `systems/s01-mathematics.md`
- **Neuron:** The trailing 30-day calculations: win rate, avg R per trade, profit factor, max drawdown, recovery factor, Sharpe ratio.
- **Synapse:** Update weekly. Compare to backtest metrics. If live performance diverges >25% from backtest, the system needs re-evaluation.

### Petrodollar
- **Primary:** `08-forex-trading-the-purest-flow.md`
- **Secondary:** `14-monetary-plumbing-global.md`, `plumbing-hierarchy-master.md`
- **Neuron:** The system where oil is priced in USD and oil-exporting nations recycle their dollar revenue through US Treasuries — creating structural demand for dollars.
- **Synapse:** The petrodollar is the single largest source of structural USD demand; any shift (Saudi-China oil trading in yuan) is an existential threat to dollar hegemony.

### Pine Script
- **Primary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`
- **Neuron:** TradingView's built-in scripting language for custom indicators, multi-timeframe scanners, and simple backtesting strategies.
- **Synapse:** Fastest path from idea → working script. Zero setup, runs in browser. Use for scanning and alerts; switch to Python for complex logic.

### Pipe Theory
- **Primary:** `plumbing-hierarchy-master.md`
- **Secondary:** `06-day-trading-tap-the-flow.md`, `05-how-money-flows-in-the-system.md`
- **Neuron:** The system is designed to have money flow through specific pipes. A trader positions in the pipe; flow passes through their account on the way to its destination.
- **Synapse:** You do not create value or predict direction — you read the flow and place yourself in its path. This removes the pressure to be "right" and replaces it with the skill of reading flow.

### Pip Value
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** The monetary value of a single pip movement: Pip Value = (0.0001 or 0.01) × Lot Size. Varies by pair (JPY pairs are 2 decimal places).
- **Synapse:** The fundamental unit of P&L calculation. MES tick = $1.25, MNQ tick = $0.50. Know these numbers before you size a single position.

### Point of Control (POC)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s05-intraday-market-structure.md`
- **Neuron:** The price with the highest volume in a volume profile — the "fair price" consensus where most transactions occurred. Price gravitates back here like gravity.
- **Synapse:** Ranks #1 in level strength. Returns to POC with decreasing volume = mean reversion; returns with increasing volume = level breaking.

### Position Sizing
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`, `systems/s12-capital-management-and-scaling.md`
- **Neuron:** The calculation that converts risk % into actual trade size: Risk $ = Account × Risk%; Lots = Risk $ ÷ (Stop Pips × Pip Value per Lot).
- **Synapse:** Position sizing is more important than entry or exit. A good system with bad sizing fails; a mediocre system with excellent sizing survives.

### Post-Trade Record
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`
- **Neuron:** The post-exit journal entry: exit time, exit type, P&L ($ and R), MFE/MAE, emotional state, execution quality, lesson.
- **Synapse:** Fill out within 10 minutes of closing while memory is fresh. The post-trade record is the raw material for the weekly review and the emotional decision log.

### Power Hour
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** The final 30 minutes of options expiration (3:30-4:00 PM EST) — gamma approaches infinity, dealers hedge violently, volume is 2-3× normal.
- **Synapse:** The most mechanically reliable move of the week. Wait for the pin break, then ride the direction. Do NOT hold futures through 4:00 PM Friday.

### Pre-Trade Record
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`, `systems/s10-execution-and-trade-management.md`
- **Neuron:** The pre-entry journal fields: date, pair, direction, setup, TF, levels, risk amount, R:R, bias alignment, emotional state, thesis statement.
- **Synapse:** If you can't fill out the pre-trade record, you don't have a trade. The record is the gate: no record, no entry.

### Pre-Trade State Check
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`, `systems/s10-execution-and-trade-management.md`
- **Neuron:** A 2-minute scan before every trade: sleep, blood sugar, emotional baseline, urgency check, reason check, setup check. If any line fails, no trade.
- **Synapse:** The cheapest insurance in trading. 2 minutes prevents 90% of emotional mistakes. Skipping it 2 days in a row = gambling slope detected.

### Primary Dealer
- **Primary:** `core/money-creation-mechanism.md`
- **Secondary:** `14-monetary-plumbing-global.md`, `05-how-money-flows-in-the-system.md`
- **Neuron:** Banks authorized to trade directly with the central bank — they buy new government debt at auction and distribute it to the market.
- **Synapse:** Primary dealers are the transmission mechanism for QE/QT. When the Fed buys bonds, it buys from primary dealers, who then have reserves to lend.

### Profit Factor
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`
- **Neuron:** Gross Profits ÷ Gross Losses. PF > 1.5 = profitable, PF > 2 = very profitable, PF > 3 = suspiciously good (likely curve-fit).
- **Synapse:** The simplest system health check. PF < 1.0 after 60 trades = abandon the system. PF 1.5-2.5 = real edge.

### Pullback in a Trend
- **Primary:** `systems/s06-top-down-analysis.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s10-execution-and-trade-management.md`
- **Neuron:** When the daily chart pulls back in the opposite direction of the weekly trend, and the 1H chart reverses back toward the weekly direction.
- **Synapse:** This IS the Money-Generating Scenario. The most predictable, repeatable setup in existence. 4:1+ R:R with >60% win rate.

### Put Wall
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A strike with massive open interest in puts — dealers hedging puts sell futures as price drops, creating a liquidity floor that resists further downside.
- **Synapse:** Do NOT short below a put wall. Look for longs at the put wall with a stop below. If it breaks (rare), the floor collapses and price freefalls.

### Pyramiding
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Adding to a winning position as it moves in your favor — 1 unit at entry, 2 at +1R, 3 at +2R. Works ONLY if stop moves with each add.
- **Synapse:** Pyramiding without moving your stop increases average entry price and total risk. Always move stop to breakeven or previous entry point.

### R-Multiple
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`, `systems/s04-backtesting-and-system-development.md`
- **Neuron:** R = risk on a trade (stop distance). Every result is measured in R: +2R winner, −1R loser, +5R runner. Decouples performance from absolute dollars.
- **Synapse:** R-multiples are the universal language of trading performance. A $200 win is meaningless until you know the risk was $100 (2R) or $400 (0.5R).

### R:R Calculator (CLI)
- **Primary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Secondary:** `systems/s01-mathematics.md`
- **Neuron:** A command-line tool that computes R:R from entry, stop, and target: `python rr.py --entry 1.1050 --stop 1.1030 --target 1.1090`.
- **Synapse:** The fastest way to check R:R before entry without mental math. Use it until R:R estimation becomes automatic.

### Range Day
- **Primary:** `systems/s05-intraday-market-structure.md**
- **Secondary:** `systems/s06-top-down-analysis.md`, `systems/s07-order-flow-levels.md`
- **Neuron:** ~50% of days — price establishes a range in the opening drive and oscillates within it. Failed breakouts are the dominant pattern.
- **Synapse:** On range days, stop trying to trend-trade. Trade mean reversion at the range edges. If ADX < 20, range-day protocols are active.

### Recovery Factor
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`, `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** Net Profit ÷ Max Drawdown. > 3 = strong system. < 1 = your drawdown is bigger than your annual profit — reconsider the approach.
- **Synapse:** Recovery factor tells you if the returns are worth the pain. A high-return system with a 40% drawdown has a low recovery factor and will destroy you psychologically.

### Reflexivity
- **Primary:** `04-what-the-powerful-understand.md`
- **Secondary:** `plumbing-hierarchy-master.md`, `06-day-trading-tap-the-flow.md`
- **Neuron:** George Soros's theory that market participants' biased views influence market fundamentals, which in turn change participants' views — creating feedback loops.
- **Synapse:** Reflexivity explains why trends overshoot fundamentals (both up and down). Markets don't discover "true" prices; they create prices that change the underlying reality.

### Regime Detection
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`, `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** Classifying the current market as trending (ADX > 25) or ranging (ADX < 20) to determine which system to deploy.
- **Synapse:** Trade the regime, not your bias. A trend-following system is harmful in a range; a mean-reversion system is harmful in a trend. Know which regime is active.

### Revenge Trading
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`, `systems/s12-capital-management-and-scaling.md`
- **Neuron:** The urge to "win it back" immediately after a loss — driven by the amygdala's fight-or-flight response to financial threat.
- **Synapse:** Session over. Close everything. One loss is data; two in a row is a signal; three is a blow-up in progress. STOP AT TWO.

### Reversal Day
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** ~20% of days — price opens in one direction, fails at a key level, reverses across the opening range, and trends opposite.
- **Synapse:** Best traded by waiting for the reversal confirmation (break of OR high/low with delta) rather than anticipating it.

### Round Numbers
- **Primary:** `systems/s07-order-flow-levels.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`
- **Neuron:** Psychological price levels (1.1000, 5400, 100.00) where everyone places orders and stops. Weak alone, strong with volume profile confluence.
- **Synapse:** Ranks #8 in level strength. Alone, a round number is a suggestion. With VBPC (volume-by-price cluster at the round number), it becomes a fortress.

### RRP (Reverse Repo Facility)
- **Primary:** `core/liquidity-equation.md`
- **Secondary:** `14-monetary-plumbing-global.md`, `core/global-flow-map.md`
- **Neuron:** Money market funds park cash overnight at the Fed in exchange for Treasuries. RRP rising = money idle, not circulating (liquidity drain).
- **Synapse:** RRP is one of the three components of Net Liquidity. When RRP drops to zero, the liquidity tide has turned — QT starts biting.

### Scaling In/Out
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Entering or exiting a position in partial units rather than all at once. Scale in to improve average entry; scale out to capture profits while letting remainder run.
- **Synapse:** 50/50 scaling out (50% at +1R, 50% at +3R) gives you the same total profit as a full 2R exit while improving hit rate and psychological comfort.

### Semi-Automation
- **Primary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`
- **Neuron:** Code alerts you + you decide — the sweet spot between manual and fully automated. Scanner → Alert → Review → 1-Click Entry.
- **Synapse:** Do NOT build a trading bot in month 1. Start with analysis automation (journal parser, session timer, scanner). Move to execution only after 6+ months of verified edge.

### Session Architecture
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s13-options-mechanics-for-futures-traders.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** The daily macro structure: Overnight → Opening Drive → Lunch Lull → Closing Auction. Each phase has distinct volume, volatility, and trading behavior.
- **Synapse:** Knowing where you are in the session architecture tells you what kind of price action to expect and which system to deploy.

### Shadow Banking
- **Primary:** `core/money-creation-mechanism.md`
- **Secondary:** `14-monetary-plumbing-global.md`, `plumbing-hierarchy-master.md`
- **Neuron:** Non-bank financial intermediaries (money market funds, hedge funds, private credit) that perform bank-like functions without bank regulation — ~$4T+ daily in repo/reverse repo.
- **Synapse:** Shadow banking creates near-money that circulates outside regulated banking; when shadow banking freezes (2008, 2020), liquidity evaporates instantly.

### Sharpe Ratio
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`, `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** (Return − Risk-Free Rate) ÷ Standard Deviation of Returns. Measures risk-adjusted return. > 1 = decent, > 2 = excellent, > 3 = suspicious.
- **Synapse:** Sharpe penalizes upside volatility (big wins hurt the ratio). Use Sortino instead — it only counts downside volatility and is always ≥ Sharpe.

### SOFR/Repo
- **Primary:** `14-monetary-plumbing-global.md`
- **Secondary:** `core/liquidity-equation.md`, `core/money-creation-mechanism.md`
- **Neuron:** Secured Overnight Financing Rate — the cost of borrowing cash overnight backed by Treasury collateral. The new benchmark replacing LIBOR.
- **Synapse:** SOFR spikes = cash shortage in the banking system = stress. Repo market "tantrums" (Sep 2019) signal plumbing failures that precede broader crises.

### Sole Proprietorship (vs. Corporation)
- **Primary:** `systems/s11-trading-business-and-tax.md`
- **Secondary:** `systems/s12-capital-management-and-scaling.md`
- **Neuron:** A sole proprietor reports trading income on T2125, pays personal marginal rates + CPP. Incorporation at ~27% corporate rate makes sense above $100k net profit.
- **Synapse:** Do NOT incorporate before $100k consistent profit. Compliance ($1k-$3k/year) eats the tax savings at lower income. File as sole prop until Phase 3.

### Sortino Ratio
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`, `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** Same as Sharpe but only penalizes downside volatility. Fixes Sharpe's flaw of penalizing upside spikes.
- **Synapse:** Always use Sortino over Sharpe for evaluating trading systems. Sortino is always ≥ Sharpe because it only counts the volatility that hurts.

### Stacked Imbalances
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** Three or more consecutive price levels within a footprint candle showing the same-side imbalance — strong directional pressure.
- **Synapse:** Stacked imbalances = trend continuation is highly probable. Enter in the direction of the imbalance with confidence.

### Standard Deviation (Volatility)
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** A measure of how spread out price returns are — high σ = high volatility = wider stops needed. ∼95% of data falls within 2σ.
- **Synapse:** Don't calculate by hand; use TradingView's built-in Standard Deviation indicator. A reading of 2.0 means the typical daily move is 2.0 units.

### Stop Runs (Liquidity Sweeps)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** Price deliberately pushes through a known level to trigger stop-loss orders, then reverses — the aggressive trader absorbs the stop-triggered flow at a discount.
- **Synapse:** Confirmed by a wick below/above a key level + positive/negative delta at the wick (absorption of triggered flow). This IS the entry signal for reversal traders.

### Stopped Volume
- **Primary:** `systems/s07-order-flow-levels.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** A price level where a trend stopped — high volume at the trend exhaustion point. The opposite of POC (where volume confirms consensus).
- **Synapse:** Ranks #6 in level strength. Stopped volume marks where the trend died; price returning here is likely to respect it as resistance/support.

### Structural Levels
- **Primary:** `systems/s07-order-flow-levels.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`, `systems/s06-top-down-analysis.md`
- **Neuron:** Price levels derived from actual trading activity (volume profile, order flow) rather than geometry (Fibonacci, trendlines) — ranked by source of strength.
- **Synapse:** The strength hierarchy: POC > HVN > LVN > Previous Day VAH/VAL > Delta Pivot > Stopped Volume > Sweep Level > Round Number > Fib > Trendline.

### Structural Stop
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s07-order-flow-levels.md`
- **Neuron:** A stop placed beyond the wick of a sweep candle, or beyond an HVN — placed at a "real" level where price would invalidate the trade thesis.
- **Synapse:** Never use fixed pip stops (20 pips EUR/USD). Always place stops at structural levels. If the level is too far, skip the trade.

### Survivorship Bias
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Neuron:** Backtesting only includes symbols that still exist — the ones that went bankrupt were delisted and missing from the data. Your backtest misses the worst outcomes.
- **Synapse:** Trade major FX pairs and index futures (/ES, /NQ) — they don't go to zero. For stocks, include delisted names. For crypto, expect survivorship bias to inflate backtest results.

### Sweep Level
- **Primary:** `systems/s07-order-flow-levels.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** A price beyond an obvious liquidity level (previous high/low) that got "swept" (wicked through) before reversing. After the sweep, the level acts as support/resistance.
- **Synapse:** Ranks #7 in level strength. Do NOT short at the top of a sweep; do NOT buy at the bottom. Wait for the sweep and reversal confirmation, then enter.

### System (6 Components)
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`, `systems/s10-execution-and-trade-management.md`
- **Neuron:** A trading system requires all 6 components: entry, stop, target, filter, position sizing, and session rules. Without all 6, you have an idea, not a system.
- **Synapse:** Most retail has entry rules only. If you cannot write down all 6 components right now, you are gambling, not trading.

### TDA (Timeframe Discrepancy Analysis)
- **Primary:** `systems/s06-top-down-analysis.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`, `systems/s02-trading-psychology.md`
- **Neuron:** A framework for resolving conflicting signals across timeframes: Weekly up + Daily pullback + 1H reversal = best setup. Weekly range + Daily range + 1H chop = avoid.
- **Synapse:** TDA conflict is the #1 cause of frustration trading. When multiple timeframes disagree, the protocol is: wait for alignment OR skip the trade entirely.

### TGA (Treasury General Account)
- **Primary:** `core/liquidity-equation.md`
- **Secondary:** `core/global-flow-map.md`, `14-monetary-plumbing-global.md`
- **Neuron:** The US Treasury's cash account at the Fed. TGA rising = Treasury pulling money out of banking system (liquidity drain). TGA falling = spending injecting liquidity.
- **Synapse:** TGA is one of three Net Liquidity components. Debt ceiling resolutions allow TGA to refill (drain); spending bills drain TGA (inject). Track TGA weekly for risk asset direction.

### Three-Phase Model (Survival/Growth/Independence)
- **Primary:** `systems/s12-capital-management-and-scaling.md`
- **Secondary:** `CURRICULUM.md`, `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** The account growth model: Phase 1 (< $10k, 0.5% risk, don't blow up), Phase 2 ($10k-$50k, 1% risk, replace one expense), Phase 3 ($50k+, replace all expenses).
- **Synapse:** Attempting to skip a phase is the fastest way to return to Phase 1. Each phase has different rules, goals, and psychological demands. Respect them.

### Three-Pool Model
- **Primary:** `core/global-flow-map.md`
- **Secondary:** `plumbing-hierarchy-master.md`, `core/liquidity-equation.md`
- **Neuron:** Global liquidity pools in three interconnected reservoirs: Central Bank Reserves (narrow), Broad Money (M2/M3), and Near-Money (repo, Eurodollars, shadow banking).
- **Synapse:** Flow between pools determines asset price direction. Central bank → reserves → bank lending → broad money → spending → inflation. Monitor pool levels for regime shifts.

### Tilting
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** The state after multiple losses where rational decision-making is replaced by frustration-driven aggression — increasing size, ignoring setup rules, revenge mindset.
- **Synapse:** Tilting is detectable before it destroys the account. Early warning: skipping the pre-trade check, not journaling losing trades, increasing size after a loss.

### Tradovate API
- **Primary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Secondary:** `09-futures-trading-energy-and-receipts.md`
- **Neuron:** REST + WebSocket API for trading futures via Tradovate — OAuth 2.0, place/cancel orders, real-time quotes. Official Python SDK.
- **Synapse:** Do NOT touch the API until 6+ months of consistent manual profitability. Start with read-only (auto-journal), progress to 1-click semi-automation.

### Trailing Stop
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** A stop that moves with price as the trade goes in your favor — fixed distance, structure-based, or volatility-based (1.5×ATR).
- **Synapse:** For the first 6 months, do NOT trail. Let targets hit. Trailing adds complexity and often results in giving back too much profit.

### Trend Day
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** ~20% of days — price opens, finds liquidity, then trends in one direction all day with no significant pullback beyond the opening balance.
- **Synapse:** On trend days, let trades run. Use trailing stops or hold to target. Do NOT fade the edges — counter-trend trades on trend days get obliterated.

### Value Area (VAH/VAL)
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s05-intraday-market-structure.md`
- **Neuron:** The price range where 70% of volume traded — VAH (Value Area High) and VAL (Value Area Low) are the edges of institutional fair value.
- **Synapse:** Breaks above VAH with volume = buyers stepping up (trend up). Breaks below VAL with volume = sellers stepping down (trend down). Price inside VA = balanced auction.

### Volatility-Adjusted Sizing
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s01-mathematics.md`, `systems/s10-execution-and-trade-management.md`
- **Neuron:** Position size = (Account × Risk%) ÷ (ATR × 1.5). As volatility expands, position size shrinks; as volatility contracts, position size grows.
- **Synapse:** Superior for systems with variable stop distances and changing market volatility. Keeps risk % consistent across regimes — the stop adapts.

### Volatility Drag
- **Primary:** `systems/s01-mathematics.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** The reduction in geometric return caused by variance: Geometric Return ≈ Arithmetic Return − (σ² ÷ 2). Volatility literally erodes compounding.
- **Synapse:** Doubling position size more than doubles the drag. A 2% avg trade with 10% σ has 0.5% drag per trade. At 4% risk with 20% σ, drag = 2% per trade.

### Volume Profile
- **Primary:** `systems/s03-volume-profile-and-order-flow.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s05-intraday-market-structure.md`
- **Neuron:** Volume displayed per PRICE (not per time) — a vertical histogram showing where institutional interest clusters at each price level.
- **Synapse:** The single most important tool for identifying real support/resistance. Use TradingView's Fixed Range Volume Profile (free tier). The patterns are universal.

### Walk-Forward Analysis
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s14-algorithmic-and-semi-automated-trading.md`
- **Neuron:** A rolling out-of-sample test: backtest on 2023 data → test on 2024 Q1, then add Q1 to backtest → test Q2, and so on.
- **Synapse:** If the system holds up across each rolling window, it's robust. This is what pro quants do. Retail can simulate by comparing 3-month chunks.

### Weekly Bias
- **Primary:** `systems/s06-top-down-analysis.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** The one directional answer from the weekly chart: up, down, or nowhere. Determined by price vs. weekly EMA 21 and HH/HL vs. LH/LL sequence.
- **Synapse:** All intraday trades must align with the weekly bias. Weekly = direction, Daily = context, Intraday = execution. Violate this sequence at your own risk.

### Weekly Review
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`, `systems/s04-backtesting-and-system-development.md`
- **Neuron:** A 15-minute Sunday ritual: aggregate the week's trades, analyze losses for pattern vs. randomness, extract 1-2 focus items for next week.
- **Synapse:** The weekly review is the feedback loop that turns journal data into behavioral change. Without it, the journal is just record-keeping.

### 3-Strike Rule
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** After 3 consecutive losses OR daily loss limit → close all positions, walk away 2+ hours. Prevents a bad day from becoming a blown account.
- **Synapse:** 3 losses is still within statistical variance (6.4% with 60% WR), but the psychology of 3 losses triggers the revenge cascade. The rule stops the cascade before it starts.

### 7 Cognitive Defects
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `conversations/2026-07-29_arena-analysis.md`
- **Neuron:** Seven hardwired cognitive defects that are root causes of the Four Dangerous States: narrative addiction, temporal compression, prospect theory, agency illusion, social proof contamination, complexity bias, survival bias blindness.
- **Synapse:** Parts 1-4 manage symptoms. Part 7 treats root causes. Treating both is required for lasting psychological change.

### 14 Mental Exercises (Practice Regimen)
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** Fourteen daily/weekly drills (pre-mortem, devil's advocate, EV calibration, coin flip rewire, chart autopsy, rapid pattern drill, emotional replay, 5-second rule, silence training, drawdown simulation, what-did-I-miss review, distraction audit, gratitude close, reset protocol).
- **Synapse:** Without practice, psychology is theory. These exercises TRAIN the psychological muscles the same way backtesting trains the analytical muscles.

### 80% Rule (Value Area Re-Entry)
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s07-order-flow-levels.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** If price opens outside the prior value area and re-enters within 1-2 hours, ~80% probability of rotation to the opposite value area edge.
- **Synapse:** This is a testable mechanical rule. Add to your playbook and backtest across 50+ sessions.

### $ADD (NYSE Advance/Decline)
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`
- **Neuron:** Number of advancing NYSE stocks minus declining stocks. Confirms breadth of market moves. If /ES is up but $ADD is negative, the rally is narrow and likely to fail.
- **Synapse:** Use $ADD + $TICK together. $TICK shows speed of the move; $ADD shows whether it has support.

### $TICK (NYSE Tick)
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** Number of stocks on an uptick minus downtick. Range -2000 to +2000. >+1000 = overbought (fade). <-1000 = oversold (buy).
- **Synapse:** $TICK is a REVERSAL indicator, not a trend indicator. Use it to time fades, not to confirm direction.

### $VOLD (NYSE Volume)
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** Volume-weighted breadth. Divergence between $VOLD and price = reversal signal. Confirmation between $VOLD and price = real move.
- **Synapse:** $VOLD is the most reliable of the three internals because it weighs by volume. If price and $VOLD agree, the move is institutionally backed.

### Anti-Fragile Position Architecture (Probe → Confirm → Conviction)
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Enter 10-20% as probe (buy information), add 30-40% on confirmation, add remaining on structure break. Lose small when wrong; full-size when right.
- **Synapse:** Transforms position sizing from a SINGLE BET to a PROCESS. The probe IS the cost of learning. If you can't afford the probe, the trade is too big.

### Anti-Strategy Strategy
- **Primary:** `systems/s04-backtesting-and-system-development.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Identify the "obvious" trade everyone sees. Plan for its failure. If the obvious trade fails, trapped traders create a bigger move in the opposite direction.
- **Synapse:** The failure of the obvious trade IS the best trade. This is the "contra-trade" approach. Requires identifying what the herd expects.

### Biological Hedging
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `00-background-edge.md`
- **Neuron:** Sleep (7-9h), HRV monitoring (no trade if depressed), exercise (30m before trading), blood sugar management, box breathing under stress. The body IS the trading platform.
- **Synapse:** Performance physiology is not optional. A 5% drop in cognitive performance from poor sleep costs more in trading losses than any edge can recover.

### "Buy Information" Philosophy
- **Primary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Secondary:** `mental-models/information-half-life.md`
- **Neuron:** Every small initial position is a payment for information. If the probe loses, you learned "this level is not valid today." That information is worth the probe cost.
- **Synapse:** Reframes losses as tuition. The question is not "did I lose?" — it's "what did I learn?" If the answer is nothing, you didn't pay attention.

### Casino Mindset
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `mental-models/pipe-theory.md`
- **Neuron:** "I am the house, not the gambler." The house has an edge, takes many bets, and doesn't care about any single outcome. The gambler chases, hopes, and prays.
- **Synapse:** Every time you feel hope or prayer during a trade, you've switched from house to gambler. Close the trade. The next one is the house's bet.

### Catalyst Theory / Talent Stack
- **Primary:** `00-background-edge.md`
- **Secondary:** `mental-models/wealth-code-synthesis.md`, `conversations/2026-07-29_arena-analysis-catalyst.md`
- **Neuron:** The observation that rich people are not necessarily geniuses but structured masters of one asymmetric choke point — a catalyst they went pathological on for 5-15 years, built ownership around, and applied leverage to. The opposite of broad gathering.
- **Synapse:** "Interesting" is the enemy of "leverage." Broad curiosity feels like progress but is sophisticated procrastination for intelligent people. The game is not to know more — it's to own the bottleneck.

### Complexity Bias
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`
- **Neuron:** The brain mistakes complexity for sophistication. A 12-indicator system "feels" more reliable than a 2-line system. It's not. Complexity adds noise, not signal.
- **Synapse:** Your system should fit on a 3x5 index card. If it doesn't, strip until it does.

### Decision Quality Score
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`
- **Neuron:** Rate every trade 1-5 on decision quality INDEPENDENTLY of outcome. A good decision can lose. A bad decision can win. The DQ score is the signal; P&L is noise.
- **Synapse:** Track rolling 30-trade average DQ. If DQ drops below 3.5, your process is broken regardless of P&L. Fix the process first.

### Entropy Model of Markets
- **Primary:** `mental-models/pipe-theory.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`, `systems/s03-volume-profile-and-order-flow.md`
- **Neuron:** Markets oscillate between low-entropy (compression/order) and high-entropy (expansion/disorder). The transitions between these states are where nearly all extractable profit resides.
- **Synapse:** Humans trade price; elite traders trade entropy. Compression → anticipate expansion. Expansion with decreasing volatility → anticipate compression (range). This model unifies all regime detection.

### Information Contamination
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `mental-models/information-half-life.md`, `conversations/2026-07-29_arena-analysis.md`
- **Neuron:** Every piece of external opinion consumed before trading DEGRADES decision quality. YouTube, Discord, Twitter, Arena chats — all create anchoring bias.
- **Synapse:** Isolation first. Do your own analysis before consuming ANY external content. Use external input as a CHECK, not a SOURCE.

### Information Decay Curve (Half-Life)
- **Primary:** `mental-models/information-half-life.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`, `systems/s02-trading-psychology.md`
- **Neuron:** Every piece of information has a half-life: nanoseconds (order book), seconds (headlines), minutes (intraday structure), hours (daily patterns). Humans treat all information as equally current.
- **Synapse:** Using expired information = trading on noise. Know the half-life of the information you're acting on. Don't use level-2 prints from 30 seconds ago as entry rationale.

### Luck vs. Skill Column
- **Primary:** `systems/s09-journaling-and-performance-analysis.md`
- **Secondary:** `systems/s02-trading-psychology.md`
- **Neuron:** For every winning trade, classify as skill (setup matched backtest rules, execution per plan) or luck (worked but didn't match rules). Track both win rates separately.
- **Synapse:** If luck WR > skill WR over 60+ trades, you don't have an edge — you're getting lucky. The system needs revision, not celebration.

### Market Internal Dashboard
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`
- **Neuron:** $TICK, $ADD, $VOLD form the three-core internal dashboard for /ES and /NQ traders. Tells you whether the move is real before price confirms.
- **Synapse:** Check internals before every breakout trade. A breakout without internal confirmation is a trap 60%+ of the time.

### Narrative Addiction
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `conversations/2026-07-29_arena-analysis.md`
- **Neuron:** The brain demands a story for every price move. The story is almost always wrong, but the brain prefers a wrong story over no story. Leads to trading the narrative instead of the structure.
- **Synapse:** After every trade, answer "what was the STRUCTURAL reason?" (volume level, delta shift, structural break). If you can't, your trade was based on a story.

### "Next Bus" Mindset
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** "The market is a bus that comes every 5 minutes." If you miss one setup, another will come. There is no scarcity of opportunities.
- **Synapse:** FOMO disappears when you genuinely believe the next bus is minutes away. Scarcity is the enemy of patience.

### OPEX (Option Expiry) Pinning
- **Primary:** `systems/s13-options-mechanics-for-futures-traders.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`
- **Neuron:** Price gravitates toward the "max pain" strike price (where most options expire worthless) before monthly OPEX. After expiry, pinned volatility releases.
- **Synapse:** Check forexlive.com daily for large option expiries. $1B+ expiry at a strike = gravitational pull. Trade the pin AND the post-expiry breakout.

### "Pay the Toll" Model
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** Losses are not failures — they are TOLLS. Every road has a toll. The question is whether the toll is worth the destination. A toll is expected; a failure is a surprise.
- **Synapse:** Track your "toll" (total losses) as a separate line item. As long as the toll is less than the revenue, the road is profitable. The toll is not a mistake.

### Predator-Prey Market Ecosystem
- **Primary:** `mental-models/pipe-theory.md`
- **Secondary:** `systems/s03-volume-profile-and-order-flow.md`, `systems/s07-order-flow-levels.md`
- **Neuron:** Markets are a food chain. Your stops ARE the predator's food supply. Where most traders place stops → you should place entries. Where most traders place entries → you should place nothing.
- **Synapse:** This is the "anti-herd" execution model. Your entry should be where the herd's pain is (their stop-loss), not where their hope is (their entry).

### Prospect Theory (Loss/Gain Asymmetry)
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s08-advanced-risk-and-position-sizing.md`
- **Neuron:** Loss of $100 hurts ~2.25x more than gain of $100 feels good. Causes: hold losers too long, exit winners too early.
- **Synapse:** The only fix is mechanical: set exit rules BEFORE entry. The stop and target are not suggestions — they are protection against your own hardwired asymmetry.

### Second Move News Protocol
- **Primary:** `systems/s10-execution-and-trade-management.md`
- **Secondary:** `systems/s05-intraday-market-structure.md`
- **Neuron:** After high-impact data, wait for the initial spike (0-30 sec) → let the reaction range form (1-15 min) → trade the break of the reaction range in the direction of the daily/weekly trend.
- **Synapse:** The first move is noise (algo reaction). The second move is signal (institutional positioning). Ignore the first, trade the second.

### Sector Rotation (Market Cycle)
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s06-top-down-analysis.md`
- **Neuron:** Markets rotate through sectors in a predictable sequence during risk-on/risk-off cycles: Tech → Industrial/Materials → Energy → Utilities/Defensive → Gold/Treasuries.
- **Synapse:** Rotation from tech to utilities in 3 days = cycle is late, risk-off approaching. Rotation from defensives to tech = cycle restarting, risk-on.

### Social Proof Contamination
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s09-journaling-and-performance-analysis.md`
- **Neuron:** Seeing others make money creates urgency to act. You don't know their context, but your brain treats their success as evidence you should trade too.
- **Synapse:** Before opening any social feed, pre-write your session plan. Social feeds are post-session only. Treat as journal review material, not research.

### Survival Bias Blindness
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `systems/s04-backtesting-and-system-development.md`
- **Neuron:** You only see the traders who made it. The 95% who failed are invisible. This makes trading look easier than it is.
- **Synapse:** Before every session, read one story of a trader who blew up. Not to scare yourself — to remember that this is the baseline outcome. Survival is not guaranteed.

### Temporal Arbitrage / High-Information Moments
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `mental-models/pipe-theory.md`
- **Neuron:** The market reveals its hand at specific moments: first test of a level, first 5 min post-data, session transitions, first pullback in a trend. These moments contain 10-100x more actionable information.
- **Synapse:** Allocate 80% of attention to these 20% of moments. The rest of the time, do nothing. "Patience is a position" is literal — your capital is safest when you're waiting.

### Temporal Compression
- **Primary:** `systems/s02-trading-psychology.md`
- **Secondary:** `conversations/2026-07-29_arena-analysis.md`
- **Neuron:** The brain compresses price action bursts together, making you feel like you "missed" something. FOMO is temporal compression, not actual opportunity cost.
- **Synapse:** Wait for a candle close before ANY decision. The fact that you "saw it coming" after the fact is hindsight bias, not skill.

### Time-Based Edges
- **Primary:** `systems/s05-intraday-market-structure.md`
- **Secondary:** `systems/s10-execution-and-trade-management.md`
- **Neuron:** Predictable minute-level patterns: 9:30-9:50 initial drive, 9:50-10:10 first reversal window, 11:15 European close inflection, 14:00-15:30 closing auction, 15:30-15:50 MOC imbalance, 16:00 close surge.
- **Synapse:** These edges are specific enough to script. If an edge is not on the clock, it's not a time-based edge — it's a guess.

### Abundant vs Clean Supply (Water vs Boat)
- **Primary:** `mental-models/water-vs-boat.md`
- **Secondary:** `systems/CURRICULUM.md`, `core/repo-plumbing.md`
- **Neuron:** Markets differ by supply structure. FX/futures = abundant supply (deep, uncornerable, no one can see your order). Single stocks = clean supply (finite shares, one whale can move it). Abundant supply = water; clean supply = boat.
- **Synapse:** Trade the water first, boats as the end game. The FX/futures-first doctrine is a supply-structure argument, not a preference.

### Food Chain Tiers (Player Hierarchy)
- **Primary:** `plumbing-hierarchy-master.md` (Section 2.9)
- **Secondary:** `mental-models/water-vs-boat.md`
- **Neuron:** Tier 0 (Fed) → Tier 1 (Big 4 dealers) → Tier 2 (BlackRock/Vanguard) → Tier 3 (hedge funds/prop firms) → Tier 4 (mid-tier) → Tier 5 (sovereign/crypto) → Tier 6 (retail plankton). You sit where you sit; the map lets you pick your predators.
- **Synapse:** Prop firm = becoming a Tier 3 subcontractor. The way up is tier by tier — you feed on the tier above, get fed on by the tier below, until you eat the flow instead of being the flow.

### Repo Pawn Shop Model
- **Primary:** `core/repo-plumbing.md`
- **Secondary:** `mental-models/water-vs-boat.md`
- **Neuron:** Repo is a pawn shop for billionaires — sell the bond today, buy it back tomorrow at a slightly higher price. Nobody actually sells anything; the collateral is insurance, the trade is a loan. It exists so money moves without assets changing hands.
- **Synapse:** BlackRock lends bonds to JPMorgan because both win and neither disturbs the boat's price. The biggest flows are invisible — they happen in repo, off-exchange, never hitting the tape.
