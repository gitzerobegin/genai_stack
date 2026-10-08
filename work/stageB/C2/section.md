## C2. Guardrails

> **Executive summary.** Guardrails are the run-time checks that sit on either side of a model or agent call: they inspect what goes in (user input, retrieved documents, tool results) and what comes out (text, tool calls), and they block, transform or flag it against policy [AJ]. The original graphic has no guardrail control; its only safety-adjacent tiles are the L9 evaluation and red-teaming tools, which test before release but block nothing at run time [VF: A1-S062, A1-S068] [AJ]. Three things define the market in October 2026. First, the hyperscalers now ship broad managed services: Bedrock Guardrails covers content and prompt-attack filters, denied topics, PII, contextual grounding and Automated Reasoning [VF: A6-S072]; Azure Prompt Shields has been GA since August 2024, with Task Adherence for agent tool use in preview [VF: A6-S055]; and Google's Model Armor enforces data residency by default [VF: A6-S067, B-C2-S003]. Second, the open-source options are fragile: NeMo Guardrails is still 0.x Beta [VF: A6-S003], Meta has released no new Llama Guard, Prompt Guard or LlamaFirewall since May 2025 [VF: A6-S006, A6-S107], and Harvey announced its acquisition of Guardrails AI on 9 September 2026, after the project had retired hosted remote inference [VF: A6-S028, V2-S026, V2-S071]. Third, guardrails are moving towards agent behaviour, checking tool use and goal hijacking [VF: A6-S055, A6-S039]. **Recommendation:** own the guardrail policy and its test set; invoke guardrails from the gateway (C1) as a layered set of deterministic rules, small classifiers and, only where needed, model-based checks; and remember that a guardrail cannot make an autonomous workflow safe that should have been a deterministic one (L3) [Rec].

### C2.1 Responsibility

**The problem this control owns.** At run time, stop inputs and outputs that breach policy, and record why [AJ]. It breaks down into six jobs:

- **Input controls.** Detect prompt injection and jailbreaks in user input and, more importantly for agents, in retrieved documents and tool results (indirect injection) [AJ]. Azure Prompt Shields covers both user-input and document attacks [VF: A6-S054].
- **Output controls.** Block or transform harmful, off-policy, leaking or ungrounded output [AJ].
- **Policy enforcement.** Denied topics, word lists, regulated-advice restrictions and house rules [VF: A6-S072] [AJ].
- **Content safety.** Harm categories with thresholds [VF: A6-S054, A6-S067].
- **Grounding checks.** Is the output supported by the supplied context, and are its numbers the authoritative ones? [VF: A6-S072] [AJ]
- **Agent-behaviour checks.** Is the agent's tool use aligned with the task? Azure Task Adherence (preview) and LlamaFirewall AlignmentCheck target this [VF: A6-S055, A6-S039].

**Three kinds of mechanism [AJ].** The distinction matters for latency, cost, explainability and false positives:

| Mechanism | Examples | Behaviour |
|---|---|---|
| **Rules** (deterministic) | Word filters, denied-topic lists, regex and entity patterns, numeric comparators | Fast, explainable, brittle; false positives are predictable and fixable |
| **Classifiers** (small trained models) | Prompt Guard 2 (22M/86M), Llama Guard 4 (12B), Prompt Shields, content filters | Fast to moderate; probabilistic; thresholds need tuning per domain and language |
| **Model-based judges** (an LLM checks the output) | NeMo self-check rails, LlamaFirewall AlignmentCheck (chain-of-thought auditing) [VF: A6-S036, A6-S039] | Flexible, slow and costly; can be manipulated by the same text it judges; needs calibration |

Bedrock's Automated Reasoning checks sit apart from all three as a formal-reasoning check [VF: A6-S072]; its exact mechanism was not reviewed in the fact base [NPV].

**Hand-offs.** C2 is invoked by the gateway (C1) before and after model and tool calls, and by the workflow (L3) at its own checkpoints [AJ]. It shares PII detection with C3 (C3 owns tokenisation and residency; C2 owns blocking) [AJ]. It shares detectors and attack datasets with L9 (offline red-teaming) and C7 (security testing) [AJ]. Its decisions feed C8 evidence [AJ].

**What the control does not own.** It does not own the decision about how much autonomy a workflow has (L3), the authorisation of tool calls (C4), or the validation of output quality over time (L9) [AJ].

### C2.2 Why it matters

**Guardrails cannot fix a workflow that should never have been autonomous [AJ].** This is the central design point for this control. A guardrail is a filter on a stream of actions; it reduces the probability that a bad action passes, but it does not reduce the number of actions an agent is allowed to attempt. If an agent has write access to a client-facing system, a content filter on its output is not a control over that access [AJ]. The plan's worked example is built as "a deterministic workflow, not a free agent", with read-only tools and a human approval gate; most of its safety comes from that design, and the guardrails are the second line [AJ]. The OWASP Agentic list starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042], and the most effective mitigation for goal hijack is to give the agent no goal it can be hijacked towards: fixed steps, read-only tools, scoped identity [AJ].

When guardrails are badly designed, four things go wrong [AJ]:
- **Wrong place.** Only the user's prompt is screened, while retrieved documents and tool results, the real injection path for agents, pass unchecked.
- **Wrong mechanism.** A content-safety classifier is asked to catch a business error it was never trained for, such as a wrong sign on a currency effect.
- **False positives drive bypass.** An over-sensitive filter blocks legitimate finance vocabulary, users route around it, and the control disappears.
- **Fail open.** A guard times out and the gateway passes the request.

