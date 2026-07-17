# GANGOTRI PROTOCOL — Source → Flow → Distributary → Tap

## "Plumbing tells you the direction. Structure tells you the entry."

---

## THE FRAMEWORK — Three Integrated Lenses

Every trade must pass all three. Any single lens says NO → no trade. No exceptions.

```
LENS 1 — PLUMBING (Gangotri / Source)
│   What does the liquidity equation say?
│   Output: Trade Mode (ON/OFF/CAUTIOUS) + Bias + Active Edges
│   Source: systems/live-data-workflow.md → VERDICT
│   Depth: core/liquidity-equation.md, hierarchy Part 5
│
LENS 2 — STRUCTURE (Bhagirathi / Distributary)
│   What is the market structure doing?
│   Output: Setup pattern + Entry zone + Invalid levels
│   Source: hierarchy-master Part 9.2 (ICT synthesis)
│   Depth: hierarchy Part 5 (15 edges), Part 9.2 table
│
LENS 3 — EXECUTION (Tap / Your Entry)
│   Does a specific setup align with both above?
│   Output: Entry price + Stop + Target + Size
│   Source: trading/mes-mnq-playbook or complete-strategy-orb-eurusd
│   Depth: position-sizing-by-flow, eval-mode-protocol
```

---

## THE COMBINED EDGE MATRIX — Plumbing Signal → ICT Expression → Your Trade

| Plumbing Signal | ICT Expression | Your Trade |
|-----------------|---------------|------------|
| **Net Liq ↑ (expansion)** | Bullish FVG on 4H, displacement up, OTE retrace | Buy the FVG retrace after displacement. Target: next high. |
| **Net Liq ↓ (contraction)** | Sellside liquidity above PDH, bearish CHoCH | Short after sweep of PDH + flip. Target: next low. |
| **TGA drawdown (injecting)** | Daily displacement candle up, liquidity grab below prior low | Buy the sweep-and-flip. Stop below the swept low. |
| **TGA building (draining)** | Bearish PDH sweep, rejection at resistance | Short the sweep-and-flip. Stop above PDH. |
| **RRP > $500B** | Abundant liquidity — all setups have higher probability | Size up per regime. Every pattern is more likely to work. |
| **RRP < $50B** | Liquidity extraction — patterns may fail, false breaks | Size down. Take profit faster. Don't let winners run. |
| **Repo stress (SOFR > IORB + 5bp)** | Spreads widen, gaps, erratic movement | FLAT. No trades. The plumbing is broken. |
| **XCCY basis widening (negative)** | USD strength — EUR/USD selloffs are aggressive | Short EUR/USD on bounce to FVG. Or stay in MES to avoid FX. |
| **COT spec extreme (90th+ percentile)** | Reversal patterns on D1 — sweeps of recent range extremes | Fade the extreme. If specs are max long, look for sellside sweep + flip. |
| **VIX < 12 + Net Liq ↑** | Trend day — ORB break + continuation | Size up. ORB break in direction of Net Liq. Ride. |
| **VIX 20-25 + Net Liq ↓** | Choppy — sweeps both directions, no follow-through | ORB fade. Short the high, buy the low. Quick exits. |
| **CPI / FOMC / NFP day** | Pre-event range, post-event displacement | No new positions 30 min before. Wait 15 min post. Then: trade the displacement. |

---

## THE 3-QUESTION GATE — Before Every Entry

```
Q1 — PLUMBING: Does Net Liq direction support this trade?
    Go to: systems/live-data-workflow.md → VERDICT
    Check: Trade Mode must be ON or CAUTIOUS (not OFF)
    Check: Bias must align with your intended direction
    YES → proceed. NO → skip.

Q2 — STRUCTURE: Is there an ICT pattern aligning with the plumbing?
    Check: Is there a FVG, displacement, or sweep in the direction of Net Liq?
    Check: Are we in a relevant killzone (London/NY am/NY pm)?
    Check: Has the CHoCH confirmed the bias?
    YES → proceed. NO → wait. Structureless flow = no entry.

Q3 — EXECUTION: Is my specific setup triggered with valid R:R?
    Check: Has the exact entry rule been met? (ORB break, FVG retrace, etc.)
    Check: Is R:R at least 1:1.5? (1:2 preferred for eval mode)
    Check: Is size correct per today's regime?
    YES → enter. NO → wait.

ALL THREE = YES → trade.
ANY ONE = NO → skip. No exceptions. No "close enough."
```

