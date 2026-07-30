# s09 — Journaling and Performance Analysis

## Part 1: Why Journal

Most traders don't journal. Most traders lose money. These are not unrelated.

Without a journal, you:
- Cannot separate luck from skill
- Cannot identify your actual edge (win rate, EV) from a sample
- Repeat the same mistakes across weeks because you never analyzed them
- Don't know what you do differently on green days vs. red days
- Have NO data to improve — you're flying blind

**With a journal, you can:**
- Calculate actual expectancy vs. perceived expectancy
- Identify your most profitable setups (by time, pair, level type)
- Spot behavioral patterns (e.g., "I always lose trades entered between 11-12pm")
- Track emotional state vs. trading performance
- Compare backtest results to live results

---

## Part 2: The Trade Journal Template

### Pre-Trade Record (before entering)

| Field | Example | Why |
|-------|---------|-----|
| Date/time | 2026-08-01 09:35 | Session tracking |
| Pair / Symbol | EUR/USD, /ES | Asset tracking |
| Direction | Long / Short | Which side |
| Setup Type | POC bounce, FVG, etc. | Pattern classification |
| Timeframe | 5m entry, 1H bias | TDA context |
| Levels (entry, stop, target) | 1.1050, 1.1030, 1.1090 | Where exactly |
| Risk amount ($) | $10 (0.1% of $10k) | Sizing check |
| R:R | 2:1 | Verify target |
| Bias alignment (from s06) | Weekly up, daily up, 1H down | TDA check |
| Emotional state (from s02) | Calm | Psychology check |
| Why are you taking this trade? | "Price at daily POC with delta divergence on 5m" | Logic — for review later |

### Post-Trade Record (after closing)

| Field | Example | Why |
|-------|---------|-----|
| Exit time | 2026-08-01 11:45 | Session tracking |
| Exit type | TP hit / Stop hit / Manual / Time | Categorize |
| P&L ($) | +$20 | Raw result |
| P&L (R) | +2R | Normalized result |
| Max favorable excursion (MFE) | +3.5R | How far price went in your favor |
| Max adverse excursion (MAE) | −0.8R | How far price went against you |
| Was execution as planned? | Yes / No | Discipline check |
| Emotional state at exit | Neutral / Euphoric / Frustrated | Psychology |
| Notes | "I hesitated on entry, entered 2 pips late. Missed 1R." | For improvement |

### Daily Summary (after session)

