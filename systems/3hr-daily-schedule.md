# 3-HOUR DAILY SCHEDULE — The Operating System

## "The pre-session, the journal, the plumbing check — these are NOT optional extras."

---

## THE DAILY BLOCK

**3 hours per day.** Every day. No exceptions. Structure rotates between trading days and study days.

```
                    ┌───────────────────────────────┐
                    │       DAILY 3-HOUR BLOCK        │
                    │    (flexible scheduling below)   │
                    └───────────────────────────────┘
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
   ┌──────────────────┐                               ┌──────────────────┐
   │  TRADING DAYS     │                               │  STUDY DAYS       │
   │  (Mon-Fri,        │                               │  (trading off or  │
   │   session active) │                               │   weekend)        │
   └──────────────────┘                               └──────────────────┘
```

---

## TRADING DAY SCHEDULE (Mon-Fri, NY Session)

### Block A: Pre-Session Prep (30 min before market open)

```
TIME          ACTIVITY                    TOOL                      CHECK
───           ────────                    ────                      ─────
:00-:15       Live data workflow          systems/live-data-        ☐ No skipping
                                          workflow.md               this step
             Open 5 URLs, record
             6 numbers, compute Net
             Liq, get verdict

:16-:20       Chart prep                 TradingView               ☐ Levels marked
             Mark ORB range, VWAP,                                 ☐ Bias set
             key levels, session lines

:21-:25       Commandments read          trading/trading-           ☐ 10 rules
             (read aloud if possible)     commandments.md            read aloud
             "Protect the account
             first"

:26-:30       Session plan written       Paper or notepad          ☐ 2 lines written
             "I will [setup] at                                      (see live-data-
             [level]..."                                             workflow.md)
```

### Block B: Trading Session (60-90 min)

```
TIME (PT)    ACTIVITY                    RULES
───          ────────                    ─────
6:30-7:00    NY Open — watch only        ☐ No trades. First 15-min
                                          candle sets ORB range.
                                          
7:00-7:30    Execute if setup triggers   ☐ Max 1-2 trades
                                         ☐ 0.25-1% risk per trade
                                         ☐ Record screenshot
                                         
7:30-8:00    Continue session or stop    ☐ If target hit → stop
                                         ☐ If 2 consecutive losses
                                            → stop for the day
                                         ☐ If plumbing says "flat"
                                            → study instead

[9:00-10:30] LUNCH CHOP — DO NOT TRADE   ☐ Read plumbing if session
                                          was short

[10:30-11:30] POWER HOUR (optional)      ☐ Only if morning was clean
                                          ☐ 1 trade maximum
```

### Block C: Post-Session Review (15 min)

```
TIME          ACTIVITY                    CHECK
───           ────────                    ─────
+0:00         Journal every trade        ☐ Screenshot chart + entry/exit
                                          ☐ 1-2 sentences per trade
                                          ☐ R multiple recorded

+0:05         Session summary            ☐ Did bias match what price did?
                                          ☐ Did I follow the plan?
                                          ☐ One thing to improve

+0:10         Update tracker             ☐ Running P&L updated
                                          ☐ Daily / weekly / monthly
                                          ☐ Note: tomorrow's key level
```

### Block D: Study Time (remaining 45-75 min)

```
TIME          ACTIVITY                    COMMITMENT
───           ────────                    ─────
Remaining     Study plumbing or           ☐ 45-75 min minimum
              mental model NOT            ☐ No charts during this time
              related to today's trades    ☐ Focus on understanding, not
              (see study day schedule)       performance review
```

---

## STUDY DAY SCHEDULE (Non-Trading Days / Weekends)

### Weekly Rotation

| Day | Study Focus | Primary File(s) | Secondary |
|-----|-------------|-----------------|-----------|
| **Sunday** | Weekly plumbing prep | `systems/weekly-flow-checklist.md` + COT report | Set bias for Monday |
| **Monday** | After trading: journal review only | Trade journal + performance metrics | — |
| **Tuesday** | Esoteric plumbing | `core/plumbing-esoterica.md` (2 sections) | Add glossary note |
| **Wednesday** | Mental models | `mental-models/pipe-theory.md` or whichever needs reinforcement | Write journal entry |
| **Thursday** | Strategy refinement | Read your last 20 trade screenshots | What patterns worked? |
| **Friday** | Prep for next week | COT data + plumbing check + level set | — |
| **Saturday** | Deep dive or rest | `plumbing-hierarchy-master.md` — one Part per hour | Push new Feynman terms |
| **Saturday** | **OR: Rest day** | No screens. No charts. Walk outside. | — |

