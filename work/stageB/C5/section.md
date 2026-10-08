## C5. Prompt and configuration management

> **Executive summary.** This control decides which instructions, model, parameters, tools and retrieval settings a GenAI system runs with, who may change them, and how a change is tested, released and rolled back. The original graphic has no box for it [AJ]. What exists in the market today is mostly a capability inside other products. Langfuse and LangSmith each ship a prompt registry inside their L9 platforms [VF: A7-S071, A7-S076]. LaunchDarkly delivers model and prompt configuration through its feature-flag service and renamed the product from AI Configs to AgentControl in 2026, with the API unchanged [VF: A7-S117, V2-S045]. PromptLayer remains an independent registry [VF: A7-S004]. The "prompts as code" pattern keeps prompt files (Prompty, Dotprompt) in the application repository and tests them in CI [VF: A7-S067, A7-S066, A7-S068]. Two ownership changes touch the control: ClickHouse announced its acquisition of Langfuse on 16 January 2026 [VF: A7-S075, V2-S041], and OpenAI announced its acquisition of Promptfoo on 9 March 2026, with no closing date published [VF: A7-S068, V2-S042]. The central argument of this section is that a prompt, an embedding-model version and a retrieval setting are all production configuration [AJ]. A change to any of them can change the output as much as a model upgrade, so each needs versioning, review, an evaluation gate and rollback [AJ]. **Recommendation:** make Git the system of record for every approved prompt and configuration item, approved by pull request with a second reviewer and an L9 eval gate, and released as one pinned manifest. Use a registry (Langfuse or LangSmith, whichever is the L9 platform) only to deliver approved versions at run time and to link each trace to the version that produced it. Use feature-flag rollout (LaunchDarkly AgentControl, PromptLayer release labels) only to choose between versions that have already been approved [Rec].

### C5.1 Responsibility

**The problem this control owns.** It owns the *configuration of record* for every GenAI system: the exact set of settings that, together with the input data, determines the output [AJ]. That set is wider than the prompt [AJ]:
- **Prompts.** System prompt, task templates, few-shot examples, output schemas, house-style instructions.
- **Model configuration.** Provider, model identifier pinned to a dated version, temperature, token limits, reasoning or effort settings.
- **Tool configuration.** The tool allow-list for each workflow step, tool descriptions as the model sees them, and argument schemas (L4).
- **Retrieval configuration.** Embedding model and version, reranker and version, chunking parameters, top-k, filters and fusion weights (L6, L7).
- **Routing configuration.** Primary model, fallback model, region constraints and cost tier, as enforced by the gateway (C1).
- **Policy references.** The guardrail policy version (C2) and the evaluation thresholds that gate release (L9).

**The four jobs.** For that set, the control provides versioning (every item has an immutable version identifier), environment management (development, test and production see different approved versions), change control (review, approval, evaluation gate, release, rollback) and progressive delivery (a new version reaches a segment first, with a kill switch) [AJ].

**Hand-offs.**
- *To L3 orchestration and the gateway (C1):* the release manifest that the workflow and gateway load at start-up or fetch at run time [AJ].
- *To L7:* the pinned embedding and reranker versions. The L7 section already concludes that the embedding model version is production configuration, because changing it forces the whole corpus to be re-embedded, and it asks C5 to hold the pin [AJ].
- *To L9:* the version identifier, which every trace and every evaluation result must carry. Langfuse links prompt versions to traces so that performance can be analysed by version [VF: A7-S071]. L9 consumes C5 versions "because each result must reference the exact version it tested" [AJ].
- *To C8:* change records, approvals and the evidence that the eval gate passed, which form part of model-risk change management [AJ].
- *From C4:* the identities of the author, the approver and the release pipeline, so that segregation of duties can be enforced [AJ].

**What C5 does not own.** Secrets and credentials belong to C7 and must never sit in a prompt or configuration file [AJ]. Access policy belongs to C4. The evaluation logic and thresholds belong to L9; C5 only records which threshold version applied [AJ].

### C5.2 Why it matters

Prompts are code that non-engineers can edit, that compilers cannot check, and whose effect is visible only in outputs [AJ]. When this control is weak, four things break [AJ]:

- **Unreviewed production changes.** Registry vendors sell the ability to change prompts without a deployment. Langfuse states that "prompt updates deploy instantly, without needing to involve engineering" [VF: A7-S071]. That is useful for iteration and dangerous for a regulated output, unless the production label is protected [AJ].
- **No reproducibility.** If the trace records only "the latest prompt", nobody can say which version produced a past output [AJ].
- **Silent configuration drift.** A store auto-embedding with an unpinned default model, a model alias that moves to a new snapshot, or a top-k changed in one environment all change outputs without any prompt change [AJ].
- **No exit.** Prompts held only in a vendor UI must be re-created during a stressed exit, exactly when time is shortest [AJ].

