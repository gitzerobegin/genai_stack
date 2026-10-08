# Enterprise GenAI Stack: October 2026 (package README)

| | |
|---|---|
| **As of** | 8 October 2026 |
| **Status** | Checkpoint 1: research baseline only. Report, appendix, slides, explorer and LinkedIn folders are filled in at later stages. |
| **Method** | Plan v4.3, §13: Stage 0 baseline → Stage A research (8 streams) → Stage A′ adversarial verification (2 verifiers) → B write → C synthesise → C2 LinkedIn → D package |
| **Disclosure** | The author is an Anthropic model. Anthropic products and standards (Claude, Claude Agent SDK, MCP, Agent Skills) are scored on the same rubric as everything else, with independent alternatives named. |

## Contents (plan §14 layout)

| Folder | Content | Status at CP1 |
|---|---|---|
| `01_Report/` | Master architecture document (.docx, .pdf) | Stage B–D |
| `02_Appendix/` | Product technical appendix | Stage B–D |
| `03_Slides/` | Executive deck | Stage D |
| `04_Explorer/` | Interactive explorer | Stage D |
| `05_Data/` | `products.json` / `.xlsx` (140 products, fact cells with label, confidence and sources), `regulatory_facts.json`, `what_changed.xlsx` | **Done (facts; scores in Stage B)** |
| `06_References/` | `bibliography.xlsx` (1,119 sources plus a claim→source map), `snapshots/<stream>/`, `originals/` | **Done** |
| `07_LinkedIn/` | Series and content calendar | Stage C2 |

## Confidence legend

| Label | Meaning |
|---|---|
| **Verified fact** | From a primary source: vendor docs, announcement, trust centre or regulator |
| **Reported** | From a secondary source |
| **Architectural judgement** | Author's reasoning |
| **Recommendation** | Author's advice |
| **Not publicly verified** | No source could confirm it; never guessed |

**`conf`:**
- **high:** primary, current and unambiguous
- **medium:** primary but read via a search extract, or undated; or several consistent secondary sources
- **low:** single secondary or aggregator source

## Archive file types

| File | What it is |
|---|---|
| `*.txt` | Text snapshot of a page fetched directly |
| `*.extract.txt` | Dated record of what the web-search tool returned for a page whose host was blocked by the research environment's egress policy. This is **not** a copy of the page; the URL remains the citation. |
| `link-only` | Paywalled, blocked or failed; cited by link only and never worked around |
