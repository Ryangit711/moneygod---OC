# MONEYGOD — OC MASTER MAP (Scoped to Trading Mastery)

## (57 files · ~16,500 lines · 6 phases · 25 lexicon terms · Updated 2026-07-23)

*This is the bird's eye view of moneygod---OC only. For the full system view across all repos, see aman-os/ARCHITECTURE/MASTER_MAP.md.*

---

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    MONEYGOD — OC  (CASH ENGINE)                                ║
║         "Money is concentrated human time and energy."                          ║
║         "The flow exists. Your job: read the plumbing, sit in the pipe."       ║
║                                                                                  ║
║         57 files · ~16,500 lines · 6 phases · 25 lexicon terms                  ║
║         STATUS: ACTIVE PERMANENTLY (the cash engine)                            ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

---

## THE PATH — 6 Phases to Funded Trader

```
P0 (Foundations)    → What money actually is
P1 (Plumbing)       → How money moves (the machine)
P2 (Systems/Ritual) → Discipline before strategy
P3 (Mental Models)  → Mind before method
P4 (Trading)        → Tapping the flow (demo)
P5 (Prop/Live)      → Get funded. First payout. Repeat.
```

```
Week    Phase   What
─────────────────────────────────────────────────
1       P0      What money is — origins, debt, economy
2       P0      Internalize — explain it to someone else
3       P1      Plumbing — repo, flows, liquidity equation
4       P1      Esoterica — Eurodollar, XCCY, FRA-OIS
5       P2-3    Systems + Mental models — ritual before strategy
6-7     P4      Chart foundations — watch, don't trade
8-12    P5      Demo — 60 trades, positive expectancy
13+     P6      Prop eval → funded → compound → freedom
```

---

## THE PLUMBING — How Money Moves

```
CENTRAL BANK PUMP
    │
    ▼
┌─────────────────────────────────────────────────────┐
│  CB Reserves ──▶ Commercial Bank Credit              │
│                   │                                   │
│                   ▼                                   │
│  Three-Pool Model:                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │  BANKS   │─▶│   GOV    │─▶│ MARKETS  │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│                   │                                   │
│                   ▼                                   │
│  Net Liq = ΔCB BS − ΔTGA − ΔRRP                    │
│  (The formula that reads global liquidity)           │
└─────────────────────────────────────────────────────┘
    │
    ▼
YOUR JOB: Sit in the pipe as flow passes through
```

---

## FILE INVENTORY

