# Draft master document, layers 9–7 (Checkpoint 2)

> Draft for calibration, 8 October 2026. Claim tags: [VF: id] verified fact · [R: id] reported · [AJ] architectural judgement · [Rec] recommendation · [NPV] not publicly verified. Source IDs resolve in `Enterprise_GenAI_Stack_Oct2026/06_References/bibliography.xlsx`. Disclosure: the author is an Anthropic model; Anthropic products and standards are scored on the same rubric as everything else.

## 9. Evaluation and observability (cross-cutting)

> **Executive summary.** This layer answers two questions for every GenAI system: is the output good enough to use, and what actually happened when it ran? Three things have changed since the original graphic. First, ownership has consolidated. Dynatrace completed its acquisition of Arize (Phoenix and AX) on 1 October 2026 [VF: A1-S045, V1-S005]. ClickHouse announced it had acquired Langfuse on 16 January 2026 [VF: A1-S021, V2-S041]. OpenAI announced its acquisition of Promptfoo on 9 March 2026, with no closing date published [VF: A1-S024, V1-S006]. W&B Weave has been part of CoreWeave since 5 May 2025 [VF: A1-S131]. Second, OpenTelemetry has become the common ingest format [AJ], although the GenAI semantic conventions are still at "Development" status [VF: A1-S058]. Third, the products now reach across the stack into gateways, prompt management, guardrails and automated fix proposals [VF: A1-S043, A1-S039, A1-S067]. This layer is not a box at the end of the pipeline [AJ]. **Recommendation:** instrument once with OpenTelemetry GenAI conventions or OpenInference, and own the evaluation harness and the evidence store. Then pick one platform of record for traces and evals (self-hosted Langfuse, or MLflow where an ML platform already exists, or LangSmith for LangGraph estates). Run two CI eval and red-team tools, one of them independent of any model vendor [Rec].

### 9.1 Responsibility

**The problem this layer owns.** It produces measured, retained evidence that a GenAI system behaves as intended, before release and while in service [AJ]. This breaks down into three jobs:

- **Evaluation.** Offline and CI suites, online scoring, human review, LLM-as-a-judge and red-teaming, covering faithfulness and groundedness, hallucination, relevance, recall@k and precision@k, tool-call accuracy, trajectory and safety [AJ].
- **Observability.** Each request needs one trace covering prompt, model and version, retrieved context, tool calls, latency, tokens, cost and errors [AJ].
- **Production feedback.** User and reviewer signals, drift and regression detection, and model comparison all flow back into the datasets that gate the next release [AJ].

**Hand-offs.** The layer receives spans from every other layer: gateway (C1), models (L1, L2), orchestration (L3), tools (L4), retrieval (L5 to L7) and ingestion (L8). It passes evaluation results, approvals and monitoring evidence to C8, cost per task to C6, and red-team findings to C2 and C7. It consumes prompt and configuration versions from C5, because each result must reference the exact version it tested [AJ].

**What the layer does not own.** It does not own the run-time blocking of unsafe outputs; that belongs to C2 guardrails. The two share detectors and datasets [AJ].

### 9.2 Why it matters

When this layer is badly designed, failures surface late and cannot be explained [AJ]. A model or prompt changes and quality regresses silently; no trace links an output to the context and tool results that produced it; an uncalibrated LLM judge scores everything "faithful"; spend has no per-task attribution [AJ]. Traces also contain prompts, retrieved documents and outputs, so in an asset manager they contain client and portfolio data. An unmanaged SaaS trace store is a residency and confidentiality exposure in its own right [AJ].

**Illustrative scenario [AJ].** A fund-reporting team switches the drafting model to a newer minor version through the gateway. Their only evaluation is a weekly sample read by an analyst. The new model rounds selection effects differently and sometimes swaps "overweight" and "underweight" when describing a currency effect. Each draft still reads fluently. Three monthly cycles pass before a portfolio manager notices a mismatch against the attribution report. By then, nobody can say which commentaries were affected: traces were kept for 15 days on a free tier, and the prompt version was not recorded. Every commentary must be re-checked by hand. A numeric-faithfulness check, plus retention aligned to the records policy, would have caught the change on day one. The scenario is invented; it is not a reported incident.

### 9.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Numeric faithfulness | Share of figures matching the authoritative source value under an agreed rounding rule | 100% at release; any miss blocks | Deterministic comparator against tool output in the trace |
| Groundedness / faithfulness | Share of claims supported by retrieved or approved context | Per use case (e.g. ≥0.95 for regulated text) | Calibrated LLM judge or NLI metric |
| Retrieval recall@k / precision@k | Relevant documents found in top k / relevant share of top k | Per corpus; watch the trend | Labelled query set in CI |
| Tool-call accuracy | Correct tool, arguments and order | ≥0.98 for read-only data tools | Assertions against expected calls |
| Trajectory adherence | Runs following the approved graph with no unexpected steps | Any unapproved call is a defect | Plan-adherence metrics over traces |
| Red-team pass rate | Attack cases (OWASP LLM and Agentic 2026) handled safely | No critical failures at release | Two red-team tools in CI |
| Judge–human agreement | LLM judge versus expert labels | e.g. Cohen's kappa ≥0.7 before gating | Periodic double-labelling |
| Trace completeness | Requests with full trace (prompt, model, context IDs, tool I/O, evals) | ≥99.9% in scope | Gateway logs reconciled to trace store |
| p95 latency, cost per task | Latency and loaded token cost per completed task | Budget per use case | Trace and gateway data |
| Human-intervention rate | Outputs edited or rejected, and edit size | Falling trend; spikes reviewed | Reviewer feedback as trace scores |
| Time to detect regression or drift | Change in model, prompt or data to failing eval | Same day for gated systems | CI on every change; online sampling alerts |

The IOSCO supervisory toolkit names indicators for asset managers that include the accuracy of AI-supported valuations against benchmarks and the level and frequency of human intervention in AI-driven investment processes [VF: R-INTL-AI-ASSETMGMT, A8-S058]. The last two KPIs above are designed to produce that evidence [AJ].

### 9.4 How it works

The mechanics have three loops that share one trace and dataset store.

1. **Instrumentation.** Each layer emits spans (model call, retrieval, tool execution, agent step) using the OpenTelemetry GenAI semantic conventions, still at "Development" status as of 7 October 2026 [VF: A1-S058]. Since semconv v1.42.0 these definitions live in a dedicated repository, `semantic-conventions-genai` [VF: A1-S060], covering client inference, agents, tool execution, retrieval, evaluation and MCP [VF: A1-S061]. It defines a `gen_ai.evaluation.result` event with name, score, label and explanation [VF: A1-S059], so a score can travel on the same pipe as the trace it judges [AJ]. OpenInference (Apache-2.0) is the alternative used by Phoenix and AX [VF: A1-S049, A1-S066].
2. **Offline and CI evaluation.** Versioned datasets (golden cases, past failures, red-team cases) run against every change to model, prompt, retrieval configuration or tool, and results gate the merge. Six of the original products document a CI path: pytest plugins for LangSmith [VF: A1-S108], Phoenix [VF: A1-S106] and Opik [VF: A1-S067]; DeepEval's Pytest-like framework [VF: A1-S068]; Promptfoo with GitHub Actions, GitLab and Jenkins [VF: A1-S065]; and Braintrust's GitHub Action posting PR comments [VF: A1-S109].
3. **Online evaluation and feedback.** Evaluators score a sample of production traces, and reviewer edits and user ratings attach to traces as scores: Opik online evaluation rules [VF: A1-S072], Langfuse evaluators [VF: A1-S073], Datadog evaluations [VF: A1-S099]. Clustering groups recurring failures: LangSmith Engine [VF: A1-S039], Braintrust Topics [VF: A1-S043], AX Signal [VF: A1-S046]. Failing cases are promoted into the CI dataset, which closes the loop [AJ].

```text
   L1/L2 model ─┐  L3 agent ─┐  L4 tools ─┐  L5-L7 retrieval ─┐  C1 gateway ─┐
                ▼            ▼            ▼                   ▼              ▼
          OTel GenAI / OpenInference spans  ──►  OTel Collector (firm-owned)
                                                   │  redact (C3) · route · sample
                         ┌─────────────────────────┼──────────────────────────┐
                         ▼                         ▼                          ▼
              Platform of record           APM (ops alerting)        Evidence archive
            (traces, datasets, evals,       latency, errors,         (WORM / records
             prompts, annotations)          cost dashboards           policy, C8)
                    ▲      │
   reviewer edits,  │      ▼ online evaluators (sampled)
   user feedback ───┘   failures ──► CI datasets ──► offline evals + red-team ──► release gate
```

The **firm-owned collector** is the key design choice. It applies redaction before data leaves the estate, fans out to more than one backend, and makes the platform of record replaceable [AJ].

### 9.5 Enterprise design principles

**Security**

- Treat the trace store as a production data store holding client data. Encrypt it, apply access control, and redact at the collector [AJ].
- Datadog scans and redacts sensitive data in traces [VF: A1-S097]. Langfuse gates server-side ingestion masking behind its Enterprise licence [VF: A1-S033].
- Phoenix ships with authentication off by default [VF: A1-S105]. Turn it on before any real data arrives [Rec].
- Disable vendor telemetry in self-hosted tools. Langfuse's is on by default [VF: A1-S033]; Phoenix's can be disabled [VF: A1-S066] [Rec].

**Scalability, resilience and cost**

- Keep full traces for regulated outputs and sample the online evaluations; the judge model is the main evaluation cost driver [AJ].
- Instrumentation must never block the request path, and the release gate must work when a SaaS platform is down, so export asynchronously and run CI evals from the firm's repository [AJ].
- Pricing units differ: units (Langfuse) [VF: A1-S031], spans and GB (AX) [VF: A1-S047], LLM spans (Datadog) [VF: A1-S097], seats plus traces (LangSmith) [VF: A1-S035], processed GB and scores (Braintrust) [VF: A1-S040]. Model cost at production volume before committing [Rec].

**Governance and portability**

- Version everything a score depends on (dataset, metric code, judge model and prompt, application prompt, model version) and store it with the result [AJ]. Calibrate LLM judges against human labels before they gate anything [Rec].
- Reconcile gateway request counts against trace counts, so missing traces are detected [AJ].
- Instrument once with OTel GenAI or OpenInference, keep vendor SDKs at the edge, and keep datasets and metric code in Git [Rec].

**Patterns [AJ]:** Collector fan-out to a platform of record plus APM; eval-as-code in CI; judge model routed through the gateway; reviewer edits captured as labelled data; two red-team tools, one independent of any model vendor.

**Anti-patterns [AJ]:** vendor SDK hard-wired into application code; a model vendor's tool as the only independent test of that vendor's model; uncalibrated judges; retention set by the free tier rather than the records policy; online evaluation sending client data to an unassessed third-party judge.

### 9.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Coverage of the plan's questions (faithfulness, recall@k/precision@k, tool-call accuracy, trajectory, red-teaming, online evaluation, CI regression, drift); dataset and experiment management; deterministic code scorers alongside LLM judges |
| Enterprise readiness (15%) | SSO, project RBAC, audit logs of who viewed or changed traces and scores, SCIM, SLA, multi-team tenancy; which of these are licence-gated when self-hosted |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 as baseline; because traces carry client data, 5 is reserved for products that add customer-managed keys, ISO 42001 or similar; redaction at ingest |
| Deployment flexibility (15%) | Self-host or BYOC for trace residency; air-gap for validation sandboxes; region pinning |
| Ecosystem (5%) | OTLP ingest with GenAI conventions or OpenInference; CI integrations; framework coverage |
| Reliability and maturity (10%) | Release cadence; ownership stability (five of eleven products changed or announced a change of owner in 2025–26); pre-1.0 versioning |
| Cost / TCO (5%) | Pricing unit, judge-token spend, self-host operations (ClickHouse, Kubernetes, PostgreSQL) |
| Lock-in / portability (15%) | Licence (MIT/Apache vs ELv2 vs proprietary); export; whether eval logic lives in your repo; vendor neutrality of red-team tooling |

### 9.7 Product deep dives

**Langfuse (ClickHouse).**
- *What it is now:* an open-core LLM engineering platform covering tracing, prompt versioning, LLM-as-a-judge and code evaluators, user feedback, manual labelling, datasets and experiments [VF: A1-S073]. The core is MIT. Code under `ee/` needs a commercial licence key when self-hosted: SCIM, audit logging, data-retention policies, project-level RBAC and server-side ingestion masking [VF: A1-S023, A1-S033]. ClickHouse announced the acquisition on 16 January 2026 alongside its US$400M Series D [VF: A1-S021, V2-S041].
- *Instrumentation and hosting:* there is a native OTLP/HTTP endpoint (no gRPC). `gen_ai.*` attributes are mapped, but Langfuse-specific attributes take precedence [VF: A1-S032]. Langfuse Cloud holds SOC 2 Type II and ISO 27001, with isolated EU (Ireland), US, HIPAA and Japan regions [VF: A1-S029, A1-S030]. Python SDK 4.17.0 was released on 5 October 2026 [VF: A1-S001].
- *Strengths:* the most complete permissively licensed platform of record that can be self-hosted [AJ].
- *Limitations:* the evidence controls (audit logs, project RBAC) are the paid part. Storage and the self-hosted Enterprise tier are tied to ClickHouse [VF: A1-S033].
- *Choose when:* you need in-estate traces with a supported enterprise licence [AJ].
- *Avoid when:* you will not pay for the audit and RBAC modules [AJ].
- *Competitors:* LangSmith, Opik, MLflow.
- *FS note:* self-host in the UK or EU, or use the EU Cloud region. Budget for Enterprise [Rec].
- **Tier: Strategic. Flag: Acquired.**

**LangSmith (LangChain).**
- *What it is now:* trace capture, offline and online evaluation, prompt management and hosted agent deployment. It ingests native and OTLP traces [VF: A1-S034, A1-S037]. Interrupt 2026 added LangSmith Engine (public beta, which clusters production failures and can open PRs), Sandboxes GA and an LLM Gateway with audit logging. Agent Builder was renamed LangSmith Fleet [VF: A1-S039].
- *Certifications and deployment:* SOC 2 Type II, ISO 27001:2022 and HIPAA, with a BAA on Enterprise. US or EU regions are available on all tiers [VF: A1-S036, A1-S126]. BYOC on AWS, self-hosting and air-gapped self-hosting are Enterprise options [VF: A1-S034].
- *Strengths:* the tightest fit with LangGraph, and a broad commercial feature set [AJ].
- *Limitations:* LangChain recommends the native format over OTel for performance [VF: A1-S037]. The platform now bundles the agent runtime [VF: A1-S039]. Self-hosting needs at least 16 vCPU and 64 GB, plus PostgreSQL, Redis and ClickHouse [VF: A1-S034]. Pricing is per seat plus overage [VF: A1-S035].
- *Choose when:* LangGraph is the standard [AJ].
- *Avoid when:* your estate is framework-heterogeneous, or you want the observability vendor separated from the runtime vendor [AJ].
- *Competitors:* Langfuse, Braintrust, Arize AX.
- *FS note:* dual-instrument with OTel so that evidence survives an exit, and keep Engine's proposed fixes under change control [Rec].
- **Tier: Strategic, conditional: only in a LangGraph estate and only with OTel dual-instrumentation as the exit route, because lock-in scores 2 [AJ]. No flag.**

**Braintrust.**
- *What it is now:* an independent, proprietary platform built around experiments, datasets and scorers, with production logging. Its Trace conference in February 2026 introduced Topics (trace clustering) and Loop (AI-assisted optimisation), and Braintrust Gateway routes and traces model calls [VF: A1-S043]. It raised a US$80M Series B on 17 February 2026 [VF: A1-S028].
- *Deployment:* the hybrid model keeps a Braintrust-hosted control plane and puts the data plane in the customer's AWS, GCP or Azure. Customer-managed KMS keys are supported [VF: A1-S041]. The US or EU data plane is fixed when the organisation is created [VF: A1-S042].
- *Certifications:* SOC 2 Type II, with a HIPAA BAA on Enterprise. No ISO 27001 certification was found [VF: A1-S125].
- *Access control:* SSO/SAML and OIDC, built-in groups with Enterprise custom and object-level permissions, and Enterprise audit logs queryable by SQL [VF: B-REV-S020, B-REV-S021].
- *Strengths:* evaluation ergonomics and PR-level feedback [VF: A1-S109] [AJ].
- *Limitations:* evaluation logic and datasets sit in the proprietary platform [VF: A1-S042].
- *Choose when:* eval-driven development matters most and the hybrid model is acceptable [AJ].
- *Avoid when:* ISO 27001 is a gate [AJ].
- *Competitors:* LangSmith, Langfuse, AX.
- *FS note:* assess the control-plane metadata under SYSC 8 and DORA, not only the data plane [AJ].
- **Tier: Tactical. No flag.**

**Arize Phoenix (Dynatrace).**
- *What it is now:* self-hosted tracing on OTel and OpenInference, with response and retrieval evaluations, datasets, experiments, prompt management, an MCP endpoint and a pytest plugin [VF: A1-S066, A1-S106]. Version 20.19.0 was released on 1 October 2026 [VF: A1-S004].
- *Licence:* Elastic License 2.0. It is source-available, not OSI-approved, and may not be offered to third parties as a managed service [VF: A1-S048, A1-S107]. Phoenix has no feature gates [VF: A1-S046].
- *Access control and support:* authentication is optional and off by default. When enabled, the roles are admin, member and viewer [VF: A1-S105]. Full SSO, RBAC and audit trails are AX features, and Phoenix has community support only [VF: A1-S046].
- *Strengths:* OpenInference portability and free air-gapped use [VF: A1-S046, A1-S049].
- *Limitations:* not a governed multi-team store [AJ]. Arize says it will keep supporting Phoenix, with capabilities integrated into Dynatrace over time [VF: A1-S045].
- *Choose when:* you need validation sandboxes or developer workbenches [AJ].
- *Avoid when:* you need the production record, or your licence policy admits OSI licences only [AJ].
- *Competitors:* Langfuse, Opik, MLflow.
- *FS note:* enable authentication and disable telemetry; it is not an audit store [Rec].
- **Tier: Tactical. Flag: Acquired.**

