# CP5: final package, for your review and sign-off

| | |
|---|---|
| **Date** | 9 October 2026 |
| **Status** | All stages complete (0 → A → A′ → B → C → C2 → D). Waiting for your sign-off. |
| **Branch** | `claude/nice-meitner-0me752` on `github.com/gitzerobegin/genai_stack` |
| **ZIP** | `Enterprise_GenAI_Stack_Oct2026/Enterprise_GenAI_Stack_Oct2026.zip` (CP5-4 follow-up: committed in the package folder on the working branch, because a GitHub Release could not be created from this session) |
| **Claude Doc** | Executive summary and synthesis (CP5-2): https://claude.ai/code/artifact/74918687-c7fb-43e9-86fb-c729062bf9c6 |

## What was delivered (plan §14)

| Deliverable | File | Notes |
|---|---|---|
| Master document | `01_Report/Master_Architecture.docx`, `.pdf`, `.md` | Disclosure and final tiers → Part I executive summary → Part II method → 9 layer chapters → 8 control chapters → Parts III–XI → LinkedIn series → Annexes A–B. Claim labels shown as small footnotes in Word/PDF (CP5-1); inline tags in the `.md`. |
| Product appendix | `02_Appendix/Product_Technical_Appendix.*` | One entry per record: tier, scorecard, assessment, every fact cell with label and sources |
| Executive deck | `03_Slides/Executive_Deck.pptx`, `.pdf` | 28 slides; validated and visually checked |
| Explorer | `04_Explorer/explorer.html` | Offline single file (CP5-3): products, compare, worked example, hypotheses, reference stacks, final stack |
| Dataset | `05_Data/products.json`/`.xlsx`, `regulatory_facts.json`, `what_changed.xlsx` | 140 records (138 scored), 4,620 fact cells, 20 regulatory facts |
| Sources | `06_References/bibliography.xlsx`, `snapshots/`, `originals/` | 1,255 sources; `originals/` is empty in this run (see below) |
| LinkedIn | `07_LinkedIn/Content_Calendar.xlsx`, `LinkedIn_Series.docx` | 24 posts, 12 weeks, 3 reactive templates. Enter the date of Post 1 (any weekday; user decision 10 October 2026) in cell E1. No clearance column needed (CP4b). |

**Final tiers:** 58 Strategic, 67 Tactical, 13 Experimental, 2 unscored (EthicalAgents and Ragoos, unverifiable).

## Quality checks run

- Tag check on the synthesis and all 17 sections: 0 unknown source IDs, 0 long untagged paragraphs, no banned words.
- Dataset integrity: 0 issues.
- Synthesis reviewed by an independent reviewer: 45 edits (`work/stageC/synthesis_review.md`), covering consistency, accuracy of 45 sampled claims and all regulatory statements, conflict-of-interest attribution and readability.
- Deck: `validate.py` passed; rendered and inspected slide by slide.

## What could not be verified

- **1,557 of 4,620 fact cells are "Not publicly verified".** Mostly start-up certifications, EU regions, SSO/RBAC and pricing. Never guessed; scores capped under the rubric.
- **798 sources are search-tool extracts**, not page snapshots, because the research environment's egress policy blocked most hosts. They carry `conf: medium`. No PDF originals were saved.
- **No audit report was read directly.** All SOC 2 / ISO statements come from vendor pages or trust centres.
- **Hyperscaler model services** (Bedrock, Microsoft Foundry, Gemini Enterprise Agent Platform) are treated as access patterns, not scored records.
- **Not yet profiled:** Azure AI Search, Vertex AI Vector Search, Bedrock embeddings and rerank, ServiceNow AI Control Tower, OneTrust, Daytona, Modal.
- **Open date conflicts:** GPT-6 Astra GA status; GLM-5.3 release date; Guardrails AI cutoff; OWASP LLM 2026 publication month. The full OWASP LLM 2026 list was not retrieved.

## Decision at CP5

**XI.5 avoid list (user, 9 October 2026): move to "monitor".** The two rows that sat outside the four CP4-7 grounds (Chinese-origin vendors' own hosted APIs for client data; billing intermediation through a gateway or router) moved from XI.5 to the XI.6 monitor list. No tier changed. The I.4 route rule (never a Chinese-origin vendor's own API for client data) stays as a recommendation. Applied to the synthesis, the Claude Doc, the master document, the explorer, deck slide 16 and the ZIP.

## How to close the gaps

Follow `RERUN_ON_DESKTOP.md` on a machine with open internet: re-fetch the blocked sources (`tools/refetch_sources.py`), run the NPV gap report and the G1/G2 gap-fill prompts, re-score the affected layers, then rebuild with the commands in `MEMORY.md`.
