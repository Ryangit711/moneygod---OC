# MULTI-ACCOUNT GATEWAY — Trading Multiple Prop Accounts

## "One brain, many accounts. Same analysis, same risk, same journal."

---

## THE TRUTH

There is no single platform that connects to all prop firms. Each firm gives you separate login credentials on their platform. You can't literally trade 5 firms from 1 window.

**But you CAN create a unified execution flow** — the same analysis, the same risk rules, the same journal — applied uniformly across every account. That's the gateway.

---

## THE 4-LAYER ARCHITECTURE

```
LAYER 1: ANALYSIS (TradingView — 1 window)
├── Open once, mark up charts, set alerts
├── This is your brain — same analysis regardless of firm
├── Used for: bias, levels, setups, structural reading
└── ALWAYS the same. No firm-specific analysis.

LAYER 2: EXECUTION (Per-firm platform)
├── MT5 window for FTMO / Funding Pips / The5ers (FX)
├── Tradovate window for MyFundedFutures / TradeDay / Tradeify (futures)
├── Each has its own login, its own rules, its own drawdown
├── You switch between them based on today's instrument
└── Same execution ritual on each: pre-session → trade → journal.

LAYER 3: RISK (Single model, applied uniformly)
├── 0.25% per trade, per account
├── 2% daily max, per account (or 50% of firm's limit)
├── 3% combined daily max across ALL accounts
├── Max 2 trades per account per session
├── If 2 accounts hit daily loss → stop ALL accounts
└── Risk is calculated BEFORE entry, never after.

LAYER 4: JOURNAL (Single source of truth)
├── systems/trade-journal-template.md
├── One journal entry per trade, noting firm + account
├── Weekly review: combined P&L across all accounts
├── Track: which firm performs best, which instrument, which session
└── The journal tells you where to scale and where to cut.
```

---

## THE FIRM COMBINATIONS

### Combo 1: FX + Futures (Recommended)

```
FIRM 1: FTMO (or Funding Pips) — FX/CFDs
├── Instrument: EUR/USD, USD/CAD
├── Platform: MT5
├── Account size: $10K-$25K
└── Purpose: Currency trading during London/NY overlap

FIRM 2: MyFundedFutures (or Apex) — CME Futures
├── Instrument: MES, MNQ
├── Platform: Tradovate (or NinjaTrader)
├── Account size: $25K-$50K
└── Purpose: Index futures during NY session

WHY THIS COMBO:
├── FX trades when futures are thin (London session)
├── Futures trade when FX is thin (NY session)
├── You diversify across markets AND firms
├── If one firm has issues, the other keeps running
└── Different drawdown types (fixed vs EOD) reduce correlated risk
```

### Combo 2: Two FX Firms

```
FIRM 1: FTMO — Most reputable, 2-phase
FIRM 2: Funding Pips — Cheapest, 1-step

WHY: Different eval structures test different skills.
FTMO tests consistency (2 phases). Funding Pips tests speed (1 step).
If you pass both, you're versatile.
```

### Combo 3: Two Futures Firms

```
FIRM 1: MyFundedFutures — EOD drawdown (more forgiving)
FIRM 2: Apex — Trailing drawdown (more aggressive)

WHY: Different drawdown types force different risk management.
EOD lets you hold through intraday volatility. Trailing forces tighter stops.
Mastering both makes you adaptable.
```

---

## THE SCALING PATH

### Stage 1: Prove It (1 Account)

```
Firm: FTMO (FX) or MyFundedFutures (futures)
Account: $10K-$25K
Risk: 0.25% per trade
Goal: Pass eval, take first payout
Timeline: Month 1-3
Rule: DO NOT add a second account until you've taken 2 payouts from this one
```

### Stage 2: Duplicate It (2-3 Accounts)

```
Firms: Same firm, or add a second
Accounts: 2-3 × $10K-$25K
Risk: 0.25% per trade per account
Goal: Prove consistency across multiple accounts
Timeline: Month 3-6
Rule: If account 1 is in drawdown, DO NOT trade account 2
```

### Stage 3: Diversify It (3-5 Accounts, 2-3 Firms)

```
Firms: 1 FX firm + 1 futures firm + 1 backup
Accounts: 3-5 × $10K-$50K
Risk: 0.25% per trade per account, max 3% combined daily loss
Goal: Spread counterparty risk
Timeline: Month 6-12
Rule: Never have >50% of total capital at one firm
```

### Stage 4: Compound It (5+ Accounts)

```
Firms: 3-4 firms, mix of FX and futures
Accounts: 5-10 accounts, $100K+ total funded capital
Risk: 0.25-0.5% per trade per account
Goal: Scale to $10K+/month income
Timeline: Year 1-2
Rule: Scale only after 3 consecutive profitable months at current level
```

---

## MULTI-ACCOUNT RISK RULES

### The Combined Risk Model

