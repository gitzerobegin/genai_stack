# Enterprise GenAI reference architecture, October 2026: synthesis

| | |
|---|---|
| **Date** | 9 October 2026 |
| **Status** | Stage C synthesis (plan §12 and §16). It covers Parts I and III–XI of the master document. Part II (method, confidence legend, scorecard and classification) and the 17 layer and control chapters sit elsewhere in the master document. |
| **Basis** | The 17 Stage B sections (`work/stageB/{L9..L1,C1..C8}/section.md`), their x.9–x.13 subsections, `work/stageB/_review/all_scores.md` with the CP4 tier decisions applied, `regulatory_facts.json`, and the What-changed table (`checkpoints/CP1/02_What_Changed_Since_Original_Diagram.md`) |
| **Binding decisions applied** | CP1 (SR 26-2 framing; NPV caps), CP2 rules 6–9, CP3 rules 10–13 and tiers, CP4 decisions 1–9 (`checkpoints/CP4/00_CP4_CP4b_Decisions.md`) |
| **Claim tags** | `[VF …]` verified fact · `[R …]` reported, each followed by source IDs · `[AJ]` architectural judgement · `[Rec]` recommendation · `[NPV]` not publicly verified. IDs resolve in `Enterprise_GenAI_Stack_Oct2026/06_References/bibliography.xlsx` and `05_Data/regulatory_facts.json`. |

> **Conflict-of-interest disclosure.** The author is an Anthropic model. This synthesis ranks Anthropic's Claude models, the Claude Agent SDK and two Anthropic-originated standards (the Model Context Protocol and Agent Skills) alongside their competitors. All of them were scored on the same rubric as every other product. The Strategic, conditional tier of the Claude model family was set by the reader at CP4, on the neutral-rubric scores the calibration reviewer put forward; the author did not set it, and the conflict-of-interest disclosure stays in force. Wherever an Anthropic product or an Anthropic-originated standard appears in a recommended stack, an independent alternative is named beside it [AJ].

**Tier changes applied in this synthesis (CP4, set by the reader).** These are treated as final even where a section file still shows the earlier tier [AJ]:

| Item | Section draft | Final tier (CP4) | Condition |
|---|---|---|---|
| L1 Anthropic Claude family | Tactical, FS 3.55 | **Strategic, conditional**, FS ≈ 3.80 on neutral-rubric scores (cost 4, security 5) | Consumed through a hyperscaler UK or EU region, with a qualified non-Anthropic fallback; an independent alternative always named |
| L2 SGLang | Tactical, FS 3.65 | **Strategic, conditional** | Qualified backup engine to vLLM, once CVE-2026-3059 is confirmed fixed in the deployed version and internal ports are isolated |
| L2 Fireworks AI | Tactical ("candidate") | **Strategic, conditional** | Managed open-model inference, once its ISO certificates are confirmed |
| L3 Pydantic AI | Tactical, FS 3.55 | **Strategic, conditional** | Python teams wanting type-safe agent steps |
| L3 Google ADK / Agent Engine | Strategic, conditional (CP4 review) | **Strategic, conditional** | Google Cloud is the primary cloud |
| L3 Claude Agent SDK | Experimental, maturity 1 | **Experimental**, maturity 2 (FS 2.75) | Sandboxed sub-step only; the vendor's own "Alpha" label is noted |
| L1 Gemini | Strategic, conditional | Unchanged | Google Cloud is the primary cloud |
| L1 DeepSeek, Kimi, GLM | Tactical, Experimental, Tactical | Unchanged | Hosting caveat: on Azure, Kimi and GLM run on Fireworks outside the tenant |

After these changes the 140 records stand at **58 Strategic, 67 Tactical, 13 Experimental and 2 unscored** [AJ]. Eighteen or more Strategic items sit below FS 3.6 because of rule 10 (hyperscaler lead services) or a reader decision, so a Strategic tier always travels with its condition, and in this synthesis **the condition is the decision, not the total** [AJ].

---

# Part I: Executive summary

## I.1 What changed since the original architecture

