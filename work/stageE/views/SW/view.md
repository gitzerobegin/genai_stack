# Part XIV: The view for software product companies

**In brief.**
- **Who it is for.** A software vendor that ships products with GenAI features built in, which its customers install and run: self-managed and on-premises editions, private-cloud and air-gapped editions, cloud-marketplace images and SDKs [AJ].
- **The shift from the FS view.** The asset manager of Parts I–XII is a *deployer* that owns its control plane; a software product company is a *manufacturer and provider* shipping into control planes it does not own. It owns a release plane, and its product plugs into each customer's gateway, identity, telemetry and evidence tools [AJ].
- **The recommendation.** Qualify a support matrix, not a two-vendor portfolio; let customers bring their own model account or endpoint; bundle one redistributable open-weight model for air-gapped sites; gate every shipped component on licence and supply chain; and ship auditable evidence, before the Cyber Resilience Act's main obligations apply on 11 December 2027 [Rec] [VF: E1-S001, E1-S002].
- **The caveat.** The author is an Anthropic model. Wherever an Anthropic model, SDK or Anthropic-originated standard appears below, an independent alternative is named beside it (as in Part I) [AJ].

## XIV.1 Who this view is for

**Profile.** The product already has a permission model, an audit log, an installer and a release train, and is adding GenAI features: an assistant, summarisation, extraction or a bounded agent step [AJ]. The weights reflect this: deployment flexibility 20%, licence portability 15%, cost 5% (`views.json`) [AJ].

**Assumptions [AJ].** The customer usually pays for inference, through its own account or hardware. The vendor sees no customer data in normal operation, and support telemetry is opt-in. Customers range from mid-market firms to the regulated FS firm of Parts I–XII, which is the toughest buyer. At least one edition runs air-gapped and one is sold through a hyperscaler marketplace. The vendor sells into the EU and the UK.

**The five biggest differences from the FS view.**

| # | FS view (Parts I–XII) | Software product company view | Why [AJ] |
|---:|---|---|---|
| 1 | The firm is a *deployer* under the AI Act and an outsourcing customer under DORA and PS7/26 | The vendor is a CRA *manufacturer*, a PLD *producer* and, under its own name, an AI Act *provider* | Installed software is a CRA product, and from 9 December 2026 software is a PLD product however it is supplied [VF: E1-S001, E1-S010, A8-S016] |
| 2 | One firm-owned control plane (gateway, identity, evidence) | Many customer-owned control planes; the product integrates with them and ships only minimal defaults | The vendor does not run the estate, so it cannot impose its gateway or its evidence store [AJ] |
| 3 | A two-vendor model portfolio through the primary cloud | A **support matrix**: bring-your-own model account or endpoint, plus one bundled open-weight model whose licence allows redistribution | Hosted models live for months; CRA support periods are at least five years unless expected use is shorter [VF: B-L1-S003, E1-S001] |
| 4 | Licence review as a gate on *use* | Licence review as a gate on *redistribution* (AGPL, SSPL, ELv2, BUSL, CC-BY-NC and model use policies that must flow into the EULA) | What is fine to run internally can be impossible to ship [VF: A2-S132, A7-S060, A2-S024, E2-S001] |
| 5 | Evidence per use case, in the firm's own store | Evidence per **release** (vendor), plus runtime evidence exported to the customer's own tools | Under the PLD, release history, evaluation records and logs are the main defence [VF: E1-S010] [R: E1-S013] |

## XIV.2 Findings that change for this view

**1. The vendor is a manufacturer now, and the reporting clock has already started.** The CRA's reporting duty has applied since 11 September 2026. Conformity assessment, the EU declaration of conformity and CE marking apply to each EU release from 11 December 2027 [VF: E1-S001, E1-S002]. An actively exploited vulnerability needs an early warning within 24 hours and a notification within 72 hours, through ENISA's Single Reporting Platform [VF: E1-S003, E1-S006]. A vendor-run endpoint that the product needs in order to work counts as the product's "remote data processing" and is in scope [VF: E1-S001]. For the FS firm this is a supplier question; here it is a release-engineering duty covering every bundled model, library and engine [AJ].

**2. Model lifetimes and support periods do not match.** A Gemini Flash version released on 13 August 2026 retires on 28 January 2027. OpenAI gives previews as little as about two weeks' notice. Mistral Medium 3.1 retired on 31 August 2026 [VF: B-L1-S003, B-L1-S001, B-L1-S002]. Yet the CRA support period must reflect expected use and be at least five years unless expected use is shorter, with its end month and year stated at purchase [VF: E1-S001]. A product therefore needs a configurable model route, a support matrix that changes between releases, and one bundled open-weight model the vendor controls for the whole support period [Rec].

**3. Redistribution, not use, decides the open-weight shortlist.** Gemma 4, Mistral Large 3 and Ministral 3, Qwen3.8-27B and DeepSeek V4 are Apache 2.0 or MIT and ship with the licence and notices [VF: A5-S034, A5-S074, A5-S066, A5-S063]. gpt-oss is Apache 2.0 subject to a usage policy whose text was not retrieved [VF: E2-S003, E2-S024] [NPV]. Mistral Medium 3.5 is "Modified MIT" with revenue-based exceptions [VF: V2-S018], and older Gemma and DeepSeek terms require use restrictions to be passed on as enforceable terms [VF: E2-S023, E2-S013, E2-S014]. Llama 4 needs "Built with Llama" attribution, a Notice file and a "Llama" prefix on derived models [VF: E2-S001], and its Acceptable Use Policy grants no rights to the multimodal Llama 4 models to companies with their principal place of business in the EU, end users of an incorporating product excepted [VF: E2-S002]. An EU-headquartered vendor should leave Llama 4 multimodal models out of its product [Rec].