**Illustrative scenario [AJ].** A fund-reporting workflow retrieves a broker's market note to add context to the monthly commentary. The note's PDF contains text in a white font: an instruction to describe the fund's currency effect as positive and to omit the selection effect. The firm's guardrails screen the analyst's request for jailbreaks and the model's output for harmful content and PII. Neither check fires: the analyst's request is benign, and the output is polite, harmless and contains no personal data. The draft goes to the portfolio manager with a reversed currency effect and a missing paragraph. It is caught only because the numeric check in L9 compares each figure and direction word with the attribution engine output. Afterwards the team adds two controls: a prompt-attack check on every retrieved chunk before it enters the prompt, and the same deterministic numeric comparator inline as a blocking output guard, not only as an offline evaluation. The scenario is invented; it is not a reported incident.

### C2.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Attack catch rate | Share of red-team attack cases (OWASP LLM and Agentic 2026) blocked or flagged | No critical misses at release; tracked per attack class and language | Red-team suite in CI (L9), replayed against the live guardrail configuration |
| False-positive rate | Share of a labelled benign set (real, approved finance text) blocked | Set per route; e.g. below 1% for drafting routes | Benign regression set run on every threshold or version change |
| Indirect-injection coverage | Share of retrieved chunks and tool results screened before entering a prompt | 100% for external or third-party content | Gateway and workflow logs |
| Numeric grounding pass rate | Drafts whose figures and direction words all match the authoritative source | 100% to release; any miss blocks | Deterministic comparator, inline and in L9 |
| Added latency | p95 latency added per guard and per route | Budget per route (e.g. small classifiers in tens of milliseconds; judges only where justified) | Guard spans in the trace |
| Guard cost per 1,000 requests | Unit cost of all guards on a route | Visible to C6; reviewed quarterly | Vendor unit prices times guard volume |
| Fail-closed conformance | Guard failures (timeouts, errors) that let a request through | 0 on regulated routes | Chaos tests; guard outcome logs distinguishing block from failure |
| Override and tuning trail | Threshold changes and overrides with approver and reason | 100% recorded | C5 change log |
| Bypass detection | Calls that reach a model without passing the route's guards | 0 | Gateway coverage reconciliation (C1) |

### C2.4 How it works

Guardrails are a pipeline of checks placed at four points [AJ]:

1. **On input**, before the prompt is assembled: user request screening (jailbreak, policy), PII handling via C3.
2. **On context**, before retrieved documents and tool results enter the prompt: prompt-attack screening of each chunk. Prompt Guard 2 has a 512-token window [VF: A6-S030], so long documents must be chunked before screening [AJ].
3. **On output**, before the response leaves: harm categories, PII leakage, policy topics, grounding against context, and deterministic business checks.
4. **On action**, before a tool call executes: alignment of the call with the task. Azure Task Adherence (preview) detects misaligned or premature tool use [VF: A6-S055]; Foundry guardrails can inspect tool calls and tool responses (preview), but only for Foundry Agent Service agents [VF: A6-S103]. Authorisation of the call itself belongs to C4 [AJ].

Each check returns allow, block or transform. NeMo Guardrails' IORails engine formalises this as an engine-neutral `RailOutcome` contract and distinguishes policy blocks from rail execution failures [VF: A6-S036]. That distinction is what lets a route fail closed on errors without treating every error as a policy event [AJ].

**Where the checks run.** Guardrails can run inside the application (library), as a sidecar or server, or as a managed service invoked by the gateway. The gateways all expose hooks: LiteLLM runs guardrails pre-call, during the call or post-call across chat, embeddings, MCP and A2A routes [VF: A6-S015]; Kong integrates AWS, Azure and GCP guardrail services and NeMo Guardrails [VF: A6-S017]; APIM applies Content Safety to MCP tool-call arguments and A2A payloads [VF: A6-S020]; Apigee calls Model Armor inline [VF: A6-S024]. Bedrock's `ApplyGuardrail` API applies Bedrock policies to content from any model [VF: A6-S073].

```text
 user request ─► [input rules + jailbreak classifier] ─┐
                                                       ▼
 retrieved docs / tool results ─► [chunk ─► prompt-attack classifier] ─► prompt assembly (L3)
                                                                              │
                                                       gateway (C1) ─► model (L1/L2)
                                                                              │
 output ◄─ [deterministic business checks: numbers, signs, terms] ◄─ [harm / PII / topic / grounding] ◄┘
   │            (rules: block on any mismatch)              (classifiers; judge only where needed)
   ▼
 human review (L3 gate) ──► release        every outcome ─► trace (L9) ─► evidence (C8)
 proposed tool call ─► [task-alignment check] ─► C4 authorisation ─► tool (L4)
```

**Latency and cost.** Every guard adds both, and they stack [AJ]. The unit economics differ by mechanism:

- Small classifiers are cheap: Prompt Guard 2's 22M variant is designed for low-latency, low-compute use, while Llama Guard 4 is a 12B model needing GPU-class serving [VF: A6-S030].
- Managed services price per volume: Bedrock bills per 1,000 text units per configured policy (content filters and denied topics US$0.15, sensitive-information filters US$0.10, Automated Reasoning US$0.17, as of 7 October 2026) [VF: A6-S101]; Model Armor is free to 2M tokens a month, then US$0.10 per 1M tokens [VF: A6-S067]; Azure Content Safety bills per 1,000 text records per model, a record being up to 1,000 characters, and its S0 unit prices could not be verified [VF: A6-S102, A6-S054]; Cloudflare's guardrails are billed as Workers AI inference [VF: A6-S052].
- Model-based judges cost a model call each and add the most latency [AJ].