**Arize AX (Dynatrace).**
- *What it is now:* a commercial platform for managed tracing, online and offline evaluation, monitoring and alerting, with managed evaluation compute. Multi-tenancy works through organisations and spaces. Signal groups recurring failure patterns [VF: A1-S046]. It runs on the proprietary adb database [VF: A1-S046].
- *Deployment:* SaaS, VPC, customer-managed cloud, self-hosted (Arize stores nothing) and air-gapped [VF: A1-S046, A1-S047, A1-S124].
- *Certifications:* SOC 2 Type II, PCI DSS 4.0 and HIPAA, with an EU region in Belgium. ISO 27001 is claimed on marketing pages but is absent from the official compliance page, so request the certificate [VF: A1-S124, V1-S084].
- *Ownership:* Dynatrace agreed the deal on 13 August 2026 (US$915M) and completed it on 1 October 2026, with plans to converge the product into its platform [VF: A1-S044, A1-S045, V1-S005].
- *Strengths:* the most complete deployment range among the commercial platforms [AJ]. A documented Phoenix-to-AX dual-write migration [VF: A1-S046].
- *Limitations:* the roadmap is uncertain for the next few quarters [AJ].
- *Choose when:* you run Dynatrace, or need managed online evaluation at volume with self-hosting [AJ].
- *Avoid when:* you need roadmap certainty now [AJ].
- *Competitors:* LangSmith, Datadog, Braintrust.
- *FS note:* refresh third-party due diligence after the change of control [Rec].
- **Tier: Tactical. Flags: Acquired, Duplicated** (the graphic shows Arize twice).

**DeepEval (Confident AI).**
- *What it is now:* an Apache-2.0 Python framework, "similar to Pytest but specialised for unit testing LLM apps" [VF: A1-S068, A1-S051]. Version 4.2.8 was released on 2 October 2026 [VF: A1-S005].
- *Metrics:* G-Eval, DAG, faithfulness and contextual recall and precision. It also has agentic metrics (task completion, tool correctness, plan adherence) and trajectory evaluation [VF: A1-S068].
- *Where it runs:* in any CI/CD, with any LLM or local NLP model as judge [VF: A1-S068].
- *Commercial platform:* Confident AI is the paid platform. It is available as SaaS (US, EU Frankfurt and AU regions) or in a VPC [VF: A1-S119]. Its SOC 2 and HIPAA claims are vendor statements with inconsistent plan gating [VF: A1-S119].
- *Strengths:* the closest match to this layer's research questions in one library [AJ].
- *Limitations:* OTel export goes mainly to Confident AI [VF: A1-S121]. Maintainer funding is not publicly verified [NPV].
- *Choose when:* you want code-first metrics that you own in CI [AJ].
- *Avoid when:* you are looking for production observability [AJ].
- *Competitors:* Promptfoo, MLflow, Opik.
- *FS note:* pin the library and judge versions so that results reproduce [Rec].
- **Tier: Tactical. No flag.** It is a substitutable component of an in-house harness, not a platform [AJ].

**Promptfoo (OpenAI, announced).**
- *What it is now:* an MIT CLI and library for evaluations, red-teaming and vulnerability scanning, model comparison, CI checks and PR code scanning [VF: A1-S062]. Version 0.124.0 was published on 6 October 2026 [VF: A1-S020]. Evals run locally. Enterprise comes as SaaS or On-Prem with a dedicated runner [VF: A1-S062, A1-S063]. It has an OTLP receiver that uses the GenAI conventions [VF: A1-S064].
- *Ownership:* OpenAI announced the acquisition on 9 March 2026. The closing date has not been published; Promptfoo states it is part of OpenAI [VF: A1-S024, A1-S062, V2-S042]. OpenAI plans to integrate it into OpenAI Frontier for red-teaming and risk and compliance monitoring [VF: A1-S024].
- *Strengths:* regression and red-team suites as portable config, mapped to OWASP and NIST [VF: A1-S063, A1-S065].
- *Limitations:* the tool is pre-1.0 [VF: A1-S020]. Enterprise certifications are not publicly verified [NPV].
- *Conflict of interest:* a model vendor now steers a tool that firms use to test that vendor's models and its competitors' [AJ]. Under SS1/23's independent-validation principle, that weakens the claim that the test is independent [AJ].
- *Choose when:* you want CI red-teaming run locally [AJ].
- *Avoid when:* it would be the sole independent challenge of an OpenAI-based system [AJ].
- *Independent alternative:* Confident AI's native red-teaming (DeepEval's maintainer) [VF: A1-S068].
- **Tier: Tactical. Flag: Acquired.**

**Opik (Comet).**
- *What it is now:* the whole platform is Apache-2.0, covering tracing, datasets and experiments, LLM-as-a-judge metrics, online evaluation rules, guardrails and an agent optimiser [VF: A1-S050, A1-S067, A1-S072]. Python SDK 2.2.94 was released on 7 October 2026 [VF: A1-S006].
- *Certifications:* the Comet Trust Center lists SOC 2 Type 2, ISO/IEC 27001:2022 and ISO 9001 [VF: A1-S122].
- *Pricing:* self-hosting is free. Pro Cloud costs US$19 per month as of 7 October 2026 [VF: A1-S123].
- *Strengths:* the most permissive full-platform licence in this layer [AJ].
- *Limitations:* the self-hosted open-source edition has no user management; SSO and custom roles come with Enterprise [VF: A1-S069, A1-S122, B-REV-S022]. Audit logs appear only on marketing pages [NPV]. The local Docker install is not production-ready [VF: A1-S069]. OTel is HTTP-only [VF: A1-S070]. An EU region is not publicly verified [NPV].
- *Choose when:* you want Apache-2.0 end to end and will buy Enterprise for identity, or you already run Comet [AJ].
- *Avoid when:* you would self-host the open edition for many teams [AJ].
- *Competitors:* Langfuse, Phoenix, MLflow.
- *FS note:* self-host only with Enterprise identity or a fronting identity proxy [Rec].
- **Tier: Tactical. No flag.** It scores 3.75 FS. It falls short of Strategic for two reasons: the open edition lacks identity, and the codebase is only about two years old [AJ].

**MLflow (GenAI capabilities).**
- *What it is now:* an Apache-2.0 platform with OTel-based tracing, evaluation and monitoring, a prompt registry and optimisation, and an AI Gateway [VF: A1-S103, A1-S019]. Version 3.17.0 was released on 7 October 2026 [VF: A1-S019].
- *Hosting:* managed by Databricks, SageMaker, Azure ML, Nebius and OpenShift AI, or self-hosted on-premises [VF: A1-S103]. Databricks contributed it to the Linux Foundation in 2020 under a vendor-neutral governance model [VF: B-L9-S004]. The code copyright remains with Databricks [VF: A1-S019].
- *Strengths:* GenAI evidence lands next to the classic model inventory and lifecycle that many regulated firms already run [AJ].
- *Limitations:* access controls and certifications depend on the managed host and are not verified in the fact base [NPV]. Evaluation depth compared with specialist tools has not been assessed from primary sources [NPV].
- *Choose when:* an ML platform already exists [AJ].
- *Avoid when:* you would self-host an unauthenticated tracking server [AJ].
- *Competitors:* Langfuse, Weave, Opik.
- *FS note:* verify the managed host's certifications and region per provider [Rec].
- **Tier: Strategic. No flag.**

**Datadog Agent Observability.**
- *What it is now:* a Datadog module, documented under the LLM Observability path. It traces agent steps and LLM calls with latency, tokens, cost and errors, and scans and redacts sensitive data. It also detects prompt injection, runs quality, privacy and safety evaluations, and produces Insights [VF: A1-S097, A1-S099].
- *Ingest:* it accepts OTel 1.37+ GenAI conventions or OpenInference [VF: A1-S098]. Pricing is metered per LLM span [VF: A1-S097].
- *Certifications:* the Datadog Trust Center lists SOC 2 Type 2, ISO/IEC 27001, 27017, 27018, 27701 and 42001, HIPAA and FedRAMP High [VF: B-L9-S001]. Whether that scope covers this module specifically is not stated [NPV], so security scores 4, not 5 [AJ].
- *Regions and access:* EU1 is hosted in Germany, and sites are isolated from each other [VF: B-L9-S002]. SAML SSO, RBAC with custom roles and an Audit Trail are documented [VF: B-L9-S003, B-L9-S005].
- *Strengths:* puts production LLM monitoring with on-call operations [AJ].
- *Limitations:* SaaS only. Self-hosting is not publicly verified [NPV].
- *Choose when:* Datadog is your APM standard [AJ].
- *Avoid when:* it would be the sole evaluation tool [AJ].
- *Competitors:* AX, LangSmith, Langfuse.
- *FS note:* choose the EU1 site at creation and switch on sensitive-data scanning first [Rec].
- **Tier: Tactical. Flag: Renamed** (rename date not verified).

**W&B Weave (CoreWeave).**
- *What it is now:* tracing and evaluation for agents, with autopatching of the OpenAI Agents SDK, Claude Agent SDK and Google ADK [VF: A1-S104]. It has an OTLP/HTTP endpoint and a separate endpoint for agent spans [VF: A1-S139]. Version 0.53.11 was released on 25 September 2026 [VF: A1-S018].
- *Certifications:* SOC 2 Type II and ISO/IEC 27001, 27017 and 27018. HIPAA is available on Dedicated Cloud with a BAA [VF: A1-S137].
- *Deployment and access:* Dedicated Cloud in the customer's chosen cloud and region, with per-instance keys and private connectivity. Customer-managed keys, SSO, automated provisioning, custom roles and audit logs come with Enterprise [VF: A1-S137, A1-S138].
- *Ownership:* part of CoreWeave since 5 May 2025, inside CoreWeave Forge [VF: A1-S131, A1-S138].
- *Strengths:* a strong security posture inside an existing W&B estate [AJ].
- *Limitations:* the multi-tenant cloud is North America only [VF: A1-S137]. RAG and red-team evaluation depth is not evidenced [NPV].
- *Choose when:* W&B is already the ML platform [AJ].
- *Avoid when:* you would use the multi-tenant cloud for UK or EU client data [AJ].
- *Competitors:* MLflow, LangSmith, AX.
- *FS note:* include CoreWeave in concentration analysis if it also supplies compute [Rec].
- **Tier: Tactical. Flag: Acquired.**

### 9.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9-langfuse | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3.80 | 3.70 | Strategic |
| L9-langsmith | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 2 | 3.95 | 3.80 | Strategic |
| L9-braintrust | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.40 | 3.20 | Tactical |
| L9-arize-phoenix | 4 | 2 | 3 | 4 | 4 | 4 | 4 | 3 | 3.50 | 3.35 | Tactical |
| L9-arize-ax | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 2 | 3.85 | 3.70 | Tactical |
| L9-deepeval | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 4 | 3.75 | 3.70 | Tactical |
| L9-promptfoo | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 3 | 3.70 | 3.55 | Tactical |
| L9-opik | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 3.75 | 3.75 | Tactical |
| L9-mlflow-genai | 4 | 3 | 3 | 5 | 5 | 5 | 4 | 5 | 4.10 | 4.10 | Strategic |
| L9-datadog-agent-observability | 3 | 4 | 4 | 2 | 4 | 3 | 2 | 3 | 3.15 | 3.20 | Tactical |
| L9-wandb-weave | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 2 | 3.55 | 3.55 | Tactical |

**Scoring notes [AJ]:**
- No NPV cap was triggered. Datadog's certification and access-control gaps were closed by the writer (B-L9-S001 to S005), and the CP2 review evidenced Braintrust's SSO, RBAC and audit logs and Opik's SSO and roles [VF: B-REV-S020, B-REV-S021, B-REV-S022].
- Datadog security is 4, not 5: the certifications are company-level and the module's scope is not stated. The same one-point scope rule applies to Gemini Embedding and Cohere (L7) and Mistral OCR (L8).
- DeepEval, Phoenix, MLflow and the Promptfoo CLI were scored as self-hosted software under rubric rule 2. Promptfoo Enterprise SaaS would be capped at 2 for security, because its certifications are NPV.
- Arize AX, DeepEval and Opik reach 3.6 or above but are classed Tactical. AX was acquired seven days ago. DeepEval is a substitutable library. Opik's open edition lacks identity. LangSmith is Strategic with lock-in at 2 only on the condition stated in its deep dive.
- The ownership-change reduction of 1 on lock-in was applied to Langfuse, Phoenix, AX, Promptfoo and Weave.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| Langfuse | MIT core; `ee/` modules commercial [VF: A1-S023, A1-S033] | SaaS, self-host, on-prem [VF: A1-S073, A1-S033] | SOC 2 Type II, ISO 27001 (Cloud) [VF: A1-S029] | EU region (Ireland) [VF: A1-S030] | ClickHouse, announced 16 Jan 2026 [VF: A1-S021, V2-S041] |
| LangSmith | Proprietary; SDK MIT [VF: A1-S002] | SaaS, BYOC (AWS), self-host, air-gap [VF: A1-S034] | SOC 2 Type II, ISO 27001:2022, HIPAA [VF: A1-S036, A1-S126] | EU region [VF: A1-S036] | LangChain, independent [VF: A1-S038] |
| Braintrust | Proprietary; SDK MIT [VF: A1-S003] | SaaS, hybrid data plane, self-host [VF: A1-S041] | SOC 2 Type II; no ISO 27001 found [VF: A1-S125] | EU data plane [VF: A1-S042] | Independent [VF: A1-S028] |
| Arize Phoenix | ELv2 (source-available) [VF: A1-S048] | Self-host, private cloud, air-gap [VF: A1-S066, A1-S046] | Not publicly verified [NPV] | In-estate [VF: A1-S066] | Dynatrace, completed 1 Oct 2026 [VF: A1-S045] |
| Arize AX | Proprietary [VF: A1-S046] | SaaS, VPC, self-host, air-gap [VF: A1-S046, A1-S047] | SOC 2 Type II, PCI DSS 4.0, HIPAA; ISO 27001 unconfirmed [VF: A1-S124, V1-S084] | EU region (Belgium) [VF: A1-S124] | Dynatrace, completed 1 Oct 2026 [VF: A1-S045] |
| DeepEval | Apache-2.0 [VF: A1-S051] | Library; Confident AI SaaS/VPC [VF: A1-S068, A1-S119] | Confident AI vendor-stated SOC 2 [VF: A1-S119] | Confident AI Frankfurt [VF: A1-S119] | Confident AI [VF: A1-S068] |
| Promptfoo | MIT; Enterprise commercial [VF: A1-S052, A1-S063] | Local CLI, SaaS, On-Prem [VF: A1-S063] | Not publicly verified [NPV] | Local or on-prem [VF: A1-S063] | OpenAI, announced 9 Mar 2026; closing not published [VF: A1-S024, V2-S042] |
| Opik | Apache-2.0 (full platform) [VF: A1-S050] | SaaS, self-host, on-prem [VF: A1-S069, A1-S071] | SOC 2 Type 2, ISO 27001:2022 (Comet) [VF: A1-S122] | Not publicly verified [NPV] | Comet, independent [VF: A1-S071] |
| MLflow | Apache-2.0 [VF: A1-S019] | Five managed services, self-host, on-prem [VF: A1-S103] | Depends on managed host [NPV] | Depends on host [NPV] | Linux Foundation project [VF: B-L9-S004] |
| Datadog | Proprietary SaaS [VF: A1-S097] | SaaS (regional sites) [VF: B-L9-S002] | SOC 2 Type 2, ISO 27001, ISO 42001, FedRAMP High (company) [VF: B-L9-S001] | EU1 Germany [VF: B-L9-S002] | Datadog, Inc. [VF: A1-S097] |
| W&B Weave | SDK Apache-2.0; platform proprietary [VF: A1-S018, A1-S138] | SaaS (NA), Dedicated, Self-Managed [VF: A1-S137] | SOC 2 Type II, ISO 27001/27017/27018 [VF: A1-S137] | Dedicated Cloud region choice [VF: A1-S137] | CoreWeave, completed 5 May 2025 [VF: A1-S131] |

### 9.9 Decision tree

The tree is applied in four steps. Steps 0 and 4 are not product choices; step 4 is a set of checks to run after selection [Rec].

```text
STEP 0 [Rec] (not optional): instrument with OTel GenAI conventions (or OpenInference) via a
firm-owned OTel Collector with redaction; keep datasets and metric code in Git.

STEP 1 [Rec]: Platform of record for traces, datasets, evals, prompts
  Do traces contain client/personal data that must stay in-estate or in UK/EU?
  ├─ Yes → Can you run Kubernetes + ClickHouse/PostgreSQL yourselves?
  │        ├─ Yes → Is an ML platform (Databricks / SageMaker / Azure ML) already the
  │        │        model-inventory system?
  │        │        ├─ Yes → MLflow (managed, in-region)
  │        │        └─ No  → Langfuse self-hosted + Enterprise licence
  │        │                 (alt: Opik + Comet Enterprise; LangSmith self-host if LangGraph)
  │        └─ No  → Managed with EU region or customer data plane:
  │                 LangGraph estate? → LangSmith EU / BYOC
  │                 otherwise         → Langfuse Cloud EU, Braintrust hybrid (EU),
  │                                     W&B Dedicated Cloud (EU region)
  └─ No  → Pick on team fit: LangSmith (LangGraph), Braintrust (eval-led), Langfuse

STEP 2 [Rec]: Production monitoring with ops
  Is Datadog or Dynatrace the APM standard?
  ├─ Datadog   → Datadog Agent Observability, fed by the same Collector (EU1 site)
  ├─ Dynatrace → Arize AX (re-assess after Dynatrace publishes its roadmap)
  └─ Neither   → platform of record's online evals + alerting

STEP 3 [Rec]: CI evaluation and red-teaming
  Metrics library  → DeepEval (or the platform's own evaluators), judge model via gateway
  Red-team         → Promptfoo CLI locally
                     AND, if the system under test uses an OpenAI model,
                     a second, vendor-independent red-team tool (e.g. Confident AI)
  Validation sandbox for independent reviewers → Phoenix (auth on, telemetry off, air-gapped)

STEP 4 [Rec]: Checks before go-live
  Trace retention ≥ records policy (and ≥ 6 months where AI Act Art. 26 applies)?
  Judge calibrated against human labels?  Trace completeness reconciled with gateway?
```

