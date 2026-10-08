## 2. Inference, serving and model access

> **Executive summary.** This layer turns a model choice (L1) into a callable, capacity-backed endpoint in a known place, and gives applications a governed way to reach it [AJ]. The graphic shows nine tiles as one undifferentiated "inference" box. The evidence now shows three distinct jobs. **Serving engines** run the model: vLLM (Apache-2.0, PyTorch Foundation-hosted since 7 May 2025) and SGLang (Apache-2.0, LMSYS-hosted, with RadixArk as commercial steward since May 2026) [VF: A4-S009, A4-S146, A4-S010, A4-S147]. **Inference optimisation and orchestration** sits above them: NVIDIA Dynamo calls itself "the orchestration layer above inference engines", and llm-d (a CNCF sandbox project) provides orchestration "above model servers" [VF: A4-S090, A4-S089]. **Model access** is reached through managed inference clouds (Together AI, Fireworks AI, Cerebras, Hugging Face Inference Endpoints), routers (OpenRouter, Hugging Face Inference Providers) and hyperscaler model services (Amazon Bedrock, Microsoft Foundry, Google Cloud) [VF: A4-S131, A4-S135, A4-S139, A4-S081, A4-S111, A4-S075, A5-S010]. Status has moved too: Stripe agreed to acquire OpenRouter on 19 August 2026, with closing pending on 8 October 2026 [VF: V1-S059, V1-S060]; Hugging Face's TGI repository was archived on 21 March 2026 [VF: V1-S054]; Cerebras priced its IPO on 13 May 2026 [VF: A4-S137]; Ollama now runs cloud models and is no longer local-only [VF: A4-S084]. **Recommendation:** for regulated workloads, default to managed model access in an approved region through the hyperscaler estate you already operate, called only through the firm's gateway (C1); add a private open-weight route on vLLM only where capacity, residency or exit planning justify it, and treat self-hosting as a capacity and operating-model decision rather than a cost saving [Rec].

### 2.1 Responsibility

**The problem this layer owns.** It makes a chosen model available as an endpoint with known capacity, latency, location and data handling [AJ]. That breaks down into three jobs, which H1 proposes to separate:

- **Model serving.** Loading weights onto accelerators and executing inference efficiently: batching, memory management of the KV cache, quantisation and an API surface. vLLM and SGLang are the open engines here; both expose OpenAI-compatible APIs [VF: A4-S063, A4-S010].
- **Inference optimisation and orchestration.** Coordinating many engine replicas: routing requests to the replica that already holds the relevant KV cache, separating prefill from decode, tiering the KV cache to CPU or storage, and autoscaling against a latency target. NVIDIA Dynamo and llm-d are the dedicated products [VF: A4-S090, A4-S089]; LMCache is a KV-cache layer that Dynamo integrates [VF: A4-S091].
- **Model access.** Obtaining someone else's served model under a contract: per-token serverless APIs, dedicated endpoints, reserved capacity, and routers that aggregate many providers behind one API [VF: A4-S131, A4-S135, A4-S113].

**Hand-offs.** Above this layer sits the gateway (C1), which every application call passes through; C1 owns routing policy, fallback lists, budgets, inline guard calls and the request log [AJ]. The C1 section covers the gateway products; this section does not repeat them. Below this layer sits L1: the model families and their licences. Alongside it: C3 decides what data may reach which endpoint, C6 consumes capacity and token cost, C7 owns weight provenance and engine patching, and L9 consumes per-call telemetry and qualifies fallback models [AJ].

**What the layer does not own.** It does not own the choice of model family (L1), the policy on which route a request takes (C1), or the decision that a workload may use client data (C3 and C8) [AJ]. Routers such as OpenRouter now carry budgets, allowlists, ZDR enforcement and regional routing [VF: A4-S111, A4-S109], which overlaps with C1. This section treats them as model-access sources behind the firm's gateway, consistent with C1 [AJ].

### 2.2 Why it matters

When this layer is badly designed, three things fail, usually at once [AJ].

- **Data goes somewhere nobody approved.** Where a prompt is processed is a property of the endpoint, not of the model. The same model can be processed globally, in a data zone or in one geography, depending on the deployment type selected [VF: B-L2-S006]. A provider's defaults can also store prompts: Together AI stores prompts and responses, and may use them for product improvement, unless zero data retention (ZDR) is switched on [VF: A4-S130].
- **Capacity runs out at the worst moment.** Serverless per-token APIs carry no reserved capacity; Together AI's serverless tier has no SLA, while its Provisioned Throughput does [VF: A4-S131]. On Vertex AI, traffic above a Provisioned Throughput quota goes to the global endpoint by default, which removes the residency guarantee unless overridden [VF: B-L2-S008].
- **Exit is impossible in practice.** If applications call one vendor's SDK and endpoint directly, a change of provider becomes a code programme rather than a configuration change [AJ].

**Illustrative scenario [AJ].** A fund-reporting team pilots the commentary drafter against a fast serverless open-model endpoint through a convenient hosted router, because it "just worked" during the proof of concept. Nobody checks the router's processing region or the downstream provider's retention default. Six months later the pilot is live for 40 funds. At month-end, every fund's draft is requested within the same two-hour window after attribution runs complete, and the serverless endpoint starts returning rate-limit errors. The router falls back to another provider, which is outside the approved region and stores prompts by default. Drafts are produced on time, so nobody notices for a week. Then third-party risk asks for the list of sub-processors that saw the month's client holdings, and the team cannot produce it. Everything had to be re-assessed, and the route was suspended for the next cycle. Three controls would have prevented it: an in-region managed endpoint with reserved capacity sized for the month-end peak, a fallback list restricted to qualified in-region endpoints, and the gateway, not the router, deciding the route. The scenario is invented; it is not a reported incident.

### 2.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Time to first token (TTFT), p95 | Time from request to first streamed token | Per use case; interactive drafting typically seconds, batch less critical | Gateway timing per route; engine metrics |
| Inter-token latency / output tokens per second, p95 | Streaming speed per request | Per use case | Engine metrics (self-hosted); gateway timing (managed) |
| Availability per route | Successful responses over attempted, excluding client errors | Set per route; at least the business SLA of the consuming process | Gateway logs, reconciled to provider status |
| Capacity headroom at peak | Reserved or provisioned throughput minus observed peak demand | Positive at the forecast month-end peak plus a margin | Capacity plan vs gateway peak-hour metrics |
| Throttle / 429 rate | Share of calls rejected for rate or quota | Near zero on reserved routes; alert on any sustained rate | Gateway logs |
| Fallback activation rate | Share of calls served by a fallback endpoint | Low and explained; every activation logged | Gateway route records |
| In-region processing rate | Share of calls with verified processing location inside the approved region | 100% for client-data routes | Processing-region evidence (e.g. CloudTrail inference region [VF: B-L2-S005]) joined to gateway logs |
| ZDR coverage | Share of client-data calls to endpoints with contractually confirmed ZDR or equivalent | 100% for client-data routes | Third-party register and endpoint configuration |
| Cost per 1M tokens and per task | Loaded cost including reserved capacity utilisation | Budget per use case | C6 attribution |
| GPU utilisation (self-hosted) | Busy accelerator time over paid time | High enough to beat the managed alternative | Cluster telemetry |
| Engine patch latency (self-hosted) | Days from a security advisory to deployed fix | Within the firm's vulnerability SLA | C7 vulnerability management against advisories [VF: B-L2-S004] |
| Exit drill time | Time to move a route to the qualified alternative | Hours, by configuration only | Scheduled drill through C1 |

### 2.4 How it works

**Serving mechanics.** A serving engine loads weights, schedules many requests into shared batches, and keeps each request's attention state (the KV cache) in accelerator memory [AJ]. vLLM's documented features show what "serving" now includes: PagedAttention, continuous batching, prefix caching, quantisation (FP8, MXFP4, NVFP4, INT4/8, GPTQ, AWQ, GGUF), speculative decoding (n-gram, suffix, EAGLE, DFlash) and disaggregated prefill, decode and encode [VF: A4-S063]. SGLang lists RadixAttention prefix caching, prefill/decode disaggregation, speculative decoding and FP4/FP8/INT4 quantisation [VF: A4-S010]. TensorRT-LLM, NVIDIA's engine, describes itself as a library for optimising LLM inference with quantisation and speculative decoding [VF: A4-S099].

**Optimisation and orchestration mechanics.** Above the engines, the orchestration products work at the level of a fleet [AJ]:
- *KV-aware routing.* llm-d routes on prefix-cache hits and load rather than round-robin [VF: A4-S089, A4-S062]; Dynamo provides KV-aware routing and a Kubernetes Gateway API Inference Extension plugin [VF: A4-S090].
- *Disaggregation.* Both separate prefill from decode across instances [VF: A4-S089, A4-S090].
- *KV-cache tiering.* llm-d offloads to CPU or disk with global indexing; Dynamo's KV Block Manager offloads GPU to CPU to SSD to remote storage; LMCache runs as a separate daemon so the cache survives an engine crash [VF: A4-S089, A4-S090, A4-S091].
- *SLO-driven scaling.* Dynamo's planner right-sizes pools against latency targets; llm-d offers SLO-aware autoscaling [VF: A4-S090, A4-S089].

