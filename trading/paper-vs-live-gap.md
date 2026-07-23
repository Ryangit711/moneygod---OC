# PAPER VS LIVE GAP — The Execution Gap Bible

## "Your demo account is a lie. Not a malicious one — a structural one. It fills you at prices that don't exist in the real market."

---

## THE PERFECT FILL ILLUSION

On a retail demo account (TradingView paper trading, MT5 demo from a broker site, Thinkorswim sim):

| What Demo Gives You | What Actually Happens |
|---------------------|----------------------|
| Zero slippage — fill at exact price | 1-10 ticks slippage during volatility |
| Fixed tight spreads (0.1 pips EUR/USD) | Variable spreads (0.2-5.0 pips depending on session/news) |
| Instant market order fills | Latency: 5-200ms round-trip to server |
| No commissions | $3-$7 per lot on prop firm accounts |
| Stop losses fill at exact price | Stop becomes market order → fills at whatever price is available |
| Limit orders fill the instant price touches | Limit orders sit in queue behind other orders |
| No spread widening at rollover | 5 PM ET rollover = spread minefield |

**The demo is not practice. It's an unrealistic sandbox that makes you feel better than you should.**

---

## THE 6 EXECUTION GAPS (With Exact Cost Math)

### Gap 1: Slippage

**What it is:** The difference between the price you clicked and the price you actually got filled at.

**When it happens:**
- High-volatility moments (NFP, FOMC, CPI releases)
- Fast-moving markets (trend days, gap fills)
- Low-liquidity sessions (Asian session, 5 PM ET rollover)
- Large position sizes relative to available depth

**Real numbers:**

| Instrument | Normal Slippage (1 lot) | News Volatility Slippage | Cost per Tick |
|-----------|------------------------|------------------------|---------------|
| EUR/USD | 0-1 pip | 5-10 pips | $1/pip (standard lot) |
| MES (Micro S&P) | 0-1 tick ($1.25-$5) | 5-10 ticks ($25-$50) | $5/point |
| MNQ (Micro Nasdaq) | 0-1 tick ($0.50-$2) | 5-10 ticks ($10-$20) | $2/point |
| Gold (XAU/USD) | 1-2 pips | 10-30 pips | $1/pip (standard lot) |

**The math on 40 trades/month:**
- Normal conditions: 40 trades × 0.5 pip avg slippage × $10/pip = **$200/month lost to slippage**
- During news: 40 trades × 3 pips avg slippage × $10/pip = **$1,200/month lost to slippage**

**How to measure YOUR slippage:** After every trade, compare your fill price to the price shown on TradingView at the exact moment you clicked. Log the difference. After 10 trades, you have your personal slippage profile.

---

### Gap 2: Variable Spreads

**What it is:** The gap between bid and ask changes throughout the day. Demo accounts often show fixed tight spreads. Prop firm accounts show real variable spreads.

**Real spread data (EUR/USD):**

| Session | Normal Spread | Spread During News | Your Cost per Trade |
|---------|--------------|-------------------|-------------------|
| London Open (11PM-2AM PT) | 0.2-0.5 pips | 2.0-5.0 pips | $2-$50 |
| NY AM (4AM-7AM PT) | 0.1-0.3 pips | 1.0-3.0 pips | $1-$30 |
| NY PM (7AM-9AM PT) | 0.1-0.2 pips | 0.5-2.0 pips | $1-$20 |
| Asian Session (9AM-11PM PT) | 0.5-1.0 pips | N/A | $5-$10 |
| 5 PM ET Rollover | 2.0-10.0 pips | N/A | $20-$100 |

**Why this kills you:** If your stop loss is 10 pips away and spreads widen to 5 pips at rollover, you get stopped out even though price never "touched" your stop. The spread ate the distance.

**Rule:** Never hold positions through 5 PM ET rollover. Close 15 minutes before.

---

### Gap 3: Commissions

**What it is:** Prop firms charge $3-$7 per round-trip lot. Demo accounts charge nothing.

**Commission comparison:**

| Platform | Commission per Round Trip | Monthly Cost (40 trades) |
|----------|--------------------------|------------------------|
| Retail Demo (MT5) | $0 | $0 |
| FTMO (MT5) | $3-$7/lot | $120-$280 |
| Funding Pips (MT5) | $3-$7/lot | $120-$280 |
| Apex (NinjaTrader) | $0.62/contract RT | $24.80 (40 trades) |
| TradeDay (Tradovate) | $0 (commission-free!) | $0 |
| MyFundedFutures (Tradovate) | $0.62-$2.50/contract | $24.80-$100 |

**The hidden killer:** On a $50K eval with 10% target, you need $5,000 gross profit. If you trade 40 times with $5 commission per lot, that's $200 in commissions — 4% of your profit target eaten before you even start.

