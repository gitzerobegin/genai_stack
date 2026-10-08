## 3. Agent frameworks and orchestration

> **Conflict-of-interest disclosure.** The author is an Anthropic model, and the Claude Agent SDK assessed in this section is an Anthropic product [VF: A4-S092, A4-S027]. It was scored on the same rubric as every other framework. Its limitations are recorded in full in §3.7, borderline calls on it were resolved against it, and independent alternatives are named wherever it is mentioned [AJ].

> **Executive summary.** This layer decides how an AI application sequences model calls, tool calls, state and human decisions, and what happens when a step fails half-way. Four things have changed since the original graphic. First, every major framework now ships two modes: a deterministic workflow or graph engine, and an autonomous agent loop. LangGraph combines both in one graph [VF: A4-S039]; Microsoft Agent Framework separates Agents from graph-based Workflows [VF: A4-S066]; CrewAI pairs Flows with Crews [VF: A4-S050]; Google ADK 2.0 added a Workflow Runtime [VF: A4-S114]. Second, durable execution has become a separate concern, delegated to engines such as Temporal: Pydantic AI v2 attaches durability through Temporal, DBOS or Prefect, the OpenAI Agents SDK integrates Temporal and DBOS, and Mistral Workflows is built on Temporal [VF: A4-S045, A4-S052, A4-S058]. Third, the vendor estate has been reshaped: Microsoft Agent Framework reached GA on 2 April 2026 as successor to Semantic Kernel and AutoGen, with AutoGen in maintenance mode [VF: A4-S008, A4-S012, A4-S021, V1-S050]; OpenAI's Agent Builder shuts down on 30 November 2026 [VF: A4-S054, V1-S051]; LangGraph Platform is now LangSmith Deployment [VF: A4-S031, V1-S056]; LlamaIndex says its focus has moved to LlamaParse [VF: A4-S117]; and no distinct "Mistral Agents SDK" exists [VF: A4-S057]. Fourth, the hyperscalers now sell framework-agnostic agent runtimes, such as Amazon Bedrock AgentCore, which runs each session in its own microVM [VF: A4-S116, B-L3-S004]. The graphic's single "agent framework" row hides the most important architectural choice in the stack: whether a process is a workflow or an agent [AJ]. **Recommendation:** build regulated use cases as deterministic workflow graphs with bounded LLM steps, run them on a durable-execution substrate, and keep approval gates and state in firm-controlled stores. Standardise on one framework per language estate (LangGraph by default; Microsoft Agent Framework in Microsoft estates), use Temporal (or DBOS) for durability, and admit autonomous agent loops only as sandboxed sub-steps with read-only tools [Rec].

### 3.1 Responsibility

**The problem this layer owns.** L3 turns a business process into an executable, observable plan in which some steps are code and some are model judgements [AJ]. It owns seven things, matching the plan's research questions:

- **State and persistence.** What the run knows at each step, where that state is checkpointed, and how it is restored [AJ].
- **Workflows and planning.** Whether the sequence of steps is fixed in code, chosen by a router, or planned by the model at run time [AJ].
- **Tool calling.** Which tools a step may call, with what arguments, and under whose approval; the tools themselves belong to L4 [AJ].
- **Human-in-the-loop.** Interrupts, approvals, edits and resumption [AJ].
- **Multi-agent patterns.** Handoffs, agents-as-tools, supervisors and group collaboration [AJ].
- **Durable execution and retries.** Resuming after a crash without repeating side effects, with timeouts and retry policy [AJ].
- **Deterministic versus autonomous orchestration.** The explicit decision, per use case, of how much control flow the model is given [AJ].

**Hand-offs.**

- *Up* to the application and channel: L3 exposes a run API (start, stream, interrupt, resume) and returns outputs with run IDs [AJ].
- *Down* to L4 for tools and MCP servers, to L5 for memory, to L6 to L8 for retrieval, and to L2/C1 for model calls through the gateway [AJ].
- *Sideways* to L9 (every node is a span), C2 (guardrails at node boundaries), C4 (agent identity for tool calls), C5 (prompt and graph versions) and C8 (the run record as evidence) [AJ].

**What L3 does not own.** It does not own tool authorisation, which is C4 and the L4 gateway; it does not own run-time content blocking, which is C2; and it does not own long-term memory policy, which is L5 [AJ]. A framework that bundles these (LangSmith, AgentCore, Foundry) should be configured so that the firm's own controls stay authoritative [AJ].

### 3.2 Why it matters

When this layer is badly designed, the system's behaviour stops being a property of its design and becomes a property of each run [AJ]. Three failure modes recur:

- **Autonomy where none was needed.** A task with a known sequence is given to an agent loop. Each run takes a slightly different path, so evaluation results do not transfer between runs and validation cannot cover the space of behaviours [AJ]. The plan's pair-6 tension states the counter-position: most enterprise agents should be deterministic workflows with one judgement step, and guardrails cannot fix a workflow that should never have been autonomous [AJ].
- **No durable state.** A crash, deploy or timeout restarts the run from the beginning, so tools are called twice, approvals are lost or, worse, a half-finished run is silently abandoned [AJ]. The Claude Agent SDK, for example, keeps session transcripts on local disk, where they do not survive a container restart unless a session store is configured [VF: A4-S122].
- **Approval as convention, not control.** A "human review" step that the code can skip, or that does not record who approved what, is not a gate [AJ].

**Illustrative scenario [AJ].** A team builds the monthly attribution commentary as a single autonomous agent with tools for the attribution engine, the document store and the publishing system. It works in testing. In month three, a container is recycled mid-run during the busiest reporting day. The agent had fetched attribution data and drafted text, but its state lived in process memory. The scheduler retries the run from the start. On the second run the attribution engine has been refreshed with a late price correction, so the numbers differ slightly from the first run. A fund's retry also picks up a stale draft left in a shared working directory, and because the agent has a publishing tool and a loosely worded instruction to "finalise when complete", it publishes the stale draft before the reviewer sees it. Nobody can reconstruct which data the published text came from, because the run had no checkpoint and the trace stopped at the crash. A deterministic graph with a checkpointed data snapshot, no publishing tool, and an approval interrupt that only a named human can resume would have made each of those steps impossible. The scenario is invented; it is not a reported incident.

### 3.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Path conformance | Share of runs whose executed node sequence matches the approved graph | 100% for regulated workflows; any deviation is a defect | Compare trace node sequence with the graph version (L9) |
| Resume without re-execution | Share of interrupted runs that resume from the last checkpoint without repeating completed side-effecting steps | 100% in fault-injection tests | Kill-and-resume tests in CI; tool-call counts per run ID |
| Approval-gate integrity | Share of releases that carry a recorded human approval by an authorised approver | 100%; zero bypasses | Reconcile publish events against approval records (C8) |
| Autonomy budget | Steps per run where the model chooses the next action, and maximum tool calls per run | Declared per use case; often 0–1 for regulated flows | Static analysis of the graph plus run-time counters |
| Tool-call scope | Tool calls outside the allow-list for the workflow | Zero | Gateway and orchestrator logs (L4, C4) |
| Reproducibility | Ability to re-run a past run with the same inputs, versions and recorded tool outputs | Every regulated run replayable from its record | Replay from checkpoint and recorded activity results |
| Run success rate and p95 duration | Completed runs and end-to-end latency, by workflow version | Per use case | Orchestrator metrics |
| Cost per completed run | Tokens plus runtime compute per successful run | Budget per use case | Gateway and runtime billing joined on run ID (C6) |
| Framework currency | Days behind the pinned framework's latest security fix | Within the patch SLA (e.g. 30 days) | Dependency scanning (C7) |

The IOSCO toolkit lists "level and frequency of human intervention in AI-driven investment processes" among supervisory indicators for asset managers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. The approval-gate and autonomy-budget KPIs give that indicator a design-time and a run-time measure [AJ].

### 3.4 How it works

**Two kinds of orchestration.** Anthropic's own guidance draws the line used in this section: "workflows", where LLMs and tools are orchestrated through predefined code paths, versus "agents", where LLMs dynamically direct their own processes and tool usage [VF: A4-S030]. The frameworks implement that split in different ways:

