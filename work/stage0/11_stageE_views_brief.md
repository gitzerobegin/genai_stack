# Stage E brief: further views (TS, SW, SU, AT, DV, AG)

**Added:** 9 October 2026, at the user's requests. The review was written for a regulated asset manager (the FS view). Stage E adds six further views of the same stack. Three are **adopter** views (organisations using GenAI in what they sell); three are **vendor** views (start-ups whose product must fit into an enterprise's GenAI stack):

| Code | View | Who it is for |
|---|---|---|
| FS | Regulated financial services | The master view (Parts I–XII) |
| TS | Technology service provider | Runs GenAI inside services it operates for its customers (multi-tenant SaaS, managed or hosted services) |
| SW | Software product company | Ships software with GenAI built in, deployed by its customers (self-managed, on-premises, air-gapped, marketplace) |
| SU | Start-up | Early-stage company building an AI-native product with a small team |
| AT | AI-tools start-up (vendor) | Sells a component of the Enterprise GenAI Stack (gateway, guardrail, privacy, evaluation, retrieval, ingestion, memory or governance tool) to enterprises |
| DV | Agentic-SDLC start-up (vendor) | Sells coding agents, AI code review, test generation or migration agents to enterprise engineering teams |
| AG | Agent-provider start-up (vendor) | Sells agents that do work inside customers' businesses and must run under the customer's identity, policy and evidence |

## Inputs

- **Evidence.** The same dataset (`05_Data/products.json`) plus the Stage E research:
  - `work/stageE/E1_regulation/`: CRA, PLD, NIS2, Data Act, AI Act roles, US state laws; source IDs `E1-S###`; records merged into `regulatory_facts.json`.
  - `work/stageE/E2_commercial/`: model licences for redistribution, API terms, cost levers, start-up programmes, assurance frameworks, multi-tenant guidance, marketplaces and agent distribution; source IDs `E2-S###`.
  - `work/stageE/E3_agents_sdlc/`: the agentic SDLC landscape (coding agents, as product records in `products.json`, layer "DV", unscored), secure-development guidance for AI-generated code, and agent identity / interoperability / telemetry standards; source IDs `E3-S###`.
- **Scoring.** `work/stageE/views/views.json` holds the weights per view. They are architectural judgement and sum to 100.
  - `tools/build_views.py` re-weights the Stage B criterion scores. It never changes a fact or a score.
  - It writes `05_Data/views.xlsx`, `views.json` and `work/stageE/views/<VIEW>_scores.md`.
  - The per-view fit is "Core candidate" or "Situational". It is computed and indicative; the master tiers and their conditions still stand.
- **Synthesis.** `work/stageC/synthesis.md` (the FS view) is the baseline each view departs from.

## Output per view: `work/stageE/views/<VIEW>/view.md`

One Part of the master document: TS = Part XIII, SW = Part XIV, SU = Part XV, AT = Part XVI, DV = Part XVII, AG = Part XVIII. Use H1 for the Part title and H2 for numbered sections:

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

### Vendor views (AT, DV, AG): the same eleven sections, with these changes

- **Section 3 (scoring)** scores the components the start-up builds its own product on.
- **Section 5** becomes "**Where the product sits and how it fits into the Enterprise GenAI Stack**". Map the product to its layer or control, then set out the integration contract the buyer's stack expects. Use one table, L1 → L9 then C1 → C8, showing the interface for each layer. Examples:
  - OpenAI-compatible or gateway-routed model calls (C1);
  - SSO/SCIM and the customer's agent identity and delegation (C4);
  - OpenTelemetry GenAI spans to the customer's collector (L9);
  - calls to the customer's privacy service (C3);
  - MCP/A2A behind the customer's tool gateway (L4);
  - evidence records to the customer's store (C8);
  - configuration as code (C5);
  - cost metering per tenant (C6).
- **Section 6** becomes "**What enterprise buyers will ask, and how to pass**". Use the FS view as the toughest buyer: due diligence, DORA/outsourcing flow-down, AI Act and CRA duties as a vendor, certifications and their sequencing, BYOC and residency, IP and data terms, exit and escrow.
- **Section 7** becomes "**The start-up's own reference stack**": what to build the product on, cloud-neutral plus per-cloud.
- **Section 8** adds "**Where incumbents are and where they are moving**". Draw on the dataset's ownership events: neutral tools are being acquired (synthesis Part I finding 2). Cover the positioning and exit implications.
- The worked example (section 10) is traced as the **customer** runs it, inside the customer's stack.

## Rules (as for every stage)

- Never use training memory as a fact source. Cite the dataset's source IDs or the E1/E2 IDs.
- Label every claim: `[VF: …]`, `[R: …]`, `[AJ]`, `[Rec]`, `[NPV]`.
- Write in British spelling, with no ASCII diagrams, and order layers L1 → L9 then C1 → C8.
- **Conflict of interest.** The author is an Anthropic model. Name an independent alternative beside every Anthropic product or standard recommended.
- Present each view as "the view at end of Q3 2026". Diagram-relative content (the popular stack diagram) does not belong here.
- 5,000–7,000 words per view. Check with `python3 -I tools/check_tags.py . <file>`: there must be no unknown source IDs and no long untagged paragraphs.

## Refresh

Each quarterly refresh re-runs `tools/build_views.py` after re-scoring (R3) and updates the three view Parts in R4 (`work/prompts/refresh_prompts.md`, R4b). E1 and E2 facts are re-verified in R0 and R1: the start-up credits and the US state-law dates are the most volatile.
