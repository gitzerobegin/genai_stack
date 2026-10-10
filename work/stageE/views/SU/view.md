# Part XV: The view for start-ups

This Part gives the view at end of Q3 2026 for an early-stage company building an AI-native product with a small team. It keeps the master view's layers, controls, products and criterion scores (Parts I–XII), changes the weights, adds Stage E evidence, and changes the advice wherever cash, speed and the first enterprise customer outweigh a regulator; where the FS view holds, it points back [AJ].

> **Conflict-of-interest disclosure.** The author is an Anthropic model. This Part names Anthropic's Claude models, the Claude Agent SDK, the Claude for Startups credit programme and two Anthropic-originated standards (MCP and Agent Skills). Each is scored on the same rubric as its competitors, and wherever one is recommended an independent alternative is named in the same row or sentence [AJ].

## XV.1 Who this view is for

**Profile.** The reader is an early-stage technology company, from pre-seed to Series B, building an AI-native product with a small team. Speed to a working product, cash runway and developer productivity come first. The first enterprise customers will soon ask for security assurance, and the architecture must not trap the company when it scales (`views.json`, SU profile) [AJ].

**Assumptions [AJ].**

- The team has between three and twenty engineers, no dedicated security or platform function, and no SRE rota able to patch a GPU fleet monthly.
- The product is a multi-tenant SaaS application: each customer organisation is a tenant, and customers' confidential data flows through model calls.
- The company is based in the UK or EU and sells first to UK and EU customers, with US sales possible. This mirrors the master view's jurisdiction, and the worked example (XV.10) assumes it.
- Customers are businesses, not consumers or children. Section XV.6 flags where a consumer or education product changes the answer.
- The company is the provider of its AI product under the EU AI Act, not a deployer, and does not train foundation models [AJ].

**The five biggest differences from the FS view.**

| # | FS view (Parts I–XII) | Start-up view | Why it changes [AJ] |
|---:|---|---|---|
| 1 | A firm-owned control and evidence plane first: two gateway deployments, self-hosted evaluation, immutable evidence store | A **thin** control plane in the first fortnight: one pinned open-source gateway, managed tracing on a free tier, an evidence table in the application database | Same control points, but each must cost days, not quarters |
| 2 | Models through the primary cloud's in-region service, two vendors, plus a self-hosted open-weight exit | First-party APIs or the credit-giving cloud; one vendor primary, a second qualified on the same evaluation set | Credits steer the model choice, so reversibility comes from the gateway (XV.2, finding 1) |
| 3 | The control problem is model risk, outsourcing and resilience | The control problem is **tenant isolation and the first security questionnaire** | Customers, not a supervisor, ask for evidence first |
| 4 | The firm is a deployer under SS1/23, DORA and PS7/26 | An **AI Act provider** from launch, owing Article 50 transparency; a CRA manufacturer if it ships anything installable | The role follows what the company sells (XV.6) |
| 5 | Agents registered in the workforce IdP | A **hosted customer-identity service** with tenant context on every call | The users are customers' staff |

## XV.2 Findings that change for this view

**1. Start-up credits steer the model choice, and most do not pay for other vendors' models.** Google for Startups offers up to US$350,000 to AI-first start-ups (volatile; re-verify), but the credits cover Google models such as Gemini and Gemma, and third-party models are billed directly [VF: E2-S009, E2-S010]. Claude for Startups credits apply only to the first-party Claude API, not to Bedrock or Vertex (volatile; re-verify) [VF: E2-S008]. AWS Activate offers up to US$200,000 through an Activate Provider, though AWS's own pages also say US$100,000, and Microsoft for Startups offers up to US$150,000 "across eligible Azure services" (volatile; re-verify) [VF: E2-S042, E2-S011]. No official OpenAI start-up credit page was found, and a Mistral programme could not be confirmed [R: E2-S045] [NPV]. Whether AWS or Azure credits pay for third-party models on Bedrock or Foundry was not established [NPV]. A company living on credits is pulled towards the credit-giver's models, so the model sits behind a gateway from the first commit [AJ].

**2. A router that bills on its own account can forfeit the credits.** OpenRouter charges a platform fee of 5.5% on credit purchases on its Standard plan, and Cloudflare AI Gateway charges 5% on Unified Billing credits (volatile; re-verify) [VF: A4-S144, A6-S052]. Because Anthropic's credits only work on the first-party API [VF: E2-S008], paying for model calls through an intermediary's account can mean paying cash for calls that credits would have covered [AJ]. Keep the model contracts, and the credits, in the start-up's own accounts and use the gateway for routing only, with each provider's own keys [Rec].

**3. The thin gateway is cheap, but the March 2026 compromise makes pinning mandatory at any size.** LiteLLM's core is MIT and free to self-host [VF: A6-S001, A6-S007], and gateways ship virtual keys with per-key budgets and spend reports [VF: A7-S070, A6-S015]. Malicious LiteLLM releases 1.82.7 and 1.82.8 were published to PyPI on 24 March 2026, and 1.83.0 was the first build from the rebuilt pipeline [VF: A6-S008, A6-S009]. A five-person team is as exposed to a poisoned package as a bank, so the gateway must be version-pinned with hashes from day one [Rec].

