# PLUMBING ESOTERICA — What Only Insiders Know

## "The gap between retail plumbing knowledge and what the desks at BIS, primary dealers, and macro hedge funds read daily."

Prerequisites: Read 14-monetary-plumbing-global.md, core/repo-plumbing.md, core/global-flow-map.md first. This file assumes you already understand two-layer money creation, repo mechanics, and the global flow map.

---

## 1. THE EURODOLLAR SYSTEM — The Real Offshore Plumbing

**TL;DR:** The $14T+ offshore USD credit market created by non-US banks outside the Fed's reach. This is THE plumbing layer most retail traders don't know exists. The Eurodollar curve (now SOFR 3-month futures) is the real yield curve.

### What It Actually Is

A Eurodollar is not a currency. It is a **USD deposit held at a bank outside the United States**. That bank could be:
- A foreign bank (e.g., Barclays London, Deutsche Frankfurt, ICBC Shanghai)
- The foreign branch of a US bank (e.g., JPMorgan London)

These deposits are **not subject to Fed reserve requirements, FDIC insurance, or US banking regulation**. They exist in a regulatory void. This is by design — the Eurodollar market was born in the 1950s when London banks started accepting dollar deposits that US regulations pushed offshore.

### Why This Matters More Than the Fed

The Eurodollar market is **larger than US domestic M2**. Estimates range from $13-18T. Global trade financing, emerging market debt, corporate loans, and cross-border investment are denominated in Eurodollars.

**The critical insight:** The Fed controls the price of USD reserves (the Fed Funds rate / IORB). But the Eurodollar market is a **parallel dollar system** where dollars are created by foreign banks through the same loan-deposit process — except without a central bank backstop. When this market seizes, the Fed has to step in via swap lines.

### The Eurodollar Transmission Chain

```
Non-US bank gets USD deposit (from trade, investment, or Eurodollar loan)
  → Bank now has USD liability (the deposit)
  → Bank lends those USD to a borrower (creates a new USD deposit elsewhere)
  → New deposit is also a Eurodollar
  → No US regulation touches this chain
  → The chain continues until someone uses USD to buy something in the US
```

**Key:** Every step in this chain creates dollar credit without a single dollar of Fed reserves being created. The Eurodollar system is **off the Fed's balance sheet**.

### What Insiders Watch

| Data Point | Where | Signal |
|-----------|-------|--------|
| **SOFR 3-month futures curve** | CME (ticker: SR3) | The Eurodollar futures curve reborn. Contango = normal. Backwardation = stress. |
| **Eurodollar deposit rate** | BIS statistics / Bloomberg | Rate at which offshore banks lend USD to each other. Above SOFR = stress. |
| **TED spread (old)** | FRED | LIBOR - T-bill rate. Died with LIBOR. Same concept applies with SOFR-commercial paper spread. |
| **US bank FX deposits** | FRED: bank balance sheets | Foreign deposits in US banks = Eurodollar round-trip. Rising = dollar scarcity offshore. |

### The Eurodollar Thesis (Who Gets It)

The "Eurodollar thesis" — associated with Jeffrey Snider (Alhambra), Robert Heller, Paul McCulley — argues:

> The Eurodollar market is not a subset of the Fed's system. It IS the system. The Fed is downstream of the Eurodollar market, not upstream. Global dollar credit is created primarily offshore. When Eurodollar credit contracts, it causes dollar scarcity that forces the Fed to respond.

**Evidence:** Every major financial crisis since 2008 (2008 itself, 2019 repo spike, 2020 COVID, 2022 UK gilt crisis, 2023 SVB) began with stress in the offshore dollar funding markets — before the Fed was even aware of the problem.

### Trader Actionable

- Watch SOFR 3-month futures curve shape
- When Eurodollar basis (offshore rate minus onshore rate) widens → dollar scarcity → risk-off
- When it narrows → dollar abundant → risk-on
- Compare USD LIBOR (old) vs SOFR (new) spread history to read hidden stress

---

## 2. CROSS-CURRENCY BASIS SWAPS — The Hidden Plumbing Gauge

**TL;DR:** The cost of swapping one currency for another via derivative. When this deviates from zero, it signals dollar scarcity or abundance in the offshore plumbing. **Insiders watch this daily.**

