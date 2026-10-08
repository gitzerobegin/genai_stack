# Checkpoint 1: research baseline (Stage 0, Stage A, Stage A′)

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Plan** | `inputs/Enterprise_GenAI_Stack_Consolidated_Plan_v4.3.md`, executed per `inputs/Execution_Prompt_GenAI_Stack.md` |
| **Status** | Stopped for your review, as the execution prompt requires. Stage B (writing) has **not** started. |
| **Disclosure** | The author is an Anthropic model. Anthropic products and Anthropic-originated standards are held to the same rubric as everything else. |

## 1. What is done

| Stage | Output | Where |
|---|---|---|
| **0 Baseline** | Inventory of all 80 tiles and their implied relationships; ambiguities A1–A19; missing capabilities; dataset schema (32 fields, with labelled fact cells); style guide; hypotheses H1–H8 with the evidence each needs; research and verification briefs | `work/stage0/` |
| **A Research** | 8 parallel research streams, each with a gap-filling pass:<br>① L9+L8 · ② L7+L6 · ③ L5+L4 · ④ L3+L2 · ⑤ L1 · ⑥ C1–C4 · ⑦ C5–C8 · ⑧ Regulation | `work/stageA/<stream>/` (products.json, notes.md, sources.csv) |
| **A′ Verify** | 2 adversarial verifiers. **192 high-risk claims re-checked:**<br>• 164 confirmed<br>• 21 corrected<br>• 5 downgraded<br>• 2 unresolvable<br>No fabricated claims were found. | `work/stageA_verify/V1`, `V2` (verification_log.md) |
| **Dataset** | **140 product records** and **20 regulatory records**, totalling 4,620 labelled product fact cells | `Enterprise_GenAI_Stack_Oct2026/05_Data/` (products.json, products.xlsx, regulatory_facts.json, what_changed.xlsx) |
| **Source archive** | **1,119 sources** (92% primary), each logged with URL, access date, type and archive path. **Every claim is mapped to its source.** | `Enterprise_GenAI_Stack_Oct2026/06_References/` (bibliography.xlsx, snapshots/, originals/) |

The integrity check passes: every cited source ID resolves, and no "Verified fact" or "Reported" cell lacks a source (`work/stageA/_integrity_report.md`).

### Documents for your review

1. `work/stage0/01_baseline_inventory.md`: the inventory
2. `checkpoints/CP1/02_What_Changed_Since_Original_Diagram.md`: 145 rows, verifier-corrected
3. `checkpoints/CP1/03_Ambiguity_Resolutions.md`
4. `checkpoints/CP1/04_Control_Plane_Product_List.md`
5. `checkpoints/CP1/05_Scorecard_Weights.md`

## 2. Headline findings

**The graphic is out of date in 39 of its 80 tiles.**

| Flag | Tiles |
|---|---:|
| Acquired | 9 |
| Mispositioned | 9 |
| Renamed | 8 |
| Wrong version label | 8 |
| Not publicly verified | 6 |
| Duplicated | 4 |
| Superseded | 3 |
| Deprecated | 2 |

A tile can carry more than one flag. The other 41 tiles are "No change", though several carry scope notes.

The main changes:

1. **Ownership has consolidated.** These have been acquired, or an acquisition has been announced:
   - **Graphic tiles:** Arize and Phoenix → Dynatrace · Langfuse → ClickHouse · Promptfoo → OpenAI (announced) · Voyage → MongoDB · Jina → Elastic · Tavily → Nebius · OpenRouter → Stripe (pending) · xAI → SpaceX
   - **Control plane:** Portkey → Palo Alto · Guardrails AI → Harvey · Lakera → Check Point · Protect AI → Palo Alto · Helicone → Mintlify

   Neutral tooling is increasingly owned by platform vendors. This is a lock-in and concentration signal for C1, C7 and L9.
2. **Several Layer 1 labels are wrong or incomplete.**
   - "Gemma 2.9" and "QI4" do not exist. They are Gemma 4 and Z.ai GLM-5.x.
   - "Mistral Medium 3.1" is superseded.
   - "Opus 5.5" is correct but is not Anthropic's top tier.
   - GPT-6 is a tiered family: Astra, Sol and Luna.
   - Meta's frontier family is now Muse.