---

## KILLZONE + PLUMBING INTEGRATION (Vancouver PT)

```
LONDON (12AM-3AM PT)                NY AM (5AM-8AM PT)                NY PM (8AM-10:30AM PT)
────────────────────────────────    ────────────────────────────────    ────────────────────────────────
EUR/USD primarily                   MES/MNQ mainly                      Power hour — MES/MNQ
ICT: London killzone                ICT: NY am killzone                 ICT: NY pm killzone
Plumbing: FX fixing flows,          Plumbing: MOC, options expiry,      Plumbing: institutional position
  overnight gaps, Asia session        institutional program trades        squaring, closing prints
Bias from: weekend prep +           Bias from: live-data-workflow       Bias from: session range
  overnight range                    VERDICT
                                  Setup: ORB (first 5-15 min),
Setup: London breakout,              VWAP reversion after initial        Setup: VWAP reversion,
  FVG retrace from overnight         displacement                         momentum fade into close

Note: If live-data-workflow says Trade Mode = CAUTIOUS → skip London session.
       NY am is the highest-conviction window when plumbing is aligned.
```

---

## BEFORE EVERY SESSION — Sequence

```
Step 1: systems/live-data-workflow.md (15 min)
  → Get VERDICT: Trade Mode + Instrument + Bias + Active Edges
  → Note: which edges from the Combined Edge Matrix are active today

Step 2: systems/plumbing-to-trade-bridge.md (5 min)
  → Run Decision Tree 1: Should I trade today?
  → If YES: Tree 2 (Bias) → Tree 3 (Instrument) → Tree 4 (Size)

Step 3: This file — GANGOTRI PROTOCOL (2 min)
  → Open the Combined Edge Matrix. Match today's signals.
  → Set the 3-Question Gate checkpoints for the session.
  → Write your intention: "I am looking for [pattern] on [instrument].
    If [structure] aligns with [plumbing signal], I enter. Otherwise I wait."

Step 4: trading/trading-commandments.md (1 min)
  → Read aloud. Reset the mind.

Step 5: Chart prep (5 min)
  → Mark key levels. Set alerts.
  → Ready.
```

---

## AFTER EVERY TRADE — The 3-Question Review

Same structure as the gate, but after the fact:

```
Q1 — PLUMBING: Was the plumbing verdict correct?
    Did Net Liq move as expected? Was my bias right?
    If no: why? (Event override? Data revision? Missed signal?)

Q2 — STRUCTURE: Did the pattern deliver?
    Was the FVG respected? Did the sweep trigger the flip?
    If no: was the pattern there and failed, or was it never really there?

Q3 — EXECUTION: Did I follow the plan?
    Did I enter at the planned level? Exit correctly?
    If no: what did I override?
```

---

## THE FINAL TRUTH

The plumbing is Gangotri — the source. It tells you the direction of the river.

The structure is Bhagirathi — the distributary. It tells you which channel the water takes.

The tap is your entry — the moment you put your cup in the right channel at the right time.

**Most traders install a tap without knowing where the river flows.**
**You know the river. Now learn to feel which channel it takes today.**

---

*Cross-ref: hierarchy-master Part 9.2 (ICT integration table, for expanded concept definitions)
Cross-ref: hierarchy-master Part 5 (15 edges — the plumbing source for every ICT pattern)
Cross-ref: trading/mes-mnq-playbook (MES/MNQ specific setups with R:R tables)
Cross-ref: trading/complete-strategy-orb-eurusd (ORB FX setups)
Cross-ref: trading/eval-mode-protocol (sizing rules for eval vs funded)*