**4. Model-vendor terms decide two product questions early: who may use the product, and whether you may train your own model.** The Gemini API terms and Google Cloud's generative AI terms bar services directed at, or likely to be accessed by, people under 18, and bar clinical use [VF: E2-S007, E2-S030]. Anthropic's Usage Policy applies to end users of products that integrate Claude, requires AI disclosure in consumer-facing chatbots, and requires qualified human review in high-risk uses [VF: E2-S005]. OpenAI and Anthropic bar using their services or outputs to build competing models, and Google bars using output to create models similar to a Google model except through its own tuning features [VF: E2-S026, E2-S004, E2-S007]. Treat distilling your own model from vendor outputs as barred until counsel reads the terms, and fine-tune Apache-2.0 weights instead (Gemma 4, gpt-oss, Mistral Large 3) [VF: A5-S034, E2-S003, A5-S074] [Rec].

**5. Fine-tuning does not change a start-up's role.** Supplying an AI system under its own name already makes the company its provider [VF: A8-S016], and a modifier becomes provider of a modified GPAI model only above one third of the original training compute [VF: E1-S034]. This reverses the FS view's "do not build yet" on fine-tuning (Part VIII): for a start-up it is a cost and quality decision [AJ].

**6. Tenant isolation, not model risk, is the start-up's first control problem.** OWASP LLM08:2025 names cross-context leakage in multi-tenant vector stores and recommends a permission-aware vector database [VF: E2-S051]. AWS's multi-tenant RAG guidance uses the silo, pool and bridge patterns, with per-tenant data sources and KMS keys in the silo model and automatic tenant-filter injection in the pool model [VF: E2-S050]. Azure's guidance keeps tenants' data out of a shared model unless they agree [VF: E2-S015]. Every retrieval, trace, evidence row and budget carries a tenant identifier, and a cross-tenant leak test runs in CI from the first paying customer [Rec].

**7. The first enterprise questionnaire arrives before the first regulator, and it has a standard AI format.** Buyers expect SOC 2 (2017 Trust Services Criteria with 2022 points of focus) and ISO/IEC 27001:2022, since 2013 certificates expired by 31 October 2025 [R: E2-S048, E2-S046]. CSA's STAR for AI Level 1 is a published AI-CAIQ self-assessment, while Level 2 needs ISO/IEC 42001 [VF: E2-S047]. The AI-CAIQ is a cheap, public answer to "send us your AI questionnaire" and can be filed long before an audit [AJ].

**8. EU rules cut a start-up's cost but not its duties, and two dates fall in the next quarter.** AI Act SME measures cut fees, documentation and fines (XV.6) [VF: E1-S029, E1-S031]. Software, including SaaS, is a product under the Product Liability Directive from 9 December 2026 [VF: E1-S010, E1-S011]. The Article 50(2) marking grace period ends on 2 December 2026 and covers only systems already on the market, so a product launched now has none [VF: R-EUAIA, A8-S018] [AJ].

**9. Free tiers are short-lived evidence, and the neutral tools keep changing owner.** Free observability tiers keep data for 15 to 60 days [VF: A1-S047, A1-S031, A1-S123], and Langfuse, Promptfoo and Helicone all changed owner in 2026 [VF: A1-S021, A1-S024, A7-S112]. The evaluation dataset and the prompts are product IP and belong in Git [Rec].

## XV.3 Scoring for this view

The SU weights re-weight the same eight Stage B criterion scores; no fact or score changes, and the weights are architectural judgement (`views.json`) [AJ].

