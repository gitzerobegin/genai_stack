# Stage A notes: stream A4 (L3 agent frameworks and orchestration, L2 inference, serving and model access)

| | |
|---|---|
| **As of** | 7 October 2026 |
| **Records** | 23 in `products.json` (L3: 9 graphic tiles + 3 additions; L2: 9 graphic tiles + 2 additions) |
| **Sources** | 128 (`sources.csv`), all archived under `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A4/` |
| **Disclosure** | The author is an Anthropic model. The Claude Agent SDK was profiled with the same rubric and the same scepticism as its peers. Its limitations and licence terms are recorded in full. |

**Research-environment caveat.** The shared web-search budget ran out part-way through this stream, after LangChain, LlamaIndex, Pydantic, CrewAI, OpenAI and Mistral had been researched. The rest of the evidence comes from direct fetches of hosts that were reachable:

- PyPI JSON
- the npm registry
- raw.githubusercontent.com (vendor-authored READMEs, docs-source repositories and LICENCE files)
- code.claude.com, platform.claude.com and www.anthropic.com
- one cloud.google.com blog post

Vendor websites and trust centres were blocked, so several L2 enterprise fields are recorded as Not publicly verified. See (e).

---

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| LangGraph – workflow | LangGraph 1.2.14 (MIT), GA since 1.0 on 17 October 2025. It covers both deterministic workflows and agent loops, with durable execution and HITL. Its managed runtime was renamed from **LangGraph Platform** to **LangSmith Deployment** on 14 October 2025. | Renamed (platform); descriptor incomplete | A4-S001, A4-S031, A4-S033, A4-S039 |
| LlamaIndex – document agents | The OSS framework is at 0.14.25, with Workflows as a standalone package (2.25.0). The vendor says its primary focus has moved to **LlamaParse**, the product formerly called LlamaCloud (parsing, extraction and LlamaAgents document agents). The framework is still available. | Mispositioned (commercial focus is L8); Renamed (LlamaCloud→LlamaParse) | A4-S002, A4-S013, A4-S117, A4-S042 |
| Pydantic AI – type-safe | Pydantic AI 2.54.0. v2.0 shipped on 23 June 2026 and removed graph persistence; durability now comes through Temporal, DBOS or Prefect capabilities. The 1.x line is still patched. | No change (major version moved) | A4-S003, A4-S044, A4-S045 |
| CrewAI – multi-agent | CrewAI 1.15.24 (MIT), with 1.0 on 20 October 2025. It has two modes: **Crews** (autonomous) and **Flows** (event-driven, deterministic). The commercial platform is **CrewAI AMP**, formerly CrewAI Enterprise. | Renamed (enterprise product); descriptor incomplete | A4-S004, A4-S050, A4-S049 |
| Agent SDK (OpenAI logo) | OpenAI Agents SDK: openai-agents 0.23.1 and @openai/agents 0.19.0 (MIT). The harness and sandbox update came on 15 April 2026. It is a different product from the hosted **Agents API** (beta since 10 September 2026) and from **Agent Builder**, which shuts down on 30 November 2026. | Duplicated label (A7); Version label n/a | A4-S005, A4-S053, A4-S055, A4-S054 |
| Agent SDK (Anthropic logo) | Claude Agent SDK: claude-agent-sdk 0.2.164 (classified Alpha) and @anthropic-ai/claude-agent-sdk 0.3.293. It was **renamed from Claude Code SDK** on 29 September 2025 and the old package is deprecated. Use is governed by Anthropic's Commercial Terms, even though the Python repository LICENCE is MIT. | Renamed; Duplicated label (A7) | A4-S006, A4-S011, A4-S028, A4-S027, A4-S092 |
| Mistral – Agents SDK | There is no distinct "Agents SDK". There is the **Agents API**, called through the general `mistralai` SDKs (Python 3.1.0, TS 2.7.0), and **Mistral Workflows**, a separate SDK built on Temporal (3.15.0, beta). | Not publicly verified (as named); Mispositioned | A4-S057, A4-S007, A4-S058, A4-S061 |
| AI SDK – AI SDK (triangle logo) | **Vercel AI SDK**, npm package `ai`, at 7.0.131 (Apache-2.0); 7.0 released 25 June 2026. By default it routes through Vercel AI Gateway. The companion Workflow SDK, 5.1.0, adds durability. | No change (identity resolved, A15) | A4-S022, A4-S069, A4-S106 |
| Agent Framework – Microsoft | Microsoft Agent Framework 1.20.0 (MIT), GA at 1.0.0 on 2 April 2026. It is the declared successor to **Semantic Kernel** and **AutoGen**, and AutoGen is now in maintenance mode. | No change (supersedes SK/AutoGen) | A4-S008, A4-S012, A4-S068, A4-S066 |
| Hugging Face – models & APIs | One tile covers four things: the Hub, **Inference Providers** (a router with pass-through pricing), **Inference Endpoints** (managed dedicated serving on vLLM, SGLang, TGI, llama.cpp or TEI), and **TGI**, which is in **maintenance mode** "as of 12/11/2025". | Duplicated (several products); Deprecated (TGI) | A4-S075, A4-S081, A4-S073, A4-S072 |
| OpenRouter – multi-provider | It is still a router, and it now has gateway-style controls: guardrails (budgets, allowlists, ZDR, data regions), EU/US in-region routing, and SSO/SCIM on Enterprise plans. | No change (scope widened toward C1) | A4-S111, A4-S109, A4-S110 |
| Together AI – open-source cloud | The SDK is at 2.40.0. The SDK shows inference, fine-tuning, GPU clusters and container deployments (beta). Enterprise facts are not verified. | Not publicly verified (enterprise facts) | A4-S093 |
| Fireworks AI – fast inference | The SDK is at 1.2.20. The SDK shows deployments, fine-tuning and batch inference. Enterprise facts are not verified. | Not publicly verified (enterprise facts) | A4-S094 |
| Cerebras – ultra-scale cloud | Cerebras is a chip and system vendor (WSE-3, CS-3) that also runs an inference API, and it offers on-premise systems. IPO and funding status are not verified. | Mispositioned (descriptor omits hardware) | A4-S095 |
| Ollama – run locally | The local runtime is MIT-licensed. **Ollama Cloud** now hosts larger models and offers OpenAI- and Anthropic-compatible APIs. The cloud features can be switched off. | Mispositioned (no longer local-only) | A4-S084, A4-S085, A4-S086 |
| LM Studio – desktop app | It is still a desktop app with the lms CLI (MIT). The app's licence and commercial-use terms are not verified. | Not publicly verified (licence) | A4-S087, A4-S088, A4-S016 |
| vLLM – high-throughput | vLLM 0.31.0 (Apache-2.0), released 5 October 2026, about every two weeks. It has a governance process with a TSC under "Linux Foundation Project Governance". | No change | A4-S009, A4-S063, A4-S064 |
| SGLang – efficient engine | SGLang 0.5.21 (Apache-2.0). It is hosted by the **LMSYS** non-profit, and RadixArk appears as a collaborator. | No change | A4-S010, A4-S065 |

