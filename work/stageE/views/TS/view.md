# Part XIII: The view for technology service providers

**In brief.**
- **Who it is for.** A technology company that runs GenAI inside services it operates for its customers: multi-tenant SaaS, managed or hosted services, digital platforms. It processes customer data, owes uptime and security commitments, and earns a margin on every model call [AJ].
- **What changes.** The FS view (Parts I–XII) builds a control and evidence plane for one regulated firm. A service provider builds the same plane, but every element of it must be tenant-aware, metered and sold: tenant isolation, cost per call and service levels replace model-risk validation as the hardest problems [AJ].
- **What stays.** Part I.2's gateway of record, day-one evaluation, deterministic workflows with human approval, and Git as the configuration of record [Rec].
- **The view at end of Q3 2026.** Evidence read on 9–10 October 2026; prices and capacity tiers are volatile and re-verified each quarter [AJ].

> **Conflict-of-interest disclosure.** The author is an Anthropic model. Anthropic's Claude family rises from third to second in its layer under this view's weights; that movement comes from the same criterion scores as every other product, re-weighted by `tools/build_views.py`. Wherever a Claude model, MCP or Agent Skills is mentioned as a choice, an independent alternative is named beside it [AJ].

## XIII.1 Who this view is for

**Profile.** The organisation runs one estate it controls and sells a service from it. Its tenants bring their data, their end users and often their regulators' expectations; it processes that data, answers security questionnaires, commits to uptime, and carries the model bill unless a tenant brings its own model account (views.json) [AJ].

**Assumptions.** The provider is medium-sized or larger, serves EU and UK customers including regulated financial firms, already runs a SaaS platform with tenant isolation and SSO, has a platform team rather than a model-risk function, and ships mostly a hosted service, perhaps with an installable SDK or connector [AJ].

**The five biggest differences from the FS view [AJ]:**

| # | FS view (Parts I–XII) | Technology service provider view | Consequence for the architecture |
|---:|---|---|---|
| 1 | Cost is a minor criterion (5%); tokens are not the cost driver, reviewer time is (Part VI) | Cost per call is gross margin (15%); every call is a cost of goods sold | C6 becomes a product control: per-tenant metering, unit economics and cost levers designed in from the first release [AJ] |
| 2 | Isolation means a partition per segregated mandate inside one firm | Isolation between customers is the product's core promise | Tenant identity is carried in every token, key, cache, index, trace and evidence record; cross-tenant leakage is the top risk [AJ] |
| 3 | Two model vendors exist mainly for regulatory exit (SS2/21) | Two vendors exist for service levels, capacity and suspension risk | The fallback is sized and drilled as a live capacity route, not only as an exit route [AJ] |
| 4 | The firm is a deployer under model-risk, outsourcing and resilience rules | The provider is an AI-system provider, a likely NIS2 entity, liable for its software as a product under the PLD, and a third party in its FS customers' registers | Customer assurance and contract flow-down replace model-risk validation as the governing discipline [AJ] |
| 5 | Lock-in weighs 15%; cloud-native services are conditional | Lock-in weighs 5%; the provider runs one estate it chooses | Managed cloud services rise (guardrails, DLP, cheap vector tiers); the provider's own exit duty is to its customers, under the Data Act [AJ] |

## XIII.2 Findings that change for this view

**1. The three US model vendors allow a provider to build a service on their APIs, with limits that must flow down.** Anthropic's Commercial Terms expressly permit using the services "to power products and services Customer makes available to its own customers and end users" [VF: E2-S004]. OpenAI and Google let the customer keep inputs and own outputs, and Google treats generated output as Customer Data [VF: E2-S026, E2-S007]. All three restrict using their services or outputs to build competing models; Anthropic also bars reselling raw access without approval, and OpenAI bars transferring API keys [VF: E2-S004, E2-S026, E2-S007]. A provider must therefore sell a service with its own logic, not a pass-through model API, and carry the vendors' usage policies down to end users [AJ].

**2. A tenant's misuse can suspend the whole service.** Anthropic may suspend access if it believes a customer or any of its users breaches the Usage Policy, and the policy applies to "the end users of products or services integrating Claude" [VF: E2-S004, E2-S005]. Google's generative AI terms bar any service "likely to be accessed by individuals under the age of 18", and clinical use [VF: E2-S007, E2-S030]. On a multi-tenant platform one tenant's breach can put every tenant's feature at risk, so per-tenant abuse monitoring, a per-tenant kill switch and a qualified second vendor are availability controls [AJ].

**3. Capacity, not regulation, is why the second vendor matters.** OpenAI's Priority processing (renamed Fast mode on 30 July 2026) carries a 99.9% uptime SLA, while Flex is billed at Batch rates and may return 429 under load [VF: E2-S031]. Anthropic no longer sells Priority Tier commitments; guaranteed capacity is a sales conversation [VF: E2-S006]. Azure PTU quota does not guarantee capacity [VF: E2-S017], and Anthropic's top tier, Claude Fable 5, was unavailable from 12 June to 1 July 2026 [VF: V2-S004]. The fallback vendor must be qualified, warm and sized for real traffic [AJ].

