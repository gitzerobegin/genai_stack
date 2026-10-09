## C6. AI FinOps

> **Executive summary.** This control makes the cost of GenAI visible, attributable, bounded and improvable: what each task costs, who pays for it, when spending must stop, and which design choices would make it cheaper without making it worse. The popular stack diagram has no box for it [AJ]. Four things have changed in the market. First, the measurement point has settled on the gateway: every model call passes through it, and gateways now ship budgets, rate limits and spend tracking per key, team and user [VF: A6-S015, A6-S019, A6-S053]. Second, the independent tooling is consolidating. Helicone was acquired by Mintlify on 3 March 2026 and is in maintenance mode [VF: A7-S112, V2-S043], and Portkey was acquired by Palo Alto Networks on 29 May 2026 [VF: A6-S011, V2-S025]. Third, the cloud-cost vendors Vantage and CloudZero have added AI-provider integrations, described mainly in their own blog posts [VF: A7-S113, A7-S114]. Fourth, the open billing standard is catching up but is not there yet. FOCUS 1.4 was ratified on 4 June 2026. FOCUS 1.5, which has no ratification date, adds AI model-identity properties, and a first-class input/output token-type column has been deferred [VF: V2-S046, A7-S116]. The central argument is that the metric that matters is cost per task, not cost per token [AJ]. A cheaper token that needs three retries and a longer human review is not cheaper [AJ]. **Recommendation:** meter and enforce at the gateway (C1), with virtual keys per use case and fund; join gateway records to L9 traces to report cost per completed task; reconcile monthly against provider usage APIs and cloud bills; land everything in a FOCUS-shaped dataset the firm owns; and pair every budget with an enforcement point that fails closed. Treat a FinOps SaaS tool (Vantage, CloudZero) as an optional reporting layer, not the system of record [Rec].

### C6.1 Responsibility

**The problem this control owns.** It owns the economics of the GenAI estate [AJ]:

- **Token economics.** Understanding what drives the bill: input versus output tokens, cached versus fresh input, model tier, batch versus interactive, region premiums, judge-model calls and retries [AJ].
- **Cost attribution.** Every unit of spend tagged to a use case, cost centre, fund or client segment, and to a completed task [AJ].
- **Budgets and enforcement.** Financial limits paired with technical limits that stop or degrade spend when breached [AJ].
- **Showback and chargeback.** Reporting cost to the owners who generate it, and where policy allows, charging it [AJ].
- **Optimisation.** Caching, routing to smaller models, batching, prompt and context trimming, and removing waste such as retries and runaway loops, each validated so that quality does not fall [AJ].
- **Unit economics.** Cost per task, per approved output and per business outcome, compared with the cost of the process it replaces [AJ].

**Hand-offs.**
- *From C1 gateway:* per-request token counts, model, key and metadata; enforcement of budgets and rate limits [AJ].
- *From L9:* the trace that groups model calls, tool calls and evaluation calls into one task, and the outcome of that task (approved, edited, rejected) [AJ]. L9 reports cost per task to C6 [AJ].
- *From L3:* per-run step and token ceilings, which are the agent-level enforcement point [AJ].
- *From L1/L2 providers and clouds:* usage and cost APIs and billing exports, which are the reconciliation source [VF: A7-S070, B-C6-S004, B-C6-S005].
- *To C5:* a cost-driven change (a cheaper model, a shorter prompt) is a configuration change and goes through C5 change control [AJ].
- *To C8 and procurement:* spend by provider for concentration analysis and the outsourcing register [AJ].

**What C6 does not own.** It does not choose models; L1 and the model-risk process do, with cost as one input [AJ]. It does not own the gateway, only the rules the gateway enforces for spend [AJ].

### C6.2 Why it matters

GenAI spend behaves differently from cloud infrastructure spend [AJ]. It scales with usage and with agent behaviour rather than with provisioned capacity; it can grow by orders of magnitude when an agent loops; and prices change quickly [AJ]. The FinOps Foundation's State of FinOps 2026 reports that 98% of respondents now manage AI spend and that FinOps for AI is the top forward-looking priority [VF: A7-S115]. CloudZero states that its customers typically end up at 1.5 to 2 times their initial Amazon Bedrock estimates [VF: A7-S114]; that is a vendor statement and not a decision input [AJ].

When this control is weak, four things break [AJ]:
- **Runaway spend.** An agent in a retry loop consumes tokens until someone notices the invoice.
- **No accountability.** A single provider account and one API key per environment means nobody can say which use case spent what.
- **Wrong optimisation.** Teams chase price per token, switch to a cheaper model, and lose more in retries and review time than they save.
- **Weak exit and concentration evidence.** Without spend by provider, the firm cannot show regulators how concentrated it is, or size an exit.