### 9.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Instrumentation | **Unacceptable if proprietary; acceptable on OTel/OpenInference** | Re-instrumenting every layer is the largest switching cost; every product here ingests or emits OTel or OpenInference [VF: A1-S032, A1-S037, A1-S042, A1-S049, A1-S064, A1-S070, A1-S098, A1-S103, A1-S121, A1-S139] | Firm-owned Collector; pin the semconv version, since status is "Development" [VF: A1-S058] |
| Eval datasets and metric code | **Unacceptable if only in a vendor UI** | They are the regression baseline and the validation evidence | Git-versioned datasets and scorers; results as `gen_ai.evaluation.result` events [VF: A1-S059] |
| Platform of record | **Manageable** | Replaceable if instrumentation and datasets are portable; harder with proprietary stores (adb [VF: A1-S046]) or native formats [VF: A1-S037] | Collector fan-out; periodic export to the firm's archive |
| Production APM module | **Acceptable** | Already part of ops tooling | The same Collector |
| Red-team tooling | **Manageable, with an independence caveat** | Promptfoo configs are MIT and portable [VF: A1-S052]; model-vendor ownership is the issue [AJ] | Two tools, configs in Git |
| LLM judge model | **Manageable** | Judges drift when the model changes | Route via the gateway (C1); pin and re-calibrate |

### 9.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23.* PRA SS1/23 applies to banks, building societies and PRA-designated investment firms with internal-model approval [VF: R-PRA-SS123, A8-S008]. It covers vendor models and requires independent validation (Principle 4) and ongoing performance monitoring [VF: R-PRA-SS123, A8-S008, A8-S037].
- *Who it binds.* For FCA solo-regulated managers, SS1/23 is not binding but is the natural benchmark. This layer is where its validation and monitoring evidence is produced [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026. It expressly places generative and agentic AI outside its scope and says the firm's own risk-management practices should determine their governance [VF: R-US-MRM, A8-S001, A8-S002].
- *The consequence.* No regulator defines "adequate evaluation" for an LLM agent, so the firm must set its own standard (metrics, thresholds, judge calibration, re-validation triggers), written to SS1/23 quality so it survives the agencies' planned AI request for information [AJ].

**EU AI Act.**
- *Deployer duties.* Article 26 requires deployers of high-risk systems to monitor operation, keep logs for at least six months, and report serious incidents. Financial institutions fold logging into their existing financial-services documentation [VF: R-EUAIA, A8-S011]. Annex III duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011].
- *Scope for this use case.* Most asset-management uses, including attribution commentary, are not Annex III. The live duties are transparency and literacy [AJ].
- *Recommendation.* Build Article 26-grade logging and monitoring anyway, because the same artefacts serve MRM and outsourcing evidence [Rec].
- *Provider duties.* Article 72 post-market monitoring falls on providers. A firm that substantially modifies a high-risk system can become a provider under Article 25 [VF: R-EUAIA, A8-S011].

**DORA, the UK CTP regime and outsourcing.**
- *Designations.* The DORA CTPP list and the UK CTP designations cover hyperscalers and no AI model provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023].
- *Observability SaaS is a third-party service.* A SaaS trace store holding client data belongs in the register of information, with Article 30 terms and an exit plan if it supports a critical or important function [AJ].
- *Notification lead time.* PRA PS7/26 and FCA PS26/2 require material third-party notifications from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. Contract changes forced by the Arize, Langfuse and Promptfoo ownership changes should be planned with that lead time [Rec].
- *Exit routes.* SS2/21 expects documented, tested exit plans [VF: R-PRA-SS221, A8-S048]. Evaluation suites are what let a firm re-qualify an alternative model or platform quickly [AJ].

**Residency and auditability.**
- *FCA expectations.* FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. Traces held by a vendor fall within that [AJ].
- *Transfers.* EU-to-US transfers rely on the Data Privacy Framework or SCCs, and an annulment appeal (C-703/25 P) is pending [VF: R-DATA-TRANSFERS, A8-S053]. Prefer in-estate or EU/UK-region trace stores and redact at the Collector [Rec].
- *Evidence retention.* Retention must follow the records policy, not a vendor tier. The free tiers keep data for 15 days (AX) [VF: A1-S047], 30 days (Langfuse Hobby) [VF: A1-S031] and 60 days (Opik) [VF: A1-S123] [AJ].
- *Reproducibility.* Every result needs its dataset, metric code, judge version and application prompt version [AJ].

**Concentration and independence.**
- *Vendor ownership.* Five of the eleven products are now owned by, or announced as owned by, four larger platform vendors: an APM vendor, a database vendor, a model vendor and a GPU cloud [VF: A1-S045, A1-S021, A1-S024, A1-S131].
- *The model-vendor case.* OpenAI's ownership of Promptfoo is the most sensitive [AJ]. A test tool roadmapped into OpenAI Frontier [VF: A1-S024] is a weaker basis for the effective challenge that SS1/23-style validation expects when the model under test is OpenAI's [AJ].
- *Our own conflict.* The same logic applies to any vendor's tooling. This author is an Anthropic model, and the rule above would apply equally to an Anthropic-owned evaluation tool [AJ].
- *Concentration risk.* IOSCO also flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058].

**Standards.**
- *NIST.* NIST AI RMF 1.0 and the GenAI Profile (AI 600-1) give a neutral measurement taxonomy for the evaluation standard [VF: R-NIST-AIRMF, A8-S043, A8-S044].
- *ISO.* ISO/IEC 42001 provides the management-system wrapper [VF: R-ISO-42001, A8-S045].
- *OWASP.* Red-team suites should map to the OWASP Top 10 for LLM Applications 2026, released August–September 2026 [VF: R-OWASP-LLM, V2-S056], and to the Top 10 for Agentic Applications for 2026, which starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042].
- *ESMA.* ESMA expects "ex-ante input controls and frequent ex-post output controls" [VF: R-INTL-AI-ASSETMGMT, A8-S059]. Online evaluation of production traces is the ex-post control [AJ].

### 9.12 Worked-example slice (POV 3)

**What the commentary agent needs from L9 [AJ].** The agent drafts the monthly Brinson-style attribution commentary (allocation, selection, currency, benchmark-relative return) for a generic multi-asset fund. It needs eight things from this layer:
1. **Numeric faithfulness, deterministic and blocking.** A code scorer extracts every figure, sign and direction word ("added", "detracted", "overweight") and compares it with the attribution-engine output recorded in the same trace. The read-only L4 tool call is a span, so the reference values are evidence, not memory. Any mismatch outside the agreed rounding rule fails the run; no LLM judge is involved.
2. **Groundedness against approved sources.** Each market-context claim must be supported by a retrieved, approved document (calibrated judge or NLI metric). Unsupported claims are flagged, so inference stays distinguishable from source data.
3. **House-style checks.** Rules for terminology, prohibited phrases, tense and length; an LLM judge only for tone.
4. **Trajectory check.** The workflow calls the attribution tool, then retrieval, then drafts. Any extra tool call or write attempt is a defect.
5. **Regression suite of past commentaries.** About 24 to 36 months of approved commentaries with their attribution snapshots, run on every change of model, prompt, index or judge, with each reviewer-caught error added as a case. The same suite re-qualifies a fallback model for the SS2/21 exit route.
6. **Reviewer-edit feedback loop.** PM edits are captured as diffs on the trace with an edit-size score and reason code. The monthly human-intervention rate serves the IOSCO indicator, and recurring edit types become eval cases or style rules.
7. **Evidence pack retention.** Per commentary: trace ID, prompt and template version, model and judge versions, attribution snapshot hash, retrieved document IDs, eval results with thresholds, approver and timestamp, final text and diff. It is written to the firm's WORM or records archive (C8) under the retention policy, independent of any vendor tier.
8. **Cost and latency per commentary**, reported to C6.

**What L9 must never do [AJ]:**
- pass a draft whose numbers fail the deterministic check because an LLM judge scored it "faithful"
- send untokenised client or holdings data to an external judge or SaaS trace store that has not been assessed
- let a vendor auto-fix feature (LangSmith Engine, Braintrust Loop) change a production prompt outside change control
- discard or overwrite eval evidence when a vendor tier expires
- score a release without recording which dataset and judge version produced the score

### 9.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| Downstream "evals and observability" layer with eight tiles | Products now include gateways (Braintrust, LangSmith, MLflow), guardrails (Opik), prompt management and fix proposals [VF: A1-S043, A1-S039, A1-S103, A1-S067] | A cross-cutting plane: firm-owned OTel Collector, one platform of record, CI eval and red-team harness, evidence archive in C8 [Rec] |
| Langfuse "open source" | MIT core, enterprise-gated audit and RBAC; ClickHouse-owned [VF: A1-S033, A1-S021] | Strategic platform of record, self-hosted with Enterprise licence [Rec] |
| LangSmith "trace & eval" | Agent platform (Engine, Fleet, Gateway, Deployment) [VF: A1-S039] | Strategic for LangGraph estates, dual-instrumented with OTel [Rec] |
| Braintrust "evals platform" | Repositioned to "active observability for agents"; hybrid data plane [VF: A1-S043, A1-S041] | Tactical: eval-led teams [Rec] |
| Phoenix "Atrace" | Arize Phoenix, ELv2, Dynatrace-owned [VF: A1-S048, A1-S045] | Tactical: validation sandboxes; OpenInference as portable instrumentation [Rec] |
| Arize "RAG metrics" | Arize AX, full platform; duplicate vendor tile; Dynatrace-owned [VF: A1-S046, A1-S045] | Tactical; re-assess after the Dynatrace roadmap [Rec] |
| DeepEval "LLM unit tests" | Accurate; agentic and trajectory metrics added [VF: A1-S068] | Tactical: default CI metric library [Rec] |
| Promptfoo "red-teaming" | Evals plus red-teaming; OpenAI acquisition announced 9 March 2026, closing not published [VF: A1-S062, V2-S042] | Tactical: one of two red-team tools [Rec] |
| Opik "comet" | Apache-2.0 full platform by Comet [VF: A1-S050] | Tactical: Apache-2.0 alternative with Comet Enterprise [Rec] |
| (absent) | MLflow GenAI, Datadog Agent Observability, W&B Weave [VF: A1-S103, A1-S097, A1-S104] | MLflow Strategic where an ML platform exists; Datadog and Weave Tactical [Rec] |

**H8 (evaluation and observability are cross-cutting, not a downstream layer). Provisional view; verdict in synthesis.**

The evidence supports the hypothesis on four counts.

- **The instrumentation standard spans the stack.** OTel GenAI conventions cover client inference, agents, tool execution, retrieval, evaluation and MCP. Evaluation results have their own event type [VF: A1-S061, A1-S059].
- **Tools couple CI to production.** Six of the original products document a CI evaluation path [VF: A1-S108, A1-S106, A1-S067, A1-S068, A1-S065, A1-S109], and the platform products run evaluators over production traces [VF: A1-S072, A1-S073, A1-S046, A1-S099].
- **Vendors are pushing the layer sideways.** It is moving into gateways (C1), prompt management (C5), guardrails (C2) and security testing (C7) [VF: A1-S043, A1-S103, A1-S067, A1-S024].
- **Ownership is consolidating into horizontal platforms.** The new owners are an APM vendor (Dynatrace), a database vendor (ClickHouse), a model vendor (OpenAI) and a GPU cloud (CoreWeave), and a second APM vendor (Datadog) sells its own module [VF: A1-S045, A1-S021, A1-S024, A1-S131, A1-S097].

The counter-evidence is that the OTel GenAI conventions are still "Development" and recently moved repository [VF: A1-S058, A1-S060], so the shared plane is not yet stable.

**Provisional recommendation.** Reposition L9 as a cross-cutting plane drawn alongside the control-plane components (C1 to C8) [AJ]. It should have a firm-owned telemetry and evidence spine, and the products should sit on it as replaceable backends [AJ]. **Provisional; verdict in synthesis.**


## 8. Data extraction, ingestion and web

> L8 turns source material (enterprise documents, scans, spreadsheets, slides, e-mails and web pages) into clean, structured, permission-tagged content that retrieval (L7/L6) and agents can trust. The graphic treats it as a shelf of parsers and scrapers. Since then the products have moved: LlamaParse is now the name of LlamaIndex's whole document platform [VF: A1-S080, V1-S008]; Mistral OCR is at version 4.1, with 4.0 retired on 30 September 2026 [VF: A1-S130, V1-S014]; Docling graduated within LF AI & Data in August 2026 [VF: V1-S091]; and Firecrawl's server is AGPL-3.0, with its enterprise controls offered only in the Cloud [VF: A1-S053, A1-S079]. Of the ten products assessed, only Unstructured's open-source connectors carry access-control metadata into the pipeline [VF: A1-S094], and none emits lineage [VF: A1-S094, A1-S096]. The parsers are commodity components; the enterprise value is in the control plane that wraps them [AJ]. **Recommendation:** standardise on a self-hosted, open document model (Docling as default, Unstructured ingest where connectors with ACLs are needed), put managed parsers and OCR engines behind that model as replaceable engines, and build the lineage, classification, entitlement and incremental-indexing envelope yourself [Rec].

### 8.1 Responsibility

L8 owns the path from an approved source to an indexed, governed unit of content: source → acquisition → parsing → OCR → structure extraction → cleaning → chunking → metadata → indexing (plan §5), across PDFs and scans, tables, PowerPoint and Excel, websites, e-mails, enterprise documents, structured data and multimodal documents [AJ].

The layer has two distinct jobs, and the graphic blurs them [AJ]:

1. **Acquisition:** getting bytes from a source the firm is entitled to use. Web acquisition (Firecrawl, Crawl4AI, Apify) raises questions of law, terms of service, robots.txt and provenance. Enterprise acquisition (connectors into SharePoint, OneDrive, Confluence, S3) raises questions of entitlements and change detection [AJ].
2. **Document understanding:** turning bytes into faithful structure: text, reading order, tables, figures and their coordinates. Docling, LlamaParse, MinerU, Reducto, Unstructured, Mistral OCR and Google Document AI compete here [AJ].

**Hand-offs.**

- **Downwards (sources and C3).** L8 receives documents only from sources on an approved-source register, and it receives classification and PII policy from C3 [Rec].
- **Upwards (L7 and L6).** L8 hands over chunks wrapped in a metadata envelope (source, version, ACL principals, classification, PII flags, parser manifest, lineage run ID). L7 embeds those chunks and L6 stores them with the envelope intact, so that retrieval-time filtering can enforce entitlements [Rec].
- **Sideways (L4).** L8 is not the agent's live web tool. Firecrawl, Crawl4AI and Apify all expose agent-facing interfaces (MCP or search endpoints) that overlap L4 [VF: A1-S077, A1-S074, A1-S089]. Batch ingestion into a governed corpus belongs to L8. Runtime browsing by an agent belongs to L4 and is governed as a tool call [AJ].
- **To C8.** Lineage events and parse manifests flow to the governance and evidence store [Rec].

### 8.2 Why it matters

L8 failures surface as model failures [AJ]. A merged table cell becomes a "hallucinated" number; a permission that never reached the index becomes a data leak; a web page with hidden instructions becomes an indirect prompt injection; a parser upgrade silently shifts chunk boundaries [AJ]. ESMA expects "ex-ante input controls and frequent ex-post output controls" for AI used in investment services [VF: R-INTL-AI-ASSETMGMT; A8-S058, A8-S059]. In a RAG system, L8 is where the input controls live [AJ].

**Illustrative scenario [AJ].** A multi-asset fund's monthly factsheet has a performance table with fund, benchmark and relative columns. After a routine library upgrade, the parser starts merging two header cells, so the "relative" column shifts one place left for a single share class. Nothing fails: parsing succeeds, chunks are indexed and retrieval works. The commentary agent retrieves last quarter's factsheet as context and repeats a relative-return figure that is really the benchmark return. The reviewer checks the current month's numbers against the attribution engine but not the prior-period comparison that the draft quoted. Nothing in the pipeline records which parser version produced the chunk, so nobody can tell which other documents are affected. The firm has to re-parse and re-review a quarter's corpus by hand. The cause was an unpinned parser and the absence of any table-reconciliation check, not the LLM [AJ].

### 8.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Table cell exact-match | Share of numeric table cells reproduced exactly (value, sign, unit, row/column) | ≥ 99.5% on a golden set of house documents; 100% for any table feeding a published number | Golden set of factsheets and reports with hand-keyed tables; run on every parser or model change |
| Text fidelity (OCR) | Character error rate on scanned pages | Set per document class; track the trend after each engine change | Sampled pages against reference transcriptions |
| Structural fidelity | Correct reading order, headings and table boundaries | ≥ 95% of sampled pages judged correct | Reviewer sample, stratified by layout type |
| Envelope completeness | Share of indexed chunks carrying source ID, version, ACL, classification, parser manifest and lineage run ID | 100% (hard gate: no envelope, no index) | Index-time validation rule |
| ACL propagation lag | Time from a permission change at source to the index reflecting it | Under 1 hour for confidential sources; under 24 hours otherwise | Synthetic permission-change probes |
| Deletion propagation lag | Time from source deletion to removal from every index and cache | Under 24 hours | Tombstone probes |
| Residual PII rate | PII found after redaction in sampled chunks | Zero for classes that must be masked | Second-pass scanner on samples |
| Reproducibility | Share of re-parses with a pinned manifest that produce identical output hashes | 100% for self-hosted engines; documented exceptions for hosted ones | Periodic re-parse jobs |
| Unapproved-source ingestions | Documents ingested from sources not on the register | Zero | Register check at acquisition |
| Cost per 1,000 pages | All-in parse, OCR and compute cost | Budgeted per document class | FinOps tags (C6) |

### 8.4 How it works