**4. Cost levers are large and must be designed in.** Batch processing is 50% below standard on OpenAI, Anthropic, the Gemini API, Bedrock (select models) and Azure OpenAI Global and Data Zone Batch [VF: A5-S004, A5-S011, A5-S032, E2-S032, E2-S018]. Cached input is about 90–95% cheaper on OpenAI, and an Anthropic cache read costs 0.1x the base input price (0.05x on Opus 5.5 and Sonnet 5.5) [VF: A5-S004, V2-S002]. Regional processing costs about 10% more on Bedrock regional endpoints for Claude, non-global Google Cloud endpoints and Mistral's EU endpoint [VF: A5-S011, A5-S027, A5-S075]. Stable prompt prefixes, an asynchronous path and a small model tier are architecture decisions that set the margin [AJ].

**5. Multi-tenant isolation has primary guidance, but no single standard.** Microsoft's guidance sets out four isolation models for Azure OpenAI, warns that a shared resource gives no security segmentation per deployment, and says not to share an instance when using fine-tuned models [VF: E2-S016]; tenants must agree before their data trains a shared model [VF: E2-S015]. AWS describes silo, pool and bridge patterns for multi-tenant retrieval, with per-tenant KMS keys in the silo and automatic tenant-filter injection in the pool [VF: E2-S050]. OWASP's LLM08:2025 names cross-context leakage in multi-tenant vector stores [VF: E2-S051], but no OWASP item on tenant isolation was found [NPV]. Prefix-cache-aware routing and tiered KV-cache stores are now standard in serving stacks [VF: A4-S091, A4-S090, A4-S089], and a cache shared across tenants can carry one request's context into another's [AJ]; Apigee fixed an SSRF in its semantic-cache lookup on 30 September 2026 [VF: A6-S025]. The provider must write its own tenancy standard, with a tenant key in the address of every cache, memory and checkpoint [AJ].

**6. The provider sits in two regulatory positions at once.** It is regulated in its own right under NIS2, the Product Liability Directive and AI Act Article 50 (XIII.6) [VF: E1-S017, E1-S010, E1-S035]. It is also a third party in its regulated customers' books: DORA Article 30 clauses and subcontracting rules reach it and, through it, its model API vendors [VF: E1-S055, E1-S057]. The FS view is, in effect, the provider's most demanding customer [AJ].

**7. Customer assurance has an AI-specific format.** CSA's AI Controls Matrix maps control by control to ISO/IEC 42001, and STAR for AI Level 1 is a published AI-CAIQ self-assessment, Level 2 an ISO/IEC 42001 certificate plus a scored AI-CAIQ [VF: E2-S047]. Certification against ISO/IEC 27001 is now to the 2022 edition only [R: E2-S046], and SOC 2 is still assessed against the 2017 Trust Services Criteria [R: E2-S048]. Publishing an AI-CAIQ answers most AI questionnaires once [AJ].

**8. The provider's customers will be able to switch away from it for free.** From 12 January 2027 cloud and SaaS providers may not charge for switching, including egress, and must export customer data in a machine-readable format [VF: E1-S025, E1-S026]. Whether tenant prompts, fine-tuned weights, embeddings or agent configurations are exportable data under the Act is not settled [NPV]. The provider's own portability engineering therefore faces outwards, towards its tenants [AJ].

## XIII.3 Scoring for this view

**The weights.** The view re-weights the same eight criterion scores that the FS view uses; no product fact or criterion score changes [AJ]. The weights are architectural judgement (views.json) [AJ]:

| Criterion | FS weight | TS weight | Why it moves [AJ] |
|---|---:|---:|---|
| Technical | 15 | 15 | Unchanged |
| Enterprise readiness | 15 | 15 | Unchanged: tenants still need SSO, audit and support |
| Security and compliance | 20 | 15 | Still high, but no model-risk regime applies directly |
| Deployment flexibility | 15 | 10 | The provider chooses where its own service runs |
| Ecosystem | 5 | 10 | Developer productivity and integrations matter to a product team |
| Reliability and maturity | 10 | 15 | Service levels are what customers buy |
| Cost and TCO | 5 | 15 | Every call is cost of goods sold |
| Lock-in and portability | 15 | 5 | One estate the provider controls; exit is a lesser risk |

**What moves, and why.** The largest gains go to low-cost managed services whose weakness was lock-in: Model Armor (C2) rises from 3.35 to 3.70 on cost 5, and Amazon S3 Vectors (L6), Voyage AI (L7) and Cloudflare AI Gateway (C1) each gain 0.30 on cost 4 or 5 (`TS_scores.md`) [AJ]. Sensitive Data Protection rises 0.25 on reliability 5 [AJ]. The largest falls go to portable products whose advantage was lock-in or deployment: Milvus/Zilliz drops 0.25, and llm-d, Unstructured and Presidio fall because their 5s on lock-in and deployment now weigh less [AJ].

