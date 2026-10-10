# Part XVII: The view for start-ups selling agentic SDLC tools

**In brief.**
- **Who it is for.** An early-stage company selling coding agents, AI code review, test generation, migration agents or other agentic software-development tools to engineering teams in enterprises. It competes with, or plugs into, the large coding-agent platforms (views.json) [AJ].
- **What changes.** The FS view designs a firm's control plane. A coding agent runs inside that plane and inside the customer's software-delivery chain at once: it reads source code, holds developer permissions, spends tokens heavily and changes software through a pull request. The buyer wants its own model endpoint, identity, tool gateway and evidence [AJ].
- **The hard truth.** The incumbents already ship the enterprise baseline (SSO, SCIM, audit export, MCP allow-lists, zero-retention options, ISO/IEC 42001), and several of them changed owner or product line in 2026. A start-up wins on depth in one task, model neutrality and evidence, not on breadth [VF: E3-S010, E3-S026, E3-S027, E3-S004, E3-S029, E3-S033] [AJ].
- **The view at end of Q3 2026.** Evidence read on 9–10 October 2026; prices, retention terms and product names in this market are volatile and re-verified each quarter [AJ].

> **Conflict-of-interest disclosure.** The author is an Anthropic model. Claude Code is recorded on the same evidence standard as every other tool, and wherever it is mentioned independent alternatives are named: OpenAI Codex CLI and Gemini CLI (both open source), JetBrains Junie, and Tabnine for self-hosted estates. Under this view's weights Claude rises to second in L1 and MCP (Anthropic-originated, now under the Agentic AI Foundation) to first in L4, from the same criterion scores as every other product [AJ].

## XVII.1 Who this view is for

**Profile.** A start-up of five to forty people selling one agentic capability (a migration agent, a review bot, a test generator) to engineering leaders in large enterprises, whose buyers care about code confidentiality, model choice, auditable agent changes, cost per task and fit with their repositories, CI and identity (views.json) [AJ].

**Assumptions.** EU, UK and US enterprise customers, including regulated financial firms; a SaaS and a customer-run edition; customers on GitHub or GitLab with an enterprise IdP and a hyperscaler model service; no model of its own [AJ].

**The five biggest differences from the FS view [AJ]:**

| # | FS view (Parts I–XII) | Agentic-SDLC start-up view | Consequence for the architecture |
|---:|---|---|---|
| 1 | The firm owns the control plane | The product is a workload consuming the customer's gateway, identity, vault and collector | Every model, tool and credential path points at the customer's service [AJ] |
| 2 | The crown jewels are client data | The crown jewels are source code and the credentials that can change it | No code retention, no training, and no standing write access; the pull request is the only write path [AJ] |
| 3 | Deterministic workflows with one bounded model step (Part I.2) | The agent loop is the product | Autonomy is bounded by a sandbox, an egress allow-list and a human merge, not by removing the loop [AJ] |
| 4 | Cost weighs 5%; reviewer time is the cost driver | Cost weighs 15%; long, repeated repository prefixes make tokens the cost of goods | Prompt caching, a background (flex) route and cost per task are designed in from the first release [AJ] |
| 5 | Model-risk and outsourcing rules govern a deployer | The start-up is a CRA manufacturer, an AI-system provider and a third party in FS registers | Vulnerability handling, SBOMs and flow-down replace model validation [AJ] |

## XVII.2 Findings that change for this view

**1. The customer's model endpoint is the default, not an option.** Copilot has local and enterprise bring-your-own-key [VF: E3-S002]; Cursor allows BYOK for chat models [VF: E3-S030]; the Codex CLI takes custom and local providers [VF: E3-S025]; Junie is LLM-agnostic with BYOK [VF: E3-S050]; Tabnine runs customer-chosen models [VF: E3-S055]; Claude Code runs through Anthropic, three hyperscalers or a customer gateway, with Claude models only [VF: E3-S014, E3-S079]. A product that cannot route to the customer's endpoint through the customer's gateway is below the baseline [AJ].

**2. Retention depends on the model, not the tool.** Claude Fable 5 and 5.1 retain data by default for safety classifiers, with ZDR in Copilot only through an exemption to the end of 2026 [VF: E3-S011]. Cursor's ZDR does not apply to BYOK keys [VF: E3-S032, E3-S030]; Codex cloud is not strict ZDR [VF: E3-S024]; Claude Code defaults to 30-day retention, with ZDR per qualified Enterprise organisation [VF: E3-S015]. "No retention of code" is a per-route property the product must report [AJ].

**3. The integration surfaces have converged on open formats.** AGENTS.md was donated by OpenAI to the Agentic AI Foundation on 9 December 2025 [VF: E3-S060, E3-S061]; Copilot, Cursor, Claude Code, Junie and Amp read it, while Kiro uses steering files [VF: E3-S007, E3-S031, E3-S017, E3-S051, E3-S054, E3-S042]. MCP is supported by Copilot, Cursor, Claude Code, Gemini CLI, Kiro, Junie and Amp, and an MCP allow-list is a standard admin control [VF: E3-S001, E3-S030, E3-S019, E3-S035, E3-S042, E3-S051, E3-S054, E3-S004, E3-S037]. Reading AGENTS.md and shipping an MCP server that works under a managed allow-list fits every incumbent's estate [AJ].