**4. Many "open" infrastructure components cannot be embedded as freely as they can be run.** Elasticsearch is AGPLv3, SSPL or ELv2; MongoDB Community is SSPL; Vault is BUSL 1.1, which excludes competing embedded offerings; Jina's weights are CC-BY-NC-4.0; and LM Studio's terms prohibit redistribution [VF: A2-S132, A2-S137, A7-S060, A2-S024, A4-S145]. Arize Phoenix is the reverse case: ELv2 permits redistribution but not a hosted service [VF: A1-S048], so it fits a self-managed edition but not a vendor-run SaaS edition [AJ]. XIV.8 applies this gate to every proposed component [AJ].

**5. The customer's control plane is the integration target.** Every gateway in the dataset exposes or accepts an OpenAI-compatible format [VF: A6-S015, A6-S049, A6-S053, A6-S061, A6-S063], and vLLM and SGLang serve it [VF: A4-S009, A4-S010]. One endpoint setting therefore reaches the customer's gateway, a hyperscaler deployment the customer owns, or the bundled engine; Azure's guidance already names this "tenant-provided" resource pattern [VF: E2-S016]. Where the FS firm puts its own gateway of record (Part I.2, decision 1), the product should *be routed by* the customer's gateway [Rec].

**6. Bring-your-own account shifts the model terms to the customer.** Anthropic's Commercial Terms permit powering products for the customer's own customers but bar reselling the Services without approval; OpenAI bars using Output to build competing models and transferring API keys; Google bars services likely to be accessed by under-18s; and Anthropic's Usage Policy reaches end users of integrating products [VF: E2-S004, E2-S026, E2-S007, E2-S005]. When the vendor holds the account these flow into its EULA; when the customer brings its own, the customer's terms govern [AJ]. Bring-your-own is the default [Rec].

**7. Retrieval belongs inside the product's existing permission model.** The FS equivalent of "platforms the firm already runs" (Part I.2, decision 9) is the product's own database [AJ]. pgvector is under the permissive PostgreSQL licence and ranks first in L6 under this view [VF: A2-S050, V1-S021] [AJ]. OWASP LLM08 names cross-context leakage in vector stores and recommends a permission-aware store [VF: E2-S051], which is easiest next to the product's own access-control tables [AJ].

**8. The supply chain is the vendor's own liability.** Malicious LiteLLM releases 1.82.7 and 1.82.8 were published to PyPI on 24 March 2026 [VF: A6-S008, V2-S027]. Pickle-format model files can execute code on load [VF: A7-S082, B-C7-S006]. Under the PLD, vendors stay liable for defects from software within their control, including a lack of safety-relevant security updates, and component makers share liability [VF: E1-S010]. Beyond the FS firm's mirror and pins (Part VII Stack A, C7), the vendor must patch the copies it has shipped for the whole support period [AJ].

**9. AI Act duties arrive as provider duties and written agreements.** Whoever supplies an AI system under its own name is its provider [VF: A8-S016]. Article 50 requires machine-readable marking of generated output, with a grace period to 2 December 2026 for systems on the market before 2 August 2026 [VF: E1-S035, E1-S036]. Where a customer builds a high-risk system on the product, Article 25(4) requires a written agreement, and monetised open-source components lose the exception [VF: E1-S033]. An integrator becomes a GPAI provider only above one third of the original training compute [VF: E1-S034], so ordinary fine-tuning in a product does not make the vendor one [AJ].

## XIV.3 Scoring for this view

The view re-weights the same criterion scores; no fact, score or master tier changes [AJ].

| Criterion | FS weight | SW weight | Change | Reason [AJ] |
|---|---:|---:|---:|---|
| Technical | 15 | 15 | 0 | Capability matters equally |
| Enterprise readiness | 15 | 10 | −5 | The product inherits the customer's identity and audit stack |
| Security and compliance | 20 | 15 | −5 | The vendor's CRA and PLD duties sit in its architecture, not in a component's certificates |
| Deployment flexibility | 15 | 20 | +5 | The product runs wherever the customer runs it |
| Ecosystem | 5 | 10 | +5 | Open interfaces are how the product plugs in |
| Reliability and maturity | 10 | 10 | 0 | Unchanged |
| Cost and TCO | 5 | 5 | 0 | The customer usually pays for inference |
| Lock-in and portability | 15 | 15 | 0 | Meaning widens to *redistributability* |

**What moves, and why.** The largest risers pair deployment flexibility 5 with ecosystem 4 or 5: MCP and Agent Skills (+0.25 each, MCP to 3.80), Llama Protections (+0.25), SGLang and OpenLineage (+0.20), vLLM, MLflow and Promptfoo (+0.15) (`SW_scores.md`). Managed single-cloud services with deployment 2 fall by 0.15: AgentCore Memory, Memory Bank, Gemini Embedding 2 and OpenAI embeddings [AJ].

**Ranks that change the advice [AJ].** In L6, pgvector rises from 3 to 1 and Elasticsearch falls from 1 to 3. In L7, Sentence Transformers rises to 1. In L9, DeepEval rises from 6 to 2 and Langfuse falls from 2 to 4. In L1, Anthropic falls from 3 to 4 (no self-hosting [VF: A5-S010]) and Gemini from 5 to 8 (API-only [VF: A5-S032]), while Qwen and DeepSeek rise on open weights. In C7, model and package scanning rises to 1.