The original graphic ("Full AI Stack Explained", dated October 2026) draws nine layers and 80 product tiles as a shelf of tools [AJ]. This review's What-changed table, built from Stage A research and corrected by two adversarial verifiers, flags **39 of the 80 tiles** as out of date: 9 acquired, 9 mispositioned, 8 renamed, 8 with a wrong version label, 6 not publicly verifiable, 4 duplicated, 3 superseded and 2 deprecated, with some tiles carrying more than one flag [AJ]. The full row-by-row table, with sources, is in `checkpoints/CP1/02_What_Changed_Since_Original_Diagram.md` and `Enterprise_GenAI_Stack_Oct2026/05_Data/what_changed.xlsx` [AJ]. Ten findings matter most to a regulated asset manager.

**1. The graphic describes a catalogue; the enterprise problem is a control system.** None of the eight controls this review adds (gateway, guardrails, DLP, identity, configuration, FinOps, AI security, governance) appears in the graphic [AJ]. Meanwhile the gateway has become the place where model, tool and agent traffic is governed: LiteLLM, Kong, Azure API Management, Apigee and agentgateway all govern LLM, MCP and A2A traffic [VF: A6-S015, A6-S016, A6-S053, A6-S024, A6-S061]. The architecture that matters is the control plane wrapped around the tiles, not the tiles themselves [AJ].

**2. "Neutral" tooling is now mostly owned by platform vendors.** Dynatrace completed its acquisition of Arize (Phoenix and AX) on 1 October 2026 [VF: A1-S045, V1-S005]. ClickHouse announced it had acquired Langfuse on 16 January 2026 [VF: A1-S021, V2-S041]. OpenAI announced its acquisition of Promptfoo on 9 March 2026, with no closing published [VF: A1-S024, V1-S006]. MongoDB owns Voyage AI and Elastic owns Jina AI [VF: A2-S033, V1-S023, A2-S023, V1-S025]. Nebius closed its acquisition of Tavily on 19 February 2026 [VF: A3-S084, V1-S041]. Stripe agreed to acquire OpenRouter on 19 August 2026, with closing pending [VF: V1-S059, V1-S060]. Palo Alto Networks bought Portkey and Protect AI, Check Point bought Lakera, Harvey bought Guardrails AI, and Mintlify bought Helicone [VF: A6-S011, V2-S025, A7-S014, V2-S039, A7-S012, V2-S038, A6-S028, A7-S112, V2-S043]. SpaceX acquired xAI on 2 February 2026 [VF: V2-S011]. The consequence is that independence, exit planning and effective challenge can no longer be assumed from a product's origins; they must be designed in [AJ].

**3. Models are tiered families with gated tops and short lives.** GPT-6 is a family (Astra, Sol, Luna, plus GPT-6.1 Sol) [VF: A5-S002, A5-S004]; Claude Fable 5.1 sits above Opus, Sonnet and Haiku 5.5 [VF: A5-S010, A5-S019]; Gemini 3.x runs alongside a restricted Gemini 4 Argon [VF: A5-S030, A5-S031]. The graphic's "Gemma 2.9" does not exist and Mistral Medium 3.1 retired on 31 August 2026 [VF: A5-S034, B-L1-S002]. The most capable tiers are now gated by their vendors [VF: A5-S002, A5-S003, A5-S016, A5-S031], and a Gemini Flash version released on 13 August 2026 retires on 28 January 2027 [VF: B-L1-S003]. Model choice is therefore a portfolio and lifecycle discipline, not a one-off selection [AJ].

**4. Every serious agent framework now separates workflows from agents.** LangGraph, Microsoft Agent Framework, CrewAI and Google ADK 2.0 all ship a deterministic workflow engine alongside an agent loop [VF: A4-S039, A4-S066, A4-S050, A4-S114]. Durable execution has split off into engines such as Temporal [VF: A4-S045, A4-S052, A4-S058]. Microsoft Agent Framework reached GA on 2 April 2026, with AutoGen in maintenance mode [VF: A4-S008, A4-S021, V1-S050], and OpenAI's Agent Builder shuts down on 30 November 2026 [VF: A4-S054, V1-S051]. The single most important design decision in the stack is whether a process is a workflow or an agent [AJ].