**4. The pull request is the control boundary the market has adopted.** Copilot's cloud agent works in an ephemeral environment and opens pull requests, and agent-written code is scanned by CodeQL, secret scanning and the advisory database before the pull request is finalised [VF: E3-S008, E3-S003]. Cursor attributes cloud-agent commits in Git history [VF: E3-S028]; Kiro's autonomous mode opens a pull request [VF: E3-S042]. SLSA v1.2's Source Track records who made each change and which controls applied [VF: E3-S077], but no field for agent-authored commits was found [NPV]. Recording the agent identity and the directing human in commit trailers and pull-request metadata is the practical stop-gap [Rec].

**5. Telemetry exists; complete audit does not.** Copilot exports OpenTelemetry traces of agent sessions, without prompt content by default [VF: E3-S081]. The OTel GenAI agent and MCP conventions are still at Development, with no tagged release [VF: E3-S066, E3-S067, E3-S068, E3-S069]. The Codex Compliance API does not cover every hosted file operation, command or approval, and keeps logs for 30 days [VF: E3-S023]. An audit trail of every agent action in the customer's store is a gap a start-up can fill [AJ].

**6. The incumbents are consolidating and model vendors are moving in.** Cursor is now part of SpaceX, which also owns xAI [VF: E3-S029, V2-S011]; Grok 4.5 was reportedly trained alongside Cursor, per SpaceX filings read only through a search summary [R: E3-S029]. Windsurf became Devin Desktop under Cognition, Tricentis acquired Tabnine, and Amp spun out of Sourcegraph [VF: E3-S045, E3-S056, E3-S053]. Google stopped selling new Gemini Code Assist subscriptions on 9 October 2026, and Q Developer reaches end of support on 30 April 2027 [VF: E3-S033, E3-S040]. The neutral coding tool is becoming scarce: the start-up's opening and its likely exit [AJ].

**7. Wrapping an incumbent's agent has terms attached.** A vendor that embeds Claude Code must ship it unmodified, with each end user authenticating with their own credentials [VF: E3-S016]. GitHub's third-party agent slot is in public preview and lists only Claude and Codex [VF: E3-S003]. Building on a model vendor's harness limits both the business model and the model choice [AJ].

**8. The start-up's own software is a CRA product, now.** Installed IDE plug-ins, CLIs, agents and SDKs are CRA products; the 24-hour and 72-hour reporting duty has applied since 11 September 2026 through ENISA's Single Reporting Platform, and SBOM and support-period duties apply from 11 December 2027 [VF: E1-S001, E1-S002, E1-S003, E1-S006]. An agent that writes into a customer's product also makes the start-up a component supplier to that customer's CRA products [AJ].

**9. Secure-development guidance for AI-written code is thin.** NIST SSDF v1.2 is still a draft with no practice for AI code generation, and SP 800-218A covers developing generative models [VF: E3-S063, E3-S064]; no NIST or CISA guidance on coding assistants was found [NPV]. The nearest material is the Five Eyes agentic AI guidance, OpenSSF's guide for AI code assistant instructions and the OWASP Agentic Top 10 [VF: E3-S065, E3-S062, E3-S072]. The start-up must write its own control statement against these [Rec].

**10. Caching is the cost lever.** Coding agents resend long, stable prefixes [AJ]. An Anthropic cache read costs 0.05x the base price on Opus 5.5 and Sonnet 5.5, and OpenAI's cached input on gpt-6.1-sol is US$0.10 against US$2.00 per 1M [VF: V2-S002, A5-S004]. OpenAI Flex (Batch rates, possible 429s) and Bedrock Flex (50% off) suit background migrations and test generation, not interactive sessions [VF: E2-S031, E2-S032] [AJ].

## XVII.3 Scoring for this view

**What is scored.** In a vendor view the scores describe the components the start-up builds its own product on, not the product it sells [AJ]. The ten coding-agent platforms in the landscape are recorded in `work/stageE/E3_agents_sdlc/products.json` (layer "DV") without scores or tiers, and none is given one here [AJ]. The view re-weights the same eight criterion scores the FS view uses; no product fact or criterion score changes, and the weights are architectural judgement (views.json) [AJ]:

| Criterion | FS weight | DV weight | Why it moves [AJ] |
|---|---:|---:|---|
| Technical | 15 | 25 | The product is only as good as its agent loop, models and tools |
| Enterprise readiness | 15 | 10 | The start-up supplies the enterprise wrapper itself |
| Security and compliance | 20 | 15 | Still high: customers hand over source code |
| Deployment flexibility | 15 | 10 | Needed for the customer-run edition, but the start-up picks its own stack |
| Ecosystem | 5 | 15 | Fit with developer tooling and protocols (MCP, AGENTS.md, OTel) |
| Reliability and maturity | 10 | 5 | Developer tools move fast and are pinned and patched by the start-up |
| Cost and TCO | 5 | 15 | Token-heavy workloads set gross margin or the customer's bill |
| Lock-in and portability | 15 | 5 | Developer tools are replaced often; the start-up can migrate |

**What moves, and why.** The largest gains go to components with high technical, ecosystem and cost scores: Voyage AI rises from 3.05 to 3.60, Model Armor from 3.35 to 3.80, and Grok, Agent Skills, Composio, Cloudflare AI Gateway and Prisma AIRS by 0.35 each; SPIFFE/SPIRE falls by 0.35 because its strengths in lock-in and deployment weigh less (`DV_scores.md`) [AJ]. A rise in score is not a rise in tier: Composio stays Experimental after its token-exposure incident [VF: B-L4-S007] [AJ].