**Fit changes against FS.** Core candidates number 48 under these weights, against 45 under FS, of 138 scored products (`TS_scores.md`) [AJ]. Eleven products change fit [AJ]:

| Becomes a core candidate under TS | Master tier | FS → TS | Becomes situational under TS | Master tier | FS → TS |
|---|---|---|---|---|---|
| MCP (L4); Anthropic-originated, alternative OpenAPI tools | Strategic, conditional | 3.55 → 3.60 | A2A (L4) | Strategic, conditional | 3.70 → 3.55 |
| AgentCore Gateway and Identity (L4) | Strategic, conditional (AWS) | 3.45 → 3.60 | Fireworks AI (L2) | Strategic, conditional | 3.65 → 3.55 |
| Zep and Graphiti (L5) | Tactical | 3.50 → 3.60 | Presidio (C3) | Strategic, conditional | 3.65 → 3.45 |
| Arize Phoenix (L9) | Tactical | 3.50 → 3.65 | Prompts-as-code pattern (C5) | Strategic | 3.65 → 3.55 |
| Promptfoo (L9) | Tactical | 3.55 → 3.60 | | | |
| Model Armor (C2) | Strategic, conditional (Google Cloud) | 3.35 → 3.70 | | | |
| Okta and Auth0 for AI Agents (C4) | Strategic, conditional | 3.55 → 3.60 | | | |

**How to read the fit.** The fit is computed and indicative; the master tiers and their conditions still stand, and the condition is the decision, not the total (Part I.3) [AJ]. This view keeps two products the computed fit demotes. Presidio stays the cloud-neutral privacy engine because a processor needs in-estate detection it controls, and its drop comes only from lower weights on its strengths [AJ]. Prompts-as-code stays the configuration of record because per-tenant overlays need Git history more than a single firm does [AJ]. Conversely, Zep, Phoenix and Promptfoo becoming core candidates does not change their Tactical master tier: Phoenix remains under ELv2 [VF: A1-S048], and Promptfoo's announced owner is a model vendor [VF: A1-S024].

**Anthropic.** The Claude family moves from third to second in L1 (3.80 → 3.85), behind OpenAI (4.20), mainly because Mistral's strengths in deployment and lock-in now weigh less (3.85 → 3.80); its lowest criteria remain deployment flexibility 3 and reliability 3 (`TS_scores.md`) [AJ]. Its master tier is Strategic, conditional (hyperscaler UK/EU route, non-Anthropic fallback; independent alternatives GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5) [AJ].

**Where to find the full table.** Every product's FS and TS score, rank and fit is in `05_Data/views.xlsx`; the per-layer listing is `work/stageE/views/TS_scores.md` [AJ].

## XIII.4 The architecture for this view

The FS architecture (Part IV.1) is kept layer for layer; what changes is that tenant identity becomes a dimension of every component, and cost and customer evidence become outputs of the same telemetry spine [AJ]. The control plane is still one estate, but it is one estate serving many customers, so every decision point (identity, gateway, policy, configuration) resolves a tenant before it resolves anything else [AJ].

