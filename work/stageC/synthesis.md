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

---

# Part III: Architecture hypotheses — verdicts (H1–H8)

The plan required the nine-layer structure to be tested, not assumed (plan §4). Each hypothesis below gives the evidence the sections gathered, the counter-evidence, a verdict (keep / rename / merge / split / reposition) and the resulting change to the architecture [AJ]. The verdicts are summarised first.

| # | Hypothesis | Verdict | Resulting architecture change |
|---|---|---|---|
| H1 | Split L2; promote the gateway to the control plane | **Split** (L2) and **reposition** (gateway) | L2 becomes model access · serving engines · optional optimisation; C1 becomes the "AI traffic gateway" for model, tool and agent calls [AJ] |
| H2 | Distinguish deterministic workflows from autonomous agents | **Split** (into sub-layers of one layer) and **rename** | L3 "Orchestration: workflows and agents", with three stacked concerns: workflow orchestration (default), bounded agent steps, durable execution and runtime [AJ] |
| H3 | An agent identity, authorisation and tool-governance sub-layer | **Keep**, implemented as a split | L4 gains a mandatory tool-governance sub-layer (the enforcement point); the decisions it enforces sit in C4 with C7 as one identity-and-credential plane [AJ] |
| H4 | Memory is not separate from retrieval and data | **Merge** | L5 merges physically into the stores layer; a thin "L5 memory service" stays as a governed logical component; organisational memory moves to C5; built last [AJ] |
| H5 | "Vector database" becomes "Retrieval / Knowledge Stores" | **Rename** | L6 "Retrieval, knowledge and memory stores": a derived, entitlement-filtered, rebuildable index with four implementation options [AJ] |
| H6 | Embeddings and reranking form one retrieval-optimisation layer | **Merge** | L7 "Retrieval optimisation": model choice, version pinning (held in C5), hybrid fusion policy and the retrieval evaluation gate [AJ] |
| H7 | Ingestion includes lineage, classification, PII/DLP, access-control metadata and incremental indexing | **Keep**, with a scope change (and runtime web access repositioned to L4) | L8 "Ingestion and data preparation" with a built ingestion control envelope around replaceable parsers; policy from C3, evidence to C8 [AJ] |
| H8 | Evaluation and observability are cross-cutting | **Reposition** | L9 leaves the bottom of the stack and becomes the evaluation and observability plane, joined with C8 as one evidence plane with two owners [AJ] |

## H1: Split L2 into serving → optimisation → gateway/routing, and promote the gateway

**Hypothesis.** L2 should split into model serving, inference optimisation and model gateway/routing, with the gateway promoted to a control-plane component (plan §4) [AJ].

**Evidence.**
- *Optimisation products define themselves as a separate layer.* NVIDIA Dynamo calls itself "the orchestration layer above inference engines", llm-d provides orchestration "above model servers", and LMCache calls itself "a KV cache management layer" [VF: A4-S090, A4-S089, A4-S091].
- *Access has separated from serving.* Hugging Face Inference Endpoints exposes the engine as a setting, routers aggregate many providers, and the hyperscalers sell processing location and reserved capacity as properties of the access contract [VF: A4-S081, A4-S075, A4-S113, B-L2-S005, B-L2-S006, B-L2-S008].
- *The gateway carries more than model traffic.* LiteLLM describes one control plane for LLMs, MCP servers and A2A agents, and Kong, Azure API Management, Apigee and agentgateway govern all three [VF: A6-S015, A6-S016, A6-S020, A6-S024, A6-S061]. AWS's AgentCore Gateway grew from tools towards models [VF: A6-S074, A6-S105].
- *Vendors call it a control plane, and the other controls run inline in it.* Cloudflare markets an "AI Application Control Plane" and Microsoft is integrating APIM as Foundry's AI gateway control plane [VF: A6-S019, A6-S020]. Guardrails, DLP, tool policy and cost attribution all run at the gateway [VF: A6-S017, A6-S053, A6-S026, A7-S010].
- *Security vendors are buying it.* Palo Alto Networks bought Portkey to put a gateway "in the traffic path" [VF: A6-S011].
- *L1 depends on it.* A model portfolio with residency routing, version pinning, fallback and deny-lists is unworkable without a firm-owned gateway (L1 hypothesis note) [AJ]. Cost metering and enforcement also settle at the gateway [VF: A6-S015, A6-S019, A6-S053] (C6).

**Counter-evidence.**
- vLLM and SGLang ship prefix caching, speculative decoding, quantisation and disaggregation inside the engine, so for most firms "optimisation" is engine configuration, not a product [VF: A4-S063, A4-S010].
- Dynamo and llm-d plug into the Gateway API Inference Extension, which blurs the boundary with the gateway at the Kubernetes edge [VF: A4-S090, A4-S062]. That router chooses a replica; C1 chooses a provider, model and region [AJ].
- Microsoft says its AI gateway is an extension of the API gateway, "not a separate offering" [VF: A6-S053]. The AI gateway may converge into API management rather than stand alone [AJ].
- The March 2026 LiteLLM compromise shows the blast radius of concentrating control in one component [VF: A6-S008] [AJ].

**Verdict: split L2 and reposition the gateway [AJ].** The split is real, but the order in the hypothesis is wrong for an enterprise: model access is the sub-layer most firms will actually operate, serving engines matter only where a private route is justified, and optimisation is optional and relevant only to firms that run their own GPU fleets [AJ].