**Core candidates.** 63 products are core candidates under these weights, against 45 under FS, of 138 scored; 20 become core candidates and two become situational (`DV_scores.md`, `05_Data/views.json`) [AJ]. The components a DV start-up is most likely to build on are below; tiers are quoted as in Part XI [AJ]:

| Ref | Component the start-up builds on | Master tier | FS → DV | DV fit |
|---|---|---|---|---|
| L1 | OpenAI GPT | Strategic | 4.05 → 4.35 | Core candidate |
| L1 | Claude (alternatives: GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5) | Strategic, conditional | 3.80 → 3.95 | Core candidate |
| L1 | Mistral | Strategic | 3.85 → 3.90 | Core candidate |
| L2 | vLLM | Strategic | 4.30 → 4.40 | Core candidate |
| L3 | LangGraph | Strategic | 4.20 → 4.45 | Core candidate |
| L3 | OpenAI Agents SDK | Tactical | 3.30 → 3.60 | Becomes core candidate |
| L3 | Claude Agent SDK (alternatives: LangGraph, Pydantic AI, OpenAI Agents SDK) | Experimental | 2.75 → 2.90 | Situational |
| L4 | MCP (alternative: OpenAPI tools) | Strategic, conditional | 3.55 → 3.80 | Becomes core candidate |
| L4 | E2B | Tactical | 3.35 → 3.45 | Situational |
| L9 | Promptfoo | Tactical | 3.55 → 3.75 | Becomes core candidate |
| C1 | LiteLLM | Strategic, conditional | 3.90 → 4.20 | Core candidate |
| C4 | Okta / Auth0 for AI Agents | Strategic, conditional | 3.55 → 3.80 | Becomes core candidate |
| C4 | MCP Authorization (alternative: OAuth resource-server pattern on OpenAPI tools) | Strategic, conditional | 3.45 → 3.65 | Becomes core candidate |
| C7 | HashiCorp Vault | Strategic, conditional | 3.65 → 3.75 | Core candidate |

**How to read the fit.** The fit is indicative; master tiers and conditions stand (Part I.3) [AJ]. Presidio (3.65 → 3.45) and prompts as code (3.65 → 3.50) become situational, and this view keeps both: a coding-agent vendor's prompts and tool definitions are its product and belong in Git, and the customer's privacy service is what the product calls [AJ]. E2B stays situational (3.45, below the 3.6 threshold; enterprise readiness 2), but it remains the reference pattern for the sandbox, which a coding agent cannot do without [VF: A3-S062] [AJ].

**Anthropic.** The Claude family moves from third to second in L1 (3.80 → 3.95), behind OpenAI (4.35), because its technical, ecosystem and cost scores gain weight; its lowest criteria remain deployment flexibility 3 and reliability 3 (`DV_scores.md`) [AJ]. The Claude Agent SDK remains Experimental and eleventh of twelve in L3 [VF: A4-S006, B-REVC-S001] [AJ].

**Where to find the full table.** Every product's FS and DV score, rank and fit is in `05_Data/views.xlsx`; the per-layer listing is `work/stageE/views/DV_scores.md` [AJ].

## XVII.4 The architecture for this view

The FS architecture (Part IV.1) is the buyer's and is not redrawn [AJ]. A coding agent is not a layer of it but a harness that consumes L1 models, uses L4 protocols and needs C4, C1 and L9/C8 (landscape records) [AJ]. The figure shows that footprint and the second system the product lives in, the software-delivery chain [AJ].

