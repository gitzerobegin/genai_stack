## 9. Evaluation and observability (cross-cutting)

> **Executive summary.** This layer answers two questions for every GenAI system: is the output good enough to use, and what actually happened when it ran? It does this through four connected mechanisms: offline and CI evaluation, online evaluation of production traces, traces with cost and latency, and a feedback loop from human reviewers back into the test suites. Three things have changed since the original graphic. First, ownership has consolidated. Dynatrace completed its acquisition of Arize (Phoenix and AX) on 1 October 2026 [VF: A1-S045, V1-S005]. ClickHouse announced it had acquired Langfuse on 16 January 2026 [VF: A1-S021, V2-S041]. OpenAI announced its acquisition of Promptfoo on 9 March 2026, with no closing date published [VF: A1-S024, V1-S006]. W&B Weave has been part of CoreWeave since 5 May 2025 [VF: A1-S131]. Second, OpenTelemetry has become the common ingest format [AJ], although the GenAI semantic conventions are still at "Development" status [VF: A1-S058]. Third, the products now reach across the stack into gateways, prompt management, guardrails and automated fix proposals [VF: A1-S043, A1-S039, A1-S067]. This layer is not a box at the end of the pipeline [AJ]. **Recommendation:** instrument once with OpenTelemetry GenAI conventions or OpenInference, and own the evaluation harness and the evidence store. Then pick one platform of record for traces and evals (self-hosted Langfuse, or MLflow where an ML platform already exists, or LangSmith for LangGraph estates). Run two CI eval and red-team tools, one of them independent of any model vendor [Rec].

### 9.1 Responsibility

**The problem this layer owns.** It produces measured, retained evidence that a GenAI system behaves as intended, before release and while in service [AJ]. This breaks down into three jobs:

- **Evaluation.** This covers offline and CI test suites, online scoring of production traffic, human review, LLM-as-a-judge scoring and red-teaming. The quality dimensions are correctness, faithfulness and groundedness, hallucination, answer relevance, retrieval recall@k and precision@k, tool-call accuracy and agent trajectory, plus safety [AJ].
- **Observability.** Each request needs one trace covering prompt, model and version, retrieved context, tool calls, latency, tokens, cost and errors [AJ].
- **Production feedback.** User and reviewer signals, drift and regression detection, and model comparison all flow back into the datasets that gate the next release [AJ].

**Hand-offs.** The layer receives spans from every other layer:

- the gateway (C1) and models (L1, L2)
- orchestration (L3) and tools (L4)
- retrieval (L5 to L7) and ingestion (L8) [AJ]

It passes the following on:

- **To C8 (model risk and governance):** evaluation results, approvals and monitoring evidence.
- **To C6 (FinOps):** cost per task.
- **To C2 and C7 (guardrails and security):** red-team findings.
- **To C5 (prompt management):** prompt and configuration versions, because each evaluation result must reference the exact version it tested [AJ].

**What the layer does not own.** It does not own the run-time blocking of unsafe outputs; that belongs to C2 guardrails. The two share detectors and datasets [AJ].

### 9.2 Why it matters

When this layer is badly designed, failures surface late and cannot be explained [AJ]. The typical failure modes are:

- **Silent quality regression.** A model or prompt changes, and nothing breaks loudly [AJ].
- **Untraceable answers.** No trace links an output to the context and tool results that produced it [AJ].
- **Uncalibrated judges.** An LLM judge scores everything "faithful" because nobody has checked it against human labels [AJ].
- **Cost surprises.** Spend has no per-task attribution [AJ].
- **Trace stores that leak.** Traces contain prompts, retrieved documents and outputs, so in an asset manager they contain client and portfolio data. An unmanaged SaaS trace store is a data-residency and confidentiality exposure in its own right [AJ].