**Illustrative scenario [AJ].** A fund-reporting team keeps its commentary prompts in a hosted registry and fetches the version labelled `production` at run time. During month-end, a product analyst notices that drafts describe currency effects too briefly and edits the prompt in the registry UI, moving the `production` label to the new version. The registry has no protected labels, because the team did not buy that tier. The edit also removes a sentence telling the model to state when an effect is below the materiality threshold. Forty commentaries are generated that evening. Several now describe immaterial currency effects as drivers of performance. Reviewers approve most of them because the wording reads well and the numbers still match the attribution engine. Three weeks later, a portfolio manager challenges one commentary. The trace store records the prompt name but not its version, and the registry's history shows several label moves that week, so the team cannot say with confidence which commentaries used which text. Every commentary from that cycle has to be re-reviewed. A protected production label, a pull request with a second approver, a style regression test in the eval gate and a version ID on every trace would each have stopped or contained it. The scenario is invented; it is not a reported incident.

### C5.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Configuration coverage | Share of production model calls whose prompt, model, tool and retrieval settings all resolve to an approved version ID | 100% for regulated outputs | Version IDs on gateway logs and traces, reconciled to the manifest |
| Unapproved change rate | Production configuration changes without a recorded second approver | Zero | Registry audit log and repository history versus change tickets |
| Eval-gated change share | Production changes that passed the L9 regression suite before release | 100% (emergency changes evaluated within 24 hours) | CI records linked to the release tag |
| Pin compliance | Model and embedding references pinned to a dated version rather than a moving alias | 100% | Static check of the manifest in CI |
| Trace-to-version linkage | Traces carrying prompt, model, retrieval and policy version IDs | ≥99.9% | Trace store query (L9) |
| Rollback time | Time from decision to roll back to the previous approved version serving all traffic | Minutes, not a release cycle | Rollback drill twice a year |
| Change lead time | Time from proposed prompt change to production for a standard change | Days, not weeks; a falling trend | Repository and ticket timestamps |
| Environment drift | Differences between the test manifest and production, other than the change under release | Zero at release | Manifest diff in CI |
| Fallback activation rate | Requests served by a cached or code-side default because the configuration service was unavailable | Near zero; every activation alerted | SDK metrics |
| Emergency change rate | Changes made under the emergency path | Low, and each reviewed after the event | Change records |

### C5.4 How it works

There are two delivery models, and the recommended design combines them [AJ].

**Registry-first (runtime fetch).** The application asks a registry for "the version with label X" and receives the template.
- *Langfuse.* Every version gets a version ID, and labels assign versions to environments (staging, production), tenants or experiments [VF: A7-S072]. SDKs cache prompts client-side, so a fetch adds no network latency on the hot path [VF: A7-S071]. Fetching a label that no version carries returns an error rather than falling back to another version, so a typo fails loudly; the SDKs support a fallback prompt for that case [VF: A7-S072]. Protected prompt labels let project admins and owners stop labels from being moved or deleted; they are an Enterprise feature when self-hosted [VF: A7-S072, A7-S074].
- *LangSmith.* Prompts are stored as commits with diffs. Staging and Production are reserved commit tags assigned through a promotion step, and each environment keeps an ordered rollback history [VF: A7-S076]. "Owners only" mode limits who may tag, promote or delete a prompt, webhooks fire on every commit, and prompts can be synchronised with a GitHub repository [VF: A7-S076].
- *PromptLayer.* Release labels such as `prod` select the served version, and support staged rollouts and segmenting users to specific versions [VF: A7-S088].
- *LaunchDarkly AgentControl.* The application requests a configuration for a user context. The service returns model name, parameters and messages, with a code-side default used if the service is unavailable, and a tracker records tokens, latency and success per configuration [VF: A7-S089].

**Git-first (prompts as code).** Prompt files live in the application repository. A `.prompty` file is markdown with YAML front matter for model, connection and template settings; Dotprompt is an executable template format extending Handlebars [VF: A7-S067, A7-S066]. Changes go through code review and CI, where a CLI such as Promptfoo runs evaluations against the files [VF: A7-S068]. The release tag pins prompt and configuration together with the code [AJ].

**The recommended hybrid [Rec].** Git is the record. CI evaluates every change against the L9 suite, then publishes the approved version to the registry and moves the environment label using a release-pipeline identity, which is the only identity allowed to move protected production labels. The application fetches by label, with a cached copy and a code-side default. Every trace carries the manifest version.

```text
 author (analyst / engineer)
     │  edit prompt, model pin, top-k, embedding version, fallback route
     ▼
 Git repository (system of record) ── pull request ── 2nd approver (risk owner via CODEOWNERS)
     │                                     │
     │                                     ▼
     │                         CI: L9 regression + style + numeric-faithfulness evals
     │                                     │ pass
     ▼                                     ▼
 release manifest vN (prompt vX, model id@date, embed model@ver, reranker@ver, k, policy vY)
     │  signed tag
     ├──► registry: publish vX, move protected label "production" (release identity only)
     ├──► gateway C1: routing + fallback config
     └──► C8 evidence: approval, eval results, diff
                                   │
 runtime:  L3 workflow ── fetch label (SDK cache, code-side default) ──► L1/L2 via C1
                                   │
                                   ▼
                 trace (L9) carries manifest vN + prompt vX  ──► rollback = move label to vN-1
```

**Progressive delivery.** Feature-flag style rollout is useful for prompts in the same way as for code: release a new version to an internal segment, compare evaluations and reviewer edit rates, then widen [AJ]. AgentControl and PromptLayer release labels provide the targeting mechanics [VF: A7-S089, A7-S088]. For a regulated output, the variants being compared must both have passed the approval and eval gate; rollout is a way to limit exposure, not a substitute for approval [Rec].

