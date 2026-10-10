# The Enterprise GenAI Stack: the view at end of Q3 2026 (package README)

![Veyan](08_Graphic/veyan_lockup.png)

| | |
|---|---|
| **As of** | 9 October 2026 |
| **Status** | Checkpoint 5: final package, signed off; rebuilt with the house conventions and a print edition |
| **Scope** | A new baseline for the enterprise GenAI stack as it stands at the end of Q3 2026, built from this review's own research: 140 product records across nine layers and eight cross-cutting enterprise controls, assessed for a regulated UK/EU asset manager, with six further views |
| **Method** | Plan v4.3, §13. Stage 0 scoping → Stage A research (8 streams) → Stage A′ adversarial verification (2 verifiers) → Stage B writing (17 chapters, three calibration reviews) → Stage C synthesis (with an independent reviewer) → Stage C2 LinkedIn series → Stage D package |
| **Disclosure** | The author is an Anthropic model. Anthropic products and standards (Claude, the Claude Agent SDK, MCP and Agent Skills) are scored on the same rubric as everything else, and an independent alternative is always named. Tiers the reader set at checkpoints are marked as the reader's decision. |
| **Not advice** | Personal research. It does not describe any firm's actual platform or vendor choices. Re-verify any fact before you rely on it. |

## Contents (plan §14 layout)

| Folder | File | What it is |
|---|---|---|
| `01_Report/` | `Master_Architecture.docx` / `.md` | The master document: disclosure and final tiers, Part I executive summary, Part II method, the nine layer chapters (**L1 → L9**), the eight control chapters (C1–C8), Parts III–XII (hypotheses, reference architecture, FS view, worked example, four reference stacks, build vs buy, lock-in, 18-month roadmap, final stack, and the new baseline at a glance), Parts XIII–XVIII (the six further views: technology service provider, software product company, start-up, and AI-tools, agentic-SDLC and agent-provider vendor start-ups), and an annex pointing to the companion files. Every flow is a figure, and each LinkedIn post visual sits in the chapter it illustrates. Word shows claim labels as small footnotes; the `.md` keeps the inline tags. |
| `01_Report/Print/` | `Interior.docx`, `Cover_Paperback.pdf`, `Cover_Front.jpg`, `Ebook.epub`, `Publishing_Kit.md`, `Build_Summary.md` | **The book edition**, ready for Amazon KDP or any print-on-demand service: 8.5 × 11 in interior with mirrored margins, Parts opening on right-hand pages, running heads, a copyright page and contents; a full-wrap cover sized from the page count; a Kindle EPUB; and the publishing checklist, with the store listing and KDP checks. |
| `02_Appendix/` | `Product_Technical_Appendix.docx` / `.md` | One entry per product record: tier, scorecard (generic and FS weights), fit by view (score and core/situational fit in all seven views), assessment, and every fact cell with its label and source IDs; a "Seven views" section explains the weights |
| `03_Slides/` | `Executive_Deck.pptx` / `.pdf` | 38-slide executive deck, including a "Seven lenses" section (one slide per view and what holds across all seven) |
| `04_Explorer/` | `explorer.html` | Offline, single-file explorer: choose one of the seven views (scores, ranks and core candidates re-weighted), filter and compare products, read the view Parts in the "Seven views" tab, and read the worked example, hypotheses, reference stacks and final stack. Open it in any browser; it needs no network. |
| `05_Data/` | `products.json` / `.xlsx`, `regulatory_facts.json`, `views.json` / `.xlsx` | The dataset: 140 records (138 scored), fact cells with label, confidence and sources; 27 regulatory and standards records; the re-weighted scores for the six further views |
| `06_References/` | `bibliography.xlsx`, `snapshots/<stream>/`, `originals/` | 1,449 sources plus a claim → source map; text snapshots and dated search extracts |
| `08_Graphic/` | `Enterprise_GenAI_Stack_Oct2026.png` / `.pdf` (stack poster), `Architecture_One_Page.png` / `.pdf`, `diagrams/*.png`, each with an editable source (`.md` or `.html`) | The stack poster: control plane, then layers **L1 → L9**, one tile per assessed product (138) coloured by final tier. The one-page architecture. Every flow and decision tree in the report, as a Mermaid diagram. `linkedin/P00–P24`: the visual for each LinkedIn post (1080 × 1350 PNG, PDF and HTML, editable `.md`; render with `node tools/render_post_visuals.js`). **To edit:** change the `.md` or `.html` source, then run `python3 -I tools/build_stack_graphic.py .` (poster) and/or `NODE_PATH=$(npm root -g) node tools/render_graphic.js <html> <basename>` (poster, architecture) or `NODE_PATH=$(npm root -g) node tools/render_diagrams.js` (diagrams). |
| `07_LinkedIn/` | `Content_Calendar.xlsx`, `LinkedIn_Series.docx` | The only home of the LinkedIn series: an introduction post (Post 0) and 32 posts over 17 weeks (Posts 25–32: "One stack, seven lenses"), each with its visual, plus 3 reactive templates. `Book/` holds the series as a book (Interior.docx, cover, EPUB; Part IV covers the views). Enter the date of Post 1 in cell E1 and suggested dates fill in (no weekday is fixed; edit any date). Post 0 goes out a few days before. |

## Headline numbers

- **140** product records, **138** scored: **58 Strategic, 67 Tactical, 13 Experimental**. Most Strategic tiers are conditional, and the condition is the decision.
- **1,449** sources, **4,620** fact cells. **1,557** cells are *Not publicly verified* and were never guessed.
- **A new baseline.** This edition sets the baseline for the enterprise GenAI stack at the end of Q3 2026. Each quarterly edition is compared with the previous one, tier by tier and record by record (`tools/diff_tiers.py`).

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
- Everything is as of the end of Q3 2026 (evidence dated up to 9 October 2026). The LinkedIn posts each list what to re-verify before posting.
- To fill the gaps from a machine with open internet access, follow `RERUN_ON_DESKTOP.md` in the GitHub repository (branch `claude/nice-meitner-0me752`).

## Rebuilding

Every file in this package is generated from the sources in the repository. To rebuild all of it after an edit or a quarterly refresh, run `bash tools/rebuild_all.sh` from the repository root (see `RERUN_ON_DESKTOP.md` and `REFRESH_QUARTERLY.md`).
