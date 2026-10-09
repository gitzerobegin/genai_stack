# Stage E brief: further views (technology service provider, software product company, start-up)

**Added:** 9 October 2026, at the user's request. The review was written for a regulated asset manager (the FS view). Stage E adds three further views of the same stack:

| Code | View | Who it is for |
|---|---|---|
| FS | Regulated financial services | The master view (Parts I–XII) |
| TS | Technology service provider | Runs GenAI inside services it operates for its customers (multi-tenant SaaS, managed or hosted services) |
| SW | Software product company | Ships software with GenAI built in, deployed by its customers (self-managed, on-premises, air-gapped, marketplace) |
| SU | Start-up | Early-stage company building an AI-native product with a small team |

## Inputs

- **Evidence.** The same dataset (`05_Data/products.json`) plus the Stage E research:
  - `work/stageE/E1_regulation/`: CRA, PLD, NIS2, Data Act, AI Act roles, US state laws; source IDs `E1-S###`; records merged into `regulatory_facts.json`.
  - `work/stageE/E2_commercial/`: model licences for redistribution, API terms, cost levers, start-up programmes, assurance frameworks, multi-tenant guidance; source IDs `E2-S###`.
- **Scoring.** `work/stageE/views/views.json` holds the weights per view. They are architectural judgement and sum to 100.
  - `tools/build_views.py` re-weights the Stage B criterion scores. It never changes a fact or a score.
  - It writes `05_Data/views.xlsx`, `views.json` and `work/stageE/views/<VIEW>_scores.md`.
  - The per-view fit is "Core candidate" or "Situational". It is computed and indicative; the master tiers and their conditions still stand.
- **Synthesis.** `work/stageC/synthesis.md` (the FS view) is the baseline each view departs from.

## Output per view: `work/stageE/views/<VIEW>/view.md`

One Part of the master document: TS = Part XIII, SW = Part XIV, SU = Part XV. Use H1 for the Part title and H2 for numbered sections:

1. **Who this view is for**: profile, assumptions, and the five biggest differences from the FS view (a table)
2. **Findings that change for this view**: 6–10 findings, each tied to evidence
3. **Scoring for this view**: the weights against FS, what moves and why (from `<VIEW>_scores.md`), core-candidate count, and where to find the full table (`05_Data/views.xlsx`)
4. **The architecture for this view**: one Mermaid figure. Its source goes in `Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/<VIEW>-1.md`, rendered with `node tools/render_diagrams.js`; the image line and caption follow the chapter convention
5. **Layer by layer, then control by control**: one table, rows L1 → L9 then C1 → C8. Columns: default choice for this view, change from the FS view, why
6. **Regulation, contracts and customer assurance** for this view
7. **Reference stack**: cloud-neutral, plus AWS / Azure / Google Cloud columns where they differ
8. **Build vs buy, and lock-in**
9. **Roadmap**: phases, sized to the organisation
10. **Worked example**, from `views.json`: a trace table (step · what happens · components), boundaries (may / must never), and the evidence kept
11. **Checklist, what to avoid, what to monitor**

## Rules (as for every stage)

- Never use training memory as a fact source. Cite the dataset's source IDs or the E1/E2 IDs.
- Label every claim: `[VF: …]`, `[R: …]`, `[AJ]`, `[Rec]`, `[NPV]`.
- Write in British spelling, with no ASCII diagrams, and order layers L1 → L9 then C1 → C8.
- **Conflict of interest.** The author is an Anthropic model. Name an independent alternative beside every Anthropic product or standard recommended.
- Present each view as "the view at end of Q3 2026". Diagram-relative content (the popular stack diagram) does not belong here.
- 5,000–7,000 words per view. Check with `python3 -I tools/check_tags.py . <file>`: there must be no unknown source IDs and no long untagged paragraphs.

## Refresh

Each quarterly refresh re-runs `tools/build_views.py` after re-scoring (R3) and updates the three view Parts in R4 (`work/prompts/refresh_prompts.md`, R4b). E1 and E2 facts are re-verified in R0 and R1: the start-up credits and the US state-law dates are the most volatile.