**Rule:** Factor commissions into your R:R calculation. If your target is 10 pips and commission is $5 per lot, your REAL target is 10 pips minus the spread minus the commission. The net must still be 1:1.5 R:R minimum.

---

### Gap 4: Spread Widening at Session Boundaries

**What it is:** During the 30-minute window around the daily rollover (4:30-5:30 PM ET), global banks reset their ledgers. Spreads blow out.

| Time (ET) | Event | EUR/USD Spread | MES Spread |
|-----------|-------|---------------|-----------|
| 4:30 PM | Pre-rollover | 0.2 pips | 1 tick |
| 4:45 PM | Banks pulling quotes | 1.0-2.0 pips | 2-3 ticks |
| 5:00 PM | Daily close / rollover | 3.0-10.0 pips | 5-10 ticks |
| 5:15 PM | New session opens | 1.0-2.0 pips | 2-3 ticks |
| 5:30 PM | Normalization | 0.3-0.5 pips | 1-2 ticks |

**Why this kills you:** If you have a position open at 5 PM ET with a 10-pip stop loss, and spreads widen to 5 pips, you might get stopped out even though price never reached your stop. The spread gap consumed the distance.

**Rule:** Close all positions 15 minutes before 5 PM ET. No exceptions. The rollover spread is not a risk you take — it's a tax you refuse to pay.

---

### Gap 5: Stop Execution Gap

**What it is:** On demo, stop-loss orders execute at the exact stop price. On live/prop firm accounts, a stop-loss order becomes a MARKET ORDER once triggered — it fills at whatever price is available.

**Example:**
- You set a stop at 1.0850 on EUR/USD
- Price spikes through 1.0850 during NFP
- Demo fill: 1.0850 (exact)
- Live fill: 1.0845 (5 pips worse — price moved through your level before your order reached the exchange)

**Real scenario on MES:**
- Stop at 4500.00
- NFP spike hits 4499.75
- Your stop triggers → becomes market order → fills at 4499.50 (2 ticks worse)
- Cost: 2 ticks × $5/point = $10 extra loss per contract
- On 3 contracts: $30 unexpected loss

**How to mitigate:**
- Widen stops by 1-2 ticks beyond the "obvious" level
- Use hard stop-loss orders placed on the server (never mental stops)
- Avoid holding through high-impact news — flatten 15 min before

---

### Gap 6: Limit Order Queue Position

**What it is:** On demo, limit orders fill the instant price touches your level. On live, your limit order sits in a queue behind every order placed before you at that price.

**The math:**
- On ES during active RTH, there may be 500+ orders queued at a key level
- Your limit order at that level goes to the back of the line
- Price may need to trade THROUGH your level by several ticks before your order fills
- On a scalping strategy targeting 5-10 ticks, this means you miss 30-50% of your entries

**Impact by strategy:**

| Strategy | Limit Order Impact | Mitigation |
|----------|-------------------|------------|
| Scalping (3-5 pip target) | Severe — may miss 50%+ of entries | Use market orders for scalps, accept slippage |
| Day trading (10-20 pip target) | Moderate — may miss 20% of entries | Use limit orders, accept some misses |
| Swing trading (50+ pip target) | Minimal — queue position less important | Use limit orders, wait patiently |

**Rule:** For your first 50 trades, use market orders only. Learn the fill quality first. After 50 trades, you'll know when limit orders work and when they don't.

---

## THE EXECUTION COST CALCULATOR

Before every eval, compute your real cost per trade:

```
TRUE COST PER TRADE = Spread Cost + Slippage Estimate + Commission

Where:
  Spread Cost = avg spread (pips) × pip value × lot size
  Slippage Estimate = avg slippage (pips) × pip value × lot size
  Commission = per-round-trip commission × lot size

Example (EUR/USD, 1 standard lot, FTMO):
  Spread: 0.3 pips × $10 = $3.00
  Slippage: 0.5 pips × $10 = $5.00
  Commission: $5.00
  TRUE COST: $13.00 per trade

Example (MES, 1 contract, Apex):
  Spread: 1 tick × $5 = $5.00
  Slippage: 0.5 ticks × $5 = $2.50
  Commission: $0.62
  TRUE COST: $8.12 per trade

Monthly cost (40 trades):
  EUR/USD: $13 × 40 = $520/month
  MES: $8.12 × 40 = $325/month
```

**If your strategy generates less than 2× your monthly execution cost, it's not profitable.** A strategy that makes $400/month but costs $520/month in execution is a net loser — even if your win rate is 60%.

---

## HOW TO BRIDGE THE GAP — 6 Tactical Rules