![The technology service provider's GenAI architecture: one estate, every call tenant-aware](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/TS-1.png){width=100%}

*Figure: The provider runs one control plane for all tenants: tenant identity travels in every token, the gateway meters, limits and routes per tenant, the knowledge plane is partitioned by tenant (pooled by default, siloed for tenants who pay for it), and every span carries the tenant ID so cost, margin and customer evidence can be reported per tenant. Editable source: `08_Graphic/diagrams/TS-1.md`.* [AJ]

**Three tenancy tiers, one code path.** The architecture offers three isolation tiers built from the same components, following the pool, bridge and silo patterns [VF: E2-S050, E2-S053] [AJ]:

| Tier | Model plane | Knowledge plane | Who buys it [AJ] |
|---|---|---|---|
| Pooled (default) | Shared deployments; per-tenant virtual key, quota and budget | Shared index; tenant filter injected server-side from the token, never from the prompt | Most tenants |
| Bridged | Shared deployments; dedicated provisioned capacity or region for the tenant | Partition or namespace per tenant; per-tenant encryption key | Regulated tenants, tenants with residency clauses |
| Siloed | Dedicated deployment, or the tenant's own model account | Own index and key; deployment stamp per tenant | Tenants that pay for single-tenancy or bring fine-tuned models |

Fine-tuned models always sit in the siloed tier, because Microsoft's guidance warns that a shared resource gives no security segmentation per deployment [VF: E2-S016]. The tenant-provided model account is a recognised pattern for customers with their own quota, content-filter policy or provisioned throughput [VF: E2-S016].

**Four properties the design must prove [AJ].** A tenant can never retrieve, cache-hit or trace-read another tenant's content; every model call is attributable to a tenant, a feature and a price; a tenant's AI setting (on, off, region, model route) is configuration, changed without a release; and a vendor outage or suspension degrades the service to the fallback route rather than stopping it.

## XIII.5 Layer by layer, then control by control

Each row gives the provider's default and how it departs from the FS defaults (Part I.2, Part VII Stack A). Master tiers are quoted unchanged [AJ].

| Layer / control | Default choice for this view | Change from the FS view | Why |
|---|---|---|---|
| L1 models | Two unrelated mid-tier vendors plus a small tier: OpenAI GPT (Strategic) with Claude (Strategic, conditional) or Mistral (Strategic); Claude's independent alternatives GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5 | First-party APIs acceptable for tenants without residency needs; EU/UK tenant data stays on an in-region route; heavy small-tier use | OpenAI has first-party EU processing [VF: A5-S006]; Claude has no first-party EU/UK inference [VF: V2-S075]; prices span US$0.10–10 per 1M input within a family [VF: A5-S004, A5-S011] |
| L2 inference | Primary cloud's model service with reserved capacity for peaks, Batch or Flex for asynchronous work; vLLM (Strategic) only for one high-volume open model | Capacity tiers are a service-level design, not an exit drill; Fireworks becomes situational | Bedrock, Foundry and OpenAI capacity tiers [VF: E2-S032, E2-S017, E2-S033] |
| L3 orchestration | LangGraph (Strategic) + Temporal (Strategic); Microsoft Agent Framework (Strategic) in .NET estates | Same choice; tenant ID and overlay become workflow inputs | Deterministic workflows remain the default [VF: A4-S039, B-L3-S002] |
| L4 tools | Tenant tools through the tool gateway with per-tenant delegated tokens; MCP (Strategic, conditional; alternative OpenAPI tools) | The provider is itself the multi-tenant token holder the FS view rejects in a third party, so it must engineer per-tenant vaulting | A broker holding every user's tokens is a concentrated target [VF: B-L4-S007] [AJ] |
| L5 memory | None at first; later per-tenant memory on L6 | Zep (Tactical) is a core candidate on score, but memory stays last | Memory poisoning is ASI06 [VF: B-L5-S001] |
| L6 stores | pgvector (Strategic) partitioned by tenant; Qdrant (Strategic) for many-tenant filtered search; S3 Vectors (Tactical) as AWS cost tier | Tenant isolation replaces intra-firm entitlement as the defining duty | Qdrant tiered multitenancy [VF: A2-S103]; S3 Vectors US$0.06 per GB-month [VF: A2-S087] |
| L7 retrieval optimisation | OpenAI text-embedding-3 (Tactical) or Cohere (Tactical); Sentence Transformers (Strategic) as exit | Hosted embeddings rise on cost; per-tenant re-embedding planned | A model change re-embeds every tenant's index [AJ] |
| L8 ingestion | Docling (Strategic) and Unstructured (Strategic) connectors with per-tenant credentials | Per-tenant deletion on exit is contractual | Data Act switching [VF: E1-S025] |
| L9 evaluation | OTel Collector with tenant ID on every span; Langfuse (Strategic) or MLflow (Strategic); DeepEval (Tactical); Promptfoo (Tactical) plus an independent red-team tool | Suites run globally and per tenant; tenant data in evaluation needs consent | OTel GenAI conventions still Development [VF: A1-S058]; consent for shared training [VF: E2-S015] |
| C1 gateway | LiteLLM (Strategic, conditional), pinned and signed, a virtual key per tenant and feature | Per-tenant keys, quotas, budgets and caches | Per-tenant spend reports [VF: A7-S070, A6-S015]; PyPI compromise [VF: A6-S008] |
| C2 guardrails | Primary cloud's managed detector (Model Armor, Bedrock Guardrails, Azure AI Content Safety; Strategic, conditional) plus per-tenant deterministic policy | Managed detectors rise on cost | Model Armor free to 2 million tokens a month, then US$0.10 per 1M [VF: A6-S067] |
| C3 privacy | Presidio (Strategic, conditional) behind a privacy-service API; Sensitive Data Protection on Google Cloud | Per-tenant entity policy; redaction before models and in traces | Kept despite a situational computed fit [AJ] |
| C4 identity | Provider CIAM or Okta/Auth0 for AI Agents (Strategic, conditional), with OPA (Strategic) | Customer identity replaces the workforce IdP; tenant is a mandatory claim | Auth0 Token Vault brokers API tokens for agents [VF: A6-S099] |
| C5 configuration | Git manifest with tenant overlays; Langfuse Prompts (Strategic) labels for variants | AI on/off, region, route and tone are configuration | Labels can assign versions to tenants [VF: A7-S072] |
| C6 FinOps | Gateway attribution (Strategic) to tenant, feature and plan in a FOCUS (Strategic)-shaped dataset joined to billing | From reporting to gross-margin control | Batch and caching halve unit cost or better [VF: A5-S004, V2-S002] |
| C7 security | Vault (Strategic, conditional) with per-tenant paths; scanning (Strategic); tenant content as untrusted input | Cross-tenant injection; NIS2 incident duties | NIS2 24-hour early warning [VF: E1-S016] |
| C8 governance | Evidence store keyed by trace and tenant; OpenLineage (Strategic); customer assurance pack | Customer assurance replaces model-risk validation | STAR for AI [VF: E2-S047]; ISO/IEC 42001 [VF: A8-S045] |

## XIII.6 Regulation, contracts and customer assurance

**The FS anchors apply only indirectly.** SR 26-2 and PRA SS1/23 govern the regulated firm, not its suppliers, and SR 26-2 places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001]. The provider meets them as evidence its FS customers request; its own duties are below [AJ].