| Framework | Deterministic mode | Autonomous mode | Durability |
|---|---|---|---|
| LangGraph | Graph with hand-coded nodes; Functional API (@entrypoint/@task) [VF: A4-S039] | LLM-driven nodes and agent loops in the same graph [VF: A4-S039] | Checkpointers (Postgres recommended in production); side effects wrapped in tasks [VF: A4-S001, A4-S039] |
| Microsoft Agent Framework | Graph Workflows: sequential, concurrent, handoff, group collaboration [VF: A4-S066] | Agents [VF: A4-S066] | Checkpointing; durable agents via Durable Task / Azure Functions (beta) [VF: A4-S066, A4-S101, A4-S102] |
| CrewAI | Flows (@start, @listen, @router) [VF: A4-S050] | Crews [VF: A4-S050] | Not publicly verified [NPV] |
| Google ADK 2.0 | Workflow Runtime: routing, fan-out/fan-in, loops, retry, state, HITL [VF: A4-S114] | Agents and multi-agent hierarchies [VF: A4-S114] | State and retry in the runtime [VF: A4-S114] |
| Pydantic AI v2 | pydantic_graph control flow [VF: A4-S119] | Typed agent loop [VF: A4-S119] | Capability backed by Temporal, DBOS or Prefect; graph persistence removed in v2 [VF: A4-S044, A4-S045] |
| LlamaIndex | Workflows (event-driven, step-based) [VF: A4-S041] | Agents [VF: A4-S117] | Not publicly verified [NPV] |
| OpenAI Agents SDK | None native (code around the SDK) [AJ] | Agent loop, handoffs, agents-as-tools [VF: A4-S120] | Sessions; Temporal and DBOS integrations; sandbox snapshot and rehydration [VF: A4-S052, A4-S053] |
| Claude Agent SDK | None [VF: A4-S027] | Claude Code agent loop with subagents [VF: A4-S027] | Session resume/fork; transcripts need a session store to survive restarts [VF: A4-S122] |
| Mistral | Workflows on Temporal [VF: A4-S058] | Agents API with handoffs [VF: A4-S057] | Temporal event history [VF: A4-S058, A4-S061] |
| Vercel | Workflow SDK (durable TS/JS functions) [VF: A4-S071] | ToolLoopAgent [VF: A4-S069] | Workflow SDK, self-hostable with Postgres [VF: A4-S071] |

