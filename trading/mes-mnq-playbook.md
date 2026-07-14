# MES/MNQ PLAYBOOK — Micro Futures Execution

## "One instrument at a time. One playbook each. Master these."

---

## TABLE OF CONTENTS

- [Instrument DNA](#instrument-dna)
- [Session Map — Vancouver PT](#session-map--vancouver-pt)
- [MES Playbook](#mes-playbook)
- [MNQ Playbook](#mnq-playbook)
- [Edge Integration](#edge-integration)
- [Risk Tables](#risk-tables)
- [The Golden Rules](#the-golden-rules)
- [References](#references)

---

## INSTRUMENT DNA

### MES (Micro S&P 500 E-mini)

| Attribute | Value |
|-----------|-------|
| Symbol | MES |
| 1 Tick | $1.25 |
| 1 Point | $5 |
| Point Value per Contract | $5 |
| Avg Daily Range | ~60 pts (~$300/contract) |
| Session | Nearly 24h (Sun 6pm ET — Fri 5pm ET) |
| Best Hours (PT) | 6:30-10:30 AM (NY session) |
| Margin (intraday, typical) | ~$50-100/contract |
| Correlation | Inverse to DXY, direct to risk-on/off |
| Liquidity | Extremely high — tight spreads, massive volume |

### MNQ (Micro Nasdaq-100 E-mini)

| Attribute | Value |
|-----------|-------|
| Symbol | MNQ |
| 1 Tick | $0.50 |
| 1 Point | $2 |
| Point Value per Contract | $2 |
| Avg Daily Range | ~150 pts (~$300/contract) |
| Session | Nearly 24h (Sun 6pm ET — Fri 5pm ET) |
| Best Hours (PT) | 6:30-10:30 AM (NY session) |
| Margin (intraday, typical) | ~$80-150/contract |
| Correlation | Tech-heavy — moves faster than MES |
| Liquidity | Very high — wider swings than MES |

**Key difference:** MNQ moves ~2.5x faster than MES in points, but 1 contract of each has similar $/pt exposure ($5/pt MES vs $2/pt MNQ × ~2.5x volatility = similar $ risk). Both are valid. Choose based on which index your edge aligns with.

---

## SESSION MAP — VANCOUVER PT

Your primary window is the **NY session**. Here's the breakdown:

| Time (PT) | Phase | What Happens | MES/MNQ Behavior |
|-----------|-------|-------------|-------------------|
| 1:00-6:30 AM | Pre-NY (electronic) | Thin liquidity, Asia/London prints range | Low volume — avoid entries, use for level prep |
| **6:30 AM** | **NY Open** | **Bell rings — highest volume** | **First 15-min candle sets the ORB range** |
| 6:30-7:00 AM | NY Open — watch only | Institutions print, algos fight for position | Do not trade. Let the book build. |
| **7:00-9:00 AM** | **Trend Establishment** | Direction emerges from open | **Prime window — 60% of daily range prints here** |
| 9:00-10:30 AM | Lunch chop | Low volume, false breakouts | Stand aside or scalp tight |
| **10:30 AM-12:30 PM** | **Power Hour** | Into-close positioning | **Second prime window — MES trades best here** |
| 12:30-1:00 PM | Close | MOC orders, settlement prints | News-driven spikes only |
| 1:00 PM+ | Post-close | Thin again | Avoid — low liquidity = whipsaw |

**Your trading window:** 7:00-9:00 AM PT AND/OR 10:30 AM-12:30 PM PT. Trade one or both. 3-hour max session per day.

---

## MES PLAYBOOK

### Strategy 1: The ORB (Opening Range Breakout) — MES

Same concept as the FX ORB, adapted for micro futures.

**Setup:**
1. NY opens at 6:30 AM PT
2. Let the first 15-min candle print (6:30-6:45 AM PT)
3. Mark the HIGH and LOW of that candle = your ORB range
4. Wait for price to break AND hold above high (long) or below low (short)
5. Entry: 1 tick past breakout level, confirmed by 1-min candle close beyond

**Entry Conditions:**
- Breakout candle closes beyond ORB range on the 1-min chart
- Volume is above the 20-period average volume
- TICK (NYSE Tick Index) confirms direction: +500+ for longs, -500+ for shorts
- No major news print in the next 30 min

| Direction | Entry Trigger | Stop | Target 1 | Target 2 |
|-----------|--------------|------|----------|----------|
| Long | Price breaks above ORB high + volume + TICK > +500 | 1-2 ticks below ORB low | 10 pts ($50) | 20 pts ($100) |
| Short | Price breaks below ORB low + volume + TICK < -500 | 1-2 ticks above ORB high | 10 pts ($50) | 20 pts ($100) |

**R:R table (1 contract MES, $5/pt):**

| Stop Dist (pts) | Stop ($) | Target 1 (10pt) R:R | Target 2 (20pt) R:R |
|----------------|---------|---------------------|---------------------|
| 5 pts ($25) | $25 | 1:2 | 1:4 |
| 8 pts ($40) | $40 | 1:1.25 | 1:2.5 |
| 10 pts ($50) | $50 | 1:1 | 1:2 |

### Strategy 2: The VWAP Reversion — MES

Trade when price is extended from VWAP at the lunch period (9:00-10:30 AM PT).

**Setup:**
1. Calculate distance from VWAP as a % of ATR(14)
2. If price > VWAP by > 0.5 ATR AND VWAP is flat/sloping down → mean reversion short
3. If price < VWAP by > 0.5 ATR AND VWAP is flat/sloping up → mean reversion long

| Direction | Entry | Stop | Target |
|-----------|-------|------|--------|
| Short | Price 0.5 ATR above VWAP with rejection wick | Above recent swing high | Return to VWAP |
| Long | Price 0.5 ATR below VWAP with rejection wick | Below recent swing low | Return to VWAP |

**Volume confirmation:** If volume is declining on the extended move, the move is exhausting. The reversion is high probability.

### Strategy 3: The Power Hour Momentum — MES

Trade from 10:30 AM-12:30 PM PT using the morning's established trend.

**Setup:**
1. Determine the morning trend (7-9 AM PT): up, down, or range
2. If trending: wait for a pullback to the 10-period EMA on the 5-min chart
3. Enter in the direction of the established trend
4. Target: the pre-lunch high/low (the extreme before 9 AM PT)

| Trend | Entry | Stop | Target |
|-------|-------|------|--------|
| Morning was up, pullback to 10 EMA | Long at EMA bounce | Below the pullback low | Pre-lunch high |
| Morning was down, pullback to 10 EMA | Short at EMA rejection | Above the pullback high | Pre-lunch low |

**Rule:** If the morning was a range (not trending), skip Power Hour. Ranges that continue into close are traps.

---

## MNQ PLAYBOOK

### Strategy 1: The Breakout Scalp — MNQ

MNQ moves faster than MES. Trade it when tech stocks are driving the session.

**Setup:**
1. Identify the 15-min range from 6:30-7:00 AM PT (first 2 candles)
2. Mark the high and low
3. Wait for breakout with volume
4. Scalp 20-40 pts per trade

| Direction | Entry | Stop | Target 1 | Target 2 |
|-----------|-------|------|----------|----------|
| Long | Break above 15-min range high + volume | Below range low by 5 pts | 20 pts ($40) | 40 pts ($80) |
| Short | Break below 15-min range low + volume | Above range high by 5 pts | 20 pts ($40) | 40 pts ($80) |

**R:R table (1 contract MNQ, $2/pt):**

| Stop Dist (pts) | Stop ($) | Target 1 (20pt, $40) R:R | Target 2 (40pt, $80) R:R |
|----------------|---------|--------------------------|--------------------------|
| 10 pts ($20) | $20 | 1:2 | 1:4 |
| 15 pts ($30) | $30 | 1:1.33 | 1:2.67 |
| 20 pts ($40) | $40 | 1:1 | 1:2 |

### Strategy 2: Opening Gap Play — MNQ

When MNQ opens gapping up or down from previous close, there's a ~70% probability of a gap fill within the first 2 hours.

**Setup:**
1. Check the gap from previous day's close to today's open
2. If gap > 50 pts, it will likely fill
3. Wait for the initial move to exhaust (first 15-min candle)
4. Enter toward the gap fill

| Gap Direction | Play | Entry | Stop | Target |
|--------------|------|-------|------|--------|
| Gap up | Long the fill (short the gap) | Wait for bearish rejection at gap high | Above gap high by 10 pts | Gap fill level |
| Gap down | Short the fill (long the gap) | Wait for bullish rejection at gap low | Below gap low by 10 pts | Gap fill level |

**Rule:** If the gap doesn't start filling within 90 min of the open, the play is invalid. The trend is real.

### Strategy 3: Sector Rotation Read — MNQ

MNQ is dominated by mega-cap tech (AAPL, MSFT, GOOGL, AMZN, NVDA, META). When a sector rotation is happening (e.g., money moving from growth to value), MNQ diverges from MES.

**Setup:**
1. Compare MES vs MNQ price action over the last 2 hours
2. If MES is up but MNQ is flat/down → money leaving tech (bearish MNQ bias)
3. If MNQ is leading MES to the upside → tech is driving (bullish MNQ bias)

| Divergence | Play | Entry |
|-----------|------|-------|
| MNQ weaker than MES | Short MNQ on bounces | Fade rallies in MNQ |
| MNQ stronger than MES | Long MNQ on dips | Buy pullbacks in MNQ |

---

## EDGE INTEGRATION

These playbooks connect to the 15 trading edges from `plumbing-hierarchy-master.md Part 5`. Here's when each playbook applies based on which edge is active:

| Active Edge (from Part 5) | Playbook to Use | Bias | Size |
|---------------------------|----------------|------|------|
| Edge 1: CB Pivot Play | MES Power Hour | Direction of expected policy | Normal |
| Edge 2: RRP-to-Zero Squeeze | MES ORB | Bullish when RRP draining | Normal+ |
| Edge 3: TGA Directional | MES ORB + VWAP Reversion | Direction of TGA flow | Normal |
| Edge 4: Primary Dealer Contrarian | Both | Inverse to dealer positioning | Normal |
| Edge 5: COT Speculative Extreme | VWAP Reversion | Fade the extreme | Reduced |
| Edge 6: Gamma Squeeze | MNQ Gap Play | Direction of squeeze | Normal+ if early |
| Edge 7: Repo Market Stress | None — stand aside | Risk-off | Flat or micro |
| Edge 8: Cross-Currency Basis | MES VWAP Reversion | Short risk if dollar shortage | Reduced |
| Edge 9: Quarter-End Rebalance | MES Power Hour | Fade the quarterly trend | Normal |
| Edge 10: Dealer Gamma Flip | MNQ Breakout Scalp | Trend direction after flip | Normal+ |
| Edge 11: Liquidity Void | MNQ Breakout Scalp | Direction of void sweep | Normal |
| Edge 12: CTA Stop Run | MES VWAP Reversion | Fade the breakout | Normal |
| Edge 13: Wholesale Order Flow | MES ORB | Fade newsless drift | Normal |
| Edge 14: Funding Trade Unwind | MNQ Breakout Scalp | Direction of unwind | Normal |
| Edge 15: BIS Quarterly Watch | Any | Long-term direction | Reduced (small position) |

**For each edge definition, open:** `plumbing-hierarchy-master.md → Part 5 → [Edge #]`

---

## RISK TABLES

### Per-Trade Risk ($) by Account Size and Position Count

**MES ($5/pt):**

| Account | 1 MES | 2 MES | 3 MES | Max Risk/Day (3%) |
|---------|-------|-------|-------|-------------------|
| $2,000 | $20 | $40 | $60 | $60 |
| $5,000 | $50 | $100 | $150 | $150 |
| $10,000 | $100 | $200 | $300 | $300 |
| $25,000 | $250 | $500 | $750 | $750 |

**MNQ ($2/pt):**

| Account | 1 MNQ | 2 MNQ | 3 MNQ | Max Risk/Day (3%) |
|---------|-------|-------|-------|-------------------|
| $2,000 | $20 | $40 | $60 | $60 |
| $5,000 | $50 | $100 | $150 | $150 |
| $10,000 | $100 | $200 | $300 | $300 |
| $25,000 | $250 | $500 | $750 | $750 |

### Static Max Risk (Regardless of Account)

| Limit | Value |
|-------|-------|
| Max risk per trade | $100 (matches 1$ = 1%) or 2% of eval account |
| Max risk per day | 3% of account |
| Max trades per day | 3 |
| Max consecutive losses | 2 → stop for the day |
| Daily profit target | 2R average → strongly consider stopping |
| Weekly max loss | 6% of account |

**For prop eval accounts, see:** `trading/eval-mode-protocol.md`

---

## THE GOLDEN RULES

1. **Trade one instrument per session.** Either MES OR MNQ. Not both. Switching mid-session is a loss pattern.

2. **First 30 min of every session (6:30-7:00 AM PT):** Watch only. The first 15-min candle sets the range. The second 15-min candle confirms or rejects it. Trade starts at 7:00 AM.

3. **If no setup by 9:00 AM PT, stop looking for MES/MNQ.** Wait for Power Hour (10:30 AM). If no setup there either, the day is a loss. Take it. Don't force.

4. **Gap days: size down by 50%.** Gap opens mean the overnight session had news you slept through. The first hour is algos finding fair value. Let them.

5. **News prints: flat 15 min before and 15 min after.** The algos front-run. The initial spike is noise. The real move starts 15 min after.

6. **When plumbing edges say "stand aside" (Edge 7, Edge 8 with extreme dollar shortage), stand aside.** The market will be there tomorrow. Your account might not be.

7. **MMM rules (from hierarchy Part 6):** Setups MUST have all 5 elements before entry — Bias, Level, Trigger, Stop, Target. If one is missing, no trade.

---

## REFERENCES

- **Edge definitions:** `plumbing-hierarchy-master.md → Part 5` (lines 1998-2160) — 15 trading edges
- **HUD:** `plumbing-hierarchy-master.md → Part 6` (lines 2162-2250) — full trading cockpit
- **Ritual:** `plumbing-hierarchy-master.md → Part 7` (lines 2253-2325) — pre/post-session, weekly, monthly
- **Position sizing by liquidity:** `systems/position-sizing-by-flow.md` — determines account risk % per regime
- **Prop firm rules:** `trading/eval-mode-protocol.md` — different sizing for eval vs funded
- **Prop firm specs:** `trading/prop-firm-playbook.md` — Goat/FTMO/Apex comparison
- **Commandments (pre-session read):** `trading/trading-commandments.md` — 10 rules
- **Daily pre-session:** `systems/daily-pre-session.md` — 5-min ritual
- **Live data workflow:** `systems/live-data-workflow.md` — plumbing data → trade decision