---

## (b) Ambiguities owned by this stream

### A7: three "Agent SDK" tiles

Resolved as three separate products from three vendors.

- **OpenAI Agents SDK.** Open source (MIT) and provider-agnostic. It supports the OpenAI Responses and Chat Completions APIs and "100+ other LLMs" [VF: A4-S005, A4-S120].
  - OpenAI also has two other agent products that should not be confused with it:
    - the hosted **Agents API**: public beta, managed Codex harness, US-only residency, no ZDR [VF: A4-S055]
    - **AgentKit/Agent Builder**: deprecation announced 3 June 2026, shutdown 30 November 2026 [VF: A4-S054]
- **Claude Agent SDK.** Embeds Claude Code's agent loop as a library and spawns a Claude Code CLI subprocess for each session [VF: A4-S027, A4-S122].
  - Renamed from the Claude Code SDK [VF: A4-S028, A4-S011].
  - Its hosted counterpart is Claude Managed Agents (beta) [VF: A4-S124].
- **Mistral.** See A17.

### A15: "AI SDK" (triangle logo)

Resolved as the **Vercel AI SDK**. The npm package `ai` describes itself as "AI SDK by Vercel" [VF: A4-S022]. The LICENCE reads "Copyright 2023 Vercel, Inc.", Apache-2.0 [VF: A4-S070].