| Regime | What applies to a provider | Date | Consequence [AJ] |
|---|---|---|---|
| AI Act Article 50 | Supplying an AI system under its own name makes the provider its provider [VF: A8-S016]; chat features disclose AI; generated content is marked; pre-August 2026 systems have until 2 December 2026 for marking [VF: E1-S035, E1-S036] | Since 2 Aug 2026; marking for systems already on the market by 2 Dec 2026 | Disclosure and marking as tenant settings with a provider floor |
| AI Act roles | Fine-tuning makes an integrator a GPAI provider only above one third of original training compute [VF: E1-S034] | In force | Per-tenant tuning does not normally make the provider a GPAI provider |
| NIS2 | Cloud, MSP and MSSP providers, medium and large, in scope [VF: E1-S017, E1-S018]; 24-hour, 72-hour, one-month reporting [VF: E1-S016]; supply-chain policy reaching model vendors [VF: E1-S019]; management liability [VF: E1-S016] | Per transposition [NPV] | Model vendor incidents feed the provider's incident process |
| Product Liability Directive | Software, including SaaS, is a product from 9 December 2026 [VF: E1-S010, E1-S011, E1-S012]; the AI Liability Directive was withdrawn [VF: E1-S014] | 9 Dec 2026 | Agents that can delete a person's data need approval gates |
| Cyber Resilience Act | A hosted service is in scope only as the remote processing of a product supplied, such as an SDK [VF: E1-S001] [R: E1-S007]; main obligations from 11 December 2027 [VF: E1-S002] | 11 Dec 2027 | Keep installable components few, with SBOMs |
| Data Act | No switching charges from 12 January 2027; export in machine-readable form [VF: E1-S025, E1-S026] | 12 Jan 2027 | Tenant export of prompts, overlays, content and evidence |
| UK Cyber Security and Resilience Bill | Would bring medium and large MSPs into the NIS Regulations; before the Lords on 9 October 2026 [VF: E1-S021, E1-S022, E1-S023] | Not law | Plan ICO registration |
| US state laws | Colorado's replacement law is stayed [VF: E1-S038, E1-S040]; California ADMT rules from 1 January 2027 [VF: E1-S047] | 1 Jan 2027 | Only features assisting consequential decisions are caught |

**What FS customers will impose.** DORA Article 30 clauses cover service description, subcontracting, data locations, return of data on exit, service levels, incident assistance, termination and resilience training [VF: A8-S021, E1-S055]; critical functions add exit strategies and on-site audit [VF: E1-S056]. The provider must name its subcontractors, including model API vendors, pass audit rights down and let the customer object to material changes [VF: E1-S057]. UK customers notify material third parties from 18 March 2027 [VF: R-PRA-SS221, A8-S062]. Expect FS customers to ask for the parts of Part V.8's evidence register that touch the service [AJ].

**Flow-down and subprocessors [Rec].** The provider's terms should carry each model vendor's usage policy to end users [VF: E2-S005], the AI-disclosure and high-risk human-review duties [VF: E2-S005], Google's under-18 and clinical-use bars [VF: E2-S007], and Anthropic's requirement that users be told not to rely on factual outputs unchecked [VF: E2-S004]. Model vendors are subprocessors: Anthropic's DPA gives prior notice of new subprocessors with a right to object [VF: E2-S012], and every route, fallbacks included, belongs on the provider's own list before it carries tenant data. Anthropic's Usage Policy effective 12 November 2026 has not been compared with the current text [NPV].

**The customer assurance pack [Rec].** SOC 2 Type II [R: E2-S048]; ISO/IEC 27001:2022 [R: E2-S046]; an AI-CAIQ at STAR for AI Level 1, then Level 2 with ISO/IEC 42001 [VF: E2-S047, A8-S045]; the model vendors' own assurance [VF: A5-S021, A5-S007, V2-S062, A5-S028, A5-S075]; the subprocessor list; the tenancy standard; and a register of AI features with their routes, data use and opt-out controls.

## XIII.7 Reference stack

Stack A's control plane (Part VII), made tenant-aware, with managed services accepted where cost and reliability win. S, T and E abbreviate the master tiers; hyperscaler model services are access patterns, not scored (Part I.3) [AJ].

