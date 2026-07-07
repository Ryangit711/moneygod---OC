# LIQUIDITY EQUATION — The Master Formula
## Net Liquidity = The Single Metric That Drives 90% of Asset Prices

## THE EQUATION

```
NET LIQUIDITY = Δ Central Bank Balance Sheet
              − Δ Treasury General Account (TGA)
              − Δ Reverse Repo Facility (RRP)
```

### Why This Works

Central bank balance sheet expansion = new reserves entering the system.
TGA rising = Treasury pulling money out of the banking system (liquidity drain).
RRP rising = money sitting idle at the Fed, not circulating (liquidity drain).

**When Net Liquidity > 0:** Risk assets rally. Equities, crypto, commodities, EM.
**When Net Liquidity < 0:** Risk assets decline. Cash is king.

---

## TRI-REGION APPLICATION

### 🇺🇸 US — Fed Dominates Global Liquidity

| Component | What It Is | Where to Check | Signal |
|-----------|-----------|----------------|--------|
| **Fed Balance Sheet** | Total assets: Treasuries + MBS + loans | FRED: WALCL | ↑ = liquidity injection |
| **TGA** | Treasury's cash at Fed | FRED: WDTGAL | ↑ = liquidity drain (taxes, debt issuance) |
| **RRP** | Overnight reverse repo (money market funds parking at Fed) | FRED: RRPONTSYD | ↑ = liquidity drain (money idle) |
| **ON RRP** | Overnight reverse repo facility usage | NY Fed RRP page | Same as RRP, daily view |
| **BTFP / Discount Window** | Emergency lending facilities (only active during stress) | Fed H.4.1 | ↑ = stress in banking system |

**US Net Liquidity Proxy:** `Δ Fed BS − Δ TGA − Δ RRP`
- When positive → buy risk
- When negative → sell risk

### 🇨🇦 Canada — BoC Follows, Commodity Amplifies

| Component | What It Is | Where to Check | Signal |
|-----------|-----------|----------------|--------|
| **BoC Balance Sheet** | Total assets (GoC bonds, repos, advances) | BoC website | ↑ = liquidity injection |
| **Chartered Bank Credit** | Money creation via lending | StatsCan | ↑ = broad money growing |
| **GoC Bond Auctions Bid-to-Cover** | Demand for Canadian debt | Finance Canada | ↓ < 2.0 = weak demand |
| **WTI Inventory (EIA)** | Crude storage level | EIA Weekly | ↓ = bullish CAD |
| **Housing Market** | Sales, prices, mortgage credit | CREA, CMHC | ↑ = domestic liquidity growing |

**Note:** Canada's liquidity is ~70% imported from US via trade and capital flows.
BoC independence is a myth — Canada's rates follow Fed's rates with lag.

### 🇪🇺 Europe — ECB Manages a Fragmented Union

| Component | What It Is | Where to Check | Signal |
|-----------|-----------|----------------|--------|
| **ECB Balance Sheet** | Total assets (mainly bonds) | ECB website | ↑ = liquidity injection |
| **TLTRO Repayments** | Banks repaying cheap ECB loans | ECB data | ↓ repayments = liquidity staying |
| **PEPP / APP** | Pandemic/long-term asset purchases | ECB data | ↓ = tightening |
| **Target2 Balances** | Cross-border claims within Eurosystem | ECB data | ↑ divergence = stress |
| **EUR/USD Basis Swap** | Cost to convert EUR to USD | Bloomberg | ↑ negative = dollar shortage in Europe |

**Key Insight:** The Eurodollar market (dollars held outside US) is the hidden plumbing.
European banks borrow and lend USD offshore. When the basis swap widens, there's a dollar shortage abroad → global risk-off.

---

## LIQUIDITY CYCLE PHASES

```
PHASE 1                    PHASE 2                     PHASE 3
INJECTION                  PEAK                        DRAINAGE
────────                    ────                        ────────
 Fed BS ↑                   Fed BS flat               Fed BS ↓
 TGA ↓                      TGA at low                 TGA ↑ (taxes)
 RRP ↓                      RRP at low                 RRP ↑
 Net Liq > 0                Net Liq ≈ 0               Net Liq < 0
                            ────                        ────────
Everything rallies          Market tops,               Everything falls,
biggest gains early         volatility spikes          cash outperforms
```

---

## THE WEEKLY LIQUIDITY READ (5 Minutes)

### Every Wednesday (Fed H.4.1 release at 4:30pm ET):

```python
# Pseudo-calculation:
Delta_Fed_BS        = this_week_fed_bs - last_week_fed_bs
Delta_TGA           = this_week_tga - last_week_tga
Delta_RRP           = this_week_rrp - last_week_rrp

net_liquidity       = Delta_Fed_BS - Delta_TGA - Delta_RRP

if net_liquidity > 50e9:     # $50B+ injection
    signal = "STRONG RISK-ON"
elif net_liquidity > 10e9:   # $10B-50B
    signal = "MILD RISK-ON"
elif net_liquidity < -10e9:   # drain
    signal = "LIQUIDITY DRAINING — CAUTIOUS"
elif net_liquidity < -50e9:   # major drain
    signal = "RISK-OFF — DEFENSIVE"
```

---

## DRAWDOWN OF THIS EQUATION

**Remember from 07-what-money-actually-is-no-bs.md:**
The trader is not creating value. The trader is reading the pipes and placing their bucket in the current. This liquidity equation is the **most reliable map of where the current flows.**

**The equation doesn't predict. It reads the present.** When the Fed is injecting and TGA is draining, money IS flowing. Your job is to be in the path.

---

## REFERENCES

- [05-how-money-flows-in-the-system.md] — Central bank pump, 3-pool model
- [13-weekly-flow-tapping-operating-system.md] — The OS this powers
- [14-monetary-plumbing-global.md] — Reserves, Eurodollar, global flows
- [tri-region-flow-map.md] — How the regions connect