### What It Is

A cross-currency basis swap (XCCY swap) allows Party A to borrow USD and lend EUR (or vice versa) for a fixed period. The "basis" is the spread above or below the standard interest rate that one party pays.

```
Example: European bank needs USD for 3 months
  → Enters EUR/USD XCCY swap
  → Pays EUR interest + basis/spread
  → Receives USD
  → At maturity, reverses

If EUR/USD basis = −30bps:
  → European bank pays 30bps EXTRA for USD
  → Signal: dollars are scarce globally
  → Non-US banks are willing to pay a premium to get USD
```

### Why It Matters

The cross-currency basis is the **price of dollar access for non-US banks**. When it goes deeply negative, it means:
1. Non-US banks cannot get USD cheaply
2. Global dollar credit creation is slowing
3. Plumbing stress is building
4. Eventually the Fed will have to provide swap lines

**Size:** The FX swap and XCCY market is ~$80T+ notional (BIS 2022 triennial). Larger than spot FX. This is where plumbing stress shows up first.

### Key Pairs to Watch

| Pair | What It Tells You |
|------|-------------------|
| **EUR/USD XCCY 3-month** | European bank USD access. Most watched. When deeply negative → dollar scarcity in Europe → risk-off. |
| **USD/JPY XCCY 3-month** | Japanese bank USD access. Japan is the largest holder of US Treasuries. When negative → Japan may sell USTs for USD. |
| **GBP/USD XCCY** | UK bank USD access. UK gilt crisis 2022: GBP basis went deeply negative before the crisis broke. |
| **EUR/USD XCCY 1-year** | Longer-term dollar scarcity signal. Banks can't get term USD funding. |
| **USD/CNH XCCY** | China offshore USD access. When deeply negative → China stress → PBOC intervention. |

### Reading It in Real Time

```
Basis near zero (within ±5bps):
  → Dollar access normal. Plumbing working.
  → Risk-on environment.

Basis −10 to −25bps:
  → Mild dollar scarcity. Watch but don't panic.
  → Reduce size, check other indicators.

Basis −25 to −50bps:
  → Significant dollar stress. Plumbing under pressure.
  → Go defensive. Reduce risk.

Basis −50bps+:
  → Crisis plumbing. Dollar famine.
  → Prepare for Fed swap line announcement.
  → Historically: 2008, 2020, 2022 UK crisis.
```

**Where to see it:** Bloomberg (FXBA), Reuters, or your broker's cross-currency swap screen. Some data via FRED (EUR/USD XCCY series), BIS quarterly.

### Historical Events

| Date | EUR/USD XCCY | What Happened |
|------|-------------|---------------|
| Oct 2008 | −300bps+ | Total dollar freeze. Fed launched unlimited swap lines. |
| Mar 2020 | −100bps+ | COVID freeze. Fed reopened swap lines with 14 CBs. |
| Sep 2019 | −30bps | Repo spike was a Eurodollar crisis, not just US repo. |
| Sep 2022 | −60bps | UK gilt crisis. BoE had to intervene in pension LDI. |

---

## 3. FRA-OIS / PLUMBING STRESS GAUGES

**TL;DR:** The "fear gauge" of the banking system. When banks charge each other more for 3-month funding relative to the risk-free overnight rate, the plumbing is stressed.

### What It Is

**FRA-OIS spread** = 3-month Forward Rate Agreement rate minus 3-month Overnight Index Swap rate.

- FRA: the rate banks expect to pay/receive for 3-month unsecured funding in the future
- OIS: the risk-free rate (expected average overnight rate over 3 months, locked in via swaps)
- **Spread = the premium banks charge each other for unsecured 3-month lending**

The old version was the **LIBOR-OIS spread** (died with LIBOR). Now it's **FRA-OIS** (using SOFR for the OIS leg).

### What It Signals

| FRA-OIS Level | Meaning |
|--------------|---------|
| **0-10bps** | Normal. Plumbing working. No stress. |
| **10-25bps** | Elevated. Some concern. Watch. |
| **25-50bps** | Stress. Banks hoarding cash. Reduce risk. |
| **50-100bps** | Crisis. 2008 levels. Banking system in distress. |
| **100bps+** | Systemic. Total plumbing seizure. |

