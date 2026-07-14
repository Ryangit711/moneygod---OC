# LIVE DATA WORKFLOW — 15-Min Morning Plumbing Check

## "The plumbing tells you what the market HAS to do. The chart tells you how."

---

## THE 15-MINUTE ROUTINE

This is the ONLY place where raw plumbing data becomes a tradeable verdict. Do this before you open any chart, before you check any news, before you even think about a position.

**Total time:** 15 min. Every trading day. Non-negotiable.

```
┌─────────────────────────────────────────────────────────────┐
│                 15 MINUTES — DO NOT SKIP                     │
├─────────────────────────────────────────────────────────────┤
│  MIN 1-3 ── OPEN 5 URLS, RECORD 6 RAW NUMBERS              │
│  MIN 4-6 ── COMPUTE THE LIQUIDITY EQUATION                  │
│  MIN 7-9 ── READ THE 3-MARKET SIGNALS                       │
│  MIN 10-12 ── VERDICT: TRADE MODE + INSTRUMENT + BIAS      │
│  MIN 13-15 ── SESSION PLAN: 2 LINES OF TEXT                  │
└─────────────────────────────────────────────────────────────┘
```

---

## MIN 1-3: OPEN 5 URLs, RECORD 6 NUMBERS

### URL 1: Fed Balance Sheet + TGA + RRP
**Source:** FRED (fred.stlouisfed.org)

| What | FRED Series | Where to Find | Record |
|------|-------------|---------------|--------|
| Fed Balance Sheet | WALCL | Value = total assets ($B) | $____B |
| TGA | WDTGAL | Value = TGA balance ($B) | $____B |
| RRP | RRPONTSYD | Value = ON RRP facility ($B) | $____B |

**Record the raw numbers.** Don't interpret yet. Just write them down.

### URL 2: SOFR Rate
**Source:** NY Fed SOFR page (newyorkfed.org/markets/reference-rates/sofr)

| What | Record |
|------|--------|
| SOFR (overnight) | __.___% |
| SOFR vs IORB spread (see plumbing-esoterica for formula) | __ basis points |

### URL 3: DXY + VIX
**Source:** TradingView or any free chart

| Symbol | Record |
|--------|--------|
| DXY (Dollar Index) | ___.___ (price) + direction (↑/↓/→) |
| VIX (Volatility Index) | ___.__ (value) |

### URL 4: MES/MNQ Overnight
**Source:** TradingView

| Symbol | Record |
|--------|--------|
| MES | Open price, overnight high/low, gap from previous close? |
| MNQ | Open price, overnight high/low, gap from previous close? |

### URL 5: Economic Calendar
**Source:** Forex Factory or TradingView calendar

| What to Check | Record |
|--------------|--------|
| Today's high-impact events? | Time + Event + Expected |
| Wednesday? (EIA day) | Check crude inventory expectations |
| Friday? (NFP/CPI day) | Check data expectations |

---

## MIN 4-6: COMPUTE THE LIQUIDITY EQUATION

### The Formula

```
NET LIQUIDITY = Δ Fed Balance Sheet − Δ TGA − Δ RRP

where:
  Δ = this week's value − last week's value
```

### Do the Math

| Component | This Week | Last Week | Change (Δ) |
|-----------|-----------|-----------|------------|
| Fed BS | $____B | $____B | $____B (+/−) |
| TGA | $____B | $____B | $____B (+/−) |
| RRP | $____B | $____B | $____B (+/−) |

```
Net Liquidity = ΔBS($___) − ΔTGA($___) − ΔRRP($___)
              = $_____B
```

### The Verdict

| If Net Liq Is | Signal | What It Means |
|--------------|--------|---------------|
| > +$50B | Strong risk-on | Full risk appetite. Trend days likely. |
| +$10B to +$50B | Mild risk-on | Selective risk. Bias upward. |
| -$10B to +$10B | Neutral | No liquidity edge. Trade technicals only. |
| -$10B to -$50B | Draining | Cautious. Reduced size. Tight stops. |
| < -$50B | Risk-off | Liquidity leaving. Flat or micro size. |

**Write your verdict: `LIQUIDITY = [INJECT / NEUTRAL / DRAIN]`**

### Additional Health Checks

| Check | Source | Healthy Range | Concern |
|-------|--------|--------------|---------|
| SOFR vs IORB | FRED | SOFR ≤ IORB | If SOFR > IORB = repo stress (Edge 7) |
| Cross-currency basis | Bloomberg (CCBS) or BIS | Near zero | If widening negative = dollar shortage (Edge 8) |
| VIX level | TradingView | < 20 | > 25 = stress, > 30 = panic |
| DXY trend | TradingView | — | 5-day direction matters more than level |

