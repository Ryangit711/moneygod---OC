# GROWTH PROTOCOL — The Living System

**This repo is not a static document. It is a living organism that grows with every study session.**

You study → you learn → you write → you push → the system evolves. The git history is not a changelog — it is the fossil record of your mind expanding.

---

## THE CYCLE

```
STUDY ──▶ ENCOUNTER FUZZY TERM ──▶ FEYNMAN BREAKDOWN ──▶ ADD TO LEXICON
  │                                                                   │
  └──────────────────────▶ PUSH ◀─── UPDATE CROSS-REF ◀─── UPDATE MAP ◀┘
```

### Step 1: Study
Read any file in the repo. Take notes. Find gaps in your understanding.

### Step 2: Identify fuzzy terms
Any concept you can't explain to a 12-year-old → it goes into Part 11.

### Step 3: Write Feynman breakdown
Open `plumbing-hierarchy-master.md`, scroll to Part 11, add:
```
### 11.XX [Term Name]
```
Follow the existing format: simple language, real mechanism, no jargon hiding.

### Step 4: Update MAP.md
Find the Part 11 cross-reference table in MAP.md. Add your new term with:
- Term number and name
- Primary source file (where in the repo this concept is taught)
- One-line "What It Unlocks"

### Step 5: Update GROWTH_PROTOCOL.md stats
Increment the counters below.

### Step 6: Push
```
git add -A && git commit -m "GROWTH — [n] new terms: [term list] — YYYY-MM-DD" && git push
```

---

## GROWTH COUNTERS (Update After Every Session)

| Metric | Count | Date of Last Addition |
|--------|:-----:|:---------------------:|
| Total files | 41 | 2026-07-12 |
| Total lines | ~11,400 | 2026-07-12 |
| Part 11 terms | 25 | 2026-07-11 |
| Plumbing-esoterica lines | 646 | 2026-07-07 |
| Sessions on record | 1 | 2026-07-07 |

---

## WHAT CAN GROW

| Component | How It Grows | Limit |
|-----------|-------------|-------|
| **Part 11 Lexicon** | New Feynman term after every study session | None — the more terms, the sharper the system |
| **plumbing-esoterica.md** | Deeper dives into esoteric plumbing layers | Add sections as you uncover them |
| **MAP.md cross-reference** | Every new term gets cross-referenced to source file | Auto-updates with each term |
| **core/ files** | New plumbing layers discovered during study | Add files as needed |
| **trading/ strategies** | Backtested edges that work in live market | Quality over quantity |
| **references/** | New books, papers, tools found | Keep adding to the list |
| **conversations/** | Session records — what you thought, what you learned | One per major study session |

---

## THE THREE LAWS OF GROWTH

1. **Never delete.** Only add. If something is superseded, archive it with a reference. The system only grows.
2. **Never waste a fuzzy term.** Every word you can't explain from first principles is a key to a locked door. Break it down, add it to Part 11, unlock the door.
3. **Push after every session.** The git history IS your learning journey. Every commit is a timestamp of understanding gained. The repo and you grow together — symbiotically, semantically.

---

## STARTING A STUDY SESSION

```
Before reading anything:
  1. git pull
  2. Open GROWTH_PROTOCOL.md → note the current counters
  3. Open MAP.md → orient yourself in the file system
  4. Read → encounter → break down → add → push
```

## ENDING A STUDY SESSION

```
Before walking away:
  1. Update GROWTH_PROTOCOL counters
  2. git add -A && git commit -m "GROWTH — [description]" && git push
  3. If you added terms, verify MAP.md cross-reference is updated
```

---

*This file itself grows. If you find a better way to grow, add it here. Never replace.*