| Layer / control | Cloud-neutral | AWS primary | Azure primary | Google Cloud primary |
|---|---|---|---|---|
| L1 models | OpenAI GPT (S) + Claude (S, cond.; alternative GPT-6.1 Sol or Mistral Medium 3.5) or Mistral (S) | Claude Sonnet 5.5 or a GPT-6 tier on Bedrock (confirm EU availability [VF: A5-S008, V2-S079]) | GPT-6.1 Sol in a Foundry Data Zone; Mistral fallback | Gemini (S, cond.), not for tenants serving under-18s [VF: E2-S007]; Claude or Mistral fallback |
| L2 capacity | Standard + reserved + Batch/Flex; vLLM (S) for one open model | Bedrock Reserved / Priority / Flex [VF: E2-S032] | Foundry Provisioned with spillover [VF: E2-S017] | Provisioned Throughput [VF: A5-S027] |
| L3 orchestration | LangGraph (S) + Temporal (S) | Strands on AgentCore (S, cond.) | Microsoft Agent Framework (S) | ADK on Agent Engine (S, cond.) |
| L4 tools | Tool gateway; MCP (S, cond.; alternative OpenAPI tools) | AgentCore Gateway + Identity (S, cond.) | APIM AI gateway (S, cond.) | Apigee MCP (S, cond.) |
| L6 stores | pgvector (S); Qdrant (S) | + S3 Vectors (T) cost tier | pgvector on Azure Database for PostgreSQL | pgvector on Cloud SQL |
| L7 embeddings | text-embedding-3 (T) or Cohere (T); Sentence Transformers (S) | Cohere or Voyage on SageMaker (T) | Cohere on Foundry (T) | Gemini Embedding 2 (S, cond.) |
| L8 ingestion | Docling (S) + Unstructured (S) | Same | Same | Document AI (S, cond.) |
| L9 evaluation | Langfuse (S) or MLflow (S); DeepEval (T); Promptfoo (T) + independent tool | MLflow on SageMaker | MLflow on Azure ML | Langfuse self-hosted |
| C1 gateway | LiteLLM (S, cond.) | + AgentCore Gateway for tools | APIM GA policies (S, cond.) | Apigee (S, cond.) |
| C2 guardrails | Per-tenant policy + NeMo Guardrails (T) | Bedrock Guardrails (S, cond.) | Azure AI Content Safety (S, cond.) | Model Armor (S, cond.) |
| C3 privacy | Presidio (S, cond.) | Presidio | Presidio; Purview DSPM (S, cond.) for posture | Sensitive Data Protection (S, cond.) |
| C4 identity | Provider CIAM or Okta/Auth0 (S, cond.) + OPA (S) | AgentCore Identity + Cedar policy (S) | Entra Agent ID (S, cond.) for staff | Okta/Auth0 + OPA |
| C5–C8 | Git with tenant overlays; gateway cost + FOCUS (S); Vault (S, cond.); evidence store + OpenLineage (S) | + application inference profiles [VF: B-C6-S004] | + Foundry project tags [VF: B-C6-S005] | Gateway metering |

**Do not build yet [Rec].** Per-tenant fine-tuning; long-term memory; autonomous agents with write tools; A2A; a GPU fleet beyond one open model; a dedicated vector engine without a failed load test; a governance platform; any Experimental product, including the Claude Agent SDK (alternatives LangGraph, Pydantic AI or the OpenAI Agents SDK) [VF: A4-S006, B-REVC-S001].

## XIII.8 Build vs buy, and lock-in

**The rule changes in one place.** Part VIII's rule stands; for a provider, the tenancy model and unit economics are part of the control statement, so they move into the build column [AJ]:

| Component | FS decision (Part VIII) | TS decision | Why [AJ] |
|---|---|---|---|
| Tenancy enforcement (tenant claim, filter injection, cache and key partitioning) | Not a separate component | **Build** | No profiled product enforces tenancy end to end |
| Cost per tenant and pricing data (C6) | Build (thin) | **Build, product grade** | Margin depends on it |
| Identity for agents (C4) | Buy the workforce IdP | **Buy CIAM, build the tenant model** | Agents act for tenants' users |
| Detectors (C2, C3) | Hybrid, swappable | **Buy managed, keep the policy** | Cost and reliability favour managed detectors |
| Evaluation (L9) | Hybrid | **Hybrid, per-tenant suites** | Large tenants' acceptance tests become regression sets |

**Lock-in, reread.** Lock-in weighs 5% because the provider can migrate on its own schedule [AJ]. Three lock-ins still matter. A single model vendor is a service-level risk, given suspension for tenants' misuse [VF: E2-S004] and the suspension of Fable 5 access from 12 June to 1 July 2026 [VF: V2-S004]. Billing intermediation puts a third party in the margin, and OpenRouter's sale to Stripe is pending [VF: V1-S059]. Ownership churn (Portkey to Palo Alto Networks, Langfuse to ClickHouse, Arize to Dynatrace, Promptfoo to OpenAI, announced) turns each embedded tool's change of control into a subprocessor notice [VF: A6-S011, A1-S021, A1-S045, A1-S024] [AJ].