**Illustrative scenario [AJ].** A research team runs an agent that summarises broker notes overnight. On a Friday a document-store tool starts returning a malformed error. The agent's planner treats each error as a reason to re-read the full document set and try again, and the workflow has no step limit. The team had set a monthly budget on the gateway, but the gateway was deployed without the database its budget feature needs, so the budget was never enforced. The fact base records that LiteLLM's `max_budget` fails open without a database, and that the proxy admin key bypasses budget checks [VF: A6-S015]. The loop runs for 60 hours. Nothing breaks visibly: the provider keeps answering, and the summaries are simply never produced. On Monday, the provider's rate limit for the shared organisation account has been consumed, and the client-facing assistant, which uses the same account, is throttled during market open. The finance team sees the spend two weeks later on the invoice. A per-run step and token ceiling in the workflow, a gateway budget tested to fail closed, an anomaly alert on tool calls per task, and separate keys and limits per use case would each have stopped or contained it. The scenario is invented; it is not a reported incident.

### C6.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Cost per completed task | All model, judge and tool-call cost for one task that reached its outcome, divided by completed tasks | Per use case; falling trend at constant quality | Gateway records joined to L9 traces by run ID |
| Cost per approved output | Cost per task including failed and regenerated attempts, per output a human approved | Per use case; compared with the manual baseline | Trace outcome (approved, edited, rejected) |
| Attribution coverage | Share of AI spend tagged to a use case and cost centre | ≥98% | Gateway key metadata reconciled to invoice |
| Invoice reconciliation variance | Difference between gateway-metered cost and provider or cloud billing | Within ±2% monthly | Provider usage API and billing export versus gateway |
| Budget enforcement coverage | Share of production keys with an enforced budget and rate limit that fails closed | 100% | Gateway configuration audit and a fail-closed test |
| Time to detect anomalous spend | From the start of an anomaly to an alert | Under 1 hour for agent workloads | Alert timestamps versus trace data |
| Retry rate and tool calls per task | Model retries and tool invocations per completed task | Stable band per workflow; spikes alerted | Traces; FinOps Foundation lists both as waste diagnostics [VF: A7-S115] |
| Cache hit rate | Share of input tokens served from provider prompt cache or gateway cache | Rising for stable prompts | Provider usage data (cached vs uncached input) [VF: A7-S070] |
| Model mix | Share of spend on the smallest model that passes the eval gate for each step | Rising | Gateway records by model |
| Forecast accuracy | Forecast versus actual monthly spend per use case | Within ±15% | Budget versus actual |
| Provider concentration | Share of AI spend with the largest provider | Reported quarterly to the third-party risk committee | FOCUS-shaped dataset by provider |

**Target guidance from the FinOps Foundation.** Its tokenomics guidance is to instrument and measure for 30 to 60 days, set budgets at 110% to 120% of that baseline, and alert at 80% and 100% [VF: A7-S115]. It also states: "Pair every financial cap with an engineering enforcement point. A budget without a quota is a number, not a control." [VF: A7-S115].

### C6.4 How it works

The mechanics have five stages: meter, attribute, reconcile, enforce and optimise [AJ].

1. **Meter at the gateway.** Every model call goes through the gateway with a virtual key per use case (and, where needed, per fund or client segment) and request metadata carrying the run ID [AJ]. LiteLLM provides virtual keys, budgets at key, user, team and customer level, TPM and RPM limits, and spend tracking; a database is required for global budgets and spend tracking [VF: A6-S015]. Managed gateways offer equivalents: token limits and quotas per consumer key in Azure API Management [VF: A6-S053], token-limit enforcement and consumption monitoring in Apigee [VF: A6-S024], token budgeting and rate limiting in Kong [VF: A6-S016], and cost-based spend limits and identity-based per-user budgets in Cloudflare AI Gateway [VF: A6-S019].
2. **Attribute to tasks.** The gateway knows tokens per call; L9 knows which calls form a task and what the task's outcome was [AJ]. Joining them on run ID gives cost per task and cost per approved output [AJ].
3. **Reconcile with the provider and the cloud.** Gateway prices are estimates from a price table; invoices are the truth [AJ].
   - *Direct provider APIs.* Anthropic's Usage & Cost Admin API reports usage by API key, workspace, model and service tier, separating uncached input, cached input, cache creation and output tokens; it needs an Admin API key, and workspace keys do not work [VF: A7-S070].
   - *Amazon Bedrock.* Application inference profiles carry cost allocation tags into Cost Explorer and the Cost and Usage Report. Granularity is per usage type per day, not per request, so per-request attribution needs invocation logs or gateway data [VF: B-C6-S004].
   - *Microsoft Foundry.* Azure OpenAI is token-metered by model, deployment type and meter. Project-level cost attribution tags each Foundry project's usage automatically (preview, models sold by Azure only), and cost data appears with a delay of about five hours [VF: B-C6-S005].
   - *Google Vertex AI.* Labels for model cost attribution were not verified in this run [NPV].
