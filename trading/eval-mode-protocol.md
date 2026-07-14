# EVAL MODE PROTOCOL — Passing the Prop Firm Challenge

## "The eval is not a test. It's training for how you'll trade real capital."

---

## THE CORE DIFFERENCE

| Dimension | Eval Mode | Funded Mode |
|-----------|-----------|-------------|
| **Goal** | Hit profit target without breaching max drawdown | Compound consistently, take monthly payouts |
| **Risk per trade** | 0.25-0.5% of account | 0.5-1% of account |
| **Max daily loss** | 1-2% (firm dependent) | 2-3% |
| **Max trades** | 1-2 per day | 2-3 per day |
| **Position sizing** | Micro only — 1 MES or 1 MNQ | Scale to 2-3 contracts |
| **Psychology** | "I can't lose this account" | "I can always get another funded account" |
| **Time horizon** | Days to weeks (hit target) | Months to years (compound) |
| **Exit strategy** | Take profits faster, trail tighter | Let winners run, wider trails |

**Golden rule for eval:** You're not trying to hit the target fast. You're trying to pass while proving you have a consistent edge. The firms know this. The ones with the highest profit targets and shortest time limits are designed to fail you.

---

## THE PROP FIRM PARAMETERS

### Goat Funded Trader (Recommended Start)

| Parameter | Value |
|-----------|-------|
| Eval type | 1-step |
| Profit target | 10% |
| Max daily loss | 4% |
| Max total loss | 6% |
| Time limit | None |
| Profit split (funded) | 80-100% |
| Min trading days | 5 (recommended) |
| Platform | MT5 |

**The best first eval because:** No time limit means you can trade 0.25% risk for 40 trading days and hit the target without breaking a sweat. No rush.

### FTMO

| Parameter | Value |
|-----------|-------|
| Eval type | 2-phase |
| Phase 1 target | 10% |
| Phase 2 target | 5% |
| Max daily loss | 5% |
| Max total loss | 10% |
| Time limit | Unlimited (paid account) |
| Min trading days | 4 per phase |
| Profit split | 80-90% |
| Platform | MT5 |

**Consider after passing Goat first.** Two-phase is harder psychologically — you pass Phase 1, then have to do it again. But FTMO is the most reputable firm in the industry.

### Apex Trader Funding

| Parameter | Value |
|-----------|-------|
| Eval type | 1-step |
| Profit target | Varies by account size |
| Max daily loss | Varies |
| Max total loss | Varies (trailing) |
| Time limit | 7 days minimum |
| Profit split | 100% first $25K, then 90% |
| Platform | Rithmic / NinjaTrader |

**Best for scaling after proven.** Apex allows multiple eval accounts and combines them. Start with Goat, then scale with Apex once you have a track record.

### Comparison: Daily Loss Rules

The single most important parameter. Know your firm's exact rule:

| Firm | Daily Loss Calculation | Breach Behavior |
|------|----------------------|-----------------|
| Goat | Daily loss = P&L of current day only (reset to 0 at market close) | Account closed, can reset at reduced fee |
| FTMO | Daily loss = equity at 5PM ET previous day minus current equity | Account closed, must repurchase |
| Apex | Trailing loss = highest equity minus current equity | Account closed, can reset at fee |
| Topstep | Daily loss = realized + unrealized P&L for current session | Combine reset available |

**Your rule:** Know the daily loss limit for YOUR firm. Set your personal max at 50% of their limit. If their daily loss is 4%, your personal max is 2%. You never want to hit their limit — only your own.

---

## EVAL TRADING RULES

### Rule 1: Size Down by 50% vs Funded

| Account Size | Eval Risk/Trade | Eval $ Risk | MES Contracts | MNQ Contracts |
|-------------|-----------------|------------|--------------|--------------|
| $5,000 eval | 0.25% ($12.50) | $12.50 | 1 (10pt stop) | 1 (10pt stop at $20 = push size) |
| $10,000 eval | 0.25% ($25) | $25 | 1 (20pt stop) | 1 (12pt stop) |
| $25,000 eval | 0.25% ($62.50) | $62.50 | 1 or 2 (tight) | 2 (tight stops) |
| $50,000 eval | 0.25% ($125) | $125 | 2 (25pt stop) | 2 (30pt stop) |

**Hard rule:** Never trade more than 1-2 contracts during eval. Nothing bigger.

### Rule 2: Daily Target = 0.5% (Not the Profit Target)

Do not try to hit the 10% profit target in one day. That's gambling.

| Account | Daily Target ($) | Days to 10% at 0.5%/day |
|---------|-----------------|------------------------|
| $5,000 | $25 | 20 trading days (1 month) |
| $10,000 | $50 | 20 trading days |
| $25,000 | $125 | 20 trading days |
| $50,000 | $250 | 20 trading days |

**The math:** 0.5% per day for 20 days = 10%. If you miss days or have losses, it takes 25-30 trading days. That's fine. No time limit on Goat.

### Rule 3: Stop After 2 Consecutive Losses

In eval mode, two losses in a row isn't just bad luck — it's a signal.

| Scenario | Action |
|----------|--------|
| 2 losses in a row | Stop trading for the day. Review journal. Check if plumbing signal shifted. |
| 2 losses in 3 days | Reduce size by 50%. You're off your game. |
| Weekly loss > 3% | Stop trading for the week. Read plumbing. Find the disconnect. |