**Resulting architecture change [Rec].**
- L2 is renamed **"Inference and model access"**, drawn as three sub-layers: *model access* (the primary cloud's model service, managed inference clouds, dedicated endpoints, routers), *serving engines* (vLLM, SGLang as the qualified backup), and *inference optimisation* (llm-d, Dynamo, LMCache; optional, marked "own-GPU estates only").
- Routing policy, fallback, budgets, guard invocation and the request log leave L2 and become **C1, the AI traffic gateway**, covering model, tool (MCP) and agent (A2A) calls. C1 is drawn as a logical control that may be implemented on the firm's API-management platform, deployed twice, failing closed.
- Agent logic never lives in the gateway; it routes and records, it does not author.

## H2: An "agent framework" is not one layer

**Hypothesis.** Architecture should distinguish deterministic workflows from autonomous agents (plan §4) [AJ].

**Evidence.**
- *Every major framework ships both modes, and several document the split.* LangGraph combines deterministic logic and LLM decisions in one graph; Microsoft Agent Framework separates Agents from Workflows; CrewAI pairs Flows with Crews and recommends Flows as the outer process; Google ADK 2.0 added a Workflow Runtime; LlamaIndex, Mistral and Vercel ship workflow engines [VF: A4-S039, A4-S066, A4-S050, A4-S114, A4-S041, A4-S058, A4-S071]. Anthropic's own guidance separates workflows from agents in the same terms [VF: A4-S030].
- *Durability is separating from both.* Pydantic AI v2 delegates durability to Temporal, DBOS or Prefect; the OpenAI Agents SDK integrates Temporal and DBOS; Mistral built Workflows on Temporal [VF: A4-S044, A4-S045, A4-S052, A4-S058].
- *Runtimes are separating from frameworks.* AgentCore hosts agents from several frameworks with per-session microVM isolation, and Foundry Hosted Agents accepts agents built with any framework [VF: A4-S116, B-L3-S004, B-L3-S006].
- *Visual builders are retreating.* OpenAI is retiring Agent Builder on 30 November 2026 and points code users to the SDK [VF: A4-S054].
- *Guardrails cannot rescue the wrong design.* The newest guardrail features for agent behaviour (Task Adherence, AlignmentCheck) are preview or unmaintained [VF: A6-S055, A6-S039, A6-S107], which supports deciding autonomy first (C2) [AJ].
- *Supervisors want a human in the loop.* The OCC observes banks adopting agentic AI "with guardrails and human-in-the-loop accountability" [VF: R-US-AGENCY-AI, A8-S004], and the Bank of England found 55% of AI use cases had some autonomous decision-making and 2% were fully autonomous [VF: R-UK-AI-STATEMENTS, A8-S056].

**Counter-evidence.** The split is two modes inside one framework, not two products with separate vendors [AJ]. Single-mode autonomous harnesses (the OpenAI and Claude agent SDKs, Mistral's Agents API) are moving fastest [VF: A4-S053, A4-S027, A4-S057].

**Verdict: split, as sub-layers of one layer, and rename [AJ].** Drawing workflows and agents as two separate layers would imply two vendors and two integration surfaces where one framework does both [AJ].

**Resulting architecture change [Rec].**
- L3 is renamed **"Orchestration: workflows and agents"**, with three stacked concerns: (1) *deterministic workflow orchestration* (graph, state, approvals), the default for enterprise processes; (2) *bounded autonomous agent steps*, admitted per use case with a declared autonomy budget, a tool allow-list and a sandbox; (3) *durable execution and managed runtime* (Temporal or DBOS; AgentCore Runtime, Foundry Hosted Agents or Agent Engine) beneath both.
- Use-case classification ("is the sequence known in advance?") happens before any framework choice (L3 §3.9 step 0). Most regulated asset-management "agents" are workflows with one judgement step.
- Model-vendor harnesses (OpenAI Agents SDK, Claude Agent SDK) appear only inside concern (2), as replaceable nodes, with a model-agnostic equivalent kept available.

## H3: An agent identity, authorisation and tool-governance sub-layer

**Hypothesis.** Tools and protocols need an explicit agent identity, authorisation and tool-governance sub-layer (plan §4) [AJ].

**Evidence.**
- *The protocol leaves room for governance but does not supply it.* MCP 2026-07-28 puts method and tool names in headers for gateways and deprecates Dynamic Client Registration, but authorisation remains optional and tool annotations remain hints [VF: A3-S015, A3-S057, A3-S055, A3-S020]. MCP's own roadmap says today's model assumes a person approving access in a browser, and names agent identity (DPoP, Workload Identity Federation) as a priority [VF: A3-S016].
- *A2A leaves the same gap.* Agent Card signing is optional and delegated-authority semantics are undefined [VF: A3-S078].
- *The building blocks are GA.* Entra Agent ID, Auth0 and Okta for AI Agents, Okta Agent SSO (which Okta states is the MCP Enterprise-Managed Authorization extension), Cedar-based AgentCore Policy, and graduated SPIFFE/SPIRE and OPA [VF: V2-S032, A6-S097, A6-S100, V2-S035, A6-S026, A6-S087, A6-S046]. Vault's agentic IAM enforces request-scoped, on-behalf-of authority [VF: A7-S034].
- *Gateways implement tool governance today.* Kong offers MCP access controls and token exchange, LiteLLM filters tools per key, and Azure API Management brokers OAuth for MCP servers [VF: A6-S016, A6-S017, A6-S015, A6-S053]. AgentCore Gateway, Identity and Policy implement the whole sub-layer as a managed service [VF: A3-S047, A6-S026].
- *There is no trustworthy public allow-list.* The official MCP Registry is preview at API v0.1 and moderates by denylisting; enterprises build private registries in GitHub and Azure API Center [VF: A3-S019, A3-S042, A3-S043, A3-S044].
- *The threat lists name the gap.* OWASP's agentic list includes ASI02 Tool Misuse and ASI03 Identity and Privilege Abuse [VF: B-C4-S005], and the Composio incident shows the cost of a third party holding every user's tokens [VF: B-L4-S007].

**Counter-evidence.** The products that implement the sub-layer are the C1 gateways and C4 identity services, not new L4 products, so a separate box could duplicate them [AJ]. The control also spans the identity provider, the gateway, the tool servers and the secrets broker, which argues for a control-plane component rather than a sub-layer (C4 §C4.13) [AJ].

**Verdict: keep, implemented as a split [AJ].** The two section views are both right about different things. The *enforcement point* must sit physically between L3 and the tools, so that no tool is reachable except through it; the *decisions* (who the agent is, on whose behalf it acts, which policy applies, which credential is issued) belong to the control plane [AJ].

**Resulting architecture change [Rec].**
- L4 is renamed **"Tools and connectivity"** and gains a mandatory **tool-governance sub-layer**: the tool gateway (usually the C1 product's MCP endpoint), the private allow-listed registry, hash-pinned tool definitions, the policy enforcement point and the per-call audit event.
- C4 (identity and authorisation) and C7 (secrets and credentials) are designed as **one identity-and-credential plane**, drawn as two controls: C4 owns agent registration, delegation and policy (OPA or Cedar in Git); C7 owns credential issuance.
- MCP is the default agent-to-tool protocol, Strategic only behind this sub-layer (CP3). Its independent alternative is OpenAPI-described tools behind the same gateway; A2A is used only where cross-team or cross-vendor delegation is in scope.

## H4: Memory may not be separate from retrieval and data architecture

**Hypothesis.** Memory may not be separate from retrieval and data architecture; conversation, working, episodic, semantic, organisational and long-term memory should be distinguished from knowledge bases (plan §4) [AJ].

**Evidence.**
- *Memory products are retrieval stacks with an extraction step.* Mem0, Graphiti, Cognee, LangMem and Letta store memory in SQL, vector, graph, LangGraph-store or git-backed file stores, and recall with the same hybrid semantic, keyword and graph search as knowledge retrieval [VF: A3-S053, A3-S003, A3-S005, A3-S006, A3-S073, A3-S001, A3-S064].
- *Products are converging with RAG.* Supermemory combines RAG and memory in one query, and Cognee and Zep ingest documents and business data into the same graph as conversations [VF: A3-S064, A3-S005, A3-S003].
- *Platforms are absorbing memory.* AWS and Google ship memory inside their agent platforms; Anthropic's memory tool runs file operations on storage the developer controls; OpenAI persists conversation state through its Conversations API [VF: A3-S048, A3-S108, A3-S069, A3-S110].
- *The independent layer is thinning* (finding 7 in Part I) [VF: A3-S081, V1-S043, A3-S059, A3-S093, A3-S006].
- *The worked example needs no memory product.* Its "memory of terminology and the PM's edits" is a governed, versioned style artefact in Git or the prompt store (L5 §5.12) [AJ].

**Counter-evidence.** Memory has a write path that retrieval does not: extraction, consolidation, contradiction handling and decay [VF: A3-S109, A3-S003, A3-S064]. Its governance differs in kind, because it is written by an agent, is per subject and must be erasable per person [AJ]. Both hyperscalers chose to expose memory as a distinct service, not as a feature of their vector stores [VF: A3-S047, A3-S108].

**Verdict: merge [AJ].** Memory should not be a separate infrastructure layer [AJ]. The counter-evidence is about governance, not storage, so it justifies a logical component, not a layer [AJ].

**Resulting architecture change [Rec].**
- Physically, memory is stored in the firm's L6 stores; the layer is renamed **"Retrieval, knowledge and memory stores"** (see H5).
- Logically, a thin **L5 memory service** remains in the diagram, because it carries the controls unique to memory: the policy-gated write path, the subject index, retention and erasure "beyond use", and a memory snapshot ID per run.
- Organisational and procedural memory (style rules, glossaries) is not agent memory: it is a versioned artefact in C5, proposed by the agent and approved by a person.
- Memory is built last (Phase 6). Hyperscaler memory (AgentCore Memory, Memory Bank) is used only where the agent runtime already lives on that cloud.

## H5: "Vector database" should become "Retrieval / Knowledge Stores"

**Hypothesis.** The "vector database" layer should be renamed Retrieval / Knowledge Stores (plan §4) [AJ].

**Evidence.**
- *Hybrid is standard.* Lexical and vector retrieval with fusion ships in turbopuffer, Chroma Cloud, Milvus, Elasticsearch, MongoDB, Qdrant, Pinecone and Weaviate [VF: A2-S056, A2-S060, A2-S054, A2-S133, A2-S141, A2-S103, A2-S101, A2-S110]. A vector-only store such as S3 Vectors is positioned by its own vendor as a tier behind a search engine [VF: A2-S092, A2-S093].
- *General-purpose databases absorbed the feature.* PostgreSQL (pgvector), MongoDB including self-managed Community Edition, and Elasticsearch offer vector retrieval in platforms firms already run [VF: A2-S061, A2-S137, A2-S133].
- *Storage is moving to object stores.* S3 Vectors, Milvus 3.0 and turbopuffer keep durable vectors in object storage [VF: A2-S081, A2-S118, A2-S124].
- *Vendors reposition above the store.* Pinecone sells Nexus as a "knowledge engine for agents", and Elastic calls itself "the Search AI Company" [VF: A2-S073, A2-S023].

**Counter-evidence.** Dedicated engines still differentiate on filtered search, tenant isolation and scale [VF: A2-S103, A2-S124, A2-S117], so the category survives as one implementation option [AJ]. "Knowledge store" risks overlapping with memory and ingestion, because Nexus reaches into both [VF: A2-S073] [AJ].

**Verdict: rename [AJ].** The H4 merge extends the name.

**Resulting architecture change [Rec].**
- L6 becomes **"Retrieval, knowledge and memory stores"**, defined by responsibility: a derived, entitlement-filtered, rebuildable index over approved content, never the system of record.
- Four implementation options sit beneath it: vectors in the operational database (pgvector, MongoDB), search engines (Elasticsearch, OpenSearch), dedicated vector engines (Qdrant, Milvus; Pinecone or turbopuffer BYOC), and object-store tiers (S3 Vectors).
- Knowledge-engine products sit at the boundary with L8 and the memory service, and their compiled outputs are treated as disposable derived data.
- The defining duties are entitlement filtering inside the search, tenant isolation, rebuild-from-source tested twice a year, and erasure that reaches the index.

## H6: Embeddings and reranking form one retrieval-optimisation layer

**Hypothesis.** Embeddings and reranking form one retrieval-optimisation layer (plan §4) [AJ].

**Evidence.**
- *Vendors ship both.* Six of the seven verified model vendors offer an embedding model and a reranker; Google's reranker is a separate Vertex ranking API [VF: A2-S012, A2-S010, A2-S006, A2-S034, A2-S025, A2-S026, A2-S030, A2-S020, B-REV-S026]. Sentence Transformers covers both in one library [VF: A2-S029].
- *The two are evaluated and versioned together*, and changing the embedding model forces the whole corpus to be re-embedded (L7 §7.10) [AJ].
- *The compute is moving into the store.* MongoDB, Pinecone and Elastic host embedding and reranking natively [VF: A2-S141, A2-S101, A2-S133].
- *Configuration management needs the pins.* C5's release manifest pins the embedding and reranker versions and enforces the dual-index migration (C5 §C5.13) [AJ].

**Counter-evidence.** Store-hosted models blur the line between L6 and L7; MongoDB's native reranking and automated embedding are still preview and do not yet support Geography targeting [VF: A2-S141, A2-S142].

**Verdict: merge [AJ].** The layer should be defined by responsibility, not by where the compute runs [AJ].

**Resulting architecture change [Rec].**
- L7 becomes **"Retrieval optimisation"**: model choice by in-domain evaluation, version pinning, hybrid fusion policy, reranking and the retrieval evaluation gate, whether the models run as APIs, in the estate or inside the store.
- Embedding-model version is named explicitly as a governed configuration item in C5, because it is the one decision in this layer with a corpus-wide migration cost.
- A thin internal service (`embed`, `rerank`) keeps raw text and a `model_version` tag on every vector, and migrates by dual index behind an L9 regression gate.

## H7: Ingestion must include lineage, classification, PII/DLP, access-control metadata and incremental indexing

**Hypothesis.** Ingestion must include lineage, classification, PII detection/DLP, access-control metadata and incremental indexing (plan §4) [AJ].

**Evidence.**
- *Products cover only fragments.* Unstructured captures ACLs and reprocesses on permission change; Firecrawl redacts PII and offers ZDR; no L8 product emits lineage [VF: A1-S094, A1-S076, A1-S096].
- *The lineage standard lacks GenAI facets.* OpenLineage is the neutral standard with Airflow, Spark, dbt and Flink coverage, but has no GenAI-specific facets [VF: A7-S041, A7-S045, A7-S042]. Collibra integrates OpenLineage with an AI use-case register, the first verified bridge between AI governance and data lineage [VF: A7-S099, A7-S122].
- *DLP applies at ingestion as well as at run time.* Sensitive Data Protection de-identifies stores, Presidio is designed for pipelines, and Skyflow de-identifies before ingestion [VF: A6-S066, A6-S068, A6-S081].
- *Decisions made at ingestion cannot be undone downstream.* Once a document has gone to a third-party parser and been indexed without its ACL, no prompt-level control can repair it (L8 §8.11) [AJ].
- *Agents read documents, so ingestion is an attack path.* ASI01 Agent Goal Hijack can arrive through indirect injection in documents [VF: R-OWASP-AGENTIC, A8-S042] [AJ].

**Counter-evidence.** DLP is being absorbed into gateways and guardrails [VF: A6-S052, A6-S016, A6-S072, A6-S067], and runtime lineage for LLM calls lives in OpenTelemetry traces, not OpenLineage [AJ].

**Verdict: keep, with a scope change; runtime web access is repositioned to L4 [AJ].** The enterprise additions are not product features to buy but a control envelope to build around replaceable parsers [AJ].

**Resulting architecture change [Rec].**
- L8 becomes **"Ingestion and data preparation"**, with two sub-layers (web acquisition; document understanding) under a built **ingestion control envelope**: (1) an approved-source register as the single entry point; (2) an acquisition contract (content hash, source version, ACL snapshot, fail-closed "permission unavailable" state); (3) pre-parse classification and DLP through the C3 privacy service; (4) a parse manifest (engine, version, model ID, config hash); (5) a metadata envelope on every chunk, enforced as an index gate; (6) OpenLineage events with firm GenAI facets, plus incremental indexing on content hash and ACL digest, with tombstones propagated to L6 and caches.
- Policy comes from C3; evidence is consumed by C8. Build-time lineage (OpenLineage) and runtime lineage (OTel traces in L9) are joined in the evidence pack by index version and document IDs.
- An agent fetching web pages at run time is an L4 tool call, governed as such, not L8 ingestion.

## H8: Evaluation and observability are cross-cutting, not a downstream layer

**Hypothesis.** Evaluation and observability are cross-cutting, not a downstream layer (plan §4) [AJ].

**Evidence.**
- *The instrumentation standard spans the stack.* OTel GenAI conventions cover client inference, agents, tool execution, retrieval, evaluation and MCP, and evaluation results have their own event type [VF: A1-S061, A1-S059].
- *Tools couple CI to production.* Six of the original products document a CI evaluation path, and the platforms run evaluators over production traces [VF: A1-S108, A1-S106, A1-S067, A1-S068, A1-S065, A1-S109, A1-S072, A1-S073, A1-S046, A1-S099].
- *Vendors push the layer sideways* into gateways, prompt management, guardrails and security testing [VF: A1-S043, A1-S103, A1-S067, A1-S024]. Every prompt registry is part of an observability platform or adds evaluation of its own [VF: A7-S071, A7-S076, A7-S004, A7-S117].
- *Governance products consume evaluation evidence directly.* watsonx.governance Enforcement Tracking retrieves agent evaluation metrics against thresholds, and ValidMind logs tests to the governance record [VF: A7-S111, A7-S003, A7-S056].
- *Regulators converge on ongoing monitoring.* AI Act Articles 26 and 72, the PRA's AI roundtables under SS1/23, ESMA's "frequent ex-post output controls" and IOSCO's human-intervention indicator all require it [VF: R-EUAIA, A8-S016, A8-S017; R-PRA-SS123, A8-S009; R-INTL-AI-ASSETMGMT, A8-S059, A8-S058].
- *Red-teaming is both security and validation evidence* (C7 §C7.13) [VF: A7-S027, A1-S062] [AJ].

**Counter-evidence.** The OTel GenAI conventions are still at "Development" status and recently moved repository, so the shared plane is not yet stable [VF: A1-S058, A1-S060]. Independence is weakening at the tool level with OpenAI's announced acquisition of Promptfoo [VF: A1-S024, V2-S042].

**Verdict: reposition [AJ].** L9 is not the last box in the pipeline; it is the plane on which every other layer produces evidence [AJ].

**Resulting architecture change [Rec].**
- L9 is drawn as the **evaluation and observability plane**, alongside the control plane, with a firm-owned telemetry and evidence spine (OTel Collector with redaction, pinned semantic-convention version, Git-versioned datasets and scorers) and products as replaceable back ends.
- **L9 and C8 form one evidence plane with two owners**: L9 produces the evidence; C8 sets thresholds, approves and retains it in the firm-owned evidence store.
- The independence rule is architectural: two red-team tools, one independent of the model vendor under test; validators extend the suite rather than reuse the developers' tests unchanged.

---

# Part IV: Reference architecture

## IV.1 The revised layer model

The verdicts in Part III produce the model below. Layer numbers are kept for traceability to the original graphic and the 17 section chapters; the names change [AJ].

| # | Original name | Revised name | Change | Defining duty [AJ] |
|---|---|---|---|---|
| L9 | Evals and observability | **Evaluation and observability plane** | Repositioned (H8) | Produce evidence for every layer; one telemetry spine |
| L8 | Data extraction | **Ingestion and data preparation** | Scope extended (H7); runtime web access moved to L4 | Approved sources only; ACL, classification, manifest and lineage on every chunk |
| L7 | Embeddings; RAG re-rankers | **Retrieval optimisation** | Merged (H6) | Pinned embed and rerank versions; hybrid fusion; retrieval eval gate |
| L6 | Vector DBs | **Retrieval, knowledge and memory stores** | Renamed (H5); absorbs L5 (H4) | Derived, entitlement-filtered, rebuildable index |
| L5 | Memory | **Memory service** (logical component of L6) | Merged (H4) | Policy-gated writes, subject erasure, per-run snapshot |
| L4 | Tools and protocols | **Tools and connectivity**, with a **tool-governance sub-layer** | Kept and split (H3) | No tool reachable except through the governed gateway |
| L3 | Agent frameworks | **Orchestration: workflows and agents** | Split into three concerns (H2) | Deterministic by default; durable; approval gates |
| L2 | Inference | **Inference and model access** | Split (H1); routing moved to C1 | In-region model access; private route on vLLM where justified |
| L1 | LLMs | **Foundation-model portfolio** | Kept | Two mid-tier vendors, a small tier and an open-weight tier, all pinned |
| C1–C8 | (absent) | **Control plane** | Added | Firm-owned policy and evidence for every call |

The control plane has eight components. C1 is the AI traffic gateway (model, tool and agent calls); C2 guardrails; C3 the privacy service; C4 identity and authorisation; C5 the configuration of record; C6 AI FinOps; C7 AI security; C8 model risk, governance and the evidence store [AJ]. C4 and C7 are designed as one identity-and-credential plane, and L9 and C8 as one evidence plane with two owners (Part III) [AJ].

```text
+==================================================================================================+
| CONTROL PLANE                                                                                    |
|  C4 identity & authz <-> C7 secrets/credentials   C3 privacy service   C2 guardrail detectors     |
|  C5 configuration of record (Git manifest)        C6 FinOps (metering at C1, cost per task)       |
|  C1 AI TRAFFIC GATEWAY (model | MCP tools | A2A agents) -- two deployments, in region, fail closed|
|  C8 model risk & governance: inventory, validation, EVIDENCE STORE (immutable, keyed by trace ID)  |
+==================================================================================================+
      ^ policy, identity, config, guards               | evidence (traces, evals, approvals)
+-----|------------------------------------------------v-------------------------------------------+
| L9 EVALUATION & OBSERVABILITY PLANE: OTel Collector (redaction) -> platform of record; CI evals;  |
|    online evals; red-team (two tools, one vendor-independent); human-edit capture                |
+--------------------------------------------------------------------------------------------------+
| AGENT PLANE                                                                                      |
|  L3 ORCHESTRATION  [workflow graph (default)] [bounded agent step] [durable execution / runtime]  |
|  L4 TOOLS          [tool-governance sub-layer: registry, pinned defs, PEP, audit] -> tool servers |
|                    (read-only MCP / OpenAPI tools, sandbox, web search via egress proxy, A2A)     |
+--------------------------------------------------------------------------------------------------+
| KNOWLEDGE PLANE                                                                                  |
|  L8 INGESTION   source register -> acquire -> classify (C3) -> parse -> manifest -> envelope      |
|  L7 RETRIEVAL OPTIMISATION   embed (pinned) | hybrid fusion | rerank (pinned)                     |
|  L6 STORES      derived indexes (pgvector / search engine / vector engine / object tier)          |
|                 + L5 memory service (write gate, subject index, erasure, snapshots)               |
+--------------------------------------------------------------------------------------------------+
| MODEL PLANE                                                                                      |
|  L2 INFERENCE   model access (primary-cloud service, in region) | serving (vLLM; SGLang backup)   |
|                 | optimisation (llm-d / Dynamo; own-GPU estates only)                             |
|  L1 PORTFOLIO   mid tier vendor A | mid tier vendor B | small model | self-hosted open weights    |
+--------------------------------------------------------------------------------------------------+
```

## IV.2 One request traced end to end

The worked example (Part VI) traces the attribution-commentary agent in full. To show the generic path, this section traces a different, common request: a client-servicing analyst asks "What did our house view say about euro duration in Q3, and how is fund X positioned?" [AJ]. The request needs retrieval over approved research and one read-only tool call [AJ].

```text
 1  Analyst signs in (SSO, step-up if policy says) -------------------------------- C4
 2  Workflow "research-answer v7" starts; manifest pinned (prompt, models, index) - L3, C5
 3  Agent identity registered with sponsor; OBO token for analyst, minutes TTL ---- C4, C7
 4  Input guard: prompt-attack check; privacy service tokenises client names ------ C2, C3 (via C1)
 5  Retrieval: query -> embed (pinned) -> entitlement-filtered hybrid search ------ L7, L6
           -> rerank (pinned) -> chunks with doc ID, version, ACL, trust tier ---- L8 envelope
 6  Retrieved chunks screened for indirect injection ----------------------------- C2, C7
 7  Tool call get_fund_positioning(fund X) through tool gateway:
           allow-list + definition hash + OPA/Cedar decision + audit event ------- L4 sub-layer, C4
 8  Model call via gateway route "research-answer": in-region primary model,
           qualified fallback, budget check, request log ------------------------- C1, L2, L1, C6
 9  Output guards: PII re-check, numeric/citation grounding, denied topics ------- C2, C3
10  Online evaluation sampled; trace (OTel) to platform of record ---------------- L9
11  Answer shown with citations; re-identification only for the entitled analyst - C3, C4
12  Evidence record (trace ID, versions, documents, tool calls, guard verdicts,
           cost) written to the evidence store; inventory entry updated ---------- C8, C6
```

Three properties follow from the design rather than from any product. The model never sees a credential, a client identifier or a document the analyst is not entitled to; every step carries the same trace ID; and switching the primary model is a gateway configuration change re-qualified by the L9 suite [AJ].

## IV.3 Comparison and decision framework: the master "if X, choose Y" guide

This one-page guide consolidates the x.9 decision trees of all 17 sections. Each row is a decision a platform team will actually face; the section reference holds the full tree [Rec].

| # | If… | …choose | Not | Ref |
|---:|---|---|---|---|
| 1 | Any production model, MCP or agent traffic | One gateway of record, two deployments, fail closed; provider keys only in its vault | Applications calling vendor APIs directly | C1 |
| 2 | You already run Kong / Apigee / Azure APIM | That platform's AI gateway (Kong hybrid; Apigee hybrid; APIM policies in GA tiers, not the preview tier) | A second, separate API-gateway estate | C1 |
| 3 | No API-gateway standard, client data in UK/EU | LiteLLM self-hosted, Enterprise-licensed, pinned and signed (alt: agentgateway for MCP/A2A-led Kubernetes estates) | A SaaS gateway in the client-data path without verified log residency | C1 |
| 4 | Client, personal or confidential data in a model call | The primary cloud's model service in an approved UK/EU region (Bedrock geographic or in-Region, Foundry Data Zone or Regional, Gemini Enterprise Agent Platform regional endpoint) | Global endpoints; routers without contractual ZDR and residency; any Chinese-origin vendor's own API | L1, L2 |
| 5 | Choosing the mid-tier model | Two unrelated vendors, same region, both qualified on the same L9 suite | A single proprietary frontier vendor for an important business service | L1 |
| 6 | Claude appears in the shortlist | Hyperscaler EU/UK route only, with a non-Anthropic fallback (GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5) | The first-party API for client data (no first-party EU/UK inference) | L1 |
| 7 | Data must never leave the estate | Self-hosted Gemma 4 or Mistral (Medium 3.5 / Large 3) on vLLM; Chinese-origin weights only by explicit policy, without tool access | Pickle-format weights from public sources | L1, L2, C7 |
| 8 | Need a private open-weight route but no SRE capacity for GPUs | Private-VPC managed inference (Fireworks BYOC or EU dedicated, once ISO certificates are confirmed; Together EU dedicated; HF Endpoints with PrivateLink) | Own GPUs without monthly engine patching | L2 |
| 9 | Own GPUs | vLLM (supported distribution if needed); SGLang qualified as backup once CVE-2026-3059 is confirmed fixed; llm-d or Dynamo only as a non-production pilot | An optimisation layer before a single engine is stable | L2 |
| 10 | Process steps are known in advance | Deterministic workflow graph, autonomy budget 0 or 1 | An autonomous agent loop | L3 |
| 11 | Python or TypeScript back end, no hyperscaler runtime preference | LangGraph (Pydantic AI for typed agent steps; Temporal or DBOS for durability) | A firm abstraction layer over frameworks | L3 |
| 12 | Microsoft / .NET estate | Microsoft Agent Framework (Workflows for the process) on Foundry Hosted Agents | New AutoGen or Semantic Kernel code | L3 |
| 13 | AWS or Google Cloud is the primary cloud and its runtime is wanted | Strands on AgentCore Runtime; ADK on Agent Engine | Mixing runtimes across clouds for one use case | L3 |
| 14 | An autonomous sub-task is unavoidable | One sandboxed node with read-only tools, traces to the firm's collector; a model-vendor harness (OpenAI Agents SDK; Claude Agent SDK, Experimental) only inside it | Vendor-hosted agent state for regulated workflows | L3 |
| 15 | Agent needs an internal system of record | A read-only MCP server (or OpenAPI tool) owned by that system's team | Write tools in a drafting agent | L4 |
| 16 | Agent acts for a user in a SaaS app | Per-user delegated OAuth via EMA or token exchange; vault in the firm's estate | A multi-tenant token broker holding every user's tokens | L4, C4 |
| 17 | Public web search | Search API through an egress proxy with DLP and ZDR, non-confidential queries only (Exa or Tavily) | Any query carrying client, holdings or deal context | L4 |
| 18 | Generated code must run | microVM sandbox, default-deny egress, no standing secrets (E2B BYOC or EU region) | Running code in the agent's own container | L4, C7 |
| 19 | Agent-to-agent delegation across teams or vendors | A2A 1.0 with signed Agent Cards, through a gateway that understands A2A | A2A where a workflow could call tools instead | L4 |
| 20 | Corpus is already in PostgreSQL / Elastic / MongoDB | Vectors in that platform (pgvector; Elasticsearch hybrid with document-level security; MongoDB Vector Search) | A new dedicated vector database | L6 |
| 21 | Load test fails on filtered latency, tenant isolation or scale | Qdrant or Milvus (self-hosted or BYOC); Pinecone BYOC where a managed proprietary store is acceptable | A dedicated engine adopted without the load test | L6 |
| 22 | Exact identifiers matter (ISINs, fund codes) | Hybrid first stage (BM25 + dense, fused) before rerank | Dense-only retrieval | L6, L7 |
| 23 | Choosing an embedding model | In-domain bake-off on 100–300 labelled queries; pin the version; keep raw text | Vendor benchmark claims | L7 |
| 24 | Embedding must stay in the estate | Sentence Transformers serving an Apache-2.0 model; Cohere private deployment where vendor support is needed | Jina CC-BY-NC weights self-hosted without a licence | L7 |
| 25 | Ingesting enterprise documents | Docling (default engine) and Unstructured ingest connectors for ACL capture, inside the built control envelope | Indexing a document whose permission fetch failed | L8 |
| 26 | Tables feed numbers anyone will quote | Dual-parse and reconcile; parsed numbers stay non-authoritative | Parsed figures as a data source | L8 |
| 27 | Long-term memory requested | First ask whether session state plus retrieval suffices; organisational memory goes to C5 | A memory SaaS holding client conversation data by default | L5 |
| 28 | Platform of record for traces and evals | Langfuse self-hosted (Enterprise licence), MLflow where an ML platform exists, LangSmith for LangGraph estates | Evaluation datasets held only in a vendor UI | L9 |
| 29 | Red-teaming a system that uses an OpenAI model | Promptfoo plus a second, vendor-independent tool | One vendor-owned red-team tool | L9, C7 |
| 30 | Guardrails | Deterministic business invariants first (in-house), then the primary cloud's managed detector (Bedrock Guardrails, Azure AI Content Safety, Model Armor) or NeMo Guardrails orchestrating two independent detectors | A model-based judge as the sole check on numbers | C2 |
| 31 | Sensitive data in prompts | Presidio in-estate behind the firm's privacy-service API (Google Sensitive Data Protection on Google Cloud) | A different detector per layer | C3 |
| 32 | Reversible pseudonymisation at scale | Keys in the firm's KMS/HSM; a vault vendor (Protegrity, Skyflow) only with tested bulk detokenisation on exit | A vendor-held token map without an exit test | C3 |
| 33 | Registering agents | The workforce IdP that holds the humans (Entra Agent ID or Okta for AI Agents), with a named sponsor | Shared service accounts or developer tokens | C4 |
| 34 | Policy decision point for tool calls | OPA at the gateway; Cedar where AgentCore Gateway is used | Policy held only in a vendor console | C4 |
| 35 | Prompts and configuration | Git as system of record; registry only for run-time delivery; flags only between approved variants | Editing production prompts in a registry UI | C5 |
| 36 | Cost management | Gateway virtual keys per use case; FOCUS-shaped firm dataset; cost per approved task | Buying a FinOps tool for AI alone; Helicone | C6 |
| 37 | Runtime AI-security detector | A swappable detector behind the gateway from the existing security supplier, or HiddenLayer as the independent specialist | A security platform bundled with the gateway without an exit plan | C7 |
| 38 | Secrets for agents | Vault (Enterprise agentic IAM) in multi-cloud estates; the cloud's native service plus workload identity otherwise | Credentials in prompts, context, memory or traces | C7 |
| 39 | Governance workflow tool | Own the inventory schema and evidence store first; then ValidMind (MRM-led), watsonx.governance (IBM estates), Collibra (catalogue of record) or Credo AI (policy-led) | A vendor policy pack presented as proof of compliance | C8 |
| 40 | Lineage | OpenLineage with firm GenAI facets for build-time; OTel traces for run time | A proprietary lineage store as the only record | C8, L8 |

---

# Part V: Financial-services point of view (consolidated)

Every section carries its own regulated-FS lens (x.11). This part consolidates them into one view per instrument: what the instrument says, what it means for the architecture, and the evidence a firm must be able to produce [AJ]. The binding framing is that SR 26-2 supersedes SR 11-7 and excludes GenAI and agentic AI; that PRA SS1/23 and the EU AI Act are the anchors; that DORA and the UK CTP regime designate hyperscalers, not model vendors; and that PS7/26 and PS26/2 apply from 18 March 2027 (CP1, brief rule 4) [AJ].

## V.1 Model risk: SR 26-2, PRA SS1/23 and the definition of a "model"

**What the instruments say.**
- *SR 26-2.* SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026 were issued on 17 April 2026 and supersede SR 11-7 and SR 21-8 [VF: R-US-MRM, A8-S001, A8-S002, A8-S005, V2-S049]. They are supervisory guidance, expected to be most relevant to banking organisations with more than US$30bn in total assets [VF: R-US-MRM, A8-S002, A8-S003]. They keep risk-based, materiality-driven MRM with effective challenge by independent reviewers [VF: R-US-MRM, A8-S001, A8-S002]. Generative and agentic AI models are expressly out of scope; for those, the firm's own risk-management practices determine controls [VF: R-US-MRM, A8-S001, A8-S002]. The agencies' planned request for information on MRM and AI had not been published by 7 October 2026 [VF: R-US-MRM, R-US-AGENCY-AI, A8-S003, A8-S007].
- *PRA SS1/23.* SS1/23 took effect on 17 May 2024 and applies to banks, building societies and PRA-designated investment firms with internal-model approval; insurers are not covered, and the PRA later narrowed its expectations to internal-model firms [VF: R-PRA-SS123, A8-S008, A8-S061]. It sets five principles (identification and classification with a complete inventory including AI/ML; governance with an SMF holder; development, implementation and use; independent validation; risk mitigants), covers vendor models and is technology-agnostic [VF: R-PRA-SS123, A8-S008, A8-S037]. Principle 1.1(b) lets firms apply MRM disciplines to material, complex deterministic quantitative methods that are not models [VF: R-PRA-SS123, A8-S061]. Members of the Bank of England's AI Consortium report that GenAI is "often classified as high risk" under SS1/23-type frameworks [VF: R-PRA-SS123, A8-S010].
- *UK supervision.* The FCA has made no new AI-specific rules and relies on Consumer Duty and SM&CR [VF: R-UK-AI-STATEMENTS, A8-S055]. The FPC judged in March 2026 that GenAI and agentic AI did not yet present systemic risk, but that the risks are likely to increase, potentially rapidly [VF: R-UK-AI-STATEMENTS, A8-S056].

**What it means for the architecture [AJ].**
- The US carve-out does not remove the governance need; it moves the burden to the firm. A US bank-owned manager has no supervisory template for LLM agents and must write its own standard. Writing it to SS1/23 quality is the defensible course everywhere, because the planned RFI may reintroduce expectations.
- A foundation model is a model by construction; an agent is a system that contains a model; where an LLM transforms or explains quantitative estimates, as in attribution commentary, it should be governed as in scope. SS1/23 Principle 1.1(b) is the cleanest UK hook for governing the whole agent, not only the LLM inside it (C8 §C8.11).
- **The governed unit is the use case**, with the foundation model recorded as a vendor-model component and a **version bundle** (model and fallback versions, prompt template, retrieval index and embedding model, tool list and scopes, guardrail configuration, eval-suite and judge versions). This works under all three regimes.
- **Every bundle change is a model change**: a provider's silent update or fallback (C1), a quantisation change (L2), an embedding or reranker swap (L7), a new tool (L4), a prompt edit (C5) or a cost optimisation (C6) all trigger the L9 regression suite, and material ones trigger re-validation.
- **The eval suite is most of the validation evidence**, but only if someone independent challenges and extends it, it is versioned with its results, and it is retained beyond any vendor tier.

**Evidence a firm must produce [Rec].** A firm GenAI model-risk standard (scope, tiers, validation depth, change triggers, evidence pack, retention); an inventory entry per use case with materiality tier, version bundle and named SMF; independent validation reports with use limitations; ongoing monitoring against thresholds; effective-challenge records; quarterly attestation for tier-1 uses.

## V.2 EU AI Act

**What it says.**
- *Timeline.* Prohibitions and AI literacy have applied since 2 February 2025; GPAI obligations since 2 August 2025, with Commission enforcement powers (fines up to 3% of global turnover) from 2 August 2026; GPAI models placed on the market before 2 August 2025 must comply by 2 August 2027 [VF: R-EUAIA, A8-S011, A8-S019]. Regulation (EU) 2026/1744, in force 27 July 2026, moved Annex III high-risk obligations to 2 December 2027 and Annex I to 2 August 2028, leaving GPAI, prohibitions and general transparency timelines unchanged [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011, V2-S050].
- *Deployers.* Article 26 requires deployers of high-risk systems to use them per instructions, assign competent human oversight, use relevant and representative input data where they control it, keep logs for at least six months (within financial-services documentation for financial institutions), monitor operation and report serious incidents [VF: R-EUAIA, A8-S016]. Article 4 now requires providers and deployers to "take measures to support" AI literacy [VF: R-EUAIA, A8-S060]. Article 50 transparency has applied since 2 August 2026, with until 2 December 2026 for the Article 50(2) marking duty on generative systems already on the market [VF: R-EUAIA, A8-S018, V2-S078].
- *Becoming a provider.* Under Article 25 a deployer becomes a provider if it substantially modifies a high-risk system or changes an AI system's intended purpose so that it becomes high-risk [VF: R-EUAIA, A8-S016]. Annex III points relevant to financial services are employment (4(a), 4(b)), creditworthiness (5(b)) and life and health insurance pricing (5(c)) [VF: R-EUAIA, A8-S017].
- *GPAI Code of Practice.* Signatories include Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI and OpenAI; xAI signed only the Safety and Security chapter [VF: R-EU-GPAI-COP, A8-S015, A8-S035]. The status of Meta, DeepSeek, Alibaba, Moonshot and Z.ai was not verified [NPV].

**What it means [AJ].** An asset manager using third-party LLMs is normally a deployer, and attribution commentary, research summaries and operations are not Annex III uses. The live duties are literacy, Article 50 where content is published, prohibitions, and vendor documentation under Article 53. HR uses and any credit or life and health insurance pricing would be high-risk from 2 December 2027. A system prompt is where intended purpose is most easily changed, so purpose-changing configuration edits must route to the inventory owner (C5). Build Article 26-grade logging, oversight and monitoring for every use case anyway: the same artefacts serve SS1/23, outsourcing and audit, and they are cheap to build once and expensive to retrofit.

**Evidence [Rec].** An AI inventory with risk classification per use case (prohibited, high-risk, Article 50, minimal); AI literacy records; Article 50 disclosures and marking evidence; for any high-risk use, human-oversight assignments, logs of at least six months, monitoring and incident records, and a fundamental rights impact assessment for 5(b) and 5(c); each GPAI vendor's Code of Practice status and Model Documentation Form.

## V.3 DORA, the UK CTP regime, PS7/26 and outsourcing

**What they say.**
- *DORA.* DORA has applied since 17 January 2025; it requires an ICT risk framework extending to third parties, incident classification and reporting, resilience testing, and a register of information for all ICT third-party arrangements with Article 30 contract terms [VF: R-DORA, A8-S021, A8-S025]. Registers are reported annually by 31 March from 2026 [VF: R-DORA, A8-S021]. The first CTPP list (18 November 2025, 19 providers) includes AWS, Google Cloud and Microsoft entities and no AI model provider [VF: R-DORA, A8-S020, A8-S021, V2-S051].
- *UK CTP regime.* AWS, Google Cloud, Microsoft and Oracle were designated as critical third parties with effect from 13 July 2026; no AI model provider is designated, and firms keep their own due-diligence and contingency duties [VF: R-UK-CTP, A8-S023, A8-S024, V2-S052].
- *PRA PS7/26 and FCA PS26/2.* From 18 March 2027, firms must notify before entering into or significantly changing a material third-party arrangement and submit an annual register [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062, V2-S053]. SS2/21 expects documented and tested exit plans, including stressed exit [VF: R-PRA-SS221, A8-S048]. Under SYSC 8 senior management cannot delegate responsibility through outsourcing, and FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049].
- *EBA.* EBA/GL/2026/09 on non-ICT third-party risk was finalised on 18 September 2026 and will replace the 2019 outsourcing guidelines from a date not yet fixed [VF: R-EBA-OUTSOURCING, A8-S050, V2-S054].
- *US.* The interagency third-party guidance names lifecycle risk management, including ongoing monitoring and termination [R: R-US-TPRM, A8-S033].

**What it means [AJ].**
- **Consuming a model through the primary hyperscaler places it inside an already-overseen, already-contracted relationship**; a direct contract with a model vendor, inference cloud, router or tooling start-up does not, and leaves oversight with the firm. This is the strongest regulatory argument for the hyperscaler model service as the default access route.
- **Every SaaS in the stack is an ICT third-party arrangement**: model APIs, gateway SaaS, trace stores, vector stores, parsers, search APIs, memory services, guardrail and detector services, governance tools. Each needs a register entry and, where it supports a critical or important function, Article 30 terms and an exit plan.
- **The gateway (C1), portable prompts and configuration (C5) and the evaluation suite (L9) are the exit route.** An exit plan that has never been drilled through the gateway is not tested. The credible stressed exit is an open-weight model already qualified on vLLM, switched by configuration.
- **Ownership changes are third-party events.** Langfuse, Arize, Promptfoo, Portkey, Tavily, OpenRouter and trail ML all changed or are changing owner [VF: A1-S021, A1-S045, A1-S024, A6-S011, V1-S041, V1-S059, A7-S101], and from 18 March 2027 a significant change to a material arrangement needs notification lead time.
- **Hyperscaler concentration is real.** Many specialist stores and tools run on the same three clouds, so their outages correlate with the cloud's; record the underlying cloud for every service (L6 §6.11).

**Evidence [Rec].** A register entry per AI-related ICT provider; materiality and MTP assessments; Article 30-compliant contracts with audit, sub-outsourcing and termination rights; documented and drilled exit plans with measured switch and rebuild times; MTP notifications and the annual register from 18 March 2027; AI incidents classified under the DORA and FCA incident schemes.

## V.4 Data residency and transfers

**What applies.** UK GDPR as amended by the Data (Use and Access) Act 2025 is in force, including changes to third-country transfers and automated decision-making [VF: R-DATA-TRANSFERS, A8-S051, V2-S076]. EU-to-UK transfers can rely on adequacy until 27 December 2031 [VF: R-DATA-TRANSFERS, A8-S052, V2-S055]. EU-to-US transfers rely on the Data Privacy Framework or SCCs, and the appeal C-703/25 P against the General Court's judgment was pending on 7 October 2026 [VF: R-DATA-TRANSFERS, A8-S053, V2-S059]. Erasure must reach live systems and put backups "beyond use" [VF: B-L5-S005].

**What the evidence shows about processing location.**
- Storage residency and processing residency are different promises: Foundry Global deployments may process prompts anywhere while storing data in the chosen geography; Bedrock geographic profiles move prompts between Regions in the geography; Google's global endpoint gives no residency guarantee [VF: B-L2-S006, B-L2-S005, B-L2-S008].
- OpenAI's UK endpoint stores data in the UK but does not process there [VF: V2-S079]. Anthropic offers no first-party EU or UK inference; EU processing for Claude is available through Google Cloud and Bedrock regional endpoints [VF: A5-S013, V2-S075, A5-S027]. Mistral hosts data in the EU by default and commits inference location on its EU endpoint [VF: A5-S075].
- London-originated Bedrock requests can route to EU Regions, so UK-only processing must be checked per model [VF: B-L2-S005]. Vertex default overflow can cross a residency boundary [VF: B-L2-S008].
- No hosted embedding API in L7 verified UK processing; Gemini Embedding's EU endpoint excludes the UK [VF: A2-S039].
- DeepSeek's own platform stores personal data in the PRC [VF: A5-S062].

**What it means [AJ].** Residency must be configured and evidenced for every copy: the model endpoint, the trace store, the vector store and its backups, the memory store, the guardrail and DLP services and the detectors. Embeddings derived from client documents inherit the classification of the text. The gateway is where processing region is pinned and evidenced per request; tokenisation before a US-hosted call reduces the personal data exposed to the DPF appeal risk.

**Evidence [Rec].** A transfer mechanism and transfer risk assessment per AI vendor; records of processing listing LLM vendors as processors; configuration evidence of processing location per call (for example Bedrock's CloudTrail inference-Region field [VF: B-L2-S005]); erasure runbooks covering memory, vectors, traces, evaluation sets and caches.

## V.5 Auditability and reproducibility

**What "complete" means.** The plan's definition is a complete trace of prompt, model version, data, tool calls, approvals and outputs, with reproducibility and retention (plan §10) [AJ]. Because an LLM may not reproduce the same text twice, reproducibility means **re-performance of the evidence**: the original inputs, output and check results are retained, a re-run on the pinned model passes the same thresholds while that version is available, and after retirement the firm shows the retained evidence plus the re-qualification of the replacement on the same suite (C8 §C8.12) [AJ]. Retention follows the firm's records policy, not a vendor tier: free tiers keep data for 15 days (Arize AX), 30 days (Langfuse Hobby) and 60 days (Opik) [VF: A1-S047, A1-S031, A1-S123]. For US broker-dealers, SEC Rule 17a-4(f)(2) allows a complete time-stamped audit-trail alternative to WORM storage, on a vendor summary [R: A8-S034].

**Evidence [Rec].** The per-output evidence pack (Part VI.4), written automatically to the firm's immutable archive at approval and keyed by trace ID.

## V.6 Concentration risk

IOSCO's Supervisory Toolkit (FR/02/2026) flags concentration risk from reliance on a few AI technology providers, names the "level and frequency of human intervention" as an indicator, and records AI-washing at asset managers [VF: R-INTL-AI-ASSETMGMT, A8-S058, V2-S077]. Concentration now appears in four forms [AJ]:

| Form | Example evidence | Architectural answer [Rec] |
|---|---|---|
| One model vendor | Fable 5 was suspended 12 June – 1 July 2026 [VF: V2-S004]; Flash versions live about five to six months [VF: B-L1-S003] | Two-vendor mid tier, both qualified; open-weight exit route |
| One cloud | The model, gateway, guardrail, DLP and memory services of a cloud all sit under one designated provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023] | Accept consciously for the primary cloud; keep a second route for important services |
| One vendor across adjacent layers | Database companies own Voyage and Jina [VF: A2-S033, A2-S023]; Palo Alto Networks supplies AI runtime security, model scanning and an AI gateway [VF: A7-S014, A7-S016, A7-S028]; IBM owns Vault and sells watsonx.governance [VF: A7-S032, A7-S058] | Keep the gateway choice separate from the detector choice; record bundles in the exit plan |
| Governance of open standards | Both MCP Lead Maintainers are Anthropic staff and Agent Skills is Anthropic-maintained [VF: A3-S082, A3-S115] | A firm using Claude models should note that one vendor then influences the model, the tool protocol and the skills format; this author is an Anthropic model and the point applies in full [AJ] |

## V.7 Standards: NIST, ISO/IEC 42001/42005/42006, OWASP 2026

- *NIST.* AI RMF 1.0 (26 January 2023) is under revision with no revised version published by 7 October 2026, and AI 600-1, the Generative AI Profile, was released on 26 July 2024 [VF: R-NIST-AIRMF, A8-S043, A8-S044, V2-S060]. Agent-specific work includes the NCCoE concept paper on AI agent identity and authorisation (February 2026) and a planned SP 800-53 control overlay for AI agent systems [VF: R-NIST-AIRMF, A8-S006]. NIST pages now use "Super Intelligence" terminology, so documents should be cited by their published titles [VF: R-NIST-AIRMF, V2-S060]. Use AI RMF and AI 600-1 as the neutral control taxonomy for C8 and L9 [Rec].
- *ISO.* ISO/IEC 42001:2023 sets requirements for an AI management system; 42005:2025 gives guidance on AI system impact assessments; 42006:2025 sets requirements for bodies certifying against 42001 [VF: R-ISO-42001, A8-S045, A8-S046, A8-S047, V2-S057]. 42001 is the management-system wrapper for the whole control plane, 42005 a usable template for Article 27-style assessments, and 42006 makes vendor certificates more comparable [AJ]. Check certificate scope, not the logo: OpenAI's 42001 scope wording does not name the API Platform [VF: A5-S007, V2-S062] [Rec].
- *OWASP.* The Top 10 for LLM Applications 2026 was released in August–September 2026, and its full list was not retrieved [VF: R-OWASP-LLM, V2-S056]; Excessive Agency is reported as ranked third [R: A8-S041]. The Top 10 for Agentic Applications for 2026 starts with ASI01 Agent Goal Hijack and includes ASI02 Tool Misuse, ASI03 Identity and Privilege Abuse, ASI04 Agentic Supply Chain, ASI05 Unexpected Code Execution, ASI06 Memory and Context Poisoning and ASI07 Insecure Inter-Agent Communication [VF: R-OWASP-AGENTIC, A8-S042, B-C4-S005]. Map red-team and threat-model evidence to both 2026 lists and keep the 2025 identifiers (for example LLM08 Vector and Embedding Weaknesses) for traceability [Rec].
- *ESMA.* ESMA expects ex-ante input controls, frequent ex-post output controls and due diligence on third-party AI, and holds management bodies responsible for decisions taken by AI tools [VF: R-INTL-AI-ASSETMGMT, A8-S059]. In this architecture the ex-ante controls are the approved-source register, entitlement filtering, input guardrails and pinned configuration; the ex-post controls are output guardrails, online evaluation and the human approval gate [AJ].
- *SEC.* The SEC's predictive data analytics proposal was withdrawn on 12 June 2025 [VF: R-SEC-ADVISERS, A8-S057, V2-S058].

## V.8 The consolidated evidence register

The table maps each evidence artefact to the component that produces it and the regimes it serves [AJ]. It is the specification for the C8 evidence store.

| Artefact | Produced by | SS1/23 / firm standard | EU AI Act | DORA / PS7/26 / SYSC 8 | Data protection | IOSCO / ESMA |
|---|---|---|---|---|---|---|
| Use-case inventory entry with version bundle, tier, SMF | C8, C5 | ✓ | ✓ (classification) | | | ✓ (board accountability) |
| Independent validation report and challenge set | C8, L9 | ✓ | | | | ✓ (model testing) |
| Regression suite, results, judge calibration | L9 | ✓ | ✓ (monitoring) | ✓ (exit re-qualification) | | ✓ |
| Gateway request log (model, version, region, fallback) | C1 | ✓ | ✓ (Art. 26 logs) | ✓ (exit drills) | ✓ (location) | |
| Trace with tool calls, retrieved document IDs | L9, L4, L6 | ✓ | ✓ | | | ✓ (ex-post) |
| Approval record with approver identity and edit diff | L3, C4 | ✓ | ✓ (oversight) | | | ✓ (human intervention) |
| Guardrail and detector decisions, overrides | C2, C7 | ✓ (mitigants) | ✓ | ✓ (incidents) | | ✓ (ex-ante/ex-post) |
| Privacy-service policy, recall tests, re-identification log | C3 | | | | ✓ | |
| Configuration release manifest and pull-request approvals | C5 | ✓ (change control) | ✓ (Art. 25 purpose) | | | |
| Register entry, contract, exit plan, MTP notification | C8 (third-party risk) | | | ✓ | ✓ (transfers) | ✓ (due diligence) |
| Cost per task, provider concentration | C6 | | | ✓ (materiality) | | ✓ (concentration) |
| Red-team results mapped to OWASP 2026 | C7, L9 | ✓ | | ✓ (testing) | | |
| Build-time lineage (OpenLineage) and parse manifests | L8, C8 | ✓ | ✓ (input data) | | ✓ (erasure) | |
| AI-claims substantiation | C8 | | ✓ (Art. 50) | | | ✓ (AI-washing) |

---

# Part VI: Worked example — the performance-attribution commentary agent, end to end

**The use case.** An agent drafts the monthly performance-attribution commentary for a generic multi-asset fund: Brinson-style allocation and selection effects, currency, and benchmark-relative return. A portfolio manager reviews and approves every draft before release (plan §11) [AJ]. The example is generic, illustrative and cloud-neutral: each component is named once in cloud-neutral form, with AWS, Azure and Google Cloud equivalents side by side (CP4-6) [AJ].

**The architectural reading in one paragraph.** This is a deterministic workflow, not a free agent. Every number comes from the attribution engine through a read-only tool; the model's only job is to write narrative around figures it is given; a deterministic check proves every figure in the draft matches the engine; and a named human approves. The LLM is therefore governed as a model-dependent use case under the firm's standard, and the use case is not Annex III [AJ].

## VI.1 Request trace, rebuilt with the recommended components

```text
 0  RELEASE MANIFEST "commentary-release 2026.10" pinned (C5): prompt set v14, drafting model@date
    (temperature 0), fallback model@date, embedding + reranker versions = index model_version tag,
    top-k 8, tool list (read-only), guardrail policy v6, eval threshold set v3      [illustrative]
 1  Analyst signs in through SSO; workflow started for fund X, period 2026-09 ........ C4
 2  Agent identity (registered, sponsor = head of performance reporting) obtains an OBO
    token: audience = attribution MCP server, scope attribution.read, TTL minutes .... C4, C7
 3  L3 WORKFLOW GRAPH (durable; graph version recorded):
    3a get_attribution_results(fund X, 2026-09, model v) via TOOL GATEWAY
       -> allow-list + definition hash + policy (fund within analyst entitlements)
       -> snapshot ID + hash recorded as a durable activity ........................ L4, C4, L3
    3b get_fund_reference_data (benchmark, share classes; no client identifiers) ..... L4
    3c search_approved_commentary: embed (pinned) -> entitlement-filtered hybrid search
       over prior approved commentaries, style guide, approved market notes -> rerank -> L7, L6
       chunks carry doc ID, version, ACL, trust tier, parse manifest ................ L8
    3d retrieved chunks screened for indirect injection; flagged chunk dropped + logged C2, C7
    3e client identifiers tokenised (segregated mandates) ........................... C3
    3f ONE LLM DRAFTING STEP via gateway route attribution-commentary-draft:
       in-region primary model; qualified different-vendor fallback; budget + per-run
       ceiling; fail closed if both unavailable .................................... C1, L2, L1, C6
    3g OUTPUT GUARDS: deterministic numeric comparator (every figure, sign, direction
       word vs snapshot); PII re-check; placeholders unchanged; denied topics
       (forecasts, advice); narrative grounding flags for reviewer ................... C2, C3
    3h EVAL GATE: numeric faithfulness 100% (blocking), groundedness, style, trajectory L9
       fail -> bounded retry edge to 3f (limit) or "returned for revision"; never approval
    3i APPROVAL INTERRUPT: named PM (not the requester, not the agent), step-up auth;
       decision, identity, edit diff, reason code recorded ........................... L3, C4
 4  Release service publishes using the approver's identity (outside the agent) ...... L3
 5  Evidence pack written to the immutable archive, keyed by trace ID ................ C8
 6  Edit diff feeds the human-intervention metric and proposed style rules (PR to C5) L9, C5
```

## VI.2 Per-layer slice (cloud-neutral, with AWS / Azure / Google Cloud equivalents)

| Layer / control | What it does for this agent [AJ] | Cloud-neutral component [Rec] | AWS | Azure | Google Cloud |
|---|---|---|---|---|---|
| L8 | Parse prior factsheets and commentaries; dual-parse tables and reconcile; register market-note licences | Docling self-hosted; Unstructured ingest pattern for ACL capture; built control envelope | Same, on the firm's AWS account (no AWS document service verified [NPV]) | Same, on Azure (no Azure document service verified [NPV]) | Docling, or Document AI where confirmed in region [VF: A1-S101] |
| L7 | Hybrid retrieval of comparable commentary; rerank by fund, period and theme | Sentence Transformers model or Cohere private deployment, pinned; in-domain bake-off | Cohere or Voyage on SageMaker [VF: A2-S012, A2-S044] | Cohere on Microsoft Foundry [VF: A2-S012] | Gemini Embedding 2, EU endpoint (excludes UK) [VF: A2-S004, A2-S039] |
| L6 | One store, three collections; entitlement filter inside the search; hard empty result; retention per chunk | pgvector on managed PostgreSQL, schema per segregated mandate; Elasticsearch if already operated | pgvector on RDS or Aurora [VF: B-L6-S004] | pgvector on Azure Database for PostgreSQL [VF: B-L6-S005] | pgvector on Cloud SQL [VF: B-L6-S005] |
| L5 | Versioned style memory (glossary, approved style rules), recalled by version hash | No memory product: Git or the prompt store (C5) plus L6 retrieval | AgentCore Memory only if later needed [VF: V1-S087] | No Azure memory service profiled [NPV] | Memory Bank only if later needed [VF: V1-S088] |
| L4 | Read-only tools onto the attribution engine and fund reference data; sandbox for derived figures | Read-only MCP servers owned by the engine team (alt: OpenAPI tools); E2B-style microVM sandbox, no egress | AgentCore Gateway + Identity [VF: A3-S047, A6-S026] | APIM AI gateway + API Center private registry [VF: A6-S053, A3-S044] | Apigee MCP support [VF: A6-S023] |
| L3 | Pinned graph; one drafting step; eval gate as a hard edge; approval interrupt; durable resume reuses the same snapshot | LangGraph with a firm-controlled Postgres checkpointer, or Temporal activities | Strands on AgentCore Runtime [VF: A4-S116, B-L3-S004] | Microsoft Agent Framework Workflows on Foundry Hosted Agents [VF: A4-S066, B-L3-S006] | ADK 2.0 Workflow Runtime on Agent Engine [VF: A4-S114] |
| L2 | In-region managed endpoint; reserved capacity for month-end; qualified fallback; vLLM stressed-exit route | Primary cloud's model service; vLLM private route for one open-weight model | Bedrock geographic or in-Region profile [VF: B-L2-S005] | Foundry Data Zone or Regional deployment, PTUs [VF: B-L2-S006] | Regional endpoint, Provisioned Throughput with overflow pinned [VF: B-L2-S008] |
| L1 | Primary drafting model, different-vendor fallback, small classifier, self-hosted open-weight model | Two-vendor mid tier; Gemma 4 or Mistral Medium 3.5 self-hosted | Claude Sonnet 5.5 primary, a GPT-6 tier or Mistral fallback (independent alternative to Claude named) | GPT-6.1 Sol primary, Mistral Medium 3.5 fallback | Gemini 3.8 Flash primary, Claude Sonnet 5.5 via Google Cloud EU fallback |
| L9 | Numeric faithfulness, groundedness, style, trajectory; regression suite of 24–36 months; edit capture | OTel Collector with redaction; Langfuse self-hosted or MLflow; DeepEval; Promptfoo plus an independent red-team tool | MLflow on SageMaker [VF: A1-S103] | MLflow on Azure ML [VF: A1-S103] | Langfuse self-hosted (no native option profiled) |
| C1 | Route with residency constraint, fallback, budgets, inline guards, MCP endpoint | LiteLLM Enterprise or Kong AI Gateway hybrid | AgentCore Gateway for tools; model routing on the cloud-neutral gateway [VF: A6-S021, A6-S022] | APIM GA AI policies [VF: A6-S020] | Apigee AI gateway [VF: A6-S024] |
| C2 | Injection screening of retrieved chunks; numeric comparator; denied topics | Firm-coded comparator; NeMo Guardrails with Prompt Guard 2 plus a second detector | Bedrock Guardrails (ApplyGuardrail) [VF: A6-S072, A6-S073] | Azure AI Content Safety Prompt Shields on documents [VF: A6-S054, A6-S055] | Model Armor, strict residency [VF: A6-S067, B-C2-S003] |
| C3 | Tokenise client identifiers; re-identify only for the reviewer; redacted traces | Presidio behind the firm's privacy-service API | Presidio, or Bedrock Guardrails PII filter behind the same API [VF: A6-S072] | Presidio; Purview DSPM for posture [VF: A6-S090] | Sensitive Data Protection [VF: A6-S066] |
| C4 | Agent identity with sponsor; OBO; deny-by-default policy; approver identity | Workforce IdP + OPA + SPIFFE/SPIRE | AgentCore Identity + Policy (Cedar) [VF: A6-S026] | Entra Agent ID [VF: V2-S032] | Workforce IdP (Okta or Entra) + OPA; no Google agent-identity product profiled [NPV] |
| C5 | Prompt set and release manifest in Git; PR with investment-risk approver; protected production label | Prompty or Dotprompt files; registry of the L9 platform | Same | Same | Same |
| C6 | Cost per approved commentary; budget that fails closed; loop alerts | Gateway virtual keys; FOCUS-shaped dataset | Bedrock application inference profiles [VF: B-C6-S004] | Foundry project cost tags [VF: B-C6-S005] | Not profiled |
| C7 | No outbound channel; secrets brokered; canary documents; pinned dependencies | Vault agentic IAM or cloud secrets plus workload identity; private package mirror | Same | Same | Same |
| C8 | Inventory entry; validation; evidence pack; quarterly attestation | Firm evidence store; OpenLineage; governance tool optional | Same | Same | Same |

**Why the L1 row names Claude only for AWS.** In the L1 section's per-cloud portfolio, Claude Sonnet 5.5 is the primary drafting model only in an AWS estate and the fallback in a Google Cloud estate; GPT-6.1 Sol, Gemini 3.8 Flash and Mistral Medium 3.5 are named as independent alternatives in the same table [AJ]. Claude's EU processing runs through Bedrock or Google Cloud regional endpoints, not the first-party API [VF: V2-S075, A5-S027]. GPT-6 Astra on Bedrock is in-Region only in two US Regions, so EU availability of any GPT-6 tier on Bedrock must be confirmed per model [VF: A5-S008, V2-S079].

**What it costs [AJ].** On the C6 worked arithmetic, a draft of about 40,000 input and 3,000 output tokens on a mid-tier model at US$2 / US$10 per 1M tokens (the list price of both Claude Sonnet 5.5 and GPT-6.1 Sol as of 7 October 2026 [VF: A5-S011, A5-S004]) costs about US$0.11, and with judges and an average of 2.5 drafts per approved commentary the token cost is roughly US$0.30, or about US$12 a month for 40 funds. The token figures are the author's own. The conclusion matters more than the number: tokens are not the cost driver; reviewer time is, so the metric to manage is the regeneration and edit rate [AJ].

**The threat it is built to survive [AJ].** C7's scenario is a third-party market note containing hidden text telling the model to state that currency hedging added 40 basis points and to send the draft elsewhere. The defence is layered so that no single control has to catch it: there is no outbound tool to hijack; the numeric comparator fails any figure not in the engine snapshot; retrieved text is wrapped as data; a detector screens retrieved chunks and quarantines the source; canary documents in staging fail the release gate; and the PM approves before release.

## VI.3 Boundaries

**What the agent may do [Rec]:**
- draft narrative text around figures supplied by the attribution engine;
- explain allocation, selection and currency effects in the house style;
- reference market context from approved, registered sources, with citations to document versions;
- propose wording, and propose new style rules as a pull request for human approval.

**What the agent must never do, and the component that enforces it [Rec]:**

| Never | Enforced by |
|---|---|
| Generate, round, recompute or "correct" an authoritative number | L4 read-only tools; C2 numeric comparator; L9 blocking eval; L1 boundary |
| Use a figure from retrieved commentary, memory or a parsed document as data | L8 `document_derived` tag; L6/L7 context-only rule; L5 contradiction check |
| Present inference as source data | C2 narrative grounding; L9 groundedness; citations to document versions |
| Publish without recorded human approval | L3 approval interrupt; release service acting on the approver's identity; C4 segregation of duties |
| Produce an output that cannot be reproduced, or discard evaluation evidence | C5 manifest; C8 evidence pack in the firm archive; L9 retention beyond any vendor tier |
| Call a write, publish, e-mail or HTTP tool | L4 allow-list (no such tool exists); C4 policy; C7 capability separation |
| Send client identifiers to an external model, search or SaaS store | C3 tokenisation; L4 egress proxy; L9 Collector redaction |
| Retrieve another fund's or client's material | L6 entitlement filter inside the search; partition per segregated mandate; CI cross-fund probes |
| Run on a model alias, a preview model or an unqualified fallback | C1 route definition; C5 pins; L9 re-qualification |
| Mix two attribution snapshots in one draft after a resume | L3 durable activity reuses the recorded snapshot |

## VI.4 The audit evidence pack

Each approved commentary produces one evidence pack, written automatically to the firm's immutable archive at approval and keyed by trace ID (C8 §C8.12) [Rec]:

| # | Element | Contents | Produced by |
|---:|---|---|---|
| 1 | Prompt version | Template ID and version; system-prompt hash; rendered prompt (tokenised per C3); release manifest ID | C5, C3 |
| 2 | Model version | Provider, model ID and exact version as returned by the gateway (not the alias); parameters; processing region; fallback flag | C1, L2 |
| 3 | Data snapshot | Attribution snapshot hash and run ID; holdings and benchmark as-of dates; retrieved document IDs, versions, trust tiers and scores; index version; embedding and reranker versions; parse manifests | L4, L6, L7, L8 |
| 4 | Tool calls | Each call with arguments hash, response hash, definition hash, policy decision, latency, and the identities used (agent and on-behalf-of analyst) | L4, C4, C7 |
| 5 | Evaluation results | Numeric faithfulness per figure; groundedness; style; trajectory; detector verdicts; metric-code and judge versions; thresholds | L9, C2, C7 |
| 6 | Approver | PM's authenticated identity; decision; edit diff between draft and final; reason code | L3, C4 |
| 7 | Timestamps | Request, each step, evaluation, approval and release, from a synchronised clock | L9 |
| 8 | Final output and cost | Released text and hash; distribution record; tokens and cost per commentary | L3, C6 |

The inventory entry that governs the use case records its owner, accountable SMF, materiality tier (tier 1: client-facing, regulated communication, uses model outputs), EU AI Act category (not Annex III; Article 50 assessed, human editorial review applies), outsourcing entries, the full version bundle, validation reference and use limitations ("no figures generated by the model"), monitoring thresholds (numeric faithfulness 100%), change triggers and a quarterly review cycle (C8 §C8.12) [AJ]. Pinning versions and keeping a fallback qualified on the same suite is also the SS2/21 exit route [VF: R-PRA-SS221, A8-S048] [AJ].