### Rule 1: Use Limit Entries Where Possible

| Situation | Use | Why |
|-----------|-----|-----|
| Pullback to known level | Limit order | You control the price, avoid slippage |
| Breakout of range | Market order | Speed matters more than exact price |
| News event | Neither — stand aside | Slippage is unpredictable |
| Opening range breakout | Market order (1 tick past level) | Speed is the edge |

### Rule 2: Widen Stops by 1-2 Ticks

If your analysis says stop at 1.0850, place it at 1.0848 (2 pips wider). This absorbs the spread fluctuation and prevents "spread stop-outs" where price never actually touched your level.

### Rule 3: Trade Only During Peak Liquidity

| Session (PT) | Liquidity | Spread | Slippage | Your Window |
|--------------|-----------|--------|----------|-------------|
| 4:00-5:00 AM | Low | Wide | High | Prep only |
| **5:00-7:00 AM** | **Highest** | **Tightest** | **Lowest** | **PRIME** |
| **7:00-9:00 AM** | **High** | **Tight** | **Low** | **PRIME** |
| 9:00-10:30 AM | Medium | Normal | Normal | Power Hour |
| 10:30 AM+ | Declining | Widening | Increasing | Avoid |

### Rule 4: Never Trade Within 15 Min of Major News

| Event | Time (ET) | Your Action |
|-------|-----------|-------------|
| NFP | First Friday, 8:30 AM | Flat 15 min before, wait 15 min after |
| FOMC | 8 specific dates, 2:00 PM | Flat 15 min before, wait 15 min after |
| CPI | Monthly, 8:30 AM | Flat 15 min before, wait 15 min after |
| PPI | Monthly, 8:30 AM | Flat 15 min before, wait 15 min after |

### Rule 5: Set Max Slippage Tolerance

On MT5: Tools → Options → Trade → Max deviation: set to 3-5 pips.
If the market moves beyond your tolerance, the order is rejected instead of filling at a terrible price.

### Rule 6: Run the Execution Audit

For your first 10 trades on any new platform:

```
Trade # | Your Fill Price | TradingView Price at Click | Slippage | Notes
1       | 1.0852          | 1.0850                      | 2 pips   | Market order, normal
2       | 1.0848          | 1.0850                      | -2 pips  | Positive slippage!
3       | 1.0855          | 1.0850                      | 5 pips   | High vol moment
...
```

After 10 trades, calculate your average slippage. This becomes YOUR slippage constant — factor it into every future R:R calculation.

---

## THE PROP FIRM B-BOOK REALITY

### What's Actually Happening Behind the Scenes

99% of prop firms operate on a **B-Book model** during evaluation:

```
YOU click "Buy" on MT5
  → Order goes to Prop Firm Server
  → Server records it in their internal database
  → NO order goes to any real exchange
  → Your P&L is calculated against the live market feed
  → But your actual position is never placed anywhere
```

**This means:**
- The firm is your counterparty. If you lose, they keep the money.
- If you win, they pay you from other traders' losses (and challenge fees).
- The "live market data" is real. Your fills are simulated against that data.

### Why This Matters for Execution

Even though it's B-Book sim, reputable firms apply **slippage parameters** to make it realistic:
- They won't fill you at prices that don't exist in the real market
- They apply variable spreads that mirror real conditions
- They charge commissions that mirror real broker costs

**But some firms use Virtual Dealer Plug-ins (VDPs)** that can:
- Artificially widen spreads beyond real market conditions
- Delay execution by 200-500ms to worsen your fill
- Create asymmetric slippage (you slip more on entries than exits)

### How to Detect Artificial Slippage

1. Open TradingView with a live EUR/USD feed
2. Open your prop firm's MT5 with their EUR/USD feed
3. Place 10 market orders on the prop firm demo
4. Compare each fill to TradingView's price at the same instant
5. If your average slippage is >1 pip on EUR/USD during normal conditions, the firm may be using a VDP

**Reputable firms (FTMO, The5ers, Funding Pips) have clean execution.** Budget firms with high promotional discounts may use more aggressive VDP settings.

### A-Book vs B-Book vs Hybrid

| Model | What Happens | Who Pays When You Win | Execution Quality |
|-------|-------------|----------------------|-------------------|
| **B-Book** | Firm is your counterparty | Firm pays from their pool | Simulated, may have VDP |
| **A-Book** | Your trades go to real LP | LP pays, firm takes commission | Real market execution |
| **Hybrid** | Good traders → A-Book, rest → B-Book | Varies | Varies by trader tier |

**Most firms are Hybrid:** they evaluate you on B-Book, then move profitable traders to A-Book (or shadow-copy your trades to live markets). This means execution may IMPROVE once you're funded.

---