4. **Normalise to a FOCUS-shaped dataset.** FOCUS has no AI-specific columns today; tokens are carried by SKU IDs indicating token charges, ConsumedUnit and ConsumedQuantity, and FOCUS 1.2 added columns for virtual currencies such as credits and tokens [VF: A7-S116]. FOCUS 1.5 is scoped to add AI pricing dimensions (cached versus fresh tokens, global versus regional serving) on SkuPriceDetails and four model properties, ModelDeveloper, ModelFamily, ModelId and ModelVersion, with no new columns; a token-type column is deferred and no ratification date has been published [VF: V2-S046]. Map tokens to SKU and ConsumedQuantity now, and add the model properties when 1.5 is ratified [Rec].
5. **Enforce and optimise.** Budgets act at three levels: per run (step and token ceilings in the L3 workflow), per key (gateway budgets and rate limits) and per month (financial budget and alerts) [AJ]. Optimisation proposals go through C5 change control and the L9 eval gate before release [Rec].

![C6 cost metering: from workflow call to cost per task](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/C6-1.png){width=100%}

*Figure: Every model call is metered at the gateway, joined to L9 traces on run_id and reconciled monthly to provider data, so the firm-owned dataset can report cost per task, per approved output and per fund. Editable source: `08_Graphic/diagrams/C6-1.md`.* [AJ]

**Where the money goes in an agent.** For a multi-step agent, the cost of one task is the sum of every planning call, tool-result summarisation call, retry, evaluation-judge call and regeneration after a reviewer rejection [AJ]. That is why the unit has to be the task, and why the trace is the only record that can assemble it [AJ].

### C6.5 Enterprise design principles

**Unit economics first**
- Report cost per completed task and per approved output, not cost per token or per call [Rec]. Include judge calls and regenerations [AJ].
- Compare against the cost of the process being replaced, including human review time. For most drafting use cases, reviewer time is larger than the token bill [AJ].

**Enforcement that fails closed**
- Pair every budget with an enforcement point [VF: A7-S115]. Test it: deploy the budget, exceed it in a test environment, and confirm requests are refused [Rec].
- Know the failure modes of the chosen gateway. In LiteLLM, `max_budget` without a database does not enforce, prompt-injection guardrails are off by default, and the proxy admin key bypasses budget checks [VF: A6-S015]. Restrict the admin key to break-glass use under C4 [Rec].
- Put step and token ceilings in the workflow (L3), because a gateway budget sized for a month will not stop a loop within an hour [AJ].
- Separate experimental from run-rate AI spend; the FinOps Foundation recommends this split [VF: A7-S115].

**Attribution design**
- One virtual key per use case and environment as the minimum; per fund or client segment where chargeback needs it [AJ]. Shared keys destroy attribution [AJ].
- Use cloud-native tagging where models are consumed through a cloud: Bedrock application inference profiles [VF: B-C6-S004] and Foundry project tags [VF: B-C6-S005].

**Optimisation levers (each needs an eval gate) [AJ]**
- *Prompt caching.* Provider cache reads are far cheaper than fresh input. Claude Opus 5.5 lists US$4 per 1M input tokens and US$0.20 per 1M cache-read tokens (as of 7 October 2026) [VF: A5-S011]. Kimi K3 is reported at US$3 and US$0.30; Chinese-vendor API prices are on the verifiers' do-not-rely list, so this is Reported and not a decision input [R: A5-S069]. Stable system prompts and style guides placed first in the context benefit most [AJ].
- *Gateway caching.* LiteLLM offers exact and semantic caching, and Azure API Management offers semantic caching [VF: A6-S015, A6-S053]. A semantic cache returns an answer to a *similar* question, which is unacceptable for outputs that must reflect this month's data [AJ]. Use exact caching only for regulated outputs [Rec].
- *Routing to smaller models.* The price spread inside one vendor's range is large: gpt-6-luna lists US$0.10 input and US$0.50 output per 1M tokens, against US$10 and US$50 for gpt-6-astra (as of 7 October 2026) [VF: A5-S004]. Classification, extraction and judging steps can often use the small model if the eval gate agrees [AJ].
- *Batching.* Anthropic's and OpenAI's batch APIs are 50% off list price [VF: A5-S011, A5-S004]. Azure offers discounted Flex processing for delay-tolerant workloads [VF: B-C6-S005]. Month-end drafting that is reviewed the next morning is a batch workload [AJ].
- *Context discipline.* Long prompts can move into a higher price band: Claude Haiku 5.5 is US$0.10/US$0.50 per 1M for prompts up to 100K tokens and US$0.50/US$2.50 above [VF: A5-S011]. Retrieve less, better (L7) [AJ].
- *Residency has a price.* Anthropic's US-only inference geography costs 1.1 times standard [VF: A5-S011]. Budget for residency choices explicitly [AJ].
- *Prices move.* OpenAI's GPT-6 Sol and Luna were priced 50% below GPT-5.6 promotional pricing [VF: A5-S001]. Re-run the cost model quarterly and keep the price table in the gateway under change control [Rec].

**Security**
- Provider admin keys are powerful credentials. Vantage's Anthropic integration uses an Admin API key, which has revocable read-write access [VF: A7-S113]. Grant third-party cost tools the least privilege the provider allows and rotate keys (C4, C7) [Rec].
- Cost exports should carry metadata, not prompts or outputs [Rec].