### Other Stress Gauges

| Gauge | What It Measures | Normal | Stress | Data Source |
|-------|-----------------|--------|--------|-------------|
| **FRA-OIS** | 3-month bank funding cost vs risk-free | <10bps | >25bps | Bloomberg, FRED |
| **TED Spread** (old) | LIBOR vs T-bill (3m) | <30bps | >50bps | FRED (historical) |
| **SOFR vs IORB** | Effective overnight rate vs Fed's floor | Near IORB | Above IORB + 5bps | NY Fed |
| **EFFR vs IORB** | Effective fed funds rate vs interest on reserves | Near IORB | Above IORB | NY Fed |
| **CP-SOFR spread** | Commercial paper vs secured rate | <20bps | >50bps | FRED |
| **CD-SOFR spread** | Certificate of deposit vs secured rate | <25bps | >50bps | FRED |

### Why Most Traders Miss This

Retail trading education doesn't mention FRA-OIS. Even most finance textbooks don't. But every macro hedge fund desk has it on their screen. It's the canary.

**Your weekly check:** Open FRED, type "FRA-OIS" or "TEDRATE" (old). If it's above 25bps, reduce position size. If above 50bps, stop trading.

---

## 4. PRIMARY DEALER POSITIONING — The Plumbers' Own Books

**TL;DR:** The NY Fed publishes which bonds primary dealers are holding. Their positioning tells you where smart money sees risk — weeks before it hits price.

### What It Is

Primary dealers are the 22-24 banks that trade directly with the NY Fed. They are REQUIRED to participate in Treasury auctions and to provide data on their positions.

**The data release:** Every Thursday at ~4:15PM ET, the NY Fed publishes the **Primary Dealer Statistics** (formerly the PD Survey of Market Making and Finance). It shows:
- Dealers' net positions in Treasuries, MBS, agency debt
- Their financing (repo borrowing, reverse repo lending)
- Their derivative exposure

### How Insiders Read It

| Signal | What It Means |
|--------|---------------|
| **Dealers net LONG Treasuries ($B+)** | Dealers holding inventory. They expect rates to fall (prices to rise) or are warehousing for clients. If extreme, they may be forced to hedge. |
| **Dealers net SHORT Treasuries ($B+)** | Dealers positioned for rates to rise. If extreme, they may be covering → rate rally. |
| **Dealers net LONG MBS** | They expect mortgages to outperform. Usually when Fed is buying MBS or cuts expected. |
| **Dealer repo borrowing RISING** | Dealers levering up. Risk-on signal. |
| **Dealer reverse repo LENDING RISING** | Dealers parking cash. Risk-off signal. |
| **Dealer cash balances RISING** | Defensive. Not deploying capital. |

### The Tell: Dealer Treasury Shorts vs Position Limits

Dealers have internal risk limits. When they are max short 10-year Treasuries, a small move against them forces explosive covering → the "short squeeze" in bonds that precedes risk-off events.

**Example:** In early 2020, dealers were massively long Treasuries coming into COVID. When the sell-off hit, they couldn't absorb selling. The Fed had to step in.

**Your weekly check:** Read the NY Fed Primary Dealer Statistics (released Thursday 4:15PM). Look for extreme net positions (>$50B in one direction) as a warning.

---

## 5. FX SWAP FUNDING MARKET — Bigger Than Spot, Invisible to Retail

**TL;DR:** The FX swap market ($80T+ notional) is where banks fund themselves in foreign currency. It's NOT forex trading. It's plumbing. Stress here shows up days before spot moves.

### What It Is

An FX swap is different from a spot forex trade:
- **Spot FX:** I buy EUR/USD today. Delivery in T+2. Pure speculation or hedging.
- **FX swap:** I borrow EUR, lend USD for 1 week, then reverse at a pre-agreed rate. This is **funding**, not speculation.

Banks use FX swaps to:
- Get dollars when they only have local currency
- Fund their USD loan book without having USD deposits
- Arbitrage cross-currency funding costs

### The Hidden Signal