Route-level design follows: deterministic rules everywhere, small classifiers on all untrusted input, managed or larger classifiers on output, and model-based judges only on routes where nothing cheaper can decide [Rec].

### C2.5 Enterprise design principles

**Security**

- Screen indirect inputs (retrieved documents, tool results, emails), not only user prompts [Rec]. ASI01 Agent Goal Hijack is the first entry in the OWASP Agentic list [VF: R-OWASP-AGENTIC, A8-S042].
- Fail closed on regulated routes. NeMo's streaming output rails fail closed when actions fail (0.24.0) [VF: A6-S036]; LiteLLM's prompt-injection guardrails are off by default [VF: A6-S015]. Configure and test the behaviour explicitly [Rec].
- Do not let one model judge itself. A judge that reads attacker-controlled text can be attacked by it [AJ].
- Do not rely on one detector family. An independent tester reported Prompt Guard weak against non-English and obfuscated prompts [R: A6-S031]. Layer classifiers from different vendors and include multilingual cases in the test set [Rec].

**Scalability, resilience and cost**

- Give each guard a latency budget and a timeout, with a defined outcome on timeout [Rec].
- Run cheap checks first and stop early on a block [AJ].
- A managed guardrail service in a different provider or region from the model adds a dependency and a data flow; include it in the resilience and residency analysis [AJ].

**Governance and false-positive management**

- Version guardrail configurations, thresholds and detector versions in C5, and record which version made each decision [Rec].
- Maintain two datasets: an attack set (OWASP-mapped, multilingual) and a benign set of real approved text from the domain. Every threshold change runs both [Rec].
- Provide a governed override path: an analyst can request release of a blocked draft, a second person approves, and the case joins the benign set if it was a false positive [Rec]. Without that path, users find their own bypass [AJ].
- Classify each guard's decisions as policy blocks or execution failures, so failures are fixed and blocks are reviewed [VF: A6-S036] [AJ].

**Observability**

- Emit each guard decision (guard, version, score, threshold, outcome, latency) as a span on the request trace (L9) [AJ].
- Watch block rates per route; a sudden rise is either an attack or a regression in the guard [AJ].

**Portability**

- Keep the policy (what is forbidden, and on which route) separate from the detector (which product detects it) [AJ]. Then a vendor change swaps detectors without rewriting policy [AJ].

**Patterns [AJ]:** guardrails invoked from the gateway; layered rules → classifiers → judges; screening of every retrieved chunk; deterministic business checks as blocking output guards; benign and attack regression sets; governed overrides; policy separate from detector.

**Anti-patterns [AJ]:** guardrails as a substitute for workflow design; screening only the user prompt; a content-safety classifier as the only output check for a numbers-heavy document; LLM-as-judge for checks a regex or comparator can do; thresholds tuned once on vendor defaults; silent fail-open on guard timeout; a guardrail service outside the approved region for client data.

### C2.6 Product selection criteria

| Scorecard criterion | What to evaluate in this control [AJ] |
|---|---|
| Technical (15% FS) | Coverage of input, indirect-input, output, grounding and tool-use checks; which mechanisms (rules, classifiers, judges); multilingual performance on your data; configurable thresholds; block vs transform; standalone API usable from any gateway |
| Enterprise readiness (15%) | Identity and audit on configuration changes; versioned configurations; support |
| Security and compliance (20%) | Certifications naming the service; CMK; fail-closed behaviour; for self-hosted, release hygiene and licence clarity |
| Deployment flexibility (15%) | Self-hosted or in-region managed service; residency enforcement of guard inference |
| Ecosystem (5%) | Gateway integrations (LiteLLM, Kong, APIM, Apigee); framework integrations |
| Reliability and maturity (10%) | GA vs preview; release cadence; ownership stability; maintenance risk |
| Cost / TCO (5%) | Unit price per policy and per volume; GPU cost for self-hosted classifiers; judge-token cost |
| Lock-in / portability (15%) | Proprietary API vs open weights or open source; whether policies can be expressed outside the vendor |

### C2.7 Product deep dives

**NVIDIA NeMo Guardrails (NVIDIA).**
- *What it is now:* an Apache-2.0 toolkit for programmable rails: content safety, topic safety and jailbreak detection (including a NIM-based jailbreak model), self-check rails, Colang dialogue rails and third-party integrations. It runs as a library or as an OpenAI-compatible Guardrails server with a `/v1/checks` endpoint [VF: A6-S036, A6-S027]. Version 0.24.1 was released on 16 September 2026 [VF: A6-S003, V2-S028].
- *Direction:* the new IORails engine runs input, output and tool rails without a Colang runtime dependency, with an allow/block/transform contract and typed rail manifests; F5 AI Guardrails is among the new integrations [VF: A6-S036, A6-S027].
- *Commercial packaging:* the NeMo Guardrails microservice (Helm on customer Kubernetes) is "NVIDIA AI Enterprise Supported", listed at US$4,500 per GPU per year or US$1 per GPU-hour on cloud marketplaces [VF: A6-S111, A6-S112]. The microservice supports Colang 1.0 configurations only and lacks some toolkit server features [VF: A6-S111].
- *Strengths:* the widest set of rail types in one in-estate framework, and an explicit distinction between policy blocks and execution failures [VF: A6-S036] [AJ].
- *Limitations:* still 0.x, classified Beta, with breaking changes in minor releases (for example, the `/v1/checks` inline config removal in 0.24.0) [VF: A6-S003, A6-S036]. Model-based rails depend on NIM, Nemotron or another LLM endpoint [VF: A6-S027]. NVIDIA pages disagree on the number of content-safety categories (23 vs 42) [NPV].
- *Choose when:* you want an in-estate orchestration layer that combines rules, classifiers and model-based checks [AJ].
- *Avoid when:* you cannot absorb breaking changes in a pre-1.0 dependency [AJ].
- *Competitors:* Guardrails AI, Llama Protections, Check Point AI Guardrails (C7).
- *FS note:* pin versions, call it from the gateway as a server, and gate every upgrade on the attack and benign regression sets [Rec].
- **Tier: Tactical; a Strategic candidate at 1.0 [AJ]. Flag: none.**