**The inverse lock-in [Rec].** Make the service easy to leave, because the Data Act removes switching charges from 12 January 2027 [VF: E1-S025]: keep each tenant's prompts, overlays, content, evaluation sets and evidence exportable in open formats (Git, OTel, OpenLineage, FOCUS). Embeddings can be regenerated if raw text is kept [AJ].

## XIII.9 Roadmap

**Size.** Twelve months, October 2026 to September 2027, for a platform team of six to ten engineers shipping one feature first. The order follows Part X, without a model-validation phase and with tenancy and assurance added [AJ].

| Date | Event | Consequence [AJ] |
|---|---|---|
| 2 December 2026 | Article 50 marking deadline for systems already on the market [VF: E1-S036] | Disclosure and marking live before GA |
| 9 December 2026 | PLD applies [VF: E1-S011] | Write-capable agents behind approval gates |
| 1 January 2027 | Gemini 3.8 Flash price doubles [VF: A5-S027, V2-S010] | Re-price Google routes |
| 12 January 2027 | Data Act: no switching charges [VF: E1-S025] | Tenant export ready |
| 18 March 2027 | UK FS customers' third-party notifications [VF: R-PRA-SS221, A8-S062] | Assurance pack and DORA clauses ready |
| 11 December 2027 | CRA main obligations [VF: E1-S002] | SDKs and connectors inventoried from Phase 4 |

**Phases [Rec]:**

| Phase (months) | Scope | Exit criterion |
|---|---|---|
| 0 Terms, tenancy, assurance (0–2) | Tenancy standard; vendor terms flowed down; two vendors and primary cloud chosen; subprocessor list; AI-CAIQ started; Article 50 features identified | Standard approved; vendor due diligence filed as NIS2 supply-chain evidence [VF: E1-S019] |
| 1 Telemetry and evaluation (1–3) | Collector with tenant ID and redaction; Langfuse or MLflow; CI harness; cross-tenant leak test and canary tenant | Every span carries tenant and feature; leak test blocking |
| 2 Gateway, metering, capacity (2–5) | Gateway twice, per-tenant keys, quotas, budgets, kill switch; two routes qualified; Batch route; cost dataset joined to billing | Fallback drill under load; cost per call reported per tenant |
| 3 First feature, pooled (4–7) | The worked example with tenant settings, opt-out, approval and evidence | Tenants live; edit rate and cost per accepted draft reported |
| 4 Premium tenancy, FS customers (6–9) | Bridged and siloed tiers; region-pinned routes; tenant model accounts; DORA clause set; tenant export; CRA inventory | FS due diligence passed; export tested |
| 5 Tools and optimisation (9–12) | Read-only tenant tools with delegated tokens; caching; small-tier routing; memory and tuning review | Optimisations pass regression; margin on plan; ISO/IEC 42001 decision |

## XIII.10 Worked example: drafting replies on a multi-tenant support platform

**The use case.** A multi-tenant customer-support platform adds an agent that drafts replies to its customers' end users from each tenant's own knowledge base, with a human support agent approving each reply; tenant isolation, per-tenant cost and the customer's right to opt out of AI are the hard parts (views.json) [AJ]. Like Part VI, this is a deterministic workflow with one bounded drafting step and a named approver; unlike Part VI, every step resolves a tenant first: whose content, policy, region, budget and evidence [AJ].