**Patterns [AJ]:** gateway metering with virtual keys per use case; run ID joined to traces; FOCUS-shaped firm-owned dataset; monthly reconciliation; three-level enforcement (run, key, month); cost dashboards that show cost per approved output next to quality KPIs; optimisation as a change through C5 and L9.

**Anti-patterns [AJ]:** one API key per environment; budgets that alert but never block; optimising price per token without measuring retries and review time; semantic caching of regulated outputs; a FinOps SaaS tool as the only record; a cheaper model swapped in by the platform team without re-validation.

### C6.6 Product selection criteria

| Scorecard criterion | What to evaluate in this control [AJ] |
|---|---|
| Technical (15% FS) | Per-request metering; budgets and rate limits at key, team, user and customer level; fail-closed behaviour; token-type breakdown (cached, uncached, output); allocation rules; task-level joins; forecasting and anomaly detection |
| Enterprise readiness (15%) | SSO, RBAC scoped to cost data, audit of budget and key changes, SCIM, SLA |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in scope; privilege required on provider admin keys; whether prompts or outputs are ingested |
| Deployment flexibility (15%) | In-estate metering (self-hosted gateway); SaaS region for billing metadata |
| Ecosystem (5%) | Providers and clouds covered; FOCUS export or mapping; API access to the cost data |
| Reliability and maturity (10%) | Ownership stability (Helicone, Portkey), maintenance status, supply-chain history |
| Cost / TCO (5%) | Pricing basis (percentage of spend, tiers, free), operations burden |
| Lock-in / portability (15%) | Whether allocation rules and history can be exported in an open schema |

### C6.7 Product deep dives

**Gateway-native and provider-native cost attribution (pattern).**
- *What it is now:* the gateway issues virtual keys per team, project or user and records token usage and cost per request, enabling budgets and multi-tenant spend reports; provider admin APIs supply organisation-level usage and cost for reconciliation [VF: A7-S010, A7-S070]. Example implementations as of 7 October 2026: LiteLLM 1.104.1 (MIT core), the Portkey SDK 2.3.4 and Anthropic's Usage & Cost Admin API [VF: A7-S010, A7-S081, A7-S070]. The gateway products are profiled in C1.
- *Implementations and controls:* LiteLLM Enterprise adds SSO, RBAC, SCIM and audit logs of key, team, user and model changes [VF: A6-S007]. It announced an updated SOC 2 Type 2 report in September 2026 [VF: A6-S108]. On 24 March 2026, malicious LiteLLM versions 1.82.7 and 1.82.8 were published to PyPI using stolen release credentials and quarantined within about 40 minutes (Snyk reports about three hours) [VF: A6-S008, V2-S027].
- *Cloud equivalents:* Bedrock application inference profiles with cost allocation tags [VF: B-C6-S004]; Foundry project-level cost attribution (preview) [VF: B-C6-S005]; token quotas in Azure API Management and Apigee [VF: A6-S053, A6-S024].
- *Ownership:* Palo Alto Networks completed its acquisition of Portkey on 29 May 2026, and its AI Gateway went GA on 16 July 2026 [VF: A6-S011, V2-S025, A7-S028].
- *Strengths:* the only point where spend can be attributed per request and stopped in real time [AJ].
- *Limitations:* some controls fail open by default [VF: A6-S015]. Cloud billing tags are daily aggregates [VF: B-C6-S004]. Cost per task needs a trace join that no product in the fact base performs end to end [AJ].
- *Choose when:* always, as the metering and enforcement point [Rec].
- *Avoid when:* never as the only record; reconcile with invoices [Rec].
- *Competitors:* Helicone, Vantage, CloudZero.
- *Conflict of interest:* this author is an Anthropic model. Anthropic's Usage & Cost Admin API is cited as one provider-side source; gateway metering and cloud billing (Bedrock, Foundry) are independent of any model vendor and are the recommended primary record [AJ].
- *FS note:* test that budgets fail closed, restrict the admin key, and reconcile monthly for the outsourcing register [Rec].
- **Tier: Strategic. Flag: Acquired** (Portkey, as one implementation).

**Helicone (Mintlify).**
- *What it is now:* an AI gateway and LLM observability platform that tracks cost, latency and quality per request, session and user, with prompt versioning and fallbacks [VF: A7-S046]. It is Apache-2.0 and self-hostable with Docker [VF: A7-S046].
- *Ownership and status:* Mintlify acquired Helicone on 3 March 2026. The product is in maintenance mode: security fixes, bug fixes and new model support continue, and standalone feature development has wound down [VF: A7-S112, V2-S043]. The npm helper package has had no release since 7 November 2025 [VF: A7-S047].
- *Certifications:* the README states "SOC 2 and GDPR compliant" without a SOC 2 type [VF: A7-S046]. Access controls are not publicly verified [NPV].
- *Strengths:* simple base-URL integration; open licence [VF: A7-S046].
- *Limitations:* no roadmap; a competitor says new sign-ups are disabled, which is a single rival source [NPV].
- *Choose when:* only as a bridge while migrating an existing deployment [AJ].
- *Avoid when:* any new deployment [Rec].
- *Competitors:* gateway-native attribution (C1), Langfuse (L9), LiteLLM (C1).
- *FS note:* record the ownership and maintenance change in the third-party file and plan the migration [Rec].
- **Tier: Experimental. Flags: Acquired, Not recommended.**