```
moneygod---OC/
├── CURRICULUM.md              ← Front door (6-phase study path)
├── MAP.md                     ← Master map (all files, all connections)
├── GROWTH_PROTOCOL.md         ← Living system heartbeat
├── plumbing-hierarchy-master.md ← 3,307 lines, 12 parts (the deep dive)
│
├── ROOT (15 numbered files)   ← Core curriculum
│   ├── 01-origins-of-money-and-debt.md
│   ├── 02-the-real-meaning-of-economy.md
│   ├── 03-money-as-debt-modern-system.md
│   ├── 04-what-the-powerful-understand.md
│   ├── 05-how-money-flows-in-the-system.md
│   ├── 06-day-trading-tap-the-flow.md
│   ├── 07-what-money-actually-is-no-bs.md
│   ├── 08-forex-trading-the-purest-flow.md
│   ├── 09-futures-trading-energy-and-receipts.md
│   ├── 10-investing-and-compounding.md
│   ├── 11-escaping-the-rat-race.md
│   ├── 12-who-knows-this-level.md
│   ├── 13-weekly-flow-tapping-operating-system.md
│   ├── 14-forex-clock-resources.md
│   └── 14-monetary-plumbing-global.md
│
├── core/                      ← Deep plumbing (6 files, 1,937 lines)
│   ├── global-flow-map.md         (689 lines, 18-region master)
│   ├── liquidity-equation.md      (122 lines, Net Liq formula)
│   ├── money-creation-mechanism.md (120 lines, per-region)
│   ├── plumbing-esoterica.md      (646 lines, insider knowledge)
│   ├── repo-plumbing.md           (188 lines, SOFR/repo)
│   └── tri-region-flow-map.md     (172 lines, US→CA→EU)
│
├── mental-models/             ← Mind before method (3 files, 533 lines)
│   ├── pipe-theory.md             (145 lines, core model)
│   ├── wealth-code-synthesis.md   (129 lines, pyramid × pipe)
│   └── 10-level-mastery-path.md   (259 lines, 18-month path)
│
├── systems/                   ← Discipline framework (9 files)
│   ├── daily-pre-session.md       (209 lines, 5-min ritual)
│   ├── position-sizing-by-flow.md (223 lines, size by regime)
│   ├── weekly-flow-checklist.md   (135 lines, 15-min check)
│   ├── live-data-workflow.md      (15-min morning check)
│   ├── plumbing-to-trade-bridge.md (decision trees)
│   ├── 3hr-daily-schedule.md      (the daily OS)
│   ├── gangotri-protocol.md       (integration master)
│   └── accumulation-distribution-syllabus.md (12-week learning)
│
├── trading/                   ← Execution (9 files)
│   ├── complete-strategy-orb-eurusd.md (ORB + London breakout)
│   ├── prop-firm-playbook.md     (~200 lines, 11 firms, 2026 data)
│   ├── trading-commandments.md   (70 lines, 10 rules — READ DAILY)
│   ├── mes-mnq-playbook.md       (MES/MNQ execution)
│   ├── eval-mode-protocol.md     (prop eval rules)
│   ├── fill-your-cup.md          (first payout to freedom)
│   ├── paper-vs-live-gap.md       (~250 lines, execution gap bible)
│   ├── prop-firm-architecture.md  (~300 lines, master prop firm map)
│   └── multi-account-gateway.md   (~200 lines, multi-account architecture)
│
├── quickstart/                ← Day-1 setup (4 files, 564 lines)
├── references/                ← 70+ books/papers/tools
└── conversations/             ← Session records
```

---

## THE THREE LAWS

```
LAW 1 — Money is not real. Social construct backed by force.
         Banks create it from nothing as debt. System requires
         perpetual growth or it collapses.

LAW 2 — The flow exists. CBs pump > banks route > institutions
         position > retail provides exit liquidity. Your job: read
         the plumbing, sit in the pipe.

LAW 3 — The goal is not infinite money. The goal is to hit your
         freedom number and take back control of your time.
```

---

## THE BRIDGE TO TRADING

```
PLUMBING (How it works)        BRIDGE (Translation)      TRADING (What you do)
│                               │                         │
│  Money is debt                │  Live Data Workflow      │  Commandments
│  CB reserves                  │  Plumbing-to-Trade       │  MES/MNQ Playbook
│  Repo/SOFR                    │  Bridge Decision Trees   │  Eval Mode Protocol
│  TGA · RRP                    │  Gangotri Protocol       │  ORB Strategy
│  Liquidity equation           │  3hr Daily Schedule      │  Fill Your Cup
│                               │                         │
│  "The Machine"                │  "The Nervous System"    │  "The Hands"
```

---

## STATUS

| Metric | Value |
|--------|-------|
| Status | ACTIVE PERMANENTLY |
| Lifespan | Permanent (the cash engine) |
| Total files | 57 |
| Total lines | ~16,500 |
| Phases | 6 |
| Lexicon terms | 25 |
| Core plumbing | 6 files (1,937 lines) |
| Master reference | 1 file, 12 parts, 3,307 lines |
| External references | 70+ |

---

## CONNECTIONS

| Connected To | How | Direction |
|-------------|-----|-----------|
| **aman-os** | LINKS.md — shared identity, ripple out | moneygod → aman-os (inward only) |
| **ABHIMANYU-2.0** | None — they don't know about each other | — |

---

*"The cash engine runs forever. Every study session, every trade, every term — the system only grows."*
