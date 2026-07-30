# ASSIMILATION PROTOCOL — The Kernel for All Incoming Information

**Status:** CORE KERNEL — sits alongside `GROWTH_PROTOCOL.md`, `SYMBIOTIC_MAP.md`, and `CURRICULUM.md`.
**Function:** When ANY new information enters the system (Arena chat, journal entry, book excerpt, trade observation, AI insight, life event, news, random thought), this protocol decides WHERE it goes, WHY it goes there, and HOW it connects to what already exists.
**Origin:** Authorized 2026-07-29. This is the permanent operating system for information flow. Nothing in this file is ever deleted — only extended.

---

## THE PRINCIPLE

> **The reef is already alive. (See `SYMBIOTIC_MAP.md`.) When a new piece of information arrives, do not drop it on the sand. Find its organism. Attach it. The reef grows by one cell. NOTHING is lost. EVERYTHING finds a home.**

Like groceries arriving at a kitchen:
- Salt → salt box
- Chili flakes → chili flakes jar
- Eggs → egg tray
- Receipt → receipt drawer
- New spice with no jar yet → new jar, labelled, placed on the correct shelf

Like Cybertron absorbing an old Autobot's parts:
- The part knows what it is
- The body knows where it goes
- Assimilation is automatic because the taxonomy is absolute
- Nothing is overwritten. The new part enhances what was already alive.

---

## THE THREE KINGDOMS (Inherited from SYMBIOTIC_MAP.md)

Every piece of trading-relevant information belongs to exactly ONE primary kingdom. Some pieces bridge two — these get a primary home and a synaptic link to the secondary.

```
PLUMBING KINGDOM          BRIDGE KINGDOM          TRADING KINGDOM
(What IS)                 (What it MEANS)         (What I DO)
─────────────────         ────────────────         ──────────────
core/ (6 files)           systems/ (9+ files)      trading/ (9+ files)
plumbing-hierarchy-       live-data-workflow       commandments
master.md (12 parts)      plumbing-to-trade-bridge mes-mnq-playbook
14-monetary-plumbing      3hr-daily-schedule       eval-mode
05-how-money-flows        daily-pre-session        prop-firm
01-07 foundation files    weekly-flow-checklist    ORB-strategy
                          position-sizing-by-flow  fill-your-cup

+ Foundational extensions (added 2026-07-29):
00-background-edge        s01-mathematics          s06-fx-execution
s02-trading-psychology    s03-volume-profile       s07-futures-execution
s04-backtesting           s05-intraday-structure   s08-advanced-risk
s09-journaling            s10-institutional-       s11-trading-business
                          plumbing-eurodollar      s12-capital-management
s13-options-mechanics     s14-algorithmic-trading
```

**If information doesn't fit any kingdom, it doesn't belong in this repo.**
Moneygod is the CASH ENGINE. Family pressures, spiritual insights, personal journal entries belong in `aman-os` (see `ARCHITECTURE/LINKS.md`), NOT here — UNLESS they directly affect a trading decision (in which case they home to `00-background-edge.md` or `s02-trading-psychology.md`).

---

## THE TAXONOMY — Where Each Type of Information Goes

