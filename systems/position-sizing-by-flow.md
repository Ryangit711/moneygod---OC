# POSITION SIZING BY FLOW — Size Based on Liquidity, Not Conviction
## "The liquidity regime determines how much risk to take. Your conviction is irrelevant."

---

## THE CORE INSIGHT

Most traders size based on:
- "How confident am I in this setup?" (emotion)
- "How much do I want to win?" (greed)
- "Let me make back what I lost" (revenge)

**All wrong.**

The only valid input to position sizing is: **what is the liquidity regime allowing?**

- High liquidity → market can trend → you can be right, size up
- Low liquidity → market whipsaws → even if you're right, you get stopped out
- Stress conditions → anything can happen → size down to near zero

---

## POSITION SIZE = f(LIQUIDITY)

### First: Determine the Liquidity Regime (from weekly checklist)

| Regime | TGA | RRP | VIX | Max Portfolio Risk | Max Position Risk |
|--------|-----|-----|-----|-------------------|-------------------|
| **Extreme Liquidity** | ↓ Falling | >$500B | <12 | 3% daily | 1.5% per trade |
| **Abundant** | Stable | $200-500B | 12-15 | 2% daily | 1% per trade |
| **Normal** | Stable | $50-200B | 15-20 | 1% daily | 0.5% per trade |
| **Tight** | ↑ Rising | <$50B | 20-30 | 0.5% daily | 0.25% per trade |
| **Stress** | ↑↑ Spiking | ~$0 | >30 | <0.5% daily | <0.25% or flat |

Your vault (Wealth Rule Book): "The wealthy don't take more risk. They take better-structured risk."

---

### Second: Adjust by Instrument Liquidity

| Instrument | Liquidity Profile | Size Multiplier vs USD/CAD |
|-----------|------------------|---------------------------|
| **EUR/USD** | Ultra-liquid, tight spreads | 1.0x (full size) |
| **USD/CAD** | Very liquid, slightly wider | 1.0x (full size) |
| **WTI Crude (CL)** | Very liquid, gap risk at open | 0.75x |
| **Gold (XAU/USD)** | Very liquid, wide range days | 0.75x |
| **GBP/USD** | Liquid, volatile on Brexit/BOE | 0.8x |
| **USD/JPY** | Liquid, BoJ intervention risk | 0.7x |

**Spreads matter:** If spread > 0.5x recent ATR, reduce size. The spread is a cost you must overcome.

---

### Third: Calculate Actual Size

**The Formula:**
```
Position Size = (Account Balance × Risk %) ÷ (Stop Distance in Pips × Pip Value)
```

**Example:**
- Account: $10,000
- Risk %: 1% (abundant liquidity)
- Stop distance: 20 pips
- Pip value (USD/CAD): ~$0.92 per micro lot (1,000 units)
- Pip value per standard lot (100,000) = ~$92 CAD

**For standard lots:**
- Max loss per trade = $100
- Stop = 20 pips × $0.92/pip = $18.40 per mini lot (10,000 units)
- Max position = floor($100 ÷ $18.40) = 5 mini lots (50,000 units)
- = 0.5 standard lots

**For micro lots (beginner / low liquidity):**
- Max loss = $10 per trade
- Stop = 20 pips × $0.092/pip = $1.84 per micro lot
- Max position = floor($10 ÷ $1.84) = 5 micro lots (5,000 units)

**Rule:** When in doubt, use micro lots. You can always add. You can never undo a blown account.

---

## THE FOUR SIZE MODES

| Mode | Liquidity Signal | Size | Behavior |
|------|-----------------|------|----------|
| **Building** | Abundant + trending | Max regime size | Scale in to position |
| **Hunting** | Normal + ranging | Half regime size | Quick entries, tight stops |
| **Harvesting** | Tight + uncertain | Small or nothing | Take profits, don't add |
| **Hiding** | Stress + chaos | Flat | Wait. Don't trade. Read. |

**Mode is determined before the session.** Not during.

---

## SPECIAL RULES

### Correlation Sizing (Don't Overlap)

If you're long USD/CAD AND short EUR/USD AND long Gold, all three might express the same view (dollar bearish).

**Rule:** Treat correlated positions as ONE position for sizing purposes.

```
Maximum total exposure across correlated instruments:
    1 × regime max × instrument multiplier
```

**Example:** If USD/CAD is at 1.5% max (extreme liquidity), EUR/USD is at 1.5%, and Gold is at 1.125% (0.75×):