**Durable execution.** A durable engine records the result of each side-effecting step (an "activity" in Temporal's terms) so that, after a failure, the workflow is replayed and completed steps return their recorded results instead of running again [VF: A4-S019, A4-S045]. Temporal, DBOS ("ultra-lightweight durable execution") and Restate are the engines named in the fact base [VF: A4-S019, A4-S020, A4-S104]. LangGraph achieves the same effect with checkpoints, and requires side effects to be wrapped in tasks so that the Functional API can reload saved results [VF: A4-S039]. The design consequence is that model calls and tool calls must be idempotent or recorded, and that the checkpoint store holds the evidence of what the run saw [AJ].

**Runtimes are now separate from frameworks.** AgentCore runs agents written with Strands, LangGraph, CrewAI, AutoGen or custom code, and gives each user session its own microVM, which is terminated and its memory sanitised at session end [VF: A4-S116, B-L3-S004]. Session state there is ephemeral by default and AWS says it should not be used for long-term durability [VF: B-L3-S004]. A managed runtime is therefore an isolation and operations choice, not a substitute for durable workflow state [AJ].

**Reference flow.**

```text
 request (run_id, user, use case) ──► L3 workflow engine (graph version pinned, C5)
                                         │
   ┌─────────────── deterministic graph (code owns control flow) ────────────────┐
   │ [fetch data]──►[retrieve context]──►[LLM step]──►[eval gate]──►[APPROVAL]──►[release]
   │  activity:       activity:            bounded      L9 checks    interrupt;      activity:
   │  read-only tool  read-only retrieval  judgement    deterministic resume only by write by
   │  (L4/C4)         (L6-L8)              via C1       + judge       named approver  release svc
   └──────┬───────────────┬──────────────────┬──────────────┬───────────┬─────────────┘
          ▼               ▼                  ▼              ▼           ▼
   durable store: checkpoints + recorded activity results (firm-controlled DB / Temporal)
          ▼
   OTel spans per node (L9) ──► evidence pack (C8): graph version, inputs hash, outputs, approver
```

The key design choice is that the graph, not the model, owns the control flow, and that every edge where something irreversible happens is either a recorded activity or a human interrupt [AJ].

### 3.5 Enterprise design principles

**Security**

- Treat the checkpoint store as a security boundary. LangGraph has published three checkpoint deserialisation advisories since 2025 (CVE-2025-64439, CVE-2026-28277, CVE-2026-48775), all patched, and the default serializer is used by all shipped checkpointer backends [VF: B-L3-S007]. Restrict write access to the runtime identity, encrypt at rest and keep the packages current [Rec].
- Give each agent run its own identity and the narrowest tool scope; tool authorisation lives in the L4 gateway and C4, not in the prompt [Rec]. In AgentCore, code inside the microVM can reach the execution-role credentials through the metadata endpoint, so the execution role must be scoped tightly [VF: B-L3-S004].
- Run autonomous loops that execute code or touch files in sandboxes with network control. Anthropic recommends sandboxed containers for the Claude Agent SDK [VF: A4-S122], and the OpenAI Agents SDK separates the harness from compute so credentials stay away from model-generated code [VF: A4-S053].
- Do not let a vendor's default tracing export client data. The OpenAI Agents SDK traces to OpenAI's dashboard by default [VF: A4-S052]; replace it with a firm-owned exporter [Rec].

**Scalability and cost**

- Hosting models differ sharply. The Claude Agent SDK runs one long-lived subprocess per concurrent session, so compute scales with concurrent sessions rather than requests [VF: A4-S122]. AgentCore Runtime sessions stop after 15 minutes idle by default and run up to 8 hours per lifecycle; longer runs need Runtime Instances (up to 14 days) [VF: B-L3-S004]. Size the runtime on concurrent sessions and run length, not on request rate [AJ].
- Multi-agent patterns multiply model calls per task; CrewAI's Crews are a direct example [AJ]. Set a per-run token and tool-call budget in the orchestrator [Rec].

**Resilience**

- Put every side effect behind a recorded activity or task, so that a resumed run never repeats a tool call [Rec].
- Self-hosting Temporal means operating Kubernetes and persistence stores and upgrading minor versions in sequence [VF: B-L3-S002]. Temporal Cloud runs the same server, so the choice can be revisited without code changes [VF: B-L3-S002].

**Governance and observability**

- Version the graph as code, alongside prompts (C5), and record the graph version on every run [Rec].
- Make approvals first-class interrupts with the approver's identity recorded; LangGraph interrupts, Microsoft Agent Framework HITL, ADK tool confirmation and OpenAI Agents SDK resumable approvals all support this pattern [VF: A4-S118, A4-S066, A4-S114, A4-S120] [AJ].
- Emit OpenTelemetry spans per node: Microsoft Agent Framework and LlamaIndex Workflows ship OTel instrumentation [VF: A4-S066, A4-S013].

**Portability**

- The plan's abstraction strategy warns against over-abstracting agent frameworks [AJ]. Do not write a firm-wide wrapper over LangGraph, Agent Framework and ADK. Instead, keep the portable assets outside the framework: prompts (C5), tool contracts (MCP/OpenAPI, L4), evaluation suites (L9), and the workflow specification as a reviewed document [Rec].

**Patterns [AJ]:** deterministic graph with one bounded LLM step; durable activities around every side effect; approval interrupt before any irreversible action; autonomous loop confined to a sandboxed sub-step with read-only tools; framework-agnostic managed runtime for isolation.

**Anti-patterns [AJ]:** an autonomous agent for a process with a known sequence; a "finalise" or "publish" tool reachable by the model; state held only in process memory or a container's disk; approvals recorded in chat text; framework abstractions written over other frameworks; adopting a hosted agent API whose residency or retention terms do not fit the data (for example a US-only, non-ZDR beta [VF: A4-S055]).

### 3.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Both deterministic and autonomous modes; checkpointing; HITL interrupts with resume; durable execution or a clean integration with a durable engine; multi-agent primitives; typed state; streaming |
| Enterprise readiness (15%) | For libraries (rubric rule 2): what controls they enable in-estate, plus vendor support or LTS commitments. For managed runtimes: SSO, RBAC, audit, SCIM, SLA |
| Security and compliance (20%) | Library hygiene (advisories, patch cadence, licence clarity); sandboxing model; managed-runtime certifications and isolation; default telemetry destinations |
| Deployment flexibility (15%) | Runs in the firm's estate; managed options; on-prem; model-provider independence |
| Ecosystem (5%) | MCP, A2A, OTel, provider coverage; whether runtimes host it |
| Reliability and maturity (10%) | 1.x stability commitments; major-version churn; Alpha/Beta classifiers; vendor focus |
| Cost / TCO (5%) | Licence cost; runtime pricing units; operations burden of durable backends |
| Lock-in / portability (15%) | Licence; framework-specific APIs; model lock-in; whether state lives in a vendor cloud |

### 3.7 Product deep dives

**LangGraph (LangChain).**
- *What it is now:* a low-level, MIT-licensed runtime for long-running, stateful workflows or agents. It provides durable execution that resumes where it left off, human-in-the-loop via interrupts, short- and long-term memory, streaming, and a Functional API for workflow-style code; deterministic code and LLM-driven decisions can be combined in one graph [VF: A4-S118, A4-S039]. langgraph 1.2.14 was released on 6 October 2026; 1.0.0 came on 17 October 2025 with a commitment to no breaking changes until 2.0 [VF: A4-S001, A4-S033].
- *Managed runtime:* LangGraph Platform was renamed LangSmith Deployment on 14 October 2025 [VF: A4-S031, V1-S056]. It is available as cloud SaaS, BYOC/hybrid with the data plane in the customer VPC, and self-hosted on Kubernetes (Enterprise plan) [VF: A4-S036, A4-S037]. Existing Deployment customers moved to usage-based LSU pricing on 1 October 2026 [VF: A4-S036].
- *Certifications and access:* LangSmith states SOC 2 Type II and HIPAA (BAA on Enterprise); ISO 27001 is claimed on some LangChain pages but omitted from others, so its scope is unconfirmed [VF: A4-S034, A4-S035, A4-S149]. LangSmith Enterprise offers SAML 2.0/OIDC SSO, SCIM 2.0 and custom-role RBAC; self-hosted v0.14 enables ABAC and OCSF audit logs by default [VF: A4-S038].
- *Security hygiene:* three checkpoint deserialisation advisories (2025–26) were published and patched through GitHub security advisories [VF: B-L3-S007].
- *Strengths:* the most complete coverage of the seven L3 questions in a stable 1.x framework [AJ].
- *Limitations:* graph and checkpoint APIs are LangGraph-specific [VF: A4-S039]; the ecosystem pulls towards LangSmith for deployment and observability [VF: A4-S118, A4-S031].
- *Choose when:* you need deterministic graphs with bounded LLM steps, durable checkpoints and approval interrupts, in Python or TypeScript [AJ].
- *Avoid when:* a single model call would do, or you cannot control who writes to the checkpoint database [AJ].
- *Competitors:* Microsoft Agent Framework, Google ADK, Pydantic AI with Temporal.
- *FS note:* pin `langgraph` and `langgraph-checkpoint`, run the Postgres checkpointer in-region with write access limited to the runtime identity, and dual-export traces via OTel so evidence survives an exit from LangSmith [Rec].
- **Tier: Strategic. Flag: Renamed** (LangGraph Platform → LangSmith Deployment).

**LlamaIndex (LlamaIndex, Inc.).**
- *What it is now:* an MIT framework for agentic and RAG applications with Workflows, a lightweight, event-driven, step-based engine with typed state and OpenTelemetry instrumentation, standalone since June 2025 (llama-index-workflows 2.25.0) [VF: A4-S117, A4-S041, A4-S013]. llama-index-core is 0.14.25 [VF: A4-S002].
- *Vendor direction:* the README states "our primary focus has shifted towards LlamaParse"; LlamaCloud was renamed LlamaParse, and LlamaAgents (document agents on Workflows) has been in open preview since November 2025 [VF: A4-S117, A4-S042]. LlamaParse is assessed in L8.
- *Strengths:* Workflows is a clean, deterministic step engine that can be used outside the LlamaIndex ecosystem [VF: A4-S041] [AJ].
- *Limitations:* still 0.x after three years [VF: A4-S002]; framework investment may decline as the vendor's priority moves [VF: A4-S117]; HITL and durable execution are not evidenced in the fact base [NPV].
- *Choose when:* retrieval-heavy agents are already built on LlamaIndex, or LlamaParse is the chosen parser [AJ].
- *Avoid when:* you are choosing a long-term orchestration standard [AJ].
- *Competitors:* LangGraph, Pydantic AI, LlamaParse (L8) for document agents.
- *FS note:* use it as a retrieval toolkit inside a governed workflow, not as the workflow engine of record [Rec].
- **Tier: Tactical. Flag: Renamed** (LlamaCloud → LlamaParse).

**Pydantic AI (Pydantic Services).**
- *What it is now:* a typed, model-agnostic Python agent loop with structured outputs and tools; `pydantic_graph` provides graph control flow, and durable execution is attached as a capability via Temporal, DBOS or Prefect [VF: A4-S119, A4-S044, A4-S045]. Version 2.0.0 shipped on 23 June 2026 and removed `pydantic_graph.persistence`; the v1 line still receives security fixes for at least six months [VF: A4-S003, V1-S074].
- *Strengths:* type-checked inputs and outputs suit tasks where numbers and structure matter [AJ]; durability is delegated to engines co-maintained with their vendors rather than reinvented [VF: A4-S045].
- *Limitations:* two major versions in about ten months, with breaking graph-persistence changes [VF: A4-S003, A4-S044]. Commercial support is not publicly verified [NPV]. The only funding found is a US$12.5M Series A [VF: A4-S046].
- *Choose when:* a Python team wants a typed LLM step inside a Temporal or DBOS workflow [AJ].
- *Avoid when:* you need a vendor platform with SLAs [AJ].
- *Competitors:* LangGraph, OpenAI Agents SDK, Temporal with a thin SDK.
- *FS note:* pin the major version and plan migrations against the v1 support window [Rec].
- **Tier: Tactical. No flag.** At 3.55 FS it is close to Strategic; the major-version churn and absence of verified support keep it Tactical [AJ].

**CrewAI (crewAI, Inc.).**
- *What it is now:* an MIT framework with two modes. Crews are teams of role-playing agents that collaborate autonomously; Flows are event-driven, stateful process definitions (@start, @listen, @router) that can trigger Crews [VF: A4-S004, A4-S050]. The vendor recommends Flows as the outer "process definition" with Crews invoked inside for autonomous steps [VF: A4-S050]. crewai 1.15.24 was released on 7 October 2026 (1.15.25 followed hours later), and 1.0.0 on 20 October 2025 [VF: A4-S004, V1-S075].
- *Commercial platform:* CrewAI AMP deploys to CrewAI cloud, a customer VPC on AWS, Azure or GCP, or on-premises; earlier materials call it CrewAI Enterprise, but no explicit rename notice was found [VF: A4-S047, A4-S049, V1-S075]. The Enterprise plan includes SSO, RBAC, PII redaction and policies, with 45-day onboarding [VF: A4-S047].
- *Certifications:* a SOC 2 Type 2 report dated June 2026 is listed in the trust centre; a HIPAA report described as "Type 1" is listed without BAA scope [VF: A4-S048].
- *Strengths:* the vendor's own guidance matches the H2 split, which makes the right pattern the documented one [AJ].
- *Limitations:* Crew and Flow abstractions are CrewAI-specific [AJ]; durable execution and HITL are not evidenced [NPV]; confirmed funding is about US$20M, and a reported Series B is unconfirmed [VF: A4-S148].
- *Choose when:* a team wants a packaged multi-agent platform with an on-premises option [AJ].
- *Avoid when:* the process is deterministic and does not need multiple agents [AJ].
- *Competitors:* LangGraph, Microsoft Agent Framework, Google ADK.
- *FS note:* use Flows for any regulated process; confine Crews to drafting or research sub-steps behind an approval gate [Rec].
- **Tier: Tactical. No flag** (the AMP rename is not confirmed, so the Renamed flag is not applied).

**OpenAI Agents SDK (OpenAI).**
- *What it is now:* an MIT, provider-agnostic SDK: agents with tools, handoffs or agents-as-tools, input/output guardrails, sessions with persistent memory and resumable approvals, built-in tracing, voice and sandboxed agents; it supports OpenAI's Responses and Chat Completions APIs and "100+ other LLMs" [VF: A4-S120, A4-S052]. openai-agents 0.23.1 was released on 2 October 2026 [VF: A4-S005]. The 15 April 2026 update added a model-native harness and native sandbox execution with seven providers [VF: A4-S053].
- *Durability:* Temporal and DBOS integrations support durable, long-running workflows including human-in-the-loop [VF: A4-S052]; sandbox snapshot and rehydration resume runs in a fresh container [VF: A4-S053].
- *Not to be confused with:* the hosted Agents API (public beta since 10 September 2026, managed Codex harness, US-only residency and no ZDR at launch) and Agent Builder, whose deprecation was announced on 3 June 2026 with shutdown on 30 November 2026 [VF: A4-S055, A4-S054, V1-S051, V1-S083].
- *Strengths:* compact primitives with guardrails and approvals built in [AJ].
- *Limitations:* pre-1.0 [VF: A4-S005]; tracing defaults to OpenAI's dashboard [VF: A4-S052]; OpenAI retires adjacent products often (Assistants API sunset 26 August 2026; Agent Builder 30 November 2026) [VF: A4-S056, A4-S054].
- *Choose when:* you want an agent step inside a durable workflow, with a custom trace processor [AJ].
- *Avoid when:* the hosted Agents API would process UK or EU client data [AJ].
- *Competitors:* Pydantic AI, LangGraph, Claude Agent SDK.
- *FS note:* replace the default trace exporter before any client data flows, and treat Agent Builder flows as a migration item due before 30 November 2026 [Rec].
- **Tier: Tactical. No flag.**

**Claude Agent SDK (Anthropic).**
- *Conflict of interest:* this is an Anthropic product, assessed by an Anthropic model. It was scored on the same rubric, borderline calls (technical, deployment, maturity) were resolved against it, and independent alternatives are named below [AJ].
- *What it is now:* an agent harness SDK, formerly the Claude Code SDK (renamed 29 September 2025; the old package is deprecated) [VF: A4-S028, A4-S011, V1-S049]. It gives developers the agent loop, built-in file, shell and web tools, hooks, subagents, MCP, permissions, resumable and forkable sessions, skills and plugins that power Claude Code [VF: A4-S027]. claude-agent-sdk 0.2.164 (6 October 2026) carries the PyPI classifier "Development Status: 3 - Alpha"; the TypeScript package is 0.3.293 [VF: A4-S006, A4-S023].
- *Architecture:* the SDK spawns and supervises one Claude Code CLI subprocess per session over stdio; that subprocess owns a shell, a working directory and session transcripts on local disk, which do not survive a container restart unless a session store is configured [VF: A4-S122]. It is not a deterministic workflow engine [VF: A4-S027, A4-S122].
- *Licence and terms:* the Python repository licence is MIT, the npm licence field reads "SEE LICENSE IN README.md", and Anthropic's docs state that use of the SDK is governed by Anthropic's Commercial Terms of Service [VF: A4-S092, A4-S006, A4-S023, V1-S048]. Third-party products may not present themselves as Claude Code [VF: A4-S027].
- *Data handling:* the SDK inherits the API arrangement; ZDR is available per organisation for eligible Claude API features, while Claude Managed Agents, the hosted alternative (beta), is excluded from ZDR because session transcripts persist until deleted [VF: A4-S123, A4-S124]. On Bedrock or Google Cloud, the cloud provider is the data processor [VF: A4-S123].
- *Strengths:* permission modes and hooks give fine-grained approval over which tools run automatically [VF: A4-S027]; it is a capable harness for file- and code-centric autonomous tasks [AJ].
- *Limitations:* Alpha classification and 0.x versioning [VF: A4-S006]; Claude models only [VF: A4-S027, A4-S122]; Commercial Terms despite the MIT repository licence [VF: A4-S092]; compute scales with concurrent sessions [VF: A4-S122]; dependence on the bundled CLI's release cadence [VF: A4-S006]; Managed Agents excluded from ZDR [VF: A4-S123]; enterprise support not publicly verified [NPV].
- *Choose when:* a sandboxed autonomous sub-task (for example, code or document manipulation) sits inside a firm-owned workflow and Claude is already an approved model [AJ].
- *Avoid when:* you need model portability, a workflow engine, or a non-Alpha dependency for a regulated process [AJ].
- *Independent alternatives:* LangGraph or Pydantic AI for the workflow and agent step (both model-agnostic, MIT); the OpenAI Agents SDK as a comparable harness from another model vendor [AJ].
- *FS note:* run only in sandboxed containers with network control, under a workflow engine that owns state and approvals; record the Commercial Terms in the third-party file [Rec].
- **Tier: Experimental. Flag: Renamed** (Claude Code SDK → Claude Agent SDK).

**Mistral Agents API and Mistral Workflows (Mistral AI).**
- *What it is now:* there is no separately branded "Mistral Agents SDK" [VF: A4-S057]. The **Agents API** creates persistent agents with built-in connectors (code execution, web search, image generation, document library, MCP), branchable stateful conversations and handoffs executed server- or client-side, reached through the general `mistralai` SDKs (Python 3.1.0, 6 October 2026) [VF: A4-S057, A4-S007]. **Mistral Workflows** (`mistralai-workflows` 3.15.0, Beta) is a Python SDK with decorators for retries, timeouts, tracing, rate limiting and HITL, built on Temporal with a Mistral-hosted control plane and customer-run workers on Kubernetes [VF: A4-S058, A4-S061].
- *Status:* the Agents API sits under the SDK's beta namespace; Workflows is "publicly available" per the announcement, Public Preview per the docs and Beta per PyPI; durable agents are in Public Preview [VF: A4-S057, V1-S065]. SDK 3.0.0 (28 September 2026) removed some tools from chat and agent completions [VF: A4-S059].
- *Certifications and residency:* company-level SOC 2 Type II, ISO 27001:2022 and ISO 27701:2019, product scope not seen [VF: A4-S060]. Data is hosted in the EU by default with an optional US endpoint [VF: A5-S075]. Conversations can be run with `store=False` so history is not stored on Mistral cloud [R: A4-S057].
- *Strengths:* EU-default hosting and Temporal-grade durability for Mistral-centric estates [AJ].
- *Limitations:* beta and preview status; breaking SDK majors in March and September 2026 [VF: A4-S061, A4-S007]; access controls and pricing not publicly verified [NPV]; agent state lives in Mistral cloud unless disabled [VF: A4-S057].
- *Choose when:* an EU-hosted, Mistral-model estate wants managed agents [AJ].
- *Avoid when:* you need GA components or a portable framework [AJ].
- *Competitors:* OpenAI Agents SDK, Temporal (directly), LangGraph.
- *FS note:* relabel the graphic tile "Mistral Agents API (+ Workflows)"; keep the workflow definition in the firm's own code [Rec].
- **Tier: Experimental. No flag** (tile relabelled; the products exist under other names).

**Vercel AI SDK (Vercel).**
- *What it is now:* an Apache-2.0 TypeScript toolkit (npm `ai`, 7.0.131) giving a unified API across model providers for text and structured generation, tool calling and agents (ToolLoopAgent), plus UI hooks for React, Svelte, Vue and Angular [VF: A4-S022, A4-S069]. The companion Workflow SDK (5.1.0) makes TS/JS functions durable and can be self-hosted with Postgres [VF: A4-S106, A4-S071].
- *Strengths:* the most natural fit when the agent lives in a TypeScript application tier and streams to a browser [AJ].
- *Limitations:* a major version roughly every six months (5.0 July 2025, 6.0 December 2025, 7.0 June 2026) [VF: A4-S022]; defaults to Vercel AI Gateway for model access, though direct providers are supported [VF: A4-S069]; Vercel certifications not verified [NPV].
- *Choose when:* the agent is part of a Next.js or TypeScript application [AJ].
- *Avoid when:* the workflow is a back-office regulated process owned by a Python data team [AJ].
- *Competitors:* OpenAI Agents SDK (TS), LangGraph.js, Microsoft Agent Framework.
- *FS note:* route model calls through the firm's gateway (C1), not the Vercel AI Gateway default, when client data is involved [Rec].
- **Tier: Tactical. No flag.**

**Microsoft Agent Framework (Microsoft).**
- *What it is now:* an MIT framework for Python, .NET and Go that separates Agents from graph-based Workflows (sequential, concurrent, handoff, group collaboration), with checkpointing, streaming, HITL, time travel, middleware, OTel observability, declarative YAML agents, A2A and MCP [VF: A4-S066, A4-S012]. 1.0.0 GA was published on 2 April 2026 (some Microsoft posts say 3 April); 1.20.0 shipped on 2 October 2026 [VF: A4-S008, V1-S050, V1-S052].
- *Lineage:* it is the declared enterprise-ready successor to Semantic Kernel and AutoGen; AutoGen is in maintenance mode, with its last release on 30 September 2025 [VF: A4-S066, A4-S068, A4-S021]. Microsoft states that 1.0 comes with stable APIs and a commitment to long-term support [VF: A4-S012, A4-S068].
- *Durability and hosting:* durable agents run through Durable Task or Azure Durable Functions packages that are still beta [VF: A4-S101, A4-S102]. Foundry Hosted Agents is documented as generally available, while the Python Foundry hosting integration is prerelease and resilient task support is in private preview [VF: B-L3-S006].
- *Strengths:* the clearest implementation of the agents-versus-workflows split, with .NET as a first-class language [AJ].
- *Limitations:* durable packages are beta [VF: A4-S101, A4-S102]; integrations are Azure-first [VF: A4-S066]; GA is six months old [VF: A4-S008].
- *Choose when:* the estate is Microsoft or .NET, or Semantic Kernel or AutoGen code must be migrated [AJ].
- *Avoid when:* you need GA durable execution today without adding an external engine [AJ].
- *Competitors:* LangGraph, Google ADK, Strands with AgentCore.
- *FS note:* flag Semantic Kernel and AutoGen references in the estate as Superseded and plan migration; back long-running workflows with a GA durable engine until the durable packages reach GA [Rec].
- **Tier: Strategic, conditional: where Microsoft/Azure or .NET is the primary platform. No flag** (Semantic Kernel and AutoGen carry Superseded).

**Google Agent Development Kit (Google).**
- *What it is now:* an Apache-2.0, code-first framework for building, evaluating and deploying agents and multi-agent hierarchies, with OpenAPI and MCP tools and tool-confirmation HITL [VF: A4-S114]. ADK 2.0 (19 May 2026) added a Workflow Runtime, "a graph-based execution engine for composing deterministic execution flows" with routing, fan-out/fan-in, loops, retry, state, HITL and nested workflows, and a Task API for agent-to-agent delegation [VF: A4-S114, A4-S017]. google-adk 2.11.0 was released on 2 October 2026, with Java, Kotlin, Go and TypeScript ports [VF: A4-S017].
- *Hosting:* Cloud Run or Vertex AI Agent Engine [VF: A4-S114]. Google's generative AI services on Gemini Enterprise Agent Platform are in scope for ISO/IEC 42001 and SOC 2 [VF: A5-S028].
- *Strengths:* an explicit deterministic runtime alongside agents, with evaluation built in [AJ].
- *Limitations:* two major versions in twelve months [VF: A4-S017]; Gemini-optimised, with Google Cloud deployment targets [VF: A4-S114]; library security features and support not verified [NPV].
- *Choose when:* Google Cloud is the primary platform, particularly with Agent Engine [AJ].
- *Avoid when:* runtime parity across clouds is required [AJ].
- *Competitors:* Microsoft Agent Framework, LangGraph, Strands with AgentCore.
- *FS note:* treat Agent Engine as a hyperscaler service under CP2 Q1 (platform controls presumed; confirm per service) [Rec].
- **Tier: Tactical, conditional: default framework in a Google Cloud estate. No flag.**

**Strands Agents and Amazon Bedrock AgentCore (AWS).**
- *What it is now:* Strands is an Apache-2.0, model-driven agent SDK (1.58.1; 1.0 on 15 July 2025) [VF: A4-S018, A4-S115]. AgentCore deploys and operates agents "using any framework and model" (Strands, LangGraph, CrewAI, AutoGen or custom), with Runtime, Memory, Gateway, Identity, Code Interpreter, Browser and OTel observability, and supports the AG-UI protocol [VF: A4-S116]. AgentCore has been GA since 13 October 2025 [VF: V1-S087]. The AgentCore Python SDK is still classified Alpha [VF: A4-S121].
- *Runtime isolation:* each user session gets a dedicated microVM with isolated compute, memory and filesystem, terminated and sanitised at session end; sessions run up to 8 hours per lifecycle, and Runtime Instances on EC2 allow up to 14 days [VF: B-L3-S004]. All AgentCore services support VPC and PrivateLink [VF: B-L3-S004].
- *Certifications:* AgentCore is listed in AWS's SOC 1/2/3 and ISO/IEC 27001:2022 scope and is HIPAA eligible; the SOC 2 report type is not stated [VF: B-L5-S003].
- *Strengths:* separates the runtime decision from the framework decision, and gives strong per-session isolation [AJ].
- *Limitations:* AWS-only, with proprietary service APIs [VF: A4-S116]; session state is ephemeral by default and not intended for long-term durability [VF: B-L3-S004], so it is not a durable workflow engine [AJ]; Runtime pricing not verified [NPV].
- *Choose when:* AWS is the primary cloud and framework-built agents need a managed, isolated runtime [AJ].
- *Avoid when:* runtime portability across clouds is a requirement [AJ].
- *Competitors:* Microsoft Agent Framework with Foundry Hosted Agents, Google ADK with Agent Engine, self-hosted LangGraph.
- *FS note:* keep the workflow definition in a portable framework; scope execution roles tightly; platform controls presumed (CP2 Q1); confirm per service [Rec].
- **Tier: Strategic, conditional: where AWS is your primary cloud (CP3 rule 10; deployment and lock-in at 2 accepted as an existing platform commitment under rule 11). No flag.**

**Temporal (Temporal Technologies).**
- *What it is now:* a durable execution engine whose workflows record each activity so that execution resumes after failures [VF: A4-S019]. Agent frameworks run model calls, tool calls and MCP traffic as Temporal activities (Pydantic AI), offer Temporal integrations for long-running HITL agents (OpenAI Agents SDK), or build on it (Mistral Workflows) [VF: A4-S045, A4-S052, A4-S058]. The Python SDK (`temporalio` 1.34.0, 30 September 2026) dates from March 2022 [VF: A4-S019].
- *Licence and deployment:* the server is MIT-licensed and can be self-hosted, or consumed as Temporal Cloud on 14 AWS and 6 GCP regions including Europe; Cloud runs the same server, so applications move between the two without code changes [VF: B-L3-S002].
- *Certifications and access:* Temporal states SOC 2 Type 2 and HIPAA support with a signed BAA, and offers client-side payload encryption so that Temporal Cloud stores ciphertext; no ISO 27001 claim was found [VF: B-L3-S001]. Temporal Cloud supports SAML 2.0 SSO, SCIM, account roles, namespace permissions, custom roles and exportable audit logs [VF: B-L3-S003].
- *Strengths:* separates reliability from agent logic, and is independent of every model vendor [AJ].
- *Limitations:* it is not an agent framework [AJ]; self-hosting requires Kubernetes, persistence stores and sequential upgrades [VF: B-L3-S002]; workflow code becomes a hard runtime dependency [AJ]; Cloud pricing not verified [NPV]; certification evidence rests on search extracts [VF: B-L3-S001].
- *Choose when:* a regulated workflow must resume after failure without re-calling tools [AJ].
- *Avoid when:* the task is a short, stateless single call [AJ].
- *Competitors:* DBOS (dbos 3.2.0, MIT) and Restate (restate-sdk 1.0.5) [VF: A4-S020, A4-S104]; LangGraph's checkpointer for LangGraph-only estates.
- *FS note:* self-host in-region, or use Temporal Cloud with client-side encryption; request the SOC 2 report before use [Rec].
- **Tier: Strategic. No flag.**

**Not profiled separately.** AutoGen (maintenance mode) and Semantic Kernel are Superseded by Microsoft Agent Framework [VF: A4-S021, A4-S068]. AG2, an independent AutoGen fork (Apache-2.0), continues outside Microsoft [VF: A4-S103]. EthicalAgents and Ragoos were removed from the analysis because they could not be verified (CP1 Q4).

### 3.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3-langgraph | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4.40 | 4.20 | Strategic |
| L3-llamaindex | 3 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3.25 | 3.15 | Tactical |
| L3-pydantic-ai | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 3.60 | 3.55 | Tactical |
| L3-crewai | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3.25 | 3.20 | Tactical |
| L3-openai-agents-sdk | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3.45 | 3.30 | Tactical |
| L3-claude-agent-sdk | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 2 | 2.75 | 2.65 | Experimental |
| L3-mistral-agents | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2.60 | 2.55 | Experimental |
| L3-vercel-ai-sdk | 3 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3.25 | 3.15 | Tactical |
| L3-microsoft-agent-framework | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 3.80 | 3.65 | Strategic |
| L3-google-adk | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 3.45 | 3.35 | Tactical |
| L3-aws-strands-agentcore | 4 | 4 | 4 | 2 | 4 | 3 | 3 | 2 | 3.40 | 3.25 | Strategic |
| L3-temporal | 4 | 4 | 3 | 5 | 4 | 4 | 3 | 4 | 3.90 | 3.90 | Strategic |

**Scoring notes [AJ]:**
- **Libraries under rubric rule 2.** LlamaIndex, Pydantic AI, the OpenAI Agents SDK, the Claude Agent SDK, Vercel AI SDK, Microsoft Agent Framework and Google ADK were scored as self-hosted software: security on project hygiene, enterprise readiness on what they enable in-estate plus support, both capped at 4. Microsoft Agent Framework reaches 4 on enterprise readiness because Microsoft has made a long-term support commitment [VF: A4-S012]. Library security sits at 3 where hygiene evidence is absent; it is not raised by the model vendor's platform certifications.
- **Bundled commercial platforms.** LangGraph is scored with LangSmith Deployment, and CrewAI with AMP, because their records include the managed runtime. LangGraph security is 4, not 5: ISO 27001 scope is unconfirmed (rule 8), and its patched checkpoint advisories show working CVE handling rather than a clean record [VF: A4-S149, B-L3-S007].
- **NPV cap.** Mistral enterprise readiness is capped at 2: no SSO, RBAC or audit evidence [NPV]. CrewAI has SSO and RBAC verified but no SCIM, SLA or audit, so rule 7 gives 3.
- **Hyperscaler rules.** AgentCore takes enterprise readiness 4 under rule 6 (platform controls presumed (CP2 Q1); confirm per service) and security 4 under rule 8 (service in scope, SOC 2 type not stated) [VF: B-L5-S003]. It is Strategic, conditional under rule 10 as AWS's lead agent runtime, with deployment and lock-in at 2 allowed by rule 11 because the condition is an existing AWS commitment. This matches AgentCore Memory (L5) and AgentCore Gateway (C1) on security and deployment.
- **Conflict-of-interest calls on the Claude Agent SDK.** Technical (3, not 4), deployment (3, not 4) and maturity (1, not 2) were each borderline and were resolved against it. Maturity 1 applies the "pre-1.0 or beta" anchor strictly because the package is explicitly classified Alpha [VF: A4-S006]; the OpenAI Agents SDK is also pre-1.0 but has no recorded Alpha classifier, and scores 2. A reviewer may reasonably score both at 1 or both at 2; neither change alters a tier.
- **Calibration.** Six products have a criterion at 2 or below. LangGraph is the only 5 on technical; Temporal and LangGraph are the only 5s on deployment.
- **Tiers versus totals.** AgentCore (3.25) is Strategic below 3.6 by rule 10. Pydantic AI (3.55) is Tactical despite being close to the threshold, because of major-version churn.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| LangGraph | MIT; LangSmith proprietary [VF: A4-S001, A4-S036] | Library; SaaS, BYOC, self-host, on-prem [VF: A4-S037] | LangSmith SOC 2 Type II, HIPAA; ISO 27001 claimed, scope unconfirmed [VF: A4-S034, A4-S149] | LangSmith GCP EU region [VF: A4-S034] | LangChain, independent; US$125M Series B Oct 2025 [VF: A4-S032] |
| LlamaIndex | MIT; LlamaParse proprietary [VF: A4-S002, A4-S127] | Library; LlamaAgents managed or BYO infra [VF: A4-S042] | LlamaParse SOC 2 Type II [VF: A1-S115] | LlamaParse EU region [VF: A1-S115] | LlamaIndex, Inc.; funding conflicting [R: A4-S043] |
| Pydantic AI | MIT [VF: A4-S003] | Library [VF: A4-S003] | Not applicable (library) [AJ] | In-estate [AJ] | Pydantic Services; Series A [VF: A4-S046] |
| CrewAI | MIT; AMP proprietary [VF: A4-S126, A4-S047] | Library; SaaS, VPC, on-prem [VF: A4-S047, A4-S049] | SOC 2 Type 2 (June 2026) [VF: A4-S048] | Not publicly verified [NPV] | crewAI, Inc. [VF: A4-S126] |
| OpenAI Agents SDK | MIT [VF: A4-S005] | Library; hosted Agents API separate [VF: A4-S055] | Not applicable (library) [AJ] | Inherits provider; Agents API US-only [VF: A4-S055] | OpenAI [VF: A4-S005] |
| Claude Agent SDK | MIT repo; use under Commercial Terms [VF: A4-S092, V1-S048] | Self-hosted containers; Managed Agents separate [VF: A4-S122, A4-S124] | Not applicable (library); API certifications in L1 [AJ] | Inherits API route [VF: A4-S123] | Anthropic [VF: A4-S092] |
| Mistral Agents API / Workflows | SDKs Apache-2.0; services proprietary [VF: A4-S125, A4-S061] | SaaS; workers in customer Kubernetes [VF: A4-S058] | Company SOC 2 Type II, ISO 27001, 27701 [VF: A4-S060] | EU by default [VF: A5-S075] | Mistral AI [VF: A4-S125] |
| Vercel AI SDK | Apache-2.0 [VF: A4-S070] | Any Node runtime [VF: A4-S069] | Not publicly verified [NPV] | In-estate [AJ] | Vercel [VF: A4-S070] |
| Microsoft Agent Framework | MIT [VF: A4-S067] | Library; Foundry Hosted Agents [VF: A4-S066, B-L3-S006] | Not applicable (library) [AJ] | Inherits Azure region [AJ] | Microsoft [VF: A4-S067] |
| Google ADK | Apache-2.0 [VF: A4-S114] | Library; Cloud Run, Agent Engine [VF: A4-S114] | Agent Platform ISO 42001, SOC 2 (platform) [VF: A5-S028] | Inherits hosting [AJ] | Google [VF: A4-S114] |
| Strands / AgentCore | SDKs Apache-2.0; AgentCore proprietary [VF: A4-S018, A4-S116] | AWS managed; VPC, PrivateLink [VF: B-L3-S004] | AgentCore in SOC 1/2/3, ISO 27001 scope; HIPAA eligible [VF: B-L5-S003] | Not individually verified [NPV] | AWS [VF: A4-S116] |
| Temporal | Server MIT [VF: B-L3-S002] | Self-host; Cloud on AWS and GCP [VF: B-L3-S002] | SOC 2 Type 2, HIPAA BAA; no ISO 27001 found [VF: B-L3-S001] | Cloud European regions [VF: B-L3-S002] | Temporal Technologies [VF: A4-S019] |

### 3.9 Decision tree

```text
STEP 0 [Rec]: Classify the use case BEFORE choosing a framework
  Is the sequence of steps known in advance (even with branches)?
  ├─ Yes → DETERMINISTIC WORKFLOW. LLM steps are bounded nodes (draft, classify, extract,
  │        judge). Autonomy budget = 0 or 1 model-chosen step.             (most FS use cases)
  └─ No  → Can the open-ended part be isolated as one sub-step with read-only tools?
           ├─ Yes → Workflow with ONE sandboxed agent sub-step (autonomy budget declared)
           └─ No  → Autonomous agent. Requires: sandbox, tool allow-list, per-run budget,
                    approval before any write, and a named risk owner. Re-check STEP 0.

STEP 1 [Rec]: Framework (one per language estate; do not wrap frameworks in a firm abstraction)
  Microsoft / .NET estate, or Semantic Kernel / AutoGen to migrate?
  ├─ Yes → Microsoft Agent Framework (Workflows for the process; Agents for bounded steps)
  └─ No  → Python or TypeScript back end?
           ├─ Yes → LangGraph (default)
           │        alt: Pydantic AI + Temporal/DBOS where typed I/O matters most
           │        alt: Google ADK where Google Cloud / Agent Engine is the platform
           └─ TypeScript application tier streaming to a browser → Vercel AI SDK
              (+ Workflow SDK, or call a back-end LangGraph/Temporal workflow)
  Existing CrewAI or LlamaIndex code → keep, but put the process in Flows / Workflows
  and the regulated steps behind the firm's approval gate.

STEP 2 [Rec]: Durability
  Does the run last longer than one request, wait for a human, or call side-effecting tools?
  ├─ No  → framework checkpointing is enough (or none)
  └─ Yes → LangGraph only?          → Postgres checkpointer (firm-controlled, write-restricted)
           Multi-framework / long?  → Temporal (self-host in-region, or Cloud with
                                       client-side encryption); alt: DBOS, Restate
           Microsoft estate?        → Durable Task (when GA) or Temporal meanwhile

STEP 3 [Rec]: Runtime
  Primary cloud = AWS?   → AgentCore Runtime (microVM per session) for framework-built agents
  Primary cloud = Azure? → Foundry Hosted Agents
  Primary cloud = GCP?   → Vertex AI Agent Engine
  Otherwise / in-estate  → containers on the firm's Kubernetes (LangSmith Deployment self-hosted
                           if LangGraph and Enterprise licence)
  In every case: platform controls presumed (CP2 Q1); confirm per service.

STEP 4 [Rec]: Autonomous harnesses (OpenAI Agents SDK, Claude Agent SDK, Mistral Agents API)
  Only as a sandboxed sub-step, model already approved, traces to the firm's collector,
  no hosted state outside approved residency (no US-only/non-ZDR beta for UK/EU client data).

STEP 5 [Rec]: Checks before go-live
  Path conformance tested? Kill-and-resume test passes without duplicate tool calls?
  Approval gate cannot be bypassed in code? Graph version recorded on each run?
```

### 3.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Orchestration framework (LangGraph, Agent Framework, ADK, Pydantic AI) | **Acceptable** | Open source (MIT/Apache) and self-hostable [VF: A4-S001, A4-S067, A4-S114, A4-S003]; APIs are framework-specific [VF: A4-S039], but rewriting a well-specified workflow is bounded work | None over the framework (plan §12.4); keep prompts, tools, evals and the workflow spec outside it |
| Workflow state and checkpoints | **Manageable** | Checkpoint formats are framework-specific [VF: A4-S039] | Firm-controlled database; export run records to C8 so evidence outlives the framework |
| Durable-execution engine | **Manageable** | Workflow code becomes a hard dependency [AJ]; Temporal's server is MIT and portable between self-host and Cloud [VF: B-L3-S002] | Keep activities thin and framework-neutral; DBOS/Restate as alternatives [VF: A4-S020, A4-S104] |
| Managed agent runtime (AgentCore, Foundry, Agent Engine, LangSmith Deployment) | **Manageable** | Proprietary APIs [VF: A4-S116]; but they host open frameworks [VF: A4-S116] | Containerised agents built on an open framework; runtime as deployment target only |
| Vendor-hosted agent state (Mistral Agents API, OpenAI hosted Agents API, Claude Managed Agents) | **Unacceptable for regulated workflows** | State and transcripts live in the vendor cloud by default [VF: A4-S057, A4-S055, A4-S123] | Store state in the firm's estate; use `store=False` or equivalent where offered [R: A4-S057] |
| Model-locked harness (Claude Agent SDK) | **Manageable only as a sub-step** | Claude-only and governed by Commercial Terms [VF: A4-S027, A4-S092] | Wrap as one replaceable node; keep an equivalent node on a model-agnostic framework |
| Visual builders (Agent Builder) | **Unacceptable** | Agent Builder shuts down on 30 November 2026 [VF: A4-S054] | Workflows as code under version control |

### 3.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23 scope.* PRA SS1/23 applies to banks, building societies and PRA-designated investment firms with internal-model approval, and covers vendor models [VF: R-PRA-SS123, A8-S008]. Principle 1.1(b) says relevant MRM aspects can be applied to material, complex deterministic quantitative methods that are not models [VF: R-PRA-SS123, A8-S008].
- *What that means here.* An agent workflow that informs a business output is a model use requiring inventory, validation and change control, and the deterministic parts of the workflow are not exempt merely because they are code [AJ]. For FCA solo-regulated managers SS1/23 is not binding but is the natural benchmark [AJ].
- *Unit of validation.* The validated object should be the workflow version (graph, prompts, model versions, tool contracts), not the model alone [AJ]. A change to any of these is a change requiring re-evaluation (L9) [Rec].
- *Reproducibility of autonomous runs.* Validation evidence only transfers between runs if the control flow is stable [AJ]. Deterministic graphs make path conformance testable; autonomous loops need their autonomy budget, tool allow-list and trajectory checks to be validated instead [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and places generative and agentic AI expressly outside its scope, leaving their governance to the firm [VF: R-US-MRM, A8-S001, A8-S002]. US supervisors currently signal expectations by observation, such as adoption "with guardrails and human-in-the-loop accountability" [VF: R-US-AGENCY-AI, A8-S004].

**EU AI Act.**
- *Deployer duties.* Article 26 requires deployers of high-risk systems to use them per instructions, assign competent human oversight, keep logs for at least six months and monitor operation; Annex III duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011].
- *Scope.* Attribution commentary is not an Annex III use, so the live duties are AI literacy and transparency [AJ]. The orchestration layer is nevertheless where human-oversight assignment and run logging are implemented, so it should be built to Article 26 grade [Rec].
- *Provider risk.* Repurposing a system into a high-risk purpose can make the firm a provider under Article 25 [VF: R-EUAIA, A8-S011]. A general-purpose agent that teams extend with new tools is the most likely route to that outcome [AJ].

**Operational resilience and outsourcing.**
- *Designations.* DORA's CTPP list and the UK CTP designations include AWS, Google Cloud and Microsoft but no AI model provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. Hyperscaler agent runtimes therefore sit under overseen providers; independent framework vendors' platforms (LangSmith, CrewAI AMP, Temporal Cloud) do not [AJ].
- *Register and notifications.* A managed agent runtime or durable-execution SaaS supporting an important business service belongs in the register of information, and from 18 March 2027 PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062] [AJ].
- *Exit.* SS2/21 expects documented and tested exit plans [VF: R-PRA-SS221, A8-S048]. The open-source framework plus a portable durable engine is the exit route; vendor-hosted agent state is the part that does not exit cleanly [AJ].