| Incoming Info Type | Primary Home | Secondary Link | Rule |
|--------------------|--------------|----------------|------|
| **Personal journal / life event affecting trades** | `00-background-edge.md` | `s02-trading-psychology.md` | If it changes YOUR psychological state while trading → it belongs here |
| **Emotional reaction to a trade or session** | `s02-trading-psychology.md` | `00-background-edge.md` | Pure psychology insights go to s02. Background context goes to 00. |
| **Arena chat log / AI insight about markets** | `s00-concept-registry.md` (NEW, when created) + most specific existing file | `plumbing-hierarchy-master.md` | If the concept is new → registry + create file. If existing → augment the existing concept's primary file. |
| **Trade journal entry** | `s09-journaling-and-performance-analysis.md` | Trade-specific playbook (e.g., `mes-mnq-playbook.md`) | Every trade goes to s09. Cross-link to the strategy file used. |
| **New setup / pattern observed live** | `s04-backtesting-and-system-development.md` (if rule-set) OR `s03-volume-profile-and-order-flow.md` (if volume pattern) | The trading playbook for that instrument | If it's a repeatable rule → s04. If it's a one-time observation → journal it in s09. |
| **Mathematical insight / probability / position-sizing formula** | `s01-mathematics.md` | `s08-advanced-risk-and-position-sizing.md` | Numbers go to s01. Sizing context goes to s08. |
| **Tax / business / corporate structure question (Canada-specific)** | `s11-trading-business-and-tax.md` | `12-who-knows-this-level.md` (if philosophical) | All Canadian tax/business questions go to s11. |
| **Capital scaling / prop firm / withdrawal rule question** | `s12-capital-management-and-scaling.md` | `trading/prop-firm-architecture.md` | All scaling questions go to s12. Existing prop firm map cross-references. |
| **Options / gamma / delta / 0DTE mechanic** | `s13-options-mechanics-for-futures-traders.md` | `plumbing-hierarchy-master.md` Part 5 (15 edges) | All options-for-futures-traders questions go to s13. |
| **Platform / tooling question (MT5, Tradovate, TradingView, ThinkPads)** | `quickstart/02-platform-setup.md` (if beginner) OR `s14-algorithmic-and-semi-automated-trading.md` (if automation) | `basics/` files | Tools go to quickstart. Automation goes to s14. |
| **Order flow / volume profile / delta / microstructure observation** | `s03-volume-profile-and-order-flow.md` | `06-day-trading-tap-the-flow.md` | Microstructure insights go to s03. They bridge to the existing 06 file. |
| **Intraday session behavior / opening drive / power hour / gamma close** | `s05-intraday-market-structure.md` | `14-forex-clock-resources.md` | Intraday timing goes to s05. Session clock reference stays in 14. |
| **Macro plumbing / central bank / repo / Eurodollar / liquidity** | `s10-institutional-plumbing-and-eurodollar.md` (trade-relevant) OR `core/plumbing-esoterica.md` (deep theory) | `plumbing-hierarchy-master.md` | Trade-relevant macro → s10. Pure theory → core/. Deep dive → hierarchy-master. |
| **Risk / drawdown / correlation / position sizing question** | `s08-advanced-risk-and-position-sizing.md` | `systems/position-sizing-by-flow.md` (existing) | Advanced risk questions go to s08. The existing position-sizing file stays. |
| **Psychology risk / negative state detection / "flag the negatives"** | `s02-trading-psychology.md` | `00-background-edge.md` (Section 5: Danger Zone) | All negatives go to s02's negatives section. Personal-context negatives go to 00. |
| **General philosophical insight about money / system / power** | Match by era: `01-origins` (prehistory), `02-real-meaning` (Greek), `03-money-as-debt` (modern), `04-what-the-powerful-understand` (power), `07-what-money-actually-is` (synthesis) | `plumbing-hierarchy-master.md` Part 0 (Philosopher's Foundation) | Philosophy doesn't all go to one file — it matches the era. |
| **Book / paper / external reference recommendation** | `references/master-reference-list.md` | The file that prompted the recommendation | All external refs go to the master list. Cross-link from the recommending file. |
| **Coding / Pine Script / Python / automation snippet** | `s14-algorithmic-and-semi-automated-trading.md` | — | All code goes to s14. Don't inline code in unrelated files. |
| **Conversation record / session log** | `conversations/` directory | — | One file per session. Date-prefixed: `YYYY-MM-DD_topic.md` |
| **Anything not in this table** | **Stop. Do not assimilate.** Ask: does this belong in moneygod (cash engine) or aman-os (life OS)? If neither, it doesn't belong anywhere in the system. | — | The taxonomy is absolute. If it doesn't fit, it doesn't belong. |

---

## THE ASSIMILATION SEQUENCE — Step by Step

When new information arrives, run this sequence in order. No exceptions.

### Step 1: Classify (≤ 30 seconds)

Read the incoming info. Ask:
1. Is it about trading/money/markets? If NO → not for moneygod. Stop.
2. Which row of the taxonomy table above fits? Pick the row.
3. Is it about YOU (your psychology, your edge, your danger) or about THE SYSTEM (plumbing, math, mechanics)?

You now have: **primary home** + **secondary link** (if any).

### Step 2: Check the Concept Registry

Open `systems/s00-concept-registry.md` (when it exists). Search for the concept.

- If the concept EXISTS: the registry tells you the primary file. Go there.
- If the concept does NOT EXIST: this is a NEW neuron. Add a registry entry. Then proceed.

(If the registry doesn't exist yet, skip this step — it will be created as Batch 1 of execution.)

### Step 3: Home the Information

Open the primary home file. Two cases:

**Case A — Concept exists in the file:**
Append a new subsection under the existing section. Do NOT overwrite the existing definition. Format:

```markdown
### [Section Name] — Augment (YYYY-MM-DD)

[New information that extends the existing understanding.]
```

**Case B — Concept does not exist in the file:**
Append a new section. Format:

```markdown
### [New Concept Name]

[Definition / explanation / insight.]
```

### Step 4: Create the Synaptic Connection

At the bottom of the primary home file, in the `## Synaptic Connections` section (added to every file — see Batch 2 of execution), add or update the row linking to the secondary home:

```markdown
| [[secondary-home.md]] | [1-line reason for the connection] | [fire-when condition] |
```

If the secondary file already has a synaptic section, add a reciprocal row there too. **Bidirectional links are non-negotiable.**

### Step 5: Update the Concept Registry

Open `systems/s00-concept-registry.md`. If the concept is new, add:

```markdown
╔═══════════════════════════════════════════════════════════╗
║ CONCEPT: [name]                                          ║
║ Source: [where the info came from]                       ║
║ Quantum state: exists in [N] files                      ║
║                                                          ║
║ Fires in:                                                ║
║   [[primary-home.md]] — [type: core-def / example /      ║
║    application / counterpoint]                          ║
║   [[secondary.md]] — [type]                             ║
║                                                          ║
║ Fires these concepts:                                    ║
║   → [[related-1]]                                        ║
║   → [[related-2]]                                        ║
║                                                          ║
║ One-line collapse: [Feynman kill shot]                  ║
╚═══════════════════════════════════════════════════════════╝
```

If the concept exists, increment its "exists in N files" count and add the new file to its "Fires in" list.

### Step 6: Verify NO Duplication

Search the repo for the same insight in other files. If it already exists somewhere:

1. Choose the STRONGER location as primary (more specific, better context)
2. Note the weaker location in the registry as a secondary
3. Do NOT delete from the weaker location — just cross-link

### Step 7: Update MAP / Stats (if it's a new file)

If this assimilation created a NEW file (not just augmented an existing one):
1. Add the file to `MAP.md` in the appropriate kingdom/phase
2. Update the file count in `README.md` and `GROWTH_PROTOCOL.md` counters
3. Update `MAP_360.md` and `SYMBIOTIC_MAP.md` if the new file creates a new symbiotic relationship

### Step 8: Commit

```bash
git add -A
git commit -m "assimilated [concept] — [primary home] — [what changed] — YYYY-MM-DD"
git push
```

The git message format is fixed. Always: `assimilated [concept] — [home] — [change] — [date]`.

---

## THE NON-NEGOTIABLE RULES

1. **Never delete existing content.** The reef only grows. (Inherited from `GROWTH_PROTOCOL.md` Law 1.)
2. **Every concept has exactly one primary home.** Secondary homes link to it via the registry. The primary is where the concept is MOST useful — usually the most specific file.
3. **Every file ends with a `## Synaptic Connections` section.** This is absolute. If a file doesn't have one yet, it will get one in Batch 2 of execution.
4. **The registry is updated with every assimilation.** No orphan concepts. If a concept is in the repo, it's in the registry.
5. **The taxonomy decides.** Not intuition, not mood, not "this feels like it goes here." The taxonomy table above is the law. If in doubt, re-read the taxonomy.
6. **New information that doesn't fit the taxonomy goes to aman-os, not here.** This is the CASH ENGINE. Life OS is aman-os. Don't pollute the cash engine with non-trading content unless it directly affects a trading decision.
7. **Synaptic connections are bidirectional.** If file A links to file B, file B must link to file A. Always.
8. **The user proof-reads before commit.** This is the user's explicit request: "I will try to research, dissect, and proofread before always." The protocol proposes the homing; the user confirms before `git commit`.

---

## THE USER'S ROLE IN THE PROTOCOL

This protocol is the assistant's operating system, but the user is the final authority:

1. **Assistant proposes the homing** (which file, which section, which synaptic links)
2. **User reviews** — reads the proposed addition, challenges if needed
3. **User approves** → commit
4. **If user challenges** — re-home or restructure based on user's reasoning

The user has final say on placement. The protocol is the suggestion engine, not the decision maker.

---

## QUICK REFERENCE CARD (Print This)

```
INCOMING INFO
     ↓
Is it about trading/money/markets? ── NO ──▶ STOP (goes to aman-os, not here)
     ↓ YES
Which taxonomy row fits?
     ↓
Primary home identified
     ↓
Concept exists in registry? ── NO ──▶ Add registry entry (new neuron)
     ↓ YES
Open primary file → append new section/subsection (NEVER overwrite)
     ↓
Add bidirectional synaptic connection
     ↓
Update registry (increment file count)
     ↓
Check for duplication → cross-link, never delete
     ↓
If new file created → update MAP/README/GROWTH counters
     ↓
git commit: "assimilated [concept] — [home] — [change] — [date]"
     ↓
DONE. The reef grew by one cell.
```

---

## CONNECTIONS TO EXISTING ARCHITECTURE

| Existing File | Relationship to This Protocol |
|---------------|-------------------------------|
| `SYMBIOTIC_MAP.md` (378 lines, the reef) | This protocol is the ACTIVE mechanism that grows the reef. SYMBIOTIC_MAP describes the relationships; this protocol adds new organisms to them. |
| `GROWTH_PROTOCOL.md` (109 lines, study cycle) | GROWTH_PROTOCOL governs STUDY sessions. ASSIMILATION_PROTOCOL governs ALL OTHER inbound information (Arena, journal, trades, books, AI chats). They are siblings, both under the kernel. |
| `ARCHITECTURE/LINKS.md` | Defines what flows OUT to aman-os. This protocol defines what flows IN and where it homes within moneygod. |
| `ARCHITECTURE/RIPPLE_OUT.md` | Outward log. Updated when an assimilation triggers a ripple event (e.g., new lexicon term, new freedom number). |
| `systems/s00-concept-registry.md` (NEW) | The hippocampus. This protocol populates it. The registry IS the brain's memory structure — every concept, every connection, every quantum state. |
| `CURRICULUM.md` | Determines the current phase, which influences "fire-when" conditions for synaptic connections. |
| `plumbing-hierarchy-master.md` Part 11 (Lexicon) | The existing lexicon (25 terms) — these become registry entries. The lexicon and the registry are the same thing, viewed differently. |

---

## WHAT THIS PROTOCOL DOES NOT DO

- Does not replace `GROWTH_PROTOCOL.md` (study cycle) — extends it for all non-study information
- Does not replace `SYMBIOTIC_MAP.md` (reef architecture) — operationalizes it
- Does not delete or rewrite any existing file — appends only
- Does not decide for the user — proposes; user confirms
- Does not create new files unless no existing file fits the taxonomy — prefer augmentation
- Does not touch aman-os — that's a separate repo with its own protocol

---

## THE LIFECYCLE

```
Day 1: ASSIMILATION_PROTOCOL.md created. Taxonomy is law. Registry doesn't exist yet.
Day 2-7: Batch 1-4 execution creates 22 new files. Each gets synaptic connections. Concept registry built in parallel (~120 concepts across 94 files).
Day 8+: Every new Arena chat, every journal entry, every trade, every book recommended — runs through this protocol. The reef grows by one cell per assimilation. The brain fires one new synapse per connection.
Year 1+: The repo is no longer a collection of files. It is a brain. Every concept knows every related concept. Every file knows its neighbors. The curriculum becomes one of many entry points, not the only path.
Year 3+: The brain is denser than any human could memorize. It is queried, not read. A concept surfaces its connections; the connections surface theirs; the network is navigated by need, not by order.
```

---

*"A body doesn't think about where to send nutrients. The circulatory system knows. This protocol is the circulatory system. Information enters; it knows where to go."*

*git add -A && git commit -m "kernel — ASSIMILATION PROTOCOL — the operating system for all incoming information — 2026-07-29" && git push*