### C5.5 Enterprise design principles

**Security**
- Never put secrets, client identifiers or credentials into prompt templates or configuration files [Rec]. The OWASP 2025 list names System Prompt Leakage (LLM07) as a risk category, cited for traceability [R: A8-S040]; assume any prompt can be extracted [AJ].
- Treat the production label or branch as a privileged resource. Langfuse's protected labels and LangSmith's owners-only mode exist for this purpose [VF: A7-S072, A7-S076].
- A third-party registry that proxies model calls (PromptLayer's SDK can proxy provider SDK calls for logging [VF: A7-S004]) becomes part of the data path for prompts and outputs. Decide that deliberately, not by default [AJ].

**Resilience**
- The configuration service must not be a single point of failure. Client-side caching (Langfuse [VF: A7-S071]) and code-side defaults (LaunchDarkly [VF: A7-S089]) are the two patterns; use one, and alert when it activates [Rec].
- The default must itself be an approved version. A stale hard-coded default is an unreviewed configuration [AJ].

**Governance**
- **Everything that changes the output is configuration.** Prompt, model version, embedding version, reranker, top-k, tool list and guardrail policy are versioned together in one manifest [AJ].
- **Pin, never float.** Model and embedding references must name a dated version, so that the provider's alias moving does not silently change the system [AJ].
- **Segregation of duties.** The author cannot approve their own production change [Rec].
- **Classify changes.** A wording change that passes the regression suite is a standard change. A model, embedding or tool change is a material change that triggers re-validation. A change of purpose goes to the model-risk owner (C5.11) [Rec].

**Observability and cost**
- The version ID belongs on every trace span and every evaluation result, otherwise the evaluation evidence in L9 cannot be tied to a configuration [AJ].
- Pricing models differ: AgentControl meters every model call and judge run as an "AI run" [VF: A7-S118]; LangSmith prices per seat plus traces [VF: A1-S035]; Langfuse's governance controls sit in its paid Enterprise tier [VF: A7-S074]. Model the cost at production volume [Rec].

**Portability**
- Keep the canonical prompt text in a file format you control, so the registry is a cache of Git, not the other way round [Rec]. LangSmith's GitHub synchronisation is the only registry-to-Git bridge documented in the fact base [VF: A7-S076].

**Patterns [AJ]:** Git as record with CI publishing to a registry; one release manifest per system; protected production label moved only by the pipeline identity; version ID on every trace; dual-run or segment rollout for material changes; rollback drills.

**Anti-patterns [AJ]:** editing production prompts in a vendor UI; floating model aliases; embedding models chosen by a store default; prompts assembled from string literals scattered through the code; feature-flag variants that were never evaluated; a "fallback" prompt nobody has reviewed for a year; separate, unlinked version numbers for prompt, model and retrieval.

### C5.6 Product selection criteria

| Scorecard criterion | What to evaluate in this control [AJ] |
|---|---|
| Technical (15% FS) | Immutable versions and diffs; environment labels; promotion and rollback history; approval or owner controls; segmentation and progressive rollout; coverage beyond prompts (model, parameters, tools, retrieval settings); trace linkage; webhooks for CI |
| Enterprise readiness (15%) | SSO, RBAC with a separate right to move production labels, audit log of label moves with before-and-after versions, SCIM, SLA; whether these are licence-gated |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in product scope; residency of prompt text and any proxied traffic; CMK; FedRAMP or ISO 42001 for 5 |
| Deployment flexibility (15%) | Self-host or customer-cloud deployment so that prompt text and configuration stay in-estate; behaviour when the service is unreachable |
| Ecosystem (5%) | SDK languages, framework integrations, Git synchronisation, webhooks |
| Reliability and maturity (10%) | Time in GA, renames and repositioning, ownership stability |
| Cost / TCO (5%) | Pricing unit (seats, traces, runs); which governance controls are in paid tiers |
| Lock-in / portability (15%) | Export to plain files; Git sync; open file formats; whether runtime fetch can be replaced by a file read |

### C5.7 Product deep dives

The Langfuse and LangSmith platforms are profiled in L9 §9.7 (ownership, certifications, pricing, deployment). The records below cover only their prompt-management capability and refer back to §9.7 for the rest [AJ].

**Langfuse Prompt Management (ClickHouse).**
- *What it is now:* a capability of the Langfuse platform (docs v4; Python SDK 4.17.0, 5 October 2026) that stores, versions and serves prompts. Each version gets a version ID, and labels select which version the SDK fetches [VF: A7-S071, A7-S072, A7-S009]. Prompt versions are linked to traces [VF: A7-S071]. Platform profile: see §9.7.
- *Governance controls:* protected prompt labels, project-level RBAC, audit logs, SCIM and the Org Management API need an Enterprise licence key when self-hosted [VF: A7-S074]. The core, including prompt management, is MIT [VF: A7-S074, A7-S075].
- *Run-time behaviour:* prompts are cached client-side by the SDK [VF: A7-S071]. A missing label is an error, not a silent fallback, and the SDKs support a fallback prompt [VF: A7-S072].
- *Hosting:* Cloud regions in the US, EU (Ireland), Japan and a HIPAA region; self-hosted in any region, including fully offline [VF: A7-S073].
- *Strengths:* prompt versions, traces and evaluation results in one store, which is the shortest path to "which version produced this output" [AJ].
- *Limitations:* the controls that make it safe for regulated prompts are the paid part [VF: A7-S074]. No pull-request approval flow or Git synchronisation is documented in the fact base [NPV].
- *Choose when:* Langfuse is your L9 platform of record [AJ].
- *Avoid when:* you will not license Enterprise, since then any writer can move the production label [AJ].
- *Competitors:* LangSmith prompts, PromptLayer, prompts as code.
- *FS note:* protect the production label and grant the right to move it only to the CI release identity; keep Git as the record [Rec].
- **Tier: Strategic, conditional: only where Langfuse is the L9 platform and the Enterprise licence is bought (FS 3.85 after the CP3 alignment with L9). Flag: Acquired.**

**LangSmith prompt management (LangChain).**
- *What it is now:* prompts stored as a commit history with diffs; reserved Staging and Production environments assigned by promotion; per-environment rollback history; owners-only mode; webhooks on each commit; GitHub synchronisation; a public prompt hub [VF: A7-S076]. Platform profile: see §9.7.
- *Certifications and regions:* SOC 2 Type 2, HIPAA and GDPR [VF: A7-S077], with ISO 27001:2022 stated by LangChain [VF: A1-S126]. SaaS regions are US (GCP and AWS), EU (GCP europe-west4, Netherlands) and APAC. There is no EU legal entity for contracting [VF: A7-S077, A7-S078].
- *Access control:* organisation and workspace roles, custom RBAC roles and per-prompt owners [VF: A7-S080, A7-S076]; Enterprise SSO, ABAC and a support SLA at platform level [VF: A1-S035].
- *Strengths:* the most complete change-control workflow of the registries profiled here, and the only one with a documented bridge to Git [VF: A7-S076] [AJ].
- *Limitations:* prompt storage and promotion run through a proprietary service [VF: A7-S076, A7-S079]. Self-hosting is an Enterprise add-on [VF: A7-S079].
- *Choose when:* LangSmith is already the L9 platform, typically in a LangGraph estate [AJ].
- *Avoid when:* you want the prompt registry separated from the agent-runtime vendor, or need an EU contracting entity [AJ].
- *Competitors:* Langfuse prompts, PromptLayer, prompts as code.
- *FS note:* turn on owners-only mode for production prompts and GitHub sync for every prompt; promotion to Production only by the release pipeline after the eval gate [Rec].
- **Tier: Strategic, conditional: only in a LangSmith estate, with GitHub sync as the exit route. No flag.**

**PromptLayer.**
- *What it is now:* an independent prompt registry and LLM engineering workbench ("Version, test, and monitor every prompt and agent"), with evals, OpenTelemetry tracing for the OpenAI, Anthropic, Google GenAI and Bedrock SDKs, webhooks and a Docs MCP server [VF: A7-S004]. Python SDK 1.5.16 was released on 19 August 2026 [VF: A7-S004, V2-S028].
- *Release labels:* labels such as `prod` select the served version and support staged rollouts and user segmentation [VF: A7-S088].
- *Identity and deployment:* Enterprise Identity covers SSO (SAML/OIDC via WorkOS), SCIM, group-to-role mapping, SSO enforcement, an org-scoped audit log and granular RBAC [VF: A7-S086]. Enterprise customers can deploy into their own AWS account or self-host [VF: A7-S085, A7-S087].
- *Certifications:* PromptLayer states it holds SOC 2 Type 2 and offers the report on request; its DPA commits to annual SOC 2 Type II audits and annual penetration tests [VF: B-C5-S003]. No ISO 27001 was found, and the report itself was not seen [NPV].
- *Strengths:* the best identity controls and rollout mechanics among the standalone registries [VF: A7-S086, A7-S088] [AJ].
- *Limitations:* pricing and EU region are not publicly verified [NPV]. The template API is proprietary [VF: A7-S004].
- *Choose when:* you want a framework-neutral registry with segmentation, run in your own AWS account [AJ].
- *Avoid when:* ISO 27001 is a gate, or the L9 platform already provides a registry [AJ].
- *Competitors:* Langfuse prompts, LangSmith prompts, LaunchDarkly AgentControl.
- *FS note:* obtain the SOC 2 report and subprocessor list first; avoid proxy mode for regulated traffic so the gateway (C1) remains the single egress point [Rec].
- **Tier: Tactical. No flag.**

**LaunchDarkly AgentControl (formerly AI Configs).**
- *What it is now:* runtime configuration for model, parameters and prompt messages, delivered through LaunchDarkly's feature-management service [VF: A7-S089]. AI Configs went GA on 28 May 2025 and online evals on 11 March 2026. The product was renamed AgentControl (launch post 12 May 2026) and repositioned as an operational layer for agents in production, with agents, approvals and custom judges; the API is unchanged [VF: A7-S117, V2-S045].
- *Certifications and deployment:* SOC 2 Type II, ISO 27001, ISO 27701 and FedRAMP Moderate for the Federal instance [VF: A7-S119, V2-S065]. Multi-tenant SaaS, with an EU-hosted offering whose regions and data scope are not detailed, and exceptions for large and US federal customers [VF: A7-S119].
- *Access control:* SAML 2.0 SSO, with roles optionally managed by the identity provider; custom roles are an Enterprise feature [VF: B-C5-S001]. The audit log records changes to any resource, the member or token that made them, and before-and-after versions [VF: B-C5-S002]. The SSO pages are older documentation read through a search extract, so confirm current behaviour [AJ].
- *Pricing:* Developer is free with limited runs. Foundation is US$10 per service connection per month including 5,000 AI runs, then US$5 per 1,000 runs. Enterprise is custom. Each model call or judge run counts (as read 7 October 2026) [VF: A7-S118].
- *Strengths:* the most mature progressive-delivery mechanics in this control, and the strongest certification set [VF: A7-S089, A7-S119] [AJ].
- *Limitations:* SaaS only, with residency scope not detailed [VF: A7-S119]. Configuration retrieval depends on a proprietary service and SDK [VF: A7-S089].
- *Choose when:* LaunchDarkly is already the firm's feature-management standard and you need kill switches and segment rollout for model choices [AJ].
- *Avoid when:* configuration must stay in-estate or in a documented UK or EU region [AJ].
- *Competitors:* PromptLayer, Langfuse prompts, prompts as code.
- *FS note:* hold prompt text in Git and use AgentControl only to select between approved variants; record the variation on each trace [Rec].
- **Tier: Tactical. Flag: Renamed.**

**Prompts as code (pattern: Prompty, Dotprompt, eval configs in CI).**
- *What it is now:* prompts as files in the repository, reviewed and released with the code. Prompty v2 (Microsoft, MIT; Python package 2.0.2, 16 September 2026) has runtimes for Python, TypeScript, Rust and C# [VF: A7-S067, A7-S008]. Dotprompt (Google, Apache-2.0; Python 0.2.0, 5 October 2026) supports JS/TS, Python, Go, Rust and Java [VF: A7-S066, A7-S065]. Promptfoo 0.124.0 (6 October 2026, MIT) runs evaluations against the files in CI [VF: A7-S069, A7-S068].
- *Ownership:* OpenAI announced its acquisition of Promptfoo on 9 March 2026; the closing date has not been published, and Promptfoo states it is part of OpenAI and remains MIT-licensed [VF: A7-S068, V2-S042]. The Promptfoo profile and its independence caveat are in L9 §9.7.
- *Bridges:* LangSmith documents GitHub synchronisation, and a langchain-prompty integration exists [VF: A7-S076].
- *Strengths:* the change record lives in controls the firm already audits, and it survives any vendor exit [AJ].
- *Limitations:* no runtime label switching, segmentation or trace linkage without building them [AJ]. Two competing formats, both young [VF: A7-S067, A7-S065].
- *Choose when:* always, as the record of approved configuration [Rec].
- *Avoid when:* as the only mechanism where business users must iterate daily; add a registry fed by CI [AJ].
- *Competitors:* LangSmith prompts, Langfuse prompts, PromptLayer.
- *FS note:* pull-request approval by a second person, CODEOWNERS naming the risk owner, eval results attached to the PR, signed release tags [Rec]. Pair Promptfoo with a vendor-independent evaluation tool where the system under test uses an OpenAI model (L9 §9.9) [Rec].
- **Tier: Strategic. Flag: Acquired** (Promptfoo, as the example eval CLI).

### C5.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C5-langfuse-prompts | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3.95 | 3.85 | Strategic |
| C5-langsmith-prompts | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 3 | 4.00 | 3.95 | Strategic |
| C5-promptlayer | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3.40 | 3.40 | Tactical |
| C5-launchdarkly-ai-configs | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Tactical |
| C5-prompts-as-code | 3 | 4 | 3 | 5 | 3 | 3 | 4 | 4 | 3.60 | 3.65 | Strategic |

**Scoring notes [AJ]:**
- No NPV cap was triggered. LaunchDarkly's enterprise readiness was evidenced by the writer (SAML SSO, custom roles and an audit log API) [VF: B-C5-S001, B-C5-S002]. PromptLayer's SOC 2 Type 2 is now a dated vendor statement with a DPA commitment [VF: B-C5-S003]; it scores 3, not 4, because no report or ISO 27001 was seen.
- LaunchDarkly security is 4, not 5: SOC 2, ISO 27001 and FedRAMP Moderate are company-level, and AgentControl's coverage is not stated (CP2 Q4).
- The registry scores for Langfuse and LangSmith match their L9 platform scores except on lock-in, where LangSmith's prompt capability scores 3 (L9: 2) because prompt text synchronises to GitHub [VF: A7-S076]. CP3 review: Langfuse enterprise readiness was raised from 3 to 4 (FS 3.70 to 3.85) to match the CP2-reworked L9 Langfuse score; SSO, project RBAC, audit logs, SCIM and the Org Management API are verified, Enterprise-licensed when self-hosted, which is the tier's stated condition [VF: A7-S074, A1-S033].
- Langfuse deployment stays at 4 to match L9, although the C5 record verifies that self-hosted Langfuse can run fully offline [VF: A7-S073]. Both scores should be revisited together at synthesis.
- Prompts as code is scored under rubric rule 2 and is Strategic at 3.65 FS because it is the record, not the runtime. Its enterprise readiness of 4 is the rule 2 maximum; it is higher than the 3 given to OPA, FOCUS or OpenLineage because approval and audit, which are this control's whole function, are delivered by the firm's own source-control platform (inherits host controls). The Acquired flag and the lock-in reduction come from Promptfoo, the example eval CLI, which is replaceable.
- The ownership-change reduction of 1 on lock-in was applied to Langfuse and prompts as code.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| Langfuse prompts | MIT core; protected labels, RBAC, audit in `ee/` [VF: A7-S074] | SaaS, self-host, offline [VF: A7-S073] | SOC 2 Type II, ISO 27001 [VF: A7-S073] | EU region (Ireland) [VF: A7-S073] | ClickHouse, announced 16 Jan 2026 [VF: A7-S075, V2-S041] |
| LangSmith prompts | Proprietary; SDK MIT [VF: A7-S079, A7-S011] | SaaS, BYOC (AWS), self-host, air-gap [VF: A7-S079, A1-S034] | SOC 2 Type 2, ISO 27001:2022, HIPAA [VF: A7-S077, A1-S126] | EU region (Netherlands); no EU contracting entity [VF: A7-S077] | LangChain, independent [VF: A1-S038] |
| PromptLayer | Proprietary; SDK Apache-2.0 [VF: A7-S004] | SaaS, customer AWS, self-host (Enterprise) [VF: A7-S085, A7-S087] | SOC 2 Type 2 (vendor-stated) [VF: B-C5-S003] | Not publicly verified [NPV] | Independent [VF: A7-S004] |
| LaunchDarkly AgentControl | Proprietary SaaS; AI SDK Apache-2.0 [VF: A7-S059] | SaaS, US federal instance [VF: A7-S119] | SOC 2 Type II, ISO 27001, ISO 27701, FedRAMP Moderate (Federal) [VF: A7-S119, V2-S065] | EU-hosted offering; regions not detailed [VF: A7-S119] | LaunchDarkly; renamed from AI Configs 2026 [VF: A7-S117] |
| Prompts as code | Prompty MIT, Dotprompt Apache-2.0, Promptfoo MIT [VF: A7-S008, A7-S065, A7-S068] | Customer repository [VF: A7-S067, A7-S066] | Not applicable; inherits host controls [AJ] | In-estate [AJ] | Promptfoo: OpenAI, announced 9 Mar 2026; closing not published [VF: V2-S042] |

### C5.9 Decision tree

Steps 0 and 3 are not product choices; they are applied whatever is selected [Rec].

```text
STEP 0 [Rec] (not optional): Git is the system of record. One release manifest per system pins
prompt, model id@date, embedding model@version, reranker@version, retrieval params, tool list,
fallback route and guardrail policy. PR with second approver; L9 eval gate in CI.

STEP 1 [Rec]: Do you need run-time delivery (change without redeploying the application)?
  ├─ No  → Prompts as code only (Prompty or Dotprompt files, loaded at build or start-up)
  └─ Yes → Which L9 platform of record did you choose?
           ├─ Langfuse  → Langfuse prompts, Enterprise licence, protected "production" label
           ├─ LangSmith → LangSmith prompts, owners-only mode, GitHub sync on
           └─ Other / none → Must prompt text stay in-estate?
                    ├─ Yes → PromptLayer in your AWS account (after SOC 2 report review),
                    │        or self-hosted Langfuse used only as a registry
                    └─ No  → PromptLayer SaaS or the L9 platform's own registry

STEP 2 [Rec]: Do you need segment rollout, A/B or kill switches for model/prompt variants?
  ├─ LaunchDarkly is the firm's feature-flag standard → AgentControl, selecting only
  │                                                    between approved, pinned variants
  ├─ PromptLayer chosen in step 1                      → release labels / dynamic release labels
  └─ Otherwise                                         → registry labels per segment, or gateway
                                                         (C1) weighted routing between pinned models

STEP 3 [Rec]: Checks before go-live
  Production label movable only by the release identity?  Version ID on every trace?
  Cached or code-side default is an approved version?  Rollback drilled?
  Embedding/reranker versions in the manifest, matching the index's model_version tag (L7)?
```

### C5.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Prompt text and templates | **Unacceptable if held only in a vendor registry; acceptable in Git** | They are the firm's intellectual property and the content of any stressed exit | Canonical files (Prompty or Dotprompt) in the repository; the registry is a cache |
| Template syntax | **Manageable** | Prompty, Dotprompt and registry syntaxes differ [VF: A7-S067, A7-S066] | Keep templates simple (variables, sections); avoid vendor-specific logic in templates |
| Runtime fetch API | **Manageable** | Each registry has its own SDK [VF: A7-S072, A7-S004, A7-S089] | A thin internal `get_config(system, env)` interface with a file-based fallback |
| Rollout and targeting rules | **Manageable** | Targeting logic in a flag service is proprietary [VF: A7-S089] | Keep rules simple and documented in the manifest; record variation on traces |
| Change history and approvals | **Unacceptable if only in a vendor audit log** | It is model-risk evidence with a retention requirement | Repository history plus export of registry audit logs to the C8 archive |
| Model and embedding pins | **Acceptable** | They name provider versions, which is the point [AJ] | Manifest field per system; gateway enforces |

### C5.11 Regulated FS lens (POV 2)

**Model risk: a prompt change can be a model change.**
- *SS1/23.* PRA SS1/23 applies to all models used to inform business decisions, including vendor models, and sets five principles: identification and classification, governance, development and implementation, independent validation, and risk mitigants [VF: R-PRA-SS123, A8-S008, A8-S037]. It applies to banks, building societies and PRA-designated investment firms with internal-model approval for credit, market or counterparty credit risk capital; insurers are not covered [VF: R-PRA-SS123, A8-S008].
- *Applying it here.* For an LLM-based system, the "model" a validator approved is the combination of foundation model, prompt, retrieval configuration and tools [AJ]. Changing the system prompt or the embedding model can change outputs as much as changing the foundation model [AJ]. The firm's change policy should therefore define which configuration changes are material and trigger re-validation, and record each change against the inventory entry [Rec].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly excludes generative and agentic AI. For those tools, the firm's own risk-management practices determine governance and controls [VF: R-US-MRM, A8-S001, A8-S002]. No US regulator therefore defines prompt change control; the firm must set its own standard [AJ]. Writing it to SS1/23 quality is the defensible choice [Rec].
- *Effective challenge.* SR 26-2 retains effective challenge by independent reviewers for in-scope models [VF: R-US-MRM, A8-S001]. The equivalent here is that a second person, ideally the risk owner for the use case, approves production configuration changes [AJ].

**Segregation of duties.** The control must stop one person from writing, approving and releasing a production prompt [Rec]. The products offer different mechanisms: protected labels (Langfuse Enterprise) [VF: A7-S072, A7-S074], owners-only promotion (LangSmith) [VF: A7-S076], custom roles (LaunchDarkly Enterprise) [VF: B-C5-S001] and pull-request approval rules in source control [AJ]. Whichever is used, the release-pipeline identity should be the only one that can move a production label (C4) [Rec].

**EU AI Act.**
- *Deployer logging.* Article 26 requires deployers of high-risk systems to keep logs for at least six months, folded into financial-services documentation for financial institutions; Annex III duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011]. Configuration version IDs are what make those logs interpretable [AJ].
- *Changing purpose through configuration.* Under Article 25, a deployer becomes a provider if it substantially modifies a high-risk system or changes the intended purpose of an AI system so that it becomes high-risk [VF: R-EUAIA, A8-S011]. A system prompt is where intended purpose is most easily changed [AJ]. A prompt change that extends a commentary tool into, for example, HR screening is a regulatory event, not a wording change [AJ]. Purpose-changing edits should be routed to the AI inventory owner (C8) [Rec].
- *Scope for this use case.* Attribution commentary is not an Annex III use; the live duties are AI literacy and transparency [AJ].

