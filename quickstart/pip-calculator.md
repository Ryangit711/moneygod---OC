# PIP VALUE CALCULATOR
## "Know the dollar value of every pip before you enter"

---

## PIP VALUES BY PAIR

| Pair | 1 Lot (100,000) | 1 Mini (10,000) | 1 Micro (1,000) |
|------|----------------|-----------------|-----------------|
| **EUR/USD** | $10.00 USD | $1.00 USD | $0.10 USD |
| **GBP/USD** | $10.00 USD | $1.00 USD | $0.10 USD |
| **USD/JPY** | ~$9.17 USD (varies) | ~$0.92 USD | ~$0.09 USD |
| **USD/CAD** | ~$7.35 USD (varies) | ~$0.74 USD | ~$0.07 USD |
| **AUD/USD** | $10.00 USD | $1.00 USD | $0.10 USD |
| **XAU/USD (Gold)** | $10.00 USD | $1.00 USD | $0.10 USD |

**For USD/CAD (your home pair):**
- Pip value changes with exchange rate
- At 1.3600: 1 micro lot (1,000 units) = $0.735 USD per pip
- At 1.3000: 1 micro lot = $0.769 USD per pip
- At 1.4000: 1 micro lot = $0.714 USD per pip

*Rule of thumb: $0.07-0.08 USD per pip per micro lot for USD/CAD*

---

## POSITION SIZING CALCULATOR

**Formula:**
```
Position Size = (Account × Risk%) / (Stop in Pips × Pip Value)
```

### Example 1: $5000 Account, 1% Risk, 20 Pip Stop

```
Max loss = $5000 × 1% = $50
Stop = 20 pips
Pip value (USD/CAD, micro lot) = ~$0.74 USD

Size = $50 / (20 × $0.74) = $50 / $14.80 = 3.3 micro lots

→ Trade 3 micro lots (0.03 lot) 
→ Max loss = 3 × 20 × $0.74 = $44.40 (within 1%)
```

### Example 2: $1000 Account, 1% Risk, 25 Pip Stop

```
Max loss = $1000 × 1% = $10
Stop = 25 pips
Pip value (USD/CAD, micro lot) = ~$0.74

Size = $10 / (25 × $0.74) = $10 / $18.50 = 0.54 micro lots

→ Trade 0.5 micro lots (0.005 lot — check if broker allows)
→ Or reduce stop to 15 pips to trade 0.01 lot
```

---

## SIZE QUICK REFERENCE

**For a $10,000 account, 1% risk per trade:**

| Pair | Stop (pips) | Micro Lots | Mini Lots |
|------|------------|-----------|-----------|
| EUR/USD | 20 | 5.0 (0.05) | 0.5 |
| EUR/USD | 30 | 3.3 (0.033) | 0.33 |
| USD/CAD | 20 | ~6.8 (0.068) | 0.68 |
| USD/CAD | 30 | ~4.5 (0.045) | 0.45 |
| XAU/USD | 200 pips ($2) | 5.0 (0.05) | 0.5 |

**For a $2,000 account, 1% risk per trade:**

| Pair | Stop (pips) | Micro Lots |
|------|------------|-----------|
| EUR/USD | 20 | 1.0 (0.01) |
| USD/CAD | 20 | 1.3 (0.013) |
| USD/CAD | 30 | 0.9 (0.009 — round to 0.01) |

---

## THE RULE

**Never risk more than 1% of your account on a single trade.**
**Never risk more than 3% of your account in a single day.**

If your stop gets hit:
- You lose 1%. Not 5%. Not 10%. Not your account.
- Tomorrow you still have 99% to trade with.
- That's how you survive long enough to compound.

---

## REFERENCES

- [systems/position-sizing-by-flow.md] — Full sizing system (advanced)
- [trading/complete-strategy-orb-eurusd.md] — Strategy with pre-calculated targets
- [quickstart/03-demo-path.md] — Practice sizing on demo
