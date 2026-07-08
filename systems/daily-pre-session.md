# DAILY PRE-SESSION CHECKLIST — 5 Minutes Before Every Session
## "Know the flow before you touch the trade."

---

## THE 5-MINUTE PRE-SESSION (Every Trading Day)

### 1. Overnight Context (30 sec)

- **Asia/Europe session close** — where did they leave price?
- **Open / High / Low / Close** — noting key levels
- **Gap check** — is price gapping from previous close?
- **Overnight news** — any major headlines, data prints, central bank speak?

**Where:** TradingView multi-timeframe view (Daily → 4H → 1H)

---

### 2. Session-Specific (30 sec)

| Session | Focus |
|---------|-------|
| **Asia** (5pm-2am ET) | Thin liquidity. Institutions position. |
| **London open** (3am-12pm ET) | True volume starts. EUR/USD, GBP/USD active. |
| **NY open** (8am-5pm ET) | USD pairs active. Most volume. |
| **NY close** (5pm ET) | Position squaring. Pairs reverse or accelerate. |

**Your time (Vancouver):** 
- London: midnight-9am PT
- NY: 5am-2pm PT
- You trade NY hours primarily. Check what Asia/London already did.

---

### 3. Liquidity Check (1 min)

**What's the liquidity verdict today?**

| Signal | Source | Reading |
|--------|--------|---------|
| TGA ↑↓ | FRED: WTREGEN | ↑ = draining liquidity, ↓ = adding |
| RRP ↑↓ | FRED: RRPONTSYD | ↑ = idle cash abundant, ↓ = flowing |
| DXY (Dollar Index) | TradingView | Direction — up = risk-off, down = risk-on |
| S&P 500 futures | TradingView | Risk appetite |
| VIX | TradingView | <15 = complacent, >25 = fear |

**Plug into:**
- [core/liquidity-equation.md] — Net Liquidity = ΔCB BS − ΔTGA − ΔRRP
- [core/repo-plumbing.md] — SOFR check

---

### 4. Today's Calendar (30 sec)

| Event | Time | Expected | Previous | Impact |
|-------|------|----------|----------|--------|
| e.g. Jobless Claims | 8:30am ET | 230K | 234K | Medium |
| e.g. EIA Crude | 10:30am ET | -2M | -3.4M | High (WTI/CAD) |

**Your rule:** Know the prints before they hit. No surprises.

**High impact prints:** NFP, CPI, PPI, FOMC, EIA (Wednesday), BoC decisions, ECB decisions.

**Your strategy around news:**
- Wait 15 min after news print before entering
- The initial spike is noise. The true direction forms after.
- Unless the spike exceeds 1 ATR → trend may have shifted.

---

### 5. Current Positions (30 sec)

- **Open position(s):** Current P&L, distance to stop
- **Pending orders:** Where are they, did price reach overnight?
- **Today's bias:** Bullish / Bearish / Neutral per pair

---

### 6. Instrument-Specific (1 min each active pair)

#### USD/CAD
- Check WTI ($/bbl) — direction tonight
- Check Canada calendar (GDP, jobs, BoC)
- Check US calendar (EIA, NFP)
- Key structure levels (4H/1H)
- Current spread (tight = liquid; wide = event risk)

#### EUR/USD
- Check DXY
- Check ECB speak / EU data
- Key structure levels (4H/1H)

#### WTI Crude
- EIA week? (Wednesday)
- API week? (Tuesday)
- Supply disruptions? OPEC?
- Structure: contango or backwardation?

#### Gold (XAU/USD)
- Real yields direction
- DXY direction
- Geopolitical fear level

---

### 7. Session Bias Confirmation (30 sec)

**Based on the above, today's bias is:**
```
USD/CAD: [Bullish / Bearish / Neutral]
EUR/USD: [Bullish / Bearish / Neutral]
WTI:     [Bullish / Bearish / Neutral]
Gold:    [Bullish / Bearish / Neutral]
```

**Trade plan:** 
- [ ] I will trade only the setups I've identified
- [ ] I will not trade anything outside this plan
- [ ] My max loss for today is [X]% of account

---

## POST-SESSION CHECKLIST (30 sec after session)

```
1. Did my bias match what price did? [Y/N]
2. Did I follow my trade plan? [Y/N]
3. What was the flow telling me?
4. One thing I did well:
5. One thing to improve tomorrow:
```

---

## THE COMPLETE ROUTINE (Total: ~5 min pre, ~1 min post)

| Step | What | Time |
|------|------|------|
| 1. Overnight Context | Quick chart scan | 30s |
| 2. Session-Specific | When's the volume? | 30s |
| 3. Liquidity Check | TGA/RRP/DXY/VIX | 1 min |
| 4. Today's Calendar | Know the event risk | 30s |
| 5. Current Positions | Know your exposure | 30s |
| 6. Instrument-Specific | Structure / levels | 1 min |
| 7. Bias Confirmation | What are you trading today? | 30s |
| **TOTAL PRE-SESSION** | **All done before first trade** | **~5 min** |
| Post-Session Review | 5 questions | 1 min |

---

## TEMPLATE — Copy for Each Trading Day

```
## PRE-SESSION — YYYY-MM-DD

### Overnight Context
- Asia/Europe close price:
- Overnight news:
- Gap check:

### Liquidity Check
- TGA direction (↑/↓):
- RRP ($B):
- DXY:
- S&P 500 futures:
- VIX:

### Today's Calendar
| Time ET | Event | Expected | Prior |
|---------|-------|----------|-------|

### Current Positions
- /: $, SL at

### Instrument Levels
| Pair | Bias | Key Level (1H) | Key Level (4H) |
|------|------|----------------|----------------|
| USD/CAD | | | |
| EUR/USD | | | |
| WTI | | | |
| Gold | | | |

### Today's Bias
- USD/CAD:
- EUR/USD:
- WTI:
- Gold:

### Max Loss Today:
---

## POST-SESSION

1. Bias matched?:
2. Followed plan?:
3. Flow told me:
4. Good:
5. Improve:
```

---

## REFERENCES

- [systems/weekly-flow-checklist.md] — The Monday tri-region OS (includes this daily)
- [core/tri-region-flow-map.md] — Weekly flow context (pre-read before daily)
- [core/liquidity-equation.md] — Liquidity math for daily check
- [core/repo-plumbing.md] — Repo/SOFR read for daily liquidity check
- [mental-models/10-level-mastery-path.md] — Level 9 (Execution) is this applied