```text
 Approved-source register (owner, licence/ToS, legal basis, default classification, residency)
        |
        v
 [A] ACQUISITION -------------------------------------------------------------+
     web: crawler (robots/ToS checked)     enterprise: connector (+ACL digest) |
        |  raw object + content hash + source version + ACL snapshot         |
        v                                                                     |
 [B] PRE-PARSE CONTROLS: malware/type check -> classification -> PII/DLP (C3) |
        |                                                   (quarantine) <----+
        v
 [C] DOCUMENT UNDERSTANDING (replaceable engines behind one interface)
     layout/parse (Docling | Unstructured | LlamaParse | Reducto | MinerU)
     OCR engine (built-in | Mistral OCR | Document AI)
        |  canonical document model + parse manifest (engine, version, model ID, config hash)
        v
 [D] VALIDATION: table reconciliation, confidence thresholds, injection scan
        |
        v
 [E] CLEAN + CHUNK + METADATA ENVELOPE (source, version, ACL, class, PII, manifest)
        |
        v
 [F] INCREMENTAL INDEX (hash + ACL-digest diff; tombstones) --> L7 embed --> L6 store
        |
        +--> lineage events (OpenLineage run/job/dataset + custom facets) --> C8
```

**Content-type coverage.** Docling covers PDF, DOCX/XLSX/PPTX, legacy Office, HTML, CSV, images, audio and video [VF: A1-S111]. MinerU covers PDF, Office, EPUB, OFD, HTML and CSV [VF: A1-S055]. LlamaParse claims 130+ formats [VF: A1-S080]. E-mail (with attachments and thread structure) is not documented as a first-class format for any L8 product in the fact base [NPV]. Structured data should bypass document parsing and enter through governed data pipelines or L4 tools [AJ].

**Mechanics by stage.**

- **Acquisition.** Firecrawl respects robots.txt by default [VF: A1-S053]. Its X and LinkedIn data are routed through third-party providers at separate prices [VF: A1-S077, A1-S053], so the provenance of that content is one step further removed [AJ]. On the enterprise side, Unstructured's SharePoint, OneDrive and Confluence connectors compute a `permissions_version` SHA-256 digest of the ACL at index time. In incremental mode (`reprocess_all=false`, `reprocess_on_permission_change=true`), a change to the ACL alone triggers reprocessing [VF: A1-S094]. The connectors also record an unavailable permission fetch separately from an empty permission set [VF: A1-S094]. That distinction is what stops a failed lookup from being read as "public" [AJ].
- **Parsing and OCR.** Mistral OCR 4 returns paragraph-level bounding boxes, structural block labels and block-level confidence scores [VF: A1-S130, A1-S135]. Google Document AI's Layout Parser includes initial chunking [VF: A1-S101]. MinerU 4.0 adds citation locators for agent reading [VF: A1-S055]. Keep coordinates, confidence scores and locators rather than flattening to Markdown; reconciliation and citations depend on them [AJ].
- **Validation.** No product in this layer offers reconciliation of parsed tables against an authoritative source; that has to be built [AJ]. Firecrawl offers an opt-in prompt-injection check for JSON extraction [VF: A1-S077]. No equivalent was found in the document parsers [AJ].
- **Lineage.** OpenLineage defines run, job and dataset entities extended by facets [VF: A7-S041]. Its changelog has no GenAI-, LLM-, embedding- or vector-specific facets [VF: A7-S042], so parse, chunk, embed and index steps must be modelled as generic jobs or custom facets [AJ]. OpenLineage supports user-supplied tags facets, which can carry classification labels [VF: A7-S042]. Apache Airflow ships an OpenLineage provider [VF: A7-S045], so an Airflow-orchestrated ingestion pipeline can emit lineage without new tooling [AJ].

### 8.5 Enterprise design principles

**Security.**

- Treat every ingested document as untrusted input. The OWASP Top 10 for Agentic Applications for 2026 lists ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC; A8-S042]. Indirect injection through documents an agent reads is the L8 route to it [AJ].
- Scan before parsing, and quarantine anything that fails [Rec].
- Run parsers with no outbound network access, so that a malicious document cannot exfiltrate data [Rec].

**Data protection.**

- Classify and apply DLP before content reaches any third-party engine, not at the prompt [Rec].
- Presidio (MIT, now community-governed under Data Privacy Stack) and Google Sensitive Data Protection are the C3 candidates for this step [VF: A6-S040, A6-S066].
- Presidio's own README warns that it is not guaranteed to find all sensitive data [VF: A6-S068]. Sampling for residual PII is therefore a KPI, not an option [AJ].

**Entitlements.**

- Capture ACLs at acquisition, carry them on every chunk, and fail closed when the permission fetch fails [Rec].
- The Unstructured connector pattern (ACL digest, separate "unavailable" state, reprocess on change) is the reference behaviour to require of any connector, bought or built [Rec].

**Reproducibility.**

- Pin every engine version and model ID, and write them into a parse manifest stored with the output [Rec].
- Store parsed outputs, not just raw documents. Docling had reached 2.135.0 by 7 October 2026 [VF: A1-S008], and Mistral retired OCR 4.0 on 30 September 2026 [VF: A1-S130]. A hosted model that has been retired cannot reproduce last quarter's parse [AJ].

**Scalability and cost.**

- Route by document class: a cheap OCR tier for simple scans and expensive agentic tiers only for complex layouts [Rec].
- Published prices differ by more than an order of magnitude between engines. Document AI Enterprise OCR costs US$1.50 per 1,000 pages [VF: A1-S101]. Mistral OCR 4.1 costs US$4 per 1,000 pages [VF: A1-S130]. Reducto Parse costs US$10 per 1,000 pages [VF: A1-S113]. LlamaParse tiers run from 1 to 45 credits per page [VF: A1-S116]. All prices are as of 7 October 2026.

**Portability and observability.** Keep one canonical document model in-house with engines behind an adapter; a passing golden-set regression run is the switching test. Emit lineage events and pipeline metrics (quarantine rate, confidence distribution, reconciliation failures) to L9 and C8 [Rec].

**Patterns** [Rec]:
- Approved-source register as the only entry point.
- Dual-parse reconciliation for tables that feed numbers.
- Incremental indexing on content hash plus ACL digest, with tombstones for deletions.
- Quarantine queue with human release.
- Parse manifest with every output.

**Anti-patterns** [AJ]:
- Letting a vendor's managed index become the system of record for entitled content.
- Using a model "latest" alias in production.
- Flattening tables to prose before validation.
- Treating an agent's live web fetches as ingestion.
- Indexing first and classifying later.
- Using marketplace scrapers on any non-public data.

### 8.6 Product selection criteria

| Scorecard criterion | What to evaluate in L8 |
|---|---|
| Technical capability | Table and layout fidelity on *your* golden set; format coverage; coordinates and confidence output; connector ACL capture |
| Enterprise readiness | SSO, RBAC and audit on the hosted service; support terms; for libraries, an API-server mode |
| Security and compliance | SOC 2 Type II and ISO 27001 scoped to the parsing service (and BYOC installs); retention controls; training-use terms; CVE handling for open source |
| Deployment flexibility | Self-hosted, in-VPC or air-gapped options; EU and UK processing regions; network-isolated operation |
| Ecosystem | Connectors to your sources and stores; orchestration and lineage hooks (Airflow, OpenLineage) |
| Reliability and maturity | Deprecation and model-retirement windows; governance (foundation, single maintainer, venture-backed) |
| Cost / TCO | Price per 1,000 pages by tier; GPU needs for self-hosting; licence thresholds; operations burden (browsers, proxies, anti-bot) |
| Lock-in / portability | Open output format; ability to re-parse elsewhere; licence (AGPL, custom thresholds, attribution); platform reach into L6/L3 |

Vendor accuracy claims, such as Unstructured's statement that its API gives 2x table content accuracy and 58% less invented content than the open-source library, are reported claims only [R: A1-S075]. They should not be used as decision inputs [AJ].

### 8.7 Product deep dives

#### Document understanding

**Docling (Strategic).**

- **What it is now.** Docling is an MIT-licensed toolkit that parses PDF, Office (including legacy Office), ODF, HTML, images, audio and video into a unified DoclingDocument, with OCR, VLM pipelines, ASR and hybrid chunking [VF: A1-S057, A1-S111]. IBM Research Zurich started it, IBM donated it to LF AI & Data in March 2025, and it reached Graduate tier in August 2026 [VF: A1-S057, V1-S091]. It runs as a library, CLI, docling-serve REST API (stable v1) or MCP server, and IBM offers a managed "Docling for IBM watsonx" [VF: A1-S082, A1-S110]. The current version is 2.135.0, released 7 October 2026 [VF: A1-S008].
- **Strengths.** Neutral governance, a permissive licence and local processing [VF: A1-S057]. The DoclingDocument can serve as the firm's canonical document model [AJ].
- **Limitations and risks.** The README and docs navigation show no ACL, PII or lineage features [VF: A1-S057]. Individual models carry their own licences [VF: A1-S057]. Releases are very frequent, so pinning is mandatory [AJ]. It publishes a security policy with private vulnerability reporting, takes part in the OpenSSF Best Practices badge programme and signs its releases on PyPI, Quay.io and GHCR [VF: B-REV-S001].
- **Choose when** documents must stay in your estate and you want an open format that outlives engine changes. **Avoid when** you have no platform team to run a Python service.
- **Nearest competitors.** Unstructured, MinerU, LlamaParse.
- **FS note.** The default engine for confidential and client documents, provided the parse manifest is recorded [Rec].
- **Flags.** None. Inherits host controls.

**Unstructured (Strategic; Renamed).**

- **What it is now.** The Apache-2.0 `unstructured` library (0.27.16, 5 October 2026) and `unstructured-ingest` connectors stay free [VF: A1-S011, A1-S075, A1-S095]. The commercial offering is the Transform v2 API, with shared pay-as-you-go, dedicated and in-VPC Business tiers [VF: A1-S117, V1-S019]. The vendor lists SOC 2 Type 2, ISO 27001, HIPAA and GDPR, and has announced CMMC 2.0 Level 2 [VF: A1-S117, V1-S090].
- **Strengths.** It is the only L8 product with verified permission-aware ingestion: the ACL digest, reprocessing on permission change, and a separate "permission unavailable" state [VF: A1-S094]. It also offers a broad set of connectors out to vector stores and warehouses [VF: A1-S094].
- **Limitations and risks.**
  - SAML 2.0 and OIDC SSO with account- and workspace-level roles are documented for Business deployments, but no workspace audit log is documented [VF: B-REV-S016].
  - The best models are API-only [VF: A1-S075].
  - The library is still pre-1.0 after four years [VF: A1-S011].
  - The per-page price conflicts between US$0.015 and US$0.03 [VF: A1-S117, A1-S118].
  - Usage analytics are on by default [VF: A1-S075].
  - In the ingest changelog, "redaction" means credentials in error logs, not PII in content [VF: A1-S094].
- **Choose when** entitlement-preserving ingestion from SharePoint, OneDrive or Confluence matters. **Avoid when** you need a documented, exportable audit log on the hosted service today.
- **Nearest competitors.** Docling, LlamaParse, Reducto.
- **FS note.** Run the open-source connectors in your estate and use the ACL digest as the entitlement source of truth for the index [Rec].

**LlamaParse (Tactical; Renamed).**

- **What it is now.** LlamaParse is now LlamaIndex's whole document platform: Parse, Extract, Index, Split and Agents, previously marketed as LlamaCloud [VF: A1-S080, A1-S081, V1-S008]. LlamaIndex says its primary focus has shifted from the open-source framework to LlamaParse [VF: A1-S080]. Regions are NA and EU, with in-region EU storage and processing, an EU DPA and SCCs. BYOC is available on Azure, AWS and GCP, along with Helm self-hosting and on-premises installs [VF: A1-S115]. It holds SOC 2 Type II, offers a HIPAA pipeline with a BAA on request, and supports OIDC SSO for self-hosted installs [VF: A1-S115, A1-S116]. Pricing runs from Free to Enterprise, with parse tiers from 1 to 45 credits per page [VF: A1-S116].
- **Strengths.** Breadth of formats (130+) and flexible residency [VF: A1-S080, A1-S115].
- **Limitations and risks.** Permission sync, PII detection and lineage were not found [VF: A1-S080]. The legacy SDKs were deprecated in 2026 [VF: A1-S013]. Whether the SOC 2 report covers BYOC installs is not stated [NPV]. On the hosted service every organisation member has the same access to projects and resources; named roles exist only in self-hosted installs, and audit logs are not documented [VF: B-REV-S023]. The platform reaches into L6 (Index) and L3 (Agents) [VF: A1-S080].
- **Choose when** you want managed parsing with an EU region or BYOC. **Avoid when** its Index would become your system of record.
- **Nearest competitors.** Reducto, Unstructured, Docling.
- **FS note.** Use Parse and Extract only, and keep indexing in your own L6 store [Rec].

**Reducto (Tactical).**

- **What it is now.** Reducto is a proprietary API with Parse, Extract, Split, Edit, Classify and Pipeline resources, webhooks, and EU and AU endpoints [VF: A1-S092, A1-S093]. Vendor pages state SOC 2 Type I and II, HIPAA BAAs, 24-hour auto-deletion, `retention=0` on Enterprise, no training on customer data, and VPC, on-prem and air-gapped deployment [VF: A1-S112]. It has raised US$108M in total, including a Series B led by a16z in October 2025 [VF: A1-S114, V1-S018]. Pricing is US$10 per 1,000 pages for Parse and US$20 for Extract [VF: A1-S113].
- **Strengths.** Extraction-oriented API design and deployment options on paper [AJ].
- **Limitations and risks.** The security claims come from vendor-authored pages that contradict each other on ZDR eligibility, and the verifier lists them as not to be relied on. Request the SOC 2 report and BAA directly [VF: A1-S112]. SSO/SAML and RBAC are Enterprise-only features in the product docs [VF: B-REV-S017]. No PII, ACL or lineage features were found [VF: A1-S093].
- **Choose when** complex layouts justify a managed extraction API and due diligence produces the reports. **Avoid when** the reports cannot be obtained.
- **Nearest competitors.** LlamaParse, Google Document AI, Unstructured.
- **FS note.** Score it on evidence received, not on vendor pages [Rec].

**MinerU (Experimental).**

- **What it is now.** The MinerU 4.0 line (4.0.10, 29 September 2026) parses PDF, images, Office, OpenDocument, EPUB, OFD, HTML and CSV. It offers four tiers (Flash, Basic, Standard, Advanced), a document library with citation locators, and a router [VF: A1-S010, A1-S055]. It parses locally by default and uploads nothing unless `--remote` is set [VF: A1-S055].
- **Licence.** The "MinerU Open Source License" is Apache-2.0 plus additional terms. A separate commercial licence is required above 100M MAU or US$20M monthly revenue, measured group-consolidated. Online services must give attribution, and rights terminate automatically on breach [VF: A1-S054, V1-S003]. The commercial price is not published [VF: A1-S054].
- **Strengths.** Local-first operation, citation locators, and telemetry that excludes document content and can be disabled [VF: A1-S055].
- **Limitations and risks.** The Standard and Advanced tiers need a GPU with 8 GB+ VRAM [VF: A1-S055]. A 3.x to 4.0 migration happened in 2026 [VF: A1-S055].
- **Choose when** you are under the thresholds or hold a commercial licence. It can also serve as a second parser for reconciliation [AJ]. **Avoid when** a large group has no commercial licence.
- **Nearest competitors.** Docling, Unstructured, LlamaParse.
- **FS note.** Many large asset managers will exceed the group revenue threshold, so legal review comes first [AJ].

**Mistral OCR (Tactical).**

- **What it is now.** The current model is OCR 4.1 (`mistral-ocr-4-1`, aliases `mistral-ocr-latest` and `mistral-ocr-4`), part of Mistral Document AI. Vendor pages disagree on whether it was released in July or August 2026; the changelog marked it GA on 26 August 2026 [VF: A1-S130, V1-S014]. OCR 4.0 was retired on 30 September 2026. OCR 3 remains for existing integrations, and the original Mistral OCR is no longer maintained [VF: A1-S130, V1-S014]. Pricing is US$4 per 1,000 pages, or US$2 in batch [VF: A1-S130, V1-S010]. The managed API is EU-hosted, and enterprise customers can self-manage it as a single container, in a private cloud or on-premises [VF: A1-S135]. Mistral holds SOC 2 Type II, ISO 27001:2022 and ISO 27701:2019 at company level, and the OCR scope is not confirmed [VF: A1-S136]. Enterprise plans add SAML SSO, organisation roles with isolated Workspaces, and audit logs that cannot be exported [VF: B-REV-S014, B-REV-S015].
- **Strengths.** EU residency, block-level confidence scores, and price [VF: A1-S130, A1-S135].
- **Limitations and risks.** Model-version churn is the operational risk: about five weeks passed between 4.1 GA and 4.0 retirement [VF: A1-S130, V1-S014]. That window is short for a regulated re-validation cycle [AJ]. Self-hosting terms and sizing are unpublished [NPV].
- **Choose when** you need an EU or self-managed OCR engine behind your own pipeline. **Avoid when** you cannot re-validate within weeks.
- **Nearest competitors.** Google Document AI, Docling's built-in OCR, Reducto.
- **FS note.** Pin the dated model ID and treat each retirement as a change-control event [Rec].

**Google Cloud Document AI (Tactical; added).**

- **What it is now.** Document AI provides processors for Enterprise Document OCR, Form Parser, Layout Parser (with chunking), Custom Extractor, classifier/splitter and Summarizer [VF: A1-S101]. It is in scope for Google Cloud's ISO 27001/27017/27018, SOC 1/2/3 and PCI DSS [VF: A1-S102]. OCR costs US$1.50 per 1,000 pages (US$0.60 above 5M pages), and Layout Parser costs US$10 [VF: A1-S101].
- **Strengths.** Certifications and price [VF: A1-S101, A1-S102]. Google Cloud EMEA Limited is designated under both DORA and the UK CTP regime [VF: R-DORA, R-UK-CTP; A8-S020, A8-S023].
- **Limitations and risks.** Outputs are Google-specific, and the service requires Google Cloud [VF: A1-S101]. It offers us and eu multi-regions, regional processors, CMEK (allowlisted in some regions), VPC Service Controls and IAM deny policies [VF: B-REV-S010, B-REV-S011]. Azure AI Document Intelligence and AWS Textract are the equivalent services but are not in the fact base [NPV].
- **Choose when** GCP is your approved cloud. **Avoid when** you are reducing hyperscaler concentration.
- **Nearest competitors.** Mistral OCR, Reducto, and the Azure and AWS equivalents.
- **FS note.** Under the UK CTP regime, regulated firms remain responsible for their own due diligence and contingency planning [VF: R-UK-CTP; A8-S023].