3. **Two tiles appear to be fictional.** "EthicalAgents" and "Ragoos" could not be found after repeated searches.
4. **Licences have shifted from the graphic's "open source" framing.**
   - Phoenix is ELv2 (source-available).
   - Firecrawl's server is AGPL.
   - MinerU 4.0 has commercial thresholds.
   - Jina weights are CC-BY-NC.
   - Weaviate is moving to open core.
   - LM Studio is a proprietary app.
   - The Claude Agent SDK is governed by Anthropic's Commercial Terms.
5. **Protocols now sit under foundations, and identity has become a real product category.**
   - MCP (spec 2026-07-28, stateless) and A2A (1.0) are both under the Agentic AI Foundation.
   - Agent Skills is an open format **without** a neutral governance body.
   - Agent identity now has GA products and standards: Entra Agent ID, Okta Agent SSO, AgentCore Policy, and the MCP enterprise-managed authorisation extension.
6. **The regulatory anchors have moved.** Each item below has a section 6 question.
   - SR 11-7 is superseded by **SR 26-2** (17 April 2026), which **excludes GenAI and agentic AI**.
   - EU AI Act Annex III high-risk duties are deferred to **2 December 2027** (Regulation (EU) 2026/1744).
   - The DORA and UK critical-third-party designations cover hyperscalers but **no model vendor**.
   - UK third-party notification rules apply from 18 March 2027.
   - Both OWASP lists now have 2026 editions.

## 3. Early hypothesis evidence

This is evidence only. Verdicts come in Stage C.

| # | Direction of the evidence |
|---|---|
| H1 Split L2 / promote the gateway | **Supports.** Serving engines (vLLM, SGLang), optimisation layers (NVIDIA Dynamo, llm-d), routers (OpenRouter) and enterprise gateways (Kong, APIM, Apigee, agentgateway) are now marketed as distinct categories. Gateways now carry LLM, MCP and A2A traffic. |
| H2 Separate deterministic workflows from autonomous agents | **Supports.** Every major framework now ships both modes: LangGraph, Microsoft Agent Framework, CrewAI Flows vs Crews, and Pydantic AI with Temporal/DBOS. Mistral builds Workflows on Temporal. |
| H3 Identity and tool-governance sub-layer | **Strongly supports.** See finding 5. |
| H4 Memory is not separate from retrieval/data | **Mixed.** Memory products sit on vector and graph stores, and the hyperscalers now offer built-in memory (AgentCore Memory, Vertex Memory Bank). Mem0 and Zep have narrowed their open-source editions. Erasure controls vary widely. |
| H5 Rename to "Retrieval / Knowledge Stores" | **Supports.** Pinecone markets itself as a "knowledge engine". Hybrid and BM25 search are now standard. MongoDB, Elastic and Postgres have absorbed vector search. S3 Vectors is GA but has no BM25. |
| H6 Embeddings and reranking as one layer | **Supports.** Cohere, Voyage, Jina, NVIDIA and Qwen all ship both embeddings and rerankers. Pinecone, MongoDB and Elastic now host rerankers. |
| H7 Ingestion needs lineage, PII and access control | **Partly.** Unstructured syncs permission metadata and Firecrawl redacts PII, but no L8 product offers lineage. OpenLineage has no GenAI facets, although Collibra integrates with it. |
| H8 Evals and observability are cross-cutting | **Supports.**<br>• The OTel GenAI conventions are still in "Development" but are widely adopted.<br>• IBM watsonx.governance gates agents on eval thresholds.<br>• AI Act Article 26 sets minimum logging and monitoring duties for deployers. |

## 4. What could not be verified, and why

- **Research environment.** The egress policy blocked direct fetches from most vendor, trust-centre and regulator sites.
  - Direct fetch worked for PyPI, npm, raw GitHub files, anthropic.com, docs.claude.com and cloud.google.com.
  - Facts from blocked sites were read through **search extracts**. These are dated and archived as `*.extract.txt`, and their confidence is capped at *medium*.
  - Web search was capped at about 200 calls per agent turn, which is why each stream needed a gap-filling pass.