![The agentic-SDLC product inside the customer's stack: the customer's identity, models, tools and evidence; the vendor's agent loop](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/DV-1.png){width=100%}

*Figure: The start-up ships an agent runner that executes in the customer's account or on the customer's CI runners, with a thin vendor control plane that never holds source code. Every model call goes through the customer's gateway to the customer's model endpoint, every tool call through the customer's tool gateway, every credential comes from the customer's vault, and the only way the agent changes code is a pull request that the customer's CI checks and a named human merges. Spans, cost per task and an evidence record go to the customer's collector and evidence store. Editable source: `08_Graphic/diagrams/DV-1.md`.* [AJ]

**Three delivery forms, one code path.** Incumbents span vendor-hosted cloud agents (Copilot, Codex cloud), a vendor-hosted single-tenant VPC (Devin), customer runners (Claude Code self-hosted environments in beta; Junie's GitHub Action) and air-gapped installs (Tabnine) [VF: E3-S008, E3-S022, E3-S044, E3-S018, E3-S051, E3-S055]. Offer three forms from one build [AJ]:

| Form | Where code is processed | Model route | Who buys it [AJ] |
|---|---|---|---|
| Vendor-hosted sandbox, EU region | Vendor's account; ephemeral microVM per task | Vendor's two-vendor route with ZDR, or the customer's key | Pilots; non-sensitive repositories |
| Customer-run runner | Customer's CI runners or cloud account | Customer's gateway and endpoint only | Most enterprises; the FS default |
| Air-gapped edition | Customer's estate, no outbound connection | Open-weight model on the customer's vLLM | Defence-adjacent, public sector and the most regulated buyers |

**Four properties the product must prove [AJ].** It never writes to a protected branch and never merges; it holds no standing credential, receiving short-lived, repository-scoped tokens per task; every model, tool and network call is attributable to a task, an agent identity and a directing human; and removing it leaves nothing behind but pull requests, commits and evidence records in the customer's own systems.

## XVII.5 Where the product sits and how it fits into the Enterprise GenAI Stack

**Map the product first.** A DV product sits beside the stack, not in one tile: it is an L3 agent loop with L4 tools, run as a workload of the customer's platform [AJ]. The table sets out the interface the buyer's stack expects at each layer and control; the FS defaults are those of Part VII Stack A [AJ]:

| Layer / control | Interface the buyer's stack expects | What the product must do | Evidence or reason |
|---|---|---|---|
| L1 models | The customer's chosen vendor and tier, pinned | Model-agnostic prompts and tools, qualified per task type; for Claude, alternatives GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5 | Incumbents compete on model choice [VF: E3-S014, E3-S025, E3-S050] |
| L2 inference | Hyperscaler endpoint or private vLLM route | OpenAI-compatible client; tolerate Flex 429s in background work | vLLM is OpenAI-compatible [VF: A4-S063]; Flex 429s [VF: E2-S031] |
| L3 orchestration | Bounded workflow: plan, change, test, pull request | Durable task runs; step budget; stop on request | FS default (Part I.2) [AJ] |
| L4 tools | MCP behind the customer's tool gateway; AGENTS.md | MCP server under managed allow-lists (alternative: OpenAPI tools behind the same gateway); code only in a microVM with default-deny egress | [VF: E3-S004, E3-S019, A3-S062] |
| L5 memory | None held by the vendor | Learnings proposed as pull requests to AGENTS.md | Memory poisoning is ASI06 [VF: E3-S072] |
| L6 stores | The repository is the store | Per-task index in the sandbox, destroyed at task end | Every store is another copy to exit (Part VIII) [AJ] |
| L7 retrieval optimisation | The customer's `embed` service, if any | Pinned, self-hostable embeddings (Sentence Transformers) | Hosted embedding adds a processor [AJ] |
| L8 ingestion | Approved sources only | Read only what the task names | Hidden instructions are ASI01 [VF: E3-S072] |
| L9 evaluation | OTel GenAI spans to the customer's collector | `gen_ai.*` agent and tool spans, pinned version, content off by default | [VF: E3-S067, E3-S069, E3-S081] |
| C1 gateway | Gateway-routed calls, a key per product and task type | Configurable base URL and key; no direct vendor SDK path | One gateway of record (Part I.2) [AJ] |
| C2 guardrails | The customer's tests, linters and SAST | The customer's CI result is the gate | Copilot scans agent code first [VF: E3-S003] |
| C3 privacy | The customer's privacy service | Redact personal data and secrets before trace export | Six enforcement points (Part I.2) [AJ] |
| C4 identity | SSO/SCIM; agent acting for the engineer | Entra Agent ID or Okta for AI Agents; MCP EMA (alternative: OAuth on OpenAPI tools) | ID-JAG draft behind EMA [VF: E3-S073, A6-S079, A6-S080] |
| C5 configuration | Configuration as code in the customer's Git | Policy, routes and tools in a versioned file; managed settings | [VF: E3-S082, E3-S019] |
| C6 FinOps | Cost per customer, team and task | Tokens, cache hits and runner minutes in a FOCUS-shaped export | [VF: A7-S096, E3-S003] |
| C7 security | The customer's vault and package mirror | Short-lived tokens; mirror-only dependencies; SBOM per release | OpenSSF guide [VF: E3-S062] |
| C8 governance | Evidence record per agent action | Task, model, tools, commands, diff and approver to the customer's store | Part V.8 register [AJ] |

**The software-delivery chain.** The second integration contract is with the repository, CI, review and identity [AJ]:
- **Repository.** Write only to agent branches, never to protected ones; read AGENTS.md as the repository's instructions; sign commits and add trailers naming the agent identity, the task and the directing human [Rec]. Support GitHub Enterprise Server as well as cloud SCM, because Copilot is not available there while Claude Code cloud sessions are [VF: E3-S001, E3-S079] [AJ].
- **CI.** Run the customer's own tests on the customer's runners, as Junie's GitHub Action does [VF: E3-S051]; never bypass a required check [Rec].
- **Review.** The pull request is the approval record; a named human with merge rights approves, and the agent's identity can never satisfy a required review [Rec].
- **Identity.** The engineer signs in through the customer's IdP; the agent acts on that engineer's behalf with a token scoped to one repository and one task [Rec].

## XVII.6 What enterprise buyers will ask, and how to pass

**Use the FS buyer as the toughest test.** Part V describes the buyer's obligations; this section turns them into the questions a DV vendor will face [AJ].

| Question | What the regime or buyer requires | How to pass [Rec] |
|---|---|---|
| Are you a third party in our register? | DORA Article 30 clauses [VF: A8-S021, E1-S055]; critical functions add exit strategies and on-site audit [VF: E1-S056] | A ready DORA clause pack; state in writing whether the tool supports a critical function |
| Who are your subcontractors? | Identify all subcontractors, such as model API providers; pass audit rights down; allow objection to material changes [VF: E1-S057] | Publish model and sandbox providers as subprocessors |
| What are your AI Act duties? | Supplying an AI system under your own name makes you its provider [VF: A8-S016]; code assistants are not listed as high-risk, so Article 50 and the provider role are the live duties [VF: E1-S035] [AJ]; fine-tuning makes an integrator a GPAI provider only above one third of original training compute [VF: E1-S034] | State the role in the contract; disclose AI authorship in the pull request; do not fine-tune at scale |
| Are you CRA-ready? | Installed CLIs, plug-ins and agents are CRA products; reporting since 11 September 2026; SBOM and support period from 11 December 2027 [VF: E1-S001, E1-S002, E1-S003] | A vulnerability-handling policy, an SBOM per release, a stated support period and an ENISA reporting runbook [VF: E1-S006] |
| What if your agent destroys data? | Software is a product under the PLD from 9 December 2026 [VF: E1-S010, E1-S011]; data destroyed by an agent is a recoverable type of damage [AJ] | No destructive commands outside the sandbox; no write access beyond the agent branch |
| Will you meet our NIS2 supply-chain terms? | NIS2 customers impose supply-chain security terms on suppliers [VF: E1-S016, E1-S019] | Accept them, and show the incident runbook |
| Do you retain or train on our code? | Incumbents state no training on business code; retention is model-specific [VF: E3-S011, E3-S032, E3-S015, E3-S057] | No training; zero retention when customer-run; a per-model retention table when hosted |
| Who owns the output, and do you indemnify? | Anthropic defends against IP claims from authorised use, excluding modified outputs and combinations [VF: E2-S004]; Google indemnifies unmodified generated output, not agent actions [VF: E2-S007]; Copilot's indemnity depends on a filter that does not apply to its coding agent [VF: E3-S010] | Customer owns all output; pass model-vendor indemnities through where available; be explicit that agent-authored code is reviewed by the customer before merge |
| Can we run it ourselves? | Stack A prefers customer-run components (Part VII) [AJ] | Customer-run and air-gapped editions; PrivateLink or Private Link for the hosted plane [VF: E2-S052, E2-S049] |
| How do we leave? | Data Act: no switching charges from 12 January 2027 [VF: E1-S025] | Everything of value is already in the customer's repository and evidence store; configuration is a file in Git |

**Certifications and their sequencing [Rec].** The incumbents set the baseline: Copilot lists SOC 2 Type 2, ISO/IEC 27001 and ISO/IEC 42001; Cursor lists SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 42001:2023 and AIUC-1; Junie has its own SOC 2 Type II report [VF: E3-S010, E3-S026, E3-S048]. Sequence: SOC 2 Type I then Type II (still assessed against the 2017 criteria) [R: E2-S048]; ISO/IEC 27001:2022, since 2013 certificates are no longer valid [R: E2-S046]; a CSA AI-CAIQ at STAR for AI Level 1 early, because it is free to publish, then Level 2 with ISO/IEC 42001 [VF: E2-S047, A8-S045]. AIUC-1's market weight beyond one listing is not established [NPV].

**Model-vendor terms that flow down [Rec].** In a hosted edition, carry Anthropic's Usage Policy to end users (Anthropic may suspend a customer for its users' breaches) [VF: E2-S005, E2-S004], Google's under-18 bar [VF: E2-S007] and OpenAI's ban on transferring API keys [VF: E2-S026]. A customer-run edition on the customer's model account carries the customer's own terms [AJ].

**Escrow.** No source in the dataset records escrow practice for AI developer tools [NPV]; a customer-run edition with a stated support period is the stronger answer, because exit then needs no vendor [AJ].

## XVII.7 The start-up's own reference stack

**What to build the product on.** The start-up runs two planes: the agent runner it ships, and a thin SaaS control plane for licences and job metadata. S, T and E abbreviate the master tiers; hyperscaler model services are access patterns, not scored (Part I.3) [AJ].

| Layer / control | Cloud-neutral | AWS | Azure | Google Cloud |
|---|---|---|---|---|
| L1 models | Two unrelated vendors per task type: OpenAI GPT (S) with Claude (S, cond.; alternatives GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5) or Mistral (S); air-gapped: Mistral, gpt-oss or Gemma 4 (all S) | Claude or a GPT-6 tier on Bedrock [VF: A5-S008] | GPT-6.1 Sol in Foundry | Gemini (S, cond.) |
| L2 inference | Customer's endpoint first; vLLM (S) for the open-weight edition | Bedrock Standard plus Flex for background tasks [VF: E2-S032] | Foundry Standard and Batch; Azure caching nuances [VF: E2-S019] | Gemini Enterprise Agent Platform endpoint |
| L3 orchestration | LangGraph (S) + Temporal (S); Pydantic AI (S, cond.) or OpenAI Agents SDK (T); Claude Agent SDK (E) only in one sandboxed step (alternatives as before) | Strands on AgentCore (S, cond.) | Microsoft Agent Framework (S) | ADK on Agent Engine (S, cond.) |
| L4 tools | Own MCP server (MCP S, cond.; alternative OpenAPI tools); E2B (T) BYOC sandbox; AGENTS.md read, Agent Skills (T; Anthropic-maintained, alternative AGENTS.md or C5 packages) optional | AgentCore Gateway + Identity (S, cond.) | APIM AI gateway (S, cond.) | Apigee MCP (S, cond.) |
| L5–L8 | No vendor-side memory or store; per-task index in the sandbox; Sentence Transformers (S) if embeddings are needed | Same | Same | Same |
| L9 evaluation | OTel spans; Langfuse (S) or MLflow (S); task suites on real repositories; Promptfoo (T) plus an independent red-team tool | MLflow on SageMaker | MLflow on Azure ML | Langfuse self-hosted |
| C1 gateway | LiteLLM (S, cond.), pinned and signed, inside the hosted plane; customer's gateway in customer-run editions | Same | Same | Same |
| C2 guardrails | Tests and SAST as the gate; NeMo Guardrails (T) for injected instructions | Bedrock Guardrails (S, cond.) | Azure AI Content Safety (S, cond.) | Model Armor (S, cond.) |
| C3 privacy | Presidio (S, cond.) for trace redaction in the hosted plane | Same | Same | Sensitive Data Protection (S, cond.) |
| C4 identity | SSO and SCIM; Okta/Auth0 (S, cond.) or Entra Agent ID (S, cond.); MCP Authorization (S, cond.; alternative OAuth resource-server pattern on OpenAPI tools); OPA (S) | AgentCore Identity | Entra Agent ID | Okta or Entra |
| C5 configuration | Prompts, tool definitions and policies as code (S) | Same | Same | Same |
| C6 FinOps | Gateway cost attribution (S) per customer and task; FOCUS (S) export | Application inference profiles [VF: B-C6-S004] | Foundry project tags [VF: B-C6-S005] | Gateway metering |
| C7 security | Vault (S, cond.) for the hosted plane; package and model scanning (S); signed releases with SBOMs | Cloud secrets + workload identity | Same | Same |
| C8 governance | Evidence-record schema for the customer's store; OpenLineage (S) for release lineage | Same | Same | Same |

**Do not build yet [Rec].** A proprietary model or fine-tuning; vendor-side long-term memory of customer code; write access to protected branches or auto-merge; multi-agent delegation over A2A; a hosted token broker for customers' SCM credentials, given the Composio incident [VF: B-L4-S007]; Antigravity-based components where the buyer needs ISO 27001 or SOC 2 scope, because they are excluded [VF: E3-S034].

## XVII.8 Build vs buy, and lock-in; where incumbents are and where they are moving

**Build vs buy for the start-up.** Build only the task-specific core and the evidence buyers pay for; adopt open components for the rest [AJ]:

| Component | Decision | Why [AJ] |
|---|---|---|
| Task logic and the task-success evaluation suite | **Build** | This is the product, and the suite is the sales proof |
| Agent loop | **Adopt** an open framework (LangGraph, Pydantic AI, OpenAI Agents SDK) | Frameworks are open and portable [VF: A4-S001, A4-S005]; a model-vendor harness ties the product to one model |
| Sandbox | **Buy or adopt** E2B (open runtime, BYOC) or the cloud's runtime | Isolation is specialist work; the E2B runtime is Apache-2.0, so an exit exists [VF: A3-S062] |
| Evidence and audit (per-action records, commit trailers, OTel spans) | **Build** | It is the gap the incumbents leave [VF: E3-S023] |
| Enterprise wrapper (SSO, SCIM, RBAC, policy as code) | **Build**, and charge for it | The baseline [VF: E3-S027, E3-S005] |
| Model access, hosting, billing | **Buy** (model vendors, clouds, marketplaces) | Marketplace private offers draw down the buyer's cloud commitment [VF: E2-S034, E2-S036, E2-S020] |

**Lock-in, for the start-up.** Lock-in weighs 5%, but three lock-ins matter [AJ]. One model vendor is a product risk: Fable 5 access was suspended from 12 June to 1 July 2026 [VF: V2-S004], and a one-vendor product cannot serve a buyer standardised on another. An incumbent's harness brings its terms [VF: E3-S016]. One SCM's agent slot ties distribution to a preview [VF: E3-S003] [AJ].

**Where incumbents are, and where they are moving.** The landscape records, read even-handedly [AJ]:

| Incumbent | Ownership and product events | Deployment options | Model choice | Direction and implication [AJ] |
|---|---|---|---|---|
| GitHub Copilot | Folded into Microsoft CoreAI [R: E3-S013] | SaaS; GHE Cloud with residency; not on GHES [VF: E3-S001, E3-S009] | Multi-vendor; BYOK [VF: E3-S011, E3-S002] | A multi-agent hub [VF: E3-S003]; sell into it on GitHub's terms |
| Cursor | Part of SpaceX since 14 August 2026 [VF: E3-S029] | SaaS; self-hosting not found [NPV] | Multi-vendor; BYOK for chat [VF: E3-S030] | Joint training with SpaceX/xAI reported [R: E3-S029]; neutrality now questioned |
| Claude Code (Anthropic) | No ownership event recorded | SaaS; Bedrock, Google Cloud, Foundry; customer runners in beta [VF: E3-S014, E3-S018] | Claude only [VF: E3-S014] | Enterprise depth on one model family; independent alternatives: Codex CLI, Gemini CLI, Junie, Tabnine |
| OpenAI Codex | AGENTS.md donated to AAIF [VF: E3-S061] | SaaS cloud tasks; local open-source CLI [VF: E3-S020, E3-S022] | OpenAI default; custom and local providers [VF: E3-S025] | Open CLI widens reach; audit and retention gaps remain [VF: E3-S023, E3-S024] |
| Google (Code Assist, Gemini CLI, Antigravity) | Code Assist end of sale 9 October 2026 [VF: E3-S033] | Google Cloud; Gemini CLI local [VF: E3-S037, E3-S035] | Gemini; Claude optional since 8 October 2026 [VF: E3-S039] | Antigravity is outside several certifications [VF: E3-S034]; a window for certified tools |
| Kiro (AWS) | Q Developer closed to new customers; end of support 30 April 2027 [VF: E3-S040] | SaaS [VF: E3-S041] | Auto routing; Claude models [VF: E3-S042] | Forced migration; newest coding models exclusive to Kiro [VF: E3-S040] |
| Devin (Cognition) | Windsurf renamed Devin Desktop, 2 June 2026 [VF: E3-S045] | SaaS; Cognition-hosted single-tenant VPC [VF: E3-S044] | Not verified [NPV] | Autonomous-agent positioning; FedRAMP High claim unverified [VF: E3-S043] |
| JetBrains Junie | Junie CLI beta; Junie Local [VF: E3-S050, E3-S049] | SaaS; on-premises [VF: E3-S047] | LLM-agnostic, BYOK, local [VF: E3-S050] | The neutral IDE incumbent |
| Amp | Spun out of Sourcegraph [VF: E3-S053] | SaaS [VF: E3-S054] | Vendor-selected mix [VF: E3-S054] | An independent peer; a likely partner or acquirer target |
| Tabnine | Acquired by Tricentis, 30 July 2026 [VF: E3-S056] | SaaS, VPC, on-premises, air-gapped [VF: E3-S055] | Customer models [VF: E3-S055] | Folded into a quality-engineering platform [VF: E3-S056]; test generation is now a platform feature |

**Positioning and exit.** Across the stack, neutral tools are being acquired (Part I finding 2): Langfuse by ClickHouse, Arize by Dynatrace, Promptfoo by OpenAI (announced), Portkey by Palo Alto Networks, Lakera by Check Point [VF: A1-S021, A1-S045, A1-S024, A6-S011, A7-S012]. In coding tools the buyers were a model vendor's owner (SpaceX), an agent company (Cognition) and a testing platform (Tricentis) [VF: E3-S029, E3-S045, E3-S056]. So: position on what platforms will not give away (model neutrality, the customer-run edition, evidence); expect an acquisition to be a change-of-control event in every FS customer's register (Part V.3) and write terms that survive it; and keep the surfaces open (MCP, AGENTS.md, OTel), which keeps more than one acquirer interested [AJ].

## XVII.9 Roadmap

**Size.** Eighteen months from October 2026, a team of eight to twenty, one task type first [AJ].

| Date | Event | Consequence [AJ] |
|---|---|---|
| In force since 11 September 2026 | CRA reporting through ENISA's platform [VF: E1-S003, E1-S006] | Reporting runbook from Phase 0 |
| 12 November 2026 | Anthropic Usage Policy effective date [VF: E2-S005] | Review flow-down in the hosted edition |
| 22 November 2026 | ID-JAG draft -04 expires [VF: E3-S073] | Track the next draft before relying on EMA claims |
| 9 December 2026 | PLD applies [VF: E1-S011] | No destructive capability outside the sandbox |
| End of 2026 | Copilot's ZDR exemption for Claude Fable ends [VF: E3-S011] | Re-check retention tables for every Fable route |
| 12 January 2027 | Data Act switching rules [VF: E1-S025] | Export path for configuration and evidence |
| 18 March 2027 | UK FS third-party notifications [VF: R-PRA-SS221, A8-S062] | DORA and UK clause packs ready |
| 30 April 2027 | Q Developer end of support [VF: E3-S040] | Migration demand among AWS customers |
| 11 December 2027 | CRA main obligations [VF: E1-S002] | SBOMs, support periods and conformity complete |

**Phases [Rec]:**

| Phase (months) | Scope | Exit criterion |
|---|---|---|
| 0 Foundations (0–2) | Model-agnostic adapter behind LiteLLM; MCP server; AGENTS.md support; evidence-record schema; OTel spans; CRA vulnerability policy | One task type passes the evaluation suite on two model vendors |
| 1 Customer-run runner (2–6) | Runner on customer CI and cloud accounts; customer gateway, vault and collector configuration; SSO and SCIM; SOC 2 Type I; STAR for AI Level 1 | First design partner live with zero code leaving its estate |
| 2 Enterprise wrapper (5–10) | Agent identity in Entra or Okta; EMA-ready tool access; admin policy as code; DORA clause pack; SOC 2 Type II window; ISO/IEC 27001:2022 | First FS due diligence passed |
| 3 Scale and cost (9–14) | Prompt caching, Flex route for background tasks, cost per task per customer; second task type; marketplace listing | Margin per task on plan |
| 4 Regulated editions (12–18) | Air-gapped edition on vLLM with open weights; ISO/IEC 42001; CRA conformity work | CRA file complete before 11 December 2027 |

## XVII.10 Worked example: a framework-upgrade agent run inside the customer's stack

**The use case.** The start-up offers an agent that upgrades a customer's Java services to a new framework version: it opens pull requests in the customer's repository, runs the customer's tests in an isolated sandbox, and never merges without human review; enterprise customers require their own model endpoint, no retention of code and an audit trail of every agent action (views.json) [AJ]. Traced as the customer runs it, inside the customer's stack [AJ]:

| Step | What happens | Components |
|---:|---|---|
| 0 | Platform team commits the agent's policy file (repositories, model route, MCP servers, step budget, cost cap); AGENTS.md gives build and test commands | C5 |
| 1 | An engineer assigns "upgrade service X" from the issue tracker, signed in through the customer's IdP | C4 |
| 2 | The agent identity (registered, with a sponsor) gets a short-lived token scoped to repository X and the task | C4, C7 |
| 3 | A microVM starts on the customer's runners; egress only to the gateways, repository and package mirror | L4, C7 |
| 4 | The repository is cloned; AGENTS.md and the issue text are read as data, screened for injected instructions | L8, C2 |
| 5 | A per-task code index is built inside the sandbox | L7, L6 |
| 6 | Planning and editing calls go through the customer's gateway to the customer's model endpoint with no retention; a stable prefix is cached | C1, L2, L1, C6 |
| 7 | Tool calls go through the customer's tool gateway to allow-listed MCP servers; dependencies only from the mirror | L4, C4, C7 |
| 8 | The customer's tests run in the sandbox; on failure the agent revises within its step budget, then stops | L3 |
| 9 | The agent pushes an agent branch and opens a pull request with commit trailers naming the agent, the task and the engineer | L3, C4 |
| 10 | The customer's CI runs tests, SAST and secret scanning; a named reviewer approves and merges | C2, C7, C4 |
| 11 | Spans for every model call, tool call and command go to the customer's collector | L9 |
| 12 | Tokens, cache hits and runner minutes go to the cost dataset; an evidence record goes to the customer's store; the sandbox and index are destroyed | C6, C8 |

**What it costs [AJ].** Assume 200 model calls per service, each with 40,000 input tokens of which 35,000 are a cached prefix, and 1,000 output tokens. At US$2 input and US$10 output per 1M with cached input at US$0.10 (GPT-6.1 Sol; Claude Sonnet 5.5's 0.05x cache read gives the same figure) [VF: A5-S004, A5-S011, V2-S002], one call costs about US$0.024 and a service about US$4.70, against about US$18 uncached. Cache writes, retries and runner minutes come on top. The token counts are the author's assumptions [AJ].

**May [Rec]:** read the named repository, its issues and migration notes; edit code on an agent branch; run the customer's build and tests in the sandbox; open, update and comment on one pull request.

**Must never, and what enforces it [Rec]:**

| Never | Enforced by |
|---|---|
| Merge, or push to a protected branch | Branch protection; the agent cannot satisfy a required review (C4) |
| Retain or train on the customer's code | Customer endpoint with no retention (C1, L1); sandbox destroyed at task end (L4) |
| Call a model or tool outside the customer's gateways | Default-deny egress (L4, C7); gateway-only routes (C1) |
| Hold a standing credential | Short-lived, repository-scoped token from the vault (C7, C4) |
| Install a package from outside the mirror | Mirror-only resolution; OpenSSF slopsquatting defences [VF: E3-S062] |
| Follow instructions found in issues or dependencies | Repository content treated as data; injection screening (C2); OWASP ASI01 [VF: E3-S072] |
| Exceed its step budget or cost cap | Workflow budget (L3); gateway budget failing closed (C1, C6) |

**Evidence kept [Rec].** Policy-file version; agent identity, sponsor and directing engineer; model ID, version, region and route per call; every tool call and command with a result hash; resolved dependency versions; diff, tests and CI checks; the reviewer's decision; tokens, cache hits and cost. In the customer's store this answers audit, CRA vulnerability questions and any PLD claim [VF: E1-S010] [AJ].

## XVII.11 Checklist, what to avoid, what to monitor

**Checklist [Rec]:**
- Route every model call through the customer's gateway to the customer's endpoint; qualify two unrelated model vendors per task type, with a non-Anthropic route beside any Claude route (GPT-6.1 Sol, Gemini 3.8 Flash or Mistral Medium 3.5).
- Read AGENTS.md; ship an MCP server that works under managed allow-lists; keep OpenAPI tools as the independent alternative.
- Run in a microVM with default-deny egress on the customer's runners; destroy it at task end.
- Write only through pull requests, with commit trailers naming agent, task and human.
- Emit OTel GenAI spans with a pinned version; write an evidence record per action to the customer's store.
- Publish a per-model retention table, the subprocessor list, a CRA vulnerability policy and SBOMs.
- Cache stable prefixes; use Flex routes for background tasks; report cost per task.

**Avoid [Rec]:** a single-model product; a wrapped Claude Code that is modified or shares credentials [VF: E3-S016]; auto-merge; vendor-side retention of code or memories; a hosted token broker for SCM credentials [VF: B-L4-S007]; unpinned dependencies from public registries [VF: E3-S062]; claiming "ZDR" for routes that retain by default [VF: E3-S011]; relying on one platform's preview agent slot for distribution [VF: E3-S003]; a 2013 ISO/IEC 27001 certificate in a questionnaire [R: E2-S046].

**Monitor [Rec]:**

| Monitor | Trigger |
|---|---|
| Model-specific retention and the end-2026 Fable exemption [VF: E3-S011] | Update the retention table |
| Cursor under SpaceX; Tabnine under Tricentis; Amp's independence [VF: E3-S029, E3-S056, E3-S053] | Re-assess partners, competitors and acquirers |
| Antigravity certification scope [VF: E3-S034] | Re-check the window for certified alternatives |
| OTel GenAI conventions release; SLSA field for agent-authored commits [VF: E3-S069] [NPV] | Re-pin spans; adopt the field |
| ID-JAG and MCP authorisation drafts [VF: E3-S073, A3-S016] | Update the EMA integration |
| CRA guidance and delegated acts; final NIST SSDF v1.2 [VF: E3-S063] [NPV] | Re-map the control statement and support periods |
| Cache, Flex and Priority pricing [VF: V2-S002, A5-S004, E2-S031, E2-S032, E2-S006] | Re-price tasks quarterly |
