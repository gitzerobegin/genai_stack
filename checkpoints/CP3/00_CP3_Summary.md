# Checkpoint 3: layers 6–4 and controls C1–C8

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Status** | Stopped for review. Next: layers 3–1 and Stage C synthesis, then CP4. |

## 1. What is done

| Item | Detail |
|---|---|
| **New drafts** | §6 Retrieval and knowledge stores · §5 Memory · §4 Tools, protocols and connectivity · C1 AI gateway · C2 Guardrails · C3 DLP/PII · C4 Identity and access for agents · C5 Prompt and configuration management · C6 AI FinOps · C7 AI security · C8 Model risk, governance and auditability.<br>Each has all 13 parts, the CP2 deep-dive format, POV 2 and 3, and the worked-example slice. About **94,600 words**. |
| **Layers 9–7 reworked** | Re-scored under your CP2 rules (14 score changes, no tier changes). Layers 8 and 7 now use the L9 deep-dive format. About 23,600 words. |
| **Scoring** | **104 products scored.** Tiers: **29 Strategic**, 67 Tactical, 8 Experimental. EthicalAgents and Ragoos are not scored. |
| **Calibration review** | Two reviewers covered all 11 new sections:<br>• 16 score changes<br>• **3 tier changes**, all Strategic → Tactical: L4 AgentCore Gateway + Identity, C4 MCP authorisation, C4 Cedar<br>• 181 claims spot-checked: no fact found wrong; 17 wording and label fixes<br>• 11 new sources<br>The tag checker reports 0 unresolved source IDs and 0 unlabelled paragraphs in every section. |
| **Conflict of interest** | Disclosures are present for MCP, Agent Skills and the MCP authorisation profile (all Anthropic-originated), and for turbopuffer (it names Anthropic as a customer). Three borderline scores were resolved **against** the Anthropic-related item:<br>• MCP security 3 → 2<br>• turbopuffer cost 4 → 3<br>• MCP authorisation: Strategic → Tactical |
| **Dataset** | 140 products, 1,234 sources, 0 integrity issues |

### Files for your review (in `checkpoints/CP3/`)

| File | Content |
|---|---|
| `01_Draft_Layers_6-4_Controls_C1-C8.md` / `.docx` | The new drafts |
| `05_Draft_Layers_9-7_reworked.md` / `.docx` | Layers 9–7 after the CP2 rework |
| `02_Review_A_L6-L4_C1-C2.md`, `03_Review_B_C3-C8.md` | Change logs and evidence |
| `04_All_Scores.md` | Every score table, L9 → C8 |

## 2. The Strategic picks so far (FS total)

| Area | Strategic |
|---|---|
| L9 Evals and observability | MLflow 4.25 · Langfuse 3.85 · LangSmith 3.80 (only with LangGraph) |
| L8 Ingestion | Docling 4.05 · Unstructured 3.85 |
| L7 Embeddings and reranking | Sentence Transformers 3.70 |
| L6 Retrieval stores | Milvus/Zilliz 4.25 · Elasticsearch 4.25 · pgvector 4.20 · Qdrant 3.85 · MongoDB 3.65 (only where MongoDB is already operated) |
| L5 Memory | none |
| L4 Tools and protocols | MCP 3.55 (conditional: gateway, mandatory authorisation, allow-list) |
| C1 Gateway | LiteLLM 3.90 (hardened, pinned, Enterprise) · Kong 3.80 · Apigee 3.65 (both only where they are already the API standard) |
| C2 Guardrails | none: the strategic asset is the firm's own policy and test sets |
| C3 DLP/PII | Presidio 3.65 · Google SDP 3.60 (Google estates) |
| C4 Agent identity | OPA 4.20 · SPIFFE/SPIRE 4.05 · Okta/Auth0 3.55 · Entra Agent ID 3.50 (both directory-bound) |
| C5 Prompt/config | LangSmith prompts 3.95 · Langfuse prompts 3.85 · prompts-as-code 3.65 |
| C6 FinOps | FOCUS 3.85 · gateway-native cost attribution 3.70 |
| C7 AI security | Vault 3.65 (conditional) · model/package scanning 3.60 |
| C8 Governance | OpenLineage 3.85. Every commercial governance tool is Tactical because product-scoped certifications could not be verified. |

### Patterns across the whole stack [AJ]

- **Self-hostable, open or foundation-governed components take most Strategic slots.** This is the effect of the FS weights: deployment 15% and lock-in 15%.
- **Hyperscaler-native services are Tactical:** "default in that estate".
- **Memory (L5) has no Strategic product.** This fits the plan's build order, where memory comes last.
- **Commercial governance tools (C8) are all held at Tactical by unverified certifications.** No audit report has been read for any product: MEMORY blocker B4.

## 3. Calibration questions, with options