**Access mechanics.** Managed access comes in four contract shapes, and the shape decides capacity and data location [AJ]:
- *Serverless per-token*: shared capacity, often no SLA (Together AI serverless) [VF: A4-S131].
- *Dedicated endpoints*: per-replica billing whether or not traffic arrives (Together AI); per GPU-second with scale to zero (Fireworks); per-minute instance billing on AWS, Azure or GCP (Hugging Face Endpoints) [VF: A4-S131, A4-S135, A4-S083].
- *Reserved or provisioned throughput*: Together AI PTU with an uptime SLA; Microsoft Foundry provisioned throughput units (PTUs); Vertex AI Provisioned Throughput [VF: A4-S131, B-L2-S006, B-L2-S008].
- *Routers*: one API across many providers, with provider prices passed through (OpenRouter adds a fee on credit purchases; Hugging Face Inference Providers adds no markup) [VF: A4-S113, V1-S062, A4-S076].

```text
                    Applications / L3 workflows
                               │  one endpoint, workload identity (C4)
                               ▼
     ┌──────────────── C1 AI traffic gateway (control plane) ────────────────┐
     │ route policy · region pin · fallback list · budgets · guards · logs   │
     └───────┬──────────────────────┬───────────────────────┬────────────────┘
             │ (A) managed access   │ (B) router (non-     │ (C) private route
             ▼                      ▼     confidential)    ▼
   Hyperscaler model service   OpenRouter / HF        ┌─ Optimisation / orchestration ─┐
   (Bedrock geo profile,       Inference Providers    │ llm-d or Dynamo: KV-aware      │
    Foundry Data Zone,              │                 │ routing, PD split, KV tiering, │
    Vertex regional) or             ▼                 │ SLO autoscaling (optional)     │
   inference cloud dedicated   many providers        └───────────────┬────────────────┘
   endpoint (Fireworks BYOC,   (processing location                  ▼
   Together EU dedicated)       per provider)            Serving engine: vLLM / SGLang
             │                                                       │
             ▼                                                       ▼
        Provider GPUs in approved region                    Own / private-cloud GPUs
                        (L1 model weights below every route)
```

The three sub-layers of H1 are visible in the diagram: route (C) has all three (engine, optimisation, access through the gateway); routes (A) and (B) buy serving and optimisation as a service and keep only access [AJ]. The gateway is drawn above L2 because it governs every route, including routes that bypass L2 products entirely [AJ].

### 2.5 Enterprise design principles

**Security**
- Treat model weights and engine images as supply-chain inputs. vLLM published several 2026 advisories in which a malicious model repository or crafted input could execute code, including CVE-2026-22778 (critical, fixed from 0.14.1) and CVE-2026-27893, where two model files hard-coded `trust_remote_code=True` (fixed in 0.18.0) [VF: B-L2-S004]. SGLang's CVE-2026-3059 (critical, unauthenticated code execution through the multimodal ZMQ broker, 0.5.9 and below) lists no patched version in the GitHub advisory [VF: B-L2-S009], while NVD gives the vulnerable range as 0.5.5 to 0.5.9 and references the v0.5.10 release as the fix [VF: B-REVC-S002]. Load only allow-listed, scanned weights from an internal mirror, keep remote code off, and run engines on internal-only networks [Rec].
- Engines and local runtimes are not identity-aware. Ollama binds to localhost by default, and exposure is done by changing `OLLAMA_HOST` and fronting it with a proxy [VF: B-L2-S007]. Never expose an engine port directly; front it with the gateway and network policy [Rec].
- KV caches hold prompt state. Shared prefix caches and tiered or persistent KV stores (LMCache, Dynamo KVBM, llm-d tiered cache) [VF: A4-S091, A4-S090, A4-S089] can carry one request's context into another's memory or storage. Partition caches by tenant or data classification, encrypt offload tiers, and include them in data-retention scope [Rec].
- Check provider defaults, not just options. Together AI's ZDR is off by default [VF: A4-S130]; Fireworks' ZDR is on by default for open models, except the Response API, which stores conversations for 30 days unless `store=False` is set [VF: A4-S134]; OpenRouter's ZDR does not cover tools such as web search [VF: A4-S108]. Record the retention setting per route [Rec].

**Scalability and capacity**
- Self-hosting is a capacity and operating-model decision, not only a cost decision [AJ]. Owning GPUs buys guaranteed capacity and in-estate processing, but it also buys the duty to patch engines fortnightly (vLLM shipped 28 releases in 2026) [VF: A4-S009], to staff on-call for accelerators, and to forecast peaks.
- Plan capacity against the peak, not the average. Month-end and quarter-end reporting create predictable bursts [AJ]. Reserved capacity is available on every major route: Microsoft Foundry's provisioned types give lower and more consistent latency than Global Standard [VF: B-L2-S006]; Vertex AI sells Provisioned Throughput [VF: B-L2-S008]; Together AI's PTU carries an uptime SLA [VF: A4-S131].
- Make overflow behaviour explicit. Vertex AI's Single Zone Provisioned Throughput processes overflow in the purchased region at pay-as-you-go rates, but it is excluded from the Gemini online inference SLA [VF: B-L2-S008]. Choose which property matters for each route: residency or SLA [AJ].

**Resilience**
- Two qualified endpoints per production route, in the same approved region, with different failure domains [Rec]. Bedrock's EU geographic profile spreads requests across EU Regions only [VF: B-L2-S005], which is a residency-safe resilience mechanism inside one provider; it does not remove provider concentration [AJ].
- Fail closed rather than fall back out of region. OpenRouter's in-region routing fails rather than falling back [VF: A4-S109, A4-S150]; the firm's gateway should behave the same way (see C1.5) [Rec].

**Governance and observability**
- Record processing location per call. Bedrock writes the actual inference Region into CloudTrail (`inferenceRegion`) [VF: B-L2-S005]; join that evidence to the gateway log [Rec].
- Pin model versions and record engine versions for self-hosted routes, so L9 regression results refer to an exact serving configuration [AJ].

**Cost**
- Pricing units differ and do not compare directly: per 1M tokens (Together, Fireworks, Cerebras), per replica-minute (Together dedicated), per GPU-second (Fireworks), per instance-minute (Hugging Face Endpoints), per PTU-minute (Together PTU) [VF: A4-S131, A4-S135, A4-S139, A4-S083]. Model cost at the forecast utilisation, including idle reserved capacity [Rec].
- Routers add fees on top of provider prices: OpenRouter charges 5.5% on credit purchases (US$0.80 minimum), 8% on Business [VF: V1-S062, A4-S144].
- Regional processing can carry a premium. On Google Cloud, non-global endpoints are priced 10% higher from 1 July 2026 [VF: A5-S027]. Residency is a priced control; budget for it [AJ].

**Portability**
- Make the OpenAI-compatible API the contract between gateway and every endpoint. vLLM, SGLang, Ollama, Cerebras, OpenRouter and Hugging Face Inference Providers all expose it [VF: A4-S063, A4-S010, A4-S084, A4-S139, A4-S109, A4-S075]. Provider-specific features (Fireworks Response API, OpenRouter guardrails) sit behind the gateway, not in application code [Rec].
- Keep at least one open-weight model qualified on a portable engine as the stressed-exit route, even if it is never the primary [Rec].

**Patterns [AJ]:** managed in-region endpoint with reserved capacity behind the gateway; a second qualified in-region endpoint as fallback; a private vLLM route for open-weight models where residency or exit demands it; internal model mirror with scanning; capacity plan tied to the business calendar.

**Anti-patterns [AJ]:** a hosted router as the gateway of record; serverless endpoints for a fixed-time month-end batch; provider defaults left unchecked (ZDR off, Response API storage on); engines on a reachable network port with no authentication; self-hosting justified on token price alone; a "global" endpoint for client data because it launched first.

### 2.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Engines: batching, KV-cache management, quantisation, speculative decoding, disaggregation, model and hardware coverage. Access: dedicated and reserved capacity, batch, fine-tuning, routing and fallback |
| Enterprise readiness (15%) | SSO, RBAC, audit logs, SCIM, SLAs on capacity; for engines, what they enable inside your estate and whether a supported distribution exists (rule 2) |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in scope for the inference product; ZDR default and contract; CMK; BAA where needed; for engines, advisory handling and patch cadence |
| Deployment flexibility (15%) | Region choice and processing-location guarantees; dedicated, VPC/BYOC, on-prem; EU processing available now, not announced |
| Ecosystem (5%) | OpenAI-compatible API; availability on hyperscaler marketplaces; engine support across managed services |
| Reliability and maturity (10%) | 1.0 status, release cadence, governance (foundation vs single vendor), ownership changes, capacity SLAs |
| Cost / TCO (5%) | Unit pricing transparency, reserved-capacity economics, router fees, GPU and staffing cost for self-hosting |
| Lock-in / portability (15%) | Open weights and engines, OpenAI-compatible APIs, billing intermediation, proprietary hardware, ownership neutrality |

### 2.7 Product deep dives