**Operational resilience, DORA and outsourcing.**
- *Third-party status.* A SaaS registry or configuration service that delivers prompts to a production system is an ICT third-party service and belongs in the DORA register of information, with Article 30 terms and an exit strategy where it supports a critical or important function [VF: R-DORA, A8-S021] [AJ]. DORA's CTPP list and the UK CTP designations cover hyperscalers, not model or AI-tooling vendors [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023].
- *Run-time dependency.* A configuration service on the request path is a new availability dependency. Cached prompts and code-side defaults turn it into a degraded mode rather than an outage [VF: A7-S071, A7-S089] [AJ].
- *Exit.* SS2/21 expects documented, tested exit plans that cover unexpected termination [VF: R-PRA-SS221, A8-S048]. Portable prompts and configuration, together with the gateway (C1) and the eval suite (L9), are what make a stressed exit from a model vendor feasible [AJ]. PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062].

**Residency and auditability.**
- *Prompt text can be sensitive.* Prompts may embed house views, client segment rules or examples drawn from real commentary [AJ]. FG16/5 expects data location and effective access for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. Prefer an in-estate registry, or a vendor region in the UK or EU, for prompts containing confidential material [Rec].
- *Audit trail.* The trail must answer, for every output: which manifest, which prompt version, who approved it, which evaluation it passed, and when it was promoted [AJ]. Langfuse's version-to-trace linkage [VF: A7-S071], LangSmith's commit and rollback history [VF: A7-S076] and LaunchDarkly's audit log with before-and-after versions [VF: B-C5-S002] each supply part of it. Vendor audit logs should be exported to the firm's archive under the records policy, not left to a vendor plan's retention [Rec].