**Guardrails AI (Harvey).**
- *What it is now:* an Apache-2.0 Python framework that runs input and output Guards built from composable validators, supports structured-output validation and offers a Guardrails Server REST API [VF: A6-S037, A6-S029]. Version 0.11.0 was released on 14 August 2026 [VF: A6-S004, V2-S028].
- *Distribution change:* on 6 July 2026 the project announced that validators would move to standard PyPI packages and hosted remote inference would end. The repository notice gives a hard cutoff of 25 August 2026; the docs-site migration guide gives 6 August 2026 [VF: A6-S037, V2-S071, V2-S072]. Plan as if hosted inference ended on 6 August [AJ].
- *Ownership:* Harvey, a legal AI application company, announced the acquisition on 9 September 2026; terms were not disclosed, and the co-founders joined Harvey to work on agent reliability [VF: A6-S028, V2-S026]. The open-source roadmap after the acquisition is not stated [VF: A6-S028].
- *Strengths:* a simple validator model for format and structured-output checks [AJ].
- *Limitations:* 0.x [VF: A6-S004]; enterprise platform pricing known only from a secondary source [R: A6-S028]; release hygiene not verified [NPV].
- *Choose when:* you already depend on it for structured-output validation [AJ].
- *Avoid when:* choosing a new strategic guardrail dependency [AJ].
- *Competitors:* NeMo Guardrails, Llama Protections, Opik's guardrails (L9) [VF: A1-S067].
- *FS note:* freeze and vendor the validators you use, and plan a migration path [Rec].
- **Tier: Experimental. Flag: Acquired.**

**Llama Protections: Llama Guard 4, Prompt Guard 2, LlamaFirewall (Meta).**
- *What it is now:* Llama Guard 4 (12B) classifies prompts and responses, in text and images, against a safety taxonomy; Prompt Guard 2 (86M and 22M) detects prompt injection and jailbreaks within a 512-token window; LlamaFirewall combines PromptGuard, AlignmentCheck (chain-of-thought auditing for goal hijacking) and CodeShield across agent inputs, reasoning and outputs [VF: A6-S030, A6-S039, A6-S038].
- *Release status:* the newest releases found are the Llama Guard 4 and Prompt Guard 2 checkpoints of 29 April 2025 and llamafirewall 1.0.3 of 29 May 2025. A second vendor-domain search on 7 October 2026 found nothing newer, and Meta's model cards still present Llama Guard 4 as "the latest safeguard model" [VF: A6-S006, A6-S030, A6-S107, V2-S028].
- *Licence:* Llama Guard 4 is under the Llama 4 Community License, including a 700M monthly-active-user clause and an Acceptable Use Policy; the LlamaFirewall licence is not stated on PyPI [VF: A6-S030, A6-S038, A6-S006].
- *Ecosystem:* Cloudflare AI Gateway runs Llama Guard 3 8B for its guardrails, and Guardrails Hub has a Llama Guard validator [VF: A6-S052, A6-S029]. The models are also available through the Llama API moderations endpoint, NVIDIA build and Vertex Model Garden [VF: A6-S030].
- *Strengths:* a very small prompt-attack classifier suited to screening every retrieved chunk, and an alignment check aimed at agent goal hijacking [VF: A6-S030, A6-S039] [AJ].
- *Limitations:* seventeen months without a release is a maintenance risk for a security control [AJ]. An independent tester reported Prompt Guard weak against non-English and obfuscated prompts [R: A6-S031].
- *Choose when:* you want a free, in-estate first-pass classifier inside a broader framework [AJ].
- *Avoid when:* it would be your only prompt-attack defence [AJ].
- *Competitors:* Azure Prompt Shields, Model Armor, Check Point AI Guardrails (C7).
- *FS note:* use as one detector among several, with your own multilingual test set, and record the licence terms in the inventory [Rec].
- **Tier: Tactical. Flag: none** (maintenance risk stated in the rationale).