**Residency and auditability.**
- *Hosted agent services.* OpenAI's hosted Agents API is US-only with no ZDR at launch [VF: A4-S055]; Claude Managed Agents is excluded from ZDR [VF: A4-S123]; Mistral hosts data in the EU by default [VF: A5-S075]. EU-to-US transfers rely on the DPF or SCCs, with appeal C-703/25 P pending [VF: R-DATA-TRANSFERS, A8-S053].
- *Run record.* FG16/5 expects data location and effective access for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. The checkpoint store and the durable-execution history are records of what the agent saw and did, so they need the same retention, access control and residency as the outputs [AJ].

**Concentration.** IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. Three of the twelve products are model-vendor harnesses that tie orchestration to the vendor's models or cloud [AJ]. Choosing a model-agnostic framework keeps the L1 fallback route open [AJ].

**Human oversight and supervisory direction.** The Bank of England reported that 55% of AI use cases had some autonomous decision-making and 2% were fully autonomous [VF: R-UK-AI-STATEMENTS, A8-S056]. The FPC has asked for further work on agentic AI [VF: R-UK-AI-STATEMENTS, A8-S056]. ESMA expects ex-ante input controls and frequent ex-post output controls, and holds management bodies responsible for decisions taken by AI tools [VF: R-INTL-AI-ASSETMGMT, A8-S059]. An approval interrupt that only a named, authorised human can resume is the L3 implementation of that accountability [AJ].