#### Web acquisition

**Firecrawl (Tactical).**

- **What it is now.** Firecrawl is a web data API (v2) covering scrape, crawl, map, search, extract and parse, plus Agent, Browser and Interact [VF: A1-S077, A1-S079]. The server is AGPL-3.0 and the SDKs are MIT. Agent, Browser, dashboards and enterprise controls are Cloud-only [VF: A1-S053, A1-S079, V1-S002]. Per-request options include PII redaction (+4 credits per page), ZDR (+1) and a prompt-injection check for JSON extraction. Enterprise adds SSO, SCIM, key restrictions and a DPA [VF: A1-S076, A1-S077], plus Admin and Member roles and SIEM audit logging of scrape events [VF: B-REV-S024]. The privacy policy places servers and data in the US [VF: A1-S134]. Firecrawl announced Alexandria and a US$75M Series B on its blog in September 2026; its changelog dates the round 20 August [VF: A1-S129].
- **Strengths.** The richest set of per-request controls among the web tools [AJ].
- **Limitations and risks.** The security claims are vendor pages only, and the verifier says not to rely on them [VF: A1-S076]. Self-hosting means owning auth, TLS, persistence and anti-bot services [VF: A1-S079]. AGPL obligations apply to modified network services [VF: A1-S053].
- **Choose when** you need batch ingestion of approved public sources. **Avoid when** EU or UK processing is required, or when you plan to modify the server without legal review.
- **Nearest competitors.** Crawl4AI, Apify.
- **FS note.** Public data only, unless the SOC 2 report has been reviewed [Rec].

**Crawl4AI (Experimental).**

- **What it is now.** Crawl4AI is an open-source crawler that produces Markdown or structured data. It ships as a library, CLI, Docker REST server and MCP server, plus the hosted Crawl4AI Cloud [VF: A1-S074]. The current version is 0.9.4, released 23 September 2026 [VF: A1-S009]. The licence is Apache-2.0 with an appended attribution requirement for distributions and public uses, and legal review is advised [VF: A1-S056, V1-S001]. The self-hosted server requires an API token on every endpoint by default [VF: A1-S074].
- **Strengths.** Free, self-hosted, and inside your estate [VF: A1-S074].
- **Limitations and risks.** The project is pre-1.0 and started with a single maintainer [VF: A1-S009, A1-S074]. No venture funding has been disclosed; this comes from an aggregator only [R: A1-S132]. The project publishes a security policy and advisories: eight advisories, five rated high (SSRF, arbitrary file write, secret leakage, XSS), were fixed in 0.9.3 and 0.9.4 in August and September 2026, and only 0.9.x is supported [VF: B-REV-S003]. Pin 0.9.4 or later [Rec].
- **Choose when** you are prototyping, or crawling a few approved public sources. **Avoid when** it would be a critical dependency.
- **Nearest competitors.** Firecrawl, Apify.
- **FS note.** Record the attribution clause in the open-source register [Rec].

**Apify (Tactical).**

- **What it is now.** Apify runs serverless "Actors" with a proxy, datasets and queues, the Apify Store marketplace and an MCP server [VF: A1-S087, A1-S089]. It holds SOC 2 Type II [VF: A1-S085, V1-S089]. It is hosted only in AWS us-east-1, and no EU region is documented [VF: A1-S086, V1-S089]. Third-party Store Actors are outside Apify's control [VF: A1-S086]. Paid plans run from US$19 to US$999 per month, plus compute units [VF: A1-S133].
- **Strengths.** A ready-made Actor for many long-tail sites [AJ]. The MCP server exposes Store Actors directly to AI agents [VF: A1-S089], which makes Apify as much an L4 tool as an L8 pipeline component [AJ].
- **Limitations and risks.** It has a single region, its Actors and storage are platform-specific [VF: A1-S087], and no audit log was found, although organisation roles and per-resource permissions are documented and SSO is stated [VF: B-REV-S025].
- **Choose when** you need public-data collection that never touches client data. **Avoid when** any personal or confidential data is involved.
- **Nearest competitors.** Firecrawl, Crawl4AI.
- **FS note.** Treat each Actor as third-party code that needs review [Rec].

### 8.8 Comparison table

Scores are integers from 1 to 5. Totals are weighted averages from `tools/score.py` (generic and FS weights, plan §8.1).

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8-docling | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4.00 | 4.05 | Strategic |
| L8-unstructured | 4 | 3 | 4 | 5 | 4 | 3 | 3 | 4 | 3.80 | 3.85 | Strategic |
| L8-llamaparse | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 2 | 3.25 | 3.05 | Tactical |
| L8-reducto | 4 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | 3.05 | 2.90 | Tactical |
| L8-mistral-ocr | 3 | 3 | 3 | 4 | 3 | 2 | 4 | 3 | 3.15 | 3.10 | Tactical |
| L8-google-document-ai | 4 | 3 | 5 | 2 | 3 | 3 | 4 | 2 | 3.40 | 3.30 | Tactical |
| L8-firecrawl | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 2 | 3.10 | 2.85 | Tactical |
| L8-crawl4ai | 3 | 2 | 2 | 4 | 3 | 2 | 4 | 4 | 2.90 | 2.90 | Experimental |
| L8-mineru | 4 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2.80 | 2.70 | Experimental |
| L8-apify | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 2 | 2.65 | 2.55 | Tactical |

**Evidence caps applied [AJ]:**
- **Enterprise readiness capped at 2:** LlamaParse, because hosted organisations are flat and audit logs are not documented [VF: B-REV-S023]. The CP2 review lifted the caps on Unstructured, Reducto, Mistral OCR, Google Document AI and Apify after finding SSO and role documentation [VF: B-REV-S016, B-REV-S017, B-REV-S014, B-REV-S010, B-REV-S025].
- **Security capped at 2:** Firecrawl and Reducto, because their security claims are vendor-only and flagged in V1 §4.
- **Library rule** (scored on project hygiene; inherits host controls): Docling (security 4, on a verified security policy and signed releases [VF: B-REV-S001]), Crawl4AI (2, on its advisory history [VF: B-REV-S003]) and MinerU.

**Key facts** (as of 7–8 October 2026)

| Product | Licence | Deployment | Certifications | EU residency | Ownership status |
|---|---|---|---|---|---|
| Docling | MIT; models own licences [VF: A1-S057] | Library, REST, MCP, IBM-managed [VF: A1-S082, A1-S110] | n/a (library) | In-estate [AJ] | LF AI & Data Graduate, Aug 2026 [VF: V1-S091] |
| Unstructured | Apache-2.0 OSS; proprietary API [VF: A1-S011, A1-S075] | OSS, SaaS, dedicated, in-VPC [VF: A1-S117] | SOC 2 Type 2, ISO 27001, HIPAA, CMMC 2.0 L2 (vendor-listed) [VF: A1-S117, V1-S090] | Hosted region NPV; in-estate via OSS | Independent [NPV] |
| LlamaParse | Proprietary; SDK MIT [VF: A1-S014] | SaaS NA/EU, BYOC, self-host, on-prem [VF: A1-S115] | SOC 2 Type II; HIPAA BAA [VF: A1-S115] | EU region [VF: A1-S115] | LlamaIndex, Inc.; renamed from LlamaCloud [VF: A1-S080] |
| Reducto | Proprietary; SDK Apache-2.0 [VF: A1-S090] | SaaS, VPC, on-prem, air-gap (vendor) [VF: A1-S112] | SOC 2 Type I/II, HIPAA (vendor-only) [VF: A1-S112] | EU endpoint [VF: A1-S092] | Private; US$108M raised [VF: A1-S114] |
| Mistral OCR | Proprietary model [VF: A1-S135] | EU API; self-managed (enterprise) [VF: A1-S135] | Company-level SOC 2 II, ISO 27001, 27701 [VF: A1-S136] | EU-hosted API [VF: A1-S135] | Mistral AI [VF: A1-S083] |
| Google Document AI | Proprietary [VF: A1-S101] | Managed SaaS [VF: A1-S101] | ISO 27001/17/18, SOC 1/2/3, PCI DSS [VF: A1-S102]; CMEK [VF: B-REV-S011] | us/eu multi-regions [VF: B-REV-S010] | Google Cloud [VF: A1-S101] |
| Firecrawl | AGPL-3.0 server; MIT SDKs [VF: A1-S053, V1-S002] | Cloud; reduced self-host [VF: A1-S079] | SOC 2 Type II (vendor-only) [VF: A1-S076] | US per privacy policy [VF: A1-S134] | Venture-backed, Series B 2026 [VF: A1-S129] |
| Crawl4AI | Apache-2.0 + attribution clause [VF: A1-S056] | Library, Docker, hosted cloud [VF: A1-S074] | NPV | In-estate [AJ] | Open-source project; unfunded per aggregator [R: A1-S132] |
| MinerU | Custom: Apache-2.0 + thresholds [VF: A1-S054] | Local, self-host, remote service [VF: A1-S055] | NPV | In-estate by default [VF: A1-S055] | OpenDataLab MinerU Team [VF: A1-S054] |
| Apify | Proprietary; client Apache-2.0 [VF: A1-S016] | SaaS only [VF: A1-S087] | SOC 2 Type II [VF: A1-S085] | None; AWS us-east-1 only [VF: A1-S086] | Apify Technologies s.r.o. [VF: A1-S016] |

### 8.9 Decision tree

```text
START: Is the source on the approved-source register (owner, licence/ToS, legal basis, classification)?
  ├─ No  → STOP. Register it first. Never ingest from an unregistered source.
  └─ Yes → What kind of source?
      │
      ├─ PUBLIC WEB
      │   ├─ Is this an agent fetching pages at run time?  → Not L8. Govern as an L4 tool call.
      │   ├─ Does robots.txt / ToS permit it, and is the content licensed for this use? No → STOP.
      │   └─ Batch ingestion into a corpus:
      │       ├─ Must processing stay in the EU/UK or in your estate?
      │       │   ├─ Yes → Self-host: Crawl4AI (pilot) or Firecrawl server (after AGPL review)
      │       │   └─ No  → Firecrawl Cloud with ZDR (+ PII redaction if any personal data may appear)
      │       └─ Long-tail site with an existing maintained scraper, public data only → Apify
      │
      └─ ENTERPRISE DOCUMENTS
          ├─ Does the source carry permissions (SharePoint, OneDrive, Confluence)?
          │   └─ Yes → Unstructured ingest connectors (ACL digest, reprocess on change),
          │            or build a connector that meets the same contract. Fail closed.
          ├─ May the content leave your estate (classification, client contract, residency)?
          │   ├─ No  → Self-hosted engine: Docling (default); MinerU only after licence review;
          │   │        Mistral OCR self-managed or Reducto on-prem if a commercial engine is needed
          │   └─ Yes, region-bound →
          │        ├─ EU/UK required → Mistral OCR (EU API), LlamaParse EU, Reducto EU endpoint,
          │        │                   Unstructured in-VPC
          │        └─ GCP is the approved cloud → Google Document AI (confirm processor region)
          ├─ Mostly scans or handwriting? → put an OCR engine behind the parser interface;
          │                                 route by confidence score
          └─ Do tables feed numbers anyone will quote?
              └─ Yes → dual-parse + reconciliation; quarantine on mismatch; numbers stay
                       non-authoritative (authoritative figures come from L4 data tools)
```

### 8.10 Lock-in classification

| Class | Where it applies | Rationale | Abstraction to use |
|---|---|---|---|
| **Acceptable** | Docling; the Unstructured open-source library and connectors; OCR engines (Mistral OCR, Document AI OCR) used purely as OCR | Docling is MIT under neutral governance [VF: A1-S057], and Unstructured's library is Apache-2.0 [VF: A1-S011]. An OCR engine's text-plus-coordinates output is easy to swap once a golden set exists [AJ]. | A canonical document model (DoclingDocument or an in-house JSON schema) and an engine adapter interface [Rec] |
| **Manageable** | LlamaParse Parse/Extract; Reducto; Firecrawl Cloud; Unstructured Transform API | All four have proprietary APIs or credit models [VF: A1-S116, A1-S093, A1-S079]. Outputs can be converted into your model, so switching costs a re-parse plus a regression run [AJ]. | The same adapter; store your own copy of every parsed output; keep the parse manifest [Rec] |
| **Unacceptable** | A vendor-managed index (for example LlamaParse Index) as the system of record for entitled content; Apify Actors in core pipelines; MinerU above its thresholds without a commercial licence; a modified Firecrawl server exposed without AGPL compliance | These create regulatory or legal exposure. An index outside your L6 store weakens entitlement and erasure control. Third-party Actors are outside Apify's control [VF: A1-S086]. MinerU rights terminate on breach [VF: A1-S054]. | Keep indexing in your own L6 store; keep licences in the OSS register; scrape only via reviewed code [Rec] |

### 8.11 Regulated FS lens (POV 2)

**Ingestion is where data decisions are made.** Residency, PII classification and entitlements are decided when a document is acquired and parsed; once a document has gone to a third-party parser and been indexed without its ACL, no prompt-level control can undo that [AJ].

**Model risk (SS1/23, SR 26-2).**

- SS1/23 applies to vendor models and is technology-agnostic [VF: R-PRA-SS123; A8-S008]. Its Principle 1.1(b) lets firms apply relevant MRM aspects to material, complex deterministic quantitative methods that are not models [VF: R-PRA-SS123; A8-S061].
- SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly excludes generative and agentic AI. For out-of-scope tools, the firm's own governance applies [VF: R-US-MRM; A8-S001, A8-S002].
- Parsers are not themselves "models" in either definition [AJ]. They are, however, data-preparation components whose errors flow straight into an LLM's inputs. The inventory should record parser and OCR engine versions as dependencies of each AI use case [Rec].

**EU AI Act.**

- Annex III high-risk duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA; A8-S011, A8-S012]. The commentary agent is not an Annex III use case [AJ]. Where a high-risk deployment does arise, Article 26 requires relevant and representative input data where the deployer controls it, and logs kept for at least six months [VF: R-EUAIA; A8-S016, A8-S017, A8-S018].
- Separately, ESMA expects ex-ante input controls and due diligence on third-party AI [VF: R-INTL-AI-ASSETMGMT; A8-S059]. L8 validation and the approved-source register are those controls [AJ].

**Third parties (DORA, PS7/26, SYSC 8).**

- **DORA.** DORA requires a register of information covering all ICT third-party arrangements, and Article 30 contract terms [VF: R-DORA; A8-S021]. For an EU entity, every SaaS parser or crawler is such an arrangement [AJ].
- **Concentration.** The first CTPP list (19 providers) includes hyperscalers such as Google Cloud EMEA Limited, and no AI model provider [VF: R-DORA; A8-S020, A8-S022]. Specialist L8 vendors are therefore overseen only through the firm's own third-party risk management [AJ].
- **UK.** PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8; A8-S062]. A hosted parser that processes client documents for an important business service could be such an arrangement [AJ].
- **FCA FG16/5.** The guidance covers data location, effective access, concentration and exit [VF: R-FCA-SYSC8; A8-S049]. Exit is cheap only if the firm holds its own parsed outputs in an open model [AJ].
- **Due-diligence gap.** Whether vendor SOC 2 reports cover BYOC or self-hosted installs (LlamaParse, Reducto) is not stated [NPV].

**Residency and transfers.**

- Firecrawl's privacy policy places data in the US [VF: A1-S134], and Apify is hosted only in us-east-1 [VF: A1-S086]. For EU or UK personal data, the transfer basis would rest on the EU–US Data Privacy Framework or SCCs, and the DPF appeal C-703/25 P is pending [VF: R-DATA-TRANSFERS; A8-S053, V2-S059].
- EU-resident options exist: the Mistral OCR API, LlamaParse's EU region and Reducto's EU endpoint [VF: A1-S135, A1-S115, A1-S092]. Fully in-estate options also exist: Docling, MinerU and the Unstructured open-source library [VF: A1-S057, A1-S055, A1-S075].

**Auditability and reproducibility.**

- An audit pack has to show which parser version produced each chunk the agent saw [AJ].
- Hosted model retirement removes the ability to re-run a parse. Mistral retired OCR 4.0 on 30 September 2026 [VF: A1-S130].
- Retain parsed outputs, manifests and lineage events for the same period as the commentary record [Rec].

**Standards.**

- **NIST AI 600-1** (final, 26 July 2024) sets out GenAI-specific risks and suggested actions [VF: R-NIST-AIRMF; A8-S044]. Mapping those actions onto ingestion provenance controls is the firm's task [AJ].
- **ISO/IEC 42001** sets requirements for an AI management system [VF: R-ISO-42001; A8-S045]. The ingestion controls above sit inside it [AJ].
- **OWASP.** The operative list is the Top 10 for LLM Applications 2026, which supersedes the 2025 list [VF: R-OWASP-LLM; A8-S041]. Its full contents were not retrieved, so 2026 identifiers are not given here [NPV]. For traceability, the 2025 entries LLM04 Data and Model Poisoning and LLM08 Vector and Embedding Weaknesses are the ones exposed at ingestion [R: R-OWASP-LLM; A8-S040] [AJ]. The Top 10 for Agentic Applications for 2026 lists ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC; A8-S042]; indirect injection through documents an agent reads is one route to it [AJ].
- **IOSCO.** IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT; A8-S058].

### 8.12 Worked-example slice (POV 3)

The performance-attribution commentary agent drafts monthly Brinson-style commentary (allocation, selection, currency) for a generic multi-asset fund. A portfolio manager approves every draft. L8 supplies three corpora [AJ]:

| Corpus | Source class | L8 treatment [Rec] |
|---|---|---|
| Fund factsheets (prior months) | Internal, approved; contains tables | Self-hosted Docling. Dual-parse every performance table and reconcile it against the stored attribution output for that period; quarantine on any mismatch. Tag every numeric cell as `document_derived=true`. |
| Prior commentaries and house style guide | Internal, entitlement-restricted per fund and client | Connector with ACL capture (Unstructured ingest pattern). Chunks carry fund ID, client restrictions and approval status. Draft commentaries are excluded; only approved versions are indexed. |
| Market notes | Third-party research and public sources on the register only | Licence and redistribution terms recorded on the register entry. Web content is acquired in batch by a self-hosted crawler and injection-scanned. No live web fetching by the agent. |

