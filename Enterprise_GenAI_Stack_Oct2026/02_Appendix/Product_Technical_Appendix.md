---
title: "Product Technical Appendix"
subtitle: "Enterprise GenAI Full-Stack Architecture, October 2026"
---

This appendix holds the full record for every product assessed: current facts with their claim labels and source IDs (resolve in `06_References/bibliography.xlsx`), the assessment, the classification and the scorecard (generic and regulated-FS weights). Fact cells marked *Not publicly verified* could not be confirmed from a public source and were never guessed. Disclosure: researched and drafted by an Anthropic model; Anthropic-related items were scored on the same rubric, and tiers set by the reader at checkpoints are noted in the relevant chapter.

# L9: Evaluation and observability

## MLflow (GenAI capabilities: tracing, evaluation, prompt registry, AI Gateway) (`L9-mlflow-genai`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Apache-2.0, Linux Foundation-hosted and OTel-native, with managed options on the major clouds; the most portable platform of record where an ML platform already exists [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Tracing, evaluation, monitoring, prompt registry and gateway; red-teaming not native. |
| Enterprise readiness | 4 | Scored on the managed route the decision tree recommends. On Amazon SageMaker and Azure ML (A1-S103), platform IAM, SSO and audit logging are presumed under rule 6 (CP2 Q1), so 4 (within the rule 2 cap of 4); platform controls presumed (CP2 Q1); confirm per service. The Databricks, Nebius and OpenShift AI routes are not covered by the presumption, and the open-source tracking server's own controls remain NPV. |
| Security and compliance | 3 | Inherits host controls; clear Apache-2.0 licence and foundation hosting; managed-service certifications must be checked per provider. |
| Deployment flexibility | 5 | Five managed services, self-host and on-premises clusters. |
| Ecosystem | 5 | OTel- and MCP-native; managed by multiple clouds; integrated by other L9 tools (Langfuse guide). |
| Reliability and maturity | 5 | Since 2018, foundation-hosted. |
| Cost / TCO | 4 | Free; managed pricing per provider; tracking-server operations if self-hosted. |
| Lock-in / portability | 5 | Apache-2.0, Linux Foundation governance, OTel. |
| **Total (generic / FS)** | **4.25 / 4.25** | |

*Evidence rules applied:* Rule 2 (self-hosted software) applied: NPV cap not applied; enterprise_readiness and security_compliance scored on what the software enables and on project hygiene, capped at 4; inherits host controls; Rule 6 (CP2 Q1, hyperscaler presumption) applied at CP2 rework (8 October 2026) to the SageMaker and Azure ML managed routes: enterprise_readiness 3 -> 4; platform controls presumed (CP2 Q1); confirm per service

**Capabilities.** Apache-2.0 AI engineering platform: OTel-based tracing of LLM applications and agents, evaluation and quality monitoring, prompt registry and optimisation, and an AI Gateway, alongside the classic ML lifecycle [VF: A1-S103].

**Strengths**

- Managed offerings on Databricks, Amazon SageMaker, Azure ML, Nebius and Red Hat OpenShift AI, plus self-hosting and on-premises clusters [VF: A1-S103]
- Tracing built on OpenTelemetry; native MCP integration [VF: A1-S103]
- Hosted by the Linux Foundation since 2020 under a vendor-neutral open governance model [VF: B-L9-S004]
- Years of production use; first release June 2018 [VF: A1-S019]

**Limitations and risks**

- Strong Databricks association; code copyright Databricks [VF: A1-S019]
- Security and access-control features of the open-source tracking server not verified in the fact base [NPV]
- GenAI evaluation depth relative to specialist tools not assessed in primary sources [NPV]
- Spans gateway (C1) and prompt management (C5), which can blur ownership boundaries [VF: A1-S103]

**Choose when**

- MLflow already holds the firm's model inventory and lifecycle on Databricks, SageMaker or Azure ML, so GenAI evidence lands beside classic model evidence [AJ]
- You want the most neutral governance and licence in the layer [AJ]

**Avoid when**

- You would self-host the open-source server without putting it behind the firm's identity and access controls [AJ]
- Teams need richer agent-debugging UX than the platform offers and will not run a second tool [AJ]

**Nearest competitors:** L9-langfuse, L9-wandb-weave, L9-opik

**Regulated-FS note.** For firms whose model risk inventory already lives in MLflow, this is the shortest path to SS1/23-style monitoring evidence for LLM components; on SageMaker or Azure ML the platform's IAM, SSO and audit logging are presumed under CP2 Q1 but must be confirmed per service, and certifications and residency must be verified per provider [AJ].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | MLflow open-source project; code copyright Databricks, Inc. | Verified fact | A1-S019, A1-S103 |
| Category | Open-source AI engineering platform for agents, LLMs and ML models | Verified fact | A1-S103 |
| Version / lineup | mlflow 3.17.0, released 7 October 2026 | Verified fact | A1-S019 |
| Licence | Apache-2.0 | Verified fact | A1-S019 |
| Strategic direction | Repositioned as 'The Open Source AI Engineering Platform for Agents, LLMs & Models' with OTel-based tracing, evaluation and monitoring, prompt optimisation and an AI Gateway | Verified fact | A1-S103 |
| What it does | Captures traces of LLM applications and agents (built on OpenTelemetry), evaluates and monitors quality, manages and optimises prompts, and offers an AI Gateway for cost and model access control, alongside classic ML lifecycle features. | Verified fact | A1-S103 |
| Stack position | Cross-cutting L9 plus gateway (C1) and prompt management (C5) functions | Verified fact | A1-S103 |
| Integration | Python, TypeScript/JavaScript, Java SDKs; natively integrates with OpenTelemetry and MCP | Verified fact | A1-S103 |
| Dependencies | Tracking server (local or managed); deployable on Docker, Kubernetes, Azure ML, SageMaker | Verified fact | A1-S103 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Open source free; managed pricing set by each cloud provider | Verified fact | A1-S019, A1-S103 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Managed offerings on Databricks, SageMaker, Azure ML, Nebius, Red Hat OpenShift AI; tracing integrations incl. Databricks AI Gateway | Verified fact | A1-S103 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First PyPI release 4 June 2018; 190 releases | Verified fact | A1-S019 |
| Deployment | saas: Yes (managed by Databricks, Amazon SageMaker, Azure ML, Nebius, Red Hat OpenShift AI); managed_cloud: Yes; vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes; on_prem: Yes (on-premises clusters) | | |

## Langfuse (`L9-langfuse`)

**Tier:** Strategic · **Flags:** Acquired · **Original graphic label:** Langfuse – open source

*Rationale:* MIT core, OTel ingestion, self-hosting and certified EU Cloud make it a credible platform of record; ClickHouse ownership and the enterprise-gated audit/RBAC modules are the caveats [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Covers tracing, prompts, LLM-as-a-judge, datasets, experiments and annotation; no native red-teaming or documented trajectory metrics. |
| Enterprise readiness | 4 | SSO, project-level RBAC, audit logs and SCIM are documented, with SCIM, audit logs and project RBAC Enterprise-licensed when self-hosted (A1-S033): all three controls plus SCIM reach 4 under rule 7 (CP2 Q2). Not 5: SLA terms are not published and pages disagree on which tier carries SSO. |
| Security and compliance | 4 | SOC 2 Type II, ISO 27001, HIPAA BAA and isolated EU region on Cloud; no CMK/BYOK documented, so not 5 under the layer calibration. |
| Deployment flexibility | 4 | SaaS, private cloud, self-host and on-prem; BYOC not verified; air-gap not documented. |
| Ecosystem | 4 | OTel-native with broad integration guides; HTTP-only OTLP. |
| Reliability and maturity | 4 | GA, 555 PyPI releases since July 2023; ownership changed to ClickHouse in January 2026 with a stated unchanged roadmap. |
| Cost / TCO | 4 | Free MIT core and transparent Cloud pricing; ClickHouse operations and additive Enterprise pricing when self-hosted. |
| Lock-in / portability | 3 | Base 4 (MIT core, OTel ingest, own data model) reduced by 1 for the 2026 ownership change; governance is company-controlled. |
| **Total (generic / FS)** | **3.95 / 3.85** | |

*Evidence rules applied:* Rule 7 (CP2 Q2) applied at CP2 rework (8 October 2026): SSO, RBAC and audit logs plus SCIM verified (A1-S033); enterprise_readiness 3 -> 4

**Capabilities.** Open-core LLM engineering platform: OTel-based tracing of LLM calls, retrieval and agent actions; prompt versioning; LLM-as-a-judge and code evaluators over ingested traces; user feedback and manual labelling; datasets, experiments and a playground; public API [VF: A1-S073, A1-S032].

**Strengths**

- MIT core covers tracing, evals, prompt management, experiments and annotation; self-hosting on Docker, Kubernetes (Helm) or Terraform templates for AWS, Azure and GCP [VF: A1-S023, A1-S033, A1-S073]
- Native OTLP/HTTP endpoint and OTel-based SDKs, so instrumentation is not proprietary [VF: A1-S032]
- Langfuse Cloud has SOC 2 Type II and ISO 27001, isolated EU, US, HIPAA and Japan regions, and a DPA [VF: A1-S029, A1-S030]
- Published, unit-based Cloud pricing [VF: A1-S031]

**Limitations and risks**

- Owned by ClickHouse, Inc. (announced 16 January 2026); self-hosted Enterprise tier is bundled with ClickHouse commercial offerings [VF: A1-S021, A1-S033, V2-S041]
- SCIM, audit logging, retention policies, project-level RBAC and server-side ingestion masking need an Enterprise licence key when self-hosted [VF: A1-S033]
- OTLP over HTTP only (no gRPC); Langfuse-specific attributes take precedence over gen_ai.* [VF: A1-S032]
- Self-hosted telemetry is on by default (opt-out) [VF: A1-S033]
- SLA terms not published in sources reviewed [VF: A1-S031]

**Choose when**

- You want a self-hosted platform of record for traces, evals and prompts inside your own estate, with an MIT core and an enterprise licence for the audit and RBAC modules [AJ]
- Framework-neutral instrumentation through OTel matters more than deep integration with one agent framework [AJ]

**Avoid when**

- You need SCIM, audit logs and project RBAC but will not buy the Enterprise licence [AJ]
- You cannot operate a ClickHouse-backed service and do not want Langfuse Cloud [AJ]

**Nearest competitors:** L9-langsmith, L9-opik, L9-arize-phoenix, L9-mlflow-genai

**Regulated-FS note.** Best fit for a UK/EU manager that must keep traces (which contain client data) in-region or in-estate; budget for the Enterprise licence because audit logs and project RBAC are evidence controls, not extras; disable default telemetry [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Langfuse, acquired by ClickHouse, Inc. (announced January 2026); repository copyright now 'ClickHouse, Inc.' | Verified fact | A1-S021, A1-S022, A1-S023, A1-S073, V1-S007 |
| Category | Open-core LLM engineering platform: tracing/observability, prompt management, evaluations, datasets and playground | Verified fact | A1-S073 |
| Version / lineup | Python SDK langfuse 4.17.0, released 5 October 2026 (server release number not verified) | Verified fact | A1-S001 |
| Licence | Open core: MIT for all product capabilities (tracing, evals, prompt management, experiments, annotation, playground); code under ee/ directories needs a commercial licence key when self-hosted (SCIM, audit logging, data-retention policies, project-level RBAC, server-side ingestion masking) | Verified fact | A1-S023, A1-S033 |
| Status events | Acquired by ClickHouse, Inc.; announced with ClickHouse's US$400M Series D (announced 16 January 2026 per the ClickHouse blog); terms undisclosed | Verified fact | A1-S021, A1-S022, A1-S073, V1-S007 |
| Strategic direction | Joined ClickHouse in January 2026; founders state the roadmap is unchanged and the commitment to open source and self-hosting remains; self-hosted Enterprise tier is now bundled with ClickHouse Cloud, BYOC or Private and priced additively | Verified fact | A1-S021, A1-S022, A1-S033 |
| What it does | Instruments LLM applications and ingests traces of LLM calls, retrieval, embedding and agent actions; provides prompt versioning, LLM-as-a-judge and code evaluators, user feedback and manual labelling, datasets and experiments, a playground and a public API. | Verified fact | A1-S073 |
| Stack position | Cross-cutting observability and evaluation platform spanning development and production; graphic places it in L9 as 'open source', which is accurate for the core but omits the open-core split | Verified fact | A1-S073, A1-S033 |
| Integration | Native OTLP/HTTP endpoint (/api/public/otel, JSON and protobuf; no gRPC); Python SDK v3+ and JS SDK v4+ built on OpenTelemetry; maps gen_ai.* attributes to generations but Langfuse-specific attributes take precedence; OpenAPI spec and typed SDKs | Verified fact | A1-S032, A1-S073 |
| Dependencies | Built on ClickHouse (analytics store); self-hosted via Docker Compose, Kubernetes (Helm, preferred for production) or Terraform templates for AWS, Azure and GCP | Verified fact | A1-S073 |
| Certifications | Langfuse Cloud: SOC 2 Type II and ISO 27001 (reports on request, Pro/Team/Enterprise); HIPAA-ready region with BAA on eligible plans; annual third-party penetration tests | Verified fact | A1-S029 |
| GDPR / residency | Isolated regions: EU (AWS eu-west-1, Ireland), US (us-west-2), HIPAA (us-west-2) and Japan (ap-northeast-1); DPA available; Postgres backups copied within the same jurisdiction; self-hosting for full isolation | Verified fact | A1-S029, A1-S030 |
| Security features | Annual third-party penetration tests (Cloud); server-side ingestion masking (Enterprise module); self-hosted telemetry on by default (opt-out, but always on with an EE licence key) | Verified fact | A1-S029, A1-S033 |
| Access controls | SCIM, audit logs, project-level RBAC and retention policies are Enterprise modules when self-hosted; pages are inconsistent on whether SSO/RBAC sit in the open-source tier | Verified fact | A1-S033 |
| Enterprise support | Enterprise plan (US$2,499/month on Cloud); SLA terms not published in sources reviewed | Verified fact | A1-S031 |
| Pricing | Cloud: Hobby free (50k units/month, 30 days, 2 users); Core US$29/month; Pro US$199/month; Enterprise US$2,499/month; 100k units included on paid plans, then US$8 per 100k units, falling to US$6 per 100k above 50M; unit = trace + observation + score | Verified fact | A1-S031 |
| Infrastructure cost | Self-hosted Enterprise pricing is additive to a ClickHouse commercial plan; infrastructure sizing not verified | Verified fact | A1-S033 |
| Ecosystem | OpenTelemetry-based; integration guides for OpenLLMetry, MLflow, vLLM, Spring AI, GitHub Copilot and Go/Java/C#/Ruby via OTel | Verified fact | A1-S032 |
| Adoption signals | Over 20K GitHub stars and more than 26M SDK installs per month at end of 2025 (ClickHouse figures) | Verified fact | A1-S021 |
| Maturity | First PyPI release 12 July 2023; 555 PyPI releases to 5 October 2026 (frequent cadence) | Verified fact | A1-S001 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## LangSmith (`L9-langsmith`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** LangSmith – trace & eval

*Rationale:* Strongest commercial option for LangGraph estates with the certifications and deployment options FS needs. Strategic is conditional: only inside a LangGraph estate, and only with OTel dual-instrumentation as the exit route, because lock-in scores 2 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Offline and online evals, pytest plugin, prompt management and failure clustering; Engine still beta; red-teaming not native. |
| Enterprise readiness | 4 | SSO, RBAC, ABAC, gateway audit logging and support SLA on Enterprise; SCIM not documented in the fact base. |
| Security and compliance | 4 | SOC 2 Type II, ISO 27001:2022, HIPAA BAA, EU region; no CMK/BYOK documented, so not 5 under the layer calibration. |
| Deployment flexibility | 5 | SaaS (US/EU), BYOC (AWS), self-hosted and air-gapped self-host on Enterprise. |
| Ecosystem | 4 | Large LangChain ecosystem plus OTLP ingest; native format preferred. |
| Reliability and maturity | 4 | GA since 2023, 536 SDK releases, independent and funded (US$125M Series B, October 2025). |
| Cost / TCO | 3 | Transparent but per-seat plus per-trace; heavy self-host footprint. |
| Lock-in / portability | 2 | Proprietary platform, native format recommended, growing bundling with the agent runtime. |
| **Total (generic / FS)** | **3.95 / 3.80** | |

**Capabilities.** Proprietary observability, evaluation and deployment platform: native and OTel trace ingest, offline and online evaluation on datasets, prompt management, pytest plugin, and hosted agent deployment; now also Engine (beta), Fleet, Sandboxes and an LLM Gateway [VF: A1-S034, A1-S037, A1-S039, A1-S108].

**Strengths**

- Deepest coupling to LangGraph/LangChain, the orchestration framework many teams already use [VF: A1-S037, A1-S039]
- SOC 2 Type II, ISO 27001:2022, HIPAA (BAA on Enterprise) and GDPR; US or EU managed regions on all tiers [VF: A1-S036, A1-S126]
- SaaS, BYOC on AWS, self-hosted and air-gapped self-host on Enterprise [VF: A1-S034]
- Enterprise SSO, RBAC and ABAC; support SLA [VF: A1-S035]

**Limitations and risks**

- Native tracing format is recommended over OTel for performance, which pulls instrumentation towards a proprietary format [VF: A1-S037]
- Platform increasingly bundles the LangChain agent runtime (Fleet, Deployment), widening the blast radius of a vendor change [VF: A1-S039]
- Self-hosting needs at least 16 vCPU / 64 GB plus PostgreSQL, Redis and ClickHouse [VF: A1-S034]
- Per-seat Plus pricing plus per-trace overage [VF: A1-S035]
- LangSmith Engine is public beta [VF: A1-S039]

**Choose when**

- LangGraph is your orchestration standard and you want one supported platform for traces, evals and deployment [AJ]
- You need a commercial vendor with SOC 2, ISO 27001 and an EU region, or BYOC/self-host for residency [AJ]

**Avoid when**

- Your agents are framework-heterogeneous and you want a neutral trace store [AJ]
- You do not want the observability vendor to also be your agent runtime vendor [AJ]

**Nearest competitors:** L9-langfuse, L9-braintrust, L9-arize-ax

**Regulated-FS note.** Use the EU region or self-host for client data; instrument with OTel GenAI conventions even if native SDKs are also used, so the evidence trail survives a platform exit; keep Engine-proposed fixes behind change control [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LangChain, Inc. (independent; US$125M Series B at US$1.25B valuation, 20 October 2025) | Verified fact | A1-S038 |
| Category | Proprietary agent and LLM observability, evaluation and deployment platform (now also hosting LangSmith Fleet, Engine, Sandboxes and an LLM Gateway) | Verified fact | A1-S034, A1-S039 |
| Version / lineup | SaaS (continuously released); Python SDK langsmith 0.14.4, released 2 October 2026 | Verified fact | A1-S002 |
| Licence | Proprietary platform; SDK MIT-licensed | Verified fact | A1-S002, A1-S108 |
| Status events | Agent Builder renamed LangSmith Fleet (2026); LangSmith Deployment billing moved to usage-based model; existing customers migrated 1 October 2026 | Verified fact | A1-S035, A1-S039, V1-S016 |
| Strategic direction | Interrupt 2026 (13-14 May): LangSmith Engine (public beta; clusters production failures and proposes fixes, can open PRs), SmithDB (claimed up to 15x faster; simpler self-hosting), Sandboxes GA, LLM Gateway with audit logging; Agent Builder renamed LangSmith Fleet; new Fleet pricing from 15 July 2026 | Verified fact | A1-S039 |
| What it does | Captures traces of LLM and agent runs, runs offline and online evaluations on datasets, manages prompts and hosts agent deployments; ingests native and OpenTelemetry traces. | Verified fact | A1-S034, A1-S037, A1-S108 |
| Stack position | Cross-cutting observability/evaluation plus agent deployment runtime; broader than the graphic's 'trace & eval' label | Verified fact | A1-S034, A1-S039 |
| Integration | Native SDKs (Python/JS); OTLP endpoint for any OTel exporter (x-api-key header); original OTel launch required OpenLLMetry conventions, newer guides use OTel GenAI conventions; native format recommended when LangSmith is sole backend; pytest plugin in SDK | Verified fact | A1-S037, A1-S108 |
| Dependencies | Self-hosted: Kubernetes (min. 16 vCPU, 64 GB) or Docker, PostgreSQL, Redis, ClickHouse, optional blob storage | Verified fact | A1-S034 |
| Certifications | SOC 2 Type II; ISO 27001:2022 (stated in LangChain resource page and LangSmith Engine security docs); HIPAA (BAA on Enterprise plan only); GDPR; reports via trust.langchain.com | Verified fact | A1-S036, A1-S126, V1-S068 |
| GDPR / residency | Managed cloud in US or EU (EU data stored in the Netherlands per academy page) on all tiers at no extra cost; DPA on request; trust centre trust.langchain.com | Verified fact | A1-S036 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Enterprise: custom SSO, ABAC and RBAC; audit logging for LLM Gateway administrative actions | Verified fact | A1-S035, A1-S039 |
| Enterprise support | Enterprise plan with support SLA, custom seats and workspaces | Verified fact | A1-S035 |
| Pricing | Developer US$0 (1 seat, 5k base traces/month); Plus US$39 per seat/month with 10k traces included, overage per trace; Enterprise custom, invoiced annually | Verified fact | A1-S035 |
| Infrastructure cost | Self-hosting requires a Kubernetes cluster of at least 16 vCPU / 64 GB plus PostgreSQL, Redis and ClickHouse | Verified fact | A1-S034 |
| Ecosystem | Works with LangChain/LangGraph and any framework via SDK or OTel; guides for Temporal, VS Code Copilot Chat and Microsoft Agent Framework | Verified fact | A1-S037 |
| Adoption signals | LangChain Series B investors include IVP (lead), Sequoia, Benchmark, CapitalG, Sapphire, ServiceNow, Workday, Cisco, Datadog and Databricks | Verified fact | A1-S038 |
| Maturity | First langsmith SDK release on PyPI 26 June 2023; 536 releases to 2 October 2026 | Verified fact | A1-S002 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (BYOC on AWS, Enterprise only); private_cloud: Yes (self-hosted in own cloud, Enterprise); self_hosted: Yes (Enterprise); on_prem: Yes (air-gapped self-host positioned) | | |

## Opik (`L9-opik`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Opik – comet

*Rationale:* Most permissive full-platform licence in the layer, but missing user management in the open edition and a young codebase keep it below the foundational tier [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Tracing, offline and online evals, guardrails and optimiser; red-teaming not native. |
| Enterprise readiness | 3 | Enterprise SAML/OIDC SSO, organisation and workspace roles with Enterprise custom roles (B-REV-S022); audit logs only on marketing pages; open edition has no user management. |
| Security and compliance | 4 | SOC 2 Type 2 and ISO 27001:2022 at Comet level; residency NPV; no CMK documented. |
| Deployment flexibility | 4 | Comet SaaS, self-host on Kubernetes, on-prem as part of Comet; BYOC not verified. |
| Ecosystem | 3 | OTel HTTP, PyTest, MCP and a moderate integration list. |
| Reliability and maturity | 3 | 635 releases since September 2024; young and fast-moving. |
| Cost / TCO | 5 | Free full-platform self-hosting and low cloud entry price. |
| Lock-in / portability | 4 | Apache-2.0 platform with OTel ingest; company-governed, so not 5. |
| **Total (generic / FS)** | **3.75 / 3.75** | |

*Evidence rules applied:* Rule 8 (CP2 Q4) checked at CP2 rework (8 October 2026): SOC 2 Type 2 and ISO 27001 are listed against the Opik Enterprise plan (A1-S122), so product scope is stated; security_compliance 4 kept

**Capabilities.** Apache-2.0 platform from Comet for tracing LLM calls and agents, datasets and experiments with LLM-as-a-judge metrics (hallucination, moderation, RAG), online evaluation rules on production traces, dashboards, guardrails and an agent/prompt optimiser; PyTest integration, OTel over HTTP, MCP server [VF: A1-S067, A1-S070, A1-S072].

**Strengths**

- The whole platform, including online evaluation and the optimiser, is Apache-2.0 [VF: A1-S050, A1-S067]
- Online evaluation rules apply LLM-as-a-judge to production traces [VF: A1-S072]
- Comet Trust Center lists SOC 2 Type 2 and ISO/IEC 27001:2022 [VF: A1-S122]
- Low published cloud pricing and free self-hosting [VF: A1-S123]

**Limitations and risks**

- Self-hosted open source has no user management; SSO, custom roles and service accounts come with Enterprise [VF: A1-S069, A1-S122, A1-S123, B-REV-S022]
- Local Docker install is not production-ready; Kubernetes/Helm required [VF: A1-S069]
- OTel over HTTP only [VF: A1-S070]
- EU region and data residency not publicly verified [NPV]
- About two years old with very frequent releases [VF: A1-S006]

**Choose when**

- You want a fully Apache-2.0 platform with online evaluation and are willing to buy Comet Enterprise for user management [AJ]
- You already run Comet for ML experiment tracking [AJ]

**Avoid when**

- You plan to self-host the open-source edition for multiple teams without an identity layer [AJ]
- You need a verified EU SaaS region [AJ]

**Nearest competitors:** L9-langfuse, L9-arize-phoenix, L9-mlflow-genai

**Regulated-FS note.** Self-host for residency, but only with Enterprise user management or a fronting identity proxy; without it the trace store has no access control or attribution [AJ].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Comet ML, Inc. (Comet) | Verified fact | A1-S050, A1-S071, A1-S006 |
| Category | Open-source LLM observability, evaluation, prompt/agent optimisation and guardrails platform | Verified fact | A1-S067 |
| Version / lineup | opik 2.2.94 (Python SDK), released 7 October 2026 | Verified fact | A1-S006 |
| Licence | Apache-2.0 for the full platform (backend, UI, evaluation, online evaluation, optimiser) | Verified fact | A1-S050, A1-S067 |
| Strategic direction | Agent Optimizer SDK, Opik Guardrails, online evaluation rules, MCP server; positioned as free-to-self-host alternative to platforms gating self-hosting behind Enterprise plans | Verified fact | A1-S067, A1-S072 |
| What it does | Traces LLM calls and agent activity, runs datasets/experiments with LLM-as-a-judge metrics (hallucination, moderation, RAG), scores production traces with online evaluation rules, and provides dashboards, guardrails and prompt optimisation. | Verified fact | A1-S067, A1-S072 |
| Stack position | Cross-cutting observability and evaluation; can run standalone or inside the Comet MLOps platform | Verified fact | A1-S071 |
| Integration | Python and TypeScript SDKs, REST API, OpenTelemetry (HTTP transport only), PyTest integration for CI, MCP server | Verified fact | A1-S067, A1-S070 |
| Dependencies | Self-host via local Docker install (not production-ready) or Kubernetes/Helm; ClickHouse cold-tier and backup guides exist | Verified fact | A1-S069, A1-S067 |
| Certifications | Comet Trust Center: SOC 2 Type 2, ISO/IEC 27001:2022, ISO 9001:2015; HIPAA and GDPR listed as Enterprise-plan features (not certifications) | Verified fact | A1-S122 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Self-hosted open source has no user management; Enterprise adds SSO and service accounts | Verified fact | A1-S069, A1-S122, A1-S123 |
| Enterprise support | Enterprise plan: dedicated support and SLAs, flexible deployments | Verified fact | A1-S122, A1-S123 |
| Pricing | Self-hosted free; Free cloud (25k spans/month, 10 members, 60-day retention); Pro Cloud US$19/month (100k spans, 50 members); Enterprise custom | Verified fact | A1-S123, A1-S067 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Integrations incl. Google ADK, Autogen, Flowise AI, Cloudflare Workers AI and OpenTelemetry | Verified fact | A1-S067 |
| Adoption signals | 20,000+ GitHub stars (vendor README); claims scale of 40M+ traces/day | Verified fact | A1-S067 |
| Maturity | First PyPI release 2 September 2024; 635 releases to 7 October 2026 | Verified fact | A1-S006 |
| Deployment | saas: Yes (Comet-hosted); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes; on_prem: Yes (as part of self-hosted Comet platform) | | |

## Arize AX (`L9-arize-ax`)

**Tier:** Tactical · **Flags:** Acquired, Duplicated · **Original graphic label:** Arize – RAG metrics

*Rationale:* Technically strong and FS-deployable, but acquired seven days ago with a convergence roadmap; re-assess for Strategic once Dynatrace publishes product plans [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Online and offline evals, monitoring, alerting and failure-pattern grouping at volume; red-teaming not native. |
| Enterprise readiness | 4 | SAML SSO, RBAC, audit trails, multi-tenancy, SLAs; SCIM not documented in the fact base. |
| Security and compliance | 4 | SOC 2 Type II, PCI DSS 4.0, HIPAA, EU region and self-host; ISO 27001 unconfirmed on the official compliance page, so 4. |
| Deployment flexibility | 5 | SaaS, VPC, customer-managed cloud, self-host and air-gap. |
| Ecosystem | 4 | OpenInference catalogue shared with Phoenix; increasingly tied to Dynatrace. |
| Reliability and maturity | 3 | Commercial since 2020, but ownership changed on 1 October 2026 with platform convergence planned. |
| Cost / TCO | 3 | Transparent Free and Pro tiers, no per-seat charges; Enterprise custom. |
| Lock-in / portability | 2 | Base 3 (proprietary backend on portable instrumentation) reduced by 1 for the 2026 ownership change. |
| **Total (generic / FS)** | **3.85 / 3.70** | |

**Capabilities.** Commercial agent observability and evaluation: managed tracing, online and offline evaluation, monitoring and alerting at high volume, managed evaluation compute, multi-tenancy via organisations and spaces, and Signal, a scheduled worker that groups recurring failure patterns into issues [VF: A1-S046, A1-S047].

**Strengths**

- Same OTel/OpenInference instrumentation as Phoenix, with a documented Phoenix-to-AX migration by dual-writing [VF: A1-S046, A1-S049]
- SaaS, VPC, customer-managed cloud, self-hosted and air-gapped deployment [VF: A1-S046, A1-S047]
- SAML SSO with RBAC mapping, audit trails, dedicated support and SLAs on Enterprise [VF: A1-S046, A1-S124]
- SOC 2 Type II, PCI DSS 4.0 Level 1, HIPAA (Enterprise) and an EU data region in Belgium [VF: A1-S124, A1-S047]

**Limitations and risks**

- Dynatrace completed the acquisition on 1 October 2026 and plans to converge the product into its platform [VF: A1-S045, V1-S005]
- Runs on the proprietary adb OLAP database [VF: A1-S046]
- ISO 27001 appears on marketing pages but not on the official AX compliance page; request the certificate [VF: A1-S124, V1-S084]
- Enterprise pricing is custom [VF: A1-S047]

**Choose when**

- You run Dynatrace already, or you need managed high-volume online evaluation with air-gapped or self-hosted options [AJ]
- Phoenix is in use for development and you want a supported production tier on the same instrumentation [AJ]

**Avoid when**

- You need roadmap certainty in the next two to three quarters while Dynatrace integration plans settle [AJ]
- ISO 27001 is a hard procurement gate and the certificate cannot be produced [AJ]

**Nearest competitors:** L9-langsmith, L9-datadog-agent-observability, L9-braintrust

**Regulated-FS note.** Self-hosted AX (Arize stores nothing) answers trace residency; re-run third-party due diligence and the DORA register entry after the ownership change, and obtain the ISO certificate before relying on it [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Arize AI, a Dynatrace company (acquisition completed 1 October 2026) | Verified fact | A1-S044, A1-S045, V1-S005 |
| Category | Commercial AI agent observability and evaluation platform (SaaS or licensed private deployment) | Verified fact | A1-S046, A1-S047 |
| Version / lineup | SaaS; Python SDK arize 8.58.0, released 7 October 2026; tiers AX Free, AX Pro, AX Enterprise | Verified fact | A1-S007, A1-S047 |
| Licence | Proprietary; self-hosting requires a commercial licence; Python SDK Apache-2.0 | Verified fact | A1-S046, A1-S007 |
| Status events | Dynatrace definitive agreement to acquire Arize, 13 August 2026 (US$915M, approx. US$815M cash); Acquisition completed 1 October 2026 | Verified fact | A1-S044, A1-S045, V1-S005 |
| Strategic direction | Signal (scheduled worker grouping recurring failure patterns into issues), Alyx assistant, ADB data fabric; post-acquisition integration into Dynatrace planned | Verified fact | A1-S046, A1-S047, A1-S045 |
| What it does | Managed tracing, online and offline evaluation, monitoring and alerting for LLM and agent applications at high volume, with managed evaluation compute and multi-tenancy via organisations and spaces. | Verified fact | A1-S046 |
| Stack position | Cross-cutting production observability and evaluation; graphic's 'RAG metrics' descriptor understates scope | Verified fact | A1-S046, A1-S047 |
| Integration | OpenTelemetry and OpenInference instrumentation shared with Phoenix; documented Phoenix-to-AX migration via dual-writing | Verified fact | A1-S046, A1-S049 |
| Dependencies | Runs on Arize's proprietary adb OLAP database | Verified fact | A1-S046 |
| Certifications | SOC 2 Type II; PCI DSS 4.0 Level 1 Service Provider; CSA STAR Level 1 self-assessment; HIPAA (Enterprise tier only per pricing table; docs say compliant, self-hosted page says HIPAA-ready); ISO/IEC 27001 (A-LIGN, announced c. August 2026) is stated on marketing pages but is NOT listed on the official AX compliance docs page - confirm the certificate before relying on it | Verified fact | A1-S124, A1-S047, V1-S084 |
| GDPR / residency | EU data region in Belgium; self-hosted (customer Kubernetes and object storage, Arize stores nothing) and air-gapped options; GDPR compliance claimed | Verified fact | A1-S124 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | SSO, RBAC and audit trails; self-hosted AX supports any SAML 2.0 IdP (Okta, Entra, OneLogin, Ping) with RBAC role mapping; 'Enterprise SSO' on Enterprise tier; multi-tenancy via organisations and spaces | Verified fact | A1-S046, A1-S124 |
| Enterprise support | Dedicated support and SLAs (Enterprise) | Verified fact | A1-S046, A1-S047 |
| Pricing | AX Free US$0 (25k spans, 1 GB, 15-day retention); AX Pro US$50/month (50k spans, 10 GB, 30 days, overages); AX Enterprise custom; no per-seat charges, unlimited users and evaluations | Verified fact | A1-S047 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Same integration catalogue as Phoenix via OpenInference | Verified fact | A1-S046, A1-S066 |
| Adoption signals | Acquisition value US$915M (Dynatrace) | Verified fact | A1-S044 |
| Maturity | arize SDK first published on PyPI 25 March 2020; 369 releases | Verified fact | A1-S007 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (VPC deployment, Enterprise); private_cloud: Yes (customer-managed cloud, commercial licence); self_hosted: Yes (commercial licence); on_prem: Yes (on-prem / air-gapped, Enterprise) | | |

## DeepEval (`L9-deepeval`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** DeepEval – LLM unit tests

*Rationale:* The most complete open metric library for the layer's questions, but it is a substitutable component of an in-house eval harness, not a platform [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Broadest metric coverage (RAG, agentic, trajectory, G-Eval, DAG); no tracing store of its own. |
| Enterprise readiness | 3 | Self-hosted library (rule 2): enables CI evaluation in-estate; commercial platform exists but its access controls are not verified. |
| Security and compliance | 3 | Inherits host controls; clear Apache-2.0 licence; Confident AI SOC 2/HIPAA are vendor statements with gating conflicts. |
| Deployment flexibility | 5 | Library runs anywhere, including air-gapped with local judges; Confident AI SaaS, VPC and self-host options. |
| Ecosystem | 4 | Many framework integrations; OTel export mainly to Confident AI. |
| Reliability and maturity | 3 | 527 releases since August 2023; fast-changing metric set; funding NPV. |
| Cost / TCO | 4 | Free; judge-token spend dominates. |
| Lock-in / portability | 4 | Apache-2.0 library; company-governed, with commercial steering. |
| **Total (generic / FS)** | **3.75 / 3.70** | |

*Evidence rules applied:* Rule 2 (self-hosted software) applied: NPV cap not applied; enterprise_readiness and security_compliance scored on what the software enables and on project hygiene, capped at 4; inherits host controls

**Capabilities.** Apache-2.0 Python evaluation framework, 'similar to Pytest but specialised for unit testing LLM apps': LLM-as-a-judge, statistical and NLP metrics, including G-Eval, DAG, RAG faithfulness and contextual recall/precision, and agentic metrics (task completion, tool correctness, plan adherence) with trajectory evaluation; runs in any CI/CD [VF: A1-S068].

**Strengths**

- Covers the layer's research questions directly: faithfulness, contextual recall/precision, tool correctness and trajectory [VF: A1-S068]
- Runs locally with any LLM as judge or with local NLP models, so evaluation can stay inside the estate [VF: A1-S068]
- Broad framework integrations (LangGraph, Pydantic AI, CrewAI, OpenAI Agents, Google ADK, LlamaIndex and others) [VF: A1-S068]
- Apache-2.0 [VF: A1-S051]

**Limitations and risks**

- Commercial features steer to the Confident AI platform [VF: A1-S068]
- OTel export is primarily to Confident AI's OTLP/HTTP endpoint; export to arbitrary collectors not confirmed [VF: A1-S121]
- Confident AI certifications are vendor statements with inconsistent plan gating [VF: A1-S119]
- LLM-judge token spend is the main cost driver [AJ]
- Maintainer funding not publicly verified [NPV]

**Choose when**

- You want a code-first metric library inside pytest and CI, owned and versioned by the engineering team [AJ]
- You need agent trajectory and tool-correctness metrics without adopting a platform [AJ]

**Avoid when**

- You expect a production observability system; DeepEval is a test framework [AJ]
- You would rely on its LLM-judge metrics as the sole evidence for validation without calibrating them against human labels [AJ]

**Nearest competitors:** L9-promptfoo, L9-mlflow-genai, L9-opik

**Regulated-FS note.** Run it inside the firm's CI with an approved judge model behind the gateway; pin the library and judge versions in the evidence pack so results are reproducible [AJ].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Confident AI (maintainer; also sells the Confident AI evals and observability platform) | Verified fact | A1-S068, A1-S051 |
| Category | Open-source LLM evaluation framework ('similar to Pytest but specialised for unit testing LLM apps') | Verified fact | A1-S068 |
| Version / lineup | deepeval 4.2.8, released 2 October 2026 | Verified fact | A1-S005 |
| Licence | Apache-2.0 (framework); Confident AI platform is commercial | Verified fact | A1-S051, A1-S005, A1-S068 |
| Strategic direction | Agentic metrics (task completion, tool correctness, plan adherence), trajectory evaluation, JevEval metric; Confident AI positioned for organisation-wide quality standards, native red teaming and an MCP server | Verified fact | A1-S068 |
| What it does | Provides ready-made LLM-as-a-judge, statistical and NLP metrics (G-Eval, DAG, RAG metrics such as faithfulness and contextual recall/precision, agentic metrics) that run as test cases, including in CI/CD. | Verified fact | A1-S068 |
| Stack position | Developer-side evaluation library feeding CI; production observability comes from Confident AI or another platform. Graphic label 'LLM unit tests' is accurate. | Verified fact | A1-S068 |
| Integration | Python and TypeScript integrations (LangChain/LangGraph callbacks, Pydantic AI, CrewAI, OpenAI Agents, AWS AgentCore, Google ADK, AI SDK, Mastra, LlamaIndex, Strands); runs in any CI/CD; OpenTelemetry: ConfidentSpanExporter and framework OTel span processors export to Confident AI's OTLP/HTTP endpoint (no gRPC), regional endpoint via CONFIDENT_OTEL_URL, run_otel exports evaluation-run spans to an OTLP endpoint | Verified fact | A1-S068, A1-S121 |
| Dependencies | Python library; metrics use any LLM as judge or local NLP models | Verified fact | A1-S068 |
| Certifications | Confident AI states SOC 2 and HIPAA compliance (HIPAA BAA); plan gating conflicts between pages (Team-and-above vs Enterprise/Premium add-on); self-hosted compliance depends on customer environment | Verified fact | A1-S119 |
| GDPR / residency | Confident AI regions: US (default, North Carolina), EU (Frankfurt) and AU; GDPR handling applies to EU-region data; EU hosting may need a higher plan or add-on (pages conflict) | Verified fact | A1-S119 |
| Security features | Encryption at rest and TLS in transit (Confident AI); self-hosted keeps keys and data in customer cloud account | Verified fact | A1-S119 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | DeepEval framework free (Apache-2.0); Confident AI: Free (2 seats, 1 project, 1 GB-month spans), Starter US$200/month (unlimited seats, 5 projects, 5 GB-months, then US$1 per GB-month), Team US$2,000/month (75 GB-months), Enterprise custom | Verified fact | A1-S051, A1-S120 |
| Infrastructure cost | Main cost driver is LLM-judge token spend per evaluation run | Architectural judgement |  |
| Ecosystem | Broad framework integrations listed above | Verified fact | A1-S068 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First PyPI release 15 August 2023; 527 releases to 2 October 2026 | Verified fact | A1-S005 |
| Deployment | saas: Yes (Confident AI platform); managed_cloud: Not publicly verified; vpc_byoc: Yes (Enterprise: deploy in own VPC via Terraform module); private_cloud: Yes (AWS, Azure, GCP); self_hosted: Yes (library runs locally; platform self-host on Enterprise); on_prem: Yes (on-prem on Enterprise, per vendor homepage) | | |

## Promptfoo (`L9-promptfoo`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** Promptfoo – red-teaming

*Rationale:* Valuable eval and red-team harness under MIT, but now owned by a model vendor with an unpublished closing date; use as one of two red-team tools, not the sole independent check [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Regression evals, red-teaming, model comparison and PR code scanning; not a production trace store. |
| Enterprise readiness | 3 | Enterprise RBAC, team management, SLA and professional services; SSO and audit logs not documented. |
| Security and compliance | 3 | Scored as a locally run MIT CLI (rule 2): inherits host controls, local-only execution. Enterprise SaaS certifications are NPV and would cap that edition at 2. |
| Deployment flexibility | 5 | Local CLI, Enterprise SaaS, and On-Prem on AWS, Azure or GCP with a dedicated runner. |
| Ecosystem | 4 | CI integrations, OTLP receiver, many providers, OWASP/NIST reports. |
| Reliability and maturity | 3 | Frequent releases since 2023 but pre-1.0; acquisition announced 9 March 2026, closing not published. |
| Cost / TCO | 4 | Free MIT CLI; attack-generation and grader model spend. |
| Lock-in / portability | 3 | Base 4 (MIT, portable configs) reduced by 1 for the announced acquisition; governance is vendor-controlled. |
| **Total (generic / FS)** | **3.70 / 3.55** | |

*Evidence rules applied:* Rule 2 (self-hosted software) applied: NPV cap not applied; enterprise_readiness and security_compliance scored on what the software enables and on project hygiene, capped at 4; inherits host controls

**Capabilities.** MIT CLI and library for automated evaluation of prompts, models and agents, red-teaming and vulnerability scanning, side-by-side model comparison, CI/CD checks and pull-request code scanning for LLM security issues; Promptfoo Enterprise as SaaS or On-Prem [VF: A1-S062, A1-S063].

**Strengths**

- Combines regression evals and red-teaming in one declarative config that runs in GitHub Actions, GitLab CI and Jenkins [VF: A1-S062, A1-S065]
- Evals run locally ('your prompts never leave your machine'); On-Prem edition with a dedicated runner and network isolation [VF: A1-S062, A1-S063]
- Built-in OTLP receiver using OTel GenAI conventions [VF: A1-S064]
- OWASP and NIST compliance reports; providers include OpenAI, Anthropic, Azure, Bedrock and Ollama [VF: A1-S062, A1-S063, A1-S065]

**Limitations and risks**

- OpenAI announced the acquisition on 9 March 2026; the closing date has not been published, and the README says Promptfoo is part of OpenAI [VF: A1-S024, A1-S062, V1-S006, V2-S042]
- OpenAI plans to integrate it into OpenAI Frontier, so the roadmap follows a model vendor's priorities [VF: A1-S024]
- Pre-1.0 version numbering (0.124.0) [VF: A1-S020]
- Enterprise edition certifications not publicly verified [NPV]

**Choose when**

- You need red-team and regression suites as code in CI, run locally against any provider [AJ]
- You want OWASP-mapped test evidence for C7 security testing [AJ]

**Avoid when**

- A model vendor owning your independent red-team tool is unacceptable to your model-risk function without a second, independent tool [AJ]
- You would buy Enterprise SaaS before certifications are evidenced [AJ]

**Nearest competitors:** L9-deepeval, L9-braintrust, L9-langsmith

**Regulated-FS note.** Keep using the MIT CLI locally, pin the version, and keep test configs in the firm's repo so they are portable; pair it with an independent tool when the system under test uses OpenAI models, to preserve effective challenge [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Promptfoo, now part of OpenAI (acquisition agreement announced 9 March 2026; README states 'Promptfoo is now part of OpenAI') | Verified fact | A1-S024, A1-S025, A1-S062 |
| Category | Open-source CLI and library for LLM evals and red teaming, plus Promptfoo Enterprise (SaaS and On-Prem) | Verified fact | A1-S062, A1-S063 |
| Version / lineup | promptfoo 0.124.0 (npm), published 6 October 2026 | Verified fact | A1-S020 |
| Licence | MIT (open source); Enterprise editions commercial | Verified fact | A1-S052, A1-S020, A1-S062, A1-S063 |
| Status events | Acquisition by OpenAI announced 9 March 2026 (terms undisclosed; subject to closing conditions); the README now says "part of OpenAI", but no dated closing notice was found as of 8 October 2026 | Verified fact | A1-S024, A1-S025, A1-S062, V1-S006 |
| Strategic direction | OpenAI plans to integrate Promptfoo into OpenAI Frontier for automated red-teaming, security review of agentic workflows and risk/compliance monitoring, while continuing the open-source project | Verified fact | A1-S024, A1-S025 |
| What it does | Runs automated evaluations of prompts, models and agents, red-teaming and vulnerability scanning, side-by-side model comparison, CI/CD checks and code scanning of pull requests for LLM security issues. | Verified fact | A1-S062 |
| Stack position | Spans pre-production evaluation and AI security testing (C7); the graphic's 'red-teaming' descriptor omits its general eval role | Verified fact | A1-S062, A1-S063 |
| Integration | CLI/library; CI/CD (GitHub Actions, GitLab CI, Jenkins); built-in OTLP receiver ingesting spans with OTel GenAI semantic conventions; API (Enterprise) | Verified fact | A1-S064, A1-S065, A1-S063 |
| Dependencies | Node.js CLI (also brew and pip); evals run locally ('your prompts never leave your machine'); Enterprise On-Prem includes a dedicated runner | Verified fact | A1-S062, A1-S063 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Community edition runs locally; Enterprise On-Prem keeps scans inside the network perimeter | Verified fact | A1-S062, A1-S063 |
| Security features | Network isolation and dedicated runner in On-Prem edition | Verified fact | A1-S063 |
| Access controls | RBAC and team management in Enterprise editions only | Verified fact | A1-S063 |
| Enterprise support | Enterprise: SLA, professional services, dedicated Slack | Verified fact | A1-S063 |
| Pricing | Community free (MIT); Enterprise contact sales | Verified fact | A1-S063 |
| Infrastructure cost | Cost driver is model/API spend for generated attacks and graders | Architectural judgement |  |
| Ecosystem | Providers incl. OpenAI, Anthropic, Azure, Bedrock, Ollama; SIEM and issue-tracker integrations in Enterprise; OWASP/NIST compliance reports | Verified fact | A1-S062, A1-S063, A1-S065 |
| Adoption signals | Over 25% of Fortune 500 use Promptfoo (company claim); ~US$23M raised, US$86M valuation after July 2025 round (PitchBook) | Reported | A1-S026 |
| Maturity | npm package created 3 May 2023; frequent releases | Verified fact | A1-S020 |
| Deployment | saas: Yes (Promptfoo Enterprise SaaS); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes (On-Prem on AWS, Azure, GCP); self_hosted: Yes; on_prem: Yes (Enterprise On-Prem) | | |

## Arize Phoenix (`L9-arize-phoenix`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** Phoenix – Atrace

*Rationale:* Useful, portable workbench with strong instrumentation; ELv2, no audit trail, community-only support and new Dynatrace ownership make it unsuitable as the production record [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Tracing, retrieval and response evals, datasets, experiments, prompt management and pytest; online production monitoring is the AX proposition. |
| Enterprise readiness | 3 | Scored as self-hosted software (rule 2). With authentication enabled, Phoenix provides admin, member and viewer roles and login through OAuth2 identity providers (A1-S105): two of SSO, RBAC and audit logs verified, so 3 under rule 7 (CP2 Q2). No audit trail, SCIM or commercial support for Phoenix itself, so not above 3. |
| Security and compliance | 3 | Inherits host controls; licence is clear, telemetry can be disabled; auth off by default is a hygiene weakness. Certifications NPV for Phoenix Cloud, not used. |
| Deployment flexibility | 4 | Self-host, private-cloud templates and air-gap; Phoenix Cloud low confidence; no BYOC. |
| Ecosystem | 4 | OpenInference is accepted by other backends; broad framework and provider auto-instrumentation. |
| Reliability and maturity | 4 | 700 releases since January 2023; Dynatrace completed acquisition 1 October 2026 with a support commitment. |
| Cost / TCO | 4 | Free with no caps; one instance per team and PostgreSQL to operate. |
| Lock-in / portability | 3 | Base 4 (portable OTel/OpenInference, source-available) reduced by 1 for the 2026 ownership change; ELv2 is not permissive. |
| **Total (generic / FS)** | **3.65 / 3.50** | |

*Evidence rules applied:* Rule 2 (self-hosted software) applied: NPV cap not applied; enterprise_readiness and security_compliance scored on what the software enables and on project hygiene, capped at 4; inherits host controls; Rule 7 (CP2 Q2) applied at CP2 rework (8 October 2026) for consistency with Opik and Unstructured: roles and OAuth2 IdP login verified (A1-S105); enterprise_readiness 2 -> 3; no audit trail

**Capabilities.** Self-hosted tracing and evaluation built on OpenTelemetry and OpenInference: LLM-based response and retrieval evaluations, versioned datasets, experiments, prompt playground and management, REST API, MCP endpoint and a pytest plugin for eval-in-CI [VF: A1-S066, A1-S049, A1-S106].

**Strengths**

- OpenInference instrumentation (Apache-2.0) routes the same spans to Phoenix, Arize AX or other backends, including Datadog [VF: A1-S049, A1-S066, A1-S098]
- No feature gates and no usage caps when self-hosted [VF: A1-S046, A1-S047]
- Data stays in the customer environment; default web-analytics telemetry carries no trace data and can be disabled [VF: A1-S066]
- Air-gapped deployment supported; cloud templates for AWS, Azure and Google Cloud Run [VF: A1-S046, A1-S066]

**Limitations and risks**

- Elastic License 2.0: source-available, not OSI open source; cannot be offered to third parties as a managed service [VF: A1-S048, A1-S107]
- Authentication is optional and off by default [VF: A1-S105]
- Single-tenant per instance; full SSO, RBAC and audit trails are provided through AX, not Phoenix [VF: A1-S046]
- Community support only [VF: A1-S046]
- Owned by Dynatrace since 1 October 2026; capabilities to be integrated into Dynatrace over time [VF: A1-S045, V1-S005]

**Choose when**

- You want a free, self-hosted tracing and eval workbench for development and validation teams, with OpenInference as the portable instrumentation [AJ]
- Validators need an isolated, air-gapped instance per model review [AJ]

**Avoid when**

- You need a multi-team production system of record with SSO, audit trails and support [AJ]
- Your open-source policy admits only OSI-approved licences [AJ]

**Nearest competitors:** L9-langfuse, L9-opik, L9-mlflow-genai

**Regulated-FS note.** Good for independent validation sandboxes; switch authentication on, disable telemetry, and do not treat it as the audit store, because it has no audit trail [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Arize AI, a Dynatrace company (Dynatrace completed the acquisition on 1 October 2026) | Verified fact | A1-S044, A1-S045, V1-S005 |
| Category | Source-available (ELv2), self-hosted AI observability and evaluation platform | Verified fact | A1-S048, A1-S066, A1-S107 |
| Version / lineup | arize-phoenix 20.19.0, released 1 October 2026 | Verified fact | A1-S004 |
| Licence | Elastic License 2.0: free self-hosting, modification and redistribution, but may not be provided to third parties as a hosted or managed service; not OSI-approved although marketed as 'open source'; no feature gates | Verified fact | A1-S048, A1-S046, A1-S107, V1-S013 |
| Status events | Dynatrace signed a definitive agreement to acquire Arize, 13 August 2026 (US$915M cash and stock); Acquisition completed 1 October 2026 (Dynatrace investor-relations release, 4:05 p.m. EDT) | Verified fact | A1-S044, A1-S045, V1-S005 |
| Strategic direction | Arize will continue to support Phoenix after the Dynatrace acquisition and integrate capabilities into Dynatrace over time; recent additions include PXI (built-in AI engineering agent) and a remote MCP server | Verified fact | A1-S045, A1-S066 |
| What it does | Traces LLM applications with OpenTelemetry-based instrumentation and runs LLM-based response and retrieval evaluations, versioned datasets, experiments, a prompt playground and prompt management. | Verified fact | A1-S066 |
| Stack position | Cross-cutting tracing and evaluation for development and self-hosted production; it is the open product, while Arize AX is the commercial platform (graphic shows both as separate tiles) | Verified fact | A1-S046, A1-S066 |
| Integration | OpenTelemetry with OpenInference instrumentation (Apache-2.0); same instrumentation routes to Phoenix or AX; REST API; built-in MCP endpoint; pytest plugin for eval-in-CI | Verified fact | A1-S049, A1-S066, A1-S106 |
| Dependencies | SQLite by default; PostgreSQL 14+ recommended for production; single-tenant per instance | Verified fact | A1-S046 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Self-hosted: data remains in the customer environment; default web-analytics telemetry collects no trace or evaluation data and can be disabled (PHOENIX_TELEMETRY_ENABLED=false) | Verified fact | A1-S066 |
| Security features | Authentication optional and off by default; when enabled supports secure cookies and Phoenix acts as an OAuth2 authorisation server for MCP and other clients | Verified fact | A1-S046, A1-S105 |
| Access controls | Roles admin, member and viewer when auth enabled; login via OAuth2 identity providers; Arize states full SSO/RBAC/audit trails are provided through AX | Verified fact | A1-S105, A1-S046 |
| Enterprise support | Community support only; dedicated support and SLAs via Arize AX | Verified fact | A1-S046 |
| Pricing | Free to self-host, no usage caps | Verified fact | A1-S047, A1-S107 |
| Infrastructure cost | Cost is the customer's compute and PostgreSQL; multi-team use requires multiple instances | Architectural judgement |  |
| Ecosystem | Out-of-the-box tracing for OpenAI Agents SDK, Claude Agent SDK, LangGraph, Vercel AI SDK, Mastra, CrewAI, LlamaIndex, DSPy and providers incl. OpenAI, Anthropic, Google GenAI, Bedrock, OpenRouter, LiteLLM | Verified fact | A1-S066 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First PyPI release 18 January 2023; 700 releases to 1 October 2026 | Verified fact | A1-S004 |
| Deployment | saas: Yes (Phoenix Cloud referenced); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes (AWS CloudFormation, Azure, Google Cloud Run templates); self_hosted: Yes; on_prem: Yes (air-gapped supported) | | |

## W&B Weave (Weights & Biases) (`L9-wandb-weave`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* Good security posture and deployment options, but evaluation depth is less evidenced and the product follows a compute vendor's platform strategy [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Agent tracing and evaluation with SDK autopatching; RAG metrics, online rules and red-teaming not evidenced. |
| Enterprise readiness | 4 | SSO, automated provisioning, custom roles, audit logs and an enterprise support package. |
| Security and compliance | 4 | The Weave documentation states SOC 2 Type II for both managed platforms, HIPAA on Dedicated Cloud and customer-managed keys on Enterprise (A1-S137, A1-S138); ISO/IEC 27001/27017/27018 are listed at W&B site level with Weave scope not stated, so 4 under rule 8 (CP2 Q4): 5 needs SOC 2 Type II and ISO 27001 within the product's scope. |
| Deployment flexibility | 4 | Multi-tenant SaaS, Dedicated Cloud, Self-Managed and on-prem; air-gap not documented. |
| Ecosystem | 3 | OTLP ingest and agent SDK autopatching; strongest inside the W&B estate. |
| Reliability and maturity | 3 | Three years of releases, pre-1.0 SDK; owned by CoreWeave since May 2025. |
| Cost / TCO | 3 | Pro from US$60/month plus usage-based ingestion; Enterprise by quote. |
| Lock-in / portability | 2 | Base 3 (proprietary platform, OTel ingest, Apache-2.0 SDK) reduced by 1 for the 2025 ownership change. |
| **Total (generic / FS)** | **3.40 / 3.35** | |

*Evidence rules applied:* Rule 8 (CP2 Q4) applied at CP2 rework (8 October 2026): ISO certifications are W&B site-level with Weave scope not stated; security_compliance 5 -> 4

**Capabilities.** Tracing and evaluation toolkit for agents and LLM applications from Weights & Biases: traces conversations, turns, LLM and tool calls; evaluates agents; autopatches agent SDKs including OpenAI Agents SDK, Claude Agent SDK and Google ADK; OTLP/HTTP endpoint plus a dedicated agents endpoint [VF: A1-S104, A1-S139].

**Strengths**

- SOC 2 Type II, ISO/IEC 27001, 27017 and 27018; HIPAA on Dedicated Cloud with BAA [VF: A1-S137]
- Dedicated Cloud in a customer-chosen cloud and region, with isolated resources, per-instance keys and private connectivity; customer-managed keys on Enterprise [VF: A1-S137, A1-S138]
- Enterprise SSO, automated user provisioning, custom roles and audit logs [VF: A1-S138]
- Self-managed and on-premises options with ingest sampling for cost control [VF: A1-S137]

**Limitations and risks**

- Part of CoreWeave since 5 May 2025 and now inside CoreWeave Forge [VF: A1-S131, A1-S138]
- Multi-tenant cloud is North America only [VF: A1-S137]
- Pre-1.0 SDK versioning [VF: A1-S018]
- Hosted platform is proprietary [VF: A1-S138]
- Evaluation depth for RAG and red-teaming not evidenced in the fact base [NPV]

**Choose when**

- W&B is already the firm's ML experiment platform and you want agent traces and evals in the same governed estate [AJ]
- You need a dedicated single-tenant cloud in a chosen region with customer-managed keys [AJ]

**Avoid when**

- You would use the multi-tenant cloud for EU or UK client data [AJ]
- You do not otherwise use W&B; the platform cost is hard to justify for L9 alone [AJ]

**Nearest competitors:** L9-mlflow-genai, L9-langsmith, L9-arize-ax

**Regulated-FS note.** Use Dedicated Cloud in an EU/UK region or Self-Managed; include CoreWeave in the concentration analysis if it also supplies GPU capacity [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Weights & Biases, part of CoreWeave, Inc. (acquisition completed 5 May 2025); now a named product within CoreWeave Forge | Verified fact | A1-S131, A1-S138 |
| Category | Tracing and evaluation toolkit for AI agents and LLM applications | Verified fact | A1-S104 |
| Version / lineup | weave 0.53.11 (Python), released 25 September 2026 | Verified fact | A1-S018 |
| Licence | SDK Apache-2.0; hosted W&B platform proprietary (Pro/Enterprise) | Verified fact | A1-S018, A1-S138 |
| Status events | Weights & Biases acquired by CoreWeave (announced 4 March 2025, completed 5 May 2025) | Verified fact | A1-S131, V1-S011 |
| Strategic direction | Agent-focused tracing (Agents view, dedicated OTLP endpoint for agent spans) inside CoreWeave Forge | Verified fact | A1-S104, A1-S139, A1-S138 |
| What it does | Traces agent conversations, turns, LLM and tool calls, and evaluates agents and LLM applications; autopatches agent SDKs such as OpenAI Agents SDK, Claude Agent SDK and Google ADK. | Verified fact | A1-S104 |
| Stack position | Cross-cutting L9 tracing/evaluation within the broader W&B ML platform | Verified fact | A1-S104, A1-S137 |
| Integration | Python/TypeScript SDK; OTLP/HTTP protobuf endpoint (trace.wandb.ai/otel/v1/traces) and agents endpoint; OTel Collector forwarding | Verified fact | A1-S104, A1-S139 |
| Dependencies | Self-managed W&B Server: Kubernetes, MySQL 8.4.x, S3-compatible object storage, Redis; Dedicated Cloud stores Weave data in a dedicated ClickHouse Cloud cluster | Verified fact | A1-S137 |
| Certifications | SOC 2 Type II (multi-tenant and Dedicated Cloud); ISO/IEC 27001:2022, 27017:2015, 27018:2019; HIPAA on Dedicated Cloud with BAA (Weave HIPAA status on other deployments conflicting) | Verified fact | A1-S137 |
| GDPR / residency | Multi-tenant cloud in North America; Dedicated Cloud in customer-chosen cloud and region | Verified fact | A1-S137 |
| Security features | Dedicated Cloud: isolated network/compute/storage, per-instance encryption key, IP allowlisting, private connectivity; Enterprise: customer-managed encryption keys | Verified fact | A1-S137, A1-S138 |
| Access controls | Enterprise: SSO, automated user provisioning, custom roles, audit logs | Verified fact | A1-S138 |
| Enterprise support | Enterprise support package; Enterprise invoiced annually upfront | Verified fact | A1-S138 |
| Pricing | Pro from US$60/month; Enterprise by quote; Weave data ingestion billed monthly in arrears by usage; extra storage US$0.03/GB | Verified fact | A1-S138 |
| Infrastructure cost | Self-managed instances can use ingest sampling to control cost at high trace volume | Verified fact | A1-S137 |
| Ecosystem | Integrations incl. OpenAI Agents SDK, Claude Agent SDK, Google ADK, Agno, Vercel AI SDK | Verified fact | A1-S104, A1-S139 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | weave first on PyPI 7 June 2023; 147 releases | Verified fact | A1-S018 |
| Deployment | saas: Yes (multi-tenant on Google Cloud, North America); managed_cloud: Yes (Dedicated Cloud on AWS, Google Cloud, Azure); vpc_byoc: Not publicly verified; private_cloud: Yes (Self-Managed); self_hosted: Yes; on_prem: Yes (on-premises Self-Managed) | | |

## Braintrust (`L9-braintrust`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Braintrust – evals platform

*Rationale:* Strong evaluation workflow and a sensible hybrid model, but proprietary eval assets and no ISO 27001 keep it out of the foundational tier for FS [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Leading offline-eval ergonomics plus production logging, clustering and gateway; red-teaming not native. |
| Enterprise readiness | 3 | SSO/SAML (Okta, Entra ID, Google Workspace) and OIDC; built-in groups plus Enterprise custom, project and object-level permissions; Enterprise audit logs queryable by SQL (B-REV-S020, B-REV-S021); SCIM and SLA not documented. |
| Security and compliance | 3 | SOC 2 Type II, encryption, CMK in hybrid and EU data plane; no ISO 27001 found and HIPAA wording inconsistent. |
| Deployment flexibility | 4 | SaaS, hybrid data plane in customer cloud, self-host on Enterprise; air-gap low confidence. |
| Ecosystem | 4 | OTLP ingest, MCP endpoint, GitHub Action, several agent framework integrations. |
| Reliability and maturity | 3 | GA since 2023 with frequent releases; venture-funded and repositioning towards observability. |
| Cost / TCO | 3 | Published Pro price (US$249/month plus usage); Enterprise custom. |
| Lock-in / portability | 2 | Proprietary platform holding eval logic and datasets; OTel ingest only partially mitigates. |
| **Total (generic / FS)** | **3.40 / 3.20** | |

**Capabilities.** Proprietary evaluation and observability platform: experiments, datasets and scorers; production trace logging; Topics trace clustering; Loop AI-assisted prompt/model optimisation; a gateway that routes and traces model calls; GitHub Action posting eval results on pull requests [VF: A1-S043, A1-S040, A1-S109].

**Strengths**

- Strong offline evaluation workflow with PR-level CI feedback [VF: A1-S109]
- Hybrid deployment: Braintrust-hosted control plane with the data plane in the customer's AWS, GCP or Azure; customer-managed KMS keys and private networking [VF: A1-S041]
- US or EU data plane chosen at organisation creation; EU processing in the DPA [VF: A1-S042]
- OTLP trace endpoints in US and EU [VF: A1-S042]

**Limitations and risks**

- No ISO 27001 certification found; SOC 2 Type II reports under mutual NDA [VF: A1-S041, A1-S125]
- Evaluation logic and datasets live in the proprietary platform [VF: A1-S042]
- Region cannot be changed after organisation creation [VF: A1-S042]
- Hybrid control plane still holds metadata and hashed keys, and uses Clerk for auth [VF: A1-S041]
- Valuation figures are press-reported only and are not a decision input [R: A1-S027]

**Choose when**

- Evaluation-driven development is the main need and teams want rich experiment comparison in pull requests [AJ]
- You want trace data in your own cloud account but are content with a vendor-run control plane [AJ]

**Avoid when**

- Your procurement baseline requires ISO 27001 [AJ]
- You need a fully self-contained, air-gapped deployment with no external control plane (air-gap is vendor-mentioned only, low confidence) [AJ]

**Nearest competitors:** L9-langsmith, L9-langfuse, L9-arize-ax

**Regulated-FS note.** The hybrid data plane answers the residency question for traces, but the control plane's metadata must still be assessed under SYSC 8/DORA; choose the EU data plane at creation because it cannot be changed [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Braintrust (independent, venture-backed; no acquisition found) | Verified fact | A1-S028 |
| Category | Proprietary AI evaluation and observability platform, marketed as 'the active observability platform for agents' | Verified fact | A1-S043 |
| Version / lineup | SaaS; Python SDK braintrust 0.45.0, released 7 October 2026 | Verified fact | A1-S003 |
| Licence | Proprietary platform; Python SDK MIT | Verified fact | A1-S003 |
| Strategic direction | US$80M Series B (17 February 2026) to become the observability layer for production AI; Trace conference (February 2026) introduced Topics (trace clustering), Loop (AI-assisted prompt/model optimisation) and later Patterns; Braintrust Gateway routes and traces model calls | Verified fact | A1-S028, A1-S043 |
| What it does | Runs offline evaluations (experiments, datasets, scorers) and logs production traces; clusters traces into topics and uses an AI assistant (Loop) to propose prompt or model changes; a gateway routes LLM calls while recording traces. | Verified fact | A1-S043, A1-S040 |
| Stack position | Cross-cutting evaluation and observability; graphic's 'evals platform' understates the production tracing and gateway scope | Verified fact | A1-S043 |
| Integration | SDKs; OTLP trace endpoint (api.braintrust.dev/otel, EU api-eu.braintrust.dev/otel) with Bearer auth; MCP endpoint; GitHub Action for evals on pull requests | Verified fact | A1-S042, A1-S109 |
| Dependencies | Hybrid: Braintrust-hosted control plane (UI, metadata, auth via Clerk) with data plane in customer AWS, GCP or Azure deployed by Terraform | Verified fact | A1-S041 |
| Certifications | SOC 2 Type II (reports via Trust Center under mutual NDA); HIPAA support with BAA on Enterprise plans; no ISO 27001 certification found | Verified fact | A1-S041, A1-S125 |
| GDPR / residency | US or EU data plane chosen at organisation creation and not changeable; DPA states EU storage and processing of data plane for Pro customers electing EU; control plane holds hashed keys and metadata | Verified fact | A1-S042 |
| Security features | AES-256 at rest, TLS 1.2 in transit, API keys stored as one-way hashes; customer-managed KMS keys and private networking in hybrid | Verified fact | A1-S041 |
| Access controls | Pro: more flexible permission roles; Enterprise: RBAC, deployment approvals, retention controls | Verified fact | A1-S040 |
| Enterprise support | Enterprise: custom pricing, dedicated support | Verified fact | A1-S040 |
| Pricing | Starter free (usage-based, no platform fee); Pro US$249/month incl. 5 GB processed data (+US$3/GB) and 50k scores (+US$1.50 per 1k), 30-day retention; Enterprise custom | Verified fact | A1-S040 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | OTel ingest from any framework; integrations listed for Cloudflare Agents, LiveKit Agents, Claude Code (OTel) | Verified fact | A1-S042 |
| Adoption signals | Seed US$5.1M (Greylock), Series A US$36M (Oct 2024), Series B US$80M led by ICONIQ (Feb 2026) | Verified fact | A1-S028, V1-S017 |
| Maturity | First braintrust SDK on PyPI 24 May 2023; 290 releases to 7 October 2026 | Verified fact | A1-S003 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (hybrid data plane in customer cloud); private_cloud: Yes; self_hosted: Yes (Enterprise); on_prem: Yes (air-gapping mentioned by vendor) | | |

## Datadog Agent Observability (documented under the LLM Observability URL path) (`L9-datadog-agent-observability`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** not in graphic

*Rationale:* Right answer for production monitoring in Datadog estates, with strong company-level certifications; SaaS-only and per-span metering make it a complement to, not the home of, evaluation evidence [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Strong production tracing, cost, redaction and online evals; offline experiments and CI evaluation not evidenced. |
| Enterprise readiness | 4 | SAML SSO, RBAC with default and custom roles, a Roles API for managing roles and permissions, and Audit Trail (B-L9-S003, B-L9-S005): all three controls plus an admin API, so 4 under rule 7 (CP2 Q2); SLA and support terms not captured. |
| Security and compliance | 4 | SOC 2 Type 2, ISO 27001, ISO 42001, HIPAA and FedRAMP High at company level (B-L9-S001); module-level scope not stated, so one point below the anchor under the cross-layer scope rule applied to Gemini, Cohere and Mistral. |
| Deployment flexibility | 2 | SaaS only, though across isolated regional sites including EU1 (Germany). |
| Ecosystem | 4 | OTel GenAI 1.37+ and OpenInference ingest; native APM integration. |
| Reliability and maturity | 3 | Established platform, but the module's maturity and rename date are not verified. |
| Cost / TCO | 2 | Per-span metering on top of the Datadog platform; rates not captured in the fact base. |
| Lock-in / portability | 3 | Proprietary SaaS on standard ingest interfaces; export not verified. |
| **Total (generic / FS)** | **3.15 / 3.20** | |

*Evidence rules applied:* Rule 7 (CP2 Q2) checked at CP2 rework (8 October 2026): enterprise_readiness 4 kept, re-evidenced with the Roles API (B-L9-S003); rule 8 (CP2 Q4) scope rule confirmed for security_compliance 4

**Capabilities.** Datadog module (documented as Agent Observability under the LLM Observability path) that traces each agent step and LLM call with latency, token usage, cost and errors; scans and redacts sensitive data; identifies prompt injection; runs quality, privacy and safety evaluations; and offers automated Insights [VF: A1-S097, A1-S099].

**Strengths**

- Correlates LLM traces with APM and infrastructure telemetry already in Datadog [VF: A1-S097]
- Accepts OTel traces using OTel 1.37+ GenAI conventions or OpenInference [VF: A1-S098]
- Built-in sensitive-data scanning and redaction in traces [VF: A1-S097]
- Datadog Trust Center lists SOC 2 Type 2, ISO/IEC 27001, 27017, 27018, 27701 and 42001, HIPAA and FedRAMP High; EU1 site in Germany; SAML SSO, RBAC with custom roles and an Audit Trail [VF: B-L9-S001, B-L9-S002, B-L9-S003, B-L9-S005]

**Limitations and risks**

- SaaS only; self-hosted and VPC deployment not publicly verified [NPV]
- Requires the Datadog platform [VF: A1-S097]
- Metered per LLM span; rates are on the Datadog pricing page and were not captured [VF: A1-S097]
- Whether the Trust Center listings cover this module specifically is not stated [NPV]
- Offline/CI evaluation features not documented in the fact base [NPV]

**Choose when**

- Datadog is the firm's APM standard and production LLM monitoring should sit with on-call operations [AJ]
- You want sensitive-data redaction applied at the observability tier [AJ]

**Avoid when**

- You need self-hosting or air-gap for trace data [AJ]
- It would become the only evaluation tool; pair it with a CI eval harness [AJ]

**Nearest competitors:** L9-arize-ax, L9-langsmith, L9-langfuse

**Regulated-FS note.** Pin the EU1 site at organisation creation (sites are isolated), turn on sensitive-data scanning before any client data flows, and confirm in the contract that LLM Observability is within the certified scope [AJ].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Datadog, Inc. | Verified fact | A1-S097 |
| Category | APM-vendor LLM/agent observability and evaluation module | Verified fact | A1-S097 |
| Version / lineup | SaaS module of the Datadog platform (continuous release) | Verified fact | A1-S097 |
| Licence | Proprietary SaaS | Verified fact | A1-S097 |
| Status events | Product documented as 'Agent Observability' at the llm_observability docs path (rename date not verified) | Verified fact | A1-S097 |
| Strategic direction | Agent-centric monitoring with automated Insights (root cause, impact, recommended fix), evaluations of quality, privacy and safety, sensitive-data scanning and prompt-injection detection | Verified fact | A1-S097, A1-S099 |
| What it does | Monitors, troubleshoots and evaluates LLM-powered applications: traces each agent step and LLM call with latency, token usage, cost and errors, scans and redacts sensitive data and runs evaluations. | Verified fact | A1-S097, A1-S099 |
| Stack position | Cross-cutting production observability integrated with Datadog APM and infrastructure monitoring | Verified fact | A1-S097 |
| Integration | Accepts OpenTelemetry traces using OTel 1.37+ GenAI semantic conventions or OpenInference conventions; auto-instrumentation for OpenAI, LangChain, Bedrock, Anthropic | Verified fact | A1-S098, A1-S097 |
| Dependencies | Datadog platform; Datadog SDK auto-instrumentation or OTel | Verified fact | A1-S097, A1-S098 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Automatic sensitive-data scanning and redaction; prompt-injection identification | Verified fact | A1-S097 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Metered on number of LLM spans ingested (rates on Datadog pricing page) | Verified fact | A1-S097 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Integrates with OpenAI, LangChain, AWS Bedrock, Anthropic; OTel and OpenInference ingestion | Verified fact | A1-S097, A1-S098 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

# L8: Data extraction, ingestion and web

## Docling (`L8-docling`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Docling – doc parser

*Rationale:* MIT, foundation-governed and self-hostable, so it can anchor the firm's canonical document model; enterprise controls are built around it.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Broad formats, OCR, VLM and chunking; no ACL, PII or lineage, and table accuracy not independently verified. |
| Enterprise readiness | 3 | Library rule: inherits host controls; docling-serve gives an API boundary; commercial managed option via IBM watsonx. |
| Security and compliance | 4 | Library rule: MIT; SECURITY.md with private vulnerability reporting, OpenSSF Best Practices badge participation and cryptographically signed releases on PyPI, Quay.io and GHCR [VF: B-REV-S001]; IBM offers a managed service. |
| Deployment flexibility | 4 | Self-hosted, private cloud, on-prem and an IBM-managed service; air-gap not explicitly documented. |
| Ecosystem | 4 | MCP server, REST server and agent-framework integrations; LF AI & Data project. |
| Reliability and maturity | 4 | Graduate-tier foundation project with steady releases; rapid minor-version churn. |
| Cost / TCO | 5 | Free; CPU sufficient for standard pipelines, GPU only for VLM/ASR paths [AJ]. |
| Lock-in / portability | 5 | MIT, open format, neutral governance. |
| **Total (generic / FS)** | **4.00 / 4.05** | |

*Evidence rules applied:* Library rule applied (enterprise_readiness and security_compliance scored on what the library enables and project hygiene; inherits host controls)

**Capabilities.** Open-source conversion of PDF, Office, legacy Office, HTML, images, audio and video into a unified DoclingDocument, with OCR, VLM pipelines, ASR and hybrid chunking; runs as a library, CLI, docling-serve REST API or MCP server [VF: A1-S057, A1-S111, A1-S082].

**Strengths**

- MIT licence and LF AI & Data governance (donated March 2025; Graduate tier August 2026) [VF: A1-S057, V1-S091]
- Local or self-hosted processing keeps documents in the firm's estate [AJ]
- Broad format coverage including PPTX, XLSX and legacy Office [VF: A1-S111]
- A documented canonical representation (DoclingDocument) that can serve as the firm's internal document model [AJ]

**Limitations and risks**

- No ACL, PII or lineage features in the README or docs navigation [VF: A1-S057]
- Very fast release cadence (2.135.0 on 7 October 2026; 223 releases in about two years) makes version pinning mandatory [VF: A1-S008]
- Individual models carry their own licences, which need separate review [VF: A1-S057]
- A security policy with private vulnerability reporting, OpenSSF Best Practices badge participation and signed releases is published [VF: B-REV-S001]

**Choose when**

- Documents must not leave the firm's estate
- You want an open canonical document model that survives a change of parser or OCR engine

**Avoid when**

- You need managed, permission-aware connectors out of the box
- You have no platform team to run, pin and patch a Python service

**Nearest competitors:** L8-unstructured, L8-mineru, L8-llamaparse

**Regulated-FS note.** Default self-hosted parser for client and confidential documents; pin the docling version and each model version in a parse manifest so that a parse can be reproduced for audit [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Docling Project, hosted by the LF AI & Data Foundation; started by IBM Research Zurich | Verified fact | A1-S057, V1-S091 |
| Category | Open-source document conversion and parsing toolkit (PDF, Office, HTML, images, audio) with VLM pipelines and chunking | Verified fact | A1-S057, A1-S111 |
| Version / lineup | docling 2.135.0, released 7 October 2026; docling-serve has a stable v1 API | Verified fact | A1-S008, A1-S082 |
| Licence | MIT (codebase); individual models carry their own licences | Verified fact | A1-S057, A1-S008 |
| Status events | March 2025: IBM donated Docling to the LF AI & Data Foundation as an Incubation-stage project (formal induction announced 29 April 2025); August 2026: graduated to Graduate-tier LF AI & Data project; Repository now under the docling-project organisation | Verified fact | A1-S057, V1-S091 |
| Strategic direction | VLM support including IBM GraniteDocling, MCP server for agents, docling-serve API server, managed 'Docling for IBM watsonx' | Verified fact | A1-S057, A1-S082, A1-S110 |
| What it does | Parses many document formats into a unified DoclingDocument representation and exports Markdown, JSON and other formats; supports OCR, VLM pipelines, ASR for audio/video and hybrid chunking. | Verified fact | A1-S057, A1-S111 |
| Stack position | L8 document parsing; runs locally or as an API service | Verified fact | A1-S057, A1-S082 |
| Integration | Python library and CLI, REST API (docling-serve), MCP server; integrations with agent frameworks | Verified fact | A1-S057, A1-S082 |
| Dependencies | Python; LibreOffice for legacy Office/RTF; optional ASR extra and ffmpeg for media; optional VLMs | Verified fact | A1-S111 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Local/self-hosted processing keeps documents in the customer environment | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Commercial managed option via IBM watsonx | Verified fact | A1-S110 |
| Pricing | Free (MIT); managed IBM watsonx pricing not captured | Verified fact | A1-S057, A1-S110 |
| Infrastructure cost | CPU is sufficient for standard pipelines; VLM and ASR pipelines benefit from GPU | Architectural judgement |  |
| Ecosystem | Format coverage: PDF, DOCX/XLSX/PPTX, legacy Office, ODF, EPUB, Apple iWork, Markdown, AsciiDoc, LaTeX, HTML, MHTML, CSV, images, audio, video | Verified fact | A1-S111 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First PyPI release 15 July 2024; 223 releases to 7 October 2026 | Verified fact | A1-S008 |
| Deployment | saas: Not publicly verified; managed_cloud: Yes (Docling for IBM watsonx managed service); vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## Unstructured: open-source 'unstructured' library and 'unstructured-ingest' connectors; commercial Transform v2 API / platform (`L8-unstructured`)

**Tier:** Strategic · **Flags:** Renamed · **Original graphic label:** Unstructured – ETL for docs

*Rationale:* The open-source ingest connectors are the only verified source of ACL metadata and incremental reprocessing in L8, with an in-VPC commercial path.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Partitioning, chunking and the only verified ACL-aware incremental connectors; best table quality is API-only. |
| Enterprise readiness | 3 | SAML 2.0/OIDC SSO and account- and workspace-level roles mapped from IdP groups on Business deployments [VF: B-REV-S016]; no workspace audit log documented (stdout logging for the customer's own collection), so 3. |
| Security and compliance | 4 | Vendor-listed SOC 2 Type 2, ISO 27001, HIPAA and CMMC 2.0 Level 2 (medium confidence); FedRAMP wording is 'alignment' only and is not relied on; data region not verified. |
| Deployment flexibility | 5 | Shared SaaS, dedicated, in-VPC, self-hosted open source and vendor-marketed on-prem/air-gapped. |
| Ecosystem | 4 | Large connector catalogue into vector stores and warehouses. |
| Reliability and maturity | 3 | Four years of releases, but pre-1.0 library and a PyPI/changelog version mismatch. |
| Cost / TCO | 3 | Open source free; API pricing published but conflicting. |
| Lock-in / portability | 4 | Apache-2.0 library and connectors; proprietary API for best models. |
| **Total (generic / FS)** | **3.80 / 3.85** | |

*Evidence rules applied:* NPV cap lifted at CP2 review (8 October 2026): SSO and RBAC verified (B-REV-S016); audit-log feature not documented; Rule 7 (CP2 Q2) checked at CP2 rework: SSO and RBAC verified, audit logs not documented, so 3 kept (maximum without all three controls)

**Capabilities.** Apache-2.0 'unstructured' partitioning library and 'unstructured-ingest' connectors (SharePoint including Teams channel files, OneDrive, Confluence, Salesforce, S3 and others) that move data to vector stores and warehouses; commercial Transform v2 API with shared, dedicated and in-VPC tiers [VF: A1-S075, A1-S094, A1-S117, V1-S019].

**Strengths**

- Only L8 product with verified permission-aware ingestion: a permissions_version SHA-256 ACL digest that triggers reprocessing on ACL-only change [VF: A1-S094]
- Distinguishes an unavailable permission fetch from an empty permission set [VF: A1-S094]
- Vendor lists SOC 2 Type 2, ISO 27001, HIPAA and CMMC 2.0 Level 2 [VF: A1-S117, V1-S090]
- Open-source library and connectors stay free, so the pipeline can run in the firm's estate [VF: A1-S075]

**Limitations and risks**

- No workspace audit-log feature is documented; logs go to stdout for the customer's own collection [VF: B-REV-S016]
- Highest-quality models only via the proprietary API [VF: A1-S075]
- Library still pre-1.0 after four years (0.27.16) [VF: A1-S011]
- Per-page price conflict (US$0.015 vs US$0.03) [VF: A1-S117, A1-S118]
- Library sends usage analytics by default [VF: A1-S075]

**Choose when**

- You need connector-level ACL capture and incremental reprocessing from SharePoint, OneDrive or Confluence
- You want one pipeline that can run as open source in-estate or as an in-VPC commercial tier

**Avoid when**

- You need a documented, exportable audit log on the hosted service today
- Your corpus is mostly scanned or table-heavy and you will not pay for the API models [AJ]

**Nearest competitors:** L8-docling, L8-llamaparse, L8-reducto

**Regulated-FS note.** The connector ACL digest is the nearest thing in this layer to entitlement-preserving ingestion; disable default analytics and confirm the hosted data region before any client data is sent [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Unstructured (Unstructured-IO) | Verified fact | A1-S075, A1-S012 |
| Category | Document partitioning and ETL for LLMs: open-source library plus commercial hosted API | Verified fact | A1-S075 |
| Version / lineup | unstructured 0.27.16 (5 October 2026); unstructured-ingest 1.11.19 on PyPI (23 September 2026; changelog lists 1.11.21); unstructured-client SDK 0.46.2 | Verified fact | A1-S011, A1-S095, A1-S094, A1-S012 |
| Licence | Open source Apache-2.0 (library and ingest); commercial API proprietary; client SDK MIT | Verified fact | A1-S011, A1-S095, A1-S012, A1-S075 |
| Status events | Commercial API now branded 'Transform v2' (date not verified) | Verified fact | A1-S075 |
| Strategic direction | Open-source library 'is, and will stay, completely free'; higher-quality models offered via the Transform v2 API, which the vendor claims gives 2x table content accuracy and 58% less invented content than the library | Verified fact | A1-S075 |
| What it does | Partitions PDFs, HTML, Word and many other formats into structured elements, with chunking, and moves data from source connectors to destinations (vector DBs, warehouses). | Verified fact | A1-S075, A1-S094 |
| Stack position | L8 ingestion/ETL, including connector-level permissions metadata relevant to H7 | Verified fact | A1-S094 |
| Integration | Python library, ingest connectors (SharePoint incl. Teams channel files, OneDrive, Confluence, Salesforce, Databricks, S3, Teradata, Milvus and others), hosted API with client SDK | Verified fact | A1-S094, A1-S012, A1-S075 |
| Dependencies | Python; tesseract and poppler for PDFs/images; Docker images available | Verified fact | A1-S075 |
| Certifications | SOC 2 Type 2, HIPAA, ISO 27001 and GDPR listed on pricing page and API docs; CMMC 2.0 Level 2 certification (110/110, announced c. November 2025); API docs also claim "adherence" to FedRAMP, but no FedRAMP authorisation was found - do not state FedRAMP; certificates via trust.unstructured.io | Verified fact | A1-S117, V1-S090 |
| GDPR / residency | DPA available; GDPR claim scoped to SaaS hosted product; data region not verified | Verified fact | A1-S117 |
| Security features | Ingest connectors emit a permissions_version ACL digest (SHA-256) so ACL-only changes trigger reprocessing; credential redaction in connector errors; library sends lightweight usage analytics by default | Verified fact | A1-S094, A1-S075 |
| Access controls | Connector-level permission metadata captured from SharePoint, OneDrive and Confluence (ACL digest); platform RBAC/SSO not verified | Verified fact | A1-S094 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Let's Go free (10,000 pages once per account); Pay-As-You-Go US$0.015 per page; Business (dedicated or in-VPC) custom. Conflict: Terms of Service and older pages state US$0.03 per page after 15,000 free pages/month | Verified fact | A1-S117, A1-S118 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Large connector catalogue in unstructured-ingest | Verified fact | A1-S094 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | unstructured first on PyPI 6 September 2022; 237 releases | Verified fact | A1-S011 |
| Deployment | saas: Yes (hosted API; Let's Go / Pay-As-You-Go shared); managed_cloud: Yes (dedicated instance in Unstructured's cloud, Business plan); vpc_byoc: Yes (in-VPC in customer cloud, Business plan); private_cloud: Yes (open source); self_hosted: Yes (open source); on_prem: Yes (open source; vendor markets on-prem/air-gapped) | | |

## Google Cloud Document AI (`L8-google-document-ai`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10). Google's lead document-processing service; confirm the processor region and keep outputs in the firm's canonical document model to limit processor lock-in [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | OCR, form parsing, layout parsing with chunking, custom extraction and classification. |
| Enterprise readiness | 4 | Consumed through Google Cloud: IAM including deny policies, VPC Service Controls, IAM-governed Cloud Audit Logs and SAML/OIDC federation at platform level [VF: B-REV-S010, B-REV-S012]; rule 6 (CP2 Q1) presumes platform controls, and no product-specific gap is evidenced, so 4; platform controls presumed (CP2 Q1); confirm per service. Not 5: Document AI's predefined roles and SLA terms were not read. |
| Security and compliance | 4 | In scope for Google Cloud ISO 27001/27017/27018, SOC 1/2/3 and PCI DSS (A1-S102), plus CMEK and US/EU data residency (B-REV-S010, B-REV-S011); CMEK needs allowlisting in some regions. Held at 4, not 5, under rule 8: the scope page names a 'SOC 2 Report' without stating Type II, as for AgentCore Memory (L5); the same Google scope evidence gives 4 for Sensitive Data Protection, Model Armor and Apigee. |
| Deployment flexibility | 2 | Managed SaaS only; us and eu multi-regions and regional processors (B-REV-S010, B-REV-S011); no VPC or self-hosted option. |
| Ecosystem | 3 | Google Cloud ecosystem; integrations not captured. |
| Reliability and maturity | 3 | Hyperscaler managed service; maturity facts not captured [AJ]. |
| Cost / TCO | 4 | Transparent per-page pricing with volume tiers. |
| Lock-in / portability | 2 | Google-specific processors and outputs; adds to hyperscaler concentration. |
| **Total (generic / FS)** | **3.40 / 3.25** | |

*Evidence rules applied:* NPV cap lifted at CP2 review (8 October 2026): platform IAM, Cloud Audit Logs and federated SSO verified (B-REV-S010, S012); Rule 6 (CP2 Q1, hyperscaler presumption) applied at CP2 rework: enterprise_readiness 3 -> 4; platform controls presumed (CP2 Q1); confirm per service; Rule 8 (CP2 Q4) re-checked at CP3 rework (8 October 2026): certifications are product-scoped (A1-S102) with CMEK, but the SOC 2 report type is not stated, so security_compliance 5 -> 4 for consistency with other hyperscaler services

**Capabilities.** Google Cloud managed OCR, parsing, extraction and classification through processors: Enterprise Document OCR, Form Parser, Layout Parser (with initial chunking), Custom Extractor, classifier/splitter and Summarizer [VF: A1-S101].

**Strengths**

- In scope for Google Cloud ISO 27001/27017/27018, SOC 1/2/3 and PCI DSS [VF: A1-S102]
- Published per-page pricing; Enterprise Document OCR at US$1.50 per 1,000 pages [VF: A1-S101]
- Runs on a provider designated under DORA and the UK CTP regime (Google Cloud EMEA Limited) [VF: A8-S020, A8-S023]

**Limitations and risks**

- Processor outputs are Google-specific and require Google Cloud [VF: A1-S101]
- IAM, VPC Service Controls, us/eu multi-regions and CMEK were evidenced at CP2 review [VF: B-REV-S010, B-REV-S011]; support and SLA terms not captured [NPV]; platform controls presumed (CP2 Q1); confirm per service [Rec]
- SaaS only; no self-hosting [AJ]
- Form Parser and Custom Extractor at US$30 per 1,000 pages [VF: A1-S101]

**Choose when**

- Google Cloud is already the firm's approved cloud and processing region is confirmed
- You want hyperscaler certifications and consolidated third-party oversight

**Avoid when**

- Documents must stay on-prem or in a non-GCP estate
- You are trying to reduce hyperscaler concentration

**Nearest competitors:** L8-mistral-ocr, L8-reducto, Azure AI Document Intelligence (not in fact base), AWS Textract (not in fact base)

**Regulated-FS note.** Natural choice for a GCP-centred firm; confirm the processor region before use and keep outputs in the firm's canonical document model to avoid processor lock-in [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google Cloud (Alphabet) | Verified fact | A1-S101 |
| Category | Managed document OCR, parsing, extraction and classification service | Verified fact | A1-S101 |
| Version / lineup | Processors incl. Enterprise Document OCR, Form Parser, Layout Parser (with initial chunking), Custom Extractor, classifier/splitter, Summarizer | Verified fact | A1-S101 |
| Licence | Proprietary cloud service | Verified fact | A1-S101 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Extracts text, structure and entities from documents via pre-trained and custom processors, including layout parsing with chunking for RAG. | Verified fact | A1-S101 |
| Stack position | L8 OCR/parsing as a hyperscaler managed service | Verified fact | A1-S101 |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Google Cloud project | Verified fact | A1-S101 |
| Certifications | In scope for Google Cloud ISO 27001/27017/27018, SOC 1/2/3, PCI DSS and penetration testing | Verified fact | A1-S102 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Enterprise Document OCR US$1.50 per 1,000 pages (1k-5M pages/month; US$0.60 above 5M; first 1,000 free); Form Parser and Custom Extractor US$30 per 1,000 pages (first 1M, US$20 above); Layout Parser US$10 per 1,000 pages; discounts for consumption models | Verified fact | A1-S101 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Mistral OCR 4.1 (alias mistral-ocr-latest), part of Mistral Document AI (`L8-mistral-ocr`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Mistral OCR – OCR

*Rationale:* A good EU or self-managed OCR engine to sit behind an interface, but short model-retirement windows make it a component, not a foundation.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Strong OCR feature set with confidence scores; covers only the OCR step of the pipeline. |
| Enterprise readiness | 4 | Enterprise plan: SAML SSO, Admin/Billing/Member roles with isolated Workspaces and SCIM provisioning, audit logs on by default [VF: B-REV-S014, B-REV-S015]: all three controls plus SCIM, so 4 under rule 7 (CP2 Q2). Not 5: audit-log export is not supported, OIDC is not supported and SLA terms are NPV. |
| Security and compliance | 3 | Company-level SOC 2 Type II, ISO 27001 and ISO 27701; OCR scope unconfirmed. |
| Deployment flexibility | 4 | EU SaaS, private cloud, self-managed container and on-prem under enterprise agreement. |
| Ecosystem | 3 | Mistral SDKs with opt-in OTel spans; usable inside other parsers. |
| Reliability and maturity | 2 | OCR 4.0 retired about five weeks after 4.1 reached GA; frequent version replacement. |
| Cost / TCO | 4 | US$4 per 1,000 pages, US$2 batch; self-host pricing unpublished. |
| Lock-in / portability | 3 | Proprietary model, but text/JSON output is easy to swap behind an interface. |
| **Total (generic / FS)** | **3.30 / 3.25** | |

*Evidence rules applied:* NPV cap lifted at CP2 review (8 October 2026): SSO, RBAC and audit logs verified (B-REV-S014, S015); Rule 7 (CP2 Q2) applied at CP2 rework: all three controls plus SCIM; enterprise_readiness 3 -> 4; audit-log export not supported (stated as a due-diligence condition); Rule 8 (CP2 Q4) confirmed: company-level certifications with OCR scope not confirmed score one below the anchor (3)

**Capabilities.** Mistral OCR 4.1 (alias mistral-ocr-latest), part of Mistral Document AI: OCR endpoint returning structured output with bounding boxes, block labels, table formatting, header/footer extraction and block-level confidence scores [VF: A1-S083, A1-S130].

**Strengths**

- EU-hosted managed API [VF: A1-S135]
- Self-managed single-container, private-cloud and on-prem deployment for enterprise customers [VF: A1-S135]
- Low published price: US$4 per 1,000 pages, US$2 in batch [VF: A1-S130, V1-S010]
- Block-level confidence scores support quarantine thresholds [VF: A1-S130]

**Limitations and risks**

- Model-version churn: OCR 4.1 GA 26 August 2026 and OCR 4.0 retired 30 September 2026; the original model is no longer maintained [VF: A1-S130, V1-S014]
- Certifications are company-level; OCR scope not confirmed [VF: A1-S136]
- Self-hosting licence terms and hardware sizing not published [NPV]
- OCR only: no connectors, ACL, PII or lineage [AJ]
- Audit logs cannot be exported [VF: B-REV-S015], so the firm cannot hold them in its own archive without a vendor export route [AJ]

**Choose when**

- You need an EU-resident or self-managed OCR engine behind your own parsing pipeline
- Scanned documents dominate and cost per page matters

**Avoid when**

- You cannot re-validate within a deprecation window of weeks
- You call the 'latest' alias in production

**Nearest competitors:** L8-google-document-ai, L8-docling, L8-reducto

**Regulated-FS note.** Pin the dated model ID (not mistral-ocr-latest), store OCR outputs with the model ID, and treat each model retirement as a change-control event with re-validation [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Mistral AI | Verified fact | A1-S083, A1-S084 |
| Category | Hosted OCR / document understanding model API | Verified fact | A1-S083 |
| Version / lineup | OCR 4.1 (mistral-ocr-4-1; aliases mistral-ocr-latest and mistral-ocr-4): released July 2026 (model page 16 July; changelog 26 July) and marked Generally Available in the changelog on 26 August 2026 (governance page gives a 13 August 2026 release date); OCR 4.0 deprecated late September and retired 30 September 2026; OCR 3 (25.12) still available for existing integrations; original Mistral OCR no longer maintained | Verified fact | A1-S130, V1-S014, V1-S010 |
| Licence | Proprietary model; hosted API, with self-managed deployment for enterprise customers under agreement | Verified fact | A1-S135 |
| Status events | OCR 4.0 retired 30 September 2026 (replaced by OCR 4.1 at same price); Original Mistral OCR no longer maintained | Verified fact | A1-S130, V1-S014 |
| Strategic direction | OCR 4 positioned for document intelligence: paragraph-level bounding boxes, structural block labels, block-level confidence scores; compact single-container self-hosting for residency and sovereignty | Verified fact | A1-S130, A1-S135 |
| What it does | OCR endpoint that processes a document (URL or file) and returns structured output, with optional bounding-box and document annotations in a requested format, table formatting, header/footer extraction, layout blocks and confidence scores. | Verified fact | A1-S083 |
| Stack position | L8 OCR; also usable as a model inside other parsers | Verified fact | A1-S083 |
| Integration | REST /v1/ocr via Mistral SDKs; SDK can emit opt-in OpenTelemetry traces following GenAI semantic conventions | Verified fact | A1-S083, A1-S084 |
| Dependencies | Mistral API (La Plateforme) | Verified fact | A1-S083 |
| Certifications | Mistral AI company-level SOC 2 Type II, ISO/IEC 27001:2022 and ISO/IEC 27701:2019 (Trust Center); scope for OCR not confirmed | Verified fact | A1-S136 |
| GDPR / residency | Managed API runs on Mistral infrastructure hosted in the EU; self-hosting keeps documents in customer environment | Verified fact | A1-S135 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | US$4 per 1,000 pages (cached input US$0.40); annotated pages US$5 per 1,000; 50% batch discount (US$2 per 1,000); no-code Document AI US$5 per 1,000 pages | Verified fact | A1-S130, A1-S135, V1-S010 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Python SDK mistralai 3.1.0 (6 October 2026) | Verified fact | A1-S017 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (EU-hosted serverless API); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes (private cloud, enterprise); self_hosted: Yes (single-container self-managed, enterprise); on_prem: Yes (on-premises, enterprise) | | |

## LlamaParse (now the name of LlamaIndex's whole document platform: Parse, Extract, Index, Split, Agents; previously marketed as LlamaCloud) (`L8-llamaparse`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** LlamaParse – PDF / documents

*Rationale:* Capable managed parser with EU and BYOC options, but proprietary credits, SDK churn and a platform that reaches into L6/L3 argue against a foundational dependency.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Parse, extract, split, classify and index across 130+ formats; no ACL, PII or lineage. |
| Enterprise readiness | 3 | SSO through SAML and OIDC on the managed service and the Enterprise plan is verified (A1-S116, B-REV-S023): one verified control lifts the NPV cap to 3 under rule 7 (CP2 Q2). Hosted organisations are flat (every member has the same access) [VF: B-REV-S023], named roles exist only when self-hosted, and audit logs are not documented, so not above 3. |
| Security and compliance | 3 | SOC 2 Type II and HIPAA BAA (medium confidence); no ISO 27001 found. |
| Deployment flexibility | 4 | SaaS NA/EU, BYOC, self-hosted and on-prem; air-gap not stated. |
| Ecosystem | 4 | LlamaIndex framework, MCP server, Python/TypeScript SDKs. |
| Reliability and maturity | 3 | Rename and SDK migration in 2026; company focus has shifted onto this product. |
| Cost / TCO | 3 | Published credits, but agentic tiers cost up to 45 credits per page. |
| Lock-in / portability | 2 | Proprietary credit model and API; managed index and agents deepen dependency. |
| **Total (generic / FS)** | **3.40 / 3.20** | |

*Evidence rules applied:* NPV cap lifted at CP2 rework (8 October 2026) under rule 7 (CP2 Q2): SSO verified (A1-S116, B-REV-S023); enterprise_readiness 2 -> 3, held at 3 because hosted roles are flat and audit logs are not documented

**Capabilities.** LlamaParse is now LlamaIndex's whole document platform (formerly LlamaCloud): agentic OCR and parsing of 130+ formats in priced tiers, structured extraction, splitting, classification, managed ingest/index/RAG pipelines and document agents [VF: A1-S080, A1-S081, V1-S008].

**Strengths**

- EU region with in-region storage and processing, EU DPA and SCCs [VF: A1-S115]
- BYOC on Azure, AWS and GCP, self-hosting via Helm, and on-premises [VF: A1-S115]
- SOC 2 Type II and a HIPAA pipeline with BAA on request [VF: A1-S115]
- Transparent credit pricing by parse tier [VF: A1-S116]

**Limitations and risks**

- Permission sync, PII detection and lineage not found [VF: A1-S080]
- SDK churn: legacy llama-cloud-services and llama-parse packages deprecated in 2026 [VF: A1-S013, A1-S014]
- Platform scope spans L8, L6 and L3, which invites a single-vendor knowledge stack [AJ]
- Whether SOC 2 covers BYOC or self-hosted installs is not stated [NPV]
- On the hosted service every organisation member has the same access to projects and resources; named roles exist only in self-hosted installs [VF: B-REV-S023]

**Choose when**

- You want a managed parser with an EU region or BYOC and per-page tier choice
- Complex layouts justify a higher-cost agentic tier on a subset of documents [AJ]

**Avoid when**

- You would let the vendor's Index become the system of record for entitled content
- You need ACL-preserving connectors

**Nearest competitors:** L8-reducto, L8-unstructured, L8-docling

**Regulated-FS note.** Use Parse and Extract behind the firm's own document model and keep indexing in the firm's L6 store; record the parse tier and SDK version with every output [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LlamaIndex, Inc. | Verified fact | A1-S080 |
| Category | Proprietary 'enterprise platform for agentic OCR, parsing, extraction, indexing' | Verified fact | A1-S080, A1-S081 |
| Version / lineup | SaaS; current Python SDK llama-cloud 2.17.0 (7 October 2026); legacy llama-cloud-services / llama-parse packages deprecated, maintained until 1 May 2026 | Verified fact | A1-S014, A1-S013, A1-S081 |
| Licence | Proprietary SaaS; SDKs MIT; companion open-source LiteParse is Apache-2.0 | Verified fact | A1-S014, A1-S080 |
| Status events | Platform branding consolidated under LlamaParse (README: 'LlamaParse is its own platform'); llama-cloud-services and llama-parse SDKs deprecated (maintenance to 1 May 2026) | Verified fact | A1-S080, A1-S013, V1-S008 |
| Strategic direction | LlamaIndex states its primary focus has shifted from the OSS framework to LlamaParse, LiteParse and parsing benchmarks (ParseBench, ExtractBench) | Verified fact | A1-S080 |
| What it does | Agentic OCR and parsing of 130+ formats with parse tiers, structured extraction, document splitting, managed ingest/index/RAG pipelines and deployable document agents. | Verified fact | A1-S080, A1-S081 |
| Stack position | L8 parsing plus managed indexing (L6) and document agents (L3); broader than the graphic's 'PDF / documents' tile | Verified fact | A1-S080 |
| Integration | REST API, Python and TypeScript SDKs, MCP server; usable with or without the LlamaIndex framework | Verified fact | A1-S081, A1-S080 |
| Dependencies | LlamaParse cloud (NA or EU) and API key; self-hosted/BYOC: Helm chart on Kubernetes (EKS, AKS, GKE or conformant) plus customer-selected LLM providers | Verified fact | A1-S081, A1-S115 |
| Certifications | SOC 2 Type II (report via Trust Center); HIPAA-compliant pipeline for Enterprise with BAA on request | Verified fact | A1-S115 |
| GDPR / residency | EU region (api.cloud.eu.llamaindex.ai): data stored and processed in EU; EU DPA, SCCs and Article 27 representative; region-specific API keys; self-hosted LLM provider choice affects residency | Verified fact | A1-S115 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Self-hosted: OIDC with Microsoft Entra ID, Okta; Enterprise plan includes SSO | Verified fact | A1-S115, A1-S116 |
| Enterprise support | Enterprise: negotiated credits and rate limits (5x), dedicated support, flexible deployment; Pro priority support | Verified fact | A1-S116 |
| Pricing | Free (10k credits/month), Starter US$50/month (40k credits), Pro US$500/month (400k credits), Enterprise custom; overage US$1.25 per 1,000 credits; parse 1-45 credits/page by tier (Fast 1, Cost-effective 3, Agentic 10, Agentic Plus 45) | Verified fact | A1-S116 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | LlamaIndex framework, MCP clients, LiteParse (open-source local parser) | Verified fact | A1-S080, A1-S081 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | llama-parse first on PyPI 2 February 2024; new llama-cloud SDK line >=1.0 | Verified fact | A1-S013, A1-S014 |
| Deployment | saas: Yes (NA and EU regions); managed_cloud: Not publicly verified; vpc_byoc: Yes (BYOC on Azure, AWS, GCP); private_cloud: Yes; self_hosted: Yes; on_prem: Yes (on-premises) | | |

## Firecrawl (`L8-firecrawl`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Firecrawl – web to LLM-ready

*Rationale:* The most enterprise-ready web acquisition option, but AGPL open core, US-only data location and unverified security evidence keep it tactical.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Full web acquisition surface plus parsing, PII redaction and prompt-injection check. |
| Enterprise readiness | 4 | SAML/OIDC SSO and SCIM on Enterprise, Admin and Member roles, SIEM audit logging of scrape events to Sentinel [VF: B-REV-S024]: all three controls plus SCIM, so 4 under rule 7 (CP2 Q2). Not 5: built-in roles only (no custom roles), team-management events not stated as logged, SLA NPV. |
| Security and compliance | 2 | Capped: SOC 2 Type II and HIPAA wording are vendor-page claims flagged by the V1 verifier. |
| Deployment flexibility | 3 | Cloud plus a reduced-feature self-hosted server. |
| Ecosystem | 4 | SDKs, CLI, webhooks; Alexandria plugins for major assistants. |
| Reliability and maturity | 3 | Two and a half years of SDK releases and recent Series B; API moved to v2. |
| Cost / TCO | 3 | Published credits; self-hosting means owning auth, TLS, persistence and anti-bot services. |
| Lock-in / portability | 2 | AGPL server and Cloud-only features create SaaS dependency. |
| **Total (generic / FS)** | **3.25 / 3.00** | |

*Evidence rules applied:* security_compliance capped at 2: Firecrawl security claims are vendor-only and flagged in V1 verification_log section 4; Rule 7 (CP2 Q2) applied at CP2 rework (8 October 2026): all three controls plus SCIM (B-REV-S024); enterprise_readiness 3 -> 4

**Capabilities.** Web data API (v2) for scrape, crawl, map, search, extract and parse into Markdown or JSON, plus Cloud-only Agent, Browser and Interact; respects robots.txt by default; Alexandria agent data library launched September 2026 [VF: A1-S053, A1-S077, A1-S079, A1-S129].

**Strengths**

- Per-request PII redaction, Zero Data Retention and an opt-in prompt-injection check for JSON extraction [VF: A1-S076, A1-S077]
- Enterprise SSO (SAML, OIDC), SCIM, IP and key restrictions and a DPA [VF: A1-S076]
- Self-hostable server for public-web crawling inside the firm's estate [VF: A1-S078]
- Transparent credit pricing [VF: A1-S127]

**Limitations and risks**

- Server is AGPL-3.0; enterprise controls, Agent and Browser are Cloud-only [VF: A1-S053, A1-S079, V1-S002]
- Privacy policy places servers and stored data in the US [VF: A1-S134]
- Security claims are vendor pages only; verifier says do not rely on them [VF: A1-S076]
- No document-level ACL or lineage [AJ]

**Choose when**

- Batch acquisition of approved public web sources, where US processing is acceptable or the self-hosted server is used
- You want PII redaction and ZDR as per-request switches on web content

**Avoid when**

- You plan to modify and expose the server as a network service without AGPL review
- Data must be processed in the EU or UK

**Nearest competitors:** L8-crawl4ai, L8-apify

**Regulated-FS note.** Use only for public, approved sources; route client or confidential data elsewhere, and obtain the SOC 2 report before relying on the Cloud for anything beyond public content [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Firecrawl (PyPI author listed as Mendable.ai); venture-backed (Series B US$75M, September 2026) | Verified fact | A1-S015, A1-S053, A1-S129 |
| Category | Web data API for AI: scrape, crawl, map, search, extract, parse, browser interaction and an autonomous research agent | Verified fact | A1-S077, A1-S079 |
| Version / lineup | Self-host guide pins server release v2.11.162; Python SDK firecrawl-py 4.49.3 released 7 October 2026; API v2 | Verified fact | A1-S078, A1-S015 |
| Licence | Open core: server AGPL-3.0; SDKs and some UI components MIT; Agent, Browser, Interact, dashboards and enterprise controls are Cloud-only | Verified fact | A1-S053, A1-S079, V1-S002 |
| Strategic direction | Launched Alexandria (September 2026): one interface over official data providers (e.g. Wikimedia Enterprise), custom connectors, Firecrawl indexes and the live web for agents; available as plugin in ChatGPT, Codex, Claude and Claude Code (October 2026); plus Agent, Interact, PII redaction and enterprise controls | Verified fact | A1-S129, A1-S076, A1-S079 |
| What it does | Turns websites and documents into LLM-ready markdown or structured JSON via scrape/crawl/map/search endpoints, with LLM extraction, PDF parsing and an agent for web research; respects robots.txt by default. | Verified fact | A1-S053, A1-S077 |
| Stack position | L8 web acquisition and parsing; overlaps L4 (search/browser tools for agents) | Verified fact | A1-S077, A1-S079 |
| Integration | REST API v2, Python/JS SDKs, CLI; webhooks | Verified fact | A1-S053, A1-S077 |
| Dependencies | Self-host: Docker Compose stack with PostgreSQL (pg_cron) and supporting services; LLM features need an OpenAI-compatible provider or Ollama; no verified minimum host size | Verified fact | A1-S078, A1-S079 |
| Certifications | SOC 2 Type II | Verified fact | A1-S076, V1-S080 |
| GDPR / residency | Privacy policy states servers and stored data are in the United States; vendor pages conflict (one older blog claims EU residency; 2026 page says US data residency); DPA and Zero Data Retention available | Verified fact | A1-S134, A1-S076 |
| Security features | Zero Data Retention (+1 credit/page), PII redaction (+4 credits/page), opt-in prompt-injection check for JSON extraction, static IP allowlisting, IP and API-key restrictions | Verified fact | A1-S076, A1-S077 |
| Access controls | SSO (SAML, OIDC), SCIM directory sync, per-key restrictions, spend limits per key/team (Enterprise) | Verified fact | A1-S076 |
| Enterprise support | Enterprise plans with dedicated support, custom credits, reserved concurrency | Verified fact | A1-S076 |
| Pricing | Free 1,000 credits/month; Hobby US$19/month (5k credits); Standard US$99/month (100k); Growth US$399/month (500k); Scale and Enterprise above; annual discounts; credits: scrape 1/page, JSON extraction +4, ZDR +1, PII redaction +4 | Verified fact | A1-S127, A1-S077 |
| Infrastructure cost | Self-hosting means owning authentication, TLS, persistence, monitoring, capacity and upgrades; advanced anti-bot services must be run separately | Verified fact | A1-S079 |
| Ecosystem | SDKs, CLI, X/LinkedIn routed via third-party providers with separate pricing | Verified fact | A1-S077, A1-S053 |
| Adoption signals | Series A US$14.5M (Nexus, 19 August 2025; >350,000 developers, 48k GitHub stars then); Series B US$75M led by Smash Capital (announced 22 September 2026 on the Firecrawl blog; changelog entry dated 20 August 2026; Form D shows US$82.06M preferred sold, first sale 31 August 2026) | Verified fact | A1-S128, A1-S129, V1-S015, V1-S009 |
| Maturity | firecrawl-py first published 12 April 2024; 209 releases | Verified fact | A1-S015 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes (self-host); self_hosted: Yes (reduced feature set); on_prem: Not publicly verified | | |

## Crawl4AI (`L8-crawl4ai`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** Crawl4AI – open crawler

*Rationale:* Useful and permissive in practice, but pre-1.0, single-maintainer and carrying a non-standard licence term.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers crawling, Markdown and extraction; no PII, ACL or provenance features. |
| Enterprise readiness | 2 | Library rule: token auth by default; no commercial enterprise support verified. |
| Security and compliance | 2 | Library rule: SECURITY.md and GitHub advisories exist (B-REV-S003), but eight advisories, five rated HIGH (SSRF, arbitrary file write, secret leakage, XSS), were fixed in 0.9.3-0.9.4 (August-September 2026) and only 0.9.x is supported; attribution term on the licence. |
| Deployment flexibility | 4 | Library, Docker server, private cloud, on-prem and hosted cloud. |
| Ecosystem | 3 | MCP for common coding assistants; smaller ecosystem than commercial peers. |
| Reliability and maturity | 2 | Pre-1.0 versioning and single-maintainer origin. |
| Cost / TCO | 4 | Free; operations cost is browsers and proxies. |
| Lock-in / portability | 4 | Open source, but the attribution clause is not plain Apache-2.0. |
| **Total (generic / FS)** | **2.90 / 2.90** | |

*Evidence rules applied:* Library rule applied (enterprise_readiness and security_compliance capped at 4; scored on project hygiene; inherits host controls); Rule 7 (CP2 Q2) checked at CP2 rework: no SSO, RBAC or audit control verified (token auth only, A1-S074); enterprise_readiness 2 kept under the library rule

**Capabilities.** Open-source crawler and scraper producing LLM-ready Markdown or structured data with browser automation, batch crawling and LLM extraction; Python library, CLI, self-hosted REST server, MCP and a hosted Crawl4AI Cloud [VF: A1-S074].

**Strengths**

- Self-hosted Docker server, with an API token required on every endpoint by default [VF: A1-S074]
- Free library; cost is browser compute and proxies [VF: A1-S074]
- Runs entirely inside the firm's estate [VF: A1-S074]

**Limitations and risks**

- Apache-2.0 plus an appended attribution requirement covering distributions and public uses; legal review advised [VF: A1-S056, V1-S001]
- Pre-1.0 (0.9.4) with a single-maintainer origin [VF: A1-S009, A1-S074]
- No disclosed venture funding (aggregator only) [R: A1-S132]
- No certifications or enterprise support found [NPV]

**Choose when**

- Self-hosted crawling of a small set of approved public sources by a team that can own it
- Prototyping web acquisition before committing to a commercial service

**Avoid when**

- It would be a critical production dependency without a support route
- Legal cannot accept the attribution clause for your use

**Nearest competitors:** L8-firecrawl, L8-apify

**Regulated-FS note.** Acceptable for public data in a controlled estate; record the attribution clause in the open-source register and do not use the hosted cloud for anything confidential [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Open-source project by UncleCode, now also offering hosted Crawl4AI Cloud | Verified fact | A1-S009, A1-S056, A1-S074 |
| Category | Open-source web crawler/scraper producing LLM-ready Markdown, plus a hosted API | Verified fact | A1-S074 |
| Version / lineup | v0.9.4, 23 September 2026 | Verified fact | A1-S009, A1-S074 |
| Licence | Apache-2.0 with an additional attribution requirement for distributions and public uses | Verified fact | A1-S056, V1-S001 |
| Status events | Crawl4AI Cloud hosted service launched (date not verified) | Verified fact | A1-S074 |
| Strategic direction | Launched Crawl4AI Cloud (search, answer, extraction without own LLM key, bot-wall handling, MCP) alongside the free library and Docker server | Verified fact | A1-S074 |
| What it does | Crawls and scrapes websites into clean Markdown or structured data for RAG and agents, with browser automation, batch crawling and LLM-based extraction. | Verified fact | A1-S074 |
| Stack position | L8 web acquisition; overlaps L4 search tools via the cloud API | Verified fact | A1-S074 |
| Integration | Python library, CLI, self-hosted REST API (/md, /crawl, /screenshot, /pdf, /execute_js), MCP, hosted API | Verified fact | A1-S074 |
| Dependencies | Python with headless browsers; Docker server image (AMD64/ARM64) | Verified fact | A1-S074 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Self-hosted server requires CRAWL4AI_API_TOKEN on every endpoint by default | Verified fact | A1-S074 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Library free; Crawl4AI Cloud pay-as-you-go with free starting credit; 1 credit = US$0.001 | Reported | A1-S132, A1-S074 |
| Infrastructure cost | Self-hosting cost is browser compute and proxies | Architectural judgement |  |
| Ecosystem | MCP for Claude Code, Codex, Cursor, OpenCode | Verified fact | A1-S074 |
| Adoption signals | No venture funding found; aggregator lists Crawl4AI as unfunded (Singapore, founded 2024); project funded via sponsorships and Crawl4AI Cloud | Reported | A1-S132 |
| Maturity | First PyPI release 25 September 2024; pre-1.0 (0.9.x) | Verified fact | A1-S009 |
| Deployment | saas: Yes (Crawl4AI Cloud); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## Reducto (`L8-reducto`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Reducto – enterprise docs

*Rationale:* Technically strong managed extraction with flexible deployment on paper, but security evidence is vendor-only and the API is proprietary.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Parse, extract, split, classify, edit and pipelines with webhooks; no governance metadata. |
| Enterprise readiness | 3 | SSO/SAML and RBAC listed as Enterprise features in the product docs [VF: B-REV-S017]; audit logging appears only on a marketing page; support terms NPV. |
| Security and compliance | 2 | Capped: SOC 2/HIPAA/ZDR claims are vendor-only and flagged by the V1 verifier. |
| Deployment flexibility | 4 | SaaS with EU/AU endpoints, VPC, on-prem and air-gap, all vendor-stated at medium confidence. |
| Ecosystem | 2 | REST API and Python SDK; wider integrations not verified. |
| Reliability and maturity | 3 | Well funded and in production use per vendor (about 1 billion pages, October 2025); SDK still 0.x. |
| Cost / TCO | 3 | Transparent per-page rates; Parse at US$10 per 1,000 pages is above OCR-only engines. |
| Lock-in / portability | 2 | Proprietary API and schema; no open format. |
| **Total (generic / FS)** | **3.05 / 2.90** | |

*Evidence rules applied:* NPV cap on enterprise_readiness lifted at CP2 review: SSO/SAML and RBAC on Enterprise per docs.reducto.ai (B-REV-S017); security_compliance capped at 2 (kept): certifications are vendor-only claims flagged in V1 verification_log section 4; Rule 7 (CP2 Q2) checked at CP2 rework: SSO and RBAC verified, audit logging only on a marketing page, so 3 kept

**Capabilities.** Proprietary document ingestion API with Parse, Extract, Split, Edit, Classify and Pipeline resources, asynchronous jobs and webhooks; EU and AU endpoints [VF: A1-S093, A1-S092].

**Strengths**

- Vendor-stated VPC, on-prem and air-gapped deployment with offline model updates [VF: A1-S112]
- Retention controls: auto-deletion within 24 hours on Growth/Enterprise and retention=0 on Enterprise [VF: A1-S112]
- Published per-page pricing by operation [VF: A1-S113]
- Funded (US$108M total, Series B led by a16z, October 2025) [VF: A1-S114, V1-S018]

**Limitations and risks**

- Security and deployment claims come from vendor-authored pages with internal inconsistencies; verifier says do not rely on them without the SOC 2 report [VF: A1-S112]
- SSO/SAML and RBAC are Enterprise-only [VF: B-REV-S017]; audit logging and enterprise support terms not verified [NPV]
- No PII, ACL or lineage features found [VF: A1-S092, A1-S093]
- Proprietary API and output schema [VF: A1-S093]

**Choose when**

- Complex financial or legal layouts where a managed extraction API justifies its price, and you can obtain the SOC 2 report and contract terms
- You need an air-gapped commercial parser and will validate the claim in due diligence

**Avoid when**

- Due diligence cannot obtain the SOC 2 report and BAA/DPA
- Extraction output would be treated as authoritative numbers

**Nearest competitors:** L8-llamaparse, L8-google-document-ai, L8-unstructured

**Regulated-FS note.** Promising for complex documents, but treat every security claim as unverified until the SOC 2 report and contract are in hand; pin to the EU endpoint or on-prem install for EU/UK client data [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Reducto (private; US$108M total funding after US$75M Series B led by a16z, October 2025) | Verified fact | A1-S114, V1-S018 |
| Category | Proprietary document ingestion API: parse, extract, split, edit, classify and pipelines | Verified fact | A1-S093 |
| Version / lineup | SaaS API; Python SDK reductoai 0.24.0, released 8 September 2026 | Verified fact | A1-S090 |
| Licence | Proprietary API; Python SDK Apache-2.0 | Verified fact | A1-S090 |
| Strategic direction | Series B used for model research, product and enterprise adoption; launched pay-as-you-go tier with 15k free credits (October 2025) | Verified fact | A1-S114 |
| What it does | API that parses documents into structured output and extracts, splits, edits and classifies documents, with asynchronous jobs, pipelines and webhooks. | Verified fact | A1-S093, A1-S091 |
| Stack position | L8 parsing and structured extraction | Verified fact | A1-S093 |
| Integration | REST API; Python SDK (sync/async); webhooks | Verified fact | A1-S091, A1-S093 |
| Dependencies | Reducto hosted API | Verified fact | A1-S092 |
| Certifications | SOC 2 Type I and Type II completed (report on request); HIPAA BAAs offered | Verified fact | A1-S112 |
| GDPR / residency | EU and AU regional endpoints (Enterprise option); API data auto-deleted within 24 hours on Growth/Enterprise, retention=0 (immediate deletion) for Enterprise; customer data not used for training on Growth/Enterprise | Verified fact | A1-S092, A1-S112 |
| Security features | Zero/short data retention controls; VPC deployment with no external storage; air-gapped install with offline model updates | Verified fact | A1-S112 |
| Access controls | SSO/SAML supported (VPC deployment) | Verified fact | A1-S112 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Per 1,000 pages: Parse US$10, Extract US$20, Deep Extract US$40, Split US$20, Classify US$7.50, Edit US$60; Standard pay-as-you-go with US$150 free usage (page also says 15,000 free credits); Enterprise custom | Verified fact | A1-S113 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Close to 1 billion pages processed; named customers Harvey, Rogo, Scale AI (October 2025) | Verified fact | A1-S114 |
| Maturity | SDK first published on PyPI 12 October 2024 | Verified fact | A1-S090 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (customer VPC); private_cloud: Yes (customer VPC); self_hosted: Yes; on_prem: Yes (on-prem and air-gapped) | | |

## MinerU (`L8-mineru`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** MinerU – PDF parser

*Rationale:* Technically capable and local-first, but a custom licence with revenue thresholds, an unpublished commercial price and fresh major-version change.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Four parsing tiers, broad formats and citation locators; no ACL, PII or lineage. |
| Enterprise readiness | 2 | Library rule: no enterprise support offer or access controls found. |
| Security and compliance | 2 | Library rule: local-first and telemetry opt-out, but custom licence with termination clause and no verified CVE process. |
| Deployment flexibility | 4 | Local, self-hosted, on-prem and an optional remote service. |
| Ecosystem | 2 | Integrations not verified. |
| Reliability and maturity | 3 | GA 4.0 line with frequent releases, but young (first PyPI June 2025) and a 2026 major migration. |
| Cost / TCO | 2 | Free below thresholds; commercial price above them is unpublished, plus GPU cost. |
| Lock-in / portability | 2 | Custom licence with revenue/MAU thresholds and automatic termination. |
| **Total (generic / FS)** | **2.80 / 2.70** | |

*Evidence rules applied:* Library rule applied (enterprise_readiness and security_compliance capped at 4; scored on project hygiene; inherits host controls); Rule 7 (CP2 Q2) checked at CP2 rework: no SSO, RBAC or audit control verified; enterprise_readiness 2 kept under the library rule

**Capabilities.** MinerU 4.0: local-first parsing of PDF, images, Office, OpenDocument, EPUB, OFD, HTML and CSV into Markdown/JSON with four parsing tiers, a document library with citation locators for agents, and a multi-service router [VF: A1-S055, A1-S010].

**Strengths**

- Local by default; documents are not uploaded unless remote parsing is set explicitly [VF: A1-S055]
- Citation locators give stable references for agent reading [VF: A1-S055]
- Telemetry is anonymous, excludes document content and file names, and can be disabled [VF: A1-S055]

**Limitations and risks**

- Custom 'MinerU Open Source License': separate commercial licence above 100M MAU or US$20M monthly revenue (group-consolidated); rights terminate on breach [VF: A1-S054, V1-S003]
- Commercial licence price not published [VF: A1-S054]
- Standard/Advanced tiers need a GPU with 8 GB+ VRAM [VF: A1-S055]
- Major-version migration (3.x to 4.0) in 2026 [VF: A1-S055]

**Choose when**

- Below the licence thresholds, or with a commercial licence in place, and local GPU parsing is acceptable
- As a second parser for reconciliation of hard tables [AJ]

**Avoid when**

- A large firm whose group revenue exceeds the threshold has no commercial licence
- You need vendor support or certifications

**Nearest competitors:** L8-docling, L8-unstructured, L8-llamaparse

**Regulated-FS note.** Large asset managers are likely to exceed the group-consolidated revenue threshold, so legal must clear the licence before any production use [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | OpenDataLab MinerU Team | Verified fact | A1-S054, A1-S055 |
| Category | Open-source document parsing tool and local document library with VLM-based parsing tiers | Verified fact | A1-S055, A1-S010 |
| Version / lineup | MinerU 4.0 line; mineru 4.0.10 released 29 September 2026 | Verified fact | A1-S010, A1-S055, V1-S004 |
| Licence | 'MinerU Open Source License': Apache-2.0 plus additional terms - separate commercial licence required above 100M MAU or US$20M monthly revenue (group-consolidated); attribution required for online services; rights terminate automatically on breach | Verified fact | A1-S054, A1-S010, V1-S003 |
| Status events | MinerU 4.0 released (3.x to 4.0 migration guide) | Verified fact | A1-S055 |
| Strategic direction | MinerU 4.0 adds four parsing tiers (Flash/Basic/Standard/Advanced), a document library with citation locators for agent reading, multi-format input and a router for multiple services | Verified fact | A1-S055 |
| What it does | Converts PDF, images, Office, OpenDocument, EPUB, OFD, HTML and CSV into Markdown/JSON and other formats, caches and searches results, and serves them to agents with stable citations. | Verified fact | A1-S055 |
| Stack position | L8 parsing/OCR; local-first with optional remote service (mineru.net) | Verified fact | A1-S055 |
| Integration | Python SDK, V1 API, CLI, Gradio WebUI, multi-service Router; remote parsing only with explicit --remote | Verified fact | A1-S055 |
| Dependencies | ONNX/PyTorch small models; llama.cpp, vLLM or LMDeploy for the VLM; Standard/Advanced tiers require GPU/MPS with 8 GB+ VRAM | Verified fact | A1-S055 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Parses locally by default; documents are not uploaded to the official service unless remote parsing is explicitly configured | Verified fact | A1-S055 |
| Security features | Anonymous aggregated telemetry (no document content or file names), can be disabled | Verified fact | A1-S055 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free under MinerU licence below thresholds; commercial licence above thresholds (price not published) | Verified fact | A1-S054 |
| Infrastructure cost | GPU with 8 GB+ VRAM needed for higher-quality tiers | Verified fact | A1-S055 |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | mineru package first on PyPI 13 June 2025; 96 releases | Verified fact | A1-S010 |
| Deployment | saas: Yes (mineru.net web app / remote API); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## Apify (`L8-apify`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Apify – scrapers

*Rationale:* Convenient for public long-tail scraping, but single US region, marketplace code risk and platform-specific Actors.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Scraping, automation, proxy and storage; no parsing depth or governance metadata. |
| Enterprise readiness | 3 | Organisation accounts with customisable roles and per-resource permissions, enforced 2FA and session limits; SSO stated in Apify's shared-responsibility documentation [VF: B-REV-S025]; no audit log found, so 3. |
| Security and compliance | 3 | SOC 2 Type II, encryption in transit and at rest, tenant isolation. |
| Deployment flexibility | 1 | One SaaS region only (AWS us-east-1). |
| Ecosystem | 3 | Store Actors, MCP server and connectors. |
| Reliability and maturity | 3 | Client library on PyPI since 2021 with frequent releases. |
| Cost / TCO | 3 | Published plans and compute-unit rates. |
| Lock-in / portability | 2 | Platform-specific Actors and storage; proprietary API. |
| **Total (generic / FS)** | **2.65 / 2.55** | |

*Evidence rules applied:* NPV cap lifted at CP2 review (8 October 2026): roles and SSO documented (B-REV-S025); no audit log found; Rule 7 (CP2 Q2) checked at CP2 rework: roles and SSO verified, no audit log found, so 3 kept

**Capabilities.** Serverless 'Actor' platform for scrapers and automations with Apify Proxy, datasets, key-value stores and request queues, the Apify Store marketplace and an MCP server [VF: A1-S087, A1-S089].

**Strengths**

- Large marketplace of ready-made Actors [VF: A1-S089]
- SOC 2 Type II with report via trust.apify.com [VF: A1-S085, V1-S089]
- Transparent compute-unit pricing [VF: A1-S133]

**Limitations and risks**

- Hosted only in AWS us-east-1; no EU region documented [VF: A1-S086, V1-S089]
- Third-party Store Actors are outside Apify's control under its shared-responsibility model [VF: A1-S086]
- Actors and storage are platform-specific [VF: A1-S087]
- Access controls and enterprise support not verified [NPV]

**Choose when**

- Long-tail public-web acquisition where a maintained Actor already exists and the data is public
- Short-lived research or market-data collection that never touches client data

**Avoid when**

- Any personal, client or confidential data is involved
- Data must be processed in the EU or UK

**Nearest competitors:** L8-firecrawl, L8-crawl4ai

**Regulated-FS note.** US-only processing and third-party Actors make it unsuitable for anything beyond public data; review each Actor as third-party code [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Apify Technologies s.r.o. | Verified fact | A1-S016 |
| Category | Web scraping and automation platform with an Actor marketplace (Apify Store), managed proxy and storage | Verified fact | A1-S087, A1-S089 |
| Version / lineup | SaaS platform; apify-client (Python) 3.2.1, released 25 September 2026 | Verified fact | A1-S016 |
| Licence | Proprietary platform; Python API client Apache-2.0 | Verified fact | A1-S016 |
| Strategic direction | Exposes Store Actors to AI agents through the Apify MCP server (mcp.apify.com) | Verified fact | A1-S089 |
| What it does | Runs serverless 'Actors' (scrapers and automations) in isolated containers, routes traffic through Apify Proxy, and stores results in datasets, key-value stores and request queues reachable via API. | Verified fact | A1-S087 |
| Stack position | L8 web acquisition; overlaps L4 tools via MCP | Verified fact | A1-S087, A1-S089 |
| Integration | REST API v2, JavaScript and Python clients, webhooks, MCP server, third-party connectors | Verified fact | A1-S087, A1-S089 |
| Dependencies | Hosted on AWS in a single region (us-east-1) across multiple Availability Zones; MongoDB Atlas, S3 and DynamoDB | Verified fact | A1-S086, A1-S087 |
| Certifications | SOC 2 Type II (report via trust.apify.com) | Verified fact | A1-S085, V1-S089 |
| GDPR / residency | Platform data hosted in AWS us-east-1 (no EU region documented) | Verified fact | A1-S086, V1-S089 |
| Security features | Encryption in transit and at rest; tenant isolation; shared-responsibility model documented | Verified fact | A1-S086, A1-S085 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free US$0 (US$5 prepaid usage, CU US$0.20); Starter US$19/month (CU US$0.20); Scale US$199/month (CU US$0.16); Business US$999/month (CU US$0.13); 1 CU = 1 GB RAM for 1 hour | Verified fact | A1-S133, A1-S088 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Apify Store Actors; MCP clients | Verified fact | A1-S089 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | apify-client first on PyPI 17 May 2021; 237 releases | Verified fact | A1-S016 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

# L7: Embeddings and reranking

## Cohere Embed 5 (embed-v5.0-pro, embed-v5.0-fast) and Cohere Rerank 4 (rerank-v4.0-pro, rerank-v4.0-fast) (`L7-cohere`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Cohere – Embed v3 + Rerank

*Rationale:* The widest deployment range among the hosted vendors, with FS-grade certifications. FS 3.70 on the hyperscaler route meets the numeric guide for Strategic, but it stays Tactical until its stated condition is met: per-service due diligence confirming the Foundry or SageMaker controls (the CP2 Q1 presumption is not that evidence), with the pending Aleph Alpha combination recorded as an ownership event. Upgrade candidate [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Current embed and rerank, multimodal, 128K context, Matryoshka and binary; no domain-specific models evidenced. |
| Enterprise readiness | 4 | Scored on the Microsoft Foundry and Amazon SageMaker routes (A2-S012), which the FS recommendation uses for VPC and in-region deployment: platform IAM, SSO and audit logging presumed under rule 6 (CP2 Q1), so 4; platform controls presumed (CP2 Q1); confirm per service. The direct hosted API documents only Owner and User team roles (B-REV-S013), one verified control, and would score 3 under rule 7 (CP2 Q2); SSO and audit logs for it remain NPV. |
| Security and compliance | 4 | SOC 2 Type II, ISO 27001, ISO 42001, ZDR on request and private deployment; CMK and EU hosted region unverified. |
| Deployment flexibility | 4 | SaaS, partner clouds, VPC, single-tenant and on-prem; air-gap not verified. |
| Ecosystem | 4 | Microsoft Foundry, SageMaker, LangChain, and Cohere Rerank hosted inside Pinecone. |
| Reliability and maturity | 3 | Mature, fast-moving line; pending Aleph Alpha combination adds governance uncertainty. |
| Cost / TCO | 3 | Embed prices published (Pro US$0.12, Fast US$0.08 per 1M text tokens); rerank price not found. |
| Lock-in / portability | 3 | Proprietary, but deployable in the firm's estate; rule 3 not applied because Cohere is the combining party, revisit on close. |
| **Total (generic / FS)** | **3.75 / 3.70** | |

*Evidence rules applied:* NPV cap lifted at CP2 rework (8 October 2026): rule 6 (CP2 Q1) on the Foundry and SageMaker routes gives 4 (platform controls presumed (CP2 Q1); confirm per service); the direct hosted API, with only Owner and User roles verified (B-REV-S013), would be 3 under rule 7 (CP2 Q2); Rule 8 (CP2 Q4) confirmed: company-level SOC 2 Type II, ISO 27001 and ISO 42001 with product scope not stated, security_compliance 4

**Capabilities.** Embed 5 (embed-v5.0-pro, embed-v5.0-fast; 30 September 2026): text, images and mixed text-image inputs into one vector, 100+ languages, 128K-token context, Matryoshka 256-2,048 dims, float/int8/binary outputs, Pro and Fast in one shared space. Rerank 4 (Pro and Fast; 11 December 2025): 32K-token context, multilingual, JSON documents [VF: A2-S012, A2-S009, A2-S010].

**Strengths**

- Embed and rerank from one vendor, both current generations [VF: A2-S012, A2-S010]
- Widest deployment range among hosted vendors: SaaS, Microsoft Foundry, Amazon SageMaker, VPC, Model Vault single-tenant, on-premises [VF: A2-S012, A2-S015]
- SOC 2 Type II, ISO 27001 and ISO 42001 [VF: A2-S014]; 30-day default log deletion and ZDR on request for enterprise customers [VF: A2-S145]
- Storage arithmetic is published: Cohere's example shrinks 100M chunks from about 819 GB to 3.2 GB with reduced dimensions and binary output [VF: A2-S013]

**Limitations and risks**

- The hosted platform documents only Owner and User team roles [VF: B-REV-S013]; SSO/SAML and audit logs for the direct hosted API were not found [NPV]; on Microsoft Foundry and SageMaker the platform's controls are presumed under CP2 Q1 and must be confirmed per service [AJ]; enterprise support terms NPV
- Rerank per-search price not found [VF: A2-S013]
- Aleph Alpha business combination signed 16 September 2026, pending regulatory approval [VF: A2-S018, V1-S028]; valuation figures conflict and are not used [AJ]
- EU hosted-region details not verified [NPV]; CMK for the hosted API not found [NPV]
- Vendor claims of 'highest average' scores are not decision inputs [R: A2-S013]

**Choose when**

- Embedding and reranking must run inside the firm's VPC or data centre with a commercial vendor behind it
- Long documents (128K context) or mixed text-image pages need one vector

**Avoid when**

- Public evidence of SSO/RBAC/audit for the direct hosted API is a hard procurement gate, the Foundry or SageMaker route is not available, and the evidence cannot be obtained in due diligence
- Ownership stability through the Aleph Alpha approval period is a hard requirement

**Nearest competitors:** L7-voyage, L7-jina, L7-nvidia-nemo-retriever, L7-gemini-embedding

**Regulated-FS note.** The private and Model Vault routes keep client-data embeddings off shared infrastructure, and Cohere states it has no access to prompts in private or partner deployments [VF: A2-S015, A2-S145]. Track the Aleph Alpha approval as an ownership event in the third-party register [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Cohere Inc. (pending business combination with Aleph Alpha, signed 16 September 2026) | Verified fact | A2-S018 |
| Category | Embedding and reranking models (hosted API, cloud marketplaces, private deployment) | Verified fact | A2-S011, A2-S015 |
| Version / lineup | Embed 5 (30 September 2026): Pro and Fast tiers in a shared embedding space; embed-v4.0 still listed. Rerank 4 (11 December 2025): Pro and Fast; Rerank 3.5 still available on Azure. | Verified fact | A2-S012, A2-S010, A2-S011, V1-S027, V1-S033 |
| Licence | Proprietary models (hosted API, marketplace and private deployments) | Verified fact | A2-S015 |
| Status events | 2025: Embed v4 (multimodal, 128K context) released; August 2025: US$500M raise at US$6.8B valuation; 11 December 2025: Rerank v4.0 released; 24 April 2026: Cohere and Aleph Alpha announce plan to combine; 16 September 2026: definitive business combination agreement signed, subject to regulatory approval; 30 September 2026: Embed 5 released | Verified fact | A2-S011, A2-S017, A2-S010, A2-S018, A2-S012, V1-S028 |
| Strategic direction | Enterprise/sovereign AI positioning: private on-prem/VPC deployment, Model Vault single-tenant hosting, and a transatlantic combination with Aleph Alpha (Berlin/Toronto HQs) | Verified fact | A2-S015, A2-S012, A2-S018 |
| What it does | Embed 5 embeds text, images and mixed text-image inputs (e.g. PDF pages) into one vector; 100+ languages; 128K-token context; Matryoshka 256-2,048 dims; float, int8 and binary outputs. Rerank 4 reorders candidates by relevance with 32K-token context and handles multilingual text and JSON documents. | Verified fact | A2-S012, A2-S009 |
| Stack position | L7, covering embedding and reranking from one vendor; correctly placed. | Architectural judgement |  |
| Integration | Cohere Embed and Rerank APIs (v2), SDKs, Azure AI Foundry and SageMaker endpoints; LangChain integration | Verified fact | A2-S011, A2-S012 |
| Dependencies | Cohere API, or partner clouds (Microsoft Foundry, Amazon SageMaker), or customer infrastructure for private deployments | Verified fact | A2-S012, A2-S015 |
| Certifications | SOC 2 Type II (annual; report under mNDA), ISO 27001, ISO 42001, UK Cyber Essentials; HIPAA listed as an FAQ entry (BAA not confirmed) | Verified fact | A2-S014 |
| GDPR / residency | Enterprise default: logged prompts/generations deleted after 30 days; Zero Data Retention available to enterprise customers on request (usage data still received); no Cohere access to prompts in private/partner deployments; EU hosted-region details not verified | Verified fact | A2-S145, A2-S014 |
| Security features | Private on-prem/VPC deployments with no Cohere access to customer data; Encrypted Vault product for regulated workloads | Verified fact | A2-S015, A2-S014 |
| Access controls | SSO/SAML, RBAC and audit-log export for the hosted API not found in public sources (7 October 2026); Model Vault attestation produces a signed record usable for audit | Verified fact | A2-S145 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Embed 5 Pro US$0.12 and Fast US$0.08 per 1M text tokens; images US$0.40 per 1M tokens (both). Rerank billed per search (rate not found). Model Vault: e.g. Embed 5 Pro Small US$3.00/hour or US$2,000/month; Rerank 4 Pro Large US$10.00/hour or US$6,500/month per instance. | Verified fact | A2-S013, A2-S016 |
| Infrastructure cost | Dedicated (Vault) instances billed per instance-hour or month | Verified fact | A2-S016 |
| Ecosystem | Available on Microsoft Foundry/Azure, Amazon SageMaker; LangChain integration | Verified fact | A2-S011, A2-S012 |
| Adoption signals | Funding: US$500M at US$6.8B (August 2025); press reports (September 2026) of talks at a US$20B valuation (unconfirmed) | Verified fact | A2-S017, A2-S019 |
| Maturity | Mature product line; frequent generations (Embed v4 2025, Rerank 4 Dec 2025, Embed 5 Sep 2026) | Verified fact | A2-S011, A2-S010, A2-S012 |
| Deployment | saas: Yes; managed_cloud: Yes (Microsoft Foundry, Amazon SageMaker; Model Vault single-tenant); vpc_byoc: Yes (VPC deployment); private_cloud: Yes (Model Vault single-tenant); self_hosted: Yes (private deployment); on_prem: Yes | | |

## Sentence Transformers (sentence-transformers library; SBERT.net) (`L7-sentence-transformers`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** SBERT – Sentence transformers

*Rationale:* The portable, self-hosted toolkit for embeddings, reranking, sparse and late interaction; the firm's exit route and fine-tuning base.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Covers dense, cross-encoder, sparse and multi-vector with fine-tuning; quality depends on the chosen model. |
| Enterprise readiness | 3 | Rule 2: enables in-estate serving and fine-tuning; no commercial support verified (capped at 4). |
| Security and compliance | 3 | Rule 2: Apache-2.0; SECURITY.md with private vulnerability reporting and CVE issuance through GitHub advisories (B-REV-S002); release signing not verified; inherits host controls. |
| Deployment flexibility | 4 | Self-host, on-prem and air-gap; no managed option of its own. |
| Ecosystem | 5 | Over 15,000 models on Hugging Face; many MTEB models load through it. |
| Reliability and maturity | 4 | Since 2019, regular 2026 releases, Hugging Face stewardship. |
| Cost / TCO | 4 | Free; compute and operations are the cost. |
| Lock-in / portability | 4 | Apache-2.0 and model-agnostic; stewarded by one company rather than a neutral foundation. |
| **Total (generic / FS)** | **3.80 / 3.70** | |

*Evidence rules applied:* Rule 2 (self-hosted library): enterprise_readiness and security_compliance capped at 4; NPV cap not applied

**Capabilities.** Apache-2.0 Python library (6.1.0, 18 September 2026) for dense embeddings, Cross-Encoder rerankers, Sparse Encoders and Multi-Vector Encoders (ColBERT-style late interaction), with training and fine-tuning; over 15,000 pre-trained models on Hugging Face [VF: A2-S029, A2-S032, A2-S028]. Maintained by Hugging Face [VF: A2-S028, V1-S092].

**Strengths**

- One toolkit for the whole retrieval-optimisation layer: bi-encoder, cross-encoder, sparse and late interaction [VF: A2-S029]
- Fine-tuning on in-domain pairs is the main route to domain adaptation without a vendor [VF: A2-S029] [AJ]
- Model-agnostic and permissively licensed, so it is the natural exit route from any hosted embedding API [AJ]

**Limitations and risks**

- A library, not a model: quality depends on the model chosen and on the firm's evaluation [AJ]
- No commercial support offer verified [NPV]; a security policy with private reporting and CVE issuance exists [VF: B-REV-S002], but release signing is not verified [NPV]
- Depends on Hugging Face stewardship and a small maintainer team [AJ]
- Model licences on the Hub vary; each model needs its own licence check (for example, Jina weights are CC-BY-NC-4.0) [VF: A2-S024] [AJ]

**Choose when**

- Embeddings or reranking must run inside the firm's estate, including air-gapped
- Domain fine-tuning or a reproducible, pinned retrieval stack is required

**Avoid when**

- There is no team to operate model serving, patching and evaluation
- A vendor SLA is mandatory for the retrieval path

**Nearest competitors:** L7-nvidia-nemo-retriever, L7-qwen3-embedding, L7-cohere

**Regulated-FS note.** Inherits host controls: residency, access and logging are whatever the firm's platform provides [AJ]. Pin library and model versions and record both in the evidence pack [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Hugging Face (maintainer Tom Aarsen); originally developed by UKP Lab, TU Darmstadt (author Nils Reimers) | Verified fact | A2-S029, A2-S028, V1-S092 |
| Category | Open-source Python library for embedding, reranker (cross-encoder), sparse-encoder and multi-vector models | Verified fact | A2-S029 |
| Version / lineup | 6.1.0, released 18 September 2026 (6.0.0 on 18 August 2026) | Verified fact | A2-S029, A2-S032 |
| Licence | Open source, Apache-2.0 | Verified fact | A2-S029, A2-S028 |
| Status events | Late 2023: Tom Aarsen took over maintainership; c. late 2025: project formally transitioned from UKP Lab to Hugging Face (date not confirmed); 18 August 2026: v6.0.0; 18 September 2026: v6.1.0 | Verified fact | A2-S028, A2-S032, V1-S092 |
| Strategic direction | Broadening from dense embeddings to Cross-Encoder rerankers (v4), Sparse Encoders (v5) and Multi-Vector Encoders for ColBERT-style late interaction (v6) | Verified fact | A2-S028, A2-S029 |
| What it does | Computes embeddings, cross-encoder similarity scores, sparse embeddings and token-level multi-vector embeddings, and trains/fine-tunes such models; over 15,000 pre-trained models on Hugging Face. | Verified fact | A2-S029 |
| Stack position | L7 tooling (library/runtime for self-hosted models), not a hosted model; complements rather than competes with API vendors. | Architectural judgement |  |
| Integration | Python library; models from Hugging Face Hub | Verified fact | A2-S029 |
| Dependencies | Python >=3.10; PyTorch/transformers ecosystem; optional image and audio extras | Verified fact | A2-S029 |
| Certifications | Not applicable (open-source library) | Architectural judgement |  |
| GDPR / residency | Not applicable (runs in customer environment) | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free, open source (Apache-2.0) | Verified fact | A2-S029 |
| Infrastructure cost | CPU/GPU compute for inference and fine-tuning; cost scales with model size and corpus volume | Architectural judgement |  |
| Ecosystem | Hugging Face Hub; many MTEB leaderboard models load via the library | Verified fact | A2-S029 |
| Adoption signals | Over 15,000 pre-trained Sentence Transformers models on Hugging Face | Verified fact | A2-S029 |
| Maturity | Introduced 2019; eight releases between May and September 2026 | Verified fact | A2-S028, A2-S032 |
| Deployment | saas: No (library); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes | | |

## Gemini Embedding 2 (model id gemini-embedding-2) (`L7-gemini-embedding`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Gemini – Embedding 2

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10), consumed through Vertex AI. Google's lead embedding model and the leading multimodal option; not where UK-only processing is mandatory, because the eu multi-region excludes the UK [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Multimodal, multilingual, Matryoshka 128-3,072; task types unsupported; Google's reranker is the separate Vertex ranking API (B-REV-S026). |
| Enterprise readiness | 4 | Consumed through Google Cloud Vertex AI: IAM predefined, custom and endpoint-level roles, Cloud Audit Logs (Data Access logs for predict calls must be enabled) and SAML/OIDC federation verified at platform level [VF: B-REV-S007, B-REV-S008, B-REV-S012]; rule 6 (CP2 Q1) presumes platform controls, and no product-specific gap is evidenced, so 4; platform controls presumed (CP2 Q1); confirm per service. Not 5: SCIM and support terms are not evidenced. |
| Security and compliance | 4 | Strong platform certifications including ISO 42001 and FedRAMP High; generative AI on the platform supports CMEK, VPC-SC and data residency (B-REV-S009), but per-model scope for embedding calls is not confirmed, so 4. |
| Deployment flexibility | 2 | Gemini API and Vertex AI only (global, us, eu); no private or self-hosted route. |
| Ecosystem | 3 | Google platform integration and one named adopter (Box); wider ecosystem NPV. |
| Reliability and maturity | 3 | GA since April 2026 (about 5.5 months); pricing pages lagged the GA status. |
| Cost / TCO | 3 | Transparent, but text pricing above peers; multimodal priced per modality. |
| Lock-in / portability | 2 | Proprietary hosted API plus Google platform coupling; re-embedding to switch. |
| **Total (generic / FS)** | **3.30 / 3.20** | |

*Evidence rules applied:* NPV cap lifted at CP2 review (8 October 2026): platform IAM, Cloud Audit Logs and federated SSO verified (B-REV-S007, S008, S012); Rule 6 (CP2 Q1, hyperscaler presumption) applied at CP2 rework: enterprise_readiness 3 -> 4; platform controls presumed (CP2 Q1); confirm per service; Rule 8 (CP2 Q4) confirmed: platform-level certifications with per-model scope not confirmed, security_compliance 4

**Capabilities.** gemini-embedding-2 (GA 22 April 2026): one embedding space for text, images, video, audio and PDFs across 100+ languages; 8,192 text tokens; Matryoshka output 128-3,072 dims [VF: A2-S004, A2-S005]. Hosted on the Gemini API and Vertex AI (being renamed Gemini Enterprise Agent Platform) [VF: A2-S039].

**Strengths**

- Natively multimodal with Matryoshka dimensions, useful for scanned documents and charts [VF: A2-S004, A2-S005]
- Platform certifications for Generative AI on Vertex AI: SOC 2, ISO/IEC 27001, ISO/IEC 42001, HIPAA, FedRAMP High [VF: A2-S043]
- 'eu' multi-region endpoint keeps data in EU member states [VF: A2-S039]; Batch at 50% of standard price [VF: A2-S005, A2-S038]

**Limitations and risks**

- EU multi-region excludes the UK and Switzerland [VF: A2-S039]
- Per-model certification coverage and CMEK applicability for embedding calls not confirmed [VF: A2-S043, A2-S039]
- Hosted only, no weights; coupling to Google platform services (File Search, Memory Bank) [AJ]
- task_type parameter not supported [VF: A2-S005]; Google's reranker is a separate service, the Vertex ranking API (semantic-ranker models; version 005 in preview from 1 September 2026) [VF: B-REV-S026]
- Text price US$0.20 per 1M tokens is higher than most hosted peers (as of 7 October 2026) [VF: A2-S038]

**Choose when**

- The estate is Google Cloud-centred and EU processing is sufficient
- Retrieval must span images, audio, video or PDF pages in one vector space

**Avoid when**

- UK processing is mandatory
- Self-hosting or an exit route that keeps the same vectors is required

**Nearest competitors:** L7-cohere, L7-voyage, L7-jina, L7-openai

**Regulated-FS note.** Google Cloud EMEA Limited is a designated DORA CTPP and UK CTP [VF: A8-S020, A8-S023]; consuming the model through Vertex AI places it with a designated provider, which does not remove the firm's own outsourcing duties [AJ]. The 'eu' endpoint does not cover the UK [VF: A2-S039].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google (Google DeepMind / Google Cloud) | Verified fact | A2-S004 |
| Category | Hosted multimodal embedding model API | Verified fact | A2-S004, A2-S005 |
| Version / lineup | gemini-embedding-2: preview 10 March 2026 (gemini-embedding-2-preview), GA 22 April 2026; text-only gemini-embedding-001 remains available | Verified fact | A2-S004, A2-S005, A2-S039, V1-S073 |
| Licence | Proprietary; hosted API only (Gemini API and Vertex AI / Gemini Enterprise Agent Platform) | Verified fact | A2-S004 |
| Status events | 10 March 2026: gemini-embedding-2-preview released; 22 April 2026: gemini-embedding-2 GA on Gemini API and Vertex AI; 2026: Google Cloud documentation renames Vertex AI generative AI docs to 'Gemini Enterprise Agent Platform' | Verified fact | A2-S004, A2-S005, A2-S039 |
| Strategic direction | Google's first natively multimodal embedding model: text, images, video, audio and documents in one embedding space; positioned for agentic multimodal RAG; Gemini File Search API gained multimodal support | Verified fact | A2-S004, A2-S005 |
| What it does | Maps text, images (up to 6 per request), video, audio (no transcription step) and PDFs (up to 6 pages) into a shared vector space across 100+ languages; 8,192 text-token input; Matryoshka output 128-3,072 dims (3,072/1,536/768 recommended) with automatic normalisation; multiple inputs in one request produce one aggregated embedding; task_type parameter not supported. | Verified fact | A2-S004, A2-S005 |
| Stack position | L7 embedding model; placement correct. Also reached through Google platform services (File Search, Memory Bank), so it can be consumed implicitly inside higher layers. | Architectural judgement |  |
| Integration | Gemini API and Vertex AI SDK/REST; Batch API at 50% of standard price | Verified fact | A2-S005, A2-S038 |
| Dependencies | Google Gemini API or Google Cloud Vertex AI (Gemini Enterprise Agent Platform) | Verified fact | A2-S004, A2-S039 |
| Certifications | Generative AI on Vertex AI: SOC 2, ISO/IEC 27001, ISO/IEC 42001, HIPAA, FedRAMP High (scope per product/feature; per-model coverage for gemini-embedding-2 not confirmed) | Verified fact | A2-S043 |
| GDPR / residency | Available on the 'eu' multi-region endpoint, which keeps data within EU member states (UK and Switzerland excluded); batch supported in global, us and eu | Verified fact | A2-S039 |
| Security features | Vertex AI supports customer-managed encryption keys (CMEK) with location rules; applicability to gemini-embedding-2 calls not confirmed | Verified fact | A2-S039 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Gemini API paid tier per 1M tokens: text US$0.20, image US$0.45, audio US$6.50, video US$12.00; Batch: text US$0.10, image US$0.225, audio US$3.25, video US$6.00; free tier available. Vertex AI: text US$0.20 online / US$0.10 batch, image US$0.45 online. | Verified fact | A2-S038 |
| Infrastructure cost | Not applicable: hosted only | Architectural judgement |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Box is integrating Gemini Embedding 2 multimodal capabilities into the Box Agentic Platform (Google Cloud blog) | Verified fact | A2-S047 |
| Maturity | GA since 22 April 2026 (about 5.5 months) | Verified fact | A2-S004 |
| Deployment | saas: Yes (Gemini Developer API); managed_cloud: Yes (Google Cloud Vertex AI / Gemini Enterprise Agent Platform; global, us and eu endpoints); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No (no downloadable weights); on_prem: Not publicly verified | | |

## OpenAI embeddings: text-embedding-3-large and text-embedding-3-small (`L7-openai`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** OpenAI – Embeddings 3

*Rationale:* Competent, well-controlled text embeddings, but hosted-only, text-only and without a reranker; a baseline, not a foundation.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Core text embedding with shortening via 'dimensions'; no reranker, no multimodal, 2024 generation. |
| Enterprise readiness | 4 | SAML/OIDC SSO, tenant SCIM for the API Platform (from 17 September 2026), organisation and project roles with custom roles, Admin API and audit logs of administrative events [VF: B-REV-S004, B-REV-S005, B-REV-S006]; support/SLA terms not verified and audit logs exclude request content with best-effort retention, so not 5. |
| Security and compliance | 4 | SOC 2 Type 2, ISO 27001/27701, HIPAA BAA, ZDR and EU residency for the endpoint; CMK not verified. |
| Deployment flexibility | 2 | Hosted SaaS only, with US and EU processing regions; no VPC or self-host verified. |
| Ecosystem | 3 | Standard REST endpoint, SDKs and Batch API; broader ecosystem evidence NPV in the dataset. |
| Reliability and maturity | 4 | GA since January 2024 and unchanged for about 2.7 years. |
| Cost / TCO | 4 | Transparent per-token pricing at the low end of the hosted market; Batch halves 3-large. |
| Lock-in / portability | 2 | Proprietary hosted API, no weights; switching forces full re-embedding. |
| **Total (generic / FS)** | **3.30 / 3.20** | |

*Evidence rules applied:* NPV cap lifted at CP2 review (8 October 2026): SSO, RBAC and audit logs verified (B-REV-S004 to S006); Rules 7 and 8 checked at CP2 rework (8 October 2026): enterprise_readiness 4 and security_compliance 4 kept

**Capabilities.** Hosted text embeddings: text-embedding-3-large (3,072 dims by default, shortened with the 'dimensions' parameter) and text-embedding-3-small, 8,192-token input, released 25 January 2024 [VF: A2-S001, A2-S002]. No first-party reranker was found [VF: A2-S001].

**Strengths**

- Stable, unchanged generation since January 2024, so a pinned model has not been forced to move [VF: A2-S002] [AJ]
- Strong documented controls for the endpoint: SOC 2 Type 2, ISO/IEC 27001 and 27701, ZDR-eligible /v1/embeddings, EU storage and processing residency with Modified Abuse Monitoring or ZDR, HIPAA BAA [VF: A2-S036, A2-S144]
- Low, transparent price: 3-small US$0.02 and 3-large US$0.13 per 1M tokens, Batch at half price for 3-large (as of 7 October 2026) [VF: A2-S001, A2-S035]
- API Platform identity and access: SAML/OIDC SSO, SCIM, organisation and project roles with custom roles, Admin API and audit logs [VF: B-REV-S004, B-REV-S005, B-REV-S006]

**Limitations and risks**

- Text only; no reranker, so a second vendor or library is needed for two-stage retrieval [VF: A2-S001] [AJ]
- Hosted only, no downloadable weights; vectors are model-specific, so exit means re-embedding the corpus [AJ]
- UK region is storage-only for embeddings; processing in Europe needs Modified Abuse Monitoring or ZDR [VF: A2-S144]
- Audit logs record administrative events only, not request content, and are kept on a best-effort basis, so they must be exported to the firm's archive [VF: B-REV-S006]; CMK/BYOK not verified [NPV]
- Ageing generation with no announced successor; successor timing unknown [AJ]

**Choose when**

- OpenAI is already the contracted L1 provider with ZDR and EU residency approved, and the corpus is text-only
- A low-cost English or multilingual text baseline is needed for an in-domain bake-off

**Avoid when**

- Data must be processed in the UK or inside the firm's own estate
- Multimodal retrieval (scanned factsheets, charts) or a single-vendor embed-plus-rerank pair is required

**Nearest competitors:** L7-gemini-embedding, L7-cohere, L7-voyage

**Regulated-FS note.** Usable for EU-processed client data only under ZDR or Modified Abuse Monitoring on an EU project [VF: A2-S144]; UK processing is not offered for this endpoint [VF: A2-S144]. A direct OpenAI contract is an ICT third-party arrangement outside the DORA CTPP perimeter, so oversight sits with the firm [VF: A8-S021] [AJ].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | OpenAI | Verified fact | A2-S002 |
| Category | Hosted text-embedding model API | Verified fact | A2-S003 |
| Version / lineup | text-embedding-3-large (most capable; 3,072 dims default) and text-embedding-3-small, both released 25 January 2024; text-embedding-ada-002 still listed. No newer OpenAI embedding model found as of 7 October 2026. | Verified fact | A2-S001, A2-S002 |
| Licence | Proprietary; available only as a hosted API | Verified fact | A2-S001, A2-S003 |
| Status events | 25 January 2024: text-embedding-3-small/-large launched; ada-002 not deprecated at launch | Verified fact | A2-S002 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Converts text into dense vectors for search, clustering and recommendation. Output defaults to 3,072 dimensions for 3-large and can be shortened via the 'dimensions' parameter; maximum input 8,192 tokens. | Verified fact | A2-S001, A2-S003 |
| Stack position | L7 embedding model; placement in the graphic is correct. Embedding only (no first-party reranker found), so a separate reranker is needed for two-stage retrieval. | Architectural judgement |  |
| Integration | REST /v1/embeddings endpoint and OpenAI SDKs; Batch API at half the standard per-token price for 3-large | Verified fact | A2-S003, A2-S035 |
| Dependencies | OpenAI API platform (cloud service) | Verified fact | A2-S003 |
| Certifications | SOC 2 Type 2 (API and business products); ISO/IEC 27001:2022 and 27701:2019; CSA STAR Level 1; /v1/embeddings on HIPAA-eligible list with BAA and Modified Retention | Verified fact | A2-S036, A2-S144 |
| GDPR / residency | /v1/embeddings: Zero Data Retention eligible (prior approval); data residency per project - US and Europe support storage and processing (Europe requires Modified Abuse Monitoring or ZDR); UK, Australia, Canada, Japan, India, Singapore, South Korea storage only; Europe projects handle requests in-region with ZDR; DPA available | Verified fact | A2-S144, A2-S037 |
| Security features | AES-256 at rest, TLS 1.2+ in transit; customer API data not used for training by default. CMK/BYOK for the API not verified. | Verified fact | A2-S037 |
| Access controls | SSO/MFA advertised for the API platform; SCIM, RBAC granularity and audit-log scope not verified in this run | Verified fact | A2-S036 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | text-embedding-3-large US$0.13 per 1M tokens (Batch US$0.065); text-embedding-3-small US$0.02 per 1M tokens | Verified fact | A2-S001, A2-S035 |
| Infrastructure cost | Not applicable: hosted only; cost is per token | Architectural judgement |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GA since January 2024; no successor model announced in the ~2.7 years since | Verified fact | A2-S002, A2-S001 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No (no downloadable weights published); on_prem: No | | |

## Jina AI search foundation models (jina-embeddings-v5-text, jina-embeddings-v5-omni, jina-reranker-v3.5), part of Elastic (`L7-jina`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** Jina AI – Embeddings v3

*Rationale:* Natural choice inside Elastic estates; non-commercial weights and an opaque price list make it a poor neutral default.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Multilingual, multimodal, long-context embeddings and listwise and multimodal rerankers. |
| Enterprise readiness | 3 | Scored on the recommended Elastic Inference Service route: Elastic Cloud SAML SSO and RBAC at platform level [VF: B-REV-S019]; audit logging of EIS calls not evidenced. The standalone Jina API (API keys only) would stay capped at 2. |
| Security and compliance | 3 | Elastic Cloud SOC 2 Type II and ISO 27001 cover the EIS route; hosted Jina API scope unconfirmed. |
| Deployment flexibility | 4 | SaaS API, Elastic Inference Service, on-prem Docker with air-gap; VPC NPV. |
| Ecosystem | 4 | Default in Elasticsearch semantic_text; Hugging Face and vLLM recipes. |
| Reliability and maturity | 3 | Three releases in February-July 2026; ownership changed October 2025. |
| Cost / TCO | 2 | API rates not retrieved, on-prem by quote, CC-BY-NC weights: opaque for planning. |
| Lock-in / portability | 2 | CC-BY-NC weights route commercial use through Elastic (would be 3); reduced by 1 for the 2025 acquisition. |
| **Total (generic / FS)** | **3.30 / 3.15** | |

*Evidence rules applied:* NPV cap lifted at CP2 review for the Elastic Inference Service route (B-REV-S019); the standalone Jina API remains capped at 2 (API keys only); Rule 7 (CP2 Q2) checked at CP2 rework: SSO and RBAC verified on Elastic Cloud, audit logging of EIS calls not evidenced, so 3 kept; rule 8 (CP2 Q4) confirmed for security 3 (Elastic Cloud certifications, Jina API scope unconfirmed)

**Capabilities.** Jina AI, part of Elastic since 9 October 2025 [VF: A2-S023, V1-S025]: jina-embeddings-v5-text (February 2026; 32,768-token context, 1,024 dims), v5-omni (May 2026; text, image, audio, video, PDF, with text vectors identical to v5-text), jina-reranker-v3.5 (July 2026, listwise) and jina-reranker-m0 (multimodal) [VF: A2-S025, A2-S026, V1-S026].

**Strengths**

- Default embedding model behind Elasticsearch semantic_text, so it is the low-effort path for Elastic estates [VF: A2-S133]
- Commercial on-premises licence with Docker containers and air-gapped deployment [VF: A2-S042, A2-S045]
- v5-omni text vectors match v5-text, so adding modalities need not force text re-embedding [VF: A2-S025]

**Limitations and risks**

- Weights are CC-BY-NC-4.0: commercial self-hosting needs the Jina API, a marketplace, Elastic Inference Service or an on-prem licence [VF: A2-S024, A2-S042]
- Acquired by Elastic (October 2025); Jina's own policies predate the acquisition [VF: A2-S023, A2-S024]
- Hosted Jina API SOC 2 scope not confirmed; Elastic Cloud holds ISO 27001/27017/27018 and SOC 2 Type II [VF: A2-S045]
- API per-token rates not retrieved; on-prem licence priced via sales [VF: A2-S042]
- Vendor-reported 63.20 nDCG@10 on BEIR is not a decision input [R: A2-S026]

**Choose when**

- Elasticsearch is the L6 store and the firm wants embedding and reranking inside the same platform
- Air-gapped multimodal retrieval is needed under a commercial licence

**Avoid when**

- The plan assumes free commercial self-hosting of the weights
- Store and embedding vendor must be independent for concentration reasons

**Nearest competitors:** L7-voyage, L7-cohere, L7-qwen3-embedding, L7-sentence-transformers

**Regulated-FS note.** Data processing is now under Elastic's terms; region details for the hosted API not verified [VF: A2-S024]. Confirm the licence route in writing before any self-hosted production use [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Jina AI GmbH, acquired by Elastic N.V. (completed October 2025) | Verified fact | A2-S023, A2-S024 |
| Category | Embedding and reranking models (hosted API, Elastic Inference Service, on-prem licence, open weights for non-commercial use) | Verified fact | A2-S042, A2-S024 |
| Version / lineup | jina-embeddings-v5-text small (677M params, 32,768-token context, 1,024 dims) and nano (239M) - February 2026; jina-embeddings-v5-omni small and nano - May 2026 (default API embedding model); jina-reranker-v3.5 (0.6B listwise) - July 2026; jina-reranker-m0 (multimodal) also listed | Verified fact | A2-S025, A2-S026, V1-S026 |
| Licence | Model weights CC-BY-NC-4.0 (commercial use via Jina API, cloud marketplaces, Elastic Inference Service or on-prem licence); jina-embeddings-v4 under Qwen Research Licence (no commercial use) | Verified fact | A2-S024, A2-S042, V1-S026 |
| Status events | 9 October 2025: Elastic completes acquisition of Jina AI (IR release); February 2026: jina-embeddings-v5-text; May 2026: jina-embeddings-v5-omni; June 2026: v5-omni small/nano available on Elastic Inference Service; July 2026: jina-reranker-v3.5 | Verified fact | A2-S023, A2-S025, A2-S027, A2-S026, V1-S025 |
| Strategic direction | Being integrated into Elastic: Jina models served on Elastic Inference Service alongside ELSER; rerankers for visual and long-context multilingual documents | Verified fact | A2-S023, A2-S027, A2-S042 |
| What it does | Multilingual and multimodal embedding models (text, image, audio, video, PDF in one space) and listwise rerankers; v3.5 reranker reports 63.20 nDCG@10 on BEIR and up to 1.56x faster than v3 on long documents (vendor-reported). | Verified fact | A2-S025, A2-S026 |
| Stack position | L7 embed + rerank; now also a native component of Elasticsearch (L6) via Elastic Inference Service. | Architectural judgement |  |
| Integration | Jina Embedding and Reranker APIs (token-billed); Elasticsearch open inference API / EIS; Hugging Face weights; vLLM recipes | Verified fact | A2-S042, A2-S025 |
| Dependencies | Jina hosted API; or Elastic Cloud (EIS); or Docker containers on customer infrastructure (on-prem licence) | Verified fact | A2-S042, A2-S045 |
| Certifications | Elastic Cloud: ISO 27001, ISO 27017, ISO 27018, SOC 2 Type II; coverage of the hosted Jina API not confirmed | Verified fact | A2-S045 |
| GDPR / residency | Jina data processing now governed by Elastic's data processing terms; region details not verified | Verified fact | A2-S024 |
| Security features | Customer data encrypted in transit and at rest with per-customer keys; request data not used for training (Jina legal page) | Verified fact | A2-S045 |
| Access controls | API-key access managed by customer; other controls not verified | Verified fact | A2-S045 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Jina API billed per token processed (rates not retrieved); EIS billed per million input tokens on Elastic Cloud; on-prem annual licence via Elastic Sales. Rate limits: Free 100 RPM/100K TPM, Paid 500 RPM/2M TPM, Premium 5,000 RPM/50M TPM. | Verified fact | A2-S042 |
| Infrastructure cost | On-prem licence priced by models deployed and inference hardware, not per token | Verified fact | A2-S042 |
| Ecosystem | Elasticsearch integration via open inference API and EIS; Hugging Face; vLLM | Verified fact | A2-S042, A2-S025 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Rapid cadence: three model releases in Feb-Jul 2026 after acquisition | Verified fact | A2-S025, A2-S026 |
| Deployment | saas: Yes (Jina API); managed_cloud: Yes (Elastic Inference Service on Elastic Cloud; cloud marketplaces); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (commercial on-prem licence; Docker containers, air-gapped supported); on_prem: Yes | | |

## Qwen3-Embedding and Qwen3-Reranker (open weights); Qwen3-VL-Embedding / Qwen3-VL-Reranker (multimodal); hosted as text-embedding-v4 and qwen3-rerank on Alibaba Cloud Model Studio (`L7-qwen3-embedding`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Qwen3 – Embeddings

*Rationale:* Capable Apache 2.0 embed-plus-rerank pair for self-hosting; usable only after provenance review and with in-house operations.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Embed and rerank in three sizes, 32K context, 119 languages, multimodal VL variants. |
| Enterprise readiness | 2 | Rule 2 (self-hosted open weights; hosted Model Studio route not recommended): enables in-estate serving only; no commercial support for self-hosting verified, so 2. |
| Security and compliance | 2 | Rule 2: Apache-2.0 licence is clear, but no security policy or signed-release evidence was verified and a model-provenance review is outstanding, so 2; inherits host controls. |
| Deployment flexibility | 4 | Self-host, on-prem and disconnected use via open weights, plus SaaS outside the EU. |
| Ecosystem | 3 | Hugging Face and ModelScope weights; OpenAI-compatible batch API on Model Studio; wider ecosystem NPV. |
| Reliability and maturity | 3 | Released June 2025 with a January 2026 multimodal successor; long-term support NPV. |
| Cost / TCO | 4 | Free weights; cost is GPU and operations, light for 0.6B, heavier for 8B. |
| Lock-in / portability | 4 | Apache 2.0 and self-hostable; single-vendor governance and model-specific vectors keep it below 5. |
| **Total (generic / FS)** | **3.20 / 3.15** | |

*Evidence rules applied:* Rule 2 (self-hosted open weights) applied instead of the NPV cap, because the recommendation is self-host only; scores unchanged at 2 on project hygiene and support, not on missing hosted certifications; Rule 7 (CP2 Q2) checked at CP2 rework: no SSO, RBAC or audit control verified; rule 2 scores kept

**Capabilities.** Open-weight Qwen3-Embedding and Qwen3-Reranker in 0.6B, 4B and 8B (June 2025; 32K context; 119 languages; Apache 2.0) and Qwen3-VL-Embedding/-Reranker (January 2026) [VF: A2-S020, A2-S021, V1-S093]. Hosted as text-embedding-v4 (64-2,048 dims) and qwen3-rerank on Alibaba Cloud Model Studio [VF: A2-S022].

**Strengths**

- Apache 2.0 embed and rerank pair that can run fully inside the firm's estate, including disconnected environments [VF: A2-S020] [AJ]
- Three sizes allow a cost/quality trade-off; 0.6B runs on modest hardware [AJ]
- Multimodal successors (VL) in the same family [VF: A2-S021]

**Limitations and risks**

- Chinese-origin model; FS firms will require provenance and supply-chain review before use [AJ]
- Hosted Model Studio regions are Singapore, Hong Kong and Beijing; no EU region verified [VF: A2-S022]
- No commercial support or certifications verified [NPV]; Qwen3-VL embedding licence not verified [NPV]
- MTEB No.1 claim dates from 5 June 2025 and is vendor-reported; current rank not verified [R: A2-S020]
- Self-hosting the 8B models needs datacentre GPUs and an in-house serving team [AJ]

**Choose when**

- A self-hosted, permissively licensed embed-plus-rerank pair is required and provenance review approves it
- Multilingual corpora need in-estate processing at low marginal cost

**Avoid when**

- Policy excludes Chinese-origin model weights, or only the hosted API would be used
- There is no capacity to operate GPU inference

**Nearest competitors:** L7-sentence-transformers, L7-nvidia-nemo-retriever, L7-jina, L7-voyage

**Regulated-FS note.** Self-hosted weights keep client data in the firm's estate; the hosted API is not a fit for EU/UK client data on verified regions [VF: A2-S022]. Hosted prices come from Alibaba's own pricing page [VF: A2-S022], but the hosted route is not the recommended one for client data, so they are not a decision input [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Alibaba Group (Qwen team; Alibaba Cloud) | Verified fact | A2-S020, A2-S022 |
| Category | Open-weight embedding and reranking models, also offered as hosted API | Verified fact | A2-S020, A2-S022 |
| Version / lineup | Qwen3-Embedding and Qwen3-Reranker in 0.6B, 4B and 8B (June 2025; 32K context; 119 languages); Qwen3-VL-Embedding and Qwen3-VL-Reranker (January 2026); hosted text-embedding-v4, qwen3.7-text-embedding, qwen3-rerank, qwen3-vl-rerank | Verified fact | A2-S020, A2-S021, A2-S022 |
| Licence | Open weights, Apache 2.0 (Qwen3-Embedding/Reranker); hosted API proprietary service | Verified fact | A2-S020 |
| Status events | June 2025: Qwen3-Embedding and Qwen3-Reranker released (Apache 2.0); January 2026 (paper 8 January 2026): Qwen3-VL-Embedding and Qwen3-VL-Reranker (2B and 8B) released | Verified fact | A2-S020, A2-S021, V1-S093 |
| Strategic direction | Extending to multimodal retrieval (Qwen3-VL-Embedding/Reranker) and newer hosted embedding versions (qwen3.7-text-embedding, 201 languages) | Verified fact | A2-S021, A2-S022 |
| What it does | Text embedding and reranking models built on Qwen3 foundation models; hosted text-embedding-v4 supports 64-2,048 dims (1,024 default). | Verified fact | A2-S020, A2-S022 |
| Stack position | L7; family covers both embed and rerank, so the graphic understates it. | Architectural judgement |  |
| Integration | Hugging Face / ModelScope weights; Model Studio API including OpenAI-compatible batch API | Verified fact | A2-S020, A2-S022 |
| Dependencies | Self-host on GPU/CPU from Hugging Face/ModelScope weights, or Alibaba Cloud Model Studio | Verified fact | A2-S020, A2-S022 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Model Studio pricing lists Singapore, Hong Kong and Beijing regions; no EU region verified | Verified fact | A2-S022 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Model Studio: text-embedding-v4 US$0.07 per 1M tokens (Singapore; US$0.072 Beijing); qwen3.7-text-embedding US$0.07 (Singapore); qwen3-rerank US$0.10 per 1M input tokens (Singapore), output free; 1M free tokens for 90 days. Open weights free. | Verified fact | A2-S022 |
| Infrastructure cost | Self-hosting cost driven by GPU size: 0.6B runs on modest hardware; 8B needs a datacentre GPU for production throughput | Architectural judgement |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | 8B embedding ranked No.1 on MTEB multilingual (score 70.58) as of 5 June 2025 (vendor-reported); Jina reports its v3.5 reranker beating Qwen3-Reranker-4B on BEIR | Verified fact | A2-S020, A2-S026 |
| Maturity | Open-weight release June 2025; multimodal successor January 2026 | Verified fact | A2-S020, A2-S021 |
| Deployment | saas: Yes (Alibaba Cloud Model Studio); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open weights); on_prem: Yes (open weights) | | |

## Voyage AI by MongoDB (Voyage 4 embedding family; Rerank 3 rerankers) (`L7-voyage`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** Voyage AI – Voyage-3

*Rationale:* Technically the deepest lineup, but certifications are unverified, key APIs are in preview and ownership now couples it to MongoDB.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading breadth in primary docs: domain, contextual, multimodal, shared space, quantisation and rerankers. |
| Enterprise readiness | 3 | Scored on the Atlas route recommended for MongoDB estates: Voyage model API keys are governed by Atlas organisation and project roles (Organization Owner, Project Owner, Project Model Owner and read-only roles), with an Admin API endpoint for model keys [VF: B-REV-S028]. One verified control lifts the NPV cap to 3 under rule 7 (CP2 Q2); SSO and audit logging of model-key use are not stated. The AWS Marketplace in-VPC route (A2-S044) would score 4 under rule 6 (CP2 Q1). |
| Security and compliance | 2 | SOC 2/HIPAA appear only as a reported homepage listing; trust-portal scope unverified. |
| Deployment flexibility | 3 | SaaS, Atlas, AWS/Azure marketplaces and in-VPC SageMaker; only nano is self-hostable. |
| Ecosystem | 4 | Native in MongoDB, on AWS and Azure marketplaces; listed in Anthropic's embeddings docs (author conflict noted). |
| Reliability and maturity | 3 | Frequent generations; MongoDB-integrated APIs and rerank-3 in preview; ownership changed in February 2025. |
| Cost / TCO | 4 | Transparent, low per-token pricing with a large free allowance. |
| Lock-in / portability | 2 | Proprietary API (except nano) on standard interfaces would be 3; reduced by 1 for the 2025 acquisition. |
| **Total (generic / FS)** | **3.40 / 3.05** | |

*Evidence rules applied:* NPV cap on enterprise_readiness lifted at CP2 rework (8 October 2026) under rule 7 (CP2 Q2): Atlas organisation and project roles govern model API keys (B-REV-S028); SSO and audit logging for key use not stated, so 3; security_compliance capped at 2 (kept): certifications only Reported from a homepage listing; MongoDB's SOC 2 scope page does not name Voyage and excludes preview features (B-REV-S027)

**Capabilities.** Voyage AI by MongoDB: Voyage 4 family (voyage-4-large, voyage-4, voyage-4-lite, open-weight voyage-4-nano) in one shared embedding space; voyage-code-4, voyage-context-4 (contextualised chunks), voyage-multimodal-3.5, domain models voyage-finance-2 and voyage-law-2; rerank-3 and rerank-3-lite (30 September 2026) with 32K-token context [VF: A2-S006, A2-S007, A2-S034]. rerank-3 is listed as Preview on MongoDB's model lifecycle page [VF: V1-S024].

**Strengths**

- Broadest lineup against this layer's research questions: domain (finance), contextual, code, multimodal, quantisation including binary, and instruction-following rerankers [VF: A2-S006, A2-S007, A2-S034]
- Shared Voyage 4 space lets a team index with a large model and query with a small one without re-embedding [VF: A2-S006]
- Low published prices: voyage-4 US$0.06 per 1M tokens with 200M free tokens per model; rerank-3 US$0.05, rerank-3-lite US$0.02 per 1M tokens (as of 7 October 2026) [VF: A2-S007, A2-S034]
- In-VPC route via the AWS Marketplace model package in the customer's account [VF: A2-S044]

**Limitations and risks**

- Acquired by MongoDB (closed 17 February 2025) [VF: A2-S033, V1-S023]; roadmap now tied to MongoDB [AJ]
- Certifications rest on a homepage listing; trust-portal report scope not verified [R: A2-S044]; MongoDB points standalone Voyage to a separate trust portal [VF: A2-S138]
- rerank-3 is Preview on MongoDB's lifecycle page; Atlas Embedding and Reranking API and Automated Embedding are public preview [VF: V1-S024, A2-S077, A2-S078]
- Only voyage-4-nano can be self-hosted [VF: A2-S071]
- Vendor claims that rerank-3 beats competitors are not decision inputs [R: A2-S141]
- Atlas roles govern who can create, edit or delete model API keys [VF: B-REV-S028], but SSO and audit logging of key use are not stated [NPV]

**Choose when**

- MongoDB is the L6 store, or the firm accepts MongoDB as a strategic supplier
- Finance-domain vocabulary and contextualised chunks matter, subject to in-domain evaluation
- EU processing via the Atlas Europe Geography is acceptable

**Avoid when**

- UK processing or on-premises hosting of the main models is mandatory
- Independence between the retrieval-store vendor and the embedding vendor is a concentration requirement

**Nearest competitors:** L7-cohere, L7-jina, L7-qwen3-embedding, L7-openai

**Regulated-FS note.** The Atlas Embedding and Reranking API offers an EEA Geography with no fallback outside it, at a 10% premium [VF: A2-S142]; Automated Embedding and Native Reranking do not yet support Geography targeting [VF: A2-S142]. Request the Voyage SOC 2 report and its scope before use with client data [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Voyage AI, acquired by MongoDB, Inc. (closed 17 February 2025) | Verified fact | A2-S033 |
| Category | Embedding and reranking models (hosted API, marketplace model packages, one open-weight model) | Verified fact | A2-S007, A2-S044 |
| Version / lineup | Voyage 4 (launched 15 January 2026): voyage-4-large, voyage-4, voyage-4-lite, voyage-4-nano (open weights); plus voyage-code-4, voyage-context-4 (contextualised chunk embeddings), voyage-multimodal-3.5 (text, image, video); domain models voyage-finance-2 and voyage-law-2. Rerankers: rerank-3 and rerank-3-lite (announced 30 September 2026; MongoDB model-lifecycle page lists them as Preview), rerank-2.5 series retained for existing users. | Verified fact | A2-S006, A2-S007, A2-S034, A2-S071, V1-S024 |
| Licence | Proprietary hosted models; voyage-4-nano is open-weight under Apache 2.0 | Verified fact | A2-S006, A2-S071 |
| Status events | 17 February 2025: acquired by MongoDB (announced 24 February 2025); August 2025: rerank-2.5 / rerank-2.5-lite with instruction following; 15 January 2026: Voyage 4 family launched; Voyage 3.x becomes previous generation; 30 September 2026: rerank-3 / rerank-3-lite launched; rerank-2.5 becomes previous generation | Verified fact | A2-S033, A2-S006, A2-S034, V1-S023, V1-S024 |
| Strategic direction | Being folded into MongoDB: Embedding and Reranking API on Atlas (public preview) and Automated Embedding in MongoDB Vector Search (public preview on Community Edition; Atlas 'coming soon' as of January 2026). Voyage 4 models share one embedding space so documents and queries can use different model sizes. | Verified fact | A2-S008, A2-S077, A2-S078, A2-S006 |
| What it does | General-purpose, code, domain-specific, contextualised and multimodal embedding models plus instruction-following rerankers (32K-token context). voyage-4: 32,000-token context, 1,024 default dims (256/512/2,048 options), multiple quantisation options including binary. | Verified fact | A2-S007, A2-S006, A2-S034 |
| Stack position | L7, covering both embedding and reranking; increasingly also embedded inside L6 (MongoDB Vector Search automated embedding). | Architectural judgement |  |
| Integration | REST API and SDKs; Atlas Embedding and Reranking API; AWS and Azure Marketplace; automated embedding inside MongoDB Vector Search | Verified fact | A2-S033, A2-S077, A2-S078 |
| Dependencies | Voyage/MongoDB hosted API, or AWS SageMaker (GPU instances such as ml.g5.xlarge) for marketplace model packages; voyage-4-nano runs anywhere (Hugging Face weights) | Verified fact | A2-S044, A2-S071 |
| Certifications | SOC 2 and HIPAA listed in Voyage AI homepage/terms; MongoDB Trust Portal refers standalone Voyage to a separate VoyageAI Trust Portal (report scope not verified) | Reported | A2-S044, A2-S143, A2-S138 |
| GDPR / residency | Atlas Embedding and Reranking API: Europe Geography (EEA regions) and US Geography processing boundaries, no fallback outside the Geography, 10% price premium (announced 1 September 2026, public preview at launch); Voyage-hosted API: opt-out of training gives zero-day retention | Verified fact | A2-S142, A2-S143 |
| Security features | In-VPC marketplace deployment keeps data flow and API access in the customer's account (AWS acts as sub-processor) | Verified fact | A2-S044 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | voyage-4 US$0.06 per 1M tokens, first 200M tokens free per model; rerank-3 US$0.05 and rerank-3-lite US$0.02 per 1M tokens | Verified fact | A2-S007, A2-S034 |
| Infrastructure cost | Marketplace self-deployment requires SageMaker GPU instances (e.g. ml.g5.xlarge); default quotas are often zero | Verified fact | A2-S044 |
| Ecosystem | Recommended in Anthropic's Claude embeddings documentation; available via AWS and Azure marketplaces; native in MongoDB | Verified fact | A2-S071, A2-S033, A2-S078 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Frequent model generations (rerank-2.5 Aug 2025, Voyage 4 Jan 2026, rerank-3 Sep 2026); MongoDB-integrated APIs still in public preview | Verified fact | A2-S034, A2-S006, A2-S077 |
| Deployment | saas: Yes; managed_cloud: Yes (AWS Marketplace, Azure Marketplace, MongoDB Atlas); vpc_byoc: Yes (model package deployed in the customer's AWS account and VPC via SageMaker); private_cloud: Not publicly verified; self_hosted: Partial (voyage-4-nano open weights only); on_prem: Not publicly verified | | |

## NVIDIA NeMo Retriever embedding and reranking NIM microservices (Nemotron embedding/reranking models) (`L7-nvidia-nemo-retriever`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** NVIDIA – Embed

*Rationale:* Sound self-hosted runtime for NVIDIA-standardised estates; licence cost and GPU coupling make it a poor neutral default.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Embed and rerank including multimodal; shorter context and fixed dimensions; Matryoshka not evidenced. |
| Enterprise readiness | 3 | Commercial subscription with Helm/Kubernetes deployment; inherits host IAM; support terms NPV. |
| Security and compliance | 3 | Self-hosted container (certifications not applicable); licence clear; container hardening evidence NPV. |
| Deployment flexibility | 4 | Any cloud or data centre with supported GPUs, NVIDIA API Catalog for development; air-gap NPV. |
| Ecosystem | 3 | NeMo Retriever pipeline and Helm chart; wider ecosystem NPV. |
| Reliability and maturity | 3 | Frequent NIM releases; inconsistent version dating across pages. |
| Cost / TCO | 2 | Per-GPU licence on top of GPU infrastructure. |
| Lock-in / portability | 2 | Tied to NVIDIA GPUs and the AI Enterprise licence; per-model licences vary. |
| **Total (generic / FS)** | **3.00 / 2.95** | |

*Evidence rules applied:* NPV cap not applied to security_compliance: self-hosted container, vendor certifications not applicable; scored on in-estate deployment and licence clarity; Rule 6 (CP2 Q1) not applied at CP2 rework: no hyperscaler-consumed route is in the fact base; scores kept

**Capabilities.** NVIDIA NeMo Retriever embedding and reranking NIM microservices: Embedding NIM 2.3 (nemotron-3-embed-1b added in 2.2; llama-nemotron-embed-1b-v2; llama-nemotron-embed-vl-1b-v2) and Reranking NIM 2.0.0 (llama-nemotron-rerank-vl-1b-v2, rerank-1b-v2, rerank-500m-v2), deployed by Helm on Kubernetes or Docker [VF: A2-S030, A2-S031, V1-S094].

**Strengths**

- Embed and rerank, text and multimodal, as GPU-optimised containers that run in any cloud or data centre with supported GPUs [VF: A2-S031, A2-S040]
- Client data stays in the firm's environment when self-hosted [AJ]
- Fits estates that already standardise on NVIDIA AI Enterprise for L2 serving [AJ]

**Limitations and risks**

- Production use requires NVIDIA AI Enterprise, from US$4,500 per GPU per year or about US$1 per GPU per hour in cloud (as of 7 October 2026) [VF: A2-S040]
- Two-layer licensing (container agreement plus per-model licences that vary) [VF: A2-S041]
- Shorter limits than API peers: nemotron-3-embed-1b is text-only, fixed 2,048 dims, 4,096-token maximum [VF: V1-S094, A2-S031]
- Helm chart warns that a text-only reranker silently degrades multimodal reranking [VF: A2-S031]
- Release dates inconsistent across NGC and Hugging Face pages; container security features NPV

**Choose when**

- The firm already licenses NVIDIA AI Enterprise and runs GPU Kubernetes
- A vendor-supported, self-hosted embed-plus-rerank runtime is required

**Avoid when**

- Retrieval volumes do not justify per-GPU licences
- The firm wants to avoid deepening GPU-vendor concentration

**Nearest competitors:** L7-sentence-transformers, L7-qwen3-embedding, L7-cohere

**Regulated-FS note.** Self-hosting removes cross-border transfer questions for the retrieval path [AJ]; the AI Enterprise subscription becomes the third-party arrangement to register [AJ].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | NVIDIA | Verified fact | A2-S030 |
| Category | Containerised embedding and reranking inference microservices (NIM) with NVIDIA models | Verified fact | A2-S031, A2-S040 |
| Version / lineup | Embedding NIM 2.3: nemotron-3-embed-1b, llama-nemotron-embed-1b-v2, llama-nemotron-embed-vl-1b-v2 (multimodal). Reranking NIM 2.0.0: llama-nemotron-rerank-vl-1b-v2 (multimodal, NGC update 3 August 2026), llama-nemotron-rerank-1b-v2, llama-nemotron-rerank-500m-v2 (8,192-token max). | Verified fact | A2-S031, A2-S030 |
| Licence | Proprietary container (NVIDIA Software License Agreement + AI product terms); models under NVIDIA Open Model License (varies by model); production use requires NVIDIA AI Enterprise | Verified fact | A2-S041, A2-S040 |
| Status events | Reranking NIM 1.11.0: multimodal reranker llama-nemotron-rerank-vl-1b-v2 introduced; Reranking NIM 2.0.0: major runtime upgrade; Embedding NIM 2.2: nemotron-3-embed-1b added (text-only, fixed 2,048 dims, 4,096-token max); NIM 2.3 current | Verified fact | A2-S030, A2-S031, V1-S094 |
| Strategic direction | Moving to multimodal (text + image) embedding and reranking as defaults in the NeMo Retriever Helm chart | Verified fact | A2-S031, A2-S030 |
| What it does | GPU-optimised microservices that serve NVIDIA embedding and reranking models behind an API, deployable via Helm on Kubernetes or Docker, as part of the NeMo Retriever RAG pipeline. | Verified fact | A2-S031, A2-S030 |
| Stack position | L7 runtime + models (embed and rerank) - straddles L7 and L2 (serving). Graphic label 'Embed' understates the reranking component. | Architectural judgement |  |
| Integration | NIM REST APIs; NVIDIA API catalog Retrieval APIs for hosted trial; Helm chart | Verified fact | A2-S031 |
| Dependencies | NVIDIA GPUs; NGC container registry; Kubernetes/Helm for the NeMo Retriever chart | Verified fact | A2-S031 |
| Certifications | Not applicable to self-hosted containers; NVIDIA-hosted service certifications not researched | Architectural judgement |  |
| GDPR / residency | Runs in customer environment when self-hosted | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free for research/development/test via NVIDIA Developer Program (up to 16 GPUs); production requires NVIDIA AI Enterprise from US$4,500 per GPU per year or ~US$1 per GPU per hour in cloud; 90-day trial | Verified fact | A2-S040 |
| Infrastructure cost | GPU-bound: licence is per GPU plus GPU infrastructure | Verified fact | A2-S040 |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Frequent releases (NIM 2.x; Helm 26.08.1 recommended) | Verified fact | A2-S031 |
| Deployment | saas: Yes for development (NVIDIA API catalog); partner-hosted serverless NIM for production; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (any cloud or data centre with supported GPUs); on_prem: Yes | | |

## Not publicly verified (`L7-ethicalagents`)

**Tier:** Not scored · **Flags:** Not publicly verified · **Original graphic label:** EthicalAgents – embeddings

*Rationale:* Could not be verified; removed per CP1 Q4(a).

**Capabilities.** Not publicly verified: no product of this name found after six searches by Stage A and a fresh search by the verifier [VF: A2-S079, V1-S036].

**Limitations and risks**

- No evidence the product exists [NPV]

**Avoid when**

- Do not select: removed per CP1 decision Q4(a)

**Regulated-FS note.** Removed from the analysis per CP1 decision Q4(a).

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Not publicly verified | Not publicly verified |  |
| Category | Not publicly verified | Not publicly verified |  |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Not publicly verified | Not publicly verified |  |
| Stack position | Not publicly verified | Not publicly verified |  |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Not publicly verified (`L7-ragoos`)

**Tier:** Not scored · **Flags:** Not publicly verified · **Original graphic label:** Ragoos – RAG re-rankers

*Rationale:* Could not be verified; removed per CP1 Q4(a).

**Capabilities.** Not publicly verified: no product of this name found after six searches by Stage A and a fresh search by the verifier [VF: A2-S080, V1-S036].

**Limitations and risks**

- No evidence the product exists [NPV]

**Avoid when**

- Do not select: removed per CP1 decision Q4(a)

**Regulated-FS note.** Removed from the analysis per CP1 decision Q4(a).

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Not publicly verified | Not publicly verified |  |
| Category | Not publicly verified | Not publicly verified |  |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Not publicly verified | Not publicly verified |  |
| Stack position | Not publicly verified | Not publicly verified |  |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

# L6: Retrieval and knowledge stores

## Elasticsearch (Elastic Search AI Platform) (`L6-elasticsearch`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Elasticsearch – hybrid search

*Rationale:* Strategic, conditional: where Elastic is already operated, because cost scores 2 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | BM25, quantised vectors, RRF/linear fusion, restrictive-filter optimisation and document-level security cover the layer's research questions |
| Enterprise readiness | 4 | SAML/OIDC SSO, RBAC, DLS/FLS and audit logging (A2-S134; Elastic Cloud SSO/RBAC B-REV-S019), plus the Elastic Cloud API with role-bearing organisation API keys (B-REVA-S003): rule 7 allows 4; SCIM not found, Cloud audit tier and SLA not confirmed |
| Security and compliance | 5 | Elastic Cloud ISO 27001 and SOC 2 Type II within the product, plus CMK |
| Deployment flexibility | 4 | Hosted and Serverless on three clouds, self-managed and on-prem; no BYOC evidenced |
| Ecosystem | 5 | De-facto search standard; REST; OpenSearch fork |
| Reliability and maturity | 5 | Years of production use; frequent minors |
| Cost / TCO | 2 | Paid tiers for key security features; cluster pricing not verified; operations heavy |
| Lock-in / portability | 3 | AGPL option but paid features proprietary; SSPL/ELv2 alternatives (rule 4) |
| **Total (generic / FS)** | **4.30 / 4.25** | |

**Capabilities.** Distributed search engine combining BM25, dense/sparse vectors (BBQ/DiskBBQ default since 9.1), RRF and linear hybrid retrievers, semantic_text auto-embedding (Jina v5 default) and document-level security; Elastic 9.5 GA 4 August 2026 [VF: A2-S133, A2-S134, V1-S085].

**Strengths**

- Mature lexical plus vector and hybrid retrieval in one engine [VF: A2-S133] [AJ]
- Field- and document-level security maps to entitlement-aware retrieval [VF: A2-S134]
- Elastic Cloud ISO 27001/27017/27018, SOC 2 Type II; CMK on Hosted Enterprise; Private Link incl. London [VF: A2-S045, A2-S134]
- AGPLv3 option and OpenSearch fork as exit routes [VF: A2-S132, A2-S136]

**Limitations and risks**

- Security features in paid tiers (Platinum/Enterprise) [VF: A2-S134]
- Cluster pricing not verified; heavy operations when self-managed [NPV] [AJ]
- Bundled Jina embedding couples L6 and L7 [VF: A2-S023]
- VectorDB index mode only in technical preview [VF: V1-S085]

**Choose when**

- Elastic or OpenSearch is already an operated platform, or the corpus is lexical-heavy [AJ]

**Avoid when**

- It would be introduced only for vectors with no search team [AJ]

**Nearest competitors:** L6-mongodb-atlas-vector-search, L6-weaviate, OpenSearch (no record)

**Regulated-FS note.** Use document-level security for entitlements; pin the semantic_text model; choose AGPL distribution only after legal review [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Elastic N.V. (NYSE: ESTC) | Verified fact | A2-S023 |
| Category | Search engine with full-text (BM25), vector and hybrid retrieval; general-purpose search platform | Verified fact | A2-S023, A2-S042 |
| Version / lineup | Elastic Stack 9.5 (GA 4 August 2026; patch 9.5.4); Python client 9.5.1 (9 September 2026) | Verified fact | A2-S133, A2-S057, V1-S085 |
| Licence | Source: triple licence - AGPLv3 (OSI open source, added 2024; core under AGPL since 8.16), SSPL 1.0 or Elastic License 2.0; paid features proprietary; clients Apache-2.0 | Verified fact | A2-S132 |
| Status events | 9 October 2025: Elastic completes acquisition of Jina AI; June 2026: jina-embeddings-v5-omni on Elastic Inference Service | Verified fact | A2-S023, A2-S027, V1-S025 |
| Strategic direction | 'Search AI Company': acquired Jina AI for multimodal/multilingual embeddings and rerankers complementing ELSER; Elastic Inference Service hosts Jina v5-omni models | Verified fact | A2-S023, A2-S027, A2-S042 |
| What it does | Distributed search engine combining BM25, dense/sparse vectors (BBQ/DiskBBQ quantisation, default since 9.1) and hybrid retrievers (RRF, linear with l2_norm), semantic_text fields with automatic chunking and embedding (default Jina v5), MMR diversification; 9.5 adds VectorDB index mode (preview) and multimodal semantic field (preview). | Verified fact | A2-S133, A2-S042, A2-S023 |
| Stack position | L6 retrieval store with built-in L7 inference; a 'retrieval/knowledge store' rather than a pure vector DB. | Architectural judgement |  |
| Integration | REST API, official language clients (e.g. Python 9.5.1), open inference API, Elastic Inference Service | Verified fact | A2-S057, A2-S042 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Elastic Cloud: ISO 27001, ISO 27017, ISO 27018, SOC 2 Type II (report via Trust Center) | Verified fact | A2-S045 |
| GDPR / residency | EU/UK hosted regions: AWS Frankfurt, Zurich, Stockholm, Milan, Ireland, London, Paris; GCP Finland, Belgium, London, Frankfurt, Netherlands, Paris; Azure Ireland, UK South, Netherlands; Serverless in AWS Frankfurt, Ireland, London and others | Verified fact | A2-S135 |
| Security features | Encryption at rest by default; customer-managed keys (AWS KMS, Azure Key Vault, Google Cloud KMS) on Elastic Cloud Hosted with Enterprise subscription (Serverless BYOK on roadmap); AWS PrivateLink, Azure Private Link, GCP Private Service Connect incl. London | Verified fact | A2-S134 |
| Access controls | SAML/OIDC SSO, RBAC, field/document-level security and audit logging (self-managed: Platinum tier); Elastic Cloud tier mapping not confirmed | Verified fact | A2-S134 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Elastic Inference Service billed per million tokens on Elastic Cloud (consumption-based); cluster pricing not verified | Verified fact | A2-S042 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Jina models and ELSER via Elastic Inference Service; OpenSearch fork as alternative (OpenSearch 3.9.0, 29 September 2026; opensearch-py 3.2.0, Apache-2.0) | Verified fact | A2-S023, A2-S136, A2-S058 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Mature; frequent minors (9.0-9.5 in ~16 months) | Verified fact | A2-S133 |
| Deployment | saas: Yes (Elastic Cloud Hosted and Serverless); managed_cloud: Yes (AWS, GCP, Azure); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (self-managed; AGPL/SSPL/ELv2 source); on_prem: Yes | | |

## Milvus (open source) and Zilliz Cloud (managed Milvus) (`L6-milvus-zilliz`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Milvus – vector search

*Rationale:* Foundation-governed, permissively licensed engine with a certified managed and BYOC route; scale option behind Qdrant [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Dense/sparse, BM25, JSON indexing, lake-native storage; multi-tenancy and filtered performance not evidenced |
| Enterprise readiness | 4 | SSO, audit logs and 99.95% SLA on Enterprise Dedicated (A2-S120), plus organisation, project and cluster RBAC with custom roles and SCIM (B-REVA-S001): all three controls plus SLA and SCIM (rule 7) |
| Security and compliance | 4 | Combined record: Zilliz Cloud has product-scoped SOC 2 Type II and ISO 27001 plus CMEK (would reach 5 under rule 8), but the self-hosted Milvus route is scored on rule 2 hygiene, which is not evidenced; 4 reflects the recommended mix of self-host and BYOC |
| Deployment flexibility | 5 | SaaS on three clouds, BYOC, self-host, on-prem |
| Ecosystem | 4 | pymilvus; mainstream integrations |
| Reliability and maturity | 4 | LF AI & Data graduated; 2.6 maintained; 3.0 GA only ten weeks |
| Cost / TCO | 3 | OSS free but distributed operations heavy; Zilliz BYOC pricing unpublished |
| Lock-in / portability | 5 | Apache-2.0 under neutral foundation governance |
| **Total (generic / FS)** | **4.10 / 4.25** | |

**Capabilities.** Apache-2.0 distributed vector database (LF AI & Data graduated) with dense/sparse vectors, BM25, JSON path indexing and online schema changes; Milvus 3.0 'lake-native' GA 29 July 2026; Zilliz Cloud as managed and BYOC 'Vector Lakebase' [VF: A2-S118, A2-S117, A2-S054, A2-S119].

**Strengths**

- Foundation governance and Apache-2.0 [VF: A2-S118]
- Zilliz Cloud SOC 2 Type II (incl. BYOC) and ISO 27001; CMEK on Business Critical [VF: A2-S119, A2-S120]
- Enterprise Dedicated with SSO, audit logs and 99.95% SLA [VF: A2-S120]
- Same API from Lite to Distributed to Zilliz Cloud [VF: A2-S054]
- Organisation, project and cluster RBAC with custom roles, IdP group mapping and SCIM on Zilliz Cloud [VF: B-REVA-S001]

**Limitations and risks**

- 3.0 not guaranteed compatible with 2.6 servers [VF: A2-S117]
- Milvus Lite has no authentication, roles or TLS [VF: A2-S054]
- Distributed Milvus is a heavy operational commitment [AJ]
- Zilliz last disclosed raise 2022 [VF: A2-S122]

**Choose when**

- Very large corpora, open-source portability with managed or BYOC options, or vectors alongside lakehouse data [AJ]

**Avoid when**

- A small team must self-operate Distributed Milvus [AJ]
- 3.0 features are needed before the 3.x line matures [AJ]

**Nearest competitors:** L6-qdrant, L6-pinecone, L6-weaviate

**Regulated-FS note.** Stay on 2.6 or a validated 3.0.x until regression tests pass; Zilliz BYOC for residency; never expose Lite beyond a laptop [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Milvus: open-source project, graduated LF AI & Data project; Zilliz (creator and main maintainer) offers Zilliz Cloud | Verified fact | A2-S118, A2-S053 |
| Category | Distributed open-source vector database ('lake-native' from 3.0) plus managed 'Vector Lakebase' (Zilliz Cloud) | Verified fact | A2-S118 |
| Version / lineup | Milvus 3.0.2 (20 September 2026); 3.0.0 GA 29 July 2026; 2.6.24 (16 September 2026) still maintained; PyMilvus 3.0.2; Milvus Lite 3.2.1. Zilliz Cloud: Milvus 3.0.x in Private Review for on-demand compute | Verified fact | A2-S117, A2-S118, A2-S053, A2-S054, V1-S031 |
| Licence | Open source, Apache-2.0 (Milvus 3.0); Zilliz Cloud commercial | Verified fact | A2-S118 |
| Status events | June 2025: Milvus 2.6 (BM25 full-text speedups, JSON path indexing); 16 July 2026: Milvus 3.0 announced; 29 July 2026: Milvus 3.0.0 GA (not guaranteed compatible with 2.6 servers); 20 September 2026: 3.0.2 | Verified fact | A2-S117, A2-S118 |
| Strategic direction | Repositioning as 'lake-native': indexes over vectors kept in object storage and open formats (Loon engine, Vortex columnar format), External Collections for lakehouse workflows; Zilliz Cloud as 'Vector Lakebase' | Verified fact | A2-S118, A2-S117 |
| What it does | Vector database with dense/sparse vectors (SINDI sparse index), BM25 full-text, JSON path indexing, faceted search, online schema changes; tiers from Milvus Lite to Distributed and Zilliz Cloud. | Verified fact | A2-S117, A2-S054 |
| Stack position | L6 dedicated vector database; placement correct. | Architectural judgement |  |
| Integration | pymilvus SDK (gRPC); same API across Lite, Standalone, Distributed and Zilliz Cloud | Verified fact | A2-S054 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Zilliz Cloud: SOC 2 Type II (scope incl. Free, Serverless, Dedicated, BYOC; report under NDA) and ISO/IEC 27001; GDPR-ready and HIPAA-ready (HIPAA-eligible on Business Critical) | Verified fact | A2-S119, A2-S120 |
| GDPR / residency | EU regions: AWS Frankfurt and Ireland, GCP Frankfurt, Azure Germany West Central and North Europe (Ireland) | Verified fact | A2-S121 |
| Security features | CMEK and HIPAA eligibility on Business Critical; private endpoints on Enterprise; BYOC shared-responsibility model (customer manages VPC and storage encryption) | Verified fact | A2-S120, A2-S119 |
| Access controls | SSO and audit logs on Enterprise Dedicated | Verified fact | A2-S120 |
| Enterprise support | Enterprise Dedicated with 99.95% uptime SLA | Verified fact | A2-S120 |
| Pricing | Zilliz Cloud: Serverless from US$0/month; Enterprise Dedicated from US$197/month; storage standardised at US$0.04/GB-month from 1 January 2026 (announced late 2025); BYOC not published. Milvus open source free. | Verified fact | A2-S120 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Zilliz total funding US$113M (Series B extension US$60M, August 2022); no 2025-2026 round found | Verified fact | A2-S122 |
| Maturity | Mature 2.x line still patched; 3.0 GA July 2026 with breaking compatibility | Verified fact | A2-S117 |
| Deployment | saas: Yes (Zilliz Cloud Serverless/Dedicated); managed_cloud: Yes (AWS, GCP, Azure); vpc_byoc: Yes (Zilliz BYOC: data plane in customer cloud account); private_cloud: Not publicly verified; self_hosted: Yes (Standalone, Distributed); on_prem: Yes | | |

## PostgreSQL with the pgvector extension (`L6-pgvector`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Postgres – + pgvector

*Rationale:* Lowest-increment, permissively licensed, transactionally integrated option on every hyperscaler; the default answer to 'do we need a dedicated vector DB?' [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Dense+sparse, HNSW/IVFFlat, filter-aware scans and SQL joins; no native BM25 and scale limits keep it below 5 |
| Enterprise readiness | 4 | Rule 2: inherits host controls; consumed via RDS/Aurora, Azure or Cloud SQL/AlloyDB so platform controls presumed (CP2 Q1); confirm per service |
| Security and compliance | 3 | Rule 2 hygiene: permissive licence and prompt CVE fixes, but two 2026 memory-safety CVEs (one CVSS 8.8) and host patch lag; signed releases not verified |
| Deployment flexibility | 5 | Self-host, on-prem and air-gap, plus managed services on AWS, Azure and Google Cloud |
| Ecosystem | 5 | SQL; supported by all three hyperscalers' managed PostgreSQL and Bedrock Knowledge Bases via Aurora |
| Reliability and maturity | 4 | Active 0.8.x maintenance (five 2026 releases) on a long-established database; still pre-1.0 versioning |
| Cost / TCO | 5 | Free; cost is PostgreSQL compute and RAM already operated |
| Lock-in / portability | 5 | PostgreSQL License, SQL interface, multiple managed hosts |
| **Total (generic / FS)** | **4.25 / 4.20** | |

*Evidence rules applied:* Rule 2 (self-hosted software): security scored on project hygiene; enterprise readiness on host controls with CP2 Q1 presumption for managed hyperscaler PostgreSQL

**Capabilities.** PostgreSQL extension adding vector types (incl. sparsevec) and HNSW/IVFFlat ANN indexes, so vectors sit beside relational data and SQL filters; iterative index scans and filter-aware index selection since 0.8.0; 0.8.7 released 1 October 2026 [VF: A2-S063, A2-S061, V1-S020, V1-S022].

**Strengths**

- Transactional integration: vectors, metadata and entitlement tables in one ACID database [AJ]
- PostgreSQL License (permissive, OSI) [VF: V1-S021]
- Managed on Amazon RDS/Aurora, Azure Database for PostgreSQL, Cloud SQL and AlloyDB [VF: B-L6-S004, B-L6-S005]
- Security fixes shipped promptly in 2026 (0.8.2, 0.8.7) [VF: V1-S020, V1-S022]

**Limitations and risks**

- CVE-2026-103484 (CVSS 8.8, IVFFlat build, possible code execution) fixed in 0.8.7; CVE-2026-3172 fixed in 0.8.2 [VF: V1-S022, A2-S062]
- Managed hosts lag upstream (latest RDS release seen carries 0.8.2) and Azure manages the version [VF: B-L6-S004, B-L6-S005]
- No BM25 ranking in the extension; hybrid needs sparsevec or app-side fusion [VF: A2-S063] [AJ]
- HNSW indexes are memory-hungry; large-scale filtered behaviour not evidenced [AJ] [NPV]

**Choose when**

- PostgreSQL is a firm standard and the corpus is millions, not billions, of chunks [AJ]
- Entitlements already live in relational tables [AJ]

**Avoid when**

- Thousands of isolated tenants with independent scaling are needed [AJ]
- Low-latency search over a very large corpus under selective filters [AJ]

**Nearest competitors:** L6-mongodb-atlas-vector-search, L6-elasticsearch, L6-qdrant

**Regulated-FS note.** Default for UK/EU managed PostgreSQL; track host pgvector version against CVEs; restrict index-creation rights; one schema per segregated mandate [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | pgvector open-source project (lead author Andrew Kane per Python client) on PostgreSQL | Verified fact | A2-S050, A2-S061 |
| Category | Vector search extension for a general-purpose relational database | Verified fact | A2-S061 |
| Version / lineup | pgvector 0.8.7 (released 1 October 2026 per CHANGELOG; announced on postgresql.org 5 October 2026); earlier 2026 releases 0.8.2 (Feb), 0.8.3 (17 Jun), 0.8.4 (30 Jun), 0.8.5 (8 Jul), 0.8.6 (29 Jul). Python client pgvector 0.5.0 (6 July 2026). | Verified fact | A2-S061, A2-S062, A2-S063, A2-S050, V1-S020, V1-S022 |
| Licence | Open source: PostgreSQL License (permissive, OSI-approved) for the extension; pgvector-python is MIT | Verified fact | A2-S050, V1-S021 |
| Status events | February 2026: 0.8.2 fixes CVE-2026-3172 (parallel HNSW build buffer overflow); 1 October 2026 (announced 5 October): 0.8.7 fixes an IVFFlat index-build buffer overflow (CVE-2026-103484, CVSS 8.8) that can allow arbitrary code execution by a user able to create IVFFlat indexes; Adjacent: pgvecto.rs deprecated in favour of VectorChord (early 2025); Timescale renamed Tiger Data (17 June 2025), pgvectorscale continues | Verified fact | A2-S062, A2-S061, A2-S066, A2-S067, A2-S064, A2-S065, V1-S020, V1-S022 |
| Strategic direction | Maintenance and security fixes on the 0.8.x line in 2026 (HNSW vacuuming, IVFFlat memory); supports dense and sparse (sparsevec) vectors | Verified fact | A2-S063, A2-S061 |
| What it does | Adds vector data types (including sparsevec) and HNSW and IVFFlat approximate-nearest-neighbour indexes to PostgreSQL, so vectors live alongside relational data and SQL filters. | Verified fact | A2-S063, A2-S061 |
| Stack position | L6 retrieval store inside the operational/analytical database tier; strong fit where transactional integration and SQL filtering matter. | Architectural judgement |  |
| Integration | SQL; client libraries such as pgvector-python | Verified fact | A2-S050 |
| Dependencies | PostgreSQL server (Postgres 18 referenced in 2026 fixes) | Verified fact | A2-S063 |
| Certifications | Depends on the hosting Postgres service; not applicable to the extension | Architectural judgement |  |
| GDPR / residency | Depends on hosting choice | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free, open source | Verified fact | A2-S050, A2-S061 |
| Infrastructure cost | Cost is Postgres compute/RAM (HNSW indexes are memory-hungry) and storage; no separate vector service | Architectural judgement |  |
| Ecosystem | Extensions: pgvectorscale (Tiger Data; up to 16,000 dims) and VectorChord (successor to pgvecto.rs) | Verified fact | A2-S064, A2-S066 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Active 0.8.x maintenance with five 2026 releases | Verified fact | A2-S061, A2-S062, A2-S063 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes | | |

## Qdrant (open-source vector search engine; Qdrant Cloud, Hybrid Cloud, Private Cloud) (`L6-qdrant`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Qdrant – open source

*Rationale:* Permissive licence, filter-aware multi-tenant engine and air-gap-capable deployment make it the default dedicated engine when a trigger is met [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Dense/sparse, ACORN filtering, RRF, multitenancy, quantisation; BM25 not evidenced |
| Enterprise readiness | 4 | Cloud RBAC with custom roles, SSO (Premium add-on) and audit access logging (B-L6-S007), plus the Cloud Management API and a 99.9% (99.95% multi-AZ) SLA on Premium (B-REVA-S002): rule 7 allows 4; SCIM not verified |
| Security and compliance | 3 | SOC 2 Type II and HIPAA but no ISO 27001: maximum 3 in this layer |
| Deployment flexibility | 5 | SaaS, hybrid, private incl. air-gap, self-host |
| Ecosystem | 4 | REST/gRPC with OpenAPI, FastEmbed, three clouds |
| Reliability and maturity | 3 | Frequent releases but breaking storage migration at 1.16; vendor-governed |
| Cost / TCO | 4 | Free OSS; managed from US$25 (as captured) |
| Lock-in / portability | 4 | Apache-2.0 and self-hostable; single-vendor governance |
| **Total (generic / FS)** | **3.90 / 3.85** | |

**Capabilities.** Apache-2.0 Rust vector search engine with dense and sparse vectors, payload filtering (ACORN), weighted RRF fusion, tiered multitenancy, quantisation and audit access logging; server 1.19.2 (5 October 2026) [VF: A2-S108, A2-S103, A2-S102].

**Strengths**

- Filter-aware search and tiered multitenancy suit entitlement-heavy, many-tenant retrieval [VF: A2-S103] [AJ]
- Managed, Hybrid (customer network) and Private Cloud incl. air-gapped, plus self-host [VF: A2-S106]
- Cloud RBAC with custom roles, SSO add-on, collection-scoped JWT keys [VF: B-L6-S007]
- Apache-2.0; US$50M Series B March 2026 [VF: A2-S108, A2-S107]
- Cloud Management API with management keys; 99.9% uptime SLA on Premium (99.95% multi-AZ) [VF: B-REVA-S002]

**Limitations and risks**

- No ISO 27001 found; HIPAA BAA documented for Managed Cloud only [VF: V1-S069]
- Upgrade cannot skip 1.16 (storage migration) [VF: A2-S102]
- SSO is a Premium add-on [VF: B-L6-S007]
- Managed pricing evidence thin and possibly stale [VF: A2-S106]
- Management and database keys are not revoked when the creating user leaves; offboarding must revoke them [VF: B-REVA-S002]

**Choose when**

- A dedicated engine is needed in your own estate or cloud account, with strong filtering and tenant isolation [AJ]

**Avoid when**

- ISO 27001 is a hard gate for a vendor-operated service [AJ]

**Nearest competitors:** L6-milvus-zilliz, L6-weaviate, L6-pinecone

**Regulated-FS note.** Self-host or Hybrid Cloud for client data; collection-scoped keys per service; enable audit access logging [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Qdrant (Qdrant Solutions GmbH, Berlin-headquartered) | Verified fact | A2-S105, A2-S107 |
| Category | Open-source vector search engine with managed, hybrid and private cloud offerings | Verified fact | A2-S107, A2-S106 |
| Version / lineup | Server v1.19.2 (5 October 2026; 1.19.0 on 5 August 2026); Private Cloud validated 1.19.0 (4 September 2026); Python client 1.19.1 (16 September 2026) | Verified fact | A2-S102, A2-S104, A2-S052 |
| Licence | Open source, Apache-2.0 (server and client); managed/hybrid/private cloud commercial | Verified fact | A2-S108, A2-S052 |
| Status events | 1.16: RocksDB to Gridstore storage migration (cannot be skipped on upgrade); 12 March 2026: US$50M Series B led by AVP; 27 March 2026: 1.17.1; 17 July 2026: 1.18.3; 5 August 2026: 1.19.0; 5 October 2026: 1.19.2 | Verified fact | A2-S102, A2-S103, A2-S107 |
| Strategic direction | 'Composable vector search as core infrastructure' from agentic workflows to edge devices (Series B, March 2026); recent releases add relevance-feedback queries, weighted RRF, audit access logging, tiered multitenancy, TurboQuant quantisation and low-memory mode | Verified fact | A2-S107, A2-S103, A2-S102 |
| What it does | Rust vector search engine with dense and sparse vectors, payload filtering (ACORN filtered search), hybrid fusion (weighted RRF), multitenancy, quantisation; client local mode and FastEmbed; Qdrant Cloud server-side inference on paid plans. | Verified fact | A2-S103, A2-S102, A2-S052 |
| Stack position | L6 dedicated vector search engine; placement correct. | Architectural judgement |  |
| Integration | REST/gRPC API (OpenAPI), Python client with sync/async, FastEmbed (ONNX) embeddings, Qdrant Cloud inference | Verified fact | A2-S052 |
| Dependencies | Self-hosted Docker/Kubernetes, or Qdrant Cloud on AWS, GCP, Azure | Verified fact | A2-S052, A2-S105 |
| Certifications | SOC 2 Type II (renewed over 12-month period); HIPAA compliance with BAA (Managed Cloud / on request); ISO 27001 not found | Verified fact | A2-S105, V1-S069 |
| GDPR / residency | DPA for GDPR; EU customers can keep data in EU regions exclusively; Cloud Inference runs in the EU for EU-region clusters | Verified fact | A2-S105 |
| Security features | Paid managed clusters on dedicated resources; Hybrid/Private Cloud keep data in customer environment; v1.19.2 warns at startup when no API keys configured | Verified fact | A2-S106, A2-S102 |
| Access controls | Audit access logging added in 1.17; SSO/RBAC for Qdrant Cloud not verified | Verified fact | A2-S103 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Managed Cloud priced on vCPU, RAM, disk and inference tokens, 'from US$25'; Hybrid Cloud figure US$0.014 per hour (unit unclear); Private Cloud and Enterprise on request | Verified fact | A2-S106 |
| Infrastructure cost | Self-hosting cost driven by RAM (or disk with on-disk/inline storage) and CPU; quantisation reduces memory | Architectural judgement |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | US$50M Series B (12 March 2026; AVP, Bosch Ventures, Unusual Ventures, Spark Capital, 42CAP); total funding US$87.8M (TechTarget); earlier US$28M Series A and US$7.5M seed; Canva quoted as customer | Verified fact | A2-S107, V1-S032 |
| Maturity | Monthly-ish minor releases (1.16-1.19 in about a year); breaking storage migration at 1.16 | Verified fact | A2-S102 |
| Deployment | saas: Yes (Qdrant Managed Cloud); managed_cloud: Yes (AWS, GCP, Azure); vpc_byoc: Yes (Hybrid Cloud: clusters in customer network, managed via Qdrant Cloud UI; Enterprise plan); private_cloud: Yes (Private Cloud, incl. air-gapped); self_hosted: Yes; on_prem: Yes | | |

## Pinecone (vector database; Pinecone Nexus knowledge engine) (`L6-pinecone`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Pinecone – managed

*Rationale:* Scores 3.80 FS but lock-in is 2 and it would be a net-new proprietary dependency whose vendor is widening into L5/L8 (Nexus); a criterion at 2 is accepted as a Strategic condition only where it rides on an existing platform commitment (Elastic, MongoDB), so Pinecone is held at Tactical until an exit route is decided [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Dense+sparse cascading retrieval, filters, namespaces, DRN scale; BM25 not evidenced |
| Enterprise readiness | 4 | SSO, SCIM, RBAC and audit logs verified on Enterprise; SLA not verified |
| Security and compliance | 5 | SOC 2 Type II and ISO 27001 from the product's own trust centre plus CMEK |
| Deployment flexibility | 4 | SaaS on three clouds plus BYOC; no self-host or air-gap |
| Ecosystem | 3 | Proprietary REST/SDK; OneLake and Marketplace integrations |
| Reliability and maturity | 4 | Core service mature; SDK v10 breaking; Nexus GA only since August 2026 |
| Cost / TCO | 3 | Transparent unit pricing but Standard/Enterprise minimums and idle BYOC nodes |
| Lock-in / portability | 2 | Proprietary API and format; Nexus/KnowQL coupling |
| **Total (generic / FS)** | **3.85 / 3.80** | |

**Capabilities.** Fully managed vector/document index with metadata filtering, namespaces, server-side embedding, hosted rerankers and a sparse model for cascading retrieval; Dedicated Read Nodes GA April 2026; Nexus knowledge engine GA 6 August 2026 [VF: A2-S051, A2-S101, A2-S072, A2-S073].

**Strengths**

- SOC 2 Type II, ISO 27001:2022, HIPAA BAA, project-level CMEK, PrivateLink [VF: A2-S095, A2-S096, V1-S078]
- SAML SSO, SCIM, RBAC for users, service accounts and API keys, audit logs on Enterprise [VF: A2-S097, A2-S098]
- BYOC GA on AWS, GCP and Azure with no vendor inbound access [VF: A2-S069, V1-S034]
- EU serverless regions in Ireland, Frankfurt and the Netherlands [VF: B-L6-S003]

**Limitations and risks**

- Proprietary API and service; Nexus/KnowQL deepen coupling [VF: A2-S051, A2-S073] [AJ]
- BYOC needs Enterprise and supports Dedicated Read Nodes only; some features absent in BYOC as of late August 2026 [VF: V1-S034]
- SDK v10 breaking changes (September 2026) [VF: A2-S051]
- Last disclosed funding 2023; CEO change September 2025 [VF: A2-S075, A2-S068]
- BYOC nodes billed whether idle or busy [VF: A2-S069]

**Choose when**

- A managed dedicated store at scale with enterprise identity, keys and BYOC is required [AJ]

**Avoid when**

- Self-hosting or air-gap is required [AJ]
- Nexus would become the only home of curated knowledge [AJ]

**Nearest competitors:** L6-milvus-zilliz, L6-qdrant, L6-turbopuffer

**Regulated-FS note.** Use Enterprise BYOC or an EU region; keep source of truth and raw text outside; treat Nexus as a separate decision with its own exit plan [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Pinecone Systems, Inc. (New York); CEO Ash Ashutosh since September 2025, founder Edo Liberty Chief Scientist | Verified fact | A2-S051, A2-S072, A2-S068 |
| Category | Managed vector database / knowledge infrastructure for AI | Verified fact | A2-S051, A2-S073 |
| Version / lineup | Managed service (serverless on-demand and Dedicated Read Nodes; BYOC); Python SDK 10.0.0 (3 September 2026) introduces schema-based document indexes and a deployment parameter; Nexus GA 6 August 2026 | Verified fact | A2-S051, A2-S072, A2-S069, A2-S073 |
| Licence | Proprietary managed service; Python SDK Apache-2.0 | Verified fact | A2-S051 |
| Status events | September 2025: Ash Ashutosh appointed CEO; April 2026: Dedicated Read Nodes GA; May 2026: Nexus early access, Marketplace launch, US$20/month Builder tier; 3 June 2026: Nexus + Microsoft OneLake integration; July 2026: Nexus public preview; 6 August 2026: Nexus GA; 3 September 2026: Python SDK v10 (breaking API changes); Late September 2026: BYOC announced generally available on AWS, GCP and Azure (Enterprise plan; some features such as Assistant, Inference and on-demand indexes were not yet available in BYOC as of late August) | Verified fact | A2-S068, A2-S072, A2-S074, A2-S073, A2-S051, V1-S029, V1-S034 |
| Strategic direction | Repositioning from vector database to knowledge infrastructure for agents: Nexus context compiler + composable retriever with KnowQL query language, field-level access control, citations, PII-aware ingestion and lineage; Microsoft OneLake integration (June 2026); Pinecone Marketplace (May 2026) | Verified fact | A2-S073, A2-S074 |
| What it does | Fully managed vector/document index with metadata filtering, namespaces and server-side embedding (create_for_model), plus Nexus for compiling enterprise data into task-specific knowledge artifacts for agents. | Verified fact | A2-S051, A2-S073 |
| Stack position | L6; with Nexus it also reaches into L5 memory/knowledge and L8 ingestion territory. | Architectural judgement |  |
| Integration | REST API and SDKs (Python v10); integrated inference: server-side embedding, hosted rerankers (pinecone-rerank-v0, cohere-rerank 3.5, bge-reranker-v2-m3) and sparse model pinecone-sparse-english-v0 for hybrid/cascading retrieval; Marketplace; OneLake connector for Nexus | Verified fact | A2-S051, A2-S101, A2-S073, A2-S074 |
| Dependencies | Pinecone cloud on AWS, GCP or Azure; BYOC runs in the customer's Kubernetes cluster with FoundationDB for metadata | Verified fact | A2-S069 |
| Certifications | SOC 2 Type II (2025 report, zero deviations); ISO/IEC 27001:2022 (annual surveillance audit); HIPAA with BAA on request; GDPR-ready; CCPA | Verified fact | A2-S095, A2-S096, V1-S078 |
| GDPR / residency | Frankfurt cloud region announced (newsroom headline; date not retrieved); Nexus BYOC data-residency reference exists | Reported | A2-S076 |
| Security features | AES-256 at rest, TLS in transit; CMEK at project level (irreversible toggle); AWS PrivateLink GA for serverless indexes; BYOC data plane in customer VPC with no vendor SSH/VPN/inbound access | Verified fact | A2-S096, A2-S097, A2-S069 |
| Access controls | SSO (SAML; Okta, Google Workforce) for Enterprise; SCIM + SAML; RBAC for users, service accounts and API keys (control/data plane roles); audit logs on Enterprise or HIPAA add-on (30-minute JSON batches); Nexus field-level access control | Verified fact | A2-S097, A2-S098, A2-S073 |
| Enterprise support | Standard and Enterprise plans; Enterprise unlocks SSO, audit logs, BYOC | Verified fact | A2-S072, A2-S097, A2-S099 |
| Pricing | Builder tier US$20/month (May 2026); Standard minimum US$50/month, Enterprise minimum US$500/month; committed-use rates (vary by cloud/region): Standard storage US$0.33/GB-month, writes US$4-4.50 per million WU, reads US$16-18 per million RU; Enterprise writes US$6-6.75, reads US$24-27 per million; query = 1 RU per GB of namespace (min 0.25); BYOC: platform fee + per-DRN rate + own cloud costs | Verified fact | A2-S074, A2-S099, A2-S100, A2-S069 |
| Infrastructure cost | BYOC nodes billed whether idle or busy | Verified fact | A2-S069 |
| Ecosystem | Microsoft OneLake (Nexus); Pinecone Marketplace | Verified fact | A2-S073, A2-S074 |
| Adoption signals | US$138M total funding (Andreessen Horowitz, ICONIQ, Menlo, Wing); Series B US$100M at US$750M (2023); ZoomInfo DRN customer story (April 2026) | Verified fact | A2-S072, A2-S075 |
| Maturity | Core service mature; Nexus GA since August 2026; SDK v10 is a breaking change | Verified fact | A2-S073, A2-S051 |
| Deployment | saas: Yes; managed_cloud: Yes (AWS, GCP, Azure regions); vpc_byoc: Yes (Enterprise; AWS, GCP, Azure; Dedicated Read Node indexes only; zero vendor access); private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## Weaviate (database; Weaviate Cloud: Shared, Dedicated, BYOC) (`L6-weaviate`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Weaviate – open source

*Rationale:* Capable and ISO-certified, but the open-core licence transition is incomplete and unannounced [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Hybrid search, filtering, MMR, Boost, quantisation; multi-tenancy not evidenced in the fact base |
| Enterprise readiness | 3 | RBAC, OIDC and audit logs verified for the database; SCIM, SLA and Cloud console RBAC not |
| Security and compliance | 4 | SOC 2 Type II and ISO 27001; CMEK not verified; BYOC scope not stated |
| Deployment flexibility | 5 | SaaS, dedicated, BYOC, self-host |
| Ecosystem | 4 | Mainstream clients and integrations |
| Reliability and maturity | 3 | Frequent minors, three-minor support window, licence change in flight |
| Cost / TCO | 3 | Open core; enterprise features behind licence keys; pricing naming conflicts |
| Lock-in / portability | 3 | BSD core but commercial enterprise features (rule 4) |
| **Total (generic / FS)** | **3.75 / 3.70** | |

**Capabilities.** Vector database combining vector search with structured filtering and hybrid search; Boost API and MMR GA in 1.39; v1.39.7 (25 September 2026); open core in transition [VF: A2-S110, A2-S109, A2-S115].

**Strengths**

- SOC 2 Type II and ISO 27001:2022; HIPAA on Premium Dedicated (AWS) [VF: A2-S111, A2-S112, A2-S113]
- RBAC with custom roles, OIDC users and groups, automatic RBAC audit logging [VF: B-L6-S009]
- SaaS, Dedicated (~40 regions), BYOC and self-host [VF: A2-S111, A2-S114, A2-S115]

**Limitations and risks**

- Enterprise features moving to commercial 'wl/' licence (1.40 RC; unannounced) [VF: A2-S115, V1-S070]
- Only latest three minors supported [VF: A2-S109]
- Weaviate Cloud console RBAC not yet available; BYOC certification scope not stated [VF: B-L6-S009, A2-S114]
- Pricing tier names conflict; last confirmed funding 2023 [VF: A2-S111] [R: A2-S116]

**Choose when**

- Weaviate is already in use, or hybrid search with an ISO-certified dedicated service is needed [AJ]

**Avoid when**

- Licence policy needs certainty about which features remain BSD [AJ]

**Nearest competitors:** L6-qdrant, L6-milvus-zilliz, L6-elasticsearch

**Regulated-FS note.** Obtain a written statement of which security features fall under the commercial licence before standardising [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Weaviate B.V. | Verified fact | A2-S115, A2-S116 |
| Category | Vector database with hybrid search, open core | Verified fact | A2-S110, A2-S115 |
| Version / lineup | v1.39.7 (25 September 2026); v1.40.0-rc.1 (19 September 2026); supported minors 1.37-1.39; Python client 4.23.1 | Verified fact | A2-S109, A2-S055 |
| Licence | Open core: most code BSD-3-Clause; 'wl/' enterprise features under a separate commercial Weaviate licence with licence key (2026 change, in 1.40 RC; merge/stable status not confirmed) | Verified fact | A2-S115, A2-S109, V1-S070 |
| Status events | April 2023: US$50M Series B (secondary source); 2026: enterprise 'wl/' licence and licence-key switch added (1.40.0-rc.1, 19 September 2026); 25 September 2026: v1.39.7 | Verified fact | A2-S116, A2-S109, A2-S115 |
| Strategic direction | Introducing an Enterprise Edition behind licence keys (2026); 1.39 GA of Boost API and MMR diversity, 4-bit Rotational Quantization preview, experimental Search REST API | Verified fact | A2-S115, A2-S110 |
| What it does | Stores objects and vectors and combines vector search with structured filtering; features include Boost API, MMR diversity, rotational quantisation. | Verified fact | A2-S110, A2-S115 |
| Stack position | L6 dedicated vector database; placement correct. | Architectural judgement |  |
| Integration | Python client (v4) | Verified fact | A2-S055 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type II (via Drata); ISO 27001:2022; HIPAA on Premium Dedicated (AWS) with signed BAA; BYOC certification scope not stated | Verified fact | A2-S111, A2-S112, A2-S113, A2-S114 |
| GDPR / residency | Shared Cloud on AWS US East and Europe (Frankfurt); Premium Dedicated in ~40 regions | Verified fact | A2-S111 |
| Security features | Encryption in transit and at rest, immutable backups (HIPAA offering) | Verified fact | A2-S113 |
| Access controls | Role-based access controls | Verified fact | A2-S113 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free; Flex pay-as-you-go from US$45/month; Premium (Dedicated) priced by region; BYOC metered CPU/memory rates; September 2026 backup-rate update. A blog describes a 'Plus' tier from US$280/month (naming conflict) | Verified fact | A2-S111 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | US$50M Series B (April 2023, led by Index Ventures), total US$67.7M; no 2025-2026 round confirmed | Reported | A2-S116 |
| Maturity | Frequent minor releases; only latest three minors supported | Verified fact | A2-S109 |
| Deployment | saas: Yes (Shared and Dedicated cloud); managed_cloud: Yes (~40 regions across GCP, AWS, Azure for Premium Dedicated); vpc_byoc: Yes (Weaviate manages data plane in customer VPC); private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes | | |

## MongoDB Vector Search (Atlas; self-managed Community Edition and Enterprise Advanced) (`L6-mongodb-atlas-vector-search`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** MongoDB – Atlas vector

*Rationale:* Strategic, conditional: only where MongoDB is already the operational store, because lock-in scores 2; the condition is an existing platform commitment, which is why it differs from Pinecone [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Vector, full-text and hybrid GA; rerank and auto-embedding preview |
| Enterprise readiness | 4 | SSO, roles and auditing verified (B-L6-S001) plus the Atlas Admin API (B-REV-S028): rule 7 allows 4; SCIM and SLA not verified |
| Security and compliance | 4 | Strong platform certifications but scope rule (CP2 Q4): platform-level, preview features excluded |
| Deployment flexibility | 4 | Atlas on three clouds plus self-managed; no BYOC |
| Ecosystem | 4 | Official drivers and aggregation API; Voyage integration |
| Reliability and maturity | 4 | Atlas mature; self-managed search GA only since c. July 2026 |
| Cost / TCO | 3 | Hourly Search Nodes; Community free; price tables conflict |
| Lock-in / portability | 2 | SSPL and proprietary Atlas; Voyage coupling |
| **Total (generic / FS)** | **3.80 / 3.65** | |

**Capabilities.** Vector and full-text search inside MongoDB via $vectorSearch/$search with hybrid fusion GA; $rerank (Voyage, preview) and Automated Embedding (preview); GA on Atlas and self-managed Community/Enterprise Advanced 8.2+ [VF: A2-S137, A2-S141, A2-S078, V1-S035].

**Strengths**

- Transactional integration where documents already live in MongoDB [AJ]
- Atlas ISO 27001:2022, SOC 2 Type II, PCI DSS, HITRUST, CSA STAR; FedRAMP Moderate for Gov [VF: A2-S138]
- SAML/OIDC SSO, org/project and custom database roles, database auditing on M10+ [VF: B-L6-S001]
- Self-managed option on 8.2+ [VF: A2-S137]

**Limitations and risks**

- SSPL for self-managed; Atlas proprietary; Voyage-native features couple L6 and L7 [VF: A2-S137, A2-S141]
- CMK covers search indexes only on dedicated Search Nodes [VF: A2-S139]
- Native rerank and Automated Embedding are preview and lack Geography targeting [VF: A2-S141, A2-S142]
- SOC 2 scope excludes preview features; Atlas log retention 30 days [VF: B-REV-S027, B-L6-S001]

**Choose when**

- MongoDB is the system of record for the documents being retrieved [AJ]

**Avoid when**

- MongoDB would be adopted only for retrieval [AJ]
- Preview reranking or embedding would sit in regulated flows [AJ]

**Nearest competitors:** L6-pgvector, L6-elasticsearch, L6-pinecone

**Regulated-FS note.** Dedicated Search Nodes so CMK covers indexes; export audit logs to the firm's archive; Voyage features off until GA and Geography-scoped [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | MongoDB, Inc. (owner of Voyage AI since February 2025) | Verified fact | A2-S033 |
| Category | Vector search built into a general-purpose document database | Verified fact | A2-S078 |
| Version / lineup | Atlas Vector Search; self-managed Search/Vector Search GA on MongoDB 8.2+ (mongot); hybrid search GA; $rerank native reranking (public preview, 8.3+); Automated Embedding (public preview); PyMongo 4.18.2 (24 September 2026) | Verified fact | A2-S137, A2-S141, A2-S078, A2-S059, V1-S035 |
| Licence | Atlas: proprietary managed service; Community Edition and mongot under SSPL (source-available); Enterprise Advanced commercial | Verified fact | A2-S137 |
| Status events | 17 February 2025: acquires Voyage AI; January 2026: Automated Embedding (public preview, Community); c. July 2026: Search and Vector Search GA for Community and Enterprise Advanced; c. July 2026: hybrid search GA; $rerank public preview; 1 September 2026: Europe Geography for Atlas Embedding and Reranking API; c. 30 September 2026: rerank-3 announced for native reranking | Verified fact | A2-S033, A2-S008, A2-S137, A2-S141, A2-S142, V1-S023, V1-S035 |
| Strategic direction | Vertical integration of retrieval: Voyage AI embeddings/rerankers native in the database (automated embedding, Atlas Embedding and Reranking API); announcement on native reranking and hybrid search for agent retrieval | Verified fact | A2-S008, A2-S077, A2-S078 |
| What it does | Vector and full-text search inside the document database via $vectorSearch/$search, hybrid fusion ($rankFusion RRF, $scoreFusion), index-less $rerank with Voyage cross-encoders (max 1,000 docs), and automated embedding with Voyage models. | Verified fact | A2-S137, A2-S141, A2-S078 |
| Stack position | L6 inside the operational database; with Voyage it spans L6 and L7. | Architectural judgement |  |
| Integration | MongoDB query API/aggregation via official drivers (e.g. PyMongo); Atlas Embedding and Reranking API | Verified fact | A2-S059, A2-S077 |
| Dependencies | MongoDB Atlas or MongoDB Community Edition; Voyage AI models for automated embedding | Verified fact | A2-S078 |
| Certifications | Atlas: ISO/IEC 27001:2022, SOC 2 Type II, PCI DSS, HITRUST, CSA STAR, HIPAA examination by third-party assessor; FedRAMP Moderate for Atlas for Government | Verified fact | A2-S138 |
| GDPR / residency | Atlas cluster region chosen by customer; Atlas Embedding and Reranking API offers Europe (EEA) Geography processing boundary; Automated Embedding and Native Reranking do not yet support Geography targeting | Verified fact | A2-S142, A2-S139 |
| Security features | AES-256 at rest by default; customer key management with AWS KMS, Azure Key Vault, Google Cloud KMS (not Free/Flex); search indexes covered by CMK only with dedicated Search Nodes | Verified fact | A2-S139 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Vector Search runs on cluster or dedicated Search Nodes (2-32 nodes, hourly, M10+); indicative Search Node tiers S20 US$0.12/hour to S80 US$3.26/hour; Flex US$8-30/month; Community self-managed free (SSPL); Geography-scoped Embedding API +10% | Verified fact | A2-S140, A2-S137, A2-S142 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (MongoDB Atlas); managed_cloud: Yes (Atlas on AWS, Azure, GCP); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Community Edition and Enterprise Advanced, MongoDB 8.2+, GA); on_prem: Yes | | |

## Amazon S3 Vectors (`L6-s3-vectors`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** S3 Vectors – AWS

*Rationale:* Tactical, default in AWS estates as the low-cost vector tier. Not AWS's lead vector-search service: AWS positions it as a durable tier behind OpenSearch [VF: A2-S092], so rubric rule 10 (CP3 Q2) does not make it Strategic [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Vector similarity with metadata filters at large scale; no lexical or hybrid |
| Enterprise readiness | 4 | Hyperscaler presumption: platform controls presumed (CP2 Q1); confirm per service; IAM and CloudTrail data events verified |
| Security and compliance | 4 | CMK per index and PrivateLink; platform certifications without stated S3 Vectors scope: one below anchor (CP2 Q4) |
| Deployment flexibility | 2 | AWS regional service only |
| Ecosystem | 3 | Bedrock Knowledge Bases and OpenSearch; proprietary API |
| Reliability and maturity | 3 | GA about ten months; evolving quotas |
| Cost / TCO | 5 | Pay-per-use storage and query, clearly efficient |
| Lock-in / portability | 2 | AWS-only API; designated CTPP concentration |
| **Total (generic / FS)** | **3.30 / 3.15** | |

*Evidence rules applied:* security_compliance at 4 (not 5) under CP2 Q4: S3 Vectors compliance scope not stated

**Capabilities.** Object storage with native vector indexes in vector buckets: up to 2 billion vectors per index, 50 metadata keys, 10,000 top-K, metadata filters; no BM25; Bedrock Knowledge Bases and OpenSearch integration; GA December 2025 [VF: A2-S083, A2-S086, A2-S089, A2-S093, V1-S030].

**Strengths**

- Very low storage cost with no provisioned compute [VF: A2-S087]
- SSE-KMS CMK per bucket or index, PrivateLink, IAM [VF: A2-S090, A2-S091]
- CloudTrail data events for vector operations [VF: B-L6-S006]
- About 34 Regions incl. European Sovereign Cloud and GovCloud [VF: A2-S084]

**Limitations and risks**

- AWS-only proprietary API [VF: A2-S092]
- No BM25/hybrid; pairs with OpenSearch [VF: A2-S083, A2-S093]
- Compliance-programme scope and HIPAA eligibility not confirmed [VF: A2-S090, B-L6-S006]
- Limits and prices changed several times in 2026 [VF: A2-S086, A2-S088]

**Choose when**

- AWS-centred firms needing a cheap durable tier or Bedrock Knowledge Base [AJ]

**Avoid when**

- Lexical search, low tail latency or a multi-cloud exit is required [AJ]

**Nearest competitors:** L6-turbopuffer, L6-milvus-zilliz, L6-pgvector

**Regulated-FS note.** Enable CloudTrail data events on regulated indexes; set KMS key at index creation; record under the AWS CTPP concentration entry [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Amazon Web Services | Verified fact | A2-S081 |
| Category | Object storage with native vector storage and similarity query (vector buckets and indexes) | Verified fact | A2-S094, A2-S092 |
| Version / lineup | Generally available since December 2025 (preview July 2025); up to 2 billion vectors per index, 10,000 indexes per bucket; 10,000 top-K per query since June 2026 | Verified fact | A2-S081, A2-S094, A2-S086, V1-S030 |
| Licence | Proprietary AWS managed service | Verified fact | A2-S092 |
| Status events | July 2025: preview (5 Regions); December 2025: GA in 14 Regions; March 2026: +17 Regions (31 total); June 2026: 10,000 results per query; query data-processed charges cut up to 80% for >10M-vector indexes; July 2026: AWS GovCloud (US) Regions | Verified fact | A2-S094, A2-S081, A2-S085, A2-S086, A2-S088, A2-S084 |
| Strategic direction | Positioned as low-cost, durable vector tier integrated with Bedrock Knowledge Bases and OpenSearch (tiering hot vectors to OpenSearch); rapid regional expansion and price cuts for large indexes in 2026 | Verified fact | A2-S092, A2-S093, A2-S085, A2-S088 |
| What it does | Stores vectors (1-4,096 dims) with up to 50 metadata keys in vector indexes inside vector buckets and serves similarity queries with metadata filters via S3 Vectors APIs (PutVectors, QueryVectors); up to 1,000 write requests/s per index. | Verified fact | A2-S083 |
| Stack position | L6 cost-optimised vector tier on object storage; not a full retrieval engine (no native BM25/hybrid) - pairs with OpenSearch for hybrid/low-latency; supports H5 'object-store vectors'. | Architectural judgement |  |
| Integration | S3 Vectors API/SDKs; Bedrock Knowledge Bases vector store (35 metadata keys, 1 KB metadata limit); OpenSearch managed clusters can use S3 Vectors as storage engine, or export to OpenSearch Serverless; CloudFormation support | Verified fact | A2-S089, A2-S093, A2-S092 |
| Dependencies | AWS account and Region; optionally Bedrock Knowledge Bases or Amazon OpenSearch Service | Verified fact | A2-S089, A2-S093 |
| Certifications | HIPAA eligibility and other compliance scope for S3 Vectors specifically not confirmed (general S3 programmes do not establish S3 Vectors scope) | Verified fact | A2-S090 |
| GDPR / residency | Regional service: about 34 Regions listed incl. AWS European Sovereign Cloud (Germany); data stays in chosen Region | Verified fact | A2-S084, A2-S085 |
| Security features | SSE-S3 by default; SSE-KMS with customer-managed keys per bucket or index (immutable after index creation; covers metadata); AWS PrivateLink interface endpoints with endpoint policies; IAM-based access | Verified fact | A2-S090, A2-S091 |
| Access controls | AWS IAM policies (S3 Vectors actions plus KMS permissions); CloudTrail monitoring of KMS key usage; S3 Vectors CloudTrail data-event coverage not confirmed | Verified fact | A2-S090 |
| Enterprise support | Covered by AWS Support plans (not verified specifically) | Architectural judgement |  |
| Pricing | Storage US$0.06/GB-month; PUT US$0.20 per logical GB (128 KB minimum per PUT); queries US$2.50 per million requests plus data processed US$0.004/TB (first 100K vectors), US$0.002/TB (100K-10M), US$0.0004/TB (10M+), data returned US$0.01/GB (first 512 KB/query free); up to 80% lower data-processed charges for >10M-vector indexes from June 2026 | Verified fact | A2-S087, A2-S088, V1-S030 |
| Infrastructure cost | Pay-per-use storage and query; no provisioned compute; AWS worked example: 50M vectors (4.1 KB each), 1M queries x 10,000 results = US$178.61/month | Verified fact | A2-S087 |
| Ecosystem | Amazon Bedrock Knowledge Bases, Amazon OpenSearch Service, Aurora PostgreSQL (AWS blog on SQL over S3 Vectors) | Verified fact | A2-S089, A2-S093 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GA ~10 months (December 2025); limits and pricing changed several times in 2026 | Verified fact | A2-S081, A2-S086, A2-S088 |
| Deployment | saas: Yes (AWS managed); managed_cloud: Yes (AWS Regions incl. GovCloud and European Sovereign Cloud); vpc_byoc: Not applicable (runs in customer's AWS account as a regional service); private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## turbopuffer (`L6-turbopuffer`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** turbopuffer – cloud vector store

*Rationale:* Distinctive object-storage design and per-namespace keys, but coarse key scoping, no ISO 27001, an Enterprise entry price well above peers and a proprietary API; author conflict disclosed and borderline calls resolved against it [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Vector + BM25 + filters with namespace isolation at scale; cold latency trade-off |
| Enterprise readiness | 3 | Dashboard SSO verified (lifts cap, CP2 Q2); no documented roles, admin-only BYOC keys, audit logs in beta |
| Security and compliance | 3 | SOC 2 Type 2, HIPAA, per-namespace CMEK, but no ISO 27001: maximum 3 |
| Deployment flexibility | 4 | SaaS on three clouds, dedicated clusters and BYOC; no self-host |
| Ecosystem | 3 | HTTP API and generated SDK; integrations not evidenced |
| Reliability and maturity | 3 | Young company; named customers and profitability only via press |
| Cost / TCO | 3 | Published minimums and object-storage pricing, but the Enterprise tier needed for CMEK and private networking starts at US$4,096 per month with a 35% usage premium (Pinecone Enterprise from US$500); 3, resolved against the Anthropic-related item (CP3 review A) |
| Lock-in / portability | 2 | Proprietary API and storage format |
| **Total (generic / FS)** | **3.30 / 3.15** | |

**Capabilities.** Proprietary serverless search on object storage: namespaced ANN vector (SPFresh) and BM25 full-text with filters; stateless compute with SSD/memory caches; SaaS and BYOC on AWS, GCP and Azure [VF: A2-S056, A2-S124, A2-S125]. Conflict of interest: Anthropic, the author's developer, is reported as a customer [R: A2-S126].

**Strengths**

- Object-storage economics for very large, many-tenant corpora [VF: A2-S124] [AJ]
- Per-namespace CMEK and private networking on Enterprise; HIPAA BAA on Scale+ [VF: A2-S123, V1-S077]
- BYOC with manual customer approval of vendor operations [VF: A2-S125]
- Region-pinned data incl. Frankfurt [VF: B-L6-S002]

**Limitations and risks**

- No built-in document-level RBAC; BYOC keys are admin keys [VF: B-L6-S002]
- Audit logs with SIEM only an opt-in beta (March 2026) [VF: B-L6-S002]
- No ISO 27001 found [NPV]
- Cold-query latency much higher than cached (vendor figures) [R: A2-S124]
- Funding and revenue only from press/aggregator [R: A2-S126, A2-S127]

**Choose when**

- Very many tenants or very large corpora with skewed access, BYOC and per-tenant keys [AJ]

**Avoid when**

- Fine-grained key scopes, ISO 27001 or self-hosting are required [AJ]

**Nearest competitors:** L6-pinecone, L6-milvus-zilliz, L6-s3-vectors

**Regulated-FS note.** BYOC only for client data; one namespace and key per client; warm-up policy for latency-sensitive tenants; independent alternative Zilliz BYOC [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | turbopuffer (Ottawa; CEO Simon Eskildsen per press) | Verified fact | A2-S056, A2-S126 |
| Category | Serverless vector and full-text search on object storage | Verified fact | A2-S124, A2-S056 |
| Version / lineup | Managed service; Python SDK 2.11.0 (7 October 2026) | Verified fact | A2-S056 |
| Licence | Proprietary service; Python SDK MIT | Verified fact | A2-S056 |
| Status events | 19 December 2025: undisclosed raise from Lachy Groom and Thrive Capital (press) | Verified fact | A2-S126 |
| Strategic direction | Object-storage-first search engine targeting very large multi-tenant workloads; BYOC on AWS, GCP and Azure | Verified fact | A2-S124, A2-S125 |
| What it does | Namespaced search API with ANN vector (SPFresh centroid index) and BM25 full-text ranking plus filters; all durable state in object storage with SSD/memory caches (cold p50 874 ms vs cached p50 14 ms on 1M docs). | Verified fact | A2-S056, A2-S124 |
| Stack position | L6 retrieval store (vector + full-text), placement correct; the BM25 support supports the H5 'retrieval store' framing. | Architectural judgement |  |
| Integration | HTTP API; generated Python SDK (sync and async) | Verified fact | A2-S056 |
| Dependencies | Object storage (S3, GCS, Azure Blob) as system of record; Kubernetes for BYOC | Verified fact | A2-S124, A2-S125 |
| Certifications | SOC 2 Type 2 (report on request); HIPAA BAA on Scale and Enterprise tiers | Verified fact | A2-S125, A2-S123, V1-S077 |
| GDPR / residency | DPA for GDPR/CCPA; region chosen per client (e.g. gcp-us-central1); full EU region list not verified | Verified fact | A2-S123, A2-S056 |
| Security features | TLS 1.2+ in transit; AES-256 at rest including SSD cache; Enterprise: per-namespace customer-managed encryption keys and private networking | Verified fact | A2-S125, A2-S123 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Minimum monthly usage: Launch US$16, Scale US$256, Enterprise >=US$4,096 (35% usage premium); storage on logical bytes; queries on data scanned (min 1.28 GB/namespace) and returned, with volume discounts | Verified fact | A2-S123, V1-S077 |
| Infrastructure cost | Object-storage economics; cold-query latency trade-off | Verified fact | A2-S124 |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Named customers include Anthropic, Atlassian, Cursor, Notion, Legora; Sacra estimates ~US$100M annualised revenue (March 2026); <US$1M primary capital raised per CEO | Reported | A2-S126, A2-S127, A2-S125 |
| Maturity | Very frequent SDK releases (2.11.0 on 7 October 2026) | Verified fact | A2-S056 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (customer Kubernetes on AWS, GCP, Azure; manual customer approval for operations); private_cloud: Not publicly verified; self_hosted: No (BYOC only); on_prem: Not publicly verified | | |

## Chroma (open source) and Chroma Cloud (`L6-chroma`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Chroma – open source

*Rationale:* Useful for prototypes and harnesses; enterprise controls undocumented and release cadence uncertain [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Core vector store with filters; hybrid and full-text only on Cloud; scale not evidenced |
| Enterprise readiness | 2 | Customer-facing SSO, roles and audit logs NPV; only tenant-scoped access and DB-scoped keys found |
| Security and compliance | 3 | SOC 2 Type II and CMEK; no ISO 27001: maximum 3 |
| Deployment flexibility | 4 | Embedded, self-host, Cloud, single-tenant and BYOC, but self-host lacks auth and only one EU cloud region |
| Ecosystem | 3 | Python/JS clients; ecosystem not evidenced |
| Reliability and maturity | 2 | Rust rewrite 2025; five months without a PyPI release; seed-funded |
| Cost / TCO | 4 | Free OSS; transparent cloud usage pricing |
| Lock-in / portability | 4 | Apache-2.0, vendor-governed |
| **Total (generic / FS)** | **3.05 / 3.10** | |

*Evidence rules applied:* enterprise_readiness capped at 2: customer SSO, RBAC and audit logs NPV

**Capabilities.** Apache-2.0 embedded or client-server database for documents and embeddings with a small API; Chroma Cloud adds serverless vector, hybrid and full-text search, BYOC and single-tenant options [VF: A2-S060, A2-S128].

**Strengths**

- Fastest path from notebook to working retrieval [AJ]
- Apache-2.0 [VF: A2-S060]
- Chroma Cloud SOC 2 Type II and CMEK GA [VF: A2-S130, B-L6-S008]
- Transparent usage pricing [VF: A2-S128]

**Limitations and risks**

- Open-source build has no built-in auth since 1.0 [VF: A2-S131]
- Customer SSO, roles and audit logs not documented [NPV]
- No PyPI release since 5 May 2026 at time of research [VF: A2-S060]
- Multi-tenant cloud only in us-east-1 and GCP Belgium; no UK region [VF: A2-S129]

**Choose when**

- Prototypes, evaluation harnesses, embedded single-user tools [AJ]

**Avoid when**

- Client-confidential data or production-critical systems [AJ]

**Nearest competitors:** L6-pgvector, L6-qdrant, L6-turbopuffer

**Regulated-FS note.** Never self-host the open-source server without an authenticating proxy; no promotion of prototypes without a re-platforming decision [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Chroma (Jeff Huber, Anton Troynikov listed as authors) | Verified fact | A2-S060 |
| Category | Open-source embedding/vector database with serverless cloud service | Verified fact | A2-S060 |
| Version / lineup | chromadb 1.5.9 (5 May 2026) | Verified fact | A2-S060 |
| Licence | Open source, Apache-2.0 | Verified fact | A2-S060 |
| Status events | 1 March 2025: Chroma 1.0 (Rust rewrite; built-in auth implementations removed); 5 May 2026: chromadb 1.5.9 | Verified fact | A2-S131, A2-S060 |
| Strategic direction | Positions itself as 'the open-source data infrastructure for AI'; Chroma Cloud offers serverless vector, hybrid and full-text search | Verified fact | A2-S060 |
| What it does | Embedded or client-server database for documents and embeddings with a small API (create collection, add, query); Chroma Cloud adds serverless hybrid and full-text search. | Verified fact | A2-S060 |
| Stack position | L6; strong for prototyping/embedded use, Cloud targets production. | Architectural judgement |  |
| Integration | Python and JavaScript clients; in-memory, persistent or client-server mode | Verified fact | A2-S060 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Chroma Cloud SOC 2 Type II | Verified fact | A2-S130, A2-S128, V1-S086 |
| GDPR / residency | Multi-tenant regions: AWS us-east-1 and GCP europe-west1 (Belgium); data stays in chosen region | Verified fact | A2-S129 |
| Security features | Customer-managed encryption keys changelog entry exists (content not retrieved); open-source build has no built-in auth since 1.0 | Reported | A2-S130, A2-S131 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Starter US$0 + usage (US$5 credit): US$2.50/GiB written, US$0.33/GiB-month stored, US$0.0075/TiB queried, US$0.09/GiB returned; Team US$250/month + usage; single-tenant/BYOC custom | Verified fact | A2-S128, V1-S086 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | US$18M seed round | Verified fact | A2-S131 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Chroma Cloud, multi-tenant); managed_cloud: Not publicly verified; vpc_byoc: Yes (BYOC clusters, fixed minimum cost); private_cloud: Yes (single-tenant clusters, custom pricing); self_hosted: Yes; on_prem: Yes | | |

# L5: Memory

## Zep (managed context-graph platform, 'Zep Cloud') and Graphiti (open-source temporal knowledge-graph framework) (`L5-zep`)

**Tier:** Tactical · **Flags:** Deprecated · **Original graphic label:** Zep – graph memory

*Rationale:* Technically the strongest memory model for audit and temporal reasoning; tier-gated compliance, a proprietary managed engine and pre-1.0 Graphiti keep it Tactical [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Bi-temporal graph, episodes with provenance, hybrid retrieval, users and threads: leading depth on the layer's memory-type questions |
| Enterprise readiness | 4 | IdP sign-in, RBAC + ABAC and audit logs with one-year retention, plus a guaranteed SLA on Enterprise (A3-S107, A3-S089): rule 7 allows 4 (CP3 review A, consistent with Mistral OCR); condition: audit logs cover web-app actions only, not API or SDK calls |
| Security and compliance | 3 | SOC 2 Type II + HIPAA + BYOK on Enterprise; no ISO 27001 found (same calibration as Braintrust in L9) |
| Deployment flexibility | 4 | SaaS and BYOC (AWS/GCP/Azure); Graphiti self-host; no supported self-host of Zep itself |
| Ecosystem | 4 | Broad framework integrations; Graphiti 31,529 stars; MCP server |
| Reliability and maturity | 3 | Graphiti pre-1.0 with frequent releases; SDK 4.0 beta; Community Edition deprecated; no acquisition found |
| Cost / TCO | 3 | Published credit pricing (Flex US$125, Flex Plus US$375 per month); Graphiti cost is graph DB + LLM ingestion |
| Lock-in / portability | 2 | Zep Cloud proprietary engine and API; Graphiti (Apache-2.0) is a partial exit with no documented migration |
| **Total (generic / FS)** | **3.75 / 3.50** | |

**Capabilities.** Zep Cloud managed context-graph platform on a proprietary Context Graph Engine, with Graphiti (Apache-2.0) as the open-source temporal knowledge-graph framework: entities, facts with validity windows, episodes with provenance, communities; invalidation rather than deletion; hybrid semantic, keyword and graph retrieval [VF: A3-S003, A3-S059].

**Strengths**

- Bi-temporal facts and per-episode provenance suit audit and how-facts-changed questions [VF: A3-S003]
- SOC 2 Type II, HIPAA BAA, BYOK and BYOC on Enterprise [VF: A3-S089, A3-S090]
- Right-to-be-forgotten and time-based retention purge (Zep Archive); EU residency on request; DPAs [VF: A3-S107]
- Integrations with ADK, Microsoft Agent Framework, LangGraph, Strands and others; Graphiti MCP server [VF: A3-S059, A3-S003]

**Limitations and risks**

- Community Edition deprecated; Graphiti is the only OSS path [VF: A3-S059, V1-S044]
- Compliance only on Enterprise, not Flex or Flex Plus [VF: A3-S089]
- Audit logs cover web-app member actions, not API or SDK calls [VF: A3-S107]
- Graphiti pre-1.0; zep-cloud SDK 4.0 in beta [VF: A3-S003, A3-S002]
- Proprietary graph engine in Zep Cloud; migration path to Graphiti not documented [VF: A3-S003] [NPV]

**Choose when**

- Temporal validity and provenance of memory matter (mandate or terminology changes over time) [AJ]
- Graphiti self-hosted on Neo4j or Neptune for in-estate data [AJ]

**Avoid when**

- You need API-level audit logs from the vendor, ISO 27001, or a supported self-hosted full platform [AJ]

**Nearest competitors:** L5-mem0, L5-cognee, L5-gcp-vertex-memory-bank

**Regulated-FS note.** Prefer self-hosted Graphiti on an approved graph store and test that erasure removes invalidated facts and episodes; use Zep Cloud only on Enterprise with EU residency requested [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Zep (getzep) | Verified fact | A3-S059 |
| Category | Managed agent memory / context-graph infrastructure; Graphiti is the open-source temporal knowledge-graph library underneath | Verified fact | A3-S003 |
| Version / lineup | zep-cloud Python SDK 3.30.0 (24 September 2026), 4.0.0b1 pre-release (6 October 2026); graphiti-core 0.30.2 (8 September 2026) | Verified fact | A3-S002, A3-S003 |
| Licence | Zep platform proprietary; Graphiti Apache-2.0; Zep Community Edition deprecated and unsupported | Verified fact | A3-S003, A3-S059 |
| Status events | Zep Community Edition deprecated; code moved to legacy/ folder (status on 7 October 2026; date of deprecation not verified); Graphiti: Kuzu backend deprecated because upstream Kuzu project is unmaintained | Verified fact | A3-S059, A3-S003, V1-S044 |
| Strategic direction | Positions Zep as 'context infrastructure' powered by a proprietary Context Graph Engine built for millions of per-user/entity context graphs; ships agent plugins for Claude Code, Codex, Cursor, Claude Desktop/Cowork and ChatGPT | Verified fact | A3-S003, A3-S059 |
| What it does | Graphiti builds temporal context graphs: entities, facts with validity windows (bi-temporal), episodes with provenance and communities; old facts are invalidated rather than deleted; retrieval is hybrid semantic, keyword and graph search. Zep adds managed users, threads and message storage, dashboard and pre-configured retrieval (vendor claims sub-200ms) | Verified fact | A3-S003 |
| Stack position | Spans L5 memory and L6 knowledge store: a temporal knowledge graph that ingests chat history and business data; the graphic's 'graph memory' descriptor matches Graphiti's design | Verified fact | A3-S003 |
| Integration | Zep SDKs for Python, TypeScript and Go; framework integrations for Google ADK, Microsoft Agent Framework, AutoGen, AG2, CrewAI, LangGraph, LiveKit, Pydantic AI, Strands Agents, Mastra and Vercel AI SDK; Graphiti offers an MCP server and FastAPI REST service | Verified fact | A3-S059, A3-S003 |
| Dependencies | Graphiti requires Neo4j 5.26, FalkorDB 1.1.2 or Amazon Neptune (with OpenSearch Serverless for full text); Kuzu deprecated; defaults to OpenAI for LLM and embeddings and needs an LLM with structured output. Zep Cloud uses its proprietary graph engine (no third-party graph DB) | Verified fact | A3-S003 |
| Certifications | SOC 2 Type II and HIPAA BAA on Enterprise plan only (not on Flex/Flex Plus); reports via Zep Trust Center | Verified fact | A3-S089, A3-S090 |
| GDPR / residency | Signs DPAs with EU customers; US hosting by default, EU residency available on request; right-to-be-forgotten and time-based retention/purge features (Zep Archive) | Verified fact | A3-S107, A3-S089 |
| Security features | BYOK (cloud with your own keys) and BYOC (your own VPC on AWS, GCP or Azure) on Enterprise; BYOK via AWS KMS in emerging-companies programme | Verified fact | A3-S089, A3-S090 |
| Access controls | IdP-based member sign-in (SAML not named); RBAC for dashboard (account/project roles) and ABAC policies for data reads/writes; audit logs cover web-app member actions only, not API/SDK calls; Enterprise retains audit and API logs 1 year | Verified fact | A3-S107 |
| Enterprise support | Enterprise: custom pricing, negotiated credit rates, guaranteed SLA | Verified fact | A3-S089 |
| Pricing | Flex US$125/month (50,000 credits); Flex Plus US$375/month (200,000 credits); Enterprise custom; emerging-companies programme US$13,000 first year | Verified fact | A3-S089, A3-S090 |
| Infrastructure cost | Graphiti self-hosting cost is driven by the graph database (Neo4j/FalkorDB/Neptune) and LLM calls during ingestion; README warns of LLM rate-limit (429) errors at default concurrency | Verified fact | A3-S003 |
| Ecosystem | Integrations across major agent frameworks; Graphiti backends Neo4j, FalkorDB, Neptune | Verified fact | A3-S059, A3-S003 |
| Adoption signals | getzep/graphiti 31,529 GitHub stars; getzep/zep 4,951 stars (7 October 2026). Backers named as Y Combinator and Engineering Capital; no 2025-2026 round found | Verified fact | A3-S054, A3-S090 |
| Maturity | graphiti-core first released August 2024, 194 releases, still pre-1.0 (0.30.x); zep-cloud SDK on 3.x with a 4.0 beta in progress | Verified fact | A3-S003, A3-S002 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (BYOC on Enterprise; AWS, GCP, Azure); private_cloud: Not publicly verified; self_hosted: Graphiti only (self-hosted framework); Zep Community Edition is deprecated; on_prem: Not publicly verified | | |

## Mem0 (open-source library and self-hosted server; Mem0 Platform managed service) (`L5-mem0`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Mem0 – memory layer

*Rationale:* Broad, store-agnostic memory API useful behind a firm-owned wrapper; certification evidence and OSS/Platform divergence keep it off the Strategic tier [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Covers extraction, scoping, hybrid recall, deletion and history; graph and decay only on Platform |
| Enterprise readiness | 4 | Enterprise plan lists SSO, audit logs and SLA support (A3-S049); Platform org/project member roles and an event feed (A3-S080): all three controls plus SLA reach 4 under rule 7 (CP3 review A, consistent with Firecrawl and Mistral OCR); condition: evidence is a pricing page and OSS has no org concept |
| Security and compliance | 2 | SOC 2 Type I confirmed by vendor; Type II claims conflict; no report seen; HIPAA and BYOK vendor-stated |
| Deployment flexibility | 4 | SaaS, self-host and on-prem verified; VPC and air-gap are vendor claims from a marketing guide |
| Ecosystem | 4 | Wide vector-store support, LangGraph and CrewAI integrations; MCP repository archived |
| Reliability and maturity | 3 | Two years of releases but breaking changes in April 2026 (ADD-only, graph removed from OSS); no acquisition found |
| Cost / TCO | 4 | Apache-2.0 OSS; published tiers (Starter US$19, Pro US$249 per month); self-host cost is LLM + embedder + vector store |
| Lock-in / portability | 3 | Apache-2.0 OSS on standard stores, but key features (incl. export) Platform-only |
| **Total (generic / FS)** | **3.55 / 3.35** | |

*Evidence rules applied:* security_compliance at 2: SOC 2 Type II status conflicting on vendor pages, only Type I confirmed (treated as below the 3 anchor)

**Capabilities.** Open-core agent memory layer: extracts facts from conversations and agent actions, scopes them by user_id, agent_id and run_id, retrieves with semantic + BM25 + entity signals; add/search/get/update/delete/delete_all and per-memory history in OSS and Platform; storage in SQL + third-party vector store + entity store [VF: A3-S001, A3-S080, A3-S053].

**Strengths**

- Supports 14+ vector stores incl. PGVector, Elasticsearch, OpenSearch, MongoDB, so the canonical record can sit in the firm's L6 store [VF: A3-S080, A3-S053]
- Apache-2.0 OSS server with authentication on by default [VF: A3-S001]
- Platform has org/project roles and a project-wide event feed of add/search/delete events usable for audit [VF: A3-S080]
- Largest community in the layer (66,777 GitHub stars, 7 October 2026) [VF: A3-S054]

**Limitations and risks**

- SOC 2 status conflicts on vendor pages (Type I; Type II in progress; Type II for Enterprise); trust-centre report not seen [VF: A3-S051, A3-S106]
- No managed EU region found [VF: A3-S106]
- OSS v2.0.0 (14 April 2026) removed external graph stores; graph memory, decay, temporal reasoning, Dream, webhooks and export are Platform-only [VF: A3-S081, V1-S043, A3-S080]
- ADD-only OSS extraction: memories accumulate unless pruned [VF: A3-S081]
- Vendor benchmark figures (LoCoMo 92.5, LongMemEval 94.4) are vendor-reported only [R: A3-S081]

**Choose when**

- You want a framework-neutral memory API self-hosted on your own approved vector store, behind your own policy gate [AJ]

**Avoid when**

- You would put regulated data on the managed Platform before a SOC 2 Type II report is obtained [AJ]
- You need a queryable graph in open source [AJ]

**Nearest competitors:** L5-zep, L5-supermemory, L5-aws-agentcore-memory, L5-cognee

**Regulated-FS note.** Self-host the OSS server against the approved vector store, implement the subject index and write gate in a firm-owned wrapper, and obtain the SOC 2 report before any Platform use [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Mem0 (start-up; Y Combinator S24 per project README) | Verified fact | A3-S001 |
| Category | Agent memory layer: open-source memory library/server plus managed memory platform | Verified fact | A3-S001, A3-S080 |
| Version / lineup | mem0ai 2.2.1 on PyPI (25 September 2026). New memory algorithm announced April 2026; open-source v2.0.0 (14 April 2026) introduced breaking changes | Verified fact | A3-S001, A3-S053, A3-S081 |
| Licence | Open core: open-source SDK/server under Apache-2.0; Mem0 Platform is proprietary and carries Platform-only features (graph memory, memory decay, temporal reasoning, Dream consolidation, webhooks, memory export) | Verified fact | A3-S001, A3-S080 |
| Status events | 14 April 2026: open-source v2.0.0 removed all external graph store backends (Neo4j, Memgraph, Kuzu, Apache AGE, Neptune) and the enableGraph option (SDK changelog files the deletions under v2.0.1); OSS now uses built-in entity linking (a parallel entity collection that boosts retrieval, not a queryable graph); graph memory is a Platform-only feature; October 2025: US$24M combined seed and Series A led by Basis Set Ventures (Reported); mem0ai/mem0-mcp repository archived (status on 7 October 2026) | Verified fact | A3-S053, A3-S081, A3-S052, A3-S054, V1-S043, V1-S081 |
| Strategic direction | April 2026 algorithm: single-pass ADD-only extraction, entity linking, multi-signal retrieval (semantic + BM25 + entity) and temporal reasoning; vendor-reported LoCoMo 92.5 and LongMemEval 94.4 on the managed platform. Graph memory moved to Platform-only. Skills for coding agents include an 'OSS-to-Platform' migration skill | Verified fact | A3-S001, A3-S081 |
| What it does | Extracts facts from conversations and agent actions, stores them as memories scoped by user_id, agent_id and run_id, and retrieves them with entity-aware ranking. Core operations add, search, get, update, delete, delete_all and per-memory history exist in both the open-source Memory class and the hosted MemoryClient | Verified fact | A3-S080 |
| Stack position | Memory service sitting on top of retrieval infrastructure: stores facts in a SQL database, embeddings in a third-party vector database and entities in an entity store; the open-source build defaults to a local Qdrant instance | Verified fact | A3-S053, A3-S080 |
| Integration | Python and JavaScript SDKs plus REST API (self-hosted server or hosted); integrations documented for LangGraph and CrewAI; vector store support includes Qdrant, Chroma, PGVector, Pinecone, Oracle, Milvus, MongoDB, Redis, Valkey, Elasticsearch, OpenSearch, Supabase, Upstash and Azure (Python) | Verified fact | A3-S001, A3-S080, A3-S053 |
| Dependencies | Requires an LLM and an embedder; Python package depends on openai, qdrant-client and sqlalchemy; you provision and pay for the vector store, LLM and embedder when self-hosting | Verified fact | A3-S001, A3-S080 |
| Certifications | Vendor pages conflict: SOC 2 Type I (homepage/About), 'Type II audit in progress' (one article) and 'Type II for Enterprise' (one guide); HIPAA claimed; Trust Center report not seen | Verified fact | A3-S051, A3-S106 |
| GDPR / residency | Vendor states GDPR compliant; no managed EU region found; residency addressed through self-hosted/private-cloud/air-gapped deployment | Verified fact | A3-S051, A3-S106 |
| Security features | Vendor states BYOK encryption across deployment models; self-hosted server has authentication on by default | Verified fact | A3-S051, A3-S001 |
| Access controls | Enterprise plan lists SSO and audit logs; Platform has multi-organisation/multi-project structure with member roles and a project-wide event feed (add/search/delete events) usable for audit; open source has no org/project concept and only per-memory history | Verified fact | A3-S049, A3-S080 |
| Enterprise support | Enterprise plan with SLA support; Pro plan includes private Slack support | Verified fact | A3-S049 |
| Pricing | Hobby free (10,000 adds / 1,000 retrievals per month); Starter US$19 per month; Pro US$249 per month (graph memory, Dream); Enterprise custom (on-prem, SSO, audit logs, SLA) | Verified fact | A3-S049 |
| Infrastructure cost | Self-hosting cost is driven by the vector store, LLM calls for extraction and the embedder, all provisioned and paid for by the customer | Verified fact | A3-S080 |
| Ecosystem | Broad vector-store support (14+ in Python); TypeScript SDK adds Amazon S3 Vectors and Neptune Analytics; LangGraph and CrewAI integrations | Verified fact | A3-S053, A3-S001 |
| Adoption signals | 66,777 GitHub stars (7 October 2026). Reported at Series A (October 2025): 14M downloads, API calls grew from 35M (Q1) to 186M (Q3 2025) | Verified fact | A3-S054, A3-S052 |
| Maturity | First PyPI release 18 May 2024; 192 releases; v2.x with frequent releases (eight between 4 August and 25 September 2026) | Verified fact | A3-S001 |
| Deployment | saas: Yes; managed_cloud: Yes (vendor states private Kubernetes deployment inside customer VPC); vpc_byoc: Yes (vendor claim); private_cloud: Yes (vendor claim: private Kubernetes); self_hosted: Yes (docker compose server; library); on_prem: Yes (Enterprise on-prem; vendor also claims air-gapped) | | |

## Cognee (`L5-cognee`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Cognee – knowledge graphs

*Rationale:* Credible in-estate graph-plus-vector memory with strong deployment options; no certification and seed-stage funding limit it to scoped, self-hosted use [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Graph + vector memory with remember/recall/improve/forget and local extraction |
| Enterprise readiness | 3 | Rule 2 basis: authenticated multi-tenant users, Enterprise SSO, SLAs and a dedicated support engineer (A3-S005, A3-S095); one verified control gives 3 under rule 7 (CP3 review A, consistent with LlamaParse and Browserbase); RBAC and audit logs NPV |
| Security and compliance | 2 | Scored as self-hosted software (vendor-recommended) under rule 2: encryption, private mode, air-gap verified; security policy and signed releases NPV. Cognee Cloud alone would score 1 (no certification by vendor statement) |
| Deployment flexibility | 5 | Cloud, BYOC, self-host, on-prem and air-gap |
| Ecosystem | 3 | MCP server and community plugins; 31,561 stars; optional standard graph and vector stores |
| Reliability and maturity | 3 | Post-1.0 (1.6.x), 178 releases since March 2024; seed-stage company; no acquisition found |
| Cost / TCO | 3 | Free OSS locally; Cloud US$1 per 1M tokens; production Postgres graph licensed |
| Lock-in / portability | 3 | Apache-2.0 core on standard stores, but production Postgres graph is licensed |
| **Total (generic / FS)** | **3.35 / 3.25** | |

*Evidence rules applied:* Rule 2 applied (self-hosted software; inherits host controls): security_compliance and enterprise_readiness scored on self-hosted basis, capped at 4; enterprise_readiness: NPV cap lifted to 3 by verified SSO (rule 7)

**Capabilities.** Open-source memory platform building knowledge graphs plus vectors from documents, code and conversations; remember, recall, improve and forget; retrieval selects graph, vector or code context; local small-model extraction; MCP server [VF: A3-S005].

**Strengths**

- Runs fully in-estate or air-gapped with zero external API calls [VF: A3-S095]
- Backs onto Postgres/pgvector, Neo4j or Neptune [VF: A3-S005]
- EU company with GDPR process audit, DPA, erasure and portability support; BYOC in customer EU cloud account [VF: A3-S095]
- Enterprise SSO, SLAs and dedicated support engineer [VF: A3-S095]

**Limitations and risks**

- States it holds no SOC 2, ISO 27001 or equivalent certification [VF: A3-S095]
- Production Postgres graph store is a licensed product [VF: A3-S005]
- RBAC and audit logs not documented [NPV]
- Seed-stage funding; aggregators disagree on amount [R: A3-S094]

**Choose when**

- Memory or graph-backed knowledge must be fully in-estate or air-gapped in the EU and you can supply the controls [AJ]

**Avoid when**

- You want a managed service to carry certification evidence [AJ]

**Nearest competitors:** L5-zep, L5-mem0, L5-supermemory

**Regulated-FS note.** Self-host only, on an approved Postgres or Neo4j, behind the firm's identity proxy and audit logging; treat Cognee Cloud as out of scope for client data until certified [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Cognee (Berlin-based; GitHub org topoteretes) | Verified fact | A3-S005, A3-S095 |
| Category | Open-source AI memory platform building knowledge graphs plus vectors from documents, code and conversations | Verified fact | A3-S005 |
| Version / lineup | cognee 1.6.3 (7 October 2026) | Verified fact | A3-S005 |
| Licence | Open core: Apache-2.0 library; production-ready Postgres-as-graph store is a licensed product; Cognee Cloud managed service | Verified fact | A3-S005 |
| Strategic direction | Since 1.0, the whole memory layer can run on one Postgres instance (demo feature in OSS); small-model local extraction (GLiNER) without an LLM key; plugins and MCP for agents | Verified fact | A3-S005 |
| What it does | Turns documents, code and conversations into a self-hosted knowledge graph agents can search; operations include remember, recall, improve (enrich/apply feedback) and forget (remove an item or dataset); retrieval selects graph, vector or code context | Verified fact | A3-S005 |
| Stack position | Spans L5 memory and L6/L8 (ingestion into graph and vector stores); graphic's 'knowledge graphs' descriptor is accurate | Verified fact | A3-S005 |
| Integration | Python library, CLI, REST API (port 8000), UI and MCP server (port 8001) via Docker | Verified fact | A3-S005 |
| Dependencies | Default embedded stores: SQLite (relational), LanceDB (vector) and the 'ladybug' graph package; optional Neo4j, Amazon Neptune and Postgres/PGVector; Redis-compatible cache | Verified fact | A3-S005 |
| Certifications | Cognee states it does not currently hold SOC 2, ISO 27001 or equivalent third-party certification; recommends self-hosting in customer's certified environment | Verified fact | A3-S095 |
| GDPR / residency | EU company; GDPR-aligned processes audited with heyData; DPA on request; access, erasure and portability rights supported; Enterprise BYOC data plane in customer's EU cloud account; Cloud tenants each get a dedicated managed Postgres project | Verified fact | A3-S095 |
| Security features | Encryption at rest and in transit; private deployment mode with zero external API calls; air-gapped self-hosting | Verified fact | A3-S095 |
| Access controls | Multi-tenant mode with authenticated users by default (API); Enterprise SSO | Verified fact | A3-S005, A3-S095 |
| Enterprise support | Enterprise: SSO, SLAs, dedicated support engineer, BYOC (fixed-scope engagement, custom price) | Verified fact | A3-S095 |
| Pricing | Cloud free tier (1M tokens, one workspace); Standard US$1.00 per 1M tokens processed plus US$5 per extra workspace; Enterprise custom; self-hosted OSS free | Verified fact | A3-S095 |
| Infrastructure cost | Can run free locally with small models; production graph on Postgres requires a licence | Verified fact | A3-S005 |
| Ecosystem | Community plugins repository (cognee-community); MCP server | Verified fact | A3-S005, A3-S054 |
| Adoption signals | topoteretes/cognee 31,561 GitHub stars (7 October 2026); US$7.5M seed led by Pebblebed (February 2026, Reported) after US$1.5M (November 2024) | Verified fact | A3-S054, A3-S094 |
| Maturity | First PyPI release 13 March 2024; 178 releases; post-1.0 (1.6.x) | Verified fact | A3-S005 |
| Deployment | saas: Yes (Cognee Cloud); managed_cloud: Not publicly verified; vpc_byoc: Yes (Enterprise BYOC); private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes (on-prem and air-gapped self-hosting) | | |

## Amazon Bedrock AgentCore Memory (`L5-aws-agentcore-memory`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where AWS is your primary cloud and the agent runtime is AgentCore (CP3 Q2, rubric rule 10). AWS's lead managed agent memory service with good lifecycle documentation; a customer-managed key at creation and a pruner from day one are part of the condition, and deployment and lock-in at 2 are accepted under rule 11 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Short- and long-term memory with multiple extraction strategies, namespaces and self-managed pipelines |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1): AWS IAM, SSO federation and CloudTrail; AWS guidance on restricting memory APIs. Platform controls presumed (CP2 Q1); confirm per service |
| Security and compliance | 4 | Service-level SOC 1/2/3 and ISO 27001 scope plus CMK; SOC 2 report type not stated and Memory not named separately, so 4 not 5 (rule 8) |
| Deployment flexibility | 2 | AWS managed only, with VPC/PrivateLink connectivity; no self-host |
| Ecosystem | 3 | Strands SDK and AgentCore APIs; wider ecosystem NPV |
| Reliability and maturity | 3 | GA October 2025 with steady feature additions |
| Cost / TCO | 3 | Published unit pricing for short- and long-term memory (B-REVA-S005), changed on 6 October 2026; extraction LLM cost on top; transparent, so 3 (consistent with Memory Bank) |
| Lock-in / portability | 2 | Proprietary AWS API; records listable for export; hyperscaler lock-in |
| **Total (generic / FS)** | **3.30 / 3.20** | |

**Capabilities.** Managed memory in Amazon Bedrock AgentCore: short-term raw session events; long-term records via semantic, summary, user-preference, episodic or custom strategies, grouped by namespaces and retrieved by semantic search; self-managed strategy; record streaming; JSON-payload extraction (August 2026) [VF: A3-S111, A3-S047, V1-S087].

**Strengths**

- Detailed lifecycle documentation incl. per-user namespace erasure, batch delete and AWS guidance on retention policies [VF: A3-S111]
- KMS encryption with optional customer-managed key; AWS Config rule and Security Hub control flag memories without CMK [VF: B-L5-S002]
- AgentCore in AWS scope for SOC 1/2/3 and ISO/IEC 27001; HIPAA eligible [VF: B-L5-S003]
- VPC and PrivateLink [VF: A3-S047]

**Limitations and risks**

- No built-in TTL for long-term records; firm must build a pruner [VF: A3-S111]
- Harness-managed memory cannot be deleted via the Memory APIs [VF: A3-S111]
- Customer-managed key cannot be changed after creation for harness-managed memory [VF: B-L5-S002]
- AWS-only proprietary API [VF: A3-S047]; memory pricing changed on 6 October 2026 (short-term now per GB) [VF: B-REVA-S005]; EU Region availability for Memory not individually verified [VF: A3-S048] [NPV]

**Choose when**

- The agent runs on AgentCore or Strands in AWS [AJ]

**Avoid when**

- You need memory portable across clouds, or the runtime is elsewhere [AJ]

**Nearest competitors:** L5-gcp-vertex-memory-bank, L5-mem0, L5-zep

**Regulated-FS note.** Set a customer-managed key at creation, deploy the pruner on day one, confirm the Region list for UK/EU data, and keep a periodic export to the firm's store; platform controls presumed (CP2 Q1), confirm per service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Amazon Web Services | Verified fact | A3-S047 |
| Category | Cloud-platform managed agent memory service | Verified fact | A3-S047 |
| Version / lineup | Generally available since October 2025 as part of Amazon Bedrock AgentCore; AgentCore harness GA auto-provisions managed memory | Verified fact | A3-S047, A3-S048 |
| Licence | Proprietary managed service | Verified fact | A3-S047 |
| Status events | 13 October 2025: AgentCore GA (Memory included; nine Regions at launch, fifteen by October 2026); August 2026: extraction from non-conversational JSON payloads | Verified fact | A3-S047, A3-S111, V1-S087 |
| Strategic direction | Self-managed memory strategy gives control of extraction and consolidation pipelines; bundled into AgentCore harness | Verified fact | A3-S047, A3-S048 |
| What it does | Short-term memory stores raw session events (messages, tool calls); long-term memory extracts records via strategies (semantic, summary, user preference, episodic, custom model/prompt) retrievable by semantic search, grouped by namespaces | Verified fact | A3-S111 |
| Stack position | Platform-native alternative to independent L5 memory products | Architectural judgement |  |
| Integration | AgentCore APIs (CreateMemory, ListMemoryRecords, DeleteMemoryRecord, BatchDeleteMemoryRecords); record streaming events; Strands Agents SDK integration; JSON-payload extraction (August 2026) | Verified fact | A3-S111 |
| Dependencies | AWS account; part of Amazon Bedrock AgentCore | Verified fact | A3-S047 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | AgentCore available in 15 AWS Regions (EU regions not individually verified) | Verified fact | A3-S048 |
| Security features | VPC, PrivateLink, CloudFormation and tagging across AgentCore; event expiry for short-term events (7-365 days per API reference, minimum value conflict); no built-in TTL for long-term records (AWS recommends a pruner using timestamp filters); per-user erasure by listing and deleting namespace records; deleting a memory resource removes all events and records; harness-managed memory cannot be deleted via Memory APIs | Verified fact | A3-S047, A3-S111 |
| Access controls | AWS IAM (assumed from platform; not separately verified for Memory) | Architectural judgement |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GA October 2025 | Verified fact | A3-S047, V1-S087 |
| Deployment | saas: Yes (AWS managed); managed_cloud: Yes; vpc_byoc: VPC and AWS PrivateLink supported; private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## Vertex AI Agent Engine Memory Bank (newer docs: 'Agent Platform Memory Bank' in Gemini Enterprise Agent Platform) (`L5-gcp-vertex-memory-bank`)

**Tier:** Strategic · **Flags:** Renamed · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud and the agent runtime is Agent Engine (CP3 Q2, rubric rule 10). Google's lead managed agent memory service with a strong scope model; written confirmation of data residency (the feature table and residency terms conflict) and a regional CMEK endpoint are part of the condition [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Extraction, consolidation, scoping, TTL and revisions |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1): Google Cloud IAM, Cloud Audit Logs and SSO federation. Platform controls presumed (CP2 Q1); confirm per service |
| Security and compliance | 4 | Platform-level SOC 2, ISO 27001, ISO 42001 with product scope not stated (rule 8: one below the anchor of 5), plus CMEK and VPC-SC; residency conflict noted |
| Deployment flexibility | 2 | Google Cloud managed only; no self-host |
| Ecosystem | 3 | ADK, LangGraph and CrewAI samples |
| Reliability and maturity | 3 | Preview July 2025, GA December 2025, billing from January 2026; rebranding under way |
| Cost / TCO | 3 | Published per-memory pricing; extraction LLM billed separately |
| Lock-in / portability | 2 | Proprietary API; memories tied to Agent Runtime instance; Gemini dependency |
| **Total (generic / FS)** | **3.30 / 3.20** | |

**Capabilities.** Managed long-term memory in Google's agent platform: Gemini-based asynchronous extraction of facts and preferences, consolidation with contradiction resolution, exact-scope retrieval with optional similarity search; TTL optional; revisions; purge by filter [VF: A3-S108, A3-S109].

**Strengths**

- Immutable scope with exact-scope retrieval [VF: A3-S109]
- Consolidation resolves contradictions; purge by filter with dry run [VF: A3-S109]
- Transparent unit pricing: US$0.25 per 1,000 stored, US$0.50 per 1,000 retrieved (LLM billed separately) [VF: V1-S088]
- VPC-SC, CMEK and data residency at rest listed for Memory Bank [VF: B-L5-S004]

**Limitations and risks**

- CMEK not available on the global endpoint; data residency terms list Memory Bank as excluded, conflicting with the feature table [VF: B-L5-S004]
- TTL default none; memory revisions kept 365 days by default [VF: A3-S109]
- Memories deleted with the Agent Runtime instance; extraction depends on Gemini [VF: A3-S109, A3-S108]
- Platform certifications (SOC 2, ISO 27001, ISO 42001) stated per product or feature; Memory Bank inclusion not stated [VF: A2-S043] [NPV]

**Choose when**

- The agent runs on ADK or Agent Engine in Google Cloud [AJ]

**Avoid when**

- You need cross-cloud portability or confirmed UK/EU at-rest residency before Google confirms it in writing [AJ]

**Nearest competitors:** L5-aws-agentcore-memory, L5-mem0, L5-zep

**Regulated-FS note.** Use a regional endpoint with CMEK, set TTL and a shorter revision retention, and obtain written residency confirmation; platform controls presumed (CP2 Q1), confirm per service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google Cloud | Verified fact | A3-S108 |
| Category | Cloud-platform managed agent long-term memory service | Verified fact | A3-S108 |
| Version / lineup | Public preview 8 July 2025; release notes state Sessions and Memory Bank generally available (date not captured); usage charging from 28 January 2026 | Verified fact | A3-S108, A3-S109 |
| Licence | Proprietary managed service | Verified fact | A3-S108 |
| Status events | 8 July 2025: public preview; December 2025: Agent Engine Sessions and Memory Bank GA (Vertex AI release notes; exact day not captured); 28 January 2026: billing starts | Verified fact | A3-S108, A3-S109, V1-S088 |
| Strategic direction | Integrated with Agent Development Kit and Agent Engine Sessions; samples for LangGraph and CrewAI; rebranding under Gemini Enterprise Agent Platform | Verified fact | A3-S108, A3-S109 |
| What it does | Uses Gemini models to extract facts, preferences and context asynchronously from conversation history, consolidates them with existing memories (resolving contradictions), and retrieves them by scope (e.g. user ID) with optional embedding similarity search | Verified fact | A3-S108, A3-S109 |
| Stack position | Platform-native alternative to independent L5 memory products | Architectural judgement |  |
| Integration | REST API and Vertex AI SDK; ADK memory service; LangGraph and CrewAI samples | Verified fact | A3-S108, A3-S109 |
| Dependencies | Google Cloud project; Agent Engine Sessions as a source; Gemini models | Verified fact | A3-S108 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Scope is immutable and retrieval returns only exact-scope matches; optional TTL (default none; memory revisions default 365 days); delete by name and purge by filter with dry run; consolidation may delete contradicted memories or honour explicit 'forget' instructions; deleting the Agent Runtime instance deletes built-in memories | Verified fact | A3-S109 |
| Access controls | Google Cloud IAM (assumed from platform; not separately verified) | Architectural judgement |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | US$0.25 per 1,000 memories stored and US$0.50 per 1,000 memories retrieved; LLM usage for memory generation billed separately; charging began 28 January 2026 | Verified fact | A3-S109, V1-S088 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | ADK, LangGraph, CrewAI | Verified fact | A3-S108 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Preview 8 July 2025; GA December 2025; billing from 28 January 2026 | Verified fact | A3-S108, A3-S109, V1-S088 |
| Deployment | saas: Yes (Google Cloud managed); managed_cloud: Yes; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## Supermemory (`L5-supermemory`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** Supermemory – memory API

*Rationale:* Fast-moving combined memory-and-RAG API with a proprietary server, seed funding and an API that changed major version this week [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Memory, profiles, forgetting and hybrid RAG in one API |
| Enterprise readiness | 3 | SSO on Enterprise verified (protocols undocumented) (A3-S096): one verified control lifts the cap to 3 under rule 7 (CP3 review A, consistent with LlamaParse and Browserbase); RBAC and audit logs NPV |
| Security and compliance | 2 | SOC 2 claimed from Scale tier with report type unconfirmed; HIPAA Enterprise; DPA |
| Deployment flexibility | 5 | SaaS, dedicated, customer cloud, self-host (Scale+), air-gap (Enterprise) |
| Ecosystem | 4 | Framework wrappers, MCP, coding-agent plugins |
| Reliability and maturity | 2 | SDK first released April 2025; v5 breaking change 6 October 2026; seed only; no acquisition found |
| Cost / TCO | 3 | Published tiers (Pro US$19 to Scale US$399 per month); self-hosting only on higher tiers |
| Lock-in / portability | 2 | Proprietary server binary and API; namespace API just changed |
| **Total (generic / FS)** | **3.30 / 3.05** | |

*Evidence rules applied:* security_compliance at 2: SOC 2 report type not confirmed (pricing page only); enterprise_readiness: NPV cap lifted to 3 by verified SSO (rule 7)

**Capabilities.** Memory and context engine API: fact extraction, user profiles, temporal and contradiction handling, automatic forgetting, hybrid search over documents and memories, connectors and file processing; v5 namespace-first API [VF: A3-S064, A3-S012].

**Strengths**

- Explicit forget operations: forget, forget_matching, namespace delete, automatic expiry [VF: A3-S012, A3-S064]
- Wide deployment range incl. customer-cloud dedicated deployments and air-gapped Enterprise [VF: A3-S122, A3-S096]
- Many framework wrappers and an MCP server [VF: A3-S064]

**Limitations and risks**

- Self-hosted server binary not open source; hosted API proprietary [VF: A3-S066, A3-S096]
- SOC 2 report type not confirmed on pricing page; no managed EU region found [VF: A3-S096, A3-S122]
- SSO protocols undocumented; RBAC and audit logs not documented [VF: A3-S096] [NPV]
- v5 breaking API change on 6 October 2026 [VF: A3-S012]
- Bundles memory and knowledge behind one API, blurring owner-curated and agent-written content [AJ]
- Benchmark leadership is a vendor claim [R: A3-S064]

**Choose when**

- A team prototype needs memory plus RAG quickly, outside regulated data [AJ]

**Avoid when**

- Memory and knowledge need different owners, approvals and retention, or you need a stable API [AJ]

**Nearest competitors:** L5-mem0, L5-zep, L5-cognee

**Regulated-FS note.** Not for client or personal data until SOC 2 report type, audit logging and EU residency are confirmed [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Supermemory | Verified fact | A3-S064 |
| Category | Memory and context engine API: memory extraction, user profiles, hybrid RAG search, connectors and file processing | Verified fact | A3-S064 |
| Version / lineup | Python SDK 5.0.0 (6 October 2026) for the namespace-first v5 API (breaking change from 3.x) | Verified fact | A3-S012 |
| Licence | Open core: repository MIT and SDK Apache-2.0, but the self-hosted server binary is not open source (free within a lite licence); hosted API proprietary | Verified fact | A3-S066, A3-S012, A3-S096 |
| Status events | 6 October 2026: v5 SDK moves to namespace-first API (MIGRATION from 3.x required) | Verified fact | A3-S012 |
| Strategic direction | Bundles memory with RAG, connectors and multimodal extractors in one API; plugins for Claude Code, Cursor, Codex, OpenCode and others; vendor claims #1 on LongMemEval, LoCoMo and ConvoMem | Verified fact | A3-S064 |
| What it does | Extracts facts from conversations, maintains user profiles, handles temporal changes and contradictions, automatically forgets expired information and returns context via hybrid search over documents and memories | Verified fact | A3-S064 |
| Stack position | Combines L5 memory, L6 retrieval and L8 ingestion (connectors, OCR, transcription) behind one API | Verified fact | A3-S064 |
| Integration | REST API, Python/TypeScript SDKs, hosted MCP server, framework wrappers (Vercel AI SDK, LangChain, LangGraph, OpenAI Agents SDK, Mastra, Agno, Claude Memory Tool, n8n); connectors for Google Drive, Gmail, Notion, OneDrive and GitHub | Verified fact | A3-S064, A3-S012 |
| Dependencies | Self-hosted build embeds a graph engine and local embeddings (bge-base-en-v1.5 by default) and stores data in a local directory; any OpenAI-compatible LLM | Verified fact | A3-S064 |
| Certifications | SOC 2 (from Scale tier) and HIPAA on Enterprise per pricing page; blog posts say SOC 2 Type 2 (report type not confirmed on pricing page) | Verified fact | A3-S096 |
| GDPR / residency | Security page states GDPR compliant with access and erasure workflows; DPA signed on request; no managed EU region found; dedicated deployments in customer AWS/GCP/Azure for residency | Verified fact | A3-S122, A3-S096 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | SSO on Enterprise tier (protocols not documented); namespaces isolate content | Verified fact | A3-S096, A3-S012 |
| Enterprise support | Enterprise: custom contracts, DPA, SSO, custom integrations | Verified fact | A3-S096 |
| Pricing | Free (US$5 monthly credits); Pro US$19; Max US$100; Scale US$399 per month; Enterprise custom | Verified fact | A3-S096 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Plugins for coding agents and MCP clients; framework wrappers listed above | Verified fact | A3-S064 |
| Adoption signals | supermemoryai/supermemory 31,146 GitHub stars (7 October 2026); seed US$2.6M (October 2025, later reported as US$3M) led by Susa Ventures, Browder Capital and SF1.vc (Reported) | Verified fact | A3-S054, A3-S097 |
| Maturity | Python SDK first released 29 April 2025; 87 releases; v5 API just released | Verified fact | A3-S012 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (dedicated deployment in customer AWS, GCP or Azure account); private_cloud: Yes (dedicated infrastructure run by Supermemory); self_hosted: Yes: Supermemory local free for individuals within a lite licence (server binary not open source); organisational self-hosting on Scale and Enterprise; on_prem: Yes (Enterprise air-gapped self-hosting) | | |

## Letta (formerly MemGPT); current product is Letta Code, a stateful agent harness, with Letta Cloud (`L5-letta`)

**Tier:** Experimental · **Flags:** Superseded · **Original graphic label:** Letta – stateful agents

*Rationale:* Repositioned as an agent harness with changing architecture and no certification; belongs with L3 harness evaluation [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Memory blocks and MemFS within its own harness; not usable as a memory layer for other frameworks |
| Enterprise readiness | 3 | RBAC and SAML/OIDC SSO on Enterprise (two of three); audit logs NPV; dedicated support |
| Security and compliance | 2 | No certification found |
| Deployment flexibility | 3 | Letta Cloud SaaS and self-hosted server; on-prem and VPC NPV |
| Ecosystem | 3 | Model-agnostic; skills ecosystem; but a harness rather than an integration point |
| Reliability and maturity | 2 | Pre-1.0 Letta Code launched October 2025; architecture changed twice; no acquisition found |
| Cost / TCO | 4 | Apache-2.0; Pro US$20 per month; free with own model keys |
| Lock-in / portability | 3 | Apache-2.0 and git-backed memory files are portable, but agent state defaults to Letta Cloud and AgentFile export was removed |
| **Total (generic / FS)** | **2.85 / 2.75** | |

*Evidence rules applied:* security_compliance capped at 2: certifications NPV (none found, A3-S118)

**Capabilities.** Stateful agent harness (Letta Code) with memory blocks and all context tracked in a git-backed memory filesystem (MemFS) that can sync to GitHub; Letta Cloud default backend or self-hosted 'letta server'; not a standalone memory layer [VF: A3-S073, A3-S060, A3-S093].

**Strengths**

- Memory as version-controlled files: every change is a reviewable diff [VF: A3-S073]
- Model-agnostic; works with OpenAI, Anthropic, Z.ai and local models [VF: A3-S073]
- Enterprise RBAC and SAML/OIDC SSO [VF: A3-S091]
- Apache-2.0 licence [VF: A3-S004, A3-S077]

**Limitations and risks**

- Pivot in March 2026: server memory tools, templates, server-side sleep-time agents and tool rules deprecated; V1 server retired [VF: A3-S093, A3-S060]
- AgentFile export/import removed [VF: A3-S073]
- No SOC 2 or trust centre found; privacy policy states no specific retention periods [VF: A3-S118]
- Pre-1.0 with very rapid releases (eight in six days) [VF: A3-S077, A3-S004]
- Git history retains deleted content unless rewritten, complicating erasure [AJ]

**Choose when**

- Evaluating a stateful coding or operations agent outside regulated client data [AJ]

**Avoid when**

- You need a memory service for an existing LangGraph, ADK or Strands workflow [AJ]
- Certifications are a gate [AJ]

**Nearest competitors:** L5-langmem, L5-aws-agentcore-memory, L5-gcp-vertex-memory-bank

**Regulated-FS note.** Copy the git-backed memory idea for governed style memory in the firm's own repository; do not adopt the product as a regulated-workflow dependency today [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Letta (letta-ai) | Verified fact | A3-S060 |
| Category | Stateful agent harness/runtime with self-editing memory; not a standalone memory library | Verified fact | A3-S073 |
| Version / lineup | Letta Code 0.34.4 (4 October 2026; PyPI 'letta' and npm '@letta-ai/letta-code'); letta-client Python SDK 1.12.1 (2 June 2026) | Verified fact | A3-S004, A3-S077, A3-S014 |
| Licence | Open source Apache-2.0 (Letta Code); Letta Cloud hosted service | Verified fact | A3-S004, A3-S077, A3-S073 |
| Status events | Letta V1 API server retired to an 'archive' branch; active source moved to letta-ai/letta-code (status on 7 October 2026); PyPI package 'letta' now installs the Letta Code CLI, 'not a Python SDK or API server'; AgentFile (.af) export/import deprecated and removed from Letta Code; lettabot repository archived, replaced by Letta Code channels | Verified fact | A3-S060, A3-S004, A3-S073, A3-S054, V1-S081 |
| Strategic direction | 'Letta's Next Phase' (March 2026): Letta Code as model-agnostic agent harness with git-backed memory (MemFS); legacy server memory tools (e.g. core_memory_replace), templates, server-side sleep-time agents and tool rules deprecated. Letta Code launched December 2025; desktop app April 2026 | Verified fact | A3-S093, A3-S073, V1-S042 |
| What it does | Runs long-lived agents with memory, identity and conversation history; memory blocks and all context are tracked in a git-backed memory filesystem (MemFS) that can sync to a GitHub repository; supports message search across agents, subagents, hooks, permissions and secrets | Verified fact | A3-S073 |
| Stack position | Straddles L3 (agent harness) and L5 (memory); the graphic's 'stateful agents' descriptor is accurate, but Letta is not a drop-in memory layer for other frameworks | Verified fact | A3-S073 |
| Integration | Letta Agent SDK (TypeScript), letta-client for the Letta API (Python), 'letta server' App Server, Agent Skills folders (.agents/skills), messaging channels | Verified fact | A3-S060, A3-S004, A3-S073 |
| Dependencies | Bring-your-own LLM provider keys; Letta Cloud is the default backend storing agent state; local mode keeps agents on disk; Python wheel bundles a Node.js runtime | Verified fact | A3-S004, A3-S073 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Privacy policy: model inputs/outputs retained only for hosted services; no specific retention periods; agent state (memories, messages, tool calls) persisted in a database and retrievable after compaction | Verified fact | A3-S118 |
| Security features | Secrets feature exposes secrets as environment variables while obfuscating values from context (requires Letta sign-in) | Verified fact | A3-S073 |
| Access controls | Enterprise tier: RBAC and SAML/OIDC SSO; Letta Code permission modes for agent actions | Verified fact | A3-S091, A3-S073 |
| Enterprise support | Enterprise tier with dedicated support | Verified fact | A3-S091 |
| Pricing | Pro US$20/month with usage quota and pay-as-you-go overage (up to 20 stateful agents); LLM usage at underlying token cost; free with own model keys; Enterprise volume pricing | Verified fact | A3-S091 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Works with OpenAI, Anthropic, Z.ai and local models; installs skills from GitHub, ClawHub and Hermes Skills Hub | Verified fact | A3-S073 |
| Adoption signals | letta-ai/letta 25,070 and letta-code 3,541 GitHub stars (7 October 2026). US$10M seed led by Felicis (September 2024, Reported); no later round found | Verified fact | A3-S054, A3-S092 |
| Maturity | Letta Code first published 24 October 2025; pre-1.0 with very rapid releases (eight releases 29 September to 4 October 2026) | Verified fact | A3-S077, A3-S004 |
| Deployment | saas: Yes (Letta Cloud); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes ('letta server' for local or self-hosted agents); on_prem: Not publicly verified | | |

## LangMem (`L5-langmem`)

**Tier:** Experimental · **Flags:** Not publicly verified · **Original graphic label:** LangMem – long-term

*Rationale:* Pre-1.0 and apparently stalled; useful as patterns, not as a dependency [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Extraction, consolidation and procedural memory, but no lifecycle or erasure features documented |
| Enterprise readiness | 2 | Rule 2: enables memory inside LangGraph; no commercial support for LangMem itself verified |
| Security and compliance | 2 | Rule 2: security policy, CVE handling and signed releases NPV |
| Deployment flexibility | 4 | Library runs wherever LangGraph and its store run, incl. in-estate |
| Ecosystem | 3 | LangGraph and LangChain only |
| Reliability and maturity | 1 | Pre-1.0 (0.0.x) with no release for about 11 months |
| Cost / TCO | 4 | MIT and free; cost is store plus extraction LLM; a stalled library may need in-house maintenance |
| Lock-in / portability | 3 | MIT, but bound to LangGraph store abstractions |
| **Total (generic / FS)** | **2.75 / 2.65** | |

*Evidence rules applied:* Rule 2 applied (self-hosted library; inherits host controls): security_compliance and enterprise_readiness capped at 4

**Capabilities.** MIT library of memory utilities for LangGraph: extraction, hot-path memory tools, background memory manager and prompt refinement (procedural memory); persists via LangGraph BaseStore [VF: A3-S006].

**Strengths**

- Clear example of procedural memory (prompt refinement) and background consolidation [VF: A3-S006]
- No service to operate; MIT licence [VF: A3-S006]

**Limitations and risks**

- 0.0.30, no PyPI release since 27 October 2025 [VF: A3-S006]
- Tied to LangGraph store abstractions; InMemoryStore loses data on restart [VF: A3-S006]
- Whether LangChain has superseded it is not verified [NPV]
- Security and access control inherit entirely from the store and platform [AJ]

**Choose when**

- Already on LangGraph and want reference patterns, accepting you may maintain the code [AJ]

**Avoid when**

- You need a supported dependency [AJ]

**Nearest competitors:** L5-mem0, L5-zep, L5-letta

**Regulated-FS note.** Never let automatic prompt refinement change production prompts; route proposals through C5 change control [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LangChain | Verified fact | A3-S006 |
| Category | Open-source memory utilities library for LangGraph agents | Verified fact | A3-S006 |
| Version / lineup | langmem 0.0.30 (27 October 2025); no newer PyPI release as of 7 October 2026 | Verified fact | A3-S006 |
| Licence | Open source, MIT | Verified fact | A3-S006 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Extracts information from conversations, provides hot-path memory management/search tools for agents, a background memory manager that consolidates knowledge, and prompt refinement to optimise agent behaviour | Verified fact | A3-S006 |
| Stack position | Library inside L3 (LangGraph) using LangGraph's long-term memory store; not a separate memory service | Verified fact | A3-S006 |
| Integration | Python API; native integration with LangGraph long-term memory store, available in LangGraph Platform deployments | Verified fact | A3-S006 |
| Dependencies | langgraph, langchain-core, langsmith and trustcall; persistence via LangGraph BaseStore (InMemoryStore loses data on restart) | Verified fact | A3-S006 |
| Certifications | Not applicable (library); inherits controls of the hosting platform and store | Architectural judgement |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (MIT library) | Verified fact | A3-S006 |
| Infrastructure cost | Cost driven by the chosen LangGraph store backend and LLM calls for extraction | Verified fact | A3-S006 |
| Ecosystem | LangGraph/LangChain ecosystem | Verified fact | A3-S006 |
| Adoption signals | langchain-ai/langmem 1,696 GitHub stars (7 October 2026) | Verified fact | A3-S054 |
| Maturity | Pre-1.0 (0.0.x); last PyPI release 27 October 2025, about 11 months before review date | Verified fact | A3-S006 |
| Deployment | saas: No standalone SaaS (runs inside LangGraph Platform deployments); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (library); on_prem: Yes (library) | | |

# L4: Tools, protocols and connectivity

## Agent2Agent (A2A) Protocol (`L4-a2a`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** A2A – agent-to-agent

*Rationale:* Strategic, conditional: where cross-team or cross-vendor agent delegation is in scope (CP3 Q1); signed Agent Cards verified, and delegated authority scoped and revocable by the firm, because the protocol does not define it [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers agent-to-agent interop well; not the main tool-invocation path and delegation semantics incomplete [AJ] |
| Enterprise readiness | 3 | Open spec (rule 2): authenticated extended cards and declared security schemes; support via implementers [VF: A3-S078] |
| Security and compliance | 3 | Rule 2 hygiene: modern OAuth flows, optional signing, undefined revocation semantics [VF: A3-S078, A3-S079] |
| Deployment flexibility | 5 | Implementations self-hostable anywhere [AJ] |
| Ecosystem | 4 | 150+ organisations and cloud availability (April 2026) [VF: A3-S025] |
| Reliability and maturity | 3 | 1.0 only since March 2026 with breaking changes; foundation-hosted [VF: A3-S079, A3-S116] |
| Cost / TCO | 4 | Free specification; operations cost in implementations [AJ] |
| Lock-in / portability | 5 | Apache-2.0 with neutral multi-vendor governance [VF: A3-S075, A3-S065] |
| **Total (generic / FS)** | **3.60 / 3.70** | |

**Capabilities.** Open protocol (Apache-2.0) for communication between opaque agents: Agent Card discovery, messages, long-running tasks with streaming and push notifications; v1.0 adds multi-tenancy, multiple bindings, optional JWS-signed Agent Cards and modernised OAuth flows [VF: A3-S078, A3-S030, A3-S079].

**Strengths**

- Multi-vendor TSC of eight companies and AAIF Growth Stage status [VF: A3-S065, A3-S117]
- Designed for delegated long-running tasks between agents [VF: A3-S078]
- Signed Agent Cards available [VF: A3-S078]

**Limitations and risks**

- Card signing optional; clients SHOULD verify only when present [VF: A3-S078]
- No defined scope, validity or revocation semantics for authorisation obtained in AUTH_REQUIRED [VF: A3-S078]
- 1.0 broke the interaction protocol; some SDKs lag [VF: A3-S079] [R: A3-S030]

**Choose when**

- Agents owned by different teams or vendors must delegate work to each other [AJ]

**Avoid when**

- A deterministic workflow calling tools would do [AJ]

**Nearest competitors:** L4-mcp, C1-agentgateway, L4-aws-agentcore-gateway-identity

**Regulated-FS note.** Require signed Agent Cards and verify them; scope and revoke delegated authority in your own gateway and IdP [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | A2A Project: contributed by Google to the Linux Foundation (2025); accepted as a Growth Stage project of the Agentic AI Foundation (AAIF announcement 17 August 2026; A2A blog 27 August 2026); TSC seats: Google, Microsoft, Cisco, AWS, Salesforce, ServiceNow, SAP, IBM | Verified fact | A3-S065, A3-S116, A3-S117, A3-S025, V1-S039 |
| Category | Open protocol for communication and interoperability between opaque agent applications | Verified fact | A3-S078 |
| Version / lineup | Specification 1.0.0 (12 March 2026), patch 1.0.1 (26 May 2026); A2A Python SDK a2a-sdk 1.2.2 (5 October 2026) | Verified fact | A3-S079, A3-S078, A3-S075, V1-S039 |
| Licence | Open specification and SDKs, Apache-2.0 | Verified fact | A3-S075, A3-S025 |
| Status events | August 2025: IBM's Agent Communication Protocol (ACP) merged into A2A; IBM joined the TSC; 12 March 2026: A2A 1.0.0, first stable release (changelog; AAIF and Google also say March 2026; the 9 April 2026 Linux Foundation release is the one-year anniversary announcement); 26 May 2026: A2A 1.0.1; 17 August 2026: AAIF announced A2A joining; A2A blog (27 August 2026) confirms acceptance as AAIF Growth Stage project | Verified fact | A3-S032, A3-S065, A3-S079, A3-S116, A3-S026, A3-S025, A3-S117, V1-S039, V1-S038 |
| Strategic direction | v1.0 adds multi-tenancy, multi-protocol bindings, verb-style operations, signed Agent Cards and modernised OAuth flows; joined AAIF alongside MCP as separate project with own TSC (August 2026) | Verified fact | A3-S030, A3-S040 |
| What it does | Lets a client agent discover a remote agent via its Agent Card (/.well-known/agent-card.json), send messages and manage asynchronous, long-running tasks with streaming and push notifications; version negotiated via A2A-Version header | Verified fact | A3-S078, A3-S030 |
| Stack position | L4 agent-to-agent interoperability, complementary to MCP (agent-to-tool) | Verified fact | A3-S040 |
| Integration | Official SDKs (Python, JavaScript and others); Agent Cards advertise supportedInterfaces with protocol binding and version | Verified fact | A3-S075, A3-S031, A3-S054 |
| Dependencies | HTTP-based bindings (JSON-RPC, gRPC, REST); security via declared securitySchemes incl. OAuth 2.0 and OpenID Connect | Verified fact | A3-S078 |
| Certifications | Not applicable (open specification) | Architectural judgement |  |
| GDPR / residency | Not applicable (open specification) | Architectural judgement |  |
| Security features | Agent Cards MAY be signed with JWS (RFC 7515) over RFC 8785-canonicalised JSON; clients SHOULD verify when present. OAuth flows modernised (device code, PKCE; implicit/password removed). The protocol does not define scope, validity or revocation semantics for authorisation obtained in the AUTH_REQUIRED task state | Verified fact | A3-S078, A3-S079, A3-S031 |
| Access controls | Authenticated extended Agent Card available only after client authenticates with a declared scheme | Verified fact | A3-S078 |
| Enterprise support | Not applicable (community specification) | Architectural judgement |  |
| Pricing | Free open specification | Verified fact | A3-S075 |
| Infrastructure cost | Not applicable | Architectural judgement |  |
| Ecosystem | More than 150 supporting organisations and availability in major cloud platforms (April 2026) | Verified fact | A3-S025 |
| Adoption signals | a2aproject/A2A 26,049 GitHub stars (7 October 2026); 150+ organisations (April 2026) | Verified fact | A3-S054, A3-S025 |
| Maturity | First public spec 2025; 1.0 stable March 2026 with breaking changes to the interaction protocol (Agent Card backward-compatible) | Verified fact | A3-S079, A3-S030 |
| Deployment | saas: No (open specification; deployment depends on each implementation); managed_cloud: No (open specification; deployment depends on each implementation); vpc_byoc: No (open specification; deployment depends on each implementation); private_cloud: No (open specification; deployment depends on each implementation); self_hosted: Yes (implementations can be self-hosted; the specification itself is not a hosted service); on_prem: Yes (implementations can be self-hosted; the specification itself is not a hosted service) | | |

## Model Context Protocol (MCP) (`L4-mcp`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** MCP – tools standard

*Rationale:* Strategic, conditional: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions. Tier set by the reader at Checkpoint 3 (CP3 Q1), treating MCP and its authorisation profile (C4-mcp-authorization) as one decision; FS 3.55 is below the 3.6 guide and security scores 2, which is why the condition is mandatory. Conflict of interest: MCP originated at Anthropic and the author is an Anthropic model [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Covers tool invocation, enterprise authorisation and long-running tasks; security enforcement (allow-listing, signing) left outside the spec [AJ] |
| Enterprise readiness | 3 | Open spec (rule 2): enables central IdP policy via EMA; no commercial support from the project itself [AJ] |
| Security and compliance | 2 | Rule 2 hygiene: advisories are published with fixes (B-REVA-S006), but the specification leaves authorisation optional, has no tool-definition signing, carries a documented tool-poisoning attack class, and the TypeScript SDK had several High advisories in 2026, including one sending OAuth credentials to a server-chosen authorisation server [VF: A3-S055, A3-S023, B-REVA-S006]. Below A2A (optional card signing) on integrity; borderline 3/2 resolved against the Anthropic-originated item (CP3 review A) |
| Deployment flexibility | 5 | Implementations run anywhere, including stdio locally and air-gapped [AJ] |
| Ecosystem | 5 | De facto standard with broad client and launch-partner support [VF: A3-S015, A3-S018] |
| Reliability and maturity | 3 | Foundation-hosted with a 12-month deprecation policy, but breaking changes in July 2026 and Registry still preview [VF: A3-S015, A3-S042] |
| Cost / TCO | 4 | Free specification and SDKs; cost lies in operating servers, gateway and authorisation server [AJ] |
| Lock-in / portability | 4 | MIT under AAIF, but technical direction concentrated in Anthropic maintainers, so not fully neutral governance [VF: A3-S082] |
| **Total (generic / FS)** | **3.70 / 3.55** | |

**Capabilities.** Open protocol (MIT) for connecting agent hosts to tools, resources and prompts over JSON-RPC; spec 2026-07-28 is stateless with Mcp-Method/Mcp-Name headers for gateway routing, Tasks for long-running work, an optional OAuth 2.1 authorisation profile (RFC 8707, RFC 9728, RFC 9207, PKCE, no token passthrough) and the stable Enterprise-Managed Authorization extension (ID-JAG) [VF: A3-S015, A3-S057, A3-S055, A3-S056, A3-S017]. Conflict of interest: originated at Anthropic; author is an Anthropic model [AJ].

**Strengths**

- De facto agent-to-tool contract with Tier 1 SDKs in TypeScript, Python, Go and C# and client support across major vendors [VF: A3-S015, A3-S018]
- Header-based routing makes gateway enforcement practical [VF: A3-S015]
- EMA gives central IdP policy and one audit trail [VF: A3-S017]
- Hosted by AAIF (Linux Foundation) since 9 December 2025 [VF: A3-S018, V1-S038]

**Limitations and risks**

- Authorisation is OPTIONAL in the specification [VF: A3-S055]
- Tool annotations are untrusted hints [VF: A3-S020]
- Tool poisoning: 36.5% average attack success across 20 models in MCPTox [VF: A3-S023]; OWASP MCP03 tool poisoning [VF: A3-S045]
- IDE clients (including Claude Code) had high-severity auto-execution issues [R: A3-S022]
- Both Lead Maintainers are Anthropic staff; AAIF does not set technical direction [VF: A3-S082, A3-S018]
- Official Registry still preview, API v0.1, denylist moderation [VF: A3-S019, A3-S042, A3-S036]
- 2026-07-28 contained breaking changes and deprecations (Roots, Sampling, Logging, DCR) [VF: A3-S015, V2-S031]
- 2026 TypeScript SDK advisories include GHSA-6qxp-vccf-f47h (High: OAuth credentials sent to a server-chosen authorisation server; the fix also needs expectedIssuer configured), GHSA-22jm-h49p-29qw (High) and CVE-2026-25536 (High) [VF: B-REVA-S006]

**Choose when**

- One tool contract is needed across several agent frameworks and model vendors [AJ]

**Avoid when**

- Clients would connect directly to third-party servers without a gateway, private registry and pinned definitions [AJ]

**Nearest competitors:** OpenAPI tool definitions via gateway, L4-a2a, L4-aws-agentcore-gateway-identity

**Regulated-FS note.** Adopt the protocol, not the public ecosystem: internal servers behind a firm-owned gateway with authorisation mandatory and definitions hash-pinned; independent alternative is OpenAPI-described tools exposed through a gateway [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Open-source project hosted by the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation; originated at Anthropic (created by David Soria Parra and Justin Spahr-Summers) and donated on 9 December 2025 | Verified fact | A3-S018, A3-S058, V1-S038 |
| Category | Open protocol specification for connecting agents/LLM applications to tools, resources and prompts | Verified fact | A3-S058, A3-S015 |
| Version / lineup | Specification 2026-07-28 (released 28 July 2026; previous 2025-11-25). Tier 1 SDKs: TypeScript, Python, Go, C#; Python 'mcp' 2.3.0 (2 October 2026); TypeScript '@modelcontextprotocol/sdk' 1.32.1 (5 October 2026) | Verified fact | A3-S015, A3-S057, A3-S011, A3-S074, V1-S037 |
| Licence | Open specification; specification repository and SDKs MIT-licensed | Verified fact | A3-S058, A3-S011, A3-S074 |
| Status events | 9 December 2025: donated by Anthropic to the Agentic AI Foundation (Linux Foundation); maintainer structure unchanged; 8 September 2025: official MCP Registry launched in preview; API frozen at v0.1 (24 October 2025); Registry working-group charter lists 'Registry API v1 GA' as Ideating with no target date; /v0.1 live and /v1 absent on 7 October 2026; 18 June 2026: Enterprise-Managed Authorization extension declared stable; 28 July 2026: spec 2026-07-28 removes sessions and the initialize handshake (stateless core), adds Multi Round-Trip Requests, header-based routing, cacheable lists, extensi | Verified fact | A3-S015, A3-S017, A3-S018, A3-S019, A3-S036, A3-S042, A3-S057, A3-S082, A3-S114, V1-S037, V1-S038, V1-S045 |
| Strategic direction | Roadmap (22 August 2026): agentic messaging primitives (server-initiated events, Tasks), HTTP-native transport unification, agent identity and enterprise security (DPoP, Workload Identity Federation, ID-JAG, token exchange; engagement with IETF OAuth and WIMSE), progressive tool discovery for large catalogues, SDK conformance | Verified fact | A3-S016 |
| What it does | Defines how clients (agent hosts) discover and call server-exposed tools, resources and prompts over JSON-RPC; as of 2026-07-28 each request is self-describing and stateless, with optional server/discover, and long-running work via the Tasks extension | Verified fact | A3-S015, A3-S057 |
| Stack position | L4 connectivity standard; the 2026-07-28 release puts method and tool names in Mcp-Method/Mcp-Name HTTP headers so gateways, rate limiters and WAFs can route and authorise without parsing bodies | Verified fact | A3-S015 |
| Integration | Open protocol with official SDKs (TypeScript, Python, Go, C# Tier 1; Rust beta); first-class client support reported in ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot and VS Code (December 2025) | Verified fact | A3-S015, A3-S018 |
| Dependencies | Transports stdio and Streamable HTTP; remote authorisation relies on an external OAuth 2.1 authorisation server | Verified fact | A3-S055, A3-S057 |
| Certifications | Not applicable (open specification) | Architectural judgement |  |
| GDPR / residency | Not applicable (open specification) | Architectural judgement |  |
| Security features | Authorisation is OPTIONAL. When used: OAuth 2.1 (draft-13) with PKCE; servers MUST publish Protected Resource Metadata (RFC 9728); clients MUST send Resource Indicators (RFC 8707); servers MUST validate token audience; token passthrough forbidden; RFC 9207 issuer validation; DCR deprecated for Client ID Metadata Documents. Tool annotations are untrusted hints | Verified fact | A3-S055, A3-S056, A3-S057, A3-S020 |
| Access controls | Enterprise-Managed Authorization extension (stable 18 June 2026): IdP issues an Identity Assertion JWT Authorization Grant (ID-JAG) exchanged for MCP access tokens, giving central policy and audit; Okta (Cross App Access) first IdP; adopted by Anthropic clients, VS Code and servers incl. Asana, Atlassian, Canva, Figma, Linear and Supabase | Verified fact | A3-S017 |
| Enterprise support | Not applicable (community specification); support comes from implementers | Architectural judgement |  |
| Pricing | Free open specification and SDKs | Verified fact | A3-S058, A3-S011 |
| Infrastructure cost | Cost lies in hosting MCP servers, gateways and the authorisation server | Architectural judgement |  |
| Ecosystem | Launch partners for 2026-07-28 include AWS (AgentCore; Tasks extension contributed by AWS), Cloudflare, Google Cloud, Microsoft Foundry, Figma, Netlify, Supabase, Honeycomb, FastMCP/Horizon and Runlayer; official Registry with public and private sub-registries | Verified fact | A3-S015, A3-S019 |
| Adoption signals | 97M monthly SDK downloads and 10,000 active servers (December 2025); close to 0.5bn monthly downloads across Tier 1 SDKs and >1bn total each for TypeScript and Python (July 2026, project claim); modelcontextprotocol/servers 91,068 GitHub stars | Verified fact | A3-S018, A3-S015, A3-S054 |
| Maturity | Initial release November 2024 (first SDK on PyPI 20 November 2024); formal deprecation policy with 12-month minimum window; 2026-07-28 contained breaking changes | Verified fact | A3-S011, A3-S015 |
| Deployment | saas: No (open specification; deployment depends on each implementation); managed_cloud: No (open specification; deployment depends on each implementation); vpc_byoc: No (open specification; deployment depends on each implementation); private_cloud: No (open specification; deployment depends on each implementation); self_hosted: Yes (implementations can be self-hosted; the specification itself is not a hosted service); on_prem: Yes (implementations can be self-hosted; the specification itself is not a hosted service) | | |

## Amazon Bedrock AgentCore Gateway and AgentCore Identity (`L4-aws-agentcore-gateway-identity`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where AWS is your primary cloud (CP3 Q2, rubric rule 10). AWS's lead managed tool gateway and agent identity service; deployment 2 (AWS-managed only) is accepted under rule 11 because the condition is an existing platform commitment. Same tier as C1-aws-agentcore-gateway [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Tool conversion, inbound identity, outbound vault and Cedar policy [VF: A6-S021, A6-S026] |
| Enterprise readiness | 4 | Hyperscaler presumption: platform controls presumed (CP2 Q1); confirm per service [AJ] |
| Security and compliance | 4 | SOC 1/2/3 scope listed; ISO listed with inconsistent wording; CMK for vault; one point below 5 under rule 8 [VF: B-L4-S001, B-L4-S002, A6-S074] |
| Deployment flexibility | 2 | Managed AWS service only, with VPC and PrivateLink connectivity; no self-host (A3-S047, A3-S048); 2, consistent with C1-aws-agentcore-gateway and every other AWS-only managed service (CP3 review A) |
| Ecosystem | 4 | MCP on both sides, OAuth and IAM integration [VF: A3-S047] |
| Reliability and maturity | 3 | GA October 2025 with regular feature releases (A3-S047, A3-S048); about one year GA, so 3, consistent with AgentCore Memory (L5) (CP3 review A) |
| Cost / TCO | 4 | Low published per-call pricing [VF: A6-S021] |
| Lock-in / portability | 3 | Proprietary AWS API but standard MCP/OAuth interfaces; Cedar policies portable [VF: A6-S045] |
| **Total (generic / FS)** | **3.55 / 3.45** | |

**Capabilities.** Managed MCP tool gateway (APIs, Lambda and MCP servers as tools; IAM or JWT inbound; 3LO outbound) plus agent identity and refresh-token vault; pairs with Cedar-based AgentCore Policy for pre-execution authorisation [VF: A3-S047, A3-S048, A6-S021, A6-S074, A6-S026]. Same service also profiled as C1-aws-agentcore-gateway [AJ].

**Strengths**

- Most complete managed implementation of the tool-governance sub-layer found [AJ]
- Supports MCP 2026-07-28 and earlier revisions [VF: A6-S105]
- Customer-managed KMS key for the token vault [VF: A6-S074]
- Published per-call pricing [VF: A6-S021]

**Limitations and risks**

- AWS only; no self-hosted option [VF: A3-S047]
- ISO scope wording inconsistent across AWS pages ('aligns' pending third-party review) [VF: B-L4-S002]
- Adds to AWS concentration [AJ]

**Choose when**

- AWS is the primary agent platform [AJ]

**Avoid when**

- Tools and agents span several clouds and one policy point is required [AJ]

**Nearest competitors:** C1-azure-apim-ai-gateway, C1-agentgateway, C1-kong-ai-gateway, L4-composio

**Regulated-FS note.** Sits within AWS, a designated CTP under DORA and the UK regime; include in AWS concentration analysis; platform controls presumed (CP2 Q1), confirm per service [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Amazon Web Services | Verified fact | A3-S047 |
| Category | Managed MCP tool gateway and agent identity/credential service | Verified fact | A3-S047 |
| Version / lineup | GA October 2025; Gateway three-legged OAuth for MCP targets GA and VPC egress (April 2026); supports MCP 2026-07-28 stateless core | Verified fact | A3-S047, A3-S048, A3-S015 |
| Licence | Proprietary managed service | Verified fact | A3-S047 |
| Status events | October 2025: GA; April 2026: Gateway 3LO for MCP targets GA; VPC egress for Gateway and Identity | Verified fact | A3-S047, A3-S048 |
| Strategic direction | AWS contributed the MCP Tasks extension and supports the stateless 2026-07-28 spec in AgentCore | Verified fact | A3-S015 |
| What it does | Gateway converts APIs and Lambda functions into agent tools and fronts existing MCP servers with IAM or OAuth authorisation; Identity provides identity-aware authorisation, a vault for refresh tokens and integrations with OAuth services | Verified fact | A3-S047 |
| Stack position | L4 governance sub-layer (MCP gateway) plus C4 agent identity | Architectural judgement |  |
| Integration | MCP (server-facing and client-facing), OAuth, IAM | Verified fact | A3-S047 |
| Dependencies | AWS account and Amazon Bedrock AgentCore | Verified fact | A3-S047 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | 15 AWS Regions (EU coverage not individually verified) | Verified fact | A3-S048 |
| Security features | Refresh-token vault; IAM or OAuth for agent-to-tool calls; private networking | Verified fact | A3-S047 |
| Access controls | Identity-aware authorisation; per-user tokens via 3LO for MCP targets | Verified fact | A3-S047, A3-S048 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GA October 2025 | Verified fact | A3-S047 |
| Deployment | saas: Yes; managed_cloud: Yes; vpc_byoc: VPC, PrivateLink and VPC egress supported; private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## Browserbase (cloud browser infrastructure) and Stagehand (open-source browser automation SDK) (`L4-browserbase`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Browserbase – cloud browsers

*Rationale:* Well-controlled browser runtime for the narrow case where no API exists [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Isolated browsers plus AI interaction layer [VF: A3-S013] |
| Enterprise readiness | 3 | SAML SSO verified (CP2 rule 7: max 3) [VF: B-L4-S004] |
| Security and compliance | 3 | SOC 2 Type II, pen test, DPA; no ISO 27001 [VF: A3-S102] |
| Deployment flexibility | 3 | SaaS plus VPC/private-cloud options for large enterprise [VF: A3-S102] |
| Ecosystem | 4 | Stagehand widely used; CDP/Playwright standard [VF: A3-S054] |
| Reliability and maturity | 3 | Since April 2024, 46 SDK releases; MCP repo archived [VF: A3-S013, A3-S054] |
| Cost / TCO | 3 | Transparent tiered pricing [VF: A3-S102] |
| Lock-in / portability | 4 | Client-side tooling open and portable; service proprietary [AJ] |
| **Total (generic / FS)** | **3.35 / 3.35** | |

**Capabilities.** Managed headless browsers driven over CDP by Playwright/Puppeteer, with Stagehand (MIT) for AI-driven interaction and extraction [VF: A3-S013, A3-S068].

**Strengths**

- SOC 2 Type II (2025, 2026), pen test, HIPAA BAA, DPA, US/EU/Asia residency for large enterprise [VF: A3-S102]
- SAML SSO on Enterprise; recordings to customer S3 [VF: B-L4-S004]
- Portable client side (Playwright, CDP, MIT Stagehand) [VF: A3-S013, A3-S068]

**Limitations and risks**

- Standalone MCP server repository archived [VF: A3-S054, V1-S081]
- No admin audit log found; plan naming inconsistent [VF: B-L4-S004] [NPV]
- Browser automation is fragile and hard to audit compared with APIs [AJ]

**Choose when**

- An agent must operate a website that has no API [AJ]

**Avoid when**

- An API or read-only data tool exists [AJ]

**Nearest competitors:** L8-firecrawl, L8-apify, L4-e2b

**Regulated-FS note.** Allow-list target domains and never give browser sessions credentials to client-facing systems [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Browserbase Inc. | Verified fact | A3-S068 |
| Category | Managed headless-browser infrastructure for agents | Verified fact | A3-S013 |
| Version / lineup | browserbase Python SDK 1.20.0 (24 September 2026); Stagehand 4.1.0 (9 September 2026) | Verified fact | A3-S013, A3-S076 |
| Licence | SDK Apache-2.0; Stagehand MIT; browser service proprietary | Verified fact | A3-S013, A3-S068 |
| Status events | browserbase/mcp-server-browserbase repository archived (status on 7 October 2026) | Verified fact | A3-S054, V1-S081 |
| Strategic direction | Agent skills collection and Stagehand integrations with coding agents; standalone MCP server repository archived | Verified fact | A3-S054 |
| What it does | Creates remote browser sessions that Playwright/Puppeteer connect to over CDP; Stagehand adds AI-driven interaction and data extraction | Verified fact | A3-S013, A3-S054 |
| Stack position | L4 tool runtime (browser execution); overlaps L8 web extraction | Verified fact | A3-S013 |
| Integration | REST API, Python/Node SDKs, CDP connect URL, Stagehand SDK, agent skills | Verified fact | A3-S013, A3-S054 |
| Dependencies | Browserbase hosted service; Playwright/CDP client | Verified fact | A3-S013 |
| Certifications | SOC 2 Type II reports 2025 and 2026; 2026 penetration test; HIPAA with BAA on Scale/Enterprise | Verified fact | A3-S102 |
| GDPR / residency | Data residency controls US/EU/Asia for large enterprise customers; DPA available | Verified fact | A3-S102 |
| Security features | Isolated browsers; VPC connectivity and private cloud options for large enterprises | Verified fact | A3-S102 |
| Access controls | SSO on enterprise tier | Verified fact | A3-S102 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free; Developer US$20/month; Startup US$99/month; Scale/Enterprise custom | Verified fact | A3-S102 |
| Infrastructure cost | Not applicable (SaaS) | Architectural judgement |  |
| Ecosystem | Stagehand works with Claude Code, Codex, Mastra and others (repo description) | Verified fact | A3-S054 |
| Adoption signals | browserbase/stagehand 25,562 GitHub stars (7 October 2026); US$40M Series B led by Notable Capital (June 2025, reported US$300M valuation) | Verified fact | A3-S054, A3-S103 |
| Maturity | Python SDK first released April 2024; 46 releases | Verified fact | A3-S013 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: VPC connectivity for large enterprise customers; private_cloud: Yes (private cloud options for large enterprise customers); self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## E2B (`L4-e2b`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** E2B – code sandboxes

*Rationale:* Reference sandbox pattern; missing enterprise identity controls keep it short of Strategic [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Leading isolation, egress and secrets design for code execution [VF: A3-S062] |
| Enterprise readiness | 2 | Capped at 2: SSO, SCIM and RBAC planned, no verified customer audit log [VF: B-L4-S003] |
| Security and compliance | 3 | SOC 2 Type II (control plane), HIPAA BAA, pen test; no ISO 27001 [VF: A3-S104, A3-S120] |
| Deployment flexibility | 4 | Cloud with EU region, BYOC AWS/GCP, dedicated; no production self-host or air-gap [VF: A3-S120, A3-S062] |
| Ecosystem | 4 | SDKs, OTel export, broad agent use [VF: A3-S062, A3-S054] |
| Reliability and maturity | 3 | Since August 2023, 365 SDK releases; Series A stage [VF: A3-S007, A3-S105] |
| Cost / TCO | 3 | Published pricing but high Enterprise minimum and heavy self-host stack [VF: A3-S104, A3-S062] |
| Lock-in / portability | 4 | Apache-2.0 runtime and MIT SDK; proprietary cloud [VF: A3-S062] |
| **Total (generic / FS)** | **3.35 / 3.35** | |

*Evidence rules applied:* enterprise_readiness capped at 2: SSO/SCIM/RBAC listed as planned; no verified SSO, RBAC or customer audit log (B-L4-S003)

**Capabilities.** Firecracker microVM sandboxes for AI-generated code with per-sandbox egress firewall, workload identity tokens and secrets kept out of API/logs/spans; Apache-2.0 runtime; Cloud, BYOC (AWS, GCP) and dedicated deployments [VF: A3-S062, A3-S007, A3-S120].

**Strengths**

- Strong isolation and egress model [VF: A3-S062]
- Open-source runtime as an exit route [VF: A3-S062]
- EU region and BYOC keep data in customer VPC [VF: A3-S120, A3-S104]

**Limitations and risks**

- SSO, SCIM and RBAC still 'planned'; no customer audit-log export found [VF: B-L4-S003]
- Self-hosting is evaluation-only per vendor [VF: A3-S062]
- SOC 2 scope excludes customer BYOC accounts [VF: A3-S104, V1-S096]
- Enterprise minimum US$3,000 per month [VF: A3-S104]

**Choose when**

- Any generated code must run, including derived calculations [AJ]

**Avoid when**

- You need console SSO and RBAC today and cannot compensate with BYOC and your cloud IAM [AJ]

**Nearest competitors:** L4-aws-agentcore-gateway-identity, LangSmith Sandboxes, Daytona / Modal (not profiled)

**Regulated-FS note.** Use BYOC or the EU region with default-deny egress; reconcile sandbox outputs to authoritative engines before use [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | E2B | Verified fact | A3-S062 |
| Category | Secure cloud sandboxes (Firecracker microVMs) for running AI-generated code | Verified fact | A3-S062 |
| Version / lineup | e2b SDK 2.53.1 and e2b-code-interpreter 2.10.3 (6 October 2026) | Verified fact | A3-S007 |
| Licence | Open source: SDK MIT; E2B Runtime (control plane, orchestrator, in-VM agent) Apache-2.0; E2B Cloud hosted service | Verified fact | A3-S007, A3-S062 |
| Strategic direction | Positions itself as 'the AI agent cloud': snapshot-resume microVMs, pause/resume, forking running sandboxes, persistent volumes, secrets and workload identity | Verified fact | A3-S062 |
| What it does | Starts isolated sandboxes from pre-booted templates, runs commands and code, exposes ports via sandbox URLs and pauses idle sandboxes | Verified fact | A3-S062, A3-S007 |
| Stack position | L4 tool runtime (code execution); also a C7 sandboxing control | Verified fact | A3-S062 |
| Integration | Python/JavaScript SDKs and CLI; REST API; envd in-VM API over Connect RPC/REST | Verified fact | A3-S062 |
| Dependencies | Self-hosting needs Linux with KVM; runtime uses PostgreSQL, Redis, ClickHouse and object storage | Verified fact | A3-S062 |
| Certifications | SOC 2 Type II (covers E2B software and control plane; BYOC cloud account is customer's responsibility); HIPAA BAA on Enterprise; pen test and DPA in trust centre | Verified fact | A3-S104, A3-S120, V1-S096 |
| GDPR / residency | Managed regions US (default), EU and APAC (EU/APAC on Pro and above, enabled by support); regions do not share state; BYOC on AWS and GCP keeps traffic and logs in customer VPC | Verified fact | A3-S120, A3-S104 |
| Security features | One Firecracker microVM per sandbox with own cgroup and network namespace; per-sandbox nftables egress firewall with domain allow/deny lists; secrets never cross API/logs/spans; short-lived workload identity tokens; per-sandbox access tokens for URLs | Verified fact | A3-S062 |
| Access controls | SSO, SCIM and RBAC listed as planned on Enterprise page (page about 436 days old); Enterprise telemetry to customer OTLP endpoint and signed lifecycle webhooks | Verified fact | A3-S120 |
| Enterprise support | Enterprise dedicated deployments offered | Verified fact | A3-S062 |
| Pricing | Hobby free (one-time US$100 credit); Pro US$150/month plus usage; Enterprise custom with US$3,000/month minimum; per-second billing, paused sandboxes not billed | Verified fact | A3-S104 |
| Infrastructure cost | Self-host cost drivers: KVM hosts, object storage for templates/snapshots, PostgreSQL, Redis and ClickHouse | Verified fact | A3-S062 |
| Ecosystem | OpenTelemetry export built in | Verified fact | A3-S062 |
| Adoption signals | e2b-dev/E2B 14,219 GitHub stars (7 October 2026); US$21M Series A led by Insight Partners (July 2025); vendor claims 88% of Fortune 100 signed up | Verified fact | A3-S054, A3-S105 |
| Maturity | SDK first released August 2023; 365 releases | Verified fact | A3-S007 |
| Deployment | saas: Yes (E2B Cloud); managed_cloud: Yes (dedicated deployment run by E2B inside customer account); vpc_byoc: Yes (BYOC on AWS and GCP; Azure not yet per docs, listed on Enterprise page - conflict); private_cloud: Not publicly verified; self_hosted: Yes for evaluation (E2B Embed single host; GCP Terraform and Kubernetes manifests) - vendor says not a production pattern; on_prem: Not publicly verified | | |

## Agent Skills (SKILL.md open format) (`L4-agent-skills`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Agent Skills – reusable skills

*Rationale:* Useful format, but vendor-led governance, no versioning and no provenance keep it out of foundational use [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Packages procedural knowledge competently; no versioning, dependency or signing model [AJ] |
| Enterprise readiness | 2 | Open format (rule 2): enterprise provisioning is a vendor feature, not part of the standard [VF: A3-S029] |
| Security and compliance | 2 | Rule 2 hygiene: executable content without signing or provenance [VF: A3-S037, A3-S072] |
| Deployment flexibility | 5 | Plain files usable anywhere [VF: A3-S061] |
| Ecosystem | 4 | 46 clients including major vendors, but young [VF: A3-S113] |
| Reliability and maturity | 2 | Under one year as an open standard; no tagged releases [VF: A3-S029, A3-S115] |
| Cost / TCO | 5 | Free, no operations [VF: A3-S061] |
| Lock-in / portability | 3 | Portable Markdown, but no neutral governance [VF: V1-S046] |
| **Total (generic / FS)** | **3.20 / 3.00** | |

**Capabilities.** Open packaging format (SKILL.md plus optional scripts, references, assets) with progressive disclosure; adopted by 46 listed clients including OpenAI Codex and Gemini CLI [VF: A3-S061, A3-S113, A3-S033, A3-S034]. Conflict of interest: originated at Anthropic and maintained by Anthropic staff; author is an Anthropic model [AJ].

**Strengths**

- Plain, reviewable files portable across clients [VF: A3-S061]
- Independent adoption confirmed by OpenAI and Google documentation [VF: A3-S033, A3-S034, V1-S047]

**Limitations and risks**

- No neutral governance body; maintainers are Anthropic employees; AAIF proposal not accepted on available evidence [VF: V1-S046, A3-S115, A3-S112]
- Living document with no tagged releases [VF: A3-S115]
- No signing or provenance; skills can carry executable scripts; vendor warns of exfiltration [VF: A3-S037, A3-S061, A3-S072]

**Choose when**

- Packaging internally authored house procedures for several agent clients [AJ]

**Avoid when**

- Skills would come from outside the firm or carry scripts that run with agent credentials [AJ]

**Nearest competitors:** AGENTS.md, C5 prompt packages (Git-based), L4-mcp

**Regulated-FS note.** Internally authored, Git-reviewed, script-free skills only until signing, versioning and neutral governance exist; independent alternatives are C5 prompt packages and AGENTS.md [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Originated at Anthropic (launched 16 October 2025; published as an open standard 18 December 2025); specification maintained in the agentskills/agentskills repository and agentskills.io; no published governance body or charter, and no evidence that it is an AAIF-hosted project (AAIF material treats the format as owned by the Agent Skills specification; secondary claims that Anthropic stewards it through AAIF are unsupported) | Verified fact | A3-S028, A3-S029, A3-S061, V1-S046 |
| Category | Open packaging format for procedural knowledge: folders with SKILL.md (name and description required) plus optional scripts, references and assets | Verified fact | A3-S061, A3-S037 |
| Version / lineup | No versioned releases: specification is a 'living document'; tagged releases with changelog are planned (AAIF proposal); no CHANGELOG.md in repository root on 7 October 2026 | Verified fact | A3-S115, A3-S112 |
| Licence | Open specification; repository code Apache-2.0, documentation CC-BY-4.0 | Verified fact | A3-S061 |
| Status events | 18 December 2025: published as an open standard | Verified fact | A3-S029, V1-S040 |
| Strategic direction | Portable across agent products; AAIF 'Skills Over MCP' working group exploring delivery of skills via MCP; Claude adds org-wide admin provisioning and a partner skills directory | Verified fact | A3-S038, A3-S029 |
| What it does | Agents load only skill names/descriptions at start-up, read the full SKILL.md when a task matches (progressive disclosure) and may execute bundled scripts | Verified fact | A3-S061 |
| Stack position | Sits between L3 agent harness and L4 tools: packaged instructions plus code, often wrapping MCP tools | Architectural judgement |  |
| Integration | Filesystem convention (.agents/skills and vendor paths); Claude API /v1/skills endpoint; adopted by OpenAI Codex and Google Gemini CLI | Verified fact | A3-S029, A3-S033, A3-S034 |
| Dependencies | A skills-compatible agent with file access; scripts require a code-execution environment (Claude requires Code Execution and File Creation) | Verified fact | A3-S029, A3-S061 |
| Certifications | Not applicable (open format) | Architectural judgement |  |
| GDPR / residency | Not applicable (open format) | Architectural judgement |  |
| Security features | No signing or provenance in the core format found; Anthropic warns malicious skills may exfiltrate data and advises installing only from trusted sources; Gemini CLI docs advise inspecting third-party skills | Verified fact | A3-S072, A3-S034, A3-S037 |
| Access controls | Claude Team/Enterprise admins can provision skills centrally (vendor feature, not part of the standard) | Verified fact | A3-S029 |
| Enterprise support | Not applicable (open format) | Architectural judgement |  |
| Pricing | Free open format | Verified fact | A3-S061 |
| Infrastructure cost | Not applicable | Architectural judgement |  |
| Ecosystem | 46 client products listed on agentskills.io showcase (e.g. ChatGPT & Codex, Gemini CLI, GitHub Copilot, VS Code, Cursor, Goose, Kiro, Junie, Databricks Genie Code, Snowflake Cortex Code, Mistral AI Vibe, Spring AI, Letta); OpenAI and Google primary docs confirm support | Verified fact | A3-S027, A3-S033, A3-S034, A3-S113, V1-S047 |
| Adoption signals | agentskills/agentskills 25,954 GitHub stars (7 October 2026) | Verified fact | A3-S054 |
| Maturity | Specification repository created 16 December 2025; no versioned releases found | Verified fact | A3-S054 |
| Deployment | saas: No (open specification; deployment depends on each implementation); managed_cloud: No (open specification; deployment depends on each implementation); vpc_byoc: No (open specification; deployment depends on each implementation); private_cloud: No (open specification; deployment depends on each implementation); self_hosted: Yes (implementations can be self-hosted; the specification itself is not a hosted service); on_prem: Yes (implementations can be self-hosted; the specification itself is not a hosted service) | | |

## Composio (`L4-composio`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** Composio – integrations

*Rationale:* Credential-broker model, vendor-only security evidence and the May 2026 token-exposure incident make it unsuitable as a critical dependency [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Broad connectors, per-user auth, gateway and policy features [VF: A3-S063, A3-S119] |
| Enterprise readiness | 3 | SSO, SCIM, RBAC, audit logs and SLA are vendor-stated; one-or-more controls lift the cap to 3 under CP2 rule 7 [VF: A3-S119, A3-S098] |
| Security and compliance | 2 | Capped at 2: certifications vendor-marketing only (V1 section 4); May 2026 incident [VF: B-L4-S007] |
| Deployment flexibility | 4 | SaaS plus VPC, self-host and on-prem on Enterprise; no air-gap evidence [VF: A3-S098] |
| Ecosystem | 4 | Adapters for major frameworks and remote MCP server [VF: A3-S063] |
| Reliability and maturity | 2 | Pre-1.0 SDK, 2.0 beta, recent security incident [VF: A3-S008, B-L4-S007] |
| Cost / TCO | 3 | Metered per-call pricing published (low confidence) [VF: A3-S098] |
| Lock-in / portability | 2 | Proprietary API holding user tokens; hard exit [AJ] |
| **Total (generic / FS)** | **3.15 / 2.90** | |

*Evidence rules applied:* security_compliance capped at 2: Composio security claims are vendor marketing only (V1 verification log section 4)

**Capabilities.** Managed tool-integration platform: 1000+ toolkits, per-user sessions, OAuth/connected-account brokering, per-session tool restriction, and an MCP Gateway with vendor-stated SSO, SCIM, policy-as-code and per-call audit logs [VF: A3-S063, A3-S008, A3-S119, A3-S098].

**Strengths**

- Broadest SaaS connector catalogue with per-user authentication [VF: A3-S063]
- Self-hosted, VPC and on-premises options on Enterprise [VF: A3-S098]

**Limitations and risks**

- May 2026 incident: unauthorised access to internal systems; about 0.3% of connections and 5,241 API keys possibly exposed; token revocations and customer rotation required [VF: B-L4-S007]
- Security claims are vendor marketing only (V1 log section 4) [NPV]
- Holds end users' OAuth tokens: high switching cost [AJ]
- Managed cloud US-hosted; EU residency needs self-hosting [VF: A3-S119]
- SDK pre-1.0 with 2.0 in beta [VF: A3-S008, V1-S098]

**Choose when**

- A low-risk internal productivity agent needs many SaaS connectors quickly, self-hosted [AJ]

**Avoid when**

- The agent touches client data or you cannot self-host in-region [AJ]

**Nearest competitors:** L4-aws-agentcore-gateway-identity, C4-okta-auth0-ai-agents, C1-kong-ai-gateway

**Regulated-FS note.** Do not let a third party hold staff OAuth tokens to firm systems in its multi-tenant cloud; if used, self-host and keep the token vault in your estate [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Composio (SDK copyright Sampark Inc.; San Francisco) | Verified fact | A3-S063, A3-S067, A3-S099 |
| Category | Managed tool-integration platform for agents: 1000+ pre-authenticated toolkits, per-user sessions, authentication, triggers and a sandbox | Verified fact | A3-S063 |
| Version / lineup | Python SDK composio 0.25.0 (29 September 2026); 2.0.0b0 pre-release (31 August 2026) | Verified fact | A3-S008, V1-S098 |
| Licence | SDKs MIT; platform is a hosted proprietary service (API key from dashboard) | Verified fact | A3-S067, A3-S063 |
| Strategic direction | Session-based meta tools; markets an MCP Gateway product with governance (policy, audit, SSO) | Verified fact | A3-S008, A3-S119 |
| What it does | Creates per-user sessions whose tools an agent calls across 1000+ apps; handles OAuth/connected accounts and restricts toolkits, tools, auth configs and connected accounts per session | Verified fact | A3-S063, A3-S008 |
| Stack position | L4 integration/tool-hub; also acts as a managed credential broker for third-party apps | Verified fact | A3-S063 |
| Integration | Python/TypeScript SDKs, CLI, provider adapters for OpenAI Agents, Claude Agent SDK, Vercel AI SDK, LangChain; remote MCP server | Verified fact | A3-S063, A3-S054 |
| Dependencies | Composio hosted API | Verified fact | A3-S063 |
| Certifications | Vendor states SOC 2 Type II and ISO/IEC 27001:2022; evidence via trust centre (security.composio.dev) | Verified fact | A3-S098 |
| GDPR / residency | Managed cloud hosted in the US; EU-only residency requires self-hosted Enterprise deployment | Verified fact | A3-S119 |
| Security features | Credentials AES-256 encrypted and isolated from app code and LLM context; KMS key management on Enterprise; Zero Data Retention on Pro and above | Verified fact | A3-S098, A3-S119 |
| Access controls | SAML 2.0/OIDC SSO (Okta, Entra ID, Google Workspace) and SCIM 2.0 on Enterprise; action-level policy-as-code RBAC; per-call audit logs incl. denied calls, 7-day to 1-year retention, SIEM export; per-session tool restrictions | Verified fact | A3-S119, A3-S098, A3-S008 |
| Enterprise support | Enterprise: MSA/DPA/SLA, dedicated support, committed volume | Verified fact | A3-S098 |
| Pricing | Metered by tool call: free 20,000 calls/month; US$29/month for 200,000; US$229/month for 2M; Enterprise custom (as reported on Composio comparison pages) | Verified fact | A3-S098 |
| Infrastructure cost | Not applicable (SaaS) | Architectural judgement |  |
| Ecosystem | Provider adapters for major agent frameworks; maintains awesome-claude-skills list (76,670 stars) | Verified fact | A3-S063, A3-S054 |
| Adoption signals | ComposioHQ/composio 30,464 GitHub stars (7 October 2026); US$25M Series A led by Lightspeed (July 2025; US$29M total, Reported) | Verified fact | A3-S054, A3-S099 |
| Maturity | Current Python SDK line first published December 2024; pre-1.0 with 2.0 in beta | Verified fact | A3-S008 |
| Deployment | saas: Yes; managed_cloud: Yes (regional managed cloud handling); vpc_byoc: Yes (Enterprise VPC deployment); private_cloud: Not publicly verified; self_hosted: Yes (Enterprise fully self-hosted); on_prem: Yes (on-premise option on Enterprise) | | |

## Exa (`L4-exa`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Exa – search API

*Rationale:* Competent, certified search API; SaaS-only with no EU region [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers search and extraction competently [VF: A3-S010] |
| Enterprise readiness | 3 | SSO and SCIM verified; RBAC and audit logs not found (CP2 rule 7: max 3) [VF: A3-S121] |
| Security and compliance | 3 | SOC 2 Type II, DPA; no ISO 27001 found [VF: A3-S100, A3-S121] |
| Deployment flexibility | 1 | One SaaS service, no region choice found [VF: A3-S121] |
| Ecosystem | 3 | SDKs and MCP server; mainstream [VF: A3-S054] |
| Reliability and maturity | 3 | Steady releases since January 2024; well funded [VF: A3-S010] [R: A3-S101] |
| Cost / TCO | 3 | Transparent per-request pricing with a page conflict [VF: A3-S100] |
| Lock-in / portability | 3 | Proprietary index, but trivially swappable behind one interface [AJ] |
| **Total (generic / FS)** | **2.70 / 2.70** | |

**Capabilities.** Web search API for AI with filters, page contents, answers and structured output; MCP server [VF: A3-S010, A3-S054].

**Strengths**

- SOC 2 Type II with 2026 bridge letter; ZDR on Enterprise; DPA with SCCs and UK Addendum [VF: A3-S100, A3-S121]
- Dashboard SSO and SCIM on Enterprise [VF: A3-S121]

**Limitations and risks**

- SaaS only; no EU processing region found [VF: A3-S121]
- Pricing conflict US$7 vs US$4 per 1,000 searches [VF: A3-S100]
- Search queries can leak confidential intent [AJ]

**Choose when**

- Public-web research on non-confidential questions [AJ]

**Avoid when**

- Queries could contain client, holdings or deal information [AJ]

**Nearest competitors:** L4-tavily, L8-firecrawl, L8-apify

**Regulated-FS note.** Enable ZDR, route through the egress proxy with DLP, and register as an ICT third-party service [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Exa (Exa Labs, Inc.) | Verified fact | A3-S010, A3-S121 |
| Category | Web search API for AI (search, contents, answer, streaming) | Verified fact | A3-S010 |
| Version / lineup | exa-py 2.25.0 (1 October 2026) | Verified fact | A3-S010 |
| Licence | SDK MIT; search API proprietary | Verified fact | A3-S010 |
| Strategic direction | Search with structured output schemas and streamed answers | Verified fact | A3-S010 |
| What it does | Searches the web with date/domain filters, returns page contents/highlights, generates answers and supports structured output via output_schema | Verified fact | A3-S010 |
| Stack position | L4 tool (web retrieval) feeding agents; overlaps L8 web extraction | Verified fact | A3-S010 |
| Integration | Python and JavaScript SDKs; MCP server (exa-mcp-server) | Verified fact | A3-S010, A3-S054 |
| Dependencies | Exa hosted API (API key) | Verified fact | A3-S010 |
| Certifications | SOC 2 Type II (security, confidentiality, availability); 2026 bridge letter; HIPAA BAA for eligible Enterprise customers | Verified fact | A3-S100, A3-S121 |
| GDPR / residency | DPA with EU SCCs (2021/914) and UK Addendum; GDPR/CCPA rights honoured; zero data retention on Enterprise; no EU processing region stated | Verified fact | A3-S121, A3-S100 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | SSO and SCIM for the Exa Dashboard on Enterprise | Verified fact | A3-S121 |
| Enterprise support | Enterprise: custom MSA/DPA, volume discounts, custom datasets | Verified fact | A3-S100, A3-S121 |
| Pricing | Search US$7 per 1,000 requests; Monitors US$15 per 1,000; one page says from US$4 per 1,000 (conflict); Enterprise custom | Verified fact | A3-S100 |
| Infrastructure cost | Not applicable (SaaS) | Architectural judgement |  |
| Ecosystem | MCP server for agent clients | Verified fact | A3-S054 |
| Adoption signals | exa-mcp-server 5,091 GitHub stars (7 October 2026); US$85M Series B at US$700M (September 2025, Benchmark) and US$250M Series C at US$2.2B (May 2026, a16z) (Reported) | Verified fact | A3-S054, A3-S101 |
| Maturity | exa-py first released January 2024; 130 releases | Verified fact | A3-S010 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Tavily (`L4-tavily`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** Tavily – search API

*Rationale:* Useful search API with good proxy support; SaaS-only and newly acquired [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Search, extract, crawl and research endpoints [VF: A3-S009] |
| Enterprise readiness | 3 | RBAC roles verified (CP2 rule 7 lifts cap to 3); SSO and audit logs not found [VF: B-L4-S006] |
| Security and compliance | 3 | SOC 2 Type II per Trust Center; GDPR and ZDR stated; no ISO [VF: B-L4-S005, A3-S088] |
| Deployment flexibility | 1 | SaaS only, no region choice found [VF: A3-S088] |
| Ecosystem | 3 | SDKs and MCP server [VF: A3-S054] |
| Reliability and maturity | 3 | Releases since 2023; acquired by Nebius February 2026 [VF: A3-S009, V1-S041] |
| Cost / TCO | 3 | Transparent credit pricing [VF: A3-S088] |
| Lock-in / portability | 2 | Proprietary but swappable; reduced by 1 for ownership change (rule 3) [AJ] |
| **Total (generic / FS)** | **2.65 / 2.55** | |

**Capabilities.** Search, extract, crawl, map and research API for agents; custom HTTP session injection for proxying through an enterprise gateway; MCP server [VF: A3-S009, A3-S054].

**Strengths**

- Gateway-proxy support built into the SDK [VF: A3-S009]
- SOC 2 Type II via Trust Center; Owner/Admin/Member roles; Enterprise SLAs [VF: B-L4-S005, B-L4-S006, A3-S088]

**Limitations and risks**

- Acquired by Nebius (closed 19 February 2026); roadmap tied to a neocloud [VF: V1-S041, A3-S084]
- No EU processing region found; SSO not found [VF: A3-S088] [NPV]

**Choose when**

- Search plus extraction in one API, proxied through your gateway [AJ]

**Avoid when**

- You need EU processing or roadmap independence from Nebius [AJ]

**Nearest competitors:** L4-exa, L8-firecrawl

**Regulated-FS note.** Refresh third-party due diligence after the change of control and plan contract changes around PS7/26 notification lead times [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Tavily, a wholly owned subsidiary of Nebius Group N.V. (acquisition announced 10 February 2026; closed 19 February 2026) | Verified fact | A3-S084, A3-S085, A3-S086, V1-S041 |
| Category | Search, extract, crawl, map and research API for agents | Verified fact | A3-S009 |
| Version / lineup | tavily-python 0.8.5 (6 October 2026); @tavily/core 0.7.14 (6 October 2026) | Verified fact | A3-S009, A3-S083 |
| Licence | Proprietary API; JavaScript SDK MIT; Python SDK licence not stated in PyPI metadata | Verified fact | A3-S083, A3-S009 |
| Status events | 10 February 2026: Tavily announced it is joining Nebius; 19 February 2026: acquisition closed, Nebius acquiring 100% ownership (Nebius FY2025 Form 20-F); Nebius 6-K describes a merger making Tavily a wholly owned subsidiary, cash consideration; Nebius Q1 2026 filing accounts for the acquisition as completed: fair value of consideration US$189.7M (US$177.2M cash) plus an ARR-based earnout measured December 2026 and March 2027; Press reported a US$275M deal value (not disclosed by Nebius) | Verified fact | A3-S084, A3-S085, A3-S086, A3-S087, V1-S041 |
| Strategic direction | Integration into Nebius AI cloud (Token Factory reported); Tavily states API, data policies and zero data retention unchanged; adds asynchronous research tasks and keyless trial mode | Verified fact | A3-S084, A3-S086, A3-S009 |
| What it does | Provides web search, content extraction, site crawl/map and multi-step research endpoints via API | Verified fact | A3-S009 |
| Stack position | L4 tool (web retrieval) for agents; overlaps L8 | Verified fact | A3-S009 |
| Integration | Python/JS SDKs; supports custom HTTP session injection so enterprises can proxy traffic through an API gateway for central auth, logging and policy; MCP server | Verified fact | A3-S009, A3-S054 |
| Dependencies | Tavily hosted API | Verified fact | A3-S009 |
| Certifications | Vendor states SOC 2 certified; report type and period not confirmed (trust.tavily.com) | Verified fact | A3-S088 |
| GDPR / residency | Vendor states GDPR and CCPA compliant; zero data retention described as core; EU processing region not found | Verified fact | A3-S088, A3-S084 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Enterprise plan (custom): custom rate limits, dedicated account manager, Slack channel, AI engineer support, uptime and support SLAs | Verified fact | A3-S088 |
| Pricing | Free 1,000 credits per month; pay-as-you-go US$0.008 per credit; monthly plans US$0.0075-0.005 per credit; Enterprise custom | Verified fact | A3-S088, A3-S009 |
| Infrastructure cost | Not applicable (SaaS) | Architectural judgement |  |
| Ecosystem | MCP server (tavily-mcp) | Verified fact | A3-S054 |
| Adoption signals | tavily-mcp 2,422 and tavily-python 1,420 GitHub stars (7 October 2026) | Verified fact | A3-S054 |
| Maturity | tavily-python first released September 2023; 69 releases | Verified fact | A3-S009 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

# L3: Agent frameworks and orchestration

## LangGraph (open-source framework); managed runtime now branded LangSmith Deployment (formerly LangGraph Platform) (`L3-langgraph`)

**Tier:** Strategic · **Flags:** Renamed · **Original graphic label:** LangGraph – workflow

*Rationale:* Deepest coverage of the L3 questions with a stable 1.x line; Renamed refers to LangGraph Platform -> LangSmith Deployment.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Durable execution, interrupts, time travel, memory, deterministic plus LLM nodes, both Functional and Graph APIs [VF: A4-S118, A4-S039] |
| Enterprise readiness | 4 | LangSmith Enterprise: SAML/OIDC SSO, SCIM, custom-role RBAC, audit logs on self-hosted [VF: A4-S038] |
| Security and compliance | 4 | LangSmith SOC 2 Type II and HIPAA; ISO 27001 claimed, scope unconfirmed, so 4 not 5 (rule 8); OSS advisories published and patched [VF: A4-S034, B-L3-S007] |
| Deployment flexibility | 5 | Library anywhere; LangSmith Deployment SaaS, BYOC/hybrid, self-hosted and on-prem Kubernetes [VF: A4-S036, A4-S037] |
| Ecosystem | 5 | LangChain integrations, JS port, hosted by AgentCore and other runtimes [VF: A4-S118, A4-S116] |
| Reliability and maturity | 4 | 1.0 GA October 2025, Production/Stable, frequent releases, stable API commitment [VF: A4-S001, A4-S033] |
| Cost / TCO | 4 | OSS free; LangSmith seat and LSU pricing published [VF: A4-S036] |
| Lock-in / portability | 3 | MIT, self-hostable, but graph/checkpoint APIs proprietary to LangGraph and deployment is proprietary [VF: A4-S001, A4-S039] |
| **Total (generic / FS)** | **4.40 / 4.20** | |

**Capabilities.** Low-level stateful graph runtime (MIT) combining deterministic code and LLM decisions in one graph, with checkpointed durable execution, interrupts for human-in-the-loop, time travel, memory and streaming; managed runtime is LangSmith Deployment (formerly LangGraph Platform) [VF: A4-S118, A4-S039, A4-S031].

**Strengths**

- Covers every L3 research question in one GA (1.x) framework with a no-breaking-changes commitment until 2.0 [VF: A4-S033] [AJ]
- Deployment range from library to SaaS, BYOC, self-hosted and on-prem Kubernetes [VF: A4-S036, A4-S037]

**Limitations and risks**

- Graph and checkpoint APIs are LangGraph-specific [VF: A4-S039]
- Three checkpoint deserialisation advisories in 2025-26, all patched; the checkpoint store is a security boundary [VF: B-L3-S007]
- LangSmith ISO 27001 claimed but scope unconfirmed [VF: A4-S034, A4-S035, A4-S149]
- Full self-hosted platform needs the Enterprise plan [VF: A4-S037]

**Choose when**

- You need deterministic workflow graphs with one or more LLM steps, durable checkpoints and approval interrupts [AJ]
- Python or TypeScript teams standardising on one orchestration framework [AJ]

**Avoid when**

- The workflow is a single model call that needs no framework [AJ]
- You cannot restrict write access to the checkpoint database [AJ]

**Nearest competitors:** L3-microsoft-agent-framework, L3-pydantic-ai, L3-google-adk, L3-temporal

**Regulated-FS note.** Pin langgraph and langgraph-checkpoint, keep checkpoints in a firm-controlled Postgres with write access limited to the runtime, and export traces via OTel as well as LangSmith [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LangChain, Inc. | Verified fact | A4-S001, A4-S032 |
| Category | Low-level stateful agent and workflow orchestration framework (graph runtime) with a commercial managed deployment service | Verified fact | A4-S118, A4-S037 |
| Version / lineup | langgraph 1.2.14 on PyPI (released 6 October 2026); @langchain/langgraph 1.4.21 on npm (7 October 2026); 1.0.0 released 17 October 2025 (Python) / 18 October 2025 (JS) | Verified fact | A4-S001, A4-S026 |
| Licence | Open source, MIT (framework). LangSmith (Observability, Evaluation, Deployment) is proprietary SaaS / self-hosted enterprise software | Verified fact | A4-S001, A4-S026, A4-S036 |
| Status events | 14 October 2025: LangGraph Platform renamed LangSmith Deployment; LangGraph Studio renamed LangSmith Studio; 17 October 2025: LangGraph 1.0.0 GA on PyPI; 1 October 2026: existing LangSmith Deployment customers move from per-run/uptime pricing to usage-based LSU pricing | Verified fact | A4-S031, A4-S001, A4-S036, V1-S056 |
| Strategic direction | LangGraph 1.0 positioned as 'the first stable major release in the durable agent framework space' with no breaking changes until 2.0; LangChain 1.0 create_agent runs on the LangGraph runtime; Deep Agents harness built on LangGraph. Interrupt 2026 (13-14 May 2026) launched LangSmith Engine, Managed Deep Agents, SmithDB, Context Hub, an LLM Gateway and Sandboxes GA; Agent Builder rebranded LangSmith Fleet (March 2026) | Verified fact | A4-S033, A4-S118, A4-S040 |
| What it does | Provides low-level infrastructure for long-running, stateful workflows or agents: durable execution that resumes from where it left off, human-in-the-loop via interrupts, short- and long-term memory, streaming, and deployment through LangSmith. Deterministic code and LLM-driven decisions can be combined in one graph; a Functional API (@entrypoint/@task) offers a workflow style. | Verified fact | A4-S118, A4-S039 |
| Stack position | Agent orchestration runtime (L3). LangSmith Deployment is a separate agent-hosting runtime; LangSmith Observability/Evaluation sit in L9. The graphic's label 'workflow' captures only part of its role: LangGraph covers both deterministic workflows and agent loops. | Verified fact | A4-S039, A4-S031 |
| Integration | Python and JS/TS libraries; LangGraph SDK / Agent Server API for deployed graphs; LangChain model and tool integrations; tracing to LangSmith | Verified fact | A4-S118, A4-S037 |
| Dependencies | Python >=3.10 (or JS/TS); checkpointer backend for persistence (durable, database-backed checkpointer recommended in production, e.g. Postgres via langgraph-checkpoint-postgres); LangSmith for deployment/observability (optional); any LLM provider via LangChain integrations | Verified fact | A4-S001, A4-S039 |
| Certifications | LangSmith: SOC 2 Type II and HIPAA (BAA on Enterprise) consistently stated; ISO 27001 stated only on the enterprise marketing page and LangSmith Engine security docs ('certified to ISO 27001'), while LangSmith enterprise/shared-responsibility docs and the EU-residency announcement omit it and the trust-centre listing seen does not name it. Treat ISO 27001 as claimed, scope unconfirmed. Not applicable to the OSS library. | Verified fact | A4-S034, A4-S035, A4-S149 |
| GDPR / residency | LangSmith regional instances: GCP EU (eu.smith.langchain.com), GCP US, GCP APAC, AWS US; available on all plans; region migration not supported; no EU legal entity for contracting; DPA on request | Verified fact | A4-S034 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | LangSmith Enterprise: SAML 2.0 / OIDC SSO with JIT provisioning, SCIM 2.0, workspace RBAC with custom roles; self-hosted v0.14: ABAC and audit logs (OCSF 1.7.0) enabled by default | Verified fact | A4-S038 |
| Enterprise support | LangSmith Enterprise plan (custom pricing, invoiced annually upfront) | Verified fact | A4-S036 |
| Pricing | LangGraph OSS free (MIT). LangSmith Plus US$39 per seat per month (10k base traces/month then pay-as-you-go; 1 free small serverless deployment); Enterprise custom. Deployment billed on resources consumed in LangChain Standard Units (LSU), replacing per-run/uptime pricing (pricing page shows 1 LSU = US$1 in the Engine section) | Verified fact | A4-S036 |
| Infrastructure cost | Self-hosting requires a durable checkpointer database; self-hosted LangSmith Deployment runs control plane and Agent Servers on customer Kubernetes | Verified fact | A4-S039, A4-S037 |
| Ecosystem | LangChain integrations; Deep Agents; LangSmith; JS/TS port (LangGraph.js); NVIDIA Dynamo publishes a LangChain integration | Verified fact | A4-S118, A4-S026, A4-S098 |
| Adoption signals | README names Klarna, Replit and Elastic; LangChain raised US$125M at US$1.25B valuation (IVP lead) alongside the 1.0 releases (October 2025) | Verified fact | A4-S118, A4-S032 |
| Maturity | First PyPI release 8 January 2024; 1.0 GA October 2025 (Development Status: Production/Stable); frequent releases (1.2.14 on 6 October 2026) | Verified fact | A4-S001 |
| Deployment | saas: Yes (LangSmith Deployment cloud; Plus plan or above); managed_cloud: Yes (LangSmith Deployment managed cloud); vpc_byoc: Yes (BYOC and hybrid: data plane in customer VPC; Enterprise plan); private_cloud: Yes (self-hosted LangSmith with Deployment control plane on Kubernetes; Enterprise plan); self_hosted: Yes (open-source library runs anywhere; full self-hosted platform requires Enterprise plan); on_prem: Yes (self-hosted Kubernetes deployment of LangSmith; Enterprise) | | |

## Temporal (durable execution platform; Python SDK temporalio) (`L3-temporal`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic as the durable-execution substrate under deterministic workflows; independent of model vendors.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Leading durability, retries and deterministic workflow semantics; no agent loop itself [VF: A4-S019, A4-S045] |
| Enterprise readiness | 4 | SAML SSO, SCIM, roles and custom roles, audit logs, Cloud Ops API; SLA not verified [VF: B-L3-S003] |
| Security and compliance | 3 | SOC 2 Type 2, HIPAA BAA, GDPR DPA, client-side encryption; no ISO 27001 found [VF: B-L3-S001] |
| Deployment flexibility | 5 | Temporal Cloud on 14 AWS and 6 GCP regions incl. Europe; MIT self-host anywhere [VF: B-L3-S002] |
| Ecosystem | 4 | Built into Pydantic AI, OpenAI Agents SDK, Mistral Workflows [VF: A4-S045, A4-S052, A4-S058] |
| Reliability and maturity | 4 | Python SDK since March 2022; long-established [VF: A4-S019] |
| Cost / TCO | 3 | Cloud pricing not verified; self-host operations heavy [NPV] [VF: B-L3-S002] |
| Lock-in / portability | 4 | MIT server; portable between self-host and Cloud; code is Temporal-specific [VF: B-L3-S002] |
| **Total (generic / FS)** | **3.90 / 3.90** | |

**Capabilities.** Durable execution engine: workflows whose activities are recorded so execution resumes after failure; used beneath Pydantic AI, the OpenAI Agents SDK and Mistral Workflows. MIT server, self-hosted or Temporal Cloud on AWS and GCP [VF: A4-S019, A4-S045, A4-S052, A4-S058, B-L3-S002].

**Strengths**

- Separates reliability (retries, resume, timers, signals) from agent logic [AJ]
- Same server in self-hosted and Cloud; moves without code changes [VF: B-L3-S002]
- Cloud: SAML SSO, SCIM, roles, exportable audit logs [VF: B-L3-S003]

**Limitations and risks**

- Not an agent framework [AJ]
- Self-hosting needs Kubernetes and persistence stores, sequential upgrades [VF: B-L3-S002]
- No ISO 27001 found; certification evidence from search extracts [VF: B-L3-S001]
- Workflow code becomes a hard dependency [AJ]
- Cloud pricing not verified [NPV]

**Choose when**

- Any regulated agent workflow that must resume without re-calling tools [AJ]

**Avoid when**

- Short, stateless single-call tasks [AJ]

**Nearest competitors:** DBOS, Restate, L3-langgraph, L3-microsoft-agent-framework

**Regulated-FS note.** Encrypt payloads client-side so Temporal Cloud stores ciphertext, or self-host in-region [VF: B-L3-S001] [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Temporal Technologies Inc. | Verified fact | A4-S019 |
| Category | Durable execution / workflow orchestration engine used as the reliability layer under agent frameworks | Verified fact | A4-S019, A4-S045, A4-S058 |
| Version / lineup | temporalio (Python SDK) 1.34.0 (30 September 2026) | Verified fact | A4-S019 |
| Licence | Python SDK MIT; server licence and Temporal Cloud terms not verified in this run | Verified fact | A4-S019 |
| Status events | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Runs workflows whose steps (activities) are recorded so execution resumes after failures. Agent frameworks run model calls, tool calls and MCP traffic as Temporal activities (Pydantic AI), offer Temporal integrations for long-running human-in-the-loop agents (OpenAI Agents SDK), or build their workflow product on it (Mistral Workflows). | Verified fact | A4-S045, A4-S052, A4-S058 |
| Stack position | Cross-cutting reliability substrate beneath L3 (deterministic workflow layer in H2), not an agent framework itself | Architectural judgement |  |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Integrated by Pydantic AI, OpenAI Agents SDK and Mistral Workflows; alternatives DBOS (dbos 3.2.0, MIT) and Restate (restate-sdk 1.0.5) | Verified fact | A4-S045, A4-S052, A4-S058, A4-S020, A4-S104 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Python SDK since March 2022 | Verified fact | A4-S019 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Microsoft Agent Framework (MAF) (`L3-microsoft-agent-framework`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Agent Framework – Microsoft

*Rationale:* Strategic, conditional: where Microsoft/Azure or .NET is the primary platform; supersedes Semantic Kernel and AutoGen.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Agents plus graph workflows, checkpointing, HITL, time travel, A2A/MCP; durability beta [VF: A4-S066, A4-S101] |
| Enterprise readiness | 4 | Library (rule 2) with Microsoft long-term support commitment; Foundry Hosted Agents GA [VF: A4-S012, B-L3-S006] |
| Security and compliance | 3 | Library (rule 2); hygiene not assessed; Azure/Foundry certifications out of record scope [AJ] |
| Deployment flexibility | 4 | Library anywhere; Foundry Hosted Agents and Azure Functions managed [VF: A4-S008, A4-S066] |
| Ecosystem | 4 | Foundry, Azure OpenAI, OpenAI, Copilot Studio, A2A, MCP, OTel [VF: A4-S066, A4-S008] |
| Reliability and maturity | 4 | GA April 2026 with LTS commitment; successor to two mature frameworks [VF: A4-S008, A4-S012] |
| Cost / TCO | 4 | Free MIT; durable hosting extra [VF: A4-S067] |
| Lock-in / portability | 3 | MIT, multi-provider, but Azure-first integrations [VF: A4-S066] |
| **Total (generic / FS)** | **3.80 / 3.65** | |

**Capabilities.** MIT framework (Python, .NET, Go) that separates Agents from graph-based Workflows (sequential, concurrent, handoff, group collaboration) with checkpointing, streaming, HITL and time travel; durable agents via Durable Task or Azure Durable Functions (beta); A2A, MCP, OTel; declared successor to Semantic Kernel and AutoGen; Foundry Hosted Agents for managed hosting [VF: A4-S066, A4-S012, A4-S101, A4-S102, B-L3-S006].

**Strengths**

- Explicit agents-versus-workflows split is the clearest H2 implementation [VF: A4-S066] [AJ]
- 1.0 with stable APIs and a long-term support commitment [VF: A4-S012, A4-S068]
- .NET first-class for Microsoft estates [VF: A4-S066]

**Limitations and risks**

- Durable extensions still beta [VF: A4-S101, A4-S102]
- Foundry hosting integration package for Python prerelease [VF: B-L3-S006]
- First-class integrations are Azure/Foundry [VF: A4-S066]
- Young GA (April 2026) [VF: A4-S008]

**Choose when**

- Microsoft/.NET estate, or Semantic Kernel/AutoGen code to migrate [AJ]

**Avoid when**

- You need GA durable execution today without adding Temporal or Durable Task [AJ]

**Nearest competitors:** L3-langgraph, L3-google-adk, L3-aws-strands-agentcore

**Regulated-FS note.** Migrate Semantic Kernel and AutoGen workloads here; until durable packages are GA, back long-running workflows with a GA durable engine [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Microsoft Corporation | Verified fact | A4-S067 |
| Category | Multi-language agent and multi-agent workflow framework (Python, .NET, Go) | Verified fact | A4-S066 |
| Version / lineup | agent-framework (Python) 1.20.0 (2 October 2026); 1.0.0 GA 2 April 2026 (Development Status: Production/Stable); durable extensions agent-framework-durabletask and agent-framework-azurefunctions still beta (1.0.0b260922) | Verified fact | A4-S008, A4-S101, A4-S102 |
| Licence | Open source, MIT | Verified fact | A4-S067, A4-S008 |
| Status events | 1 October 2025: first public preview on PyPI; 2 April 2026: 1.0.0 GA; Semantic Kernel README: 'Semantic Kernel is now Microsoft Agent Framework'; AutoGen placed in maintenance mode (no new features; community managed); last autogen-agentchat release 0.7.5 on 30 September 2025 | Verified fact | A4-S008, A4-S012, A4-S068, A4-S021, V1-S050, V1-S052 |
| Strategic direction | Declared 'enterprise-ready successor' to both Semantic Kernel and AutoGen; graph-based workflows (sequential, concurrent, handoff, group collaboration) with checkpointing, streaming, human-in-the-loop and time-travel; Foundry Hosted Agents; A2A and MCP interoperability; declarative YAML agents; Agent Skills | Verified fact | A4-S066, A4-S012, A4-S068 |
| What it does | Builds agents (chat-client based, multi-provider) and multi-agent workflows; middleware; OpenTelemetry observability; DevUI; durable agents via Durable Task or Azure Durable Functions that persist state and recover from failures. | Verified fact | A4-S066, A4-S101, A4-S102 |
| Stack position | L3; explicitly separates Agents from graph-based Workflows within one framework | Verified fact | A4-S066 |
| Integration | Python packages (agent-framework-core, -foundry, preview -copilotstudio), NuGet for .NET; A2A and MCP; OpenTelemetry | Verified fact | A4-S008, A4-S066, A4-S012 |
| Dependencies | Python >=3.10 or .NET (Go SDK separate repo); providers incl. Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK; optional Durable Task / Azure Functions | Verified fact | A4-S008, A4-S066, A4-S101 |
| Certifications | Not applicable to the MIT library; Azure/Foundry certifications out of scope for this record | Architectural judgement |  |
| GDPR / residency | Inherits the chosen model provider/hosting (e.g. Azure region) | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Microsoft states 1.0 comes with stable APIs and a commitment to long-term support | Verified fact | A4-S012, A4-S068 |
| Pricing | Free (MIT); hosting and models billed separately | Verified fact | A4-S067 |
| Infrastructure cost | Durable agents require a Durable Task scheduler or Azure Functions | Architectural judgement |  |
| Ecosystem | Microsoft Foundry, Azure OpenAI, OpenAI, Copilot Studio, GitHub Copilot SDK; A2A; MCP | Verified fact | A4-S066, A4-S008 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GA since April 2026; weekly-to-fortnightly minor releases (1.13 on 30 July 2026 to 1.20 on 2 October 2026) | Verified fact | A4-S008 |
| Deployment | saas: No for the framework; Foundry Hosted Agents provides managed hosting; managed_cloud: Yes (Foundry Hosted Agents; Azure Durable Functions); vpc_byoc: Yes (library runs inside the customer's own environment); private_cloud: Yes (library runs inside the customer's own environment); self_hosted: Yes; on_prem: Yes (library) | | |

## Pydantic AI (`L3-pydantic-ai`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Pydantic AI – type-safe

*Rationale:* Strategic, conditional: for Python teams wanting type-safe agents, typically as the typed agent step inside a Temporal or DBOS workflow; pin the major version (breaking v2 ten months after v1) and note that commercial support is not verified. Upgraded from Tactical by the reader at Checkpoint 4 (CP4-4); scores unchanged (FS 3.55) [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Typed agent loop, graph control flow, durable capabilities via Temporal/DBOS/Prefect, MCP [VF: A4-S119, A4-S045] |
| Enterprise readiness | 3 | Library (rule 2): enables controls in your estate; support not verified [NPV] |
| Security and compliance | 3 | Library hygiene: v1 security fixes promised for six months after v2 [VF: V1-S074]; inherits host controls |
| Deployment flexibility | 4 | Library anywhere; no managed runtime [VF: A4-S003] |
| Ecosystem | 4 | Temporal, DBOS, Prefect integrations co-maintained; Logfire OTel [VF: A4-S045] |
| Reliability and maturity | 3 | Production/Stable, but breaking v2 ten months after v1 [VF: A4-S003, A4-S044] |
| Cost / TCO | 4 | Free MIT; durability backend adds cost [VF: A4-S003] [AJ] |
| Lock-in / portability | 4 | MIT, model-agnostic, durability on standard engines [VF: A4-S003, A4-S119] |
| **Total (generic / FS)** | **3.60 / 3.55** | |

**Capabilities.** Typed, model-agnostic Python agent loop with structured outputs and tools, pydantic_graph for graph control flow, and durable execution attached as a capability via Temporal, DBOS or Prefect [VF: A4-S119, A4-S044, A4-S045].

**Strengths**

- Type-checked inputs and outputs suit numeric and structured tasks [AJ]
- Delegates durability to established engines instead of inventing its own [VF: A4-S045] [AJ]

**Limitations and risks**

- v2 (June 2026) removed graph persistence; two majors in about ten months [VF: A4-S003, A4-S044]
- Commercial support not publicly verified [NPV]
- Small vendor: US$12.5M Series A is the only round found [VF: A4-S046]

**Choose when**

- Python teams wanting a typed agent step inside a Temporal or DBOS workflow [AJ]

**Avoid when**

- You need a vendor-supported platform with SLAs [AJ]

**Nearest competitors:** L3-langgraph, L3-openai-agents-sdk, L3-temporal

**Regulated-FS note.** Pin the major version; v1 receives security fixes for at least six months after v2 [VF: V1-S074] [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Pydantic Services Inc. | Verified fact | A4-S003, A4-S046 |
| Category | Typed Python agent framework (agent loop) with optional graph library (pydantic_graph) and durable-execution integrations | Verified fact | A4-S119, A4-S044 |
| Version / lineup | pydantic-ai 2.54.0 (3 October 2026); v2.0.0 released 23 June 2026; v1 line still patched (1.107.7 on 30 September 2026) | Verified fact | A4-S003 |
| Licence | Open source, MIT | Verified fact | A4-S003, A4-S119 |
| Status events | 5 September 2025: v1.0.0; 23 June 2026: v2.0.0 (breaking: pydantic_graph.persistence removed); Pydantic AI Gateway (gateway.pydantic.dev) deprecated and moved into Logfire | Verified fact | A4-S003, A4-S044, A4-S046, V1-S074 |
| Strategic direction | v2 (first beta 20 May 2026) introduced a capability layer, a leaner core and 'the Harness'; durability is moving onto the capability layer (runtime extension point tracked for after v2). AI Gateway merged into Pydantic Logfire (adds failover, load balancing, DLP, spend caps) | Verified fact | A4-S044, A4-S046 |
| What it does | A typed, extensible agent loop for Python with model-agnostic providers, structured outputs and tools; pydantic_graph provides graph-based control flow; durable execution is attached as a capability via Temporal, DBOS or Prefect (plus Harness packages such as AWS Lambda and Step Persistence). | Verified fact | A4-S119, A4-S044, A4-S045 |
| Stack position | L3 agent framework; observability via Logfire (L9) and gateway via Logfire (C1) are separate commercial products | Verified fact | A4-S046 |
| Integration | Python library; MCP support; OpenTelemetry via Logfire; durable-execution capabilities (TemporalDurability, DBOSDurability, PrefectDurability) | Verified fact | A4-S045, A4-S119 |
| Dependencies | Python >=3.10; Pydantic; model provider SDKs; optional Temporal/DBOS/Prefect for durability | Verified fact | A4-S003, A4-S045 |
| Certifications | Not applicable to the open-source library; Logfire certifications out of scope for this record | Architectural judgement |  |
| GDPR / residency | Not applicable (library; data flows go to the customer's chosen model provider) | Architectural judgement |  |
| Security features | Logfire AI Gateway (separate product) offers DLP scanning of prompts/completions for secrets and PII, and spend caps | Verified fact | A4-S046 |
| Access controls | Not applicable (library) | Architectural judgement |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (MIT) | Verified fact | A4-S003 |
| Infrastructure cost | Costs are model tokens plus any durable-execution backend (Temporal cluster, database for DBOS) | Architectural judgement |  |
| Ecosystem | Temporal, DBOS and Prefect integrations co-maintained with those vendors; Logfire; GitHub Agentic Workflows harness | Verified fact | A4-S045, A4-S119 |
| Adoption signals | Pydantic raised a US$12.5M Series A led by Sequoia (announced with Logfire GA, c. late 2024); no later round found | Verified fact | A4-S046 |
| Maturity | First release May 2024; 1.0 September 2025; 2.0 June 2026; Development Status: Production/Stable; 344 releases on PyPI | Verified fact | A4-S003 |
| Deployment | saas: No; managed_cloud: No; vpc_byoc: Yes (library runs inside the customer's own environment); private_cloud: Yes (library runs inside the customer's own environment); self_hosted: Yes (library); on_prem: Yes (library) | | |

## Agent Development Kit (ADK) (`L3-google-adk`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud (rule 10: ADK on Agent Engine is Google's lead agent framework and runtime, matching Strands/AgentCore on AWS and Microsoft Agent Framework on Azure); no criterion at 1; scored as a library under rule 2, so enterprise readiness and security stay at 3. Tier changed from Tactical by CP4 reviewer C for rule-10 parity. Confirmed by the reader at Checkpoint 4 (CP4-4).

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Workflow Runtime, multi-agent, A2A Task API, HITL, evaluation [VF: A4-S114] |
| Enterprise readiness | 3 | Library (rule 2); no support commitment recorded [NPV] |
| Security and compliance | 3 | Library (rule 2); managed route on Agent Platform in ISO 42001 and SOC 2 scope [VF: A5-S028] |
| Deployment flexibility | 4 | Library anywhere; Cloud Run and Agent Engine [VF: A4-S114] |
| Ecosystem | 3 | MCP, OpenAPI, A2A; broader ecosystem not verified [VF: A4-S114] [NPV] |
| Reliability and maturity | 3 | 1.0 May 2025, 2.0 May 2026 [VF: A4-S017] |
| Cost / TCO | 4 | Free Apache-2.0 [VF: A4-S114] |
| Lock-in / portability | 3 | Apache-2.0 but Gemini-optimised and GCP-targeted [VF: A4-S114] |
| **Total (generic / FS)** | **3.45 / 3.35** | |

**Capabilities.** Apache-2.0 code-first agent framework (Python, Java, Kotlin, Go, TS); ADK 2.0 adds a graph-based Workflow Runtime (routing, fan-out/fan-in, loops, retry, state, HITL, nested workflows) and a Task API for agent-to-agent delegation; deploys to Cloud Run or Vertex AI Agent Engine [VF: A4-S114, A4-S017].

**Strengths**

- Explicit deterministic Workflow Runtime alongside agents [VF: A4-S114] [AJ]
- Tool-confirmation HITL and evaluation built in [VF: A4-S114]

**Limitations and risks**

- Two major versions in twelve months [VF: A4-S017]
- Gemini-optimised; Google Cloud deployment targets [VF: A4-S114]
- Security features and access controls not verified for the library [NPV]

**Choose when**

- Google Cloud estates, especially with Agent Engine [AJ]

**Avoid when**

- You need cross-cloud hosting parity [AJ]

**Nearest competitors:** L3-microsoft-agent-framework, L3-langgraph, L3-aws-strands-agentcore

**Regulated-FS note.** Treat Agent Engine as a hyperscaler service under CP2 Q1 and confirm its controls per service [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google | Verified fact | A4-S114 |
| Category | Open-source, code-first agent framework with a graph-based deterministic Workflow Runtime | Verified fact | A4-S114 |
| Version / lineup | google-adk 2.11.0 (2 October 2026); 2.0.0 on 19 May 2026; 1.0.0 on 20 May 2025; also Java, Kotlin, Go and TypeScript ports | Verified fact | A4-S017, A4-S114 |
| Licence | Open source, Apache-2.0 | Verified fact | A4-S114 |
| Status events | 19 May 2026: ADK 2.0.0 | Verified fact | A4-S017 |
| Strategic direction | ADK 2.0 adds a Workflow Runtime (routing, fan-out/fan-in, loops, retry, state, human-in-the-loop, nested workflows) and a Task API for agent-to-agent delegation; optimised for Gemini but model-agnostic | Verified fact | A4-S114 |
| What it does | Builds, evaluates and deploys agents and multi-agent hierarchies with tools (OpenAPI, MCP), tool-confirmation HITL, and deterministic graph workflows; deploys to Cloud Run or Vertex AI Agent Engine. | Verified fact | A4-S114 |
| Stack position | L3 framework; Vertex AI Agent Engine is the managed runtime | Verified fact | A4-S114 |
| Integration | Libraries; MCP and OpenAPI tools; A2A delegation via Task API | Verified fact | A4-S114 |
| Dependencies | Python (or Java/Kotlin/Go/TS); Gemini or other models | Verified fact | A4-S114 |
| Certifications | Not applicable to the library | Architectural judgement |  |
| GDPR / residency | Inherits hosting/model choice | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (Apache-2.0) | Verified fact | A4-S114 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | 1.0 May 2025; 2.0 May 2026 | Verified fact | A4-S017 |
| Deployment | saas: No; managed_cloud: Yes (Vertex AI Agent Engine, Cloud Run); vpc_byoc: Yes (library runs inside the customer's own environment); private_cloud: Yes (library runs inside the customer's own environment); self_hosted: Yes; on_prem: Yes (library) | | |

## OpenAI Agents SDK (Python: openai-agents; JS/TS: @openai/agents) (`L3-openai-agents-sdk`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Agent SDK (OpenAI logo)

*Rationale:* Good agent-step SDK, but pre-1.0 and surrounded by product churn.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Agent loop, handoffs, guardrails, sessions, approvals, tracing, sandboxes, Temporal/DBOS durability [VF: A4-S120, A4-S052, A4-S053] |
| Enterprise readiness | 3 | Library (rule 2); enterprise support not verified [NPV] |
| Security and compliance | 3 | Library (rule 2); harness keeps credentials away from model-generated code [VF: A4-S053]; hygiene not assessed |
| Deployment flexibility | 4 | Library anywhere; model calls to chosen provider [VF: A4-S005] |
| Ecosystem | 4 | MCP, sandbox partners, Temporal, DBOS, Bedrock Managed Agents [VF: A4-S053, A4-S055] |
| Reliability and maturity | 2 | Pre-1.0 versioning; neighbouring products sunset in 2026 [VF: A4-S005, A4-S054, A4-S056] |
| Cost / TCO | 4 | Free MIT [VF: A4-S005] |
| Lock-in / portability | 3 | MIT and provider-agnostic, but defaults favour OpenAI services [VF: A4-S120, A4-S052] |
| **Total (generic / FS)** | **3.45 / 3.30** | |

**Capabilities.** MIT, provider-agnostic multi-agent SDK: agents with tools, handoffs or agents-as-tools, input/output guardrails, sessions with resumable approvals, tracing, sandboxed agents; Temporal and DBOS integrations for durable runs. Distinct from the hosted Agents API (beta) and Agent Builder (shutting down 30 November 2026) [VF: A4-S120, A4-S052, A4-S053, A4-S055, A4-S054].

**Strengths**

- Compact primitives with guardrails and approvals built in [VF: A4-S120] [AJ]
- Works with 100+ non-OpenAI models [VF: A4-S120]

**Limitations and risks**

- Pre-1.0 (0.23.1) [VF: A4-S005]
- Tracing defaults to OpenAI's dashboard [VF: A4-S052]
- Adjacent OpenAI products are retired frequently [VF: A4-S056, A4-S054]
- Hosted Agents API is US-only with no ZDR at launch [VF: A4-S055]

**Choose when**

- An agent step inside a durable workflow, with a custom trace processor [AJ]

**Avoid when**

- You would use the hosted Agents API for UK/EU client data [AJ]

**Nearest competitors:** L3-pydantic-ai, L3-langgraph, L3-claude-agent-sdk

**Regulated-FS note.** Replace the default trace exporter with a firm-owned OTel processor before any client data flows [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | OpenAI | Verified fact | A4-S005 |
| Category | Open-source, provider-agnostic multi-agent SDK (agent loop, handoffs, guardrails, sessions, tracing, sandbox harness) | Verified fact | A4-S120, A4-S052 |
| Version / lineup | openai-agents 0.23.1 (2 October 2026); @openai/agents 0.19.0 (5 October 2026) | Verified fact | A4-S005, A4-S024 |
| Licence | Open source, MIT | Verified fact | A4-S005, A4-S024 |
| Status events | 4 March 2025: first PyPI release; 3 June 2026: Agent Builder (AgentKit) deprecation announced; shutdown 30 November 2026; Agents SDK is the code-based migration path; 26 August 2026: Assistants API sunset (Responses API is the replacement); 10 September 2026: separate hosted Agents API in public beta | Verified fact | A4-S005, A4-S054, A4-S056, A4-S055, V1-S051, V1-S083 |
| Strategic direction | 15 April 2026 'next evolution': model-native harness (configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP/skills/AGENTS.md), native sandbox execution with Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel, snapshot/rehydration; TypeScript parity May 2026. OpenAI also launched a hosted Agents API (public beta 10 September 2026) running a managed Codex harness, and is retiring Agent Builder in favour of the Agents SDK | Verified fact | A4-S053, A4-S055, A4-S054 |
| What it does | Lightweight framework for multi-agent workflows: agents with tools, handoffs (delegated agent takes over the conversation) or agents-as-tools, input/output guardrails, sessions (persistent memory, resumable approvals), built-in tracing, voice/realtime agents and sandboxed agents. Supports OpenAI Responses and Chat Completions APIs and 100+ other LLMs. | Verified fact | A4-S120, A4-S052 |
| Stack position | L3 agent framework. The hosted Agents API is a managed agent runtime (distinct product); tracing defaults to OpenAI's dashboard (L9 overlap) | Verified fact | A4-S055, A4-S052 |
| Integration | Python/TS libraries; MCP; custom trace processors; Temporal and DBOS integrations for durable long-running workflows incl. human-in-the-loop | Verified fact | A4-S052, A4-S053 |
| Dependencies | Python >=3.10 or Node; an LLM provider (OpenAI by default); optional sandbox provider; optional Temporal/DBOS for durability | Verified fact | A4-S005, A4-S053, A4-S052 |
| Certifications | Not applicable to the MIT library; OpenAI platform certifications covered by the L1 stream | Architectural judgement |  |
| GDPR / residency | SDK: inherits the configured model provider. Hosted Agents API (separate product): US data residency only and no Zero Data Retention support at launch | Verified fact | A4-S055 |
| Security features | Harness separated from compute so credentials stay away from model-generated code; sandbox snapshot and rehydration | Verified fact | A4-S053 |
| Access controls | Not applicable (library) | Architectural judgement |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | SDK free (MIT); model usage billed by provider. Hosted Agents API: sandboxes at standard container rates plus model usage | Verified fact | A4-S005, A4-S055 |
| Infrastructure cost | Sandboxed agents add container/sandbox-provider cost on top of tokens | Architectural judgement |  |
| Ecosystem | Sandbox partners (Blaxel, Cloudflare, Daytona, E2B, Modal, Runloop, Vercel); Temporal, DBOS; Amazon Bedrock Managed Agents built with OpenAI on the Agents API | Verified fact | A4-S053, A4-S052, A4-S055 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First release March 2025; still 0.x versioning (0.23.1); frequent releases (123 on PyPI) | Verified fact | A4-S005 |
| Deployment | saas: No for the SDK (library); hosted alternative is the separate Agents API (beta); managed_cloud: No for the SDK; Agents API runs in OpenAI-hosted or customer-connected sandboxes; vpc_byoc: Yes (library runs inside the customer's own environment); private_cloud: Yes (library runs inside the customer's own environment); self_hosted: Yes (library); on_prem: Yes (library; model calls still go to the chosen provider) | | |

## Strands Agents (open-source SDK) and Amazon Bedrock AgentCore (managed agent runtime and services) (`L3-aws-strands-agentcore`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where AWS is your primary cloud (rule 10, lead AWS agent runtime); deployment and lock-in at 2 accepted under rule 11 as an existing platform commitment.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Isolated runtime, memory, gateway, identity, any framework; no deterministic durable workflow engine [VF: A4-S116, B-L3-S004] |
| Enterprise readiness | 4 | Hyperscaler presumption (rule 6); platform controls presumed (CP2 Q1); confirm per service |
| Security and compliance | 4 | AgentCore in AWS SOC 1/2/3 and ISO 27001 scope, HIPAA eligible; SOC 2 type not stated, so 4 (rule 8) [VF: B-L5-S003] |
| Deployment flexibility | 2 | AgentCore AWS-only; Strands portable [VF: A4-S116, A4-S018] |
| Ecosystem | 4 | Any framework, MCP gateway, AG-UI [VF: A4-S116] |
| Reliability and maturity | 3 | AgentCore GA 13 October 2025; Strands 1.0 July 2025; SDK Alpha [VF: V1-S087, A4-S018, A4-S121] |
| Cost / TCO | 3 | Runtime pricing not retrieved [NPV]; consumption model assumed [AJ] |
| Lock-in / portability | 2 | Proprietary AWS-only service APIs [VF: A4-S116] |
| **Total (generic / FS)** | **3.40 / 3.25** | |

**Capabilities.** Strands Agents (Apache-2.0 model-driven agent SDK) plus Amazon Bedrock AgentCore, a framework-agnostic managed agent platform: Runtime with per-session microVM isolation (up to 8 hours per lifecycle), Memory, Gateway, Identity, Observability; hosts Strands, LangGraph, CrewAI, AutoGen or custom agents [VF: A4-S115, A4-S116, B-L3-S004].

**Strengths**

- Per-session microVM isolation and VPC/PrivateLink [VF: B-L3-S004]
- Runs any framework, so it separates runtime choice from framework choice [VF: A4-S116] [AJ]

**Limitations and risks**

- AWS-only, proprietary APIs [VF: A4-S116]
- Session state ephemeral by default; Runtime is not a durable workflow engine [VF: B-L3-S004]
- AgentCore SDK classified Alpha [VF: A4-S121]
- Execution-role credentials reachable from code in the microVM [VF: B-L3-S004]
- Runtime pricing not verified [NPV]

**Choose when**

- AWS is the primary cloud and you need a managed, isolated runtime for framework-built agents [AJ]

**Avoid when**

- Multi-cloud portability of the runtime is a requirement [AJ]

**Nearest competitors:** L3-microsoft-agent-framework, L3-google-adk, L3-langgraph

**Regulated-FS note.** Keep the workflow definition in a portable framework; scope execution roles tightly; platform controls presumed (CP2 Q1); confirm per service [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Amazon Web Services | Verified fact | A4-S116 |
| Category | Model-driven agent SDK plus framework-agnostic managed agent platform (Runtime, Memory, Gateway, Identity) | Verified fact | A4-S115, A4-S116 |
| Version / lineup | strands-agents 1.58.1 (6 October 2026; 1.0.0 15 July 2025); bedrock-agentcore SDK 1.24.1 (7 October 2026; classifier Alpha) | Verified fact | A4-S018, A4-S121 |
| Licence | SDKs Apache-2.0; AgentCore is a proprietary AWS managed service | Verified fact | A4-S018, A4-S121, A4-S116 |
| Status events | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | AgentCore deploys and operates agents 'using any framework and model' (Strands, LangGraph, CrewAI, AutoGen or custom) with session-isolated Runtime, Memory, Gateway (APIs to MCP tools) and Identity; supports AG-UI protocol. | Verified fact | A4-S116 |
| Stack position | L3 framework (Strands) and managed agent runtime (AgentCore); AgentCore Gateway/Identity overlap L4/C4 | Verified fact | A4-S116 |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Strands 1.0 July 2025; AgentCore SDK still Alpha-classified | Verified fact | A4-S018, A4-S121 |
| Deployment | saas: No; managed_cloud: Yes (AgentCore); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Strands SDK); on_prem: Not publicly verified | | |

## CrewAI (open-source framework: Crews and Flows); commercial platform CrewAI AMP (Agent Management Platform; earlier materials say CrewAI Enterprise; explicit rename notice not found) (`L3-crewai`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** CrewAI – multi-agent

*Rationale:* Both modes available, but abstractions are proprietary and durability is unproven.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Crews plus Flows cover multi-agent and workflow modes; HITL/durability not evidenced [VF: A4-S050] [NPV] |
| Enterprise readiness | 3 | AMP Enterprise SSO and RBAC verified; no SCIM, SLA or audit evidence, so 3 (rule 7) [VF: A4-S047] |
| Security and compliance | 3 | SOC 2 Type 2 report (June 2026) listed; HIPAA Type 1 only [VF: A4-S048] |
| Deployment flexibility | 4 | SaaS, VPC on AWS/Azure/GCP, on-prem, OSS self-host; air-gap not verified [VF: A4-S047, A4-S049] |
| Ecosystem | 4 | crewai-tools, AMP, HPE partnership; hosted by AgentCore [VF: A4-S004, A4-S049, A4-S116] |
| Reliability and maturity | 3 | 1.x since October 2025; very high release frequency [VF: A4-S004] |
| Cost / TCO | 3 | Free tier 50 executions/month; Enterprise custom-priced [VF: A4-S047] |
| Lock-in / portability | 3 | MIT framework, proprietary abstractions and AMP [VF: A4-S126, A4-S047] |
| **Total (generic / FS)** | **3.25 / 3.20** | |

**Capabilities.** MIT multi-agent framework with two modes: Crews (autonomous role-based agents) and Flows (event-driven, stateful process definitions); commercial platform CrewAI AMP (earlier materials call it CrewAI Enterprise) [VF: A4-S004, A4-S050, A4-S049, V1-S075].

**Strengths**

- Vendor itself recommends Flows as the outer process with Crews inside, which matches the H2 split [VF: A4-S050] [AJ]
- AMP deploys to cloud, customer VPC or on-premises [VF: A4-S047, A4-S049]

**Limitations and risks**

- Crew and Flow abstractions are CrewAI-specific [AJ]
- Durable execution and HITL not evidenced [NPV]
- Funding confirmed only to about US$20M [VF: A4-S148]
- Multi-agent Crews multiply LLM calls per task [AJ]

**Choose when**

- Teams that want a packaged multi-agent platform with on-prem option [AJ]

**Avoid when**

- The task is deterministic and does not need multiple autonomous agents [AJ]

**Nearest competitors:** L3-langgraph, L3-microsoft-agent-framework, L3-google-adk

**Regulated-FS note.** Use Flows for any regulated process and confine Crews to drafting or research sub-steps behind an approval gate [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | crewAI, Inc. | Verified fact | A4-S126 |
| Category | Multi-agent orchestration framework (role-based Crews) with event-driven Flows, plus a commercial agent management platform | Verified fact | A4-S004, A4-S050 |
| Version / lineup | crewai 1.15.24 (7 October 2026); 1.0.0 released 20 October 2025 | Verified fact | A4-S004 |
| Licence | Open source, MIT (framework); CrewAI AMP proprietary | Verified fact | A4-S004, A4-S126, A4-S047 |
| Status events | 20 October 2025: CrewAI 1.0.0; CrewAI AMP is the commercial platform; earlier materials call it CrewAI Enterprise (rename inferred from /enterprise/ doc paths and older naming; no explicit rename notice found; one blog used 'AOP') | Verified fact | A4-S004, A4-S049, V1-S075 |
| Strategic direction | Vendor recommends Flows as the outer 'process definition' with Crews invoked inside for autonomous collaborative steps; AMP adds deployment, SSO/RBAC, PII redaction and policies | Verified fact | A4-S050, A4-S047 |
| What it does | Crews: teams of role-playing agents that collaborate autonomously. Flows: event-driven, stateful process definitions (@start, @listen, @router, and_/or_) giving granular control; Flows can trigger Crews. AMP deploys and manages these in CrewAI cloud, customer VPC or on-premises. | Verified fact | A4-S004, A4-S050, A4-S049 |
| Stack position | L3 multi-agent framework; AMP also acts as an agent runtime/management platform | Verified fact | A4-S049 |
| Integration | Python library and CLI; crewai-tools package; AMP deployment | Verified fact | A4-S004, A4-S049 |
| Dependencies | Python >=3.10,<3.14; standalone (not built on LangChain); LLM providers via integrations | Verified fact | A4-S004 |
| Certifications | SOC 2 Type 2 (report dated June 2026 listed in trust centre); HIPAA audit report dated February 2026 listed (described as 'Type 1'; scope/BAA not shown) | Verified fact | A4-S048 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Enterprise plan: PII redaction, policies, workload identity | Verified fact | A4-S047 |
| Access controls | Enterprise plan: SSO, RBAC | Verified fact | A4-S047 |
| Enterprise support | Enterprise plan with 45-day onboarding; forward-deployed engineering and training sold separately | Verified fact | A4-S047 |
| Pricing | Free tier: 50 workflow executions/month; Enterprise custom-priced (pricing page metadata about a year old) | Verified fact | A4-S047 |
| Infrastructure cost | Multi-agent Crews multiply LLM calls per task; token cost dominates | Architectural judgement |  |
| Ecosystem | crewai-tools; AMP; HPE on-prem partnership | Verified fact | A4-S004, A4-S049 |
| Adoption signals | Vendor and TechCrunch (Oct 2024): US$18M seed+Series A (Boldstart, Craft, Earl Grey, Insight Partners); CrewAI 2025 blog: ~US$20M raised. A ~US$20M Series B (15 April 2026) appears only in PitchBook/Forge; no vendor or major-outlet announcement found | Verified fact | A4-S148, A4-S051 |
| Maturity | First release November 2023; 1.0 in October 2025; very high release frequency (461 PyPI releases incl. nightly dev builds) | Verified fact | A4-S004 |
| Deployment | saas: Yes (CrewAI cloud); managed_cloud: Yes; vpc_byoc: Yes (customer VPC on AWS, Azure or GCP); private_cloud: Yes (private VPC); self_hosted: Yes (OSS framework); on_prem: Yes (AMP on customer infrastructure; HPE pre-installed hardware offer) | | |

## LlamaIndex (open-source framework, incl. Workflows); commercial platform now named LlamaParse (formerly LlamaCloud), which includes LlamaAgents (`L3-llamaindex`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** LlamaIndex – document agents

*Rationale:* Capable but 0.x and no longer the vendor's focus; Renamed refers to LlamaCloud -> LlamaParse.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Workflows plus agents and RAG; HITL and durability not evidenced [VF: A4-S041] [NPV] |
| Enterprise readiness | 3 | Library (rule 2); LlamaParse Enterprise SSO is one verified control [VF: A1-S115, A1-S116] |
| Security and compliance | 3 | Library hygiene not assessed; LlamaParse SOC 2 Type II and HIPAA BAA [VF: A1-S115] |
| Deployment flexibility | 4 | Library anywhere; LlamaAgents managed or bring-your-own infrastructure [VF: A4-S042] |
| Ecosystem | 4 | Broad LLM and vector-store integrations [VF: A4-S117] |
| Reliability and maturity | 2 | 0.x versioning after three years; vendor focus moved to LlamaParse [VF: A4-S002, A4-S117] |
| Cost / TCO | 4 | Framework free (MIT) [VF: A4-S002] |
| Lock-in / portability | 3 | MIT but Workflows API is LlamaIndex-specific [VF: A4-S041] |
| **Total (generic / FS)** | **3.25 / 3.15** | |

**Capabilities.** MIT framework for RAG and agentic applications with Workflows, an event-driven, step-based engine with typed state and OpenTelemetry instrumentation; LlamaAgents deploys document agents on the proprietary LlamaParse platform (formerly LlamaCloud) [VF: A4-S117, A4-S041, A4-S042].

**Strengths**

- Workflows is a clean deterministic step engine usable outside the LlamaIndex ecosystem [VF: A4-S041] [AJ]
- Large integration catalogue for retrieval [VF: A4-S117]

**Limitations and risks**

- Vendor says its primary focus has shifted to LlamaParse [VF: A4-S117]
- Framework still 0.x after three years [VF: A4-S002]
- Human-in-the-loop and durable execution not evidenced in the fact base [NPV]

**Choose when**

- Retrieval-heavy agents already built on LlamaIndex [AJ]
- Document agents where LlamaParse is the chosen L8 parser [AJ]

**Avoid when**

- You need a long-term orchestration standard with roadmap commitment [AJ]

**Nearest competitors:** L3-langgraph, L3-pydantic-ai, L8-llamaparse

**Regulated-FS note.** Treat as a retrieval toolkit inside a governed workflow rather than as the orchestration standard [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LlamaIndex, Inc. (run-llama) | Verified fact | A4-S117 |
| Category | RAG / agentic application framework with an event-driven workflow engine; vendor's commercial focus is document parsing and document agents | Verified fact | A4-S117, A4-S041 |
| Version / lineup | llama-index / llama-index-core 0.14.25 (21 September 2026); llama-index-workflows 2.25.0 (25 September 2026) | Verified fact | A4-S002, A4-S013 |
| Licence | Open source, MIT (framework and workflows); LlamaParse platform is proprietary SaaS | Verified fact | A4-S002, A4-S013, A4-S127, A4-S117 |
| Status events | 30 June 2025: Workflows 1.0 released as a standalone package (llama-index-workflows); November 2025: LlamaAgents open preview; 2026: LlamaCloud renamed LlamaParse; 2026: vendor states primary focus shifted from OSS framework to LlamaParse | Verified fact | A4-S041, A4-S042, A4-S117 |
| Strategic direction | README (2026): 'our primary focus has shifted towards LlamaParse, along with liteparse and our benchmarking efforts'; the OSS framework remains available as an open toolkit. LlamaAgents (document agents built on Workflows) in open preview from November 2025; LlamaAgents Builder (natural-language to Workflow code) February 2026 | Verified fact | A4-S117, A4-S042 |
| What it does | Open-source framework for building agentic and RAG applications over data, with Workflows: a lightweight, event-driven, step-based engine for multi-step agentic applications in Python and TypeScript (typed state, resource injection, OpenTelemetry instrumentation). LlamaParse adds Parse, Extract, Index and LlamaAgents (deployed document agents). | Verified fact | A4-S117, A4-S041, A4-S013 |
| Stack position | L3 for the framework/Workflows; the commercial product is mainly L8 (document extraction, LlamaParse) and the graphic's 'document agents' descriptor reflects that. The framework is no longer the vendor's primary focus. | Verified fact | A4-S117 |
| Integration | Python/TS libraries; llamactl CLI to deploy Agent Workflows to LlamaCloud/LlamaParse or as a headless API; OpenTelemetry instrumentation | Verified fact | A4-S042, A4-S041 |
| Dependencies | Python >=3.9/3.10 or TypeScript; LLM and embedding providers; vector stores via integrations; LlamaParse API for managed parsing (optional) | Verified fact | A4-S002 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Framework free (MIT). LlamaParse metered in credits; third-party pages report ~US$1.25 per 1,000 credits in 2026 and ~10,000 free credits per month; vendor pricing page not retrieved | Reported | A4-S043 |
| Infrastructure cost | Self-hosted framework cost is driven by LLM/embedding tokens and the chosen vector store, not the library | Architectural judgement |  |
| Ecosystem | Large integration catalogue (LLMs, vector stores); Workflows usable outside the LlamaIndex ecosystem; LlamaParse usable with or without the framework | Verified fact | A4-S117, A4-S041 |
| Adoption signals | Funding reported as US$27.5M (Greylock, Norwest; Series A May 2025) by Tracxn; another source reports US$19M (conflict) | Reported | A4-S043 |
| Maturity | Framework first released February 2023; still 0.x versioning (0.14.25); Workflows 1.0 since June 2025 and now 2.x | Verified fact | A4-S002, A4-S013, A4-S041 |
| Deployment | saas: Yes (LlamaParse / LlamaAgents managed cloud); managed_cloud: Yes (LlamaAgents managed cloud); vpc_byoc: Yes (LlamaAgents: 'bring-your-own infrastructure' option); private_cloud: Not publicly verified; self_hosted: Yes (OSS framework); on_prem: Not publicly verified | | |

## AI SDK (by Vercel); npm package 'ai' (`L3-vercel-ai-sdk`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** AI SDK – AI SDK (triangle logo)

*Rationale:* Good TS application toolkit; fast-moving majors; not an orchestration standard.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Unified model API, tools, ToolLoopAgent, UI streaming; durability via separate Workflow SDK [VF: A4-S069, A4-S071] |
| Enterprise readiness | 3 | Library (rule 2); enterprise support not verified [NPV] |
| Security and compliance | 3 | Library (rule 2); Apache-2.0 licence clear [VF: A4-S070]; hygiene not assessed |
| Deployment flexibility | 4 | Any Node runtime [VF: A4-S069] |
| Ecosystem | 4 | Major UI frameworks and model providers [VF: A4-S069] |
| Reliability and maturity | 2 | Major version roughly every six months [VF: A4-S022] |
| Cost / TCO | 4 | Free; gateway priced separately [VF: A4-S070] |
| Lock-in / portability | 3 | Apache-2.0; optional gateway default [VF: A4-S069] |
| **Total (generic / FS)** | **3.25 / 3.15** | |

**Capabilities.** Apache-2.0 TypeScript toolkit (npm 'ai') for provider-agnostic generation, structured output, tool calling and ToolLoopAgent agents, with UI hooks for React, Svelte, Vue and Angular; companion Workflow SDK makes TS/JS functions durable [VF: A4-S069, A4-S071, A4-S106].

**Strengths**

- Best fit for TypeScript front ends that stream agent output to the browser [AJ]
- Workflow SDK can be self-hosted with Postgres [VF: A4-S071]

**Limitations and risks**

- Three major versions in about eleven months [VF: A4-S022]
- Defaults to Vercel AI Gateway for model access [VF: A4-S069]
- Vercel certifications not verified [NPV]

**Choose when**

- The agent is part of a Next.js or TypeScript application tier [AJ]

**Avoid when**

- Back-office regulated workflows owned by a Python data team [AJ]

**Nearest competitors:** L3-openai-agents-sdk, L3-langgraph, L3-microsoft-agent-framework

**Regulated-FS note.** Use direct provider packages or the firm's gateway, not the Vercel AI Gateway default, for client data [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Vercel, Inc. | Verified fact | A4-S070, A4-S069 |
| Category | Provider-agnostic TypeScript toolkit for AI applications and agents (generation, structured output, tool-loop agents, UI hooks) | Verified fact | A4-S069 |
| Version / lineup | ai 7.0.131 (7 October 2026); 7.0.0 released 25 June 2026 (6.0.0 22 December 2025; 5.0.0 31 July 2025) | Verified fact | A4-S022, V1-S082 |
| Licence | Open source, Apache-2.0 | Verified fact | A4-S022, A4-S070 |
| Status events | 25 June 2026: AI SDK 7.0.0; 30 September 2026: Workflow SDK 5.0.0 | Verified fact | A4-S022, A4-S106 |
| Strategic direction | Defaults to the Vercel AI Gateway for model access (direct provider packages also supported); ToolLoopAgent abstraction; companion Workflow SDK (npm 'workflow' 5.1.0) makes TS/JS functions durable | Verified fact | A4-S069, A4-S071, A4-S106 |
| What it does | Unified API across model providers for text and structured generation, tool calling and agents (ToolLoopAgent), plus AI SDK UI hooks for React, Svelte, Vue and Angular and streaming agent responses to the browser. | Verified fact | A4-S069 |
| Stack position | L3 (TypeScript agent/app framework) with an application/UI layer component; model routing via Vercel AI Gateway overlaps L2/C1 | Verified fact | A4-S069 |
| Integration | TypeScript library; provider adapters; AI Gateway model strings; UI framework hooks | Verified fact | A4-S069 |
| Dependencies | Node.js 22+; provider packages (@ai-sdk/openai, @ai-sdk/anthropic, @ai-sdk/google, ...) or Vercel AI Gateway | Verified fact | A4-S069 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not applicable (library) | Architectural judgement |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (Apache-2.0); AI Gateway usage priced separately (not retrieved) | Verified fact | A4-S070 |
| Infrastructure cost | Not material for the library | Architectural judgement |  |
| Ecosystem | Next.js, React, Svelte, Vue, Angular; providers OpenAI, Anthropic, Google and others; Vercel Sandbox; Workflow SDK | Verified fact | A4-S069, A4-S071 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Package name 'ai' reused; AI SDK 3.0 February 2024; major version roughly every 6 months (5.0 July 2025, 6.0 December 2025, 7.0 June 2026) | Verified fact | A4-S022 |
| Deployment | saas: No; managed_cloud: No; vpc_byoc: Yes (library runs inside the customer's own environment); private_cloud: Yes (library runs inside the customer's own environment); self_hosted: Yes (library runs in any Node runtime); on_prem: Yes (library) | | |

## Claude Agent SDK (Python: claude-agent-sdk; TypeScript: @anthropic-ai/claude-agent-sdk); formerly Claude Code SDK (`L3-claude-agent-sdk`)

**Tier:** Experimental · **Flags:** Renamed · **Original graphic label:** Agent SDK (Anthropic logo)

*Rationale:* Alpha (the vendor's own PyPI classifier), single-model and subprocess-bound; stays Experimental. Maturity set to 2 by the reader at Checkpoint 4 (CP4-9), in line with the OpenAI Agents SDK; technical 3 and deployment 3 are the peer-consistent values (CP4 review C). Conflict of interest disclosed.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Rich autonomous harness, but no workflow engine or built-in durable execution [VF: A4-S027, A4-S122]; borderline 3/4 resolved down |
| Enterprise readiness | 3 | Library (rule 2): permission modes and hooks; API-key auth; enterprise support not verified [VF: A4-S027] [NPV] |
| Security and compliance | 3 | Library (rule 2); inherits Claude API terms where ZDR is available, but Managed Agents excluded from ZDR [VF: A4-S123] |
| Deployment flexibility | 3 | Self-hosted in containers/Kubernetes; model inference remains a cloud API; subprocess-per-session hosting [VF: A4-S122]; borderline 3/4 resolved down |
| Ecosystem | 3 | MCP, plugins and skills; Claude models only [VF: A4-S027] |
| Reliability and maturity | 2 | Alpha development status (PyPI 'Development Status: 3 - Alpha'), pre-1.0, renamed September 2025 [VF: A4-S006, A4-S029, B-REVC-S001]. Scored 2, the same as the pre-1.0 OpenAI Agents SDK, by the reader at Checkpoint 4 (CP4-9; previously 1 under a strict reading of the anchor). The Alpha label is recorded as a limitation and reflected in the Experimental tier. |
| Cost / TCO | 3 | No SDK charge; compute scales with concurrent sessions [VF: A4-S122] [AJ] |
| Lock-in / portability | 2 | Claude-only, bundled CLI binary, Commercial Terms [VF: A4-S027, A4-S092] |
| **Total (generic / FS)** | **2.85 / 2.75** | |

**Capabilities.** Anthropic's agent harness SDK (formerly Claude Code SDK): embeds Claude Code's agent loop, built-in file/shell/web tools, hooks, subagents, MCP, permission modes and resumable/forkable sessions as a Python or TypeScript library; spawns one Claude Code CLI subprocess per session [VF: A4-S027, A4-S122, A4-S028]. Conflict of interest: Anthropic product scored by an Anthropic model.

**Strengths**

- Permission modes and hooks give fine-grained tool approval [VF: A4-S027]
- Strong fit for code- and file-centric autonomous tasks [AJ]

**Limitations and risks**

- Python package classified Alpha; 0.x versioning [VF: A4-S006]
- Claude models only, via Claude API, Bedrock or Google Cloud [VF: A4-S006, A4-S122]
- Use governed by Anthropic Commercial Terms despite the MIT repository licence [VF: A4-S092, V1-S048]
- One long-lived subprocess per session; transcripts on local disk unless a SessionStore is configured [VF: A4-S122]
- Claude Managed Agents is excluded from ZDR [VF: A4-S123]
- No deterministic workflow engine [VF: A4-S027]

**Choose when**

- A sandboxed autonomous sub-task (e.g. code or document manipulation) inside a firm-owned workflow, where Claude is already an approved model [AJ]

**Avoid when**

- You need model portability or a deterministic workflow engine [AJ]
- A regulated process would run on an Alpha-classified dependency [AJ]

**Nearest competitors:** L3-openai-agents-sdk, L3-langgraph, L3-pydantic-ai

**Regulated-FS note.** Run only in sandboxed containers with network controls, under a workflow engine that owns state and approvals; independent alternatives are LangGraph and Pydantic AI [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Anthropic, PBC | Verified fact | A4-S092, A4-S027 |
| Category | Agent harness SDK that embeds Claude Code's agent loop, built-in tools and context management as a library | Verified fact | A4-S027 |
| Version / lineup | claude-agent-sdk 0.2.164 (6 October 2026; PyPI classifier 'Development Status: 3 - Alpha'); @anthropic-ai/claude-agent-sdk 0.3.293 (7 October 2026) | Verified fact | A4-S006, A4-S023 |
| Licence | Python repository LICENSE is MIT; npm package licence field reads 'SEE LICENSE IN README.md'; Anthropic docs state use of the SDK is governed by Anthropic's Commercial Terms of Service (except components under their own licence) | Verified fact | A4-S092, A4-S006, A4-S023, A4-S027, V1-S048 |
| Status events | 29 September 2025: Claude Code SDK renamed Claude Agent SDK (claude-agent-sdk 0.1.0 first published to PyPI 28 September 2025 UTC) (packages claude-code-sdk -> claude-agent-sdk, @anthropic-ai/claude-code -> @anthropic-ai/claude-agent-sdk); claude-code-sdk marked deprecated and no longer maintained (last release 0.0.25, 29 September 2025) | Verified fact | A4-S029, A4-S028, A4-S011, V1-S049 |
| Strategic direction | Positioned for agents beyond coding; Anthropic also offers Claude Managed Agents (beta), a hosted agent harness with Anthropic-managed or self-hosted sandboxes, as the hosted alternative | Verified fact | A4-S028, A4-S027, A4-S124 |
| What it does | Gives developers the same tools, agent loop and context management that power Claude Code, programmable in Python and TypeScript: built-in file/shell/web tools, hooks, subagents, MCP, permissions, sessions (resume/fork), skills, commands, memory and plugins. | Verified fact | A4-S027 |
| Stack position | L3 agent harness (autonomous agent loop). It is not a deterministic workflow engine; it runs as a supervised CLI subprocess per session | Verified fact | A4-S027, A4-S122 |
| Integration | Python/TS libraries; MCP for tools/data; hooks; CLI subprocess with JSON output for other languages | Verified fact | A4-S027 |
| Dependencies | Bundled Claude Code CLI binary (spawned as a subprocess per session over stdio); Python >=3.10 or Node; Claude models via the Claude API, or provider endpoints on Amazon Bedrock or Google Cloud's Agent Platform; durable store needed to persist session transcripts beyond local disk | Verified fact | A4-S006, A4-S122 |
| Certifications | Not applicable to the SDK; Anthropic platform certifications are covered in the L1 Anthropic record (stream A5) | Architectural judgement |  |
| GDPR / residency | SDK inherits the API arrangement: ZDR is available per organisation for eligible Claude API features and for Claude Code used with Commercial-org API keys; Claude Managed Agents is excluded from ZDR (session transcripts persist until deleted); on Bedrock / Google Cloud the cloud provider is the data processor | Verified fact | A4-S123 |
| Security features | Permission modes controlling which tools run automatically or need approval; hooks; recommended sandboxed containers for process isolation and network control | Verified fact | A4-S027, A4-S122 |
| Access controls | Third-party products may not offer claude.ai login or rate limits unless previously approved; API-key authentication required | Verified fact | A4-S027 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | SDK has no separate charge identified; usage billed as Claude API tokens (pricing covered by L1 stream) | Architectural judgement |  |
| Infrastructure cost | One long-lived subprocess per concurrent session (own shell, working directory and transcript), so compute scales with concurrent sessions rather than requests | Verified fact | A4-S122 |
| Ecosystem | MCP, Claude Code plugins/skills; runs on Claude API, Amazon Bedrock or Google Cloud; OpenAI publishes a migration cookbook from the Claude Agent SDK to its Agents SDK and Anthropic publishes the reverse | Verified fact | A4-S027, A4-S122, A4-S028 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Renamed and relaunched September 2025; 0.x versioning; Python package classified Alpha; very frequent releases (149 on PyPI) | Verified fact | A4-S006, A4-S029 |
| Deployment | saas: No for the SDK; hosted alternative is Claude Managed Agents (beta); managed_cloud: No for the SDK; Managed Agents runs in Anthropic-managed cloud sandboxes or self-hosted sandboxes; vpc_byoc: Yes (self-hosted in customer containers/Kubernetes); private_cloud: Yes (self-hosted); self_hosted: Yes; on_prem: Yes (process runs on customer infrastructure; model inference remains a cloud API call) | | |

## Mistral Agents API (exposed through the mistralai Python and TypeScript client SDKs, with an 'agents' extra) and Mistral Workflows (mistralai-workflows SDK); no separately branded 'Mistral Agents SDK' product found (`L3-mistral-agents`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** Mistral – Agents SDK

*Rationale:* Real products under a different name; beta status and proprietary hosted state. Tile relabelled 'Mistral Agents API (+ Workflows)'.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Hosted agents plus durable Workflows, but beta [VF: A4-S057, A4-S058] |
| Enterprise readiness | 2 | SSO/RBAC/audit not publicly verified; capped at 2 [NPV] |
| Security and compliance | 3 | Company-level SOC 2 Type II, ISO 27001, ISO 27701; product scope not stated, so one below (rule 8) [VF: A4-S060] |
| Deployment flexibility | 3 | SaaS; Workflows workers in customer Kubernetes, control plane Mistral-hosted [VF: A4-S058] |
| Ecosystem | 3 | MCP connectors; Temporal underneath [VF: A4-S057, A4-S058] |
| Reliability and maturity | 2 | Beta / Public Preview components; breaking SDK majors [VF: A4-S061, A4-S007] |
| Cost / TCO | 2 | Pricing not publicly verified; customer-run worker infrastructure [NPV] [VF: A4-S058] |
| Lock-in / portability | 2 | Proprietary hosted API, Mistral-model-centric [VF: A4-S057] |
| **Total (generic / FS)** | **2.60 / 2.55** | |

*Evidence rules applied:* enterprise_readiness capped at 2: access controls NPV

**Capabilities.** No distinct 'Mistral Agents SDK' exists. Mistral offers the Agents API (persistent agents, connectors incl. MCP, branchable stateful conversations, handoffs) through the general mistralai SDKs, and Mistral Workflows, a Temporal-based durable workflow SDK with Mistral-hosted control plane and customer-run workers [VF: A4-S057, A4-S058, A4-S061].

**Strengths**

- EU hosting by default for the company's services [VF: A5-S075]
- Workflows brings Temporal-grade durability with HITL decorators [VF: A4-S058]

**Limitations and risks**

- Agents API in beta namespace; Workflows Beta/Public Preview; breaking SDK majors March and September 2026 [VF: A4-S057, A4-S061, A4-S007, V1-S065]
- State lives in Mistral cloud unless store=False [VF: A4-S057]
- Access controls not publicly verified [NPV]
- Pricing not publicly verified [NPV]

**Choose when**

- An EU-hosted, Mistral-model estate wanting managed agents [AJ]

**Avoid when**

- You need a portable framework or GA components [AJ]

**Nearest competitors:** L3-openai-agents-sdk, L3-temporal, L3-langgraph

**Regulated-FS note.** Run conversations with store=False and keep the workflow definition in the firm's own Temporal or framework code [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Mistral AI | Verified fact | A4-S057, A4-S125 |
| Category | Hosted agent API (stateful conversations, connectors, handoffs) plus a Temporal-based durable workflow platform | Verified fact | A4-S057, A4-S058 |
| Version / lineup | mistralai (Python) 3.1.0 (6 October 2026; 3.0.0 on 28 September 2026); @mistralai/mistralai 2.7.0 (9 September 2026); mistralai-workflows 3.15.0 (14 September 2026, Beta) | Verified fact | A4-S007, A4-S025, A4-S061 |
| Licence | Client SDKs Apache-2.0; mistralai-workflows Apache-2.0; Agents API and Workflows control plane are proprietary hosted services | Verified fact | A4-S125, A4-S025, A4-S061 |
| Status events | SDK 3.0.0 (28 September 2026): HTTPX2, code_interpreter/web_search tools removed from chat/agents completions (use Conversations API or an agent); Le Chat rebranded (Work/Vibe naming in docs); Le Chat agents cannot be used programmatically | Verified fact | A4-S059, A4-S007, A4-S057 |
| Strategic direction | Agents API launched as a dedicated agentic API alongside chat completions; Studio adds built-in and custom MCP connectors with human-in-the-loop approvals; Mistral Workflows (v3.0 public, c. September 2026) built on Temporal with Mistral-hosted control plane and customer-run workers | Verified fact | A4-S057, A4-S058 |
| What it does | Agents API: create persistent agents with built-in connectors (code execution, web search, image generation, document library/RAG, MCP), stateful conversations that can be branched, and handoffs between agents executed server-side or client-side. Workflows: Python SDK with decorators for retries, timeouts, tracing, rate limiting and human-in-the-loop, with event-history durability. | Verified fact | A4-S057, A4-S058, A4-S061 |
| Stack position | L3, but as a vendor-hosted agent runtime rather than a portable framework; Workflows is a durable workflow engine (H2) | Verified fact | A4-S057, A4-S058 |
| Integration | REST API and client SDKs (Python/TS); MCP connectors; Workflows Python SDK | Verified fact | A4-S057, A4-S061 |
| Dependencies | Mistral cloud (La Plateforme/Studio); Mistral models; Workflows workers on customer Kubernetes via Helm connecting to Mistral-hosted Temporal cluster | Verified fact | A4-S058 |
| Certifications | Mistral AI: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27701:2019 (company-level; scope/dates not seen) | Verified fact | A4-S060 |
| GDPR / residency | Third-party summaries say EU hosting by default with optional US endpoint and ZDR negotiable via enterprise sales; Agents API conversations can be run with store=False (history not stored on Mistral cloud) | Reported | A4-S060, A4-S057 |
| Security features | Connector tool allow/deny lists; human-in-the-loop approval for sensitive actions | Verified fact | A4-S057 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Workflows requires customer-operated worker infrastructure (Kubernetes) | Verified fact | A4-S058 |
| Ecosystem | MCP connectors (built-in and custom); Temporal (Workflows engine) | Verified fact | A4-S057, A4-S058 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Agents API under client.beta namespace in SDK examples; Workflows SDK classified Beta; durable agents in Public Preview | Verified fact | A4-S057, A4-S061, V1-S065 |
| Deployment | saas: Yes; managed_cloud: Yes; vpc_byoc: Yes (partial: Workflows workers run in customer Kubernetes; control plane Mistral-hosted); private_cloud: Not publicly verified; self_hosted: Yes (partial: Workflows LocalSession for experimental or on-premises use); on_prem: Not publicly verified | | |

# L2: Inference, serving and model access

## vLLM (`L2-vllm`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** vLLM – high-throughput

*Rationale:* Default serving engine for any self-hosted route; neutral governance; conditional on patch and model-provenance discipline

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading depth: quantisation, speculative decoding, prefix caching, disaggregation, multi-hardware [VF: A4-S063] |
| Enterprise readiness | 4 | Rule 2: enables in-estate serving; inherits host controls; commercial support via Red Hat AI Inference lifts the 4 cap [VF: B-L2-S001] |
| Security and compliance | 3 | Rule 2 hygiene: published advisory process with fixed versions [VF: A4-S063, B-L2-S004], but several 2026 RCE advisories, one critical |
| Deployment flexibility | 5 | Self-host, private cloud, on-prem, and managed via third parties [VF: A4-S063, A4-S081] |
| Ecosystem | 5 | De-facto standard with OpenAI-compatible API; 2,000+ contributors [VF: A4-S063] |
| Reliability and maturity | 4 | Foundation-hosted since May 2025 [VF: A4-S146]; held at 4 for pre-1.0 versioning and fast cadence [VF: A4-S009] |
| Cost / TCO | 4 | Free; cost is GPU hours and operations [AJ] |
| Lock-in / portability | 5 | Apache-2.0, open APIs, neutral governance [VF: A4-S009, A4-S146] |
| **Total (generic / FS)** | **4.35 / 4.30** | |

**Capabilities.** Apache-2.0 LLM inference and serving engine (0.31.0, 5 October 2026), PyTorch Foundation-hosted since 7 May 2025, with PagedAttention, continuous batching, prefix caching, quantisation (FP8, MXFP4, NVFP4, INT4/8, GPTQ/AWQ, GGUF), speculative decoding (n-gram, suffix, EAGLE, DFlash), disaggregated prefill/decode/encode, OpenAI-compatible and Anthropic Messages APIs, 200+ architectures and multi-vendor hardware [VF: A4-S009, A4-S063, A4-S146]. A commercially supported distribution exists (Red Hat AI Inference) [VF: B-L2-S001].

**Strengths**

- Broadest optimisation feature set inside one engine [VF: A4-S063] [AJ]
- Neutral foundation governance and Apache-2.0 [VF: A4-S146, A4-S009]
- De-facto substrate: under Hugging Face Endpoints, llm-d and Dynamo [VF: A4-S081, A4-S089, A4-S090]

**Limitations and risks**

- Pre-1.0 with roughly fortnightly releases (28 in 2026) [VF: A4-S009]
- A run of 2026 code-execution advisories, including critical CVE-2026-22778, mostly via untrusted model files or media inputs [VF: B-L2-S004]
- No identity, audit or tenancy of its own; inherits host and gateway controls [AJ]

**Choose when**

- You self-host open-weight models on your own or private-cloud GPUs [AJ]
- You want the default engine with the widest model and hardware coverage [AJ]

**Avoid when**

- You cannot run a monthly patch cadence and model-provenance controls [AJ]
- You have no GPU capacity or SRE capability; use managed access instead [AJ]

**Nearest competitors:** L2-sglang, TensorRT-LLM, L2-hugging-face

**Regulated-FS note.** Run behind the gateway (C1), load only allow-listed, scanned weights with trust_remote_code off, pin versions and track advisories [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | vLLM project, a PyTorch Foundation-hosted project (Linux Foundation) since May 2025; originated at UC Berkeley Sky Computing Lab; lead maintainers include Woosuk Kwon, Zhuohan Li, Simon Mo, Kaichao You and Robert Shaw | Verified fact | A4-S146, A4-S063, A4-S064 |
| Category | Open-source LLM inference and serving engine | Verified fact | A4-S063 |
| Version / lineup | vllm 0.31.0 (5 October 2026); 28 releases in 2026 (0.14.0 in January to 0.31.0) | Verified fact | A4-S009 |
| Licence | Open source, Apache-2.0 | Verified fact | A4-S009 |
| Status events | 7 May 2025: accepted as a PyTorch Foundation-hosted project when the foundation became an umbrella foundation | Verified fact | A4-S146, V1-S064 |
| Strategic direction | PagedAttention, continuous batching, prefix caching, quantisation (FP8, MXFP4, NVFP4, INT4/8, GPTQ/AWQ, GGUF), speculative decoding (n-gram, suffix, EAGLE, DFlash), disaggregated prefill/decode/encode; OpenAI-compatible server plus Anthropic Messages API and gRPC; 200+ architectures; NVIDIA, AMD, Intel GPUs, CPUs and plugins (TPU, Gaudi, Ascend, Apple Silicon) | Verified fact | A4-S063 |
| What it does | High-throughput, memory-efficient inference and serving library and server for LLMs, multimodal, embedding and reward models. | Verified fact | A4-S063 |
| Stack position | Serving engine (L2) underneath managed services (e.g. Hugging Face Endpoints) and distributed orchestration layers (llm-d, NVIDIA Dynamo) | Verified fact | A4-S081, A4-S089, A4-S090 |
| Integration | OpenAI-compatible API, Anthropic Messages API, gRPC; Python library | Verified fact | A4-S063 |
| Dependencies | Python <3.15,>=3.10; PyTorch; accelerators (NVIDIA/AMD/Intel GPUs, CPUs, hardware plugins) | Verified fact | A4-S009, A4-S063 |
| Certifications | Not applicable (open-source software) | Architectural judgement |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (Apache-2.0) | Verified fact | A4-S009 |
| Infrastructure cost | Dominated by accelerator hours and memory; throughput features (batching, quantisation, prefix caching) drive cost per token | Architectural judgement |  |
| Ecosystem | Hugging Face models; llm-d builds on vLLM; Dynamo supports vLLM backend; sponsors listed on vllm.ai | Verified fact | A4-S063, A4-S089, A4-S090 |
| Adoption signals | README: 'over 2000 contributors' from 'many dozens of academic institutions and companies' | Verified fact | A4-S063 |
| Maturity | First PyPI release June 2023; still 0.x; roughly fortnightly releases | Verified fact | A4-S009 |
| Deployment | saas: No; managed_cloud: Yes (via third parties, e.g. Hugging Face Inference Endpoints); vpc_byoc: Yes (self-deployed); private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## Fireworks AI (`L2-fireworks-ai`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Fireworks AI – fast inference

*Rationale:* Strategic, conditional: for managed open-model inference, once its ISO 27001, 27701 and 42001 certificates are confirmed (trust-centre and docs pages conflict); the strongest controls among the independent inference clouds. For client data use EU dedicated or BYOC deployments, because the self-serve residency setting is US-only. Upgraded from Tactical ('candidate for Strategic after due diligence') by the reader at Checkpoint 4 (CP4-4); scores unchanged (FS 3.65) [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Serverless, dedicated, batch, fine-tuning/RFT, BYOC, FireRouter [VF: A4-S135, A4-S152] |
| Enterprise readiness | 4 | SSO, RBAC and audit logs with CLI (rule 7 to 4); audit logs are recent [VF: A4-S152] |
| Security and compliance | 3 | SOC 2 Type II, CMK, ZDR default; ISO claims not relied on (V1 section 4), so 3 [VF: A4-S133, V1-S067] |
| Deployment flexibility | 4 | SaaS, dedicated, reserved, BYOC; no on-prem [VF: A4-S152] |
| Ecosystem | 4 | OpenAI-compatible; Microsoft Foundry; Hugging Face partner [VF: A4-S134, A4-S075] |
| Reliability and maturity | 3 | GA, well funded; revenue concentration reported [VF: A4-S141] |
| Cost / TCO | 3 | Transparent but GPU rates higher than peers; batch at 50% [VF: A4-S135] |
| Lock-in / portability | 4 | Open models portable; BYOC reduces data-plane lock-in [VF: A4-S152] |
| **Total (generic / FS)** | **3.65 / 3.65** | |

**Capabilities.** Managed inference and fine-tuning for open models (serverless, on-demand and reserved dedicated, batch, RFT), hybrid BYOC in the customer VPC, customer-managed keys, SSO (OIDC/SAML), RBAC and audit logs; ZDR by default for open models except the Response API (30-day storage by default); SOC 2 Type II, while ISO 27001/27701/42001 claims conflict across its own pages [VF: A4-S135, A4-S152, A4-S134, A4-S133, V1-S067].

**Strengths**

- ZDR by default and BYOC data plane [VF: A4-S134, A4-S152]
- Customer-managed keys logged in the customer's cloud audit log [VF: A4-S152]
- Microsoft Foundry partnership [VF: A4-S134]

**Limitations and risks**

- ISO claims conflict ('achieved' vs 'in progress') [VF: V1-S067]
- Self-serve data-residency setting lists US only; EU via sales [VF: A4-S134]
- Revenue concentration reported [VF: A4-S141]
- Response API exception to ZDR [VF: A4-S134]

**Choose when**

- Dedicated or BYOC open-model serving where you want a managed engine without running GPUs [AJ]

**Avoid when**

- The Response API for client data without store=False [VF: A4-S134] [AJ]
- ISO certificates are a hard gate before you have seen them [AJ]

**Nearest competitors:** L2-together-ai, L2-hugging-face, Hyperscaler model catalogues

**Regulated-FS note.** Request ISO certificates and BAA terms from the trust centre; prefer BYOC or EU dedicated deployments; disable Response API storage [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Fireworks AI, Inc.; privately held | Verified fact | A4-S136, A4-S141 |
| Category | Managed inference and fine-tuning platform for open models (serverless, on-demand dedicated, reserved, BYOC) | Verified fact | A4-S135, A4-S152 |
| Version / lineup | Official SDK fireworks-ai 1.2.20 (6 October 2026); serverless, on-demand deployments, batch inference, fine-tuning/RFT, Virtual Cloud (GA), FireRouter | Verified fact | A4-S094, A4-S134, A4-S152 |
| Licence | Proprietary cloud service; official Python SDK Apache-2.0 | Verified fact | A4-S094 |
| Status events | 28 October 2025: Series C US$250M at US$4B; 15-16 July 2026: Series D US$1.505B at US$17.5B (Atreides, Index, TCV) | Verified fact | A4-S136, A4-S141, V1-S058 |
| Strategic direction | Series D (July 2026) to expand compute and engineering; positioning on 'specialised intelligence' (customers fine-tuning open models on proprietary data); reports >US$1B annualised revenue and >40 trillion tokens/day | Verified fact | A4-S141 |
| What it does | Serves open models via serverless per-token APIs and per-GPU-second dedicated deployments, batch inference at 50% of serverless price, fine-tuning and reinforcement fine-tuning, with enterprise reserved capacity and hybrid BYOC. | Verified fact | A4-S135, A4-S152 |
| Stack position | Managed inference cloud (L2); FireRouter adds routing | Architectural judgement |  |
| Integration | Official Python SDK; OpenAI-compatible APIs; Microsoft Foundry partnership; Hugging Face Inference Providers partner | Verified fact | A4-S094, A4-S134, A4-S075 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type II; HIPAA (report of compliance listed; 'HIPAA-ready' on inference page); ISO 27001:2022, ISO 27701, ISO/IEC 42001:2023; GDPR (trust centre). BAA availability not seen; one Fireworks docs page still lists the three ISO certifications as "(in progress)" - request certificates from trust.fireworks.ai | Verified fact | A4-S133, V1-S067 |
| GDPR / residency | ZDR by default for open models (prompts/outputs only in volatile memory); exceptions: Response API stores conversations by default for 30 days (store=False avoids), training/fine-tuning/agent features. Enterprise data-residency setting rejects out-of-region requests, but documented options are None and US only (others via sales); EU regions (Frankfurt, Iceland) exist for deployments | Verified fact | A4-S134 |
| Security features | Customer-managed encryption keys (usage logged in customer cloud audit log); enterprise-enforceable ZDR policy; service accounts | Verified fact | A4-S152, A4-S134 |
| Access controls | Custom SSO via OIDC or SAML 2.0 (enterprise); RBAC; Audit Logs page and CLI | Verified fact | A4-S152 |
| Enterprise support | Enterprise reserved tier (multi-region deployments, custom optimisations, BYOC) | Verified fact | A4-S152 |
| Pricing | On-demand GPUs: H100/H200 US$8.00/h, B200 US$13.00/h, B300 US$15.00/h, billed per GPU-second (page ~167 days old; a secondary review cites US$7.00/h). Serverless per 1M tokens: <4B US$0.10, 4-16B US$0.20, >16B US$0.90; Kimi K3 US$3 in/US$15 out; batch 50% of serverless | Verified fact | A4-S135 |
| Infrastructure cost | Dedicated deployments scale to zero; billed per GPU-second | Verified fact | A4-S135 |
| Ecosystem | Microsoft Foundry; Hugging Face Inference Providers; Anthropic as a ZDR sub-processor for select services | Verified fact | A4-S134, A4-S075 |
| Adoption signals | Series D US$1.505B at US$17.5B (July 2026); >US$1B annualised revenue; CNBC: about half of revenue from Cursor as of 2025 | Verified fact | A4-S141 |
| Maturity | SDK since October 2022; Series D-stage company | Verified fact | A4-S094, A4-S141 |
| Deployment | saas: Yes (serverless); managed_cloud: Yes (on-demand and reserved dedicated deployments); vpc_byoc: Yes (hybrid BYOC: Fireworks inference engine in customer VPC; enterprise reserved tier); private_cloud: Yes (reserved capacity); self_hosted: Yes (partial: BYOC in customer cloud account); on_prem: Not publicly verified | | |

## SGLang (`L2-sglang`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** SGLang – efficient engine

*Rationale:* Strategic, conditional: as the qualified backup engine to vLLM, once CVE-2026-3059 is confirmed fixed in the deployed version (NVD and OSV reference a fix in 0.5.10; the GitHub advisory lists none), with internal ports isolated; not the default engine. Upgraded from Tactical by the reader at Checkpoint 4 (CP4-4); scores unchanged (FS 3.65), with security 2 carried as the tier condition [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading depth: RadixAttention, PD disaggregation, speculative decoding, quantisation [VF: A4-S010] |
| Enterprise readiness | 3 | Rule 2: inherits host controls; no verified commercial support, so the 4 cap applies; scored 3 [AJ] |
| Security and compliance | 2 | Rule 2 hygiene: critical unauthenticated RCE (fix evidenced only by NVD/OSV references to v0.5.10; GitHub advisory lists none), disclosure-response concerns and a reported bypass of an earlier fix [VF: B-L2-S009, B-REVC-S002]; kept at 2 at Checkpoint 4 (CP4-4 changed the tier only; a confirmed fix is the tier condition) |
| Deployment flexibility | 5 | Self-host, VPC, on-prem; managed via Hugging Face Endpoints [VF: A4-S065, A4-S081] |
| Ecosystem | 4 | OpenAI-compatible; Dynamo backend; RL frameworks [VF: A4-S010, A4-S090, A4-S065] |
| Reliability and maturity | 3 | 0.x since January 2024; new commercial steward in May 2026 [VF: A4-S010, A4-S147] |
| Cost / TCO | 4 | Free; GPU and operations cost [AJ] |
| Lock-in / portability | 4 | Apache-2.0, but governance is a non-profit plus VC-backed steward rather than a neutral foundation [VF: A4-S128, A4-S147] |
| **Total (generic / FS)** | **3.80 / 3.65** | |

*Evidence rules applied:* enterprise_readiness capped at 4 (rule 2, no verified commercial support); not binding at 3

**Capabilities.** Apache-2.0 serving framework (0.5.21, 1 October 2026) hosted by the LMSYS non-profit, with RadixAttention prefix caching, PD disaggregation, speculative decoding, FP4/FP8 quantisation, TPU and multi-vendor hardware support and day-0 support for new open models; RadixArk (US$100M seed, May 2026) is its commercial steward [VF: A4-S010, A4-S065, A4-S147, V1-S063].

**Strengths**

- Prefix-cache-heavy and agentic workloads (RadixAttention) [VF: A4-S010] [AJ]
- Fast day-0 model support [VF: A4-S065]
- Apache-2.0, OpenAI-compatible [VF: A4-S128, A4-S010]

**Limitations and risks**

- CVE-2026-3059 (critical, unauthenticated RCE via ZMQ broker, <=0.5.9): the GitHub advisory lists no patched version, while NVD references a fix in v0.5.10 and OSV a fixed commit; an earlier fix (CVE-2025-10164) has an unanswered bypass report [VF: B-L2-S009, B-REVC-S002]
- Pre-1.0; governance with a non-profit plus a VC-backed steward, no formal transfer found [VF: A4-S010, A4-S147]
- No verified commercial support offer [NPV]

**Choose when**

- Second engine where prefix reuse or a model's day-0 support matters [AJ]
- TPU serving [VF: A4-S010]

**Avoid when**

- The engine port could be reachable beyond a locked-down serving namespace [AJ]
- You need a vendor-supported distribution today [AJ]

**Nearest competitors:** L2-vllm, TensorRT-LLM, L2-nvidia-dynamo

**Regulated-FS note.** Qualify as the alternative engine in the exit plan; isolate internal ports and confirm CVE-2026-3059 status for the deployed version before use [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | SGLang open-source project hosted by LMSYS (non-profit); commercial steward RadixArk (founded by SGLang creators Ying Sheng and Banghua Zhu; US$100M seed, May 2026) | Verified fact | A4-S065, A4-S147 |
| Category | Open-source inference/serving framework for LLMs, VLMs and diffusion models; RL rollout backend | Verified fact | A4-S065 |
| Version / lineup | sglang 0.5.21 (1 October 2026); 21 releases in 2026 | Verified fact | A4-S010 |
| Licence | Open source, Apache-2.0 | Verified fact | A4-S010, A4-S128 |
| Status events | 5 May 2026: RadixArk launches with US$100M seed (Accel lead, Spark co-lead; NVIDIA, AMD participate) at US$400M post-money to steward SGLang and build a commercial platform | Verified fact | A4-S147, V1-S063 |
| Strategic direction | Optimised for agentic workloads, RL rollouts and large-scale serving: RadixAttention prefix caching, PD disaggregation, speculative decoding (DFlash, Spec V2, June 2026), FP4/FP8 quantisation; TPU support with Google and RadixArk (July 2026); day-0 support for new open models (e.g. DeepSeek-V4, Kimi K3) | Verified fact | A4-S010, A4-S065 |
| What it does | High-performance serving framework delivering low-latency, high-throughput inference from a single GPU to large clusters, OpenAI-API compatible, with broad model and hardware support (NVIDIA, AMD, Intel Xeon, Google TPU, Ascend). | Verified fact | A4-S010 |
| Stack position | Serving engine (L2); natively supported by Hugging Face Inference Endpoints and as a Dynamo backend | Verified fact | A4-S081, A4-S090 |
| Integration | OpenAI-compatible API; Python runtime; Docker | Verified fact | A4-S010, A4-S065 |
| Dependencies | Python >=3.10; accelerators; Docker image lmsysorg/sglang | Verified fact | A4-S010, A4-S065 |
| Certifications | Not applicable (open-source software) | Architectural judgement |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (Apache-2.0) | Verified fact | A4-S010 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | RL frameworks Miles (RadixArk), slime, AReaL, Tunix, verl; Dynamo; Hugging Face Endpoints | Verified fact | A4-S065, A4-S090, A4-S081 |
| Adoption signals | Project states it powers over 400,000 GPUs worldwide | Verified fact | A4-S010 |
| Maturity | First release January 2024; still 0.x; frequent releases | Verified fact | A4-S010 |
| Deployment | saas: No; managed_cloud: Yes (via third parties, e.g. Hugging Face Inference Endpoints); vpc_byoc: Yes; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## Hugging Face: Hub (models/datasets/Spaces/buckets/Jobs), Inference Providers (routed serverless inference), Inference Endpoints (managed dedicated deployments); Text Generation Inference (TGI) in maintenance mode (`L2-hugging-face`)

**Tier:** Strategic · **Flags:** Duplicated, Deprecated · **Original graphic label:** Hugging Face – models & APIs

*Rationale:* Strategic, conditional: as the governed open-weight supply source (Enterprise plan); Endpoints Tactical; Inference Providers not for client data

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Hub, router and dedicated serving with engine choice [VF: A4-S075, A4-S081] |
| Enterprise readiness | 4 | SSO (SAML/OIDC), SCIM, RBAC and audit logs on Team/Enterprise (rule 7) [VF: A4-S080, A4-S079] |
| Security and compliance | 3 | SOC 2 Type 2 covering Hub and Endpoints; no ISO 27001 found [VF: A4-S074, A4-S082] |
| Deployment flexibility | 3 | SaaS plus managed endpoints on three clouds with PrivateLink; not BYOC [VF: A4-S083, A4-S082] |
| Ecosystem | 5 | De-facto distribution standard; OpenAI-compatible router; many partners [VF: A4-S075] |
| Reliability and maturity | 3 | Hub mature since 2020, but TGI archived and Endpoints instance deprecations [VF: A4-S014, V1-S054, A4-S083] |
| Cost / TCO | 4 | Pass-through pricing; per-minute instance billing [VF: A4-S076, A4-S083] |
| Lock-in / portability | 4 | Models portable, open engines, OpenAI-compatible routing [VF: A4-S076, A4-S075] |
| **Total (generic / FS)** | **3.70 / 3.60** | |

**Capabilities.** Four products under one tile: the Hub (model and dataset distribution with SSO, SCIM, RBAC, audit logs and EU storage on Team/Enterprise), Inference Providers (OpenAI-compatible router to partner clouds with pass-through pricing), Inference Endpoints (managed dedicated serving on AWS, Azure or GCP with vLLM, SGLang, TGI, llama.cpp or TEI, SOC 2 Type 2, AWS PrivateLink) and TGI (maintenance mode; repository archived 21 March 2026) [VF: A4-S074, A4-S075, A4-S080, A4-S081, A4-S082, V1-S054].

**Strengths**

- The de-facto open-weight distribution point, with enterprise identity controls [VF: A4-S075, A4-S080] [AJ]
- Endpoints let you choose the engine and the cloud region [VF: A4-S081, A4-S083]
- No markup on routed provider calls [VF: A4-S076]

**Limitations and risks**

- TGI archived; Endpoints customers on TGI must migrate [VF: V1-S054]
- Inference Providers inherits each partner's security and retention [VF: A4-S077]
- BAA not explicitly tied to Inference Endpoints; no ISO 27001 found [VF: V1-S097]

**Choose when**

- You need a governed source of open weights and a managed dedicated endpoint in a chosen cloud region [AJ]

**Avoid when**

- Routing client data through Inference Providers to partners you have not assessed [AJ]

**Nearest competitors:** L2-together-ai, L2-fireworks-ai, Amazon SageMaker / Azure ML model catalogues

**Regulated-FS note.** Use the Hub (Enterprise, EU storage) as the governed model supply with scanning and an internal mirror; use Endpoints only in an approved region with PrivateLink [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Hugging Face | Verified fact | A4-S074 |
| Category | Model hub plus inference router and managed dedicated inference service | Verified fact | A4-S075, A4-S081 |
| Version / lineup | huggingface_hub client 2.1.1 (1 October 2026); Inference Endpoints natively supports vLLM, TGI, SGLang, llama.cpp and TEI engines | Verified fact | A4-S014, A4-S081 |
| Licence | Hub client and TGI Apache-2.0; Hub, Inference Providers and Inference Endpoints are proprietary hosted services | Verified fact | A4-S014, A4-S072, A4-S081 |
| Status events | TGI in maintenance mode 'as of 12/11/2025' (only minor bug fixes, docs and lightweight maintenance); Endpoints: AWS H100 instances marked 'Deprecated from December 2025'; 21 March 2026: TGI GitHub repository archived (read-only); latest release v3.3.7; Hugging Face recommends vLLM or SGLang | Verified fact | A4-S073, A4-S072, A4-S083, V1-S054, V1-S055 |
| Strategic direction | TGI moved to maintenance mode; Hugging Face recommends vLLM and SGLang (and llama.cpp/MLX locally). Inference Providers routes to partner clouds (e.g. Cerebras, Groq, Together, Fireworks, Baseten, Nscale, OVHcloud, Scaleway, Z.ai) with pass-through pricing | Verified fact | A4-S072, A4-S073, A4-S075, A4-S076 |
| What it does | Hub hosts and versions models/datasets with private repos, tokens, resource groups and malware/pickle/secrets scanning. Inference Providers gives one token and API across many third-party providers (OpenAI-compatible, provider selectable by suffix). Inference Endpoints deploys a chosen Hub model on a chosen engine to managed AWS/Azure/GCP instances billed per minute. | Verified fact | A4-S074, A4-S075, A4-S081, A4-S083 |
| Stack position | Spans model distribution (L1 adjacency), routing/aggregation (gateway-like, L2/C1) and managed serving (L2). The single tile conflates three products | Verified fact | A4-S075, A4-S081 |
| Integration | huggingface_hub (Python) and JS clients, hf CLI; OpenAI-compatible router; Endpoints REST | Verified fact | A4-S014, A4-S075 |
| Dependencies | Endpoints run on AWS, Azure or GCP instances; Inference Providers depend on partner providers' own security and retention | Verified fact | A4-S083, A4-S077 |
| Certifications | SOC 2 Type 2 (Hub and Inference Endpoints); GDPR compliant; BAA and GDPR DPA via Enterprise plan | Verified fact | A4-S074, A4-S082, V1-S097 |
| GDPR / residency | Storage regions US and EU for Team/Enterprise orgs (APAC, GCC coming); Inference Providers does not store request/response bodies, logs kept up to 30 days; Endpoints do not store payloads, logs kept 30 days | Verified fact | A4-S078, A4-S077, A4-S082 |
| Security features | TLS in transit; AWS PrivateLink for Endpoints; malware, pickle and secrets scanning; resource groups | Verified fact | A4-S082, A4-S074 |
| Access controls | SSO (SAML 2.0/OIDC) on Team & Enterprise, Managed SSO on Enterprise Plus, SCIM, RBAC, audit logs (Team & Enterprise) | Verified fact | A4-S080, A4-S079, A4-S082 |
| Enterprise support | Team, Enterprise and Enterprise Plus plans | Verified fact | A4-S080 |
| Pricing | Inference Providers: provider rates passed through with no HF markup; PRO and Team/Enterprise seats include US$2.00/month compute credits. Endpoints: hourly instance rates billed per minute, e.g. AWS L4 x1 US$0.80/h, AWS H200 x1 US$5/h | Verified fact | A4-S076, A4-S083 |
| Infrastructure cost | Endpoint cost = instance-hours (GPU type and count) billed per minute | Verified fact | A4-S083 |
| Ecosystem | Partners: Baseten, Cerebras, Cohere, DeepInfra, Fal, Featherless, Fireworks, Groq, Novita, Nscale, OVHcloud, Public AI, Replicate, Scaleway, Together, WaveSpeed, Z.ai; engines vLLM, SGLang, llama.cpp, TEI | Verified fact | A4-S075, A4-S081 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Hub client since 2020; TGI superseded by vLLM/SGLang | Verified fact | A4-S014, A4-S073 |
| Deployment | saas: Yes (Hub, Inference Providers); managed_cloud: Yes (Inference Endpoints on AWS/Azure/GCP); vpc_byoc: No (AWS PrivateLink private connectivity offered; not BYOC); private_cloud: Not publicly verified; self_hosted: Yes for open-source engines (TGI) and client libraries only; on_prem: Not publicly verified | | |

## Together AI (`L2-together-ai`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Together AI – open-source cloud

*Rationale:* Capable open-model cloud; unsafe defaults (ZDR off) and partial RBAC keep it Tactical

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Serverless, dedicated, PTU, fine-tuning, GPU clusters [VF: A4-S131] |
| Enterprise readiness | 3 | SSO on Scale/Enterprise; partial RBAC; audit trails for GPU clusters only (rule 7) [VF: A4-S151] |
| Security and compliance | 3 | SOC 2 Type 2 and ISO 27001 vendor-stated without product scope: one below anchor (rule 8) [VF: A4-S129, V1-S079] |
| Deployment flexibility | 4 | SaaS, dedicated, VPC deployments incl. EU, reserved capacity; no self-host [VF: A4-S130, A4-S131] |
| Ecosystem | 3 | Hugging Face partner; NVIDIA partner [VF: A4-S075, A4-S132] |
| Reliability and maturity | 3 | GA services; PTU SLA but serverless none; RBAC still rolling out [VF: A4-S131, A4-S151] |
| Cost / TCO | 4 | Transparent per-token and per-hour pricing; one H100 price conflict [VF: A4-S131] |
| Lock-in / portability | 4 | Open-weight models and standard usage; contractual capacity [VF: A4-S131] |
| **Total (generic / FS)** | **3.50 / 3.50** | |

**Capabilities.** AI-native cloud: serverless and dedicated inference for open-weight models, Provisioned Throughput with SLA, fine-tuning and GPU clusters; SOC 2 Type 2 and ISO 27001:2022 (vendor-stated); ZDR available but off by default; EU dedicated endpoints only on Scale and Enterprise; US$800M Series C on 1 July 2026 [VF: A4-S131, A4-S129, A4-S130, V1-S079, V1-S057].

**Strengths**

- Broad open-model catalogue plus dedicated and reserved capacity [VF: A4-S131]
- EU and US cluster sites [VF: A4-S130]

**Limitations and risks**

- Default storage of prompts and responses, with possible product-improvement use, unless ZDR is enabled [VF: A4-S130]
- Serverless has no region selection [VF: A4-S130]
- Product-level RBAC still being rolled out [VF: A4-S151]
- HIPAA wording inconsistent; customer BAA not confirmed [VF: V1-S079]

**Choose when**

- Open-weight models on dedicated EU endpoints with ZDR on, under a Scale or Enterprise contract [AJ]

**Avoid when**

- Serverless use with client data, or any use with ZDR left at default [AJ]

**Nearest competitors:** L2-fireworks-ai, L2-hugging-face, Hyperscaler model catalogues (Bedrock, Foundry, Vertex)

**Regulated-FS note.** Contract ZDR on, EU dedicated endpoints and the PTU SLA; confirm certification scope from the trust centre [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Together Computer, Inc. (trading as Together AI); privately held | Verified fact | A4-S132 |
| Category | AI-native cloud: serverless and dedicated inference for open-weight models, fine-tuning, GPU clusters, provisioned throughput | Verified fact | A4-S131, A4-S093 |
| Version / lineup | Official SDK together 2.40.0 (7 October 2026); products: serverless inference, dedicated endpoints, Provisioned Throughput (PTU), fine-tuning, GPU clusters (on-demand, reserved, Instant Clusters), container deployments ('Jig', beta) | Verified fact | A4-S093, A4-S131 |
| Licence | Proprietary cloud service; official Python SDK Apache-2.0 | Verified fact | A4-S093 |
| Status events | February 2025: Series B US$305M at US$3.3B; 1 July 2026: Series C US$800M at US$8.3B post-money (Aramco Ventures lead) | Verified fact | A4-S132, V1-S057 |
| Strategic direction | Raised US$800M Series C (1 July 2026) to scale its 'neocloud'; reports annual bookings above US$1.15B; adding Provisioned Throughput with SLA and EU dedicated capacity | Verified fact | A4-S132, A4-S131, A4-S130 |
| What it does | Hosts open-weight models behind serverless per-token APIs and per-minute dedicated endpoints, offers reserved token capacity (PTU), fine-tuning, and on-demand or reserved NVIDIA GPU clusters (H100 to GB300). | Verified fact | A4-S131, A4-S093 |
| Stack position | Managed inference cloud plus GPU IaaS (L2 and below); routers such as OpenRouter and Hugging Face Inference Providers sit in front of it | Architectural judgement |  |
| Integration | Official Python SDK and CLI; Hugging Face Inference Providers partner | Verified fact | A4-S093, A4-S075 |
| Dependencies | Together-operated data centres (cluster sites listed in US and Europe: France, Netherlands, Sweden, Romania) | Verified fact | A4-S130 |
| Certifications | SOC 2 Type 2 and ISO 27001:2022 (vendor blog and product pages); HIPAA described inconsistently ('compliant', 'HIPAA-aligned', 'HIPAA-ready') with BAAs mentioned; report scope/dates not seen | Verified fact | A4-S129, V1-S079 |
| GDPR / residency | ZDR available at organisation level but OFF by default: by default prompts and responses are stored and may be used for product improvement unless ZDR is enabled; training on customer data is opt-in (off by default); metadata retained for billing. Serverless has no region selection; EU dedicated endpoints only on Scale and Enterprise plans | Verified fact | A4-S130 |
| Security features | Encryption in transit and at rest and audit logging cited for HIPAA programme; private networking/VPC deployments | Verified fact | A4-S129, A4-S130 |
| Access controls | SSO (SAML/OIDC; Okta, Entra, Google Workspace, JumpCloud) on Scale and Enterprise plans; org/project RBAC (admin/developer) but product-level RBAC for fine-tuning, endpoints and serverless 'still being rolled out'; per-user audit trails for GPU clusters | Verified fact | A4-S151 |
| Enterprise support | Scale and Enterprise plans; PTUs carry an uptime SLA, serverless does not | Verified fact | A4-S130, A4-S131 |
| Pricing | Serverless per 1M tokens (in/out), e.g. GPT-OSS 120B US$0.15/US$0.60, Llama 3.3 70B Turbo US$1.04/US$1.04, Kimi K3 US$3.00/US$15.00; dedicated H100 US$3.99/h in docs vs US$5.49/h on pricing page (conflict); GPU clusters on-demand H100 US$3.99, B200 US$8.19 per GPU-hour; PTU US$0.05 per PTU-minute | Verified fact | A4-S131 |
| Infrastructure cost | Dedicated endpoints bill per running replica-minute regardless of traffic; serverless cheaper for bursty load | Verified fact | A4-S131 |
| Ecosystem | Hugging Face Inference Providers partner; NVIDIA partner | Verified fact | A4-S075, A4-S132 |
| Adoption signals | US$800M Series C at US$8.3B (July 2026); annual bookings reported above US$1.15B | Verified fact | A4-S132, V1-S057 |
| Maturity | SDK first released April 2023; company funded through Series C | Verified fact | A4-S093, A4-S132 |
| Deployment | saas: Yes (serverless); managed_cloud: Yes (dedicated endpoints, GPU clusters); vpc_byoc: Yes (private networking and VPC-based deployments, incl. EU regions); private_cloud: Yes (dedicated / reserved capacity); self_hosted: No; on_prem: Not publicly verified | | |

## llm-d (`L2-llm-d`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* The neutral-governance option for the optimisation sub-layer, but pre-1.0 and only Technology Preview support

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Prefix-cache-aware routing, tiered KV cache, PD disaggregation, wide EP [VF: A4-S089] |
| Enterprise readiness | 3 | Rule 2: inherits Kubernetes controls; Red Hat offer is Technology Preview, so the 4 cap applies; 3 [VF: B-L2-S002] |
| Security and compliance | 2 | Rule 2 hygiene: security policy, CVE handling and signing not verified [NPV] |
| Deployment flexibility | 4 | Self-host, VPC, private cloud, on-prem on Kubernetes; no SaaS [VF: A4-S089] |
| Ecosystem | 4 | vLLM, SGLang, KServe, Gateway API Inference Extension; broad founding coalition [VF: A4-S089, A4-S062] |
| Reliability and maturity | 2 | CNCF sandbox, v0.7; Technology Preview support [VF: A4-S089, B-L2-S002] |
| Cost / TCO | 3 | Free; heavy Kubernetes and GPU operations [AJ] |
| Lock-in / portability | 5 | Apache-2.0 under CNCF neutral governance [VF: A4-S089] |
| **Total (generic / FS)** | **3.30 / 3.35** | |

*Evidence rules applied:* enterprise_readiness capped at 4 (rule 2, support is Technology Preview only); not binding at 3

**Capabilities.** Apache-2.0 Kubernetes-native distributed inference stack above vLLM and SGLang: prefix-cache- and load-aware routing, tiered KV-cache management, PD disaggregation, wide expert parallelism and SLO-aware autoscaling; CNCF sandbox project (March 2026) founded by Red Hat, Google Cloud, IBM Research, CoreWeave and NVIDIA; v0.7 in May 2026 [VF: A4-S089, A4-S062]. Red Hat supports it only as a Technology Preview [VF: B-L2-S002].

**Strengths**

- Neutral governance (CNCF) and multi-vendor founders [VF: A4-S089]
- Builds on the Kubernetes Gateway API Inference Extension rather than a private router [VF: A4-S062]

**Limitations and risks**

- Pre-1.0 (v0.7) and sandbox stage [VF: A4-S089]
- Vendor support is Technology Preview, not covered by production SLAs [VF: B-L2-S002]
- Needs Kubernetes and data-centre accelerators [VF: A4-S089, B-L2-S002]

**Choose when**

- Kubernetes is your platform standard and you are building a multi-model internal inference service [AJ]

**Avoid when**

- You need production-supported software now [VF: B-L2-S002] [AJ]
- Volumes do not justify multi-replica routing [AJ]

**Nearest competitors:** L2-nvidia-dynamo, L2-vllm, KServe

**Regulated-FS note.** Pilot in non-production with Red Hat or GKE; revisit at 1.0 and at Red Hat GA support [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | llm-d project (CNCF sandbox; founded by Red Hat, Google Cloud, IBM Research, CoreWeave and NVIDIA) | Verified fact | A4-S089, A4-S062 |
| Category | Kubernetes-native distributed inference serving stack above model servers | Verified fact | A4-S089 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Not publicly verified | Not publicly verified |  |
| Status events | Not publicly verified | Not publicly verified |  |
| Strategic direction | Launched 20 May 2025 (Google Cloud as founding contributor) building on vLLM and the Gateway API Inference Extension (GKE Inference Gateway) | Verified fact | A4-S062 |
| What it does | Intelligent prefix-cache- and load-aware routing, tiered KV-cache management, PD disaggregation and wide expert parallelism, SLO-aware autoscaling and batch APIs, on top of vLLM/SGLang. | Verified fact | A4-S089 |
| Stack position | Inference optimisation / routing sub-layer above serving engines (H1) | Verified fact | A4-S089 |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | vLLM, SGLang, Kubernetes, KServe; partners incl. AMD, Cisco, Hugging Face, Intel, Lambda, Mistral AI | Verified fact | A4-S089, A4-S062 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: No; managed_cloud: Not publicly verified; vpc_byoc: Yes; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## OpenRouter (`L2-openrouter`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** OpenRouter – multi-provider

*Rationale:* Useful router for evaluation; third-party SaaS with billing intermediation and a pending change of owner

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Routing, fallback, provider selection, budgets, allowlists, ZDR, regions [VF: A4-S111, A4-S113] |
| Enterprise readiness | 4 | SSO, SCIM, org roles on Enterprise; contractual SLA on Enterprise (rule 7 to 4) [VF: A4-S110, A4-S112, A4-S150] |
| Security and compliance | 3 | SOC 2 Type 2 (report on request); no BAA; no ISO 27001 found [VF: A4-S142] |
| Deployment flexibility | 2 | SaaS only, with EU/US processing regions on higher plans [VF: A4-S107, A4-S109] |
| Ecosystem | 4 | OpenAI-compatible; many providers [VF: A4-S109, A4-S112] |
| Reliability and maturity | 3 | Operating at scale but no published SLA figure; Stripe acquisition pending (rule 3 mention) [VF: A4-S150, V1-S059] |
| Cost / TCO | 3 | Provider prices passed through plus 5.5-8% platform fee [VF: V1-S062, A4-S144] |
| Lock-in / portability | 2 | OpenAI-compatible (3) but proprietary guardrails and billing; reduced by 1 for ownership change (rule 3) [VF: A4-S111, V1-S059] |
| **Total (generic / FS)** | **3.25 / 3.05** | |

**Capabilities.** Hosted multi-provider model router with budgets, model and provider allowlists, ZDR enforcement, EU/US in-region routing (Business and Enterprise), SSO and SCIM (Enterprise); SOC 2 Type 2, no HIPAA BAA; 5.5% fee on credit purchases; Stripe agreed to acquire it (announced 19 August 2026, pending as of 8 October 2026) [VF: A4-S111, A4-S109, A4-S110, A4-S142, A4-S144, V1-S062, V1-S059].

**Strengths**

- Fastest way to evaluate many models behind one OpenAI-compatible API [VF: A4-S113] [AJ]
- In-region routing fails rather than falling back out of region [VF: A4-S109, A4-S150]

**Limitations and risks**

- Third-party SaaS in the data path; Batch API, web search and fetch not region-resident [VF: A4-S150]
- Billing intermediation (5.5% Standard, 8% Business) [VF: V1-S062, A4-S144]
- Ownership change pending; deal value is press-reported only [VF: V1-S059]
- No numeric uptime target published [VF: A4-S150]

**Choose when**

- Model exploration and non-confidential workloads, behind the firm's gateway [AJ]

**Avoid when**

- Client or personal data without ZDR and in-region routing contractually enforced [AJ]
- As the firm's gateway of record (see C1) [AJ]

**Nearest competitors:** L2-hugging-face, C1-litellm, C1-portkey

**Regulated-FS note.** Treat as a model-access source behind C1, not as C1; reassess terms and data-processing roles when the Stripe acquisition closes [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | OpenRouter, Inc.; subject to a pending acquisition by Stripe (agreement announced 19 August 2026; not confirmed closed as of 8 October 2026) | Verified fact | A4-S143, V1-S059 |
| Category | Hosted multi-provider model router / aggregator with gateway-style governance (budgets, allowlists, ZDR, regional routing) | Verified fact | A4-S111, A4-S109 |
| Version / lineup | Official Python SDK openrouter 1.3.32 (7 October 2026; first release 13 November 2025) | Verified fact | A4-S096 |
| Licence | Proprietary SaaS; SDK Apache-2.0 | Verified fact | A4-S096 |
| Status events | 26 May 2026: US$113M Series B led by CapitalG (company press release); 19 August 2026: Stripe signed an agreement to acquire OpenRouter (announced by both companies); closing expected "in the coming weeks", subject to customary conditions; no completion notice found as of 8 October 2026; price undisclosed (press reports range from over US$7B to over US$8B); OpenRouter says name, product and roadmap are unchanged | Verified fact | V1-S061, V1-S059, V1-S060 |
| Strategic direction | Enterprise features: workspaces, workspace budgets, guardrails (budget limits, model/provider allowlists, ZDR, data regions, prompt-injection and sensitive-info guardrails), SSO and SCIM group mappings, EU/US in-region routing | Verified fact | A4-S112, A4-S111, A4-S109 |
| What it does | Single API to many models and providers with routing, fallbacks and provider selection; passes through provider pricing; lets organisations enforce ZDR, regions, budgets and model/provider allowlists per workspace, key or member. | Verified fact | A4-S113, A4-S108, A4-S111 |
| Stack position | Model access router (L2) with control-plane features overlapping C1 (AI gateway) but as a third-party SaaS in the data path | Verified fact | A4-S111 |
| Integration | OpenAI-compatible API, @openrouter/sdk and Python SDK; BYOK; Datadog/Braintrust broadcast | Verified fact | A4-S109, A4-S113, A4-S096 |
| Dependencies | Underlying model providers; their data policies (OpenRouter tracks per-endpoint retention/training policy) | Verified fact | A4-S108 |
| Certifications | SOC 2 Type 2 (trust centre; report on request); no HIPAA BAA offered | Verified fact | A4-S142 |
| GDPR / residency | Prompts/responses not stored unless the customer opts in; metadata stored. ZDR enforceable globally, per model group, guardrail or request. EU/US in-region routing on Business and Enterprise plans; fails rather than falling back out-of-region; Batch API, web search and web fetch not region-resident | Verified fact | A4-S107, A4-S108, A4-S109, A4-S150 |
| Security features | Guardrails for prompt injection, sensitive information and secret formats; ZDR does not cover plugins/tools such as web search | Verified fact | A4-S111, A4-S108 |
| Access controls | SSO (Okta, Entra ID, Google Workspace, custom SAML) on Enterprise plans; SCIM group mappings; org admin roles | Verified fact | A4-S110, A4-S112 |
| Enterprise support | Business plan (self-serve, no minimum) and Enterprise plan (contractual SLAs, support SLA, dedicated Slack, CSM, forward-deployed engineer); no numeric uptime target published; ~50-minute full outage in August 2025 noted by vendor | Verified fact | A4-S109, A4-S150 |
| Pricing | Provider prices passed through without markup; platform fee on credit purchases: Standard 5.5% (US$0.80 minimum), Business 8%, Enterprise custom; BYOK 5% of model cost after plan allowance | Verified fact | A4-S144, A4-S113, V1-S062 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Many providers; coding-agent launchers (ori) for Claude Code, Codex, OpenCode | Verified fact | A4-S112 |
| Adoption signals | Series B US$113M led by CapitalG (26 May 2026, company release), about US$1.3B post-money (New York Times, reported); Series A US$40M (June 2025); 25 trillion tokens per week (May 2026, company); Stripe acquisition agreement August 2026 (value reported, not disclosed) | Verified fact | A4-S143, V1-S061, V1-S060 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Yes; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## NVIDIA Dynamo (`L2-nvidia-dynamo`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Clear H1 evidence and real capability, but beta packaging and month-long support windows make it unsuitable as a critical dependency today

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Disaggregation, KV-aware routing, KV offload, SLA planner [VF: A4-S090] |
| Enterprise readiness | 3 | Rule 2: commercial support exists (NVAIE feature branch) [VF: B-L2-S003]; inherits host controls; 3 |
| Security and compliance | 2 | Rule 2 hygiene: security policy and CVE handling not verified [NPV]; fixes only in new releases [VF: B-L2-S003] |
| Deployment flexibility | 4 | Self-host on Kubernetes, VPC, on-prem; guides for EKS, GKE, AKS [VF: A4-S090] |
| Ecosystem | 3 | Three engine backends, GAIE plugin, LMCache [VF: A4-S090, A4-S091] |
| Reliability and maturity | 2 | Beta classifier; 1.0 claim conflicts; one-month support windows [VF: A4-S098, A4-S090, B-L2-S003] |
| Cost / TCO | 3 | Free; heavy Kubernetes and GPU operations, subscription for support [VF: B-L2-S003] [AJ] |
| Lock-in / portability | 3 | Apache-2.0 but NVIDIA-led and NVIDIA-optimised [VF: A4-S090] |
| **Total (generic / FS)** | **3.10 / 3.00** | |

**Capabilities.** Apache-2.0 distributed inference orchestration layer above vLLM, SGLang and TensorRT-LLM: disaggregated serving, KV-aware routing, multi-tier KV block manager, SLA-based planner and autoscaling, a Kubernetes Gateway API Inference Extension plugin; ai-dynamo 1.5.1 (7 October 2026, PyPI classifier Beta) [VF: A4-S090, A4-S098]. Enterprise support is an NVIDIA AI Enterprise feature branch [VF: B-L2-S003].

**Strengths**

- Explicit optimisation sub-layer that does not replace the engine [VF: A4-S090]
- Engine-agnostic across three backends; integrates LMCache [VF: A4-S090, A4-S091]

**Limitations and risks**

- Beta classifier on PyPI while the README calls 1.0 production-ready (conflict) [VF: A4-S098, A4-S090]
- Support is a one-month feature branch with no backports and needs a subscription [VF: B-L2-S003]
- NVIDIA-led and NVIDIA-GPU-optimised [VF: A4-S090]

**Choose when**

- You run multi-node NVIDIA GPU serving at a scale where disaggregation pays [AJ]

**Avoid when**

- Single-node or modest volumes; vLLM alone is enough [AJ]
- You need long-term-support releases [VF: B-L2-S003] [AJ]

**Nearest competitors:** L2-llm-d, L2-vllm, L2-sglang

**Regulated-FS note.** Treat as an optimisation layer you can remove: keep the engine's OpenAI-compatible API as the contract to the gateway [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | NVIDIA | Verified fact | A4-S098 |
| Category | Distributed inference orchestration / optimisation layer above inference engines | Verified fact | A4-S090 |
| Version / lineup | ai-dynamo 1.5.1 (7 October 2026; PyPI classifier Beta); first release March 2025 | Verified fact | A4-S098 |
| Licence | Open source, Apache-2.0 | Verified fact | A4-S098, A4-S090 |
| Status events | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | 'The orchestration layer above inference engines — it doesn't replace SGLang, TensorRT-LLM, or vLLM': disaggregated serving, KV-aware routing, multi-tier KV caching (KVBM), SLA-based planner and autoscaling; 1.0 added zero-config deploy, agentic-inference hints and multimodal E/P/D. | Verified fact | A4-S090 |
| Stack position | Inference optimisation sub-layer between serving engines and gateways (H1) | Verified fact | A4-S090 |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free (Apache-2.0) | Verified fact | A4-S098 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Backends SGLang, TensorRT-LLM, vLLM; integrates LMCache (September 2025); LangChain and NeMo Agent Toolkit integrations | Verified fact | A4-S090, A4-S091 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: No; managed_cloud: Not publicly verified; vpc_byoc: Yes; private_cloud: Yes; self_hosted: Yes; on_prem: Yes | | |

## Ollama (local runtime) with Ollama Cloud (hosted cloud models) (`L2-ollama`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Ollama – run locally

*Rationale:* Useful developer runtime; Ollama Cloud is an unverified third-party processor

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers local serving competently; not a multi-tenant production engine [VF: A4-S084] [AJ] |
| Enterprise readiness | 2 | No SSO, RBAC or audit verified for Cloud; NPV cap [NPV] |
| Security and compliance | 2 | Cloud certifications NPV (cap); local runtime has no documented authentication [VF: B-L2-S007] [NPV] |
| Deployment flexibility | 4 | Local, on-prem and SaaS; no VPC [VF: A4-S084, A4-S085] |
| Ecosystem | 4 | Large community integrations; OpenAI/Anthropic-compatible APIs [VF: A4-S084] |
| Reliability and maturity | 2 | Server version and maturity not verified; cloud pricing changed 31 August 2026 [VF: V1-S066] [NPV] |
| Cost / TCO | 4 | Runtime free; Cloud plans published [VF: V1-S066] |
| Lock-in / portability | 4 | MIT runtime and portable models; Cloud proprietary [VF: A4-S086] |
| **Total (generic / FS)** | **3.00 / 2.95** | |

*Evidence rules applied:* enterprise_readiness capped at 2: SSO/RBAC/audit NPV; security_compliance capped at 2: Ollama Cloud certifications NPV

**Capabilities.** MIT-licensed local LLM runtime and model packager, plus Ollama Cloud, a hosted service for larger models with OpenAI- and Anthropic-compatible APIs; cloud features can be disabled; usage-based cloud plans from 31 August 2026 [VF: A4-S084, A4-S085, A4-S086, V1-S066]. Binds 127.0.0.1:11434 by default [VF: B-L2-S007].

**Strengths**

- Simplest local runtime for laptops and disconnected prototyping [AJ]
- MIT runtime, portable models [VF: A4-S086]
- Cloud can be switched off (OLLAMA_NO_CLOUD) [VF: A4-S085]

**Limitations and risks**

- No longer local-only: cloud models change the data-flow assumption [VF: A4-S084]
- Ollama Cloud certifications, SSO and audit not publicly verified [NPV]
- Built-in API authentication not documented; exposure relies on a proxy [VF: B-L2-S007] [AJ]

**Choose when**

- Developer workstations and offline evaluation with cloud disabled [AJ]

**Avoid when**

- Any shared or production serving [AJ]
- Client data on Ollama Cloud [AJ]

**Nearest competitors:** L2-lm-studio, llama.cpp, L2-vllm

**Regulated-FS note.** Allow on managed desktops only with OLLAMA_NO_CLOUD enforced and localhost binding; never as a production endpoint [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Ollama | Verified fact | A4-S086 |
| Category | Local LLM runtime and model packager, plus an optional hosted cloud-model service | Verified fact | A4-S084 |
| Version / lineup | Official Python client ollama 0.6.3 (29 September 2026); server/app version not retrieved | Verified fact | A4-S015 |
| Licence | Open source, MIT (runtime); Ollama Cloud is a hosted service with plans | Verified fact | A4-S086, A4-S084 |
| Status events | Cloud models introduced (e.g. *-cloud tags; gemma4:cloud); cloud features can be disabled (OLLAMA_NO_CLOUD=1) | Verified fact | A4-S015, A4-S085 |
| Strategic direction | Cloud models run in Ollama's cloud from apps, CLI or API with an API key; launchers for coding agents (Claude Code, Codex, OpenCode); OpenAI- and Anthropic-compatible APIs | Verified fact | A4-S084 |
| What it does | Runs open-weight models locally (no prompt visibility to Ollama when local) and optionally offloads larger models to Ollama's cloud; embeddings; OpenAI/Anthropic-compatible endpoints. | Verified fact | A4-S085, A4-S084, A4-S015 |
| Stack position | Developer/edge local runtime (L2); not a multi-tenant production serving engine. Ollama Cloud adds a hosted inference option | Verified fact | A4-S084 |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Local: Ollama does not see prompts. Cloud: prompts/responses processed to serve requests but not stored or logged and never used for training; basic account info and usage metadata collected | Verified fact | A4-S085, A4-S084 |
| Security features | Cloud features can be disabled for local-only mode (disable_ollama_cloud / OLLAMA_NO_CLOUD) | Verified fact | A4-S085 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Local runtime free (MIT). Ollama Cloud usage-based plans from 31 August 2026: Free (small monthly usage on starter models, pay-as-you-go credits), Pro US$20/month (US$60 usage included), Max US$100/month (US$300 included), Team US$500/month (US$1,000 shared usage, unlimited users); per-token rates by model; no hourly or weekly caps; off-peak discounts | Verified fact | A4-S084, V1-S066 |
| Infrastructure cost | Local cost is the user's own hardware (GPU/Apple silicon RAM) | Architectural judgement |  |
| Ecosystem | Large community integration list; Google Cloud Run tutorial; Claude Code/Codex/OpenCode launchers | Verified fact | A4-S084 |
| Adoption signals | US$65M funding round reported July 2026 (SiliconANGLE, 9 July 2026) | Reported | V1-S071 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Ollama Cloud); managed_cloud: Yes (Ollama Cloud); vpc_byoc: No; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes | | |

## Cerebras Systems (Cerebras Inference / Cerebras Cloud; CS-3 systems) (`L2-cerebras`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Cerebras – ultra-scale cloud

*Rationale:* Distinctive speed but thin enterprise controls and no EU processing yet

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Fast inference on a smaller catalogue; on-prem systems [VF: A4-S095, A4-S139] |
| Enterprise readiness | 3 | Console roles verified (rule 7 lifts the cap to 3); no SSO or audit documented [VF: A4-S153] |
| Security and compliance | 2 | SOC 2 Type 2 listed in the trust centre without product scope (rule 8) [VF: A4-S138, V1-S095] |
| Deployment flexibility | 3 | SaaS, dedicated, on-prem systems; no EU region yet [VF: A4-S139, A4-S095, A4-S140] |
| Ecosystem | 3 | OpenAI-compatible; AWS Marketplace; Hugging Face partner [VF: A4-S139, A4-S075] |
| Reliability and maturity | 3 | Public company; inference cloud since 2024; customer concentration [VF: A4-S137, A4-S154] |
| Cost / TCO | 3 | Transparent per-token pricing; enterprise flat pricing [VF: A4-S139] |
| Lock-in / portability | 3 | OpenAI-compatible API, proprietary hardware [VF: A4-S139, A4-S095] |
| **Total (generic / FS)** | **2.85 / 2.80** | |

**Capabilities.** Chip and system vendor (WSE-3, CS-3) that also runs an OpenAI-compatible inference cloud and sells on-premise systems; IPO priced 13 May 2026 (Nasdaq: CBRS); 750MW OpenAI agreement; SOC 2 Type 2, GDPR and CCPA listed, HIPAA not; EU capacity targeted for end-2026 [VF: A4-S095, A4-S137, A4-S154, A4-S138, A4-S140, V1-S095].

**Strengths**

- Very low-latency inference as a design point [VF: A4-S095] [AJ]
- On-premise CS-3 option [VF: A4-S095]

**Limitations and risks**

- No SSO documented; console roles only [VF: A4-S153]
- Data may be processed outside the US unless otherwise agreed; no EU capacity yet [VF: A4-S153, A4-S140]
- ZDR evidence is privacy-policy and blog level [VF: A4-S153, A4-S138]
- Customer concentration in the OpenAI agreement [VF: A4-S154]

**Choose when**

- Latency-critical, non-confidential workloads on supported open models [AJ]

**Avoid when**

- Client data until EU capacity and contractual ZDR exist [AJ]

**Nearest competitors:** L2-together-ai, L2-fireworks-ai, Groq

**Regulated-FS note.** Re-assess when EU capacity is live and SSO and contractual ZDR are documented [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Cerebras Systems Inc., listed on Nasdaq (CBRS) since 14 May 2026 | Verified fact | A4-S137 |
| Category | AI chip and system vendor (WSE-3, CS-3) that also operates an inference cloud and sells on-premise systems | Verified fact | A4-S095, A4-S154 |
| Version / lineup | cerebras-cloud-sdk 1.91.0 (16 July 2026); hardware WSE-3 / CS-3; Inference tiers: free, pay-per-token (Exploration), Enterprise; Cerebras Code subscriptions | Verified fact | A4-S095, A4-S139 |
| Licence | Proprietary hardware and cloud service; SDK Apache-2.0 | Verified fact | A4-S095 |
| Status events | December 2025: OpenAI master relationship agreement (750MW); 13 May 2026: IPO priced at US$185/share (30M Class A shares, ~US$5.55B); Nasdaq: CBRS from 14 May 2026; 8 July 2026: European expansion announced | Verified fact | A4-S154, A4-S137, A4-S140, V1-S053 |
| Strategic direction | Large inference supply agreement with OpenAI (750MW, Dec 2025; option for further 1.25GW by 2030); European expansion: first EU capacity by end-2026 (France, Nordics), 200MW by end-2027, 165MW Mikkeli (Finland) site | Verified fact | A4-S154, A4-S140 |
| What it does | Provides high-speed inference through an OpenAI-compatible REST API on CS-3 systems in Cerebras data centres, and sells CS-3 systems for on-premise deployment. | Verified fact | A4-S095, A4-S139 |
| Stack position | Both hardware vendor (below L2) and inference provider (L2). The graphic's 'ultra-scale cloud' omits the hardware business | Verified fact | A4-S095 |
| Integration | Official SDK; OpenAI-compatible API; AWS Marketplace billing; Hugging Face Inference Providers partner | Verified fact | A4-S095, A4-S139, A4-S075 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type 2, GDPR, CCPA listed in trust centre; HIPAA not listed | Verified fact | A4-S138, V1-S095 |
| GDPR / residency | Privacy policy: inputs and outputs of inference services not retained; logs deleted when no longer needed; data may be processed outside the US unless otherwise agreed. Blog claims (Jan 2025): inference runs in US data centres with zero data retention. EU capacity announced but not yet online (target end-2026) | Verified fact | A4-S153, A4-S138, A4-S140 |
| Security features | Encryption at rest and in transit (trust centre sections) | Verified fact | A4-S138 |
| Access controls | Console roles: Organization Admin, Project Admin, Project Member; projects group keys and rate limits; API-key auth; no SSO documentation found | Verified fact | A4-S153 |
| Enterprise support | Enterprise tier: custom SLAs, dedicated support, fine-tuned models, 3/6/12-month contracts | Verified fact | A4-S139 |
| Pricing | Pay-per-token per 1M tokens (in/out): Llama 3.1 8B US$0.10/US$0.10, Llama 3.3 70B US$0.85/US$1.20, Qwen 3 32B US$0.40/US$0.80; free tier limited to 8,192-token context; Enterprise flat monthly pricing by tokens-per-minute; Cerebras Code Pro US$50/month, Max US$200/month | Verified fact | A4-S139 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | IPO raised ~US$5.55B (May 2026); OpenAI 750MW commitment; 600MW of data-centre capacity under contract (Q2 2026 results) | Verified fact | A4-S137, A4-S154 |
| Maturity | Public company since May 2026; inference cloud since 2024 | Verified fact | A4-S137, A4-S139 |
| Deployment | saas: Yes; managed_cloud: Yes (Enterprise dedicated capacity); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: Yes (on-premise CS-3 systems) | | |

## LM Studio (desktop app) with lms CLI and Python/JS SDKs (`L2-lm-studio`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** LM Studio – desktop app

*Rationale:* Desktop-only tool; not part of the serving architecture

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 2 | Desktop runtime only; missing production-serving functions [VF: A4-S087] [AJ] |
| Enterprise readiness | 2 | SSO on Enterprise verified at low confidence (rule 7 allows up to 3); no audit or support evidence, so 2 [VF: A4-S145] |
| Security and compliance | 2 | Desktop software, proprietary; security features NPV [NPV] |
| Deployment flexibility | 2 | Desktop on-prem only; no server, VPC or SaaS [VF: A4-S087] |
| Ecosystem | 2 | Integrations largely NPV beyond CLI and SDKs [VF: A4-S087, A4-S016] |
| Reliability and maturity | 2 | Maturity NPV; SDK last release August 2025 [VF: A4-S016] |
| Cost / TCO | 4 | Free for internal business use [VF: A4-S145] |
| Lock-in / portability | 3 | Proprietary app, but models and the OpenAI-style local API are portable [AJ] |
| **Total (generic / FS)** | **2.25 / 2.25** | |

*Evidence rules applied:* security_compliance capped at 2: security features and certifications NPV

**Capabilities.** Proprietary desktop app for downloading and running local models with a local API server, MIT lms CLI and SDKs; free for personal and internal business use since about July 2025; may not be redistributed or offered as a service; a paid Enterprise plan adds SSO and model/MCP gating [VF: A4-S087, A4-S088, A4-S145, V1-S076].

**Strengths**

- Low-friction desktop evaluation of open models [AJ]
- Enterprise plan gating of models and MCP servers [VF: A4-S145]

**Limitations and risks**

- Proprietary app terms forbid offering it as a service [VF: A4-S145]
- Security features, support, versioning and maturity largely not publicly verified [NPV]
- Python SDK last released August 2025 [VF: A4-S016]

**Choose when**

- Managed developer desktops where a GUI and model gating help adoption [AJ]

**Avoid when**

- Any server or shared use [VF: A4-S145] [AJ]

**Nearest competitors:** L2-ollama, llama.cpp

**Regulated-FS note.** Permit only via the Enterprise plan on managed devices with an approved-model list; exclude client data [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LM Studio | Verified fact | A4-S088 |
| Category | Desktop application for running local models, with a local API server | Verified fact | A4-S087 |
| Version / lineup | lmstudio Python SDK 1.5.0 (22 August 2025); lms CLI ships with LM Studio 0.2.22 and newer; desktop app version not retrieved | Verified fact | A4-S016, A4-S087 |
| Licence | Desktop app proprietary (App Terms of Service): licensed for personal and/or internal business use, free at work without a separate commercial licence; prohibits modification, redistribution, sublicensing, offering as a service, reverse engineering. lms CLI MIT | Verified fact | A4-S145, A4-S088, V1-S076 |
| Status events | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Downloads and runs models locally; lms CLI starts/stops the local API server and lists models; SDKs allow programmatic access. | Verified fact | A4-S087, A4-S016 |
| Stack position | Developer-desktop runtime (L2); not a production serving tier | Architectural judgement |  |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not applicable (desktop software) | Architectural judgement |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | SSO and model/MCP gating on paid Enterprise plan | Verified fact | A4-S145 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free for personal and internal work use; paid Enterprise plan for SSO and model/MCP gating; LM Link free during preview | Verified fact | A4-S145 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: No; managed_cloud: No; vpc_byoc: No; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes | | |

# L1: Foundation models

## OpenAI GPT model family (GPT-6: Astra, Sol, Luna; GPT-6.1 Sol), plus GPT-5.6 Sol/Terra/Luna and open-weight gpt-oss (`L1-openai`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** OpenAI – GPT-6

*Rationale:* Broadest evidenced lineup, two hyperscaler routes plus first-party EU processing, product-scoped SOC 2 and ISO 27001; concentration is managed by pairing with a second vendor, not by avoiding OpenAI [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Covers every plan §5 L1 question on primary evidence: frontier, mid and small tiers, reasoning, image input, coding, a specialist cyber line and Apache-2.0 open weights (A5-S002, A5-S005, A5-S008). Benchmarks not used. |
| Enterprise readiness | 4 | First-party SSO/RBAC/audit and support terms are NPV; GPT-6 is consumed in-tenant through Bedrock and Foundry, so the hyperscaler presumption gives 4 (rule 6). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 4 | SOC 2 Type 2 and ISO 27001 within API scope, ZDR and first-party EU residency (A5-S006, A5-S007, V2-S062); not 5 because ISO 42001 scope does not name the API and CMK is not verified (rule 8). |
| Deployment flexibility | 4 | First-party SaaS (US, EU, UK-storage endpoints), Bedrock, Foundry, and self-hosted/air-gapped gpt-oss; 4 not 5 because the frontier tiers cannot be self-hosted and gpt-oss dates from August 2025. |
| Ecosystem | 5 | The OpenAI API shape is the de facto interface: other vendors publish OpenAI-compatible endpoints (A5-S010, A5-S077, A5-S038); official SDKs; two hyperscalers. |
| Reliability and maturity | 4 | Years of production use and a published deprecation policy (B-L1-S001); fast tier churn (GPT-5.6 in July, GPT-6 in September 2026) and the Astra GA conflict keep it at 4. |
| Cost / TCO | 4 | Transparent per-tier pricing (Luna US$0.10/US$0.50, Sol US$2/US$10, Astra US$10/US$50 per 1M) with 50% batch discount (A5-S004); competitive, not uniquely efficient. |
| Lock-in / portability | 3 | Proprietary frontier API on a de facto standard interface, on two non-OpenAI clouds, with Apache-2.0 gpt-oss as a portability option. |
| **Total (generic / FS)** | **4.25 / 4.05** | |

**Capabilities.** Tiered proprietary family: GPT-6 Astra (gated flagship, introduced 3 September 2026), GPT-6 Sol and Luna (22 September 2026), GPT-6.1 Sol (29 September 2026), with GPT-5.6 Sol/Terra/Luna still offered; all GPT-6 tiers are reasoning models with text and image input; Daybreak cyber models in limited availability on Bedrock; open-weight gpt-oss-120b/20b under Apache 2.0 (August 2025) [VF: A5-S001, A5-S002, A5-S003, A5-S005, A5-S008, A5-S009, A5-S083].

**Strengths**

- Complete tier ladder (frontier, mid, small) plus Apache-2.0 open weights, so one vendor covers every portfolio tier except sovereign self-hosted frontier [VF: A5-S002, A5-S005] [AJ]
- Available on AWS Bedrock and Microsoft Foundry as well as the first-party API, including EU Data Zone deployments on Foundry [VF: A5-S008, A5-S009]
- First-party EU residency: eu.api.openai.com stores and processes in region (new projects, with Modified Abuse Monitoring or ZDR) [VF: A5-S006, V2-S079]
- SOC 2 Type 2 for the API Platform and ISO/IEC 27001, 27017, 27018, 27701 covering the API [VF: A5-S007, V2-S062]
- Published deprecation notice policy: at least 6 months for GA models, at least 3 months for specialised variants [VF: B-L1-S001]

**Limitations and risks**

- Frontier tiers are closed-weight and API-only; fine-tuning is not supported for Astra [VF: A5-S003]
- Astra is gated (rated 'Critical' for cybersecurity; enterprise admins must enable it), and OpenAI said 'not yet generally available' while AWS lists it GA on Bedrock [VF: A5-S002, A5-S003, A5-S008]
- UK endpoint stores data in the UK but does not process there [VF: A5-S006, V2-S079]
- Bedrock Astra is in-region only in us-east-1 and us-west-2 [VF: A5-S008]
- ISO/IEC 42001 scope wording does not name the API Platform; CMK and first-party SSO/SCIM/RBAC were not verified [VF: V2-S062] [NPV]
- Preview models may be retired on about 2 weeks' notice [VF: B-L1-S001]
- Not on Google Cloud except gpt-oss [VF: A5-S027]

**Choose when**

- You need a primary or fallback frontier vendor available in-tenant on Azure or AWS with a first-party EU residency option [AJ]
- You want one vendor relationship that also supplies a small classification tier (Luna) and a self-hostable open-weight model (gpt-oss) [AJ]

**Avoid when**

- Google Cloud is the only permitted cloud and you need GPT-6 tiers [AJ]
- You need UK in-country processing [AJ]
- You would use Promptfoo, now announced as part of OpenAI, as the only independent test of an OpenAI-based system [AJ]

**Nearest competitors:** L1-anthropic, L1-google-gemini, L1-mistral

**Regulated-FS note.** Consume via Microsoft Foundry EU Data Zone or the EU first-party endpoint with ZDR or Modified Abuse Monitoring; pin dated snapshots, track the deprecations page, and keep a second vendor qualified as the SS2/21 exit route [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | OpenAI | Verified fact | A5-S047, A5-S002 |
| Category | Frontier model vendor: proprietary API models (reasoning, multimodal input, coding) plus Apache-2.0 open-weight models | Verified fact | A5-S002, A5-S005 |
| Version / lineup | flagship: GPT-6 Astra, introduced 3 September 2026 per ChatGPT release notes (limited organisations first; "Path to Astra" post of 1 September explains a several-week hold for cyber safeguards); OpenAI forum post says API and Pro/Enterprise access on 4 September; Bedrock model card lists 8 September (AWS GA date). Gated: enterprise admins must enable; first OpenAI model rated "Critical" for cybersecurity. 1,050,000-token context, 128K output, knowledge cut-off 30 April 2026. [A5-S083, A5-S002, A5-S003, A5-S008]; mid: GPT-6 Sol (22 September 2026) and GPT-6.1 Sol (29 September 2026; now the def | Verified fact | A5-S001, A5-S002, A5-S003, A5-S004, A5-S005, A5-S008, A5-S009, A5-S083, V2-S008, V2-S024 |
| Licence | Proprietary, API-only for GPT-6 and GPT-5.6 (closed weights; fine-tuning not supported for Astra). Open weights for gpt-oss under Apache 2.0 plus gpt-oss usage policy. | Verified fact | A5-S003, A5-S005 |
| Status events | 9 July 2026: GPT-5.6 Sol/Terra/Luna GA; 30 July 2026: GPT-5.6 Luna -80% and Terra -20% price cuts; 3 September 2026: GPT-6 Astra introduced (limited organisations); API from 4 September; Bedrock GA 8 September; 22 September 2026: GPT-6 Sol and Luna; 29 September 2026: GPT-6.1 Sol; 7 October 2026: GPT-6 rolled out to ChatGPT Chat | Verified fact | A5-S001, A5-S002, A5-S083, V2-S024 |
| Strategic direction | Generation number plus capability-tier naming (Sol/Terra/Luna introduced with GPT-5.6, July 2026) so tiers can advance on separate cadences; staged, gated releases for cyber-capable models (Daybreak trusted-access programme); rapid price cuts (GPT-6 Sol/Luna 50% below GPT-5.6 promotional pricing); distribution through AWS Bedrock and Microsoft Foundry. | Verified fact | A5-S001, A5-S002, A5-S008, A5-S009 |
| What it does | General-purpose large language models served through the OpenAI API (Responses and Chat Completions), ChatGPT, Codex and partner clouds; tiers trade capability against cost and latency. | Verified fact | A5-S002, A5-S008 |
| Stack position | L1 foundation model. Placement in the graphic is correct; OpenAI also appears at L3 (Agents SDK) and L7 (embeddings). | Architectural judgement |  |
| Integration | REST API (Responses, Chat Completions, Batch), official SDKs (openai Python 3.26.0, Apache-2.0, 6 October 2026); also via Bedrock (bedrock-mantle and bedrock-runtime endpoints) and Microsoft Foundry deployments. | Verified fact | A5-S047, A5-S008, A5-S009 |
| Dependencies | Hosted service on OpenAI infrastructure (Astra trained on >100,000 GPUs at Stargate, Texas) or partner clouds (AWS Bedrock, Microsoft Foundry). gpt-oss runs on own GPUs (120b fits one H100) via vLLM, Ollama, llama.cpp. | Verified fact | A5-S003, A5-S005, A5-S008, A5-S009 |
| Certifications | SOC 2 Type 2 (API Platform; latest report 1 July 2025 to 30 June 2026); ISO/IEC 27001:2022, 27017, 27018, 27701 (Schellman; API, ChatGPT Enterprise, Edu; not ChatGPT Business); ISO/IEC 42001:2023 AI management system (scope wording covers consumer and business AI products and models; the API Platform is not named explicitly); SOC 3; CSA STAR Level 1 self-assessment. | Verified fact | A5-S007, V2-S062 |
| GDPR / residency | DPA available. API: no training on API data by default; inputs/outputs may be retained up to 30 days unless Zero Data Retention (approval required; some endpoints not ZDR-eligible). EU residency: eu.api.openai.com, storage and processing in region, new projects only, requires Modified Abuse Monitoring or ZDR. UK: gb.api.openai.com storage only, processing not in UK. Microsoft Foundry offers EU Data Zone deployments; Bedrock Astra in-region only in us-east-1/us-west-2 (Mantle). | Verified fact | A5-S006, A5-S009, A5-S008, V2-S079 |
| Security features | Private Safety Processing option (customer-controlled storage under ZDR) in phased rollout; other controls (CMK, private networking) not verified in this run. | Verified fact | A5-S006 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | gpt-6-astra: US$10 input / US$50 output per 1M tokens (<=272K input); US$20 / US$75 above 272K; batch 50% off; gpt-6.1-sol / gpt-6-sol: US$2 input / US$10 output per 1M; gpt-6-luna: US$0.10 input / US$0.50 output per 1M; gpt-5.6-sol (promotional to at least 21 November 2026): US$4 / US$20 per 1M; Microsoft Foundry GPT-6 Sol Global Standard: US$2 / US$10 per 1M (Data Zone slightly higher) | Verified fact | A5-S004, A5-S001, A5-S009, V2-S008, V2-S024 |
| Infrastructure cost | gpt-oss-120b (117B total, 5.1B active parameters) fits a single H100; gpt-oss-20b targets local use. | Verified fact | A5-S005 |
| Ecosystem | AWS Bedrock (GPT-6 Astra/Sol/Luna, GPT-5.6, gpt-oss), Microsoft Foundry (GPT-6 family, 28 Global regions, US/EU Data Zones), Google Cloud (gpt-oss-120b/20b only). | Verified fact | A5-S008, A5-S009, A5-S027 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GPT-6 Sol/Luna GA in API and partner clouds; GPT-6 Astra gated, not generally available per OpenAI release notes, though AWS lists it GA on Bedrock (conflict recorded). | Verified fact | A5-S002, A5-S008 |
| Deployment | saas: Yes; managed_cloud: Yes (AWS Bedrock; Microsoft Foundry); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes, gpt-oss only; on_prem: Yes, gpt-oss only | | |

## Mistral AI model family (Mistral Large 4 preview; Mistral Medium 3.5; Mistral Large 3; Mistral Small 4.0; Ministral 3; Magistral; Devstral 2; Codestral; Mistral OCR; Voxtral) (`L1-mistral`)

**Tier:** Strategic · **Flags:** Superseded · **Original graphic label:** Mistral – Medium 3.1

*Rationale:* The strongest combination of EU residency, open weights and multi-cloud availability in the layer; Strategic as the EU and open-weight leg of the portfolio, not as the sole frontier model [AJ]. 'Superseded' refers to the graphic's Medium 3.1 label.

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Broad lineup across general, reasoning, coding, OCR and speech, with open weights (A5-S074, A5-S038); frontier tier only in preview. |
| Enterprise readiness | 4 | First-party access controls NPV; hyperscaler routes give the presumption (rule 6). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 3 | SOC 2 Type II and ISO 27001/27701 plus EU residency (A5-S075) would anchor at 4; product scope not stated, so one point lower (rule 8). |
| Deployment flexibility | 5 | EU SaaS, three hyperscalers, Scaleway, self-host, on-premises and air-gap with open weights (A5-S074, A5-S038). |
| Ecosystem | 4 | Three hyperscalers and mainstream open-serving support (A5-S039). |
| Reliability and maturity | 3 | GA mid tier with a published retirement table (B-L1-S002); frontier preview days old; fast retirements (Medium 3.1 within about a year). |
| Cost / TCO | 4 | Medium 3.5 at US$1.50/US$7.50 per 1M (A5-S074) and free open weights; EU endpoint carries 10% surcharge (A5-S075). |
| Lock-in / portability | 4 | Open weights under Apache 2.0 or Modified MIT; revenue thresholds on Medium 3.5 (rule 4) keep it from 5. |
| **Total (generic / FS)** | **3.90 / 3.85** | |

**Capabilities.** Mistral AI family: Mistral Large 4 (public preview 6 October 2026, API-only, weights targeted for 27 October 2026, licence unpublished), Mistral Medium 3.5 (28 April 2026, 128B dense, 256K context, Modified MIT v26.04), Large 3 (Apache 2.0), Small 4.0, Ministral 3, Magistral reasoning, Devstral 2 and Codestral coding, Mistral OCR and Voxtral speech [VF: A5-S074, A5-S076, V2-S017, V2-S018] [R: A5-S038].

**Strengths**

- EU hosting by default, with an EU regional endpoint (api.eu.mistral.ai) committing inference location [VF: A5-S075]
- Open weights across tiers (Large 3 Apache 2.0; Medium 3.5 Modified MIT; Ministral 3 Apache 2.0) [VF: A5-S074]
- Offered on Google Cloud, Bedrock and Microsoft Foundry (different subsets) [R: A5-S027, A5-S038]
- Published deprecation and retirement table with replacements [VF: B-L1-S002]
- Signatory of the GPAI Code of Practice [VF: R-EU-GPAI-COP, A8-S015]

**Limitations and risks**

- Frontier tier is a days-old preview; Large 4 licence and list price unpublished; parameter counts differ between launch post and docs [VF: A5-S076, V2-S017]
- Medium 3.5's Modified MIT licence has revenue-based exceptions [VF: A5-S074, V2-S018]
- Certifications stated on the help centre without product scope; ZDR only for pay-as-you-go stateless calls at Mistral's discretion; default 30-day retention [VF: A5-S075]
- Mistral Medium 3.1, the graphic's label, retired on 31 August 2026 [VF: B-L1-S002]
- Resells Z.ai GLM models on its platform, so a Mistral contract does not by itself exclude Chinese-origin models [R: A5-S038]

**Choose when**

- You need an EU-domiciled vendor with an EU inference endpoint as primary or fallback [AJ]
- You want open weights from a non-Chinese vendor for a self-hosted sensitive-data tier [AJ]

**Avoid when**

- You need a GA frontier-class model today [AJ]
- Your licence policy cannot accept revenue-threshold licences for Medium 3.5 [AJ]

**Nearest competitors:** L1-openai, L1-google-gemma, L1-meta

**Regulated-FS note.** Use api.eu.mistral.ai or self-hosted weights; obtain the SOC 2 report and ISO certificate scope from the Trust Center; exclude resold third-party models via model allow-lists at the gateway [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Mistral AI (official mistralai SDK author "Mistral") | Verified fact | A5-S047 |
| Category | Model vendor with API and open-weight models (general, reasoning, coding, OCR, speech) | Reported | A5-S038 |
| Version / lineup | frontier_preview: Mistral Large 4, public preview 6 October 2026; ~1T total / 49-52B active MoE, multimodal, 1M context; open weights promised by end of October 2026 (27 October per VentureBeat); preview API-only in Mistral Studio. [A5-S076]; flagship_mid: Mistral Medium 3.5, 128B dense, 256K context, released 28 April 2026 (changelog lists 26 April), open weights under Modified MIT v26.04; API US$1.5 / US$7.5 per 1M. [A5-S074]; large_open: Mistral Large 3 (December 2025), 675B total / 41B active MoE, Apache 2.0. [A5-S074]; small: Mistral Small 4.0 (26.03); Ministral 3 3B/8B/14B (25.12). [A5-S | Verified fact | A5-S038, A5-S027, A5-S039, A5-S074, A5-S076, V2-S017, V2-S018 |
| Licence | Mixed: Large 3 and Ministral 3 Apache 2.0; Medium 3.5 Modified MIT (revenue-based exceptions); Large 4 licence not yet published; some models API-only. | Verified fact | A5-S074, A5-S076, V2-S018 |
| Status events | December 2025: Mistral Large 3, Ministral 3; March 2026: Mistral Small 4.0; April 2026: Mistral Medium 3.5 supersedes Medium 3.1 (dates inferred from model-card version codes); 6 October 2026: Mistral Large 4 public preview | Reported | A5-S038, A5-S076 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | General, reasoning, coding, OCR and speech models via Mistral's API (La Plateforme) and partner clouds, with some models released as open weights. | Reported | A5-S038 |
| Stack position | L1 foundation model; Mistral also appears at L3 (Agents) and L8 (Mistral OCR). | Architectural judgement |  |
| Integration | Mistral API; mistralai Python SDK 3.1.0 (6 October 2026). | Verified fact | A5-S047 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type II and ISO 27001/27701 (per Mistral help centre; reports via Trust Center on request). | Verified fact | A5-S075 |
| GDPR / residency | Data hosted in the EU by default; optional US endpoint; EU regional endpoint api.eu.mistral.ai (10% surcharge) commits inference location; some features may transfer data outside EU (listed on Trust Center). API data not used for training; default 30-day retention for abuse monitoring; ZDR only for pay-as-you-go stateless calls, at Mistral's discretion. | Verified fact | A5-S075 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Mistral Medium 3.5: US$1.50 input / US$7.50 output per 1M; Mistral Large 3: US$0.50 / US$1.50 per 1M (aggregator); Mistral Small 4.0: US$0.15 / US$0.60 per 1M (aggregator); Mistral Large 4 preview: 50% launch discount for 2 weeks; list price not verified | Verified fact | A5-S074, A5-S038, A5-S076 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Google Cloud, Amazon Bedrock, Microsoft Foundry, Scaleway (Medium 3.5 128B), OpenRouter; SGLang day-0 support for Large 3. | Reported | A5-S027, A5-S038, A5-S039 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Yes (Google Cloud: Medium 3, Small 3.1, Codestral 2, OCR; Bedrock: Large 3, Devstral 2, Ministral 3, Magistral Small, Pixtral Large incl. eu., Voxtral; Microsoft Foundry: Large 3, Medium 3.5, OCR 4); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open-weight models: Large 3, Medium 3.5, Ministral 3); on_prem: Yes (open-weight models) | | |

## Anthropic Claude model family (Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5; restricted Claude Mythos 5.1) (`L1-anthropic`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Claude – Opus 5.5

*Rationale:* Strategic, conditional: consumed only through a hyperscaler EU or UK region (Bedrock regional endpoint or Google Cloud EU), as one of two frontier and mid-tier vendors with a non-Anthropic fallback qualified on the same evaluation suite, not as the sole frontier model; independent alternatives are OpenAI GPT-6.1 Sol, Gemini 3.8 Flash and Mistral Medium 3.5. FS 3.80 with no criterion below 3. Tier and neutral scoring set by the reader at Checkpoint 4 (CP4-1); the author's pipeline had resolved three borderline scores against Anthropic. Security 5 and cost 4 are the neutral rubric values identified in CP4 review C (previously 4 and 3). The first-party residency gap and the June 2026 Fable 5 suspension remain factual weaknesses and are stated as conditions. Conflict of interest: the author is an Anthropic model [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Four GA tiers with 1M context, reasoning, image input and coding (A5-S010); no open-weight, audio or image-output models and no GA specialist line, so fewer plan §5 questions covered than OpenAI or Google; borderline 4/5 resolved against Anthropic (conflict rule). CP4 review C found 4 is also the neutral value on peers; unchanged at CP4. |
| Enterprise readiness | 4 | Workspaces, Admin API, Compliance API / Activity Feed and WIF verified (A5-S013, A5-S018) plus in-tenant hyperscaler routes (rule 6); not 5 because SSO/SCIM detail and SLA are NPV. Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 5 | Product-scoped SOC 2 Type II, ISO 27001 and ISO 42001 covering the API and Claude in Bedrock and Google Cloud, plus CMEK in the admin console (A5-S021, V2-S063, A5-S013), meet the rule-8 test for 5. Set to 5, the neutral rubric value, by the reader at Checkpoint 4 (CP4-1; previously held at 4 against Anthropic). Residency and ZDR are optional extras under the anchor, so the absence of a first-party EU/UK inference geography (V2-S075) and the top tier's conflicting ZDR position (A5-S023, A5-S016) are carried as tier conditions, not score deductions; the Azure-hosted Foundry deployment is still 'In-Process Q4 2026' for certification (V2-S063). |
| Deployment flexibility | 3 | First-party SaaS plus Bedrock, Google Cloud, Foundry and Claude Platform on AWS; no self-hosting or on-premises (A5-S010). |
| Ecosystem | 4 | Three hyperscalers and an OpenAI SDK compatibility endpoint (A5-S010); the API itself is not the de facto standard; borderline 4/5 resolved against Anthropic. CP4 review C found 4 is also the neutral value on peers; unchanged at CP4. |
| Reliability and maturity | 3 | Published retirement commitments (A5-S010) are positive, but top-tier access was suspended 12 June to 1 July 2026 (V2-S004), four models shipped in five weeks, and the D.C. Circuit upheld a federal supply-chain-risk designation (A5-S084). |
| Cost / TCO | 4 | Transparent; list prices equal OpenAI's at every tier (Fable 5.1 = Astra US$10/US$50; Sonnet 5.5 = GPT-6.1 Sol US$2/US$10; Haiku 5.5 = Luna US$0.10/US$0.50 per 1M) with a 50% batch discount (A5-S011, A5-S004), and OpenAI scores 4. The 10% regional premium does not hold peers at 3 (Mistral and Grok score 4), and the dearer recommended default (Opus 5.5, US$4/US$20) is a deployment choice, not a vendor price. Set to 4, the neutral rubric value, by the reader at Checkpoint 4 (CP4-1; previously 3). |
| Lock-in / portability | 3 | Proprietary API with no open weights, but on three clouds and with an OpenAI-compatible endpoint, so a gateway can switch it out. |
| **Total (generic / FS)** | **3.85 / 3.80** | |

**Capabilities.** Proprietary Claude family: Claude Fable 5.1 (top GA tier, 1 September 2026), Opus 5.5 (22 September 2026; Anthropic's recommended starting point), Sonnet 5.5 (28 September 2026) and Haiku 5.5 (7 October 2026); Mythos 5.1 is the same model as Fable 5.1 with looser safeguards for trusted-access programmes only; all four GA models have adaptive thinking, text and image input, text output, 1M-token context and 128K output; no open weights [VF: A5-S010, A5-S012, A5-S016, A5-S019, A5-S020, V2-S066]. Conflict of interest: the author is an Anthropic model.

**Strengths**

- Available on all three hyperscalers (Bedrock, Google Cloud, Microsoft Foundry) plus Claude Platform on AWS and the first-party API [VF: A5-S010]
- SOC 2 Type II, ISO 27001:2022 and ISO/IEC 42001:2023 with stated scope covering the API and Claude in Bedrock and Google Cloud [VF: A5-S021, V2-S063]
- Documented admin controls: Workspaces, Admin API, Workload Identity Federation, Compliance API / Activity Feed with 6-year retention, CMEK listed in the admin console [VF: A5-S013, A5-S018]
- Published retirement commitments ('not sooner than' September/October 2027) for current models [VF: A5-S010]

**Limitations and risks**

- No first-party EU or UK inference option: inference_geo is 'global' or 'us' only and workspace geo is 'us' only; EU processing requires Google Cloud EU or Bedrock regional endpoints at a 10% premium [VF: A5-S013, V2-S075, A5-S011, A5-S027]
- Claude Fable 5 access was suspended on 12 June 2026 and restored from 1 July 2026 [VF: V2-S004]
- Fable 5.1 is a 'Covered Model' requiring 30-day retention unless expressly authorised, which conflicts with the launch post on ZDR eligibility [VF: A5-S023, A5-S016]
- On 25 September 2026 the D.C. Circuit (No. 26-1049) upheld, 2-1, the US Department of Defense's FASCSA supply-chain-risk designation of Anthropic, with effect stayed pending a rehearing petition; a separate N.D. Cal. ruling of 27 August 2026 held the other (s.3252) designation unlawful [VF: A5-S084, V2-S068] [R: V2-S005]
- Bartz v. Anthropic US$1.5bn class settlement over pirated books received final approval on 20 July 2026 [VF: A5-S085] [R: V2-S007]
- No open weights; no audio or image output [VF: A5-S010]
- Claude in Microsoft Foundry hosted on Azure is listed as certification 'In-Process Q4 2026' [VF: V2-S063]
- Enterprise support tiers and SLA not publicly verified [NPV]

**Choose when**

- You need a second frontier vendor that is available in-tenant on whichever hyperscaler is primary, including Google Cloud where OpenAI's GPT-6 is not offered [AJ]
- Long-context (1M tokens on every tier) drafting or agentic coding is the main workload [AJ]

**Avoid when**

- EU or UK processing must be contracted with the model vendor itself rather than through a hyperscaler [AJ]
- The firm has US defence-contract exposure and its legal team has not assessed the supply-chain-risk designation [AJ]
- You need a self-hostable model from the same vendor [AJ]

**Nearest competitors:** L1-openai, L1-google-gemini, L1-mistral

**Regulated-FS note.** Consume only through a hyperscaler EU region (Bedrock regional endpoint or Google Cloud EU), with a non-Anthropic fallback qualified on the same evaluation suite; independent alternatives are OpenAI GPT-6.1 Sol and Gemini 3.8 Flash [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Anthropic, PBC (public benefit corporation; confidentially submitted draft S-1 for proposed IPO on 1 June 2026) | Verified fact | A5-S024 |
| Category | Frontier model vendor: proprietary API models (reasoning, vision input, coding/agentic) | Verified fact | A5-S010 |
| Version / lineup | flagship: Claude Fable 5.1, GA 1 September 2026, "for demanding reasoning and long-horizon agentic work"; Claude Mythos 5.1 is the same model with more permissive cyber/biology safeguards, available only via trusted-access programmes (limited US organisations). [A5-S016, A5-S022, A5-S010]; default_recommended: Claude Opus 5.5, 22 September 2026, first model of the Claude 5.5 family; Anthropic docs recommend it as the starting point for most workloads. [A5-S019, A5-S010]; mid: Claude Sonnet 5.5, 28 September 2026. [A5-S012, A5-S010]; small: Claude Haiku 5.5, 7 October 2026 (Haiku 4.5 still list | Verified fact | A5-S010, A5-S012, A5-S016, A5-S019, A5-S020, A5-S022, V2-S001, V2-S003, V2-S004, V2-S066 |
| Licence | Proprietary; API and partner-cloud access only; no open weights. | Verified fact | A5-S010, V2-S001 |
| Status events | 4 September 2025: sales barred to entities controlled from unsupported regions such as China; US Department of Defense/War "supply chain risk" designation: Anthropic sued 9 March 2026; the DoD relied on two designations litigated separately - N.D. California (Judge Rita F. Lin, No. 3:26-cv-01996) granted Anthropic summary judgment on 27 August 2026 that the 10 U.S.C. s.3252 designation was unlawful (First Amendment retaliation, due process, arbitrary and capricious); D.C. Circuit (No. 26-1049, Katsas and Rao; Henderson dissenting) upheld the other under FASCSA on 25 September 2026, effect stay | Verified fact | A5-S045, A5-S025, A5-S024, A5-S026, A5-S016, A5-S019, A5-S012, A5-S020, A5-S084, A5-S085, V2-S004, V2-S005, V2-S006, V2-S007, V2-S068 |
| Strategic direction | Tiered safeguards (Fable vs Mythos; Cyber and Life Sciences Verification Programmes); Enterprise Frontier Safeguards (customer-controlled data storage) phased from autumn 2026; price cuts (Opus 5.5 inputs/outputs 20% below Opus 5; cache reads cheaper); multi-cloud distribution; stated "pacing the frontier" policy; IPO preparation. | Verified fact | A5-S016, A5-S019, A5-S020, A5-S024 |
| What it does | General-purpose LLMs for coding, agentic work and knowledge work, served via the Claude API, Claude apps and partner clouds. | Verified fact | A5-S010, A5-S019 |
| Stack position | L1 foundation model. Placement correct; Anthropic also appears at L3 (Claude Agent SDK) and originated L4 standards (MCP, Agent Skills). | Architectural judgement |  |
| Integration | Messages API, Batch API, Models API; OpenAI SDK compatibility endpoint; official SDKs (anthropic Python 1.12.0, MIT, 7 October 2026); model IDs published for Bedrock, Google Cloud, Microsoft Foundry and Claude Platform on AWS. | Verified fact | A5-S010, A5-S013, A5-S047 |
| Dependencies | Hosted service only (Anthropic first-party, Claude Platform on AWS, Amazon Bedrock, Google Cloud, Microsoft Foundry). | Verified fact | A5-S010, A5-S018 |
| Certifications | SOC 2 Type I and Type II, ISO 27001:2022, ISO/IEC 42001:2023 (Schellman), HIPAA-ready configuration, CSA STAR Level 2; scope covers API, Claude Enterprise/Team, Claude in Bedrock and Google Cloud; Claude in Microsoft Foundry hosted on Anthropic is in scope; the Foundry deployment hosted on Azure is listed "In-Process Q4 2026"; Claude for Government listed N/A. SOC 2 bridge letters dated August and October 2026. | Verified fact | A5-S021, A5-S017, V2-S063 |
| GDPR / residency | Commercial/API data not used for training without express permission; consumer plans (Free/Pro/Max) opt-in training with 5-year retention since 28 August 2025 (commercial and API excluded). ZDR on request per organisation; Fable 5.1/Mythos 5.1/Fable 5/Mythos 5 are "Covered Models" requiring 30-day retention and not ZDR unless expressly authorised (conflicts with launch post saying eligible customers may use Fable 5.1 with ZDR until EFS ships). First-party inference_geo supports only "global" or "us"; workspace (storage) geo only "us"; no first-party EU/UK inference option documented. EU proces | Verified fact | A5-S018, A5-S023, A5-S013, A5-S011, A5-S027, A5-S016, V2-S075, V2-S066 |
| Security features | Admin console lists Encryption keys (CMEK), Access Transparency, Inference hooks, Compliance API, Workload Identity Federation (documentation sections). | Verified fact | A5-S013 |
| Access controls | Workspaces, Admin API, user management, Workload Identity Federation, Compliance API / Activity Feed (6-year retention) documented. | Verified fact | A5-S013, A5-S018 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Claude Fable 5.1: US$10 input / US$50 output per 1M (cache read US$0.25); Claude Opus 5.5: US$4 / US$20 per 1M (cache read US$0.20); Claude Sonnet 5.5: US$2 / US$10 per 1M; Claude Haiku 5.5: US$0.10 / US$0.50 per 1M for prompts up to 100K tokens; US$0.50 / US$2.50 above; modifiers: Batch API 50% off; US-only inference_geo 1.1x; full 1M context at standard price except Haiku 5.5 | Verified fact | A5-S011, A5-S010, V2-S002 |
| Infrastructure cost | Not applicable (no self-hosting). | Verified fact | A5-S010 |
| Ecosystem | Amazon Bedrock, Google Cloud (Vertex AI / Gemini Enterprise Agent Platform), Microsoft Foundry, Claude Platform on AWS; Claude Code, Cowork. | Verified fact | A5-S010, A5-S027 |
| Adoption signals | Anthropic-announced customers include Barclays (1 October 2026); Millennium cited in Fable 5.1 launch (vendor-selected). | Verified fact | A5-S012, A5-S016 |
| Maturity | Four GA tiers released 1 September to 7 October 2026; published retirement commitments ("not sooner than" September/October 2027). | Verified fact | A5-S010 |
| Deployment | saas: Yes; managed_cloud: Yes (Bedrock, Google Cloud, Microsoft Foundry, Claude Platform on AWS); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: No | | |

## Google Gemma 4 (open-weight family) (`L1-google-gemma`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Gemma – 2.9

*Rationale:* Strategic, conditional: as the small, self-hosted open-weight tier of the portfolio; not a substitute for a frontier model [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Competent small and medium multimodal models; no frontier tier (A5-S034). |
| Enterprise readiness | 4 | Managed Gemma 4 on Google Cloud and Bedrock gives the hyperscaler presumption (rule 6); self-hosted weights inherit host controls. Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 3 | Scored as self-hosted weights (rule 2): clear Apache 2.0 licence (V2-S020); signed releases and CVE handling not evidenced; inherits host controls. |
| Deployment flexibility | 5 | Managed, self-hosted, on-premises, edge and air-gap (A5-S034). |
| Ecosystem | 4 | Mainstream open-weight tooling and three hosting routes (A5-S034, A5-S027). |
| Reliability and maturity | 4 | Fourth generation, GA open release from Google (A5-S034). |
| Cost / TCO | 4 | Free weights; the larger sizes need a data-centre GPU, so operations are not trivial. |
| Lock-in / portability | 4 | Permissive open weights; governance by one vendor, not neutral, so not 5. |
| **Total (generic / FS)** | **3.80 / 3.80** | |

**Capabilities.** Gemma 4 open-weight family: E2B, E4B, 26B MoE and 31B dense (31 March / 2 April 2026) and a 12B unified multimodal model (3 June 2026); image and video input on all sizes, audio on E2B/E4B; up to 256K context; Apache 2.0 [VF: A5-S034, A5-S035, V2-S020].

**Strengths**

- Apache 2.0 weights from a major vendor, runnable from phones and laptops to a single data-centre GPU [VF: A5-S034, V2-S020] [R: A5-S035]
- Managed hosting on Google Cloud and Bedrock as well as self-hosting [VF: A5-S027] [R: A5-S038]
- Broad tool support (Hugging Face, Kaggle, Ollama, Unsloth) [VF: A5-S034]

**Limitations and risks**

- Small and medium sizes only; no frontier-class model [VF: A5-S034]
- No vendor support for weights verified; security depends on the host [AJ]
- One README links a separate Gemma 4 licence page that was not read [VF: A5-S034]

**Choose when**

- You need a self-hosted classification, extraction or redaction model inside the estate [AJ]
- Data must never leave the firm's infrastructure [AJ]

**Avoid when**

- The task needs frontier reasoning or long-form drafting quality [AJ]

**Nearest competitors:** L1-mistral, L1-meta, L1-alibaba-qwen

**Regulated-FS note.** Self-host behind the gateway with model files scanned and pinned by hash (C7); validate as a model in its own right [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google (Google DeepMind) | Verified fact | A5-S034 |
| Category | Open-weight model family (small/medium, multimodal, on-device) | Verified fact | A5-S034 |
| Version / lineup | current: Gemma 4: E2B, E4B, 26B MoE (A4B), 31B Dense released 31 March 2026 (releases page) / 2 April 2026 (blog); Gemma 4 12B unified encoder-free multimodal added 3 June 2026; MTP drafters April 2026. [A5-S034]; context: 128K (E2B/E4B), up to 256K (larger models); LiteLLM lists 262,144 for 26B/31B. [A5-S034, A5-S038]; multimodal: All models take image and video input; E2B/E4B also audio. [A5-S034]; previous: Gemma 3 (1B/4B/12B/27B) still self-deployable on Google Cloud and on Bedrock. [A5-S027, A5-S038]; graphic_label_check: "2.9" is WRONG: no Gemma 2.9 exists in any source found; current ge | Verified fact | A5-S034, A5-S035, A5-S027, A5-S038, V2-S020 |
| Licence | Open weights under Apache 2.0 (Hugging Face model cards and Google blog); one README also links a separate Gemma 4 licence page on ai.google.dev (not read). | Verified fact | A5-S034, A5-S035, V2-S020 |
| Status events | 31 March / 2 April 2026: Gemma 4 launch; 3 June 2026: Gemma 4 12B | Verified fact | A5-S034, V2-S020 |
| Strategic direction | Edge and on-device focus (Android AICore, AI Edge Gallery), agentic features (function calling, structured JSON), Google reports 150 million Gemma 4 downloads. | Verified fact | A5-S034 |
| What it does | Open-weight multimodal models for local, edge and self-hosted deployment, also served by Google and third parties. | Verified fact | A5-S034 |
| Stack position | L1 open-weight model; the graphic shows it beside Gemini, but its natural deployment is self-hosted via L2 serving engines. | Architectural judgement |  |
| Integration | Weights on Hugging Face/Kaggle/Ollama; hosted Gemma 4 on Gemini API and Google Cloud (26B), Bedrock Mantle (31B, 26B, E2B incl. US GovCloud), Cloudflare, Together, OpenRouter. | Verified fact | A5-S034, A5-S027, A5-S038 |
| Dependencies | Runs on own hardware (laptop to GPU server) via Hugging Face, Kaggle, Ollama; Google AI Edge for devices. | Verified fact | A5-S034 |
| Certifications | Not applicable to weights; Google Cloud hosting inherits Google Cloud certifications. | Architectural judgement |  |
| GDPR / residency | Self-hosting keeps data wherever the operator runs the model. | Architectural judgement |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | No vendor support for open weights verified; support via hosting cloud. | Architectural judgement |  |
| Pricing | weights: Free (Apache 2.0); Google Cloud Gemma 4 26B managed: US$0.15 input / US$0.60 output per 1M | Verified fact | A5-S034, A5-S027 |
| Infrastructure cost | E2B/E4B target phones and laptops; 26B MoE and 31B dense need a single data-centre GPU class (quantisation-aware-training GGUF releases available). | Reported | A5-S034, A5-S035 |
| Ecosystem | Hugging Face, Kaggle, Ollama, Unsloth (QAT, MTP, GGUF, MLX), Google Cloud, Bedrock, Cloudflare Workers AI, Together, DeepInfra. | Verified fact | A5-S034, A5-S043, A5-S038 |
| Adoption signals | Google reports 150 million Gemma 4 downloads. | Verified fact | A5-S034 |
| Maturity | Fourth generation; GA open release. | Verified fact | A5-S034 |
| Deployment | saas: Yes (Gemini API / AI Studio hosting); managed_cloud: Yes (Google Cloud; Amazon Bedrock); vpc_byoc: Yes (self-deploy in own cloud account); private_cloud: Yes (open weights); self_hosted: Yes; on_prem: Yes | | |

## Google Gemini model family (Gemini 3.x: 3.1 Pro, 3.8 Flash, 3.5 Flash-Lite; Gemini 4 Argon in limited release) (`L1-google-gemini`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** Gemini – Gemini

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud (rule 10, the lead model service on that cloud); deployment and lock-in score 2, allowed under rule 11 as an existing platform commitment; FS 3.35 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Broadest evidenced modality range plus reasoning, small, coding-oriented and cyber variants, with Gemma as Google's open-weight line (A5-S030, A5-S027); benchmarks not used. |
| Enterprise readiness | 4 | Consumed through Google Cloud: hyperscaler presumption (rule 6). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 4 | SOC 2 and ISO 42001 for Google Cloud generative AI services, UK/EU data-at-rest residency, ZDR configuration (A5-S028, A5-S029, A5-S033); ISO 27001 scope not in the fact base; stays at 4 (rules 8 and 10). |
| Deployment flexibility | 2 | Google Cloud (regional endpoints) and the Gemini API only; no other cloud, no self-hosting (A5-S027, A5-S032). |
| Ecosystem | 3 | Deep inside Google Cloud (Model Garden, agent runtime) but isolated from AWS and Azure estates (A5-S027). |
| Reliability and maturity | 3 | Flash tiers GA; Pro preview for eight months; Flash versions retire within about five to six months of release (B-L1-S003). |
| Cost / TCO | 3 | Transparent, but 3.8 Flash doubles on 1 January 2027 and regional endpoints carry a 10% premium (A5-S027, V2-S010). |
| Lock-in / portability | 2 | Proprietary API on one cloud only (A5-S027). |
| **Total (generic / FS)** | **3.50 / 3.35** | |

**Capabilities.** Proprietary Gemini 3.x production lineup: 3.1 Pro (still preview since 19 February 2026), 3.8 Flash (GA 2 September 2026), 3.5 Flash-Lite, 3.8 Live and TTS models, image models and cyber-specialised Flash variants; Gemini 4 Argon announced 30 September 2026 with access restricted to trusted cyber defenders (Fairwind) and not on Google Cloud at launch; natively multimodal input (text, image, video, audio) [VF: A5-S027, A5-S030, A5-S031, A5-S032, V2-S009, V2-S010].

**Strengths**

- Widest native modality coverage in the layer: text, image, video and audio input, live audio, TTS and image generation [VF: A5-S030, A5-S027]
- Google Cloud generative AI services in scope for SOC 2 and ISO/IEC 42001 [VF: A5-S028, A5-S037]
- Data-at-rest residency for generative AI in the UK and several EU countries; ZDR achievable on Google Cloud by disabling logging, caching and session resumption [VF: A5-S029, A5-S033]
- Per-model retirement dates published on Google Cloud model pages [VF: B-L1-S003]

**Limitations and risks**

- Pro tier has been preview-only since February 2026; Gemini 3.5 Pro was reportedly cancelled [VF: A5-S032] [R: A5-S036]
- Short Flash lifetimes: 3.7 Flash released 13 August 2026 retires 28 January 2027; 3.6 Flash retires 19 November 2026 [VF: B-L1-S003]
- Google Cloud only; no AWS or Azure listing found; no self-hosting [VF: A5-S027, A5-S032]
- Paid Gemini API (non-Google Cloud) may cache content in any country [VF: A5-S033]
- 3.8 Flash introductory price rises from US$0.75/US$3.75 to US$1.50/US$7.50 per 1M on 1 January 2027; non-global endpoints cost 10% more [VF: A5-S027, V2-S010]
- Frontier tier (Argon) not available for general enterprise use; pricing not published [VF: A5-S031] [NPV]

**Choose when**

- Google Cloud is the primary cloud [AJ]
- The workload needs native audio, video or live multimodal input [AJ]

**Avoid when**

- You need a GA Pro-class model with a long support window today [AJ]
- Your primary cloud is AWS or Azure and you do not want a cross-cloud data flow [AJ]
- You would use the consumer Gemini API rather than Google Cloud for client data [AJ]

**Nearest competitors:** L1-openai, L1-anthropic, L1-mistral

**Regulated-FS note.** Use only through Google Cloud regional (EU or UK) endpoints with logging and caching disabled, pin dated model IDs, and plan re-validation around the short Flash retirement dates [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google (Google DeepMind / Google LLC) | Verified fact | A5-S047, A5-S031 |
| Category | Frontier model vendor: proprietary API models (reasoning, native multimodal input, live audio, TTS, image) | Verified fact | A5-S030, A5-S027 |
| Version / lineup | frontier_restricted: Gemini 4 Argon, announced 30 September 2026; rolling out first to trusted cyber defenders (Fairwind Program); paid API and AI Ultra "next", no date; 1M-token output limit claimed. Not on Vertex AI at launch. [A5-S031, A5-S036]; pro: Gemini 3.1 Pro, preview since 19 February 2026, still labelled preview (gemini-3.1-pro-preview); 1,048,576 input / 65,536 output tokens. Gemini 3 Pro retired 9 March 2026. Gemini 3.5 Pro never released (reported cancelled). [A5-S030, A5-S032, A5-S036]; mid_flash: Gemini 3.8 Flash GA 2 September 2026 ("most intelligent Flash", long-horizon codin | Verified fact | A5-S027, A5-S030, A5-S031, A5-S032, A5-S036, V2-S009, V2-S010 |
| Licence | Proprietary, API-only. | Verified fact | A5-S032 |
| Status events | 9 March 2026: Gemini 3 Pro shut down (replaced by 3.1 Pro); 18 September 2026: Gemini 2.5 access limited to recent users; 30 September 2026: Gemini 4 Argon announced (limited); April 2026: Vertex AI renamed Gemini Enterprise Agent Platform (renames listed in 22 April 2026 release notes) | Verified fact | A5-S030, A5-S031, A5-S028, V2-S009, V2-S037 |
| Strategic direction | Fast Flash cadence (3.5 to 3.8 between May and September 2026) with introductory pricing; Pro tier stalled at 3.1 preview; new Gemini 4 naming with Argon; cyber-specialised variants (3.5/3.8 Flash Cyber); Vertex AI renamed Gemini Enterprise Agent Platform. | Verified fact | A5-S030, A5-S031, A5-S027, A5-S028 |
| What it does | Natively multimodal LLMs (text, image, video, audio input) via the Gemini Developer API / AI Studio and Google Cloud (Gemini Enterprise Agent Platform, formerly Vertex AI). | Verified fact | A5-S027, A5-S033 |
| Stack position | L1 foundation model; Google also appears at L7 (Gemini Embedding) and owns the Gemma open-weight family. | Architectural judgement |  |
| Integration | Gemini API (google-genai SDK 2.29.0, Apache-2.0, 7 October 2026), Interactions API, Live API, Google Cloud endpoints (global, multi-region, regional). | Verified fact | A5-S047, A5-S030, A5-S027 |
| Dependencies | Hosted on Google infrastructure only. | Verified fact | A5-S027 |
| Certifications | Google Cloud generative AI services (Gemini Enterprise Agent Platform) in scope for ISO/IEC 42001:2023 and SOC 2; Gemini in Workspace and Gemini app FedRAMP High. | Verified fact | A5-S028, A5-S037 |
| GDPR / residency | Paid Gemini API: prompts/responses not used to improve products, processed under Google DPA, logged for a limited period for abuse detection and may be cached in any country. Free tier content used for improvement (except EEA/UK/Switzerland, where paid terms apply). Vertex/Agent Platform: no training without permission; ZDR achievable by disabling logging, session resumption and caching and avoiding Search grounding. Data-at-rest residency for generative AI in UK, Netherlands, France, Germany, Belgium etc. (2023 commitment); non-global endpoints priced 10% higher from 1 July 2026. | Verified fact | A5-S033, A5-S032, A5-S029, A5-S027 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Gemini 3.1 Pro Preview: US$2 input / US$12 output per 1M (<=200K); US$4 / US$18 above; Gemini 3.8 Flash: US$0.75 / US$3.75 per 1M introductory to 31 December 2026; US$1.50 / US$7.50 from 1 January 2027; Gemini 3.5 Flash-Lite: US$0.30 / US$2.50 per 1M; Gemini 4 Argon: Not publicly verified | Verified fact | A5-S027, A5-S032, A5-S030, V2-S010 |
| Infrastructure cost | Not applicable (no self-hosting). | Architectural judgement |  |
| Ecosystem | Google Cloud Gemini Enterprise Agent Platform (200+ models in Model Garden), AI Studio, Antigravity agent runtime defaults to 3.8 Flash. | Verified fact | A5-S027, A5-S030 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Flash tiers GA; Pro tier preview only (3.1 Pro); frontier (Argon) restricted. | Verified fact | A5-S030, A5-S032, A5-S031 |
| Deployment | saas: Yes; managed_cloud: Yes (Google Cloud only); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: Not publicly verified | | |

## xAI Grok model family (Grok 4.7 flagship; 4.6, 4.5, 4.3, 4.20; Grok 4.1 Fast; grok-code-fast-1 / Grok Build) (`L1-xai-grok`)

**Tier:** Tactical · **Flags:** Acquired · **Original graphic label:** Grok

*Rationale:* Capable, cheap and on every hyperscaler, but the change of control, naming churn, missing ISO certification and derived-data terms keep it out of the foundation tier [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Flagship, reasoning, multi-agent, fast, coding and generative-media variants (A5-S079, A5-S027); no open weights verified. |
| Enterprise readiness | 4 | Admin settings and audit logs verified (A5-S080) plus hyperscaler routes (rule 6). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 3 | SOC 2 Type II, ZDR, HIPAA BAA (A5-S080); no ISO 27001 and no EU residency for the API, so the anchor-3 baseline only. |
| Deployment flexibility | 3 | First-party SaaS plus all three hyperscalers; no self-hosting verified. |
| Ecosystem | 4 | Google Cloud, Bedrock (incl. GovCloud) and Foundry listings; official SDK (A5-S027, A5-S047). |
| Reliability and maturity | 3 | GA with a steady release cadence, but acquired on 2 February 2026 with naming churn since (V2-S011) and open regulatory investigations into the consumer product (V2-S070). |
| Cost / TCO | 4 | Transparent and low list prices (A5-S079); 1.1x for the US regional endpoint. |
| Lock-in / portability | 2 | Proprietary API on standard routes would be 3; reduced by 1 for the 2026 change of ownership (rule 3). |
| **Total (generic / FS)** | **3.50 / 3.25** | |

**Capabilities.** Proprietary Grok family from SpaceXAI (formerly xAI): Grok 4.7 flagship (21 September 2026, 500K context, configurable reasoning effort), Grok 4.6, 4.5, 4.3 and 4.20 (reasoning, non-reasoning and multi-agent), Grok 4.1 Fast, grok-code-fast-1, image and video generation [VF: A5-S079, V2-S012] [R: A5-S038].

**Strengths**

- Available on all three hyperscalers, including AWS GovCloud for Grok 4.6 [VF: A5-S027] [R: A5-S038]
- SOC 2 Type II, HIPAA-eligible deployments, team-level ZDR and admin audit logs [VF: A5-S080]
- Low flagship list price: US$2/US$6 per 1M up to 200K tokens [VF: A5-S079, V2-S012]

**Limitations and risks**

- SpaceX acquired xAI in an all-stock deal on 2 February 2026; the unit now trades as SpaceXAI, and a further rename was announced on 4 October 2026 but had not taken effect [VF: V2-S011] [R: A5-S081]
- No ISO certifications found; Trust Center under NDA [VF: A5-S080]
- Default endpoint gives no region guarantee; only a US regional endpoint is documented for the API [VF: A5-S080]
- Enterprise terms let the vendor create and own de-identified derived data except under ZDR [VF: A5-S080]
- EU Commission DSA proceedings (26 January 2026) and Ofcom, ICO and Irish DPC investigations into Grok-generated images on X; no outcomes found [VF: V2-S070] [R: A5-S082]
- Signed only the Safety and Security chapter of the GPAI Code of Practice [VF: R-EU-GPAI-COP, A8-S015]

**Choose when**

- A low-cost reasoning model already offered in-tenant on your hyperscaler is wanted as a secondary or evaluation option [AJ]

**Avoid when**

- Client data would go to the first-party API without ZDR [AJ]
- Ownership stability or ISO 27001 is a gating criterion [AJ]

**Nearest competitors:** L1-openai, L1-anthropic, L1-google-gemini

**Regulated-FS note.** If used, use only through a hyperscaler region with platform data terms, and refresh third-party due diligence after the change of control [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | xAI, acquired by SpaceX in an all-stock deal announced and closed 2 February 2026 (wholly owned subsidiary); the AI unit was rebranded SpaceXAI in mid-2026 (July per Wikipedia, 7 May per another reference; no primary source for the date); on 4 October 2026 Elon Musk said SpaceXAI will be renamed SpaceXSI, which had not taken effect as of 5 October 2026 reports | Reported | A5-S081, A5-S079, V2-S011 |
| Category | Frontier model vendor: proprietary API models (reasoning and non-reasoning variants, vision, coding, image/video generation) | Reported | A5-S038 |
| Version / lineup | flagship: Grok 4.7, launched 21 September 2026; 500K context; configurable reasoning effort (low to xhigh). [A5-S079]; previous_flagships: Grok 4.6 (Bedrock incl. US GovCloud, Azure, Google Cloud; xAI SDK README example), Grok 4.5. [A5-S038, A5-S027, A5-S047]; mid_reasoning: Grok 4.20 Reasoning / Non-Reasoning / Multi-agent (model ID suffix 0309), Grok 4.3; 1M context. [A5-S038, A5-S027]; small_fast: Grok 4.1 Fast Reasoning / Non-Reasoning. [A5-S027]; coding: grok-code-fast-1; grok-build. [A5-S038]; multimodal: Grok Imagine image 2.0 and video 1.5; voice transcription. [A5-S038]; open_weight:  | Verified fact | A5-S038, A5-S027, A5-S047, A5-S079, V2-S012 |
| Licence | Proprietary API (open-weight status of older Grok models not verified). | Reported | A5-S038 |
| Status events | 2 February 2026: SpaceX acquired xAI (all-stock; xAI became a wholly owned SpaceX subsidiary); mid-2026 (July per Wikipedia; 7 May per another reference): rebranded SpaceXAI (Grok names unchanged); 21 September 2026: Grok 4.7; January-February 2026: EU Commission DSA proceedings (26 January), Ofcom (12 January), ICO (3 February) and Irish DPC (17 February) investigations into X over Grok-generated sexualised images; no outcomes found as of spring 2026; 4 October 2026: Musk announced SpaceXAI will be renamed SpaceXSI (following a 29 September 2026 US executive order on "super intelligence" term | Reported | A5-S081, A5-S079, A5-S082, V2-S011, V2-S070 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | General-purpose reasoning LLMs and multi-agent variants via the xAI API and partner clouds. | Reported | A5-S038 |
| Stack position | L1 foundation model; placement correct. | Architectural judgement |  |
| Integration | xAI API; official xai-sdk (Python 1.20.0, Apache-2.0, 24 September 2026). | Verified fact | A5-S047 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type II (per xAI API FAQ and business pages; Trust Center under NDA); HIPAA-eligible deployments with BAA. ISO certifications not found. | Verified fact | A5-S080 |
| GDPR / residency | API inputs/outputs not used for training without explicit permission; default 30-day encrypted retention for abuse auditing; team-level Zero Data Retention (deleted within one hour; disables stateful APIs). Enterprise terms let xAI create and own de-identified/aggregated derived data except under ZDR. US regional endpoint (us.api.x.ai) available; default endpoint gives no region guarantee; EU residency mentioned only on voice/imagine product pages. Grok on Google Cloud follows Google Cloud data terms. | Verified fact | A5-S080 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Team-level admin settings and audit logs of administrative events (content excluded under ZDR). | Verified fact | A5-S080 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Grok 4.7 (xAI API): US$2 input / US$6 output per 1M (<=200K); US$4 / US$12 above 200K; cached US$0.50; US regional endpoint 1.1x; Grok 4.20 / 4.3 (Google Cloud): US$1.25 / US$2.50 per 1M; Grok 4.1 Fast (Google Cloud): US$0.20 / US$0.50 per 1M | Verified fact | A5-S079, A5-S027, V2-S012 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Google Cloud (Grok 4.7, 4.6, 4.20, 4.3, 4.1 Fast), Amazon Bedrock (Grok 4.6 global/US/US-Gov), Microsoft Foundry (Grok 4.6, 4.3, 4.20, 4.1 Fast, code-fast-1). | Verified fact | A5-S027, A5-S038 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Yes (Google Cloud; Amazon Bedrock incl. US GovCloud; Microsoft Foundry); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## DeepSeek V4 family (DeepSeek-V4-Pro; DeepSeek-V4.1-Flash, which replaced V4-Flash in the API) (`L1-deepseek`)

**Tier:** Tactical · **Flags:** Not recommended · **Original graphic label:** DeepSeek – V4

*Rationale:* Tactical, conditional: self-hosted MIT weights or Microsoft Foundry in-tenant only; the 'Not recommended' flag applies to DeepSeek's hosted API (PRC storage, unremediated Garante limitation) [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Large MoE reasoning models with 1M context and vision in Flash (A5-S063, A5-S064); no capability claim taken from vendor benchmarks. |
| Enterprise readiness | 4 | 4 only for the Microsoft Foundry route, where Azure sells DeepSeek V4 directly and processes it in-tenant in the customer's geography (rule 6; A5-S087); DeepSeek's own API has no verified SSO/RBAC/audit and would be capped at 2. Hosting caveat (CP4-3): on Azure, Microsoft Foundry's Kimi K3 and GLM-5.x run on Fireworks outside the customer tenant, while DeepSeek V4 is sold directly and processed in-tenant (A5-S087). Kept at 4 by the reader at Checkpoint 4 (CP4-3). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 1 | Hosted API meets anchor 1: no verified certification, PRC storage (A5-S062) and an unremediated Garante limitation (A5-S048, V2-S023). Self-hosted weights would score about 3 under rule 2 (inherits host controls), with CAISI's hijacking findings (A5-S049) as a model-behaviour risk. |
| Deployment flexibility | 4 | Self-host and air-gap possible (MIT), Foundry in-tenant, own SaaS; 4 not 5 because the vendor SaaS is PRC-only and V4 is not on Bedrock or Google Cloud (A5-S086, A5-S027). |
| Ecosystem | 4 | Broad open-serving support and third-party hosts (A5-S039, A5-S044, A5-S087). |
| Reliability and maturity | 2 | Phase-out of V4-Pro announced 10 September and reversed 17 September 2026 (V2-S013); certifications and support NPV. |
| Cost / TCO | 3 | Weights free (MIT) but V4-Pro needs a large multi-GPU cluster; hosted prices are aggregator-level and not used (V2 §4 item 3). |
| Lock-in / portability | 4 | MIT weights mean no model lock-in once self-hosted; jurisdictional exit risk is captured in security and tier. |
| **Total (generic / FS)** | **3.25 / 3.15** | |

*Evidence rules applied:* security_compliance at 1 (below the NPV cap of 2): certifications NPV plus unremediated regulatory finding on the hosted API

**Capabilities.** DeepSeek V4 family: V4-Pro (1.6T total / 49B active, GA 13 August 2026, 1M context; a planned phase-out was reversed on 17 September 2026) and V4.1-Flash (10 September 2026, replaced V4-Flash in the API, native vision); thinking and non-thinking modes; open weights under MIT [VF: A5-S063, A5-S064, A5-S065, V2-S013].

**Strengths**

- MIT-licensed open weights: the most permissive licence among the large Chinese-origin families [VF: A5-S063]
- Microsoft Foundry sells V4-Pro and V4-Flash directly, processed in the customer's geography or Data Zone [VF: A5-S087]
- Day-0 support in common open serving engines (SGLang, LMDeploy, KTransformers) [R: A5-S039, A5-S044, A5-S042]

**Limitations and risks**

- Hosted API: DeepSeek stores data in the PRC under PRC-law terms; API training position not stated; no EU/UK residency [VF: A5-S062]
- Italy's Garante imposed an urgent limitation on DeepSeek's processing of Italian users' data on 30 January 2025; no lifting or fine found [VF: A5-S048, V2-S023]
- Korea PIPC found unconsented transfers of prompts and device data (24 April 2025); Berlin DPA reported the app under DSA Art. 16 (27 June 2025) [VF: A5-S053, A5-S058]
- Government-device bans: Australia, Taiwan agencies, US DoD (FY2026 NDAA s.1532) and intelligence community, several US states and Commerce bureaus, UK DWP; no US private-sector ban as of October 2026 [VF: A5-S054, A5-S059, A5-S057, A5-S056, A5-S061, A5-S060]
- NIST CAISI (September 2025) found DeepSeek R1/V3.1 more susceptible to agent hijacking and jailbreaks, with censorship risk [VF: A5-S049]
- Certifications, access controls and enterprise support not publicly verified [NPV]
- API prices are aggregator-sourced for decision purposes and not used as inputs [R: A5-S038]

**Choose when**

- A firm's sovereignty policy permits Chinese-origin weights and a self-hosted or Foundry in-tenant model is needed for low-risk, non-agentic internal tasks [AJ]

**Avoid when**

- Any route sends data to DeepSeek's own API [AJ]
- The model would act agentically with tool access, given CAISI's hijacking findings [AJ]
- The firm has US DoD contract exposure (s.1532) [AJ]

**Nearest competitors:** L1-mistral, L1-google-gemma, L1-alibaba-qwen

**Regulated-FS note.** Hosted API not recommended for a regulated firm; if used at all, self-host the MIT weights or use Foundry in-tenant, behind the gateway and guardrails, with a documented sovereignty assessment [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | DeepSeek (Hangzhou DeepSeek AI; PRC). Open Platform terms governed by laws of mainland PRC; US bills name High Flyer as owner. | Reported | A5-S062, A5-S055, A5-S049 |
| Category | Open-weight model vendor with hosted API (reasoning, coding; Flash vision experimental) | Reported | A5-S038, A5-S041 |
| Version / lineup | flagship: DeepSeek-V4-Pro: preview 24 April 2026 (1.6T total / 49B active); GA 13 August 2026 (V4-Pro-0813); 1M context, 384K output. The planned phase-out (routing V4-Pro calls to V4.1-Flash from 14 September 2026) was reversed: the pricing-page footnote updated 17 September 2026 says the V4-Pro API continues with billing unchanged (the 10 September news post still carries the phase-out wording). [A5-S063, A5-S064, A5-S065]; small_fast: DeepSeek-V4.1-Flash: released 10 September 2026; 552B MoE, 8B/16B active; native vision; API name deepseek-flash; replaces V4-Flash (preview 24 April; officia | Verified fact | A5-S063, A5-S064, A5-S065, A5-S027, A5-S086, V2-S013 |
| Licence | Open weights under MIT licence; also hosted API. | Verified fact | A5-S063 |
| Status events | 24 April 2026: V4 preview (Pro, Flash); 31 July 2026: V4-Flash-0731 official; 13 August 2026: V4-Pro GA; peak/off-peak pricing from 16 August; 10 September 2026: V4.1-Flash; price cuts; V4-Pro phase-out announced, then reversed on 17 September 2026 (V4-Pro API continues) | Verified fact | A5-S063, A5-S064, V2-S013 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Large mixture-of-experts LLMs released as open weights and served via DeepSeek's own API and third-party clouds. | Reported | A5-S044, A5-S038 |
| Stack position | L1 foundation model; open weights also make it an L2 self-hosting candidate. | Architectural judgement |  |
| Integration | DeepSeek API (OpenAI-compatible model IDs per aggregator); open weights served by SGLang, vLLM-class engines, KTransformers, LMDeploy. | Reported | A5-S038, A5-S039, A5-S042, A5-S044 |
| Dependencies | Self-hosting requires large multi-GPU clusters (V4-Pro ~1.6T parameters); V4-Flash demonstrated on single Ascend NPU with CPU expert offload (KTransformers). | Reported | A5-S044, A5-S042 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | DeepSeek states it collects, processes and stores personal data in the PRC (consumer and Open Platform policies); Open Platform terms under mainland PRC law; consumer data may be used for training with opt-out; API training position not stated. No EU/UK residency option. Non-China processing only via third-party hosting (e.g. Microsoft Foundry) or self-hosted weights. | Verified fact | A5-S062, A5-S087 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | deepseek-v4-pro (peak): US$1.32 input (cache miss) / US$3.96 output per 1M; off-peak half; deepseek-flash = V4.1-Flash (peak): US$0.30 / US$1.20 per 1M; off-peak US$0.15 / US$0.60; Microsoft Foundry V4-Pro: US$1.74 / US$3.48 per 1M (aggregator) | Verified fact | A5-S065, A5-S038 |
| Infrastructure cost | V4-Pro ~1.6T and V4-Flash ~284B total parameters (LMDeploy); quantised V4-Flash runs on a single Ascend NPU with CPU offload (KTransformers). | Reported | A5-S044, A5-S042 |
| Ecosystem | Day-0 support in SGLang; supported by LMDeploy, KTransformers, Xinference, Unsloth; hosted by Microsoft Foundry, Alibaba Model Studio, Together, Fireworks, Nebius, Databricks, OpenRouter. | Reported | A5-S039, A5-S044, A5-S042, A5-S041, A5-S043, A5-S038 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (DeepSeek API, data stored in PRC); managed_cloud: Yes: Microsoft Foundry sells V4-Pro/V4-Flash directly by Azure (customer geography, Global or DataZone processing); Bedrock and Google Cloud offer only V3.x/R1 (Bedrock V3.2 includes EU profile); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open weights); on_prem: Yes (open weights) | | |

## Z.ai (Zhipu) GLM model family (GLM-5.3, GLM-5.3-Flash, GLM-5.2, GLM-5.1, GLM-5; GLM-4.7) (`L1-zai-glm`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** QI4 (Z logo) – Q4

*Rationale:* Tactical, conditional: self-hosted GLM-5.3-Flash (MIT) only, after sanctions review; Entity List status and unverified data terms rule out the hosted API [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Large agentic/coding model, a multimodal MIT Flash tier and an image model; CAISI's independent assessment places GLM-5.3 near the frontier on cyber tasks (A5-S052). |
| Enterprise readiness | 4 | The Bedrock (AWS-operated) route gives the hyperscaler presumption (rule 6): GLM 5.3 cross-Region only from 5 October 2026, GLM 5 in-Region in London (A5-S086). Hosting caveat (CP4-3): on Azure, Microsoft Foundry's Kimi K3 and GLM-5.x run on Fireworks outside the customer tenant, while DeepSeek V4 is sold directly and processed in-tenant (A5-S087). The Azure route therefore does not support this score, and Z.ai API controls are NPV (would be 2). Kept at 4 by the reader at Checkpoint 4 (CP4-3). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 2 | Certifications NPV (cap 2); Singapore processing and DPA conflict (A5-S073). |
| Deployment flexibility | 4 | Own API, three hyperscalers (London in-Region for GLM 5), Mistral platform, self-host and on-premises. |
| Ecosystem | 3 | Present on many platforms, but the current GLM-5.3 reaches them via cross-Region or pass-through routes; Mistral retires GLM 5.2 on its platform on 31 October 2026 (B-L1-S002). |
| Reliability and maturity | 2 | Entity List exposure is a continuity risk for any commercial relationship (A5-S072); maturity and support NPV. |
| Cost / TCO | 3 | MIT Flash weights are cheap to run; GLM-5.3 needs multi-GPU serving; hosted prices not decision inputs (V2 §4 item 3). |
| Lock-in / portability | 3 | MIT for Flash; MIT-style grant with a MaaS condition for GLM-5.3 (rule 4). |
| **Total (generic / FS)** | **3.25 / 3.15** | |

*Evidence rules applied:* security_compliance capped at 2: certifications NPV

**Capabilities.** Z.ai (Zhipu) GLM-5.x family: GLM-5.3 (753B, API mid-August 2026 (14 August per CAISI, 18 August per press), weights about 28 August under a bespoke licence), GLM-5.3-Flash (26 August 2026, 320B / 18B active, natively multimodal, MIT), GLM-5.2 open weights, GLM-Image; the graphic's 'QI4' label matches no model [VF: A5-S071, V2-S021] [R: V2-S016, A5-S038, A5-S042].

**Strengths**

- GLM-5.3-Flash is MIT-licensed and targets consumer GPUs [VF: A5-S071] [R: A5-S042]
- Available on Google Cloud, Bedrock (GLM 5 in-Region in London), Microsoft Foundry and Mistral's platform [VF: A5-S086, A5-S027] [R: A5-S038]
- NIST CAISI (September 2026) assessed GLM-5.3 as the most cyber-capable open-weight model to date, about four months behind the US frontier [VF: A5-S052, V2-S021]

**Limitations and risks**

- Zhipu AI has been on the US Entity List since 16 January 2025, with a presumption of denial for EAR items [VF: A5-S072]
- Data 'generally processed in Singapore'; DPA versions conflict on storage; privacy policy cites training under legitimate interest [VF: A5-S073]
- GLM-5.3 on Bedrock is US/global cross-Region only; Foundry's GLM is Fireworks-operated outside the tenant [VF: A5-S086, A5-S087]
- CAISI found GLM-5.2 safeguards allow agentic exploit assistance [VF: A5-S052]
- Certifications, access controls and support not publicly verified [NPV]

**Choose when**

- Sovereignty policy and sanctions counsel permit it, and a small MIT model (GLM-5.3-Flash) is needed self-hosted [AJ]

**Avoid when**

- Any direct commercial relationship with Z.ai would be required, until legal review of the Entity List exposure [AJ]
- Client data would go to the Z.ai API [AJ]

**Nearest competitors:** L1-deepseek, L1-alibaba-qwen, L1-mistral

**Regulated-FS note.** Self-hosted MIT weights only, after sanctions and licence review; no Z.ai API for client data [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Z.ai (Zhipu AI; listed in US Entity List as Beijing Zhipu Huazhang Technology Co., Ltd. a.k.a. Zhipu AI). International services provided by Jingsheng Hengxing Technology Pte. Ltd. (Singapore). | Verified fact | A5-S072, A5-S073 |
| Category | Open-weight and API model vendor (agentic/coding LLMs, multimodal, image) | Reported | A5-S038, A5-S041 |
| Version / lineup | flagship: GLM-5.3 (753B; same base as GLM-5.2, post-trained; API launch mid-August 2026 (14 August per NIST CAISI, 18 August per press); weights about 28 August 2026 under a bespoke glm-5.3 licence; on Bedrock from 5 October 2026), GLM-5.2 (open weights, 1M context, June 2026). [A5-S071, A5-S086, A5-S042]; small_fast: GLM-5.3-Flash (320B total / 18B active, first natively multimodal GLM-5, MIT); GLM-5.3-FlashX. [A5-S071]; previous: GLM-5 (day-0 support 12 February 2026), GLM-5.1, GLM-5-Code, GLM-4.7 / 4.7-Flash. [A5-S042, A5-S038]; multimodal: GLM-Image. [A5-S041]; graphic_label_check: "QI4" / | Reported | A5-S038, A5-S041, A5-S042, A5-S043, A5-S044, A5-S071, A5-S086, V2-S016, V2-S021 |
| Licence | GLM-5.3-Flash: MIT. GLM-5.3: MIT-style grant with "Model as a Service" condition (MaaS businesses >US$10bn revenue need Z.ai security review). | Verified fact | A5-S071 |
| Status events | 12 February 2026: GLM-5; 17 June 2026: GLM-5.2; 26 August 2026: GLM-5.3-Flash open weights (MIT); 16 January 2025: Zhipu AI added to US Entity List (presumption of denial for EAR items); 5 October 2026: GLM 5.3 GA on Amazon Bedrock (eligible enterprise customers); 14 August 2026 (CAISI) / 18 August 2026 (press): GLM-5.3 released; weights about 28 August 2026; September 2026: NIST CAISI assessment finds GLM-5.3 the most cyber-capable open-weight model to date, about four months behind the US frontier | Reported | A5-S042, A5-S072, A5-S086, V2-S016, V2-S021 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Large MoE LLMs for agentic and coding workloads released as open weights and via the Z.ai API. | Reported | A5-S043, A5-S038 |
| Stack position | L1 foundation model. | Architectural judgement |  |
| Integration | Z.ai API (zai-sdk 0.2.3, 16 June 2026); open weights via SGLang, KTransformers, Unsloth, LMDeploy, Xinference; also resold on Mistral's platform (zai-glm-5-3). | Verified fact | A5-S047, A5-S039, A5-S038 |
| Dependencies | GLM-5.2 ~744-754B parameters requires multi-GPU serving; NVFP4 serving reported at 500 TPS with SGLang. | Reported | A5-S043, A5-S044, A5-S039 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Personal data "generally processed in Singapore"; may transfer to Z.ai Group affiliates overseas. Current DPA says API content is not stored (older version said temporary storage - conflict). General privacy policy cites model training under legitimate interest; API terms do not expressly exclude API inputs from training. No EU residency option found. Bedrock GLM 5 in-Region in eu-west-2 (London); GLM 5.3 via US/global cross-Region only. | Verified fact | A5-S073, A5-S086 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | GLM-5.3 (Z.ai): US$1.40 input / US$4.40 output per 1M; cached US$0.26; GLM-5.3-Flash: US$0.15 / US$0.50 per 1M; GLM-5.2 (Google Cloud): US$1.40 / US$4.40 per 1M | Verified fact | A5-S071, A5-S027 |
| Infrastructure cost | GLM-5.2 runnable locally only with heavy quantisation (Unsloth dynamic GGUFs); GLM-5.3-Flash targets consumer GPUs. | Reported | A5-S043, A5-S042 |
| Ecosystem | Google Cloud, Bedrock, Microsoft Foundry, Mistral platform; SGLang, KTransformers, Unsloth, LMDeploy, Xinference. | Reported | A5-S027, A5-S038, A5-S039, A5-S042, A5-S043, A5-S044, A5-S041 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Z.ai API); managed_cloud: Yes (Google Cloud GLM-4.7/5/5.2; Amazon Bedrock GLM-5/4.7 US regions; Microsoft Foundry Fireworks-operated GLM-5 to 5.3; Mistral platform GLM-5.x); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open weights); on_prem: Yes (open weights) | | |

## Meta Muse family (Muse Spark 1.1-1.3 via Meta Model API; Muse Glimmer 30B open weights; Muse Code; Muse Image) plus Llama 4 (Scout, Maverick) (`L1-meta`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** Meta – Llama (new: Muse)

*Rationale:* Brand transition from Llama to Muse is under way, the API is weeks past GA and its data terms are unverified; useful for open-weight continuity only [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | API flagship, small open model, code and image models (A5-S077, A5-S078); capability evidence beyond names is thin and Llama has not been refreshed since April 2025. |
| Enterprise readiness | 4 | Muse Spark 1.3 on Foundry and Llama 4 on all three hyperscalers give the presumption (rule 6); Meta Model API controls NPV. Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 2 | Certifications and data terms NPV (cap 2); contributor tier trains on data (V2-S019). |
| Deployment flexibility | 4 | Meta API, hyperscalers and self-hosted open weights. |
| Ecosystem | 4 | Llama's broad hosting footprint plus Foundry, OCI and Google Cloud preview for Muse (A5-S077, A5-S027). |
| Reliability and maturity | 2 | Brand transition in 2026, API GA only since late September 2026, stale SDK (A5-S047). |
| Cost / TCO | 3 | Muse prices are aggregator-level; Llama 4 on Google Cloud is cheap (A5-S027); contributor pricing is excluded as a data-use condition. |
| Lock-in / portability | 3 | Mixed: Apache 2.0 (Glimmer, secondary), community licence with MAU threshold (Llama 4, rule 4), API-only flagship. |
| **Total (generic / FS)** | **3.15 / 3.05** | |

*Evidence rules applied:* security_compliance capped at 2: certifications NPV

**Capabilities.** Meta Muse family from Meta Superintelligence Labs: Muse Spark (announced April 2026; 1.1 to 1.3 via the Meta Model API, GA at Meta Connect 23-24 September 2026; 1M context), Muse Glimmer 30B open weights (August 2026, Apache 2.0 per secondary sources), Muse Code and Muse Image; plus Llama 4 Scout and Maverick under the Llama 4 Community License [VF: A5-S077, A5-S078, V2-S019, A5-S027] [R: A5-S038, A5-S040].

**Strengths**

- Llama 4 is available on Google Cloud, Bedrock and Foundry; Muse Spark 1.3 is on Foundry [VF: A5-S027] [R: A5-S038]
- An open small model (Glimmer 30B) alongside the API flagship [VF: A5-S078] [R: A5-S040]

**Limitations and risks**

- Meta Model API data terms, certifications and EU residency not publicly verified [NPV]
- The 'contributor' tier is discounted in exchange for Meta training on prompts and completions: a data-use condition, not a cheaper price [VF: V2-S019]
- Llama 4 Community License requires a separate licence above 700M MAU; no Llama release since Llama 4 [VF: A5-S077] [R: A5-S038]
- Official llama-api-client SDK last released 18 December 2025 [VF: A5-S047]
- Glimmer's Apache 2.0 licence rests on secondary sources [R: V2-S019]

**Choose when**

- You already self-host Llama 4 and want continuity, or you want Glimmer 30B as an additional open-weight option [AJ]

**Avoid when**

- Client data would go to the Meta Model API before its data terms are verified [AJ]
- Any route would use the contributor tier [AJ]

**Nearest competitors:** L1-google-gemma, L1-mistral, L1-openai

**Regulated-FS note.** Block the contributor tier at the gateway; use Llama 4 or Glimmer only self-hosted or via a hyperscaler [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Meta (models built by Meta Superintelligence Labs) | Verified fact | A5-S077, A5-S078 |
| Category | Model vendor: hosted API models (Muse Spark) and open-weight models (Muse Glimmer, Llama 4) | Reported | A5-S038, A5-S040 |
| Version / lineup | flagship_api: Muse Spark announced April 2026 (Meta Superintelligence Labs); Muse Spark 1.1 with public Meta Model API preview 9 July 2026; 1.2 on 5 August 2026; 1.3 on 2 September 2026; Meta Model API GA globally (announced at Meta Connect, 23-24 September 2026; pre-Connect developer page still said public preview); 1,048,576 context; OpenAI/Anthropic-SDK compatible; on Oracle Cloud, Microsoft Foundry, Google Cloud private preview. [A5-S077, A5-S038]; open_weight: Muse Glimmer 30B, released August 2026 under Apache 2.0 (distilled from Muse Spark, agentic, consumer hardware). [A5-S078, A5-S040 | Verified fact | A5-S038, A5-S040, A5-S027, A5-S047, A5-S077, A5-S078, V2-S019 |
| Licence | Muse Spark: hosted API only. Muse Glimmer 30B: Apache 2.0. Llama 4: Llama 4 Community License (attribution; >700M MAU need separate licence; California law). | Verified fact | A5-S077, A5-S078 |
| Status events | April 2026: Muse Spark announced; 9 July 2026: Meta Model API public preview (Muse Spark 1.1); 5 August 2026: Muse Spark 1.2, Muse Code; August 2026: Muse Glimmer 30B (Apache 2.0); 2 September 2026: Muse Spark 1.3; Meta Connect 2026: Meta Model API GA | Verified fact | A5-S077, A5-S078, V2-S019 |
| Strategic direction | Frontier effort moved to Meta Superintelligence Labs' Muse brand: hosted API flagship (Muse Spark) plus a permissively licensed small open model (Muse Glimmer), distribution via Oracle, Microsoft and Google clouds. | Verified fact | A5-S077, A5-S078 |
| What it does | Multimodal reasoning LLMs via Meta's developer API and partner clouds; open-weight models for self-hosting. | Reported | A5-S038, A5-S040 |
| Stack position | L1 foundation model. | Architectural judgement |  |
| Integration | Meta developer API (Llama API client SDK); Microsoft Foundry; open weights via ModelScope/Hugging Face and inference providers. | Reported | A5-S047, A5-S038, A5-S040 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Muse Spark 1.3 (Meta API): US$1.25 input / US$4.25 output per 1M (aggregator); contributor variant US$0.10 / US$0.20; Muse Glimmer 30B (Together): US$0.35 / US$1.50 per 1M; Llama 4 Maverick (Google Cloud): US$0.35 / US$1.15 per 1M; Llama 4 Scout (Google Cloud): US$0.25 / US$0.70 per 1M | Reported | A5-S038, A5-S027 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Microsoft Foundry, Google Cloud, Amazon Bedrock, Together, Fireworks, DeepInfra, OpenRouter, ms-swift. | Reported | A5-S038, A5-S027, A5-S040 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Meta API); managed_cloud: Yes (Microsoft Foundry Muse Spark 1.3; Llama 4 on Google Cloud, Bedrock, Foundry); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Muse Glimmer 30B, Llama 4); on_prem: Yes (open-weight models) | | |

## Alibaba Qwen model family (Qwen3.8: Max, Flash, Omni-Flash API; open-weight Qwen3.8-27B, Qwen3.8-2.4T-A95B, Qwen3.8-Flash-Next) (`L1-alibaba-qwen`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** Qwen – 3.8

*Rationale:* Tactical, conditional: self-hosted Apache-2.0 sizes only, subject to sovereignty policy; hosted Max and Model Studio lack verified certifications and controls [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Dense and MoE sizes, omni-modal, coding and embedding variants (A5-S068, A5-S038); evidence is partly secondary. |
| Enterprise readiness | 2 | Qwen3.8 is on no hyperscaler, so rule 6 does not apply; Model Studio SSO/RBAC/audit NPV (cap 2). |
| Security and compliance | 2 | Certifications NPV (cap 2); Frankfurt region and no-training statement are positives (A5-S067). |
| Deployment flexibility | 4 | Model Studio (EU scope available) plus self-host and on-premises for open sizes; no current-generation hyperscaler route. |
| Ecosystem | 4 | Broad open-serving and third-party hosting support (A5-S038, A5-S041, A5-S043). |
| Reliability and maturity | 3 | Frequent generations (3.5 to 3.8 within 2026); maturity evidence NPV; 3 on observed cadence. |
| Cost / TCO | 3 | Apache-2.0 small sizes are cheap to run; hosted prices are not decision inputs (V2 §4 item 3); flagship needs multi-node serving. |
| Lock-in / portability | 3 | Apache-2.0 for small sizes; custom licence with a revenue threshold for the flagship (rule 4). |
| **Total (generic / FS)** | **3.15 / 3.00** | |

*Evidence rules applied:* enterprise_readiness capped at 2: SSO/RBAC/audit NPV and no current-generation hyperscaler route; security_compliance capped at 2: certifications NPV

**Capabilities.** Qwen3.8 family: hosted qwen3.8-max (launched 3 August 2026), qwen3.8-flash and omni-flash through Alibaba Cloud Model Studio; open weights Qwen3.8-27B (Apache 2.0), Qwen3.8-2.4T-A95B (12 August 2026, custom Qwen3.8-Max License) and Qwen3.8-Flash-Next; coding and embedding lines [VF: A5-S066, A5-S068] [R: V2-S014, A5-S038, A5-S040].

**Strengths**

- Widest open-weight size range in the layer (27B to 2.4T total) [VF: A5-S066] [R: A5-S041]
- Model Studio is region-bound, with a Frankfurt EU scope, and says it never trains on customer data [VF: A5-S067]
- Qwen3.8-27B under Apache 2.0 [VF: A5-S066]

**Limitations and risks**

- Qwen3.8 is not offered on any hyperscaler; Bedrock and Google Cloud carry only Qwen3 [VF: A5-S086, A5-S027]
- Flagship weights use a custom licence: Model-as-a-Service businesses above US$50m trailing revenue need a separate licence (licence file not read) [R: V2-S014]
- Taiwan's NSB (November 2025) found security and bias failings in Tongyi/Qwen among five PRC models; no CAISI evaluation of Qwen found [VF: A5-S059, A5-S051]
- Reported July 2026 consideration in Beijing of restricting overseas access to leading Chinese models including open-weight Qwen (unenacted) [R: A5-S060]
- Certifications, access controls and support for Model Studio not publicly verified [NPV]

**Choose when**

- A small Apache-2.0 model (Qwen3.8-27B) is needed self-hosted and the firm's sovereignty policy permits Chinese-origin weights [AJ]

**Avoid when**

- The firm needs a hyperscaler-hosted current-generation route [AJ]
- You would deploy the flagship weights without legal review of the custom licence [AJ]

**Nearest competitors:** L1-google-gemma, L1-mistral, L1-deepseek

**Regulated-FS note.** Self-host the Apache-2.0 sizes only; treat Model Studio Frankfurt as unassessed until certifications are verified [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Alibaba Cloud (Qwen team); official dashscope SDK published by Alibaba Cloud | Verified fact | A5-S047 |
| Category | Open-weight and API model vendor (general, reasoning, coding, omni-modal, embeddings) | Reported | A5-S038, A5-S040 |
| Version / lineup | flagship_api: qwen3.8-max (snapshot qwen3.8-max-0902), 1M context, 128K output; US$2 / US$6 per 1M (International scope). [A5-S068, A5-S038]; small_api: qwen3.8-flash and qwen3.8-omni-flash, ~992K context. [A5-S038]; open_weight: Qwen3.8-2.4T-A95B flagship weights (hosted Qwen3.8-Max launched 3 August 2026; weights 12 August 2026; ~95B active; open weights reportedly text-only and without the full 1M context; custom Qwen3.8-Max License), Qwen3.8-27B (Apache 2.0, 262K native context), Qwen3.8-Flash (open-weight multimodal MoE, ~late August 2026), Qwen3.8-Flash-Next. [A5-S066, A5-S068, A5-S040,  | Verified fact | A5-S038, A5-S040, A5-S041, A5-S044, A5-S027, A5-S066, A5-S068, V2-S014 |
| Licence | Mixed: Qwen3.8-27B Apache 2.0; Qwen3.8-2.4T-A95B (open weights 12 August 2026) under a custom "Qwen3.8-Max License": Model-as-a-Service or AI-assistant businesses with over US$50m trailing revenue need a separate licence, with attribution duties for very large products (Reported; licence file not read); Max/Plus API tiers proprietary; Qwen-Image-2.1 reportedly research-only. | Reported | A5-S066, V2-S014 |
| Status events | February 2026: Qwen3.5 (LMDeploy support); 26 August 2026: Qwen3.8-Flash-Next (ms-swift day-0); 3 August 2026: Qwen3.8-Max hosted launch (Reported); 12 August 2026: Qwen3.8-2.4T-A95B open weights under Qwen3.8-Max License (Reported) | Reported | A5-S044, A5-S040, V2-S014 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Family of dense and MoE LLMs, multimodal and coding variants, offered as open weights and via Alibaba Cloud Model Studio (DashScope) API. | Reported | A5-S038, A5-S041 |
| Stack position | L1 foundation model; Qwen3 embeddings also appear at L7. | Architectural judgement |  |
| Integration | DashScope API (dashscope SDK 1.27.7, Apache 2.0, 24 September 2026); open weights via Hugging Face/ModelScope served by vLLM, SGLang, LMDeploy, Xinference. | Verified fact | A5-S047, A5-S041 |
| Dependencies | Self-hosting: model sizes range from 27B to 2.4T total parameters (Qwen3.8). | Reported | A5-S041 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Alibaba says it never uses customer data for model training (Model Studio FAQ). Region-bound storage: Frankfurt region supports an EU deployment scope (workspace-dedicated endpoint), Singapore "International" scope, US (Virginia) US scope, Beijing mainland scope; static data remains in the selected region. Bedrock-hosted Qwen3 available in London, Ireland, Stockholm, Milan regions. | Verified fact | A5-S067, A5-S086 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | qwen3.8-max (International): US$2 input / US$6 output per 1M; cached US$0.25; qwen3.8-flash (Singapore): US$0.15 / US$0.47 per 1M; Global/US US$0.113 / US$0.382; Google Cloud Qwen3-235B-A22B-2507: US$0.22 / US$0.88 per 1M | Verified fact | A5-S068, A5-S027 |
| Infrastructure cost | Qwen3.8 open sizes 27B (single-GPU class with quantisation) to 2.4T-A95B (multi-node). | Reported | A5-S041, A5-S043 |
| Ecosystem | Google Cloud, Amazon Bedrock (Qwen3 incl. eu-west-2 London), Together, DeepInfra, Groq, OpenRouter; Unsloth, ms-swift, LLaMA-Factory, Xinference support. | Reported | A5-S027, A5-S038, A5-S040, A5-S041, A5-S043 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Alibaba Cloud Model Studio); managed_cloud: Yes (Google Cloud Qwen3 models; Amazon Bedrock Qwen3 family incl. EU/UK regions); Qwen3.8 not listed on hyperscalers; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open-weight sizes); on_prem: Yes (open-weight sizes) | | |

## Moonshot AI Kimi model family (Kimi K3; K2.7-Code, K2.6, K2.5, K2-Thinking) (`L1-moonshot-kimi`)

**Tier:** Experimental · **Flags:** none · **Original graphic label:** Kimi – K3

*Rationale:* Large and capable on paper, but evidence is largely secondary, the weights are expensive to host, the licence is custom and no in-region hyperscaler route exists [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | One flagship plus a coding variant; CAISI places K3 below frontier cyber capability (A5-S051); narrower lineup than peers. |
| Enterprise readiness | 4 | The Bedrock (AWS-operated) route, through US, India and global cross-Region profiles only (A5-S086), gives the hyperscaler presumption (rule 6). Hosting caveat (CP4-3): on Azure, Microsoft Foundry's Kimi K3 and GLM-5.x run on Fireworks outside the customer tenant, while DeepSeek V4 is sold directly and processed in-tenant (A5-S087). The Azure route therefore does not support this score, and the Kimi API's controls are NPV (would be 2). Kept at 4 by the reader at Checkpoint 4 (CP4-3). Platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 2 | Certifications NPV (cap 2); Singapore storage; training-policy conflict (A5-S070). |
| Deployment flexibility | 3 | Own API, Bedrock cross-Region only, Foundry outside tenant, self-host of 2.8T weights; no in-region managed route. |
| Ecosystem | 3 | SGLang, Xinference and two hyperscalers, but the current model reaches them only through cross-Region or pass-through routes. |
| Reliability and maturity | 2 | Maturity, support and adoption NPV; facts rest on secondary sources (V2-S015). |
| Cost / TCO | 2 | Self-hosting a 2.8T MoE is a heavy operations burden; hosted prices are not decision inputs (V2 §4 item 3). |
| Lock-in / portability | 3 | Open weights, but under a custom licence with thresholds (rule 4). |
| **Total (generic / FS)** | **2.80 / 2.80** | |

*Evidence rules applied:* security_compliance capped at 2: certifications NPV

**Capabilities.** Kimi K3 (launched 16 July 2026; weights by 27 July 2026; 2.8T-parameter MoE, about 104B active reported; native multimodal; 1M context) plus K2.7-Code and earlier K2.x models [VF: A5-S069] [R: V2-S015, A5-S038].

**Strengths**

- Open weights for a very large multimodal model [VF: A5-S069]
- Offered on Amazon Bedrock and Microsoft Foundry [VF: A5-S086, A5-S087]

**Limitations and risks**

- International API stores data in Singapore; mainland platform in the PRC; API page says no training but the privacy policy lists training as a purpose [VF: A5-S070]
- Bedrock offers K3 only through cross-Region profiles (US, India, global); Foundry's K3 is Fireworks-operated with inference outside the customer's tenant [VF: A5-S086, A5-S087]
- Custom Kimi K3 License with revenue and MAU thresholds, not MIT [VF: A5-S069] [R: V2-S015]
- CAISI with UK AISI (July 2026): below frontier cyber capability; safeguards did not stop attempted exploit development; K2 Thinking heavily censored in Chinese [VF: A5-S051, V2-S021]
- Context only, not a scored limitation: Anthropic alleges that Moonshot distilled Claude; this is an unadjudicated competitor allegation and the author is an Anthropic model, so it is not used in any score [VF: A5-S046, V2-S022]
- Certifications, access controls and support not publicly verified [NPV]

**Choose when**

- Research or evaluation of large open-weight multimodal models in an isolated environment [AJ]

**Avoid when**

- Any production use with client data in a regulated firm today [AJ]

**Nearest competitors:** L1-deepseek, L1-zai-glm, L1-alibaba-qwen

**Regulated-FS note.** Do not use for client data; if evaluated, self-host in an isolated sandbox after licence review [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Moonshot AI: international API operated by Moonshot AI PTE. LTD. (Singapore); mainland platform by Beijing Moonshot Technology (PRC) | Verified fact | A5-S070 |
| Category | Open-weight and API model vendor (agentic, reasoning, multimodal) | Reported | A5-S038, A5-S040 |
| Version / lineup | flagship: Kimi K3, launched 16 July 2026; weights released by 27 July 2026 on Hugging Face; 2.8T-parameter MoE (about 104B active, reported); native multimodal; 1M context. [A5-S069, A5-S039, A5-S040]; coding: Kimi K2.7-Code (262K context). [A5-S038]; previous: Kimi K2.6, K2.5 (January 2026 per KTransformers), K2-Thinking (on Google Cloud and Bedrock). [A5-S038, A5-S042, A5-S027]; graphic_label_check: "K3" is CORRECT (16 July 2026), verified from Moonshot pages. | Verified fact | A5-S038, A5-S039, A5-S040, A5-S041, A5-S042, A5-S027, A5-S069, V2-S015, V2-S021 |
| Licence | Open weights under the custom "Kimi K3 License" (MIT-style grant; hosted-service providers above a revenue threshold need a separate agreement; attribution for products >100M MAU or >US$20M monthly revenue). Kimi K2.7-Code uses a "Modified MIT" licence. | Verified fact | A5-S069, V2-S015 |
| Status events | January 2026: Kimi K2.5; July 2026: Kimi K3 open release | Reported | A5-S042, A5-S039, A5-S040 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Large multimodal agentic LLMs offered as open weights and via Moonshot's Kimi platform API. | Reported | A5-S040, A5-S038 |
| Stack position | L1 foundation model. | Architectural judgement |  |
| Integration | Kimi platform API (platform.kimi.ai per aggregator source links); open weights via SGLang, Xinference, ms-swift, Unsloth. | Reported | A5-S038, A5-S039, A5-S041 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | International API platform stores data on servers in Singapore; mainland platform keeps data in the PRC. Kimi API help page says API inputs/outputs are not used for training; the international privacy policy (30 April 2025) lists model training as a purpose (conflict). No EU residency option found. Bedrock offers Kimi K3 via US, India and global cross-Region profiles (no in-Region); Microsoft Foundry offers K3 via Fireworks pass-through (US Data Zone). | Verified fact | A5-S070, A5-S086, A5-S087 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Kimi K3 (Kimi API): US$3 input / US$15 output per 1M; cached input US$0.30; flat across 1M context; Kimi K3 (Bedrock global): US$3 / US$15 per 1M (aggregator) | Verified fact | A5-S069, A5-S038 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Amazon Bedrock, Microsoft Foundry, Google Cloud (K2-Thinking), SGLang, Xinference, ms-swift, Unsloth. | Reported | A5-S038, A5-S027, A5-S039, A5-S041, A5-S040, A5-S043 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Kimi platform API); managed_cloud: Yes (Bedrock Kimi K3 cross-Region profiles; Microsoft Foundry via Fireworks - inference on Fireworks GPUs outside customer tenant; Google Cloud K2-Thinking); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open weights); on_prem: Yes (open weights) | | |

# C1: AI / LLM gateway

## LiteLLM (Python SDK and LiteLLM Proxy / 'AI Gateway') (`C1-litellm`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: only as a hardened, pinned, Enterprise-licensed internal service, because the March 2026 compromise and fail-open defaults put security and maturity at 3 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading coverage of the C1 research questions: routing, fallback, budgets, rate limits, semantic cache, guardrail hooks, logging, LLM+MCP+A2A [VF: A6-S015] |
| Enterprise readiness | 4 | SSO, RBAC, SCIM and audit logs on the Enterprise tier, custom SLAs and named support channels [VF: A6-S007, A6-S051]; rule 2 lets an OSS product with commercial support exceed 4, but the licence gating keeps it at 4 |
| Security and compliance | 3 | SOC 2 Type 2 refreshed September 2026; ISO 27001 unconfirmed [VF: A6-S108]. Serious supply-chain incident in March 2026, remediated (CI/CD v2, cosign, Mandiant review) [VF: A6-S008, A6-S009]; held at 3 |
| Deployment flexibility | 4 | Self-hosted, customer-account (VPC) and hosted options verified [VF: A6-S007, A6-S022, A6-S051]; on-prem and air-gap not verified [NPV] |
| Ecosystem | 5 | De facto open interface (OpenAI format), 100+ providers, MCP, A2A, logging callbacks; used by AWS's Guidance [VF: A6-S015, A6-S022] |
| Reliability and maturity | 3 | Since July 2023 with very high cadence [VF: A6-S001], but a 2026 supply-chain compromise and fail-open defaults [VF: A6-S008, A6-S015] |
| Cost / TCO | 4 | Free to self-host; Enterprise licence priced on capacity (pricing description conflicts); database and Redis to operate [VF: A6-S007, A6-S015] |
| Lock-in / portability | 4 | MIT core and OpenAI-format API; enterprise features proprietary [VF: A6-S001, A6-S002]; no ownership change found |
| **Total (generic / FS)** | **4.05 / 3.90** | |

*Evidence rules applied:* Rule 2 basis: self-hosted open-core software with commercial support; NPV cap not applied

**Capabilities.** Open-core Python SDK and proxy exposing 100+ providers through an OpenAI-format API, with virtual keys, budgets per key/user/team/customer, TPM/RPM limits, fallbacks, exact and semantic caching, pre/during/post-call guardrail hooks and logging callbacks; the same proxy fronts MCP servers and A2A agents [VF: A6-S015, A6-S051].

**Strengths**

- Widest provider coverage and the de facto open-source gateway; basis of AWS's own multi-provider Guidance [VF: A6-S015, A6-S022] [AJ]
- One control plane for LLM, MCP and A2A traffic with shared auth, limits and spend tracking [VF: A6-S015]
- MIT core and OpenAI-format API keep the application exit cheap [VF: A6-S001, A6-S015] [AJ]

**Limitations and risks**

- PyPI supply-chain compromise on 24 March 2026 (1.82.7 and 1.82.8) via CI credentials; clean v1.83.0 released 30 March 2026 (US time) from a rebuilt pipeline [VF: A6-S008, A6-S009, V2-S027, V2-S028]
- Several controls fail open or are off by default: max_budget without a database, prompt-injection guardrails off, admin key bypasses budgets; A2A agents open to all callers until an allowlist is set [VF: A6-S015]
- SSO beyond 5 users, RBAC, SCIM and audit logs need the commercial licence; pricing model described inconsistently [VF: A6-S007]
- ISO 27001 recertification not confirmed [VF: A6-S108]

**Choose when**

- You want a self-hosted, provider-neutral gateway for LLM, MCP and A2A traffic and will run it as a hardened internal service [AJ]
- You will buy the Enterprise licence for SSO, RBAC and audit logs [AJ]

**Avoid when**

- You cannot pin versions, mirror packages and verify signed images [AJ]
- You would run the open edition without a database and accept fail-open budgets [AJ]

**Nearest competitors:** C1-kong-ai-gateway, C1-portkey, C1-agentgateway

**Regulated-FS note.** Treat as a Tier-1 internal service: install only from a private mirror with pinned hashes, deploy the cosign-signed images, run fail-closed configuration and buy Enterprise for audit evidence [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | BerriAI (PyPI author of litellm); no acquisition found in sources consulted | Verified fact | A6-S001 |
| Category | AI/LLM gateway (open-source proxy) that also acts as MCP gateway and A2A agent gateway | Verified fact | A6-S015, A6-S051 |
| Version / lineup | litellm 1.104.1 (PyPI, 7 October 2026; 1.105.0rc2 pre-release the same day); proprietary litellm-enterprise 0.1.74 (7 October 2026) | Verified fact | A6-S001, A6-S002, V2-S028 |
| Licence | Open core: core package MIT; enterprise features under the LiteLLM Commercial License, shipped as litellm-enterprise (LicenseRef-Proprietary) | Verified fact | A6-S001, A6-S002, A6-S051 |
| Status events | 24 March 2026: malicious litellm 1.82.7 and 1.82.8 published to PyPI using release credentials stolen via a compromised Trivy scanner in CI; quarantined after about 40 minutes per LiteLLM (Snyk reports an exposure window of about three hours); both versions are no longer listed on PyPI; 30 March 2026 (US time; PyPI upload 31 March 2026 05:08 UTC): v1.83.0 released as first build from rebuilt CI/CD v2 pipeline after forensic review with Mandiant and Veria Labs | Verified fact | A6-S008, A6-S009, A6-S010, V2-S027, V2-S028 |
| Strategic direction | Positions the proxy as one control plane for LLMs, MCP servers and A2A agents with shared auth, rate limiting and usage dashboard; v1.89.0 added A2A agent providers and per-MCP-server controls; after March 2026 incident moved to CI/CD v2 with ephemeral credentials and cosign-signed images | Verified fact | A6-S015, A6-S009, A6-S051 |
| What it does | Python SDK and proxy server that expose 100+ LLM providers through an OpenAI-format API, with virtual keys, budgets (key/user/team/customer), TPM/RPM limits, fallbacks, exact and semantic caching, guardrail hooks (pre-call, during-call, post-call) and logging callbacks; the same proxy fronts registered MCP servers and A2A agents with access control, cost tracking and guardrails. | Verified fact | A6-S015, A6-S051 |
| Stack position | Gateway/control plane between applications or agents and model providers, MCP tool servers and A2A agents. Absent from the graphic (L2 shows OpenRouter, a hosted router, not an enterprise gateway). | Verified fact | A6-S015 |
| Integration | OpenAI-compatible REST API; MCP endpoint (fixed endpoint for all registered MCP tools, OAuth passthrough with issuer-scoped JWT auth); A2A message/send and message/stream; logging callbacks (e.g. per-team Langfuse projects), log export to S3/GCS/Azure Blob; JWT/OIDC request auth | Verified fact | A6-S015, A6-S007 |
| Dependencies | Python >=3.10,<3.15; a database is required for global budgets and spend tracking; Redis, Valkey or Qdrant back semantic caching; official Docker images on GHCR | Verified fact | A6-S001, A6-S015, A6-S051 |
| Certifications | SOC 2 Type 2: updated report announced September 2026 (recertification with Vanta, independent auditor), available via trust.litellm.ai on request. ISO 27001: recertification announced March 2026; completion not confirmed (Data Privacy page lists only SOC 2 Type II) | Verified fact | A6-S108 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Docker images on GHCR signed with cosign from v1.83.0; virtual keys; guardrail framework applied across chat, embeddings, MCP and A2A routes (prompt-injection guardrails off by default); ISMS, regular vulnerability scans and a vulnerability disclosure policy | Verified fact | A6-S051, A6-S009, A6-S015, A6-S108 |
| Access controls | Admin UI SSO via Okta, Azure AD, Google Workspace or any OIDC/SAML IdP (free up to 5 users, then enterprise licence); RBAC, SCIM and audit logs of key/team/user/model changes in Enterprise tier | Verified fact | A6-S007 |
| Enterprise support | Enterprise tier: professional support via dedicated Discord/Slack, custom SLAs, feature prioritisation, custom integrations | Verified fact | A6-S051 |
| Pricing | Open-source proxy free to self-host. Enterprise: annual licence priced on gateway request capacity, deployment architecture and support ('never per token'); 30-day trial key by email. Docs Enterprise page instead describes usage-based pricing (conflict). | Verified fact | A6-S007 |
| Infrastructure cost | Self-hosted cost is container compute plus the database needed for budgets/spend and Redis/Valkey for caching and multi-instance rate limits | Verified fact | A6-S015 |
| Ecosystem | 100+ LLM providers; MCP and A2A; Langfuse and other logging callbacks; basis of AWS 'Guidance for Multi-Provider Generative AI Gateway on AWS' | Verified fact | A6-S015, A6-S022 |
| Adoption signals | About 3 to 3.4 million PyPI downloads per day (InfoQ and Trend Micro, March 2026) | Reported | A6-S010 |
| Maturity | First PyPI release 27 July 2023; very high release cadence (several releases on 7 October 2026 alone) | Verified fact | A6-S001 |
| Deployment | saas: Yes (hosted LiteLLM proxy referenced in README and Enterprise docs); managed_cloud: Not publicly verified; vpc_byoc: Yes (customer-account deployment pattern, e.g. AWS Guidance deploys LiteLLM on ECS/EKS); private_cloud: Not publicly verified; self_hosted: Yes (free to self-host; Docker images); on_prem: Not publicly verified | | |

## Kong AI Gateway (AI Gateway 2.x runtime in Kong Konnect; AI plugins in Kong Gateway 3.x) (`C1-kong-ai-gateway`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Kong is the API standard; cost (2) is a stated condition because pricing is not public [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading coverage across LLM, MCP and A2A, including guardrails, PII sanitisation and cost governance [VF: A6-S016, A6-S017] |
| Enterprise readiness | 4 | Konnect SSO (SAML or OIDC) with teams, predefined roles and IdP group mapping (B-REVA-S004), audit logs, Kong Identity principals and a 99.99% Konnect SLA (A6-S109, A6-S016, A6-S018): all three controls plus SLA reach 4 under rule 7 |
| Security and compliance | 4 | ISO 27001:2022 and SOC 2 Type II both naming AI Gateway; PCI DSS for Konnect [VF: A6-S109]; no CMK, ISO 42001 or FedRAMP evidence, so not 5 |
| Deployment flexibility | 4 | Konnect SaaS, Dedicated Cloud Gateways, hybrid and self-managed [VF: A6-S018]; on-prem and air-gap not verified [NPV] |
| Ecosystem | 4 | Large API-gateway ecosystem; AWS SigV4, Foundry, SageMaker and NeMo integrations [VF: A6-S017, A6-S016] |
| Reliability and maturity | 3 | AI plugins since 3.6 (2024) but AI Gateway 2.0 GA only on 1 September 2026, with a configuration-model change [VF: A6-S016, A6-S017, V2-S034] |
| Cost / TCO | 2 | Pricing 'contact sales'; advanced plugins licence-gated [VF: A6-S017, A6-S018] |
| Lock-in / portability | 3 | Apache-2.0 OSS core, but 2.x runtime and advanced plugins licence-gated [VF: A6-S017] |
| **Total (generic / FS)** | **3.85 / 3.80** | |

**Capabilities.** AI gateway for LLM, MCP and A2A traffic on Kong's API platform: multi-provider routing and load balancing, token budgets and rate limits, semantic caching, semantic prompt/response guards, PII sanitisation, cloud guardrail and NeMo Guardrails integrations, MCP access control and tool filtering; AI Gateway 2.x is a dedicated runtime in Konnect [VF: A6-S016, A6-S017].

**Strengths**

- Broad AI policy set on an enterprise API-gateway estate many firms already run [VF: A6-S016] [AJ]
- Product-scoped SOC 2 Type II and ISO 27001:2022 covering AI Gateway [VF: A6-S109]
- Tracks the MCP 2026-07-28 revision and offers per-caller MCP tool exposure [VF: A6-S017, A6-S016]
- Konnect organisation SSO (SAML or OIDC), teams and roles with IdP group mapping [VF: B-REVA-S004]

**Limitations and risks**

- Configuration model changed from 3.x plugins to 2.x entities; migration needed before 3.18 [VF: A6-S016, A6-S017]
- Advanced AI plugins and AI Gateway 2.x are licence-gated or Konnect-delivered [VF: A6-S017]
- Pricing not published [VF: A6-S017, A6-S018]

**Choose when**

- Kong is already your API gateway standard [AJ]
- You need product-scoped certifications for the gateway itself [AJ]

**Avoid when**

- You want a free, self-hosted gateway with no licence dependency [AJ]
- You cannot plan the 3.x-to-2.x migration in the next year [AJ]

**Nearest competitors:** C1-litellm, C1-google-apigee-ai-gateway, C1-azure-apim-ai-gateway

**Regulated-FS note.** Prefer the hybrid mode (customer-run data plane) so prompts and logs stay in region; confirm audit-log export on Konnect [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Kong Inc. | Verified fact | A6-S016 |
| Category | AI gateway (LLM, MCP and A2A traffic) built on an API gateway vendor's platform | Verified fact | A6-S016, A6-S017 |
| Version / lineup | AI Gateway 2.0 GA on 1 September 2026; 2.1.0 (22 September 2026) and 2.2.0 (30 September 2026); AI plugins supported on Kong Gateway 3.14 LTS (3.14.0.0, 7 April 2026) | Verified fact | A6-S016, A6-S017, V2-S034 |
| Licence | Open core: Kong Gateway OSS (Apache-2.0) with basic AI plugins released as open source in 3.6; advanced AI plugins (e.g. AI Proxy Advanced) require an AI/Enterprise licence; AI Gateway 2.x delivered via Konnect | Verified fact | A6-S017, A6-S018 |
| Status events | 1 September 2026: Kong AI Gateway 2.0 GA as a dedicated runtime (configuration moves from plugins to AI Model Provider/AI Model entities) | Verified fact | A6-S016, A6-S017, V2-S034 |
| Strategic direction | Separate AI runtime with its own control plane, admin API and release cadence for LLM, MCP and agent workloads; MCP Server Bundling, principal-aware AI traffic policies via Kong Identity, modality-aware cost governance; migration from 3.x plugins recommended before 3.18 | Verified fact | A6-S016, A6-S017 |
| What it does | Governs LLM, MCP and A2A traffic: multi-provider routing and load balancing, token budgeting and rate limiting, semantic caching, semantic prompt/response guards, PII sanitisation, integrations with cloud guardrail services and NVIDIA NeMo Guardrails, MCP access control and tool filtering, A2A traffic management. | Verified fact | A6-S016, A6-S017 |
| Stack position | Gateway/control plane; extends an existing enterprise API gateway estate to AI traffic | Verified fact | A6-S016 |
| Integration | Gateway plugins/entities; supports MCP protocol revision 2026-07-28 (2.1.0); AWS SigV4 upstream auth for Bedrock AgentCore; providers incl. Microsoft Foundry, Amazon SageMaker, Kimi | Verified fact | A6-S016, A6-S017 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | ISO/IEC 27001:2022 certificate LC-516-21 (Linford & Company, issued 1 September 2026, valid to 31 August 2029) covering the API and AI Connectivity Platform; SOC 2 Type II (security, availability, confidentiality) covering Konnect, Dedicated Cloud Gateways, Kong Gateway Enterprise, Kong AI Gateway, Kong Mesh, Insomnia; PCI DSS v4.0.1 (Konnect, Dedicated Cloud Gateways); CSA STAR Level 1 self-assessment | Verified fact | A6-S109 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Konnect and Dev Portal audit logs; Kong Identity principals usable in AI Gateway policies | Verified fact | A6-S109, A6-S016 |
| Enterprise support | 99.99% SLA advertised for Konnect cloud | Verified fact | A6-S018 |
| Pricing | Not published in sources consulted beyond 'Contact sales'/consumption model; AI Gateway paid plugins listed as add-on or included depending on tier | Verified fact | A6-S017, A6-S018 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Series E of US$175m at US$2bn valuation (date not verified); total equity raised estimated at US$345m (Sacra) | Reported | A6-S018 |
| Maturity | AI plugins since Kong Gateway 3.6 (2024); AI Gateway 2.x GA since 1 September 2026 | Verified fact | A6-S016, A6-S017 |
| Deployment | saas: Yes (Konnect managed control plane); managed_cloud: Yes (Dedicated Cloud Gateways on AWS, Azure or GCP); vpc_byoc: Yes (hybrid: Kong-run control plane, customer-run data plane); private_cloud: Not publicly verified; self_hosted: Yes (fully self-managed gateways); on_prem: Not publicly verified | | |

## Apigee (API management) used as an AI gateway (`C1-google-apigee-ai-gateway`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud or Apigee is already the API standard (CP3 Q2, rubric rule 10); lock-in at 2 is the stated condition [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Token limits, semantic cache, routing with circuit breaking, auditing, Model Armor, MCP, A2A [VF: A6-S024, A6-S023] |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1); access-control detail not in the fact base [NPV]; confirm per service |
| Security and compliance | 4 | Apigee named in Google Cloud SOC 2 and ISO/IEC 27001 scope [VF: A6-S070, A6-S071]; CMK not verified, so not 5 |
| Deployment flexibility | 4 | Apigee X SaaS and Apigee hybrid self-managed runtime [VF: A6-S069, A6-S025] |
| Ecosystem | 4 | OAuth/JWT, MCP, A2A, AP2, multicloud routing [VF: A6-S024] |
| Reliability and maturity | 4 | Mature API management; AI and MCP features added 2025–26 [VF: A6-S023, A6-S025] |
| Cost / TCO | 3 | Transparent pay-as-you-go per call, with paid analytics and security add-ons [VF: A6-S069] |
| Lock-in / portability | 2 | Proprietary policy model [VF: A6-S024] |
| **Total (generic / FS)** | **3.80 / 3.65** | |

*Evidence rules applied:* enterprise_readiness set to 4 under the hyperscaler presumption (CP2 Q1): platform controls presumed; confirm per service

**Capabilities.** Apigee API management marketed as an AI gateway: token limits and monitoring, semantic caching, multicloud model routing with circuit breaking, LLM auditing and logging, Model Armor screening, MCP (GA 31 March 2026) and A2A support; SaaS or hybrid self-managed runtime [VF: A6-S024, A6-S023, A6-S025].

**Strengths**

- Mature API-management product with product-scoped SOC 2 and ISO 27001 [VF: A6-S070, A6-S071]
- Hybrid runtime gives a customer-run data plane [VF: A6-S025]
- Inline Model Armor screening [VF: A6-S024]

**Limitations and risks**

- Proprietary policy model [VF: A6-S024]
- Per-call pricing plus add-ons for analytics and security [VF: A6-S069]
- Semantic cache needed an SSRF fix on 30 September 2026 [VF: A6-S025]

**Choose when**

- Google Cloud is primary, or Apigee is already your API standard [AJ]
- You want the gateway data plane in your own Kubernetes (hybrid) [AJ]

**Avoid when**

- You want a light, low-cost model gateway with no API-management estate [AJ]

**Nearest competitors:** C1-azure-apim-ai-gateway, C1-kong-ai-gateway, C1-litellm

**Regulated-FS note.** Run hybrid in a UK or EU region and confirm residency of LLM audit logs; keep semantic caching off for client-specific routes [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google Cloud | Verified fact | A6-S024 |
| Category | Cloud API management platform with AI gateway policies (LLM, MCP, A2A) | Verified fact | A6-S024 |
| Version / lineup | Apigee X (SaaS) and Apigee hybrid 1.17 (1.17.1 on 30 September 2026); Apigee MCP support GA 31 March 2026; API hub MCP server GA 24 July 2026 | Verified fact | A6-S023, A6-S025 |
| Licence | Proprietary managed service (hybrid runtime self-managed) | Verified fact | A6-S069 |
| Strategic direction | Apigee marketed as the AI gateway for agentic AI: supports SSE and JSON-RPC for MCP, A2A and AP2; multicloud model routing; MCP server and MCP transcoding; Model Armor integration | Verified fact | A6-S024 |
| What it does | Token limit enforcement and token consumption monitoring, semantic caching, multicloud model routing with circuit breaking, LLM auditing and logging, API keys/OAuth 2.0/JWT, quotas, Model Armor prompt/response screening, exposing existing APIs as MCP tools. | Verified fact | A6-S024, A6-S023 |
| Stack position | Gateway/control plane for AI traffic in Google Cloud and multicloud estates | Verified fact | A6-S024 |
| Integration | Apigee proxies and policies; extension processor applies policies to traffic that bypasses a proxy; MCP endpoints (hybrid 1.17) | Verified fact | A6-S023, A6-S025 |
| Dependencies | Model Armor for prompt/response screening; vector search index and embeddings for semantic cache | Verified fact | A6-S023, A6-S024 |
| Certifications | Apigee listed in Google Cloud SOC 2 and ISO/IEC 27001 scope | Verified fact | A6-S070, A6-S071 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Pay-as-you-go: Standard proxy US$20 per 1M calls (up to 50M), Extensible proxy US$100 per 1M calls (up to 50M), tiered down at volume; API Analytics add-on US$20 per 1M calls; Advanced API Security US$350 per 1M calls; subscription tiers also offered | Verified fact | A6-S069 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Mature API management product; AI-specific policies and MCP support added 2025-2026 | Verified fact | A6-S023, A6-S025 |
| Deployment | saas: Yes (Apigee on Google Cloud); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Apigee hybrid runtime); on_prem: Not publicly verified | | |

## Portkey AI Gateway, now branded 'Prisma AIRS AI Gateway' (Palo Alto Networks) (`C1-portkey`)

**Tier:** Tactical · **Flags:** Acquired, Renamed · **Original graphic label:** not in graphic

*Rationale:* Tactical: capable, but ownership and branding changed four months ago and the post-acquisition commercial terms are not public [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Routing, fallback, budgets, guardrails, MCP gateway [VF: A6-S049, A6-S014]; A2A not evidenced [NPV] |
| Enterprise readiness | 4 | SSO/SAML 2.0, SCIM, organisation and workspace roles and organisation-wide audit logs (B-C1-S001, B-C1-S002), with IdP group mapping in the docs changelog (B-C1-S003): all three controls plus SCIM reach 4 under rule 7 (CP3 review A, consistent with Firecrawl); condition: evidence is mainly vendor pages and post-acquisition terms are not public |
| Security and compliance | 3 | SOC 2 Type 2, ISO 27001, GDPR and HIPAA claimed, tier coverage unclear [VF: A6-S013]; scope rule (CP2 Q4) applied |
| Deployment flexibility | 4 | SaaS, VPC, private cloud and self-hosted OSS; air-gap no longer offered [VF: A6-S013, A6-S049] |
| Ecosystem | 4 | OpenAI-compatible API and SDKs, 1,600+ models, MCP, Cloudflare Workers [VF: A6-S049] |
| Reliability and maturity | 3 | Acquired May 2026; Prisma AIRS AI Gateway GA 16 July 2026 [VF: V2-S048]; OSS Gateway 2.0 pre-release [VF: A6-S049] |
| Cost / TCO | 3 | Published tiers (free, US$49/month Production, custom Enterprise) may be stale; post-acquisition pricing not verified [VF: A6-S013] |
| Lock-in / portability | 3 | MIT core reduces lock-in, but governance features are proprietary; ownership change minus 1 (rule 3) [VF: A6-S050, A6-S011] |
| **Total (generic / FS)** | **3.60 / 3.50** | |

*Evidence rules applied:* enterprise_readiness: NPV cap lifted by verified SSO, roles, audit logs and SCIM (rule 7)

**Capabilities.** AI gateway routing to 1,600+ models with fallbacks, retries, load balancing, caching, budgets, guardrails and logging, plus an MCP Gateway with a single auth layer; now Palo Alto Networks' Prisma AIRS AI Gateway [VF: A6-S049, A6-S011, A6-S014].

**Strengths**

- Mature routing and fallback configuration as JSON Configs, with guardrails in the same config [VF: A6-S049]
- MIT open-source gateway with a pre-release Gateway 2.0 that merges enterprise gateway code into open source [VF: A6-S049, A6-S050]
- Now sits inside a security vendor's runtime-inspection platform [VF: A6-S011]

**Limitations and risks**

- Acquired by Palo Alto Networks, completed 29 May 2026; US$117m per the 10-K [VF: A6-S012, V2-S025]; roadmap now tied to Prisma AIRS [VF: A6-S011]
- Certifications claimed on pricing pages with unclear tier coverage; pricing page possibly stale [VF: A6-S013]
- Gateway 2.0 is pre-release; fully air-gapped deployment no longer offered [VF: A6-S049, A6-S013]
- Access-control evidence comes largely from marketing pages [VF: B-C1-S001, B-C1-S002]

**Choose when**

- You already run Prisma AIRS and want gateway and runtime inspection from one security vendor [AJ]
- You want a managed gateway with VPC or private-cloud options [VF: A6-S013] [AJ]

**Avoid when**

- You need vendor-neutral governance of the traffic path, or air-gapped deployment [AJ]
- You cannot absorb a contract re-papering after the change of control [AJ]

**Nearest competitors:** C1-litellm, C1-kong-ai-gateway, C1-cloudflare-ai-gateway

**Regulated-FS note.** Refresh third-party due diligence and the DORA register entry after the change of control; confirm which certifications cover the Prisma AIRS-branded service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Palo Alto Networks (acquired Portkey, Inc.; completed 29 May 2026) | Verified fact | A6-S011, A6-S012, V2-S025 |
| Category | AI gateway (LLM gateway plus MCP gateway) with guardrails, observability and governance | Verified fact | A6-S049, A6-S014 |
| Version / lineup | Open-source gateway on GitHub with 'Gateway 2.0 (Pre-Release)' that merges Portkey's core enterprise gateway into open source; Prisma AIRS AI Gateway described by PANW as generally available | Verified fact | A6-S049, A6-S011 |
| Licence | Open core: open-source gateway MIT (Copyright 2024 Portkey, Inc.); hosted and enterprise platform proprietary | Verified fact | A6-S050, A6-S013 |
| Status events | 30 April 2026: Palo Alto Networks announced intent to acquire Portkey; 29 May 2026: acquisition completed; FY2026 Form 10-K reports total purchase consideration of US$117m (10-Q had stated US$140m incl. replacement awards); 2026: product documentation retitled 'Portkey (Prisma AIRS AI Gateway)' | Verified fact | A6-S011, A6-S012, A6-S014, V2-S025, V2-S048 |
| Strategic direction | Becoming the AI gateway inside PANW's Prisma AIRS platform, inspecting AI traffic at runtime and enforcing security and governance policy for agents; core enterprise gateway being merged into open source with Gateway 2.0 | Verified fact | A6-S011, A6-S049 |
| What it does | Routes requests to 1,600+ models through one API with fallbacks, retries, load balancing, timeouts, caching, budgets/quotas, guardrails and logging; MCP Gateway gives a single auth layer, access control and observability for agent-to-tool connections. | Verified fact | A6-S049, A6-S011, A6-S014 |
| Stack position | Gateway/control plane in the traffic path between applications or agents and model providers and MCP servers; now also a security enforcement point for PANW | Verified fact | A6-S011 |
| Integration | OpenAI-compatible API and SDKs; JSON 'Configs' for routing rules, retries and input/output guardrails; MCP Gateway | Verified fact | A6-S049 |
| Dependencies | Open-source gateway runs on Node.js (npx), Docker or Cloudflare Workers | Verified fact | A6-S049 |
| Certifications | SOC 2 Type 2, ISO 27001, GDPR and HIPAA claimed on Portkey enterprise/pricing pages; tier coverage unclear | Verified fact | A6-S013 |
| GDPR / residency | GDPR compliance claimed; custom BAAs and data isolation on Enterprise; EU processing region not verified | Verified fact | A6-S013 |
| Security features | Data isolation and export to customer data lakes (Enterprise); runtime inspection of AI traffic under Prisma AIRS | Verified fact | A6-S013, A6-S011 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Developer: free (10k recorded logs/month, 3-day retention). Production: US$49/month (100k requests; US$9 per extra 100k up to 3M). Enterprise: custom. Post-acquisition pricing under Prisma AIRS not verified. | Verified fact | A6-S013 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | 1,600+ language, vision, audio and image models; MCP servers; deployable on Cloudflare Workers | Verified fact | A6-S049 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Prisma AIRS AI Gateway described as generally available; open-source Gateway 2.0 still pre-release | Verified fact | A6-S011, A6-S049 |
| Deployment | saas: Yes (hosted gateway / managed SaaS); managed_cloud: Not publicly verified; vpc_byoc: Yes (VPC hosting on Enterprise plan); private_cloud: Yes (private cloud deployment on Enterprise plan); self_hosted: Yes (open-source gateway); on_prem: No for fully air-gapped deployment ('No Longer Offered' in feature comparison) | | |

## agentgateway (`C1-agentgateway`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Tactical: the most neutral governance in the layer, but young and with unverified hygiene [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | LLM, MCP and A2A gateway with budgets, failover and OAuth [VF: A6-S061]; caching and guardrail depth not verified [NPV] |
| Enterprise readiness | 3 | Rule 2: OAuth on MCP and a commercial enterprise distribution with audit tooling [VF: A6-S061, B-C1-S010] |
| Security and compliance | 2 | Rule 2 hygiene (security policy, CVE handling, signed releases) not verified [NPV] |
| Deployment flexibility | 4 | Self-hosted [VF: A6-S061]; enterprise distribution from Solo [VF: B-C1-S010] |
| Ecosystem | 3 | OpenAI-compatible, MCP, A2A, OpenAPI; multi-vendor contributors [VF: A6-S061, B-C1-S009] |
| Reliability and maturity | 3 | 1.x line, v1.6.0 on 2 October 2026; foundation-hosted since August 2025 [VF: A6-S062, B-C1-S009] |
| Cost / TCO | 4 | Free open source; operations cost is your own [VF: A6-S061] |
| Lock-in / portability | 5 | Apache-2.0 with neutral governance [VF: A6-S061, B-C1-S009] |
| **Total (generic / FS)** | **3.40 / 3.45** | |

*Evidence rules applied:* Rule 2 basis: self-hosted open-source software; NPV cap not applied; commercial support exists (B-C1-S010)

**Capabilities.** Open-source proxy for agent-to-LLM, agent-to-tool and agent-to-agent traffic: OpenAI-compatible routing with budget and spend controls, load balancing and failover, MCP federation with OAuth, and an A2A gateway [VF: A6-S061].

**Strengths**

- Apache-2.0 under vendor-neutral foundation governance [VF: A6-S061, B-C1-S009]
- Covers LLM, MCP and A2A in one data plane [VF: A6-S061]
- Commercial distribution and support exist (Solo Enterprise for agentgateway) [VF: B-C1-S010]

**Limitations and risks**

- Security hygiene (policy, signed releases) and access-control detail not verified [NPV]
- Current foundation home reported differently (Linux Foundation vs Agentic AI Foundation) [VF: B-C1-S009]
- Adoption not verified [NPV]

**Choose when**

- You want a neutral, open-source gateway for MCP and A2A traffic in Kubernetes estates [AJ]

**Avoid when**

- You need certified SaaS or turnkey cost attribution today [AJ]

**Nearest competitors:** C1-litellm, C1-envoy-ai-gateway, C1-kong-ai-gateway

**Regulated-FS note.** Pilot for MCP and A2A traffic with the enterprise distribution, and verify its release-signing and CVE process before production [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | agentgateway project, a Linux Foundation project | Verified fact | A6-S061 |
| Category | Open-source AI-native proxy: LLM gateway, MCP gateway and A2A gateway | Verified fact | A6-S061 |
| Version / lineup | v1.6.0 (2 October 2026) | Verified fact | A6-S062, V2-S061 |
| Licence | Open source (Apache-2.0) | Verified fact | A6-S061 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Proxy providing security, observability and governance for agent-to-LLM, agent-to-tool and agent-to-agent traffic: OpenAI-compatible LLM routing with budget and spend controls, load balancing and failover; MCP tool federation over stdio/HTTP/SSE/Streamable HTTP with OAuth; A2A gateway. | Verified fact | A6-S061 |
| Stack position | Gateway/control plane spanning model, tool and agent traffic | Verified fact | A6-S061 |
| Integration | OpenAI-compatible API, MCP, A2A, OpenAPI integration | Verified fact | A6-S061 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source | Verified fact | A6-S061 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | 1.x release line; latest v1.6.0 on 2 October 2026 | Verified fact | A6-S062 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Not publicly verified | | |

## AI gateway in Azure API Management (plus the AI Gateway tier, preview) (`C1-azure-apim-ai-gateway`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Azure is your primary cloud (CP3 Q2, rubric rule 10), using the GA AI gateway policies in existing APIM tiers, not the preview AI Gateway tier (no SLA); lock-in 2 is accepted under rule 11 because the condition is an existing platform commitment [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Token limits, metrics, semantic cache, load balancing, circuit breaking, content safety on LLM/MCP/A2A [VF: A6-S053, A6-S020] |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1): platform controls presumed; Entra sign-in and caller-keyed limits verified [VF: A6-S020, A6-S053]; confirm per service |
| Security and compliance | 4 | FedRAMP High audit scope names API Management [VF: A6-S056]; Azure ISO 27001 and SOC 2 are platform-level without naming the service [VF: B-C1-S007, B-C1-S008]; scope rule applied, so 4 |
| Deployment flexibility | 2 | Managed Azure service only in the fact base; preview tier in two regions [VF: A6-S053, A6-S020]; self-hosted gateway not verified [NPV] |
| Ecosystem | 4 | OpenAI-compatible unified API (preview), Anthropic Messages API, Foundry, MCP and A2A import [VF: A6-S053] |
| Reliability and maturity | 3 | Core LLM policies GA; tier and unified API preview without SLA [VF: A6-S020, A6-S053] |
| Cost / TCO | 3 | Preview tier free; classic tier prices not verified [VF: A6-S020] [NPV] |
| Lock-in / portability | 2 | APIM-specific policy XML and Azure dependency [VF: A6-S053] |
| **Total (generic / FS)** | **3.40 / 3.25** | |

*Evidence rules applied:* enterprise_readiness set to 4 under the hyperscaler presumption (CP2 Q1): platform controls presumed; confirm per service

**Capabilities.** AI gateway policies in Azure API Management: token limits and quotas per consumer, token metrics, semantic caching, load balancing and circuit breaking, Content Safety (incl. Prompt Shields) on LLM, MCP and A2A traffic, MCP exposure and governance, OAuth via credential manager; plus a dedicated AI Gateway tier in preview [VF: A6-S053, A6-S020].

**Strengths**

- Extends an API gateway many Azure estates already operate; Microsoft calls it 'not a separate offering' [VF: A6-S053]
- Content safety applies to MCP tool-call arguments and A2A payloads, not only prompts [VF: A6-S020]
- API Management is in Azure FedRAMP High audit scope [VF: A6-S056]

**Limitations and risks**

- AI Gateway tier is preview: East US 2 and Sweden Central only, free, no SLA [VF: A6-S020, V2-S073]
- Policies are APIM-specific XML [VF: A6-S053]
- Classic tier pricing and self-hosted options not verified [NPV]

**Choose when**

- Azure is your primary cloud and APIM your API standard [AJ]
- You want content safety enforced on tool and agent traffic at the gateway [AJ]

**Avoid when**

- You need the AI Gateway tier in production now (no SLA) [AJ]
- Your multi-cloud exit plan needs a gateway outside any one hyperscaler [AJ]

**Nearest competitors:** C1-google-apigee-ai-gateway, C1-kong-ai-gateway, C1-litellm

**Regulated-FS note.** Use the GA policies in existing tiers for production; do not place regulated traffic on the preview tier; keep policy logic documented so it can be re-expressed elsewhere [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Microsoft | Verified fact | A6-S053 |
| Category | Cloud-native API management platform with AI gateway policies (LLM, MCP and A2A) | Verified fact | A6-S053 |
| Version / lineup | Policy-based AI gateway available across APIM tiers (doc dated 29 May 2026); AI Gateway tier in public preview since about late July 2026; unified model API (preview) | Verified fact | A6-S053, A6-S020, V2-S073 |
| Licence | Proprietary managed Azure service | Verified fact | A6-S053 |
| Strategic direction | Extends APIM to govern models from Foundry, OpenAI-compatible third parties, Anthropic and Google Vertex AI, MCP servers and A2A agents; integration into Microsoft Foundry as its AI gateway control plane (preview) | Verified fact | A6-S053, A6-S020 |
| What it does | Token limit and quota policies per consumer key, token metrics, semantic caching (Azure Managed Redis), load balancing and circuit breaking across AI backends, content safety checks via Azure AI Content Safety (incl. Prompt Shields) on LLM, MCP and A2A traffic, exposing REST APIs as MCP servers and governing existing MCP servers, OAuth via credential manager. | Verified fact | A6-S053, A6-S020 |
| Stack position | Extension of APIM's existing API gateway, 'not a separate offering'; control plane for AI traffic in Azure estates | Verified fact | A6-S053 |
| Integration | Policy XML (e.g. llm-token-limit), OpenAI-compatible unified model API (preview), Anthropic Messages API (v2 tiers), MCP and A2A API import | Verified fact | A6-S053 |
| Dependencies | Azure API Management instance; Azure Managed Redis (or RediSearch-compatible cache) and an embeddings deployment for semantic caching; Azure AI Content Safety for moderation; Application Insights for metrics | Verified fact | A6-S053, A6-S020 |
| Certifications | API Management is in Azure FedRAMP High and DoD IL2 audit scope (Azure public, list updated February 2026) | Verified fact | A6-S056 |
| GDPR / residency | AI Gateway tier preview limited to East US 2 and Sweden Central regions | Verified fact | A6-S020 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Microsoft Entra ID sign-in required for AI Gateway tier quickstart; token limits keyed on subscription, IP or caller identity; OAuth for MCP via credential manager | Verified fact | A6-S020, A6-S053 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | AI Gateway tier free during public preview, pricing to be announced; classic APIM tier pricing not verified | Verified fact | A6-S020 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Core LLM policies GA; AI Gateway tier and unified model API in preview with no SLA | Verified fact | A6-S020, A6-S053 |
| Deployment | saas: Yes (managed Azure service); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Amazon Bedrock AgentCore Gateway (plus 'Guidance for Multi-Provider Generative AI Gateway on AWS') (`C1-aws-agentcore-gateway`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where AWS is your primary cloud (CP3 Q2, rubric rule 10), as the gateway for MCP and tool traffic. Maturity 2 is a stated condition: keep model routing on a gateway with GA inference routing until AWS states GA and Regions for inference targets. Same tier as L4-aws-agentcore-gateway-identity [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Strong MCP gateway and policy; LLM routing new with no GA wording; no semantic cache evidenced [VF: A6-S074, A6-S105] [NPV] |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1); IAM/JWT auth and principal rules verified [VF: A6-S074]; confirm per service |
| Security and compliance | 4 | AgentCore in SOC 1/2/3 scope (July 2026) and assessed for ISO/IEC 27001 (February 2026) [VF: B-C1-S004, B-C1-S005, B-C1-S006]; CMK for the token vault [VF: A6-S074]. Held at 4, not 5: the ISO evidence is a partly garbled search extract and FedRAMP status conflicts |
| Deployment flexibility | 2 | Managed AWS service only; Gateway regional list not verified [VF: A6-S021, A6-S026] |
| Ecosystem | 3 | MCP-native; Kong SigV4 and Entra Agent ID integrations [VF: A6-S016, A6-S058] |
| Reliability and maturity | 2 | AgentCore GA October 2025; inference targets and token limits announced 6 August 2026 without GA wording [VF: A6-S021, A6-S106] |
| Cost / TCO | 4 | US$0.005 per 1,000 invocations and similar unit prices [VF: A6-S021] |
| Lock-in / portability | 2 | AWS-specific control plane and IAM [VF: A6-S074] |
| **Total (generic / FS)** | **3.10 / 3.00** | |

*Evidence rules applied:* enterprise_readiness set to 4 under the hyperscaler presumption (CP2 Q1): platform controls presumed; confirm per service

**Capabilities.** Managed gateway that turns APIs, Lambda functions and MCP servers into MCP tools behind one endpoint, with IAM or JWT inbound auth, request/response interceptors, Cedar policy enforcement and, newly, inference targets that route to LLM providers with token-aware rate limits; AWS has no product named 'AI gateway' [VF: A6-S021, A6-S074, A6-S105, A6-S026].

**Strengths**

- Strongest policy model for tool calls: deny-by-default Cedar policies with decisions logged to CloudWatch [VF: A6-S026]
- Tracks MCP 2026-07-28 [VF: A6-S021]
- Low, transparent per-invocation pricing [VF: A6-S021]

**Limitations and risks**

- No explicit GA statement or regional list for inference targets; documentation conflicts on multi-target selection [VF: A6-S105, A6-S106]
- Fast-moving API surface (171 control-plane operations) [VF: A6-S074]
- AWS-specific control plane [VF: A6-S074]

**Choose when**

- You run agents on AWS and need governed MCP tool access with policy enforcement [AJ]

**Avoid when**

- You need a mature multi-provider LLM gateway today; use AWS's LiteLLM-based Guidance or another C1 product for model traffic [VF: A6-S022] [AJ]

**Nearest competitors:** C1-litellm, C1-kong-ai-gateway, C1-agentgateway

**Regulated-FS note.** Use it for tool traffic first; keep model routing on a gateway with GA inference routing until AWS states GA and regions for inference targets [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Amazon Web Services | Verified fact | A6-S021 |
| Category | Managed agent/MCP gateway with emerging LLM inference routing; plus a LiteLLM-based reference pattern | Verified fact | A6-S021, A6-S074, A6-S022 |
| Version / lineup | AgentCore GA October 2025; Gateway supports MCP versions 2026-07-28, 2025-11-25, 2025-06-18, 2025-03-26; inference targets documented (connectors for bedrock-mantle, openai, anthropic; provider configs for OpenAI-compatible endpoints); token-based rate limiting announced 6 August 2026 | Verified fact | A6-S021, A6-S105, A6-S106, A6-S074 |
| Licence | Proprietary managed service (Guidance pattern uses open-source LiteLLM, MIT) | Verified fact | A6-S021, A6-S022 |
| Strategic direction | AgentCore Gateway is growing from an MCP tool gateway into a combined tool and model gateway: inference targets route to LLM providers; rate limits cover request rates, token consumption and concurrency; rules give principal-based access control and routing; Policy engines (Cedar) authorise every tool call | Verified fact | A6-S074, A6-S026 |
| What it does | Turns APIs (OpenAPI, Smithy), Lambda functions and existing MCP servers into MCP tools behind one endpoint with inbound auth (custom JWT, IAM) and outbound credentials via AgentCore Identity, semantic tool search, request/response interceptors and policy enforcement; can route to LLM providers via inference targets. Inference targets expose an /inference path usable with the OpenAI or Anthropic SDK (route by model field; 'target/model' pins a provider); rate limits cover requests, tokens per minute (estimated up front, reconciled with provider usage) and connections, scoped by JWT claims, IAM  | Verified fact | A6-S021, A6-S074, A6-S026, A6-S105 |
| Stack position | Combined tool (MCP) and model (inference) gateway in the AWS agent stack; the LiteLLM-based Guidance remains AWS's published multi-provider gateway pattern | Verified fact | A6-S105, A6-S022 |
| Integration | MCP (protocol type MCP); authoriser types CUSTOM_JWT, AWS_IAM, NONE, AUTHENTICATE_ONLY; interception points REQUEST/RESPONSE; MCP target types OpenAPI schema, Smithy model, Lambda, MCP server, API Gateway, connector | Verified fact | A6-S074 |
| Dependencies | AWS account; AgentCore Identity for credentials; optional AgentCore Policy engine; Guidance pattern uses ECS/EKS, ALB, WAF, CloudFront/Route 53 | Verified fact | A6-S021, A6-S022, A6-S074 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | AgentCore Policy GA in 13 regions incl. Europe (Ireland); Gateway regional list not verified | Verified fact | A6-S026 |
| Security features | Customer-managed KMS key for AgentCore token vault (SetTokenVaultCMK API); policy decisions logged to CloudWatch | Verified fact | A6-S074, A6-S026 |
| Access controls | IAM or custom JWT inbound auth; gateway rules keyed on IAM principals; Cedar policy engine with default deny on tool calls | Verified fact | A6-S074, A6-S026 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Gateway: US$0.005 per 1,000 API invocations (ListTools, InvokeTool, Ping); US$0.025 per 1,000 Search API calls; US$0.02 per 100 tools indexed per month; data egress to customer VPC US$0.006/GB | Verified fact | A6-S021 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Kong AI Gateway 2.0 adds SigV4 auth for Bedrock AgentCore endpoints; Microsoft Entra Agent ID documents securing Bedrock agents | Verified fact | A6-S016, A6-S058 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | AgentCore GA October 2025; inference targets documented and token rate limiting announced 6 August 2026, but no explicit GA statement or regional list for inference targets was found; docs conflict on multi-target selection (round-robin vs random) | Verified fact | A6-S021, A6-S105, A6-S106 |
| Deployment | saas: Yes (managed AWS service); managed_cloud: Not publicly verified; vpc_byoc: Guidance pattern deploys into the customer's own AWS account (ECS/EKS); private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Agent Router (formerly Envoy AI Gateway) (`C1-envoy-ai-gateway`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** not in graphic

*Rationale:* Tactical: sound plumbing for Envoy estates, but narrower than the leaders and with unverified hygiene [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Routing, quotas, failover, credentials and attribution for LLM and MCP [VF: A6-S063]; guardrails and caching not verified [NPV] |
| Enterprise readiness | 2 | Rule 2: Tier One gateway centralises auth and rate limits [VF: A6-S063]; RBAC and audit not verified; no commercial support offer verified beyond a listed 'Tetrate Agent Router Service' provider [VF: A6-S063] |
| Security and compliance | 2 | Rule 2 hygiene not verified [NPV] |
| Deployment flexibility | 3 | Self-hosted on Kubernetes only [VF: A6-S063] |
| Ecosystem | 3 | Envoy ecosystem; OpenAI-compatible API [VF: A6-S063] |
| Reliability and maturity | 3 | 1.x line, v1.2.0 on 6 October 2026; renamed and moved in 2026 [VF: A6-S064, V2-S029] |
| Cost / TCO | 4 | Free open source; Kubernetes operations [VF: A6-S063] |
| Lock-in / portability | 5 | Apache-2.0, neutral foundation [VF: A6-S063] |
| **Total (generic / FS)** | **2.90 / 3.00** | |

*Evidence rules applied:* Rule 2 basis: self-hosted open-source software; NPV cap not applied

**Capabilities.** Agent Router (formerly Envoy AI Gateway): one OpenAI-compatible API for hosted and self-hosted models and MCP servers, with centralised credentials, routing, quotas, failover and usage attribution enforced by Envoy and Envoy Gateway, in a two-tier design [VF: A6-S063].

**Strengths**

- Built on Envoy, which many Kubernetes platforms already run [VF: A6-S063] [AJ]
- Apache-2.0 under the Agentic AI Foundation [VF: A6-S063]
- Usage attribution and quotas suit chargeback [VF: A6-S063]

**Limitations and risks**

- Renamed and moved foundation in 2026; repository moved [VF: A6-S063, V2-S029]
- Access control, security features and hygiene not verified [NPV]
- Kubernetes and Envoy Gateway required [VF: A6-S063]

**Choose when**

- Your platform team runs Envoy Gateway and wants AI routing in the same mesh [AJ]

**Avoid when**

- You do not run Kubernetes, or need guardrail and caching features in the gateway itself [AJ]

**Nearest competitors:** C1-agentgateway, C1-litellm, C1-kong-ai-gateway

**Regulated-FS note.** Treat as platform plumbing: pair with a separate guardrail service and log store, and track the rename in the software inventory [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Agentic AI Foundation project (formerly under the Envoy project) | Verified fact | A6-S063 |
| Category | Open-source AI gateway on Envoy Proxy / Envoy Gateway (Kubernetes) | Verified fact | A6-S063 |
| Version / lineup | v1.2.0 (6 October 2026) | Verified fact | A6-S064, V2-S061 |
| Licence | Open source (Apache-2.0) | Verified fact | A6-S063 |
| Status events | 2026: renamed from Envoy AI Gateway to Agent Router and moved to the Agentic AI Foundation; deployed resources not renamed | Verified fact | A6-S063, V2-S029 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | One OpenAI-compatible API for hosted and self-hosted models and MCP servers; platform teams centralise credentials, routing, quotas, failover and usage attribution, enforced by Envoy and Envoy Gateway; two-tier design with a Tier One gateway for auth, top-level routing and global rate limiting. | Verified fact | A6-S063 |
| Stack position | Gateway/control plane in Kubernetes-based platforms | Verified fact | A6-S063 |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Envoy Proxy and Envoy Gateway on Kubernetes (CLI also available) | Verified fact | A6-S063 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source; a commercial 'Tetrate Agent Router Service' is listed among providers | Verified fact | A6-S063 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | 1.x release line; v1.2.0 on 6 October 2026 | Verified fact | A6-S064 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Not publicly verified | | |

## Cloudflare AI Gateway (`C1-cloudflare-ai-gateway`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Tactical: useful edge controls, but managed-only with unverified log localisation and no MCP evidence [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers routing, fallback, caching, rate limits, spend limits, DLP and guardrails [VF: A6-S019, A6-S052]; MCP/A2A and policy depth not evidenced [NPV] |
| Enterprise readiness | 3 | Identity-based budgets via Cloudflare Access verified [VF: A6-S019]; one control verified lifts the cap to a maximum of 3 (rule 7); enterprise support NPV |
| Security and compliance | 3 | SOC 2 Type II names AI Gateway; ISO 27001:2022 is platform-wide without naming it [VF: A6-S110]; Trust Hub pages flagged as possibly old, so 3 |
| Deployment flexibility | 2 | SaaS only; no self-host or on-prem [VF: A6-S052] |
| Ecosystem | 4 | Many providers via BYOK or Unified Billing, Workers AI, Logpush, Cloudflare One DLP [VF: A6-S052, A6-S019] |
| Reliability and maturity | 3 | GA with frequent 2026 changes, including two log-pricing changes [VF: A6-S019, V2-S074] |
| Cost / TCO | 4 | Core features and DLP free; guardrails billed as Workers AI inference; 5% Unified Billing fee; per-GB log pricing from 1 December 2026 [VF: A6-S052, V2-S074] |
| Lock-in / portability | 2 | Proprietary managed service in the data path; Unified Billing deepens dependency [VF: A6-S052] |
| **Total (generic / FS)** | **3.00 / 2.80** | |

*Evidence rules applied:* enterprise_readiness: NPV cap lifted to max 3 by one verified control (identity-based controls), rule 7

**Capabilities.** Managed edge proxy for AI provider calls with analytics, caching, rate limiting, logging, Llama Guard guardrails, DLP scanning, dynamic routing and fallback, spend limits, identity-based budgets and Unified Billing [VF: A6-S019, A6-S052].

**Strengths**

- Lowest-friction adoption: a one-line endpoint change, core features free [VF: A6-S052]
- DLP and guardrails available at the edge [VF: A6-S052]
- SOC 2 Type II with AI Gateway named in scope [VF: A6-S110]

**Limitations and risks**

- Managed only: no self-hosting or on-prem [VF: A6-S052]
- AI Gateway-specific data localisation not verified [VF: A6-S110]
- Unified Billing (5% fee) ties provider spend to Cloudflare; future features may be premium; log pricing changed in September 2026 and again from 1 December 2026 [VF: A6-S052, V2-S074]
- MCP and A2A governance not evidenced [NPV]

**Choose when**

- You already run Cloudflare Zero Trust and want quick visibility, caching and spend limits for non-confidential workloads [AJ]

**Avoid when**

- Prompts contain client data that must stay in-estate or in a verified region [AJ]
- You want the gateway to be the exit route from a provider rather than another dependency [AJ]

**Nearest competitors:** C1-portkey, C1-litellm, L2-openrouter

**Regulated-FS note.** Use BYOK rather than Unified Billing, confirm AI Gateway log localisation in writing, and keep regulated client data off this path until it is confirmed [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Cloudflare, Inc. | Verified fact | A6-S052 |
| Category | Managed SaaS AI gateway at the network edge | Verified fact | A6-S019, A6-S052 |
| Version / lineup | Continuously delivered SaaS (no version numbers); 2026 additions include spend limits (June), identity-based controls (August), Unified Billing invoice changes (1 September) and new log pricing (24 September) | Verified fact | A6-S019, A6-S052 |
| Licence | Proprietary managed service | Verified fact | A6-S052 |
| Strategic direction | Positioned as an 'AI Application Control Plane': unified billing across providers and Workers AI, cost-based spend limits, identity-based budgets via Cloudflare Access, Dynamic Routing and Auto Router | Verified fact | A6-S019 |
| What it does | Proxy for AI provider calls with analytics, caching, rate limiting, logging, guardrails (Llama Guard on Workers AI), DLP scanning, dynamic routing/fallback across providers, spend limits and unified billing. | Verified fact | A6-S019, A6-S052 |
| Stack position | Gateway/control plane delivered from Cloudflare's network; complements rather than replaces a self-hosted gateway | Verified fact | A6-S019 |
| Integration | One-line endpoint change to route provider calls; BYOK or Unified Billing; Logpush | Verified fact | A6-S052, A6-S019 |
| Dependencies | Cloudflare account; Workers AI for guardrail inference; Zero Trust subscription for full DLP profiles | Verified fact | A6-S052 |
| Certifications | SOC 2 Type II (security, confidentiality, availability) with AI Gateway named in scope; ISO 27001:2022 for the global cloud platform (AI Gateway not named individually); ISO 27701, ISO 27018 and PCI DSS Level 1 also maintained | Verified fact | A6-S110 |
| GDPR / residency | EU transfers rely on EU-U.S. Data Privacy Framework certifications with SCCs as fallback; Data Localization Suite (in SOC 2 scope) sets where data is stored and protected; AI Gateway-specific localisation behaviour not verified | Verified fact | A6-S110 |
| Security features | DLP scanning of prompts/responses (two predefined profiles free; full profiles with Zero Trust DLP); guardrails on prompts and responses | Verified fact | A6-S052 |
| Access controls | Identity-based controls using Cloudflare Access identity for per-user budgets (August 2026) | Verified fact | A6-S019 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Core features (analytics, caching, rate limiting) free on all plans; DLP free; guardrails billed as Workers AI token inference; 5% fee on Unified Billing credits (no markup on provider tokens); Logpush 10M requests/month then US$0.05 per million on Workers Paid; logs follow Workers Logs pricing for gateways created on/after 24 September 2026. From 1 December 2026 (announced): unified per-GB log pricing covering AI Gateway logs, US$0.25 per GB ingested and US$0.10 per GB-month stored after 50 GB / 10 GB-month included (blog announcement; terms may change). | Verified fact | A6-S052, V2-S074 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Third-party model providers via BYOK or Unified Billing; Workers AI models; Cloudflare One DLP | Verified fact | A6-S052, A6-S019 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Generally available managed service with frequent changelog entries in 2026 | Verified fact | A6-S019 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No (managed service only); on_prem: No | | |

# C2: Guardrails

## NVIDIA NeMo Guardrails (open-source library and Guardrails server) (`C2-nemo-guardrails`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Tactical: the most capable in-estate framework, but 0.x Beta with breaking changes; a Strategic candidate at 1.0 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Input, output, dialogue, retrieval and tool rails; jailbreak, content and topic safety; self-check rails; IORails [VF: A6-S027, A6-S036] |
| Enterprise readiness | 3 | Rule 2: server mode, OTel-style spans; identity inherits host; commercial support via NVIDIA AI Enterprise [VF: A6-S036, A6-S111] |
| Security and compliance | 3 | Rule 2 hygiene: fail-closed streaming rails and explicit block-vs-failure outcomes [VF: A6-S036]; security policy and signed releases NPV; NVIDIA certifications for the microservice NPV |
| Deployment flexibility | 4 | Library, server and Helm microservice on customer Kubernetes [VF: A6-S036, A6-S111] |
| Ecosystem | 4 | Kong NeMo plugin, F5 AI Guardrails integration, NIM safety models [VF: A6-S017, A6-S036] |
| Reliability and maturity | 2 | First release April 2023 but still 0.x Beta, breaking changes in minors (0.24.0) [VF: A6-S003, A6-S036] |
| Cost / TCO | 4 | Free; optional AI Enterprise at US$4,500 per GPU per year; model rails add inference cost [VF: A6-S112, A6-S003] |
| Lock-in / portability | 4 | Apache-2.0 but NVIDIA-governed; model rails can use any LLM endpoint [VF: A6-S003, A6-S036] |
| **Total (generic / FS)** | **3.50 / 3.45** | |

*Evidence rules applied:* Rule 2 basis: self-hosted open-source library; NPV cap not applied; commercial support exists (NVIDIA AI Enterprise)

**Capabilities.** Apache-2.0 toolkit adding programmable rails around LLM applications: content safety, topic safety, jailbreak detection (including a NIM-based model), self-check rails, Colang dialogue rails and third-party integrations; runs as a library or an OpenAI-compatible Guardrails server with a /v1/checks endpoint; new IORails engine for input, output and tool rails [VF: A6-S036, A6-S027].

**Strengths**

- Widest rail types in one in-estate framework: input, output, dialogue, retrieval and tool rails [VF: A6-S027, A6-S036]
- Engine-neutral allow/block/transform contract and fail-closed streaming output rails [VF: A6-S036]
- Supported microservice via NVIDIA AI Enterprise [VF: A6-S111, A6-S112]

**Limitations and risks**

- Still 0.x and classified Beta, with breaking changes in minor releases [VF: A6-S003, A6-S036]
- Model-based rails depend on NIM/Nemotron or other LLM endpoints [VF: A6-S027, A6-S036]
- The supported microservice accepts Colang 1.0 configurations only and lacks some toolkit server features [VF: A6-S111]

**Choose when**

- You want an in-estate guardrail orchestration layer combining classifiers, rules and model-based checks [AJ]
- You run NVIDIA AI Enterprise and want supported safety NIMs [AJ]

**Avoid when**

- You cannot absorb breaking changes in a pre-1.0 dependency [AJ]

**Nearest competitors:** C2-guardrails-ai, C2-meta-llama-protections, C7-lakera

**Regulated-FS note.** Pin versions, run it as a sidecar or server called from the gateway, and keep rail definitions in Git with the L9 red-team suite as the regression gate [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | NVIDIA (repository NVIDIA-NeMo/Guardrails) | Verified fact | A6-S003 |
| Category | Open-source programmable guardrails toolkit (input, output, dialogue, retrieval and tool rails) | Verified fact | A6-S003, A6-S027 |
| Version / lineup | 0.24.1 (16 September 2026); 0.24.0 (25 August 2026) | Verified fact | A6-S003, A6-S036, V2-S028 |
| Licence | Open source (Apache-2.0) | Verified fact | A6-S003 |
| Strategic direction | New optimised IORails engine for input/output/tool rails without Colang runtime dependency; engine-neutral RailOutcome allow/block/transform contract; typed rail manifests; server health endpoints and output-rail check mode; third-party integrations such as F5 AI Guardrails | Verified fact | A6-S036, A6-S027 |
| What it does | Adds programmable rails around LLM applications: content safety, topic safety and jailbreak detection (incl. NIM-based jailbreak model), self-check rails, dialogue rails in Colang, and third-party guardrail integrations; can run as a library or as an OpenAI-compatible Guardrails server with a /v1/checks endpoint. | Verified fact | A6-S036, A6-S027 |
| Stack position | Guardrail layer wrapping model calls inside the application or as a sidecar/server; can also be called from gateways (Kong added an NVIDIA NeMo Guardrails plugin in AI Gateway 2.0.1) | Verified fact | A6-S027, A6-S017 |
| Integration | Python library; OpenAI-compatible server with /v1/chat/completions-style and /v1/checks endpoints; OpenTelemetry-style tracing spans | Verified fact | A6-S036, A6-S027 |
| Dependencies | Python >=3.10,<3.14; LLM or NIM endpoints for model-based rails; transformers and torch for the local classifier; microservice places NemoGuard safety NIMs (content safety, topic control, jailbreak detection) between the application and its LLM | Verified fact | A6-S003, A6-S036, A6-S111 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Streaming output rails fail closed when actions fail (0.24.0); IORails distinguishes policy blocks from rail execution failures | Verified fact | A6-S036 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | NeMo Guardrails microservice (NeMo Microservices, Helm chart on NGC) is tagged 'NVIDIA AI Enterprise Supported'; AI Enterprise subscriptions include Business Standard support, Business Critical at extra cost | Verified fact | A6-S111, A6-S112 |
| Pricing | Open-source toolkit free (Apache-2.0). Supported microservice via NVIDIA AI Enterprise: list US$4,500 per GPU per year (self-managed, support included) or US$1 per GPU-hour on cloud marketplaces | Verified fact | A6-S003, A6-S112 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First PyPI release 25 April 2023; still 0.x and classified Beta; roughly monthly-to-bimonthly minor releases in 2026 (0.21 March, 0.22 May, 0.23 July, 0.24 August) | Verified fact | A6-S003 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes (NeMo Guardrails microservice deployed via Helm on customer Kubernetes); self_hosted: Yes (library or server); on_prem: Not publicly verified | | |

## Amazon Bedrock Guardrails (`C2-bedrock-guardrails`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where AWS is your primary cloud (CP3 Q2, rubric rule 10). The strongest managed policy set and AWS's lead guardrail service; use the Classic tier or region-constrained profiles for client data, because the Standard tier uses cross-region inference [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Content and prompt-attack filters, denied topics, PII (incl. UK identifiers), contextual grounding, Automated Reasoning, standalone API [VF: A6-S072, A6-S073] |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1); confirm per service |
| Security and compliance | 4 | Bedrock in AWS SOC 1/2/3 scope since 15 August 2023 and on the ISO 27001 list [VF: B-C2-S001, B-C2-S002]; Guardrails not named separately, so the scope rule applies; customer KMS key supported [VF: A6-S072] |
| Deployment flexibility | 2 | Managed AWS only; cross-region profiles [VF: A6-S072] |
| Ecosystem | 3 | Referenced by Kong and AWS's gateway Guidance [VF: A6-S017, A6-S022] |
| Reliability and maturity | 3 | Priced since at least December 2024; tiers added June 2025 (A6-S101, A6-S072); maturity fact cell NPV and InvokeGuardrailChecks GA not verified; 3, consistent with Azure AI Content Safety (GA August 2024) and Model Armor (CP3 review A) |
| Cost / TCO | 3 | Transparent per-policy unit pricing, e.g. US$0.15 per 1,000 text units for content filters [VF: A6-S101] |
| Lock-in / portability | 2 | AWS-specific API [VF: A6-S072] |
| **Total (generic / FS)** | **3.50 / 3.35** | |

*Evidence rules applied:* enterprise_readiness set to 4 under the hyperscaler presumption (CP2 Q1): platform controls presumed; confirm per service

**Capabilities.** Managed guardrails for prompts and responses: content filters (including PROMPT_ATTACK) with Classic and Standard tiers, denied topics, word filters, PII detection with block or anonymise actions (31 entity types including UK NHS and NI numbers, IBAN, SWIFT), contextual grounding and Automated Reasoning checks; usable with any model through the standalone ApplyGuardrail API [VF: A6-S072, A6-S073].

**Strengths**

- Broadest managed policy set, including grounding and Automated Reasoning [VF: A6-S072] [AJ]
- Model-independent via ApplyGuardrail [VF: A6-S073]
- Customer KMS key encryption [VF: A6-S072]

**Limitations and risks**

- Standard tier uses cross-region inference, a residency consideration [VF: A6-S072, A6-S101]
- Per-policy pricing stacks [VF: A6-S101]
- AWS-specific API [VF: A6-S072]

**Choose when**

- You run on AWS and want managed input/output guardrails, PII handling and grounding checks [AJ]
- You want guardrails callable for non-Bedrock models [AJ]

**Avoid when**

- You need the guardrail to run outside AWS, or cannot accept cross-region inference on the Standard tier [AJ]

**Nearest competitors:** C2-azure-ai-content-safety, C2-google-model-armor, C2-nemo-guardrails

**Regulated-FS note.** Pin guardrail versions in C5, use the Classic tier or region-constrained profiles for client data, and evaluate false-positive rates per policy on your own data [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Amazon Web Services | Verified fact | A6-S072 |
| Category | Managed guardrail service for generative AI inputs and outputs | Verified fact | A6-S072 |
| Version / lineup | Managed service; API model includes content filters with CLASSIC and STANDARD tiers, denied topics, word filters, sensitive-information (PII) filters, contextual grounding, Automated Reasoning policies and cross-region guardrail profiles (botocore 1.43.109, 7 October 2026); Standard/Classic safeguard tiers for content filters and denied topics introduced June 2025 (Standard uses cross-region inference) | Verified fact | A6-S072, A6-S075, A6-S101 |
| Licence | Proprietary managed service | Verified fact | A6-S072 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Configurable guardrails applied to prompts and model responses: content filters (sexual, violence, hate, insults, misconduct, prompt attack), denied topics, word filters, PII detection with block or anonymise actions (31 entity types incl. UK NHS and NI numbers, IBAN, SWIFT), contextual grounding checks and Automated Reasoning checks; usable with Bedrock models or standalone via the ApplyGuardrail API. | Verified fact | A6-S072, A6-S073 |
| Stack position | Guardrail service callable inline with Bedrock inference or independently of any model (ApplyGuardrail); also used in the AWS multi-provider gateway Guidance | Verified fact | A6-S073, A6-S022 |
| Integration | AWS API/SDK: CreateGuardrail (control plane), ApplyGuardrail and InvokeGuardrailChecks (runtime) | Verified fact | A6-S072, A6-S073 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Cross-region guardrail profiles route guardrail inference to defined destination regions (crossRegionConfig) | Verified fact | A6-S072 |
| Security features | Guardrails can be encrypted with a customer KMS key (kmsKeyId) | Verified fact | A6-S072 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Per 1,000 text units (1 unit = 1,000 characters, billed per configured policy): content filters US$0.15 and denied topics US$0.15 (since 1 December 2024); sensitive-information filters US$0.10 and Automated Reasoning checks US$0.17 (from AWS worked pricing examples); no separate Standard-tier rate found | Verified fact | A6-S101 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Referenced as a guardrail option in Kong AI Gateway ('AWS, Azure and GCP guardrail services') | Verified fact | A6-S017 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (managed AWS service); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: Not publicly verified | | |

## Model Armor (`C2-google-model-armor`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10). Google's lead guardrail service, efficient and residency-aware; narrower than Bedrock (grounding not evidenced), and the London residency position must be confirmed in writing where UK residency is required [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Prompt injection and jailbreak, malicious URLs and files, harm, sensitive data [VF: A6-S067]; grounding not evidenced [NPV] |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1); confirm per service |
| Security and compliance | 4 | Named in Google Cloud SOC 2 and ISO/IEC 27001 scope [VF: A6-S070, A6-S071]; CMK not verified, so not 5 |
| Deployment flexibility | 2 | Managed only, with regional and multi-regional endpoints [VF: B-C2-S003, B-C2-S004] |
| Ecosystem | 4 | Apigee, Agent Platform, Google MCP servers, Service Extensions, Firebase, LangChain [VF: A6-S067] |
| Reliability and maturity | 3 | Active release notes; GA date not verified [VF: B-C2-S005] [NPV] |
| Cost / TCO | 5 | Free to 2M tokens/month, then US$0.10 per 1M tokens [VF: A6-S067] |
| Lock-in / portability | 2 | Google-specific API [VF: A6-S067] |
| **Total (generic / FS)** | **3.60 / 3.35** | |

*Evidence rules applied:* enterprise_readiness set to 4 under the hyperscaler presumption (CP2 Q1): platform controls presumed; confirm per service

**Capabilities.** Managed screening of prompts, responses and agent interactions for prompt injection and jailbreaks, malicious URLs and files, harmful content with adjustable thresholds, and sensitive-data leaks (built on Sensitive Data Protection); invoked inline from Apigee, Agent Platform, Google MCP servers, Service Extensions, Firebase or LangChain [VF: A6-S067].

**Strengths**

- Strict data residency by default at template level, with six European regions plus an eu multi-region [VF: B-C2-S003, B-C2-S004]
- Low unit price: free to 2M tokens/month, then US$0.10 per 1M tokens [VF: A6-S067]
- Product-scoped SOC 2 and ISO 27001 [VF: A6-S070, A6-S071]

**Limitations and risks**

- No grounding or denied-topic checks in the fact base [NPV]
- London (europe-west2) has reduced features and conflicting in-use residency statements [VF: B-C2-S003, B-C2-S005]
- Google-specific API [VF: A6-S067]

**Choose when**

- You run on Google Cloud or Apigee and want low-cost, region-pinned screening [AJ]

**Avoid when**

- You need grounding checks, or the full feature set in London [AJ]

**Nearest competitors:** C2-bedrock-guardrails, C2-azure-ai-content-safety, C7-lakera

**Regulated-FS note.** Pin templates to an EU region with strict residency left on; if UK residency is required, confirm the London feature and in-use residency status in writing [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google Cloud | Verified fact | A6-S067 |
| Category | Managed runtime security/guardrail service for prompts, responses and agent interactions | Verified fact | A6-S067 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Not publicly verified | Not publicly verified |  |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Screens prompts, responses and agent interactions for prompt injection and jailbreaks, malicious URLs and files, harmful content with adjustable confidence thresholds, and sensitive data leaks (built on Sensitive Data Protection). | Verified fact | A6-S067 |
| Stack position | Guardrail service invoked inline from Apigee, Gemini Enterprise Agent Platform, Google MCP servers, Service Extensions, Firebase or LangChain | Verified fact | A6-S067, A6-S023 |
| Integration | API and inline integrations (Apigee, Agent Platform, Google MCP servers, Service Extensions, Firebase, LangChain) | Verified fact | A6-S067 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Listed in Google Cloud SOC 2 and ISO/IEC 27001 scope | Verified fact | A6-S070, A6-S071 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free up to 2 million tokens/month, then US$0.10 per additional 1 million tokens (pay-as-you-go and SCC Premium) | Verified fact | A6-S067 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Azure AI Content Safety (Prompt Shields); Azure product and pricing pages now titled 'Content Safety in Foundry Control Plane' (`C2-azure-ai-content-safety`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Azure is your primary cloud (CP3 Q2, rubric rule 10). Azure's lead guardrail service; GA features only (Prompt Shields, protected material) on regulated routes, because the agent-oriented and groundedness features are preview [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Harm categories, Prompt Shields (direct and document attacks), protected material; groundedness and Task Adherence preview [VF: A6-S054, A6-S055] |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1); confirm per service |
| Security and compliance | 4 | Azure ISO 27001 and SOC 2 are platform-level without naming the service [VF: B-C1-S007, B-C1-S008]; BYOK supported [VF: A6-S054]; scope rule applied, so 4 |
| Deployment flexibility | 2 | Azure resource in supported regions only [VF: A6-S054] |
| Ecosystem | 4 | APIM llm-content-safety policy, Foundry guardrails, SDKs [VF: A6-S053, A6-S103] |
| Reliability and maturity | 3 | Core GA since 2024; agent features preview; 90-day deprecation policy [VF: A6-S054, A6-S055] |
| Cost / TCO | 2 | Free tier 5,000 records/month; S0 billed per 1,000 records per model, unit prices not verified [VF: A6-S102] |
| Lock-in / portability | 2 | Azure-specific API [VF: A6-S054] |
| **Total (generic / FS)** | **3.30 / 3.20** | |

*Evidence rules applied:* enterprise_readiness set to 4 under the hyperscaler presumption (CP2 Q1): platform controls presumed; confirm per service

**Capabilities.** Managed APIs for harm categories with severity levels, Prompt Shields for user-input and document attacks, protected material detection, groundedness detection (preview), custom categories (preview) and Task Adherence for agent tool use (preview); callable from APIM on LLM, MCP and A2A traffic [VF: A6-S054, A6-S055, A6-S020].

**Strengths**

- Prompt Shields GA since August 2024, covering indirect (document) attacks [VF: A6-S055, A6-S054]
- Enforceable at the APIM gateway on tool and agent payloads [VF: A6-S020]
- BYOK encryption [VF: A6-S054]

**Limitations and risks**

- Groundedness, custom categories and Task Adherence are preview [VF: A6-S054, A6-S055]
- S0 unit prices not verified [VF: A6-S102]
- Foundry tool-call inspection is preview and only for Foundry Agent Service agents [VF: A6-S103]

**Choose when**

- You run on Azure and want prompt-attack and harm screening at the APIM gateway [AJ]

**Avoid when**

- You need GA groundedness checks today, or a guardrail outside Azure [AJ]

**Nearest competitors:** C2-bedrock-guardrails, C2-google-model-armor, C7-lakera

**Regulated-FS note.** Use Prompt Shields on retrieved documents as well as user input; treat preview features as non-production; confirm product scope in the Service Trust Portal [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Microsoft | Verified fact | A6-S054 |
| Category | Managed content-safety and prompt-attack detection APIs | Verified fact | A6-S054 |
| Version / lineup | Prompt Shields and Protected Material (text) GA August 2024; Task Adherence public preview November 2025; groundedness detection and custom categories in preview; Python SDK azure-ai-contentsafety 1.0.0 (12 December 2023) | Verified fact | A6-S055, A6-S054, A6-S084 |
| Licence | Proprietary managed service (SDK MIT) | Verified fact | A6-S054, A6-S084 |
| Strategic direction | Moving from content moderation to agent safety: Task Adherence API (preview) for agent tool use; Prompt Shields for direct and indirect attacks; Microsoft Foundry 'guardrails' (named collections of controls, default Microsoft.DefaultV2) build on Content Safety models and inspect user input, output, tool calls and tool responses (tool inspection in preview), currently only for Foundry Agent Service agents | Verified fact | A6-S055, A6-S054, A6-S103 |
| What it does | APIs to analyse text and images for sexual, violence, hate and self-harm content with severity levels; Prompt Shields for user-input and document attacks; protected material detection; groundedness detection (preview); custom categories (preview); Task Adherence for agent tool use (preview). | Verified fact | A6-S054, A6-S055 |
| Stack position | Guardrail service called by applications, Microsoft Foundry and Azure API Management (llm-content-safety policy) | Verified fact | A6-S053, A6-S020 |
| Integration | REST API and SDKs; APIM llm-content-safety policy; Content Safety Studio | Verified fact | A6-S054, A6-S053 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Resource must be created in a supported region; region list not reproduced in sources consulted | Verified fact | A6-S054 |
| Security features | Encryption at rest with customer-managed keys (BYOK) supported | Verified fact | A6-S054 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free tier: 5,000 text records/month (F0, 5 RPS). Standard (S0): billed per 1,000 text records, each model (incl. Prompt Shields) with its own rate; a text record is up to 1,000 characters. Published S0 unit prices did not render; a community figure of US$0.38 per 1,000 records is unverified | Verified fact | A6-S102, A6-S054 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Core moderation and Prompt Shields GA; several agent-oriented features in preview; 90-day deprecation policy for superseded API versions | Verified fact | A6-S054, A6-S055 |
| Deployment | saas: Yes (Azure resource in supported regions); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Llama Protections: Llama Guard 4 (12B), Llama Prompt Guard 2 (86M/22M), LlamaFirewall, Code Shield (`C2-meta-llama-protections`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Tactical: useful self-hosted detectors, but no release for 17 months is a maintenance risk for a security control [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Safety taxonomy classifier, prompt-attack classifier, agent alignment check and code scanner [VF: A6-S030, A6-S039]; 512-token window and reported multilingual weakness [VF: A6-S030] [R: A6-S031] |
| Enterprise readiness | 2 | Rule 2: components only; no commercial support from Meta verified [NPV] |
| Security and compliance | 2 | Rule 2: custom licence; LlamaFirewall licence not stated on PyPI [VF: A6-S030, A6-S006]; CVE handling NPV |
| Deployment flexibility | 5 | Open weights run anywhere, including air-gapped; also hosted by third parties [VF: A6-S030] |
| Ecosystem | 4 | Embedded in Cloudflare and Guardrails Hub; hosted on NVIDIA build and Vertex Model Garden [VF: A6-S052, A6-S029, A6-S030] |
| Reliability and maturity | 2 | Mature lineage but no release after May 2025 [VF: A6-S006, A6-S107] |
| Cost / TCO | 4 | Free; 12B model needs GPU-class serving, 22M model is cheap [VF: A6-S030] |
| Lock-in / portability | 3 | Portable weights under a custom community licence [VF: A6-S030, A6-S038] |
| **Total (generic / FS)** | **3.10 / 2.95** | |

*Evidence rules applied:* Rule 2 basis: self-hosted open weights and open-source framework; NPV cap not applied

**Capabilities.** Meta's open-weight safety components: Llama Guard 4 (12B) classifies prompts and responses (text and images) against a safety taxonomy; Prompt Guard 2 (86M/22M) detects prompt injection and jailbreaks within a 512-token window; LlamaFirewall orchestrates PromptGuard, AlignmentCheck and CodeShield across agent inputs, reasoning and outputs [VF: A6-S030, A6-S039, A6-S038].

**Strengths**

- Small, cheap prompt-attack classifier (22M) suited to inline use [VF: A6-S030]
- AlignmentCheck targets agent goal hijacking [VF: A6-S039]
- Widely embedded: Cloudflare runs Llama Guard; Guardrails Hub has a validator [VF: A6-S052, A6-S029]

**Limitations and risks**

- No release found since Llama Guard 4 / Prompt Guard 2 (29 April 2025) and llamafirewall 1.0.3 (29 May 2025) [VF: A6-S006, A6-S030, A6-S107]
- Llama community licence with a 700M MAU clause and Acceptable Use Policy, not OSI [VF: A6-S030, A6-S038]
- An independent tester reported Prompt Guard weak against non-English and obfuscated prompts [R: A6-S031]

**Choose when**

- You want an in-estate, low-cost first-pass classifier inside a broader guardrail framework [AJ]

**Avoid when**

- It would be your only prompt-attack defence, or you need a maintained component with a release cadence [AJ]

**Nearest competitors:** C2-azure-ai-content-safety, C2-google-model-armor, C7-lakera

**Regulated-FS note.** Use only as one detector among several, with your own evaluation set; record the licence terms and the maintenance risk in the inventory [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Meta | Verified fact | A6-S006, A6-S031 |
| Category | Open-weight safety classifiers plus an open-source agent guardrail framework | Verified fact | A6-S030, A6-S039 |
| Version / lineup | Llama Guard 4 12B and Prompt Guard 2 86M/22M (checkpoints 29 April 2025); llamafirewall 1.0.3 (PyPI, 29 May 2025) | Verified fact | A6-S030, A6-S006, V2-S028 |
| Licence | Models: Llama Community licences (Llama Guard 4 under Llama 4 Community License, incl. 700M MAU clause and Acceptable Use Policy); evals/benchmarks MIT; LlamaFirewall licence not stated on PyPI | Verified fact | A6-S030, A6-S038, A6-S006 |
| Strategic direction | Agent-focused layered defence: LlamaFirewall orchestrates PromptGuard, AlignmentCheck (chain-of-thought auditing for goal hijacking) and CodeShield scanners; no newer release found since mid-2025 | Verified fact | A6-S039, A6-S031 |
| What it does | Llama Guard 4 classifies prompts and responses (text and images) against a safety taxonomy; Prompt Guard 2 detects prompt injection and jailbreaks (512-token window); LlamaFirewall combines scanners across agent inputs, reasoning and outputs; Code Shield filters insecure generated code. | Verified fact | A6-S030, A6-S039, A6-S038 |
| Stack position | Model-level guardrail components called by applications, gateways or guardrail frameworks (e.g. Guardrails Hub has a Llama Guard validator; Cloudflare AI Gateway uses Llama Guard) | Verified fact | A6-S029, A6-S052 |
| Integration | Hugging Face model weights; Llama API moderations endpoint; hosted on third parties (e.g. NVIDIA build, Vertex Model Garden); pip install llamafirewall | Verified fact | A6-S030, A6-S039 |
| Dependencies | GPU/CPU inference for 12B (Llama Guard 4) or 22M/86M (Prompt Guard 2) models; LlamaFirewall Python package | Verified fact | A6-S030, A6-S006 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free to download under licence terms | Verified fact | A6-S030 |
| Infrastructure cost | Llama Guard 4 is a 12B-parameter model (GPU class serving); Prompt Guard 2 22M designed for low-latency, low-compute use | Verified fact | A6-S030 |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Mature model lineage (Llama Guard 1 to 4); Meta's current model cards still present Llama Guard 4 (12B) as 'the latest safeguard model'; no 2026 release found in a vendor-domain search | Verified fact | A6-S038, A6-S030, A6-S006, A6-S107 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open weights and open-source framework); on_prem: Not publicly verified | | |

## Guardrails AI (open-source 'guardrails' framework and Guardrails Hub validators) (`C2-guardrails-ai`)

**Tier:** Experimental · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* Experimental: the owner is now an application company, the distribution model changed weeks before the deal, and the roadmap is not stated [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Validators and structured-output validation; no native grounding or prompt-attack depth evidenced beyond validators [VF: A6-S037, A6-S029] |
| Enterprise readiness | 2 | Rule 2: library plus REST server; enterprise platform 'talk to sales' per a secondary source only [R: A6-S028] |
| Security and compliance | 2 | Rule 2 hygiene not verified [NPV]; distribution change mid-2026 [VF: A6-S037] |
| Deployment flexibility | 3 | Self-hosted only now that remote inference is retired [VF: A6-S037] |
| Ecosystem | 3 | Hub validators (including Llama Guard) and 250,000+ monthly downloads (vendor claim) [VF: A6-S029, A6-S028] |
| Reliability and maturity | 2 | 0.x since 2023; acquired; distribution changed [VF: A6-S004, A6-S028, A6-S037] |
| Cost / TCO | 4 | Free open source [VF: A6-S004] |
| Lock-in / portability | 3 | Apache-2.0, but acquired and not neutrally governed: minus 1 (rule 3) [VF: A6-S004, A6-S028] |
| **Total (generic / FS)** | **2.70 / 2.60** | |

*Evidence rules applied:* Rule 2 basis: self-hosted open-source library; NPV cap not applied

**Capabilities.** Apache-2.0 Python framework running input and output Guards with composable validators and structured-output validation, plus a Guardrails Server REST API; validators now ship as PyPI packages after the hosted hub and remote inference were retired [VF: A6-S037, A6-S029, A6-S004].

**Strengths**

- Simple validator model for structured-output and format checks [VF: A6-S037] [AJ]
- Apache-2.0 [VF: A6-S004]

**Limitations and risks**

- Acquired by Harvey, a legal AI application company, on 9 September 2026; open-source roadmap not stated [VF: A6-S028, V2-S026]
- Hosted hub install and remote inference retired; cutoff given as 25 August (repository) or 6 August 2026 (docs) [VF: V2-S071, V2-S072]
- 0.x versioning [VF: A6-S004]

**Choose when**

- You already use it for structured-output validation and can vendor the validators you need [AJ]

**Avoid when**

- You are choosing a new strategic guardrail dependency [AJ]

**Nearest competitors:** C2-nemo-guardrails, C2-meta-llama-protections, L9-opik

**Regulated-FS note.** Freeze and vendor the validators in use, plan a migration path, and do not rely on any hosted Guardrails service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Harvey (acquired Guardrails AI, announced 9 September 2026) | Verified fact | A6-S028 |
| Category | Open-source input/output validation framework for LLM applications | Verified fact | A6-S037 |
| Version / lineup | guardrails-ai 0.11.0 (14 August 2026) | Verified fact | A6-S004, V2-S028 |
| Licence | Open source (Apache-2.0) | Verified fact | A6-S004, A6-S037 |
| Status events | 6 July 2026: announced move of validators to PyPI and discontinuation of hosted remote inference (hard cutoff 25 August 2026 per the repository HUB_UPDATE.md; the docs-site 0.11 migration guide gives 6 August 2026); 9 September 2026: acquired by Harvey; co-founders Shreya Rajpal and Zayd Simjee joined Harvey; terms undisclosed | Verified fact | A6-S037, A6-S028, V2-S026, V2-S071, V2-S072 |
| Strategic direction | Validators moving to standard PyPI packages; hosted remote inferencing discontinued (cutoff 25 August 2026); team joined Harvey's product and engineering organisation to work on agent reliability | Verified fact | A6-S037, A6-S028 |
| What it does | Runs input and output Guards in the application that detect, quantify and mitigate specific risks using composable validators (from Guardrails Hub), and supports structured output validation; also offers a Guardrails Server REST API. | Verified fact | A6-S037, A6-S029 |
| Stack position | Application-level guardrail library around model calls | Verified fact | A6-S037 |
| Integration | Python SDK; validators installed with pip as guardrails-ai-<name>; Guardrails Server REST API | Verified fact | A6-S029, A6-S037 |
| Dependencies | Python >=3.10,<3.14; individual validators may need their own models | Verified fact | A6-S004, A6-S029 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Open-source framework free; enterprise platform and Snowglobe sold via sales (last known) | Reported | A6-S028 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Harvey states the framework is downloaded more than 250,000 times a month (vendor claim) | Verified fact | A6-S028 |
| Maturity | First PyPI release 13 March 2023; 0.x versioning | Verified fact | A6-S004 |
| Deployment | saas: No longer for free remote inference (retired 25 August 2026); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Not publicly verified | | |

# C3: DLP and PII protection

## Presidio (Data Privacy Stack) (`C3-presidio`)

**Tier:** Strategic · **Flags:** Renamed · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: as the in-estate engine behind a firm-owned privacy service with recall testing and a sampling second detector; enterprise readiness is what the firm builds around it [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers detection and masking across text, images and structured data; no vault tokenisation, discovery or classification of stores. |
| Enterprise readiness | 3 | Rule 2 library: enables in-estate detection; no commercial support; REST services unauthenticated by default (NPV). |
| Security and compliance | 3 | Rule 2 hygiene: security policy with private reporting verified (B-C3-S001); MIT clear; signed releases NPV; inherits host controls. |
| Deployment flexibility | 5 | Self-hosted library or containers, in-estate and offline-capable with local NER models. |
| Ecosystem | 3 | Python and REST interfaces; gateway and guardrail integrations not verified in the fact base. |
| Reliability and maturity | 3 | Releases since March 2020 with several a year; governance moved to volunteers in 2026. |
| Cost / TCO | 4 | Free; operating cost is recogniser tuning and testing. |
| Lock-in / portability | 5 | MIT with neutral community governance; rule 3 reduction not applied (permissive OSS, neutral governance). |
| **Total (generic / FS)** | **3.50 / 3.65** | |

*Evidence rules applied:* Rule 2 (self-hosted library): enterprise_readiness and security_compliance capped at 4; NPV cap not applied; inherits host controls

**Capabilities.** Open-source PII detection and de-identification SDK (analyzer, anonymizer, image redactor incl. DICOM, structured data) using NER, regex, rules and checksums with context; LLM-based recognisers added; Python packages and Docker REST services [VF: A6-S068, A6-S040, A6-S041]. 2.2.364 (22 July 2026), MIT [VF: A6-S005, V2-S028].

**Strengths**

- Runs entirely in-estate, so 'must not leave' text is inspected before any external call [AJ]
- MIT licence and community governance with a Technical Steering Committee [VF: A6-S040, V2-S030]
- Custom recognisers are code the firm can own, version and test [AJ]
- Published security policy with private vulnerability reporting and 48-hour acknowledgement [VF: B-C3-S001]

**Limitations and risks**

- README warns detection is not guaranteed to find all sensitive data [VF: A6-S068]
- Maintained by volunteers; not owned or operated by a commercial entity; no commercial support [VF: A6-S040]
- Ownership moved from Microsoft in 2026; images moved from MCR to GHCR [VF: A6-S040, A6-S041]
- No vault, discovery or built-in authentication on REST services documented [NPV]
- Signed releases not verified [NPV]

**Choose when**

- You need in-estate detection behind a firm-owned privacy service [AJ]
- You need firm-specific recognisers (client codes, account numbers) [AJ]

**Avoid when**

- You need a supported product with an SLA [AJ]
- You need reversible tokenisation at scale or estate-wide discovery [AJ]

**Nearest competitors:** C3-google-sdp, C2-bedrock-guardrails, C3-protegrity

**Regulated-FS note.** Pin versions, update image references after the GHCR move, and gate upgrades on recall per entity class measured on the firm's test corpus [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Community-governed open-source project under the Data Privacy Stack organisation (formerly Microsoft); Technical Steering Committee | Verified fact | A6-S040, V2-S030 |
| Category | Open-source PII detection and de-identification SDK (text, images, structured data) | Verified fact | A6-S068 |
| Version / lineup | presidio-analyzer and presidio-anonymizer 2.2.364 (22 July 2026) | Verified fact | A6-S005, V2-S028 |
| Licence | Open source (MIT) | Verified fact | A6-S005, A6-S040 |
| Status events | 2026: transitioned from a Microsoft-owned project to community governance under Data Privacy Stack (rebrand in 2.2.363, 28 June 2026); container images moved from MCR to GHCR | Verified fact | A6-S040, A6-S041 |
| Strategic direction | Independent, vendor-neutral governance; continued recognisers for new jurisdictions (e.g. South African, Philippine IDs) and LLM-based recognisers (LangExtract) | Verified fact | A6-S040, A6-S041 |
| What it does | Identifies PII in text and images using NER, regular expressions, rule-based logic and checksums with context, and de-identifies it; separate modules for analyzer, anonymizer, image redactor (incl. DICOM) and structured data. README warns detection is not guaranteed to find all sensitive data. | Verified fact | A6-S068 |
| Stack position | Library or microservice used in ingestion pipelines, gateways and guardrail hooks to detect and mask PII | Verified fact | A6-S068 |
| Integration | Python packages, REST services in Docker images (ghcr.io/data-privacy-stack/presidio-*) | Verified fact | A6-S040, A6-S068 |
| Dependencies | Python >=3.10,<3.15; spaCy/Stanza or Hugging Face NER models (NoOpNlpEngine available) | Verified fact | A6-S005, A6-S041 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source | Verified fact | A6-S040 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | First PyPI release 10 March 2020; 2.2.x line with several releases per year | Verified fact | A6-S005 |
| Deployment | saas: No (not operated by a commercial entity); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Not publicly verified | | |

## Sensitive Data Protection (including Cloud Data Loss Prevention / DLP API) (`C3-google-sdp`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10), because deployment flexibility and lock-in score 2 [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Discovery, profiling, 200+ detectors, masking, tokenisation and bucketing, runtime prompt/response use via Model Armor. |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1): platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 4 | SOC 2 and ISO 27001 product-scoped; KMS-wrapped de-identification keys; CMEK for stored profiles and EU locations not verified, so 4 not 5. |
| Deployment flexibility | 2 | SaaS only on Google Cloud; regional processing possible; no self-host. |
| Ecosystem | 4 | Built into Google Cloud storage services, Model Armor and Apigee; hybrid jobs for external data. |
| Reliability and maturity | 5 | Long-established service (client library since February 2018). |
| Cost / TCO | 3 | Transparent but volume-priced: US$3.00/GiB after 1 GiB free; discovery subscription US$2,500/unit/month. |
| Lock-in / portability | 2 | Google Cloud-specific API; outputs portable. |
| **Total (generic / FS)** | **3.80 / 3.60** | |

**Capabilities.** Managed discovery, classification and de-identification (formerly Cloud DLP): profiling of BigQuery, Cloud SQL, Cloud Storage and Agent Platform; 200+ detectors; masking, tokenisation, bucketing; hybrid jobs for external sources; underpins Model Armor [VF: A6-S066, A6-S065, A6-S067].

**Strengths**

- Broadest managed detection and transformation set in the control [AJ]
- Product-scoped SOC 2 and ISO 27001 [VF: A6-S070, A6-S071]
- Tokenisation keys wrapped by Cloud KMS, global or in the request region [VF: B-C3-S002]
- Transparent per-GiB pricing [VF: A6-S065]

**Limitations and risks**

- No self-hosted option [VF: A6-S066]
- Google Cloud-specific API [VF: A6-S066]
- Supported EU locations not retrieved [NPV]
- Raw text must be sent to the service for inspection [AJ]

**Choose when**

- Google Cloud is the data platform [AJ]
- Model Armor or Apigee are already in the path [AJ]

**Avoid when**

- Policy forbids sending raw client text to a cloud service before tokenisation [AJ]
- You need a multi-cloud engine with one API [AJ]

**Nearest competitors:** C3-presidio, C3-microsoft-purview-dspm-ai, C2-bedrock-guardrails

**Regulated-FS note.** Pin processing and key location to an approved EU/UK region and confirm against the locations page; platform controls presumed (CP2 Q1); confirm per service [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Google Cloud | Verified fact | A6-S066 |
| Category | Managed sensitive-data discovery, classification and de-identification service | Verified fact | A6-S066 |
| Version / lineup | Managed service; Python client google-cloud-dlp 3.40.0 (1 October 2026) | Verified fact | A6-S083 |
| Licence | Proprietary managed service (client libraries Apache-2.0) | Verified fact | A6-S066, A6-S083 |
| Strategic direction | Positioned for AI workloads: de-identify training/tuning data and protect generative AI prompts and responses at run time; underpins Model Armor's sensitive-data screening | Verified fact | A6-S066, A6-S067 |
| What it does | Discovery and profiling of sensitive data across BigQuery, Cloud SQL, Cloud Storage and Agent Platform; inspection with 200+ predefined detectors; de-identification by masking, tokenisation, bucketing; content methods for any data source (hybrid jobs). | Verified fact | A6-S066, A6-S065 |
| Stack position | DLP service used in ingestion pipelines and at run time on prompts/responses (directly or through Model Armor) | Verified fact | A6-S066, A6-S067 |
| Integration | DLP API and client libraries; built-in integrations with Google Cloud storage services; hybrid jobs for external sources | Verified fact | A6-S066, A6-S065 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Listed in Google Cloud SOC 2 and ISO/IEC 27001 scope | Verified fact | A6-S070, A6-S071 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Content/hybrid inspection: first 1 GiB/month free, then US$3.00/GiB to 1 TiB and US$2.00/GiB above; storage inspection from US$1.00/GiB tiered to US$0.60/GiB; discovery in consumption mode (bytes profiled) or subscription at US$2,500 per subscription unit/month | Verified fact | A6-S065 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Long-established service (client library first released February 2018) | Verified fact | A6-S083 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: No; on_prem: Not publicly verified | | |

## Microsoft Purview Data Security Posture Management (new unified DSPM, GA May 2026), absorbing the earlier 'DSPM for AI' experience (`C3-microsoft-purview-dspm-ai`)

**Tier:** Strategic · **Flags:** Renamed · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Azure and Microsoft 365 are your primary cloud and E5 or the Purview Suite is already licensed (CP3 Q2, rubric rule 10). Microsoft's lead AI data-security posture service, for posture and Copilot evidence only: it is not the prompt-path DLP control for custom agents [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Posture, discovery and risk assessment of AI interactions; no verified inline transformation for custom apps. |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1): platform controls presumed (CP2 Q1); confirm per service. |
| Security and compliance | 4 | Purview portal ISO 27001 and Purview FedRAMP High; DSPM not named and commercial SOC 2 scope does not list the portal; scope rule applied (4). |
| Deployment flexibility | 2 | Microsoft cloud service only; GCC coverage reduced. |
| Ecosystem | 4 | Microsoft 365, Entra-registered apps, ChatGPT Enterprise and Foundry; partner sources preview. |
| Reliability and maturity | 3 | Unified DSPM GA May 2026 after consolidation; preview components remain. |
| Cost / TCO | 2 | Requires E5 or Purview Suite; licensing for Business Premium conflicting. |
| Lock-in / portability | 2 | Microsoft-specific posture model and labels. |
| **Total (generic / FS)** | **3.10 / 3.05** | |

**Capabilities.** Unified Purview Data Security Posture Management (GA May 2026) absorbing DSPM for AI: discovers and assesses data-security risk in AI use, including prompts and responses for Microsoft 365 Copilot, Entra-registered AI apps and ChatGPT Enterprise; covers Foundry workloads; partner sources and the posture agent in preview [VF: A6-S090, A6-S091, V2-S036].

**Strengths**

- Posture over the AI apps employees already use, inside the Microsoft compliance estate [AJ]
- Purview portal in ISO 27001 scope; Purview in FedRAMP High scope [VF: B-C4-S008, A6-S056]

**Limitations and risks**

- Posture and governance, not an inline tokenisation engine for custom agents [AJ]
- Requires Microsoft 365 E5 or Purview Suite; Business Premium coverage conflicting [VF: A6-S091] [R: A6-S092]
- Partner data sources and the posture agent still preview [VF: V2-S036]
- Feature list of the new DSPM beyond AI coverage not verified [NPV]

**Choose when**

- Microsoft 365 Copilot or ChatGPT Enterprise is in use and E5/Purview Suite is licensed [AJ]

**Avoid when**

- You need run-time masking in a custom agent's prompt path [AJ]
- You are not a Microsoft estate [AJ]

**Nearest competitors:** C3-google-sdp, C3-protegrity, C3-skyflow

**Regulated-FS note.** Use for SaaS AI and Copilot posture evidence; do not count it as the prompt-path DLP control for custom agents; platform controls presumed (CP2 Q1); confirm per service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Microsoft | Verified fact | A6-S056 |
| Category | Data security posture management for AI and data estates within the Microsoft Purview suite | Verified fact | A6-S090, A6-S091 |
| Version / lineup | New DSPM generally available May 2026; classic DSPM and DSPM for AI remained until June 2026; partner (non-Microsoft) data sources and the Data Security Posture Agent still preview | Verified fact | A6-S090, V2-S036 |
| Licence | Proprietary SaaS; requires Microsoft 365 E5 or Microsoft Purview Suite (formerly Microsoft 365 E5 Compliance) | Verified fact | A6-S091 |
| Status events | May-June 2026: DSPM for AI consolidated into the new unified Purview DSPM (GA May 2026) | Verified fact | A6-S090, V2-S036 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Discovers and assesses data-security risk in AI use, including interactions, prompts and responses for Microsoft 365 Copilot, Entra-registered AI apps and ChatGPT Enterprise (E5 required for prompt/response coverage); Purview also covers Microsoft Foundry workloads | Verified fact | A6-S091 |
| Stack position | Not publicly verified | Not publicly verified |  |
| Integration | Not publicly verified | Not publicly verified |  |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Microsoft Purview (incl. Data Map, Data Estate Insights and governance portal) in Azure FedRAMP High and DoD IL2 scope | Verified fact | A6-S056 |
| GDPR / residency | In US Government GCC only Microsoft 365 Copilot and supported AI sites are available in DSPM for AI | Verified fact | A6-S091 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Included in Microsoft 365 E5 / Purview Suite; community answers state the Purview Suite for Business Premium add-on (US$10/user/month) includes DSPM for AI - conflicting, unverified by an official licensing matrix | Reported | A6-S091, A6-S092 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Agent 365 is available as an add-on to Microsoft E5/A5/Business Premium or Microsoft Defender Suite + Microsoft Purview Suite | Verified fact | A6-S059 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Microsoft cloud service); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Skyflow (Data Privacy Vault; Detect) (`C3-skyflow`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Purpose-built for reversible LLM tokenisation, but a vendor-held vault is a lock-in and outsourcing decision, not a default [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Vault tokenisation, de-identification and authorised rehydration across the AI flow. |
| Enterprise readiness | 3 | CP2 Q2: role-scoped credentials (RBAC) verified; SSO and audit NPV; max 3. |
| Security and compliance | 4 | ISO 27001:2022, SOC 2 Type II and PCI DSS L1 listed on the trust page; no CMK/ISO 42001/FedRAMP verified; reports not public. |
| Deployment flexibility | 2 | Hosted vaults in many regions; self-host not verified. |
| Ecosystem | 3 | REST APIs and SDKs; mainstream. |
| Reliability and maturity | 3 | SDK since October 2021; v1 EOL forces migration; funding last verified 2024. |
| Cost / TCO | 2 | Pricing not published. |
| Lock-in / portability | 2 | Vendor-held vault and token map; exit requires bulk detokenisation. |
| **Total (generic / FS)** | **3.05 / 3.00** | |

*Evidence rules applied:* enterprise_readiness: CP2 Q2 partial evidence (RBAC only verified), max 3

**Capabilities.** Data privacy vault: stores sensitive data and returns tokens; detokenises under role-scoped credentials; Detect APIs de-identify text and files; LLM Privacy Vault tokenises or masks data before models, prompts, RAG, tools, traces and agent workflows with authorised rehydration; EU vaults [VF: A6-S081, A6-S095].

**Strengths**

- Built around reversible tokenisation of LLM traffic [VF: A6-S095]
- Residency by vault region, including EU vaults [VF: A6-S095]
- Security page lists ISO 27001:2022, SOC 2 Type II and PCI DSS Level 1 [VF: B-C3-S005]

**Limitations and risks**

- Vendor holds the sensitive values and sits on the critical path of re-identification [AJ]
- Self-hosting, SSO, audit logs and pricing not verified [NPV]
- SDK v1 end of life 31 October 2026 [VF: A6-S081]
- No funding round verified after March 2024 [VF: A6-S096]
- Certification reports not public [VF: B-C3-S005]

**Choose when**

- You need reversible pseudonymisation across many applications with per-region vaults [AJ]

**Avoid when**

- Policy requires identifiers to stay in the firm's estate [AJ]
- You cannot test bulk detokenisation for exit [AJ]

**Nearest competitors:** C3-protegrity, C3-google-sdp, firm-built token service

**Regulated-FS note.** Migrate off SDK v1 before 31 October 2026; test bulk detokenisation as the exit plan; assess financial resilience as a material outsourcing [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Skyflow | Verified fact | A6-S081 |
| Category | Data privacy vault with tokenisation and de-identification (Detect) APIs | Verified fact | A6-S081 |
| Version / lineup | Python SDK skyflow 2.1.3 (4 August 2026); SDK v1 in maintenance, end of life 31 October 2026 | Verified fact | A6-S081 |
| Licence | Proprietary SaaS; SDK published on PyPI | Verified fact | A6-S081 |
| Strategic direction | LLM Privacy Vault: tokenises or masks sensitive data before it reaches models, prompts, RAG, tools, traces and agent workflows, with authorised rehydration; Runtime Data Control for Enterprise AI Search | Verified fact | A6-S095 |
| What it does | Stores sensitive data in vaults and returns tokens; detokenises under role-scoped credentials; Detect APIs de-identify text and files (redaction types) for use in AI and analytics workflows. | Verified fact | A6-S081 |
| Stack position | Vault/tokenisation service outside the AI stack; de-identification before prompts or ingestion | Verified fact | A6-S081 |
| Integration | REST APIs and SDKs; vault URLs per cluster (https://{cluster_id}.vault.skyflowapis.com); environments PROD, SANDBOX, DEV, STAGE | Verified fact | A6-S081 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Vendor states compliance with ISO 27001, SOC 2 Type 1 and Type 2, PCI DSS Level 1, GDPR and HIPAA (vendor claim; reports not seen) | Verified fact | A6-S095 |
| GDPR / residency | EU data privacy vaults offered; vault infrastructure 'available in over 100 countries'; regional deployments e.g. AWS Jakarta | Verified fact | A6-S095 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Bearer tokens scoped to roles; API key and static bearer token authentication | Verified fact | A6-S081 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Latest verified funding: US$30m Series B extension led by Khosla Ventures (28 March 2024); total equity about US$100m per Crunchbase (via Finovate); named customers GoodRx, Lenovo, Hippocratic AI | Verified fact | A6-S096 |
| Maturity | SDK first released October 2021 | Verified fact | A6-S081 |
| Deployment | saas: Yes (hosted vaults); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Protegrity (data protection platform; 'Protegrity AI Developer Edition') (`C3-protegrity`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strong tokenisation and audit model for existing customers; AI editions not yet GA and certification currency unverified [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Discovery, tokenisation, masking, reversible protect/unprotect and semantic guardrails. |
| Enterprise readiness | 3 | CP2 Q2: RBAC and audit verified for ESA (B-C3-S004); SSO NPV; max 3. |
| Security and compliance | 2 | Anchor-based 2: ISO 27001:2013 announced 2023 with renewal unverified; no SOC 2 found. |
| Deployment flexibility | 3 | Customer-deployed core platform and containerised Developer Edition; AI Team Edition AWS-only. |
| Ecosystem | 3 | Python module, APIs, protectors and gateway; mainstream rather than broad. |
| Reliability and maturity | 3 | Established core platform; AI Team Edition Tech Preview. |
| Cost / TCO | 2 | Pricing not published; enterprise licensing. |
| Lock-in / portability | 2 | Proprietary policies and tokens; reversal depends on Protegrity. |
| **Total (generic / FS)** | **2.90 / 2.75** | |

*Evidence rules applied:* security_compliance 2 by anchor (certificate currency unverified, no SOC 2 found); not an NPV cap; enterprise_readiness: CP2 Q2 partial evidence (RBAC and audit verified, SSO NPV), max 3

**Capabilities.** Enterprise data-protection platform: Data Discovery for PII in unstructured text; Find and Redact, Protect and Unprotect under Protegrity protection policies (tokenisation, masking); Semantic Guardrail API; ESA central policy with role-per-data-element permissions and audit [VF: A6-S082, B-C3-S004]. AI Team Edition (17 November 2025) still Tech Preview, AWS-only [VF: A6-S093].

**Strengths**

- Role-per-data-element Unprotect rights and audit at every protection point [VF: B-C3-S004]
- Same tokens and policies can span structured data and the AI path [AJ]

**Limitations and risks**

- AI Team Edition documented as Tech Preview; AWS-only [VF: A6-S093]
- Only certification verified is ISO 27001:2013 (2023); no SOC 2 report found [VF: A6-S094, B-C3-S003]
- SSO not verified; pricing not published [NPV]
- Tokenised data depends on Protegrity policies to reverse [AJ]

**Choose when**

- Protegrity already tokenises your structured data [AJ]

**Avoid when**

- You are not on AWS for the AI editions [AJ]
- A current SOC 2 Type II report is a procurement gate [AJ]

**Nearest competitors:** C3-skyflow, C3-google-sdp, C3-presidio

**Regulated-FS note.** Request the current ISO certificate and any SOC 2 report; treat AI Team Edition as a pilot until GA [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Protegrity | Verified fact | A6-S082 |
| Category | Enterprise data protection: discovery, tokenisation, masking, plus semantic guardrails for GenAI | Verified fact | A6-S082 |
| Version / lineup | Protegrity AI Team Edition launched 17 November 2025 (docs still say Tech Preview, not GA; April 2026 release says 'available now'); AI Enterprise Edition; protegrity-developer-python 1.1.1 (16 December 2025) | Verified fact | A6-S093, A6-S082 |
| Licence | Proprietary platform; AI Developer Edition Python module MIT-licensed | Verified fact | A6-S082 |
| Status events | 17 November 2025: AI Team Edition launched for agentic workflows; April 2026: team expansion announcement (no funding or acquisition disclosed) | Verified fact | A6-S093 |
| Strategic direction | Targets GenAI: protect sensitive data in prompts, outputs and training data; Semantic Guardrail API scans conversations for PII and risk | Verified fact | A6-S082 |
| What it does | Data Discovery classifies PII in unstructured text; Find and Redact / Protect / Unprotect using Protegrity protection policies (tokenisation, masking); Application Protector for structured protect/unprotect; Semantic Guardrail scanning. | Verified fact | A6-S082 |
| Stack position | DLP/tokenisation layer applied in data pipelines and on prompts/responses | Verified fact | A6-S082 |
| Integration | Python module and APIs; containerised Developer Edition sandbox | Verified fact | A6-S082 |
| Dependencies | AI Team Edition deployment currently AWS-specific | Verified fact | A6-S093 |
| Certifications | ISO 27001:2013 certification for its ISMS announced August 2023 (current renewal/2022 transition not verified); no Protegrity SOC 2 report found - SOC 2 references describe customer audit support | Verified fact | A6-S094, A6-S093 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (containerised Developer Edition); on_prem: Not publicly verified | | |

# C4: Identity and access for agents

## Open Policy Agent (OPA) (`C4-opa`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* The neutral, mature policy decision point for agent tool governance across clouds [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | General ABAC/RBAC policy engine; agent semantics are the firm's to model. |
| Enterprise readiness | 3 | Rule 2: enables central policy decisions in-estate; commercial support not verified. |
| Security and compliance | 4 | Rule 2 hygiene: security policy (B-C4-S001), CNCF graduated, Apache-2.0. |
| Deployment flexibility | 5 | Library, sidecar or daemon; self-hosted and on-premises. |
| Ecosystem | 5 | Used across services, APIs, Kubernetes and infrastructure. |
| Reliability and maturity | 4 | Graduated since 2021 with regular releases; maintainer funding not verified. |
| Cost / TCO | 4 | Free; Rego skills and policy testing are the cost. |
| Lock-in / portability | 5 | Open source, Apache-2.0, CNCF governance. |
| **Total (generic / FS)** | **4.15 / 4.20** | |

*Evidence rules applied:* Rule 2 (self-hosted software / open specification): enterprise_readiness and security_compliance capped at 4; NPV cap not applied; inherits host controls

**Capabilities.** Open Policy Agent: general-purpose policy engine evaluating Rego policies against JSON input for allow/deny or richer decisions, as library or sidecar/daemon, across services, APIs, Kubernetes and infrastructure; v1.21.1 (29 September 2026), Apache-2.0, CNCF graduated (February 2021) [VF: A6-S046, A6-S048, A6-S088].

**Strengths**

- One policy engine for gateway, tool server and infrastructure decisions [VF: A6-S046]
- CNCF graduated with a published security policy [VF: A6-S046, B-C4-S001]
- Policies are code that can be unit-tested and versioned [AJ]

**Limitations and risks**

- No agent-specific features verified [NPV]
- Reported 2025 move of the original maintainers to Apple not verified [NPV]
- Rego is a learning curve [AJ]

**Choose when**

- You want one vendor-neutral PDP across clouds and runtimes [AJ]

**Avoid when**

- Your agent estate is AWS AgentCore and you want managed, automated-reasoning-checked policies [AJ]

**Nearest competitors:** C4-cedar, Gateway-native policy (Kong, AgentCore Policy)

**Regulated-FS note.** Evaluate every tool call at the gateway with principal, agent, tool and arguments as input; keep policies and their tests in Git under change control [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Open Policy Agent project, CNCF graduated (graduated February 2021) | Verified fact | A6-S046 |
| Category | Open-source general-purpose policy engine (policy-as-code, Rego) | Verified fact | A6-S046 |
| Version / lineup | v1.21.1 (29 September 2026) | Verified fact | A6-S048, A6-S047, V2-S061 |
| Licence | Open source (Apache-2.0) | Verified fact | A6-S088 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Evaluates context-aware policies written in Rego against JSON input to return allow/deny or richer decisions, enabling unified policy enforcement across services, APIs, Kubernetes and infrastructure. | Verified fact | A6-S046 |
| Stack position | Policy decision point used by gateways, agent runtimes and tool servers for ABAC/RBAC decisions | Verified fact | A6-S046 |
| Integration | Rego policies; library or sidecar/daemon; VS Code extension and Rego Playground | Verified fact | A6-S046 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source | Verified fact | A6-S088 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | CNCF graduated; 1.x line with regular releases (1.21.0 and 1.21.1 in 2026) | Verified fact | A6-S046, A6-S047 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes | | |

## SPIFFE (specification) and SPIRE (SPIFFE Runtime Environment) (`C4-spiffe-spire`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* The neutral workload-identity layer beneath agents and tools; mature, open and portable [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Workload identity and attestation; one core C4 function, not delegation or authorisation. |
| Enterprise readiness | 3 | Rule 2: enables estate-wide workload identity; commercial distributions not assessed. |
| Security and compliance | 4 | Rule 2 hygiene: security policy with supported versions (B-C4-S002), third-party audit, CNCF assessments. |
| Deployment flexibility | 5 | Self-hosted anywhere including on-premises. |
| Ecosystem | 4 | Envoy SDS, Kubernetes and cloud node attestors. |
| Reliability and maturity | 5 | CNCF graduated with regular releases. |
| Cost / TCO | 3 | Free, but server and attestor operations are material. |
| Lock-in / portability | 5 | Open standard, Apache-2.0, CNCF governance. |
| **Total (generic / FS)** | **3.85 / 4.05** | |

*Evidence rules applied:* Rule 2 (self-hosted software / open specification): enterprise_readiness and security_compliance capped at 4; NPV cap not applied; inherits host controls

**Capabilities.** SPIFFE specification and SPIRE runtime: attests running workloads and issues SPIFFE IDs and X.509/JWT SVIDs through the Workload API for mTLS or signed JWTs; Envoy SDS; SPIRE v1.15.3 (21 August 2026), Apache-2.0, CNCF graduated [VF: A6-S087, A6-S042, A6-S043, A6-S089].

**Strengths**

- Removes static secrets for workload-to-workload trust [AJ]
- CNCF graduated; Cure53 audit (2021) and CNCF security assessments [VF: A6-S087]
- Security fixes for current and previous minor release series [VF: B-C4-S002]

**Limitations and risks**

- Machine identity only; carries no delegated user authority [VF: A6-S087]
- No agent-specific SPIFFE profile verified [NPV]
- Operating SPIRE servers and attestors is a platform-team commitment [AJ]

**Choose when**

- Agents, gateways and MCP servers run on Kubernetes or mixed infrastructure and need workload identity without long-lived secrets [AJ]

**Avoid when**

- A cloud-native workload identity already covers every runtime [AJ]

**Nearest competitors:** Cloud workload identity federation (Entra, AWS IAM), C7-hashicorp-vault

**Regulated-FS note.** Use SVIDs for agent-runtime-to-gateway and gateway-to-tool mTLS; never as a substitute for the user's delegated token [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | SPIFFE project, CNCF graduated | Verified fact | A6-S087 |
| Category | Open specification and open-source implementation for workload identity | Verified fact | A6-S087 |
| Version / lineup | SPIRE v1.15.3 (21 August 2026); 1.16.0 unreleased | Verified fact | A6-S043, A6-S042, V2-S061 |
| Licence | Open source (Apache-2.0) | Verified fact | A6-S089 |
| Strategic direction | Recent SPIRE releases add Slurm workload attestor, Azure Blob trust-bundle publishing, nested-agent bootstrap and Kubernetes attestation options | Verified fact | A6-S042 |
| What it does | SPIRE exposes the SPIFFE Workload API, attests running software and issues SPIFFE IDs and SVIDs to it, so workloads can establish mutual trust (e.g. mTLS or signed JWTs) and authenticate to secret stores, databases or cloud services; also implements Envoy SDS. | Verified fact | A6-S087 |
| Stack position | Workload identity layer beneath agent runtimes, gateways and MCP servers (machine identity rather than delegated user authority) | Verified fact | A6-S087 |
| Integration | SPIFFE Workload API and SDS API; X.509 and JWT SVIDs | Verified fact | A6-S042 |
| Dependencies | SPIRE server and agents; node attestors (e.g. Kubernetes PSAT, AWS IID) | Verified fact | A6-S042 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Third-party security audit by Cure53 (February 2021); CNCF security assessments 2018 and 2020 | Verified fact | A6-S087 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source | Verified fact | A6-S089 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | CNCF graduated; regular releases (1.15.1 May, 1.15.2 July, 1.15.3 August 2026) | Verified fact | A6-S087, A6-S042 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes (self-managed software) | | |

## Cedar policy language; Amazon Verified Permissions (managed Cedar); Policy in Amazon Bedrock AgentCore (Cedar-based) (`C4-cedar`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where AWS is your primary cloud and agents run on AgentCore Gateway (CP3 Q2, rubric rule 10). AgentCore Policy is AWS's lead managed policy service for agent tool calls, and its enforcement point (AgentCore Gateway) is now Strategic on the same condition in C1 and L4. OPA remains the cloud-neutral default; keep Cedar source in Git so policies stay portable [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Strong tool-call authorisation with partial evaluation and automated reasoning; no external lookups. |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1) for AgentCore Policy and Verified Permissions: platform controls presumed (CP2 Q1); confirm per service; Cedar library under rule 2. |
| Security and compliance | 4 | Cedar library hygiene verified (B-C4-S003); Amazon Bedrock AgentCore listed in AWS SOC 1/2/3 scope (GA features in scope unless excluded) and in ISO/IEC 27001 programmes [VF: B-C1-S005, B-C1-S006, B-L4-S002]; held at 4, not 5, for consistency with C1 and L4 (ISO wording partly garbled, FedRAMP unresolved). |
| Deployment flexibility | 4 | Cedar library anywhere; AgentCore Policy in 13 AWS regions incl. Ireland and GovCloud. |
| Ecosystem | 3 | AWS services and CNCF (per AWS); narrower than OPA. |
| Reliability and maturity | 3 | Cedar 4.x regular releases; AgentCore Policy GA March 2026; Dogwood new. |
| Cost / TCO | 4 | Cedar free; managed pricing transparent. |
| Lock-in / portability | 3 | Cedar open source, but enforcement tied to AgentCore Gateway and authoring moving to Dogwood. |
| **Total (generic / FS)** | **3.75 / 3.70** | |

*Evidence rules applied:* Rule 2 (self-hosted software / open specification): enterprise_readiness and security_compliance capped at 4; NPV cap not applied; inherits host controls (Cedar library part); CP3 review: AgentCore Policy security re-based on the AgentCore SOC and ISO evidence already logged by C1 and L4 (B-C1-S005, B-C1-S006, B-L4-S002); 3 to 4

**Capabilities.** Cedar policy language and engine (Apache-2.0; 4.13.0, 15 September 2026) for RBAC/ABAC with schema validation and automated-reasoning analysis; Amazon Verified Permissions (managed Cedar); Policy in Amazon Bedrock AgentCore (GA 3 March 2026, 13 Regions): deny-by-default evaluation of every gateway tool call on identity claims and arguments, denied tools filtered from tools/list, natural-language authoring, decisions logged to CloudWatch; policies now authored in Dogwood, an open-source Cedar superset [VF: A6-S044, A6-S045, A6-S026, A6-S104, V2-S033].

**Strengths**

- Deny-by-default tool-call authorisation with partial evaluation of tools/list [VF: A6-S026]
- Designed for automated reasoning over policy sets [VF: A6-S045]
- Transparent per-request pricing: US$0.000025 per authorisation request [VF: A6-S021]
- Security policy with 1-business-day acknowledgement and embargoed advisories [VF: B-C4-S003]

**Limitations and risks**

- Cedar cannot do external lookups at evaluation time; AWS recommends Lambda interceptors [VF: A6-S026]
- AgentCore Policy enforcement is tied to AgentCore Gateway [VF: A6-S026]
- Cedar 2 to 4 migration was breaking for Verified Permissions users [VF: A6-S104]
- Dogwood governance and licence not checked [NPV]
- AgentCore is in AWS SOC 1/2/3 scope and ISO/IEC 27001 programmes, but the ISO wording is partly garbled and FedRAMP status is unresolved [VF: B-C1-S005, B-C1-S006, B-L4-S002]

**Choose when**

- The agent estate runs on AWS AgentCore Gateway [AJ]
- You want analysable policies with a smaller language than Rego [AJ]

**Avoid when**

- You need runtime external data lookups in policy [AJ]
- You are multi-cloud and want one PDP (prefer OPA) [AJ]

**Nearest competitors:** C4-opa, Gateway-native policy (Kong)

**Regulated-FS note.** Review AI-generated policies before activation, keep the Cedar source in Git, and avoid Dogwood-only constructs where portability matters; platform controls presumed (CP2 Q1); confirm per service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Cedar project (cedar-policy GitHub organisation; created by AWS); AgentCore Policy by Amazon Web Services | Verified fact | A6-S045, A6-S026 |
| Category | Open-source authorisation policy language and engine; managed agent tool-call policy service (AgentCore Policy) | Verified fact | A6-S045, A6-S026 |
| Version / lineup | cedar-policy 4.13.0 (15 September 2026; Cedar language version 4.5); Policy in Amazon Bedrock AgentCore GA 3 March 2026 in 13 Regions (preview December 2025) | Verified fact | A6-S044, A6-S085, A6-S026, V2-S033 |
| Licence | Cedar: open source (Apache-2.0); AgentCore Policy: proprietary managed service | Verified fact | A6-S045, A6-S026 |
| Status events | 3 March 2026: Policy in Amazon Bedrock AgentCore generally available (Cedar-based); 6 April 2026: Amazon Verified Permissions adds policy store aliases and named policies/templates; from April 2026 authorisation APIs disabled for policy stores still on Cedar 2 (Cedar 4 required); May 2026: Verified Permissions aligned with Cedar, supports multiple namespaces; 6 August 2026: temporal policies and rate limiting announced for AgentCore | Verified fact | A6-S026, A6-S104, A6-S106, V2-S033 |
| Strategic direction | AWS uses Cedar as the deny-by-default authorisation layer for agent tool calls through AgentCore Gateway, with natural-language policy authoring, schema generation from MCP tool descriptions and automated-reasoning analysis of policy sets; current AgentCore documentation has policies authored in Dogwood, described by AWS as an open-source, Cedar-compatible policy language for AI agents (every valid Cedar policy is valid Dogwood); AWS says Cedar has joined the CNCF | Verified fact | A6-S026, A6-S074, V2-S033 |
| What it does | Cedar expresses RBAC and ABAC permissions (principal, action, resource, context) that are validated against a schema and designed for automated-reasoning analysis. AgentCore Policy attaches a Cedar policy engine to a Gateway; every agent-to-tool call is evaluated before execution using identity claims and tool arguments; denied tools are filtered from tools/list via partial evaluation; decisions are logged to CloudWatch. | Verified fact | A6-S045, A6-S026 |
| Stack position | Policy decision point for agent tool calls (inside the gateway) and for application authorisation | Verified fact | A6-S026 |
| Integration | Cedar Rust crate, WASM/TypeScript bindings, language server; AgentCore CreatePolicyEngine/CreatePolicy/StartPolicyGeneration APIs | Verified fact | A6-S045, A6-S085, A6-S074 |
| Dependencies | Cedar: Rust crates (WASM bindings for JavaScript); AgentCore Policy: AgentCore Gateway | Verified fact | A6-S045, A6-S085, A6-S074 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | AgentCore Policy GA in 13 AWS regions incl. Europe (Ireland); also AWS GovCloud (US-West) | Verified fact | A6-S026 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Cedar free. AgentCore Policy: US$0.000025 per authorisation request (first 100 temporal policies per engine no extra authorisation charge); US$0.13 per 1,000 input tokens for natural-language policy processing | Verified fact | A6-S021 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Cedar 4.x with regular releases (4.11.2 June, 4.12.0 July, 4.13.0 September 2026) | Verified fact | A6-S044 |
| Deployment | saas: Yes (AgentCore Policy managed service); managed_cloud: Yes (Amazon Verified Permissions); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Cedar library); on_prem: Not publicly verified | | |

## Auth0 for AI Agents; Okta for AI Agents; Okta Agent SSO (Cross App Access, XAA) (`C4-okta-auth0-ai-agents`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Okta is the workforce IdP; FS 3.55 is below the usual 3.6 because deployment scores 2 (SaaS only), accepted because agent identities must live in the same directory as the delegating humans [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Delegation, token vaulting, async human approval, fine-grained RAG authorisation and enterprise-managed MCP access. |
| Enterprise readiness | 4 | CP2 Q2 (rule 7): SSO (Agent SSO, core Okta SSO), a dedicated AI agent administrator role plus agent ownership and certification campaigns (RBAC), and System Log events for AI agents in reference documentation (audit), plus the System Log management API [VF: B-C4-S007, B-REVB-S001]; 4. Not 5: SLA and agent-specific SCIM not verified, and System Log retention is 90 days. |
| Security and compliance | 4 | ISO 27001:2022, SOC 2 Type II and FedRAMP at company level; product scope not stated (scope rule, 4). |
| Deployment flexibility | 2 | SaaS only (Okta and Auth0 clouds); private deployment not verified. |
| Ecosystem | 4 | XAA adopted as the MCP extension with named SaaS support; SDKs for Python and JavaScript frameworks. |
| Reliability and maturity | 3 | Core GA November 2025 to August 2026; SDKs changing fast. |
| Cost / TCO | 3 | XAA included in core SSO; Auth0 tiers published; Okta for AI Agents price not published. |
| Lock-in / portability | 3 | Proprietary platforms on open standards (OAuth, OIDC, CIBA, ID-JAG). |
| **Total (generic / FS)** | **3.65 / 3.55** | |

*Evidence rules applied:* CP3 review: earlier CP2 Q2 cap (audit only on a training page) lifted; System Log coverage of AI agents and the AI agent administrator role are in Okta reference documentation (B-REVB-S001)

**Capabilities.** Auth0 for AI Agents (GA 19 November 2025: user authentication, Token Vault, asynchronous authorisation via CIBA, FGA for RAG; Auth for MCP and OBO Token Exchange GA May 2026); Okta for AI Agents (GA 30 April 2026: discover, onboard, protect, govern agent identities); Okta Agent SSO / Cross App Access (GA 24 August 2026), the MCP Enterprise-Managed Authorization extension [VF: A6-S097, A6-S100, A6-S099, V2-S035].

**Strengths**

- Standards-based delegation: RFC 8693 token exchange, RFC 7523, ID-JAG, OpenID CIBA [VF: A6-S079, A6-S076]
- Agents in Universal Directory with human owners and access-certification campaigns [VF: B-C4-S007]
- XAA included in core Okta SSO; out-of-box support from Atlassian, Slack, Figma and others [VF: A6-S099]
- Company-level ISO 27001:2022, SOC 2 Type II and FedRAMP authorisations [VF: B-C4-S006]

**Limitations and risks**

- Auth0 AI SDKs flagged 'under heavy development'; @auth0/ai at major version 6 within about 13 months [VF: A6-S078, A6-S077]
- Okta Agent Gateway and Shadow AI Agent Discovery announced, not confirmed shipped [VF: A6-S100]
- System Log records AI agent events and a dedicated AI agent administrator role exists [VF: B-REVB-S001]; System Log retention is 90 days per Okta support, so export agent events to the firm's SIEM [VF: B-REVB-S001]
- Okta for AI Agents price not published; EU residency not verified [NPV]

**Choose when**

- Okta is the workforce IdP [AJ]
- Customer-facing or SaaS-integrated agents need Token Vault and CIBA approvals [AJ]

**Avoid when**

- Entra is the workforce IdP [AJ]
- You need a self-hosted IdP [AJ]

**Nearest competitors:** C4-entra-agent-id, C7-hashicorp-vault, C4-mcp-authorization

**Regulated-FS note.** Use XAA/ID-JAG for enterprise-managed MCP access, pin SDK versions, and confirm product scope of the SOC 2 and ISO certificates under NDA [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Okta, Inc. (Auth0 is an Okta product) | Verified fact | A6-S078, A6-S080 |
| Category | Identity and authorisation for AI agents (delegated access, async approval, fine-grained authorisation, enterprise-managed app-to-app access) | Verified fact | A6-S078, A6-S080 |
| Version / lineup | Auth0 for AI Agents GA 19 November 2025 (User Authentication, Token Vault, Asynchronous Authorization, FGA for RAG); May 2026 additions Auth for MCP and On-Behalf-Of Token Exchange GA; Okta for AI Agents GA 30 April 2026; Agent SSO / XAA GA 24 August 2026; SDKs auth0-ai 1.0.2 and @auth0/ai 6.0.2 | Verified fact | A6-S097, A6-S100, A6-S099, A6-S076, A6-S077, V2-S035 |
| Licence | Proprietary identity platforms; AI SDKs Apache-2.0 | Verified fact | A6-S076, A6-S077 |
| Status events | 19 November 2025: Auth0 for AI Agents GA; 30 April 2026: Okta for AI Agents GA; 24 August 2026: Okta Agent SSO (Cross App Access) GA, included in core Okta SSO | Verified fact | A6-S097, A6-S100, A6-S099, V2-S035 |
| Strategic direction | Cross App Access built on the IETF Identity Assertion Authorization Grant so the enterprise IdP mediates agent-to-app access; MCP standardised this as the Enterprise-Managed Authorization extension | Verified fact | A6-S080, A6-S079 |
| What it does | Auth0 AI SDKs: user authentication for agents, calling third-party APIs on users' behalf, authorisation for RAG (fine-grained), and asynchronous human approval using OpenID CIBA. Cross App Access: MCP client exchanges an enterprise ID token for an ID-JAG at the IdP, then for an access token at the MCP server's authorisation server. Auth0 Token Vault stores and brokers third-party API tokens (e.g. Google Drive, Jira, Slack) for agents; Okta for AI Agents discovers, onboards, protects and governs agent identities across frameworks and clouds. | Verified fact | A6-S078, A6-S076, A6-S080, A6-S079, A6-S097, A6-S100 |
| Stack position | Identity provider / authorisation server for agents and MCP servers | Verified fact | A6-S079 |
| Integration | OAuth 2.0 / OIDC, OpenID CIBA, RFC 8693 token exchange and RFC 7523 JWT grant (ID-JAG); SDKs for Python and JavaScript agent frameworks | Verified fact | A6-S076, A6-S079, A6-S078 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Okta Agent SSO (XAA) included in core Okta SSO at no additional cost; Okta for AI Agents is a separate subscription (price not published). Auth0: Token Vault connections by plan (Free 2; Essentials/Professional 3 plus add-on; Enterprise 4 plus add-on); Free US$0 up to 25,000 MAU, Professional US$240/month (pricing page may be stale) | Verified fact | A6-S099, A6-S098 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | XAA out-of-the-box support includes Anthropic (Claude), Asana, Atlassian, Canva, Datadog, Figma, Glean, Linear, Notion, Slack, Supabase; XAA incorporated as the MCP Enterprise-Managed Authorization extension | Verified fact | A6-S099, A6-S035 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Core products GA (November 2025 to August 2026); Auth0 AI SDKs still flagged 'under heavy development'; Okta Agent Gateway and Shadow AI Agent Discovery announced for Q3 2026 (not confirmed shipped); Auth0 Agent Gateway in beta | Verified fact | A6-S097, A6-S099, A6-S100, A6-S078, V2-S035 |
| Deployment | saas: Yes (Okta and Auth0 cloud identity services); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Microsoft Entra Agent ID (`C4-entra-agent-id`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: where Entra is the workforce IdP; FS 3.50 is below the usual 3.6 because deployment and cost score 2, accepted because agent identity must live in the same directory as the delegating humans [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Blueprints, agent identities, OBO and autonomous flows, Conditional Access, governance, ID Protection and audit for agents. |
| Enterprise readiness | 4 | Hyperscaler presumption (CP2 Q1): platform controls presumed (CP2 Q1); confirm per service; access controls and audit logs for agents also verified (A6-S058). |
| Security and compliance | 4 | Entra ID in ISO 27001 (commercial) and FedRAMP High scope; commercial SOC 2 scope does not name it; Agent ID and Agent 365 not named separately (scope rule, 4). |
| Deployment flexibility | 2 | Microsoft cloud service only. |
| Ecosystem | 4 | Guides for Bedrock and n8n agents, MCP and A2A, workload identity federation. |
| Reliability and maturity | 3 | GA April 2026; parts still preview. |
| Cost / TCO | 2 | Agent 365 licence needed for security features; prices not verified. |
| Lock-in / portability | 3 | Standard OAuth/OIDC tokens, but proprietary agent constructs and licensing. |
| **Total (generic / FS)** | **3.55 / 3.50** | |

**Capabilities.** Agent identity platform in Microsoft Entra: agent identity blueprints, agent identities, agent users, owners/sponsors/managers; OAuth client_credentials for autonomous agents, jwt-bearer On-Behalf-Of, refresh_token for long-running delegated work, no interactive flows; Conditional Access, ID Governance access packages, ID Protection, network controls and sign-in/audit logs extended to agents; supports MCP, A2A and non-Microsoft agents via sidecar SDK or workload identity federation [VF: A6-S057, A6-S058, A6-S060]. GA April 2026 [VF: V2-S032].

**Strengths**

- Agent identity in the same directory as the human principals, so OBO delegation and Conditional Access apply natively [AJ]
- Explicit sponsor/owner model and access packages for agents [VF: A6-S057, A6-S058]
- Standard OAuth flows; no interactive flows for agent entities [VF: A6-S060]
- Entra ID in ISO 27001 and FedRAMP High scope [VF: B-C4-S008, A6-S056]

**Limitations and risks**

- Security features (Conditional Access, ID Protection, governance) for agents need Microsoft Agent 365 licences (included in E7; add-on to E5/A5/Business Premium) [VF: A6-S059, V2-S032]
- Microsoft-specific constructs (blueprints, agent users) [VF: A6-S057]
- Some admin-centre wizards still preview; registry converging into Agent 365 [VF: A6-S058]
- Agent 365 list prices not verified [NPV]

**Choose when**

- Entra is the workforce IdP [AJ]
- Copilot Studio or Foundry agents are in the estate [AJ]

**Avoid when**

- Okta is the workforce IdP and Entra would be a second identity plane [AJ]

**Nearest competitors:** C4-okta-auth0-ai-agents, C7-hashicorp-vault, Amazon Bedrock AgentCore Identity

**Regulated-FS note.** Register every agent with a named sponsor, use OBO for user-initiated work, and budget Agent 365 licensing before relying on Conditional Access for agents; platform controls presumed (CP2 Q1); confirm per service [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Microsoft | Verified fact | A6-S057 |
| Category | Agent identity platform within Microsoft Entra (identity provider for AI agents) | Verified fact | A6-S057 |
| Version / lineup | Generally available (Entra release log lists GA under April 2026; What's new page dated 1 May 2026); some admin-centre creation wizards still preview | Verified fact | A6-S058, V2-S032 |
| Licence | Proprietary; Agent ID available to all Microsoft Entra customers; Entra security features for agents require Microsoft Agent 365 licences | Verified fact | A6-S059 |
| Status events | April 2026: Entra Agent ID generally available (Entra release log); agent registry converging under Microsoft Agent 365 | Verified fact | A6-S058, V2-S032 |
| Strategic direction | Identity foundation for Microsoft Agent 365 (agent registry converging there); extends Zero Trust controls to agents; supports non-Microsoft agents (AWS Bedrock, GCP, n8n) via Entra ID Auth SDK sidecar or workload identity federation | Verified fact | A6-S058, A6-S057 |
| What it does | Creates and manages agent identities from agent identity blueprints (parent-child templates), agent service principals and agents' user accounts with owners, sponsors and managers; applies Conditional Access, ID Governance (access packages for OBO and autonomous scenarios), ID Protection (risky agents), network controls and sign-in/audit logs to agents. | Verified fact | A6-S057, A6-S058 |
| Stack position | Identity provider and authorisation server for agents; sits beside the agent runtime and tool layer | Verified fact | A6-S057 |
| Integration | OAuth 2.0 with Federated Identity Credentials: client_credentials for autonomous agents, jwt-bearer for On-Behalf-Of delegation, refresh_token for long-running user-delegated work; no interactive flows for agent entities; supports MCP and A2A | Verified fact | A6-S060, A6-S057 |
| Dependencies | Microsoft Entra tenant; Microsoft Agent 365 licences for security features | Verified fact | A6-S059 |
| Certifications | Microsoft Entra ID (P1/P2) and Entra ID Governance in Azure FedRAMP High scope (Agent ID not listed separately) | Verified fact | A6-S056 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Conditional Access for agents; access packages; sponsor lifecycle workflows; sign-in and audit logs for agents | Verified fact | A6-S058 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Agent ID included for Entra customers; Agent 365 per-user licence required for security extensions (included in Microsoft 365 E7); list prices not verified | Verified fact | A6-S059 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Guides for securing Amazon Bedrock and n8n agents; migration of Copilot Studio agents and custom app registrations | Verified fact | A6-S058 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | GA in April 2026 after preview (announced at Microsoft Build 2025); documentation marks some features as new or preview | Verified fact | A6-S058, V2-S032 |
| Deployment | saas: Yes (Microsoft Entra cloud service); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## MCP Authorization (MCP specification 2026-07-28) plus Enterprise-Managed Authorization extension (`C4-mcp-authorization`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic, conditional: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions. Tier set by the reader at Checkpoint 3 (CP3 Q1): MCP (L4-mcp) and its authorisation profile are one decision. FS 3.45 and reliability 2 (IETF drafts, four breaking revisions) are why the condition includes pinning the specification revision at the gateway. Conflict of interest: MCP originated at Anthropic and the author is an Anthropic model [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Strong agent-to-tool contract (audience binding, PRM, issuer validation, EMA); optional and silent on fine-grained policy. |
| Enterprise readiness | 3 | Rule 2: EMA lets the corporate IdP govern access; enterprise features come from implementations. |
| Security and compliance | 3 | Rule 2 hygiene: private advisory reporting and documented trust model (B-C4-S004); optional authorisation and draft dependencies keep it at 3. |
| Deployment flexibility | 4 | Implementation-dependent; usable in self-hosted and managed gateways. |
| Ecosystem | 4 | Implemented by AWS AgentCore Gateway, Kong AI Gateway, Okta XAA and Azure API Management; MCP itself is the de facto tool protocol (L4 scores it 5), but authorisation is optional and adoption of the authorisation profile across servers is not publicly verified, so 4. |
| Reliability and maturity | 2 | Four breaking revisions in about 16 months; OAuth 2.1 still draft. |
| Cost / TCO | 4 | Free specification; implementation and re-certification on each revision cost effort. |
| Lock-in / portability | 4 | Open specification under Linux Foundation hosting; maintainer concentration at one vendor. |
| **Total (generic / FS)** | **3.50 / 3.45** | |

*Evidence rules applied:* Rule 2 (self-hosted software / open specification): enterprise_readiness and security_compliance capped at 4; NPV cap not applied; inherits host controls

**Capabilities.** Authorisation profile of OAuth 2.1 (still an IETF draft) for MCP: server as resource server with Protected Resource Metadata (RFC 9728), PKCE, audience-bound tokens via Resource Indicators (RFC 8707), token passthrough forbidden; 2026-07-28 adds RFC 9207 issuer validation and issuer-bound clients and deprecates Dynamic Client Registration; Enterprise-Managed Authorization (ID-JAG) extension Stable. Authorisation is OPTIONAL [VF: A6-S033, A6-S034, A6-S032, A6-S035, A6-S079].

**Strengths**

- Audience binding and the ban on token passthrough address the confused-deputy problem [VF: A6-S034]
- Enterprise IdP decides which MCP servers an employee can use (EMA/ID-JAG) [VF: A6-S035, A6-S079]
- Implemented by AgentCore Gateway, Kong and Okta XAA [VF: A6-S021, A6-S017, A6-S099]
- Hosted by the Agentic AI Foundation (Linux Foundation) since 9 December 2025 [VF: A3-S018]

**Limitations and risks**

- Authorisation is OPTIONAL in MCP [VF: A6-S033]
- Frequent breaking revisions: 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28 [VF: A6-S033, A6-S021]
- Several dependencies are IETF drafts, including OAuth 2.1 [VF: A6-S033, A6-S079]
- Both Lead Maintainers are Anthropic staff [VF: A3-S082]; the author is an Anthropic model (conflict of interest)
- Security policy states clients trust configured servers and that access control is the server developer's responsibility [VF: B-C4-S004]

**Choose when**

- MCP is the firm's tool protocol [AJ]

**Avoid when**

- Tools are exposed as REST/OpenAPI behind a gateway, where plain OAuth 2.0 resource-server patterns suffice [AJ]

**Nearest competitors:** Gateway-native tool auth (Kong, AgentCore Gateway, Azure APIM credential manager), C4-okta-auth0-ai-agents, OAuth 2.0 resource-server pattern for REST tools

**Regulated-FS note.** Strategic, conditional, and mandatory wherever MCP is used (CP3 Q1): make authorisation mandatory by firm policy, pin the spec revision at the gateway, and require EMA so the corporate IdP mediates access; the durable controls are the IdP and the gateway PDP, which keep working if the tool protocol changes [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Model Context Protocol project (specification and extensions published in modelcontextprotocol GitHub organisation) | Verified fact | A6-S032, A6-S079 |
| Category | Open specification (authorisation profile of OAuth 2.1 for agent-to-tool access) | Verified fact | A6-S033 |
| Version / lineup | Specification revision 2026-07-28 (previous 2025-11-25); Enterprise-Managed Authorization extension status 'Stable'; Python SDK mcp 2.3.0 (2 October 2026) | Verified fact | A6-S032, A6-S079, A6-S086, V2-S031 |
| Licence | Open specification | Verified fact | A6-S033 |
| Status events | 28 July 2026: MCP specification revision 2026-07-28 published; OAuth Dynamic Client Registration deprecated as a registration mechanism | Verified fact | A6-S032, V2-S031 |
| Strategic direction | Hardening for enterprise use: RFC 9207 issuer validation, issuer-bound client registration, Client ID Metadata Documents replacing Dynamic Client Registration, enterprise IdP control via ID-JAG; feature lifecycle policy with 12-month deprecation window; 2026-07-28 also makes the protocol stateless (no initialize handshake), removes SSE stream resumability, and deprecates the Roots, Sampling and Logging features | Verified fact | A6-S032, A6-S035, V2-S031 |
| What it does | Defines how MCP clients obtain and present access tokens to protected MCP servers: MCP server is an OAuth 2.1 resource server; MUST publish Protected Resource Metadata (RFC 9728); clients MUST use PKCE and Resource Indicators (RFC 8707) so tokens are audience-bound; servers MUST reject tokens not issued for them (token passthrough forbidden). The Enterprise-Managed Authorization extension lets the corporate IdP decide which MCP servers an employee can use via an Identity Assertion JWT Authorization Grant. | Verified fact | A6-S033, A6-S034, A6-S035, A6-S079 |
| Stack position | Authorisation contract between agents (MCP clients), MCP servers and identity providers; the standards basis for an agent identity/authorisation sub-layer | Verified fact | A6-S033, A6-S035 |
| Integration | HTTP Authorization bearer header on every request; WWW-Authenticate resource_metadata discovery; scope challenge handling | Verified fact | A6-S033 |
| Dependencies | OAuth 2.1 (draft-ietf-oauth-v2-1-13), RFC 8414, RFC 7591 (deprecated path), RFC 8707, RFC 9728, RFC 9207, draft-ietf-oauth-client-id-metadata-document-00; extension uses draft-ietf-oauth-identity-assertion-authz-grant, RFC 8693, RFC 7523 | Verified fact | A6-S033, A6-S079 |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open specification | Verified fact | A6-S033 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Implemented by gateways: AWS AgentCore Gateway supports MCP 2026-07-28; Kong AI Gateway 2.1.0 supports 2026-07-28; Okta Cross App Access sample uses ID-JAG; Okta states XAA is 'formally incorporated as the official Enterprise-Managed Authorization extension' for MCP | Verified fact | A6-S021, A6-S017, A6-S080, A6-S099 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Authorisation is OPTIONAL in MCP; several underlying documents are IETF drafts; frequent breaking revisions (2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28) | Verified fact | A6-S033, A6-S021 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

# C5: Prompt and configuration management

## LangSmith prompt management (Prompts, Prompt Hub) (`C5-langsmith-prompts`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strategic only in a LangSmith/LangGraph estate, with GitHub sync enabled as the exit route; otherwise Tactical [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Commits, diffs, environments, promotion, rollback history, owners, webhooks and Git sync; no documented percentage rollout or user segmentation. |
| Enterprise readiness | 4 | Organisation and workspace roles, custom RBAC and per-prompt owners; Enterprise SSO, ABAC and support SLA from the platform record; SCIM not documented. |
| Security and compliance | 4 | SOC 2 Type II, ISO 27001:2022, HIPAA BAA on Enterprise; no CMK/BYOK documented, so not 5. |
| Deployment flexibility | 5 | SaaS in US, EU and APAC regions, BYOC on AWS, self-hosted and air-gapped self-host on Enterprise. |
| Ecosystem | 4 | LangChain ecosystem, langchain-prompty integration, webhooks and GitHub sync. |
| Reliability and maturity | 4 | GA since 2023, independent and funded (US$125M Series B, October 2025). |
| Cost / TCO | 3 | Per-seat plus per-trace pricing; heavy self-host footprint. |
| Lock-in / portability | 3 | Proprietary service, but prompt text syncs to GitHub, so lock-in is lower than for LangSmith traces (L9 scores 2). |
| **Total (generic / FS)** | **4.00 / 3.95** | |

**Capabilities.** Prompts stored as a commit history with diffs; reserved Staging and Production environments assigned by promotion; per-environment rollback history; 'owners only' mode restricting who may tag, promote or delete; webhooks on every commit; synchronisation of prompts with a GitHub repository; public prompt hub [VF: A7-S076].

**Strengths**

- The most complete change-control workflow among the registries profiled: commits, diffs, promotion, rollback history and prompt owners [VF: A7-S076] [AJ]
- GitHub synchronisation gives a documented export path and lets Git remain the record [VF: A7-S076]
- Webhooks on commit can trigger CI evaluation and change tickets [VF: A7-S076]
- SOC 2 Type II, ISO 27001:2022 and HIPAA; US, EU (Netherlands) and APAC regions; BYOC on AWS, self-host and air-gapped self-host on Enterprise [VF: A7-S077, A1-S036, A1-S126, A1-S034]

**Limitations and risks**

- Proprietary service for prompt storage and promotion [VF: A7-S076, A7-S079]
- No EU legal entity for contracting [VF: A7-S077]
- Self-hosting is an Enterprise add-on with a heavy footprint (Kubernetes, PostgreSQL, Redis, ClickHouse) [VF: A7-S079, A1-S034]
- Platform increasingly bundles the LangChain agent runtime [VF: A1-S039]

**Choose when**

- LangSmith is already the L9 platform and LangGraph the orchestration standard [AJ]
- Product owners need a UI promotion and rollback workflow while engineering keeps Git as the record via sync [AJ]

**Avoid when**

- You want the prompt registry separated from the agent runtime vendor [AJ]
- Contracting with an EU legal entity is a requirement [AJ]

**Nearest competitors:** C5-langfuse-prompts, C5-promptlayer, C5-prompts-as-code

**Regulated-FS note.** Enable owners-only mode on production prompts, route promotion through a service identity triggered after the eval gate, and use GitHub sync so that the approved prompt text also lives in the firm's repository [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LangChain, Inc. | Verified fact | A7-S076, A7-S011 |
| Category | Prompt management within an LLM observability, evaluation and deployment platform | Verified fact | A7-S076, A7-S078 |
| Version / lineup | langsmith Python SDK 0.14.4 released 2 October 2026 (platform is a continuously deployed SaaS) | Verified fact | A7-S011 |
| Licence | Proprietary platform (self-hosting is an Enterprise add-on); langsmith SDK MIT | Verified fact | A7-S079, A7-S011 |
| Strategic direction | Prompt workflow modelled on commits: environments (Staging/Production) as reserved commit tags, promotion UI, prompt owners, webhooks on commit and synchronisation of prompts with a GitHub repository | Verified fact | A7-S076 |
| What it does | Stores prompts as a commit history with diffs; commit tags and the reserved 'staging' and 'production' tags mark which version is live in each environment. 'Owners only' mode restricts who can tag, promote or delete a prompt. Webhooks fire on each commit, and a public prompt hub offers community prompts. | Verified fact | A7-S076 |
| Stack position | Control-plane capability (C5) inside the L9 LangSmith platform; the graphic shows LangSmith only as 'trace & eval' | Verified fact | A7-S076 |
| Integration | LangSmith UI, API and SDK; webhooks on prompt commit; GitHub synchronisation | Verified fact | A7-S076 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type 2; HIPAA compliant; GDPR | Verified fact | A7-S077 |
| GDPR / residency | SaaS regions: US (GCP us-central1), EU (GCP europe-west4, Netherlands), APAC (GCP australia-southeast1, from May 2026), US on AWS (us-east-2, from April 2026). No EU legal entity for contracting. | Verified fact | A7-S077, A7-S078 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Organisation and workspace roles, custom RBAC roles, personal access tokens; per-prompt owners | Verified fact | A7-S080, A7-S076 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | langsmith SDK first published on PyPI 26 June 2023 | Verified fact | A7-S011 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Enterprise add-on, Kubernetes); on_prem: Not publicly verified | | |

## Langfuse Prompt Management (a capability of the Langfuse platform) (`C5-langfuse-prompts`)

**Tier:** Strategic · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* Strategic only where Langfuse is the L9 platform of record and the Enterprise licence is bought for protected labels, RBAC and audit logs; otherwise Tactical [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Versions, environment/tenant/experiment labels, client caching, loud failure on missing labels and trace linkage; no documented approval workflow, Git sync or percentage rollout. |
| Enterprise readiness | 4 | Rule 7, aligned with the CP2 rework of L9 Langfuse (4): SSO, project-level RBAC, audit logs, SCIM and the Org Management API verified [VF: A7-S074, A1-S033]; Enterprise-licensed when self-hosted, which is a stated condition of the tier; SLA terms not published. |
| Security and compliance | 4 | SOC 2 Type II and ISO 27001 with annual audits, DPA, EU region on Cloud; no CMK/BYOK documented, so not 5. |
| Deployment flexibility | 4 | SaaS (US, EU, JP, HIPAA regions), self-hosted in any region and fully offline; kept at 4 for consistency with L9 because vendor-managed BYOC is not documented (see scoring notes). |
| Ecosystem | 4 | Open-source SDKs in Python and JS/TS, OTel-based platform, wide adoption of the parent platform; prompt API is Langfuse-specific. |
| Reliability and maturity | 4 | Platform at v4, frequent SDK releases (4.17.0 on 5 October 2026); ownership changed to ClickHouse in January 2026 with no planned licence change. |
| Cost / TCO | 4 | MIT core free; the governance controls this control needs are in the paid Enterprise tier. |
| Lock-in / portability | 3 | Base 4 (MIT, self-hostable, prompts are text) reduced by 1 for the 2026 ownership change. |
| **Total (generic / FS)** | **3.95 / 3.85** | |

*Evidence rules applied:* CP3 review: enterprise readiness raised from 3 to 4 to match the CP2-reworked L9 Langfuse score (rule 7: all three controls plus SCIM and an admin API)

**Capabilities.** Prompt registry inside the Langfuse platform: every prompt version gets an immutable version ID; labels (production, staging, tenant or experiment) select which version the SDK fetches; SDKs cache prompts client-side; prompt versions are linked to traces so quality and cost can be analysed by version; protected prompt labels restrict who may move a production label (Enterprise) [VF: A7-S071, A7-S072, A7-S074].

**Strengths**

- Version-to-trace linkage answers 'which prompt version produced this output' inside the same store that holds the evaluation evidence (see L9) [VF: A7-S071]
- Client-side SDK caching keeps the registry off the hot path [VF: A7-S071, A7-S072]
- A missing label returns an error rather than silently serving another version, so a mislabelled environment fails loudly [VF: A7-S072]
- MIT core; self-hosted or Cloud with SOC 2 Type II, ISO 27001 and an EU (Ireland) region [VF: A7-S073, A7-S074]

**Limitations and risks**

- Protected prompt labels, project-level RBAC, audit logs and SCIM need an Enterprise licence key when self-hosted, so segregation of duties on production prompts is a paid feature [VF: A7-S074]
- No native pull-request style approval or Git synchronisation documented in the fact base [NPV]
- Owned by ClickHouse (acquisition announced 16 January 2026) [VF: A7-S075, V2-S041]
- Langfuse-specific prompt API and SDK [VF: A7-S072]

**Choose when**

- Langfuse is already the L9 platform of record and you want prompt versions and traces in one place [AJ]
- You need a self-hosted registry inside the estate [AJ]

**Avoid when**

- You will not buy the Enterprise licence, because without protected labels any project member with write access can move the production label [AJ]
- Your change process requires approvals to happen in the source-control system [AJ]

**Nearest competitors:** C5-langsmith-prompts, C5-promptlayer, C5-prompts-as-code

**Regulated-FS note.** Use as the runtime delivery and trace-linkage layer, fed by CI from Git after the eval gate; make the production label protected and restrict label moves to the release pipeline's identity [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Langfuse (part of ClickHouse, Inc. since January 2026, per the Langfuse README; LICENSE copyright 'ClickHouse, Inc.') | Verified fact | A7-S075, V2-S041 |
| Category | Prompt management / prompt registry (feature of an open-source LLM engineering platform) | Verified fact | A7-S071 |
| Version / lineup | Docs labelled 'Version: v4'; Python SDK langfuse 4.17.0 released 5 October 2026 | Verified fact | A7-S009, A7-S074 |
| Licence | Open core: core features (including prompt management) MIT; 'Protected Prompt Labels', project-level RBAC, audit logs, SCIM and data-retention policies require an Enterprise licence key (ee folders) | Verified fact | A7-S074, A7-S075 |
| Status events | 16 January 2026: ClickHouse announced its acquisition of Langfuse alongside a US$400m Series D; Langfuse states no planned licensing changes (closing date not stated) | Verified fact | A7-S075, V2-S041 |
| Strategic direction | Positions prompt management as decoupling prompt updates from code deployment so non-engineers can change prompts in the UI; prompts linked to traces to analyse performance by prompt version | Verified fact | A7-S071 |
| What it does | Stores, versions and serves prompts centrally instead of hard-coding them. Each prompt version gets a version ID; labels (e.g. production, staging, tenant or experiment labels) select which version the SDK fetches. SDKs cache prompts client-side, so retrieval adds no network latency on the hot path. | Verified fact | A7-S071, A7-S072 |
| Stack position | Control-plane capability (C5) embedded in the L9 observability platform; prompt versions are linked to traces. The original graphic shows Langfuse only in L9 and has no prompt-management layer. | Verified fact | A7-S071 |
| Integration | Langfuse SDKs (e.g. Python create_prompt/update_prompt, fetch by label) and UI; prompts cached by SDK | Verified fact | A7-S071, A7-S072 |
| Dependencies | Same infrastructure as Langfuse Cloud when self-hosted: Postgres, ClickHouse, Redis and S3-compatible object storage; Langfuse Cloud runs on AWS and ClickHouse Cloud | Verified fact | A7-S073, A7-S074 |
| Certifications | SOC 2 Type II and ISO 27001 (annual audits), external penetration tests, HIPAA-ready region; reports on request | Verified fact | A7-S073 |
| GDPR / residency | GDPR compliant; DPA available; Langfuse Cloud regions US (us-west-2), EU (eu-west-1 Ireland), JP (ap-northeast-1) and HIPAA (us-west-2); self-hosted in any region | Verified fact | A7-S073 |
| Security features | Encryption, project-scoped tenant isolation with RBAC checks before queries, masking, data retention and deletion controls | Verified fact | A7-S073 |
| Access controls | Project-level RBAC roles, protected prompt labels (restricting who can change production labels), audit logs, SCIM and Org Management API are Enterprise (licence-key) features when self-hosted | Verified fact | A7-S074 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Self-hosting runs the same stack as the cloud service (Postgres, ClickHouse, Redis, object storage); 'no scalability limitations between the different versions' | Verified fact | A7-S074 |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | langfuse Python package first published on PyPI 12 July 2023; latest 4.17.0 (5 October 2026) | Verified fact | A7-S009, V2-S028 |
| Maturity | Platform at major version 4 (docs); SDK releases frequent (4.17.0 on 5 October 2026) | Verified fact | A7-S009, A7-S074 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes (self-hosted can run fully offline/air-gapped) | | |

## Prompts-as-code pattern: Git-versioned prompt files (Prompty, Dotprompt) tested by config-driven evals (e.g. Promptfoo) (`C5-prompts-as-code`)

**Tier:** Strategic · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* The only option whose change record lives in the firm's own controls and survives any vendor exit; the Acquired flag refers to Promptfoo as the example eval CLI, which is replaceable [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Versioning, review, diff and CI evaluation are strong; runtime delivery, segmentation, instant rollback and trace linkage have to be built. |
| Enterprise readiness | 4 | Rubric rule 2: scored on what the pattern enables in-estate. It inherits the firm's source-control SSO, RBAC, mandatory approvals and audit; scored at the rule 2 maximum of 4 (no commercial support for the formats) because approval and audit are the whole function of this control, unlike OPA or OpenLineage (3). |
| Security and compliance | 3 | Rubric rule 2: clear permissive licences; security policies, signed releases and CVE handling for the format libraries not verified; inherits host controls. |
| Deployment flexibility | 5 | Files in the customer's repository; runs anywhere, including air-gapped. |
| Ecosystem | 3 | Two vendor-originated formats plus CLI tooling, langchain-prompty and LangSmith GitHub sync; no single standard. |
| Reliability and maturity | 3 | Git practice is mature; the formats are young (Prompty v2, Dotprompt 0.2.0) and Promptfoo is pre-1.0 and changing ownership. |
| Cost / TCO | 4 | Free and open source; engineering effort to build runtime delivery and trace linkage. |
| Lock-in / portability | 4 | Base 5 (plain files under customer control, permissive licences) reduced by 1 because the example eval tool's ownership is changing and the formats are not under neutral governance. |
| **Total (generic / FS)** | **3.60 / 3.65** | |

*Evidence rules applied:* Rubric rule 2 (self-hosted libraries and open formats): enterprise readiness and security scored on what the pattern enables and on project hygiene, each capped at 4; inherits host controls

**Capabilities.** Prompts as files in the application repository: Prompty (.prompty, markdown with YAML front matter for model, connection and template settings) or Dotprompt (executable Handlebars-based templates, language- and provider-agnostic); changes go through code review and CI, where a CLI such as Promptfoo evaluates the prompt files [VF: A7-S067, A7-S066, A7-S068].

**Strengths**

- Uses the firm's existing change-management controls (review, approval, branch protection, release tagging) without a new vendor [AJ]
- Open formats with permissive licences: Prompty MIT, Dotprompt Apache-2.0, Promptfoo MIT [VF: A7-S008, A7-S065, A7-S068]
- Multi-language runtimes: Prompty for Python, TypeScript, Rust and C#; Dotprompt for JS/TS, Python, Go, Rust and Java [VF: A7-S067, A7-S066]
- One artefact can carry prompt, model and parameter settings, so the release pins them together [VF: A7-S067] [AJ]

**Limitations and risks**

- No runtime label switching, segmentation or instant rollback without a deployment; trace linkage must be built [AJ]
- Two competing formats, both pre-1.0 or recently re-versioned (Dotprompt Python 0.2.0; Prompty v2) [VF: A7-S065, A7-S067]
- Promptfoo: OpenAI announced its acquisition on 9 March 2026, closing date not published; Promptfoo states it is part of OpenAI [VF: A7-S068, V2-S042]
- Non-engineers cannot change prompts without a pull request, which is a feature for control and a cost for agility [AJ]

**Choose when**

- Always, as the system of record for approved prompts and configuration in a regulated firm [Rec]

**Avoid when**

- As the only mechanism when business users must test prompt variants daily; pair it with a registry that CI publishes to [AJ]

**Nearest competitors:** C5-langsmith-prompts, C5-langfuse-prompts, C5-promptlayer

**Regulated-FS note.** Make the repository the change record that model-risk and audit teams inspect: pull-request approval by a second person, CODEOWNERS for the risk owner, eval results attached to the PR, and a signed release tag pinning prompt, model and retrieval versions [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Pattern; formats from Microsoft (Prompty), Google (Dotprompt); Promptfoo is now part of OpenAI | Verified fact | A7-S067, A7-S066, A7-S068, V2-S042 |
| Category | Named pattern and open file formats | Verified fact | A7-S067, A7-S066 |
| Version / lineup | Prompty v2 (Python prompty 2.0.2, 16 September 2026; runtimes for Python, TypeScript, Rust, C#); Dotprompt (Python dotpromptz 0.2.0, 5 October 2026; JS/TS, Python, Go, Rust, Java); promptfoo 0.124.0 on npm (6 October 2026) | Verified fact | A7-S008, A7-S067, A7-S065, A7-S066, A7-S069 |
| Licence | Open source: Prompty MIT; Dotprompt Apache-2.0; Promptfoo MIT | Verified fact | A7-S008, A7-S065, A7-S068 |
| Status events | Promptfoo 'is now part of OpenAI' and 'remains open source and MIT licensed' (README); OpenAI announced its agreement to acquire Promptfoo on 9 March 2026 (terms undisclosed; closing date not published) | Verified fact | A7-S068, A7-S022, V2-S042 |
| Strategic direction | Prompty v2 aligns the .prompty format across runtimes with generated model types and conformance vectors; Dotprompt ships IDE extensions and editors; Promptfoo remains open source after joining OpenAI | Verified fact | A7-S067, A7-S066, A7-S068 |
| What it does | Prompts live as files in the application repository: .prompty is a markdown format with YAML front matter for model, connection and template settings; Dotprompt is an executable prompt template format extending Handlebars, agnostic to language and model provider. Changes go through code review and CI, where a CLI such as promptfoo runs evaluations against the prompt files. | Verified fact | A7-S067, A7-S066, A7-S068 |
| Stack position | Alternative or complement to registry-based C5 tools: Git is the system of record and release follows the software change process | Architectural judgement |  |
| Integration | Libraries in multiple languages, VS Code extension (Prompty), IDE/editor plug-ins (Dotprompt), promptfoo CLI via npm, brew or pip (Python wrapper promptfoo 0.2.0, 18 September 2026) | Verified fact | A7-S067, A7-S066, A7-S068, A7-S095 |
| Dependencies | Source control and CI; language runtime packages for the chosen format | Verified fact | A7-S067, A7-S066 |
| Certifications | Not applicable (pattern and open formats) | Architectural judgement |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open-source formats and tools | Verified fact | A7-S008, A7-S065, A7-S068 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | LangSmith documents synchronising prompts with a GitHub repository, bridging registry and Git approaches; langchain-prompty integration package exists | Verified fact | A7-S076 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Not applicable (pattern); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (files in the customer's repository); on_prem: Not publicly verified | | |

## PromptLayer (Prompt Registry) (`C5-promptlayer`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strong identity controls and rollout features, but security evidence is vendor-stated, pricing is unverified and it duplicates the registry built into the L9 platforms [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Versioned registry, release labels, staged rollout, segmentation and A/B testing, evals and tracing; approval workflow not documented. |
| Enterprise readiness | 4 | SSO, SCIM, group-role mapping, SSO enforcement, audit log and granular RBAC verified on Enterprise; SLA not verified. |
| Security and compliance | 3 | Vendor-stated SOC 2 Type 2 with a DPA committing to annual SOC 2 Type II audits and penetration tests; no ISO 27001; report not seen. |
| Deployment flexibility | 4 | SaaS, customer AWS account and self-hosted (Enterprise); air-gap and on-premises not verified. |
| Ecosystem | 3 | REST API, Python/JS SDKs, OTel tracing for major provider SDKs, webhooks; smaller ecosystem than the platform vendors. |
| Reliability and maturity | 3 | Independent, continuous releases on the 1.5.x SDK line since 2022; funding not verified. |
| Cost / TCO | 2 | Pricing not publicly verified; self-hosting and identity features need an Enterprise contract. |
| Lock-in / portability | 3 | Proprietary template API, but templates are text retrievable by API; no Git sync documented. |
| **Total (generic / FS)** | **3.40 / 3.40** | |

**Capabilities.** Prompt Registry with versioned templates; release labels (e.g. 'prod') select the served version and support staged rollouts, user segmentation and A/B testing via dynamic release labels; SDK fetches templates and can proxy provider calls for logging; evals and OpenTelemetry tracing alongside [VF: A7-S004, A7-S088].

**Strengths**

- Release labels support staged rollout and segmentation of users to prompt versions, closest to feature-flag practice among the registries [VF: A7-S088]
- Enterprise Identity: SSO (SAML/OIDC via WorkOS), SCIM, group-to-role mapping, SSO enforcement, org-scoped audit log and granular RBAC [VF: A7-S086]
- Deployable into the customer's AWS account or self-hosted on Enterprise [VF: A7-S085, A7-S087]
- Independent; no acquisition found [VF: A7-S004]

**Limitations and risks**

- SOC 2 Type 2 is a vendor statement; no report or ISO 27001 seen [VF: B-C5-S003]
- Pricing and EU region not publicly verified [NPV]
- Proprietary template API; no Git synchronisation documented [VF: A7-S004] [NPV]
- Small vendor; funding not publicly verified [NPV]

**Choose when**

- You want a standalone, model- and framework-neutral prompt registry with segmentation, and can run it in your own AWS account [AJ]

**Avoid when**

- ISO 27001 is a procurement gate [AJ]
- You already run Langfuse or LangSmith as the L9 platform, which would duplicate the registry [AJ]

**Nearest competitors:** C5-langfuse-prompts, C5-langsmith-prompts, C5-launchdarkly-ai-configs

**Regulated-FS note.** Request the SOC 2 Type II report and subprocessor list before use with client data, prefer the customer-AWS deployment, and do not use the SDK proxy mode for regulated traffic unless the gateway (C1) is bypassed by design [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | PromptLayer (GitHub organisation 'MagnivOrg'); independent - no acquisition found | Verified fact | A7-S004 |
| Category | Prompt registry and LLM engineering workbench (versioning, evals, tracing) | Verified fact | A7-S004 |
| Version / lineup | promptlayer Python SDK 1.5.16 released 19 August 2026 | Verified fact | A7-S004, V2-S028 |
| Licence | Proprietary platform; Python SDK Apache-2.0; self-hosting requires an Enterprise licence | Verified fact | A7-S004, A7-S085 |
| Strategic direction | Extends from prompt registry to agents and evals ('Version, test, and monitor every prompt and agent'); ships coding-agent skills and a Docs MCP server; OpenTelemetry tracing auto-instrumentation | Verified fact | A7-S004 |
| What it does | Prompt Registry stores versioned prompt templates; release labels (e.g. 'prod') select the version served and support staged rollouts and user segmentation. The SDK fetches templates and can proxy provider SDK calls for logging; evals and tracing sit alongside. | Verified fact | A7-S004, A7-S088 |
| Stack position | Control-plane prompt management (C5) with overlap into L9 tracing/evals | Verified fact | A7-S004 |
| Integration | REST API and Python/JS SDKs; proxy wrapper around OpenAI and other SDKs; OpenTelemetry tracing for OpenAI, Anthropic, Google GenAI and AWS Bedrock SDKs; webhooks | Verified fact | A7-S004 |
| Dependencies | Self-hosted: Python Flask backend, PostgreSQL 15, object storage (Amazon S3 or Google Cloud Storage), Valkey 8.1.0; AWS reference deployment uses EKS, RDS, ElastiCache and OpenSearch via OpenTofu and Helm | Verified fact | A7-S085, A7-S087 |
| Certifications | Claims SOC 2, HIPAA and GDPR compliance (self-hosted 'inherits the same SOC 2, HIPAA, and GDPR compliance'); SOC 2 type not stated on the page fetched | Verified fact | A7-S085 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Enterprise Identity: SSO (SAML/OIDC via WorkOS), SCIM directory sync, group-to-role mappings, SSO enforcement, org-scoped audit log; RBAC with granular permissions | Verified fact | A7-S086 |
| Enterprise support | Enterprise plan required for self-hosting and Enterprise Identity; contact sales | Verified fact | A7-S085, A7-S086 |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | promptlayer package first published on PyPI 29 December 2022 | Verified fact | A7-S004 |
| Maturity | SDK on 1.5.x line; continuous releases (1.5.16 on 19 August 2026) | Verified fact | A7-S004 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (deploy into customer AWS account); private_cloud: Not publicly verified; self_hosted: Yes (Enterprise only); on_prem: Not publicly verified | | |

## LaunchDarkly AgentControl (formerly AI Configs; API unchanged) (`C5-launchdarkly-ai-configs`)

**Tier:** Tactical · **Flags:** Renamed · **Original graphic label:** not in graphic

*Rationale:* Strongest certifications and rollout mechanics in the control, but SaaS-only with unverified residency scope and proprietary configuration delivery [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Runtime configuration of model, parameters and messages, per-context targeting, defaults, metrics, online evals and approvals; prompt diffing and Git-based review not documented. |
| Enterprise readiness | 4 | SAML SSO, Enterprise custom roles, audit log API and Enterprise uptime SLA; SSO and roles evidence is a search extract of older pages (medium confidence); SCIM not verified. |
| Security and compliance | 4 | SOC 2 Type II, ISO 27001, ISO 27701 and FedRAMP Moderate are company-level; AgentControl's coverage is not stated, so one below 5 (CP2 Q4). |
| Deployment flexibility | 2 | Multi-tenant SaaS, an EU-hosted offering without region detail, and a US federal instance; no self-host or VPC. |
| Ecosystem | 3 | Established feature-management platform with an Apache-2.0 AI SDK; AI-specific integrations not evidenced beyond the Python SDK. |
| Reliability and maturity | 3 | Parent platform long-established, but the AI product is about 16 months GA and was renamed and repositioned in May 2026. |
| Cost / TCO | 3 | Transparent pricing (US$10 per service connection per month with 5,000 AI runs; US$5 per extra 1,000), but metered on every model call. |
| Lock-in / portability | 2 | Proprietary service and SDK; code-side defaults reduce runtime dependency but no export path is documented. |
| **Total (generic / FS)** | **3.30 / 3.20** | |

**Capabilities.** AgentControl (formerly AI Configs; API unchanged) delivers model name, parameters and prompt messages per user context from the LaunchDarkly feature-management service, with variable interpolation, a code-side default if the service is unavailable, and a tracker recording tokens, latency and success per configuration; online evals with custom judges GA 11 March 2026; agents, trends and approvals added [VF: A7-S089, A7-S117, V2-S045].

**Strengths**

- Feature-flag style targeting and rollout of model and prompt configuration per user context, with a code-side default as the failure mode [VF: A7-S089]
- SOC 2 Type II, ISO 27001, ISO 27701 and FedRAMP Moderate (Federal instance); Enterprise uptime SLA [VF: A7-S119, V2-S065]
- SAML SSO with IdP-managed roles, Enterprise custom roles and an audit log API with before-and-after versions of each change [VF: B-C5-S001, B-C5-S002]
- Published per-run pricing [VF: A7-S118]

**Limitations and risks**

- Multi-tenant SaaS only; EU residency offered but regions and data scope not detailed [VF: A7-S119]
- Proprietary configuration service and SDK; no export path verified [VF: A7-S089] [NPV]
- Renamed and repositioned twice in about a year (GA May 2025, AgentControl May 2026) [VF: A7-S117]
- Every model call and judge run counts as a billable AI run [VF: A7-S118]

**Choose when**

- LaunchDarkly is already the firm's feature-management standard and you need per-segment rollout and kill switches for model and prompt choices [AJ]

**Avoid when**

- Configuration must be held in the UK or EU with documented regions, or in-estate [AJ]
- Volume is high and per-run metering would dominate the cost [AJ]

**Nearest competitors:** C5-promptlayer, C5-langfuse-prompts, C5-prompts-as-code

**Regulated-FS note.** Keep the approved prompt text in Git and use AgentControl only to choose between approved, pinned variants; record the variation key on every trace, confirm EU data scope and audit-log retention on the contracted plan [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LaunchDarkly | Verified fact | A7-S059 |
| Category | Runtime configuration for model, parameters and prompt messages, delivered through a feature-management platform | Verified fact | A7-S089 |
| Version / lineup | AI Configs GA 28 May 2025; online evals GA 11 March 2026; renamed AgentControl (launch post 12 May 2026; rebrand noted by 1 April 2026); Python AI SDK launchdarkly-server-sdk-ai 1.2.0 (17 July 2026) | Verified fact | A7-S117, A7-S059 |
| Licence | Proprietary SaaS; AI SDK Apache-2.0 | Verified fact | A7-S059 |
| Status events | 28 May 2025: AI Configs GA; 11 March 2026: online evals GA; 12 May 2026: 'Introducing AgentControl' (AI Configs renamed AgentControl) | Verified fact | A7-S117 |
| Strategic direction | Repositioned from prompt/model configuration to an operational layer for agents in production: agents, tools, trends, approvals, online evals with custom judges | Verified fact | A7-S117 |
| What it does | Applications request an AI Config per user context; LaunchDarkly returns the model name, parameters and messages, with variable interpolation and a code-side default used if the service is unavailable. A tracker records token usage, latency and success rates per configuration. | Verified fact | A7-S089 |
| Stack position | Control-plane configuration (C5) on top of the existing LaunchDarkly feature-flag service | Verified fact | A7-S089 |
| Integration | Server-side AI SDK (Python shown) wrapping LDClient; completion_config() with defaults; ManagedModel helper with automatic metrics | Verified fact | A7-S089 |
| Dependencies | Requires the LaunchDarkly server-side SDK (LDClient) and an SDK key | Verified fact | A7-S089 |
| Certifications | SOC 2 Type II, ISO 27001, ISO 27701, FedRAMP Moderate (Federal instance), EU-U.S. Data Privacy Framework; annual SOC 2 Type 2 audit and twice-yearly penetration tests per Security Program Addendum | Verified fact | A7-S119, V2-S065 |
| GDPR / residency | GDPR/CCPA privacy programme; EU-hosted offering supporting EU data residency advertised (regions not detailed); multi-tenant with exceptions for large and US federal customers | Verified fact | A7-S119 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Enterprise plan with custom pricing; 'Enterprise uptime SLA' advertised | Verified fact | A7-S118, A7-S119 |
| Pricing | Developer: US$0 (limited AgentControl run entitlements); Foundation: US$10 per service connection/month incl. 5,000 AI runs, US$5 per additional 1,000 runs; Enterprise: custom. An AI run = each model call or judge run (as read 7 October 2026; cached snippets of different ages) | Verified fact | A7-S118 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Vendor states LaunchDarkly 'serves over 100 billion feature flags daily' (undated README claim) | Verified fact | A7-S089 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes (dedicated US federal instance, FedRAMP Moderate); self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

# C6: AI FinOps

## FinOps Open Cost and Usage Specification (FOCUS) (`C6-finops-focus`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Open, foundation-governed schema that removes tool lock-in from cost data; strategic as the data model, not as a product [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers cost and usage normalisation; AI model identity not yet ratified and token type deferred. |
| Enterprise readiness | 3 | Rubric rule 2: enables a common cost dataset and chargeback inside the estate; no commercial support of its own. |
| Security and compliance | 3 | Rubric rule 2: a specification with clear CC BY 4.0 licence and a validator; inherits the controls of the data platform it lands in. |
| Deployment flexibility | 5 | Specification; implemented anywhere. |
| Ecosystem | 4 | FinOps Foundation, validator and vendor mappings (e.g. Vantage); AI-provider adoption not verified. |
| Reliability and maturity | 4 | Ratified releases on a semi-annual cadence since 2024 under the Joint Development Foundation; AI scope still in progress. |
| Cost / TCO | 5 | Free open specification. |
| Lock-in / portability | 5 | Open standard, permissive licence, neutral governance. |
| **Total (generic / FS)** | **3.80 / 3.85** | |

*Evidence rules applied:* Rubric rule 2 (open specification): enterprise readiness and security scored on what the specification enables and on hygiene, each capped at 4; inherits host controls

**Capabilities.** Open specification for cost and usage data. FOCUS 1.4 was ratified on 4 June 2026; 1.2 added virtual-currency columns for credits and tokens; tokens are carried today through SKU IDs, ConsumedUnit and ConsumedQuantity. FOCUS 1.5 (no ratification date) is scoped to add AI pricing dimensions on SkuPriceDetails and four model-identity properties (ModelDeveloper, ModelFamily, ModelId, ModelVersion) with no new columns; a first-class token-type (input/output) column is deferred [VF: A7-S049, A7-S116, V2-S046].

**Strengths**

- Vendor-neutral target schema for normalising gateway logs, provider invoices and cloud bills [VF: A7-S048] [AJ]
- Free, CC BY 4.0, with a conformance validator (2.2.1, August 2026) [VF: A7-S096, A7-S050]
- Steady cadence: six public releases since June 2023 [VF: A7-S049]
- FinOps Framework 2026 adds a FinOps for AI category; vendors such as Vantage map to FOCUS [VF: A7-S115, A7-S113]

**Limitations and risks**

- No AI-specific columns today; model identity arrives only with 1.5, which has no date, and token type is deferred [VF: A7-S116, V2-S046]
- It is a data model only: no metering, budgets or enforcement [AJ]
- Adoption by AI providers not publicly verified [NPV]

**Choose when**

- Always, as the target schema for the firm's AI cost dataset [Rec]

**Avoid when**

- Do not wait for 1.5 to start: map tokens to SKU and ConsumedQuantity now [Rec]

**Nearest competitors:** C6-vantage, C6-cloudzero, C6-gateway-cost-attribution

**Regulated-FS note.** A FOCUS-shaped AI cost dataset makes provider spend comparable for concentration analysis and lets cost allocation feed the outsourcing register without vendor-specific mapping [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | FinOps Foundation FOCUS Working Group (copyright Joint Development Foundation Projects, LLC, FOCUS Series) | Verified fact | A7-S048, A7-S096 |
| Category | Open specification (billing/cost and usage data schema) | Verified fact | A7-S048 |
| Version / lineup | v1.4 ratified by the FOCUS Steering Committee on 4 June 2026 (adds BillingPeriod and InvoiceDetail datasets, 47 columns); v1.3 December 2025; v1.2 June 2025; v1.1 November 2024; v1.0 20 June 2024 | Verified fact | A7-S049, V2-S046 |
| Licence | Open specification; documents under Creative Commons Attribution 4.0 International | Verified fact | A7-S096 |
| Status events | 4 June 2026: FOCUS 1.4 ratified (Invoice Detail and Billing Period datasets; zero incompatible changes); validator support for 1.4 expected later in Q3 2026 | Verified fact | V2-S046 |
| Strategic direction | FinOps Framework 2026 adds a 'FinOps for AI' technology category; State of FinOps 2026 ranks FinOps for AI the top forward-looking priority (98% of respondents manage AI spend); FOCUS 1.5 (in progress; no ratification date) adds a Price Sheet and, for AI, confirmed scope of AI pricing dimensions (cached vs fresh tokens, global vs regional serving) as properties on SkuPriceDetails plus four model properties (ModelDeveloper, ModelFamily, ModelId, ModelVersion) with no new columns; a first-class input/output token-type column is deferred, so token splits stay in separate SKUs (SkuMeter) and Consu | Verified fact | A7-S115, A7-S116, V2-S046 |
| What it does | Defines standard datasets, columns (dimensions and metrics) and requirements so billing and usage data from different providers are interoperable and comparable. | Verified fact | A7-S048 |
| Stack position | Data-model standard underneath C6: target schema for normalising gateway token logs and provider invoices before allocation | Architectural judgement |  |
| Integration | Spec plus validation tooling; focus-validator 2.2.1 released 5 August 2026 | Verified fact | A7-S048, A7-S050 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open specification | Verified fact | A7-S096 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Tokens are representable today via FOCUS 1.2 virtual-currency columns and SKU/ConsumedUnit/ConsumedQuantity, with no AI-specific columns; AI-specific fields (model identity, input/output tokens; stretch: cached vs fresh tokens, global vs regional serving) are scoped for FOCUS 1.5 (release date not confirmed). Vendors such as Vantage map their schemas to FOCUS. | Verified fact | A7-S116, A7-S113 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Six public releases since v0.5 (June 2023); semi-annual cadence | Verified fact | A7-S049 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not applicable (specification); on_prem: Not publicly verified | | |

## Gateway-native and provider-native token cost tracking, budgets and chargeback (pattern) (`C6-gateway-cost-attribution`)

**Tier:** Strategic · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* The only place where AI spend can be attributed per request and stopped in real time; implementations are replaceable behind the OpenAI-compatible interface. Acquired refers to Portkey [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Per-key/team/user/customer budgets, rate limits, spend tracking, provider and cloud reconciliation data; cost per task needs a trace join and some controls fail open by default. |
| Enterprise readiness | 4 | Rubric rule 2 (pattern): implementations offer SSO, RBAC and audit (LiteLLM Enterprise SSO, RBAC, SCIM and audit logs; cloud IAM under CP2 Q1); capped at 4. |
| Security and compliance | 3 | Depends on implementation: LiteLLM SOC 2 Type 2 (September 2026), Cloudflare AI Gateway named in SOC 2 scope; LiteLLM's March 2026 supply-chain incident; Admin API keys are powerful credentials. |
| Deployment flexibility | 5 | Self-hosted gateways, managed cloud gateways and SaaS gateways; runs in-estate or air-gapped. |
| Ecosystem | 4 | OpenAI-compatible gateway endpoints and provider admin APIs; FOCUS mapping not native. |
| Reliability and maturity | 3 | Cloud cost tags are mature, but Foundry project attribution is preview, LiteLLM had a supply-chain incident, and Portkey changed owner. |
| Cost / TCO | 4 | Open-source core; a database is needed for budgets and spend tracking. |
| Lock-in / portability | 3 | Base 4 (open interfaces, OSS gateways) reduced by 1 because a named implementation (Portkey) changed owner; cost data models differ per gateway. |
| **Total (generic / FS)** | **3.85 / 3.70** | |

*Evidence rules applied:* Rubric rule 2 (pattern): enterprise readiness and security scored on what implementations enable and on their hygiene, each capped at 4; platform controls presumed for cloud gateways (CP2 Q1); confirm per service

**Capabilities.** Pattern: the gateway (C1) issues virtual keys per team, project, user or customer and records tokens and cost per request, enforcing budgets and rate limits (LiteLLM: budgets at key, user, team and customer level, TPM/RPM limits); provider admin APIs (Anthropic Usage & Cost Admin API) and cloud billing tags (Bedrock application inference profiles, Microsoft Foundry project tags) are the reconciliation sources [VF: A7-S010, A6-S015, A7-S070, B-C6-S004, B-C6-S005].

**Strengths**

- The gateway sees every model call, so it is the only point that can both attribute and stop spend in real time [AJ]
- Mature open-source implementation with budgets, limits and spend tracking (LiteLLM MIT core) and managed equivalents in the cloud gateways (token limits and quotas in Azure APIM, Apigee and Kong; spend limits in Cloudflare) [VF: A6-S015, A6-S053, A6-S024, A6-S016, A6-S019]
- Provider-side data breaks tokens into uncached input, cached input, cache creation and output, by API key, workspace, model and service tier, for reconciliation [VF: A7-S070]
- Cloud billing tags carry AI spend into the existing cost tools (Cost Explorer and CUR; Azure cost analysis) [VF: B-C6-S004, B-C6-S005]

**Limitations and risks**

- Some LiteLLM controls fail open or are off by default: max_budget without a database, and a proxy admin key that bypasses budget checks [VF: A6-S015]
- Cloud billing tags are aggregated per usage type per day, not per request; per-request attribution needs invocation logs or gateway data [VF: B-C6-S004]
- Gateway consolidation: Portkey acquired by Palo Alto Networks (completed 29 May 2026) and folded into Prisma AIRS [VF: A6-S011, V2-S025]
- LiteLLM suffered a PyPI supply-chain compromise on 24 March 2026 [VF: A6-S008, V2-S027]
- Cost per task needs a join between gateway records and traces (L9); no product does this end to end in the fact base [AJ]

**Choose when**

- Always, as the metering and enforcement point for model spend [Rec]

**Avoid when**

- Never as the only record: reconcile against provider invoices and cloud bills monthly [Rec]

**Nearest competitors:** C6-helicone, C6-vantage, C6-cloudzero

**Regulated-FS note.** Budget enforcement is an operational-resilience control against runaway agents; test that budgets fail closed, restrict the admin key, and reconcile gateway spend to invoices for the outsourcing register [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Pattern; implementations include LiteLLM (BerriAI), Portkey (acquired by Palo Alto Networks), Helicone, and model-provider admin APIs such as Anthropic's Usage & Cost Admin API | Verified fact | A7-S010, A7-S016, A7-S046, A7-S070 |
| Category | Named pattern (AI FinOps: metering, attribution, budgets, showback/chargeback) | Verified fact | A7-S010, A7-S070 |
| Version / lineup | Examples as of 7 October 2026: LiteLLM 1.104.1 (7 October 2026); portkey-ai SDK 2.3.4 (23 July 2026); Anthropic Usage & Cost Admin API (current docs) | Verified fact | A7-S010, A7-S081, A7-S070 |
| Licence | Mixed: LiteLLM MIT (open core gateway); Portkey SDK MIT; provider APIs proprietary | Verified fact | A7-S010, A7-S081, A7-S070 |
| Status events | 29 May 2026: Portkey, Inc. acquired by Palo Alto Networks (Form 10-Q); 16 July 2026: Palo Alto Networks AI Gateway GA (product page) | Verified fact | A7-S016, A7-S028, V2-S025, V2-S048 |
| Strategic direction | Gateways are being absorbed by security vendors: Palo Alto Networks acquired Portkey (29 May 2026) 'to enhance our Prisma AIRS capabilities' and made its AI Gateway generally available on 16 July 2026 | Verified fact | A7-S016, A7-S028 |
| What it does | A gateway issues virtual keys per team, project or user and records token usage and cost per request, enabling budgets and multi-tenant spend reports (LiteLLM: 'multi-tenant cost tracking and spend management per project/user'). Model providers expose organisation-level usage and cost data by API key, workspace, model and service tier (Anthropic Usage & Cost Admin API), which can be reconciled with gateway records. | Verified fact | A7-S010, A7-S070 |
| Stack position | Spans C1 (gateway) and C6; the gateway is the natural metering point because every model call passes through it, while provider billing APIs and cloud bills are the reconciliation source | Architectural judgement |  |
| Integration | OpenAI-compatible gateway endpoints with virtual keys; provider admin REST APIs (Anthropic Admin API key required; workspace keys do not work) | Verified fact | A7-S010, A7-S070 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Depends on implementation; open-source gateways have no licence fee for the core | Architectural judgement |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | FOCUS provides a vendor-neutral cost/usage schema (AI token fields scoped for FOCUS 1.5); cost platforms such as Vantage and CloudZero ingest provider token data via admin APIs for allocation | Verified fact | A7-S048, A7-S116, A7-S113, A7-S114 |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (e.g. hosted gateways, provider APIs); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (e.g. LiteLLM proxy, Helicone self-hosted); on_prem: Not publicly verified | | |

## Vantage (cloud cost management platform) (`C6-vantage`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Useful reporting layer for organisations already using it; SaaS-only with unverified residency and vendor-described AI features [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Provider integrations, AI tag normalisation and hierarchical allocation; billing-level granularity only, and features described in vendor blogs. |
| Enterprise readiness | 3 | SAML SSO verified (lifts NPV cap to max 3 under CP2 Q2); RBAC and audit logs not verified; SAML plan availability conflicts between pages. |
| Security and compliance | 3 | SOC 2 Type 2 and SOC 1 Type 2, reports on request; no ISO 27001 found. |
| Deployment flexibility | 2 | SaaS only; regions not verified. |
| Ecosystem | 4 | AI-provider and cloud billing integrations, API, MCP server and FOCUS-mapped schema. |
| Reliability and maturity | 3 | Established cloud cost vendor; AI features added from 2025; ownership and funding not verified. |
| Cost / TCO | 3 | Managed AI Tags at no extra cost; AI spend counts toward quota tiers whose prices were not verified. |
| Lock-in / portability | 3 | Proprietary SaaS, but FOCUS-mapped data and an API make export feasible. |
| **Total (generic / FS)** | **2.95 / 2.90** | |

**Capabilities.** Cloud cost management platform that ingests cloud and AI-provider billing (Anthropic tokens by model, workspace, API key and service tier; Claude Enterprise; OpenAI tokens by model and operation), allocates it via virtual tagging and hierarchical allocation, normalises AI spend with Managed AI Tags (model, provider, token type) and exposes data through an API and an MCP server; its internal schema maps to FOCUS [VF: A7-S113, A7-S090].

**Strengths**

- Direct AI-provider integrations, with Anthropic GA September 2025 and Claude Enterprise added July 2026 [VF: A7-S113]
- Managed AI Tags normalise model, provider and token type across providers at no extra cost [VF: A7-S113]
- SOC 1 Type 2 and SOC 2 Type 2 (reports on request) and self-service SAML SSO [VF: B-C6-S001]
- Schema mapped to FOCUS [VF: A7-S113]

**Limitations and risks**

- AI cost features are described in vendor blog posts [VF: A7-S113]
- Anthropic integration uses an Admin API key, which has revocable read-write access [VF: A7-S113]
- SaaS only; EU region, RBAC and audit logs not publicly verified [NPV]
- Billing data is per provider account, not per task; cost per commentary still needs gateway and trace data [AJ]

**Choose when**

- Vantage is already the cloud FinOps tool and you want AI provider spend in the same allocation and showback model [AJ]

**Avoid when**

- You cannot accept a third party holding a read-write provider admin key [AJ]
- You need per-request or per-task attribution, which belongs to the gateway [AJ]

**Nearest competitors:** C6-cloudzero, C6-gateway-cost-attribution, C6-finops-focus

**Regulated-FS note.** Treat it as the showback and chargeback reporting layer, fed by provider billing and gateway exports; assess the admin-key access under C4 and C7 and the platform under the outsourcing register [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Vantage (vantage.sh) | Verified fact | A7-S090 |
| Category | Cloud cost management / FinOps platform | Verified fact | A7-S090 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Not publicly verified | Not publicly verified |  |
| Strategic direction | AI cost management: native Anthropic API (GA September 2025), Claude Enterprise (July 2026) and OpenAI integrations; Managed AI Tags (vntg:ai: model, provider, token type) normalise AI spend across providers; hosted MCP server (OAuth 2.1) for cost queries | Verified fact | A7-S113, A7-S090 |
| What it does | Ingests cloud and AI-provider billing (token counts by model, workspace, API key, service tier for Anthropic; by model and operation for OpenAI) and allocates costs via virtual tagging and hierarchical allocation; exposes data through API and MCP. | Verified fact | A7-S113, A7-S090 |
| Stack position | Not publicly verified | Not publicly verified |  |
| Integration | Provider admin API keys (Anthropic Admin API, Claude Enterprise Analytics API), cloud billing integrations; Vantage API and MCP server; internal VQL schema maps to FOCUS | Verified fact | A7-S113, A7-S090 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Managed AI Tags at no additional cost; AI provider costs count toward Vantage quota tiers (tier prices not verified) | Verified fact | A7-S113 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## CloudZero (`C6-cloudzero`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Credible allocation features and SOC 2, but SaaS-only, proprietary allocation logic, unverified pricing and vendor-described AI claims [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Token-level ingestion across four AI sources and allocation by customer, feature and team; claims are vendor blog posts. |
| Enterprise readiness | 3 | SAML SSO and role-based data access verified; audit logs not verified; max 3 under CP2 Q2. |
| Security and compliance | 3 | SOC 2 Type 2 and SOC 1 Type 2 listed; no ISO 27001 found. |
| Deployment flexibility | 2 | SaaS receiving telemetry; regions not verified. |
| Ecosystem | 3 | Integrations for major AI providers and clouds plus a Kubernetes agent; FOCUS not evidenced. |
| Reliability and maturity | 3 | Established cost vendor with SOC 1 since 2022; ownership and funding not verified. |
| Cost / TCO | 2 | Pricing not publicly verified. |
| Lock-in / portability | 2 | Proprietary allocation engine (CostFormation); export and FOCUS support not verified. |
| **Total (generic / FS)** | **2.70 / 2.65** | |

**Capabilities.** Cloud cost intelligence platform that ingests token-level usage and cost from OpenAI, the Anthropic API, Amazon Bedrock (including Claude Platform on AWS) and Azure OpenAI, and allocates it by customer, feature, team, product and environment through its CostFormation engine; a Kubernetes agent supplies container telemetry [VF: A7-S114, A7-S091].

**Strengths**

- Anthropic ingestion breaks out uncached input, cache hits, output and tool usage by model, workspace and API key (vendor statement) [VF: A7-S114]
- Allocation by customer and feature supports unit economics [VF: A7-S114]
- SOC 1 Type 2 and SOC 2 Type 2 listed in the Trust Center; SAML SSO with custom roles that scope data access and map to IdP groups [VF: B-C6-S002, B-C6-S003]

**Limitations and risks**

- AI cost claims are from CloudZero's own blog posts [VF: A7-S114]
- No ISO 27001 found; SOC reports under NDA [VF: B-C6-S002]
- Pricing, EU region and audit logs not publicly verified [NPV]
- Proprietary allocation engine; FOCUS support not evidenced [NPV]

**Choose when**

- CloudZero is already the cost platform and you want AI spend allocated by customer or product next to Kubernetes costs [AJ]

**Avoid when**

- Residency of billing metadata must be documented in the UK or EU [AJ]
- You want allocation rules in an open schema [AJ]

**Nearest competitors:** C6-vantage, C6-gateway-cost-attribution, C6-finops-focus

**Regulated-FS note.** Use for showback where already contracted; keep the allocation rules documented outside the tool so chargeback survives an exit [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | CloudZero | Verified fact | A7-S091 |
| Category | Cloud cost intelligence / allocation platform | Verified fact | A7-S091 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Not publicly verified | Not publicly verified |  |
| Strategic direction | Publishes extensive AI-pricing content and positions on AI cost allocation: integrations for OpenAI, Anthropic direct API, Amazon Bedrock, Claude Platform on AWS and Azure OpenAI | Verified fact | A7-S114 |
| What it does | Ingests token-level usage and cost from AI providers and cloud bills and allocates it by customer, feature, team, product and environment via the CostFormation engine; a Kubernetes agent supplies container telemetry. | Verified fact | A7-S114, A7-S091 |
| Stack position | Not publicly verified | Not publicly verified |  |
| Integration | Kubernetes agent (Prometheus-compatible collector) shipping to CloudZero via upload API and S3 | Verified fact | A7-S091 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Vendor claims to be the first cloud cost platform to integrate directly with Anthropic; reports customers' Bedrock spend typically 1.5x-2x initial estimates | Verified fact | A7-S114 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (platform receives telemetry); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## Helicone (AI Gateway and LLM Observability Platform) (`C6-helicone`)

**Tier:** Experimental · **Flags:** Acquired, Not recommended · **Original graphic label:** not in graphic

*Rationale:* Maintenance mode after the Mintlify acquisition makes it unsuitable as a dependency; not recommended for new use [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Per-request, session and user cost and latency tracking with a gateway and prompt versioning; no budgets or chargeback features evidenced. |
| Enterprise readiness | 2 | SSO, RBAC and audit logs not publicly verified; NPV cap. |
| Security and compliance | 2 | SOC 2 claimed without type in a README; NPV cap. |
| Deployment flexibility | 3 | SaaS and self-hosted (Docker; Helm on request for enterprise). |
| Ecosystem | 3 | OpenAI-compatible base URL, integrations for major providers and frameworks, PostHog export. |
| Reliability and maturity | 1 | Maintenance mode after the Mintlify acquisition (3 March 2026); feature development wound down. |
| Cost / TCO | 4 | Apache-2.0; free tier of 10,000 requests per month. |
| Lock-in / portability | 3 | Base 4 (Apache-2.0, base-URL integration) reduced by 1 for the ownership change; governance is company-controlled. |
| **Total (generic / FS)** | **2.60 / 2.50** | |

*Evidence rules applied:* enterprise_readiness capped at 2: SSO, RBAC and audit logs NPV; security_compliance capped at 2: SOC 2 type not stated, no trust-centre report

**Capabilities.** Proxy or logging layer for LLM requests that tracks cost, latency and quality per request, session and user, with prompt versioning and an OpenAI-compatible AI gateway with fallbacks [VF: A7-S046].

**Strengths**

- Apache-2.0 and self-hostable with Docker [VF: A7-S046]
- Simple integration by changing the base URL [VF: A7-S046]

**Limitations and risks**

- Acquired by Mintlify on 3 March 2026; in maintenance mode with security fixes, bug fixes and new model support only [VF: A7-S112, V2-S043]
- No npm helper release since 7 November 2025 [VF: A7-S047]
- 'SOC 2 and GDPR compliant' stated without SOC 2 type; access controls not publicly verified [VF: A7-S046] [NPV]
- A competitor states new sign-ups are disabled (single rival source) [NPV]

**Choose when**

- Only as a short-term bridge for an existing deployment while migrating [AJ]

**Avoid when**

- Any new deployment [Rec]

**Nearest competitors:** C6-gateway-cost-attribution, L9-langfuse, C1-litellm

**Regulated-FS note.** Plan migration of existing usage to the gateway (C1) and the L9 platform; record the change of ownership and maintenance status in third-party risk files [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Helicone, acquired by Mintlify (announced and completed 3 March 2026) | Verified fact | A7-S112, V2-S043 |
| Category | AI gateway plus LLM observability with cost and latency tracking | Verified fact | A7-S046 |
| Version / lineup | No versioned platform release found; @helicone/helpers npm package last published 1.8.3 on 7 November 2025; legacy Python package 'helicone' last released 1.0.14 on 3 November 2023 | Verified fact | A7-S047, A7-S005 |
| Licence | Open source, Apache-2.0 | Verified fact | A7-S046, A7-S005 |
| Status events | 3 March 2026: acquired by Mintlify; product in maintenance mode (security and bug fixes, new model support; standalone feature development wound down) | Verified fact | A7-S112, V2-S043 |
| Strategic direction | After acquisition, founders moved to Mintlify to work on AI knowledge infrastructure; Helicone in maintenance mode | Verified fact | A7-S112 |
| What it does | Proxies or logs LLM requests, then tracks cost, latency and quality per request, session and user; supports prompt versioning and an AI gateway with fallbacks. | Verified fact | A7-S046 |
| Stack position | Overlaps C1 (gateway), L9 (observability) and C6 (cost tracking) | Verified fact | A7-S046 |
| Integration | Change base URL to the Helicone gateway (OpenAI-compatible); integrations for OpenAI, Anthropic, Gemini, LangChain, Vercel AI SDK; export to PostHog | Verified fact | A7-S046 |
| Dependencies | Self-hosting via docker-compose; production Helm chart available to enterprise customers on request | Verified fact | A7-S046 |
| Certifications | Claims 'SOC 2 and GDPR compliant' (README; SOC 2 type not stated) | Verified fact | A7-S046 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free tier of 10,000 requests per month, no credit card; paid plans not verified | Verified fact | A7-S046 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Helicone states 14.2 trillion tokens processed and 16,000 organisations served over three years | Verified fact | A7-S112 |
| Maturity | npm helper packages show no release since 7 November 2025 | Verified fact | A7-S047 |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Docker; Helm for enterprise); on_prem: Not publicly verified | | |

# C7: AI security

## HashiCorp Vault (IBM Vault Self-Managed; HCP Vault Dedicated) (`C7-hashicorp-vault`)

**Tier:** Strategic · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* Strategic for secrets and agent credential brokerage, conditional on accepting BUSL and IBM ownership (lock-in 2) [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Leading depth in secrets and agent credential brokerage; not a prompt-injection or supply-chain control. |
| Enterprise readiness | 4 | Policy ACLs, namespaces (multi-tenancy), SCIM 2.0, audit devices and IBM support lifecycle; human SSO and SLA not verified in the dataset. |
| Security and compliance | 4 | SOC 2 Type 2 and ISO 27001 with IBM Vault in scope (anchor 4); no CMK/BYOK, ISO 42001 or FedRAMP evidence for 5. |
| Deployment flexibility | 4 | HCP Vault Dedicated plus self-managed on-prem; air-gap not verified. |
| Ecosystem | 4 | API, CLI, Terraform provider and validated IdPs (IBM Verify, Auth0, PingFederate, Entra, Okta). |
| Reliability and maturity | 4 | Years of production use and IBM lifecycle; IBM ownership change (February 2025) and 2.0 major-version transition noted. |
| Cost / TCO | 3 | BUSL community use free; Enterprise needed for agentic IAM; HCP hourly pricing published. |
| Lock-in / portability | 2 | Source-available BUSL (base 3), reduced by 1 for the 2025 acquisition (rule 3); licence risk under rule 4. |
| **Total (generic / FS)** | **3.80 / 3.65** | |

**Capabilities.** Secrets storage and brokerage, dynamic credentials and certificates, identity-based authorisation; agentic IAM (GA in Vault Enterprise 2.1, 1 September 2026) registers agents, validates IdP OAuth JWTs, enforces user, agent-ceiling and request-scoped authorisation, and records user and agent in audit logs [VF: A7-S034, A7-S061].

**Strengths**

- Keeps credentials out of the model with short-lived, request-scoped issuance and dual attribution [VF: A7-S034] [AJ]
- SOC 2 Type 2 and ISO 27001/27017/27018 with IBM Vault in scope; FIPS 140-2 for Enterprise [VF: A7-S035]
- Namespaces, SCIM 2.0, policy ACLs and audit devices [VF: A7-S033, A7-S034]
- IBM lifecycle: two years support plus extensions [VF: A7-S033]

**Limitations and risks**

- BUSL 1.1 (IBM licensor) restricts competing hosted or embedded offerings [VF: A7-S060]
- Agentic IAM is Enterprise-only [VF: A7-S034]
- Owned by IBM since 27 February 2025 [VF: A7-S032]
- Version caveat: changelog stops at 2.1.1 but a v2.1.2 tag exists [VF: V2-S061]

**Choose when**

- Multi-cloud or hybrid estate needing one broker for human, workload and agent credentials [AJ]

**Avoid when**

- A single cloud's native secrets service suffices and agent delegation is not needed [AJ]

**Nearest competitors:** Cloud-native secrets managers, C4-entra-agent-id, C4-okta-auth0-ai-agents

**Regulated-FS note.** Use audit devices as the authoritative record of which agent obtained which credential on whose behalf; include IBM in concentration analysis if watsonx.governance is also chosen [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | HashiCorp, an IBM company (IBM acquisition closed 27 February 2025) | Verified fact | A7-S032 |
| Category | Secrets management, identity-based access and encryption; agentic IAM for AI agents | Verified fact | A7-S034 |
| Version / lineup | Vault 2.1.1 (16 September 2026); 2.1.0 (1 September 2026) made agentic IAM GA in Vault Enterprise; Vault 2.0 GA 14 April 2026 (first major version since 1.0, aligned to IBM lifecycle) | Verified fact | A7-S061, A7-S033, A7-S034, V2-S061 |
| Licence | Source-available Business Source License 1.1 (licensor IBM) for Vault 1.15.0 and later; production use permitted except competing hosted/embedded offerings; IBM Vault Self-Managed sold under IBM International Program License Agreement; Enterprise features need a licence | Verified fact | A7-S060, A7-S033, A7-S036 |
| Status events | 27 February 2025: IBM completed acquisition of HashiCorp; June/August 2025: HCP Vault Secrets end of sale (30 June 2025) and end of life for pay-as-you-go customers (27 August 2025); 14 April 2026: Vault 2.0 GA under IBM support lifecycle; 1 September 2026: agentic IAM GA (Vault Enterprise 2.1) | Verified fact | A7-S032, A7-S036, A7-S033, A7-S061 |
| Strategic direction | Positions Vault as the governance layer for AI agent identities: agent registry, OAuth request-scoped authorisation (authorization_details), on-behalf-of delegation, audit attribution to both user and agent; SPIFFE JWT-SVID and SCIM 2.0 in 2.0 | Verified fact | A7-S034, A7-S033 |
| What it does | Stores and brokers secrets, issues dynamic credentials and certificates, and authorises access by identity. Agentic IAM registers AI agents, validates OAuth JWTs from IdPs, enforces the intersection of user permissions, agent ceiling policies and request-scoped authorisation details, and records both user and agent in audit logs. | Verified fact | A7-S034 |
| Stack position | C7 secrets and C4 agent identity/authorisation; not shown in the original graphic | Verified fact | A7-S034 |
| Integration | API, CLI, Terraform Vault provider (vault_agent_registration, vault_oauth_resource_server_config_profile); validated IdPs: IBM Verify, Auth0, PingFederate, Microsoft Entra, Okta | Verified fact | A7-S034 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type 2; ISO 27001, 27017, 27018 (scope includes IBM Vault); Vault Enterprise FIPS 140-2; SOC 2 report under NDA via customertrust@ibm.com | Verified fact | A7-S035 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Policy-based ACLs, namespaces, SCIM 2.0 provisioning, agent registry UI, audit devices with user+agent attribution | Verified fact | A7-S033, A7-S034, A7-S061 |
| Enterprise support | IBM lifecycle for 2.x: 2 years support + 1 year critical-fix extension + 3 years usage/existing fixes | Verified fact | A7-S033 |
| Pricing | HCP Vault Dedicated: trial, pay-as-you-go or contract; hourly base cost by tier/size/region plus per-client hourly charge (Essentials/Standard); self-managed: contact sales | Verified fact | A7-S036 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (HCP Vault Dedicated); managed_cloud: Yes (HCP Vault Dedicated); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Vault Community / IBM Vault Self-Managed); on_prem: Yes (self-managed) | | |

## Model and package supply-chain scanning (pattern): ModelScan, picklescan, fickling, Hugging Face Hub scanning, safetensors (`C7-model-supply-chain-scanning`)

**Tier:** Strategic · **Flags:** Acquired · **Original graphic label:** not in graphic

*Rationale:* Mandatory baseline pattern (safetensors by default plus scanning gate); ModelScan's owner was acquired [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers executable model formats competently; pattern-matching limits and no package or agent-artefact coverage. |
| Enterprise readiness | 3 | Rule 2: CI libraries inherit host controls; no commercial support for the open tools (commercial successors are separate products). |
| Security and compliance | 3 | Rule 2 hygiene: security policy for ModelScan, clear licences; owner acquired and components pre-1.0. |
| Deployment flexibility | 5 | Runs anywhere, including air-gapped CI. |
| Ecosystem | 4 | Hugging Face Hub uses picklescan; commercial platforms build on the same approach. |
| Reliability and maturity | 3 | Mostly pre-1.0; ModelScan cadence slowed after acquisition. |
| Cost / TCO | 5 | Free open source with light operations. |
| Lock-in / portability | 4 | Permissive licences and an open format (base 5), reduced by 1 because ModelScan is vendor-owned after a 2025 acquisition (rule 3). |
| **Total (generic / FS)** | **3.65 / 3.60** | |

**Capabilities.** Pattern: safe serialisation (safetensors) plus open-source scanners (ModelScan, picklescan, fickling) in CI and at registry promotion, complemented by Hugging Face Hub-side scanning [VF: A7-S082, A7-S083, A7-S064, A7-S007, A7-S037].

**Strengths**

- safetensors removes pickle's code-execution risk ('Pickle: Unsafe, runs arbitrary code') [VF: B-C7-S006]
- Free, local, CI-native and air-gap friendly [VF: A7-S002, A7-S006] [AJ]
- ModelScan publishes a security policy with GitHub advisories [VF: B-C7-S007]

**Limitations and risks**

- picklescan only pattern-matches module names; scanning reduces but does not remove risk [VF: A7-S037]
- ModelScan's owner Protect AI is now Palo Alto Networks; README directs users to Guardian; last release February 2026 [VF: A7-S014, A7-S082, A7-S002]
- Most components pre-1.0 [VF: A7-S002, A7-S064, A7-S007]
- Does not address package compromise (LiteLLM case) [VF: A6-S008] [AJ]

**Choose when**

- Always, as the minimum gate for self-hosted weights [Rec]

**Avoid when**

- Never as the only supply-chain control [AJ]

**Nearest competitors:** C7-prisma-airs, C7-hiddenlayer, C7-openssf-model-signing

**Regulated-FS note.** Record scan results and artefact hashes in the model inventory (C8) so validation evidence refers to the exact weights scanned [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Pattern; ModelScan by Protect AI (now Palo Alto Networks); picklescan (community, used by Hugging Face); fickling by Trail of Bits; safetensors by Hugging Face | Verified fact | A7-S082, A7-S014, A7-S037, A7-S064, A7-S007 |
| Category | Named pattern plus open-source scanners (e.g. picklescan: 'Security scanner detecting Python Pickle files performing suspicious actions') and a safe serialisation format | Verified fact | A7-S082, A7-S083, A7-S007 |
| Version / lineup | modelscan 0.8.8 (18 February 2026); picklescan 1.0.5 (1 July 2026); fickling 0.1.12 (26 June 2026); safetensors 0.8.0 (9 June 2026) | Verified fact | A7-S002, A7-S006, A7-S064, A7-S007, V2-S028 |
| Licence | Open source: ModelScan Apache-2.0; picklescan MIT; fickling LGPLv3+; safetensors Apache-2.0 | Verified fact | A7-S002, A7-S006, A7-S064, A7-S007 |
| Status events | 22 July 2025: Protect AI (ModelScan, Guardian) acquired by Palo Alto Networks | Verified fact | A7-S014 |
| Strategic direction | Commercial successors bundle scanning into AI security platforms (Prisma AIRS AI Model Security, HiddenLayer Model Scanner); Hugging Face layers ClamAV, picklescan, trufflehog and third-party scanners (Protect AI, JFrog) on the Hub | Verified fact | A7-S039, A7-S029, A7-S037 |
| What it does | Scans serialised model files (pickle, H5, SavedModel and others) for code that executes on load before models enter registries or runtime; safetensors avoids executable pickle formats altogether. Hugging Face notes picklescan only pattern-matches module names, and scanning reduces but does not remove risk. | Verified fact | A7-S082, A7-S037 |
| Stack position | Pre-deployment gate in CI and model registry promotion (C7), upstream of L1/L2 self-hosted models | Architectural judgement |  |
| Integration | CLIs and Python libraries for CI pipelines; Hub-side automatic scanning of public repositories | Verified fact | A7-S082, A7-S037 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Open-source tools free; commercial scanners priced by vendor | Verified fact | A7-S002, A7-S006, A7-S031 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Protect AI reported 4.47 million model versions in 1.41 million Hub repositories scanned by 1 April 2025, flagging 352,000 issues across 51,700 models | Verified fact | A7-S037 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Hugging Face Hub scanning; commercial platforms); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (open-source CLIs); on_prem: Not publicly verified | | |

## OpenSSF Model Signing (OMS) specification and model-signing library (`C7-openssf-model-signing`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Right standard for internally produced weights, but narrow and with unverified adoption [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Does integrity and signer verification well; narrow scope by design. |
| Enterprise readiness | 3 | Rule 2: library inherits host controls; PKCS#11 and private Sigstore enable enterprise key custody. |
| Security and compliance | 3 | Rule 2 hygiene: foundation-governed, Apache-2.0; no security policy file found. |
| Deployment flexibility | 4 | Self-hosted library; offline key or certificate signing possible; private Sigstore supported. |
| Ecosystem | 2 | Adoption by hubs and registries not publicly verified. |
| Reliability and maturity | 3 | v1.0 spec (April 2025), library 1.1.1; no release in the last twelve months found. |
| Cost / TCO | 5 | Free. |
| Lock-in / portability | 5 | Open specification, Apache-2.0, neutral governance. |
| **Total (generic / FS)** | **3.35 / 3.50** | |

**Capabilities.** Open specification and Apache-2.0 library to sign and verify ML models of any format with a detached Sigstore bundle (DSSE/in-toto), using Sigstore, key pairs, certificates or PKCS#11 devices, with optional private Sigstore instances and a transparency log [VF: A7-S040, A7-S038, B-C7-S005].

**Strengths**

- Vendor-neutral integrity and signer verification under OpenSSF (Linux Foundation) [VF: A7-S040]
- HSM (PKCS#11) and private Sigstore support suit regulated key custody [VF: B-C7-S005]
- Free [VF: A7-S038]

**Limitations and risks**

- Proves integrity and signer, not provenance or safety [AJ]
- Hub and registry adoption not publicly verified [NPV]
- No library release on PyPI since 1.1.1 (10 October 2025) [VF: A7-S038]; no security policy file found

**Choose when**

- You fine-tune or distil models internally and must prove served weights equal validated weights [AJ]

**Avoid when**

- You only consume hosted model APIs [AJ]

**Nearest competitors:** C7-model-supply-chain-scanning, C7-hiddenlayer

**Regulated-FS note.** Sign with a firm-controlled key or HSM and verify the signature at model-server start-up [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | OpenSSF AI/ML Working Group (Linux Foundation); reference implementation in Sigstore model-transparency; contributors include Google, NVIDIA and HiddenLayer | Verified fact | A7-S040, A7-S038 |
| Category | Open specification and library for signing and verifying ML models | Verified fact | A7-S040 |
| Version / lineup | v1.0 launched 4 April 2025; model-signing 1.1.1 on PyPI (10 October 2025); OpenSSF podcast (July 2026) refers to v1.1 and v1.2 iterations | Verified fact | A7-S040, A7-S038, V2-S028 |
| Licence | Open source, Apache-2.0 (library) | Verified fact | A7-S038 |
| Strategic direction | Not publicly verified | Not publicly verified |  |
| What it does | Signs a model of any format and size with a detached signature (Sigstore bundle) stored with the model, using Sigstore, self-signed certificates or key pairs, so consumers can verify integrity and signer before loading. | Verified fact | A7-S040 |
| Stack position | C7 supply-chain control complementing scanning: verifies integrity and signer, not provenance or safety | Architectural judgement |  |
| Integration | Python library and CLI (sign/verify) | Verified fact | A7-S038, A7-S040 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source | Verified fact | A7-S038 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Not publicly verified | | |

## Prisma AIRS (AI Runtime Security) 3.0 (`C7-prisma-airs`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strongest runtime platform technically, but product-scoped certification is unconfirmed and credit licensing plus a proprietary SDK create lock-in; Strategic candidate only in Palo Alto estates after due diligence [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading breadth across C7 research questions: supply chain, agent artefacts, red-teaming, runtime and gateway. |
| Enterprise readiness | 3 | Tenant RBAC roles, AIRS API role and red-team override audit trail verified (B-C7-S003); AIRS-specific SSO and admin audit logs not documented, so 3. |
| Security and compliance | 3 | Company-level SOC 2 Type II and ISO 27001 with product scope not stated: one below the anchor of 4 (rule 8). |
| Deployment flexibility | 4 | Managed SaaS, AWS Marketplace, private-cloud firewall and local scans; on-prem and air-gap not verified. |
| Ecosystem | 4 | Registry, cloud-AI-platform and agent-tool connectors. |
| Reliability and maturity | 3 | GA with monthly releases, but three acquisitions in ten months and conflicting region documentation. |
| Cost / TCO | 3 | Published but complex pricing (token-metered credits, PAYG SKU). |
| Lock-in / portability | 2 | Proprietary SDK licence and credit licensing tied to Strata Cloud Manager; Palo Alto is the acquirer, so no rule 3 reduction. |
| **Total (generic / FS)** | **3.60 / 3.35** | |

**Capabilities.** AI security platform (3.0, 23 March 2026): AI Model Security (35+ formats, 25+ threat categories, local scans), AI Red Teaming (including agents), AI Runtime by API or network intercept, Agent Artifact Scanning (agent code, MCP servers, skills), AI Skill Security and AI Gateway (GA 16 July 2026) [VF: A7-S027, A7-S028, A7-S039, V2-S048].

**Strengths**

- Broadest coverage across supply chain, red-teaming, runtime and gateway [VF: A7-S027, A7-S028] [AJ]
- Registry integrations (JFrog Artifactory, GitLab Model Registry) and connectors for Microsoft Foundry, Copilot Studio and others [VF: A7-S028, A7-S031]
- Tenant RBAC roles and audit trail of red-team verdict overrides; scan logs to SIEM [VF: B-C7-S003]
- Private-cloud firewall deployment (ESXi, KVM, OpenShift, Rancher) [VF: A7-S031]

**Limitations and risks**

- Company-level SOC 2 Type II and ISO 27001:2022; Prisma AIRS scope not stated [VF: B-C7-S002]
- Not FedRAMP; API intercept unavailable in FedRAMP environments [VF: A7-S120, A7-S031]
- EU-Germany region routes some functions through the Netherlands; several modules Americas-only [VF: A7-S120]
- Credit-based licensing, one-billion-token monthly minimum and proprietary SDK licence [VF: A7-S031, A7-S063]
- Integration churn after Protect AI, Koi and Portkey acquisitions [VF: A7-S014, A7-S016] [AJ]

**Choose when**

- Palo Alto Networks is already your network security platform [AJ]
- You want one supplier for model scanning, red-teaming and runtime inspection [AJ]

**Avoid when**

- You need all processing in one EU jurisdiction [AJ]
- You do not want your AI gateway and AI security vendor to be the same company [AJ]

**Nearest competitors:** C7-hiddenlayer, C7-lakera, C7-model-supply-chain-scanning

**Regulated-FS note.** Map processing region per module before onboarding; if the AI Gateway is adopted, record gateway plus security as one concentration point in the register of information [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Palo Alto Networks (acquired Protect AI, July 2025; Koi, April 2026; Portkey, May 2026) | Verified fact | A7-S014, A7-S016 |
| Category | AI security platform: model scanning, posture, AI red teaming, runtime protection, agent security, AI gateway | Verified fact | A7-S014, A7-S027, A7-S028 |
| Version / lineup | Prisma AIRS 3.0 launched 23 March 2026 (2.0 on 28 October 2025); monthly feature releases through August 2026; modules: AI Model Security, AI Red Teaming, AI Runtime (API and network intercept), Agent Artifact Scanning, AI Skill Security, AI Gateway (GA 16 July 2026) | Verified fact | A7-S027, A7-S015, A7-S028, A7-S031 |
| Licence | Proprietary; BYOL funded with Software NGFW credits; Python API-intercept SDK (pan-aisecurity 0.11.0) under proprietary licence | Verified fact | A7-S031, A7-S063 |
| Status events | 28 April 2025: intent to acquire Protect AI announced; 22 July 2025: Protect AI acquisition completed; 28 October 2025: Prisma AIRS 2.0 completes Protect AI integration; 23 March 2026: Prisma AIRS 3.0; 14 April 2026: Koi acquired (agentic endpoint security, to enhance Prisma AIRS); 29 May 2026: Portkey acquired (AI gateway); 16 July 2026: AI Gateway GA | Verified fact | A7-S014, A7-S015, A7-S027, A7-S016, A7-S028, V2-S039, V2-S048, V2-S025 |
| Strategic direction | Moving from observing AI to 'authorising autonomous execution': agent artifact scanning (agent code, MCP servers, skills), agent red teaming (tool chaining, privilege misuse, memory poisoning), AI gateway from Portkey, integration with Anthropic inference hooks and OpenAI Codex Enterprise | Verified fact | A7-S027, A7-S028, A7-S016 |
| What it does | Scans models and agent artefacts for malicious payloads and unsafe permissions, red-teams AI apps and agents, and inspects prompts/responses at runtime via API or network intercept for injection, data leakage and policy violations. AI Model Security analyses 35+ model file types for 25+ threat categories and can run scans locally. | Verified fact | A7-S027, A7-S039, A7-S031 |
| Stack position | Cross-cutting C7 platform spanning supply chain (pre-deployment), runtime (C2/C3 overlap) and gateway (C1 overlap) | Verified fact | A7-S027, A7-S028 |
| Integration | API intercept (SDK/REST), network intercept (AI runtime firewall), model registry scan sources (JFrog Artifactory, GitLab Model Registry), connectors for Microsoft Foundry, Copilot Studio, n8n, Anthropic inference hooks, OpenAI Codex Enterprise | Verified fact | A7-S028, A7-S031 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Prisma AIRS not listed among Palo Alto Networks' FedRAMP-authorised offerings (Prisma Cloud, Prisma Access, Prisma SASE are); API intercept unavailable in FedRAMP environments. SOC 2/ISO for AIRS not verified. | Verified fact | A7-S120, A7-S031 |
| GDPR / residency | API Intercept regions: Americas, EU-Germany, India, Singapore, Japan (region determines processing and storage), but in EU-Germany URL category detection and contextual grounding run via the Netherlands; older firewall setup pages state US-only inspection; AI Model Security in US, EU-Netherlands, Japan, Singapore; AI Skill Security and AI Discovery Americas only | Verified fact | A7-S120, A7-S031 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | BYOL credits; AI Runtime API metered in billions of tokens per month (1 token = 4 characters, minimum 1 billion) from February 2026; Managed AIRS for AWS PAYG premium SKU US$3.00/hour plus traffic from US$0.065/GB | Verified fact | A7-S031 |
| Infrastructure cost | Network intercept needs at least 4 vCPUs; capacity up to 10K AI transactions per day per vCPU | Verified fact | A7-S031 |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (Managed SaaS firewall on AWS, Azure, GCP; Strata Cloud Manager); managed_cloud: Yes (Managed AIRS for AWS via AWS Marketplace); vpc_byoc: Not publicly verified; private_cloud: Yes (runtime firewall on ESXi, KVM, OpenShift, Rancher); self_hosted: Yes (model scans run locally; VM-series firewall images); on_prem: Not publicly verified | | |

## HiddenLayer AI Security Platform (`C7-hiddenlayer`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Capable independent specialist, but dated certification evidence, unverified deployment breadth and opaque pricing [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Model scanning plus agent runtime and coding-agent protection; red-teaming not evidenced. |
| Enterprise readiness | 3 | SAML SSO and RBAC verified (B-C7-S004); audit logs not documented, so 3 (rule 7). |
| Security and compliance | 3 | ISO 27001 and SOC 2 Type 2 at company level, scope not stated and evidence 20 months old: one below anchor (rule 8). |
| Deployment flexibility | 3 | Customer AWS VPC verified; SaaS and on-prem only reported. |
| Ecosystem | 3 | REST API, Python SDK, AWS Marketplace, Databricks Unity Catalog. |
| Reliability and maturity | 3 | Independent and funded; agentic modules launched in 2026. |
| Cost / TCO | 2 | Contract-only pricing, not published. |
| Lock-in / portability | 3 | Proprietary platform with Apache-2.0 SDK; independent ownership. |
| **Total (generic / FS)** | **3.10 / 3.10** | |

**Capabilities.** Model supply-chain scanning for registries and storage (S3, EFS, container registries), AI Runtime Security for agents against prompt injection, secret exposure and unsafe commands, and Agent Harness Security for coding agents (3 August 2026) [VF: A7-S017, A7-S029].

**Strengths**

- Independent; US$100m Series B on 2 September 2026 [VF: A7-S017, V2-S047]
- ISO 27001 and SOC 2 Type 2 announced February 2025 [VF: A7-S030]
- SAML SSO with RBAC and tenant user management [VF: B-C7-S004]
- Deploys inside the customer's AWS environment with private networking [VF: A7-S029]; co-contributor to OpenSSF Model Signing [VF: A7-S040]

**Limitations and risks**

- Certification evidence dated February 2025; no trust centre found [VF: A7-S030]
- SaaS and on-prem or air-gapped deployment rest on vendor text in a third-party listing [R: A7-S029]
- No customer audit-log documentation found [VF: B-C7-S004]
- Contract-only pricing [VF: A7-S029]

**Choose when**

- You want an independent model-scanning and agent-runtime specialist outside a network-security suite [AJ]

**Avoid when**

- You need verified on-prem or EU-region deployment today [AJ]

**Nearest competitors:** C7-prisma-airs, C7-lakera, C7-model-supply-chain-scanning

**Regulated-FS note.** Obtain current SOC 2 and ISO certificates and a change-of-control exit clause; independents in this market have tended to be acquired [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | HiddenLayer (independent; US$100 million Series B in September 2026, total raised over US$155 million) | Verified fact | A7-S017 |
| Category | AI security platform: model supply-chain scanning, AI runtime security for agents, AI threat detection and response | Verified fact | A7-S017, A7-S029 |
| Version / lineup | Modules: AI Supply Chain Security (Model Scanner), AI Runtime Security (agentic capabilities, March 2026), Agent Harness Security for coding agents (3 August 2026); hiddenlayer-sdk 3.10.0 (10 September 2026) | Verified fact | A7-S017, A7-S029, A7-S062 |
| Licence | Proprietary platform; Python client SDK Apache-2.0 | Verified fact | A7-S062 |
| Status events | 23 March 2026: next-generation AI Runtime Security for agents; 3 August 2026: Agent Harness Security launched; 2 September 2026: US$100m Series B (Delta-v Capital lead) | Verified fact | A7-S017, V2-S047 |
| Strategic direction | Focus on agentic runtime security and AI coding-agent protection; Databricks Unity Catalog integration being extended | Verified fact | A7-S017 |
| What it does | Scans model files for malicious code and vulnerabilities in registries and storage (S3, EFS, container registries), and protects agents at runtime against prompt injection, secret exposure and unsafe commands. | Verified fact | A7-S029, A7-S017 |
| Stack position | C7 across model supply chain and runtime | Verified fact | A7-S029, A7-S017 |
| Integration | REST API and Python SDK; AWS Marketplace; Databricks Unity Catalog integration | Verified fact | A7-S062, A7-S029, A7-S017 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | ISO 27001 and SOC 2 Type 2 (all five trust services criteria) announced 13 February 2025 | Verified fact | A7-S030 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Encryption at rest and in transit (security page) | Verified fact | A7-S030 |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Custom/contract-based; available through AWS Marketplace private offers | Verified fact | A7-S029 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Investors include Morgan Stanley and Microsoft's venture fund (Series B); co-contributor to OpenSSF Model Signing v1.0 | Verified fact | A7-S017, A7-S040 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Yes (inside customer AWS environment with private networking); private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Yes (on-prem, air-gapped or hybrid per vendor listing text) | | |

## Check Point AI Guardrails (formerly Lakera Guard), part of the Check Point AI Defense Plane; AI Agent Security in early access (`C7-lakera`)

**Tier:** Tactical · **Flags:** Acquired, Renamed · **Original graphic label:** not in graphic

*Rationale:* Focused, self-hostable runtime detector; acquisition, renaming, proprietary API and default prompt logging keep it a replaceable component [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Covers runtime injection, leakage and content screening and early-access agent discovery; no supply-chain scanning or red-teaming. |
| Enterprise readiness | 3 | SSO, RBAC (three roles) and SIEM export verified on Enterprise (rule 7); no SCIM or SLA found, so 3. |
| Security and compliance | 3 | SOC 2 Type II stated in vendor docs plus encryption (B-C7-S001); no ISO 27001; anchor 3. |
| Deployment flexibility | 4 | SaaS, self-hosted, private cloud and on-prem; air-gap not verified. |
| Ecosystem | 3 | REST API and SIEM export; broader integrations not verified. |
| Reliability and maturity | 3 | GA product; ownership change (Check Point, 22 October 2025) and naming in flux. |
| Cost / TCO | 3 | Published free tier; Enterprise quote-based. |
| Lock-in / portability | 2 | Proprietary Guard API (base 3), reduced by 1 for the 2025 acquisition (rule 3). |
| **Total (generic / FS)** | **3.10 / 3.00** | |

**Capabilities.** Runtime screening of prompts and responses through the Guard API for prompt attacks, data leakage (including PII), content violations and off-policy agent behaviour; AI Agent Security (early access from 10 April 2026) adds agent discovery and configuration risk assessment inside the Check Point AI Defense Plane [VF: A7-S025, A7-S026].

**Strengths**

- Self-hostable on-premises or in a private cloud, with EU residency on SaaS [VF: A7-S023, A7-S024]
- SOC 2 Type II stated in vendor docs; encryption at rest and in transit [VF: B-C7-S001]
- SSO, RBAC and SIEM export on Enterprise [VF: A7-S023, A7-S024]
- Free Community tier for evaluation (10,000 requests/month) [VF: A7-S023]

**Limitations and risks**

- Acquired by Check Point (completed 22 October 2025); naming in flux between Lakera and Check Point [VF: A7-S013, V2-S038, V2-S067]
- Dashboard records all prompts and model outputs by default [VF: B-C7-S001]
- No ISO 27001 certificate found [VF: B-C7-S001]
- Proprietary Guard API; no supply-chain scanning or red-teaming in the product [VF: A7-S025] [AJ]

**Choose when**

- You need a self-hostable runtime injection and leakage detector [AJ]
- Check Point is already your security standard [AJ]

**Avoid when**

- You need model scanning or red-teaming from the same product [AJ]
- You cannot control the detector's own prompt logging and retention [AJ]

**Nearest competitors:** C7-prisma-airs, C7-hiddenlayer

**Regulated-FS note.** Self-host for client data or switch off default prompt logging and align retention to the records policy; refresh due diligence after the change of control [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Check Point Software Technologies (acquired Lakera AI AG, Zurich) | Verified fact | A7-S012, A7-S013 |
| Category | AI runtime security: prompt-attack, data-leakage and policy guardrails for LLM apps and agents | Verified fact | A7-S025 |
| Version / lineup | AI Guardrails (runtime, Guard API; standalone tier available); AI Agent Security (early access from 10 April 2026); umbrella 'Check Point AI Defense Plane' launched 23 March 2026 | Verified fact | A7-S025, A7-S026 |
| Licence | Proprietary (SaaS and self-hosted licence) | Verified fact | A7-S023, A7-S024 |
| Status events | 16 September 2025: Check Point announced agreement to acquire Lakera (value not disclosed; reported c. US$300 million); 22 October 2025: completion (confirmed in Check Point Q3 2025 results); completion press release circulated 11 November 2025; FY2025 20-F reportedly gives consideration of about US$201.8m (second-hand); 23 March 2026: Check Point AI Defense Plane launched; 10 April 2026: AI Agent Security in early access | Verified fact | A7-S012, A7-S013, A7-S026, A7-S025, V2-S038, V2-S067 |
| Strategic direction | Check Point uses Lakera as the foundation of its Global Center of Excellence for AI Security, with Zurich as global AI security R&D centre; extending from guardrails to agent discovery, configuration risk assessment and runtime protection | Verified fact | A7-S012, A7-S025 |
| What it does | Screens prompts and responses through the Guard API to detect prompt attacks, data leakage (including PII), content violations and off-policy agent behaviour. AI Agent Security adds discovery of agents across platforms and risk assessment of their configuration. | Verified fact | A7-S025 |
| Stack position | Runtime control at the application/gateway boundary (C7, overlapping C2 guardrails and C3 DLP) | Verified fact | A7-S025 |
| Integration | Guard REST API; SIEM log export (Enterprise) | Verified fact | A7-S025, A7-S024 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Claims SOC 2 and GDPR compliance (pricing page; SOC 2 type not stated) | Verified fact | A7-S023 |
| GDPR / residency | Community tier: EU data residency; Enterprise: EU or US; self-hosting for full residency control | Verified fact | A7-S023, A7-S024 |
| Security features | Encryption in transit and at rest (pricing page) | Verified fact | A7-S023 |
| Access controls | SSO, RBAC (three roles) and SIEM log export are Enterprise-only | Verified fact | A7-S023, A7-S024 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Community: US$0/month, 10,000 requests/month, 8k-token prompt limit, SaaS, community support; Enterprise: quote-based (as read 7 October 2026; page undated) | Verified fact | A7-S023 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Yes; self_hosted: Yes (AI Guardrails self-hosting); on_prem: Yes | | |

# C8: Model risk, governance and auditability

## OpenLineage (with Marquez reference implementation) (`C8-openlineage`)

**Tier:** Strategic · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* The neutral lineage interchange standard; the firm must add GenAI facets [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Competent lineage model and protocol; no GenAI facets. |
| Enterprise readiness | 3 | Rule 2: specification and clients inherit host controls; no commercial support verified. |
| Security and compliance | 3 | Rule 2 hygiene: Apache-2.0, foundation governance, monthly releases; no security policy file found. |
| Deployment flexibility | 5 | Self-hosted consumers anywhere; cloud lineage transports. |
| Ecosystem | 5 | De-facto open lineage standard across Airflow, Spark, dbt, Flink, Collibra and GCP. |
| Reliability and maturity | 4 | Graduate project with roughly monthly releases since 2021; Marquez slower. |
| Cost / TCO | 4 | Free; a backend (Marquez or catalogue) must be operated. |
| Lock-in / portability | 5 | Open specification, Apache-2.0, neutral governance. |
| **Total (generic / FS)** | **3.80 / 3.85** | |

**Capabilities.** Open specification for runtime data-lineage metadata (run, job and dataset entities extended by facets, and an event protocol), with Python, Java and SQL clients and the Marquez reference implementation; 1.53.0 adds explicit dataset-, field- and job-level lineage facets [VF: A7-S041, A7-S043, A7-S042].

**Strengths**

- Neutral, foundation-governed (LF AI & Data Graduate) and Apache-2.0 [VF: A7-S041]
- Airflow provider, Spark, dbt and Flink integrations; GCP Lineage transport; Collibra integration [VF: A7-S045, A7-S042, A7-S122]
- Tag facets can carry classification labels [VF: A7-S042]

**Limitations and risks**

- No GenAI, LLM, embedding or vector facets [VF: A7-S042]
- Marquez releases slowed (0.51.1, March 2025) [VF: A7-S044]
- Does not capture run-time LLM calls (OTel's job) [AJ]

**Choose when**

- Always, for L8 ingestion and index-build pipelines [Rec]

**Avoid when**

- You expect it to trace run-time LLM calls [AJ]

**Nearest competitors:** C8-collibra-ai-governance, OTel GenAI semantic conventions

**Regulated-FS note.** Define and publish a firm GenAI facet set (source document IDs, classification tags, chunking and embedding model versions, index version) [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | LF AI & Data Foundation Graduate project (OpenLineage); Marquez is a separate LF AI & Data Graduated project | Verified fact | A7-S041, A7-S043 |
| Category | Open specification for runtime data-lineage metadata, with client libraries and integrations | Verified fact | A7-S041 |
| Version / lineup | openlineage-python 1.53.0 (1 September 2026); spec version 2-0-2 (Marquez compatibility table); Marquez latest image 0.51.1 (27 March 2025) | Verified fact | A7-S001, A7-S043, A7-S044, V2-S028 |
| Licence | Open specification and code, Apache-2.0 (OpenLineage and Marquez) | Verified fact | A7-S041, A7-S043, A7-S001 |
| Strategic direction | 1.53.0 adds explicit lineage facets (exact dataset-, field- and job-level relationships), more Spark/Flink/dbt coverage and GCP Lineage transport retries; user-supplied tags facets in Python and Java clients | Verified fact | A7-S042 |
| What it does | Defines a generic model of run, job and dataset entities with consistent naming, extended by facets, and an event protocol for emitting lineage as jobs run; Marquez collects, stores and visualises these events. | Verified fact | A7-S041, A7-S043 |
| Stack position | Lineage backbone for C8 and L8 ingestion (H7); GenAI/RAG steps (chunking, embedding, indexing) would need custom facets | Architectural judgement |  |
| Integration | OpenAPI-defined spec; Python, Java and SQL clients; integrations for Spark, Airflow, dbt, Flink; GCP Lineage and GCS transports | Verified fact | A7-S041, A7-S042 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not applicable (open specification) | Architectural judgement |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free open source | Verified fact | A7-S041 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Apache Airflow ships an OpenLineage provider (apache-airflow-providers-openlineage 2.20.2, 29 September 2026); Collibra documents an OpenLineage integration; Egeria listed as related project | Verified fact | A7-S045, A7-S122, A7-S041 |
| Adoption signals | Marquez Docker image pulled about 1.12 million times; openlineage-python first released May 2021 | Verified fact | A7-S044, A7-S001 |
| Maturity | OpenLineage releases roughly monthly (1.50-1.53 in 2026); Marquez releases slowed (0.51.1 in March 2025) | Verified fact | A7-S042, A7-S044 |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Marquez or other OpenLineage consumers); on_prem: Not publicly verified | | |

## IBM watsonx.governance (`C8-watsonx-governance`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Highest technical coverage; Tactical only because certification scope is not publicly verified; conditional Strategic for IBM estates after due diligence [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 5 | Leading coverage: inventory, evaluation of models, prompts and agents, discovery, thresholds, approvals, compliance mapping. |
| Enterprise readiness | 3 | IAM-controlled access, console roles and approval audit trail verified (B-C8-S003); SSO federation and SCIM not verified, so 3. Rule 6 not applied (IBM service on AWS, not an AWS service). |
| Security and compliance | 2 | Capped at 2: product-scoped certifications not publicly verified and FedRAMP status conflicting. |
| Deployment flexibility | 4 | SaaS, self-managed in customer cloud, on-prem and hybrid; air-gap not verified. |
| Ecosystem | 4 | Python SDK, Orchestrate, OpenPages and SageMaker integration. |
| Reliability and maturity | 4 | IBM product with continuous releases (SDK 1.5.2, September 2026). |
| Cost / TCO | 3 | Published indicative pricing including free tier. |
| Lock-in / portability | 3 | Proprietary, IBM-licensed; factsheets exportable. |
| **Total (generic / FS)** | **3.60 / 3.40** | |

*Evidence rules applied:* security_compliance capped at 2: product-scoped SOC 2/ISO 27001 not publicly verified; FedRAMP status conflicting (B-C8-S002)

**Capabilities.** Inventories AI use cases and models; evaluates models, prompt templates and agents; monitors in production and ties metrics to risks, controls and approvals; Compliance Accelerators; AI Asset Discovery (9 July 2026) for unmanaged agents, tools, MCP servers and models; Enforcement Tracking (11 August 2026) for agent metrics against thresholds; exportable factsheets [VF: A7-S103, A7-S111, A7-S058, B-C8-S003].

**Strengths**

- Broadest agent-aware governance; consumes evaluation and Guardium security evidence automatically [VF: A7-S111] [AJ]
- SaaS (IBM Cloud, AWS), self-managed in AWS/Azure, on-prem and hybrid [VF: A7-S103]
- Published, indicative pricing (Lite free; US$0.64 per evaluation) [VF: A7-S103]
- IAM and Governance-console roles; approval-workflow audit trail [VF: B-C8-S003]

**Limitations and risks**

- No product-scoped SOC 2 or ISO 27001 found; FedRAMP wording conflicts [VF: A7-S103, B-C8-S002]
- SR 11-7 accelerator maps to a superseded instrument; no SS1/23 or SR 26-2 claim [VF: A7-S103] [AJ]
- Coupling to IBM's agent runtime (watsonx Orchestrate) [VF: A7-S111]
- Pricing table in source garbled; confirm [VF: A7-S103]

**Choose when**

- You run watsonx Orchestrate or OpenPages, or want one platform for discovery, evaluation and governance of agents [AJ]

**Avoid when**

- You want governance independent of your agent runtime vendor [AJ]

**Nearest competitors:** C8-validmind, C8-modelop, C8-credo-ai

**Regulated-FS note.** Obtain SOC 2 and ISO scope letters naming watsonx.governance; record IBM as one concentration point if Vault (C7) is also used [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | IBM | Verified fact | A7-S058 |
| Category | AI governance, evaluation and model risk platform | Verified fact | A7-S058 |
| Version / lineup | Continuous SaaS updates (IBM Cloud catalog updated 20 July 2026); v2.2.0 introduced policy packs; 2026 features: AI Asset Discovery (9 July 2026), Enforcement Tracking (11 August 2026), Guardium security metrics; SDK ibm-watsonx-gov 1.5.2 (18 September 2026) | Verified fact | A7-S103, A7-S111, A7-S058 |
| Licence | Proprietary; SDK under IBM International License Agreement for Non-Warranted Programs | Verified fact | A7-S058 |
| Strategic direction | Agentic governance: automatic retrieval of agent evaluation metrics against governance thresholds, discovery of unmanaged agents, tools, MCP servers and models, regulatory horizon scanning (CUBE) previewed at Think 2026, integration with watsonx Orchestrate | Verified fact | A7-S111 |
| What it does | Inventories AI use cases and models, evaluates models, prompt templates and agents, monitors them in production and ties metrics to risks, controls and approvals; Compliance Accelerators map obligations to controls. | Verified fact | A7-S103, A7-S111, A7-S058 |
| Stack position | C8 governance consuming L9 evaluation/monitoring evidence and C7 security findings (Guardium) | Verified fact | A7-S111 |
| Integration | Python SDK with sample notebooks | Verified fact | A7-S058, A7-S094 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | FedRAMP-authorised watsonx.governance on AWS GovCloud (IBM page); SOC 2/ISO not verified | Verified fact | A7-S103 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Lite free tier; Essentials pay-as-you-go (model evaluation US$0.64 per evaluation, about 100 free); GRC per-instance and per-concurrent-user charges; AWS SaaS bundle US$38,160 (1 instance, 12,000 evaluations/year, 5 use cases, 25 concurrent users); self-managed priced per virtual processor core; indicative, varies by country | Verified fact | A7-S103 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | IBM states Leader in 2026 IDC MarketScape for AI-enabled financial GRC (with OpenPages) | Verified fact | A7-S103 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (IBM Cloud, AWS); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (software in customer-managed AWS/Azure; licences on both marketplaces); on_prem: Yes (on-premises and hybrid) | | |

## Credo AI AI governance platform (AI Registry, policy packs, Govern AI Assistant) (`C8-credo-ai`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strong deployment and identity controls for policy-led governance; certification evidence unconfirmed and validation depth limited [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 3 | Inventory, policy and evidence strong; validation and monitoring workflows not evidenced. |
| Enterprise readiness | 4 | SSO, SCIM, audit-log APIs and role scopes verified. |
| Security and compliance | 2 | Capped at 2: SOC 2 Type II report not re-confirmed (V2 section 4 item 9). |
| Deployment flexibility | 5 | EU SaaS, self-hosted and air-gapped. |
| Ecosystem | 4 | 30+ partner integrations including Azure, watsonx, Databricks, Collibra. |
| Reliability and maturity | 3 | Independent; last disclosed round July 2024; Lens deprecated. |
| Cost / TCO | 2 | Pricing not published. |
| Lock-in / portability | 3 | Proprietary but independent; audit-log APIs give data access. |
| **Total (generic / FS)** | **3.30 / 3.25** | |

*Evidence rules applied:* security_compliance capped at 2: SOC 2 Type II report not re-confirmed (V2 verification log section 4)

**Capabilities.** AI governance platform: AI Registry with auto-discovery, policy packs (EU AI Act, NIST AI RMF, ISO 42001, SOC 2) from a knowledge graph of 160+ policies and 110+ controls, audit-ready evidence and audit trails; moving to agent registry and runtime governance; AIUC-1 integrated [VF: A7-S102].

**Strengths**

- Widest deployment choice: SaaS on AWS (US) or Azure (EU), self-hosted Kubernetes, air-gapped [VF: A7-S107, A7-S123]
- SSO via OIDC (SAML via dex), SCIM, audit logs and audit-log APIs, role scopes [VF: A7-S123]
- Integrations with Azure, watsonx, Databricks, Collibra and 30+ partners [VF: A7-S102, A7-S110]

**Limitations and risks**

- SOC 2 Type II report listed but not re-confirmed by the verifier [VF: A7-S107, V2-S064]; no ISO 27001/42001 found
- No SR 26-2 or SS1/23 mapping found; light on model validation [VF: A7-S110] [AJ]
- Open-source Lens deprecated (last release May 2023) [VF: A7-S092, A7-S093]
- Pricing not published [NPV]

**Choose when**

- The programme is policy- and compliance-led across many business units [AJ]

**Avoid when**

- The main need is quantitative model validation [AJ]

**Nearest competitors:** C8-collibra-ai-governance, C8-watsonx-governance, C8-modelop

**Regulated-FS note.** Self-host or use the Azure EU instance; obtain the current SOC 2 report directly [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Credo AI | Verified fact | A7-S092, A7-S093 |
| Category | AI governance platform (registry, policy packs, evidence, third-party AI risk) | Verified fact | A7-S102, A7-S110 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Proprietary (SaaS and self-hosted); open-source Lens deprecated | Verified fact | A7-S107, A7-S123, A7-S092 |
| Status events | Open-source 'Lens' responsible-AI assessment framework marked deprecated / 'no longer maintained'; last PyPI release 1.1.8 on 3 May 2023 | Verified fact | A7-S092, A7-S093 |
| Strategic direction | Moving to agent governance: Agent Registry, runtime governance and Govern AI Assistant (GA in 2026); AIUC-1 agent standard integrated (Credo does not issue certification); policy packs for OMB M-25, Colorado ADMT, NAIC AI | Verified fact | A7-S102 |
| What it does | Auto-discovers and catalogues AI systems in an AI Registry, applies pre-built policy packs (EU AI Act, NIST AI RMF, ISO 42001, SOC 2) from a knowledge graph of 160+ policies and 110+ controls, and generates audit-ready evidence and audit trails. | Verified fact | A7-S102 |
| Stack position | C8 enterprise AI governance (policy/compliance evidence) rather than model-level validation; vendor contrasts this with SR 11-7 model risk management | Verified fact | A7-S110 |
| Integration | Integrations with Microsoft Azure, IBM watsonx, Databricks, Collibra and 30+ partners; audit-log APIs; SCIM provisioning | Verified fact | A7-S102, A7-S110, A7-S123 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 2 Type II (report dated 31 December 2025; Q3 2026 bridge letter) covering security, availability, confidentiality; no ISO 27001/42001 certificate found | Verified fact | A7-S107 |
| GDPR / residency | EU hosting on Microsoft Azure in Europe; US hosting on AWS | Verified fact | A7-S107 |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | SSO via OIDC (SAML via dex) for self-hosted; SCIM; audit logs and audit-log APIs; role scopes in tokens | Verified fact | A7-S123 |
| Enterprise support | Advisory services; vendor claims governance workflows stood up in 4 weeks | Verified fact | A7-S102 |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Vendor-stated: Visionary in Gartner's inaugural Magic Quadrant for AI Governance Platforms; Leader per Forrester and IDC; Fast Company Most Innovative 2026 | Verified fact | A7-S102 |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (AWS US; Azure EU); managed_cloud: Not publicly verified; vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Yes (Kubernetes, EKS validated, Replicated); on_prem: Yes (air-gapped install supported) | | |

## Collibra AI Governance / AI Command Center (Collibra 'Enterprise AI Control Plane') (`C8-collibra-ai-governance`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Strong certifications and the lineage bridge, but SaaS-only deployment and no validation workflow [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Inventory, assessments, controls mapping and lineage link; no validation or monitoring workflow. |
| Enterprise readiness | 3 | SAML SSO and roles verified (B-C8-S004); audit logs not documented, so 3 (rule 7). |
| Security and compliance | 4 | Company-level certifications meeting the 5 anchor, product scope not stated: 4 (rule 8). |
| Deployment flexibility | 2 | SaaS on AWS and GCP only; no self-host or VPC evidence. |
| Ecosystem | 4 | SageMaker, Azure AI Foundry and Databricks connectors; CLI; OpenLineage. |
| Reliability and maturity | 3 | Established vendor; AI module repositioned and acquisition just announced. |
| Cost / TCO | 2 | Pricing not published. |
| Lock-in / portability | 3 | Proprietary SaaS; OpenLineage integration eases lineage portability. |
| **Total (generic / FS)** | **3.20 / 3.20** | |

**Capabilities.** AI governance on Collibra's data intelligence platform: AI use-case register, model and agent asset domains linked to model versions and agents from integrated AI platforms, EU AI Act and NIST AI RMF assessment templates, 46 controls mapped to EU AI Act, NIST and BCBS 239; OpenLineage integration; trail ML acquisition (announced 5 October 2026) for continuous assessment and runtime enforcement [VF: A7-S099, A7-S122, A7-S101].

**Strengths**

- Only product joining the AI inventory to the data catalogue and lineage (OpenLineage) [VF: A7-S122, A7-S099] [AJ]
- Company-level SOC 1/2, ISO 27001/27017/27018, ISO 42001, FedRAMP, HIPAA [VF: A7-S106, A7-S100, V2-S064]
- SAML 2.0 SSO with IdP group mapping and global roles [VF: B-C8-S004]
- BCBS 239 control mapping useful for bank-owned managers [VF: A7-S099]

**Limitations and risks**

- SaaS only on current evidence (AWS and GCP); self-hosting and EU region list not verified [VF: A7-S122] [NPV]
- No model validation or monitoring workflow [AJ]
- trail ML deal three days old; integration roadmap open [VF: V2-S044]
- Pricing not published [NPV]

**Choose when**

- Collibra is already the data catalogue of record [AJ]

**Avoid when**

- You need self-hosting or a model-validation workflow [AJ]

**Nearest competitors:** C8-credo-ai, C8-watsonx-governance, C8-modelop

**Regulated-FS note.** Use the BCBS 239 mapping for bank-owned managers; confirm EU hosting and the trail ML integration roadmap [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | Collibra (acquired trail ML, Munich, announced 5 October 2026) | Verified fact | A7-S105, A7-S101 |
| Category | AI governance on a data intelligence/governance platform (AI use-case registry, assessments, controls) | Verified fact | A7-S099, A7-S122 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Proprietary SaaS | Verified fact | A7-S122 |
| Status events | January 2025: ISO 42001 certification (Schellman); AI Pact signatory; 5 October 2026: acquisition of trail ML announced (price undisclosed) | Verified fact | A7-S100, A7-S105, V2-S044, V2-S064 |
| Strategic direction | Repositioned as 'The Enterprise AI Control Plane'; adding agent-powered continuous assessment and runtime enforcement via trail ML; code-first registry CLI; AIUC-1 templates (May 2026) | Verified fact | A7-S122, A7-S105, A7-S099 |
| What it does | Provides an AI use-case register and model/agent asset domains, links use cases to model versions and agents from integrated AI platforms, runs EU AI Act and NIST AI RMF assessment templates and 46 controls mapped to EU AI Act, NIST and BCBS 239 articles. | Verified fact | A7-S099 |
| Stack position | C8 governance anchored in the data catalogue and lineage layer (bridges H7 data lineage and AI inventory) | Verified fact | A7-S099, A7-S122 |
| Integration | Platform-agnostic connectors to AWS SageMaker, Azure AI Foundry, Databricks; developer CLI manifests; OpenLineage integration | Verified fact | A7-S122, A7-S099 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | SOC 1, SOC 2, ISO 27001, 27017, 27018, ISO 42001, FedRAMP, ITAR, HIPAA, TISAX; CSA STAR self-assessment | Verified fact | A7-S106, A7-S100, V2-S064 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Not publicly verified | Not publicly verified |  |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Yes (managed on AWS and GCP); managed_cloud: Yes (Cloud Sites); vpc_byoc: Not publicly verified; private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |

## ModelOp Center (positioned as 'Enterprise AI Command Center') (`C8-modelop`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Credible automation claims but the thinnest public evidence in the set [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Inventory, intake, tiering, approvals, templates, tests and blocking workflows (vendor-described). |
| Enterprise readiness | 3 | SAML/OAuth2 IdP integration and role-based access verified (rule 7, maximum 3); audit logs not documented. |
| Security and compliance | 2 | Capped at 2: no certifications publicly verified. |
| Deployment flexibility | 4 | Self-hosted, on-prem, hybrid and EKS; SaaS not verified. |
| Ecosystem | 3 | Connectors and REST APIs; SageMaker, S3, Redshift. |
| Reliability and maturity | 2 | Maturity and release cadence not publicly verified; small disclosed funding. |
| Cost / TCO | 2 | List pricing not published. |
| Lock-in / portability | 3 | Proprietary but self-hostable; independent. |
| **Total (generic / FS)** | **3.00 / 2.95** | |

*Evidence rules applied:* security_compliance capped at 2: certifications not publicly verified (B-C8-S001)

**Capabilities.** AI governance and lifecycle automation ('Enterprise AI Command Center'): inventory with self-service intake, risk tiering and approvals; 25+ governance process templates and 100+ tests and controls; risk-based workflows that can block non-compliant actions; claimed inline protections for agents [VF: A7-S098].

**Strengths**

- Lifecycle automation that can enforce, not only record [VF: A7-S098] [AJ]
- Self-hosted, on-prem, hybrid and EKS via AWS Marketplace [VF: A7-S109]
- Identity-provider integration via OAuth2 and SAML with role-based access [VF: B-C8-S001]

**Limitations and risks**

- No SOC 2 or ISO 27001 evidence found [VF: B-C8-S001] [NPV]
- Maturity, release cadence and SaaS availability not publicly verified [NPV]
- Small disclosed funding (US$10m, date not confirmed) [VF: A7-S104]
- SR 11-7 templates map to a superseded instrument [VF: A7-S110] [AJ]

**Choose when**

- You want self-hosted governance automation with blocking workflows and will do full due diligence [AJ]

**Avoid when**

- Certification evidence is a shortlisting gate [AJ]

**Nearest competitors:** C8-watsonx-governance, C8-validmind, C8-credo-ai

**Regulated-FS note.** Require SOC 2 Type II and audit-log documentation before any pilot with production records [Rec].

**Facts (as of 2026-10-07)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | ModelOp (privately held, Chicago; raised US$10m led by Baird Capital - date not confirmed) | Verified fact | A7-S104 |
| Category | AI governance and AI lifecycle automation software | Verified fact | A7-S098 |
| Version / lineup | Not publicly verified | Not publicly verified |  |
| Licence | Proprietary | Verified fact | A7-S109 |
| Strategic direction | Governs ML, GenAI, agentic, internal and third-party AI from intake to retirement; inline protections for agentic systems (prompt injection, PII leakage, unsafe tool use); vendor claims Visionary in 2026 Gartner Magic Quadrant for AI Governance Platforms | Verified fact | A7-S098, A7-S104 |
| What it does | Maintains an inventory of AI systems with self-service intake, risk tiering and approvals; applies controls from internal policies and regulations via 25+ governance process templates and 100+ tests/controls; risk-based workflows can block non-compliant actions. | Verified fact | A7-S098 |
| Stack position | C8 governance control plane with lifecycle automation; vendor positions Collibra as data governance and Credo as compliance-focused | Verified fact | A7-S098, A7-S110 |
| Integration | Out-of-the-box connectors and REST APIs; AWS SageMaker, S3, Redshift, DocumentDB | Verified fact | A7-S104, A7-S109 |
| Dependencies | Not publicly verified | Not publicly verified |  |
| Certifications | Not publicly verified | Not publicly verified |  |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Not publicly verified | Not publicly verified |  |
| Access controls | Not publicly verified | Not publicly verified |  |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Available through AWS Marketplace; list pricing not published | Verified fact | A7-S109 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Not publicly verified | Not publicly verified |  |
| Adoption signals | Not publicly verified | Not publicly verified |  |
| Maturity | Not publicly verified | Not publicly verified |  |
| Deployment | saas: Not publicly verified; managed_cloud: Not publicly verified; vpc_byoc: Yes (Kubernetes/Amazon EKS via AWS Marketplace); private_cloud: Not publicly verified; self_hosted: Yes; on_prem: Yes (homepage lists Cloud, On-Premise, Hybrid) | | |

## ValidMind AI risk platform (ValidMind Platform and ValidMind Library) (`C8-validmind`)

**Tier:** Tactical · **Flags:** none · **Original graphic label:** not in graphic

*Rationale:* Best MRM workflow fit and the only SS1/23 claimant, held back by unverified certification evidence and unpublished pricing [AJ].

| Criterion | Score | Rationale |
|--------|--:|------------------------------|
| Technical | 4 | Inventory, documentation, validation, approvals, monitoring thresholds and attestation; lineage and agent discovery not evidenced. |
| Enterprise readiness | 3 | RBAC and audit logs verified; SSO not verified, so maximum 3 (rule 7). |
| Security and compliance | 2 | Capped at 2: SOC 2 type not stated and no report found; vendor statement only. |
| Deployment flexibility | 3 | Multi-tenant SaaS plus single-tenant VPV in the major clouds; self-hosting not verified. |
| Ecosystem | 3 | Python Library with LLM, PyTorch and Hugging Face extras; data-source connectors. |
| Reliability and maturity | 3 | Frequent Library releases since May 2023; funding not verified. |
| Cost / TCO | 2 | Pricing not published. |
| Lock-in / portability | 3 | Proprietary platform holding inventory and documentation; export not verified; AGPL library noted. |
| **Total (generic / FS)** | **2.95 / 2.90** | |

*Evidence rules applied:* security_compliance capped at 2: SOC 2 Type II not publicly verified (vendor claim, type not stated)

**Capabilities.** Model risk management platform: Python Library logs tests and documentation artefacts; Platform holds a customisable model inventory and runs documentation, validation workflows, approvals and ongoing monitoring with thresholds, alerts and workflow triggers; LLM test extras and LLM features; point-in-time model attestation [VF: A7-S003, A7-S054, A7-S056, A7-S097, B-C8-S005].

**Strengths**

- Closest fit to bank-style MRM (inventory, documentation, validation, monitoring) with GenAI tests [AJ]
- Only vendor in the set claiming PRA SS1/23 mapping; also SR 26-2, EU AI Act Article 9 and OSFI E-23 (vendor claims) [VF: A7-S051, A7-S052, A7-S053, A7-S057]
- Single-tenant Virtual Private ValidMind on AWS, GCP or Azure with private connectivity [VF: A7-S054, A7-S084]
- RBAC, audit logs, data isolation and encryption documented [VF: A7-S055]

**Limitations and risks**

- SOC 2 claimed without type; no SOC 2 Type II report or ISO certificate found [VF: A7-S121, B-C8-S005]
- SSO and self-hosting not publicly verified [NPV]
- Library is AGPL-3.0 or commercial (licence consideration under rule 4) [VF: A7-S003]
- Pricing not published [VF: A7-S003]

**Choose when**

- A second-line MRM function wants GenAI in the same validation workflow as other models [AJ]

**Avoid when**

- You need a broad AI policy and third-party AI register more than validation, or cannot obtain a SOC 2 Type II report [AJ]

**Nearest competitors:** C8-watsonx-governance, C8-modelop, C8-credo-ai

**Regulated-FS note.** Request the SOC 2 Type II report before loading risk records; check AGPL obligations for any modified Library code you distribute [Rec].

**Facts (as of 2026-10-08)**

| Field | Value | Label | Sources |
|-------|------------------------------|----|-----|
| Company | ValidMind Inc. | Verified fact | A7-S051 |
| Category | Model risk management and AI governance platform (inventory, documentation, validation, monitoring) | Verified fact | A7-S003, A7-S054 |
| Version / lineup | ValidMind Library 2.13.14 released 3 September 2026; Platform is cloud-hosted | Verified fact | A7-S003, V2-S028 |
| Licence | Open core: Library dual-licensed AGPL-3.0 or ValidMind Commercial Licence; Platform proprietary | Verified fact | A7-S003, A7-S051 |
| Strategic direction | Use-case guides map platform workflows to SR 26-2 (successor to SR 11-7), PRA SS1/23, EU AI Act and OSFI E-23; LLM features for test interpretation and document checking; LLM test extras in the Library | Verified fact | A7-S051, A7-S052, A7-S053, A7-S057, A7-S097, A7-S003 |
| What it does | The Library runs tests and logs documentation artefacts from Python model-development environments; the Platform holds a customisable model inventory and runs documentation, validation workflows, approvals and ongoing monitoring with thresholds, alerts and workflow triggers on breach. | Verified fact | A7-S003, A7-S054, A7-S056 |
| Stack position | C8 governance system of record fed by development tests and monitoring results | Verified fact | A7-S003, A7-S056 |
| Integration | Python Library and ValidMind API to Platform; private connectivity via AWS PrivateLink, Google Cloud Private Service Connect, Azure Private Link | Verified fact | A7-S054 |
| Dependencies | Python environment for the Library; data sources such as GCS, S3, Snowflake in customer environment | Verified fact | A7-S003, A7-S054 |
| Certifications | Claims to meet SOC 2, GDPR and CCPA requirements (platform page; SOC 2 type not stated); no ISO 27001/42001 certificate found | Verified fact | A7-S121 |
| GDPR / residency | Not publicly verified | Not publicly verified |  |
| Security features | Data isolation, encryption in transit and at rest, private link; states PII and customer data are not stored in documentation | Verified fact | A7-S055, A7-S054 |
| Access controls | Role-based access control; audit logs; continuous monitoring and logging | Verified fact | A7-S055 |
| Enterprise support | Not publicly verified | Not publicly verified |  |
| Pricing | Free account registration to start; commercial pricing not published | Verified fact | A7-S003 |
| Infrastructure cost | Not publicly verified | Not publicly verified |  |
| Ecosystem | Library extras for LLMs, PyTorch and Hugging Face Transformers | Verified fact | A7-S003 |
| Adoption signals | validmind package first published on PyPI 11 May 2023; vendor states Chartis ranked it No. 1 AI Governance Platform in RiskTech100 2026 | Verified fact | A7-S003, A7-S121 |
| Maturity | Frequent Library releases (2.13.x in September 2026) | Verified fact | A7-S003 |
| Deployment | saas: Yes (multi-tenant cloud); managed_cloud: Not publicly verified; vpc_byoc: Yes (Virtual Private ValidMind, single-tenant, on AWS, GCP or Azure); private_cloud: Not publicly verified; self_hosted: Not publicly verified; on_prem: Not publicly verified | | |