**In eval, the account IS your opportunity.** Losing the eval costs you the fee + the time + the momentum. Preserving the account is more important than hitting the target.

### Rule 4: Take Profits at 1:1 R:R Minimum

In eval mode, you don't need 1:3 or 1:4 home runs. You need consistent singles.

| Setup Quality | Min R:R for Eval | Notes |
|-------------|-----------------|-------|
| A+ (all 5 MMM elements perfect) | 1:1 | Let it run to 1:2 if trend is strong |
| B (3-4 elements) | 1:1 | Take the 1:1, don't get greedy |
| C (1-2 elements) | Do not trade | This is how you blow evals |

### Rule 5: Trade Only Your Best Instrument

During eval, do not switch between MES and MNQ. Pick one and stay with it.

| Instrument | Eval Suitability | Why |
|-----------|-----------------|-----|
| MES | **Best for eval** | Slower moves, tighter stops, cleaner structure. Easier to manage risk. |
| MNQ | Secondary | Faster moves can trigger daily loss limit before you react. Only after MES is proven. |
| EUR/USD | Third | Only if you have 30+ demo trades positive expectancy. Use ORB strategy only. |
| USD/CAD | Fourth | Oil correlation adds variable. Stick to MES for first eval. |

---

## THE EVAL PSYCHOLOGY LAYER

### The 4 Emotional Stages of an Eval

| Stage | When | Feeling | What to Do |
|-------|------|---------|------------|
| **Excitement** | Day 1-3 | "I'm going to pass this fast" | Calm down. Trade your smallest size. Let the first week be observation. |
| **Fear** | After first 2% drawdown | "I'm going to blow this" | You're still 4% from max loss. Breathe. Size down to 0.25% or flat for 2 days. |
| **Boredom** | Day 10-15 of consistent 0.5% days | "This is too slow, I should size up" | This is the trap. This is where evals get blown. Size stays the same. |
| **Completion** | Within 3% of target | "Almost there, one big trade" | NO. This is the most dangerous moment. Trade smaller. Close it out with singles. |

### The Pre-Eval Mental Checklist

Before you purchase any eval:

- [ ] Do I have 60+ demo trades with positive expectancy? (see CURRICULUM Phase 5)
- [ ] Have I been trading my pre-session daily for 30+ consecutive days?
- [ ] Have I journaled every demo trade?
- [ ] Is my plumbing data workflow a habit (not something I have to think about)?
- [ ] Am I willing to trade 1 MES for 25 trading days to hit 10%?

**If any answer is NO → go back to demo.** The eval is not for learning. It's for proving.

---

## THE FUNDED MINDSET

Once you pass and get funded, the rules change:

| Rule | Eval | Funded |
|------|------|--------|
| Risk per trade | 0.25% | 0.5-1% |
| Daily target | 0.5% | 1% |
| Max trades | 1-2 | 2-3 |
| Position size | 1 contract | 1-3 contracts |
| Profit taking | 1:1 R:R minimum | Let winners run to 1:2+ |
| Correlation | Avoid correlated positions | Can layer correlated positions |

**The biggest mistake funded traders make:** They trade funded accounts the same way they traded the eval. The eval teaches you risk control. The funded account teaches you how to let winners run. They are different skills. Practice both.

---

## THE EVAL ROUTINE (During Challenge)

```
PRE-SESSION (15 min)
  ☐ Plumbing data check (systems/live-data-workflow.md)
  ☐ Eval check: current P&L, distance to daily loss limit
  ☐ Set today's max loss based on eval rules (50% of firm limit)
  ☐ Set today's profit target: 0.5% of account
  ☐ Instrument: MES only (unless you've proven MNQ in demo)

SESSION (max 2 hours)
  ☐ 1-2 trades maximum
  ☐ 0.25% risk per trade
  ☐ Take 1:1 if offered. Let 1:2 run only on A+ setups.
  ☐ If hit 0.5% target → stop. Done for the day.
  ☐ If hit daily loss limit (your 50% rule) → stop. Done for the day.
  ☐ No revenge. No doubling. No "one more trade."

POST-SESSION (5 min)
  ☐ Journal every trade
  ☐ Eval P&L update
  ☐ Distance to profit target
  ☐ One sentence: "Today I [did/did not] follow the eval protocol."
```

---

## REFERENCES

- **Prop firm comparison:** `trading/prop-firm-playbook.md` — full firm specs, costs, nuances
- **MES/MNQ execution:** `trading/mes-mnq-playbook.md` — entry rules, R:R tables
- **Position sizing by liquidity:** `systems/position-sizing-by-flow.md` — adjust eval size by regime
- **Commandments (pre-session read):** `trading/trading-commandments.md` — 10 rules
- **Plumbing to trade bridge:** `systems/plumbing-to-trade-bridge.md` — which edge to trade based on today's data
- **Daily schedule:** `systems/3hr-daily-schedule.md` — how eval mode fits into the 3-hour block
- **Live data workflow:** `systems/live-data-workflow.md` — plumbing check before every eval session
- **Demo path (pre-eval prep):** `quickstart/03-demo-path.md` — 30-day plan
- **Curriculum Phase 5:** `CURRICULUM.md` lines 155-220 — demo phase milestones
- **Wealth Rule Book (your vault):** "The wealthy don't take more risk. They take better-structured risk."