**What the agent needs from L8** [AJ]:
- Retrievable prior commentary with citations back to a specific document version.
- House-style passages that are current, not superseded.
- Market context only from approved sources.
- Enough metadata for the evidence pack (C8) to record which chunks, from which document versions, parsed by which engine versions, were in context.

**What L8 must never do** [Rec]:
- **Supply a number as authoritative.** Every figure in the commentary comes from the attribution engine through read-only L4 tools. Numbers parsed from documents are context only, and the L9 numeric-faithfulness eval checks the draft against the engine output, not against parsed text. A parsing error must never be able to become a published figure.
- **Ingest from a source that is not on the register.** This includes an analyst's ad-hoc upload of a broker note whose licence has not been checked.
- **Index a document without its ACL, or index it as "public" when the permission fetch failed.**
- **Send client-identifying content to a parser outside the approved residency.**
- **Lose the parse manifest.** Without it, last month's draft cannot be reproduced.

### 8.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| One "data extraction" tile row mixing scrapers and parsers | Two distinct jobs, web acquisition and document understanding, plus agent-facing web tools that overlap L4 [VF: A1-S077, A1-S089] | Keep one L8 layer with two sub-layers (acquisition; document understanding) under a shared ingestion control plane; move runtime web access to L4 [Rec] |
| Firecrawl – web to LLM-ready | AGPL server, Cloud-only enterprise controls, US data [VF: A1-S053, A1-S079, A1-S134] | Tactical for public sources [Rec] |
| Docling – doc parser | MIT, LF AI & Data Graduate (August 2026), 2.135.0 [VF: V1-S091, A1-S008] | Strategic default engine and canonical model [Rec] |
| LlamaParse – PDF / documents | Renamed: the whole LlamaIndex platform (formerly LlamaCloud) [VF: A1-S080] | Tactical; Parse/Extract only, indexing kept in-house [Rec] |
| Crawl4AI – open crawler | Pre-1.0; Apache-2.0 plus attribution clause [VF: A1-S009, A1-S056] | Experimental; self-hosted pilots [Rec] |
| MinerU – PDF parser | 4.0, multi-format, custom licence [VF: A1-S055, A1-S054] | Experimental pending licence review [Rec] |
| Reducto – enterprise docs | Proprietary API, vendor-only security evidence [VF: A1-S112] | Tactical after due diligence [Rec] |
| Mistral OCR – OCR | OCR 4.1 (GA 26 August 2026); 4.0 retired 30 September 2026 [VF: A1-S130, V1-S014] | Tactical OCR engine; pin model ID [Rec] |
| Unstructured – ETL for docs | Free OSS plus Transform v2 API; ACL-digest connectors [VF: A1-S075, A1-S094] | Strategic for connectors and entitlement capture [Rec] |
| Apify – scrapers | Actor platform, MCP, US-only [VF: A1-S089, A1-S086] | Tactical; public data only [Rec] |
| (missing) hyperscaler document AI | Google Document AI added; Azure and AWS equivalents not verified [VF: A1-S101] [NPV] | Tactical; strategic only inside a single-cloud estate [Rec] |
| (missing) lineage, classification, PII, entitlements, incremental indexing | Partial in products: Unstructured ACL digest [VF: A1-S094]; Firecrawl PII redaction and ZDR [VF: A1-S076]; no lineage in any L8 product; OpenLineage has no GenAI facets [VF: A7-S042] | A built ingestion control plane (below) [Rec] |

**Hypothesis H7 (provisional; verdict in synthesis).** The evidence supports H7, with one refinement: the enterprise additions are not product features to buy but a control plane to build around replaceable parsers [AJ]. Only partial capabilities exist in products:

- Unstructured captures ACLs and reprocesses on permission change [VF: A1-S094].
- Firecrawl offers PII redaction and ZDR on web content [VF: A1-S076].
- Pinecone, in L6, advertises PII-aware ingestion and lineage in Nexus [VF: A2-S073, A2-S074].
- No L8 product emits lineage [VF: A1-S094, A1-S096].
- OpenLineage has no GenAI-specific facets [VF: A7-S042], so parse, chunk, embed and index steps need custom facets [AJ].

The provisional architecture has six components [Rec]:
1. **Approved-source register.** The single entry point. It records owner, licence or ToS, legal basis, default classification and residency.
2. **Acquisition contract.** Every connector, bought or built, must emit a content hash, source version and ACL snapshot or digest. It must have a distinct "permission unavailable" state that fails closed.
3. **Pre-parse classification and DLP** using a C3 engine (Presidio or a cloud DLP service). This step decides which parsers a document may be routed to.
4. **Parse manifest.** Engine, version, model ID and config hash, stored with the canonical document model output.
5. **Metadata envelope on every chunk**, enforced as an index gate: source, version, ACL principals, classification, PII flags, manifest, and lineage run ID.
6. **Lineage and incremental indexing.** OpenLineage events with custom facets, emitted from the orchestrator (for example the Airflow OpenLineage provider). The index diffs on content hash and ACL digest, and tombstones propagate deletions to L6 and caches.

The open question for synthesis is whether this control plane is an L8 sub-layer or part of C3/C8. The provisional view is that it lives in L8, with policies supplied by C3 and evidence consumed by C8 [AJ].


## 7. Embeddings and reranking

> **Executive summary.** This layer turns text, and now images, audio and PDF pages, into vectors that a retrieval store can search. It then reorders the candidates so that the few passages handed to the model are the right ones. Three things have changed since the original graphic. First, every model vendor in this layer except OpenAI now offers both an embedding model and a reranker: Cohere, Voyage, Jina, NVIDIA and Qwen ship them together, and Google offers a separate Vertex ranking API [VF: A2-S012, A2-S010, A2-S006, A2-S034, A2-S025, A2-S026, A2-S030, A2-S031, A2-S020, B-REV-S026]. Second, two of the graphic's vendors now belong to database companies: Voyage AI to MongoDB since 17 February 2025 [VF: A2-S033, V1-S023], and Jina AI to Elastic since 9 October 2025 [VF: A2-S023, V1-S025]. Third, the stores themselves now host embedding and reranking [VF: A2-S101, A2-S141, A2-S133]. The architectural point that matters most is this: the embedding model version is production configuration, because changing it forces the whole corpus to be re-embedded [AJ]. **Recommendation:** build one governed retrieval-optimisation service that pins the embedding and reranker versions, keeps raw text and model-version metadata, and migrates by dual index. Choose the models by in-domain evaluation. For regulated data, prefer options that run in your own estate or in a verified region [Rec].

### 7.1 Responsibility

**The problem this layer owns** [AJ]:
- **Representation.** Encoding chunks and queries into a vector space in which "similar meaning" means "near". This covers dense vectors and, increasingly, sparse and multi-vector forms.
- **Precision at the top.** Reordering the first-stage candidates with a more expensive model (a cross-encoder or listwise reranker) so that the top 5–10 results are correct.
- **Version discipline.** Making sure every vector in an index came from one known model version with one known configuration (dimensions, quantisation, instructions).

**Hand-offs** [AJ]:

| Direction | Layer | What crosses the boundary |
|---|---|---|
| Below (input) | L8 ingestion | Clean chunks with lineage, classification and access-control metadata. L7 never decides who may see a chunk. |
| Beside | L6 stores | Vectors, sparse terms and metadata are written to the store. At query time the store does filtered first-stage retrieval and fusion. |
| Above | L3 orchestration, L1 models | A short, ranked, entitlement-filtered context list with scores and document identifiers. |
| Across | L9, C5, C8 | Retrieval metrics feed L9. Model and version identifiers are C5 configuration. Retrieved document IDs and scores go into the C8 evidence pack. |

**A boundary that has moved.** The reranker is no longer always an L7 service. MongoDB runs Voyage cross-encoders inside an aggregation stage (`$rerank`, public preview, 8.3+) [VF: A2-S141]. Pinecone hosts its own reranker, Cohere Rerank 3.5 and bge-reranker-v2-m3 [VF: A2-S101]. Elastic's `semantic_text` field embeds automatically and defaults to Jina v5 [VF: A2-S133]. The responsibility still belongs to L7 even when the compute runs in L6: someone must own the model choice, the version pin and the evaluation [AJ].

### 7.2 Why it matters

**What breaks when this layer is badly designed** [AJ]:

- **Silent relevance decay.** The system still returns something, so nobody notices it is wrong.
- **Mixed-version indexes.** Scores from two model versions are not comparable; quality drops without an error.
- **Unplanned re-embedding.** A model is retired or replaced and the corpus must be re-processed under time pressure.
- **Entitlement leakage through ranking.** A reranker will promote another client's document if unfiltered candidates reach it.
- **Cost surprises.** Full-precision 3,072-dimension vectors held in memory across a large corpus. Cohere's own worked example shows 100M chunks shrinking from about 819 GB to 3.2 GB once reduced dimensions and binary output are used [VF: A2-S013].

**Illustrative scenario [AJ].** A platform team upgrades its embedding model on a Friday, applying the new model to the ingestion pipeline and to the query path. Nobody re-embeds the existing 4 million chunks. New documents land in the new vector space; old documents remain in the old one. Queries are now embedded with the new model and compared against mostly old vectors. Nothing errors. Over the next fortnight the commentary assistant starts citing last month's market notes and missing the house style guide, which has not changed since the spring. The defect is found only when an analyst asks why the draft quotes a superseded style rule. Nothing records which model produced which vectors, so the team cannot tell which documents are affected and has to rebuild the whole index. The controls that would have stopped it are a model-version tag on every vector, a query path that refuses to mix versions, and a retrieval regression suite in L9 run on every configuration change.

### 7.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Recall@k (first stage) | Share of golden-set queries whose relevant chunk appears in the top k candidates (k = 50–100) | ≥ 0.95 on the in-domain golden set | L9 offline evaluation on a labelled query set, on every model or config change |
| nDCG@10 / precision@5 (after rerank) | Ranking quality of the final context list | Agreed baseline; no regression > 2 points on release | Same golden set, graded relevance labels |
| Entitlement-violation rate | Retrieved items the requester is not entitled to see | 0, as a hard gate | Synthetic cross-tenant probe queries in CI and production canaries |
| Version consistency | Share of vectors in a live index carrying the index's declared model-version tag | 100% | Index metadata audit job |
| p95 query-embedding latency | Time to embed one query | < 100 ms in-region | Gateway or service traces (OTel spans) |
| p95 rerank latency | Time to rerank the candidate set | < 300 ms for 50 candidates | Service traces; alert on breach |
| Cost per 1,000 queries | Embedding plus rerank cost | Tracked and budgeted per use case | C6 FinOps attribution |
| Full re-embed time | Wall-clock time to re-embed the corpus into a shadow index | Inside the agreed change window; tested twice a year | Dry-run migration |
| Multilingual parity gap | Recall gap between English and other in-scope languages | ≤ 5 points | Golden set stratified by language |

The targets are starting points for a firm to calibrate. They are not industry benchmarks [AJ].

### 7.4 How it works

**Two paths share one model configuration.** At ingestion, each chunk is embedded (dense) and, where used, encoded as sparse terms. Both are written to the store with metadata: source, classification, entitlements, model version and chunk hash. At query time the query is embedded with the same model version. The store runs a filtered dense search and a lexical (BM25) or sparse search, fuses the two lists, and passes the top candidates to a reranker that reads query and passage together [AJ].

```text
INGESTION (L8 -> L7 -> L6)
 chunk + lineage + ACL metadata
   -> embedding service [model=X, version=v3, dims=1024, quant=int8]
   -> dense vector + sparse terms + {model_version, chunk_hash, acl, fund_id}
   -> store index "commentary_v3"          (raw text retained)
QUERY (L3 -> L7/L6 -> L3)
 query + caller identity
   -> embed query with SAME model_version as target index
   -> L6: entitlement filter FIRST (acl, fund_id, client_id)
        -> dense ANN top-100  +  BM25/sparse top-100
        -> fuse (RRF or weighted)
   -> reranker [model=R, version=r2] on top-50 (already filtered)
   -> top-5..10 with doc_id, scores, versions  -> L3 / L1
   -> trace to L9 and the C8 evidence pack
```

**The mechanics that matter for decisions:**

- **Bi-encoder vs cross-encoder.** An embedding model encodes query and document separately, so documents can be pre-computed. That is fast, but it is coarse [AJ]. A reranker reads the query and each candidate together. That is slower, but more precise, which is why it is applied only to a short candidate list [AJ]. Current rerankers take long inputs: Cohere Rerank 4 handles 32K tokens and JSON documents [VF: A2-S009], and Voyage rerank-3 has a 32K-token context [VF: A2-S034]. Jina reranker v3.5 is listwise, scoring candidates jointly [VF: A2-S026].
- **Sparse plus dense.** Lexical matching catches exact identifiers that dense vectors blur: fund codes, ISINs, share-class names [AJ]. Fusion is now a store feature: Qdrant weighted RRF [VF: A2-S103], Elasticsearch RRF and linear retrievers [VF: A2-S133], MongoDB `$rankFusion`/`$scoreFusion` [VF: A2-S141], Pinecone "cascading retrieval" [VF: A2-S101] and pgvector `sparsevec` [VF: A2-S063]. Sentence Transformers trains Sparse Encoders [VF: A2-S029].
- **Evidence for the two-stage pattern.** Anthropic reports that contextual embeddings plus contextual BM25 cut top-20 retrieval failures by 49%, and that adding a reranker raised the cut to 67% [R: A2-S070]. The author is an Anthropic model, so this is one vendor's measurement on its own data. It shows direction, not a decision input [AJ].
- **Matryoshka dimensions and quantisation.** Several models let you truncate vectors and lower precision with a controlled loss:
  - Gemini Embedding 2: 128–3,072 dims [VF: A2-S005]
  - Cohere Embed 5: 256–2,048 dims; float, int8 and binary [VF: A2-S012]
  - voyage-4: 256–2,048 dims, with binary among its quantisation options [VF: A2-S007, A2-S006]
  - Qwen's hosted model: 64–2,048 dims [VF: A2-S022]
  - OpenAI: a `dimensions` parameter [VF: A2-S001]

  Stores quantise as well: Elasticsearch uses BBQ quantisation by default since 9.1 [VF: A2-S133]. Dimension and precision are therefore index-design parameters, and they must be recorded with the model version [AJ].
- **Shared embedding spaces.** Voyage 4 [VF: A2-S006], Cohere Embed 5 Pro/Fast [VF: A2-S012] and Jina v5-omni and v5-text [VF: A2-S025] put several model sizes in one space. You can index with the large model and query with the small one. This reduces re-embedding inside a family; it does nothing for a move between vendors [AJ].
- **Contextualised chunks and late interaction.** voyage-context-4 embeds a chunk with awareness of its surrounding document [VF: A2-S007]. Sentence Transformers v6 added a Multi-Vector Encoder for ColBERT-style late interaction [VF: A2-S029, A2-S028]. ColPali-style page-image retrieval was not evidenced in this research [NPV].
- **Multimodal.** Gemini Embedding 2 [VF: A2-S004], Jina v5-omni [VF: A2-S025], Cohere Embed 5 [VF: A2-S012], voyage-multimodal-3.5 [VF: A2-S007], NVIDIA VL models [VF: A2-S031] and Qwen3-VL [VF: A2-S021] embed images alongside text. This matters for scanned factsheets and charts; text-first corpora gain little [AJ].
- **Benchmarks.** The MTEB results repository was still maintained on 21 September 2026 [VF: A2-S046]. The live leaderboard could not be fetched, so this section asserts no current ranking [NPV]. Vendor scores quoted anywhere in this section are [R] and are not decision inputs.

### 7.5 Enterprise design principles

**Security** [AJ]
- Embeddings derived from client or personal data are a derivative of that data. Classify, retain and delete them with the source.
- Enforce entitlements in the store's pre-filter, before ANN search, fusion and reranking. Never post-filter after the reranker, and never rely on the reranker to "down-rank" forbidden content.
- The operative reference is the OWASP Top 10 for LLM Applications 2026 [VF: A8-S041]. Its full contents were not retrieved, so its identifier for this risk is not given [NPV]. For traceability, the 2025 list named it LLM08 "Vector and Embedding Weaknesses" [R: A8-S040].

**Scalability and cost** [AJ]
- Choose dimensions and quantisation per index tier, by measurement.
- Batch ingestion through Batch APIs where offered. OpenAI's Batch API halves the 3-large price, and Gemini's Batch is 50% of standard [VF: A2-S035, A2-S005].
- Cap the rerank candidate count (typically 25–100) and measure the recall it buys.

**Resilience** [AJ]
- Hosted embedding APIs are on the query path. An outage stops retrieval even if the store is healthy.
- Keep a warm fallback route for the same model, such as a second region or a marketplace deployment, or degrade to lexical search.
- Never fall back to a *different* embedding model against the same index.

**Governance and change** [Rec]
- Treat `{embedding model, version, dims, quantisation, instruction prefix}` and `{reranker model, version, candidate k}` as versioned C5 configuration, promoted through environments with an L9 regression gate.
- Write the configuration hash into every vector's metadata and every trace.

**Observability** [Rec]
- Emit spans for embed, retrieval, fusion and rerank with model version, latency and top document IDs.

**Portability** [Rec]
- Always store the raw chunk text and its hash next to the vector, so you can re-embed without re-parsing.
- Put an internal embedding-service interface in front of every provider.

**Patterns**

| Pattern | Use |
|---|---|
| Dual-index migration (blue/green) [Rec] | Build `index_v4` in shadow from stored raw text. Run both, compare on the golden set and on shadow traffic, switch the read alias, keep `index_v3` until the rollback window closes. |
| Hybrid first stage + cross-encoder rerank [Rec] | Default for enterprise text. Lexical catches identifiers; dense catches paraphrase; the reranker fixes the order. |
| Index-large / query-small in a shared space [AJ] | Cuts query latency and cost within one vendor family. |
| Domain fine-tune of an open model [AJ] | Use Sentence Transformers to adapt an Apache-2.0 model on in-domain pairs when vendor models underperform on house vocabulary [VF: A2-S029]. |