**Core candidates.** There are 48 core candidates under this view's weights, against 45 under FS, of 138 scored products [AJ]. Four become core candidates: Pydantic AI (3.65), MCP (3.80), Arize Phoenix (3.60) and Promptfoo (3.70). Google Sensitive Data Protection drops to Situational (3.50; deployment 2). The fit is computed and indicative. The master tiers and their conditions still apply: MCP stays Strategic, conditional on a gateway with mandatory authorisation; Phoenix and Promptfoo stay Tactical [AJ].

**Where the score and the licence disagree.** Llama Protections rises by 0.25, but Llama Guard 4 is under the Llama 4 community licence and its Acceptable Use Policy [VF: A6-S030, A6-S038], and whether the EU multimodal restriction reaches it was not established [NPV]. The rubric does not score redistribution, so this view adds a licence gate (XIV.8) [AJ].

The full table, all seven views side by side, is in `05_Data/views.xlsx`, and the per-layer ranks are in `work/stageE/views/SW_scores.md` [AJ].

## XIV.4 The architecture for this view

The architecture has three planes: the vendor's build and release plane, the product in the customer's estate, and the customer's own control plane that the product plugs into [AJ]. The FS view's twelve decisions (Part I.2) survive but split: evidence, evaluation and supply chain move into the release plane, while gateway, identity and policy are honoured by integrating with the customer's choices [AJ].

![SW architecture: the vendor's release plane and the product inside the customer's estate](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/SW-1.png){width=100%}

*Figure: The vendor qualifies every supported model, gates every redistributed component and ships a signed release; in the customer's estate the AI feature uses the product's own permissions, calls the model through the customer's gateway or cloud account (or a bundled open-weight model on air-gapped sites), and sends telemetry and audit events to the customer's own tools. Editable source: `08_Graphic/diagrams/SW-1.md`.* [AJ]

**Ten design decisions for this view [Rec]:**

1. **A model adapter, not a gateway of record.** An OpenAI-compatible endpoint setting, model-ID pin and fallback list; the customer's gateway is the preferred target. [Rec]
2. **A published support matrix.** Each release lists the models it was qualified on; others are labelled "customer-qualified". [Rec]
3. **One bundled open-weight model under Apache 2.0 or MIT**, served by vLLM, signed, in safetensors format, and patched for the support period. [Rec]
4. **Retrieval inside the product's own database and permission model**, rebuildable, with the embedding version on every vector. [Rec]
5. **Deterministic workflows with one bounded model step.** Tools read-only by default, through the customer's tool gateway where one exists. [Rec]
6. **Identity from the customer's IdP** via the product's SSO and SCIM; no credentials beyond the user's own session. [Rec]
7. **OTel spans and audit events exported** to the customer's collector and SIEM, redaction on, conventions version pinned (still "Development" [VF: A1-S058]); nothing to the vendor without opt-in. [Rec]
8. **A licence and supply-chain gate in CI**: a redistribution register, an SBOM, model scanning, signed artefacts and a private mirror. [Rec]
9. **An evaluation harness that ships**, so the customer can re-run the suite on its own model and documents. [Rec]
10. **Article 50 disclosure and machine-readable marking built into the feature**, with a per-customer off switch. [Rec]

## XIV.5 Layer by layer, then control by control