**Standards.**
- *OWASP Agentic 2026.* The Top 10 for Agentic Applications for 2026 starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042], followed by ASI02 Tool Misuse and Exploitation and ASI03 Identity and Privilege Abuse; ASI08 Cascading Failures and ASI10 Rogue Agents are among the remaining entries reported in a summary [VF: B-L3-S005]. Deterministic graphs mitigate goal hijack by giving the model no control over the next step, and tool allow-lists per node mitigate misuse [AJ]. The 2026 LLM Top 10 ranks Excessive Agency third [VF: R-OWASP-LLM, V2-S056].
- *NIST and ISO.* NIST AI RMF and AI 600-1 provide a neutral risk taxonomy; ISO/IEC 42001 provides the management-system wrapper [VF: R-NIST-AIRMF, A8-S043, A8-S044; R-ISO-42001, A8-S045].

### 3.12 Worked-example slice (POV 3)

**What the commentary agent needs from L3 [AJ].** The plan specifies L3 for this agent as a deterministic workflow graph with a human approval gate, not a free agent. Concretely:

1. **A pinned graph, not a loop.** Nodes: authorise request (C4) → fetch attribution snapshot via read-only tool (L4) → retrieve prior commentary and house style (L6–L8) → **one LLM drafting step** via the gateway (C1) → automated evaluation gate (L9: numeric faithfulness, groundedness, style) → **mandatory human approval interrupt** → hand to release service. The graph version is recorded with every run [Rec].
2. **One judgement step.** The model drafts and explains; it does not choose which tools to call or in what order. If drafting needs a second pass (for example, after an eval failure), that is an explicit, bounded edge back to the drafting node with a retry limit [Rec].
3. **Read-only tools only.** The workflow holds no write, publish or e-mail tool. Release is performed by a separate service after approval, using the approver's identity, not the agent's [Rec].
4. **Durable execution.** The attribution snapshot and retrieval results are recorded activities. If the run fails after fetching data, it resumes from the checkpoint and reuses the recorded snapshot rather than calling the attribution engine again, so the draft and the evidence refer to the same numbers. Implementation: LangGraph with a firm-controlled Postgres checkpointer, or Temporal activities around the same steps [Rec].
5. **Eval gate as a hard edge.** A failed numeric-faithfulness check routes to "returned for revision" or to a human, never to approval [Rec].
6. **Approval that cannot be bypassed.** The approval interrupt can only be resumed by an authorised approver; the decision, approver identity, timestamp and any edits are written to the evidence pack (C8) [Rec].
7. **Evidence.** Each run record holds the graph version, prompt and model versions, the snapshot hash, retrieved document IDs, eval results, approver and final text [Rec].