**Vantage.**
- *What it is now:* a cloud cost management platform with AI-provider integrations: Anthropic API (GA September 2025), Claude Enterprise (July 2026) and OpenAI. Managed AI Tags (`vntg:ai:` model, provider, token type) normalise AI spend across providers at no extra cost. Data is exposed through an API and a hosted MCP server [VF: A7-S113, A7-S090].
- *Schema:* Vantage's internal schema maps to FOCUS; Vantage says it introduced Managed AI Tags because AI pricing diverges from the infrastructure schema [VF: A7-S113].
- *Security and access:* Vantage states SOC 1 Type 2 and SOC 2 Type 2, with reports on request, and documents self-service SAML SSO; its pages conflict on which plans include SAML [VF: B-C6-S001]. RBAC, audit logs and EU hosting are not publicly verified [NPV].
- *Strengths:* the most complete AI-provider normalisation among the cost platforms profiled, and a FOCUS-mapped schema [VF: A7-S113] [AJ].
- *Limitations:* AI features are described in vendor blog posts [VF: A7-S113]. Its Anthropic integration requires an Admin API key with read-write access [VF: A7-S113].
- *Choose when:* Vantage is already the cloud FinOps tool [AJ].
- *Avoid when:* you need per-task attribution or cannot grant read-write admin keys to a third party [AJ].
- *Competitors:* CloudZero, gateway-native attribution, FOCUS.
- *FS note:* a reporting layer for showback, fed by billing and gateway exports; assess key privileges under C4 and C7 [Rec].
- **Tier: Tactical. No flag.**

**CloudZero.**
- *What it is now:* a cloud cost intelligence platform that ingests token-level usage and cost from OpenAI, the Anthropic API, Amazon Bedrock (including Claude Platform on AWS) and Azure OpenAI, and allocates it by customer, feature, team, product and environment through its CostFormation engine. A Kubernetes agent supplies container telemetry [VF: A7-S114, A7-S091].
- *Security and access:* the CloudZero Trust Center lists SOC 1 Type 2, SOC 2 Type 2, GDPR and CCPA, with reports under NDA; no ISO 27001 was found [VF: B-C6-S002]. SAML SSO, just-in-time provisioning and custom roles that scope data access and map to identity-provider groups are documented [VF: B-C6-S003]. Audit logs are not publicly verified [NPV].
- *Strengths:* allocation by customer and feature, which is the shape unit economics needs [VF: A7-S114] [AJ].
- *Limitations:* AI cost claims come from CloudZero's own blog [VF: A7-S114]. Pricing, EU region and FOCUS support are not publicly verified [NPV].
- *Choose when:* CloudZero is already the cost platform, particularly alongside Kubernetes cost allocation [AJ].
- *Avoid when:* you want allocation rules in an open schema [AJ].
- *Competitors:* Vantage, gateway-native attribution, FOCUS.
- *FS note:* keep allocation rules documented outside the tool so chargeback survives an exit [Rec].
- **Tier: Tactical. No flag.**

**FinOps Open Cost and Usage Specification (FOCUS).**
- *What it is now:* an open specification, under CC BY 4.0, defining datasets, columns and requirements so that billing and usage data from different providers is comparable [VF: A7-S048, A7-S096]. FOCUS 1.4 was ratified on 4 June 2026, adding Invoice Detail and Billing Period datasets with zero incompatible changes [VF: V2-S046]. There have been six public releases since v0.5 in June 2023, on a semi-annual cadence [VF: A7-S049]. focus-validator 2.2.1 was released on 5 August 2026 [VF: A7-S050].
- *AI coverage:* there are no AI-specific columns today; tokens are reported through SKU IDs, ConsumedUnit and ConsumedQuantity, and through the virtual-currency columns added in 1.2 [VF: A7-S116]. FOCUS 1.5 has no ratification date. Its confirmed AI scope is pricing dimensions on SkuPriceDetails and four model properties (ModelDeveloper, ModelFamily, ModelId, ModelVersion), with no new columns. A first-class input/output token-type column is deferred, not rejected; the split stays in separate SKUs distinguished by SkuMeter [VF: V2-S046].
- *Wider context:* the FinOps Framework 2026 adds a FinOps for AI technology category, and the FinOps and Linux Foundations announced their intent to form a Tokenomics Foundation for AI billing standards; its formal launch is not confirmed [VF: A7-S115].
- *Strengths:* the only neutral schema available; it keeps the cost dataset independent of any tool [AJ].
- *Limitations:* it is a data model, not a control; AI fields are still in progress [VF: V2-S046] [AJ]. Adoption by AI providers is not publicly verified [NPV].
- *Choose when:* always, as the target schema [Rec].
- *Avoid when:* not applicable; do not wait for 1.5 before starting [Rec].
- *Competitors:* Vantage and CloudZero proprietary schemas; gateway-native data models.
- *FS note:* a FOCUS-shaped dataset makes provider spend comparable for concentration analysis and the outsourcing register [Rec].
- **Tier: Strategic. No flag.**

