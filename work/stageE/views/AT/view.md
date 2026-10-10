# Part XVI: The view for start-ups selling AI tools into the enterprise stack

**In brief.**
- **Who it is for.** An early-stage company whose product is itself a component of the Enterprise GenAI Stack: a gateway, guardrail, privacy, evaluation, observability, retrieval, ingestion, memory or governance tool, sold to the platform, security and model-risk teams that Parts I–XII describe (views.json) [AJ].
- **What changes.** The FS view designs the buyer's control plane. This view stands on the other side of the table: the start-up's product must become one replaceable call-out inside that plane, run where the buyer's data is, write its evidence into the buyer's stores and survive the buyer's third-party due diligence [AJ].
- **The hard truth.** The FS buyer is told to treat every product beneath its control plane as replaceable, to own the interface and the evidence, and to treat a change of owner as a third-party event (Part I.2, Part V.3). A tools start-up wins by designing for that posture, not against it [AJ].
- **The view at end of Q3 2026.** Evidence read on 9–10 October 2026; credits, certifications and acquisition statuses are volatile and re-verified each quarter [AJ].

> **Conflict-of-interest disclosure.** The author is an Anthropic model. Under this view's weights the Model Context Protocol (Anthropic-originated, now under the Agentic AI Foundation) rises to first in L4 and MCP Authorization becomes a core candidate in C4; both movements come from the same criterion scores as every other product, re-weighted by `tools/build_views.py`. Wherever a Claude model, MCP, MCP Authorization or Agent Skills is named as a choice, an independent alternative is named beside it [AJ].

## XVI.1 Who this view is for

**Profile.** The company has between four and twenty people, a product that sits at one layer or control of the stack, and buyers who are large or regulated enterprises (views.json) [AJ]. Its customers' platform teams have already built, or are building, the firm-owned control and evidence plane of Part I.2: one gateway of record, a firm-owned OpenTelemetry Collector, a privacy service, agent identities in the workforce IdP, Git as the configuration of record and an immutable evidence store [Rec]. The start-up sells into that plane.

**Assumptions.** The product ships in two forms, a SaaS edition in an EU region and a container the customer runs in its own cloud account; it may call models internally (for example an LLM-based recogniser or judge); its first enterprise customers include at least one EU or UK financial firm; and it has no compliance function yet, only founders who answer questionnaires [AJ].

**The five biggest differences from the FS view [AJ]:**

| # | FS view (Parts I–XII) | AI-tools start-up view | Consequence for the architecture |
|---:|---|---|---|
| 1 | The firm builds one control plane and treats products beneath it as replaceable | The start-up *is* one of those replaceable products | Design for the buyer's abstraction: an open interface, the buyer's identity, the buyer's telemetry and the buyer's evidence store; never require the buyer to route around its own gateway [AJ] |
| 2 | Deployment flexibility is a selection criterion (15%) | Deployment flexibility is the product's own engineering burden | One code path that runs as SaaS, as a private-endpoint SaaS and as a container in the customer's account, with no customer content reaching the vendor plane [AJ] |
| 3 | Ecosystem weighs 5% | Ecosystem weighs 15% | Open standards (OpenAI-compatible APIs, OTel GenAI spans, MCP or OpenAPI, OPA, FOCUS, OpenLineage) are distribution, because they are how the product plugs into what the buyer already runs [AJ] |
| 4 | The firm is a deployer and an outsourcer | The start-up is an ICT third party, possibly an AI-system provider, a CRA manufacturer for its container, and a component supplier under the PLD | Customer assurance, contract flow-down and vulnerability reporting are product features, not paperwork [AJ] |
| 5 | Ownership changes are a risk to manage | Ownership changes are the market's main exit route, and the buyer's main objection | Independence, data portability and change-of-control commitments become part of the pitch [AJ] |

## XVI.2 Findings that change for this view

**1. The buyer's architecture already assigns the start-up's place, and it is a call-out.** The FS view's twelve decisions make the gateway the route for all model, MCP and agent traffic, make detectors "swappable call-outs behind the gateway", and keep policy, test sets and evidence in firm-owned stores (Part I.2, decisions 1, 3 and 11) [Rec]. The gateways expose the hooks: LiteLLM runs guardrails pre-call, during the call and post-call across chat, embeddings, MCP and A2A routes; Kong integrates the three clouds' guardrail services and NeMo Guardrails; APIM applies Content Safety to MCP and A2A payloads; Apigee calls Model Armor inline [VF: A6-S015, A6-S017, A6-S020, A6-S024]. Whether each gateway accepts a generic call-out to an arbitrary third-party service was not verified per product [NPV]. A tool that cannot be invoked from the gateway, or that insists on being the gateway, is asking the buyer to undo its architecture [AJ].