### Study Day Block Structure

```
:00-:15     Review yesterday         What did I learn? What's fuzzy?
:16-:45     Read primary file        45 min — mark 3 fuzzy terms
:46-:55     3 Feynman breakdowns     10 min — write in Part 11 of
                                      plumbing-hierarchy-master.md
:56-:70     MAP.md update            Add any new terms, update cross-refs
:71-:80     Journal                  One page: "What I know now that I
                                      didn't know 3 hours ago"
:81-:90     Growth protocol push     git add -A && commit && push
```

---

## THE WEEKLY TIME BUDGET

### Per Week (7 days × 3 hours = 21 hours)

| Activity | Hours/Week | % of Total |
|----------|-----------|------------|
| Live data workflow | 1.5 | 7% |
| Trading session (active chart time) | 6-9 | 29-43% |
| Journaling + review | 1.5 | 7% |
| Plumbing study | 4.5 | 21% |
| Strategy refinement + edge study | 3 | 14% |
| Mental models + philosophy | 1.5 | 7% |
| Growth protocol (push, update maps) | 1 | 5% |
| **Total** | **19-22** | **~100%** |

---

## THE 4-DAY TRADING WEEK TEMPLATE

Most weeks have 5 trading days. Plan for 4 active + 1 flex.

```
MON ── Trade ── Study: weekly plumbing check + COT
TUE ── Trade ── Study: plumbing-esoterica or mental model
WED ── Trade ── Study: EIA day playbook review
THU ── Trade ── Study: trade journal review + screenshots
FRI ── Flex ─── Trade if 3 consecutive good days / Study if not
SAT ── Deep dive or rest
SUN ── Weekly plumbing prep for Monday
```

---

## WHEN THE SCHEDULE BREAKS

Life happens. Missed sessions happen. Here's the protocol:

### Missed 1 day
- No catch-up. Skip it. Resume the next day.
- Do not double up. Do not trade on back-to-back 2-hour sessions to "make up" time.

### Missed 2 consecutive days
- Resume with a study day, not a trading day.
- Run the live data workflow 3 days in a row without trading. Recalibrate.
- The market doesn't care that you missed time. Jumping back in cold = losing money.

### Missed 1 week
- Resume with 3 study days in a row.
- Read `mental-models/pipe-theory.md` again from scratch.
- Demo trade for 5 sessions before touching live.

### Missed 1 month
- Restart from CURRICULUM Phase 2 (Systems & Ritual). Do not skip.
- The discipline atrophies faster than the knowledge.

---

## THE DAILY PRE-SESSION RITUAL (Summary Card)

Print this. Pin next to your screen.

```
┌─────────────────────────────────────────────────────────────┐
│                  DAILY RITUAL — 3-HOUR BLOCK                 │
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

## REACTIVATING THE SCHEDULE AFTER THIS FILE

**These command strings reactivate the entire schedule from one instruction:**

Say `RUN RITUAL` → system reads `systems/3hr-daily-schedule.md` → activates the daily block
Say `STUDY MODE` → system loads the study day schedule → focuses on one file + Feynman + push
Say `TRADE MODE` → system loads the trading day schedule → live data workflow → session

---

## REFERENCES

- **Live data workflow:** `systems/live-data-workflow.md` — runs during pre-session
- **Plumbing-to-trade bridge:** `systems/plumbing-to-trade-bridge.md` — decision trees
- **Daily pre-session detail:** `systems/daily-pre-session.md` — full chart prep
- **MES/MNQ playbook:** `trading/mes-mnq-playbook.md` — what to execute during session
- **Eval mode protocol:** `trading/eval-mode-protocol.md` — when in prop eval
- **Fill your cup:** `trading/fill-your-cup.md` — the long game
- **Commandments:** `trading/trading-commandments.md` — read before every session
- **Curriculum:** `CURRICULUM.md` — full study path this schedule feeds into
- **Growth protocol:** `GROWTH_PROTOCOL.md` — how the system grows with every session