**Amazon Bedrock Guardrails (Amazon Web Services).**
- *What it is now:* managed guardrails applied to prompts and responses: content filters for sexual content, violence, hate, insults, misconduct and prompt attack; denied topics; word filters; PII detection with block or anonymise actions across 31 entity types, including UK NHS and National Insurance numbers, IBAN and SWIFT; contextual grounding checks; and Automated Reasoning checks [VF: A6-S072, A6-S073]. The standalone `ApplyGuardrail` API applies them to content from any model [VF: A6-S073].
- *Tiers and residency:* content filters and denied topics have Classic and Standard tiers since June 2025; the Standard tier uses cross-region inference [VF: A6-S072, A6-S101]. Cross-region guardrail profiles route guardrail inference to defined destination regions [VF: A6-S072].
- *Security and certifications:* guardrails can be encrypted with a customer KMS key [VF: A6-S072]. Bedrock has been in AWS's SOC 1, 2 and 3 scope since 15 August 2023 (Marketplace excluded) and is on AWS's ISO 27001 list; Guardrails is not named separately, and AWS treats generally available features as in scope unless excluded [VF: B-C2-S001, B-C2-S002].
- *Pricing:* per 1,000 text units (1,000 characters), billed per configured policy: US$0.15 for content filters and denied topics, US$0.10 for sensitive-information filters, US$0.17 for Automated Reasoning, as of 7 October 2026; the last two are inferred from AWS worked examples [VF: A6-S101].
- *Strengths:* the broadest managed policy set here, and the only one in the fact base with both grounding and Automated Reasoning checks [AJ].
- *Limitations:* AWS-only; `InvokeGuardrailChecks` appears in the runtime API but its GA status was not verified [VF: A6-S073] [NPV].
- *Choose when:* you run on AWS, or want managed guardrails callable for non-Bedrock models [AJ].
- *Avoid when:* the Standard tier's cross-region inference conflicts with your residency rules [AJ].
- *Competitors:* Azure AI Content Safety, Model Armor, NeMo Guardrails.
- *FS note:* use the Classic tier or region-constrained profiles for client data, and measure false positives per policy on your own benign set [Rec].
- **Tier: Strategic, conditional: where AWS is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. Flag: none.** It is AWS's lead guardrail service and the broadest managed policy set here. The condition includes the Classic tier or region-constrained profiles for client data, because the Standard tier uses cross-region inference [AJ].

**Azure AI Content Safety (Microsoft).**
- *What it is now:* APIs that analyse text and images for sexual, violence, hate and self-harm content with severity levels; Prompt Shields for user-input and document attacks; protected-material detection; groundedness detection (preview); custom categories (preview); and Task Adherence for agent tool use (preview) [VF: A6-S054, A6-S055]. Product and pricing pages are now titled "Content Safety in Foundry Control Plane" [VF: A6-S102].
- *Status:* Prompt Shields and protected material (text) GA in August 2024; Task Adherence public preview in November 2025 [VF: A6-S055]. Superseded API versions follow a 90-day deprecation policy [VF: A6-S054, A6-S055]. The Learn source pages are dated 16 September 2025, so 2026 changes may not be reflected [NPV].
- *Integration:* called from APIM through the `llm-content-safety` policy, now including MCP and A2A traffic [VF: A6-S020, A6-S053]. Microsoft Foundry "guardrails" are named collections of controls built on Content Safety models; tool-call inspection is preview and limited to Foundry Agent Service agents [VF: A6-S103].
- *Security:* encryption at rest with customer-managed keys [VF: A6-S054]. Azure's ISO 27001 and SOC 2 attestations are stated at platform level without naming the service [VF: B-C1-S007, B-C1-S008].
- *Pricing:* free tier of 5,000 text records a month; S0 billed per 1,000 records per model; published S0 unit prices could not be verified [VF: A6-S102, A6-S054].
- *Strengths:* document-attack screening that is GA, enforceable at the gateway on tool and agent payloads [AJ].
- *Limitations:* the agent-oriented and grounding features are preview [VF: A6-S055].
- *Choose when:* you run on Azure and use APIM as the gateway [AJ].
- *Avoid when:* you need GA groundedness checks or a guardrail outside Azure [AJ].
- *Competitors:* Bedrock Guardrails, Model Armor, Check Point AI Guardrails (C7).
- *FS note:* apply Prompt Shields to retrieved documents, not only user input; keep preview features off regulated routes [Rec].
- **Tier: Strategic, conditional: where Azure is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. Flag: none.** It is Azure's lead guardrail service. The condition covers GA features only (Prompt Shields, protected material) on regulated routes; the agent-oriented and groundedness features are preview. Cost at 2 is accepted under rule 11 because the condition is an existing platform commitment [AJ].

**Model Armor (Google Cloud).**
- *What it is now:* a managed service that screens prompts, responses and agent interactions for prompt injection and jailbreaks, malicious URLs and files, harmful content with adjustable thresholds, and sensitive-data leaks, built on Sensitive Data Protection [VF: A6-S067]. It is invoked inline from Apigee, Gemini Enterprise Agent Platform, Google MCP servers, Service Extensions, Firebase or LangChain [VF: A6-S067].
- *Residency:* templates enforce data residency strictly by default, disabling any feature not hosted in the template's jurisdiction [VF: B-C2-S003]. Model Armor runs in six European regions plus the `eu` multi-region; Madrid and Paris were added on 27 March 2026 [VF: B-C2-S004]. London (europe-west2) has reduced features in template mode and enforces only at-rest residency for floor settings, although the 8 July 2026 release notes say UK in-use and in-transit residency is supported with limited features; the sources conflict [VF: B-C2-S003, B-C2-S005].
- *Certifications and price:* listed in Google Cloud's SOC 2 and ISO/IEC 27001 scope [VF: A6-S070, A6-S071]. Free to 2M tokens a month, then US$0.10 per 1M tokens, as of 7 October 2026 [VF: A6-S067].
- *Strengths:* the clearest residency model of the managed services, at a low unit price [AJ].
- *Limitations:* grounding and denied-topic checks are not in the fact base [NPV]; GA date not verified [NPV].
- *Choose when:* you run on Google Cloud or Apigee [AJ].
- *Avoid when:* you need grounding checks, or full features in London [AJ].
- *Competitors:* Bedrock Guardrails, Azure AI Content Safety, Check Point AI Guardrails (C7).
- *FS note:* leave strict residency on and pin templates to an EU region; confirm the London position in writing if UK residency is required [Rec].
- **Tier: Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. Flag: none.** It is Google's lead guardrail service. It is narrower than Bedrock (grounding checks not evidenced), so pair it with a grounding check elsewhere where one is needed [AJ].