### A17: "Mistral Agents SDK"

Not found as a distinct product.

- Mistral offers the **Agents API**, which covers Agents & Conversations, connectors, and handoffs that run server-side or client-side [VF: A4-S057].
- It is reached through the general client SDKs: `mistralai` with an `agents` extra, and `@mistralai/mistralai` [VF: A4-S007, A4-S025].
- Mistral separately offers **Mistral Workflows** (`mistralai-workflows`, Apache-2.0, beta), built on Temporal. Mistral hosts the control plane and the customer runs the workers [VF: A4-S058, A4-S061].
- Recommendation for Stage B: relabel the tile "Mistral Agents API (+ Workflows)".

### A19: Hugging Face product split

Resolved into four products:

1. **Hub**: SOC 2 Type 2, SSO/SCIM, audit logs and EU storage region on Team and Enterprise plans [VF: A4-S074, A4-S080, A4-S079, A4-S078].
2. **Inference Providers**: a router to partner clouds with no HF markup. It does not store request or response bodies, and keeps logs for up to 30 days [VF: A4-S075, A4-S076, A4-S077].
3. **Inference Endpoints**: managed dedicated serving on AWS, Azure or GCP, billed per minute. Engines are vLLM, TGI, SGLang, llama.cpp and TEI. It holds SOC 2 Type 2 and offers AWS PrivateLink [VF: A4-S081, A4-S083, A4-S082].
4. **TGI**: in maintenance mode. HF recommends vLLM or SGLang instead [VF: A4-S072, A4-S073]. The maintenance-mode date is printed as "12/11/2025", which could be 11 December or 12 November 2025.

---

## (c) Hypothesis evidence (no verdicts)

### H1: serving vs inference optimisation vs gateway/routing

- **Optimisation layers describe themselves as separate from, and above, serving engines.**
  - NVIDIA Dynamo calls itself "the orchestration layer above inference engines — it doesn't replace SGLang, TensorRT-LLM, or vLLM". Its features are disaggregated serving, KV-aware routing, multi-tier KV cache and an SLA planner. It is at 1.5.1 and classed as beta [VF: A4-S090, A4-S098].
  - llm-d says: "Model servers like vLLM and SGLang handle efficiently running large language models … llm-d provides … orchestration and optimizations above model servers". It is a CNCF sandbox project founded by Red Hat, Google Cloud, IBM Research, CoreWeave and NVIDIA [VF: A4-S089].
  - Google launched llm-d on 20 May 2025 alongside the GKE Inference Gateway (Gateway API Inference Extension) [VF: A4-S062].
  - LMCache calls itself "A KV Cache Management Layer for Scalable LLM Inference". It joined the PyTorch Foundation in October 2025, and Dynamo integrated it in September 2025 [VF: A4-S091, A4-S105].
- **Optimisation techniques also ship inside the engines.**
  - vLLM lists quantisation (FP8, MXFP4, NVFP4, INT4/8, GPTQ, AWQ, GGUF), speculative decoding (n-gram, suffix, EAGLE, DFlash), prefix caching and disaggregated prefill/decode/encode as built-in features [VF: A4-S063].
  - SGLang lists RadixAttention, PD disaggregation, speculative decoding and FP4/FP8/INT4 quantisation [VF: A4-S010].
  - TensorRT-LLM is "an open-sourced library for optimizing LLM inference" with quantisation and speculative decoding (1.2.1, beta) [VF: A4-S099].