**5. Protocols moved to foundations, and agent identity became a product category.** Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation on 9 December 2025, and A2A 1.0.0 joined the same foundation in August 2026 [VF: A3-S018, V1-S038, A3-S079, A3-S116, A3-S117]. The MCP 2026-07-28 specification adds gateway-friendly routing and the Enterprise-Managed Authorization extension is stable, but authorisation remains optional in the specification [VF: A3-S015, A3-S057, A3-S017, A3-S055]. Entra Agent ID, Okta for AI Agents, Okta Agent SSO and Cedar-based AgentCore Policy all reached GA between November 2025 and August 2026 [VF: V2-S032, A6-S097, A6-S100, V2-S035, A6-S026]. An agent must now be treated as a non-human actor with its own identity and delegated authority [AJ].

**6. "Vector database" now describes a feature, not a product category.** Hybrid lexical-plus-vector retrieval ships in almost every store [VF: A2-S056, A2-S060, A2-S054, A2-S133, A2-S141, A2-S103, A2-S101]. pgvector, MongoDB and Elasticsearch put vectors inside platforms firms already run [VF: A2-S061, A2-S137, A2-S133], and Amazon S3 Vectors has been GA since December 2025 [VF: A2-S081, V1-S030]. Embedding and reranking are now sold together by almost every model vendor, and the stores host both [VF: A2-S012, A2-S010, A2-S006, A2-S025, A2-S030, A2-S020, A2-S141, A2-S101]. Retrieval is a governed, derived index over approved content, not a separate database purchase [AJ].

**7. The independent memory layer is thinning.** Mem0 removed external graph stores from its open-source build, Zep deprecated its Community Edition, Letta pivoted to an agent harness and LangMem has not released since 27 October 2025 [VF: A3-S053, V1-S043, A3-S059, A3-S093, A3-S006]. AWS and Google now ship memory inside their agent platforms [VF: V1-S087, V1-S088], and OWASP lists memory and context poisoning as ASI06 [VF: B-L5-S001]. Memory is a regulated record class that belongs with the firm's data stores, not a separate product layer [AJ].

**8. The supply chain and the tooling vendors are now attack surfaces.** Malicious LiteLLM releases 1.82.7 and 1.82.8 were published to PyPI on 24 March 2026 [VF: A6-S008, V2-S027]. Composio disclosed a May 2026 incident in which connected-account tokens and API keys were exposed [VF: B-L4-S007]. Hugging Face archived its TGI repository on 21 March 2026 and Helicone is in maintenance mode [VF: V1-S054, A7-S112]. Supply-chain, credential-custody and product-retirement risk now sit at the same level as model risk [AJ].

**9. The regulatory anchors moved in 2026.** SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001, A8-S002]. The EU AI Act's GPAI enforcement powers started on 2 August 2026, and Regulation (EU) 2026/1744 moved Annex III high-risk duties to 2 December 2027 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011]. The DORA critical-provider list and the UK CTP designations cover hyperscalers and no model vendor [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. PRA PS7/26 and FCA PS26/2 require material third-party notifications from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. OWASP published 2026 editions of both its LLM and Agentic Top 10 lists [VF: R-OWASP-LLM, V2-S056; R-OWASP-AGENTIC, A8-S042]. PRA SS1/23 and the EU AI Act are therefore the operative model-risk anchors, and the firm must write its own GenAI standard [AJ].

**10. "Open source" in the graphic often is not.** Phoenix is under ELv2, a source-available licence [VF: A1-S048], Firecrawl's server is AGPL-3.0 [VF: A1-S053], MinerU 4.0 carries commercial thresholds [VF: A1-S054], Jina's weights are CC-BY-NC-4.0 [VF: A2-S024], Weaviate is moving to open core [VF: A2-S115, V1-S070], and the Claude Agent SDK is governed by Anthropic's Commercial Terms [VF: A4-S092]. Licence review is an architectural gate, not a procurement afterthought [AJ].

## I.2 The recommended 2026 enterprise architecture in one page