| Layer / control | Default choice for this view | Change from the FS view | Why |
|---|---|---|---|
| L1 models | Customer's own hosted model (GPT, Claude, Gemini or Mistral; Strategic, with conditions); bundled Gemma 4 or Ministral 3 / Mistral Large 3 (Strategic) | Support matrix replaces the two-vendor portfolio; bundled model Apache 2.0 or MIT; for Claude, GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5 as alternatives | Hosted lifetimes are short; Apache 2.0 needs only licence and notices [VF: B-L1-S003, A5-S034, A5-S074] [AJ] |
| L2 inference | Customer's endpoint; vLLM (Strategic) inside the bundled route | vLLM moves from exit route to shipped engine; SGLang (Strategic, conditional) once CVE-2026-3059 is fixed | Apache-2.0, OpenAI-compatible [VF: A4-S009, A4-S010, B-REVC-S002] [AJ] |
| L3 orchestration | LangGraph (Strategic) or Pydantic AI (Strategic, conditional) as libraries; durability via the product's job system | Temporal optional; the Claude Agent SDK (Experimental) stays out of shipped code (alternatives: LangGraph, Pydantic AI) | MIT libraries ship; the Claude Agent SDK is under Anthropic's Commercial Terms [VF: A4-S001, A4-S003, A4-S092] [AJ] |
| L4 tools | Read-only internal tools; an MCP server (Strategic, conditional) for customers' agents, OpenAPI as the independent alternative | The product becomes a *tool provider*, not only a consumer | MIT under AAIF; authorisation is optional in the specification, so the product enforces its own [VF: A3-S058, A3-S018, A3-S055] |
| L5 memory | None; per-user preferences in the product's own data model | Same deferral; memory products are mostly open core or managed | Mem0 and Cognee keep features in licensed or platform tiers [VF: A3-S001, A3-S080, A3-S005] [AJ] |
| L6 stores | pgvector in the product's own PostgreSQL (Strategic); Qdrant or Milvus (Strategic) for a dedicated engine | Elasticsearch (Strategic) or MongoDB only where already embedded under an acceptable licence | Permissive licences ship; AGPL/SSPL/ELv2 options need legal review [VF: A2-S050, A2-S108, A2-S118, A2-S132, A2-S137] |
| L7 retrieval optimisation | Sentence Transformers (Strategic) serving an Apache-2.0 embedding model; Qwen3-Embedding (Tactical) after provenance review | Hosted embeddings only through the customer's account; Jina weights never bundled | Model version on every vector; CC-BY-NC weights cannot ship [VF: A2-S029, A2-S020, A2-S024] |
| L8 ingestion | Docling and Unstructured OSS (Strategic) embedded; each parsing model's licence checked | Managed parsers become customer-selectable options, not defaults | Docling's code is MIT but individual models carry their own licences [VF: A1-S057, A1-S008, A1-S011] |
| L9 evaluation | Shipped harness on DeepEval or Promptfoo (Tactical); OTel export; MLflow or Langfuse (Strategic) internally | Vendor platform holds *release* evidence; customer picks its runtime platform | Tools ship; Promptfoo's announced owner is a model vendor, so keep an independent second red-team tool [VF: A1-S051, A1-S052, A1-S024] |
| C1 gateway | Customer's gateway; for customers without one, an optional bundled LiteLLM core (Strategic, conditional) or agentgateway (Tactical) | The vendor does not own the gateway of record | Open cores ship; LiteLLM must be pinned to clean releases [VF: A6-S001, A6-S061, A6-S009] |
| C2 guardrails | Product invariants; NeMo Guardrails (Tactical) with a redistributable detector; cloud services as adapters | Managed detectors cannot be bundled | NeMo is Apache-2.0 but still 0.x; the Llama Guard 4 licence needs review [VF: A6-S003, A6-S030] |
| C3 privacy | Presidio (Strategic) embedded behind a product privacy API; redaction before export | Same engine; policy per customer, not firm-wide | MIT, runs in-estate [VF: A6-S005, A6-S040] |
| C4 identity | Product SSO and SCIM against the customer's IdP; OPA or Cedar (Strategic) for feature policy | Entra Agent ID and Okta for AI Agents are customer-side integrations | OPA and Cedar are Apache-2.0 [VF: A6-S088, A6-S045] |
| C5 configuration | Prompts as code (Strategic), versioned with the release; customer overrides in configuration | Prompts ship in the release, not from a runtime registry | Prompty (MIT) and Dotprompt (Apache-2.0) are open formats [VF: A7-S008, A7-S065] |
| C6 FinOps | Token and request metering exposed to the customer; FOCUS-aligned (Strategic) usage export | The vendor rarely pays for inference; the customer needs the numbers | FOCUS is CC-BY-4.0 [VF: A7-S096] |
| C7 security | Scanning (Strategic), safetensors only, OMS signing (Tactical), SBOM; the product's own secrets store | From protecting one estate to signing and patching shipped copies; Vault (Strategic, conditional) not embedded | BUSL excludes competing embedded offerings [VF: A7-S002, A7-S038, A7-S060] |
| C8 governance | OpenLineage (Strategic) events and evidence export; vendor release-evidence store | The customer's governance tool consumes the export; no vendor governance platform needed | Apache-2.0 [VF: A7-S041] [AJ] |

## XIV.6 Regulation, contracts and customer assurance

**The vendor's own duties.** Part V's anchors are SS1/23, DORA and AI Act deployer duties; this view's are the CRA, the PLD and the AI Act provider role [AJ].

| Instrument | What it requires of a software product company | Date | Source |
|---|---|---|---|
| CRA (R-EU-CRA) | Report actively exploited vulnerabilities and severe incidents within 24 h / 72 h | Since 11 September 2026 | [VF: E1-S001, E1-S003, E1-S006] |
| CRA | Conformity assessment, declaration, CE marking, SBOM, support period of at least five years unless use is shorter | 11 December 2027 | [VF: E1-S001, E1-S002] |
| PLD (R-EU-PLD) | Software is a product however supplied; liability for defects within the vendor's control, including missing safety-relevant updates | Products placed on the market from 9 December 2026 | [VF: E1-S010, E1-S011, E1-S012] |
| AI Act provider role (R-EUAIA, R-EU-AIA-ROLES) | Provider of the AI feature under its own name; Article 50 disclosure and marking; Article 25(4) agreements for customers' high-risk systems | Article 50 marking grace ends 2 December 2026; Annex III from 2 December 2027 | [VF: A8-S016, E1-S033, E1-S035, E1-S036, A8-S011] |
| CRA and AI Act link | Meeting CRA Annex I is deemed to meet Article 15 cybersecurity for a high-risk AI system; accuracy and robustness still apply | With CRA application | [R: E1-S008] |
| UK (R-UK-SOFTWARE) | No CRA equivalent; the voluntary Software Security Code of Practice (14 principles) is the buyer's reference; PSTI covers only consumer products | Code launched 7 May 2025 | [VF: E1-S051, E1-S052, E1-S053, E1-S054] |
| US states (R-US-STATE-AI) | Colorado developer documentation (intended uses, training-data categories, limitations, human review); enforcement stayed pending rulemaking | From 1 January 2027 (stayed) | [VF: E1-S038, E1-S039, E1-S040, E1-S050] |
| Data Act (R-EU-DATA-ACT) | SaaS edition only: no switching charges, egress included | From 12 January 2027 | [VF: E1-S025, E1-S026] |