### C6.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C6-gateway-cost-attribution | 4 | 4 | 3 | 5 | 4 | 3 | 4 | 3 | 3.85 | 3.70 | Strategic |
| C6-helicone | 3 | 2 | 2 | 3 | 3 | 1 | 4 | 3 | 2.60 | 2.50 | Experimental |
| C6-vantage | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 2.95 | 2.90 | Tactical |
| C6-cloudzero | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2.70 | 2.65 | Tactical |
| C6-finops-focus | 3 | 3 | 3 | 5 | 4 | 4 | 5 | 5 | 3.80 | 3.85 | Strategic |

**Scoring notes [AJ]:**
- NPV caps were applied to Helicone on enterprise readiness and security (no access-control evidence; SOC 2 type not stated).
- The writer lifted the Stage A NPV status for Vantage (SOC 2 Type 2; SAML SSO) and CloudZero (SOC 2 Type 2; SAML SSO and scoped roles) [VF: B-C6-S001, B-C6-S002, B-C6-S003]. Each has one or two of SSO, RBAC and audit verified, so enterprise readiness is 3 under CP2 Q2. Neither reaches 4 on security, because no ISO 27001 was found.
- The gateway pattern and FOCUS are scored under rubric rule 2. The gateway pattern's enterprise readiness of 4 relies on implementation evidence (LiteLLM Enterprise; cloud IAM under CP2 Q1); its security stays at 3 because of the March 2026 LiteLLM supply-chain incident and the privilege of provider admin keys.
- Helicone's reliability is 1 because maintenance mode is an anchor-1 condition. That makes it ineligible for Strategic, and it is classed Experimental with a Not recommended flag.
- The ownership-change reduction of 1 on lock-in was applied to Helicone and to the gateway pattern (Portkey).
- The two Strategic entries are a pattern and a specification, not commercial products. No commercial FinOps tool reaches 3.0 FS, mainly because deployment is SaaS-only and residency is unverified [AJ].

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| Gateway-native attribution | LiteLLM MIT core; Portkey SDK MIT; provider APIs proprietary [VF: A7-S010, A7-S081, A7-S070] | Self-hosted gateway, managed cloud gateways, SaaS [VF: A7-S010, A7-S046] | Per implementation, e.g. LiteLLM SOC 2 Type 2 [VF: A6-S108] | In-estate when self-hosted [AJ] | Portkey: Palo Alto Networks, completed 29 May 2026 [VF: V2-S025] |
| Helicone | Apache-2.0 [VF: A7-S046] | SaaS, self-host (Docker) [VF: A7-S046] | "SOC 2" claimed, type not stated [VF: A7-S046] | Not publicly verified [NPV] | Mintlify, 3 Mar 2026; maintenance mode [VF: A7-S112, V2-S043] |
| Vantage | Proprietary SaaS [AJ] | SaaS [VF: A7-S090] | SOC 1 Type 2, SOC 2 Type 2 (vendor-stated) [VF: B-C6-S001] | Not publicly verified [NPV] | Not publicly verified [NPV] |
| CloudZero | Proprietary SaaS [AJ] | SaaS [VF: A7-S091] | SOC 1 Type 2, SOC 2 Type 2 [VF: B-C6-S002] | Not publicly verified [NPV] | Not publicly verified [NPV] |
| FOCUS | CC BY 4.0 [VF: A7-S096] | Specification [AJ] | Not applicable [AJ] | Not applicable [AJ] | FinOps Foundation; Joint Development Foundation copyright [VF: A7-S048, A7-S096] |

### C6.9 Decision tree

Steps 0 and 4 are not product choices; they apply whatever is selected [Rec].

![C6 decision tree: metering, record of cost and chargeback](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/C6-2.png){height=8.8in}

*Figure: Defining the unit and the go-live checks apply whatever is chosen; gateway metering and a firm-owned FOCUS-shaped dataset come before any reporting tool. Editable source: `08_Graphic/diagrams/C6-2.md`.* [AJ]