**The answer in one sentence.** Build a firm-owned control and evidence plane first (gateway, identity, privacy, configuration, evaluation and the evidence store), run regulated work as deterministic workflows with one bounded model step and a human approval gate, consume models as a two-vendor portfolio through the primary cloud's in-region model service, and treat every product beneath that plane as a replaceable component [Rec].

```text
                 CONTROL PLANE (firm-owned policy, one evidence store)
  C1 AI traffic gateway (model + tool + agent calls) · C2 guardrails · C3 privacy service
  C4 identity & authorisation · C5 configuration of record · C6 FinOps · C7 AI security
  C8 model risk, governance & evidence store  <====  L9 evaluation & observability plane
 -------------------------------------------------------------------------------------
  AGENT PLANE      L3 orchestration: workflows (default) | bounded agent steps | durable runtime
                   L4 tools & connectivity, behind a tool-governance sub-layer (MCP / OpenAPI / A2A)
  KNOWLEDGE PLANE  L8 ingestion & data preparation (with ingestion control envelope)
                   L7 retrieval optimisation (embed + rerank + fusion, versions pinned)
                   L6 retrieval, knowledge & memory stores (derived, entitlement-filtered;
                      L5 memory service as a governed logical component)
  MODEL PLANE      L2 inference: model access | serving engines | optimisation (optional)
                   L1 foundation-model portfolio (two mid-tier vendors + small + open-weight)
```

**Twelve decisions that define the architecture [Rec]:**

1. **One gateway of record (C1)** for all production model, MCP and agent traffic, deployed twice, in region, failing closed, with pinned and signed builds. It is what makes a model exit a configuration change. [Rec]
2. **Evaluation and observability from day one (L9):** a firm-owned OpenTelemetry Collector, Git-versioned evaluation datasets, one platform of record, and two red-team tools of which one is independent of the model vendor under test. [Rec]
3. **A firm-owned evidence store (C8)**, immutable and keyed by trace ID, holding an evidence pack for every regulated output; vendor tools write to it, never instead of it. [Rec]
4. **A two-vendor model portfolio (L1)** consumed through the primary cloud's model service in an approved UK or EU region, plus a small model and a self-hosted open-weight model on vLLM as the stressed-exit route. [Rec]
5. **Deterministic workflows by default (L3)**, with a declared autonomy budget, durable execution, and approval interrupts that only a named, entitled human can resume. [Rec]
6. **Read-only tools for authoritative data (L4)**, reached only through a tool-governance sub-layer with mandatory authorisation, a private allow-listed registry and hash-pinned definitions. MCP is the default protocol; OpenAPI tools behind the same gateway are the independent alternative. [Rec]
7. **Every agent a registered identity (C4)** with a sponsor, acting on behalf of the requesting human through short-lived, audience-bound tokens; deny-by-default policy for every tool call. [Rec]
8. **One privacy service (C3)** called at six enforcement points: ingestion, prompt, tool results, output, memory writes and trace export. [Rec]
9. **Retrieval inside platforms the firm already runs (L6)**, as a derived, rebuildable, entitlement-filtered index; a dedicated vector engine only when a load test proves the need. [Rec]
10. **Git as the configuration of record (C5)**: prompts, model pins, embedding and reranker versions, tool lists and guardrail policy released as one manifest through a pull request with a second approver and an evaluation gate. [Rec]
11. **Capability separation as the first security control (C7):** no agent holds untrusted input, sensitive data and an outbound channel at once; detectors are swappable call-outs behind the gateway. [Rec]
12. **Memory last (L5/L6)**, as a governed record class with a policy-gated write path, subject-scoped erasure and per-run snapshots. [Rec]

**The default choices, cloud-neutral, with the primary-cloud equivalent [Rec].** Stack A (regulated enterprise) is the lead stack; Part VII gives all four stacks in full.