When the **FX swap-implied USD rate** (the rate a bank pays for USD via FX swap) is significantly different from the **direct USD funding rate** (SOFR/Fed Funds), it signals plumbing stress.

| Situation | Signal | Meaning |
|-----------|--------|---------|
| FX swap rate > SOFR by 20bps+ | Banks paying extra for USD via swaps | Dollar scarce. Plumbing stressed. |
| FX swap rate ≈ SOFR | Normal | Pricing efficient. No stress. |
| FX swap rate < SOFR (negative basis) | Rare but happens at quarter-end | Balance sheet constraints distort pricing. |

### How Insiders Trade This

The FX swap market gives **early warning** of dollar scarcity. When you see the EUR/USD FX swap-implied dollar rate spike:

1. Check it before 8:30AM ET (before US data)
2. If elevated → expect risk-off open in ES
3. If combined with negative XCCY basis → confirmed stress
4. Position short ES, long USD, short EM FX

**Where:** Bloomberg (FXSW), or calculate from forward points: `Implied USD rate = (Fwd points / Spot) × (360/days) × 100`

---

## 6. CCP MARGIN CASCADE — The Hidden Liquidity Drain

**TL;DR:** When volatility spikes, clearinghouses demand more margin. This creates an instant liquidity drain that feeds on itself. Insiders anticipate this. Retail gets wiped out.

### What It Is

CCPs (Central Counterparty Clearing Houses) stand between every derivatives trade. When volatility increases, CCPs recalculate risk and demand **initial margin** and **variation margin** from all participants.

**The cascade:**
```
Volatility spikes
  → CCP raises margin requirements for everyone
  → Banks/hedge funds must post more cash or collateral
  → Cash is drained from the system
  → Some participants can't meet margin → forced liquidation
  → More selling → more volatility → CCP raises margin again
  → Repeat until the central bank steps in
```

### The UK Gilt Crisis (Sep 2022) — Perfect Example

UK pension funds used LDI (Liability-Driven Investing) strategies that involved:
- Holding long-dated gilts
- Hedging with interest rate swaps (through CCPs)
- When Truss's mini-budget hit, gilt yields spiked 100bps+ in days
- CCPs demanded more margin on the swap positions
- Pension funds had to sell gilts to raise cash
- Gilt selling → yields up more → CCP demands more margin
- Nearly broke the UK pension system
- BoE stepped in with emergency gilt purchases

### How Insiders Read CCP Stress

| Signal | Where | What It Means |
|--------|-------|---------------|
| **Initial margin rising across asset classes** | CME, LCH, ICE margin notices | CCPs see more risk. Liquidity is about to drain. |
| **Futures open interest dropping while volume rising** | CME data | Forced liquidation. Participants can't hold positions. |
| **Basis between futures and spot widening** | Market data | Arbitrageurs can't fund the trade → plumbing broken. |
| **Settlement fails rising** | DTCC/FRED data | Counterparties can't deliver. Stress in settlement. |
| **Repo fails rising** | NY Fed data | Same. Cash or collateral can't be delivered. |

### Trader Actionable

When margin requirements spike:
1. Do not add positions (you will be caught in the cascade)
2. Reduce size to well below normal
3. Watch for the CB intervention — that's the buy signal
4. Bet on volatility collapsing after intervention

**Your weekly check:** CME margin notices (usually updated on Fridays). If margin is rising for ES, NQ, or CL, reduce size immediately.

---

## 7. COMMERCIAL PAPER & SHADOW BANK PLUMBING — The Canary

**TL;DR:** The short-term funding market for corporations. When CP spreads widen, non-bank credit creation stops. This breaks before everything else.

### What It Is

Commercial paper (CP) is unsecured short-term debt issued by corporations (1-270 days). Asset-backed commercial paper (ABCP) is secured by receivables, mortgages, etc.

**Size:** ~$1T outstanding in US alone.

**Who buys it:** Money market funds ($6T), pension funds, insurance companies.

**Why it matters:** CP is how corporations fund day-to-day operations. When CP market breaks, non-financial companies can't make payroll or pay suppliers. This is the transmission mechanism from plumbing stress to the real economy.

### The Break Sequence