| Criterion | FS weight | SU weight | Reason for the change [AJ] |
|---|---:|---:|---|
| Technical capability | 15 | **25** | The product is the technology; capability decides whether it works at all |
| Enterprise readiness | 15 | **5** | SSO, SCIM, audit logs and support tiers matter little before the first enterprise deal |
| Security and compliance | 20 | **10** | Still material (customers' data), but certifications are the vendor's, and the start-up's own come later |
| Deployment flexibility | 15 | **5** | One cloud and one region are enough until a customer asks for more |
| Ecosystem | 5 | **15** | Documentation, examples and integrations decide developer speed |
| Reliability and maturity | 10 | 10 | Unchanged: a broken dependency stops a small team as surely as a large one |
| Cost and TCO | 5 | **20** | Runway; free tiers and open licences matter |
| Lock-in and portability | 15 | **10** | Kept moderate, so that exits stay open cheaply |

**What moves, and why.** **57 of 138 scored products are core candidates, against 45 under FS weights**: 16 gain the fit and 4 lose it (`work/stageE/views/SU_scores.md`; full table in `05_Data/views.xlsx`). The movers follow the cost and ecosystem weights [AJ]:

- **Voyage AI** rises most (3.05 → 3.65, rank 7 → 2 in L7); its master tier stays Tactical, conditional on SOC 2 scope being evidenced [VF: A2-S044, A2-S143].
- **Model Armor** (3.35 → 3.80) becomes the top guardrail because its first 2 million tokens a month are free (volatile; re-verify) [VF: A6-S067]; it stays Strategic, conditional on Google Cloud.
- **Cloudflare AI Gateway**, **Agent Skills**, **Guardrails AI** and **Helicone** gain 0.35–0.40 on cost, but none becomes a core candidate; the last two stay Experimental [VF: A7-S112, V2-S071].
- **MCP** becomes the top L4 item (3.85), **LiteLLM** extends its C1 lead (4.20) and **pgvector** moves to first in L6 (4.40) [AJ].
- The enterprise platforms fall: Milvus/Zilliz and SPIFFE/SPIRE by 0.30; Pinecone, W&B Weave, PromptLayer and Credo AI by 0.25. Pinecone, Arize AX, Presidio and prompts-as-code lose core-candidate fit [AJ].

**Where this Part overrides the computed fit [AJ].** The fit is indicative, and four results are overridden by judgement on stated evidence:

| Item | Computed SU fit | This Part's advice | Reason |
|---|---|---|---|
| IBM watsonx.governance (C8, Tactical) | Core candidate (3.70) | Not at this stage | Technical 5 drives the score, but the AWS SaaS bundle is listed at US$38,160 a year (volatile; re-verify) [VF: A7-S103] |
| Prisma AIRS (C7, Tactical) | Core candidate (3.60) | Not at this stage | A runtime security platform is a buyer-side purchase; capability separation costs nothing [AJ] |
| Prompts-as-code (C5, Strategic) | Situational (3.45) | Default | Free, open formats [VF: A7-S067, A7-S066]; its technical 3 reflects a pattern, not a weakness |
| Presidio (C3, Strategic, cond.) | Situational (3.50) | Default redactor, in-process | MIT and free [VF: A6-S040]; the score falls only because enterprise readiness is down-weighted |

## XV.4 The architecture for this view

The architecture is the master's layer model with every control kept as a **point** but collapsed into the product's own codebase, cloud account and database [AJ]. Four things are built in the first fortnight because they cost days and are expensive to add later: the gateway with per-tenant keys, the tenant identifier on every row, OpenTelemetry tracing, and an evaluation set with the prompts in Git [Rec]. Everything in the dashed box waits for a customer who asks [Rec].

![Start-up architecture: one thin control plane, built in the first fortnight](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/SU-1.png){width=100%}

*Figure: A small team runs one product on one cloud account and one Postgres database. Every model call passes through a pinned gateway that holds the routes, per-tenant budgets and model pins. The model writes only inside deterministic workflow code, and the code checks every output before a person sees it. Traces and evaluations leave from day one through OpenTelemetry. The dashed box holds what the first enterprise customer will ask for, which is added then and not before. Editable source: `08_Graphic/diagrams/SU-1.md`.* [AJ]

Two FS principles survive intact: deterministic workflows with one bounded model step rather than autonomous loops (Part I, finding 4), and no model writes to a system of record (Part VI.3) [AJ]. What changes is that the control plane is a handful of modules owned by the product engineers, and the evidence store is a table, not an archive [AJ].

## XV.5 Layer by layer, then control by control

Master tiers are quoted as S (Strategic), T (Tactical) or E (Experimental); "SU core" or "SU situational" is the computed fit from XV.3 [AJ].

| Layer / control | Default for a start-up | Change from the FS view | Why |
|---|---|---|---|
| L1 models | One mid-tier vendor primary, chosen by a bake-off on the product's evaluation set and by the credits held: OpenAI GPT (S; SU core, 4.30), Anthropic Claude (S, cond.; SU core; independent alternatives GPT-6.1 Sol, Mistral Medium 3.5 or Gemini 3.8 Flash), Mistral (S; SU core) or Gemini (S, cond.; SU situational) on Google credits. A second vendor qualified on the same set; a small tier for triage | First-party APIs allowed; no self-hosted exit route at first | Mid tiers list at US$2 / US$10 per 1M tokens (GPT-6.1 Sol, Claude Sonnet 5.5) and small tiers at US$0.10 / US$0.50 (GPT-6 Luna, Claude Haiku 5.5) (volatile; re-verify) [VF: A5-S004, A5-S011]. The master's hyperscaler-only condition for Claude is a residency condition; Claude has no first-party EU or UK inference [VF: A5-S018, V2-S075] [AJ] |
| L2 inference | The vendors' own endpoints; Together AI (T; SU core) only for an open-weight model; vLLM (S; SU core, 4.45) once volume justifies a GPU | No in-region hyperscaler requirement until a customer asks; no own GPUs | An on-demand H100 lists at US$8.00 an hour on Fireworks (volatile; re-verify) [VF: A4-S135] [AJ] |
| L3 orchestration | Plain code first; LangGraph (S; SU core, 4.35) with a Postgres checkpointer when a flow needs state or interrupts; Pydantic AI (S, cond.; SU core) for typed Python; Vercel AI SDK (T) for TypeScript | Temporal (S) not needed at first; no managed agent runtime | LangGraph and Pydantic AI are MIT and Production/Stable [VF: A4-S001, A4-S003]; the Claude Agent SDK (E, Alpha) and OpenAI Agents SDK (T, 0.x) only as a sandboxed sub-step [VF: A4-S006, A4-S005] |
| L4 tools | Read-only connectors written in-house; MCP (S, cond.; SU core, 3.85) where a server already exists, OpenAPI tools as the independent alternative; E2B (T) for generated code | No separate tool-governance gateway; the allow-list lives in code | E2B Hobby is free with a US$100 credit (volatile; re-verify) [VF: A3-S104]; after Composio's token exposure, customers' tokens stay in the start-up's own store [VF: B-L4-S007] |
| L5 memory | None; per-tenant settings are ordinary rows | Same as FS (memory last), with no memory API | Mem0 and Zep become SU core on cost [VF: A3-S049, A3-S089], but nothing yet shows a gap they close [AJ] |
| L6 stores | pgvector (S; SU core, 4.40) in the application's Postgres, tenant column on every row, filter inside the query | Isolation per tenant, not per mandate | One database to secure, export and erase [AJ]; free under the PostgreSQL licence [VF: A2-S050] |
| L7 retrieval optimisation | The primary vendor's embedding model, or Voyage (T; SU core) once its scope is evidenced; Sentence Transformers (S; SU core) as exit; `model_version` on every vector | Hosted embeddings acceptable | text-embedding-3-small costs US$0.02 per 1M; voyage-4 US$0.06 with 200M tokens free (volatile; re-verify) [VF: A2-S001, A2-S007] |
| L8 ingestion | Docling (S; SU core, 4.25) in a background job; LlamaParse (T) free tier for hard documents | No ingestion envelope; a per-document record of source, tenant and parse version | Docling is MIT [VF: A1-S057]; LlamaParse gives 10,000 free credits a month (volatile; re-verify) [VF: A1-S116] |
| L9 evaluation | OTel instrumentation; Langfuse Cloud (S, master condition self-hosted; SU core) or Opik (T; SU core); DeepEval (T) in CI; Promptfoo (T) for red-team cases | Managed SaaS, not self-hosted; one red-team tool, not two | Langfuse Hobby is free, Core US$29 a month; Opik Pro US$19 (volatile; re-verify) [VF: A1-S031, A1-S123]; every L9 product ingests OTel [VF: A1-S032, A1-S049] |
| C1 gateway | LiteLLM open source (S, cond.; SU core, 4.20), pinned with hashes, one deployment | No Enterprise licence or second deployment at first | The master condition (hardened, pinned) still applies [VF: A6-S001, A6-S008] [AJ] |
| C2 guardrails | Deterministic checks in code; Model Armor (S, cond.; SU core) on Google Cloud, else the cloud's detector or NeMo Guardrails (T) | One detector, not two | Model Armor's first 2M tokens a month are free (volatile; re-verify) [VF: A6-S067]; figure checks are domain logic [AJ] |
| C3 privacy | Presidio (S, cond.; SU situational) in-process for trace redaction; placeholders for names in prompts; Sensitive Data Protection (S, cond.; SU core) on Google Cloud | Two enforcement points (prompt, trace export), not six | Presidio is MIT and community-governed [VF: A6-S040] |
| C4 identity | Auth0 for AI Agents (S, cond.; SU core, rank 4 → 2) for sign-in, tenant context and delegated tokens; OPA (S) when policy outgrows code | Customer identity, not workforce identity | Auth0 Free covers 25,000 MAU (volatile; re-verify; page may be stale) [VF: A6-S098] |
| C5 configuration | Prompts, pins and routes in Git with a CI evaluation gate (S); Langfuse Prompts (S) for run-time delivery | The second approver is a co-founder's review | Prompt management is in Langfuse's MIT core [VF: A7-S074] |
| C6 FinOps | Gateway keys per tenant (S); a cost-per-tenant table with FOCUS (S) column names | No FinOps tool; cost against revenue per tenant | Budgets ship in the gateway [VF: A6-S015, A7-S070] |
| C7 security | Pinned dependencies; cloud secret store; capability separation; safetensors (S) if weights are self-hosted | No runtime security platform | The supply chain is the realistic attack path [VF: A6-S008] [AJ] |
| C8 governance | An evidence table keyed by trace ID; a one-page AI register | No governance platform; OpenLineage (S) later | Customers ask for the register before any tool [AJ] |

## XV.6 Regulation, contracts and customer assurance

**The AI Act role is provider from launch.** Supplying an AI system under the company's own name makes it the provider, whichever vendor's model is underneath [VF: A8-S016]. Article 50(1) requires people to be told they are dealing with an AI system unless it is obvious, and Article 50(2) requires synthetic text to be marked machine-readably where technically feasible, but not for assistive editing that does not substantially alter the input [VF: E1-S035, E1-S036]. Whether a drafting assistant whose output a professional then edits falls inside the assistive-editing exception was not established from the evidence [NPV]. Treat drafted text as in scope until counsel says otherwise, and consider the voluntary Code of Practice on Transparency of AI-generated Content, which about 190 organisations had signed by August 2026, as the accepted route to show compliance [VF: E1-S037] [Rec].

**SME and start-up reliefs.** Article 62 gives priority sandbox access, tailored training and reduced conformity fees; sandboxes are free, documentation may be simplified, and fines are capped at the lower of the percentage or fixed amount [VF: E1-S029, E1-S030, E1-S032, E1-S031]. They cut cost, not obligations. Annex III high-risk duties (from 2 December 2027) arise only in listed uses such as hiring or credit scoring [VF: A8-S011], and a start-up heading there should join a sandbox before building [Rec].

**Product rules: CRA, PLD and the Data Act.**

| Rule | When it bites a start-up | What to do [Rec] |
|---|---|---|
| Cyber Resilience Act | Anything downloadable sold in the EU (desktop app, add-in, SDK, mobile app relying on the maker's API) makes the company a CRA manufacturer from its first sale; reporting has applied since 11 September 2026, the main obligations from 11 December 2027 [VF: E1-S001, E1-S002] | Keep the first release web-only if possible; otherwise set up 24/72-hour reporting and an SBOM now; small firms are spared only the fine for a missed 24-hour warning [VF: E1-S001] |
| Product Liability Directive | Software, including SaaS, is a product from 9 December 2026 [VF: E1-S010, E1-S011] | Keep release history, evaluation results and logs; disclosure orders make them the main defence [VF: E1-S010] [R: E1-S013] |
| Data Act switching | From 12 January 2027 no switching charges, including egress, for cloud and SaaS; customers get at most two months' notice, a 30-day transition and machine-readable export [VF: E1-S025, E1-S026] | Build tenant export early; it is a duty to EU customers and also lowers the cost of leaving a cloud when credits run out [AJ] |
| UK | No CRA equivalent; the voluntary Software Security Code of Practice (14 principles, self-assessed) is the buyer's reference [VF: E1-S051, E1-S052] | File the self-assessment with the first questionnaire |

**United States.** Most state AI duties apply only where a product makes, or helps make, consequential decisions about individuals [VF: R-US-STATE-AI] [AJ]. Texas TRAIGA (in force since 1 January 2026) prohibits AI built or used with intent to harm or discriminate unlawfully [VF: E1-S042, E1-S043]. California's SB 53 and AI Transparency Act apply only above US$500m revenue or 1,000,000 monthly users, and the CPPA's ADMT rules apply to significant decisions from 1 January 2027 [VF: E1-S044, E1-S045, E1-S047]. Colorado's law is stayed pending rulemaking [VF: E1-S040]. A productivity product that decides nothing about a person sits outside almost all of it [AJ].

**Data transfers.** Personal data sent to US model APIs relies on the EU–US Data Privacy Framework, still in effect with an appeal pending, or on standard contractual clauses [VF: A8-S053]. Anthropic's DPA includes SCCs, a UK Addendum and notice of new subprocessors [VF: E2-S012]. OpenAI offers EU residency for new projects with Modified Abuse Monitoring or ZDR, but its UK option does not process in the UK [VF: A5-S006]; Mistral hosts in the EU by default [VF: A5-S075]. The subprocessor list is the model portfolio, so a vendor change is a customer notification, not just configuration [AJ].

**Terms the start-up must flow down [Rec].** Its own terms of service should pass on the model vendors' usage policies, the AI-disclosure duty, the instruction that factual outputs need checking (an Anthropic Commercial Terms requirement), and, on Google models, the under-18 and clinical-use bars [VF: E2-S004, E2-S005, E2-S007]. Anthropic may suspend a customer for its users' breaches, so the start-up carries its tenants' misuse risk [VF: E2-S004] [AJ]. Anthropic's Usage Policy page carries an effective date of 12 November 2026, so the current version should be re-read before launch [VF: E2-S005].

**Customer assurance, sequenced to the sales pipeline.** The order below is the author's judgement on reported buyer expectations; it is not a published standard [AJ].

| Stage | Trigger | Evidence to have [Rec] | Source |
|---|---|---|---|
| 1 | First paying customer | Security page; DPA; subprocessor list (the model vendors); AI disclosure; data-export route | [VF: E2-S012, E1-S025] |
| 2 | First questionnaire | AI-CAIQ self-assessment published as STAR for AI Level 1; UK Software Security Code self-assessment; the model vendors' certificates by reference | [VF: E2-S047, E1-S051, A5-S007, A5-S021] |
| 3 | First enterprise deal | SOC 2 Type I, then Type II over the next window; SSO and SCIM; audit log export | [R: E2-S048] |
| 4 | EU enterprise and regulated buyers | ISO/IEC 27001:2022 (never 2013); EU processing route; for FS buyers, DORA Article 30 clauses (Part XVI covers the vendor side) | [R: E2-S046] [VF: E1-S055] |
| 5 | AI-specific scrutiny | ISO/IEC 42001 and STAR for AI Level 2 | [VF: E2-S047] |

## XV.7 Reference stack

The cloud-neutral column is the default; orchestration (LangGraph or Pydantic AI in the product's container) and evaluation (Langfuse Cloud or Opik via OTel) are the same on every cloud, so a row appears only where a cloud changes the answer [AJ]. Choose one cloud, usually the one whose credits are largest for the models you will actually use [Rec].

| Layer / control | Cloud-neutral default | AWS | Azure | Google Cloud |
|---|---|---|---|---|
| Credits (volatile; re-verify) | Claude for Startups via a partner VC, up to US$100K, first-party API only (independent alternatives: the hyperscaler programmes in this row) [VF: E2-S008]; NVIDIA Inception, free, with partner cloud credits [VF: E2-S044] | Activate: US$1,000–5,000 Founders, up to US$200,000 Portfolio [VF: E2-S042]; coverage of third-party Bedrock models [NPV] | Up to US$150,000 across eligible Azure services [VF: E2-S011]; tier mechanics third-party only [R: E2-S043] | Up to US$350,000 for AI-first, Google models only [VF: E2-S009, E2-S010] |
| L1 models | First-party APIs of the primary vendor and the qualified second vendor | Claude or a GPT-6 tier on Bedrock when a customer needs EU processing (confirm GPT-6 EU availability) [VF: A5-S008, V2-S079] | GPT-6.1 Sol on Foundry, Global Standard US$2 / US$10 per 1M; Data Zone EU when needed [VF: A5-S004] | Gemini 3.8 Flash at US$0.75 / US$3.75 per 1M until 31 December 2026, doubling on 1 January 2027; Gemma 4 managed at US$0.15 / US$0.60 [VF: A5-S027, V2-S010] |
| L6 stores | pgvector on the managed Postgres | RDS or Aurora [VF: B-L6-S004] | Azure Database for PostgreSQL [VF: B-L6-S005] | Cloud SQL [VF: B-L6-S005] |
| C1 gateway | LiteLLM open source, pinned | Same; AgentCore Gateway (S, cond.) only if the product moves onto AgentCore | Same | Same |
| C2 guardrails | Code checks + NeMo Guardrails | Bedrock Guardrails (S, cond.) [VF: A6-S072] | Azure AI Content Safety (S, cond.) [VF: A6-S055] | Model Armor, 2M tokens a month free [VF: A6-S067] |
| C3 privacy | Presidio in-process | Same | Same | Sensitive Data Protection [VF: A6-S065] |
| C4 identity | Auth0 for AI Agents | Same; AgentCore Identity only with AgentCore | Same | Same |

**What differs from Stack D.** The master's minimal stack (Part VII) is a regulated firm's minimum. This stack drops its in-region model service, second gateway instance, workforce-IdP agent registration, WORM archive and second red-team tool. It adds tenant isolation, customer identity, per-tenant cost and data export [AJ].

## XV.8 Build vs buy, and lock-in

**The rule.** Build what is the product, which means the workflow, the domain checks, the evaluation set and the tenant model. Buy or adopt everything else on a free or open tier, behind an interface the team owns. Do not build anything a customer has not yet asked for [AJ].

| Component | FS decision (Part VIII) | Start-up decision | Note [AJ] |
|---|---|---|---|
| Foundation models | Buy | Buy; fine-tune Apache-2.0 weights only when the evaluation set shows a gap | Distilling from vendor outputs is barred or legally unclear (XV.2, finding 4) |
| Serving | Buy access; open engine for exit | Buy access only | The open-weight route is a later cost lever, not a regulatory exit |
| Evaluation | Hybrid | Adopt a SaaS platform; build the dataset and the scorers | The dataset is IP and the regression baseline |
| Gateway | Hybrid, Enterprise-licensed | Adopt the open-source core; buy Enterprise only when a customer asks for SSO and audit on it | [VF: A6-S001] |
| Identity | Buy the IdP, build the policy | Buy hosted customer identity | Writing authentication is not a start-up's edge |
| Governance | Build the store, buy the workflow (optional) | Build a table and a one-page register | A platform is a buyer's tool |

**Lock-in that traps a start-up, and the cheap insurance against it.**

| Trap | Evidence | Insurance [Rec] |
|---|---|---|
| Credits pull the whole product onto one vendor's models and SDK | Google credits cover Google models only; Anthropic's cover the first-party API only [VF: E2-S010, E2-S008] | An OpenAI-compatible call through the gateway; no vendor SDK in product code; second vendor qualified quarterly |
| Vendor-hosted agent state | Hosted agent APIs hold the run state at the vendor [VF: A4-S055, A4-S123] | State in the start-up's own Postgres checkpointer |
| Evaluation data in a vendor UI | Free tiers keep 15–60 days [VF: A1-S031, A1-S123] | Datasets and results exported to Git or object storage |
| Customers' OAuth tokens in a broker | Composio incident [VF: B-L4-S007] | Own secrets store, per-tenant scopes |
| Licence surprises at scale | Mistral Medium 3.5 reportedly needs a commercial licence above about US$20m monthly revenue, and Qwen3.8-Max above US$50m [R: E2-S027, E2-S025]; Llama 4 multimodal grants no rights to EU-domiciled companies [VF: E2-S002] | Prefer Apache-2.0 or MIT weights; record each licence in the AI register |
| Acquired tools change terms | Four neutral tools changed owner in 2026 [VF: A1-S021, A1-S024, V2-S025, A7-S112] | OTel instrumentation; open cores you could self-host |

**Where multi-vendor pays for a start-up.** It pays in one place: a second model vendor qualified on the same evaluation set, because a single vendor's outage, retirement or policy suspension stops the product. A three-week Fable 5 outage and short Gemini Flash lifetimes show the risk [VF: V2-S004, B-L1-S003] [AJ]. Everything else in Part IX.3's "necessary" list, such as two gateway deployments, two guardrail detectors and two red-team tools, can wait for the first enterprise contract [AJ].

## XV.9 Roadmap

The phases are sized to a team of five to twenty and to a funding round, not to a regulatory calendar; dates assume a start in October 2026 [AJ].

| Phase | When | Scope [Rec] | Exit criteria [Rec] |
|---|---|---|---|
| 0. Foundations | Weeks 0–2 | Gateway with per-tenant keys and budgets; OTel tracing to a free-tier platform; prompts, model pins and an evaluation set of 50–200 real cases in Git with a CI gate; `tenant_id` on every table; AI register started | A model change is a one-line pull request that runs the evaluation set |
| 1. Design partners | Weeks 2–10 | The first workflow with one bounded model step and deterministic checks; read-only connectors; Article 50 disclosure; second vendor qualified on the set | Design partners use it weekly; numeric checks at 100%; cost per tenant measured |
| 2. Paying customers | Months 3–6 | DPA and subprocessor list; cross-tenant leak test in CI; tenant data export; batch and caching on stable prefixes; incident and vulnerability-reporting route | Leak test returns zero; cost per tenant inside the target share of revenue |
| 3. First enterprise deal | Months 6–12 | AI-CAIQ (STAR for AI Level 1); SOC 2 Type I, then Type II; SSO and SCIM; audit-log export; EU processing route; dedicated-tenant option for one large customer | The first security questionnaire is answered from existing evidence |
| 4. Scale | Months 12–24 | Gateway Enterprise licence and second deployment; ISO/IEC 27001:2022; a self-hosted open-weight small model where volume pays; a second red-team tool | Passes an FS buyer's due diligence without re-platforming |

**Dates inside the first year.**

| Date | Event | Consequence for the roadmap [AJ] |
|---|---|---|
| 30 November 2026 | OpenAI Agent Builder shuts down [VF: A4-S054] | Any prototype built there moves to code in Phase 0 |
| 2 December 2026 | Article 50(2) marking grace period ends for systems already on the market [VF: R-EUAIA, A8-S018] | No grace period for a new launch |
| 9 December 2026 | PLD applies to products placed on the market [VF: E1-S010, E1-S011] | Release history and evaluation logs kept from Phase 0 |
| 1 January 2027 | Gemini 3.8 Flash price doubles; CPPA ADMT rules apply [VF: V2-S010, E1-S047] | Re-run the cost model; confirm no significant decisions |
| 12 January 2027 | Data Act: no switching charges [VF: E1-S025, E1-S026] | Export route ready for EU customers |

## XV.10 Worked example

**The use case.** A five-person start-up builds an AI assistant for small accounting firms. It drafts client e-mails and summarises bookkeeping anomalies. It must ship in weeks, keep model spend below a set share of revenue, and pass its first customer's security questionnaire within a year (`views.json`) [AJ]. Each accounting firm is a tenant, and the data is the firm's clients' bookkeeping records, much of it personal or confidential [AJ].

**The architectural reading.** As in Part VI, this is a deterministic workflow, not a free agent: rules in code find the anomalies, figures come from the ledger, and the model writes prose around figures it is given. The accountant edits and sends; the product never sends or changes a ledger. The use is not Annex III and decides nothing about a person [AJ].

| Step | What happens | Components |
|---:|---|---|
| 0 | Release manifest in Git: prompt versions, model pins for the mid and small tiers, route, evaluation thresholds | C5 |
| 1 | The accountant signs in (MFA); the session carries the firm's tenant ID | C4 |
| 2 | Nightly job: the connector reads the firm's ledger through the bookkeeping platform's API with the firm's delegated, read-only token from the secrets store | L4, C4, C7 |
| 3 | Rules in SQL flag candidate anomalies (duplicate payments, unusual amounts, missing references); the model is not involved | L3 |
| 4 | The small tier triages flagged items as a batch job through the gateway, under the tenant's key and budget | C1, L1, C6 |
| 5 | The mid tier drafts one anomaly summary per client from the flagged rows, which are passed in as data | C1, L1 |
| 6 | A deterministic check confirms that every amount, date and account in the summary matches the source rows; a mismatch triggers one retry, then "needs review" | C2, L9 |
| 7 | The accountant asks for a client e-mail; the firm's templates and previously sent e-mails are retrieved, filtered by tenant inside the query | L6, L7 |
| 8 | The prompt uses placeholders for client names and identifiers; the application fills them in after generation | C3 |
| 9 | The e-mail is drafted on the mid tier; output checks confirm placeholders are intact, no figure is absent from the source, and there is no tax advice | C1, C2 |
| 10 | The accountant edits and sends it from their own e-mail system; the edit diff is recorded | L3, L9 |
| 11 | The OTel trace (redacted) goes to the evaluation platform; a sample is scored by a small-tier judge | L9, C3 |
| 12 | An evidence row is written: trace ID, tenant, manifest version, model ID as returned, check results, cost, and the user who sent it | C8, C6 |

**Boundaries.**

**May [Rec]:** draft e-mails and anomaly summaries for the accountant to edit; explain why a rule flagged an item, using the rule's output; suggest wording from the firm's own templates.

| Must never [Rec] | Enforced by |
|---|---|
| Send an e-mail or post to the ledger | No write tool exists (L4); sending happens in the accountant's own system |
| Invent, round or "correct" a figure | Deterministic check (C2); blocking evaluation (L9) |
| Read another firm's data | Tenant filter inside every query; leak test in CI (L6) |
| Give tax or legal advice | Denied-topic check (C2); disclosure text |
| Send identifiers to a vendor not on the subprocessor list, or run on an unpinned model | Placeholders (C3); gateway routes and pins in Git (C1, C5) |
| Use one firm's data to improve another's output without consent | Per-tenant retrieval; no shared tuning [VF: E2-S015] |

**The evidence kept, and who asks for it.**

| Element | Contents | Who will ask [AJ] |
|---|---|---|
| Manifest and model | Prompt, model and threshold versions; exact model ID and region as returned | The questionnaire; the DPA and subprocessor review; the PLD defence [VF: E1-S010] |
| Source snapshot | Ledger rows and rule outputs used, by hash | Support, when an accountant disputes a summary |
| Checks and human action | Numeric, placeholder and judge results; who edited and sent, and the diff | The questionnaire's AI section; the Article 50 position |
| Cost | Tokens and cost per step, by tenant | Gross margin |

**What it costs [AJ].** These are the author's own illustrative figures at list prices (volatile; re-verify). Assume a firm with 50 clients, 200 e-mails a month (6,000 input tokens, 4,000 of them a cached prefix, and 400 output), a monthly summary per client (8,000 in, 800 out) and small-tier triage (20,000 in per client). At US$2 / US$10 per 1M for the mid tier and US$0.10 / US$0.50 for the small tier [VF: A5-S004, A5-S011], that is about US$4.50 per firm per month. With cached input (US$0.10 per 1M on GPT-6.1 Sol; 0.05x on Claude Sonnet 5.5) and batch at 50% for nightly jobs [VF: A5-S004, V2-S002], it is about US$2.30 before cache-write charges. Tokens are not the margin risk at this scale. A runaway loop or a default to the frontier tier (US$10 / US$50 per 1M) is, which is why the per-tenant budget comes in Phase 0 [VF: A5-S004] [AJ].

## XV.11 Checklist, what to avoid, what to monitor

**Checklist [Rec].**

- [ ] Every model call goes through one pinned gateway with a key and budget per tenant (C1, C6).
- [ ] Prompts, model pins, routes and the evaluation set are in Git, and CI runs the set on every change (C5, L9).
- [ ] A second model vendor is qualified on the same set and can be switched to by configuration (L1).
- [ ] `tenant_id` is on every row, vector, trace and evidence record, and a cross-tenant leak test runs in CI (L6).
- [ ] Figures in outputs are checked deterministically against source data (C2).
- [ ] No tool writes to a customer's system of record; customers' tokens are in your own store; identifiers are redacted before traces leave (L4, C7, C3).
- [ ] The AI register records the provider role, Article 50 position, subprocessors and model licences, and the terms flow down the vendors' usage policies (C8).
- [ ] Credits and their expiry dates are on the finance calendar, with the post-credit cost per tenant modelled [Rec].

**What to avoid (evidence-based) [Rec].**

| Avoid | Evidence |
|---|---|
| Unpinned LiteLLM installs, and versions 1.82.7 and 1.82.8 | [VF: A6-S008, V2-S027] |
| Helicone for new adoption (maintenance mode) | [VF: A7-S112, V2-S043] |
| Composio managed cloud holding customers' tokens | [VF: B-L4-S007] |
| OpenAI Agent Builder for anything new (shuts 30 November 2026) | [VF: A4-S054] |
| Guardrails AI's hosted hub (retired) | [VF: V2-S071] |
| Google generative AI models in a product likely to be used by under-18s | [VF: E2-S007, E2-S030] |
| Llama 4 multimodal models for an EU-domiciled company | [VF: E2-S002] |
| Jina weights without a commercial licence; a modified Firecrawl server without AGPL compliance | [VF: A2-S024, A1-S053] |
| Paying for model calls through a router's credits when your own credits would cover them | [VF: A4-S144, E2-S008] [AJ] |

**What to monitor [Rec].**

| Monitor | Trigger for action |
|---|---|
| Start-up programme terms (Google, AWS, Microsoft, Anthropic, NVIDIA); OpenAI and Mistral programmes [NPV] | Re-verify each quarter; re-run the model bake-off when credits end [VF: E2-S008, E2-S009, E2-S011, E2-S042, E2-S044] |
| Anthropic Usage Policy effective 12 November 2026 | Re-read and update the flow-down terms [VF: E2-S005] |
| Gemini 3.8 Flash price change and Flash retirements | Re-run cost per tenant; re-qualify [VF: V2-S010, B-L1-S003] |
| Claude Agent SDK and OpenAI Agents SDK reaching 1.0 | Re-score maturity before wider use [VF: B-REVC-S001] |
| Promptfoo–OpenAI closing; Langfuse under ClickHouse; OpenRouter–Stripe closing | Check pricing and free-tier changes [VF: A1-S024, A1-S021, V1-S059] |
| Voyage SOC 2 scope | Confirm before sending customer data [VF: A2-S044, A2-S143] |
| Mistral Medium 3.5 and Large 4 licences | Read the licence file before self-hosting at scale [R: E2-S027] [VF: A5-S076] |
| The agentic-SDLC evidence (Stage E, E3), not yet available | Add coding-agent and AI-code-review guidance for the start-up's own engineering when published; Part XVII covers the vendor side [NPV] |
