# THE WEEKLY FLOW CHECKLIST
## Tri-Region Liquidity Read in 10 minutes

## THE CORE LOOP

```
Monday    → 10 min: Read liquidity across all 3 regions
Wed-Fri   → 2 min: Check EIA (Wed) + NFP/CPI (Fri)
Daily     → Before session: Quick pipe check
```

---

## MONDAY — FULL CHECK (10 min)

### Step 1: US Liquidity (3 min)

| Data Point | Where | What I See | What It Means |
|-----------|-------|-----------|---------------|
| **Fed Balance Sheet** | FRED: WALCL | ↑ / ↓ / Flat | ↑ = liquidity in, ↓ = liquidity out |
| **TGA** | FRED: WDTGAL | ↑ / ↓ / Flat | ↑ = drain, ↓ = injection |
| **Reverse Repo** | FRED: RRPONTSYD | ↑ / ↓ / Flat | ↑ = money idle (drain) |
| **Net Liquidity** | ΔBS − ΔTGA − ΔRRP | [+/−] ≈ $___B | **If > 0 = risk-on. If < 0 = risk-off.** |

**Verdict: US Liquidity is INJECTING / NEUTRAL / DRAINING**

### Step 2: Canada Check (3 min)

| Data Point | Where | What I See | What It Means |
|-----------|-------|-----------|---------------|
| **WTI Crude** | TradingView: CL1! | Price: $___/bbl ↑/↓ | ↑ = bullish CAD, ↓ = bearish CAD |
| **EIA Inventory** | EIA weekly | ___M bbl | ↓ draw = bullish, ↑ build = bearish |
| **BoC Rate** | BoC website | Current: ___% | Compare to Fed rate |
| **BoC-Fed Spread** | BoC vs Fed | ___% | Spread widening = CAD moves |
| **Housing Data** | CREA | MoM: ↑/↓ | ↑ = domestic liquidity flowing |

**Verdict: Canada Liquidity is INJECTING / NEUTRAL / DRAINING**

### Step 3: Europe Check (3 min)

| Data Point | Where | What I See | What It Means |
|-----------|-------|-----------|---------------|
| **EUR/USD** | TradingView | Price: ___ ↑/↓ | Global risk barometer |
| **ECB Balance Sheet** | ECB website | ↑ / ↓ / Flat | ↑ = liquidity in Europe |
| **EUR/USD Basis Swap** | Bloomberg/BIS | ___ bps | If wide negative = dollar shortage in Europe |
| **German Bund Yield** | TradingView | ___% ↑/↓ | European risk-free rate, benchmark |
| **Eurozone PMI** | TradingEconomics | ___ ↑/↓ | Economic health indicator |

**Verdict: Europe Liquidity is INJECTING / NEUTRAL / DRAINING**

### Step 4: Tri-Region Synthesis (1 min)

```
US:        [Injecting / Neutral / Draining]
Canada:    [Injecting / Neutral / Draining]
Europe:    [Injecting / Neutral / Draining]

GLOBAL RISK SIGNAL: [Risk-On / Mixed / Risk-Off]
```

| Signal | What to Favor |
|--------|--------------|
| **Risk-On** (all 3 injecting) | Long equities, long CAD, long EUR/USD, short USD |
| **Mixed** (1-2 injecting) | Selectively long, tight stops, pairs trading |
| **Risk-Off** (all 3 draining) | Short risk assets, long USD, long JPY/CHF, reduce size |

---

## WEDNESDAY — EIA DAY (2 min)

| Check | Source | What I Need to Know |
|-------|--------|---------------------|
| **EIA Crude Inventory** (10:30am ET) | EIA.gov | Actual vs Expected vs Prior |
| **Expected vs Actual** | TradingView calendar | A big miss moves USD/CAD 30-50 pips |
| **CAD Reaction** | USD/CAD chart | Initial spike is usually faded. Wait 5 min. |

**Playbook:** If inventory draw > forecast → CAD up → short USD/CAD after initial fake move.

---

## FRIDAY — NFP/CPI DAY (2 min)

| Check | Source | What I Need to Know |
|-------|--------|---------------------|
| **US Data Print** (8:30am ET) | BLS.gov | Actual vs Expected |
| **USD Reaction** | DXY, EUR/USD, USD/CAD | Initial move often reversed |
| **Market Interpretation** | Price action 15 min after | Is the reaction holding? |

**Rule for Fridays:** Never enter a position before the print. Wait until the market has decided (usually 15-30 min after). If you're not in the flow by then, the setup is gone.

---

## DAILY — PRE-SESSION CHECK (Before every session, 2 min)

```
1. Fed liquidity direction?    → [Injecting / Draining / Neutral]
2. WTI direction?              → [↑ / ↓ / Sideways]
3. EUR/USD direction?          → [↑ / ↓ / Sideways]  
4. High-impact news today?     → [Yes / No]  (If yes: check calendar, avoid news)
5. Am I in the pipe?           → [Yes / No]  (If no: close terminal)
```

**If answer to #5 is NO:** The market will still be there tomorrow. You don't have to trade today.

---

## POSITION SIZING BY CONFIDENCE (from liquidity signal)

| Liquidity Signal | Max Risk per Trade | Max Daily Risk | Position Size |
|-----------------|-------------------|---------------|--------------|
| Strong risk-on (all 3 injecting, > $50B) | 1.5% | 4.5% | 100% of normal |
| Mild risk-on (1-2 injecting) | 1.0% | 3.0% | 75% of normal |
| Neutral | 0.5% | 1.5% | 50% of normal |
| Risk-off (draining) | 0.25% | 0.75% | 25% or sit out |

---

## THE GOLDEN RULE

**Don't check the plumbing to find trades.**
**Check the plumbing to know when NOT to trade.**

Most losses happen on days when the liquidity signal is negative but you trade anyway.
The one who sits out during drains lives to trade another day.

---

## REFERENCES

- [core/liquidity-equation.md] — The formula behind this checklist
- [core/tri-region-flow-map.md] — Where each region fits
- [mental-models/pipe-theory.md] — Why this matters
- [13-weekly-flow-tapping-operating-system.md] — Original expanded OS
- [08-forex-trading-the-purest-flow.md] — Canadian forex specifics
- [14-forex-clock-resources.md] — Session times, data releases