The detail and evidence are in reviews A §(e) and B §(d). Option (a) is the current state.

**Q1: MCP, its authorisation profile, and A2A.** L4 MCP is Strategic (conditional, FS 3.55), the C4 MCP authorisation profile is Tactical (3.45), and A2A is Tactical (3.70). The protocol and its authorisation profile are tiered differently today.
- **(a)** Keep as now: the protocol is Strategic (conditional); its authorisation profile is Tactical but mandatory wherever MCP is used.
- **(b)** Make both Tactical. The strategic element is the firm's tool gateway plus identity (C1 and C4), and no Anthropic-originated item outranks a higher-scoring peer.
- **(c)** Make both Strategic, conditional (treated as one decision), and make A2A Strategic where cross-team or cross-vendor delegation is in scope.

**Q2: Hyperscaler-native services** (Bedrock Guardrails, AgentCore Gateway and Memory, Vertex Memory Bank, S3 Vectors, Azure Content Safety)
- **(a)** Tactical, "default in that estate". Security 4 where certifications name the parent service.
- **(b)** Strategic, conditional "where X is the primary cloud", for the lead service in each category.
- **(c)** Stricter: security 3 where certifications do not name the feature; tiers unchanged.

**Q3: Evidence needed for an enterprise-readiness score of 4**
- **(a)** Any primary vendor page counts. This is how Mem0, Zep, Portkey and Kong reached 4.
- **(b)** The extra control (SCIM, an SLA or an admin API) must come from product documentation or a trust centre, not pricing or marketing pages.
- **(c)** Revert to the writers' stricter reading: one control scores 2.

**Q4: Products with incidents or no certification**
- **(a)** As now:
  - LiteLLM: Strategic, conditional, despite the remediated March 2026 PyPI compromise.
  - Composio: Experimental.
  - Cognee: Tactical, self-host only.
- **(b)** Stricter:
  - LiteLLM: Tactical until 12 months pass without an incident.
  - Composio: flagged "Not recommended".
  - Cognee: Experimental.
- **(c)** Mixed: keep LiteLLM and Cognee as now; flag Composio "Not recommended" for client data, after its May 2026 token-exposure incident.

**Q5: Can a criterion at 2 sit under a Strategic call?** This affects Elastic, MongoDB, Kong, Apigee and LangSmith.
- **(a)** Yes, but only when the condition is an existing platform commitment. Pinecone stays Tactical.
- **(b)** Score-led: Pinecone becomes Strategic, conditional on a tested exit route.
- **(c)** No. Strategic means no criterion below 3; those products become Tactical, "default where already operated".

**Q6: Entra Agent ID (3.50) and Okta/Auth0 (3.55), Strategic below the 3.6 guide**
- **(a)** Keep both as Strategic, conditional: the agent identity must live in the directory that already holds the humans it acts for.
- **(b)** Make both Tactical, and make "agent identities in the workforce IdP" the Strategic pattern.
- **(c)** Split them. Not recommended: they differ by only 0.05 FS.

**Q7: How patterns and standards are tiered against products** (prompts-as-code, gateway cost attribution, the scanning pattern, FOCUS, OpenLineage)
- **(a)** Score and tier them like products. Ownership changes in example components reduce the lock-in score.
- **(b)** Same tiers, but drop the Acquired flag and lock-in reduction where the component is replaceable (+0.15 FS each).
- **(c)** Remove patterns from the scorecards and present them as "required design". C5, C6 and C8 would then have no Strategic product.

**Q8: Presidio (3.65), Strategic with volunteer governance since June 2026**
- **(a)** Keep Strategic, conditional: behind a firm-owned privacy-service API, with recall tests in CI.
- **(b)** Make it Tactical until the new governance has a year of track record.
- **(c)** Keep it Strategic, with a fork-and-maintain plan as a stated condition.

**Q9: Controls capped only by missing product-scoped certification** (watsonx.governance, Prisma AIRS, ValidMind, Credo AI)
- **(a)** Keep the caps and Tactical tiers, with "candidate for Strategic after due diligence" conditions.
- **(b)** Treat these as due-diligence items: score security at anchor minus one (3). watsonx.governance becomes Strategic, conditional.
- **(c)** Stricter: no "candidate" wording until an audit report has been read.

## 4. What could not be verified

| Gap | Detail |
|---|---|
| Audit reports | No audit report has been read for any product (B4). Every security score rests on vendor or trust-centre listings. |
| Search extracts | Facts from 690+ search extracts are capped at medium confidence. The desktop gap-fill (`RERUN_ON_DESKTOP.md`) would lift many caps, especially in C8, L5 and L4. |
| Interruptions | The usage limit (429) interrupted the agents twice today. No work was lost: each was resumed from its saved state (MEMORY B9). |