**Related products scored elsewhere.** Check Point AI Guardrails (formerly Lakera Guard) screens prompts and responses for prompt attacks, data leakage and off-policy agent behaviour, and is scored in C7 [VF: A7-S025]. Prisma AIRS inspects prompts and responses at runtime and is also scored in C7 [VF: A7-S027]. Opik ships guardrails within its L9 platform [VF: A1-S067], and Datadog detects prompt injection in its L9 module [VF: A1-S097].

### C2.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C2-nemo-guardrails | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 4 | 3.50 | 3.45 | Tactical |
| C2-guardrails-ai | 3 | 2 | 2 | 3 | 3 | 2 | 4 | 3 | 2.70 | 2.60 | Experimental |
| C2-meta-llama-protections | 3 | 2 | 2 | 5 | 4 | 2 | 4 | 3 | 3.10 | 2.95 | Tactical |
| C2-bedrock-guardrails | 5 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.50 | 3.35 | Strategic |
| C2-azure-ai-content-safety | 4 | 4 | 4 | 2 | 4 | 3 | 2 | 2 | 3.30 | 3.20 | Strategic |
| C2-google-model-armor | 4 | 4 | 4 | 2 | 4 | 3 | 5 | 2 | 3.60 | 3.35 | Strategic |

**Scoring notes [AJ]:**
- *No product is Strategic on score.* None reaches 3.6 FS. The three managed services (Bedrock Guardrails, Azure AI Content Safety, Model Armor) are Strategic, conditional, "where this is your primary cloud" under rubric rule 10 (CP3 Q2): each is its cloud's lead guardrail service and none has a criterion at 1. No criterion scores changed, and security stays at 4 under rule 8. The firm's own guardrail policy, its attack and benign test sets, and the gateway hooks that invoke detectors are still the durable asset; the detectors behind them should stay substitutable, which is why the open-source frameworks remain Tactical.
- *Hyperscaler presumption (CP2 Q1).* Bedrock Guardrails, Azure AI Content Safety and Model Armor score 4 on enterprise readiness: platform controls presumed (CP2 Q1); confirm per service.
- *Scope rule (CP2 Q4).* Bedrock Guardrails and Azure AI Content Safety score 4, not 5, on security because their certifications are stated for Bedrock or Azure without naming the guardrail service (B-C2-S001, B-C2-S002, B-C1-S007, B-C1-S008). Model Armor is named in Google's scope but CMK is not verified, so 4.
- *Rule 2 (self-hosted software and open weights).* NeMo Guardrails, Guardrails AI and the Llama Protections are scored as software you run, so the NPV cap does not apply. NeMo has commercial support through NVIDIA AI Enterprise; the other two have none verified.
- *Rule 3 (ownership change).* Guardrails AI's lock-in is reduced by 1: Apache-2.0, but owned by an application company rather than a neutral body.
- *Maturity of the managed services.* Bedrock Guardrails, Azure AI Content Safety and Model Armor all score 3. Bedrock had been 4; it was aligned at the CP3 review because its maturity fact cell is not verified (pricing dates from December 2024), while Azure's Prompt Shields has a verified GA date of August 2024 [VF: A6-S101, A6-S055].
- *Maturity.* Three products score 2 on maturity for three different reasons: pre-1.0 Beta (NeMo), acquisition plus distribution change (Guardrails AI) and no release for 17 months (Meta).

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| NeMo Guardrails | Apache-2.0 [VF: A6-S003] | Library, server, Helm microservice [VF: A6-S036, A6-S111] | Not applicable (software); NVIDIA certifications for the microservice NPV | In-estate [AJ] | NVIDIA [VF: A6-S003] |
| Guardrails AI | Apache-2.0 [VF: A6-S004] | Self-host only [VF: A6-S037] | Not applicable (software) | In-estate [AJ] | Harvey, announced 9 Sep 2026 [VF: A6-S028, V2-S026] |
| Llama Protections | Llama community licences [VF: A6-S030, A6-S038] | Open weights, self-host; third-party hosting [VF: A6-S030] | Not applicable (weights) | In-estate [AJ] | Meta [VF: A6-S031] |
| Bedrock Guardrails | Proprietary [VF: A6-S072] | Managed AWS [VF: A6-S072] | Bedrock in SOC 1/2/3 and ISO 27001 scope; Guardrails not named [VF: B-C2-S001, B-C2-S002] | Region-dependent; Standard tier cross-region [VF: A6-S072] | Amazon Web Services |
| Azure AI Content Safety | Proprietary; SDK MIT [VF: A6-S054, A6-S084] | Azure resource [VF: A6-S054] | Azure ISO 27001, SOC 2 platform-level [VF: B-C1-S007, B-C1-S008] | Region list not reproduced [VF: A6-S054] | Microsoft |
| Model Armor | Proprietary [VF: A6-S067] | Managed Google Cloud, regional endpoints [VF: B-C2-S003] | SOC 2 and ISO 27001 scope [VF: A6-S070, A6-S071] | Six EU regions plus `eu`; strict by default [VF: B-C2-S003, B-C2-S004] | Google Cloud |

### C2.9 Decision tree

