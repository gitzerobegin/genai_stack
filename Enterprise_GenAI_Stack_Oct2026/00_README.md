# Enterprise GenAI Stack: October 2026 (package README)

| | |
|---|---|
| **As of** | 9 October 2026 |
| **Status** | Checkpoint 5: final package, for the reader's review and sign-off |
| **Scope** | The "Full AI Stack Explained" graphic (9 layers, 80 tools), brought up to date and extended to 140 product records and 8 cross-cutting enterprise controls, assessed for a regulated UK/EU asset manager |
| **Method** | Plan v4.3, §13. Stage 0 baseline → Stage A research (8 streams) → Stage A′ adversarial verification (2 verifiers) → Stage B writing (17 chapters, three calibration reviews) → Stage C synthesis (with an independent reviewer) → Stage C2 LinkedIn series → Stage D package |
| **Disclosure** | The author is an Anthropic model. Anthropic products and standards (Claude, the Claude Agent SDK, MCP and Agent Skills) are scored on the same rubric as everything else, and an independent alternative is always named. Tiers the reader set at checkpoints are marked as the reader's decision. |
| **Not advice** | Personal research. It does not describe any firm's actual platform or vendor choices. Re-verify any fact before you rely on it. |

## Contents (plan §14 layout)

| Folder | File | What it is |
|---|---|---|
| `01_Report/` | `Master_Architecture.docx` / `.pdf` / `.md` | The master document: disclosure and final tiers, Part I executive summary, Part II method, the nine layer chapters (9 → 1), the eight control chapters (C1–C8), Parts III–XI (hypotheses, reference architecture, FS view, worked example, four reference stacks, build vs buy, lock-in, 18-month roadmap, final stack), the LinkedIn series, and Annexes A and B. Word and PDF show claim labels as small footnotes; the `.md` keeps the inline tags. |
| `02_Appendix/` | `Product_Technical_Appendix.docx` / `.pdf` / `.md` | One entry per product record: tier, scorecard (generic and FS weights), assessment, and every fact cell with its label and source IDs |
| `03_Slides/` | `Executive_Deck.pptx` / `.pdf` | 28-slide executive deck |
| `04_Explorer/` | `explorer.html` | Offline, single-file explorer: filter and compare products, and read the worked example, hypotheses, reference stacks and final stack. Open it in any browser; it needs no network. |
| `05_Data/` | `products.json` / `.xlsx`, `regulatory_facts.json`, `what_changed.xlsx` | The dataset: 140 records (138 scored), fact cells with label, confidence and sources; 20 regulatory facts |
| `06_References/` | `bibliography.xlsx`, `snapshots/<stream>/`, `originals/` | 1,255 sources plus a claim → source map; text snapshots and dated search extracts |
| `07_LinkedIn/` | `Content_Calendar.xlsx`, `LinkedIn_Series.docx` | 24 posts over 12 weeks, plus 3 reactive templates. Enter the start Tuesday in cell E1 and every date fills in. |

## Headline numbers

- **140** product records, **138** scored: **58 Strategic, 67 Tactical, 13 Experimental**. Most Strategic tiers are conditional, and the condition is the decision.
- **1,255** sources, **4,620** fact cells. **1,557** cells are *Not publicly verified* and were never guessed.

## Confidence legend

| Label | Tag | Meaning |
|---|---|---|
| **Verified fact** | `[VF: id]` | From a primary source: vendor docs, announcement, trust centre or regulator |
| **Reported** | `[R: id]` | From a secondary source |
| **Architectural judgement** | `[AJ]` | The author's reasoning |
| **Recommendation** | `[Rec]` | The author's advice |
| **Not publicly verified** | `[NPV]` | No source could confirm it; never guessed |

**Confidence (`conf`):**
- **high:** primary, current and unambiguous
- **medium:** primary but read through a search extract or undated, or several consistent secondary sources
- **low:** a single secondary or aggregator source

Source IDs resolve in `06_References/bibliography.xlsx` (sources) and `05_Data/regulatory_facts.json` (regulation).

## Archive file types

| File | What it is |
|---|---|
| `*.txt` | Text snapshot of a page fetched directly |
| `*.extract.txt` | A dated record of what the web-search tool returned for a page whose host the research environment's egress policy blocked. It is **not** a copy of the page; the URL remains the citation. |
| `link-only` | Paywalled, blocked or failed; cited by link only and never worked around |

## Known limits

- Many primary sources (trust centres, regulators) could be read only through search extracts. Those cells carry `conf: medium`.
- Certification scope, pricing and residency details are often not public. Where a vendor did not publish them, the cell says *Not publicly verified*, and scores are capped under the rubric's evidence rules.
- Everything is as of October 2026. The LinkedIn posts each list what to re-verify before posting.
- To fill the gaps from a machine with open internet access, follow `RERUN_ON_DESKTOP.md` in the GitHub repository (branch `claude/nice-meitner-0me752`).