| Rule | Value | Why |
|------|-------|-----|
| Risk per trade per account | 0.25% | Limits single-trade damage |
| Max daily loss per account | 2% (or 50% of firm's limit) | Prevents account blowup |
| Max combined daily loss (ALL accounts) | 3% of total funded capital | Prevents portfolio blowup |
| Max trades per account per session | 2 | Prevents overtrading |
| Max accounts in drawdown simultaneously | 2 | If 3+ accounts are losing, stop everything |
| Weekly review | Friday close | Review combined P&L, adjust allocation |

### The Circuit Breakers

| Trigger | Action |
|---------|--------|
| 1 account hits daily loss limit | Stop trading that account for the day |
| 2 accounts hit daily loss limit | Stop ALL accounts for the day. Review. |
| 3+ accounts in weekly drawdown > 5% | Stop ALL accounts for the week. Read plumbing. |
| Total funded capital drops 20% from peak | Stop ALL accounts for 1 week. Reduce size by 50%. |
| 1 firm has payout issues | Immediately stop trading that firm. Move capital to backup. |

### The Anti-Correlation Rule

When trading multiple accounts, DON'T take the same trade on all of them. If you're long EUR/USD on FTMO and long MES on MyFundedFutures, and the market sells off hard, BOTH accounts lose simultaneously.

**Instead:**
- Trade DIFFERENT instruments on different accounts
- Or trade DIFFERENT directions (if you have a hedge thesis)
- Or trade DIFFERENT sessions (FX during London, futures during NY)

The goal of multi-account is diversification, not duplication.

---

## THE DAILY ROUTINE (Multi-Account)

```
5:30 AM PT — PRE-SESSION
├── Open TradingView → mark levels, set bias (5 min)
├── Check live-data-workflow.md → get VERDICT (10 min)
├── Decide: which instrument today? (FX or futures?)
├── If FX → open MT5 (firm 1 or 2)
├── If futures → open Tradovate (firm 3 or 4)
└── Write intention: "I am trading [instrument] on [firm] today."

6:30-9:00 AM PT — EXECUTION
├── 1-2 trades maximum on ONE account
├── Same entry ritual regardless of firm
├── Same risk rules regardless of firm
├── Log every trade in journal immediately
└── If hit daily target → stop. Done.

9:00 AM PT — POST-SESSION
├── Close all positions (if any open)
├── Journal every trade with firm/account noted
├── Update combined P&L tracker
├── Check: did I follow my rules on ALL accounts?
└── 5 min review. Done.
```

---

## THE JOURNAL — Multi-Account Format

Add these columns to your trade journal:

```
| # | Date | Firm | Account | Instrument | Direction | Entry | Exit | Result | R | Setup | Notes |
|---|------|------|---------|-----------|-----------|-------|------|--------|---|-------|-------|
| 1 | D5 | FTMO | $10K | EUR/USD | Long | 1.0850 | 1.0870 | +20 pips | +1R | ORB | Clean fill |
| 2 | D5 | MFF | $25K | MES | Short | 4520 | 4505 | +15 pts | +1R | VWAP Rev | Slight slippage |
```

**Weekly review columns:**
```
| Firm | Account | Weekly P&L | # Trades | Win Rate | Avg R | Notes |
|------|---------|-----------|----------|----------|-------|-------|
| FTMO | $10K | +$450 | 4 | 75% | +0.8R | Good EUR/USD week |
| MFF | $25K | +$300 | 3 | 67% | +0.5R | MES worked well |
| TOTAL | $35K | +$750 | 7 | 71% | +0.7R | Combined |
```

---

## WHEN TO ADD A NEW ACCOUNT

**Add a new account when ALL of these are true:**
- [ ] Current account has taken 2+ consecutive payouts
- [ ] Current account is in profit (not drawdown)
- [ ] You have 30+ trades on current account with positive expectancy
- [ ] Your journal shows consistent rule-following (no overtrading, no revenge)
- [ ] You have the eval fee available without touching living expenses

**DO NOT add a new account when:**
- Current account is in drawdown
- You've blown an eval in the last 2 weeks
- You're feeling pressure to "make up" losses
- You haven't journaled your last 5 trades
- You're trading on emotion (fear, greed, boredom)

---

## THE END STATE

```
YEAR 1: 3-5 accounts, $50K-$100K total funded capital
├── Monthly income: $3,000-$8,000
├── Risk per trade: 0.25%
└── Working hours: 2-3 hrs/day

YEAR 2: 5-10 accounts, $100K-$250K total funded capital
├── Monthly income: $8,000-$20,000
├── Risk per trade: 0.25-0.5%
└── Working hours: 2-3 hrs/day

YEAR 3+: IBKR self-directed + remaining prop accounts
├── Monthly income: $15,000-$50,000+
├── Risk per trade: 0.5-1%
└── Trading is one income stream among many
```

**The gateway is not software. It's discipline applied uniformly across every account you touch.**

---

## REFERENCES

- **Prop firm architecture:** `trading/prop-firm-architecture.md` — every firm, every platform, every market
- **Prop firm specs:** `trading/prop-firm-playbook.md` — detailed comparison with promo codes
- **Paper vs live gap:** `trading/paper-vs-live-gap.md` — execution differences, cost math
- **Eval mode protocol:** `trading/eval-mode-protocol.md` — sizing rules for eval vs funded
- **Fill your cup:** `trading/fill-your-cup.md` — from first payout to freedom
- **Journal template:** `systems/trade-journal-template.md` — log every trade
- **Position sizing:** `systems/position-sizing-by-flow.md` — size by regime
- **Week 1 readiness:** `systems/week-1-readiness.md` — demo setup, risk caps
- **Gangotri protocol:** `systems/gangotri-protocol.md` — plumbing × structure × execution