**What this means architecturally [AJ].**
- **The SBOM includes the AI components.** Bundled open-weight models and open-source libraries become components the manufacturer must document and patch: the model, the serving engine, the parsing and embedding models [AJ].
- **The release record is the defence.** PLD disclosure orders and the presumption for technical complexity make release history, evaluation records and logs the main defence [VF: E1-S010] [R: E1-S013], so release qualification (XIV.10) is a liability control as well as a quality control [AJ].
- **Article 25(4) needs a standard information pack** for customers in HR, credit or insurance pricing who build on the product [VF: E1-S033] [Rec].
- **Open points.** The CRA fine-tier allocation and the Commission guidance's line on SaaS and support periods were not established [NPV].

**Contracts [AJ].** The EULA carries the notices and flow-down terms of every bundled model (XIV.2, finding 3), the AI disclosure duty, the hosted-model terms where the vendor holds the account, and a support-period statement consistent with the support matrix. Where the customer brings its own account, the contract should say that the customer's model terms govern and that the vendor is not a subprocessor for that inference [Rec]. Where an EU financial entity buys vendor-operated support or a hosted edition, expect DORA Article 30 clauses on subcontracting, data locations, exit, incident assistance and, for critical functions, audit rights [VF: E1-S055, E1-S056, E1-S057] [AJ].

**Customer assurance.** Expect SOC 2 against the 2017 criteria with 2022 points of focus [R: E2-S048], ISO/IEC 27001:2022 [R: E2-S046], and increasingly a CSA AI-CAIQ or STAR for AI entry [VF: E2-S047]. A self-managed product adds the SBOM, the support period, the vulnerability-handling policy, and proof that the AI feature can be switched off and run air-gapped; generate these per release, not in a sales spreadsheet [Rec].

## XIV.7 Reference stack

This is the stack the vendor *ships and builds with*, cloud-neutral by necessity [AJ]. The per-cloud columns differ only where the customer's cloud supplies the bring-your-own model route or an optional adapter. Tiers are the master tiers, abbreviated S, T and E as in Part VII [AJ].

| Layer / control | Shipped default (master tier) | Independent alternative | AWS customer | Azure customer | Google Cloud customer |
|---|---|---|---|---|---|
| L1 hosted (BYO) | Customer-chosen GPT (S), Claude (S, cond.), Gemini (S, cond.) or Mistral (S) via the customer's account | For Claude: GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5 | Bedrock in the customer's account, geographic or in-Region [VF: B-L2-S005] | Tenant-provided Foundry resource, Data Zone or Regional [VF: E2-S016, B-L2-S006] | Regional endpoint in the customer's project [VF: B-L2-S008] |
| L3 | LangGraph (S) or Pydantic AI (S, cond.) | Microsoft Agent Framework (S) for .NET products | Strands SDK (S, cond.) only if the product is AWS-only | Microsoft Agent Framework (S) | ADK (S, cond.) only if the product is Google-only |
| L4 | Product MCP server (S, cond.) and read-only internal tools | OpenAPI description of the same endpoints | Listed behind AgentCore Gateway by the customer [VF: A3-S047] | Behind APIM by the customer [VF: A6-S053] | Behind Apigee by the customer [VF: A6-S023] |
| L6 | pgvector (S) in the product database | Qdrant (S) or Milvus (S) embedded engine | pgvector on RDS/Aurora for the SaaS edition [VF: B-L6-S004] | Azure Database for PostgreSQL [VF: B-L6-S005] | Cloud SQL [VF: B-L6-S005] |
| L7 | Sentence Transformers (S) with an Apache-2.0 model | Cohere private deployment (T) where the customer licenses it [VF: A2-S015] | Customer's Bedrock embeddings (not profiled [NPV]) | Customer's Foundry embeddings (not profiled [NPV]) | Gemini Embedding 2 (S, cond.) via the customer's project |
| L8 | Docling (S) + Unstructured OSS (S) | Mistral OCR self-managed (T) under the customer's agreement [VF: A1-S135] | Same | Same | Document AI (S, cond.) as a customer option |
| L9 | OTel export; shipped harness on DeepEval (T) and Promptfoo (T) | Opik (T), Apache-2.0 for the full platform [VF: A1-S050] | Customer's MLflow on SageMaker (S) | Customer's MLflow on Azure ML (S) | Customer's Langfuse (S) |
| C1 | Customer's gateway; optional LiteLLM core (S, cond.) | agentgateway (T) | AgentCore Gateway (S, cond.) for tools, customer-owned | APIM AI policies (S, cond.) | Apigee (S, cond.) |
| C2 | Product invariants + NeMo Guardrails (T) | Check Point AI Guardrails (T), self-hosted, as a customer option [VF: A7-S024] | Bedrock Guardrails adapter (S, cond.) | Content Safety adapter (S, cond.) | Model Armor adapter (S, cond.) |
| C3 | Presidio (S, cond.) | Google Sensitive Data Protection (S, cond.) as a customer option | Same | Purview DSPM for the customer's posture (S, cond.) | Sensitive Data Protection adapter |
| C4 | Product SSO/SCIM + OPA (S) | Cedar (S) | Customer's IdP; AgentCore Identity where the customer uses it | Entra (Agent ID for agent access) (S, cond.) | Customer's IdP |
| C6 | Usage metering + FOCUS (S) export | Gateway cost attribution (S) in the customer's gateway | Bedrock application inference profiles in the customer's account [VF: B-C6-S004] | Foundry project tags [VF: B-C6-S005] | Customer gateway metering |