```
If all three are on the same side of the dollar:
    → Reduce each by 50%
    → Or pick only 1-2 trades
```

### Scaling

| To | After | Size Increment |
|----|-------|---------------|
| Add to winner | Price moves 1R in your favor | Move stop to breakeven on original. Add half original size. |
| Add to loser | **NEVER** | You are wrong. Close. Reassess. |

### Gap Risk

If your instrument gapped past your stop level:
- Don't hold and hope. Assess immediately.
- If the gap is driven by a fundamental change (Fed surprise, geopolitical), exit.
- If it's a noise gap, wait for 15 min to see if price returns.

**WTI specifically:** Gap risk at contract roll-over. Reduce size 2 days before roll.

---

## POSITION SIZING MATRIX (Print This)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    POSITION SIZING BY LIQUIDITY                         │
├────────────────────┬──────────┬──────────┬──────────┬──────────┬────────┤
│ Account Size       │ $2,000   │ $5,000   │ $10,000  │ $25,000  │ $50K+  │
├────────────────────┼──────────┼──────────┼──────────┼──────────┼────────┤
│ Abundant (1.5%)    │ $30      │ $75      │ $150     │ $375     │ $750   │
│ Normal (1%)        │ $20      │ $50      │ $100     │ $250     │ $500   │
│ Tight (0.5%)       │ $10      │ $25      │ $50      │ $125     │ $250   │
│ Stress (0.25%)     │ $5       │ $12.50   │ $25      │ $62.50   │ $125   │
├────────────────────┼──────────┼──────────┼──────────┼──────────┼────────┤
│ Micro Lot $/pip    │ $0.09    │ $0.09    │ $0.09    │ $0.09    │ —      │
│ Mini Lot $/pip     │ $0.92    │ $0.92    │ $0.92    │ $0.92    │ $0.92  │
│ Standard Lot $/pip │ —        │ —        │ $9.16    │ $9.16    │ $9.16  │
└────────────────────┴──────────┴──────────┴──────────┴──────────┴────────┘

Based on $0.916/pip per mini lot (USD/CAD at ~1.36):
  - $ value = 1,000 CAD per mini lot ÷ exchange rate = $1,000 ÷ 1.36 ≈ $735 USD per mini lot
  - Pip value = $735 × 0.0001 = $0.0735... Actually let's be precise:

PIP VALUE FOR USD/CAD:
  - Standard lot (100,000 units): $100 CAD = ~$73.5 USD
  - Mini lot (10,000 units): $10 CAD = ~$7.35 USD  
  - Micro lot (1,000 units): $1 CAD = ~$0.74 USD

(Value changes with exchange rate. Approximate at current rates.)
```

---

## THE POSITION SIZING DECISION TREE

```
┌─────────────────────────────────────┐
│ START: Check liquidity regime       │
│ TGA ↓ RRP >$500B VIX <12            │
│ → Extreme Liquidity: 1.5% per trade │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│ Check instrument liquidity          │
│ EUR/USD = 1.0x, WTI = 0.75x, etc   │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│ Check spread vs ATR                 │
│ Spread > 0.5x ATR? → Reduce size    │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│ Check correlation overlap           │
│ Multiple same-direction trades?     │
│ → Reduce each proportionally        │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│ CALCULATE: Size = (Bal × Risk%)     │
│                   ÷ (Stop × PipVal)  │
└──────────────────┬──────────────────┘
                   ▼
┌─────────────────────────────────────┐
│ Is this an add to winner?           │
│ → Half original size, or            │
│ → Exit alert: 2R minimum target     │
└─────────────────────────────────────┘
```

---

## THE GOLDEN RULES

1. **Size down when liquidity tightens.** You lose conviction-sized positions, not liquidity-sized ones.
2. **If uncertain, trade micro.** Always available. No shame.
3. **If stressed, trade nothing.** Session 0 is valid.
4. **If you're considering increasing size because you "feel" it, don't.** That's emotion.
5. **Size by pipe reading, not by chart reading.** Charts tell you where. The pipe tells you how much.
6. **2% weekly loss max.** If hit, stop trading for the week. Read more plumbing.

---

## REFERENCES

- [core/liquidity-equation.md] — The liquidity math that determines regime
- [core/repo-plumbing.md] — Repo/SOFR read for liquidity check
- [systems/weekly-flow-checklist.md] — Weekly regime determination
- [systems/daily-pre-session.md] — Daily sizing check before first trade
- [mental-models/pipe-theory.md] — "Sit in the flow, don't create it"