1. Something scares CP buyers (credit event, liquidity fear)
2. MMFs stop rolling CP — they let it mature and don't buy new issuance
3. Corporations can't roll their CP → need to draw bank credit lines
4. Bank credit lines drain deposits → banks need reserves
5. Repo market feels the strain → rates spike
6. Fed has to step in with CPFF (Commercial Paper Funding Facility) or similar

**2008:** CP market froze → AIG, Lehman couldn't fund → systemic collapse
**2020:** CP market froze in March → Fed launched CPFF March 17 → market stabilized

### What Insiders Watch

| Data Point | Where | Signal |
|-----------|-------|--------|
| **AA CP - SOFR spread** | FRED: CP spread | >50bps → stress. >100bps → crisis. |
| **A2/P2 CP - SOFR spread** | FRED | Lower-grade CP spread widening = real panic. |
| **CP outstanding volume** | FRED | Falling fast → MMFs pulling out → plumbing broken. |
| **MMF flows weekly** | ICI (Investment Company Institute) | Inflows to gov MMFs = risk-off. Inflows to prime MMFs = risk-on. |

### Shadow Banking (Non-Bank Financial Intermediation)

Shadow banking = credit intermediation outside the regulated banking system:
- Money market funds ($6T)
- Private credit / direct lending ($2T+)
- Hedge funds (levered via repo/prime brokerage)
- Insurance companies / pension funds (LDI, securities lending)
- Fintech lenders

**Size:** ~$240T globally (FSB 2023 estimate). Larger than traditional banking.

**The plumbing issue:** Shadow banks don't have central bank access. When they need liquidity, they can't go to the discount window. They must sell assets or find repo funding. This makes them the **first to break** in a crisis.

---

## 8. IOER / ON RRP CORRIDOR — The Fed's Control Room

**TL;DR:** The Fed controls short-term rates through a corridor: IORB (floor) and ON RRP (ceiling). When rates break outside this corridor, the plumbing is broken. Insiders watch this daily.

### The Corridor (Post-2021 Framework)

```
Upper bound: ON RRP rate (currently 5.30%)
  ↓
Target: Fed Funds rate (5.25-5.50%)
  ↓
Lower bound: IORB rate (5.40% — actually above the target range now due to the new framework)
```

Wait — the current framework is **floored**. Let me clarify:

**Since 2008 (floor system):**
- IORB (Interest on Reserve Balances) = the floor. Banks earn this on reserves.
- ON RRP rate = the ceiling. Non-banks earn this on cash parked at the Fed.
- Fed Funds trades between them, near IORB.

**Under normal conditions:**
- EFFR (Effective Fed Funds Rate) ≈ IORB
- SOFR (repo rate) ≤ EFFR usually (secured vs unsecured)

### What Breaks

| Situation | Signal | Meaning |
|-----------|--------|---------|
| **EFFR above IORB** | Banks willing to pay more than the floor | Reserve scarcity. Banks competing for reserves. Plumbing stress. |
| **SOFR above IORB** | Same for repo market | Cash shortage. Repo stress. (Sep 2019 signal) |
| **SOFR above ON RRP** | Repo rate above the ceiling | Extreme stress. Fed MUST act. |
| **EFFR at the bottom of the range** | No one needs reserves | Reserves abundant. Plumbing fine. |
| **ON RRP facility usage high ($500B+)** | Cash abundant. Money market funds parking at Fed. | Liquidity abundant. Risk-on. |
| **ON RRP falling fast** | Cash leaving the Fed → buying assets | Bullish for markets. |
| **ON RRP near zero** | Cash buffer gone. Treasury needs to issue bills | Reserve depletion risk. Watch. |

### The Critical Reading (Your Weekly Check)

```
1. Is EFFR at IORB?                              → Normal. Plumbing ok.
2. Is EFFR above IORB?                           → STRESS. Reduce risk.
3. Is SOFR above EFFR by >5bps?                  → Repo stress. Watch TGA.
4. Is ON RRP usage declining or already gone?    → Liquidity buffer depleting.
5. Is TGA rising while RRP falls?                → Liquidity drain. Bearish.
```

---

## 9. CHINA'S PARALLEL PLUMBING — The Decoupling Play