| Layer / control | Cloud-neutral default | AWS primary | Azure primary | Google Cloud primary |
|---|---|---|---|---|
| C1 gateway | LiteLLM Enterprise (hardened, pinned) or Kong AI Gateway hybrid | AgentCore Gateway for MCP; model routing on the cloud-neutral gateway | APIM AI gateway policies in GA tiers | Apigee (hybrid where in-estate is required) |
| L9 evaluation | Langfuse self-hosted, or MLflow where an ML platform exists | MLflow on SageMaker | MLflow on Azure ML | Langfuse self-hosted (no Google-native option profiled) |
| L1 models | Two vendors from OpenAI, Anthropic (independent alternative: GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5), Mistral, Gemini; Gemma 4 or Mistral self-hosted | Claude Sonnet 5.5 or a GPT-6 tier on Bedrock, the other as fallback | GPT-6.1 Sol in a Foundry EU Data Zone; Mistral Medium 3.5 fallback | Gemini 3.8 Flash; Claude Sonnet 5.5 via Google Cloud EU as fallback |
| L3 orchestration | LangGraph + Temporal | Strands on AgentCore Runtime | Microsoft Agent Framework + Foundry Hosted Agents | Google ADK on Agent Engine |
| L6 retrieval | pgvector on managed PostgreSQL, or Elasticsearch where operated | pgvector (RDS/Aurora) | pgvector (Azure Database for PostgreSQL) | pgvector (Cloud SQL) |
| C4 identity | Workforce IdP (Entra or Okta) + OPA + SPIFFE/SPIRE | AgentCore Identity + AgentCore Policy (Cedar) | Entra Agent ID | Workforce IdP + OPA |

## I.3 What to keep · what to remove · what is missing

**What to keep.** These elements of the original graphic remain sound, sometimes under a new name [AJ]:

| Keep | Why (tagged in the sections) |
|---|---|
| The nine-layer spine as a teaching device | It still maps the work; Part IV renames, splits and merges layers rather than discarding them [AJ] |
| vLLM, Hugging Face (Hub), SGLang (conditional) | vLLM is Apache-2.0 and PyTorch Foundation-hosted [VF: A4-S009, A4-S146]; the Hub is the governed open-weight supply [VF: A4-S075] |
| LangGraph | Workflows and agent loops in one graph, 1.x GA [VF: A4-S039, A4-S001] |
| Docling, Unstructured | MIT under LF AI & Data, graduated August 2026 [VF: V1-S091, A1-S057]; ACL-digest connectors [VF: A1-S094] |
| pgvector, Qdrant, Milvus, Elasticsearch, MongoDB | Vectors in operated platforms or open engines [VF: V1-S020, A2-S108, A2-S118, A2-S133, A2-S137] |
| Sentence Transformers | The self-hosting, fine-tuning and exit toolkit [VF: A2-S029] |
| Langfuse, LangSmith | Platforms of record for traces and evaluations [VF: A1-S033, A1-S039] |
| MCP and A2A | Now under a foundation; Strategic only behind a governed gateway (CP3) [VF: A3-S018, A3-S116] |
| OpenAI, Anthropic, Gemini, Mistral, Gemma | The portfolio candidates; the tier comes with its route condition [AJ] |

**What to remove or demote.** These should come out of an enterprise reference architecture, or be pinned below the line [Rec]:

| Remove or demote | Evidence |
|---|---|
| EthicalAgents, Ragoos | Could not be verified; removed at CP1 [VF: A2-S079, A2-S080] |
| "Gemma 2.9", "QI4", "Mistral Medium 3.1", unversioned "Mistral OCR" | Labels that do not exist or have been retired [VF: A5-S034, A5-S071, B-L1-S002, A1-S130] |
| TGI | Repository archived 21 March 2026 [VF: V1-S054] |
| OpenRouter as "the" multi-provider layer | A model-access source behind the firm's gateway, not the gateway; owner changing [VF: A4-S111, V1-S059] |
| Separate "Embeddings" and "RAG re-rankers" rows | One retrieval-optimisation responsibility [VF: A2-S012, A2-S010, A2-S029] |
| Memory as a separate infrastructure layer | Memory products are retrieval stacks with an extraction step [VF: A3-S053, A3-S003, A3-S005] |
| "Agent SDK" tiles as peers of LangGraph | Model-vendor harnesses belong in sandboxed sub-steps; the Claude Agent SDK is Alpha and the OpenAI Agents SDK is pre-1.0 [VF: A4-S006, A4-S005] |
| Ollama and LM Studio in the production picture | Developer tier only; LM Studio's terms exclude service use [VF: A4-S084, A4-S145] |
| Evaluation drawn as the last box in the pipeline | It is the evidence plane for every layer [AJ] |