**What L3 must never do [AJ]:**
- publish, send or file a commentary without a recorded human approval
- call the attribution engine again on resume and mix two data versions in one draft
- let the model choose to call tools outside the node's allow-list, or add tools at run time
- hold run state only in process memory or a container's local disk
- run the drafting step on a hosted agent service whose residency or retention terms are not approved for client data

### 3.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| LangGraph "workflow" | Both workflows and agent loops; 1.x GA; LangGraph Platform renamed LangSmith Deployment [VF: A4-S039, A4-S001, A4-S031] | Strategic default framework [Rec] |
| LlamaIndex "document agents" | Framework 0.x with Workflows; vendor focus moved to LlamaParse (formerly LlamaCloud) [VF: A4-S002, A4-S117, A4-S042] | Tactical: retrieval toolkit; LlamaParse in L8 [Rec] |
| Pydantic AI "type-safe" | v2; durability via Temporal, DBOS or Prefect [VF: A4-S003, A4-S045] | Tactical: typed agent step [Rec] |
| CrewAI "multi-agent" | Crews plus Flows; AMP platform (earlier materials: CrewAI Enterprise) [VF: A4-S050, V1-S075] | Tactical: Flows for any regulated process [Rec] |
| Agent SDK (OpenAI logo) | OpenAI Agents SDK (0.x); hosted Agents API beta; Agent Builder shuts 30 Nov 2026 [VF: A4-S005, A4-S055, A4-S054] | Tactical: sandboxed agent sub-step [Rec] |
| Agent SDK (Anthropic logo) | Claude Agent SDK, renamed from Claude Code SDK; Alpha; Commercial Terms [VF: A4-S028, A4-S006, A4-S092] | Experimental: sandboxed sub-step only (conflict of interest disclosed) [Rec] |
| Mistral "Agents SDK" | No such product: Agents API plus Workflows on Temporal (beta) [VF: A4-S057, A4-S058] | Experimental; relabel "Mistral Agents API (+ Workflows)" [Rec] |
| AI SDK (triangle logo) | Vercel AI SDK 7; Workflow SDK [VF: A4-S022, A4-S071] | Tactical: TypeScript application tier [Rec] |
| Microsoft Agent Framework | GA April 2026; successor to Semantic Kernel and AutoGen [VF: A4-S008, A4-S068] | Strategic, conditional: Microsoft/.NET estates [Rec] |
| (absent) | Google ADK 2.0 Workflow Runtime; Strands + AgentCore; Temporal [VF: A4-S114, A4-S116, A4-S019] | ADK Tactical (Google Cloud default); AgentCore Strategic, conditional (AWS primary cloud); Temporal Strategic as durability substrate [Rec] |