**The same in every cloud [Rec].** The bundled route (Gemma 4 (S) or Ministral 3 / Mistral Large 3 (S) on vLLM (S), with gpt-oss (S) or Qwen3.8-27B (T) as alternatives and SGLang (S, cond.) as the second engine), prompts as code (S) in the release, scanning (S) with OMS signing (T) and an SBOM, and OpenLineage (S) evidence export do not vary by cloud; marketplace editions ship them as an AMI, container or VM image [AJ].

**Marketplace editions [VF: E2-S034, E2-S036, E2-S020, E2-S038].** AWS private offers name up to 25 buyer accounts and can share AMI and container licences; eligible Microsoft Marketplace purchases count fully toward the Azure commitment; Google Cloud Marketplace draws down Google commitments and private offers can include third-party models for Vertex AI. Pre-wire the marketplace image to the customer's model service in that cloud, so the buyer's commitment pays for both product and inference [Rec].

## XIV.8 Build vs buy, and lock-in

**The rule for this view.** Build what makes the product the product: the AI feature, permission-aware retrieval, the model adapter, the evaluation suite and the release evidence. Embed open components whose licences allow redistribution. Never ship a component the vendor cannot redistribute, patch for the support period, or run air-gapped [AJ]. Unlike Part VIII, "buy" cannot mean a managed service in the shipped product; a managed service is only ever a *customer-selected adapter* [AJ].

| Component | Decision | The vendor builds | It embeds, or leaves to the customer |
|---|---|---|---|
| Model access (L1, L2, C1) | **Build the adapter; embed an engine** | Adapter, support matrix, qualification suite | vLLM and one Apache-2.0 model; the customer's gateway or account |
| Orchestration and tools (L3, L4) | **Embed open source; build workflows and the product's MCP server** | Feature workflows, run records, MCP and OpenAPI interfaces | LangGraph or Pydantic AI [VF: A4-S001, A4-S003]; customers' tool gateways |
| Retrieval (L6–L8) | **Build the envelope; embed the engines** | Permission filter, chunk metadata, rebuild pipeline | pgvector, Sentence Transformers, Docling, Unstructured |
| Evaluation (L9) | **Build the suite** | Datasets, scorers, customer-runnable harness | DeepEval, Promptfoo, OTel SDK |
| Controls (C2–C4) | **Hybrid; reuse the product's identity** | Invariants, privacy API, feature policy | NeMo Guardrails, Presidio, OPA; cloud detectors as adapters |
| Supply chain and evidence (C7, C8) | **Build** | Licence register, SBOM, signing, patch process, evidence export | Open scanners, OMS; the customer's SIEM and governance tool |

**The redistribution gate [Rec].** Each component gets one row in a licence register: licence, redistribution allowed, notices, flow-down terms, thresholds, and air-gap capability. Applied to the components most often proposed [AJ]:

| Outcome | Components | Source |
|---|---|---|
| Ship with notices | Gemma 4, Mistral Large 3, Ministral 3, Qwen3.8-27B, DeepSeek V4, vLLM, SGLang, LangGraph, Pydantic AI, pgvector, Qdrant, Milvus, Sentence Transformers, Docling code, Unstructured OSS, DeepEval, Promptfoo, Opik, MLflow, Presidio, OPA, Cedar, OpenLineage | Licence fields of each product record in `05_Data/products.json` [VF: A5-S034, A4-S009, A2-S050, A1-S057, A6-S005] |
| Ship with flow-down terms or thresholds | gpt-oss, Mistral Medium 3.5, Llama 4 (non-EU vendors only for multimodal models), Crawl4AI, MinerU, GLM-5.3, Kimi | [VF: E2-S024, V2-S018, E2-S001, A1-S056, A1-S054, A5-S071, A5-S069] |
| Self-managed edition only | Arize Phoenix (ELv2) | [VF: A1-S048] |
| Ship the open core; licence the rest | LiteLLM, Langfuse, Kong Gateway OSS, Weaviate, Cognee | [VF: A6-S001, A1-S023, A6-S017, A2-S115, A3-S005] |
| Legal review first | Elasticsearch, MongoDB Community, Firecrawl server, Vault, ValidMind library | [VF: A2-S132, A2-S137, A1-S053, A7-S060, A7-S003] |
| Do not ship | Jina weights without a commercial licence; Llama 4 multimodal models from an EU-domiciled vendor; LM Studio; NeMo Retriever without NVIDIA AI Enterprise | [VF: A2-S024, E2-S002, A4-S145, A2-S041] |

**Lock-in, in both directions.**
- **The vendor's lock-in.** The costly event is a terms or owner change in something already shipped: Weaviate's move to open core, Langfuse under ClickHouse, Promptfoo's announced sale to OpenAI, TGI archived [VF: A2-S115, A1-S021, A1-S024, V1-S054]. Every embedded component needs a named replacement in the register, and Part IX.1's abstractions (model routing, retrieval, embedding, evaluation, privacy) belong in the product code [Rec].
- **The customer's lock-in to the vendor.** For the SaaS edition, Data Act switching rules give at most two months' notice, a 30-day transition and machine-readable export [VF: E1-S025, E1-S026]; whether embeddings or fine-tuned weights are exportable data is unresolved [NPV]. Export documents, prompts, configuration and evidence in open formats and let the index rebuild [Rec].
- **Where multi-vendor is necessary.** At least two qualified hosted models from unrelated vendors plus the bundled model, so that one retirement or suspension does not stop the feature for every customer at once; one framework, one store and one telemetry format are enough (Part IX.3) [AJ].