**Standards.**
- *NIST and ISO.* NIST AI RMF 1.0 and the GenAI Profile (AI 600-1) [VF: R-NIST-AIRMF, A8-S043, A8-S044] and ISO/IEC 42001 [VF: R-ISO-42001, A8-S045] both expect controlled change of AI systems; this control is where that evidence is produced [AJ].
- *OWASP.* Use the OWASP Top 10 for LLM Applications 2026 and the Top 10 for Agentic Applications for 2026 [VF: R-OWASP-LLM, V2-S056; R-OWASP-AGENTIC, A8-S042]. For traceability, the 2025 list's LLM07 System Prompt Leakage is the direct mapping for prompt content [R: A8-S040].
- *ESMA.* ESMA expects ex-ante input controls and frequent ex-post output controls [VF: R-INTL-AI-ASSETMGMT, A8-S059]. An approved, pinned configuration is the ex-ante control [AJ].

### C5.12 Worked-example slice (POV 3)

**What the commentary agent needs from C5 [AJ].** The agent drafts the monthly Brinson-style attribution commentary (allocation, selection, currency, benchmark-relative return) for a generic multi-asset fund. From this control it needs six things:
1. **A versioned commentary prompt set.** System prompt, section templates (allocation, selection, currency, outlook) and the house-style rules, stored as Prompty or Dotprompt files in the commentary repository. The style rules include the materiality-threshold sentence from the C5.2 scenario as a tested requirement.
2. **A release manifest per monthly cycle.** For example, `commentary-release 2026.10`: prompt set v14, drafting model pinned to a dated version with temperature 0, fallback model pinned, embedding model and reranker versions matching the `model_version` tag on the prior-commentary index (L7), top-k 8, read-only tool list (attribution engine, approved market notes), guardrail policy v6 and eval threshold set v3. The values are illustrative.
3. **Approval by pull request.** The author is the reporting analyst or engineer. A second approver from the investment-risk function is mandatory through CODEOWNERS. The pull request shows the diff of prompt text and of every manifest field.
4. **An eval gate, linked to L9.** CI runs the regression suite of past commentaries, the deterministic numeric-faithfulness check and the house-style checks against the new manifest, and attaches the results to the pull request. A failing check blocks the merge. A material change (model, embedding or tool) also requires the validator's sign-off.
5. **Pinned per release, delivered at run time.** On merge, the pipeline tags the release, publishes the prompt set to the registry and moves the protected `production` label. Month-end runs fetch by label, with a cached copy, and fall back to the previous approved release if the registry is unreachable. The release is frozen for the duration of the month-end cycle.
6. **Version on every trace and in the evidence pack.** Each draft's trace carries the manifest and prompt version, and the C8 evidence pack records them with the approver and the eval results. Rollback means moving the label to the previous release and re-running the affected funds.

