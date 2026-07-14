# PLUMBING-TO-TRADE BRIDGE — From Liquidity Verdict to Trade Decision

## "The plumbing tells you where the flow HAS to go. Your job is to get in the pipe."

---

## CORE PRINCIPLE

**This file is the ONLY place where plumbing concepts meet trade decisions.** It does not re-explain plumbing. It references plumbing files for depth. It does not define trade setups. It references trading files for those.

Its sole purpose: **take today's plumbing data and output a tradeable verdict.**

---

## THE TRANSLATION LAYER

```
PLUMBING DOMAIN                    TRADING DOMAIN
(what's happening in the system)   (what to do about it)
                                   
  Liquidity Verdict                Trade Mode
  SOFR/IORB Spread                 Instrument Selection
  TGA/RRP Direction                Directional Bias
  Cross-Currency Basis             Position Sizing
  VIX Level                        Active Edge Selection
  DXY Trend                        Session Plan
                                   
         ▲                         ▲
         │                         │
         └─────── THIS FILE ───────┘
                   BRIDGE
         (no plumbing re-explained)
         (no trade setups defined)
```

---

## DECISION TREE 1: SHOULD I TRADE TODAY?

Start here. Before any analysis, before any data — this tree decides if you should even open the charts.

```
                               ┌─────────────────────┐
                               │   START HERE         │
                               └──────────┬──────────┘
                                          │
                                          ▼
               ┌─────────────────────────────────────┐
               │  Is VIX > 25?                       │
               └──────────┬──────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
   ┌─────────────┐              ┌─────────────────────┐
   │ FLAT         │              │ Is Net Liq < -$50B? │
   │ No trades.   │              └──────────┬──────────┘
   │ Go study     │                         │
   │ plumbing.    │           ┌───────────────┴───────────────┐
   └─────────────┘           ▼                               ▼
                     ┌─────────────┐              ┌─────────────────────┐
                     │ FLAT         │              │ Is SOFR > IORB     │
                     │ No trades.   │              │   + > 5bp spread?  │
                     │ Micro size   │              └──────────┬──────────┘
                     │ only if      │                         │
                     │ A+ setup     │           ┌───────────────┴───────────────┐
                     └─────────────┘           ▼                               ▼
                                        ┌─────────────┐              ┌─────────────────────┐
                                        │ FLAT         │              │ PROCEED             │
                                        │ Repo stress  │              │ to Decision Tree 2  │
                                        │ = no trades  │              │                     │
                                        └─────────────┘              └─────────────────────┘
```

**For the definition of each check above, open:**
- Net Liq < -$50B → `core/liquidity-equation.md` (line 96-104)
- SOFR > IORB spread → `core/repo-plumbing.md` (SOFR stress section)
- VIX > 25 → `plumbing-hierarchy-master.md → Part 6.3` (ES/MES section)

---

## DECISION TREE 2: WHAT'S MY BIAS TODAY?

```
                               ┌─────────────────────┐
                               │   NET LIQUIDITY      │
                               │   + DXY + VIX        │
                               └──────────┬──────────┘
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            ▼                             ▼                             ▼
   ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
   │ INJECT (+$30B+) │         │ NEUTRAL          │         │ DRAIN (< -$10B) │
   │ DXY falling     │         │ (+/-$10B)        │         │ DXY rising      │
   │ VIX < 15        │         │ DXY flat         │         │ VIX > 20        │
   ├─────────────────┤         │ Any VIX          │         ├─────────────────┤
   │ BIAS: BULLISH   │         ├─────────────────┤         │ BIAS: BEARISH   │
   │                 │         │ BIAS: NEUTRAL    │         │                 │
   │ Full mode       │         │                  │         │ Reduced or flat │
   │ MES + MNQ       │         │ MES only         │         │ MES only (1ct)  │
   │ Normal size     │         │ 75% size         │         │ 25-50% size     │
   │                 │         │                  │         │                 │
   │ Look for:       │         │ Look for:        │         │ Look for:       │
   │ - ORB longs     │         │ - ORB both ways  │         │ - Failed bounces│
   │ - VWAP pullback │         │ - VWAP reversion │         │ - ORB shorts    │
   │ - Power hour    │         │ - Tight scalps   │         │ - Gap fills     │
   └─────────────────┘         └─────────────────┘         └─────────────────┘
```