**2. "Neutral" tools are being bought, and buyers now price that in.** Dynatrace completed its acquisition of Arize on 1 October 2026; ClickHouse acquired Langfuse; OpenAI announced its acquisition of Promptfoo; Palo Alto Networks bought Protect AI and Portkey; Check Point bought Lakera; Harvey bought Guardrails AI; Mintlify bought Helicone; Nebius bought Tavily; MongoDB owns Voyage and Elastic owns Jina [VF: A1-S045, V1-S005, A1-S021, V2-S041, A1-S024, V1-S006, A7-S014, A6-S012, V2-S025, A7-S012, A6-S028, A7-S112, V2-S043, V1-S041, A2-S033, A2-S023]. In the FS view each of these is a third-party event, and from 18 March 2027 a significant change to a material arrangement needs advance notification [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. An acquisition is therefore both the start-up's likeliest exit and the buyer's first due-diligence question [AJ].

**3. Incumbents are bundling the function the start-up sells.** DLP now sits inside Cloudflare AI Gateway, Kong AI Gateway, Bedrock Guardrails and Model Armor [VF: A6-S052, A6-S016, A6-S072, A6-S067]. Palo Alto Networks bought Portkey to place a gateway "in the traffic path" of Prisma AIRS, which reached GA as an AI gateway on 16 July 2026 [VF: A6-S011, V2-S048]. AWS and Google ship memory inside their agent platforms [VF: V1-S087, V1-S088]. The FS view tells buyers to keep the gateway choice separate from the detector choice and to record bundles in the exit plan (Part V.6) [Rec]. A start-up's opening is the unbundled, portable, evidence-producing component that a buyer wants beside an incumbent's bundle [AJ].

**4. The free, open baseline is the real competitor.** The FS view's cloud-neutral defaults are open or open-core: Presidio (MIT, community-governed), Docling (MIT, LF AI & Data Graduate), OPA and SPIFFE/SPIRE (CNCF graduated), Langfuse (MIT core), MLflow and vLLM (Apache-2.0) [VF: A6-S040, V2-S030, V1-S091, A6-S046, A6-S087, A1-S033, A1-S103, A4-S009]. A start-up must beat "build it ourselves on the open engine" on recall, operations, evidence or time to value, not on the existence of the feature [AJ]. Open core is the established packaging: Langfuse keeps SCIM, audit logs and RBAC behind an Enterprise key, and LiteLLM gates RBAC, SCIM and audit logs to its Enterprise edition [VF: A1-S033, A6-S007].

**5. Tooling vendors are now part of the attack surface.** Malicious LiteLLM releases 1.82.7 and 1.82.8 were published to PyPI on 24 March 2026 with credentials stolen through a compromised scanner in CI [VF: A6-S008, V2-S027]. Composio disclosed a May 2026 incident in which connected-account tokens and API keys were exposed [VF: B-L4-S007]. OWASP's Agentic Top 10 for 2026 lists ASI04 Agentic Supply Chain Vulnerabilities [VF: E3-S072, A8-S042]. A start-up's release pipeline, signing and credential custody are read as part of the buyer's own supply chain [AJ].

**6. The buyer will push its regulation down to the start-up by contract.** DORA requires Article 30 provisions in every ICT service contract (service description, subcontracting, data locations, return of data on exit, service levels, incident assistance, cooperation with authorities, termination rights, resilience training) [VF: A8-S021, E1-S055]. For critical or important functions it adds exit strategies and audit and inspection rights, including on site [VF: E1-S055, E1-S056]. The start-up must identify all its subcontractors, model API providers included, pass access and audit rights down, and let the customer object to material changes [VF: E1-S057]. A NIS2 customer will add supply-chain security terms [VF: E1-S016].

**7. The start-up has duties of its own.** Installed or self-hosted tools and SDKs sold in the EU are Cyber Resilience Act products; a SaaS-only tool is in scope only as the remote data processing of a product [VF: E1-S001]. CRA reporting of actively exploited vulnerabilities has applied since 11 September 2026, and the main obligations apply from 11 December 2027 [VF: E1-S002, E1-S003, E1-S006]. A tool that is itself an AI system supplied under the start-up's name makes it that system's provider, and a component going into a customer's high-risk system needs an Article 25(4) written agreement [VF: A8-S016, E1-S033]. The Product Liability Directive treats software, SaaS included, as a product from 9 December 2026, and a component supplier is liable where its defective component made the product defective [VF: E1-S010, E1-S011].

**8. Telemetry and agent-identity standards are the integration surface, and they are not yet stable.** The OpenTelemetry GenAI conventions moved to their own repository; the agent spans and MCP conventions are at status Development, and the new repository has no tagged release [VF: E3-S066, E3-S067, E3-S068, E3-S069]. MCP authorisation is optional in the specification, while the Enterprise-Managed Authorization extension is stable and builds on ID-JAG, which is still an IETF OAuth working-group draft [VF: A3-S055, A3-S017, A6-S079, E3-S073]. The start-up should emit and accept these standards with a pinned version and an adapter, and expect renames [Rec].

## XVI.3 Scoring for this view

**What is scored.** In a vendor view the scores describe the components the start-up builds its own product on, not the product it sells [AJ]. The view re-weights the same eight criterion scores the FS view uses; no product fact or criterion score changes, and the weights are architectural judgement (views.json) [AJ]:

| Criterion | FS weight | AT weight | Why it moves [AJ] |
|---|---:|---:|---|
| Technical | 15 | 20 | The component is inside the product; its depth is the product's depth |
| Enterprise readiness | 15 | 10 | The start-up supplies the enterprise wrapper itself |
| Security and compliance | 20 | 15 | Still high: the start-up inherits its customers' expectations |
| Deployment flexibility | 15 | 15 | Unchanged: the component must run in the customer's account too |
| Ecosystem | 5 | 15 | Open standards are how the product plugs into the buyer's stack |
| Reliability and maturity | 10 | 5 | The start-up can pin and patch fast-moving components it controls |
| Cost and TCO | 5 | 10 | A young company's runway and gross margin |
| Lock-in and portability | 15 | 10 | Still matters, because the product's own portability is sold |

**What moves, and why.** The largest gains go to components with strong ecosystems and low cost: Agent Skills, Composio and Supermemory each rise by 0.30 or more, MCP rises from 3.55 to 3.85, LiteLLM from 3.90 to 4.15 and SGLang from 3.65 to 3.90, all on ecosystem 4 or 5 now weighted at 15% (`AT_scores.md`) [AJ]. DeepEval moves from sixth to third in L9 (3.70 → 3.85), and Sentence Transformers becomes first in L7 (3.90) [AJ]. Presidio falls slightly (3.65 → 3.60) and drops behind Google Sensitive Data Protection (3.65), because its strengths in lock-in and deployment weigh less [AJ]. A rise in score is not a rise in tier: Agent Skills stays Tactical and Composio stays Experimental after its token-exposure incident [VF: B-L4-S007] [AJ].

**Fit changes against FS.** Core candidates number 56 under these weights, against 45 under FS, of 138 scored products; eleven products become core candidates and none falls out (`AT_scores.md`) [AJ]:

| Becomes a core candidate under AT | Master tier | FS → AT | What it means for a tools start-up [AJ] |
|---|---|---|---|
| Pydantic AI (L3) | Strategic, conditional | 3.55 → 3.70 | Typed agent steps inside the product |
| MCP (L4); Anthropic-originated, alternative OpenAPI tools or A2A | Strategic, conditional | 3.55 → 3.85 | An agent-facing interface, behind the buyer's tool gateway |
| Zep and Graphiti (L5) | Tactical | 3.50 → 3.70 | Only for memory products; Community Edition deprecated |
| Arize Phoenix (L9) | Tactical | 3.50 → 3.65 | ELv2 and Dynatrace-owned: a competitor more than a component |
| Promptfoo (L9) | Tactical | 3.55 → 3.75 | Announced OpenAI ownership: pair with an independent red-team tool |
| Portkey (C1) | Tactical | 3.50 → 3.60 | Palo Alto-owned: a competitor or a channel |
| NeMo Guardrails (C2) | Tactical | 3.45 → 3.65 | An orchestrator a detector start-up can plug into |
| Okta / Auth0 for AI Agents (C4) | Strategic, conditional | 3.55 → 3.65 | The identity the product must accept |
| MCP Authorization (C4); Anthropic-originated, alternative OAuth 2.0 resource-server pattern on OpenAPI tools | Strategic, conditional | 3.45 → 3.65 | The authorisation profile an MCP server must enforce |
| Prisma AIRS (C7) | Tactical | 3.35 → 3.60 | An incumbent bundle, not a component |
| IBM watsonx.governance (C8) | Tactical | 3.40 → 3.60 | An incumbent the product must export evidence to |

**How to read the fit.** The fit is computed and indicative; the master tiers and their conditions still stand, and the condition is the decision, not the total (Part I.3) [AJ]. Five of the eleven are owned by incumbents (Promptfoo, Phoenix, Portkey, Prisma AIRS, watsonx.governance), so under this view they are better read as the competitors, channels or evidence destinations a start-up must interoperate with than as parts to build on [AJ]. Phoenix's ELv2 licence and Promptfoo's announced owner are recorded facts [VF: A1-S048, A1-S024].

**The components a tools start-up actually builds on.** These are the core candidates that recur in XVI.7 [AJ]:

| Ref | Component | Master tier | AT score (rank in layer) |
|---|---|---|---|
| L1 | Mistral family; Gemma 4 (open weights for in-product models) | Strategic; Strategic, conditional | 3.95 (2); 3.80 (4) |
| L2 | vLLM | Strategic | 4.45 (1) |
| L6 | pgvector | Strategic | 4.35 (1) |
| L7 | Sentence Transformers | Strategic | 3.90 (1) |
| L8 | Docling | Strategic | 4.10 (1) |
| L9 | MLflow; Langfuse; DeepEval | Strategic; Strategic; Tactical | 4.30 (1); 3.90 (2); 3.85 (3) |
| C1 | LiteLLM (internal model access, pinned) | Strategic, conditional | 4.15 (1) |
| C3 | Presidio | Strategic, conditional | 3.60 (2) |
| C4 | OPA; SPIFFE/SPIRE | Strategic; Strategic | 4.30 (1); 3.90 (2) |
| C6 | FOCUS | Strategic | 3.90 (1) |
| C7 | Model and package scanning | Strategic | 3.75 (1) |
| C8 | OpenLineage | Strategic | 3.95 (1) |

**Anthropic.** The Claude family stays third in L1 (3.80 → 3.85), behind OpenAI (4.25) and Mistral (3.95); its lowest criteria remain deployment flexibility 3 and reliability 3 (`AT_scores.md`) [AJ]. Its master tier is Strategic, conditional (hyperscaler UK/EU route, non-Anthropic fallback; independent alternatives GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5) [AJ]. The Claude Agent SDK stays Experimental at 2.85; the independent alternatives are LangGraph or Pydantic AI, or the OpenAI Agents SDK as a comparable harness [VF: A4-S006, B-REVC-S001] [AJ].

**Where to find the full table.** Every product's FS and AT score, rank and fit is in `05_Data/views.xlsx`; the per-layer listing is `work/stageE/views/AT_scores.md` [AJ].

## XVI.4 The architecture for this view

The FS architecture (Part IV.1) is the buyer's, and it is not redrawn here [AJ]. What this view adds is the start-up's footprint inside it: one component, reached through the buyer's gateway or pipeline, configured from the buyer's Git, identified by the buyer's IdP, and writing to the buyer's collector, evidence store and cost dataset. The vendor's own plane ships signed releases and support, and holds no customer content [AJ].

![Where an AI tool plugs into the customer's control plane](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/AT-1.png){width=100%}

*Figure: The buyer owns the control plane; the start-up's tool is one call-out inside it. The customer's workflow reaches the tool only through the gateway of record (and from ingestion and trace export), the tool runs in the customer's account or behind a private endpoint, takes its policy from the customer's Git, and writes spans, verdict records and usage to the customer's own collector, evidence store and cost dataset. The vendor plane ships signed releases and never sees customer content. Editable source: `08_Graphic/diagrams/AT-1.md`.* [AJ]

**Three delivery forms, one code path.** Buyers ask for BYOC or customer-VPC editions; Fireworks, turbopuffer and Together are recorded examples [VF: A4-S152, A2-S125, A4-S130]. The start-up should offer three forms from the same build [AJ]:

| Form | Where customer content is processed | Connectivity | Who buys it [AJ] |
|---|---|---|---|
| Shared SaaS, EU region | Vendor's account, EU | Public TLS endpoint, IP allow-list | Pilots; non-confidential content |
| Private SaaS | Vendor's account, EU, dedicated stamp if paid for | AWS PrivateLink endpoint service or Azure Private Link service [VF: E2-S052, E2-S049] | Regulated buyers who accept a processor |
| Customer-run container | Customer's account and region | None to the vendor for content; licence and update channel only | Buyers whose policy says "must not leave"; the FS default (Part VII Stack A) |

Automated single-tenant deployment stamps give the strongest isolation at the lowest cost efficiency [VF: E2-S053]; on AWS the provider exposes an endpoint service behind a Network Load Balancer, and on Azure the provider accepts or rejects each private-endpoint connection [VF: E2-S052, E2-S049]. Equivalent Google Cloud private-connectivity mechanics were not researched in this run [NPV].

**Four properties the product must prove [AJ].** It can be removed by a configuration change in the buyer's gateway without data loss; it never holds the buyer's credentials, keys or token maps unless the buyer chose that; every decision it makes is reproducible from a versioned policy and a pinned engine; and its absence fails closed or open exactly as the buyer's policy says, with errors distinguishable from policy blocks.

## XVI.5 Where the product sits and how it fits into the Enterprise GenAI Stack

**Map the product first.** Each AT category has a home in the FS model, an FS default it must sit beside or displace, and a dominant integration point [AJ]:

| Product category | Home | FS default the buyer already has (Part VII Stack A) | Where the product is called from [AJ] |
|---|---|---|---|
| Retrieval or memory component | L5, L6 | pgvector or Elasticsearch; memory last | The buyer's retrieval interface or memory API |
| Embedding or reranking | L7 | Sentence Transformers, pinned | The buyer's `embed` / `rerank` service |
| Ingestion and parsing | L8 | Docling and Unstructured inside a built envelope | The buyer's ingestion pipeline |
| Evaluation or observability | L9 | Firm OTel Collector; Langfuse or MLflow; DeepEval; Promptfoo plus an independent red-team tool | The Collector, CI and the evidence store |
| Gateway | C1 | LiteLLM Enterprise or Kong hybrid | It *is* the traffic path: the hardest sale |
| Guardrail or detector | C2, C7 | Deterministic checks plus NeMo Guardrails or the cloud's managed detector | Gateway hooks; NeMo Guardrails rails |
| Privacy service | C3 | Presidio behind a firm privacy-service API | The six enforcement points (C3 §C3.1) |
| Identity or policy | C4 | Workforce IdP, OPA, SPIFFE/SPIRE | The gateway's policy decision point |
| Configuration or FinOps | C5, C6 | Git manifest; gateway metering and a FOCUS-shaped dataset | CI and the cost dataset |
| Governance | C8 | Firm evidence store; a replaceable workflow tool | Exports from every other component |

**The integration contract, layer by layer, then control by control.** Whatever the product's home, the buyer's stack expects a contract at every other layer it touches. The table is written for the FS buyer, the toughest, and quotes master tiers unchanged [AJ]:

| Layer / control | What the buyer's stack expects | The interface the product should offer | Evidence |
|---|---|---|---|
| L1 models | A two-vendor portfolio consumed through its own cloud route, with pinned versions; no hidden model dependency | No hard-wired vendor; in-product models either bundled open weights (Mistral, Strategic, or Gemma 4, Strategic, conditional) or the customer's own model accounts through the customer's gateway; any Claude route paired with a non-Anthropic alternative (GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5) | Model vendors restrict reselling raw access and transferring keys [VF: E2-S004, E2-S026]; ZDR conditions differ by model and must pass through [VF: E3-S011, E3-S032] |
| L2 inference | OpenAI-compatible model access through the gateway; a vLLM private route | Accept an OpenAI-compatible base URL and key; serve bundled models on vLLM (Strategic) in the customer's account | Every gateway exposes or accepts the format [VF: A6-S015, A6-S053, A6-S061] |
| L3 orchestration | Deterministic workflows; durable activities; approval interrupts | Idempotent, side-effect-free calls safe to retry; a typed outcome (allow, block, transform) with error distinct from policy block | NeMo IORails' `RailOutcome` contract separates policy blocks from execution failures [VF: A6-S036] |
| L4 tools | No tool reachable except through the governed tool gateway; read-only by default | Where agents call the product: an MCP server (Strategic, conditional; Anthropic-originated, alternative an OpenAPI description) that enforces OAuth authorisation and works under managed allow-lists; A2A only for agent delegation | MCP authorisation is optional in the specification [VF: A3-S055]; MCP allow-listing is a standard admin control [VF: E3-S004] |
| L5 memory | Memory as a governed record class; subject erasure | Stateless by default; if state is kept, `forget_by_subject` and export | Memory poisoning is ASI06 [VF: B-L5-S001] |
| L6 stores | Derived, rebuildable, entitlement-filtered indexes | Entitlement filter applied inside the search; rebuild from source | OWASP LLM08 names cross-context leakage in vector stores [VF: E2-S051] |
| L7 retrieval optimisation | Pinned embed and rerank versions | `model_version` on every vector; customer-pinnable models | Switching a model forces re-embedding (Part IX.1) [AJ] |
| L8 ingestion | ACL, classification and lineage on every chunk | Preserve ACL and classification metadata; emit OpenLineage facets and a parse manifest | No L8 product emits lineage today [VF: A1-S094, A1-S096] |
| L9 evaluation and observability | One telemetry spine through the firm's Collector; datasets in Git | OTel GenAI spans to the customer's collector, version pinned, no content by default; scores as `gen_ai.evaluation.result` events | Conventions at Development status [VF: E3-S067, E3-S069]; evaluation event type [VF: A1-S059] |
| C1 gateway | One gateway of record; detectors as call-outs; fail-closed routes | A low-latency HTTP call-out usable from pre-call and post-call hooks, with a published latency budget and timeout behaviour | Gateway hooks [VF: A6-S015, A6-S017, A6-S020, A6-S024]; generic third-party call-out per gateway [NPV] |
| C2 guardrails | Policy and test sets owned by the firm; two detectors from different owners on untrusted input | Policy importable and exportable as files; the customer's test sets runnable against the product in CI | Detectors are being absorbed by security vendors [VF: A7-S012, A7-S014, A6-S028] |
| C3 privacy | One privacy service at six enforcement points | If the product is not the privacy service, call the customer's before storing content, and redact its own logs | Six enforcement points (C3 §C3.1) [AJ] |
| C4 identity | Workforce IdP; agents as registered identities acting on behalf of users | SAML or OIDC SSO, SCIM, RBAC; workload identity (SPIFFE/SPIRE, Strategic) or OAuth tokens for service calls; MCP Enterprise-Managed Authorization where agents call it (Anthropic-originated; alternative OAuth 2.0 on an OpenAPI interface) | EMA builds on ID-JAG [VF: A6-S079, E3-S073]; Entra Agent ID and Okta for AI Agents are GA [VF: V2-S032, A6-S100] |
| C5 configuration | Git as the configuration of record; release manifest with an evaluation gate | Policy and configuration as code with a versioned API; no setting that exists only in a console | "Policy held only in a vendor console" is the FS anti-pattern (Part IV.3, row 34) [AJ] |
| C6 FinOps | Cost per approved task; budgets that fail closed | Usage metered per customer use case or gateway key, exported in a FOCUS-shaped form | FOCUS 1.4 ratified 4 June 2026 [VF: V2-S046] |
| C7 security | Capability separation; signed and pinned dependencies; secrets in the firm's vault | Signed images, an SBOM per release, pinned dependencies, secrets from the customer's vault, no standing credentials | LiteLLM PyPI compromise [VF: A6-S008]; CRA SBOM duty [VF: E1-S001] |
| C8 governance | A firm-owned, immutable evidence store keyed by trace ID | Verdict records written to the customer's store, keyed by the customer's trace ID; audit logs exportable; retention set by the customer | Free tiers keep data 15, 30 or 60 days [VF: A1-S047, A1-S031, A1-S123] |

**The single test [AJ].** If the buyer can run its Part VI evidence pack with the product in the path, and can remove the product by changing one gateway route and one manifest entry, the product fits. If either fails, the FS buyer's own decision tree (Part IV.3) will reject it, however good the detector.

## XVI.6 What enterprise buyers will ask, and how to pass

**Read the buyer's evidence register as the specification.** Part V.8 lists what the FS buyer must produce; a tools start-up passes due diligence by producing the slice of it that touches its product [AJ]:

| Area | What the FS buyer will ask | How to pass [Rec] | Evidence |
|---|---|---|---|
| Due diligence | Ownership, funding, subcontractors, certifications, incident history, financial resilience | A one-page company fact sheet; the subprocessor list; a published security page with certificate scopes, not logos | Verifiers downgraded "vendor-stated" ISO claims without certificates [VF: A6-S109, A1-S124] |
| DORA Article 30 | The minimum clause set; for critical or important functions, exit strategies and on-site audit | A pre-drafted DORA addendum mapping each clause to the product; an exit plan template with data return in open formats | [VF: A8-S021, E1-S055, E1-S056] |
| Subcontracting | Every subcontractor named, audit rights flowed down, right to object to material changes | List model API vendors and hosting providers; a customer-run edition with no content subprocessors at all | [VF: E1-S057] |
| UK outsourcing | Material third-party notification from 18 March 2027; exit planning | Notice periods for material changes, including change of control, long enough for the buyer to notify | [VF: R-PRA-SS221, A8-S062, A8-S048] |
| NIS2 | Supply-chain security terms | Secure development policy, vulnerability handling, incident notice | [VF: E1-S016] |
| AI Act role | Is the tool an AI system? Who is its provider? Does it enter a high-risk system? | A role statement: provider if the tool is an AI system under the start-up's name; an Article 25(4) information-and-assistance clause ready for customers building high-risk systems | [VF: A8-S016, E1-S033]; free and open-source exemption ends once monetised [VF: E1-S033] |
| CRA | Is the container a product with a support period, SBOM and vulnerability reporting? | Treat the customer-run edition as a CRA product now: SBOM per release, a stated support period, a 24-hour and 72-hour reporting runbook through ENISA's Single Reporting Platform | Support period at least five years unless expected use is shorter [VF: E1-S001]; reporting live since 11 September 2026 [VF: E1-S003, E1-S006] |
| PLD | Who carries liability for a defective component? | Release history, evaluation records and logs kept as the defence; security updates within the support period | [VF: E1-S010] [R: E1-S013] |
| Certifications | SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 42001, an AI questionnaire | Sequence them (below) and publish an AI-CAIQ early | Baseline for established tool vendors [VF: A6-S109, A1-S124, A1-S137, A1-S036]; STAR for AI [VF: E2-S047] |
| BYOC and residency | Processing location per copy: content, logs, traces, backups | Customer-run edition; EU region for SaaS with logs in region; a residency statement per data class | Storage and processing residency differ (Part V.4) [VF: B-L2-S006, B-L2-S005] |
| IP and data terms | No training on customer content; customer owns outputs; who indemnifies what | Mirror the model vendors' own terms: customer retains inputs and owns outputs; no training on customer content | [VF: E2-S004, E2-S026, E2-S007] |
| Exit, switching and escrow | Data return, switching assistance, continuity if the vendor is acquired or fails | Export of policies, verdict records and configuration in open formats; no switching charges; for the customer-run edition, a licence that survives change of control or source escrow | Data Act: no switching charges from 12 January 2027 [VF: E1-S025, E1-S026]; escrow terms not researched [NPV] |

**Certification sequencing [Rec].** The order below is the author's judgement on cost and buyer value; the facts in each row are sourced:

| Step | What | Why this order | Evidence |
|---:|---|---|---|
| 1 | Security page, SBOM, CRA reporting runbook, subprocessor list | Free, and asked for in the first questionnaire | CRA reporting already applies [VF: E1-S003] |
| 2 | CSA AI-CAIQ self-assessment published (STAR for AI Level 1) | A public, AI-specific answer at low cost | [VF: E2-S047] |
| 3 | SOC 2 Type II | The baseline every established tool vendor shows; assessed against the 2017 Trust Services Criteria | [VF: A6-S109, A1-S137] [R: E2-S048] |
| 4 | ISO/IEC 27001:2022 | Certification to the 2013 edition has ended | [R: E2-S046] |
| 5 | ISO/IEC 42001, then STAR for AI Level 2 | Now common among AI developer tools; Level 2 requires it | [VF: E3-S010, E3-S026, E2-S047] |

AIUC-1 appears as an attestation on Cursor's security page; its weight with FS buyers was not assessed [VF: E3-S026] [NPV].

**What does not apply.** SR 26-2 and PRA SS1/23 govern the buyer, not the start-up; they reach it only as evidence the buyer requests [VF: R-US-MRM, A8-S001] [AJ]. US state AI laws mostly apply where a product makes, or helps make, consequential decisions about individuals, which a stack component rarely does; Colorado's replacement law is stayed [VF: E1-S038, E1-S040] [AJ].

## XVI.7 The start-up's own reference stack

**What to build the product on.** The same rule as the FS buyer's, applied to the start-up's own estate: open, portable components it can ship into a customer's account, with managed services only in the SaaS edition. S, T and E abbreviate the master tiers; hyperscaler model services are access patterns, not scored (Part I.3) [AJ].

| Layer / control | Cloud-neutral (also the customer-run edition) | AWS | Azure | Google Cloud |
|---|---|---|---|---|
| L1 in-product models | Apache-2.0 open weights: Gemma 4 (S, cond.) or Mistral Large 3 / Ministral 3 (S) for recognisers and judges; customer's own model account for anything larger | Bedrock in an EU region in the SaaS edition | Foundry Data Zone in the SaaS edition | Gemini (S, cond.) in an EU region; credits apply to Google models only [VF: E2-S010] |
| L2 serving | vLLM (S), CPU path for small models where possible | Same, on the customer's EKS | Same, on AKS | Same, on GKE |
| L3 internal workflows | Plain code; Pydantic AI (S, cond.) for typed LLM steps; LangGraph (S) if multi-step | Same | Same | Same |
| L4 agent interface | MCP server (S, cond.; Anthropic-originated, alternative OpenAPI description); AGENTS.md or skill guidance for coding agents | AWS Marketplace "AI Agents and Tools" listing for MCP servers [VF: E2-S035] | Same | Same |
| L6 product state | PostgreSQL with pgvector (S) | RDS or Aurora | Azure Database for PostgreSQL | Cloud SQL |
| L7 embeddings | Sentence Transformers (S) serving an Apache-2.0 model | Same | Same | Same |
| L8 parsing (if needed) | Docling (S) | Same | Same | Same |
| L9 own evaluation | OTel SDK with pinned GenAI conventions; MLflow (S) or Langfuse (S); DeepEval (T); Promptfoo (T) plus an independent red-team tool | MLflow on SageMaker | MLflow on Azure ML | Langfuse self-hosted |
| C1 internal model access | LiteLLM (S, cond.), pinned and mirrored, for the SaaS edition's own calls | Same | Same | Same |
| C4 product identity | OIDC/SAML SSO and SCIM for admins; OPA (S) for in-product policy; SPIFFE/SPIRE (S) for service identity | IAM roles for service accounts | Workload identity | Workload identity |
| C6 metering | Usage events exported in a FOCUS (S)-shaped form | Marketplace metering for SaaS listings [VF: E2-S034] | Marketplace purchases count toward Azure commitments [VF: E2-S036] | Marketplace purchases draw down commitments [VF: E2-S020] |
| C7 supply chain | Signed images, SBOM, pinned dependencies, safetensors only, scanning gate (S) | Same | Same | Same |
| C8 evidence | OpenLineage (S) facets; append-only verdict log exportable to the customer | Same | Same | Same |
| Delivery | Helm chart and container; SaaS in an EU region | PrivateLink endpoint service; private offers to named accounts [VF: E2-S052, E2-S034] | Private Link service shared by alias; private offers [VF: E2-S049, E2-S036] | Private offers with flexible instalments [VF: E2-S038]; private connectivity not researched [NPV] |
| Credits | Use them, but keep the model behind the gateway | Activate up to US$200,000 through a provider (AWS pages also say US$100,000) [VF: E2-S042] | Up to US$150,000 [VF: E2-S011] | Up to US$350,000 for AI-first start-ups, tied to Gemini [VF: E2-S009, E2-S010] |

**Why bundled open weights.** A model API inside the product is a subcontractor the FS buyer must register, flow audit rights to and assess for residency [VF: E1-S057]. Apache-2.0 weights such as Gemma 4 need only the licence and notices shipped [VF: A5-S034, V2-S020] [AJ]. Anthropic's start-up credits apply only to the first-party API, not to Bedrock or Vertex, and Google's AI-tier credits do not cover third-party models [VF: E2-S008, E2-S010]. Credits therefore pull the start-up towards one vendor's models; a gateway keeps that reversible [AJ].

**Do not build yet [Rec].** A proprietary agent framework or protocol; long-term memory of customer content; fine-tuned models trained on customer data; a second product category; a governance dashboard that duplicates the buyer's evidence store; any Experimental component in the shipped product, including the Claude Agent SDK (alternatives LangGraph, Pydantic AI or the OpenAI Agents SDK) [VF: A4-S006, B-REVC-S001].

## XVI.8 Build vs buy, and lock-in; where incumbents are and where they are moving

**Build vs buy for the start-up.** Part VIII's rule stands from the buyer's side; on the vendor's side the rule is to build only the differentiated core and the enterprise wrapper buyers pay for, and adopt open components for the rest [AJ]:

| Component | Decision | Why [AJ] |
|---|---|---|
| The differentiated engine (detector, evaluator, retriever) | **Build** on an open base (Presidio, Sentence Transformers, Docling) | The open base is the buyer's fallback, so the product must add measurable recall, latency or evidence on top |
| Enterprise wrapper (SSO, SCIM, RBAC, audit export, policy as code) | **Build**, and charge for it | This is where open-core vendors monetise [VF: A1-S033, A6-S007] |
| Deployment and release engineering (Helm, signing, SBOM, private endpoints) | **Build early** | It is the price of entry for the customer-run edition and the CRA |
| Telemetry, lineage and cost export (OTel, OpenLineage, FOCUS) | **Adopt** the standards | Proprietary formats count against the product in the buyer's lock-in table (Part IX.4) |
| Identity, policy engine, secrets | **Adopt** (OIDC, SCIM, OPA, the customer's vault) | The buyer will not accept a second identity plane |
| Hosting, model access, billing | **Buy** (cloud, marketplaces) | Marketplace drawdown removes a new-vendor budget line for the buyer [VF: E2-S036, E2-S020] |

**The lock-in the buyer will look for.** The FS buyer classifies each layer's lock-in (Part IX.4) [AJ]. Its "unacceptable" column describes what a start-up must not sell: credential custody in a third party's multi-tenant cloud; evaluation datasets only in a vendor UI; policy or test sets held only in a vendor console; a vendor-held token map and keys without a tested bulk-detokenisation exit; an evidence store held only by a vendor [AJ]. Licence matters too: Phoenix is ELv2, Firecrawl's server is AGPL-3.0 and Weaviate is moving to open core, and the FS view makes licence review an architectural gate [VF: A1-S048, A1-S053, A2-S115] [AJ]. A permissive or clearly open-core licence, with the enterprise wrapper as the paid part, is the least contested choice [AJ].

**Where incumbents are, and where they are moving.** The dataset's ownership events, layer by layer, then control by control [AJ]:

| Ref | Incumbent move (dataset) | Who is buying | What it means for a start-up [AJ] |
|---|---|---|---|
| L4 | Nebius completed its acquisition of Tavily on 19 February 2026 [VF: A3-S084, V1-S041] | Infrastructure cloud | Search and tool APIs are infrastructure add-ons |
| L5 | Hyperscalers ship memory in their agent runtimes; Mem0 removed external graph stores, Zep deprecated its Community Edition, Letta pivoted [VF: V1-S087, V1-S088, A3-S053, A3-S059, A3-S093] | Hyperscalers | The independent memory category is thinning; sell governance (erasure, snapshots), not storage |
| L6, L7 | MongoDB owns Voyage; Elastic owns Jina; Cohere signed a business combination with Aleph Alpha [VF: A2-S033, A2-S023, A2-S018] | Database and search companies | Embedding and reranking are being absorbed into stores; a retrieval start-up sells portability across them |
| L8 | IBM donated Docling to LF AI & Data, where it graduated [VF: A1-S057, V1-S091] | Foundations | The open default improves for free; lineage and entitlement capture remain unbundled |
| L9 | Dynatrace–Arize (completed 1 October 2026), ClickHouse–Langfuse, OpenAI–Promptfoo (announced), CoreWeave–W&B, Mintlify–Helicone (maintenance mode) [VF: A1-S045, A1-S021, A1-S024, A1-S131, A7-S112] | Observability, database, model and compute vendors | The most consolidated category; independence (Braintrust, LangSmith) is itself a selling point [VF: A1-S028, A1-S038] |
| C1 | Palo Alto–Portkey (completed 29 May 2026); OpenRouter–Stripe pending; Envoy AI Gateway renamed Agent Router and moved to the Agentic AI Foundation [VF: A6-S012, V2-S025, V1-S059, A6-S063, V2-S029] | Security, payments, foundations | The traffic path is strategic; a gateway start-up competes with foundations and security platforms at once |
| C2 | Harvey–Guardrails AI, hosted hub retired; cloud guardrails bundled with model services [VF: A6-S028, V2-S071, A6-S072, A6-S067] | Application companies, hyperscalers | A detector must be swappable and measurable to survive beside the bundles |
| C3 | Presidio moved to community governance; Purview DSPM unified; DLP added to gateways and guardrails [VF: A6-S040, V2-S030, V2-S036, A6-S052, A6-S016] | Foundations, Microsoft, gateway vendors | The XVI.10 example's market: an open default plus bundled features |
| C4 | Okta for AI Agents and Agent SSO GA; Entra Agent ID GA; Cedar-based AgentCore Policy GA [VF: A6-S100, V2-S035, V2-S032, A6-S026] | Identity platforms, hyperscalers | Agent identity is now a platform feature; build on it rather than against it |
| C6 | Helicone in maintenance mode after the Mintlify acquisition [VF: A7-S112, V2-S043] | Application companies | Cost tooling is a gateway feature; FinOps start-ups sell the FOCUS-shaped join, not metering |
| C7 | Palo Alto bought Protect AI, Koi and Portkey; Check Point bought Lakera; HiddenLayer raised a US$100m Series B; IBM owns HashiCorp [VF: A7-S014, A7-S016, A7-S012, A7-S017, V2-S047, A7-S032] | Security platforms | Security vendors buy to bundle; the independent specialist is the FS buyer's named alternative |
| C8 | Collibra announced the acquisition of trail ML on 5 October 2026 [VF: A7-S101, V2-S044] | Data-governance platforms | No governance platform reaches Strategic on public evidence; the buyer owns the store (Part VII) |

**Positioning implications [AJ].** The acquirers fall into five groups: platform and data vendors that want the traffic or the data (Dynatrace, ClickHouse, MongoDB, Elastic, CoreWeave), security platforms that want a place in the traffic path (Palo Alto Networks, Check Point), model vendors (OpenAI), application companies (Harvey, Mintlify) and infrastructure or payments firms (Nebius, Stripe). Each group buys for a different reason, so a start-up should know which group its product completes. The FS view names "independent of the model vendor under test" and "different owners" as reasons to choose a second red-team tool or detector (Part IX.3); independence is therefore a positioning asset with a shelf life.

**Exit implications [Rec].** Write the change of control into the product before it happens: data export in open formats, a licence for the customer-run edition that survives an acquisition, advance notice of change of control long enough for UK FS customers to notify [VF: A8-S062], and a published end-of-life policy. Acquirers have retired products quickly: Helicone went to maintenance mode on the day of its acquisition and Guardrails AI's hosted hub was retired [VF: A7-S112, V2-S071]. A start-up whose customers can leave safely is easier to buy and easier to sell to [AJ].

## XVI.9 Roadmap

**Size.** Eighteen months, October 2026 to March 2028, for a team growing from four to about twelve people, with the first regulated customer in production by month nine. The phases follow the buyer's own roadmap (Part X), so that the product is ready when the buyer's phase needs it [AJ].

| Date | Event | Consequence for the start-up [AJ] |
|---|---|---|
| Since 11 September 2026 | CRA vulnerability and incident reporting [VF: E1-S003, E1-S006] | Reporting runbook for the customer-run edition now |
| 9 December 2026 | PLD applies to products placed on the market [VF: E1-S011] | Release history and evaluation records kept as the defence |
| 12 January 2027 | Data Act: no switching charges [VF: E1-S025] | Export and switching assistance in the SaaS terms |
| 18 March 2027 | UK FS customers notify material third parties [VF: R-PRA-SS221, A8-S062] | DORA addendum, exit plan and change notices ready |
| 2 December 2027 | AI Act Annex III high-risk duties [VF: R-EU-OMNIBUS-AI, A8-S011] | Article 25(4) clause ready for customers building high-risk systems |
| 11 December 2027 | CRA main obligations, conformity assessment and CE marking [VF: E1-S002] | Support period, SBOM and conformity documentation complete |

**Phases [Rec]:**

| Phase (months) | Scope | Exit criterion |
|---|---|---|
| 0 Contract and fit (0–2) | Integration contract (XVI.5) as a public document; role statement under the AI Act; subprocessor list; security page; SBOM and signing in CI | One FS design partner signs off the contract table |
| 1 Two editions, one build (1–4) | EU SaaS and customer-run container from one pipeline; OTel spans to the customer's collector; policy as code | Container installed in a design partner's account with no outbound content |
| 2 Gateway and evidence (3–6) | Call-outs from at least two gateways (LiteLLM and one of Kong, APIM or Apigee); verdict records to the customer's store; usage export | The design partner's evidence pack includes the product's records |
| 3 Assurance (4–9) | AI-CAIQ published; SOC 2 Type II observation period; DORA addendum; private endpoints on AWS and Azure | First regulated customer passes due diligence |
| 4 Distribution (8–12) | Marketplace listings with private offers; MCP server for agent callers (alternative OpenAPI description) | First marketplace private offer transacted |
| 5 Scale and certify (12–18) | ISO/IEC 27001:2022; ISO/IEC 42001 decision; CRA conformity documentation; change-of-control and end-of-life policy | Ready for 11 December 2027 |

## XVI.10 Worked example: a PII-redaction and policy service called from the customer's gateway

**The use case.** A four-person start-up sells a PII-redaction and policy service that enterprises call from their AI gateway. It ships as SaaS in an EU region and as a container customers run in their own account, emits OpenTelemetry spans, and is preparing SOC 2 Type II (views.json) [AJ]. Here it is traced as the customer runs it: the FS buyer's attribution-commentary agent (Part VI), whose step 3e tokenises client identifiers for segregated mandates [AJ]. The customer runs the container edition, because the FS default keeps "must not leave" detection inside the estate (C3 §C3.5) [Rec].

| Step | What happens | Components |
|---:|---|---|
| 0 | The customer pins the service's image digest and policy version in its release manifest; the image is verified against the vendor's signature and SBOM before deployment | C5, C7 |
| 1 | The service runs in the customer's account with a workload identity; its admin console uses the customer's SSO and SCIM groups | C4, C7 |
| 2 | Ingestion calls the service on prior commentaries and market notes: classify, tag PII flags in the chunk envelope | L8, C3 |
| 3 | The analyst starts the workflow; the agent's on-behalf-of token carries the analyst's entitlements | L3, C4 |
| 4 | Retrieved chunks and tool results pass the gateway's pre-call hook; the service detects client identifiers and returns consistent placeholders (CLIENT_A, ACCT_7); the token map is stored under a key in the customer's KMS | C1, C3, C7 |
| 5 | The drafting call goes to the in-region model route; the model sees only placeholders | C1, L2, L1 |
| 6 | The post-call hook calls the service again: residual-PII check, placeholder integrity (none altered, none invented) | C1, C2, C3 |
| 7 | Re-identification only for the named reviewer, after the customer's policy decision; the service logs who, why and which policy | C3, C4 |
| 8 | Every call emits a span (entity types and counts, latency, policy version, outcome; no values) to the customer's collector | L9 |
| 9 | A verdict record keyed by the trace ID is written to the customer's evidence store | C8 |
| 10 | Usage (calls, characters inspected, policy) is exported to the customer's cost dataset | C6 |
| 11 | The collector calls the service to redact trace attributes before any export | L9, C3 |

**What it competes with.** The customer's alternative is Presidio (MIT, in-estate) behind its own API, or Google Sensitive Data Protection at US$3.00 per GiB inspected after the first free GiB [VF: A6-S040, A6-S065]. Presidio warns that detection is not guaranteed to find all sensitive data [VF: A6-S068]. The start-up wins on measured recall for domain identifiers (client codes, mandate references), placeholder integrity, evidence and operations, which the C3 KPIs already define (C3 §C3.3) [AJ].

**May [Rec]:** detect, classify, redact, mask and tokenise under the customer's policy; restore placeholders for a principal the customer's policy entitles; report entity types, counts and latencies; receive signed updates through the customer's release process.

**Must never, and what enforces it [Rec]:**

| Never | Enforced by |
|---|---|
| Send customer content, token maps or detections to the vendor plane | Customer-run edition; egress deny in the customer's network (C7); support telemetry carries counts only |
| Hold re-identification keys outside the customer's KMS | Key wrapping in the customer's KMS or vault (C7) |
| Re-identify without the customer's policy decision | Call to the customer's OPA or IdP (C4); logged reason |
| Change behaviour without a version change | Image digest and policy version pinned in the manifest (C5); CI recall tests (L9) |
| Fail open on error when the route says fail closed | Typed outcome with error distinct from block; gateway route policy (C1) |
| Write values into spans or logs | Span schema with types and counts only (L9); collector redaction |
| Keep data past the customer's retention | Retention set by the customer; verdict records stored in the customer's store (C8) |

**Evidence kept.** The customer keeps: the image digest and policy version per run, verdict records per trace ID, re-identification events with identity and reason, recall-test results per release, and usage per use case (C8, L9, C6) [Rec]. The start-up keeps: signed release history and SBOMs, its own evaluation records per release, vulnerability and incident reports, and support telemetry with no content [Rec]. Release history, evaluation records and logs are the main defence under the PLD [VF: E1-S010] [R: E1-S013].

**Regulatory reading [AJ].** If the detector uses a machine-learning or LLM recogniser, the service may be an AI system supplied under the start-up's name, which would make it the provider [VF: A8-S016]; whether that classification holds is a legal question the start-up should settle in its role statement. The container is a CRA product; the SaaS edition is in scope only as the remote processing of a product [VF: E1-S001]. The use case is not Annex III, so no Article 25(4) agreement is needed here, but a customer using the same service in a credit decision would ask for one [VF: E1-S033].

## XVI.11 Checklist, what to avoid, what to monitor

**Checklist [Rec]:**
- The integration contract (XVI.5) published, with a latency budget, timeout behaviour and a typed outcome that separates errors from policy blocks.
- One build that ships as EU SaaS, private-endpoint SaaS and a container in the customer's account, with no customer content in the vendor plane.
- SSO, SCIM, RBAC and audit export; workload identity for service calls; MCP Enterprise-Managed Authorization (alternative: OAuth 2.0 on an OpenAPI interface) where agents call the product.
- OTel GenAI spans to the customer's collector with a pinned convention version; verdict records to the customer's evidence store; usage in a FOCUS-shaped export.
- Policy and configuration as code; the customer's test sets runnable in CI against each release.
- Signed images, SBOM per release, pinned dependencies, CRA reporting runbook, stated support period.
- Subprocessor list, DORA addendum, exit plan, change-of-control notice; AI-CAIQ, then SOC 2 Type II, ISO/IEC 27001:2022 and ISO/IEC 42001.
- No hidden model dependency; bundled Apache-2.0 weights or the customer's own model accounts; any Claude route paired with a non-Anthropic alternative.

**Avoid [Rec]:** insisting on being the gateway when the buyer already has one; a SaaS-only product for content the buyer's policy says must not leave; holding customers' user tokens in a multi-tenant cloud [VF: B-L4-S007]; reselling raw model access [VF: E2-S004]; settings that exist only in a console; vendor-held token maps without a bulk export; unsigned or unpinned releases [VF: A6-S008]; certificate claims without certificates [VF: A6-S109]; a 2013-edition ISO/IEC 27001 certificate [R: E2-S046]; a licence that turns restrictive after adoption; credits that tie the product to one model vendor without a gateway [VF: E2-S010].

**Monitor [Rec]:**

| Monitor | Trigger |
|---|---|
| OTel GenAI conventions (Development, no tagged release) [VF: E3-S067, E3-S069] | Re-pin attributes on each release; adopt the first tagged version |
| MCP authorisation, ID-JAG draft (expires 22 November 2026) and IETF agent-auth work [VF: A3-S055, E3-S073, E3-S074] | Update the agent interface on publication |
| Ownership events in the product's category: Promptfoo–OpenAI and OpenRouter–Stripe closings; Collibra–trail ML; Cohere–Aleph Alpha [VF: A1-S024, V1-S059, A7-S101, A2-S018] | Re-assess positioning, partners and competitors |
| Incumbent bundling of the product's function in gateways and guardrails [VF: A6-S052, A6-S016, A6-S072, A6-S067] | Re-test differentiation against the bundle |
| CRA guidance annex, delegated acts and fine allocation [NPV] | Update conformity documentation |
| UK FS notification regime from 18 March 2027 [VF: A8-S062]; EBA/GL/2026/09 application date [VF: R-EBA-OUTSOURCING, V2-S054] | Update the DORA addendum and notice periods |
| Start-up credit terms and marketplace programmes [VF: E2-S008, E2-S009, E2-S042, E2-S034] | Re-plan hosting and distribution quarterly |
| Google Cloud private connectivity for SaaS and marketplace specifics [NPV] | Research before the first Google-primary customer |