### C6.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Metering (gateway) | **Manageable** | Cost data models differ per gateway [AJ]; gateways are being acquired [VF: V2-S025, A7-S112] | OpenAI-compatible gateway interface; export per-request records to the firm's dataset |
| Cost dataset schema | **Acceptable on FOCUS; unacceptable if only in a vendor schema** | FOCUS is open and neutral [VF: A7-S096]; vendor schemas are not [AJ] | FOCUS-shaped tables owned by the firm |
| Allocation and chargeback rules | **Unacceptable if they exist only in a proprietary engine** | They are finance policy, and CloudZero's CostFormation is proprietary [VF: A7-S114] [AJ] | Rules documented and versioned in Git (C5), applied in the firm's dataset or replicated in the tool |
| FinOps SaaS reporting | **Manageable** | Replaceable if fed from the firm's dataset [AJ] | Feed tools from exports; never make them the only record |
| Provider usage APIs | **Acceptable** | Each provider's API is its own, but only used for reconciliation [AJ] | One adapter per provider into the dataset |

### C6.11 Regulated FS lens (POV 2)

**Operational resilience: budgets are a resilience control.**
- *Unbounded consumption.* The OWASP 2025 list includes Unbounded Consumption (LLM10), cited for traceability [R: A8-S040]; the operative lists are now the OWASP Top 10 for LLM Applications 2026 and the Top 10 for Agentic Applications for 2026 [VF: R-OWASP-LLM, V2-S056; R-OWASP-AGENTIC, A8-S042]. Runaway agents are both a cost and an availability risk, because they can exhaust shared provider rate limits and starve other services (C6.2) [AJ].
- *DORA.* DORA requires an ICT risk-management framework with ongoing monitoring that extends to services from ICT third parties [VF: R-DORA, A8-S021]. Spend and rate-limit controls on AI providers belong in that framework, with tested enforcement [AJ].
- *Important business services.* Where an AI service supports an important business service, separate keys and limits per service stop a low-priority workload from consuming the capacity a critical one needs [Rec].

**Model risk: cost optimisation is a model change.**
- *SS1/23.* SS1/23 covers vendor models used to inform business decisions and expects development, implementation and use to be controlled [VF: R-PRA-SS123, A8-S008, A8-S037]. Routing a step to a cheaper model, trimming the context or turning on a cache changes the system's behaviour [AJ]. Cost optimisations therefore go through C5 change control and the L9 eval gate, and material ones through re-validation [Rec].
- *SR 26-2.* SR 26-2 excludes generative and agentic AI and leaves their governance to the firm's own practices [VF: R-US-MRM, A8-S001, A8-S002]. The firm's own standard should state that no cost-driven model change bypasses validation [Rec].

**Outsourcing registers and concentration.**
- *Registers.* DORA requires a register of information covering all ICT third-party arrangements; competent authorities report registers to the ESAs annually by 31 March from 2026 (reference date 31 December) [VF: R-DORA, A8-S021]. PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements and an annual register from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. Spend per AI provider, from the FOCUS-shaped dataset, is one of the inputs to materiality and to these registers [AJ].
- *Concentration.* IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. The provider-concentration KPI (C6.3) makes that risk measurable [AJ]. DORA and the UK CTP regime designate hyperscalers but no model vendor [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023], so oversight of direct model-vendor spend falls on the firm [AJ].
- *Exit sizing.* SS2/21 expects documented and tested exit plans [VF: R-PRA-SS221, A8-S048]. Cost per task by model is what lets the firm price the fallback route in its exit plan [AJ].

**Cost allocation to funds is a conduct question.**
- Charging AI costs to funds, rather than to the management company, is a fund-documentation and conduct decision, not a FinOps one [AJ]. Chargeback to funds should be agreed with compliance and fund governance before it is built; showback by fund is safe to build first [Rec].

**Residency, security and auditability.**
- *Cost tools see metadata.* Provider usage data is keyed by API key, workspace and model [VF: A7-S070]; it should not carry prompts or client data, and exports to SaaS cost tools should be checked for that [Rec].
- *Admin credentials.* A third-party cost tool holding a provider admin key with read-write access is a privileged-access risk [VF: A7-S113] [AJ]. Treat it under C4 and C7, and list the tool in the register of information [Rec].
- *Evidence.* The cost record for each regulated output (cost per commentary, model mix, retries) should sit in the same evidence pack as the trace and approval (C8), so that unusual cost can be investigated alongside unusual behaviour [AJ].

**Standards and guidance.**
- The FinOps Framework 2026 adds a FinOps for AI category, and FOCUS is the open data standard [VF: A7-S115, A7-S048].
- NIST AI RMF 1.0 and AI 600-1 [VF: R-NIST-AIRMF, A8-S043, A8-S044] and ISO/IEC 42001 [VF: R-ISO-42001, A8-S045] provide the management-system frame into which AI cost governance fits; neither prescribes cost controls [AJ].
- The EU AI Act sets no cost-specific obligation for deployers [AJ].

### C6.12 Worked-example slice (POV 3)