**TL;DR:** China is building a parallel financial plumbing system (CIPS, e-CNY, PBOC swap lines, gold accumulation) that bypasses the USD-dominated SWIFT/CHIPS system. This is the biggest plumbing shift happening NOW.

### CIPS (Cross-Border Interbank Payment System)

- China's alternative to SWIFT
- Launched 2015, growing rapidly
- ~120+ direct participants, ~1,200+ indirect
- Handles ~CNY 80T+ annually (~$11T)
- Still dwarfed by SWIFT's $2,000T+ but growing 20%+ YoY
- Key: combined with mBridge (CBDC cross-border project with Thailand, UAE, HK)

**Signal:** When CIPS transaction volume accelerates + BRICS nations join → USD plumbing is being bypassed. Long-term bearish for USD hegemony. Short-term: capital controls tighten as China tries to stop capital flight.

### PBOC's Toolkit (Not the Fed's Tools)

| Tool | What It Does | Fed Equivalent? |
|------|-------------|-----------------|
| **MLF (Medium-term Lending Facility)** | 1-year loans to banks at PBOC-set rate | Roughly like discount window + QE combined |
| **SLF (Standing Lending Facility)** | Overnight to 7-day emergency loans | Discount window |
| **PSL (Pledged Supplementary Lending)** | Long-term loans for policy banks to fund real estate/urbanization | No Fed equivalent |
| **RRR (Reserve Requirement Ratio)** | Controls how much banks can lend | Fed uses IORB instead |
| **LPR (Loan Prime Rate)** | Benchmark lending rate, set by PBOC from MLF + spread | Fed Funds Rate |
| **Rediscount window** | PBOC lending against commercial paper | Discount window |
| **Central bank bills** | PBOC issues bills to drain liquidity | Reverse repo / ON RRP |

**Key difference:** The PBOC has **more direct control** than the Fed. It sets RRR, MLF rate, LPR, and can direct state-owned banks to lend. The plumbing is less market-driven, more command-driven.

### PBOC Swap Lines

China has swap lines with 40+ countries (Russia, Brazil, Argentina, Saudi Arabia, Pakistan, etc.). These allow settlement in CNY instead of USD.

**Where this matters:** When a country uses the PBOC swap line to pay for Chinese imports in yuan, they bypass the SWIFT/CHIPS USD system entirely. This reduces demand for Eurodollars. Long-term: structural bearish for USD.

### China's Gold Accumulation

The PBOC has been buying gold for 18+ consecutive months (as of 2024-2025). From vault BIS.md:
- China reported ~2,200T+ gold reserves
- Actual estimates: 5,000T+ (unreported purchases)
- Combined with Russia, the BRICS+ gold accumulation is a structural shift

**Signal:** Gold buying accelerates → countries preparing for a multipolar reserve system → USD plumbing faces structural headwind.

### e-CNY (Digital Yuan)

- ~$2B in circulation (2025) — tiny vs M2
- Focused on domestic retail + cross-border pilot (mBridge)
- Not a threat to USD plumbing yet
- BUT: the infrastructure (programmable money, direct PBOC-to-user) is a paradigm shift

### The Decoupling Timeline (Insider View)

| Year | Milestone |
|------|-----------|
| **2023-25** | China + Russia settle ~50% of trade in CNY/RUB. BRICS+ expands. |
| **2025-27** | mBridge goes live with full cross-border functionality. CIPS volume doubles. |
| **2027-30** | Saudi Arabia accepts CNY for oil (partial). Gold-backed BRICS settlement token? |

**Your trade:** Long gold, short USD over 5+ year horizon. But in the near term (daily trading), ignore this. Plumbing shifts take years. Day-trade the flow, not the decade.

---

## 10. BIS STATISTICS — The Central Bankers' Data Feed

**TL;DR:** The BIS publishes the most granular data on global banking flows. Most traders don't know these exist. Reading them gives you a 3-6 month lead on where dollars are flowing globally.

### The Three Key Publications

**A. BIS Quarterly Review (March, June, September, December)**
- The most read publication inside central banks
- Contains analytical features on current plumbing issues
- June issue includes the BIS Annual Report (most important)
- **When:** Watch for "vulnerabilities" language → 3-6 month lead on policy shifts