**Illustrative scenario [AJ].** A fund-reporting team switches the drafting model to a newer minor version through the gateway. Their only evaluation is a weekly sample read by an analyst. The new model rounds selection effects differently and sometimes swaps "overweight" and "underweight" when describing a currency effect. Each draft still reads fluently. Three monthly cycles pass before a portfolio manager notices a mismatch against the attribution report. By then, nobody can say which commentaries were affected: traces were kept for 15 days on a free tier, and the prompt version was not recorded. Remediation means re-checking every commentary by hand and writing to the board. A numeric-faithfulness check in CI and in production, plus trace retention aligned to the records policy, would have caught the change on day one and bounded its impact. This scenario is invented to illustrate the mechanism; it is not a reported incident.

### 9.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Numeric faithfulness | Share of figures in an output that exactly match the authoritative source value (after an agreed rounding rule) | 100% at release gate; any miss blocks | Deterministic extractor and comparator against tool output captured in the trace |
| Groundedness / faithfulness | Share of claims supported by the retrieved or approved context | Agreed threshold per use case (e.g. ≥0.95 for regulated text), calibrated against human labels | LLM-as-a-judge or NLI metric (e.g. DeepEval faithfulness), sampled for human agreement |
| Retrieval recall@k / precision@k | Share of known-relevant documents retrieved in the top k / share of top k that are relevant | Set per corpus; track the trend, not the absolute value | Labelled query set in CI; contextual recall/precision metrics |
| Tool-call accuracy | Correct tool, correct arguments, correct order | ≥0.98 for read-only data tools in deterministic workflows | Trajectory assertions against expected tool calls |
| Agent trajectory adherence | Share of runs that follow the approved plan or graph without unexpected steps | Agreed per workflow; any unapproved tool call is a defect | Trajectory or plan-adherence metrics over traces |
| Red-team pass rate | Share of attack cases (OWASP LLM 2026 and Agentic 2026 categories) handled safely | No critical failures at release; trend tracked | Promptfoo plus an independent second tool in CI |
| Judge–human agreement | Agreement between LLM judge and expert labels | Agreed minimum (e.g. Cohen's kappa ≥0.7) before a judge is used as a gate | Periodic double-labelling |
| Trace completeness | Share of production requests with a full trace (prompt version, model version, context IDs, tool I/O, evals) | ≥99.9% for in-scope systems | Reconciliation of gateway logs against trace store |
| p95 latency and cost per task | Latency and fully loaded token cost per completed task | Budget per use case | Trace attributes, gateway cost data |
| Human-intervention rate | Share of outputs edited or rejected by reviewers, and the size of the edits | Trend down; spikes trigger review | Reviewer feedback captured as trace scores |
| Time to detect regression | From a change in model, prompt or data to a failing eval | Same day for gated systems | CI on every change; online sampling alerts |

The IOSCO supervisory toolkit names indicators for asset managers that include the accuracy of AI-supported valuations against benchmarks and the level and frequency of human intervention in AI-driven investment processes [VF: R-INTL-AI-ASSETMGMT, A8-S058]. The last two KPIs above are designed to produce that evidence [AJ].

### 9.4 How it works

The mechanics have three loops that share one trace and dataset store.

1. **Instrumentation.**
   - Each layer emits spans: model call, retrieval, tool execution, agent step.
   - The format is the OpenTelemetry GenAI semantic conventions. Their status is still "Development" as of 7 October 2026 [VF: A1-S058].
   - Since semconv v1.42.0, the `gen_ai.*`, `openai.*` and `mcp.*` definitions live in a dedicated repository, `semantic-conventions-genai` [VF: A1-S060].
   - That repository covers client inference, agents, tool execution, retrieval, evaluation and MCP [VF: A1-S061]. It defines a `gen_ai.evaluation.result` event carrying the evaluation name, score, label and explanation [VF: A1-S059].
   - OpenInference is the Apache-2.0 alternative convention used by Phoenix and AX [VF: A1-S049, A1-S066].
   - The architectural point is that an evaluation score can travel on the same telemetry pipe as the trace it judges [AJ].
2. **Offline and CI evaluation.** Versioned datasets (golden cases, past failures, red-team cases) are run against every change to model, prompt, retrieval configuration or tool. Results gate the merge. Every tool in this layer offers a CI path:
   - pytest plugins: LangSmith [VF: A1-S108], Phoenix [VF: A1-S106] and Opik [VF: A1-S067]
   - DeepEval's Pytest-like framework [VF: A1-S068]
   - Promptfoo with GitHub Actions, GitLab and Jenkins [VF: A1-S065]
   - Braintrust's GitHub Action, which posts PR comments [VF: A1-S109]
3. **Online evaluation and feedback.** Evaluators score a sample of production traces, and reviewer edits and user ratings are attached to traces as scores. Examples:
   - Opik online evaluation rules [VF: A1-S072]
   - Langfuse evaluators over ingested traces [VF: A1-S073]
   - Arize AX Signal [VF: A1-S046]
   - Datadog evaluations and Insights [VF: A1-S097, A1-S099]

   Clustering features group recurring failures: LangSmith Engine [VF: A1-S039], Braintrust Topics [VF: A1-S043] and AX Signal [VF: A1-S046]. Failing cases are promoted into the CI dataset, which closes the loop [AJ].

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

**Scalability**

- Sample online evaluations, not traces. Keep full traces for regulated outputs and sample the evaluation spend [AJ].
- The judge model is the main cost driver of evaluation [AJ].

**Resilience**

- Instrumentation must never block the request path. Use asynchronous export through the collector [AJ].
- The release gate must keep working if the SaaS evaluation platform is down. Run CI evals from code in the firm's repository [AJ].

**Governance**

- Version everything the score depends on: dataset, metric code, judge model and prompt, application prompt, model version. Store those versions with the result [AJ].
- Calibrate LLM judges against human labels before using them as gates [Rec].

**Observability of the observer**

- Reconcile gateway request counts against trace counts so that missing traces are themselves detected [AJ].

**Cost**

Several pricing models are in use:

- per unit: Langfuse [VF: A1-S031]
- per span or GB: Arize AX [VF: A1-S047], Datadog [VF: A1-S097]
- per seat plus per trace: LangSmith [VF: A1-S035]
- per processed GB and score: Braintrust [VF: A1-S040]

Model the cost at production volume before you commit [Rec].

**Portability**

- Instrument once with OTel GenAI or OpenInference and keep vendor SDKs at the edge [Rec].
- Keep evaluation datasets and metric code in Git, not only in a vendor UI [Rec].

**Patterns**

- A collector fan-out to a platform of record plus APM.
- Eval-as-code in CI.
- A judge model routed through the gateway, so the judge is governed like any other model.
- Reviewer edits captured as labelled data.
- A two-tool red-team, with one tool independent of any model vendor [AJ].

**Anti-patterns**

- A vendor SDK hard-wired into application code.
- Using a model vendor's tool as the only independent test of that vendor's model.
- An LLM judge with no calibration.
- Trace retention set by the free tier, not the records policy.
- Online evaluation that sends client data to an unassessed third-party judge [AJ].

### 9.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Coverage of the plan's questions: faithfulness and groundedness, recall@k and precision@k, tool-call accuracy, trajectory, red-teaming, online evaluation, regression in CI, drift; quality of dataset and experiment management; support for deterministic (code) scorers alongside LLM judges |
| Enterprise readiness (15%) | SSO, RBAC (project level), audit logs of who viewed or changed traces, datasets and scores; SCIM; SLA; multi-team tenancy. Check which of these are licence-gated in self-hosted editions |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 as baseline. Because traces carry client data, this layer's calibration reserves 5 for products that add customer-managed keys or ISO 42001, or similar, on top. Redaction at ingest; data residency of traces |
| Deployment flexibility (15%) | Self-host or BYOC for trace residency; air-gap for validation sandboxes; region pinning |
| Ecosystem (5%) | Native OTLP ingest using GenAI conventions or OpenInference; CI integrations; framework coverage |
| Reliability and maturity (10%) | Release cadence, ownership stability (five of the eleven products, from four vendors, changed or announced a change of ownership in 2025–26), pre-1.0 versioning |
| Cost / TCO (5%) | Pricing unit (span, trace, GB, seat, score), judge-token spend, self-host operations (ClickHouse, Kubernetes, PostgreSQL) |
| Lock-in / portability (15%) | Licence (MIT/Apache vs ELv2 vs proprietary), export of traces and datasets, whether eval logic lives in your repo or theirs, vendor neutrality of red-team tooling |

### 9.7 Product deep dives

**Langfuse (ClickHouse).**
- *What it is now:* an open-core LLM engineering platform covering tracing, prompt versioning, LLM-as-a-judge and code evaluators, user feedback, manual labelling, datasets and experiments [VF: A1-S073]. The core is MIT. Code under `ee/` needs a commercial licence key when self-hosted: SCIM, audit logging, data-retention policies, project-level RBAC and server-side ingestion masking [VF: A1-S023, A1-S033]. ClickHouse announced the acquisition on 16 January 2026 alongside its US$400M Series D [VF: A1-S021, V2-S041]. The founders state that the roadmap and the commitment to self-hosting are unchanged [VF: A1-S022].
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
- *Strengths:* the tightest fit with LangGraph, and the broadest commercial feature set in this layer [AJ].
- *Limitations:* LangChain recommends the native format over OTel for performance [VF: A1-S037]. The platform now bundles the agent runtime [VF: A1-S039]. Self-hosting needs at least 16 vCPU and 64 GB, plus PostgreSQL, Redis and ClickHouse [VF: A1-S034]. Pricing is per seat plus overage [VF: A1-S035].
- *Choose when:* LangGraph is the standard [AJ].
- *Avoid when:* your estate is framework-heterogeneous, or you want the observability vendor separated from the runtime vendor [AJ].
- *Competitors:* Langfuse, Braintrust, Arize AX.
- *FS note:* dual-instrument with OTel so that evidence survives an exit, and keep Engine's proposed fixes under change control [Rec].
- **Tier: Strategic (conditional on LangGraph). No flag.**

**Braintrust.**
- *What it is now:* an independent, proprietary platform built around experiments, datasets and scorers, with production logging. Its Trace conference in February 2026 introduced Topics (trace clustering) and Loop (AI-assisted optimisation), and Braintrust Gateway routes and traces model calls [VF: A1-S043]. It raised a US$80M Series B on 17 February 2026 [VF: A1-S028].
- *Deployment:* the hybrid model keeps a Braintrust-hosted control plane and puts the data plane in the customer's AWS, GCP or Azure. Customer-managed KMS keys are supported [VF: A1-S041]. The US or EU data plane is fixed when the organisation is created [VF: A1-S042].
- *Certifications:* SOC 2 Type II, with a HIPAA BAA on Enterprise. No ISO 27001 certification was found [VF: A1-S125].
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
- *Limitations:* the self-hosted open-source edition has no user management, and SSO comes with Enterprise [VF: A1-S069, A1-S122]. The local Docker install is not production-ready [VF: A1-S069]. OTel is HTTP-only [VF: A1-S070]. An EU region is not publicly verified [NPV].
- *Choose when:* you want Apache-2.0 end to end and will buy Enterprise for identity, or you already run Comet [AJ].
- *Avoid when:* you would self-host the open edition for many teams [AJ].
- *Competitors:* Langfuse, Phoenix, MLflow.
- **Tier: Tactical. No flag.** It scores 3.75 FS. It falls short of Strategic for two reasons: the open edition lacks identity, and the codebase is only about two years old [AJ].

**MLflow (GenAI capabilities).**
- *What it is now:* an Apache-2.0 platform with OTel-based tracing, evaluation and monitoring, a prompt registry and optimisation, and an AI Gateway [VF: A1-S103, A1-S019]. Version 3.17.0 was released on 7 October 2026 [VF: A1-S019].
- *Hosting:* managed by Databricks, SageMaker, Azure ML, Nebius and OpenShift AI, or self-hosted on-premises [VF: A1-S103]. Databricks contributed it to the Linux Foundation in 2020 under a vendor-neutral governance model [VF: B-L9-S004]. The code copyright remains with Databricks [VF: A1-S019].
- *Strengths:* GenAI evidence lands next to the classic model inventory and lifecycle that many regulated firms already run [AJ].
- *Limitations:* access controls and certifications depend on the managed host and are not verified in the fact base [NPV]. Evaluation depth compared with specialist tools has not been assessed from primary sources [NPV].
- *Choose when:* an ML platform already exists [AJ].
- *Avoid when:* you would self-host an unauthenticated tracking server [AJ].
- *Competitors:* Langfuse, Weave, Opik.
- **Tier: Strategic. No flag.**

**Datadog Agent Observability.**
- *What it is now:* a Datadog module, documented under the LLM Observability path. It traces agent steps and LLM calls with latency, tokens, cost and errors, and scans and redacts sensitive data. It also detects prompt injection, runs quality, privacy and safety evaluations, and produces Insights [VF: A1-S097, A1-S099].
- *Ingest:* it accepts OTel 1.37+ GenAI conventions or OpenInference [VF: A1-S098]. Pricing is metered per LLM span [VF: A1-S097].
- *Certifications:* the Datadog Trust Center lists SOC 2 Type 2, ISO/IEC 27001, 27017, 27018, 27701 and 42001, HIPAA and FedRAMP High [VF: B-L9-S001]. Whether that scope covers this module specifically is not stated [NPV].
- *Regions and access:* EU1 is hosted in Germany, and sites are isolated from each other [VF: B-L9-S002]. SAML SSO, RBAC with custom roles and an Audit Trail are documented [VF: B-L9-S003, B-L9-S005].
- *Strengths:* puts production LLM monitoring with on-call operations [AJ].
- *Limitations:* SaaS only. Self-hosting is not publicly verified [NPV].
- *Choose when:* Datadog is your APM standard [AJ].
- *Avoid when:* it would be the sole evaluation tool [AJ].
- *Competitors:* AX, LangSmith, Langfuse.
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
| L9-datadog-agent-observability | 3 | 4 | 5 | 2 | 4 | 3 | 2 | 3 | 3.30 | 3.40 | Tactical |
| L9-wandb-weave | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 2 | 3.55 | 3.55 | Tactical |

**Scoring notes [AJ].**

- No NPV cap was triggered. Datadog's certification and access-control gaps were closed with new primary sources (B-L9-S001 to S005).
- DeepEval, Phoenix, MLflow and the Promptfoo CLI were scored as self-hosted software under rubric rule 2. Promptfoo Enterprise SaaS would be capped at 2 for security, because its certifications are NPV.
- Arize AX, DeepEval and Opik reach 3.6 or above but are classed Tactical. AX was acquired seven days ago. DeepEval is a substitutable library. Opik's open edition lacks identity.
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
STEP 0 (not optional): instrument with OTel GenAI conventions (or OpenInference) via a
firm-owned OTel Collector with redaction; keep datasets and metric code in Git.

STEP 1: Platform of record for traces, datasets, evals, prompts
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

STEP 2: Production monitoring with ops
  Is Datadog or Dynatrace the APM standard?
  ├─ Datadog   → Datadog Agent Observability, fed by the same Collector (EU1 site)
  ├─ Dynatrace → Arize AX (re-assess after Dynatrace publishes its roadmap)
  └─ Neither   → platform of record's online evals + alerting

STEP 3: CI evaluation and red-teaming
  Metrics library  → DeepEval (or the platform's own evaluators), judge model via gateway
  Red-team         → Promptfoo CLI locally
                     AND, if the system under test uses an OpenAI model,
                     a second, vendor-independent red-team tool (e.g. Confident AI)
  Validation sandbox for independent reviewers → Phoenix (auth on, telemetry off, air-gapped)

STEP 4: Checks before go-live
  Trace retention ≥ records policy (and ≥ 6 months where AI Act Art. 26 applies)?
  Judge calibrated against human labels?  Trace completeness reconciled with gateway?
```

### 9.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Instrumentation (spans, attributes) | **Unacceptable if proprietary; acceptable on OTel/OpenInference** | Re-instrumenting every layer is the largest switching cost. Every product here ingests or emits OTel or OpenInference [VF: A1-S032, A1-S037, A1-S042, A1-S049, A1-S064, A1-S070, A1-S098, A1-S103, A1-S121, A1-S139] | OTel GenAI conventions via a firm-owned Collector. Pin the semconv version, because the status is "Development" [VF: A1-S058] |
| Evaluation datasets and metric code | **Unacceptable if they exist only in a vendor UI** | They are the regression baseline and validation evidence | Git-versioned datasets and code scorers. Emit results as `gen_ai.evaluation.result` events [VF: A1-S059] |
| Platform of record (trace store, UI) | **Manageable** | Replaceable if instrumentation and datasets are portable. Lock-in rises with proprietary stores (adb [VF: A1-S046]) and native formats [VF: A1-S037] | Collector fan-out; periodic export to the firm's archive |
| Production APM module | **Acceptable** | Already part of the firm's ops tooling; fed by the same Collector | None beyond the Collector |
| Red-team tooling | **Manageable, with a concentration caveat** | Promptfoo configs are MIT and portable [VF: A1-S052], but ownership by a model vendor raises an independence question [AJ] | Two tools, configs in Git |
| LLM judge model | **Manageable** | Judges drift when the model changes | Route through the gateway (C1). Pin the version and re-calibrate on change |

### 9.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23.* PRA SS1/23 applies to banks, building societies and PRA-designated investment firms with internal-model approval [VF: R-PRA-SS123, A8-S008]. It covers vendor models and requires independent validation (Principle 4) and ongoing performance monitoring [VF: R-PRA-SS123, A8-S008, A8-S037].
- *Who it binds.* For FCA solo-regulated managers, SS1/23 is not binding but is the natural benchmark. This layer is where its validation and monitoring evidence is produced [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026. It expressly places generative and agentic AI outside its scope and says the firm's own risk-management practices should determine their governance [VF: R-US-MRM, A8-S001, A8-S002].
- *The consequence.* No regulator has defined "adequate evaluation" for an LLM agent, so the firm must write its own standard. That standard needs metric definitions, thresholds, judge calibration and re-validation triggers, and it should be written to SS1/23 quality so it survives the agencies' planned AI request for information [AJ].

**EU AI Act.**
- *Deployer duties.* Article 26 requires deployers of high-risk systems to monitor operation, keep logs for at least six months, and report serious incidents. Financial institutions fold logging into their existing financial-services documentation [VF: R-EUAIA, A8-S011]. Annex III duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011].
- *Scope for this use case.* Most asset-management uses, including attribution commentary, are not Annex III. The live duties are transparency and literacy [AJ].
- *Recommendation.* Build Article 26-grade logging and monitoring anyway, because the same artefacts serve MRM and outsourcing evidence [Rec].
- *Provider duties.* Article 72 post-market monitoring falls on providers. A firm that substantially modifies a high-risk system can become a provider under Article 25 [VF: R-EUAIA, A8-S011].

**DORA, the UK CTP regime and outsourcing.**
- *Designations.* The DORA CTPP list and the UK CTP designations cover hyperscalers and no AI model provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023].
- *Observability SaaS is a third-party service.* A SaaS observability platform holding client traces is an ICT third-party service for the register of information. If it supports a critical or important function, it needs Article 30 terms and an exit plan [AJ].
- *Notification lead time.* PRA PS7/26 and FCA PS26/2 require material third-party notifications from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. Contract changes forced by the Arize, Langfuse and Promptfoo ownership changes should be planned with that lead time [Rec].
- *Exit routes.* SS2/21 expects documented, tested exit plans [VF: R-PRA-SS221, A8-S048]. Evaluation suites are what let a firm re-qualify an alternative model or platform quickly [AJ].

**Residency and auditability.**
- *FCA expectations.* FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. Traces held by a vendor fall within that [AJ].
- *Transfers.* EU-to-US transfers rely on the Data Privacy Framework or SCCs. An annulment appeal (C-703/25 P) is pending [VF: R-DATA-TRANSFERS, A8-S053].
- *Recommendation.* Prefer in-estate or EU/UK-region trace stores and redact at the Collector [Rec].
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

1. **Numeric faithfulness, deterministic, blocking.**
   - A code scorer extracts every figure, sign and direction word ("added", "detracted", "overweight") from the draft.
   - It compares each one with the attribution-engine tool output recorded in the same trace. The read-only L4 tool call is a span, so the reference values are evidence, not memory.
   - Any mismatch outside the agreed rounding rule fails the run. This is code, not an LLM judge.
2. **Groundedness against approved sources.** Every market-context claim must be supported by a retrieved, approved document, scored by a calibrated judge or an NLI metric. Unsupported claims are flagged, so that inference stays distinguishable from source data.
3. **House-style checks.** Terminology, prohibited phrases, tense and length are checked by rules first, with an LLM judge only for tone.
4. **Trajectory check.** In the deterministic workflow, the agent calls the attribution tool, then retrieval, then drafts. Any extra tool call or write attempt is a defect.
5. **Regression suite of past commentaries.**
   - Use about 24 to 36 months of approved commentaries with their attribution snapshots as golden cases.
   - Run them on every change of model, prompt, retrieval index or judge, and add every reviewer-caught error as a new case.
   - This suite also re-qualifies a fallback model for the SS2/21 exit route.
6. **Reviewer-edit feedback loop.**
   - The portfolio manager's edits are captured as diffs on the trace, with an edit-size score and a reason code.
   - The human-intervention rate is tracked monthly, which serves the IOSCO human-intervention indicator.
   - Recurring edit types become new eval cases or style rules.
7. **Evidence pack retention.** For each commentary, the pack holds:
   - trace ID, prompt and template version, model and version, judge version
   - attribution data snapshot hash and retrieved document IDs
   - eval results with thresholds, approver identity and timestamp
   - the final text and the diff from the draft

   It is written to the firm's WORM or records archive (C8) under the records-retention policy, independent of the observability vendor's retention.
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
| L9 drawn as a downstream "evals and observability" layer with eight tiles | Tracing, evaluation and feedback span every layer. Products now include gateways (Braintrust, LangSmith, MLflow), guardrails (Opik), prompt management and automated fix proposals [VF: A1-S043, A1-S039, A1-S103, A1-S067] | A cross-cutting plane: firm-owned OTel Collector, one platform of record, CI eval and red-team harness, evidence archive in C8 [Rec] |
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
- **Tools couple CI to production.** Six of the original products document a CI evaluation path, and every platform product ingests production traces and runs evaluators over them (see 9.4).
- **Vendors are pushing the layer sideways.** It is moving into gateways (C1), prompt management (C5), guardrails (C2) and security testing (C7) [VF: A1-S043, A1-S103, A1-S067, A1-S024].
- **Ownership is consolidating into horizontal platforms.** The new owners are APM vendors (Dynatrace, Datadog), a database vendor (ClickHouse), a model vendor (OpenAI) and a GPU cloud (CoreWeave) [VF: A1-S045, A1-S097, A1-S021, A1-S024, A1-S131].

The counter-evidence is that the OTel GenAI conventions are still "Development" and recently moved repository [VF: A1-S058, A1-S060], so the shared plane is not yet stable.

**Provisional recommendation.** Reposition L9 as a cross-cutting plane drawn alongside the control-plane components (C1 to C8) [AJ]. It should have a firm-owned telemetry and evidence spine, and the products should sit on it as replaceable backends [AJ]. **Provisional; verdict in synthesis.**