## XIV.9 Roadmap

The roadmap is sized to a quarterly release train and aligned to the vendor's dates, not to PS7/26 [AJ].

| Date | Event | Consequence [AJ] |
|---|---|---|
| Since 11 September 2026 | CRA vulnerability and incident reporting [VF: E1-S001, E1-S003] | Reporting covers AI components now |
| 2 December 2026 | Article 50 marking grace ends for systems on the market before 2 August 2026 [VF: E1-S036] | Machine-readable marking in the next release |
| 9 December 2026 | PLD applies to products placed on the market from this date [VF: E1-S011] | Release evidence kept per release |
| 1 January 2027 | Colorado developer-documentation duties (stayed pending rulemaking) [VF: E1-S038, E1-S040] | Documentation pack drafted |
| 12 January 2027 | Data Act: no switching charges for cloud and SaaS [VF: E1-S025] | SaaS edition export and switching terms |
| 28 January 2027 | A Gemini Flash version retires [VF: B-L1-S003] | Support-matrix change process exercised |
| 2 December 2027 | Annex III high-risk duties [VF: A8-S011] | Article 25(4) pack available to high-risk customers |
| 11 December 2027 | CRA conformity, declaration and CE marking [VF: E1-S001, E1-S002] | Every EU release conforms |

**Phase 0: Roles, licences and reporting (October–December 2026) [Rec].** Classify each edition under the CRA; record each AI feature's AI Act role; start the licence register and the AI-aware SBOM; extend the reporting runbook to bundled AI components; add Article 50 marking to features already on the market. *Exit:* the register covers the current release and the reporting drill has run once.

**Phase 1: Model adapter and qualification (January–March 2027) [Rec].** Ship the OpenAI-compatible adapter with pins and fallbacks; run the evaluation suite on two unrelated hosted vendors; publish the first support matrix; add redacted OTel export. *Exit:* a customer switches hosted model by configuration, and release notes carry the qualification results.

**Phase 2: Permission-aware retrieval and the first GA feature (April–June 2027) [Rec].** Retrieval in the product database with the ACL filter and embedding version tags; Docling ingestion; a cross-user leak test in CI; first feature generally available, bring-your-own model only. *Exit:* the leak test returns zero and the index rebuilds within the documented time.

**Phase 3: The bundled and air-gapped edition (July–September 2027) [Rec].** Signed, safetensors bundled model on vLLM with its notices; offline installer; customer-runnable harness; Article 25(4) and Colorado packs. *Exit:* the feature runs with no outbound connection and the bundled model passes the same suite.

**Phase 4: CRA conformity (October–December 2027) [Rec].** Conformity assessment, declaration and CE marking; support periods consistent with the matrix; a patch drill on a bundled AI component. *Exit:* the first CE-marked release ships before 11 December 2027.

**Phase 5: Agents and tools (2028) [Rec].** The product's MCP server (OpenAPI as the independent alternative) becomes a supported interface for customers' agents, with mandatory authorisation; write tools only behind customer policy and human approval. *Exit:* the OWASP agentic red-team cases pass [VF: R-OWASP-AGENTIC, A8-S042].

## XIV.10 Worked example: "ask your documents" in an on-premises document-management product

**The use case.** An on-premises document-management product ships an "ask your documents" assistant (`views.json`). Customers choose a hosted model through their own account, or a bundled open-weight model for air-gapped sites; retrieval respects the product's existing permissions [AJ]. As in Part VI, it is a deterministic workflow with one model step, grounded in documents the user may read [AJ].

**Trace.**