**B. BIS International Banking Statistics (IBS)**
- **Locational Banking Statistics (LBS):** Cross-border claims/liabilities by country. Shows where dollars are flowing geographically.
- **Consolidated Banking Statistics (CBS):** Ultimate risk basis. Shows bank exposures by borrower nationality, not just booking location.
- **When:** Quarterly data, 3-month lag. Use for position confirmation, not timing.

**C. BIS Debt Securities Statistics**
- Shows who issued how much debt, in which currency, where
- Tracks the growth of offshore currency markets (Eurodollar, euroyen, etc.)

### What Insiders Read

| Data Point | Publication | Signal |
|-----------|-------------|--------|
| **Cross-border USD claims growth** | LBS | When USD claims growth slows → dollar credit contraction → plumbing stress coming |
| **Non-US bank USD funding gap** | CBS | The gap between USD loans and USD deposits at non-US banks. Growing gap = plumbing fragility. |
| **Offshore CNY issuance** | Debt securities | Rising = yuan internationalization. Long-term trend. |
| **FX swap and OTC derivatives outstanding** | BIS OTC derivatives stats | Rising notional = more plumbing that can break. |
| **Shadow banking assets** | FSB Global Monitoring Report (hosted at BIS) | $240T and rising. Every crisis begins here. |

### The Practical Read (Monthly, 20 min)

1. Open BIS.org → Statistics → IBS
2. Check USD cross-border claims growth (quarter-over-quarter)
3. If growth is flat or declining → dollar plumbing is tighter than markets think
4. Cross-reference with FRA-OIS and XCCY basis
5. If all three are signaling stress → positioned for risk-off

---

## 11. SDR MECHANICS — The Stealth Reserve Asset

**TL;DR:** Special Drawing Rights are not a currency but a reserve asset issued by the IMF. The 2021 $650B allocation was the largest in history and was a stealth global liquidity injection that most traders ignored.

### What It Actually Is

SDRs are not money. They are a **claim on IMF member currencies**. An SDR allocation gives a country the right to exchange its SDRs for USD, EUR, JPY, GBP, or CNY from other countries.

**SDR basket (2026):**
- USD 43.38%
- EUR 29.31%
- CNY 12.28%
- JPY 7.59%
- GBP 7.52%

### How It Works

1. IMF allocates SDRs to members proportional to their quota
2. Member receives SDRs on their balance sheet (asset)
3. Member can exchange SDRs for hard currency with another member
4. The other member now holds SDRs and earns interest (SDRi)
5. SDRs can be used for: balance of payments support, CB reserve diversification, FX intervention

### The 2021 Allocation ($650B)

- Largest in history (previous: $250B in 2009)
- 60%+ went to developed economies (proportional to quota)
- Developing economies got less than they needed → they had to borrow from developed economies via SDR on-lending
- Effectively: developed economies gave developing economies access to ~$100B in hard currency without legislative approval

### Plumbing Impact

| Effect | Mechanism | Market Impact |
|--------|-----------|---------------|
| **EM reserve boost** | Developing CBs got free reserves | EM currencies rallied |
| **Global liquidity injection** | $650B equivalent of "free" reserves | Risk-on across markets |
| **USD demand reduced** | Countries could settle with SDRs instead of needing USD | Slight structural bearish USD |
| **Gold signal** | SDR allocations historically precede gold purchases by EM CBs | Bullish gold |

### Trader Actionable

- SDR allocations are rare (only 4 in history: 1970, 1979, 2009, 2021)
- When IMF discusses new allocation → expect EM rally
- When SDR interest rate (SDRi) rises → reserve costs for EM increase → EM currency weakness

---

## 12. NBFI / SHADOW BANKING — Where the Next Break Will Happen

**TL;DR:** The non-bank financial intermediation sector ($240T) is the Achilles heel of the modern plumbing system. No central bank backstop. No deposit insurance. When it breaks, it breaks fast.

### The Landscape

