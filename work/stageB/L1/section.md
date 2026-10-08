## 1. Foundation models

> **Conflict-of-interest disclosure.** The author is an Anthropic model, writing about Anthropic and its direct competitors. This is the layer where that conflict is most acute. Anthropic's Claude family was scored on exactly the same rubric as every other family. Where a score for Anthropic was borderline, it was resolved against Anthropic, and each such call is named in its rationale. Anthropic's limitations and controversies are recorded in the same detail as everyone else's. Anthropic's allegation against Chinese laboratories is presented only as an allegation. An independent alternative is named wherever a Claude model appears in a recommendation, and no vendor benchmark (including Anthropic's) is used as a decision input [AJ].

> **Executive summary.** This layer supplies the language models that every agent, retrieval pipeline and evaluation judge above it depends on. Four things have changed since the original graphic. First, every major vendor now sells a *tiered family*, not a model: GPT-6 Astra, Sol and Luna plus GPT-6.1 Sol [VF: A5-S002, A5-S004]; Claude Fable 5.1 above Opus, Sonnet and Haiku 5.5 [VF: A5-S010, A5-S019]; Gemini 3.x with a restricted Gemini 4 Argon [VF: A5-S030, A5-S031]. Version labels in the graphic are already stale or wrong (Gemma "2.9" does not exist; Mistral Medium 3.1 retired on 31 August 2026; "QI4" matches no model) [VF: A5-S034, B-L1-S002] [R: A5-S038]. Second, the most capable tiers are now *gated*: OpenAI rates Astra "Critical" for cybersecurity and requires enterprise admins to enable it, Anthropic restricts Mythos 5.1, and Google released Argon first to cyber defenders [VF: A5-S002, A5-S003, A5-S016, A5-S031]. Third, open weights have become a serious option from both US/EU vendors (gpt-oss, Gemma 4, Mistral, Muse Glimmer) and Chinese-origin vendors (DeepSeek, Qwen, Kimi, GLM), which turns *where the model runs* and *who made it* into separate decisions [VF: A5-S005, A5-S034, A5-S074, A5-S063] [AJ]. Fourth, model lifetimes are short: a Gemini Flash version released on 13 August 2026 retires on 28 January 2027 [VF: B-L1-S003]. **Recommendation:** treat models as a portfolio, not a bet. Run a tiered portfolio (frontier, mid, small and a self-hosted open-weight tier) from at least two unrelated vendors, all routed through the firm's gateway (C1), each qualified and re-qualified on the firm's own evaluation suite (L9), with pinned versions and a tested exit to the second vendor [Rec].

### 1.1 Responsibility

**The problem this layer owns.** L1 turns a prompt and context into generated text, structured output or a tool-call decision, with known capability, cost, latency, data-handling terms and support lifetime [AJ]. In practice an enterprise does not "own" this layer by building models; it owns the *choice, contract, configuration and qualification* of models it buys or self-hosts [AJ]. Five jobs follow:

- **Capability coverage.** Have a qualified model for each task class the firm runs: drafting and reasoning, extraction and classification, coding, multimodal input, and long-context synthesis [AJ].
- **Data-handling fit.** Know, for each model and route, where inference runs, what is retained, whether inputs train the model, and under which jurisdiction's law [AJ].
- **Version and lifecycle control.** Pin exact model versions, know each version's retirement date, and re-qualify before forced migration [AJ].
- **Concentration management.** Keep at least one alternative qualified for every production use so that a vendor outage, suspension, withdrawal or regulatory event does not stop the business service [AJ].
- **Model-risk evidence.** Give the model inventory (C8) an identity for each model (vendor, family, version, route, region) so that validation and monitoring attach to something stable [AJ].

**Hand-offs.** L1 is consumed only through L2 (serving and model access) and the gateway (C1): applications never call a vendor API directly [Rec]. L2 decides *how* a model is reached (vendor API, hyperscaler endpoint, or self-hosted serving engine). C1 decides *which* model a request goes to (routing, fallback, quotas, logging). L9 supplies the evaluation evidence that a model is fit for a task. C8 holds the inventory and approval. C3 and C2 sit in front of the model to mask client data and enforce content policy [AJ].

**What the layer does not own.** It does not own grounding (L6–L8), tool permissions (L4, C4) or numeric correctness. A model is never the source of an authoritative figure in this architecture [AJ].

### 1.2 Why it matters

A badly designed model layer fails in four ways [AJ]:

- **Single-vendor dependency.** A firm that hard-codes one vendor's API cannot respond when that vendor suspends a model, changes its retention terms, or becomes the subject of a government action. These are not hypothetical: Anthropic's top tier, Claude Fable 5, was made unavailable on 12 June 2026 and restored from 1 July 2026 [VF: V2-S004], and a US court upheld a federal supply-chain-risk designation of Anthropic on 25 September 2026 [VF: A5-S084].
- **Silent version drift.** Using an alias ("latest", "stable") lets the vendor change the model underneath a validated process. Google's own documentation recommends pinning versioned model IDs for predictable behaviour [VF: B-L1-S003].
- **Residency by accident.** Two routes to the "same" model can process data in different jurisdictions. Anthropic's first-party API offers only global or US inference geography, while the same models run in EU regions on Google Cloud and Bedrock [VF: A5-S013, V2-S075, A5-S027]. Microsoft Foundry runs DeepSeek V4 in the customer's geography but runs Kimi K3 and GLM-5.x through Fireworks outside the customer's tenant [VF: A5-S087].
- **Model as oracle.** Treating a fluent model as a source of numbers or facts. No model at any tier is fit to produce authoritative figures [AJ].

**Illustrative scenario [AJ].** A UK asset manager standardises its client-reporting assistant on one vendor's top-tier model through that vendor's own API, because the evaluation scores were best. The contract, data-protection assessment and model validation all name that one model. Three weeks before quarter-end the vendor withdraws access to the tier while it fixes a safeguard issue. The gateway has no second route: the fallback model named in the design document was never qualified on the commentary evaluation suite, and its data-processing terms were never assessed. Engineers point the assistant at the vendor's next tier down, which formats percentages differently, and reviewers spend the quarter-end hand-checking every draft. The firm then discovers that its operational-resilience self-assessment listed the assistant as supporting an important business service with "multi-vendor fallback". The fix is not a better model; it is a second vendor qualified in advance, on the same evaluation suite, through the same gateway, with its own contract and residency assessment. The scenario is invented; it is not a reported incident.

### 1.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Qualified-alternative coverage | Share of production use cases with a second model from a *different vendor* that has passed the same evaluation suite within the last quarter | 100% for important business services | C8 inventory joined to L9 results |
| Task-level quality | Per-use-case evaluation score (faithfulness, groundedness, numeric checks, style) for the pinned model | Thresholds per use case; numeric checks 100% | L9 regression suite on every model change |
| Version pinning rate | Share of production calls that name an exact dated or versioned model ID, not an alias | 100% | Gateway logs (C1) |
| Retirement runway | Days between today and the earliest announced retirement of any pinned model | Never below the re-qualification lead time (e.g. 90 days) | Vendor deprecation pages (e.g. B-L1-S001, B-L1-S002, B-L1-S003) reconciled with inventory |
| Residency conformance | Share of calls processed in an approved region for their data class | 100% for client data | Gateway route metadata vs data classification (C3) |
| Cost per task | Loaded token cost per completed task, by tier | Budget per use case; falling trend | Gateway metering (C6) |
| Tier mix | Share of calls served by the small or self-hosted tier where quality allows | Rising until quality thresholds bind | Gateway logs |
| p95 latency and availability | Latency and success rate per model and route | Per use case; failover tested quarterly | Gateway and L9 traces |
| Failover drill success | Share of scheduled drills where traffic moved to the alternative model with quality within threshold | 100% | Drill records (C8) |
| Concentration ratio | Share of production tokens (or important services) served by the largest single vendor | Firm-set ceiling, reported to the risk committee | Gateway metering |

### 1.4 How it works

A foundation model is reached by one of three routes, and the route matters as much as the model [AJ]:

1. **Vendor API.** The vendor runs the model and processes the data under its own terms and regions. Examples: OpenAI's EU endpoint, which stores and processes in region for new projects that use Modified Abuse Monitoring or ZDR [VF: A5-S006, V2-S079]; Mistral's EU endpoint, which commits inference location for a 10% surcharge [VF: A5-S075]; DeepSeek's API, which stores data in the PRC [VF: A5-S062].
2. **Hyperscaler-hosted.** The model runs inside AWS, Azure or Google Cloud under the cloud's IAM, logging and regional controls. Claude is on Bedrock, Google Cloud and Microsoft Foundry [VF: A5-S010]; GPT-6 is on Bedrock and Foundry [VF: A5-S008, A5-S009]; Gemini is on Google Cloud only [VF: A5-S027]. Some hyperscaler listings are pass-throughs: Foundry's Kimi K3 and GLM-5.x run on Fireworks outside the customer's tenant [VF: A5-S087], and Bedrock offers Kimi K3 only through cross-Region profiles [VF: A5-S086].
3. **Self-hosted open weights.** The firm runs the weights on its own GPUs through an L2 serving engine. Licences differ: Apache 2.0 (Gemma 4, gpt-oss, Mistral Large 3, Qwen3.8-27B), MIT (DeepSeek V4, GLM-5.3-Flash), modified or custom licences with revenue thresholds (Mistral Medium 3.5, Kimi K3, Qwen3.8 flagship, GLM-5.3, Llama 4) [VF: A5-S034, A5-S005, A5-S074, A5-S066, A5-S063, A5-S071, A5-S069, A5-S077] [R: V2-S014].

```text
 Application / agent (L3)
          │  prompt + approved context (no raw client identifiers: C3)
          ▼
 Gateway C1 ── policy: data class → allowed routes & regions; task → model tier
          │            pinned model IDs; fallback order; quotas; logging (L9, C6)
          ├────────────────────┬──────────────────────────┬─────────────────────────┐
          ▼                    ▼                          ▼                         ▼
   Frontier tier         Mid tier (default)         Small tier               Self-hosted open-weight
   (gated, rare use)     vendor A in-region         classification,          tier (L2 serving)
   e.g. Astra / Fable    e.g. GPT-6.1 Sol,          routing, extraction      e.g. Gemma 4, Mistral
                         Sonnet 5.5, Gemini 3.8     e.g. Luna, Haiku 5.5,    Medium 3.5, gpt-oss
                         Flash, Mistral Medium 3.5  Flash-Lite, Ministral    (sensitive data stays
                              │                                               in estate)
                              └─► fallback: vendor B, same tier, same region,
                                  qualified on the same L9 suite
          ▼
 Response → guardrails (C2) → evaluation (L9) → inventory & evidence (C8)
```

**The portfolio principle.** Tiers trade capability against cost and latency within a family: OpenAI lists Luna for "high-volume summarisation, extraction, classification and routing" [VF: A5-S002], and list prices span two orders of magnitude, from US$0.10 to US$10 per 1M input tokens within both the OpenAI and Anthropic families [VF: A5-S004, A5-S011]. Vendors diversify across families. Self-hosting changes the data question entirely, because no data leaves the estate [AJ]. A portfolio therefore has two axes: *tier* (frontier, mid, small, open-weight) and *vendor* (at least two unrelated vendors at the mid tier) [AJ].

**Model economics (list prices per 1M input / output tokens, as of 7–8 October 2026).** These show the order of magnitude; they are not decision inputs on their own, and Chinese-vendor API prices rest on aggregators, so they are Reported only [AJ].

| Tier | Examples |
|---|---|
| Frontier | GPT-6 Astra US$10 / US$50 [VF: A5-S004, V2-S008]; Claude Fable 5.1 US$10 / US$50 [VF: A5-S011, V2-S002]; Claude Opus 5.5 US$4 / US$20 [VF: A5-S011]; Gemini 3.1 Pro (preview) US$2 / US$12 [VF: A5-S032] |
| Mid | GPT-6.1 Sol US$2 / US$10 [VF: A5-S004]; Claude Sonnet 5.5 US$2 / US$10 [VF: A5-S011]; Gemini 3.8 Flash US$0.75 / US$3.75 introductory, US$1.50 / US$7.50 from 1 January 2027 [VF: A5-S027, V2-S010]; Mistral Medium 3.5 US$1.50 / US$7.50 [VF: A5-S074]; Grok 4.7 US$2 / US$6 [VF: A5-S079] |
| Small | GPT-6 Luna US$0.10 / US$0.50 [VF: A5-S004]; Claude Haiku 5.5 US$0.10 / US$0.50 up to 100K-token prompts [VF: A5-S011]; Gemini 3.5 Flash-Lite US$0.30 / US$2.50 [VF: A5-S027] |
| Chinese-origin APIs (Reported) | DeepSeek V4-Pro about US$1.32 / US$3.96; GLM-5.3 about US$1.40 / US$4.40; Kimi K3 about US$3 / US$15; Qwen3.8-max about US$2 / US$6 [R: A5-S038] |
| Open weights | Licence free; cost is GPUs and operations. gpt-oss-120b fits one H100 [VF: A5-S005]; Gemma 4 26B/31B need a single data-centre GPU class [R: A5-S035]; DeepSeek V4-Pro (1.6T parameters) needs a large multi-GPU cluster [R: A5-S044] |

Modifiers move the real cost more than the headline. Batch processing halves OpenAI and Anthropic prices [VF: A5-S004, A5-S011]. Regional processing costs extra: 10% on Bedrock regional endpoints for Claude [VF: A5-S011], 10% on non-global Google Cloud endpoints from 1 July 2026 [VF: A5-S027], 10% on Mistral's EU endpoint [VF: A5-S075], and 1.1x for US-only inference on Anthropic's and xAI's APIs [VF: A5-S011, A5-S079]. For a regulated firm the residency premium is the real price [AJ].

### 1.5 Enterprise design principles

**Security**

- Send no raw client identifiers to any external model; mask or tokenise at C3 before the gateway [Rec].
- Prefer routes with contractual no-training and zero or short retention. OpenAI does not train on API data by default and retains up to 30 days unless ZDR is approved [VF: A5-S006]. Anthropic does not train on commercial data without permission; ZDR is available on request, but Fable 5.1 is a "Covered Model" needing 30-day retention unless expressly authorised, which conflicts with its launch post [VF: A5-S023, A5-S016]. xAI deletes within one hour under team-level ZDR [VF: A5-S080]. Mistral offers ZDR only for pay-as-you-go stateless calls at its discretion [VF: A5-S075]. Meta's contributor tier trains on prompts and completions [VF: V2-S019]. Block any training-on-data tier at the gateway [Rec].
- Treat open-weight files as executable supply-chain artefacts: scan, sign or hash-pin, and serve from an internal registry (C7) [Rec].
- Gated cyber-capable tiers (Astra, Mythos, Argon) are off by default for a reason. Keep them disabled unless a named use case needs them [AJ].

**Scalability and resilience**

- Every production use case gets a primary and a fallback from a different vendor, on the same tier, in an approved region, qualified on the same evaluation suite [Rec].
- Run failover drills; an untested fallback is not a fallback [AJ].
- Spread across routes as well as vendors: the hyperscaler is a concentration point too, and DORA and the UK CTP regime designate the hyperscalers, not the model vendors [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023] [AJ].

**Governance and lifecycle**

- Pin exact model IDs; never use "latest" aliases in production [Rec]. Google states that pinning versioned IDs gives more predictable behaviour [VF: B-L1-S003].
- Track retirement dates. Notice periods differ: OpenAI gives at least 6 months for GA models, at least 3 months for specialised variants and as little as about 2 weeks for previews [VF: B-L1-S001]; Mistral's Labs models may go with 1 month's notice [VF: B-L1-S002]; Anthropic publishes "not sooner than" retirement commitments of September/October 2027 for current models [VF: A5-S010]; Google publishes per-model retirement dates, with recent Flash versions living about five to six months [VF: B-L1-S003].
- Never put a preview model (Gemini 3.1 Pro is still preview [VF: A5-S032]) or a days-old preview (Mistral Large 4 [VF: A5-S076]) behind an important business service [Rec].

**Observability and cost**

- Log model ID, route, region, token counts and latency for every call at the gateway, and attach evaluation results in L9 [Rec].
- Route by tier: classification and extraction to the small or self-hosted tier; drafting to the mid tier; the frontier tier only where evaluation proves the mid tier insufficient [Rec].

**Portability**

- Keep prompts, tool schemas and output schemas vendor-neutral and in Git (C5); most vendors expose OpenAI-compatible interfaces [VF: A5-S010, A5-S077] [R: A5-S038], so an OpenAI-shaped internal contract behind the gateway is the practical abstraction [AJ].
- Keep at least one open-weight model qualified per critical use case, even if it is lower quality, as the stressed-exit route [Rec].

**Patterns [AJ]:** two-vendor mid tier with gateway failover; small model for classification and routing; self-hosted open-weight tier for sensitive or air-gapped tasks; pinned versions with a retirement calendar; model-agnostic prompt templates; evaluation-gated promotion of any new version.

**Anti-patterns [AJ]:** a single vendor's API called directly from application code; aliases in production; choosing on vendor benchmark tables; frontier tier as the default; using a vendor's own API because it is cheapest without checking jurisdiction; treating a hyperscaler listing as proof of in-region, in-tenant processing; letting a vendor-owned test tool be the only independent check of that vendor's model (see L9 on Promptfoo [VF: A1-S024]).

### 1.6 Product selection criteria

The units of selection are *vendor families*, because individual versions are replaced within months. Scores follow the rubric in `08_scoring_rubric.md` and the CP2/CP3 rules [AJ].

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Breadth and depth of the current lineup against plan §5 (frontier vs open-weight; general vs specialist; reasoning, multimodal, coding, small models), on primary evidence of what the models do and independent government evaluations (CAISI). **Vendor benchmark numbers are not used.** |
| Enterprise readiness (15%) | Admin and identity controls on the vendor API; whether the current generation is offered in-tenant on a hyperscaler (CP2 Q1 presumption); support and SLA terms |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 scoped to the API; ISO 42001, CMK, ZDR, no-training terms; first-party and hyperscaler residency options; regulatory findings against the vendor |
| Deployment flexibility (15%) | Vendor API, hyperscaler (in-tenant vs pass-through), self-hosted and air-gapped open weights |
| Ecosystem (5%) | Hyperscaler distribution, OpenAI-compatible interfaces, open-serving engine support |
| Reliability and maturity (10%) | GA vs preview, retirement policy and notice, availability events, ownership stability |
| Cost / TCO (5%) | Transparent per-tier pricing, batch and caching, residency premiums, self-hosting burden. Chinese-vendor API prices are aggregator-level and not decision inputs (V2 §4 item 3) |
| Lock-in / portability / concentration (15%) | Open weights and licence terms; number of independent hosting routes; interface standardisation; ownership change (rule 3); licence thresholds (rule 4) |

**How the family scores were built [AJ].**
- *Enterprise readiness.* The hyperscaler presumption (rule 6) applies where the family's *current generation* is offered on AWS, Azure or Google Cloud, operated by the cloud. Where it is not (Qwen3.8), the vendor's own evidence applies.
- *Security.* Scored on the model vendor's own certifications and terms, not the hyperscaler's. A family whose primary evidence is "not publicly verified" is capped at 2 (rule 1); a vendor with an unremediated serious regulatory finding against its hosted service scores 1.
- *Chinese-origin families.* Each rationale states the hosted API and the self-hosted weights separately. The family score reflects the vendor as counterparty; the tier condition says which route is acceptable.

### 1.7 Product deep dives

Families are grouped as: US frontier vendors (OpenAI, Anthropic, Google Gemini, SpaceXAI Grok); open-weight-led vendors from the US and EU (Mistral, Gemma, Meta); and Chinese-origin vendors (DeepSeek, Qwen, Kimi, GLM) [AJ].

**OpenAI GPT family (OpenAI).**
- *What it is now:* GPT-6 is a tiered family. GPT-6 Astra was introduced on 3 September 2026 to a limited set of organisations, with API access from 4 September and Bedrock GA on 8 September; it is the first OpenAI model rated "Critical" for cybersecurity and must be enabled by enterprise admins [VF: A5-S083, A5-S002, A5-S003, A5-S008]. GPT-6 Sol and Luna followed on 22 September and GPT-6.1 Sol on 29 September 2026 [VF: A5-S002, A5-S004, V2-S024]. GPT-5.6 Sol, Terra and Luna (9 July 2026) are still offered [VF: A5-S001]. All GPT-6 tiers are reasoning models with text and image input [VF: A5-S009, A5-S003]. Open weights: gpt-oss-120b and 20b under Apache 2.0 (5 August 2025); no newer open-weight release was found [VF: A5-S005].
- *Certifications and deployment:* SOC 2 Type 2 for the API Platform (report period to 30 June 2026); ISO/IEC 27001, 27017, 27018 and 27701 covering the API; ISO/IEC 42001 with scope wording that does not name the API Platform [VF: A5-S007, V2-S062]. Available through the first-party API, AWS Bedrock and Microsoft Foundry (28 Global regions, US and EU Data Zones); on Google Cloud only gpt-oss is offered [VF: A5-S008, A5-S009, A5-S027].
- *Residency:* EU endpoint stores and processes in region for new projects with Modified Abuse Monitoring or ZDR; the UK endpoint stores data in the UK but does not process there; Bedrock Astra runs in-region only in us-east-1 and us-west-2 [VF: A5-S006, V2-S079, A5-S008].
- *Lifecycle:* GA models get at least 6 months' deprecation notice and previews as little as about 2 weeks; GPT-5.1 and GPT-5.4-Nano are removed on 1 April 2027 with GPT-6 Sol and Luna named as replacements [VF: B-L1-S001].
- *Strengths:* the most complete tier ladder in the layer, a de facto standard API shape, two hyperscaler routes and a first-party EU processing option [AJ].
- *Limitations:* frontier tiers are closed and API-only; Astra's status conflicts (OpenAI said "not yet generally available"; AWS lists it GA) [VF: A5-S002, A5-S008]. No UK in-country processing [VF: A5-S006]. First-party SSO, SCIM, RBAC and CMK were not verified [NPV]. OpenAI announced the acquisition of Promptfoo on 9 March 2026, so a widely used red-team tool is now vendor-owned [VF: V2-S042].
- *Choose when:* Azure or AWS is primary and you want a mid-tier default or a fallback with a first-party EU option [AJ].
- *Avoid when:* Google Cloud is the only permitted cloud, or UK in-country processing is mandatory [AJ].
- *Competitors:* Anthropic Claude, Google Gemini, Mistral.
- *FS note:* consume GPT-6.1 Sol through a Foundry EU Data Zone or the EU endpoint with ZDR; pin dated snapshots; keep a non-OpenAI fallback and a non-OpenAI red-team tool [Rec].
- **Tier: Strategic. Flag: none.** FS 4.05.

**Anthropic Claude family (Anthropic, PBC).**
- *Conflict of interest:* the author is an Anthropic model. Every borderline score below was resolved against Anthropic, and those calls are named [AJ].
- *What it is now:* Claude Fable 5.1 (1 September 2026) is the top GA model "for demanding reasoning and long-horizon agentic work"; Claude Mythos 5.1 is the same model with more permissive cyber and biology safeguards, for trusted-access programmes only [VF: A5-S016, V2-S066]. Claude Opus 5.5 (22 September 2026) is the first 5.5 model and Anthropic's recommended starting point; Sonnet 5.5 (28 September) and Haiku 5.5 (7 October 2026) complete the family [VF: A5-S019, A5-S012, A5-S020, A5-S010]. All four GA models have adaptive thinking, text and image input, text output, a 1M-token context and 128K output. There are no open weights and no audio or image output [VF: A5-S010].
- *Certifications and deployment:* SOC 2 Type I and II, ISO 27001:2022, ISO/IEC 42001:2023 and CSA STAR Level 2, with scope covering the API, Claude Enterprise and Team, and Claude in Bedrock and Google Cloud; Claude in Microsoft Foundry is in scope when hosted on Anthropic, while the Azure-hosted Foundry deployment is listed "In-Process Q4 2026" [VF: A5-S021, V2-S063]. Admin controls documented: Workspaces, Admin API, user management, Workload Identity Federation, a Compliance API and Activity Feed with 6-year retention, and CMEK in the admin console [VF: A5-S013, A5-S018]. Routes: first-party API, Claude Platform on AWS, Bedrock, Google Cloud and Microsoft Foundry [VF: A5-S010].
- *Residency:* first-party inference geography is "global" or "us" only, and workspace (storage) geography is "us" only. There is no first-party EU or UK inference option. EU processing is available through Google Cloud EU multi-region and regional endpoints and Bedrock regional endpoints, at a 10% premium [VF: A5-S013, V2-S075, A5-S011, A5-S027].
- *Availability event:* Claude Fable 5 launched on 9 June 2026; access was made unavailable on 12 June 2026 and restored from 1 July 2026 [VF: V2-S004].
- *Legal and public-sector events:*
  - The US Department of Defense designated Anthropic a "supply chain risk", relying on two designations litigated separately. On 27 August 2026 the N.D. California (Judge Rita F. Lin, No. 3:26-cv-01996) granted Anthropic summary judgment that the 10 U.S.C. s.3252 designation was unlawful [VF: V2-S068]. On 25 September 2026 the D.C. Circuit (No. 26-1049) upheld the other designation, under FASCSA, by 2–1, with its effect stayed pending a rehearing petition [VF: A5-S084] [R: V2-S005]. Sources disagree on the practical scope of that ruling, and this section makes no claim about it [AJ].
  - Bartz v. Anthropic: the US$1.5bn class settlement over pirated books received final approval on 20 July 2026 (Judge Araceli Martinez-Olguin); Judge Alsup had earlier held that training itself was fair use but that building a library from pirated books was not [VF: A5-S085] [R: V2-S007].
  - Anthropic has barred sales to entities controlled from unsupported regions such as China since 4 September 2025 [VF: A5-S045]. Anthropic alleges that DeepSeek, Moonshot and MiniMax distilled Claude through about 24,000 fraudulent accounts (23 February 2026); this is an unadjudicated allegation by a competitor [VF: A5-S046, V2-S022].
  - Anthropic confidentially submitted a draft S-1 on 1 June 2026 [VF: A5-S024].
- *Lifecycle:* retirement commitments of "not sooner than" September/October 2027 are published for current models [VF: A5-S010].
- *Strengths:* the only frontier family available in-tenant on all three hyperscalers; product-scoped SOC 2, ISO 27001 and ISO 42001; strong admin and audit APIs; long published retirement windows [VF: A5-S010, A5-S021, A5-S013] [AJ].
- *Limitations:* no first-party EU/UK processing; the top tier's ZDR position conflicts between Anthropic pages; the June 2026 suspension of the top tier; no open weights; enterprise support tiers and SLA not publicly verified [VF: V2-S075, A5-S023, V2-S004, A5-S010] [NPV].
- *Choose when:* you need a second frontier vendor in-tenant on your primary cloud, especially on Google Cloud where GPT-6 is not offered [AJ].
- *Avoid when:* EU or UK processing must be contracted directly with the model vendor; you have US defence-contract exposure that legal has not assessed; you need a self-hostable model from the same vendor [AJ].
- *Competitors:* OpenAI GPT, Google Gemini, Mistral. Independent alternatives wherever Claude is recommended: GPT-6.1 Sol (OpenAI), Gemini 3.8 Flash (Google), Mistral Medium 3.5 [Rec].
- *FS note:* consume only through a hyperscaler EU region; do not route client data to the first-party API; keep a non-Anthropic fallback qualified [Rec].
- **Tier: Tactical. Flag: none.** FS 3.55, just below the normal Strategic line, after borderline calls on technical, ecosystem and cost were resolved against Anthropic under the conflict rule. Had those three been resolved neutrally the FS total would have been about 3.8. Security was also held at 4 although the certificates meet the rule-8 threshold for 5 (see the scoring notes). The reviewer should decide whether Anthropic belongs with OpenAI as a Strategic frontier vendor; this author should not [AJ]. The CP4 calibration review left every Anthropic score unchanged and put the tier, with the neutral-rubric values, to the reader (CP4 review C, Q1) [AJ].

**Google Gemini family (Google).**
- *What it is now:* Gemini 3.x is the production lineup: 3.1 Pro (preview since 19 February 2026 and still labelled preview), 3.8 Flash (GA 2 September 2026), 3.5 Flash-Lite (21 July 2026), 3.8 Live and Live Extended Thinking (GA 15 September 2026), 3.8 Flash TTS and image models, and Flash Cyber variants [VF: A5-S030, A5-S032, A5-S027]. Gemini 4 Argon was announced on 30 September 2026 and is rolling out first to trusted cyber defenders through the Fairwind programme, with paid API access "next" and no date; it was not on Google Cloud at launch [VF: A5-S031, V2-S009]. Gemini 3.5 Pro was never released and is reported cancelled [R: A5-S036]. Vertex AI was renamed Gemini Enterprise Agent Platform in April 2026 [VF: V2-S037].
- *Certifications and deployment:* Google Cloud generative AI services are in scope for ISO/IEC 42001 and SOC 2 [VF: A5-S028, A5-S037]. Google Cloud only (no AWS or Azure listing found) plus the Gemini Developer API; no self-hosting [VF: A5-S027, A5-S032].
- *Residency:* data-at-rest residency for generative AI in the UK and several EU countries (a 2023 commitment); on Google Cloud ZDR is achievable by disabling logging, session resumption and caching and avoiding Search grounding; the paid Gemini API (not Google Cloud) may cache content in any country [VF: A5-S029, A5-S033].
- *Lifecycle:* Gemini 3.7 Flash, released 13 August 2026, retires on 28 January 2027; 3.6 Flash retires on 19 November 2026; 3.5 Flash runs to 19 May 2027 or later [VF: B-L1-S003].
- *Strengths:* the widest native modality range (text, image, video and audio input; live audio; TTS) and a fast Flash cadence [VF: A5-S030] [AJ].
- *Limitations:* no GA Pro-class model; short Flash support windows; one cloud; 3.8 Flash's introductory price doubles on 1 January 2027 [VF: A5-S032, B-L1-S003, A5-S027, V2-S010]. Argon pricing is not published [NPV].
- *Choose when:* Google Cloud is primary, or the use case needs native audio or video [AJ].
- *Avoid when:* you need a GA Pro-class model with a long support window, or your estate is AWS or Azure [AJ].
- *Competitors:* OpenAI GPT, Anthropic Claude, Mistral.
- *FS note:* use regional endpoints with logging and caching disabled; plan re-validation around the five-to-six-month Flash lifetimes; do not use the consumer Gemini API for client data [Rec].
- **Tier: Strategic, conditional: where Google Cloud is your primary cloud (CP3 rule 10, the lead model service on that cloud); deployment and lock-in score 2, allowed under rule 11 as an existing platform commitment. Flag: none.** FS 3.35. Outside a Google Cloud estate it is Tactical [AJ].

**Grok family (SpaceXAI, formerly xAI).**
- *What it is now:* Grok 4.7 launched on 21 September 2026 with a 500K context and configurable reasoning effort; earlier flagships (4.6, 4.5), 4.20 and 4.3 reasoning, non-reasoning and multi-agent models, Grok 4.1 Fast, grok-code-fast-1 and image and video generation remain available [VF: A5-S079, V2-S012, A5-S027] [R: A5-S038].
- *Ownership:* SpaceX acquired xAI in an all-stock deal announced and closed on 2 February 2026; the unit now operates as SpaceXAI (formerly xAI). A further rename was announced on 4 October 2026 and had not taken effect [VF: V2-S011] [R: A5-S081].
- *Certifications and deployment:* SOC 2 Type II with HIPAA-eligible deployments under a BAA; Trust Center under NDA; no ISO certification found [VF: A5-S080]. On Google Cloud (including Grok 4.7), Bedrock (including US GovCloud) and Microsoft Foundry [VF: A5-S027] [R: A5-S038].
- *Data terms:* no training on API data without permission; 30-day default retention; team-level ZDR; enterprise terms let the vendor create and own de-identified derived data except under ZDR; a US regional endpoint exists, but the default endpoint gives no region guarantee [VF: A5-S080].
- *Regulatory:* EU Commission DSA proceedings (26 January 2026) and Ofcom, ICO and Irish DPC investigations into Grok-generated sexualised images on X; no outcomes found [VF: V2-S070] [R: A5-S082]. xAI signed only the Safety and Security chapter of the GPAI Code of Practice [VF: R-EU-GPAI-COP, A8-S015].
- *Strengths:* low list price for a flagship and presence on all three hyperscalers [VF: A5-S079, A5-S027] [AJ].
- *Limitations:* change of control and naming churn; no ISO 27001; no documented EU API region; derived-data terms [AJ].
- *Choose when:* a low-cost secondary reasoning model is wanted, already in-tenant on your hyperscaler [AJ].
- *Avoid when:* ownership stability or ISO 27001 is a gate, or client data would reach the first-party API without ZDR [AJ].
- *Competitors:* OpenAI GPT, Anthropic Claude, Google Gemini.
- *FS note:* hyperscaler route only; refresh due diligence after the change of control [Rec].
- **Tier: Tactical. Flag: Acquired.**

**Mistral AI family (Mistral AI).**
- *What it is now:* Mistral Large 4 entered public preview on 6 October 2026: about 1T total parameters (docs say 1.05T / 52B active, the launch post 1T / 49B), multimodal, 1M context, API-only in preview, weights targeted for 27 October 2026, licence and list price not yet published [VF: A5-S076, V2-S017]. Mistral Medium 3.5 (28 April 2026; 128B dense; 256K context; Modified MIT v26.04; US$1.50 / US$7.50 per 1M) is the GA flagship [VF: A5-S074, V2-S018]. Large 3 (December 2025, Apache 2.0), Small 4.0, Ministral 3, Magistral (reasoning), Devstral 2 and Codestral (coding), Mistral OCR and Voxtral (speech) complete the line [VF: A5-S074] [R: A5-S038].
- *Certifications and residency:* SOC 2 Type II and ISO 27001/27701 per Mistral's help centre, reports via the Trust Center on request; data hosted in the EU by default; EU regional endpoint api.eu.mistral.ai commits inference location (10% surcharge); some features may transfer data outside the EU; no training on API data; default 30-day retention; ZDR only for pay-as-you-go stateless calls at Mistral's discretion [VF: A5-S075].
- *Deployment:* first-party API; Google Cloud, Bedrock and Microsoft Foundry carry different subsets; Scaleway hosts Medium 3.5; open weights for self-hosting [R: A5-S027, A5-S038] [VF: A5-S074].
- *Lifecycle:* a published table of deprecated and retired models with replacements: Medium 3.1 (the graphic's label) retired on 31 August 2026; Small 3.2 and Devstral 2 (devstral-2512) on 31 July 2026; Labs models may be removed with 1 month's notice [VF: B-L1-S002].
- *Strengths:* EU-hosted by default with an EU inference commitment, open weights at several tiers, and presence on all three hyperscalers: the natural EU and open-weight leg of a portfolio [AJ]. Mistral is a GPAI Code of Practice signatory [VF: R-EU-GPAI-COP, A8-S015].
- *Limitations:* the frontier tier is a days-old preview; Medium 3.5's licence has revenue-based exceptions; certification scope is not stated; ZDR is discretionary [VF: A5-S076, A5-S074, A5-S075]. Mistral also resells Z.ai GLM models on its platform, so contracting with Mistral does not by itself exclude Chinese-origin models [R: A5-S038] [AJ].
- *Choose when:* you need an EU-domiciled vendor and EU inference, or a non-Chinese open-weight model for a self-hosted tier [AJ].
- *Avoid when:* you need a GA frontier-class model now, or your licence policy rejects revenue-threshold terms [AJ].
- *Competitors:* OpenAI GPT, Google Gemma, Meta.
- *FS note:* use the EU endpoint or self-host; obtain the SOC 2 report and ISO certificate scope; allow-list Mistral's own models at the gateway [Rec].
- **Tier: Strategic. Flag: Superseded** (the graphic's Medium 3.1). Strategic as the EU and open-weight leg of the portfolio, not as the sole frontier model [AJ].

**Google Gemma 4 (Google).**
- *What it is now:* Gemma 4 comprises E2B, E4B, a 26B MoE and a 31B dense model (31 March / 2 April 2026) and a 12B unified multimodal model (3 June 2026). All take image and video input and E2B/E4B also take audio; context is 128K on the small sizes and up to 256K on the larger ones [VF: A5-S034, V2-S020]. The licence is Apache 2.0 [VF: A5-S034, V2-S020]. Gemma "2.9" in the graphic does not exist [VF: A5-S034].
- *Deployment:* self-hosted from phones and laptops to a single data-centre GPU; managed on Google Cloud (26B at US$0.15 / US$0.60 per 1M) and offered on Bedrock [VF: A5-S034, A5-S027] [R: A5-S038, A5-S035].
- *Strengths:* a permissively licensed, multimodal small model family from a major vendor, suitable for in-estate classification, extraction and redaction [AJ]. Google reports 150 million Gemma 4 downloads [VF: A5-S034].
- *Limitations:* no frontier tier; no vendor support for weights verified; one README links a separate Gemma licence page that was not read [VF: A5-S034] [AJ].
- *Choose when:* data must not leave the estate, or the task is high-volume classification or extraction [AJ].
- *Avoid when:* the task needs frontier reasoning or long-form drafting quality [AJ].
- *Competitors:* Mistral (Ministral, Small), Meta (Muse Glimmer, Llama 4), Qwen3.8-27B, gpt-oss.
- *FS note:* self-host behind the gateway, pin model files by hash, and validate it as a model in its own right [Rec].
- **Tier: Strategic, conditional: as the small, self-hosted open-weight tier. Flag: none.**

**Meta Muse and Llama (Meta).**
- *What it is now:* Meta Superintelligence Labs announced Muse Spark in April 2026; Muse Spark 1.1 opened the Meta Model API preview on 9 July 2026, 1.2 followed on 5 August with Muse Code, and 1.3 on 2 September; Meta announced Model API GA at Connect (23–24 September 2026) [VF: A5-S077, A5-S078, V2-S019]. Muse Glimmer 30B was released in August 2026 under Apache 2.0, on secondary evidence [VF: A5-S078] [R: V2-S019, A5-S040]. Llama 4 Scout and Maverick remain the latest Llama models, under the Llama 4 Community License (a separate licence above 700M MAU) [VF: A5-S077, A5-S027].
- *Deployment:* Meta Model API; Muse Spark 1.3 on Microsoft Foundry and Oracle Cloud, Google Cloud private preview; Llama 4 on Google Cloud, Bedrock and Foundry; open weights for self-hosting [VF: A5-S077, A5-S027] [R: A5-S038].
- *Data terms:* the "contributor" tier is discounted in exchange for Meta using prompts and completions to train future models [VF: V2-S019]. Certifications, retention and EU residency for the Meta Model API are not publicly verified [NPV].
- *Strengths:* continuity for firms already self-hosting Llama, and another US open-weight option (Glimmer) [AJ].
- *Limitations:* brand transition; API only weeks past GA; official Llama API client SDK last released 18 December 2025 [VF: A5-S047]; Meta's GPAI Code of Practice status not verified [NPV].
- *Choose when:* you already run Llama 4 in-estate, or want Glimmer as an extra open-weight candidate [AJ].
- *Avoid when:* client data would go to the Meta Model API, and always for the contributor tier [AJ].
- *Competitors:* Google Gemma, Mistral, OpenAI gpt-oss.
- *FS note:* block the contributor tier at the gateway by model ID [Rec].
- **Tier: Tactical. Flag: Renamed** (Llama to Muse as the frontier brand).

**Chinese-origin families: common facts.** The regulatory position of these four vendors is a matter of jurisdiction, data location and reputation as well as capability [AJ]. The verified facts are:
- *No private-sector ban.* No US ban on private-sector use exists as of October 2026; congressional investigations, a reported revival of executive-action plans and a pending "No Adversarial AI Act" are recorded [VF: A5-S060]. The UK has no government-wide ban; a Lords written answer (HL4479) says DeepSeek inputs "will be sent to China and thus [are] subject to Chinese law", and DWP bars DeepSeek on its devices [VF: A5-S061].
- *Government-device bans* (DeepSeek-specific): Australia's PSPF Direction 001-2025 for Commonwealth entities; Taiwan's government agencies; US FY2026 NDAA s.1532 (DoD use or acquisition, with waivers) and s.6604 (intelligence community); several Commerce bureaus; Texas, New York, Virginia and Iowa state devices [VF: A5-S054, A5-S059, A5-S057, A5-S056]. A policy tracker says the s.1532 prohibition took effect for DoD and its contractors when performing DoD contracts around 17 January 2026 [R: V2-S069].
- *Independent evaluations.* NIST's CAISI (whose pages now carry the title CAISSI [VF: V2-S021]) found DeepSeek R1/V3.1 more susceptible to agent hijacking and jailbreaks, with censorship risk (September 2025) [VF: A5-S049]; Kimi K2 Thinking heavily censored in Chinese, and Kimi K3 (with UK AISI, July 2026) below frontier cyber capability with safeguards that did not stop attempted exploit development [VF: A5-S051]; GLM-5.3 the most cyber-capable open-weight model to date, about four months behind the US frontier (September 2026) [VF: A5-S052, V2-S021]. No CAISI evaluation of Qwen was found [VF: A5-S051].
- *Export controls.* Zhipu AI has been on the US Entity List since 16 January 2025 [VF: A5-S072].
- *Data location of each vendor's own API:* DeepSeek stores data in the PRC; Moonshot's international API stores data in Singapore; Z.ai processes data "generally" in Singapore; Alibaba Model Studio is region-bound with a Frankfurt EU scope [VF: A5-S062, A5-S070, A5-S073, A5-S067].
- *Hosting outside the vendor:* Microsoft Foundry sells DeepSeek V4 directly, processed in the customer's geography; Foundry's Kimi K3 and GLM-5.x run on Fireworks outside the tenant; Bedrock offers Kimi K3 and GLM 5.3 cross-Region only and Qwen3 (not 3.8) in EU and UK regions [VF: A5-S087, A5-S086].
- *Anthropic's allegation.* Anthropic alleges that DeepSeek, Moonshot and MiniMax distilled Claude; this is an unadjudicated allegation by a competitor of these vendors, and the author is an Anthropic model, so it is not used as an input to any score [VF: A5-S046, V2-S022] [AJ].

**DeepSeek V4 family (DeepSeek, Hangzhou, PRC).**
- *What it is now:* DeepSeek-V4-Pro (1.6T total / 49B active; preview 24 April 2026, GA 13 August 2026; 1M context) and DeepSeek-V4.1-Flash (10 September 2026; replaced V4-Flash in the API; native vision); thinking and non-thinking modes; open weights under MIT [VF: A5-S063, A5-S064]. A planned V4-Pro phase-out from 14 September 2026 was reversed: the pricing page's note of 17 September says the V4-Pro API continues [VF: V2-S013]. There is no V4.1-Pro [VF: A5-S064].
- *Hosted API:* DeepSeek collects, processes and stores personal data in the PRC under mainland PRC law, with no EU/UK residency and no stated API training position [VF: A5-S062]. Italy's Garante imposed an urgent limitation on 30 January 2025 (GDPR Arts 6, 31, 32 and Chapter III), still described as continuing in May 2026 with no fine or lifting found [VF: A5-S048, V2-S023]. Korea's PIPC found unconsented transfers of prompts and device data (24 April 2025); the Berlin DPA reported the app under DSA Art. 16 (27 June 2025) [VF: A5-S053, A5-S058]. Certifications not publicly verified [NPV].
- *Self-hosted weights and in-tenant hosting:* MIT weights allow self-hosting and air-gap; V4-Flash has been run on a single Ascend NPU with CPU offload, while V4-Pro needs a large cluster [VF: A5-S063] [R: A5-S042, A5-S044]. Microsoft Foundry is the only hyperscaler offering V4 [VF: A5-S087, A5-S086, A5-S027].
- *Strengths:* the most permissive licence among the large Chinese-origin families [AJ].
- *Limitations:* hosted API unusable for client data in a regulated firm; CAISI's hijacking findings argue against agentic use; frequent product churn [AJ].
- *Choose when:* policy permits Chinese-origin weights and a self-hosted or Foundry in-tenant model is wanted for low-risk, non-agentic tasks [AJ].
- *Avoid when:* any data would reach DeepSeek's own API; the model would hold tools; the firm performs DoD contracts [AJ].
- *Competitors:* Mistral, Gemma, Qwen.
- *FS note:* hosted API not recommended; weights only, behind the gateway and guardrails, after a documented sovereignty assessment [Rec].
- **Tier: Tactical, conditional: self-hosted MIT weights or Foundry in-tenant only. Flag: Not recommended (applies to the hosted API).** Security scores 1 on the hosted API's record; self-hosted weights would score about 3 under rule 2 [AJ].

**Alibaba Qwen3.8 family (Alibaba Cloud).**
- *What it is now:* hosted qwen3.8-max (launched 3 August 2026; 1M context), qwen3.8-flash and omni-flash through Model Studio; open weights Qwen3.8-27B (Apache 2.0), Qwen3.8-2.4T-A95B (12 August 2026) and Qwen3.8-Flash-Next (26 August 2026); coding and embedding lines [VF: A5-S066, A5-S068] [R: V2-S014, A5-S040].
- *Licence:* the flagship weights use a custom "Qwen3.8-Max License" under which Model-as-a-Service businesses above US$50m trailing revenue need a separate licence; the licence file itself was not read [R: V2-S014].
- *Hosted API:* Model Studio is region-bound (Frankfurt EU scope, Singapore International, US Virginia, Beijing mainland) and says it never trains on customer data [VF: A5-S067]. Certifications and access controls not publicly verified [NPV].
- *Self-hosted and hyperscaler:* Qwen3.8 is not offered on any hyperscaler; Bedrock offers the earlier Qwen3 in London, Ireland, Stockholm and Milan [VF: A5-S086, A5-S067].
- *Regulatory:* Taiwan's NSB (November 2025) flagged Tongyi/Qwen among five PRC models with security and bias failings; no Qwen-specific ban found; Beijing was reported in July 2026 to be considering restricting overseas access to leading Chinese models, including open-weight Qwen (unenacted) [VF: A5-S059] [R: A5-S060].
- *Strengths:* widest open-weight size range; an Apache-2.0 27B model [AJ].
- *Limitations:* no hyperscaler route for the current generation; custom flagship licence; unverified certifications [AJ].
- *Choose when:* policy permits, and a small Apache-2.0 model is wanted self-hosted [AJ].
- *Avoid when:* you need a current-generation hyperscaler route, or would use the flagship weights without licence review [AJ].
- *Competitors:* Gemma, Mistral, DeepSeek.
- *FS note:* self-host the Apache-2.0 sizes only; treat Model Studio Frankfurt as unassessed [Rec].
- **Tier: Tactical, conditional: self-hosted Apache-2.0 sizes only. Flag: none.**

**Moonshot Kimi family (Moonshot AI).**
- *What it is now:* Kimi K3 launched on 16 July 2026, with weights by 27 July: a 2.8T MoE (about 104B active, reported), natively multimodal, 1M context, under the custom Kimi K3 License (revenue and MAU thresholds) [VF: A5-S069] [R: V2-S015]. K2.7-Code and earlier K2.x models remain [R: A5-S038].
- *Hosted API:* the international API is operated from Singapore and stores data there; the mainland platform keeps data in the PRC; the API page says inputs are not used for training while the international privacy policy lists training as a purpose [VF: A5-S070]. Certifications not publicly verified [NPV].
- *Hyperscaler and self-hosted:* Bedrock offers K3 through US, India and global cross-Region profiles only; Foundry's K3 is Fireworks-operated outside the tenant (US Data Zone); weights can be self-hosted but at 2.8T parameters this is a multi-node undertaking [VF: A5-S086, A5-S087] [AJ].
- *Strengths:* very large open-weight multimodal model [AJ].
- *Limitations:* most facts rest on secondary sources; no in-region managed route; custom licence; CAISI findings above [VF: V2-S015, A5-S051] [AJ].
- *Choose when:* research and evaluation in an isolated sandbox [AJ].
- *Avoid when:* any production use with client data [AJ].
- *Competitors:* DeepSeek, GLM, Qwen.
- *FS note:* no client data; sandbox only after licence review [Rec].
- **Tier: Experimental. Flag: none.**

**Z.ai GLM family (Zhipu AI; the graphic's "QI4").**
- *What it is now:* no model named "QI4" or "Q4" exists; the Z logo matches Z.ai's GLM family [R: A5-S038] [VF: A5-S047]. GLM-5.3 (753B) launched on the API in mid-August 2026 (14 August per CAISI, 18 August per press), with weights around 28 August under a bespoke licence (an MIT-style grant with a condition for very large Model-as-a-Service businesses); GLM-5.3-Flash (26 August 2026; 320B / 18B active; natively multimodal) is MIT; GLM-5.2 has open weights; GLM-Image covers images [VF: A5-S071, V2-S021] [R: V2-S016, A5-S042].
- *Hosted API:* personal data is "generally processed in Singapore" and may move to affiliates overseas; the current DPA says API content is not stored, an older version said temporary storage; the general privacy policy cites model training under legitimate interest [VF: A5-S073]. Certifications not publicly verified [NPV].
- *Hyperscaler and self-hosted:* GLM 5 runs in-Region in London on Bedrock, GLM 5.3 on Bedrock cross-Region only from 5 October 2026; Google Cloud hosts GLM-4.7/5/5.2; Foundry's GLM runs on Fireworks outside the tenant; Mistral resells GLM 5.x and retires GLM 5.2 on 31 October 2026 [VF: A5-S086, A5-S027, A5-S087, B-L1-S002].
- *Export controls:* Zhipu AI has been on the US Entity List since 16 January 2025 (presumption of denial for EAR items) [VF: A5-S072].
- *Strengths:* an MIT-licensed multimodal Flash model; CAISI's independent finding that GLM-5.3 is close to the frontier on cyber tasks [VF: A5-S071, A5-S052].
- *Limitations:* Entity List exposure for any commercial relationship; data-term conflicts; CAISI found GLM-5.2's safeguards allowed agentic exploit assistance [VF: A5-S072, A5-S073, A5-S052].
- *Choose when:* sanctions counsel and sovereignty policy permit, and a small MIT model is wanted self-hosted [AJ].
- *Avoid when:* a direct contract with Z.ai would be needed, or client data would reach the Z.ai API [AJ].
- *Competitors:* DeepSeek, Qwen, Mistral.
- *FS note:* self-hosted GLM-5.3-Flash only, after sanctions and licence review [Rec].
- **Tier: Tactical, conditional: self-hosted MIT weights only, after sanctions review. Flag: none.**

### 1.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1-openai | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4.25 | 4.05 | Strategic |
| L1-anthropic | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3.60 | 3.55 | Tactical |
| L1-google-gemini | 5 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.50 | 3.35 | Strategic |
| L1-xai-grok | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 2 | 3.50 | 3.25 | Tactical |
| L1-deepseek | 4 | 4 | 1 | 4 | 4 | 2 | 3 | 4 | 3.25 | 3.15 | Tactical |
| L1-alibaba-qwen | 4 | 2 | 2 | 4 | 4 | 3 | 3 | 3 | 3.15 | 3.00 | Tactical |
| L1-moonshot-kimi | 3 | 4 | 2 | 3 | 3 | 2 | 2 | 3 | 2.80 | 2.80 | Experimental |
| L1-zai-glm | 4 | 4 | 2 | 4 | 3 | 2 | 3 | 3 | 3.25 | 3.15 | Tactical |
| L1-mistral | 4 | 4 | 3 | 5 | 4 | 3 | 4 | 4 | 3.90 | 3.85 | Strategic |
| L1-google-gemma | 3 | 4 | 3 | 5 | 4 | 4 | 4 | 4 | 3.80 | 3.80 | Strategic |
| L1-meta | 3 | 4 | 2 | 4 | 4 | 2 | 3 | 3 | 3.15 | 3.05 | Tactical |

**Scoring notes [AJ]:**
- *Conflict of interest.* Three Anthropic criteria were borderline and were resolved against Anthropic: technical (4 not 5: no open weights, audio or image output), ecosystem (4 not 5: not the de facto API) and cost (3 not 4: same tier prices as OpenAI, but a residency premium and a dearer recommended default). Security was also held at 4 although the certificates meet the rule-8 threshold for 5, because there is no first-party EU/UK inference and the top tier's ZDR terms conflict. The tier was held at Tactical because FS 3.55 is below the normal line. The reviewer should check these calls.
- *Evidence caps.* Security is capped at 2 for Qwen, Kimi, GLM and Meta (certifications NPV, rule 1). DeepSeek scores 1: certifications NPV *and* an unremediated Garante limitation on a service that stores data in the PRC. Qwen's enterprise readiness is capped at 2 because Qwen3.8 is on no hyperscaler and Model Studio's controls are NPV.
- *Hyperscaler presumption (rule 6)* gives enterprise readiness 4 to every other family, because each has a current-generation model operated in-tenant by a hyperscaler (for DeepSeek, Microsoft Foundry; for Kimi and GLM, Bedrock cross-Region). The vendors' own APIs would score 2 for DeepSeek, Kimi, GLM and Meta. Platform controls presumed (CP2 Q1); confirm per service.
- *Certification scope (rule 8).* Mistral's certificates are stated without product scope, so security is one point below the anchor. OpenAI's ISO 42001 scope does not name the API, so it does not count toward 5.
- *Ownership change (rule 3).* Grok's lock-in was reduced by 1 and it carries the Acquired flag.
- *Licence risk (rule 4).* Revenue or usage thresholds in Medium 3.5, Llama 4, Kimi K3, Qwen3.8 flagship and GLM-5.3 are stated in the lock-in rationales.
- *Hyperscaler lead service (rule 10).* Gemini is Strategic, conditional on Google Cloud being the primary cloud, at FS 3.35. This is why Gemini outranks Anthropic in tier while scoring lower: rule 10 is a platform-commitment rule, not a quality judgement.
- *Calibration (rule 5).* Criteria at 2 or below appear for eight of the eleven families. Enterprise readiness is flat at 4 for ten families because of rule 6, not because the vendors' own controls are equal.
- *No vendor benchmark* was used for any score. Independent CAISI evaluations were used only for technical and risk rationale.

**Key facts.**

| Family | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| OpenAI | Proprietary; gpt-oss Apache 2.0 [VF: A5-S005] | API, Bedrock, Foundry; gpt-oss self-host [VF: A5-S008, A5-S009] | SOC 2 Type 2, ISO 27001/17/18/701 (API); ISO 42001 (scope does not name API) [VF: A5-S007, V2-S062] | First-party EU storage and processing (MAM/ZDR); Foundry EU Data Zone [VF: A5-S006, A5-S009] | OpenAI [VF: A5-S002] |
| Anthropic | Proprietary; no open weights [VF: A5-S010] | API, Bedrock, Google Cloud, Foundry, Claude Platform on AWS [VF: A5-S010] | SOC 2 Type II, ISO 27001, ISO 42001, CSA STAR L2 (API and Bedrock/Google Cloud in scope) [VF: A5-S021, V2-S063] | Not first-party; via Google Cloud EU and Bedrock regional (+10%) [VF: V2-S075, A5-S011] | Anthropic, PBC; draft S-1 1 June 2026 [VF: A5-S024] |
| Google Gemini | Proprietary [VF: A5-S032] | Google Cloud, Gemini API [VF: A5-S027] | SOC 2, ISO 42001 (Google Cloud gen AI) [VF: A5-S028] | UK/EU data at rest; regional endpoints [VF: A5-S029, A5-S027] | Google [VF: A5-S031] |
| Grok | Proprietary [R: A5-S038] | API, Google Cloud, Bedrock, Foundry [VF: A5-S027] | SOC 2 Type II; no ISO found [VF: A5-S080] | None documented for API [VF: A5-S080] | SpaceXAI (formerly xAI), acquired 2 Feb 2026 [VF: V2-S011] |
| Mistral | Apache 2.0 / Modified MIT / unpublished (Large 4) [VF: A5-S074, A5-S076] | API, three hyperscalers, self-host [VF: A5-S074] [R: A5-S038] | SOC 2 Type II, ISO 27001/27701 (scope unstated) [VF: A5-S075] | EU default; EU endpoint [VF: A5-S075] | Mistral AI [VF: A5-S047] |
| Gemma 4 | Apache 2.0 [VF: V2-S020] | Self-host, edge, Google Cloud, Bedrock [VF: A5-S034, A5-S027] | Not applicable to weights; inherits host [AJ] | In-estate [AJ] | Google [VF: A5-S034] |
| Meta | API-only (Muse Spark); Apache 2.0 (Glimmer, secondary); Llama 4 Community License [VF: A5-S077] [R: V2-S019] | Meta API, Foundry, OCI, hyperscalers (Llama), self-host [VF: A5-S077, A5-S027] | Not publicly verified [NPV] | Not publicly verified [NPV] | Meta [VF: A5-S077] |
| DeepSeek | MIT weights [VF: A5-S063] | API (PRC), Foundry in-tenant, self-host [VF: A5-S062, A5-S087] | Not publicly verified [NPV] | API none; Foundry customer geography [VF: A5-S062, A5-S087] | DeepSeek (PRC) [R: A5-S062] |
| Qwen | Apache 2.0 (27B); custom Max licence (flagship) [VF: A5-S066] [R: V2-S014] | Model Studio, self-host; Qwen3 only on hyperscalers [VF: A5-S067, A5-S086] | Not publicly verified [NPV] | Model Studio Frankfurt scope [VF: A5-S067] | Alibaba Cloud [VF: A5-S047] |
| Kimi | Kimi K3 License (custom) [VF: A5-S069] | API (Singapore), Bedrock cross-Region, Foundry via Fireworks, self-host [VF: A5-S086, A5-S087] | Not publicly verified [NPV] | None found [VF: A5-S070] | Moonshot AI (Singapore / PRC entities) [VF: A5-S070] |
| GLM | MIT (5.3-Flash); MIT-style with MaaS condition (5.3) [VF: A5-S071] | API (Singapore), three hyperscalers, Mistral platform, self-host [VF: A5-S086, A5-S027] | Not publicly verified [NPV] | None found; Bedrock GLM 5 in London [VF: A5-S073, A5-S086] | Zhipu AI, US Entity List [VF: A5-S072] |

### 1.9 Decision tree

The tree builds a portfolio in four steps. Step 0 is a precondition, not a product choice [Rec].

```text
STEP 0 [Rec] (not optional): all model calls go through the firm's gateway (C1) with pinned
model IDs, data-class → route/region policy, logging to L9, and a model inventory entry (C8).
Applications never call a vendor API directly.

STEP 1 [Rec]: Which routes may this data class use?
  Client / personal / confidential data?
  ├─ Yes → only (a) hyperscaler-hosted, in an approved UK/EU region, in-tenant, no-training,
  │        ZDR or short retention; or (b) self-hosted open weights in the estate.
  │        Never: a vendor's own API without a first-party EU region and ZDR;
  │               any Chinese-origin vendor's own API; any "trains on data" tier.
  └─ No (public or internal low-risk) → vendor API also allowed, after due diligence.

STEP 2 [Rec]: Mid-tier primary and fallback (two different vendors, same region)
  Primary cloud?
  ├─ Azure  → primary: GPT-6.1 Sol (Foundry EU Data Zone)
  │           fallback: Mistral Medium 3.5 (Foundry or EU endpoint)
  │           (EU processing for Claude on Foundry is not verified; its Azure-hosted
  │            deployment is still "In-Process Q4 2026" for certification)
  ├─ AWS    → primary: Claude Sonnet 5.5 or GPT-6 tier on Bedrock in an EU region
  │           (confirm per-model regional availability; Astra is US-only on Bedrock)
  │           fallback: the other of those two, or Mistral via Bedrock / EU endpoint
  ├─ Google → primary: Gemini 3.8 Flash (EU region, logging/caching off)
  │           fallback: Claude Sonnet 5.5 via Google Cloud EU (GPT-6 is not on Google Cloud)
  └─ Multi-cloud or none → primary: OpenAI EU endpoint (ZDR) or Mistral EU endpoint
              fallback: the other; add a hyperscaler route when available
  Independent alternatives to any Claude choice: GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5.

STEP 3 [Rec]: Small and open-weight tiers
  High-volume classification / extraction / routing?
    → small tier of the primary vendor (Luna, Haiku 5.5, Flash-Lite) or self-hosted Gemma 4
  Data must never leave the estate, or air-gap required?
    → self-hosted: Gemma 4 (Apache 2.0), Mistral Medium 3.5 / Large 3, gpt-oss-120b
    → Chinese-origin weights (DeepSeek MIT, Qwen3.8-27B, GLM-5.3-Flash) only if the
      firm's sovereignty policy explicitly allows them, never with tool access,
      and GLM only after sanctions review
  Frontier tier (Astra, Fable 5.1, Argon)?
    → only when evaluation shows the mid tier fails a named use case; keep disabled otherwise

STEP 4 [Rec]: Checks before go-live
  Second vendor qualified on the same L9 suite?  Failover drill passed?
  Every pinned model's retirement date > re-qualification lead time?
  Contract, DPA, register-of-information / MTP entry and exit plan done for each vendor?
```

### 1.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| A single proprietary frontier vendor for an important business service | **Unacceptable** | Suspension, retirement, legal or residency events at one vendor stop the service; the Fable 5 suspension [VF: V2-S004] and short Gemini Flash lifetimes [VF: B-L1-S003] show the risk is real | Two-vendor mid tier through the gateway; exit plan tested |
| Proprietary frontier API, consumed through a gateway with a qualified second vendor | **Manageable** | Switching cost is re-qualification, not re-engineering, if prompts and schemas are neutral | OpenAI-shaped internal contract at C1; prompts in Git (C5); L9 suite per use case |
| Vendor-specific features (prompt caching formats, vendor tool-use extensions, vendor agent runtimes) | **Manageable, if wrapped** | Each vendor's features differ; using them directly embeds the vendor | Use only behind adapters; keep a feature-free fallback path |
| Hyperscaler route for models | **Manageable** | Concentrates on a designated CTP [VF: R-UK-CTP, A8-S023]; region and model availability differ per cloud | Second route (vendor EU endpoint or self-host) for important services |
| Open weights under Apache 2.0 or MIT | **Acceptable** | The firm holds the weights and can keep running them | Internal model registry with hash pinning (C7) |
| Open weights under custom licences with thresholds (Kimi K3, Qwen3.8 flagship, GLM-5.3, Llama 4, Medium 3.5) | **Manageable** | Thresholds rarely bind an asset manager's internal use but must be read [AJ] | Legal review recorded in the inventory |
| Chinese-origin vendor's own hosted API | **Unacceptable for client data** | Jurisdiction, unverified certifications and, for DeepSeek, an unremediated GDPR limitation [VF: A5-S062, A5-S048] | Not used; weights only where policy allows |
| Training-on-data tiers (e.g. Meta contributor tier) | **Unacceptable** | Data-use condition, not a price [VF: V2-S019] | Gateway deny-list by model ID |

### 1.11 Regulated FS lens (POV 2)

**Model risk.**
- *Is an LLM a "model"?* PRA SS1/23 applies to all models used to inform business decisions, in-house or vendor, is technology-agnostic, and lists explainability and transparency as complexity factors for AI [VF: R-PRA-SS123, A8-S008, A8-S037]. It applies directly to banks, building societies and PRA-designated investment firms with internal-model approval [VF: R-PRA-SS123, A8-S008]. BoE AI Consortium minutes record that GenAI systems are often classified as high risk under SS1/23 frameworks [VF: R-PRA-SS123, A8-S037].
- *Consequence for L1.* A foundation model used in a business process should be inventoried as a vendor model with its version, route and region, validated for its intended use, and monitored (SS1/23 Principles 1, 4 and 5) [AJ]. For an FCA solo-regulated manager SS1/23 is not binding but is the natural benchmark [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly places generative and agentic AI outside its scope; for those, the firm's own risk-management practices should determine governance [VF: R-US-MRM, A8-S001, A8-S002, V2-S049]. The agencies' planned AI request for information had not been published by 7 October 2026 [VF: R-US-MRM, A8-S001]. US bank-owned managers therefore have no US supervisory model-risk standard for LLMs, and should govern them to SS1/23 quality anyway [AJ].
- *Validation independence.* Validation of a vendor model must not rely solely on the vendor's own evaluations or tooling; vendor benchmarks are not evidence [AJ].
- *Version changes are model changes.* Every model-version change (including a forced retirement) is a change requiring re-validation on the L9 suite; notice periods range from about 2 weeks for previews to at least 6 months for GA models at OpenAI [VF: B-L1-S001].

**EU AI Act.**
- *Providers versus deployers.* GPAI obligations (technical documentation, downstream information, copyright policy, training-content summary; extra duties for systemic-risk models) fall on the model providers [VF: R-EUAIA, A8-S013]. The Commission's enforcement powers over GPAI apply from 2 August 2026, and models placed on the market before 2 August 2025 must comply by 2 August 2027 [VF: R-EUAIA, A8-S011].
- *The firm is normally a deployer.* Its duties are AI literacy, Article 50 transparency where relevant and, for any Annex III high-risk use, the Article 26 deployer duties from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011]. Fine-tuning or repurposing a model into a high-risk purpose can make the firm a provider under Article 25 [VF: R-EUAIA, A8-S011].
- *Due-diligence data point.* The GPAI Code of Practice signatories include Amazon, Anthropic, Google, Microsoft, Mistral AI and OpenAI; xAI signed only the Safety and Security chapter [VF: R-EU-GPAI-COP, A8-S015]. The status of Meta, DeepSeek, Alibaba, Moonshot and Z.ai was not verified [NPV]. Record each vendor's status and request its Model Documentation Form [Rec].

**DORA, the UK CTP regime and outsourcing.**
- *Designations.* DORA's first CTPP list (18 November 2025) includes AWS, Google Cloud and Microsoft and no AI model provider [VF: R-DORA, A8-S021, V2-S051]. The UK designated AWS, Google Cloud, Microsoft and Oracle as CTPs with effect from 13 July 2026, and no model vendor [VF: R-UK-CTP, A8-S023, V2-S052].
- *Consequence.* A model consumed through a hyperscaler sits under a designated, directly overseen provider; a model consumed through the vendor's own API does not, which leaves more of the oversight burden on the firm [AJ]. Either way, the firm keeps its own due-diligence and contingency duties [VF: R-UK-CTP, A8-S023].
- *Notifications and exits.* PRA PS7/26 and FCA PS26/2 require notification before entering into or significantly changing a material third-party arrangement from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062, V2-S053]. SS2/21 expects documented and tested exit plans, including stressed exit [VF: R-PRA-SS221, A8-S048]. A hosted model supporting an important business service is likely a material arrangement, so adding a second model vendor needs notification lead time from March 2027 [AJ].
- *Concentration.* IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. The two-vendor mid tier is the architectural answer; the gateway's concentration ratio is the evidence [AJ].

**Residency and transfers.**
- *Per-vendor position.* First-party EU processing exists for OpenAI (EU endpoint) and Mistral (EU endpoint and EU default) [VF: A5-S006, A5-S075]. Anthropic offers none first-party; EU processing is through Google Cloud or Bedrock [VF: V2-S075, A5-S027]. Google offers UK/EU data at rest on Google Cloud [VF: A5-S029]. xAI documents only a US regional endpoint [VF: A5-S080].
- *Transfers.* EU-to-US transfers rely on the Data Privacy Framework or SCCs, and the DPF annulment appeal C-703/25 P is pending [VF: R-DATA-TRANSFERS, A8-S053]. EU-to-UK transfers rely on adequacy renewed to 27 December 2031 [VF: R-DATA-TRANSFERS, V2-S055]. Region-pinned hyperscaler routes plus masking at C3 reduce exposure [AJ].
- *Chinese-origin models.* No UK or US private-sector ban exists [VF: A5-S061, A5-S060]. But DeepSeek's own API stores data in the PRC, the UK government has said DeepSeek inputs are subject to Chinese law, Italy's limitation continues, and US DoD contract work is barred from DeepSeek [VF: A5-S062, A5-S061, A5-S048, V2-S023, A5-S057]. Zhipu is on the US Entity List [VF: A5-S072]. For a regulated firm the defensible position is: no Chinese-origin vendor APIs for client data; Chinese-origin open weights only by explicit policy decision, self-hosted, without tool access, and with the reputational and future-regulation risk recorded [Rec].

**Auditability.** Each output must be traceable to the exact model ID, route, region, prompt version and parameters; the gateway records these and L9 retains them under the records policy [AJ]. Anthropic's Compliance API and Activity Feed (6-year retention) is one vendor-side source, but the firm's own gateway log is the record of truth for every vendor [VF: A5-S018] [AJ].

**US public-sector exposure.** Firms with US defence work should record that the D.C. Circuit upheld a FASCSA supply-chain-risk designation of Anthropic on 25 September 2026 (stayed pending rehearing) [VF: A5-S084], and that DoD use of DeepSeek is barred under FY2026 NDAA s.1532 [VF: A5-S057]. Legal should assess both; this section does not characterise the scope of the Anthropic ruling [AJ].

**Standards.**
- *NIST.* NIST AI RMF 1.0 and the Generative AI Profile (AI 600-1) give a neutral risk taxonomy for model selection and monitoring [VF: R-NIST-AIRMF, A8-S043, A8-S044].
- *ISO.* ISO/IEC 42001 is held by OpenAI, Anthropic and Google Cloud's generative AI services, with OpenAI's scope wording not naming the API [VF: A5-S007, A5-S021, A5-S028, V2-S062]. Check the scope, not the logo [Rec].
- *OWASP.* Model selection and red-team suites should map to the OWASP Top 10 for LLM Applications 2026 (released August–September 2026) and the Top 10 for Agentic Applications for 2026 [VF: R-OWASP-LLM, V2-S056; R-OWASP-AGENTIC, A8-S042].
- *UK supervisors.* The FCA relies on existing frameworks (Consumer Duty, SM&CR) rather than AI-specific rules [VF: R-UK-AI-STATEMENTS, A8-S055]; a named senior manager should own the model portfolio [AJ].

### 1.12 Worked-example slice (POV 3)

**What the commentary agent needs from L1 [AJ].** The agent drafts the monthly Brinson-style attribution commentary (allocation, selection, currency and benchmark-relative return) for a generic multi-asset fund. A portfolio manager approves every draft. From this layer it needs four model roles, each pinned, each routed by the gateway, and each with a documented alternative:

| Role | What it does | Requirements | Example configurations (choose by primary cloud) [Rec] |
|---|---|---|---|
| **Primary drafting model** (mid tier) | Writes the narrative from the attribution engine's figures and retrieved house style | In-region (UK/EU), in-tenant, no training, ZDR or short retention; strong instruction following; pinned version with ≥ 6 months' runway | Azure: GPT-6.1 Sol in a Foundry EU Data Zone. AWS: Claude Sonnet 5.5 via a Bedrock EU regional endpoint. Google Cloud: Gemini 3.8 Flash in an EU region |
| **Fallback drafting model** (different vendor) | Takes over on outage, suspension or retirement | Same region and data terms; passed the same evaluation suite in the last quarter | Azure: Mistral Medium 3.5. AWS: a GPT-6 tier on Bedrock (confirm EU availability) or Mistral. Google Cloud: Claude Sonnet 5.5 via Google Cloud EU |
| **Small classifier** | Classifies reviewer edits, tags commentary sections, routes requests | Cheap, fast, deterministic settings; no client identifiers | GPT-6 Luna, Claude Haiku 5.5 or Gemini 3.5 Flash-Lite in-region; or self-hosted Gemma 4 E4B |
| **Self-hosted open-weight model** | Any step that touches unmasked client or holdings data (e.g. checking a draft against client-specific mandate wording) | Runs in the firm's estate; Apache 2.0 or MIT; hash-pinned | Gemma 4 31B or Mistral Medium 3.5 on the firm's GPUs via L2 |

The primary choice above names a Claude model only for an AWS estate, and an independent alternative is named in the same table [AJ].

**Flow.** The attribution engine produces the figures through a read-only tool (L4). The drafting model receives those figures as structured input, with client identifiers masked (C3), and writes prose around them. The L9 numeric-faithfulness check compares every figure, sign and direction word in the draft with the engine's output. On a mismatch the draft fails, whatever the model tier [AJ].

**What the model must never do [AJ]:**
- generate, round, recompute or "correct" any number; every figure comes from the attribution engine and is traceable
- present its own inference (e.g. a market explanation) as source data; inference must be distinguishable and grounded in approved sources
- be swapped for another model or version without the regression suite passing
- run on an alias ("latest") or a preview model
- receive unmasked client identifiers through any external route
- be a Chinese-origin vendor's hosted API, a training-on-data tier, or a gated frontier tier that nobody approved for this use

**Evidence per commentary (to C8).** Model ID and version, route and region, fallback used (yes or no), prompt and template version, token counts and cost, evaluation results, and approver [AJ].

### 1.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| OpenAI "GPT-6" | Tiered family: Astra (gated), Sol, Luna, 6.1 Sol; GPT-5.6 still offered; gpt-oss open weights [VF: A5-S002, A5-S004, A5-S001, A5-S005] | Strategic: mid-tier primary or fallback on Azure/AWS; Luna for the small tier [Rec] |
| Claude "Opus 5.5" | Correct but not top tier: Fable 5.1 above Opus/Sonnet/Haiku 5.5; Mythos restricted; Fable 5 suspended 12 June – 1 July 2026; no first-party EU inference [VF: A5-S010, V2-S004, V2-S075] | Tactical (FS 3.55, borderline calls against Anthropic; reviewer to confirm): hyperscaler EU routes only, with a non-Anthropic fallback [Rec] |
| Gemini (no version) | Gemini 3.x (3.1 Pro preview, 3.8 Flash GA, 3.5 Flash-Lite); Gemini 4 Argon restricted [VF: A5-S030, A5-S031] | Strategic where Google Cloud is primary; pin versions against short retirement windows [Rec] |
| Grok (no version) | Grok 4.7; SpaceXAI (formerly xAI) after SpaceX acquisition [VF: A5-S079, V2-S011] | Tactical: secondary option via a hyperscaler only [Rec] |
| DeepSeek "V4" | V4-Pro (phase-out reversed) and V4.1-Flash; MIT weights; API stores data in the PRC [VF: A5-S064, V2-S013, A5-S062] | Tactical, weights or Foundry in-tenant only; hosted API not recommended [Rec] |
| Qwen "3.8" | Correct; flagship weights under a custom licence; not on hyperscalers [VF: A5-S066, A5-S086] [R: V2-S014] | Tactical: Apache-2.0 sizes self-hosted, by policy [Rec] |
| Kimi "K3" | Correct; custom licence; cross-Region or pass-through hyperscaler routes only [VF: A5-S069, A5-S086, A5-S087] | Experimental [Rec] |
| "QI4" (Z logo) | No such model; Z.ai GLM-5.3 / 5.3-Flash; Zhipu on US Entity List [VF: A5-S071, A5-S072] | Tactical: MIT Flash weights only, after sanctions review [Rec] |
| Mistral "Medium 3.1" | Retired 31 August 2026; Medium 3.5 GA; Large 4 preview [VF: B-L1-S002, A5-S074, A5-S076] | Strategic as the EU and open-weight leg [Rec] |
| Gemma "2.9" | No such version; Gemma 4 under Apache 2.0 [VF: A5-S034, V2-S020] | Strategic as the small self-hosted tier [Rec] |
| Meta "Llama (new: Muse)" | Muse Spark API GA; Muse Glimmer open; Llama 4 latest Llama [VF: A5-S077, V2-S019] | Tactical: open-weight continuity; block the contributor tier [Rec] |
| (single "LLM" row) | Every vendor sells tiers; gating, short lifetimes and residency routes now matter as much as capability [VF: A5-S002, A5-S016, B-L1-S003] [AJ] | A governed model portfolio: two-vendor mid tier, small tier, self-hosted open-weight tier, all behind C1 and qualified in L9 [Rec] |

**Hypothesis note.** No hypothesis (H1–H8) is assigned to L1. The layer's findings bear on **H1** (promote the gateway to a control-plane component): a model portfolio with residency routing, version pinning, fallback and deny-lists is unworkable without a firm-owned gateway, which supports H1 [AJ]. They also bear on the LinkedIn pair-8 tension, "treat models as a portfolio, not a bet". The counter-argument is that a portfolio multiplies validation and contract work; the answer is to keep the portfolio small (two mid-tier vendors, one small model, one open-weight model) and make the L9 suite do the re-qualification [AJ]. **Provisional; verdict in synthesis.**