```text
STEP 0 [Rec] (not optional): decide the workflow's autonomy FIRST (L3).
  Can the task be a deterministic workflow with read-only tools and a human gate?
  ├─ Yes → build it that way; guardrails are the second line
  └─ No  → document why; tool authorisation (C4) and approval gates come before guardrails

STEP 1 [Rec]: Deterministic checks (always, in-house)
  Business invariants (numbers, signs, terms, forbidden phrases, identifiers) → rules/comparators
  coded by the firm, run inline as blocking output guards and in L9 CI

STEP 2 [Rec]: Managed or self-hosted detectors for injection, harm and PII?
  Where does the model run?
  ├─ AWS          → Bedrock Guardrails (Classic tier / region-pinned for client data) via ApplyGuardrail
  ├─ Azure        → Azure AI Content Safety (Prompt Shields on user input AND documents) via APIM
  ├─ Google Cloud → Model Armor (strict residency on, EU template) via Apigee
  └─ Multi-cloud or in-estate required →
        NeMo Guardrails server (pinned) orchestrating:
          Prompt Guard 2 (22M) on every retrieved chunk  +  a second, independent detector
          (a managed service above, or Check Point AI Guardrails, C7)

STEP 3 [Rec]: Model-based judges?
  Only where no rule or classifier can decide (e.g. tone, policy nuance); never as the sole
  check on numbers; calibrated against human labels (L9) before it blocks anything

STEP 4 [Rec]: Agent tool use
  Tool calls → C4 authorisation (deny by default) first;
  task-alignment checks (Azure Task Adherence, LlamaFirewall AlignmentCheck) only as extra signal

STEP 5 [Rec]: Checks before go-live
  Attack set (OWASP LLM and Agentic 2026, multilingual) and benign set both passed?
  Guards fail closed on timeout? Guard inference in the approved region? Override path governed?
```

### C2.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Guardrail policy (what is forbidden, per route) | **Unacceptable if held only in a vendor console** | It is the firm's control statement and validation evidence | Policy as code in Git (C5), referencing detectors by role |
| Detector product (classifier or managed service) | **Acceptable** | Detectors are substitutable if called through the gateway | Gateway guard hooks (C1); per-detector adapters |
| Managed guardrail APIs (Bedrock, Azure, Google) | **Manageable** | Proprietary APIs, but policies are simple to re-express [VF: A6-S072, A6-S054, A6-S067] | Standalone API calls from the gateway rather than model-coupled configuration |
| Open weights under community licences | **Manageable** | Portable, but licence terms and maintenance are risks [VF: A6-S030, A6-S107] | Record licence; keep a second detector |
| Attack and benign test sets | **Unacceptable if only in a vendor tool** | They are what lets you swap detectors safely | Git-versioned datasets shared with L9 and C7 |

### C2.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23.* SS1/23 includes model risk mitigants (Principle 5) and ongoing performance monitoring [VF: R-PRA-SS123, A8-S008]. Guardrails are mitigants; their own false-positive and false-negative rates must be monitored like model performance [AJ]. A classifier or judge used as a guardrail is itself a model and belongs in the inventory [AJ].
- *SR 26-2.* SR 26-2 places generative and agentic AI outside its scope and leaves their governance to the firm's own practices [VF: R-US-MRM, A8-S001, A8-S002]. Guardrail standards are therefore set by the firm [AJ].

**Supervisory expectations.** ESMA expects "ex-ante input controls and frequent ex-post output controls" for AI in investment services [VF: R-INTL-AI-ASSETMGMT, A8-S059]. Input guardrails are the ex-ante control and output guardrails plus L9 online evaluation are the ex-post control [AJ]. UK supervision relies on existing frameworks, including SM&CR accountability and Consumer Duty outcomes [VF: R-UK-AI-STATEMENTS, A8-S055]; a named owner for guardrail policy fits that model [Rec].

**EU AI Act.** Article 26 requires deployers of high-risk systems to monitor operation and keep logs for at least six months [VF: R-EUAIA, A8-S011], with Annex III duties from 2 December 2027 [VF: R-EU-OMNIBUS-AI, A8-S011]. Guardrail decisions (what was blocked, by which version) are part of that log [AJ]. Article 50 transparency has applied since 2 August 2026 [VF: R-EUAIA, A8-S011]; guardrails do not substitute for the disclosure duty [AJ].

**Operational resilience and outsourcing.** A managed guardrail service on the request path is an ICT third-party dependency for DORA's register [VF: R-DORA, A8-S021] [AJ]. If it is down, the route fails closed and the business service degrades, so its availability belongs in the impact tolerance analysis [AJ]. The hyperscaler guardrail services sit under providers designated as CTPPs and UK CTPs [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023].

**Residency.** Guardrail inference processes the same client data as the model. Bedrock's Standard tier uses cross-region inference [VF: A6-S072, A6-S101]; Model Armor enforces residency by default but has conflicting statements for London [VF: B-C2-S003, B-C2-S005]. EU-to-US transfers rely on the Data Privacy Framework or SCCs, with an appeal pending [VF: R-DATA-TRANSFERS, A8-S053]. Run guardrails in the same approved region as the model, or in-estate [Rec].

**Auditability.** Each decision needs the guard, its version, score, threshold, outcome and any override with approver [AJ]. Overrides are the most important records: they show that humans, not filters, made the final call [AJ].

**Concentration and ownership.** Guardrail vendors are being absorbed: Check Point bought Lakera [VF: A7-S012, A7-S013], Palo Alto Networks bought Protect AI [VF: A7-S014], and Harvey bought Guardrails AI [VF: A6-S028]. Meta's open components have not been updated since May 2025 [VF: A6-S107]. A two-detector design from different owners is a concentration control as well as a security one [AJ].