- **Managed services wrap the engines.**
  - Hugging Face Inference Endpoints describes three components (model weights, inference engine, production infrastructure) and offers vLLM, SGLang, TGI and llama.cpp as selectable engines [VF: A4-S081].
- **Routers and gateways are now adding governance features.**
  - OpenRouter guardrails: budget limits, model and provider allowlists, ZDR enforcement, data regions [VF: A4-S111]. It also offers EU/US in-region routing [VF: A4-S109].
  - LiteLLM describes itself as an "open source AI Gateway" with virtual keys, spend tracking, guardrails and load balancing [VF: A4-S097].
  - Hugging Face Inference Providers routes across providers with pass-through billing [VF: A4-S075, A4-S076].
- **Framework and observability vendors are adding gateways.**
  - Vercel AI SDK defaults to Vercel AI Gateway [VF: A4-S069].
  - Pydantic moved its AI Gateway into Logfire, adding failover, DLP and spend caps [VF: A4-S046].
  - LangChain announced an LLM Gateway at Interrupt 2026 [VF: A4-S040, conf medium].
- **The local runtimes now have hosted options.**
  - Ollama now offers cloud models [VF: A4-S084].

### H2: deterministic workflows vs autonomous agents

- **Vendor guidance.** Anthropic distinguishes "Workflows … where LLMs and tools are orchestrated through predefined code paths" from "agents … where LLMs dynamically direct their own processes and tool usage" (19 December 2024) [VF: A4-S030].
- **LangGraph.** "You can combine hand-coded, deterministic logic with LLM-driven decisions in a single graph."
  - Checkpointers support HITL, time travel and fault tolerance.
  - The Functional API (@entrypoint/@task) re-runs from the start and loads saved task results.
  - Side effects must be wrapped in tasks [VF: A4-S039].
- **Microsoft Agent Framework.** Separates Agents from graph-based Workflows (sequential, concurrent, handoff, group collaboration) with checkpointing, HITL and time-travel [VF: A4-S066]. Durable agents run through Durable Task and Azure Durable Functions packages, which are still in beta [VF: A4-S101, A4-S102].
- **CrewAI.** Flows are the "manager"/"process definition" with exact sequencing and state. Crews are for autonomous collaboration where some variation in output is acceptable. The vendor recommends Flows orchestrating Crews for high-stakes pipelines [VF: A4-S050].
- **Pydantic AI.** v2 removed `pydantic_graph.persistence` because consistent snapshotting is hard with parallel execution. Durability is a capability backed by Temporal, DBOS or Prefect, with five engines co-maintained with their vendors [VF: A4-S044, A4-S045].
- **LlamaIndex.** Workflows is an "event-driven, async-first, step-based" engine that has been a standalone package since June 2025 [VF: A4-S013, A4-S041].
- **OpenAI Agents SDK.** Offers Temporal and DBOS integrations for "durable, long-running workflows, including human-in-the-loop tasks" [VF: A4-S052]. Sandbox snapshot and rehydration resume runs in a fresh container [VF: A4-S053]. OpenAI is retiring its visual workflow builder, Agent Builder, and points code users to the SDK [VF: A4-S054].
- **Claude Agent SDK.** An autonomous agent loop that runs one subprocess per session. Session transcripts sit on local disk and are lost on restart unless mirrored to a durable store [VF: A4-S122]. It ships no workflow engine.
- **Mistral.** Workflows is built on Temporal's durable execution engine, extended with streaming, multi-tenancy and observability [VF: A4-S058]. Durable agents are in public preview [VF: A4-S057].
- **Google ADK 2.0.** Its "Workflow Runtime" is "a graph-based execution engine for composing deterministic execution flows" with retry, state and HITL [VF: A4-S114].
- **Vercel.** The Workflow SDK "makes TypeScript and JavaScript functions durable". It can be self-hosted with Postgres [VF: A4-S071].
- **Durable-execution engines, current versions.**
  - Temporal Python SDK 1.34.0 (MIT) [VF: A4-S019]
  - DBOS 3.2.0, "ultra-lightweight durable execution" [VF: A4-S020]
  - Restate SDK 1.0.5 [VF: A4-S104]