| Step | What happens | Components |
|---:|---|---|
| 0 | Release manifest pinned (prompt, models, embedding, guard policy, thresholds) with tenant T's overlay: AI on, EU region, tone, disclosure | C5 |
| 1 | T's support agent signs in through T's IdP federated to the provider's CIAM; token carries tenant, user and role | C4 |
| 2 | Opt-out check (tenant setting and end-user flag); if off, manual path, decision logged | L3, C5 |
| 3 | Workflow starts; T's quota and budget checked | L3, C1, C6 |
| 4 | Ticket redacted (payment cards, secrets, T's entities) and screened as untrusted input | C3, C2, C7 |
| 5 | `retrieve(query, tenant=T)`: filter injected server-side from the token; hybrid search in T's partition; rerank; chunks carry article ID and version | L7, L6, L8 |
| 6 | Optional read-only `get_order_status` in T's system, with a delegated token from T's vault path | L4, C4, C7 |
| 7 | Drafting call on route `support-draft` with T's key, EU route, T-scoped prefix cache, qualified fallback | C1, L2, L1 |
| 8 | Output guards: other tenants' canaries absent; PII re-check; T's policy (no promises beyond its rules); every claim cites a T article | C2, C3 |
| 9 | Draft shown labelled as AI-drafted; the support agent edits, approves or discards, and sends under their own identity | L3, C4 |
| 10 | Spans tagged with tenant and feature; sampled evaluation within T's consent; edit distance captured | L9 |
| 11 | Usage (tokens, cache hits, route, cost) to the cost dataset and T's bill; evidence record to T's partition, deleted on T's exit | C6, C8 |

**What it costs [AJ].** At US$2 input and US$10 output per 1M tokens (GPT-6.1 Sol and Claude Sonnet 5.5 list prices, as in Part VI [VF: A5-S011, A5-S004]), an assumed draft of 6,000 input and 400 output tokens costs about US$0.016; caching a 3,000-token stable prefix at OpenAI's US$0.10 cached rate [VF: A5-S004] brings it to about US$0.010. The token counts are the author's assumptions. Across millions of tickets a month this is cost of goods sold, so caching, the small tier and the discard rate are the levers [AJ].

**Is disclosure required?** The end user receives a reply sent by a human reviewer, not a conversation with the AI [AJ]. Anthropic's disclosure rule targets chatbots or agents that talk directly to external users [VF: E2-S005], and Article 50 covers systems that interact with people [VF: E1-S035]. Whether a reviewed draft triggers disclosure is a legal question; the architecture makes it a tenant setting defaulting to on [Rec].

**May [Rec]:** draft from T's knowledge base and ticket history; look up status through T's read-only tools; cite articles by version; flag knowledge-base gaps to T's administrators.

**Must never, and what enforces it [Rec]:**

| Never | Enforced by |
|---|---|
| Retrieve, cite or cache another tenant's content | Server-side tenant filter (L6); tenant-scoped caches (C1, L2); canary tests (L9, C2) |
| Run where AI is opted out | Overlay and end-user flag checked first (C5, L3) |
| Send without human approval | Approval step; send uses the human's identity (L3, C4) |
| Promise beyond T's policy, or call a write tool | Tenant-policy guard (C2); read-only scopes (L4, C4) |
| Send card numbers or secrets to a model | Privacy service before the gateway (C3) |
| Exceed T's budget or slow other tenants | Per-tenant key, quota and budget, fail closed (C1, C6) |
| Train a shared model on T's tickets | No training route; consent for evaluation use [VF: E2-S015] |
| Route an EU tenant outside the EU | Region-pinned route in T's overlay (C1, C5) |

**Evidence kept [Rec]:** manifest and overlay versions with the AI setting at run time; model ID, version, region, fallback and cache flags; tenant partition, article versions and index versions; tool-call hashes, delegated identity and policy decision; guard and evaluation verdicts; the support agent's decision and edit diff; tokens, price version and cost charged; and whether disclosure was shown. Release history, evaluation records and logs are the provider's main defence under the PLD [VF: E1-S010] [R: E1-S013].

## XIII.11 Checklist, what to avoid, what to monitor

**Checklist [Rec]:**
- A tenancy standard with pooled, bridged and siloed tiers, and a blocking cross-tenant leak test.
- Tenant, user and agent in every token; filters injected server-side; every cache, memory and store addressed by tenant.
- One gateway with per-tenant keys, quotas, budgets and kill switch; two vendors, the fallback sized for real load, with a non-Anthropic fallback for any Claude route (GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5).
- Batch, caching and a small tier in every feature; cost per tenant and feature reported against price.
- Vendor terms flowed down; every route on the subprocessor list before it carries tenant data.
- Tenant AI settings as configuration; tenant export in open formats.
- The assurance pack, and NIS2 and CRA runbooks that include model vendor incidents.

**Avoid [Rec]:** a resold pass-through model API [VF: E2-S004, E2-S026]; a shared Azure OpenAI resource for fine-tuned models [VF: E2-S016]; tenant filters applied after ranking or taken from model output; shared caches across tenants [VF: A6-S025]; Google generative AI routes for tenants likely to serve under-18s [VF: E2-S007]; shared-model training on tenant data without agreement [VF: E2-S015]; Helicone for new adoption, and Composio's managed cloud for tenant tokens [VF: A7-S112, B-L4-S007]; SLAs the model routes cannot meet, since Flex can return 429 [VF: E2-S031].

**Monitor [Rec]:**

| Monitor | Trigger |
|---|---|
| Vendor capacity terms (Anthropic Priority Tier withdrawn; OpenAI Reserved; Bedrock and Foundry tiers) [VF: E2-S006, E2-S033, E2-S032, E2-S017] | Re-plan capacity and SLAs quarterly |
| Anthropic Usage Policy effective 12 November 2026 [VF: E2-S005] | Update tenant flow-down |
| Gemini prices and Flash retirements [VF: V2-S010, B-L1-S003] | Re-price and re-qualify |
| OpenRouter–Stripe and Promptfoo–OpenAI closings [VF: V1-S059, A1-S024] | Refresh due diligence and subprocessor notices |
| NIS2 transposition in the main-establishment state [NPV]; UK Bill [VF: E1-S021]; COM(2026) 13 on MSP outsourcing [R: E1-S020] | Confirm status and duties |
| Data Act SME carve-out [VF: E1-S027]; exportability of embeddings and configurations [NPV] | Adjust export and terms |
| OWASP tenant-isolation guidance beyond LLM08 [VF: E2-S051]; OTel GenAI conventions [VF: A1-S058] | Re-map the tenancy standard; re-pin attributes |