**What the commentary agent needs from C6 [AJ].** The agent drafts the monthly Brinson-style attribution commentary for a generic multi-asset fund, with a human approval gate. From this control it needs five things:
1. **Cost per commentary and per fund.** Each fund's commentary run has a run ID. The gateway tags every call with `use_case=attribution-commentary`, the fund code and the run ID, and the L9 trace groups the drafting call, the judge calls and any regenerations. The reported unit is cost per approved commentary, per fund per month.
2. **A worked cost model (illustrative arithmetic).** Assume one draft uses about 40,000 input tokens (attribution output, retrieved prior commentary, style guide and prompt) and 3,000 output tokens. At US$2 input and US$10 output per 1M tokens, which is the list price of both Claude Sonnet 5.5 and gpt-6.1-sol as of 7 October 2026 [VF: A5-S011, A5-S004], one draft costs about US$0.08 + US$0.03 = US$0.11. Three judge calls of about 10,000 input and 500 output tokens on a small model at US$0.10/US$0.50 per 1M (Claude Haiku 5.5 or gpt-6-luna list prices) [VF: A5-S011, A5-S004] add under US$0.01. With an average of 2.5 drafts per approved commentary, the token cost is roughly US$0.30 per approved commentary, or about US$12 a month for 40 funds. The token figures and the arithmetic are the author's own [AJ]. The conclusion is that tokens are not the cost driver here; reviewer time is, so the metric that matters is the regeneration and edit rate [AJ].
3. **A monthly budget.** Measure for two month-end cycles, then set the budget at 110% to 120% of the baseline with alerts at 80% and 100%, as the FinOps Foundation recommends [VF: A7-S115]. Experimental work on new prompts uses a separate key and budget [VF: A7-S115] [Rec].
4. **Alerts on anomalous agent loops.** A per-run ceiling in the L3 workflow (for example 6 model calls and 150,000 tokens per fund; illustrative) fails the run and pages the owner. The gateway key has an RPM and TPM limit sized for month-end peaks, and a budget tested to fail closed. Alerts fire on drafts per fund above 3, tool calls per run above the workflow's fixed count, or any call outside the month-end window [AJ].
5. **Optimisation, under change control.** Month-end drafting is reviewed the next morning, so the batch APIs (50% off) fit [VF: A5-S011, A5-S004]. The style guide and system prompt are stable and placed first, so prompt caching applies [AJ]. Moving the judge calls to a smaller model, or switching to batch, is a C5 change and passes the L9 regression suite before release [Rec].

**What C6 must never allow [AJ]:**
- a cost-driven model or prompt change released without the L9 eval gate and C5 approval
- semantic caching of commentary text, which could return last month's narrative
- a budget that alerts but cannot block, on the commentary key
- the commentary sharing a key or rate limit with exploratory work
- chargeback of AI costs to fund expenses without compliance and fund-governance approval
- cost exports that contain client data or draft text

### C6.13 What changed since the popular stack diagram

| Popular stack diagram | End of Q3 2026 | Recommended |
|---|---|---|
| (absent) gateway cost tracking | Gateways ship budgets, limits and spend tracking; Portkey acquired by Palo Alto Networks [VF: A6-S015, A6-S019, V2-S025] | Strategic: gateway as the metering and enforcement point, tested to fail closed [Rec] |
| (absent) provider and cloud billing | Provider usage APIs with token-type breakdown; Bedrock and Foundry cost tags [VF: A7-S070, B-C6-S004, B-C6-S005] | Reconciliation source, monthly [Rec] |
| (absent) Helicone | Acquired by Mintlify on 3 March 2026; maintenance mode [VF: A7-S112, V2-S043] | Experimental, not recommended; migrate [Rec] |
| (absent) Vantage, CloudZero | AI-provider integrations, described in vendor blogs; SOC 2 Type 2 [VF: A7-S113, A7-S114, B-C6-S001, B-C6-S002] | Tactical: reporting layer where already used [Rec] |
| (absent) chargeback patterns | FOCUS 1.4 ratified; 1.5 adds model identity, token-type column deferred; FinOps for AI category [VF: V2-S046, A7-S115] | Strategic: firm-owned FOCUS-shaped dataset; cost per task as the headline metric [Rec] |

**Relevant hypothesis: H1 (the gateway is promoted to a control-plane component). Provisional view; verdict in synthesis.**

The evidence supports H1 from the cost side [AJ]:
- **Enforcement lives in the gateway.** Budgets, rate limits and spend tracking are gateway features in LiteLLM, Cloudflare, Azure API Management, Apigee and Kong [VF: A6-S015, A6-S019, A6-S053, A6-S024, A6-S016].
- **Standalone cost proxies are fading.** Helicone, which combined a gateway with cost tracking, is in maintenance mode [VF: A7-S112], and Portkey has been absorbed into a security platform [VF: V2-S025].
- **The cloud-cost vendors cover billing, not requests.** Vantage and CloudZero ingest provider billing and allocate it, but do not sit on the request path [VF: A7-S113, A7-S114].

The counter-evidence is that cost per task needs the trace (L9), not only the gateway, so C6 depends on two control-plane components rather than one [AJ].

**Provisional recommendation.** Keep C6 as a named control defined by responsibility, with its metering and enforcement drawn inside the C1 gateway and its unit economics drawn on the L9 trace [AJ]. **Provisional; verdict in synthesis.**