- **Fact cells.** 1,557 of the 4,620 product fact cells are *Not publicly verified*. They are mostly certifications, EU regions, SSO/RBAC and pricing for start-ups.
- **No audit report was read directly.** All SOC 2, ISO and HIPAA statements are vendor statements or trust-centre listings.
- **Claims the writers must not rely on** are listed in V1 and V2 verification logs §4. Examples:
  - press-reported deal values
  - vendor benchmark figures
  - the scope of the D.C. Circuit ruling on Anthropic
  - Chinese-vendor API prices, which come from aggregators
- **Unchecked by the verifiers** (listed in each log §5): mostly pricing and lower-risk certifications.
- **Not profiled:** ServiceNow AI Control Tower and OneTrust (C8); Daytona and Modal sandboxes (L4); Azure AI Search and Vertex AI Vector Search (L6).

## 5. Deviations from the plan

| Plan / prompt | What happened | Why |
|---|---|---|
| Source archive with originals and web snapshots | 440 direct snapshots, 677 search extracts, 2 link-only. No PDF originals could be downloaded. | Egress policy. Nothing was worked around. |
| About 120 product profiles | 140 records | 12 material additions in the layers, plus 4 extra controls found during research |
| ZIP saved to a named folder (decision 6) | Deliverables are committed to the `gitzerobegin/genai_stack` repository | You asked for results in GitHub; decision 6 was left as a placeholder |

## 6. Open questions, with options

**Q1: Scorecard weights** (`05_Scorecard_Weights.md`)
- (a) Keep the §8.1 weights as they are.
- (b) Keep the weights, but move FS 5% from Technical capability to Lock-in/concentration (making it 20%).
- (c) Keep the weights, and add a published sensitivity view: the ranking under both weight sets, plus one "concentration-heavy" set.

**Q2: How to score fields that are "Not publicly verified"**
- (a) Penalise. An NPV security or enterprise-readiness item caps that criterion at 2. This is the strict default in the style guide.
- (b) Neutral. Score from what is verified, and flag the product as "evidence incomplete".
- (c) Withhold. Do not score a criterion where more than half the inputs are NPV, and mark it "insufficient evidence".

**Q3: The FS lens and the replacement of SR 11-7**
- (a) Frame the US view around SR 26-2, and state explicitly that it excludes GenAI. Use PRA SS1/23 and the EU AI Act as the operative model-risk anchors.
- (b) Keep SR 11-7 as the conceptual reference most readers know, with a prominent "superseded" note.
- (c) Both: lead with (a), and use SR 11-7 only in a short "what changed" box.

**Q4: EthicalAgents and Ragoos**
- (a) Remove them from the analysis, with one line in the "What changed" table.
- (b) Keep them in the appendix as "Not publicly verified" records.
- (c) If you know what the graphic's author meant, tell me and I will research it.

**Q5: Evidence quality before Stage B**
- (a) Proceed on the current fact base. Confidence stays capped at medium where a fact came from a search extract.
- (b) First widen this cloud environment's network access, then run a primary-source snapshot pass on high-risk facts before Stage B. To widen it: environment settings → Network access → add vendor, trust-centre and regulator domains.
- (c) Proceed now, and run that snapshot pass on high-risk facts before CP5 only.

**Q6: Scope of the 140 records**
- (a) Keep all 140. The added records are material.
- (b) Trim to the 80 tiles plus the plan's control candidates. Move the additions to a "products to monitor" list.
- (c) Keep all 140, and also profile ServiceNow, OneTrust, Azure AI Search and Vertex Vector Search.

**Q7: How to run the rest**
- (a) Keep stopping at CP2, CP3, CP4, CP4b and CP5, as the prompt specifies.
- (b) Run unattended to CP5. I would record my assumptions in the README.
- (c) Stop only at CP4b (LinkedIn voice) and CP5.

**Q8: Deliverable destination** (decision 6)
- (a) GitHub repository only. The ZIP is committed under `Enterprise_GenAI_Stack_Oct2026/`.
- (b) Also publish the explorer as a hosted page, and the master document as a Claude Doc, as §14 specifies.
- (c) Name a folder, and the final ZIP will also be prepared for download.