| Step | What happens | Components |
|---:|---|---|
| 0 | Release 2027.2 ships a signed manifest with SBOM: prompt set, support matrix (two unrelated hosted vendors plus bundled Gemma 4 on vLLM), embedding version, guard policy, evaluation thresholds | Vendor C5, C7, L9 |
| 1 | The administrator selects a route: an OpenAI-compatible endpoint (the customer's gateway, or its Bedrock, Foundry or Google Cloud deployment) or the bundled route; the feature can be disabled per library | C1, L2, C5 |
| 2 | Ingestion: new and changed documents are parsed (Docling), chunked and embedded; each chunk carries document ID, version, the product's ACL reference and the embedding version | L8, L7, L6 |
| 3 | A user signs in through the product's SSO against the customer's IdP; groups via SCIM | C4 |
| 4 | The user asks a question; Presidio redacts configured entities before any external call | C3 |
| 5 | Retrieval: query embedding, hybrid search in the product's PostgreSQL (pgvector plus full text), filtered by the user's current ACLs inside the query, then rerank | L7, L6, C4 |
| 6 | Retrieved chunks are screened for indirect injection and wrapped as data | C2, C7 |
| 7 | One model call through the model adapter to the selected route, with the pinned model ID, a timeout, one qualified fallback, and a token ceiling | L3, C1, L1, C6 |
| 8 | Output checks: every citation references a retrieved chunk; permission re-checked on cited documents; visible AI label and machine-readable marking | C2, C4, Article 50 |
| 9 | OTel spans (redacted) to the customer's collector; an audit event to the product's audit log, forwarded to the customer's SIEM | L9, C8 |
| 10 | User feedback stays in the customer's instance, exportable for its own evaluation | L9 |

**Boundaries.**

| May [Rec] | Must never [Rec] | Enforced by |
|---|---|---|
| Answer from documents the user may read, with citations to document versions | Retrieve or cite a document the user cannot open | Permission filter inside the query; citation re-check; CI leak test |
| Summarise and compare documents | Send a document, prompt or answer to the vendor without customer opt-in | No vendor endpoint on the request path; telemetry opt-in |
| Use the customer's chosen model route | Fall back to an unqualified model, or a route the customer did not configure | Adapter fallback list limited to the support matrix; administrator setting |
| Run fully offline on the bundled model | Load model weights that are unsigned or in pickle format | Signature check at start; safetensors only |
| Propose edits or tags as suggestions | Change, move, share or delete documents | No write tools in this release |
| Show that an answer is AI-generated | Present generated text as a document's content | Article 50 label and marking; distinct UI element |

**The evidence kept.** It is split between the vendor and the customer, and neither copy depends on the other [AJ].

| Evidence | Kept by | Contents and purpose |
|---|---|---|
| Release-qualification record | Vendor | Suite version, results per supported model, manifest hash, SBOM, signatures; the PLD defence and CRA technical documentation [VF: E1-S001, E1-S010] |
| Licence register and vulnerability-handling records | Vendor | Licences, notices, flow-down terms; report, fix, release and customer notice for CRA reporting [VF: E1-S003] |
| Runtime audit event and OTel trace | Customer | User, question hash, document IDs and versions, model route and version, guard verdicts, citations; redacted spans [AJ] |
| Feedback and edits | Customer | Ratings and corrections for re-qualifying the customer's own model choice [AJ] |

**What it costs [AJ].** Inference falls on the customer; the vendor pays for the qualification matrix, one suite run per supported model per release. The number of supported models, not the token price, is the cost to manage, so keep the matrix short and fresh [AJ].

## XIV.11 Checklist, what to avoid, what to monitor

**Checklist [Rec].**
- Each edition classified under the CRA, each AI feature's AI Act role recorded, and the 24-hour / 72-hour runbook extended to bundled AI components.
- A licence register and an AI-aware SBOM in every release.
- A support matrix per release: at least two unrelated hosted vendors plus one Apache 2.0 or MIT bundled model.
- A model route configurable to the customer's gateway or account; no provider SDKs in feature code.
- ACL filtering inside the retrieval query, citation re-checks, and a leak test in CI.
- Signed, safetensors-only bundled weights; OTel export with redaction on; no data to the vendor without opt-in.
- Article 50 disclosure and marking; a per-customer off switch; Article 25(4) and Colorado documentation packs.
- An independent alternative documented for each Anthropic item: OpenAPI for MCP; AGENTS.md or C5 packages for Agent Skills; LangGraph or Pydantic AI for the Claude Agent SDK; GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5 for Claude models.

**What to avoid [Rec].**
- A hosted model ID hard-coded for a support period [VF: B-L1-S003].
- The "do not ship" row of XIV.8, and its "legal review first" row without the review.
- Pickle-format weights, and unpinned AI libraries with a recent supply-chain incident [VF: A7-S082, A6-S008].
- A vendor-run endpoint on the request path of a self-managed product: it enters CRA scope and breaks air-gapped use [VF: E1-S001].
- A firm-style gateway of record inside the product that regulated customers are asked to route through.
- The Claude Agent SDK, or any component governed by a vendor's commercial terms, in shipped code without a redistribution review [VF: A4-S092].

**What to monitor.**

| Monitor | Trigger for action [Rec] |
|---|---|
| CRA guidance C(2026) 5252 and Delegated Regulation (EU) 2026/881 | Read in full [NPV] |
| Hosted-model retirement notices | Re-qualify; publish a matrix change [VF: B-L1-S001, B-L1-S003] |
| gpt-oss usage policy, Mistral Medium 3.5 threshold wording, Mistral Large 4 and Muse Glimmer licences | Read the licence files before shipping [VF: A5-S076] [R: E2-S027, E2-S028] [NPV] |
| Ownership and licence changes of embedded tools | Re-run the redistribution gate [VF: A2-S115, A1-S021, A1-S024, A1-S045] |
| OTel GenAI conventions leaving "Development" | Re-pin the exported version [VF: A1-S058] |
| MCP authorisation and agent-identity work | Make authorisation mandatory on the product's MCP server [VF: A3-S055, A3-S016] |
| Colorado rulemaking and stay; California bills of September 2026 | Publish developer documentation when enforceable [VF: E1-S040] [NPV] |
| UK Cyber Security and Resilience Bill; AI Office Article 25(4) model terms | Check reach to software vendors; align the information pack [VF: E1-S023, E1-S033] |

**The answer, in one paragraph.** A software product company should own a release plane, not a control plane [AJ]. It should qualify a short support matrix of hosted models that customers reach through their own accounts and gateways. It should ship one Apache 2.0 or MIT model on vLLM for air-gapped sites. It should build retrieval inside its own permission model on pgvector, embed only components that pass a redistribution gate, and export telemetry and evidence to the customer's own tools. It should treat the CRA and the PLD as the architecture's deadlines [Rec]. Most of the FS view's recommendations still hold, but the vendor meets them by plugging into each customer's gateway, identity and evidence tools rather than owning those controls itself (Part I.2; Part VII Stack C for the open-source components) [AJ].