**Standards.**
- *OWASP.* The Top 10 for LLM Applications 2026 (August–September 2026) is operative [VF: R-OWASP-LLM, V2-S056]; its full list was not retrieved. For traceability, the 2025 identifiers most relevant to guardrails are LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM05 Improper Output Handling and LLM09 Misinformation [R: A8-S040]. The 2026 edition is reported to rank Excessive Agency third [R: A8-S041], which is an L3 and C4 design issue that guardrails only partly mitigate [AJ]. The Agentic list's ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042] is the threat that indirect-input screening addresses.
- *NIST and ISO.* NIST AI 600-1 lists GenAI risks and suggested actions; ISO/IEC 42001 provides the management-system wrapper [VF: R-NIST-AIRMF, A8-S044; R-ISO-42001, A8-S045].

### C2.12 Worked-example slice (POV 3)

**What the commentary agent needs from C2 [AJ].** The deterministic workflow drafts the monthly Brinson-style attribution commentary (allocation, selection, currency) for a generic multi-asset fund, and calls its guards through the gateway route `attribution-commentary-draft`:
1. **Client identifiers.** Before any text reaches the model, C3 tokenises client names, account numbers and personal identifiers; a C2 PII guard on output blocks any identifier that slips through. Bedrock's PII filter covers UK NI and NHS numbers, IBAN and SWIFT [VF: A6-S072]; firm-specific account formats need the firm's own patterns [AJ].
2. **Prompt injection from retrieved documents.** Every retrieved chunk (prior commentaries, house style, approved market notes) is screened for prompt attacks before it enters the prompt, using a document-attack detector such as Prompt Shields [VF: A6-S054] or Prompt Guard 2 on 512-token chunks [VF: A6-S030]. Third-party market notes get a second detector. A flagged chunk is dropped and logged, not sanitised.
3. **Numeric grounding check.** A deterministic comparator extracts every figure, sign and direction word ("added", "detracted", "overweight") from the draft and checks that each appears in, and agrees with, the attribution engine output for that fund and period. Any figure not in the attribution output, or any mismatch outside the agreed rounding rule, blocks the draft. This is the same check L9 runs offline, run inline here as a guard.
4. **Narrative grounding.** Market-context sentences must be supported by approved retrieved sources; a contextual-grounding check (e.g. Bedrock's [VF: A6-S072]) flags unsupported claims for the reviewer rather than blocking.
5. **Policy topics.** Denied topics: forward-looking return forecasts and personal recommendations; the draft is commentary, not advice.
6. **Fail closed.** If any guard times out, the draft is held and the analyst is told; nothing is released unchecked.
7. **Evidence.** Each guard decision, version and override is written to the trace and the C8 evidence pack.

**What C2 must never do [AJ]:**
- let a model-based judge override a failed deterministic numeric check
- treat "all guardrails passed" as approval; the human approval gate (L3) remains mandatory
- send client data to a guardrail service outside the approved region
- silently sanitise an injected document and continue as if it were trusted
- be used to justify giving the workflow more autonomy or write access than the deterministic design needs

### C2.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| **(absent).** No guardrail control; safety appears only as pre-release evaluation and red-teaming in L9 (Promptfoo, DeepEval) | Managed and open-source guardrails for input, output, grounding and agent tool use [VF: A6-S072, A6-S054, A6-S067, A6-S036] | A control-plane service invoked from the gateway: firm-owned policy and test sets, layered rules → classifiers → judges [Rec] |
| (absent) NeMo Guardrails | 0.24.1, still 0.x Beta; IORails engine; supported microservice [VF: A6-S003, A6-S036, A6-S111] | Tactical: in-estate orchestration, pinned [Rec] |
| (absent) Guardrails AI | Hosted hub retired (6 or 25 August 2026); acquired by Harvey 9 September 2026 [VF: V2-S071, V2-S072, A6-S028] | Experimental: freeze and plan migration [Rec] |
| (absent) Llama Guard / Prompt Guard | Llama Guard 4, Prompt Guard 2, LlamaFirewall 1.0.3; nothing since May 2025 [VF: A6-S030, A6-S006, A6-S107] | Tactical: one detector among several [Rec] |
| (absent) Bedrock Guardrails | Content, prompt-attack, PII, grounding, Automated Reasoning; standalone API [VF: A6-S072, A6-S073] | Strategic, conditional: where AWS is your primary cloud (CP3 Q2) [Rec] |
| (absent) Azure AI Content Safety | Prompt Shields GA; Task Adherence and groundedness preview [VF: A6-S055, A6-S054] | Strategic, conditional: where Azure is your primary cloud (CP3 Q2); GA features only [Rec] |
| (absent) Model Armor | Screening with strict residency by default; Apigee and MCP integration [VF: A6-S067, B-C2-S003] | Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2) [Rec] |

**Relation to the hypotheses (provisional; verdict in synthesis).** C2 bears on two hypotheses rather than having its own [AJ].
- **H1 (gateway as control plane).** Every gateway in C1 invokes guardrails inline, and the managed services are designed to be called from gateways [VF: A6-S015, A6-S017, A6-S020, A6-S024, A6-S073]. That supports drawing C2 as a set of services the gateway calls, not as a separate traffic hop [AJ].
- **H2 (deterministic workflows vs autonomous agents).** The newest guardrail features target agent behaviour (Task Adherence, AlignmentCheck, Foundry tool-call inspection) [VF: A6-S055, A6-S039, A6-S103], and all are preview or unmaintained. That supports the L3 position: decide autonomy first, and use guardrails as the second line, not the reason an agent is allowed to act [AJ].

**Provisional recommendation.** Keep C2 as a distinct control with its own policy, owner and test sets, implemented as detector services invoked from C1 and from L3 checkpoints [AJ]. **Provisional; verdict in synthesis.**