**Where each plumbing concept lives:**
- Net Liquidity → `core/liquidity-equation.md` (the formula and its tri-region application)
- DXY → `plumbing-hierarchy-master.md → Part 8.1` (US plumbing — why DXY matters)
- VIX → `plumbing-hierarchy-master.md → Part 6.3` (3-market HUD, ES section)

---

## DECISION TREE 3: WHICH INSTRUMENT TODAY?

```
                               ┌─────────────────────┐
                               │   TRADE MODE         │
                               │   FROM TREE 1        │
                               └──────────┬──────────┘
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            ▼                             ▼                             ▼
   ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
   │ FULL MODE        │         │ NORMAL MODE     │         │ REDUCED/FLAT    │
   ├─────────────────┤         ├─────────────────┤         ├─────────────────┤
   │ MES primary      │         │ MES only        │         │ MES 1 contract  │
   │ MNQ secondary    │         │ No MNQ          │         │ No MNQ          │
   │                  │         │                  │         │                  │
   │ If bias bullish: │         │ ORB + VWAP      │         │ ORB only        │
   │   MES ORB longs  │         │   reversion     │         │ 1-2 trades max  │
   │   MNQ on dips    │         │ 1-2 trades/day  │         │ 0.25% risk max  │
   │                  │         │ 0.5% risk/trade │         │                  │
   │ If bias bearish: │         │                  │         │ If FLAT:        │
   │   MES short      │         │ Skip if no      │         │ Study plumbing  │
   │     failed       │         │ clear setup     │         │ Read Part 3     │
   │     bounces      │         │ by 9 AM PT      │         │ (esoteric)      │
   │   MNQ gap fill   │         │                  │         │                  │
   └─────────────────┘         └─────────────────┘         └─────────────────┘
```

**Where each strategy lives:**
- MES plays → `trading/mes-mnq-playbook.md` (ORB, VWAP Reversion, Power Hour)
- MNQ plays → `trading/mes-mnq-playbook.md` (Breakout Scalp, Gap Play, Sector Rotation)
- ORB FX plays → `trading/complete-strategy-orb-eurusd.md` (USD/CAD + EUR/USD)

---

## DECISION TREE 4: HOW MUCH SIZE?

```
                               ┌─────────────────────┐
                               │   POSITION SIZING   │
                               │   BY LIQUIDITY      │
                               └──────────┬──────────┘
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            ▼                             ▼                             ▼
   ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
   │ EXTREME LIQ      │         │ NORMAL LIQ      │         │ TIGHT LIQ       │
   │ (RRP > $500B)    │         │ (RRP $50-200B)  │         │ (RRP < $50B)    │
   │ TGA falling      │         │ TGA stable      │         │ TGA rising      │
   │ VIX < 12         │         │ VIX 15-20       │         │ VIX 20-30       │
   ├─────────────────┤         ├─────────────────┤         ├─────────────────┤
   │ 1.5% per trade   │         │ 1.0% per trade  │         │ 0.25% per trade │
   │ 3% daily max     │         │ 2% daily max    │         │ 0.75% daily max │
   │ 2-3 MES          │         │ 1-2 MES         │         │ 1 MES max       │
   │ 1-2 MNQ          │         │ 1 MNQ (if used) │         │ No MNQ          │
   └─────────────────┘         └─────────────────┘         └─────────────────┘
```

**For the full position sizing framework (regimes, correlation sizing, scaling rules):**
`systems/position-sizing-by-flow.md`

**For the full liquidity regime definitions (TGA, RRP, VIX thresholds):**
`systems/position-sizing-by-flow.md` (lines 28-33, the 5-regime table)

---

## TODAY'S ACTIVE EDGES (Quick Reference)

Based on the plumbing data from `systems/live-data-workflow.md`, check which edges are active:

| If You See This in Plumbing Data | Edge(s) Active | Playbook Reference |
|--------------------------------|---------------|-------------------|
| RRP dropping > $50B/week | Edge 2: RRP-to-Zero | MES/MNQ Playbook → ORB (bullish bias) |
| TGA rising (tax season, big issuance) | Edge 3: TGA Directional | MES/MNQ Playbook → VWAP Reversion (bearish bias) |
| VIX < 13 + options volume elevated | Edge 6: Gamma Squeeze | MNQ Playbook → Gap Play or Breakout Scalp |
| SOFR > IORB for 3+ days | Edge 7: Repo Stress | Stand aside (Decision Tree 1 → FLAT) |
| Cross-currency basis widening > 20bp | Edge 8: Dollar Shortage | Reduced size, short risk assets |
| Quarter-end in 1-2 weeks | Edge 9: Rebalance | Fade quarterly trend, trade reversion |
| COT: specs > 90th %ile long ES | Edge 5: COT Extreme | Fade, look for reversal | 
| COT: specs > 90th %ile short ES | Edge 5: COT Extreme | Look for squeeze, bias bullish |
| New 20-day high fails (closes back inside) | Edge 12: CTA Stop Run | Short the failed breakout |
| Overnight gap > 20 pts with low volume | Edge 11: Liquidity Void | Expect gap fill (MNQ Gap Play) |
| Funding currencies at extreme (JPY massively short) | Edge 14: Unwind | Prepare for violent reversal in that pair |