---

## (d) Material products missing from the graphic

The following were added to `products.json` with `original_label: null`:

- **L3: Google ADK.** A code-first framework at 2.0 with a deterministic Workflow Runtime. It deploys to Vertex AI Agent Engine or Cloud Run [A4-S114, A4-S017].
- **L3: AWS Strands Agents + Bedrock AgentCore.** A framework-agnostic managed agent runtime with Memory, Gateway and Identity [A4-S115, A4-S116, A4-S121].
- **L3: Temporal.** A durable-execution substrate used by Pydantic AI, the OpenAI Agents SDK and Mistral Workflows [A4-S019, A4-S045, A4-S052, A4-S058].
- **L2: NVIDIA Dynamo.** An inference orchestration and optimisation layer [A4-S090, A4-S098].
- **L2: llm-d.** A CNCF sandbox project for Kubernetes-native distributed inference [A4-S089, A4-S062].

The following were noted but not added. Evidence was insufficient or they belong to another stream:

- Amazon Bedrock, Azure AI Foundry and Vertex AI as managed model access. No primary pages could be fetched.
- Groq (groq SDK 1.7.0) [A4-S100].
- TensorRT-LLM [A4-S099].
- LMCache [A4-S091].
- LiteLLM [A4-S097]. This is C1, stream 6.
- AG2, an independent AutoGen fork: ag2 1.1.2, Apache-2.0 [A4-S103].
- DBOS and Restate [A4-S020, A4-S104].

---

## (e) Gaps: what could not be verified, and why

1. **Together AI, Fireworks AI, Cerebras.**
   - Not verified: SOC 2, ISO and HIPAA status; retention and ZDR; EU region; SSO and RBAC; pricing; funding.
   - Not verified: Cerebras IPO and funding status.
   - Why: vendor sites and trust centres were blocked by egress policy, and the shared web-search budget was exhausted before these products were reached.
2. **OpenRouter.** Certifications and funding are not verified. The credit-purchase fee percentage is rendered dynamically in the docs source and was not captured.
3. **LM Studio.** The desktop app's licence and commercial-use terms are not verified. Only the MIT licence of the lms CLI is confirmed.
4. **vLLM.** PyTorch Foundation hosting is not confirmed from a primary page because pytorch.org was blocked. The governance doc only references "Linux Foundation Project Governance".
5. **SGLang and RadixArk.** The corporate relationship between RadixArk and SGLang is not verified.
6. **Ollama.** The server/app version is not verified, since GitHub releases were blocked. Only the Python client version (0.6.3) is confirmed.
7. **Funding.**
   - CrewAI Series B (about US$20M, April 2026) rests only on aggregators.
   - LlamaIndex funding has conflicting secondary figures.
   - No 2025 or 2026 funding was found for Pydantic. Only the US$12.5M Series A is confirmed.
   - Vercel, Hugging Face and OpenRouter funding were not checked.
8. **LangSmith ISO 27001.** It is claimed on the enterprise page but missing from the EU-residency announcement. This needs checking at trust.langchain.com.
9. **Vendor certifications not covered here.** Mistral's company-level certifications (SOC 2 Type II, ISO 27001/27701) are recorded, but scope and dates were not seen. Certifications for Vercel, Temporal and AgentCore were not retrieved.
10. **Search-tool extracts.** Every source with access status `extract` came through the search tool. Facts that rest on them alone are capped at `conf: medium`.