**H2 (an "agent framework" is not one layer; distinguish deterministic workflows from autonomous agents). Provisional view; verdict in synthesis.**

The evidence supports the hypothesis, with one refinement.

- **Every major framework now ships both modes**, and several vendors document the split explicitly: LangGraph (deterministic logic and LLM decisions in one graph), Microsoft Agent Framework (Agents versus Workflows), CrewAI (Flows versus Crews, with Flows recommended as the outer process), Google ADK 2.0 (Workflow Runtime), LlamaIndex Workflows, Mistral Workflows and Vercel's Workflow SDK [VF: A4-S039, A4-S066, A4-S050, A4-S114, A4-S041, A4-S058, A4-S071]. Anthropic's guidance separates workflows from agents in the same terms [VF: A4-S030].
- **Durability is separating from both.** Pydantic AI v2 removed its own graph persistence and delegates durability to Temporal, DBOS or Prefect; the OpenAI Agents SDK integrates Temporal and DBOS; Mistral built Workflows on Temporal [VF: A4-S044, A4-S045, A4-S052, A4-S058].
- **Runtimes are separating from frameworks.** AgentCore hosts agents from several frameworks with per-session isolation [VF: A4-S116, B-L3-S004]; Foundry Hosted Agents accepts agents built with any framework [VF: B-L3-S006].
- **Visual workflow builders are retreating.** OpenAI is retiring Agent Builder and points code users to the SDK [VF: A4-S054].

The refinement is that the split is not two products but two modes inside one framework, so it should be drawn as two sub-layers of L3 rather than as two layers with separate vendors [AJ]. The counter-evidence is that autonomous harnesses (the OpenAI and Claude agent SDKs, Mistral's Agents API) remain single-mode and are moving fastest [VF: A4-S053, A4-S027, A4-S057].

**Provisional recommendation.** Redraw L3 as three stacked concerns: (1) **deterministic workflow orchestration** (graph, state, approvals) as the default for enterprise processes; (2) **bounded autonomous agent steps**, admitted per use case with a declared autonomy budget; and (3) **durable execution and managed runtime** as a reliability substrate beneath both [AJ]. This also answers the pair-6 tension: most enterprise "agents" should be deterministic workflows with one judgement step, and guardrails cannot rescue a process that should never have been autonomous [AJ]. **Provisional; verdict in synthesis.**