**Edge definitions (do not re-read this list — go to the source):**
`plumbing-hierarchy-master.md → Part 5.2` (lines 2002-2146, all 15 edges)

---

## THE DAILY VERDICT TEMPLATE

After running Decision Trees 1-4, this is your output:

```
┌─────────────────────────────────────────────────────────────────────┐
│  DATE: YYYY-MM-DD                                                    │
├─────────────────────────────────────────────────────────────────────┤
│  TRADING: [YES / NO] — if NO, reason: _______________                │
│  TRADE MODE: [FULL / NORMAL / REDUCED / FLAT]                        │
│  INSTRUMENT: [MES / MNQ / BOTH / NONE]                               │
│  BIAS: [BULLISH / BEARISH / NEUTRAL]                                  │
│  MAX SIZE: [1 / 2 / 3] contracts                                     │
│  ACTIVE EDGES: ________________________________                     │
│  SESSION PLAN: ____________________________________                  │
│  _______________________________________________                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## WHEN THE BRIDGE SAYS "DON'T TRADE"

The most important function of this bridge is telling you when NOT to trade:

| Scenario | What the Bridge Says | What to Do Instead |
|----------|---------------------|-------------------|
| VIX > 30 + Net Liq negative | FLAT. System in stress. | Read `plumbing-hierarchy-master.md → Part 3` (esoteric structure behind the stress) |
| SOFR > IORB + RRP at $0 | FLAT. Repo stress imminent. | Read `core/repo-plumbing.md` (what repo stress actually means) |
| Cross-currency basis widening + DXY surging | REDUCED. Dollar shortage in progress. | Read `core/plumbing-esoterica.md → XCCY section` (how dollar shortages propagate) |
| Week before Fed/BoC/ECB decision | NORMAL but no new positions. Let policy come out. | Review `systems/weekly-flow-checklist.md → tri-region synthesis` |
| Back from 3+ days away from charts | REDUCED. Ease back in. | Do 3 days of live-data workflow without trading. Recalibrate. |

**All references point to PLUMBING files — not trading files.** When the bridge says don't trade, go deeper into understanding the plumbing.

---

## THE THREE LAWS OF THIS BRIDGE

1. **The plumbing always comes first.** If you don't understand WHY the data says what it says, don't trade the verdict. Go read the source file.

2. **The bridge translates, not creates.** No original plumbing concepts here. No original trade setups here. Every output traces to a source file in one of the two domains.

3. **When in doubt, the answer is "don't trade."** The bridge's most reliable output is telling you to stand aside. Learn to trust it.

---

## REFERENCES

**Plumbing sources (for understanding):**
- Liquidity equation: `core/liquidity-equation.md`
- Repo plumbing: `core/repo-plumbing.md`
- Esoteric plumbing: `core/plumbing-esoterica.md`
- Global flow map: `core/global-flow-map.md`
- Tri-region flow: `core/tri-region-flow-map.md`
- Hierarchy master (deep dive): `plumbing-hierarchy-master.md`
- Part 3 (esoteric): `plumbing-hierarchy-master.md → Part 3`
- Part 5 (15 edges): `plumbing-hierarchy-master.md → Part 5`
- Part 6 (HUD): `plumbing-hierarchy-master.md → Part 6`

**Trading sources (for execution):**
- MES/MNQ playbook: `trading/mes-mnq-playbook.md`
- ORB FX strategy: `trading/complete-strategy-orb-eurusd.md`
- Eval protocol: `trading/eval-mode-protocol.md`
- Position sizing: `systems/position-sizing-by-flow.md`
- Fill your cup: `trading/fill-your-cup.md`
- Commandments: `trading/trading-commandments.md`

**Bridge files (the workflow):**
- Live data workflow: `systems/live-data-workflow.md`
- Daily schedule: `systems/3hr-daily-schedule.md`
- This file: `systems/plumbing-to-trade-bridge.md`