| Metric | Value |
|--------|-------|
| Trades today | 3 |
| Wins / Losses | 2 / 1 |
| Total P&L ($) | +$35 |
| Total P&L (R) | +3.5R |
| Best trade | +3R (EUR/USD POC bounce) |
| Worst trade | −1R (USD/JPY FVG — didn't wait for confirmation) |
| Biggest mistake | Entered USD/JPY before delta confirmed reversal |
| What to repeat | EUR/USD POC bounce setup — good patience, correct sizing |
| State before/during | Calm → first trade good → frustrated after loss → overtraded last pair |

---

## Part 3: Performance Metrics (Trailing)

Rolling calculations — update weekly.

### Core Metrics

| Metric | Formula | Target | Track |
|--------|---------|--------|-------|
| Win rate (last 30 days) | Wins ÷ total trades in rolling window | 40-60% | Weekly |
| Avg R per trade | Total R ÷ total trades in window | >0.5R | Weekly |
| Profit factor | Gross win ÷ gross loss | >1.5 | Monthly |
| Max drawdown | Peak to trough equity | <15% | Monthly |
| Recovery factor | Net profit ÷ MaxDD | >2 | Monthly |
| Sharpe (simplified) | Avg return ÷ σ of returns | >1 | Monthly |
| Win rate by setup | Wins for setup X ÷ total trades for X | Varies | After 20+ trades per setup |
| Win rate by session | Wins in London ÷ London trades | Varies | After 20+ trades per session |

### Behavioral Metrics (Monthly)

| Metric | Green Flag | Red Flag |
|--------|-----------|----------|
| % of trades taken on impulse (no pre-trade record) | <10% | >25% |
| % of trades that hit full target | >40% | <20% |
| % of trades moved to breakeven (premature) | <15% | >30% |
| % of trades where size deviated from plan | 0% | Any (1 = too many) |
| Avg daily trades | 2-5 | >8 (overtrading) |
| Worst loss vs. planned risk | = planned | > planned (not respecting stop) |

---

## Part 4: The Weekly Review Process

Every Sunday (or last session of the week — 15 min):

### Step 1: Aggregate the Week
- Count trades, wins, losses, total P&L, total R
- Calculate win rate, profit factor, avg R per trade
- Note: is this week above or below your 30-day rolling averages?

### Step 2: Analyze the Losses
The losses matter more than wins. For each losing trade:
- Was the stop at a valid level? (s07)
- Was the trade aligned with the daily trend? (s06)
- Was the psychology clean? (s02 state check)
- If all three are YES → the trade was correct but random. Acceptable loss.
- If any is NO → process it: what specifically went wrong? Document the fix.

### Step 3: Find Patterns

| If you see | Likely cause | Fix |
|------------|-------------|-----|
| Losses cluster in London session | London session is too fast for your processing speed | Limit to NY session or reduce size |
| Losing trades cluster on a specific pair | You don't understand that pair's behavior | Remove pair from watchlist; restudy its micro-structure |
| You lose more after a win | Overconfidence — reducing focus after a win | Add post-win state check (s02 Part 3) |
| You lose more after a loss | Revenge trading (s02, Dangerous State #2) | After any loss, take 30 min break before next trade |
| You keep losing on FVG setups | Your FVG entry rule is wrong | Backtest FVG setups separately (s04) or abandon that setup |

### Step 4: Plan Next Week
- What 1-2 things will you focus on? (e.g., "Reduce trade count to 5 max per day")
- What are you going to track specifically? (e.g., "MFE/MAE for all entries")
- What setup are you testing? (If you're developing a new system, note sample count)

---

## Part 5: The Emotional Decision Log

Alongside the trade journal, keep a **separate emotional decision log**. One line per entry:

| Date | Trigger (what made me deviate from plan) | Deviation | Emotional state (before) | Emotional state (after) | Cost ($) |
|------|------------------------------------------|-----------|--------------------------|-------------------------|----------|
| Aug 1 | Lost first trade, wanted to "get it back" | Increased size from 1% to 2% | Frustrated | Regret | −$40 |
| Aug 3 | Saw big green candle, FOMO | Entered without waiting for confirmation | Greed | Relief (it worked) then guilt | +$10 (but bad habit) |
| Aug 5 | Three losses in a row | Stopped trading for day | Resentment | Acceptance | Avoided losses |

The pattern becomes visible after 20 entries. Your specific triggers. Your specific responses. Most people don't get this insight because they never log their emotions. Your emotional decision log is the fastest lever for improvement.

---

## Part 6: Decision Quality Tracking

The most dangerous error in trading is judging by outcomes. A good decision can lose (bad outcome). A bad decision can win (good outcome). If you only evaluate by P&L, you will reinforce bad habits (because they won this time) and abandon good habits (because they lost this time).

### The Decision Quality Score

Rate every trade on decision quality INDEPENDENTLY of outcome:

| Score | Meaning | Example |
|-------|---------|---------|
| **5** | Perfect execution | Setup matched all rules, entry at exact level, stop at structural level, target hit. Textbook. |
| **4** | Good execution, minor imperfection | Setup was valid, entry 2 pips off ideal, still followed plan. |
| **3** | Acceptable | Setup was valid but execution had a flaw (entered too early, exited too late). |
| **2** | Poor | Entered without full confirmation, moved stop during trade, exited before target out of fear. |
| **1** | Gambling | No setup, no plan, sized up emotionally, revenge trade. |

### The Decision Quality Field

Add this to your journal template (Part 2):

| Field | Example | Why |
|-------|---------|-----|
| Decision quality (1-5) | 4 | Separates luck from skill. A winning trade with DQ=2 is still a bad trade. A losing trade with DQ=5 is a good trade. The score is the signal; P&L is noise. |

### The 30-Trade Rolling Decision Quality

Track your average DQ across the last 30 trades. If DQ drops below 3.5:
- Something is wrong with your process
- Review the last 10 trades with DQ < 3: what was common?
- Common causes: skipping pre-trade check, trading tired, trading during lunch lull, FOMO after seeing social media

### Luck vs. Skill Column

Separate from decision quality, add a simple field:

| Field | Options |
|-------|---------|
| Skill or luck? | **Skill** if setup matched backtest rules and execution was per plan. **Luck** if it worked but didn't match rules, or if you deviated from plan and it happened to work. |

Track your "luck" win rate vs. "skill" win rate. If luck rate > skill rate, your system isn't working — you're just getting lucky. If after 60 trades your luck win rate approaches your skill win rate, you don't actually have an edge.

---

## Synaptic Connections

| Neuron | Synapse | Fire When |
|--------|---------|-----------|
| `systems/s02-trading-psychology.md` | The emotional decision log in s09 is the data-collection tool for s02's Dangerous States. Without the log, s02 is theory. With the log, s02 becomes actionable diagnosis. | Logging emotional state; reviewing journal |
| `systems/s04-backtesting-and-system-development.md` | s09's live performance metrics are compared to s04's backtest metrics. If they diverge >25% from backtest, the system needs re-evaluation. | Comparing live vs. backtest results |
| `systems/s01-mathematics.md` | Every metric in s09 (R, avg R, profit factor, Sharpe) is defined in s01. The journal's numbers have meaning only because s01 defined them. | Computing performance metrics |
| `systems/s08-advanced-risk-and-position-sizing.md` | s09's performance metrics (win rate, R) feed into s08's Kelly calculation. The journal tells you your actual edge; s08 uses that for sizing. | Determining position size from actual performance |
| `systems/s05-intraday-market-structure.md` | Session-based win rate analysis in s09 (wins by session) feeds back into s05's session framework. If you win more in London, allocate more focus there. | Analyzing session-based performance |
| `systems/s10-execution-and-trade-management.md` | MFE/MAE analysis (s09 Part 2) feeds back into s10. If MFE is consistently higher than realized exit, your exit strategy is wrong (leaving money on the table). | Refining exit rules based on MFE/MAE data |
| `systems/s00-concept-registry.md` | Each setup type in the journal maps to a concept in the registry. Make entries like "POC bounce": definitions, win rate, notes. | Building the concept registry |
| `systems/s02-trading-psychology.md` | Decision quality tracking (Part 6) directly supports s02's cognitive defects — especially Agency Illusion (Defect 4) and Survival Bias (Defect 7). The DQ score is the objective check on self-deception. | Reviewing a winning trade that felt good; DQ score keeps it honest |