**What C5 must never allow [AJ]:**
- a production prompt edited in a registry UI outside the pull-request path
- a drafting, fallback or embedding model referenced by a moving alias
- the author approving their own production change
- a feature-flag variant reaching portfolio managers before it has passed the eval gate
- a commentary whose trace cannot name the manifest that produced it
- a vendor auto-fix (LangSmith Engine, Braintrust Loop; see L9 §9.12) changing a production prompt outside change control

### C5.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| (absent) prompt management | A capability inside L9 platforms: Langfuse prompts and LangSmith prompts [VF: A7-S071, A7-S076] | Registry for run-time delivery and trace linkage, fed from Git by CI [Rec] |
| (absent) configuration management | LaunchDarkly AI Configs, renamed AgentControl in 2026 and repositioned towards agent operations [VF: A7-S117, V2-S045] | Tactical: progressive rollout between approved variants where LaunchDarkly is the standard [Rec] |
| (absent) standalone registry | PromptLayer, independent, with Enterprise identity and customer-AWS deployment [VF: A7-S004, A7-S086, A7-S087] | Tactical: framework-neutral registry where no L9 registry exists [Rec] |
| (absent) Git-based patterns | Prompty v2 and Dotprompt as open formats; Promptfoo configs in CI, with OpenAI's acquisition announced 9 March 2026 [VF: A7-S067, A7-S066, V2-S042] | Strategic: Git as the system of record for all production configuration [Rec] |
| Embedding models shown only as a component (L7) | Embedding version is production configuration (L7 §7.13) [AJ] | Embedding and reranker versions pinned in the C5 manifest [Rec] |