**What is missing.** The graphic has no place for the following, and each is a named component in the recommended architecture [AJ]:

| Missing capability | Where it now lives |
|---|---|
| AI traffic gateway (model, tool and agent calls) | C1, promoted to the control plane |
| Guardrails, owned as policy and test sets | C2, invoked from the gateway |
| DLP and PII protection at six enforcement points | C3 privacy service |
| Agent identity, delegated authority and tool governance | C4 plus the L4 tool-governance sub-layer |
| Configuration of record (prompts, pins, manifests) | C5 |
| Cost per task, budgets that fail closed | C6, metered at C1, joined to L9 traces |
| Secrets, supply chain, sandboxing, injection defence | C7 |
| Model inventory, validation, evidence store | C8 |
| Durable execution and managed agent runtimes | L3 substrate [VF: B-L3-S002, A4-S116] |
| Hyperscaler model services as the enterprise access route | L2 model access [VF: B-L2-S005, B-L2-S006, B-L2-S008] |
| Ingestion control envelope (source register, lineage, ACLs, incremental indexing) | L8, built around replaceable parsers [VF: A1-S094, A7-S042] |
| Hyperscaler agent stacks (AgentCore, Foundry, Agent Engine) | Per-cloud alternatives across L3–L5, C1, C2, C4 [VF: A3-S047, B-L3-S006, A4-S114] |

## I.4 How to read the tiers, and where this synthesis departs from the sections

**Tiers carry conditions.** "Strategic, conditional: where AWS is your primary cloud" means that the product is the right default only in that estate; the per-cloud Strategic items are alternatives, not a shopping list [AJ]. The five hyperscaler AgentCore records (L3, L4, L5, C1, C4) should be read as **one AWS platform decision**: security 4 and deployment 2 agree across all of them, and their cost and lock-in differences reflect evidence and lens, not contradictory views [AJ].

**Route, not total, for Chinese-origin model families.** The L1 scores mix routes across criteria: enterprise readiness on the best hyperscaler route, security on the vendor's own certifications [AJ]. For DeepSeek, Qwen, Kimi and GLM the decision is therefore the route: self-hosted open weights by explicit policy, or in-tenant hyperscaler hosting, never the vendor's own API for client data [Rec]. On Azure, Kimi and GLM run on Fireworks outside the customer tenant, while DeepSeek V4 is sold directly by Azure [VF: A5-S087].

**Hyperscaler model services are not scored anywhere.** Bedrock, Microsoft Foundry and the Gemini Enterprise Agent Platform (formerly Vertex AI) model services have no product records, because Stage A could not fetch their primary pages [AJ]. This synthesis treats them as covered by the L1 family records and the C1 gateways: the lead model service of the primary cloud is the default access route, Strategic, conditional on that cloud, in the same sense as rule 10 [AJ].

**Where the synthesis departs from a section [AJ].** The sections' provisional views were followed except in four places, each stated here and argued in Part III. No score is changed by these departures.

- **H3 placement.** L4 proposes a tool-governance sub-layer inside L4; C4 proposes a control-plane component. The verdict takes both: the enforcement point is an L4 sub-layer, and the decisions it enforces belong to C4 with C7. [AJ]
- **H4 strength.** L5 recommends a physical merge into L6; this synthesis agrees but keeps the "L5 memory service" label visible as a logical component, because its controls (write gate, subject erasure) are unique and auditors will look for them. [AJ]
- **H7 ownership.** L8 places the ingestion control plane in L8; C3 places policy in C3; C8 places lineage evidence in C8. The verdict keeps the build in L8, with policy from C3 and evidence to C8, and adds that runtime lineage lives in L9 traces. [AJ]
- **L1 Anthropic and L2/L3 tiers.** The L1, L2 and L3 section texts still show the pre-CP4 tiers for Anthropic, SGLang, Fireworks AI and Pydantic AI; the reader's CP4 decisions prevail here. [AJ]