The eleven records are grouped by H1 sub-layer: serving engines, optimisation and orchestration, local runtimes, and model access. Hyperscaler model services are discussed afterwards as a pattern; they have no product record in this layer and are not scored here [AJ]. Self-hosted engines and orchestration layers (vLLM, SGLang, Dynamo, llm-d, and Ollama's local runtime) are scored under rubric rule 2: security on project hygiene, enterprise readiness on what they enable in your estate, and both capped at 4 unless a commercial support offer or hardened distribution exists. They inherit host controls [AJ].

#### Sub-layer 1: serving engines

**vLLM (vLLM project, PyTorch Foundation).**
- *What it is now:* an Apache-2.0 inference and serving engine at 0.31.0, released 5 October 2026, with 28 releases in 2026 [VF: A4-S009]. It has been a PyTorch Foundation-hosted project since 7 May 2025, and its governance document names a committee that acts as the Technical Steering Committee under Linux Foundation project governance [VF: A4-S146, V1-S064, A4-S064]. Features include PagedAttention, continuous batching, prefix caching, quantisation, speculative decoding and disaggregated prefill/decode/encode, with an OpenAI-compatible server, the Anthropic Messages API and gRPC, over 200 model architectures, and NVIDIA, AMD and Intel GPUs, CPUs and hardware plugins [VF: A4-S063].
- *Position in the stack:* it is the engine underneath Hugging Face Inference Endpoints, llm-d and NVIDIA Dynamo [VF: A4-S081, A4-S089, A4-S090].
- *Support and hygiene:* Red Hat ships a supported vLLM-based server, renamed Red Hat AI Inference in version 3.4 [VF: B-L2-S001]. Security disclosures go through GitHub Security Advisories [VF: A4-S063]. In 2026 these included a critical video-input code-execution flaw (CVE-2026-22778), several model-loading flaws that bypassed `trust_remote_code=False` (CVE-2026-22807, CVE-2026-27893, and an August 2026 advisory), and an assertion bypass under Python optimised mode fixed in 0.22.0 [VF: B-L2-S004].
- *Strengths:* the broadest single-engine feature set, neutral governance, and the de-facto substrate other products build on [AJ].
- *Limitations:* pre-1.0 with a fortnightly cadence [VF: A4-S009]; its main attack surface is untrusted model files and media inputs [VF: B-L2-S004]; it has no identity, audit or tenancy of its own [AJ].
- *Choose when:* you self-host open-weight models on your own or private-cloud GPUs and want the widest model and hardware coverage [AJ].
- *Avoid when:* you cannot run a monthly patch cycle and model-provenance controls, or you have no GPU and SRE capacity [AJ].
- *Competitors:* SGLang, TensorRT-LLM, Hugging Face Inference Endpoints (managed vLLM).
- *FS note:* run behind the gateway on an internal network, load only allow-listed weights from a scanned mirror with remote code off, pin versions and track advisories; buy the supported distribution if your operating model needs a vendor on the hook [Rec].
- **Tier: Strategic, conditional: only with patch and model-provenance discipline, and only where a private route is justified (see 2.9). Flag: none.**

**SGLang (LMSYS; RadixArk as commercial steward).**
- *What it is now:* an Apache-2.0 serving framework at 0.5.21 (1 October 2026), first released in January 2024, with 21 releases in 2026 [VF: A4-S010, A4-S128]. Features include RadixAttention prefix caching, PD disaggregation, speculative decoding and FP4/FP8 quantisation, with broad hardware support (NVIDIA, AMD, Intel Xeon, Google TPU, Ascend) and day-0 support for new open models [VF: A4-S010, A4-S065]. The project states it powers over 400,000 GPUs [VF: A4-S010]; this is a project claim.
- *Governance:* the repository states it is hosted by the LMSYS non-profit [VF: A4-S065]. RadixArk, founded by SGLang's creators, launched with a US$100M seed on 5 May 2026 to steward SGLang and build a commercial platform [VF: A4-S147, V1-S063]. No transfer of code, trademark or governance from LMSYS was found [VF: A4-S147, A4-S065].
- *Security hygiene:* CVE-2026-3059, a critical unauthenticated code-execution flaw through the multimodal generation module's ZMQ broker, affects 0.5.9 and below; the GitHub advisory lists no patched version [VF: B-L2-S009], but NVD gives the vulnerable range as 0.5.5 to 0.5.9 and references the v0.5.10 release and a fixing pull request, and OSV records a fixed commit [VF: B-REVC-S002]. An earlier deserialisation flaw (CVE-2025-10164) was fixed in 0.5.4, but VulDB reports that the vendor did not respond to early disclosure, and a June 2026 issue reports a bypass of that fix [VF: B-L2-S009]. On the NVD and OSV references the current 0.5.21 should include the fix; the patch itself was not read, so confirm the deployed version against the upstream advisory [AJ].
- *Strengths:* strong on prefix-heavy and agentic workloads and quick to support new models [AJ].
- *Limitations:* the security-response evidence is weaker than vLLM's; no verified commercial support offer [NPV]; governance sits with a non-profit plus a VC-backed steward rather than a neutral foundation [AJ].
- *Choose when:* you need a second qualified engine, prefix reuse matters, or a new model is supported here first [AJ].
- *Avoid when:* the engine's internal ports could be reachable outside a locked-down serving namespace, or you need vendor support now [AJ].
- *Competitors:* vLLM, TensorRT-LLM, NVIDIA Dynamo (as orchestrator over either).
- *FS note:* qualify SGLang as the alternative engine in the exit plan, confirm the CVE status of the deployed version, and keep its multimodal and weight-update endpoints disabled or isolated [Rec].
- **Tier: Tactical. Flag: none.**

*TensorRT-LLM (NVIDIA)* is noted without a record: an open-sourced library for optimising LLM inference with quantisation and speculative decoding, at 1.2.1 and classed beta [VF: A4-S099].

#### Sub-layer 2: inference optimisation and orchestration

**NVIDIA Dynamo (NVIDIA).**
- *What it is now:* "the orchestration layer above inference engines — it doesn't replace SGLang, TensorRT-LLM, or vLLM" [VF: A4-S090]. It provides disaggregated serving, KV-aware routing, a multi-tier KV Block Manager, an SLA-based planner and autoscaling, model-weight streaming, a Kubernetes Gateway API Inference Extension plugin and topology-aware scheduling [VF: A4-S090]. It is Apache-2.0; ai-dynamo 1.5.1 was published on 7 October 2026 with a Beta PyPI classifier [VF: A4-S098].
- *Maturity conflict:* the README presents Dynamo 1.0 as "production-ready" [VF: A4-S090], while the package classifier says Beta [VF: A4-S098]. Treat the package classifier as the operative signal until NVIDIA states otherwise [AJ].
- *Support:* enterprise support is an NVIDIA AI Enterprise feature branch: each branch is supported for one month, fixes and security updates are not backported, a subscription is needed to raise cases, and only the `-enterprise` artifacts are covered. The software itself is free to use in development and production [VF: B-L2-S003].
- *Strengths:* clear separation of the optimisation sub-layer, and engine-agnostic across three backends; integrates LMCache [VF: A4-S090, A4-S091].
- *Limitations:* NVIDIA-led and NVIDIA-GPU-optimised [VF: A4-S090]; month-long support windows force continuous upgrades [VF: B-L2-S003]; project security policy not verified [NPV].
- *Choose when:* you operate multi-node NVIDIA GPU serving at a volume where disaggregation and KV-aware routing pay back [AJ].
- *Avoid when:* single-node or modest volumes, where vLLM alone suffices; or when you need long-term-support releases [AJ].
- *Competitors:* llm-d, vLLM's own disaggregation, SGLang's own disaggregation.
- *FS note:* keep the engine's OpenAI-compatible API as the contract to the gateway so Dynamo can be removed without touching applications [Rec].
- **Tier: Experimental. Flag: none.**

**llm-d (CNCF sandbox project).**
- *What it is now:* a Kubernetes-native distributed inference stack that provides "orchestration and optimizations above model servers" such as vLLM and SGLang [VF: A4-S089]. Features: prefix-cache- and load-aware routing (with experimental predicted-latency scheduling), tiered KV-cache offload to CPU or disk with global indexing, PD disaggregation and wide expert parallelism, SLO-aware autoscaling [VF: A4-S089]. It is Apache-2.0, joined the CNCF as a sandbox project in March 2026, and released v0.7 in May 2026 [VF: A4-S089]. Founders are Red Hat, Google Cloud, IBM Research, CoreWeave and NVIDIA [VF: A4-S089]. Google launched it on 20 May 2025 alongside the GKE Inference Gateway [VF: A4-S062].
- *Support:* Red Hat supports distributed inference with llm-d on OpenShift 4.19+, AKS and CoreWeave Kubernetes Service only as a Technology Preview, without production SLAs, and does not recommend production use [VF: B-L2-S002].
- *Strengths:* neutral governance and a multi-vendor founding coalition; builds on the Kubernetes Gateway API Inference Extension rather than a private router [VF: A4-S089, A4-S062].
- *Limitations:* pre-1.0 and sandbox stage [VF: A4-S089]; Technology Preview support [VF: B-L2-S002]; needs Kubernetes and data-centre accelerators [VF: B-L2-S002]; security hygiene not verified [NPV].
- *Choose when:* Kubernetes is the platform standard and you are building a shared internal inference service across several models [AJ].
- *Avoid when:* you need production-supported software today [AJ].
- *Competitors:* NVIDIA Dynamo, KServe, vLLM alone.
- *FS note:* pilot in non-production; revisit at 1.0 and when Red Hat moves support to GA [Rec].
- **Tier: Experimental. Flag: none.**

*LMCache* is noted without a record: "a KV cache management layer", vendor-neutral, running as a separate daemon so the cache survives an engine crash, a PyTorch Foundation project since October 2025 [VF: A4-S091].

#### Sub-layer 2b: local runtimes (developer tier, not production serving)

**Ollama (Ollama).**
- *What it is now:* an MIT-licensed local runtime and model packager [VF: A4-S086], plus **Ollama Cloud**, which runs larger models in Ollama's cloud through apps, CLI or API with an API key, and exposes OpenAI- and Anthropic-compatible APIs [VF: A4-S084]. The graphic's "run locally" is therefore incomplete [AJ]. Cloud features can be disabled (`OLLAMA_NO_CLOUD=1`) [VF: A4-S085]. Usage-based cloud plans started on 31 August 2026: Free, Pro US$20/month, Max US$100/month and Team US$500/month [VF: V1-S066]. A US$65M round was reported in July 2026 [R: V1-S071].
- *Data handling:* locally, Ollama does not see prompts; in the cloud, prompts and responses are processed but, per the vendor, not stored or logged and never used for training [VF: A4-S085, A4-S084]. The vendor states cloud compute runs in the US and Europe, plus Singapore for some Qwen models [VF: V1-S066].
- *Network exposure:* the server binds to 127.0.0.1:11434 by default; remote access means changing `OLLAMA_HOST` and fronting it with a proxy such as Nginx [VF: B-L2-S007]. Built-in authentication was not documented in the sources read [NPV].
- *Strengths:* the lowest-friction way to run open models on a laptop or a disconnected workstation [AJ].
- *Limitations:* Ollama Cloud certifications, SSO and audit are not publicly verified [NPV]; the server version was not retrieved [NPV].
- *Choose when:* developer workstations and offline evaluation, with cloud disabled [AJ].
- *Avoid when:* any shared or production serving, and any client data on Ollama Cloud [AJ].
- *Competitors:* LM Studio, llama.cpp, vLLM for anything shared.
- *FS note:* allow only on managed devices with `OLLAMA_NO_CLOUD` enforced by device policy and localhost binding; Ollama Cloud is an unassessed third-party processor [Rec].
- **Tier: Tactical (developer tier). Flag: none (descriptor out of date: no longer local-only).**

**LM Studio (LM Studio).**
- *What it is now:* a desktop application for downloading and running local models with a local API server, plus the MIT-licensed `lms` CLI and SDKs [VF: A4-S087, A4-S088, A4-S016]. The app is proprietary: free for personal and internal business use since about July 2025, and it may not be modified, redistributed, sublicensed or offered as a service [VF: A4-S145, V1-S076]. A paid Enterprise plan adds SSO and model and MCP gating [VF: A4-S145].
- *Strengths:* approachable desktop evaluation, and the Enterprise plan can restrict which models and MCP servers staff use [VF: A4-S145] [AJ].
- *Limitations:* security features, support, desktop version and maturity are not publicly verified [NPV]; the Python SDK was last released in August 2025 [VF: A4-S016].
- *Choose when:* managed developer desktops where a GUI helps adoption and model gating is wanted [AJ].
- *Avoid when:* any server or shared use; the terms forbid offering it as a service [VF: A4-S145] [AJ].
- *Competitors:* Ollama, llama.cpp.
- *FS note:* permit only through the Enterprise plan on managed devices with an approved-model list; no client data [Rec].
- **Tier: Tactical (developer desktop only). Flag: none.**

#### Sub-layer 3: model access

**Hugging Face (Hugging Face).**
- *What it is now:* one tile, four products [VF: A4-S075, A4-S081, A4-S073]:
  1. **Hub**: model and dataset hosting with private repositories, malware, pickle and secrets scanning; SSO (SAML/OIDC), SCIM, RBAC and audit logs on Team and Enterprise; US and EU storage regions for Team and Enterprise organisations [VF: A4-S074, A4-S080, A4-S079, A4-S078].
  2. **Inference Providers**: an OpenAI-compatible router to partner clouds (including Cerebras, Fireworks, Groq, Together, Nscale, OVHcloud, Scaleway) with provider rates passed through and no Hugging Face markup; it does not store request or response bodies and keeps logs for up to 30 days [VF: A4-S075, A4-S076, A4-S077].
  3. **Inference Endpoints**: managed dedicated deployments on AWS, Azure or GCP, billed per minute, with vLLM, SGLang, TGI, llama.cpp or TEI as the engine; SOC 2 Type 2; AWS PrivateLink; payloads not stored, logs kept 30 days [VF: A4-S081, A4-S083, A4-S082].
  4. **TGI**: maintenance mode "as of 12/11/2025" (the date format is ambiguous), and the GitHub repository was archived on 21 March 2026 at v3.3.7; Hugging Face recommends vLLM or SGLang [VF: A4-S073, A4-S072, V1-S054, V1-S055].
- *Certifications and scope:* SOC 2 Type 2 for the Hub and Endpoints; a BAA and GDPR DPA via the Enterprise plan, but the BAA is not explicitly tied to Inference Endpoints [VF: A4-S074, A4-S082, V1-S097]. No ISO 27001 was found [NPV].
- *Strengths:* the de-facto distribution point for open weights, with enterprise identity controls; Endpoints let you pick both engine and cloud region [AJ].
- *Limitations:* Inference Providers inherits each partner's security and retention [VF: A4-S077]; Endpoints are not BYOC [VF: A4-S082]; AWS H100 instances on Endpoints were marked deprecated from December 2025 [VF: A4-S083].
- *Choose when:* you need a governed source of open weights for any private route, or a managed dedicated endpoint in a chosen cloud region without running GPUs yourself [AJ].
- *Avoid when:* routing client data through Inference Providers to partners you have not assessed [AJ]. Endpoints customers still on TGI should plan migration [Rec].
- *Competitors:* Together AI and Fireworks (dedicated endpoints); hyperscaler model catalogues (Bedrock, Foundry, Vertex).
- *FS note:* treat the Hub (Enterprise plan, EU storage) as part of the model supply chain: mirror approved weights internally and scan them (C7). Use Endpoints only in an approved region with PrivateLink, and confirm BAA and DPA scope in writing [Rec].
- **Tier: Strategic, conditional: as the governed open-weight supply source on the Enterprise plan; Inference Endpoints are Tactical; Inference Providers is not for client data. Flags: Duplicated (four products in one tile), Deprecated (TGI).**

**Together AI (Together Computer, Inc.).**
- *What it is now:* an "AI-native cloud" covering serverless and dedicated inference for open-weight models, Provisioned Throughput (PTU), fine-tuning and GPU clusters from H100 to GB300 [VF: A4-S131, A4-S093]. It raised a US$800M Series C at US$8.3B post-money on 1 July 2026 [VF: A4-S132, V1-S057].
- *Certifications and data handling:* SOC 2 Type 2 (latest report 17 June 2026) and ISO 27001:2022 via A-LIGN, as vendor statements; HIPAA wording is inconsistent and a customer BAA was not confirmed [VF: A4-S129, V1-S079]. **ZDR is available at organisation level but off by default**: by default prompts and responses are stored and may be used for product improvement; training on customer data is opt-in [VF: A4-S130]. Serverless has no region selection; **EU dedicated endpoints are available only on Scale and Enterprise plans** [VF: A4-S130]. Cluster sites are listed in the US and in Europe (France, Netherlands, Sweden, Romania) [VF: A4-S130].
- *Access control:* SSO (SAML/OIDC) on Scale and Enterprise; organisation and project RBAC, but product-level RBAC for fine-tuning, endpoints and serverless is "still being rolled out"; per-user audit trails for GPU clusters [VF: A4-S151].
- *Strengths:* broad open-model catalogue with dedicated and reserved capacity, and EU sites [AJ].
- *Limitations:* unsafe defaults for regulated data, partial RBAC, and a dedicated H100 price that differs between the docs (US$3.99/h) and the pricing page (US$5.49/h) [VF: A4-S131].
- *Choose when:* open-weight models on dedicated EU endpoints with ZDR on, under a Scale or Enterprise contract [AJ].
- *Avoid when:* serverless with client data, or any use with ZDR left at default [AJ].
- *Competitors:* Fireworks AI, Hugging Face Inference Endpoints, hyperscaler model catalogues.
- *FS note:* contract ZDR on, EU dedicated endpoints and the PTU SLA; obtain the SOC 2 report and ISO certificate scope from the trust centre [Rec].
- **Tier: Tactical. Flag: none.**

**Fireworks AI (Fireworks AI, Inc.).**
- *What it is now:* managed inference and fine-tuning for open models: serverless, on-demand and reserved dedicated deployments, batch at 50% of serverless price, fine-tuning and reinforcement fine-tuning, Virtual Cloud and FireRouter [VF: A4-S135, A4-S094, A4-S152]. Hybrid BYOC puts the Fireworks engine in the customer's VPC on the enterprise reserved tier [VF: A4-S152]. It raised a US$1.505B Series D at US$17.5B on 15–16 July 2026 [VF: A4-S141, V1-S058].
- *Data handling:* **ZDR by default for open models**, with prompts and outputs held only in volatile memory; the exception is the Response API, which stores conversations for 30 days by default unless `store=False` [VF: A4-S134]. An enterprise data-residency setting rejects out-of-region requests, but the documented options are "None" and "US" only, with others via sales; EU regions (Frankfurt, Iceland) exist for deployments [VF: A4-S134].
- *Certifications:* SOC 2 Type II, HIPAA and GDPR are listed [VF: A4-S133]. ISO 27001, 27701 and 42001 are listed in the trust centre, but one Fireworks docs page still lists them as "in progress" [VF: V1-S067]. Under the verifier's binding guidance, the ISO certifications are not relied on here [AJ]. A BAA was not seen [NPV].
- *Controls:* SSO via OIDC or SAML 2.0, RBAC, an Audit Logs page and CLI, service accounts, and customer-managed encryption keys whose usage appears in the customer's cloud audit log [VF: A4-S152].
- *Strengths:* the strongest default data posture and control set among the independent inference clouds reviewed here [AJ].
- *Limitations:* conflicting ISO evidence; EU residency not self-serve; revenue concentration reported (about half from Cursor as of 2025, per CNBC) [VF: A4-S141]; GPU rates (H100 US$8.00/h) above peers, with a secondary source citing US$7.00/h [VF: A4-S135].
- *Choose when:* you want managed open-model serving with a BYOC data plane or EU dedicated deployments, without running GPUs [AJ].
- *Avoid when:* using the Response API for client data without disabling storage, or where ISO certificates are a hard gate you have not yet checked [AJ].
- *Competitors:* Together AI, Hugging Face Inference Endpoints, hyperscaler model catalogues (Fireworks also operates some models sold through Microsoft Foundry [VF: A5-S087]).
- *FS note:* request the ISO certificates and BAA terms from trust.fireworks.ai, contract EU deployments or BYOC, and set `store=False` in the gateway for any Response API route [Rec].
- **Tier: Tactical; candidate for Strategic after due diligence on ISO certificates and EU residency. Flag: none.**

**Cerebras (Cerebras Systems Inc.).**
- *What it is now:* a chip and system vendor (WSE-3, CS-3) that also runs an inference cloud with an OpenAI-compatible API, and sells CS-3 systems for on-premise deployment [VF: A4-S095, A4-S139]. The graphic's "ultra-scale cloud" omits the hardware business [AJ]. Its IPO priced on 13 May 2026 at US$185 per share (Nasdaq: CBRS) [VF: A4-S137, V1-S053]. It has a 750MW inference agreement with OpenAI from December 2025 [VF: A4-S154].
- *Certifications and data handling:* the trust centre lists SOC 2 Type 2, GDPR and CCPA; HIPAA is not listed [VF: A4-S138, V1-S095]. The privacy policy says inference inputs and outputs are not retained and that data may be processed outside the US unless otherwise agreed [VF: A4-S153]. EU capacity is announced for end-2026, with 200MW targeted by end-2027 [VF: A4-S140].
- *Controls:* console roles (Organization Admin, Project Admin, Project Member) and API keys; no SSO documentation was found [VF: A4-S153].
- *Strengths:* speed as a design point, and an on-premise system option [AJ].
- *Limitations:* thin enterprise identity controls, no EU processing yet, ZDR evidence at privacy-policy level rather than contract [VF: A4-S153, A4-S140]; customer concentration in the OpenAI agreement [VF: A4-S154].
- *Choose when:* latency-critical, non-confidential workloads on supported open models [AJ].
- *Avoid when:* client data, until EU capacity, SSO and contractual ZDR are documented [AJ].
- *Competitors:* Groq, Together AI, Fireworks AI.
- *FS note:* re-assess when the EU capacity is live; ignore post-IPO share-price moves as a decision input [Rec].
- **Tier: Tactical. Flag: none (status changed: public company).**

**OpenRouter (OpenRouter, Inc.; acquisition by Stripe pending).**
- *What it is now:* a hosted multi-provider router with one OpenAI-compatible API, routing, fallbacks and provider selection, and gateway-style controls: workspace budgets, model and provider allowlists, ZDR enforcement, data regions, and prompt-injection and sensitive-information guardrails [VF: A4-S113, A4-S111, A4-S112]. EU/US in-region routing is available on Business and Enterprise plans and fails rather than falling back out of region; the Batch API, web search and web fetch are not region-resident [VF: A4-S109, A4-S150].
- *Ownership:* Stripe and OpenRouter announced on 19 August 2026 that Stripe has agreed to acquire OpenRouter; closing was expected "in the coming weeks", and no completion notice was found by 8 October 2026 [VF: V1-S059, V1-S060]. The price is undisclosed; press figures are not relied on [AJ]. OpenRouter says its name, product and roadmap are unchanged [VF: V1-S060]. It raised a US$113M Series B led by CapitalG on 26 May 2026 [VF: V1-S061].
- *Certifications and controls:* SOC 2 Type 2 (report on request); **no HIPAA BAA** [VF: A4-S142]. SSO (Okta, Entra ID, Google Workspace, custom SAML) and SCIM group mappings on Enterprise [VF: A4-S110, A4-S112]. Contractual SLAs only on Enterprise, with no numeric uptime target published [VF: A4-S150].
- *Pricing:* provider prices passed through, plus a platform fee on credit purchases: **5.5% (US$0.80 minimum)** on Standard, 5.0% for crypto, 8% on Business, custom on Enterprise; BYOK carries a 5% fee that is being replaced by a subscription [VF: V1-S062, A4-S144].
- *Strengths:* the quickest way to evaluate many models behind one API, with residency-safe failure behaviour [AJ].
- *Limitations:* a third-party SaaS in the data path, billing intermediation between the firm and its model providers, and a pending change of owner [AJ].
- *Choose when:* model exploration and non-confidential workloads, behind the firm's gateway [AJ].
- *Avoid when:* client or personal data without ZDR and in-region routing contractually enforced; and as the firm's gateway of record, for which see C1 [AJ].
- *Competitors:* Hugging Face Inference Providers; self-hosted gateways in C1 (LiteLLM) with direct provider contracts.
- *FS note:* a model-access source behind C1, not C1 itself; reassess the contract, data-processing roles and sub-processor list when the acquisition closes, and plan any notification under PS7/26 lead times [Rec].
- **Tier: Tactical. Flag: Acquired (pending).**

#### Hyperscaler model services as the default enterprise access route (pattern, not scored)

No record exists in this layer for Amazon Bedrock, Microsoft Foundry or Google Cloud's model service (Gemini Enterprise Agent Platform, formerly Vertex AI); Stage A could not fetch their primary pages (stream A4 notes, section d). The pattern can still be described from the L1 records' availability fields and four new primary sources [AJ].

- *Breadth.* Most L1 families are reachable through at least one hyperscaler. Claude is offered on Bedrock, Google Cloud and Microsoft Foundry [VF: A5-S010]. OpenAI's GPT-6 family is on Bedrock and Microsoft Foundry [VF: A5-S008, A5-S009]. Gemini is on Google Cloud only [VF: A5-S027]. Mistral models appear on all three, with different subsets [VF: A5-S027, A5-S038]. Chinese-origin open models are hosted by hyperscalers too, for example Qwen3 and GLM 5 on Bedrock in London [VF: A5-S086].
- *Processing location is configurable, and that is the point.* On Bedrock, a geographic cross-Region inference profile keeps EU-originated requests within EU Regions; London-originated requests route between EU Regions and London; stored data, invocation logs and knowledge bases stay in the source Region; CloudTrail records the Region that processed each request; a global profile can route to any commercial Region [VF: B-L2-S005]. On Microsoft Foundry, "Global" deployments may process prompts in any geography, "Data Zone" deployments process only within the US or EU zone, and Standard and Regional Provisioned deployments process within the customer's chosen geography [VF: B-L2-S006]. On Google Cloud, regional and multi-region (US, EU) endpoints keep processing within a jurisdiction, while the global endpoint gives no residency guarantee [VF: B-L2-S008].
- *But "on a hyperscaler" does not always mean "processed by the hyperscaler".* On Microsoft Foundry, Kimi K3 is offered through Fireworks, with inference on Fireworks GPUs outside the customer tenant, while DeepSeek V4 is sold directly by Azure [VF: A5-S087]. Check who operates the model, not just whose catalogue lists it [Rec].
- *Model availability by region is uneven.* GPT-6 Astra on Bedrock is in-region only in us-east-1 and us-west-2 [VF: A5-S008, V2-S079]; Bedrock geographic profiles are not supported for some models [VF: B-L2-S005]; Kimi K3 on Bedrock has US, India and global cross-Region profiles but no in-Region option [VF: A5-S086]. The approved model list is therefore a function of region [AJ].
- *Capacity products exist on all three.* Foundry provisioned throughput units, Vertex Provisioned Throughput (regional-only for partner models such as Claude) and Bedrock cross-Region inference for throughput [VF: B-L2-S006, B-L2-S008, B-L2-S005].
- *Regulatory position.* AWS, Google Cloud and Microsoft are designated under both the DORA CTPP list and the UK CTP regime; no model provider is [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. Consuming a model through the hyperscaler therefore places the inference service inside an already-overseen, already-contracted relationship [AJ].
- *Assessment [AJ].* For a regulated firm, the lead model service of its primary cloud is the default access route: it inherits platform identity and audit (CP2 Q1 presumption; platform controls presumed (CP2 Q1); confirm per service), offers in-geography processing and reserved capacity, and avoids adding a new material third party. Its weaknesses are concentration on one cloud, a model catalogue that differs by cloud and by region, and price premiums for regional processing [VF: A5-S027]. These services would score as the lead hyperscaler service in their category under rule 10 if profiled; this is left to the L1 writer and synthesis.

### 2.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2-vllm | 5 | 4 | 3 | 5 | 5 | 4 | 4 | 5 | 4.35 | 4.30 | Strategic |
| L2-sglang | 5 | 3 | 2 | 5 | 4 | 3 | 4 | 4 | 3.80 | 3.65 | Tactical |
| L2-nvidia-dynamo | 4 | 3 | 2 | 4 | 3 | 2 | 3 | 3 | 3.10 | 3.00 | Experimental |
| L2-llm-d | 4 | 3 | 2 | 4 | 4 | 2 | 3 | 5 | 3.30 | 3.35 | Experimental |
| L2-ollama | 3 | 2 | 2 | 4 | 4 | 2 | 4 | 4 | 3.00 | 2.95 | Tactical |
| L2-lm-studio | 2 | 2 | 2 | 2 | 2 | 2 | 4 | 3 | 2.25 | 2.25 | Tactical |
| L2-hugging-face | 4 | 4 | 3 | 3 | 5 | 3 | 4 | 4 | 3.70 | 3.60 | Strategic |
| L2-openrouter | 4 | 4 | 3 | 2 | 4 | 3 | 3 | 2 | 3.25 | 3.05 | Tactical |
| L2-together-ai | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 3.50 | 3.50 | Tactical |
| L2-fireworks-ai | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 3.65 | 3.65 | Tactical |
| L2-cerebras | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2.85 | 2.80 | Tactical |

**Scoring notes [AJ]:**
- *Rule 2 (self-hosted software).* vLLM, SGLang, Dynamo and llm-d are scored as software you run; they inherit host controls. vLLM's enterprise readiness reaches 4 because a supported distribution exists (Red Hat AI Inference) [VF: B-L2-S001]. Dynamo has commercial support, but only month-long feature branches [VF: B-L2-S003], so it stays at 3. llm-d's Red Hat support is Technology Preview without production SLAs [VF: B-L2-S002], so the cap at 4 applies (not binding at 3). SGLang has no verified support offer, so the cap applies (not binding at 3).
- *Rule 2 security hygiene.* vLLM scores 3: a working advisory process with fixed versions, against a run of 2026 code-execution flaws [VF: B-L2-S004]. SGLang scores 2: a critical unauthenticated flaw whose fix is evidenced only by NVD and OSV references (the GitHub advisory still lists no patched version), plus disclosure-response concerns and a reported bypass of an earlier fix [VF: B-L2-S009, B-REVC-S002]. Whether this is 2 or 3 is put to the reader at Checkpoint 4 (CP4 review C). Dynamo and llm-d score 2 because their security policies and CVE handling were not verified [NPV].
- *NPV caps (rule 1).* Ollama: enterprise readiness and security capped at 2 (Ollama Cloud SSO, audit and certifications NPV). LM Studio: security capped at 2. LM Studio's enterprise readiness could rise to 3 under rule 7 on its Enterprise SSO, but that evidence is a low-confidence extract with no audit or support evidence, so 2 is kept.
- *Rule 7 (partial evidence).* Cerebras is lifted to 3 on verified console roles despite no SSO. OpenRouter (SSO, SCIM, roles, Enterprise SLA), Fireworks (SSO, RBAC, audit logs with CLI) and Hugging Face (SSO, SCIM, RBAC, audit logs) reach 4.
- *Rule 8 (certification scope).* Together AI's SOC 2 and ISO 27001 are vendor-stated without product scope, so 3 rather than 4. Cerebras' SOC 2 is a trust-centre listing without product scope, so 2. Fireworks scores 3 because its ISO claims conflict and are not relied on (V1 section 4); with confirmed certificates it would be a candidate for 4.
- *Rule 3 (ownership change).* OpenRouter's lock-in falls from 3 to 2 for the pending Stripe acquisition, and the change is noted in its maturity rationale. No other product in this layer changed owner in 2025–26; RadixArk's stewardship of SGLang is not an acquisition, but it is reflected in SGLang's lock-in score of 4 rather than 5.
- *Tiers.* vLLM is Strategic (FS 4.30). Hugging Face is Strategic, conditional (FS 3.60), on the narrow basis of its Hub as governed open-weight supply. SGLang (FS 3.65) and Fireworks (FS 3.65) clear 3.6 but stay Tactical: SGLang because of its security evidence (criterion at 2 with no platform-commitment condition, rule 11); Fireworks pending ISO and residency due diligence (rule 13). Dynamo and llm-d are Experimental on maturity.
- *Calibration (rule 5).* Every product except vLLM, Hugging Face, Together and Fireworks scores 2 or below on at least one criterion. For those four, the weakest scores (3 on security for all of them) are stated as conditions.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| vLLM | Apache-2.0 [VF: A4-S009] | Self-host, VPC, on-prem; managed via third parties [VF: A4-S063, A4-S081] | Not applicable (software); advisories published [VF: B-L2-S004] | In-estate [AJ] | PyTorch Foundation-hosted since 7 May 2025 [VF: A4-S146] |
| SGLang | Apache-2.0 [VF: A4-S128] | Self-host, VPC, on-prem; managed via Hugging Face [VF: A4-S065, A4-S081] | Not applicable (software); CVE-2026-3059: GitHub advisory lists no patch; NVD references a fix in 0.5.10 [VF: B-L2-S009, B-REVC-S002] | In-estate [AJ] | LMSYS-hosted; RadixArk commercial steward (May 2026) [VF: A4-S065, A4-S147] |
| NVIDIA Dynamo | Apache-2.0 [VF: A4-S098] | Self-host on Kubernetes; EKS, GKE, AKS guides [VF: A4-S090] | Not applicable; NVAIE feature-branch support [VF: B-L2-S003] | In-estate [AJ] | NVIDIA [VF: A4-S098] |
| llm-d | Apache-2.0 [VF: A4-S089] | Self-host on Kubernetes [VF: A4-S089] | Not applicable; Red Hat Technology Preview [VF: B-L2-S002] | In-estate [AJ] | CNCF sandbox (March 2026) [VF: A4-S089] |
| Ollama | MIT runtime; Cloud proprietary [VF: A4-S086, A4-S084] | Local, on-prem; Ollama Cloud SaaS [VF: A4-S085, A4-S084] | Not publicly verified [NPV] | Local in-estate; Cloud US and Europe per vendor [VF: V1-S066] | Ollama; US$65M round reported [R: V1-S071] |
| LM Studio | Proprietary app; CLI MIT [VF: A4-S145, A4-S088] | Desktop only [VF: A4-S087] | Not applicable (desktop software) [AJ] | Local [AJ] | LM Studio [VF: A4-S088] |
| Hugging Face | Hub client and TGI Apache-2.0; services proprietary [VF: A4-S014, A4-S072] | SaaS; Endpoints on AWS/Azure/GCP with PrivateLink [VF: A4-S083, A4-S082] | SOC 2 Type 2 (Hub, Endpoints) [VF: A4-S074, A4-S082] | EU storage region (Team/Enterprise); Endpoints region choice [VF: A4-S078, A4-S083] | Hugging Face; TGI archived 21 Mar 2026 [VF: V1-S054] |
| OpenRouter | Proprietary SaaS; SDK Apache-2.0 [VF: A4-S096] | SaaS only [VF: A4-S107] | SOC 2 Type 2; no BAA [VF: A4-S142] | EU in-region routing (Business/Enterprise) [VF: A4-S109] | Stripe acquisition agreed 19 Aug 2026, pending [VF: V1-S059] |
| Together AI | Proprietary; SDK Apache-2.0 [VF: A4-S093] | Serverless, dedicated, VPC, GPU clusters [VF: A4-S131, A4-S130] | SOC 2 Type 2, ISO 27001:2022 (vendor-stated) [VF: A4-S129, V1-S079] | EU dedicated endpoints on Scale/Enterprise only [VF: A4-S130] | Independent; Series C 1 Jul 2026 [VF: A4-S132] |
| Fireworks AI | Proprietary; SDK Apache-2.0 [VF: A4-S094] | Serverless, dedicated, reserved, BYOC [VF: A4-S152] | SOC 2 Type II, HIPAA; ISO claims conflicting [VF: A4-S133, V1-S067] | EU deployment regions; residency setting US-only self-serve [VF: A4-S134] | Independent; Series D Jul 2026 [VF: A4-S141] |
| Cerebras | Proprietary; SDK Apache-2.0 [VF: A4-S095] | SaaS, dedicated, on-prem CS-3 [VF: A4-S139, A4-S095] | SOC 2 Type 2, GDPR, CCPA; no HIPAA [VF: V1-S095] | None yet; EU capacity targeted end-2026 [VF: A4-S140] | Public (Nasdaq: CBRS) since May 2026 [VF: A4-S137] |

### 2.9 Decision tree

Plan §9 gives the starting example (managed API vs private-VPC managed inference vs own GPUs). The tree below extends it with the questions that decide it in a regulated firm: data classification, residency, capacity, and operating model [Rec].

```text
STEP 0 [Rec] (not optional): every route is called through the gateway (C1); the
OpenAI-compatible API is the contract; each route records model, version, endpoint,
processing region and retention setting; a fallback is qualified (L9) and in region.

STEP 1 [Rec]: What data will the route carry?
  ├─ Public / non-confidential only
  │     → Any approved managed API or router (OpenRouter, HF Inference Providers)
  │       with ZDR on; still through C1.  Go to STEP 3 for capacity.
  └─ Client, personal or confidential data → STEP 2

STEP 2 [Rec]: Is the model you need available, processed in your approved region,
              on your primary cloud's model service?
  ├─ Yes → MANAGED ACCESS (default): Bedrock geographic/in-Region profile,
  │        Foundry Data Zone or Regional deployment, or Vertex regional/multi-region
  │        endpoint. Confirm who operates the model (hyperscaler vs partner).
  │        Go to STEP 3.
  └─ No (model not in region, open-weight model needed, or exit route required)
        → Is the requirement an open-weight model?
           ├─ No  → Use the model vendor's own regional API only if contracted
           │        (DPA, ZDR, region) and registered as a material third party;
           │        otherwise choose a different model (L1).
           └─ Yes → Do you have, or will you fund, GPU capacity AND an SRE team that
                    can patch engines monthly and run on-call?
                    ├─ No  → PRIVATE-VPC MANAGED INFERENCE: Fireworks BYOC or EU
                    │        dedicated deployment; Together EU dedicated endpoint
                    │        (Scale/Enterprise, ZDR on); HF Inference Endpoints in an
                    │        approved region with PrivateLink.
                    └─ Yes → OWN GPUs: vLLM (supported distribution if your operating
                             model needs a vendor), weights from an internal mirror;
                             SGLang qualified as the alternative engine.
                             Multi-node, high volume, Kubernetes standard?
                             ├─ Yes → pilot llm-d (CNCF) or Dynamo (NVIDIA estates)
                             │        as the optimisation layer; non-production first
                             └─ No  → vLLM alone

STEP 3 [Rec]: Capacity
  Is demand bursty but time-critical (month-end, quarter-end)?
  ├─ Yes → reserved / provisioned capacity sized for the peak (Foundry PTU,
  │        Vertex Provisioned Throughput with overflow pinned in region,
  │        Together PTU, Fireworks reserved), plus a qualified in-region fallback
  └─ No  → standard / serverless in-region; batch APIs for non-interactive jobs

STEP 4 [Rec]: Checks before go-live
  Processing region evidenced per call?  ZDR / retention confirmed in the contract,
  not just the console?  Fallback in the same region and qualified?
  Engine version pinned and on the advisory watch list (self-hosted)?
  Exit drill: route moved to the alternative by gateway configuration only?
  Developer runtimes (Ollama, LM Studio): cloud disabled, no client data?
```

### 2.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Serving engine (vLLM, SGLang) | **Acceptable** | Apache-2.0, OpenAI-compatible, interchangeable for most open models [VF: A4-S009, A4-S128, A4-S063, A4-S010] | OpenAI-compatible API to the gateway; engine config in Git |
| Optimisation layer (Dynamo, llm-d) | **Manageable** | Open source, but deployment manifests and CRDs are product-specific; Dynamo is NVIDIA-led [VF: A4-S090, A4-S089] | Keep it removable: engine API stays the contract; Gateway API Inference Extension where possible [VF: A4-S062, A4-S090] |
| Managed inference cloud (Together, Fireworks, Cerebras) | **Manageable** | Open-weight models and standard APIs; contracts for reserved capacity are the switching cost [VF: A4-S131, A4-S152] | Gateway routing; open-weight model qualified on a second provider or engine |
| Hyperscaler model service | **Manageable, with concentration caveat** | Proprietary SDKs and IAM, but called through the gateway; the risk is concentration on one designated provider [VF: R-DORA, A8-S021] | Gateway with provider adapters; second cloud or private route for the stressed-exit case |
| Router in the data path (OpenRouter) | **Unacceptable for client data unless residency and ZDR are contractual; billing intermediation unacceptable for regulated workloads** | It puts a third party between the firm and its model providers, and its owner is changing [VF: V1-S062, V1-S059] | Direct provider contracts and BYOK through the firm's gateway (see C1.10) |
| Proprietary hardware (Cerebras CS-3 on-prem) | **Manageable for speed-critical niches; unacceptable as the only route** | Proprietary wafer-scale stack [VF: A4-S095] | Same models qualified on GPUs |
| Closed frontier model only available through one cloud | **Manageable if a qualified alternative exists** | Gemini is on Google Cloud only [VF: A5-S027] | Portfolio of models (L1) and the gateway exit drill |
| Desktop runtimes (Ollama, LM Studio) | **Acceptable** (developer tier) | Out of the production path [AJ] | None needed; enforce device policy |

### 2.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23.* PRA SS1/23 applies to banks, building societies and PRA-designated investment firms with internal-model approval, and covers vendor models with ongoing performance monitoring [VF: R-PRA-SS123, A8-S008]. For other asset managers it is the natural benchmark [AJ]. In this layer, a change of endpoint, engine version, quantisation level or fallback model can change outputs; treat each as a model change that needs re-qualification by the L9 regression suite [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001, A8-S002]. The firm's own governance must therefore decide which serving changes count as material [AJ].
- *Quantisation is a model change.* Running an open-weight model at FP8 or INT4 on vLLM [VF: A4-S063] is a different numerical system from the provider's reference. Record the quantisation in the model inventory (C8) [Rec].

**EU AI Act.**
- GPAI obligations sit with model providers; the Commission's enforcement powers over GPAI apply from 2 August 2026 [VF: R-EUAIA, A8-S011]. A firm that only serves an unmodified open-weight model is generally a deployer of the system it builds, not a GPAI provider; fine-tuning and redistribution need legal review [AJ].
- Article 26 requires deployers of high-risk systems to keep logs for at least six months; Annex III duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011]. Most asset-management uses, including attribution commentary, are not Annex III [AJ]. Per-call records of endpoint, model version and region from this layer, joined to the gateway log, are the evidence base anyway [Rec].

**DORA, the UK CTP regime and outsourcing.**
- *Designations.* The DORA CTPP list (18 November 2025) and the UK CTP designations (in force 13 July 2026) include AWS, Google Cloud and Microsoft; no AI model provider is designated [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. Managed access through those hyperscalers therefore sits inside an overseen relationship; direct contracts with model vendors, inference clouds and routers do not [AJ].
- *Register of information.* Every inference cloud or router used for a function is an ICT third-party arrangement for the DORA register, with Article 30 terms and exit strategies where it supports a critical or important function [VF: R-DORA, A8-S021] [AJ].
- *Notifications.* PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. Adding an inference provider behind the gateway, or a change of owner such as Stripe–OpenRouter, should be routed through third-party risk with that lead time [Rec].
- *Exit plans.* SS2/21 expects documented and tested exit plans, including stressed exit [VF: R-PRA-SS221, A8-S048]. In this layer, the credible stressed-exit route is an open-weight model already qualified on a portable engine (vLLM) in your own or a second provider's estate, switched by gateway configuration [AJ]. An exit plan that names a second provider but has never been drilled is not tested [AJ].
- *Effective access.* FCA FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. Inference providers must evidence processing location per request; Bedrock's CloudTrail inference-Region field is an example of the evidence to require [VF: B-L2-S005] [Rec].

**Data residency of inference: where prompts are processed.**
- Storage residency and processing residency are different promises. Foundry stores data at rest in the chosen geography regardless of deployment type, but Global deployments may process prompts anywhere [VF: B-L2-S006]. Bedrock keeps stored data in the source Region while geographic profiles move prompts between Regions inside the geography [VF: B-L2-S005]. OpenAI's UK endpoint provides storage only, with no UK processing [VF: V2-S079]. Contracts and configurations must name processing location, not only storage location [Rec].
- UK-specific gap: Bedrock's EU profile does not route to London as a destination for EU-originated requests, and London-originated requests can route to EU Regions [VF: B-L2-S005]. A UK firm needing UK-only processing must check per model whether an in-Region London option exists [Rec]; some models have one (Qwen3, GLM 5 on Bedrock) [VF: A5-S086].
- Transfers: EU-to-US transfers rely on the Data Privacy Framework or SCCs, with an annulment appeal (C-703/25 P) pending [VF: R-DATA-TRANSFERS, A8-S053]. Prefer in-geography processing over transfer mechanisms for client data [Rec].
- Chinese-origin models: the model weights may be acceptable on approved infrastructure even where the vendor's own API is not; DeepSeek's own platform stores personal data in the PRC [VF: A5-S062]. Serve such open weights only on approved infrastructure, and follow the L1 position on their use [Rec].

**ZDR and retention.** ZDR defaults differ: off by default at Together AI [VF: A4-S130]; on by default at Fireworks for open models, except the Response API [VF: A4-S134]; enforceable per request or guardrail at OpenRouter, but not covering tools such as web search [VF: A4-S108]; privacy-policy level only at Cerebras [VF: A4-S153]. Require ZDR in the contract for client-data routes, and verify it in the endpoint configuration that the gateway calls [Rec].

**Capacity risk.** Capacity is an operational-resilience issue, not only a performance one [AJ]. Serverless tiers may have no SLA [VF: A4-S131]; reserved capacity carries one where offered [VF: A4-S131, B-L2-S006]; and overflow behaviour can silently cross a residency boundary (Vertex default overflow to the global endpoint) [VF: B-L2-S008]. Capacity plans for important business services should name the peak, the reserved amount, the overflow behaviour and the degraded mode [Rec].

**Concentration.** IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. This layer concentrates in three ways: one cloud for all model access; one GPU vendor under every self-hosted and most managed routes (Dynamo is NVIDIA-optimised; Together and Fireworks depend on NVIDIA supply) [VF: A4-S090, A4-S132, A4-S141]; and inference clouds with concentrated revenue or customers (Fireworks' reported Cursor share; Cerebras' OpenAI agreement) [VF: A4-S141, A4-S154] [AJ]. The mitigation is a portfolio: the primary cloud's service, plus one private or second-provider route for a qualified open-weight model [Rec]. *Disclosure:* the author is an Anthropic model; Claude is cited here only as an example of multi-cloud availability, and the same rule applies to every model family [AJ].

**Standards.**
- *OWASP.* The OWASP Top 10 for LLM Applications 2026 is the operative list [VF: R-OWASP-LLM, V2-S056]. Supply-chain risk (malicious model files executing on load) and unbounded consumption (capacity abuse) are the categories this layer must address [AJ]; the vLLM and SGLang advisories show the supply-chain risk is concrete [VF: B-L2-S004, B-L2-S009]. The Top 10 for Agentic Applications for 2026 starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042].
- *NIST and ISO.* NIST AI RMF 1.0 and the GenAI Profile (AI 600-1) provide the risk taxonomy; ISO/IEC 42001 the management system [VF: R-NIST-AIRMF, A8-S043, A8-S044; R-ISO-42001, A8-S045]. Fireworks lists ISO/IEC 42001, but its own pages conflict [VF: V1-S067]; vendor regulatory-mapping claims do not raise scores (rule 13) [AJ].

### 2.12 Worked-example slice (POV 3)

**What the commentary agent needs from L2 [AJ].** The deterministic workflow drafts the monthly Brinson-style attribution commentary (allocation, selection, currency, benchmark-relative return) for a generic multi-asset fund. Its drafting calls need the following from this layer:
1. **Drafting through the gateway to a managed, in-region endpoint.** The workflow calls the C1 route `attribution-commentary-draft`; the route's primary endpoint is the primary cloud's model service in the approved UK or EU geography, using an in-Region or geographic deployment, never a global one (Bedrock geographic profile, Foundry Data Zone or Regional, or a Vertex regional endpoint) [VF: B-L2-S005, B-L2-S006, B-L2-S008].
2. **A qualified fallback model.** The fallback is a different model family in the same geography, or an open-weight model on a private-VPC dedicated endpoint (or a vLLM route), which has passed the same L9 regression suite. If neither is available, the route fails closed and the analyst is told the draft is delayed.
3. **No client data to routers without contractual ZDR and residency.** OpenRouter and Hugging Face Inference Providers are excluded from this route. If a router is ever used for this content, it must be under a contract with ZDR and in-region routing, and the router must fail rather than fall back out of region [VF: A4-S109].
4. **A capacity plan for month-end peaks.** All funds' drafts are requested in a narrow window after attribution runs complete. Size reserved capacity (Foundry PTUs or Vertex Provisioned Throughput with overflow pinned in region) for the forecast peak plus margin, and use batch processing for non-urgent regeneration [VF: B-L2-S006, B-L2-S008]. Rehearse the peak in the month before go-live, and track the throttle rate and capacity headroom KPIs (2.3).
5. **Evidence per call.** Endpoint, model and version, quantisation (private routes), processing region (for example from CloudTrail [VF: B-L2-S005]), retention setting and fallback flag go to the gateway record, L9 and the C8 evidence pack.
6. **A stressed-exit route that works.** One open-weight model is kept qualified on vLLM in an approved environment, so that the commentary can still be drafted if the primary provider is withdrawn. The switch is a gateway configuration change, drilled twice a year.

**What L2 must never do [AJ]:**
- process a draft that contains client holdings on a global endpoint, an unassessed router, or a provider with ZDR off
- overflow from reserved capacity to an out-of-region endpoint because the default allows it
- serve the drafting model from an engine version or quantisation that has not passed the regression suite
- load weights from an unscanned public source onto the private route
- generate or alter authoritative numbers; figures come only from the attribution engine through the read-only L4 tool, and the model only drafts narrative

### 2.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| One "inference" layer with nine tiles | Three jobs: serving engines, optimisation/orchestration (Dynamo, llm-d), and model access (inference clouds, routers, hyperscaler services) [VF: A4-S090, A4-S089, A4-S131, A4-S111] | Split into serving → optimisation → access; gateway moves to the control plane as C1 [AJ] |
| Hugging Face "models & APIs" | Four products: Hub, Inference Providers, Inference Endpoints, TGI (repository archived 21 Mar 2026) [VF: A4-S075, A4-S081, V1-S054] | Strategic, conditional: Hub as governed open-weight supply; Endpoints Tactical [Rec] |
| OpenRouter "multi-provider" | Router with budgets, allowlists, ZDR, EU/US routing; SOC 2, no BAA; 5.5% credit fee; Stripe acquisition pending [VF: A4-S111, A4-S142, V1-S062, V1-S059] | Tactical: model-access source behind C1, not the gateway; no client data without contractual ZDR and residency [Rec] |
| Together AI "open-source cloud" | AI-native cloud incl. GPU clusters; ZDR off by default; EU dedicated on Scale/Enterprise [VF: A4-S131, A4-S130] | Tactical: EU dedicated with ZDR on [Rec] |
| Fireworks AI "fast inference" | ZDR on by default (Response API excepted); BYOC; ISO claims conflicting [VF: A4-S134, A4-S152, V1-S067] | Tactical; candidate for Strategic after ISO and residency due diligence [Rec] |
| Cerebras "ultra-scale cloud" | Chip vendor plus inference cloud; public since May 2026; no EU capacity yet [VF: A4-S095, A4-S137, A4-S140] | Tactical: latency-critical, non-confidential workloads [Rec] |
| Ollama "run locally" | MIT local runtime plus Ollama Cloud [VF: A4-S086, A4-S084] | Tactical: developer tier with cloud disabled [Rec] |
| LM Studio "desktop app" | Proprietary app, free for internal business use, no service use [VF: A4-S145] | Tactical: managed desktops only [Rec] |
| vLLM "high-throughput" | 0.31.0, PyTorch Foundation-hosted, supported distribution available [VF: A4-S009, A4-S146, B-L2-S001] | Strategic: default engine for private routes [Rec] |
| SGLang "efficient engine" | 0.5.21, RadixArk steward; open critical advisory [VF: A4-S010, A4-S147, B-L2-S009] | Tactical: qualified alternative engine [Rec] |
| (absent) NVIDIA Dynamo, llm-d | Optimisation layers above engines; beta / sandbox [VF: A4-S098, A4-S089] | Experimental: pilot only [Rec] |
| (absent) Hyperscaler model services | In-geography processing and reserved capacity on Bedrock, Foundry and Google Cloud; hyperscalers designated under DORA and UK CTP [VF: B-L2-S005, B-L2-S006, B-L2-S008, R-UK-CTP] | Default enterprise access route in the primary cloud [Rec] |

**H1 (split L2 into model serving → inference optimisation → model gateway/routing, with the gateway promoted to a control-plane component). Provisional view; verdict in synthesis.**

The evidence supports the split on four counts.

- **The optimisation products define themselves as a separate layer.** Dynamo is "the orchestration layer above inference engines" and does not replace them [VF: A4-S090]; llm-d provides orchestration "above model servers" [VF: A4-S089]; LMCache calls itself "a KV cache management layer" [VF: A4-S091].
- **The access market has separated from serving.** Managed services expose engine choice as a setting (Hugging Face Endpoints offers vLLM, SGLang, TGI, llama.cpp and TEI) [VF: A4-S081], and routers aggregate many providers' served models [VF: A4-S075, A4-S113]. Hyperscalers sell processing location and reserved capacity as properties of the access contract, independent of the model [VF: B-L2-S005, B-L2-S006, B-L2-S008].
- **Routing and governance have moved upward.** OpenRouter added budgets, allowlists, ZDR enforcement and regional routing [VF: A4-S111, A4-S109]. The C1 evidence shows gateways now carry model, tool and agent traffic, and its provisional view promotes the gateway to the control plane as an "AI traffic gateway" (see C1.13).
- **The kinds of risk differ by sub-layer.** Engines carry supply-chain and patching risk [VF: B-L2-S004, B-L2-S009]; optimisation layers carry maturity risk [VF: A4-S098, B-L2-S002]; access carries third-party, residency and capacity risk [VF: A4-S130, B-L2-S008]. Different risks need different owners [AJ].

The counter-evidence is twofold. First, optimisation techniques also ship inside the engines: vLLM and SGLang both include prefix caching, speculative decoding, quantisation and disaggregation [VF: A4-S063, A4-S010], so for most firms "inference optimisation" is a configuration of the engine, not a separate product. Second, the boundary between optimisation-layer routing and the gateway blurs at the Kubernetes edge: Dynamo and llm-d both plug into the Gateway API Inference Extension [VF: A4-S090, A4-S062]. That in-cluster router chooses a replica, while C1 chooses a provider, model and region [AJ].

**Provisional recommendation.** Redraw L2 as three sub-layers: **model serving** (engines; vLLM and SGLang), **inference optimisation** (an optional fleet layer; llm-d, Dynamo, LMCache, and engine-native features), and **model access** (hyperscaler model services, inference clouds, dedicated endpoints and routers) [AJ]. Move routing policy, fallback, budgets, guard invocation and the request log out of L2 into the control plane as C1, consistent with C1's provisional "AI traffic gateway" [AJ]. Mark the optimisation sub-layer as relevant only to firms that run their own GPU fleets [AJ]. **Provisional; verdict in synthesis.**