---

## MIN 7-9: READ THE 3-MARKET SIGNALS

For each of your 3 primary markets, check these specific signals:

### MES/MNQ

| Signal | Check | What It Means |
|--------|-------|---------------|
| VWAP position | Price vs VWAP (1H chart) | Above = bullish bias, below = bearish |
| Overnight gap | Gap from yesterday's close | > 20 pts = expected to fill within 2 hours |
| Pre-market volume | Volume vs 20-period avg | > avg = conviction, < avg = noise |
| TICK | NYSE Tick Index | Sustained > +500 = buying pressure, < -500 = selling pressure |

### USD/CAD (if trading FX)

| Signal | Check | What It Means |
|--------|-------|---------------|
| WTI direction | CL1! | Up = bullish CAD, down = bearish CAD |
| BoC-Fed spread | BoC rate vs Fed rate | Widening = CAD divergence |
| CAD COT | CFTC (Friday release) | Extreme positioning = reversal setup |

### EUR/USD (if trading FX)

| Signal | Check | What It Means |
|--------|-------|---------------|
| DXY direction | TradingView | Down = bullish EUR, up = bearish EUR |
| Cross-currency basis | Bloomberg/BIS | Widening negative = EUR weakness |
| EUR COT | CFTC (Friday release) | Extreme positioning = reversal setup |

---

## MIN 10-12: VERDICT — TRADE MODE + INSTRUMENT + BIAS

### Step 1: Determine Trade Mode

Based on the liquidity verdict + VIX:

| Liquidity | VIX < 15 | VIX 15-20 | VIX 20-25 | VIX > 25 |
|-----------|----------|-----------|-----------|----------|
| INJECT | Full mode | Normal mode | Reduced mode | Flat |
| NEUTRAL | Normal mode | Normal mode | Reduced mode | Flat |
| DRAIN | Reduced mode | Reduced mode | Flat | Flat |

**Trade Mode = [FULL / NORMAL / REDUCED / FLAT]**

### Step 2: Choose Instrument

| If | Trade | Reason |
|----|-------|--------|
| Liquidity injecting + VIX < 20 | MES (primary) + MNQ (secondary) | Risk-on environment — both work |
| Liquidity neutral + VIX 15-20 | MES only | Single instrument, lower risk |
| Liquidity draining + any VIX | MES only (micro size) | Stay liquid, stay small |
| VIX > 25 | None | Stand aside or micro scalps only |

**Instrument = [MES / MNQ / BOTH / NONE]**

### Step 3: Set Bias

| Signal Combination | Bias |
|-------------------|------|
| Liquidity injecting + DXY falling + VWAP above | Bullish — look for longs |
| Liquidity injecting + DXY rising + VWAP below | Mixed — check for rotation |
| Liquidity draining + DXY rising + VIX rising | Bearish — look for shorts or flat |
| Liquidity neutral + no clear DXY trend | Neutral — trade ORB only, no directional bet |
| Gap up + VWAP above + volume > avg | Bullish continuation bias |
| Gap down + VWAP below + volume > avg | Bearish continuation bias |
| Gap but volume < avg | Fill expected — fade the gap |

**Bias = [BULLISH / BEARISH / NEUTRAL]**

### Step 4: Determine Active Edges

From the signals above, which of the 15 edges are active today?

| If You See | Edge May Be Active | Plays (from MES/MNQ Playbook) |
|-----------|-------------------|-------------------------------|
| RRP draining fast | Edge 2: RRP-to-Zero Squeeze | MES ORB: bullish bias |
| TGA building up | Edge 3: TGA Directional | Bearish bias, reduced size |
| VIX < 13 | Edge 6: Gamma Squeeze risk | Watch for MNQ breakout scalps |
| SOFR > IORB | Edge 7: Repo Stress | FLAT — no trades |
| VIX > 25 | Edge 7: Repo Stress | FLAT — wait |
| Quarter-end in 1-2 weeks | Edge 9: Rebalance | Fade quarterly trend |
| COT data (Friday) shows extreme | Edge 5: COT Extreme | Fade the extreme |

**Active edges: [_____ / _____ / _____]**

---

## MIN 13-15: SESSION PLAN — 2 LINES OF TEXT

Write exactly 2 lines. No more. This is your session plan:

```
Line 1: TRADE MODE, INSTRUMENT, BIAS
Line 2: "I will [setup] at [level]. If [condition], I [action]. If not, I don't trade."
```

### Examples

**Risk-on day:**
```
FULL | MES | BULLISH
I will buy the ORB breakout above 15-min high with volume. If no breakout by 7:30 AM PT, skip and wait for power hour pullback to VWAP.
```

**Neutral day:**
```
NORMAL | MES | NEUTRAL
I will trade ORB only — long above high, short below low. First 15-min candle sets range. Max 2 trades. 1:1 R:R minimum.
```

**Risk-off day:**
```
REDUCED | MES (1 contract) | BEARISH
I will short initial bounces that fail at VWAP. 1 trade maximum. 0.25% risk. If no clear rejection, stay flat.
```

**Flat day:**
```
FLAT | NONE | NONE
Staying flat. Liquidity draining + VIX > 25. Will read plumbing-hierarchy-master Part 3 instead.
```

---

## THE PRINT-AND-PIN WORKSHEET

Print this table. Fill it in every morning. Pin it next to your screen.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     LIVE DATA WORKFLOW — YYYY-MM-DD                  │
├─────────────────────────────────────────────────────────────────────┤
│ MIN 1-3: RAW DATA                                                    │
│  Fed BS: $____B    TGA: $____B    RRP: $____B                       │
│  SOFR: ___%        VIX: ___        DXY: ___ (↑/↓/→)                 │
│  MES gap: ___ pts  MNQ gap: ___ pts                                  │
│  News today: ________________________                                │
├─────────────────────────────────────────────────────────────────────┤
│ MIN 4-6: LIQUIDITY                                                   │
│  Net Liq = $____B                                                    │
│  Liquidity Verdict: [INJECT / NEUTRAL / DRAIN]                       │
│  SOFR vs IORB: [Normal / Stress]                                     │
├─────────────────────────────────────────────────────────────────────┤
│ MIN 7-9: SIGNALS                                                      │
│  VWAP position (MES): [Above / Below]                                │
│  TICK: [> +500 / < -500 / Neutral]                                   │
│  WTI: $___ (↑/↓)    DXY direction: [↑/↓/→]                          │
├─────────────────────────────────────────────────────────────────────┤
│ MIN 10-12: VERDICT                                                    │
│  Trade Mode: [FULL / NORMAL / REDUCED / FLAT]                        │
│  Instrument: [MES / MNQ / BOTH / NONE]                               │
│  Bias: [BULLISH / BEARISH / NEUTRAL]                                 │
│  Active Edges: ________________________________                      │
├─────────────────────────────────────────────────────────────────────┤
│ MIN 13-15: SESSION PLAN (2 lines)                                     │
│  Line 1: ________________________________________                    │
│  Line 2: ________________________________________                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## THE WEEKLY PLUMBING DEEP DIVE (Monday, +10 min)

On Mondays, extend the workflow by checking:

| Check | Source | Records |
|-------|--------|---------|
| COT report (Friday release) | CFTC | Spec positioning for ES, CL, 6E, 6C, GC |
| UST auction calendar | Treasury.gov | Note refunding dates |
| Balance sheets (Fed, ECB, BoC) | Respective websites | Weekly change for each |
| Cross-currency basis trend | BIS or Bloomberg | Has it widened this week? |
| Quarterly review (if due) | BIS | Big picture flow data |

**Full weekly plumbing check:** `systems/weekly-flow-checklist.md` (10 min)

---

## REFERENCES

- **Liquidity equation formula:** `core/liquidity-equation.md` — the math behind step 2
- **SOFR/repo plumbing:** `core/repo-plumbing.md` — understanding SOFR vs IORB
- **Weekly plumbing check:** `systems/weekly-flow-checklist.md` — tri-region check
- **Daily pre-session:** `systems/daily-pre-session.md` — chart prep after plumbing check
- **Plumbing to trade bridge:** `systems/plumbing-to-trade-bridge.md` — decision tree linking this data to trades
- **MES/MNQ execution:** `trading/mes-mnq-playbook.md` — playbook for today's bias
- **Position sizing:** `systems/position-sizing-by-flow.md` — size based on trade mode
- **HUD (cockpit view):** `plumbing-hierarchy-master.md → Part 6` — full signal hierarchy
- **15 edges:** `plumbing-hierarchy-master.md → Part 5` — edge library
- **Ritual (pre/post session):** `plumbing-hierarchy-master.md → Part 7` — full session rhythm