**Anti-patterns** [AJ]
- Mixing model versions in one index.
- Selecting a model from a leaderboard instead of an in-domain test.
- Post-rerank entitlement filtering.
- Letting a store auto-embed with a default model nobody pinned.
- Discarding raw text after embedding.
- Treating rerank scores as calibrated probabilities across queries.

**What re-embedding actually costs.** The API bill is the small part. A corpus of 2 million chunks at about 500 tokens each is roughly 1 billion tokens. At list prices as of 7 October 2026 that is about US$130 with OpenAI text-embedding-3-large, about US$60 with voyage-4, or about US$120 with Cohere Embed 5 Pro [VF: A2-S001, A2-S007, A2-S013]. The arithmetic is the author's own [AJ]. The real costs are elsewhere [AJ]:
- running a second index in parallel
- re-running the retrieval evaluation and any downstream answer-quality evaluation
- revalidation and change-control evidence
- the migration window

This is why model version belongs in production configuration and in the exit plan.

### 7.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical capability | Recall and nDCG on **your** golden set, in your languages and document types; reranker availability; Matryoshka and quantisation; context length; sparse, multi-vector and multimodal support; domain models |
| Enterprise readiness | SSO, RBAC and audit logs for the console and API keys; per-project keys; usage reporting; support and model-retirement notice periods (ask for them in writing) |
| Security and compliance | SOC 2 Type II and ISO 27001 scope covering the **embedding endpoint**; ZDR; CMK; DPA; sub-processors |
| Deployment flexibility | In-region processing (UK and EU separately); VPC or marketplace deployment; self-hosting and air-gap |
| Ecosystem | Native support in your L6 store; Sentence Transformers or vLLM compatibility for open models; marketplace availability |
| Reliability and maturity | GA vs preview status; deprecation policy; model-retirement history; ownership stability |
| Cost / TCO | Per-token price, Batch discount, rerank pricing basis (per search or per token), GPU and licence cost if self-hosted, storage effect of dimensions |
| Lock-in / portability | Weights availability and licence; shared-space families; store bundling; re-embedding cost |

**Enterprise controls for hosted embedding APIs are unevenly documented.** The CP2 review found SSO, RBAC and audit-log documentation for the OpenAI API platform [VF: B-REV-S004, B-REV-S005, B-REV-S006], IAM and audit logging on Google Cloud [VF: B-REV-S007, B-REV-S008], and SSO and RBAC on Elastic Cloud for the Elastic Inference Service route [VF: B-REV-S019]. Cohere documents only Owner and User team roles for its hosted platform [VF: B-REV-S013], and Voyage's Atlas API is accessed by model API keys with no access-control documentation found [VF: B-REV-S018]. Both therefore stay capped at 2 [AJ]. These controls usually come from the platform account already contracted for L1, so verify them per endpoint in due diligence [Rec].

### 7.7 Product deep dives

Each deep dive gives the current state as tagged facts, then judgement. Totals are FS-weighted.

#### OpenAI embeddings (text-embedding-3-large / -3-small)

**What it is.** OpenAI's embeddings are still the text-embedding-3 generation, released 25 January 2024; no newer model was found as of 7 October 2026 [VF: A2-S001, A2-S002]. 3-large defaults to 3,072 dimensions, can be shortened with `dimensions`, and accepts 8,192 tokens [VF: A2-S001, A2-S003]. Prices are US$0.13 per 1M tokens for 3-large (US$0.065 on Batch) and US$0.02 for 3-small [VF: A2-S001, A2-S035]. The endpoint is ZDR-eligible and in scope for EU storage and processing, which requires Modified Abuse Monitoring or ZDR; the UK is storage-only [VF: A2-S144]. Certifications include SOC 2 Type 2, ISO/IEC 27001 and 27701, and a HIPAA BAA [VF: A2-S036, A2-S144]. No OpenAI reranker was found [VF: A2-S001]. The API platform documents SAML/OIDC SSO, SCIM, organisation and project roles with custom roles, an Admin API and audit logs of administrative events [VF: B-REV-S004, B-REV-S005, B-REV-S006].

**Strengths.** A stable, cheap, well-controlled text baseline [AJ].

**Limitations and risks.** It is text-only, hosted-only and has no reranker. The generation is ageing, and its successor's timing is unknown [AJ]. Audit logs exclude request content and are kept on a best-effort basis [VF: B-REV-S006], so they must be exported to the firm's archive [Rec].

**Choose when** OpenAI is already the approved L1 provider and EU processing under ZDR suffices. **Avoid when** UK processing or self-hosting is required.

**Nearest competitors:** Gemini Embedding, Cohere, Voyage.

**FS note.** Exit means re-embedding everything [AJ].

**Tier:** Tactical; no flags (FS 3.20).

#### Gemini Embedding 2 (Google)

**What it is.** gemini-embedding-2 went GA on 22 April 2026 [VF: A2-S004]. It maps text, images, video, audio and PDFs into one space across 100+ languages, with Matryoshka output from 128 to 3,072 dims [VF: A2-S004, A2-S005]. It runs on the Gemini API and on Vertex AI, now documented as Gemini Enterprise Agent Platform, with global, us and eu endpoints [VF: A2-S039]. The eu multi-region excludes the UK and Switzerland [VF: A2-S039]. Generative AI on Vertex AI holds SOC 2, ISO/IEC 27001, ISO/IEC 42001, HIPAA and FedRAMP High, but per-model coverage is not confirmed [VF: A2-S043]. Text costs US$0.20 per 1M tokens online and US$0.10 on Batch (as of 7 October 2026) [VF: A2-S038]. Access runs through Google Cloud IAM (predefined, custom and endpoint-level roles) and Cloud Audit Logs, where Data Access logs for predict calls must be switched on [VF: B-REV-S007, B-REV-S008].

**Strengths.** A natively multimodal option with strong platform certifications [AJ].

**Limitations and risks.** It is hosted-only and has been GA for under six months. The `task_type` parameter is unsupported [VF: A2-S005]. Google's reranker is a separate service, the Vertex ranking API (semantic-ranker models, with version 005 in preview from 1 September 2026) [VF: B-REV-S026].

**Choose when** the estate is Google Cloud-centred and the content is multimodal. **Avoid when** UK-only processing is mandatory.

**Nearest competitors:** Cohere, Voyage, Jina.

**FS note.** Google Cloud EMEA Limited is a designated DORA CTPP and UK CTP [VF: A8-S020, A8-S023]. Consuming the model through Vertex AI therefore places it with a designated provider, but the firm's own SYSC 8 or SS2/21 duties remain [AJ].

**Tier:** Tactical; no flags (FS 3.05).

#### Voyage AI by MongoDB

**What it is.** MongoDB acquired Voyage AI, closing on 17 February 2025 for US$160.9M [VF: A2-S033, V1-S023]. The Voyage 4 family launched on 15 January 2026 in one shared embedding space; voyage-4-nano is open weights under Apache 2.0 [VF: A2-S006, A2-S071]. Alongside it sit voyage-context-4, voyage-code-4, voyage-multimodal-3.5, and the domain models voyage-finance-2 and voyage-law-2 [VF: A2-S007]. rerank-3 and rerank-3-lite were announced on 30 September 2026 [VF: A2-S034], but MongoDB's lifecycle page lists them as Preview [VF: V1-S024]. voyage-4 costs US$0.06 per 1M tokens, rerank-3 US$0.05 and rerank-3-lite US$0.02 (as of 7 October 2026) [VF: A2-S007, A2-S034]. The Atlas Embedding and Reranking API offers an EEA Geography at a 10% premium [VF: A2-S142]. Certifications rest on a homepage listing [R: A2-S044]. MongoDB's SOC 2 scope page does not name Voyage and excludes preview features [VF: B-REV-S027].

**Strengths.** A broad lineup against this layer's questions, including a finance-domain model [AJ].

**Limitations and risks.** Certification scope is unverified, key integrations are in preview, and the roadmap is now coupled to MongoDB [AJ].

**Choose when** MongoDB is the store. **Avoid when** the firm needs the store vendor and the embedding vendor to be different companies.

**Nearest competitors:** Cohere, Jina, Qwen3.

**FS note.** Obtain the SOC 2 report before client data flows [Rec].

**Tier:** Tactical; flag Acquired (FS 2.90).

#### Cohere Embed 5 and Rerank 4

**What it is.** Embed 5 (Pro and Fast, 30 September 2026) embeds text, images and mixed pages into one vector [VF: A2-S012]. It supports 100+ languages and a 128K-token context, with 256–2,048 dims and float, int8 or binary output [VF: A2-S012]. Rerank 4 (11 December 2025) adds a 32K-token context and handles JSON [VF: A2-S010, A2-S009]. Deployment options are SaaS, Microsoft Foundry, SageMaker, VPC, Model Vault single-tenant and on-premises [VF: A2-S012, A2-S015]. Cohere holds SOC 2 Type II, ISO 27001 and ISO 42001 [VF: A2-S014]. Enterprise logs are deleted after 30 days by default, and ZDR is available on request [VF: A2-S145]. The hosted platform documents only Owner and User team roles [VF: B-REV-S013]; SSO/SAML and audit-log documentation for the hosted API was not found [NPV]. Embed 5 Pro costs US$0.12 and Fast US$0.08 per 1M text tokens; the rerank price was not found [VF: A2-S013]. A business combination with Aleph Alpha was signed on 16 September 2026 and is pending regulatory approval [VF: A2-S018, V1-S028].

**Strengths.** The widest deployment range of the hosted vendors here, from SaaS to on-premises [AJ].

**Limitations and risks.** Hosted access controls are unverified, and the ownership event is pending [AJ].

**Choose when** embed and rerank must run in your VPC or data centre with vendor support. **Avoid when** you cannot obtain access-control evidence in due diligence [AJ].

**Nearest competitors:** Voyage, Jina, NVIDIA.

**FS note.** Cohere states it has no access to prompts in private or partner deployments [VF: A2-S145]. Record the Aleph Alpha approval as an ownership event in the third-party register [Rec].

**Tier:** Tactical; no flags (FS 3.40). It is a candidate for Strategic once due diligence closes the access-control gap [AJ].

#### Qwen3-Embedding and Qwen3-Reranker (Alibaba)

**What it is.** Qwen3-Embedding and Qwen3-Reranker come in 0.6B, 4B and 8B sizes [VF: A2-S020]. They were released in June 2025 under Apache 2.0, with a 32K context and 119 languages [VF: A2-S020]. Qwen3-VL-Embedding and -Reranker followed in January 2026 [VF: A2-S021, V1-S093]. Hosted versions run on Alibaba Cloud Model Studio, where the regions listed are Singapore, Hong Kong and Beijing; no EU region was verified [VF: A2-S022]. Qwen's June 2025 claim that the 8B model ranked first on MTEB multilingual is vendor-reported and was not re-verified [R: A2-S020].

**Strengths.** A permissive embed-plus-rerank pair that can run entirely inside the firm's estate [AJ].

**Limitations and risks.** It is a Chinese-origin model. No support or certifications are verified, and the 8B size needs GPUs [AJ].

**Choose when** self-hosting is required and a provenance review approves it. **Avoid when** policy excludes such weights, or only the hosted API would be used.

**Nearest competitors:** Sentence Transformers with other open models, NVIDIA, Jina.

**FS note.** Self-hosted, the weights create no cross-border transfer. The hosted route is not suitable for EU or UK client data on the verified regions [AJ].

**Tier:** Tactical; no flags (FS 3.15). Scored under rubric rule 2 as self-hosted weights, because the hosted route is not recommended [AJ].

#### Jina AI (part of Elastic)

**What it is.** Elastic completed its acquisition of Jina AI on 9 October 2025 [VF: A2-S023, V1-S025]. The current models are [VF: A2-S025, A2-S026, V1-S026]:
- jina-embeddings-v5-text (February 2026; 32,768-token context)
- jina-embeddings-v5-omni (May 2026; text, image, audio, video and PDF, with text vectors identical to v5-text)
- jina-reranker-v3.5 (July 2026)

Weights are CC-BY-NC-4.0. Commercial use runs through the Jina API, marketplaces, Elastic Inference Service or an on-premises licence, which supports air-gapped Docker [VF: A2-S024, A2-S042, A2-S045]. `semantic_text` defaults to Jina v5 [VF: A2-S133]. Elastic Cloud holds ISO 27001 and SOC 2 Type II; whether the hosted Jina API is in scope is not confirmed [VF: A2-S045]. Elastic Cloud documents SAML SSO and RBAC at platform level; whether they govern EIS calls specifically is not stated [VF: B-REV-S019]. API per-token rates were not retrieved [VF: A2-S042].

**Strengths.** The zero-integration path inside Elasticsearch, with multimodal and air-gap options [AJ].

**Limitations and risks.** The licence is non-commercial. Pricing is opaque, and the ownership change ties it to Elastic [AJ].

**Choose when** Elastic is the store. **Avoid when** the plan assumes free self-hosting of the weights.

**Nearest competitors:** Voyage, Cohere, Qwen3.

**FS note.** Get the licence route confirmed in writing [Rec].

**Tier:** Tactical; flag Acquired (FS 3.15, scored on the Elastic Inference Service route).

#### Sentence Transformers (Hugging Face)

**What it is.** sentence-transformers 6.1.0 was released on 18 September 2026 under Apache-2.0 [VF: A2-S029, A2-S032]. It is maintained by Hugging Face and originated at UKP Lab [VF: A2-S028, V1-S092]. It computes and trains [VF: A2-S029]:
- dense embeddings
- Cross-Encoder reranker scores
- Sparse Encoders
- ColBERT-style Multi-Vector Encoders

More than 15,000 pre-trained models on Hugging Face load through it [VF: A2-S029].

**Strengths.** One permissive toolkit for every technique in this layer, and the practical route to domain fine-tuning and to exit from any hosted API [AJ].

**Limitations and risks.** It is a library, not a model, and it has no verified commercial support [NPV]. It publishes a security policy with private reporting and CVE issuance through GitHub advisories [VF: B-REV-S002]. Each Hub model carries its own licence [AJ].

**Choose when** retrieval must run in the firm's estate, or needs fine-tuning. **Avoid when** there is no team to operate serving.

**Nearest competitors:** NVIDIA NeMo Retriever, Qwen3, Cohere private deployment.

**FS note.** It inherits host controls [AJ].

**Tier:** Strategic; no flags (FS 3.70). Rule 2 caps were applied.

#### NVIDIA NeMo Retriever embedding and reranking NIMs

**What it is.** The graphic's "NVIDIA – Embed" tile is now the set of NeMo Retriever NIM microservices [VF: A2-S030, A2-S031]:

- Embedding NIM 2.3, with nemotron-3-embed-1b (added in 2.2) and the llama-nemotron-embed text and VL models [VF: A2-S031, V1-S094]
- Reranking NIM 2.0.0, with text and multimodal rerankers [VF: A2-S030]

They deploy via Helm or Docker on supported GPUs, in any cloud or data centre [VF: A2-S031, A2-S040]. Production use requires NVIDIA AI Enterprise, from US$4,500 per GPU per year (as of 7 October 2026) [VF: A2-S040]. Model licences vary by model [VF: A2-S041]. The Helm chart warns that a text-only reranker silently degrades multimodal reranking [VF: A2-S031].

**Strengths.** A supported, self-hosted runtime for embed and rerank [AJ].

**Limitations and risks.** It deepens GPU-vendor coupling, and per-GPU licences make it expensive at low volume [AJ].

**Choose when** the firm already runs NVIDIA AI Enterprise. **Avoid when** retrieval volume is small.

**Nearest competitors:** Sentence Transformers, Qwen3, Cohere private deployment.

**FS note.** Self-hosting keeps the retrieval path in-estate; the AI Enterprise subscription becomes the third-party arrangement to register [AJ].

**Tier:** Tactical; flag Renamed (FS 2.95).

### 7.8 Comparison table

Output of `tools/score.py` (scores 1–5; totals are weighted averages):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7-openai | 3 | 4 | 4 | 2 | 3 | 4 | 4 | 2 | 3.30 | 3.20 | Tactical |
| L7-gemini-embedding | 4 | 3 | 4 | 2 | 3 | 3 | 3 | 2 | 3.15 | 3.05 | Tactical |
| L7-voyage | 5 | 2 | 2 | 3 | 4 | 3 | 4 | 2 | 3.25 | 2.90 | Tactical |
| L7-cohere | 4 | 2 | 4 | 4 | 4 | 3 | 3 | 3 | 3.45 | 3.40 | Tactical |
| L7-qwen3-embedding | 4 | 2 | 2 | 4 | 3 | 3 | 4 | 4 | 3.20 | 3.15 | Tactical |
| L7-jina | 4 | 3 | 3 | 4 | 4 | 3 | 2 | 2 | 3.30 | 3.15 | Tactical |
| L7-sentence-transformers | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 3.80 | 3.70 | Strategic |
| L7-nvidia-nemo-retriever | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 2 | 3.00 | 2.95 | Tactical |
| L7-ethicalagents | – | – | – | – | – | – | – | – | n/a | n/a | not scored |
| L7-ragoos | – | – | – | – | – | – | – | – | n/a | n/a | not scored |

**Reading the scores** [AJ]:
- The hosted vendors spread from 2.90 to 3.40 FS. OpenAI (3.20), Gemini (3.05) and Jina (3.15, Elastic route) rose at CP2 review once their platform access controls were evidenced; Cohere and Voyage stay capped on enterprise readiness.
- The spread on security (2 to 4) reflects how well certifications are evidenced, not a judgement of real security posture.
- Voyage's technical lead does not survive the FS weighting until its certification scope is evidenced.
- Qwen3 and NVIDIA are scored as self-hosted software under rule 2, like Sentence Transformers.

**Key facts** (as of 7 October 2026):