| Entity | Size | Plumbing Role | Vulnerability |
|--------|------|---------------|---------------|
| **Money Market Funds** | $6T+ | Provide short-term funding via repo, CP, CD | Massive redemptions (2008, 2020) |
| **Private Credit** | $2T+ | Direct lending to mid-market companies | No pricing transparency, no secondary market |
| **Hedge Funds** | $4T+ AUM (levered ~3-5x, so $15T+ gross) | Repo borrowing, derivatives, arbitrage | Margin calls, prime broker pullback |
| **Insurance Companies** | $40T+ | LDI, corporate bond holdings, derivatives | CCP margin cascade (2022 UK gilts) |
| **Pension Funds** | $60T+ | LDI, asset allocation | Gilt crisis proved vulnerability |
| **Exchange-Traded Funds** | $10T+ | Passive investing vehicle but plumbing-adjacent | Liquidity mismatch in high-yield/EM |
| **Fintech Lenders** | $200B+ | Direct lending, BNPL | No deposit funding, wholesale funding dependency |

### The Structural Fragility

```
Shadow banks don't have access to:
  → Central bank discount window (no reserves)
  → Deposit insurance (no stable funding)
  → LOLR (no CB backstop)

They rely on:
  → Repo funding (which can be pulled overnight)
  → Prime brokerage (which can be cut)
  → MMF funding (which can freeze)
```

**Every plumbing crisis since 2008 has originated in NBFI:**

| Crisis | NBFI Element | What Broke |
|--------|-------------|------------|
| **2008** | Shadow banking (SIVs, conduits) | ABCP market froze |
| **2019** | Hedge fund repo borrowing | Repo market seized |
| **2020** | MMFs (prime) | CP market froze, MMFs broke the buck |
| **2022 UK** | Pension LDI | CCP margin cascade on swaps |
| **2023 SVB** | Fintech / venture deposits | Uninsured deposit run (not NBFI per se but similar dynamic) |

### Insider Monitoring

| Data | Where | Signal |
|------|-------|--------|
| **MMF flows (weekly)** | ICI.org | Prime MMF outflows = plumbing stress incoming |
| **Private credit default rate** | KBRA, Moody's, Fitch | Rising defaults → private credit funds freeze redemptions |
| **Hedge fund gross leverage** | Prime broker surveys (Goldman, Morgan Stanley) | Falling = de-levering = risk-off |
| **ETF bid-ask spreads** | Market data | Widening = underlying liquidity failing |
| **LDI ratio (hedged vs unhedged)** | BoE financial stability reports | Falling = pension vulnerability rising |

---

## THE INSIDER'S WEEKLY PLUMBING CHECK (5 min)

Once a week, before Monday trading, run this check. It takes 5 minutes. It catches what 99% of traders miss.

```
1.  FRA-OIS spread                          → <10bps = normal. >25bps = stress.
2.  EUR/USD XCCY 3-month basis              → ±5bps = normal. −25bps+ = stress.
3.  SOFR 3-month futures curve               → Contango = normal. Backwardation = stress.
4.  Primary dealer net Treasury position     → >$50B in one direction = warning.
5.  ON RRP facility usage                    → >$500B = liquid. Approaching 0 = watch.
6.  EFFR vs IORB                             → Near IORB = normal. Above = stress.
7.  CP-SOFR spread                           → <20bps = normal. >50bps = stress.
8.  CME margin notices (ES, NQ, CL)          → Rising = volatility + plumbing stress.
9.  BIS quarterly / annual report (if due)   → "Vulnerabilities" language = 3-6mo lead.
10. PBOC MLF rate / RRR changes              → PBOC easing = global liquidity support.
```

**If 3+ signals are flashing simultaneously, reduce size by 50% until they normalize.**

---

## REFERENCES

- Jeffrey Snider — Eurodollar thesis, Alhambra Investment Partners
- Zoltan Pozsar — Shadow banking, collateral, Bretton Woods III
- Perry Mehrling — Money view, dealer of last resort
- BIS Quarterly Review (free on bis.org)
- NY Fed Primary Dealer Statistics (free)
- FRED database (FRA-OIS, CP spreads, MMF data)
- CME margin notices (free on cmegroup.com)
- The Silent Monetary Revolution.md (your vault — LIBOR→SOFR history)
- BIS.md (your vault — BIS power structure)

---

*File: core/plumbing-esoterica.md — What only insiders know. Everything above is missing from retail education.*