**Relevant hypotheses: H6 (embeddings and reranking as one retrieval-optimisation layer) and H8 (evaluation and observability are cross-cutting). Provisional view; verdict in synthesis.**

- **H6.** L7 proposes naming embedding-model versioning as a governed configuration item [AJ]. C5 is where that governance lives: the manifest pins the embedding and reranker versions, and the release process enforces the dual-index migration that L7 describes [AJ]. This supports H6 and adds a dependency: the retrieval-optimisation layer needs C5 to hold its pins [AJ].
- **H8.** Every prompt registry in the market is part of an observability platform (Langfuse, LangSmith) or adds evaluation and tracing of its own (PromptLayer, AgentControl's online evals) [VF: A7-S071, A7-S076, A7-S004, A7-S117]. Vendors treat prompt management and evaluation as one loop, which supports H8 [AJ].
- **Is C5 a control or a product category?** The evidence suggests C5 is a responsibility, not a product box [AJ]. Its products are features of L9 platforms or of feature-flag services, while the record that matters for regulators is the firm's own repository and approval trail [AJ].

**Provisional recommendation.** Keep C5 as a named control in the reference architecture, defined by responsibility (the configuration of record and its change control) rather than by product [AJ]. Draw it next to C8, because its output is change evidence, with run-time delivery shown as a capability of the L9 platform [AJ]. **Provisional; verdict in synthesis.**