| Product | Licence | Deployment | Certifications | EU residency | Ownership status |
|---|---|---|---|---|---|
| OpenAI | Proprietary, hosted only [VF: A2-S001] | SaaS [VF: A2-S001] | SOC 2 Type 2, ISO 27001/27701, HIPAA BAA [VF: A2-S036, A2-S144] | EU storage and processing with MAM or ZDR; UK storage-only [VF: A2-S144] | Unchanged |
| Gemini Embedding 2 | Proprietary, hosted only [VF: A2-S004] | Gemini API, Vertex AI [VF: A2-S039] | Vertex GenAI: SOC 2, ISO 27001, ISO 42001, HIPAA, FedRAMP High; per-model scope unconfirmed [VF: A2-S043] | 'eu' multi-region, excludes UK and CH [VF: A2-S039] | Unchanged (Google) |
| Voyage AI | Proprietary; voyage-4-nano Apache 2.0 [VF: A2-S071] | SaaS, Atlas, AWS/Azure marketplaces, in-VPC SageMaker [VF: A2-S033, A2-S044] | SOC 2, HIPAA listed on homepage [R: A2-S044] | Atlas EEA Geography, +10% [VF: A2-S142] | Acquired by MongoDB, 17 Feb 2025 [VF: A2-S033] |
| Cohere | Proprietary [VF: A2-S015] | SaaS, Foundry, SageMaker, VPC, Model Vault, on-prem [VF: A2-S012, A2-S015] | SOC 2 Type II, ISO 27001, ISO 42001 [VF: A2-S014] | 30-day default deletion, ZDR on request; EU region not verified [VF: A2-S145] | Aleph Alpha combination signed 16 Sep 2026, pending [VF: A2-S018] |
| Qwen3 Embedding/Reranker | Apache 2.0 weights; hosted proprietary [VF: A2-S020] | Self-host; Model Studio [VF: A2-S020, A2-S022] | Not publicly verified [NPV] | No EU hosted region verified; self-host in-estate [VF: A2-S022] | Unchanged (Alibaba) |
| Jina AI | CC-BY-NC-4.0 weights; commercial via Elastic [VF: A2-S024, A2-S042] | API, Elastic Inference Service, on-prem/air-gap [VF: A2-S042] | Elastic Cloud ISO 27001, SOC 2 Type II; Jina API scope unconfirmed [VF: A2-S045] | Region details not verified [VF: A2-S024] | Acquired by Elastic, 9 Oct 2025 [VF: V1-S025] |
| Sentence Transformers | Apache-2.0 [VF: A2-S029] | Self-host, on-prem [VF: A2-S029] | Not applicable (library) [AJ] | In-estate [AJ] | Stewardship moved to Hugging Face [VF: A2-S028] |
| NVIDIA NeMo Retriever | Proprietary container plus per-model licences [VF: A2-S041] | Self-host on supported GPUs; NVIDIA API Catalog for development [VF: A2-S040, A2-S031] | Not applicable to self-hosted containers [AJ] | In-estate [AJ] | Unchanged (NVIDIA) |

### 7.9 Decision tree

```text
START: a corpus to make retrievable (one decision per corpus / index)
1. Does the corpus contain client, personal or confidential data?
   ├─ No  → go to 3 (any approved hosted API is acceptable)
   └─ Yes → 2
2. Where may it be processed?
   ├─ Only inside our estate (or air-gapped)
   │    ├─ Need vendor support?
   │    │    ├─ Yes, NVIDIA AI Enterprise already licensed → NVIDIA NeMo Retriever NIMs
   │    │    ├─ Yes, otherwise → Cohere private / on-prem deployment
   │    │    │                   (or Jina on-prem licence if Elastic is the store)
   │    │    └─ No → Sentence Transformers serving an Apache-2.0 model
   │    │            (Qwen3 only after provenance review; voyage-4-nano is another option)
   ├─ UK processing required
   │    └─ None of the hosted APIs here verified UK processing for embeddings
   │       → treat as "own estate" (above) or a VPC/marketplace deployment in a UK
   │         region (Cohere on SageMaker/Foundry, Voyage on SageMaker); confirm the region
   └─ EU processing acceptable
        ├─ Store is MongoDB → Voyage via Atlas EEA Geography (accept preview status,
        │                    obtain the SOC 2 report)
        ├─ Store is Elasticsearch → Jina via Elastic Inference Service (pin the model)
        ├─ Google-centred estate, multimodal → Gemini Embedding 2 on the 'eu' endpoint
        ├─ OpenAI already approved, text-only → text-embedding-3 on an EU project with ZDR
        └─ Otherwise → Cohere (SaaS with ZDR, or VPC)
3. Do we need a reranker? (almost always yes for precision-critical answers)
   ├─ Same vendor offers one and it passes in-domain eval → use it
   ├─ Embedding vendor has none in the same API (OpenAI; Google's is the Vertex ranking API)
   │    → Cohere Rerank 4, Voyage rerank-3 (Preview), or a self-hosted cross-encoder
   └─ Store hosts it (MongoDB $rerank, Pinecone, Elastic) → acceptable if the
        model version is pinned and logged, and entitlement filtering precedes it
4. Exact identifiers matter (fund codes, ISINs, share classes)?
   └─ Yes → hybrid first stage (BM25/sparse + dense, fused) before rerank
5. Scanned pages, charts or images matter?
   └─ Yes → multimodal model (Gemini Embedding 2, Cohere Embed 5, Jina v5-omni,
            voyage-multimodal-3.5, NVIDIA VL), chosen by in-domain eval
6. Always: pin versions in C5, keep raw text, tag vectors with model_version,
   and migrate by dual index behind an L9 regression gate.
```

### 7.10 Lock-in classification

| Lock-in source | Class | Rationale | Abstraction to use |
|---|---|---|---|
| Reranker choice | **Acceptable** [AJ] | Stateless and applied at query time. Swapping it needs no re-index, only re-evaluation. | Internal `rerank(query, candidates)` interface; reranker version in C5 |
| Embedding model (hosted, proprietary) | **Manageable** [AJ] | Vectors are model-specific, so switching means re-embedding [AJ]. The API bill for that is small; evaluation and revalidation are the real cost (§7.5). | Internal embedding service; raw text stored; `model_version` on every vector; dual-index migration runbook tested twice a year [Rec] |
| Shared-space families (Voyage 4, Cohere Embed 5, Jina v5) | **Manageable** [AJ] | They reduce re-embedding inside the family [VF: A2-S006, A2-S012, A2-S025], but deepen commitment to one vendor. | Same as above; treat the family as one supplier in the exit plan |
| Store-bundled embedding and reranking (MongoDB Automated Embedding and `$rerank`, Elastic `semantic_text`, Pinecone integrated inference) | **Manageable**, becoming **unacceptable** if the model is unpinned or raw text is not retained [AJ] | Store and embedding model then change together, so leaving the store also means re-embedding. MongoDB's native reranking and automated embedding are still preview and do not yet support Geography targeting [VF: A2-S141, A2-S142]. | Pin the model explicitly; retain raw text outside the store; export path tested |
| Non-commercial weights self-hosted without a licence (Jina CC-BY-NC-4.0) | **Unacceptable** [AJ] | Licence breach risk [VF: A2-S024]. | Use the licensed routes, or choose an Apache-2.0 model |
| GPU-vendor runtime (NVIDIA AI Enterprise) | **Manageable** [AJ] | The runtime ties retrieval to the licence [VF: A2-S040]. Open-licensed models can move to another runtime, but per-model licences vary [VF: A2-S041]. | Serve behind the same internal interface; keep a Sentence Transformers or vLLM fallback |

### 7.11 Regulated FS lens (POV 2)

**Model risk.** SR 26-2 superseded SR 11-7 on 17 April 2026, and it expressly excludes generative and agentic AI. Firms are left to govern those under their own frameworks (R-US-MRM) [VF: A8-S001, A8-S002, A8-S003]. PRA SS1/23 is the operative UK anchor where it applies. It covers vendor models and requires a complete inventory that includes AI/ML (R-PRA-SS123) [VF: A8-S008]. For this layer [AJ]:
- Record the embedding model and the reranker in the inventory as components of each GenAI system, not as stand-alone "models".
- Treat a change to either as a material change that triggers the L9 retrieval regression and sign-off.
- Retrieval quality is part of the system's validation evidence. An unvalidated embedding swap is an unvalidated system change.

**EU AI Act.** Annex III high-risk duties apply from 2 December 2027 under Regulation (EU) 2026/1744, and GPAI obligations have been enforceable since 2 August 2026 (R-EUAIA, R-EU-OMNIBUS-AI) [VF: A8-S011, A8-S012]. The worked example is not an Annex III use, and a firm consuming embedding APIs is a deployer [AJ]. Whether any embedding model is itself a GPAI model was not established [NPV]. Article 26 deployer logging folds into financial-services record-keeping (R-EUAIA) [VF: A8-S016]; logging the retrieval step is good practice regardless [AJ].

**DORA, CTP and outsourcing.**

- DORA's first CTPP list (18 November 2025) and the UK's first CTP designations (8 July 2026) cover hyperscalers, but no model vendor (R-DORA, R-UK-CTP) [VF: A8-S020, A8-S021, A8-S023, A8-S024].
- An embedding API consumed through Vertex AI, or a marketplace deployment, therefore sits on a designated provider. A direct Voyage, Cohere, Jina or OpenAI contract does not, which leaves oversight with the firm [AJ].
- Every hosted embedding or rerank service is an ICT third-party arrangement for the DORA register [AJ].
- PRA PS7/26 and FCA PS26/2 require third-party notifications from 18 March 2027 (R-PRA-SS221, R-FCA-SYSC8) [VF: A8-S062, V2-S053]. A new embedding vendor that supports an important business service may need notification lead time [AJ].

**Residency.** The key-facts table in §7.8 gives the verified position per vendor. For UK firms two points dominate: OpenAI's UK region is storage-only for embeddings [VF: A2-S144], and Gemini's 'eu' endpoint excludes the UK [VF: A2-S039]. No hosted API in this layer verified UK processing, so UK-only data points to in-estate or UK-region VPC deployment [AJ].

**Treat embeddings as the same class of data as the text they encode** [AJ]. Vectors computed from client documents can leak information about that text, so they inherit its classification, retention and deletion obligations [AJ]. A right-to-erasure request must reach the vector index as well as the document store [Rec]. For EU/UK personal data sent to US-hosted APIs, the transfer basis rests on the Data Privacy Framework or SCCs. The DPF appeal C-703/25 P was pending as of 7 October 2026 (R-DATA-TRANSFERS) [VF: A8-S053, V2-S059].

**Chinese-origin open weights.**

- Qwen3 weights are Apache 2.0 [VF: A2-S020].
- Self-hosted, they create no data transfer [AJ]. They do need a model-provenance and supply-chain review, which is consistent with the OWASP supply-chain risk (LLM03 in the 2025 list) [R: A8-S040] [AJ].
- The hosted Model Studio API is a different decision, because its regions are Singapore, Hong Kong and Beijing [VF: A2-S022].

**Concentration.** Database companies now own two of the graphic's vendors (Voyage and Jina) [VF: A2-S033, A2-S023]. Choosing MongoDB with Voyage, or Elastic with Jina, concentrates L6 and L7 on one supplier. Their outages and ownership events then become correlated [AJ]. IOSCO names concentration among few AI technology providers as a supervisory concern (R-INTL-AI-ASSETMGMT) [VF: A8-S058]. For important business services, either accept the bundle consciously and record it in the exit plan, or keep the embedding vendor independent of the store [Rec].

**Auditability.** For every retrieval, the C8 evidence pack should hold [Rec]:
- query hash
- embedding model and version
- index version
- filter predicate (entitlements)
- candidate count
- reranker version
- final document IDs and scores

That is enough to show what the model was shown, and to reproduce it while the index version is retained.

**Standards.**

- NIST AI 600-1 is the GenAI profile for the AI RMF (R-NIST-AIRMF) [VF: A8-S043, A8-S044].
- ISO/IEC 42001 certification is a supplier signal (R-ISO-42001). Cohere [VF: A2-S014] and Generative AI on Vertex AI [VF: A2-S043] hold it.
- The OWASP Top 10 for LLM Applications 2026 and the Top 10 for Agentic Applications for 2026 are the operative lists (R-OWASP-LLM, R-OWASP-AGENTIC) [VF: A8-S041, A8-S042]. For traceability, the 2025 list's LLM08, "Vector and Embedding Weaknesses", is the direct mapping for this layer, because the 2026 identifiers were not retrieved [R: A8-S040].

### 7.12 Worked-example slice (POV 3)

**Context.** The performance-attribution commentary agent drafts the monthly commentary for a generic multi-asset fund. It explains Brinson-style allocation, selection and currency effects against the benchmark. A portfolio manager approves every draft (plan §11) [AJ].

**What the agent needs from L7** [AJ]:
1. **Comparable past commentary.** The fund's own approved commentaries for prior periods, and approved commentaries from comparable periods (for example, months with a large currency effect). These serve as style and structure exemplars.
2. **The house style guide and terminology glossary.** For example: "allocation effect" vs "asset allocation contribution", how interaction is reported, and rounding and sign conventions.
3. **Approved market-context notes** for the period, from L8's approved sources.

**How the layer serves this** [AJ]:
- **Hybrid retrieval.** Lexical retrieval matters because queries carry exact tokens: the fund code, share-class names and period labels ("Q3 2026"). Dense retrieval matters because "the overweight in Japanese equities detracted" must match "the allocation to Japan cost relative performance".
- **Domain terminology.** Run an in-domain bake-off on 100–300 labelled queries written by analysts. Compare a general model, a finance-domain model and a fine-tuned open model:
  - Voyage publishes voyage-finance-2 [VF: A2-S007].
  - Sentence Transformers supports fine-tuning [VF: A2-S029].

  Pick by recall@20 and nDCG@10, not by vendor claims [Rec].
- **Reranking for the right fund and period.** The reranker receives the instruction-style query with the fund name, the period and the attribution theme. It is evaluated on whether the top 3 contains this fund's most recent comparable commentary and the current style guide. Metadata boosts for `fund_id` and `period` are applied in fusion. They are not left to the reranker alone.
- **Entitlement first.** The store filters on `fund_id`, `client_id`, document classification and approval status *before* ANN search, BM25 and reranking. The reranker only ever sees documents the analyst is entitled to.

**What it must never do** [AJ]:
- **Retrieve another fund's or client's data.** Cross-fund probes run in CI and must return zero hits.
- **Supply numbers.** Retrieved past commentary contains old figures. Those figures must never flow into the new draft as data. All figures come from the attribution engine through L4 tools, and the L9 numeric-faithfulness eval checks that every number in the draft traces to that output.
- **Retrieve unapproved drafts** or superseded style-guide versions. Approval status and validity dates are filter fields.
- **Run on an unpinned model.** The commentary index carries one `model_version`, and the evidence pack records it alongside the reranker version and the retrieved document IDs.

### 7.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| OpenAI – Embeddings 3 | Still text-embedding-3 (January 2024); no reranker found [VF: A2-S001, A2-S002] | Tactical text baseline where OpenAI is already approved; pair with a separate reranker [Rec] |
| Gemini – Embedding 2 | gemini-embedding-2 GA 22 April 2026; multimodal; EU endpoint excludes UK [VF: A2-S004, A2-S039] | Tactical for Google-centred, multimodal estates [Rec] |
| Voyage AI – Voyage-3 | MongoDB-owned; Voyage 4 family, rerank-3 (Preview) [VF: A2-S033, A2-S006, V1-S024] | Tactical; preferred where MongoDB is the store, after SOC 2 scope is evidenced [Rec] |
| Cohere – Embed v3 + Rerank | Embed 5 and Rerank 4; Aleph Alpha combination pending [VF: A2-S012, A2-S010, A2-S018] | Tactical, Strategic candidate for private deployment once access controls are evidenced [Rec] |
| Qwen3 – Embeddings | Embedding **and** Reranker, Apache 2.0, plus VL variants [VF: A2-S020, A2-S021] | Tactical; self-host only, after provenance review [Rec] |
| Jina AI – Embeddings v3 | Elastic-owned; v5 text/omni, reranker v3.5; CC-BY-NC weights [VF: A2-S023, A2-S025, A2-S024] | Tactical inside Elastic estates; licensed routes only [Rec] |
| SBERT – Sentence transformers | 6.1.0, Apache-2.0, Hugging Face; dense, cross-encoder, sparse, multi-vector [VF: A2-S029] | **Strategic** as the self-hosting, fine-tuning and exit toolkit [Rec] |
| NVIDIA – Embed | NeMo Retriever embed and rerank NIMs; AI Enterprise needed for production [VF: A2-S031, A2-S040] | Tactical for NVIDIA-standardised estates [Rec] |
| EthicalAgents; Ragoos | Not publicly verified; removed per CP1 Q4(a) [VF: A2-S079, A2-S080] | Do not use |
| (missing) | Amazon Bedrock embeddings and Rerank, Mixedbread and ZeroEntropy were not researched in this run [NPV]; the Vertex AI ranking API exists but was not scored [VF: B-REV-S026] | Candidates for a follow-up pass; not recommended or rejected here [AJ] |
| Layer: "Embeddings" and "RAG re-rankers" as separate tiles | Vendors ship both; stores host both [VF: A2-S101, A2-S141, A2-S133] | One governed retrieval-optimisation service: pinned versions, raw text retained, dual-index migration, in-domain eval gate [Rec] |

**H6, provisional; verdict in synthesis.** The evidence supports treating embedding and reranking as one **retrieval-optimisation** concern [AJ]:

- Six of the seven verified model vendors offer both; Google's reranker is a separate Vertex service [VF: A2-S012, A2-S010, A2-S006, A2-S034, A2-S025, A2-S026, A2-S030, A2-S020, B-REV-S026].
- Sentence Transformers covers both in one library [VF: A2-S029].
- The two are evaluated together, and they are versioned together.

The same evidence also shows the compute moving into L6, because MongoDB, Pinecone and Elastic host embedding and reranking natively [VF: A2-S141, A2-S101, A2-S133]. The provisional view is to **merge** the graphic's "Embeddings" and "RAG re-rankers" into one retrieval-optimisation layer, defined by responsibility rather than by where the compute runs [AJ]. That layer owns model choice, version pinning, hybrid fusion policy and the retrieval evaluation gate, whether the models run as APIs, in the firm's own estate, or inside the store. Embedding-model versioning should be named explicitly as a governed configuration item, because it is the one decision in this layer that carries a corpus-wide migration cost [AJ].