## THE PSYCHOLOGICAL GAP

The execution gap isn't just technical. It's psychological.

### The 4 Emotional Stages (Paper → Live)

| Stage | When | Feeling | What to Do |
|-------|------|---------|------------|
| **Confidence** | Demo trading | "I'm good at this" | Remember: demo ≠ reality. Your win rate will drop 10-20% on live. |
| **Shock** | First eval trade | "The spread is wider than I expected" | This is normal. Recalculate your R:R with real costs. |
| **Fear** | After first loss on eval | "I'm going to blow this account" | You're still 4% from max loss. Breathe. Trade smaller. |
| **Adaptation** | 20+ trades on eval | "I understand the execution now" | This is where you start being a real trader. |

### The Boredom Trap

On demo, you can take 10 trades a day with no consequence. On eval, you're limited to 1-2 per day at 0.25% risk. Day 10-15 of this, you'll feel:
- "This is too slow"
- "I should size up to hit the target faster"
- "One more trade won't hurt"

**This is the #1 eval killer.** The boredom leads to overtrading, which leads to blowing the account.

**Rule:** If you feel bored during eval, read this file again. The boredom is the discipline working. Lean into it.

---

## THE TRANSITION PROTOCOL — 4-Week Bridge

### Week 1: Realistic Demo (Retail Demo + Execution Assumptions)

| Day | Activity | Purpose |
|-----|----------|---------|
| 1-2 | Trade demo as normal, but SUBTRACT 1 pip from every win and ADD 1 pip to every loss | Simulates slippage |
| 3-4 | Trade demo, but only enter on limit orders (never market) | Learn queue behavior |
| 5-7 | Trade demo with commission: mentally subtract $5 from every winning trade | Factor in real costs |

### Week 2: Prop Firm's Own Demo

| Day | Activity | Purpose |
|-----|----------|---------|
| 1 | Sign up for FTMO's free 14-day demo (or use firm's demo) | Get on their actual feed |
| 2-3 | Trade 1-2 sessions on their demo. Compare fills to TradingView. | Identify execution quality |
| 4-7 | Trade full sessions. Journal every fill. Note slippage. | Build your slippage profile |

### Week 3: Micro-Lot Live Mindset

| Day | Activity | Purpose |
|-----|----------|---------|
| 1-3 | Same demo, but treat it like live. 0.25% risk max. 1 trade per day. | Build discipline |
| 4-5 | Only take A+ setups. Flat if no A+. | Prove you can wait |
| 6-7 | Full pre-session ritual + 1 trade + journal. exactly like eval will be. | Rehearse the eval routine |

### Week 4: Pre-Eval Checklist

```
- [ ] 30+ demo trades on prop firm's feed (not retail demo)
- [ ] Average slippage documented
- [ ] Execution cost calculated (spread + slippage + commission)
- [ ] Win rate after execution costs is still positive
- [ ] R:R maintained at 1:1.5 minimum after costs
- [ ] Pre-session ritual is habitual (not something you have to think about)
- [ ] Journal entries for every trade
- [ ] Max 2 consecutive losses in any 5-trade stretch
- [ ] No overtrading (stayed within 1-2 trades/day for 5+ consecutive days)
```

**All boxes checked → you're ready for eval.**

---

## THE FINAL TRUTH

Paper trading is valuable for learning the platform, learning chart reading, and learning basic execution. But it has ONE fatal flaw: **it doesn't cost you anything when you're wrong.**

Live execution — whether prop firm eval or real capital — introduces:
- Real spreads that eat your R:R
- Real slippage that changes your entries
- Real commissions that reduce your profit
- Real psychology that tests your discipline

**The bridge is not a leap. It's a 4-week stairway.** Walk it. Don't jump.

---

## REFERENCES

- **Prop firm architecture:** `trading/prop-firm-architecture.md` — which firms, which platforms, which markets
- **Prop firm specs:** `trading/prop-firm-playbook.md` — full comparison table with promo codes
- **Multi-account gateway:** `trading/multi-account-gateway.md` — managing multiple funded accounts
- **Eval mode protocol:** `trading/eval-mode-protocol.md` — sizing and rules during challenge
- **Position sizing:** `systems/position-sizing-by-flow.md` — size by regime, not by emotion
- **Week 1 readiness:** `systems/week-1-readiness.md` — demo setup and per-session risk caps
- **Trade journal:** `systems/trade-journal-template.md` — log every trade with execution notes
- **Trading commandments:** `trading/trading-commandments.md` — 10 rules, read before every session
- **MES/MNQ playbook:** `trading/mes-mnq-playbook.md` — instrument-specific execution
- **Gangotri protocol:** `systems/gangotri-protocol.md` — plumbing × structure × execution integration
