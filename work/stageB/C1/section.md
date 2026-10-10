## C1. AI / LLM gateway

> **Executive summary.** The gateway is the single point through which every model call, and now every tool and agent call, leaves an application. It owns provider abstraction, routing and fallback, quotas and budgets, caching, policy enforcement and the request log [AJ]. The baseline draws it as a control-plane component, not a feature of the inference layer: a hosted router such as OpenRouter now carries budgets, allowlists, zero-data-retention and regional routing [VF: A4-S111, A4-S109], but it is a model-access source behind the gateway, not the gateway itself [AJ]. Four things define the market at the end of Q3 2026. First, the gateways now carry three kinds of traffic: LiteLLM, Kong, Azure API Management, Apigee and agentgateway all govern LLM, MCP and A2A traffic [VF: A6-S015, A6-S016, A6-S053, A6-S024, A6-S061]. Second, ownership is moving towards security vendors: Palo Alto Networks completed its acquisition of Portkey on 29 May 2026 and sells it as Prisma AIRS AI Gateway [VF: A6-S011, A6-S012, V2-S025]. Third, the gateway has proved to be an attack target in its own right: malicious LiteLLM 1.82.7 and 1.82.8 were published to PyPI on 24 March 2026 [VF: A6-S008, V2-S027]. Fourth, the hyperscaler offerings are real but uneven: the Azure API Management AI Gateway tier is preview with no SLA [VF: A6-S020, V2-S073], and no AWS product called "AI gateway" was found: AWS offers an MCP gateway with new inference targets and a LiteLLM-based reference pattern instead [VF: A6-S021, A6-S022, A6-S105]. **Recommendation:** run one firm-controlled gateway of record for all production LLM and MCP traffic, deployed in-region, failing closed, with pinned and signed builds. Choose LiteLLM (hardened and Enterprise-licensed), Kong, Apigee or the GA AI gateway policies in Azure API Management according to your existing API and cloud estate, and keep the model-switch route tested, because the gateway is what makes an exit plan executable [Rec].

### C1.1 Responsibility

**The problem this control owns.** The gateway decides, for every outbound AI request, who may make it, which model or tool receives it, in which region, at what cost ceiling, under which policies, and what record is kept [AJ]. It breaks down into seven jobs:

- **Provider abstraction.** One API (in practice the OpenAI-compatible format) in front of many providers, so applications do not hold provider SDKs or keys [VF: A6-S015, A6-S049, A6-S063] [AJ].
- **Routing, fallback and load balancing.** Choose a model per route, retry, fail over and balance across deployments [VF: A6-S015, A6-S049, A6-S024].
- **Quotas, rate limits and budgets.** Tokens per minute, requests per minute and spend per key, team, user or customer [VF: A6-S015, A6-S020, A6-S105].
- **Caching.** Exact and semantic response caching, which saves cost but is also a confidentiality and correctness risk [VF: A6-S015, A6-S025] [AJ].
- **Policy enforcement.** Invoke guardrails (C2), DLP (C3) and authorisation (C4) inline, before and after the model call [VF: A6-S015, A6-S017, A6-S053].
- **Logging and observability.** One record per request with caller, route, model, tokens, cost, latency, policy outcomes and errors, exported to L9 and C8 [AJ].
- **Tool and agent traffic.** MCP tool federation and A2A agent calls, with per-caller tool exposure [VF: A6-S015, A6-S016, A6-S061].

**Hand-offs.** Above the gateway sit the applications and agent workflows (L3), which call one endpoint with a workload identity from C4 [AJ]. Below it sit the model endpoints (L1 vendors, L2 hosted or self-served models), MCP tool servers (L4) and other agents [AJ]. Alongside it: C2 and C3 supply detectors it calls inline; C4 supplies identity and tool-call policy; C5 holds the routing configuration under change control; C6 consumes its cost records; L9 and C8 consume its logs as evidence; C7 owns its supply-chain assurance [AJ].

**What the control does not own.** It does not decide whether a workflow should be autonomous (L3), and it does not validate output quality (L9). A gateway that blocks a harmful string cannot tell whether an attribution figure is right [AJ].

### C1.2 Why it matters

When the gateway is missing or badly designed, three things fail together [AJ]:

- **Exit becomes theoretical.** Provider SDKs and keys spread through application code, so switching model means a programme of code changes. The exit plan that SS2/21 expects to be documented and tested [VF: R-PRA-SS221, A8-S048] cannot be executed in the time a stressed exit allows [AJ].
- **Cost and residency are invisible.** Without per-request attribution nobody can say what a task costs or where the data went [AJ].
- **The control becomes the risk.** A gateway holds every provider credential and sees every prompt. The March 2026 LiteLLM incident shows that a gateway is a high-value supply-chain target: release credentials were stolen through a compromised CI scanner and two malicious versions were published [VF: A6-S008, A6-S010]. A central component that fails open, or is itself compromised, turns one weakness into an estate-wide one [AJ].

**Illustrative scenario [AJ].** A fund-reporting team routes commentary drafting through a self-hosted gateway. The primary model is pinned to an EU region, and an engineer adds a second provider to the fallback list during a month-end capacity problem without checking where it processes data. Budgets are configured, but the gateway's spend database is unavailable after a restart, and the budget check silently passes. The team also turns on semantic caching to cut cost. Next month-end the EU endpoint is rate-limited; the gateway fails over to the US-hosted fallback for about a day; and two commentaries for similar funds receive a cached paragraph describing the wrong currency effect. Nothing alerts: requests succeeded, latency was normal and the guardrails passed. The data-protection team finds the out-of-region processing in a quarterly log review; the cached paragraph is caught at PM review only because the PM remembered the other fund. Three controls would have prevented it: a residency-constrained fallback list that fails closed, budget enforcement that fails closed, and no semantic cache on client-specific routes. The scenario is invented; it is not a reported incident. (Each of its mechanisms is documented: LiteLLM's `max_budget` fails open without a database, and its docs warn that semantic caching "goes badly wrong on agentic traffic" [VF: A6-S015].)

### C1.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Gateway coverage | Share of production LLM, MCP and A2A calls that pass through the gateway | 100% in scope; any direct provider key in an application is a defect | Provider usage reports reconciled with gateway logs; secret scanning for provider keys |
| Availability | Gateway uptime for gated workflows | At least that of the business service it supports (e.g. ≥99.95%) | Synthetic probes per route and region |
| Added latency | p95 gateway overhead excluding model time | Tens of milliseconds without inline guards; budget per guard separately | Gateway spans vs upstream spans |
| Residency conformance | Requests processed outside the approved region for the route | 0; out-of-region fallback is a blocking defect | Route policy plus provider region in each log record |
| Qualified fallback | Fallback events landing on a model that passed the route's regression suite | 100% | Fallback log joined to L9 qualification register |
| Cost attribution coverage | Requests carrying workflow, team and business-object tags | ≥99% | Gateway log completeness check; C6 reconciliation to invoices |
| Budget enforcement | Budget breaches that were not blocked or alerted | 0; fail closed on loss of the spend store | Breach log; chaos test of the spend store |
| Log completeness | Gateway records reconciled with L9 traces and provider usage | ≥99.9% | Daily three-way reconciliation |
| Time to switch provider | Time to move a route to a pre-qualified alternative by configuration | Hours, not weeks; tested at least annually | Exit drill evidence (C8) |
| Credential exposure | Provider keys held outside the gateway's secret store | 0 | Secret scanning; vault inventory (C7) |
| Supply-chain hygiene | Gateway builds deployed from pinned, verified artefacts | 100% | Image signature verification at admission; package hash pinning |

### C1.4 How it works

A request passes through five stages [AJ]:

1. **Authenticate and identify.** The caller presents a workload identity or virtual key. LiteLLM uses virtual keys and JWT/OIDC [VF: A6-S015]; AgentCore Gateway accepts IAM or custom JWT [VF: A6-S074]; Azure's AI Gateway tier requires Entra sign-in [VF: A6-S020].
2. **Apply pre-call policy.** Token and request limits per counter key (Azure's `llm-token-limit` is GA [VF: A6-S020, A6-S053]; AgentCore estimates tokens up front and reconciles them with provider usage [VF: A6-S105]), budgets, and inline guards. LiteLLM runs guardrails pre-call, during the call or post-call across chat, embeddings, MCP and A2A routes [VF: A6-S015].
3. **Route.** Pick the model or tool by route rules, then retry, load-balance or fail over. Apigee adds circuit breaking across clouds [VF: A6-S024]; Agent Router uses a two-tier design with a Tier One gateway for auth, top-level routing and global rate limits [VF: A6-S063].
4. **Apply post-call policy.** Output guards (C2), DLP (C3), cache write.
5. **Record.** Emit the request record and spans (tokens, cost, latency, policy outcomes) to the firm's collector, and cost records to C6. OpenTelemetry's GenAI conventions now cover client inference, agents, tool execution and MCP [VF: A1-S061], so the gateway can emit the same schema as the rest of the stack [AJ].

For MCP the gateway becomes a tool federator. It presents one MCP endpoint to agents and exposes only the tools each caller is allowed. Kong does this with MCP Server Bundling and per-caller tool exposure [VF: A6-S016]; AgentCore Policy removes denied tools from `tools/list` and is deny-by-default for tool calls [VF: A6-S026]. The MCP 2026-07-28 authorisation spec forbids token passthrough and requires audience validation [VF: A6-S033, A6-S034], so a gateway that fronts MCP servers must mint or exchange tokens per upstream server rather than forward the client's token [AJ].

![C1 request path: every LLM, MCP and A2A call through one firm-controlled gateway](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/C1-1.png){width=100%}

*Figure: Workflows and agents reach models, tools and other agents only through one in-region gateway that authenticates, enforces limits, guards, routes and records every call. Editable source: `08_Graphic/diagrams/C1-1.md`.* [AJ]

**Two placements.** A centralised gateway gives one policy point and one log, but is a shared single point of failure and a concentration of credentials [AJ]. A sidecar or per-domain gateway limits blast radius but multiplies configuration [AJ]. For an asset manager the practical answer is one logical gateway with at least two independent deployments (per region or per criticality tier) sharing configuration from C5 [Rec].

### C1.5 Enterprise design principles

**Security**

- Treat the gateway as Tier-1 security infrastructure: it holds every provider credential and sees every prompt [AJ].
- Install from pinned, verified artefacts. LiteLLM's images on GHCR are cosign-signed from v1.83.0 [VF: A6-S051, A6-S009]; verify signatures at admission and mirror packages internally [Rec].
- Configure fail-closed behaviour explicitly. LiteLLM limits are unset by default, `max_budget` fails open without a database, prompt-injection guardrails are off by default, and the proxy admin key bypasses budget checks [VF: A6-S015]. Its A2A agents are open to all callers until an allowlist is defined [VF: A6-S015]. Set allowlists before enabling A2A [Rec].
- Never forward a caller's token to an upstream MCP server; exchange it [VF: A6-S033, A6-S034] [Rec].
- Treat the semantic cache as attack surface and a confidentiality boundary. Apigee shipped an SSRF fix in its semantic-cache lookup on 30 September 2026 [VF: A6-S025]. Partition caches by tenant and turn them off for client-specific routes [Rec].

**Scalability and resilience**

- The gateway is on the critical path of every AI-dependent service. Run at least two independent deployments and decide in advance whether a gateway outage degrades to "no AI" (preferred for regulated outputs) or to a direct path (never, for client data) [Rec].
- Make fallback lists residency-aware and qualification-aware. A fallback model must be in the same approved region and must have passed the route's L9 regression suite [Rec]. OpenRouter's in-region routing shows the right behaviour: it fails rather than falling back out of region [VF: A4-S109, A4-S150].
- Multi-instance rate limits and budgets need shared state (database plus Redis or Valkey in LiteLLM's case) [VF: A6-S015]; test what happens when that state is lost [Rec].

**Governance**

- Routing rules, model allowlists and budgets are production configuration. Keep them in C5 under change control with approval for any change to a regulated route [Rec].
- Log policy decisions as well as requests: AgentCore Policy logs decisions to CloudWatch [VF: A6-S026]; LiteLLM Enterprise logs changes to keys, teams, users and models [VF: A6-S007].

**Observability and cost**

- Emit OTel GenAI spans and reconcile request counts with L9 traces and provider invoices [AJ].
- Tag every request with workflow, team and business object so C6 can attribute cost per task [VF: A7-S010] [AJ].
- Watch log costs: Cloudflare changed AI Gateway log pricing for gateways created from 24 September 2026 and announced per-GB pricing from 1 December 2026 [VF: A6-S052, V2-S074].

**Portability**

- Standardise applications on the OpenAI-compatible request format and one MCP endpoint, and keep provider-specific features behind route configuration [AJ].
- Policies written in a proprietary dialect (APIM XML, Apigee policies) are part of the exit cost [VF: A6-S053, A6-S024]; document their intent so they can be re-expressed [Rec].

**Patterns [AJ]:** one gateway of record with two deployments; residency-constrained, qualification-checked fallback; fail-closed budgets; per-caller MCP tool exposure with token exchange; gateway as the only holder of provider keys; routing config in Git; three-way reconciliation of gateway, trace and invoice.

**Anti-patterns [AJ]:** provider SDKs and keys in application code; "fallback to anything available"; semantic cache across tenants or clients; a SaaS gateway in the data path for client data without verified log residency; unpinned `pip install` of the gateway; one gateway instance as an unmonitored single point of failure; guardrails configured but off by default; a "god gateway" that also hosts agent logic.

### C1.6 Product selection criteria

| Scorecard criterion | What to evaluate in this control [AJ] |
|---|---|
| Technical (15% FS) | Provider breadth; routing, fallback, load balancing, circuit breaking; token-aware limits and budgets per key/team/user; semantic cache with partitioning; inline guard hooks before and after the call; MCP federation with per-caller tool exposure and token exchange; A2A; OTel output |
| Enterprise readiness (15%) | SSO, RBAC and audit of configuration changes; SCIM; admin API; SLA; multi-team tenancy; which of these are licence-gated |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 naming the gateway; CMK; supply-chain hygiene (signed images, release process) for self-hosted; fail-closed defaults |
| Deployment flexibility (15%) | Self-hosted or customer-run data plane so prompts and logs stay in region; hybrid; multi-region |
| Ecosystem (5%) | OpenAI-compatible API, MCP and A2A support, OTel export, integration with the firm's API gateway |
| Reliability and maturity (10%) | GA status of the AI-specific features (several are preview); configuration-model stability; incident history |
| Cost / TCO (5%) | Licence model (per capacity vs per call vs fee on spend); log pricing; operations burden (database, Redis) |
| Lock-in / portability (15%) | Open-source core; policy dialect; ownership stability; whether billing runs through the gateway vendor |

### C1.7 Product deep dives

**MCP disclosure.** MCP originated at Anthropic, and this author is an Anthropic model. The recommendation in this section is to govern whatever tool and agent protocols the estate uses (MCP, A2A or OpenAPI), and every product scored as Strategic supports more than one: LiteLLM, Kong, Apigee and Azure APIM govern MCP and A2A as well as model traffic, and AgentCore Gateway exposes MCP while accepting OpenAPI and Smithy targets [VF: A6-S015, A6-S016, A6-S024, A6-S020, A6-S053, A6-S021] [AJ].

**LiteLLM (BerriAI).**
- *What it is now:* an open-core Python SDK and proxy exposing 100+ providers through an OpenAI-format API, with virtual keys, budgets per key, user, team and customer, TPM/RPM limits, fallbacks, exact and semantic caching, guardrail hooks and logging callbacks. The same proxy fronts MCP servers and A2A agents [VF: A6-S015, A6-S051]. litellm 1.104.1 was published on 7 October 2026, with the proprietary litellm-enterprise 0.1.74 on the same day [VF: A6-S001, A6-S002, V2-S028]. No acquisition was found [VF: A6-S001].
- *Supply-chain incident:* on 24 March 2026, malicious versions 1.82.7 and 1.82.8 were published to PyPI using release credentials stolen through a compromised Trivy scanner in CI. LiteLLM says they were quarantined after about 40 minutes; Snyk reports an exposure window of about three hours. Both versions are no longer listed [VF: A6-S008, A6-S010, V2-S027, V2-S028]. v1.83.0 was the first build from a rebuilt CI/CD pipeline after forensic review with Mandiant and Veria Labs; PyPI shows the upload at 31 March 2026, 05:08 UTC [VF: A6-S009, V2-S028]. The intrusion vector is reported differently by different sources, and the "TeamPCP" attribution is a claim of responsibility, not an established finding [VF: V2-S027].
- *Certifications and access:* a SOC 2 Type 2 report was refreshed in September 2026; ISO 27001 recertification is announced but not confirmed [VF: A6-S108]. Admin-UI SSO is free up to five users; RBAC, SCIM and audit logs of key, team, user and model changes are Enterprise features [VF: A6-S007].
- *Strengths:* the widest provider coverage and the de facto open-source gateway; AWS's own multi-provider Guidance is built on it [VF: A6-S015, A6-S022] [AJ].
- *Limitations:* fail-open and off-by-default controls (listed in C1.5) [VF: A6-S015]; the pricing model is described inconsistently (capacity-based licence vs usage-based) [VF: A6-S007]; the release supply chain has already been compromised once [VF: A6-S008].
- *Choose when:* you want a self-hosted, provider-neutral gateway for LLM, MCP and A2A traffic and will run it as hardened internal infrastructure [AJ].
- *Avoid when:* you cannot pin, mirror and verify artefacts, or would run the open edition without a database [AJ].
- *Competitors:* Kong AI Gateway, Portkey, agentgateway.
- *FS note:* the incident is a C7 lesson as much as a C1 one: install from a private mirror with hash pinning, deploy only signed images, buy Enterprise for audit evidence, and include the gateway in the software bill of materials [Rec].
- **Tier: Strategic, conditional: only as a hardened, pinned, Enterprise-licensed internal service; security and maturity score 3 because of the March 2026 compromise and the fail-open defaults [AJ]. Flag: none.**

**Portkey, now Prisma AIRS AI Gateway (Palo Alto Networks).**
- *What it is now:* a gateway routing to 1,600+ models with fallbacks, retries, load balancing, timeouts, caching, budgets, guardrails and logging, plus an MCP Gateway with a single auth layer [VF: A6-S049]. The documentation is retitled "Portkey (Prisma AIRS AI Gateway)" [VF: A6-S014].
- *Ownership:* Palo Alto Networks completed the acquisition on 29 May 2026; its FY2026 10-K gives total consideration of US$117m [VF: A6-S012, V2-S025]. The announcement is dated 30 April 2026 in Stage A; one outlet dates it 2 June, so treat the announcement date as unconfirmed [VF: V2-S025]. Palo Alto bought it to place a gateway "in the traffic path" of Prisma AIRS [VF: A6-S011]; Prisma AIRS AI Gateway reached GA on 16 July 2026 [VF: V2-S048].
- *Open source and deployment:* the MIT gateway is moving to a pre-release Gateway 2.0 that merges the enterprise gateway into open source [VF: A6-S049, A6-S050]. Enterprise offers VPC and private-cloud hosting; fully air-gapped deployment is listed as "No Longer Offered" [VF: A6-S013].
- *Access control:* SSO/SAML 2.0 (Okta, Azure AD), SCIM, organisation Owner/Admin and workspace Manager/Member roles, and organisation-wide audit logs tied to users and timestamps [VF: B-C1-S001, B-C1-S002]. IdP groups map to workspaces and roles [VF: B-C1-S003]. Much of this evidence is marketing pages.
- *Certifications:* SOC 2 Type 2, ISO 27001, GDPR and HIPAA are claimed on pricing pages with unclear tier coverage [VF: A6-S013].
- *Strengths:* mature routing configuration with guardrails in the same config [VF: A6-S049] [AJ].
- *Limitations:* the roadmap now belongs to a security platform; post-acquisition pricing is not verified and the published price page may be stale [VF: A6-S011, A6-S013].
- *Choose when:* you already run Prisma AIRS and want gateway and runtime inspection from one vendor [AJ].
- *Avoid when:* you want vendor-neutral governance of the traffic path, or need air-gap [AJ].
- *Competitors:* LiteLLM, Kong, Cloudflare.
- *FS note:* refresh due diligence and the DORA register entry after the change of control; confirm which certificates cover the Prisma AIRS-branded service [Rec].
- **Tier: Tactical. Flags: Acquired, Renamed.**

**Kong AI Gateway (Kong Inc.).**
- *What it is now:* AI Gateway 2.0 became GA on 1 September 2026 as a dedicated runtime in Konnect with its own control plane, admin API and release cadence; 2.1.0 followed on 22 September and 2.2.0 on 30 September 2026 [VF: A6-S016, A6-S017, V2-S034]. The AI plugins remain on Kong Gateway 3.14 LTS, and Kong recommends migrating before 3.18 [VF: A6-S017].
- *Capabilities:* multi-provider routing and load balancing, token budgets and rate limits, semantic caching, semantic prompt and response guards, PII sanitisation, AWS/Azure/GCP guardrail services, NVIDIA NeMo Guardrails, MCP access control and tool filtering, MCP Server Bundling with per-caller tool exposure, principal-aware policies via Kong Identity, and A2A traffic management [VF: A6-S016, A6-S017]. 2.1.0 supports MCP revision 2026-07-28 [VF: A6-S017].
- *Certifications and deployment:* ISO/IEC 27001:2022 covering the API and AI Connectivity Platform, and SOC 2 Type II covering Kong AI Gateway among others [VF: A6-S109]. Deployment: Konnect SaaS, Dedicated Cloud Gateways, hybrid (customer data plane) and self-managed [VF: A6-S018]. A 99.99% Konnect SLA is advertised [VF: A6-S018]. Konnect supports organisation SSO with SAML or OIDC, teams with predefined roles, and mapping of IdP groups to teams [VF: B-REVA-S004].
- *Strengths:* the broadest AI policy set built on an enterprise API gateway, with certifications that name the product [AJ].
- *Limitations:* the configuration model changed from plugins to entities [VF: A6-S016]; advanced AI plugins and the 2.x runtime are licence-gated or Konnect-delivered [VF: A6-S017]; pricing is not published [VF: A6-S018].
- *Choose when:* Kong is already your API gateway [AJ].
- *Avoid when:* you want a free self-hosted gateway with no licence dependency [AJ].
- *Competitors:* LiteLLM, Apigee, Azure API Management.
- *FS note:* use hybrid mode so prompts and logs stay in your region, and plan the 3.x-to-2.x migration as a regulated change [Rec].
- **Tier: Strategic, conditional: where Kong is the API standard; cost scores 2 because pricing is not public [AJ]. Flag: none.**

**Cloudflare AI Gateway (Cloudflare, Inc.).**
- *What it is now:* a managed edge proxy for AI provider calls with analytics, caching, rate limiting, logging, guardrails, DLP scanning, dynamic routing and fallback, spend limits and Unified Billing [VF: A6-S019, A6-S052]. 2026 additions include spend limits (June), identity-based controls via Cloudflare Access (August) and Unified Billing changes (1 September) [VF: A6-S019]. Cloudflare positions it as an "AI Application Control Plane" [VF: A6-S019].
- *Guardrails and DLP:* guardrails run `@cf/meta/llama-guard-3-8b` on Workers AI and are billed as inference; two DLP profiles are free, with full profiles via Zero Trust DLP [VF: A6-S052].
- *Pricing:* core features free; 5% fee on Unified Billing credits; log pricing changed for gateways created from 24 September 2026, and per-GB pricing is announced from 1 December 2026 (US$0.25 per GB ingested and US$0.10 per GB-month after allowances) [VF: A6-S052, V2-S074].
- *Certifications:* SOC 2 Type II names AI Gateway in scope; ISO 27001:2022 is platform-wide without naming it [VF: A6-S110]. EU transfers rely on the Data Privacy Framework with SCCs as fallback; AI Gateway-specific localisation is not verified [VF: A6-S110].
- *Strengths:* lowest-friction adoption and free core controls [AJ].
- *Limitations:* managed only, no self-hosting [VF: A6-S052]; MCP and A2A governance not evidenced [NPV]; Cloudflare says some future features may be premium [VF: A6-S052].
- *Choose when:* you run Cloudflare Zero Trust and want visibility and spend limits for non-confidential workloads [AJ].
- *Avoid when:* prompts contain client data and log localisation is unconfirmed [AJ].
- *Competitors:* Portkey, LiteLLM, OpenRouter (L2).
- *FS note:* prefer BYOK to Unified Billing so the provider contract stays direct [Rec].
- **Tier: Tactical. Flag: none.**

**AI gateway in Azure API Management (Microsoft).**
- *What it is now:* AI gateway policies across existing APIM tiers, plus a dedicated AI Gateway tier in public preview [VF: A6-S053, A6-S020]. Microsoft describes the gateway as an extension of the existing API gateway, "not a separate offering" [VF: A6-S053].
- *GA policies:* `llm-token-limit`, `llm-emit-metric`, semantic caching and `llm-content-safety` [VF: A6-S020, A6-S053]. Content safety now covers MCP tool-call arguments and A2A payloads, with a Prompt Shields option [VF: A6-S020]. Other capabilities: load balancing and circuit breaking, exposing REST APIs as MCP servers, governing existing MCP servers, and OAuth via the credential manager [VF: A6-S053].
- *Preview:* the AI Gateway tier is limited to East US 2 and Sweden Central, free during preview, with no SLA [VF: A6-S020, V2-S073]. The unified OpenAI-compatible model API is also preview [VF: A6-S053]. Microsoft Foundry is integrating the gateway as its AI gateway control plane (preview) [VF: A6-S020].
- *Certifications:* API Management is in Azure's FedRAMP High and DoD IL2 audit scope [VF: A6-S056]. Azure's ISO 27001 and SOC 2 attestations are stated at platform level without naming the service [VF: B-C1-S007, B-C1-S008].
- *Strengths:* content-safety enforcement on tool and agent traffic at the gateway [VF: A6-S020] [AJ].
- *Limitations:* APIM-specific policy XML [VF: A6-S053]; classic tier pricing not verified [NPV].
- *Choose when:* Azure is primary and APIM is your API standard [AJ].
- *Avoid when:* you would put regulated traffic on the preview tier [AJ].
- *Competitors:* Apigee, Kong, LiteLLM.
- *FS note:* use the GA policies in existing tiers in UK or EU regions; keep a written statement of each policy's intent for exit [Rec].
- **Tier: Strategic, conditional: where Azure is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. Flag: none.** It is Azure's lead AI gateway. The condition covers the GA AI gateway policies in existing APIM tiers only; the preview AI Gateway tier (no SLA) stays off regulated traffic until it is GA. Lock-in at 2 is accepted under rule 11 because the condition is an existing platform commitment [AJ].

**AWS: Amazon Bedrock AgentCore Gateway (Amazon Web Services).**
- *What AWS actually offers:* no AWS product named "AI gateway" was found [AJ]. AWS offers (a) AgentCore Gateway, GA in October 2025 as an MCP gateway [VF: A6-S021]; (b) a LiteLLM-based reference architecture, the Guidance for Multi-Provider Generative AI Gateway on AWS [VF: A6-S022]; and (c) Bedrock cross-region inference for resilience [VF: A6-S022].
- *What it is now:* AgentCore Gateway turns OpenAPI and Smithy APIs, Lambda functions and existing MCP servers into MCP tools behind one endpoint, with IAM or custom-JWT inbound auth, outbound credentials via AgentCore Identity, semantic tool search, REQUEST and RESPONSE interceptors and policy enforcement [VF: A6-S021, A6-S074]. Its API now also has inference targets that route to LLM providers through an `/inference` path, with token-aware rate limits scoped by JWT claims, IAM identity and model [VF: A6-S105]. Token-based rate limiting was announced on 6 August 2026 [VF: A6-S106].
- *Policy:* AgentCore Policy reached GA on 3 March 2026 in 13 regions including Europe (Ireland). It is deny-by-default for gateway tool calls, uses identity claims and tool arguments, and logs decisions to CloudWatch [VF: A6-S026, V2-S033]. Policies are now authored in Dogwood, an open-source superset of Cedar [VF: V2-S033].
- *Certifications:* AgentCore is in scope for SOC 1, 2 and 3 (release note, July 2026) and listed on AWS's SOC services-in-scope page [VF: B-C1-S004, B-C1-S005]. It achieved ISO and CSA STAR compliance in February 2026, and the FAQ lists ISO/IEC 27001 among the assessed programmes [VF: B-C1-S004, B-C1-S006]. FedRAMP status conflicts between pages [VF: B-C1-S004, B-C1-S006]. A customer-managed KMS key is supported for the token vault [VF: A6-S074].
- *Strengths:* the strongest policy model for tool calls in this control [AJ].
- *Limitations:* no explicit GA statement or regional list was found for inference targets, and the docs conflict on multi-target selection (round-robin vs random) [VF: A6-S105]; the API surface is moving fast (171 control-plane operations) [VF: A6-S074].
- *Choose when:* you run agents on AWS and need governed MCP tool access [AJ].
- *Avoid when:* you need it as your multi-provider model gateway today [AJ].
- *Competitors:* LiteLLM (also AWS's own Guidance pattern), Kong, agentgateway.
- *FS note:* use it for tool traffic; keep model routing on a gateway with GA inference routing until AWS states GA and regions [Rec].
- **Tier: Strategic, conditional: where AWS is your primary cloud (CP3 Q2, rubric rule 10), as the gateway for MCP and tool traffic [AJ]. Flag: none.** Maturity 2 is a stated condition: it is not the model gateway of record until AWS states GA and Regions for inference targets. The same service has the same tier in L4 (`L4-aws-agentcore-gateway-identity`) [AJ].

**Apigee as an AI gateway (Google Cloud).**
- *What it is now:* Apigee is marketed as the AI gateway for agentic AI, with SSE and JSON-RPC support for MCP, A2A and AP2, multicloud model routing, MCP servers and transcoding, and Model Armor integration [VF: A6-S024]. Capabilities include token limit enforcement and monitoring, semantic caching, routing with circuit breaking, LLM auditing and logging, and API key, OAuth 2.0 and JWT [VF: A6-S024, A6-S023]. Apigee MCP support was GA on 31 March 2026, and the API hub MCP server on 24 July 2026 [VF: A6-S023, A6-S025]. An extension processor applies policies to traffic that bypasses a proxy [VF: A6-S023, A6-S025].
- *Deployment and releases:* Apigee X (SaaS) and Apigee hybrid 1.17, with 1.17.1 on 30 September 2026 fixing an SSRF issue in `SemanticCacheLookup` [VF: A6-S025, A6-S069].
- *Certifications:* Apigee is listed in Google Cloud's SOC 2 and ISO/IEC 27001 scope [VF: A6-S070, A6-S071].
- *Pricing:* pay-as-you-go per call (Standard proxy US$20 and Extensible proxy US$100 per 1M calls up to 50M), plus add-ons for analytics (US$20 per 1M) and Advanced API Security (US$350 per 1M), as of 7 October 2026 [VF: A6-S069].
- *Context:* Google renamed Vertex AI to Gemini Enterprise Agent Platform in April 2026 [VF: V2-S037].
- *Strengths:* a mature API-management product with product-scoped certifications and a customer-run data plane option [AJ].
- *Limitations:* a proprietary policy model [VF: A6-S024]; add-on pricing can dominate at volume [AJ].
- *Choose when:* Google Cloud or Apigee is your standard [AJ].
- *Avoid when:* you want a light model gateway without an API-management estate [AJ].
- *Competitors:* Azure API Management, Kong, LiteLLM.
- *FS note:* run hybrid in a UK or EU region and confirm where LLM audit logs are stored [Rec].
- **Tier: Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10) or Apigee is already the API standard; lock-in scores 2 [AJ]. Flag: none.**

**agentgateway (Linux Foundation project).**
- *What it is now:* an open-source proxy for agent-to-LLM, agent-to-tool and agent-to-agent traffic: OpenAI-compatible LLM routing with budget and spend controls, load balancing and failover; MCP tool federation over stdio, HTTP, SSE and Streamable HTTP with OAuth; and an A2A gateway [VF: A6-S061]. Apache-2.0; v1.6.0 was released on 2 October 2026 [VF: A6-S061, A6-S062, V2-S061].
- *Governance and support:* Solo.io started it and contributed it to the Linux Foundation, which accepted it on 25 August 2025; contributors include AWS, Cisco, IBM, Microsoft and Red Hat [VF: B-C1-S009]. Later sources place it in the Agentic AI Foundation under the Linux Foundation, so the current home is reported inconsistently [VF: B-C1-S009]. Solo sells an enterprise distribution, announced 15 October 2025 [VF: B-C1-S010].
- *Strengths:* the most neutral governance of any gateway here, covering all three traffic types [AJ].
- *Limitations:* security policy, release signing, access-control detail and adoption are not verified [NPV].
- *Choose when:* you want a neutral open-source gateway for MCP and A2A in a Kubernetes estate [AJ].
- *Avoid when:* you need certified SaaS or mature cost attribution today [AJ].
- *Competitors:* LiteLLM, Agent Router, Kong.
- *FS note:* pilot it for MCP and A2A traffic with commercial support, and verify its CVE process before production [Rec].
- **Tier: Tactical. Flag: none.**

**Agent Router, formerly Envoy AI Gateway (Agentic AI Foundation).**
- *What it is now:* one OpenAI-compatible API for hosted and self-hosted models and MCP servers. Platform teams centralise credentials, routing, quotas, failover and usage attribution, enforced by Envoy Proxy and Envoy Gateway [VF: A6-S063]. v1.2.0 was released on 6 October 2026 [VF: A6-S064, V2-S061].
- *Rename:* in 2026 the project was renamed Agent Router and moved to the Agentic AI Foundation; the repository moved, but CRDs, the `aigw` CLI, images and the Go module path are unchanged [VF: A6-S063, V2-S029].
- *Strengths:* fits platforms that already run Envoy Gateway; usage attribution suits chargeback [VF: A6-S063] [AJ].
- *Limitations:* Kubernetes required [VF: A6-S063]; access control, security features and hygiene not verified [NPV].
- *Choose when:* your platform team runs Envoy Gateway [AJ].
- *Avoid when:* you need guardrails or caching inside the gateway [AJ].
- *Competitors:* agentgateway, LiteLLM, Kong.
- *FS note:* pair with a separate guardrail service and log store, and record the rename in the software inventory [Rec].
- **Tier: Tactical. Flag: Renamed.**

### C1.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C1-litellm | 5 | 4 | 3 | 4 | 5 | 3 | 4 | 4 | 4.05 | 3.90 | Strategic |
| C1-portkey | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3.60 | 3.50 | Tactical |
| C1-kong-ai-gateway | 5 | 4 | 4 | 4 | 4 | 3 | 2 | 3 | 3.85 | 3.80 | Strategic |
| C1-cloudflare-ai-gateway | 3 | 3 | 3 | 2 | 4 | 3 | 4 | 2 | 3.00 | 2.80 | Tactical |
| C1-azure-apim-ai-gateway | 4 | 4 | 4 | 2 | 4 | 3 | 3 | 2 | 3.40 | 3.25 | Strategic |
| C1-aws-agentcore-gateway | 3 | 4 | 4 | 2 | 3 | 2 | 4 | 2 | 3.10 | 3.00 | Strategic |
| C1-google-apigee-ai-gateway | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 3.80 | 3.65 | Strategic |
| C1-agentgateway | 4 | 3 | 2 | 4 | 3 | 3 | 4 | 5 | 3.40 | 3.45 | Tactical |
| C1-envoy-ai-gateway | 3 | 2 | 2 | 3 | 3 | 3 | 4 | 5 | 2.90 | 3.00 | Tactical |

**Scoring notes [AJ]:**
- *Hyperscaler presumption (CP2 Q1).* Azure APIM, AgentCore Gateway and Apigee score 4 on enterprise readiness: platform controls presumed (CP2 Q1); confirm per service.
- *NPV caps and rule 7.* Cloudflare's cap was lifted to 3 on its verified identity-based controls. At the CP3 review two scores rose to 4, because rule 7 gives 4 for all three of SSO, RBAC and audit logs plus SCIM, an SLA or an admin API (as for Firecrawl in L8 and LiteLLM here): Kong, now that Konnect SSO and teams-based roles are verified [VF: B-REVA-S004] alongside its audit logs and 99.99% SLA; and Portkey, whose SSO, SCIM, roles and audit logs the writer evidenced (B-C1-S001 to S003). Portkey's condition is stated: much of the evidence is vendor pages, and post-acquisition terms are not public.
- *Scope rule (CP2 Q4).* Azure APIM's ISO 27001 and SOC 2 are platform-level without naming the service, but FedRAMP High names it, so security is 4. Portkey's certification tier coverage is unclear, so 3. AgentCore is held at 4 rather than 5 because its ISO evidence is a partly garbled search extract and FedRAMP status conflicts.
- *Rule 2 (self-hosted open source).* LiteLLM, agentgateway and Agent Router are scored as software you run. LiteLLM and agentgateway have commercial support, so the cap at 4 does not bind; agentgateway's and Agent Router's security is 2 because their release hygiene is not verified.
- *Rule 3 (ownership change).* Portkey's lock-in is reduced by 1 (MIT core, but not neutral governance).
- *Strategic despite weaknesses.* LiteLLM is Strategic with security and maturity at 3 because of the March 2026 compromise; the condition is stated in its deep dive. Kong (cost 2) and Apigee (lock-in 2) are Strategic only where they are already the API standard.
- *Hyperscaler lead services (CP3 Q2, rubric rule 10).* Azure APIM's AI gateway (FS 3.25) and AWS AgentCore Gateway (FS 3.00) are now Strategic, conditional: "where Azure (or AWS) is your primary cloud", as each cloud's lead service in this category with no criterion at 1. Apigee's condition was reworded to match. No criterion scores changed, and security stays at 4 under rule 8. The conditions carry the weaknesses: APIM on GA policies only, not the preview tier; AgentCore for tool traffic only until its inference targets are GA (maturity 2).
- *Calibration.* Every product scores 2 or below on at least one criterion except LiteLLM and Portkey, whose weakest points (security and maturity at 3) are stated.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| LiteLLM | MIT core; litellm-enterprise proprietary [VF: A6-S001, A6-S002] | Self-host, customer VPC, hosted [VF: A6-S007, A6-S022, A6-S051] | SOC 2 Type 2 (Sep 2026); ISO 27001 unconfirmed [VF: A6-S108] | In-estate when self-hosted [AJ]; hosted region NPV | BerriAI; no acquisition found [VF: A6-S001] |
| Portkey / Prisma AIRS AI Gateway | MIT gateway; platform proprietary [VF: A6-S050, A6-S013] | SaaS, VPC, private cloud, self-host; no air-gap [VF: A6-S013, A6-S049] | SOC 2 Type 2, ISO 27001, HIPAA claimed; tier coverage unclear [VF: A6-S013] | EU processing region NPV [VF: A6-S013] | Palo Alto Networks, completed 29 May 2026 (US$117m, 10-K) [VF: A6-S012, V2-S025] |
| Kong AI Gateway | Apache-2.0 OSS core; AI Gateway 2.x and advanced plugins licensed [VF: A6-S017] | Konnect SaaS, dedicated cloud, hybrid, self-managed [VF: A6-S018] | ISO 27001:2022 and SOC 2 Type II naming AI Gateway [VF: A6-S109] | Hybrid data plane in region [VF: A6-S018]; Konnect region NPV | Kong Inc., independent [VF: A6-S016] |
| Cloudflare AI Gateway | Proprietary [VF: A6-S052] | SaaS only [VF: A6-S052] | SOC 2 Type II naming AI Gateway; ISO 27001 platform-wide [VF: A6-S110] | Product-specific localisation NPV [VF: A6-S110] | Cloudflare, Inc. [VF: A6-S052] |
| Azure APIM AI gateway | Proprietary [VF: A6-S053] | Managed Azure; AI Gateway tier preview in 2 regions [VF: A6-S020] | FedRAMP High scope [VF: A6-S056]; ISO/SOC 2 platform-level [VF: B-C1-S007, B-C1-S008] | Sweden Central for the preview tier [VF: A6-S020] | Microsoft |
| AWS AgentCore Gateway | Proprietary [VF: A6-S021] | Managed AWS [VF: A6-S021] | SOC 1/2/3, ISO (Feb 2026) [VF: B-C1-S004, B-C1-S006] | Policy GA incl. Ireland; Gateway regions NPV [VF: A6-S026] | Amazon Web Services |
| Apigee | Proprietary; hybrid runtime self-managed [VF: A6-S069] | SaaS, hybrid [VF: A6-S069, A6-S025] | SOC 2 and ISO 27001 scope [VF: A6-S070, A6-S071] | Hybrid in region [AJ]; SaaS region NPV | Google Cloud |
| agentgateway | Apache-2.0 [VF: A6-S061] | Self-host [VF: A6-S061] | Not applicable (software) | In-estate [AJ] | Linux Foundation (AAIF per later sources) [VF: B-C1-S009] |
| Agent Router | Apache-2.0 [VF: A6-S063] | Self-host on Kubernetes [VF: A6-S063] | Not applicable (software) | In-estate [AJ] | Agentic AI Foundation [VF: A6-S063] |

### C1.9 Decision tree

![C1 decision tree: choosing the gateway of record](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/C1-2.png){height=8.8in}

*Figure: Fix one gateway of record first, then pick the product by data residency and existing API gateway, add tool and agent routing, and pass the go-live checks. Editable source: `08_Graphic/diagrams/C1-2.md`.* [AJ]

### C1.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Application-to-gateway API | **Acceptable** on the OpenAI-compatible format | Every product here exposes or accepts it [VF: A6-S015, A6-S049, A6-S053, A6-S061, A6-S063] | One client library; no provider SDKs in application code |
| Gateway product | **Manageable** | Replaceable if routes, budgets and policies are documented as data | Routing config in Git (C5); policy intent written down |
| Proprietary policy dialects (APIM XML, Apigee policies, Kong entities) | **Manageable, with cost** | Re-expressing policies is the main switching effort [VF: A6-S053, A6-S024, A6-S016] | Keep policy logic thin; push detection into C2/C3 services callable from any gateway |
| Billing through the gateway vendor (Unified Billing, platform fees) | **Unacceptable for regulated workloads** | It puts the vendor between the firm and its model contract [VF: A6-S052, A4-S144] | BYOK; direct provider contracts |
| SaaS gateway in the data path for client data | **Unacceptable unless log residency is verified** | Prompts and logs leave the estate [AJ] | Self-hosted or hybrid data plane |
| Model provider behind the gateway | **Acceptable** once a qualified alternative exists | The gateway plus the L9 regression suite is the exit route [AJ] | Tested switch drill |

### C1.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23.* PRA SS1/23 covers vendor models and requires ongoing performance monitoring [VF: R-PRA-SS123, A8-S008]. The gateway is where model-version changes become visible: a provider's silent model update or a fallback event is a change to the "model" that monitoring must detect [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001, A8-S002]. The firm's own governance must therefore define which routing changes need re-validation [AJ].
- *Inventory.* Treat each route (purpose, model, fallback, region) as an inventory item linked to C8, not just each model [Rec].

**EU AI Act.**
- *Deployer logging.* Article 26 requires deployers of high-risk systems to keep logs for at least six months, folded into financial-services documentation for financial institutions [VF: R-EUAIA, A8-S011]. Annex III duties apply from 2 December 2027 [VF: R-EU-OMNIBUS-AI, A8-S011].
- *Gateway logs as evidence.* The gateway is the one place that sees every request with its model version, so its logs are the natural Article 26 evidence base, joined to L9 traces [AJ]. Most asset-management uses are not Annex III, but the same logs serve MRM and outsourcing evidence [AJ].

**DORA, UK CTP and outsourcing.**
- *Third-party registers.* Under DORA, every ICT third-party arrangement belongs in the register of information, with Article 30 terms and exit strategies for critical or important functions [VF: R-DORA, A8-S021]. A SaaS gateway (Cloudflare, Portkey SaaS) is such an arrangement [AJ].
- *Designations.* The DORA CTPP list and the UK CTP designations include AWS, Google Cloud and Microsoft, and no AI model provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. Hyperscaler gateways therefore sit under designated providers; direct model APIs do not [AJ].
- *Exit planning.* SS2/21 expects documented, tested exit plans, including stressed exit [VF: R-PRA-SS221, A8-S048]. The regulatory fact base's own assessment of SS2/21 names the gateway, portable prompts and evaluation suites as the exit route [AJ]. The gateway is what makes a model exit a configuration change rather than a code programme; an exit plan that has never been drilled through the gateway is not tested [AJ].
- *Notification lead time.* PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. Adding a new model provider behind the gateway may itself be such an arrangement, so the gateway's "add provider" change must route through third-party risk [Rec].
- *Effective access.* FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049]; that applies to gateway logs held by a vendor [AJ].

**Resilience: the gateway as a single point of failure.** Concentrating every AI call in one component improves control and worsens resilience [AJ]. The answer is not to remove the gateway but to deploy it like payments infrastructure: two independent deployments, tested failover, a defined degraded mode, and an incident classification under DORA's ICT incident regime [VF: R-DORA, A8-S021] [Rec].

**Residency and transfers.** EU-to-US transfers rely on the Data Privacy Framework or SCCs, and the C-703/25 P appeal is pending [VF: R-DATA-TRANSFERS, A8-S053]. Processing location is already a priced API control on at least one first-party model API [VF: A8-S036]; OpenRouter offers EU/US in-region routing on higher plans [VF: A4-S109]. The gateway is where region pinning is enforced and evidenced per request [AJ]. Gateway logs are themselves personal data and must stay in region [Rec].

**Concentration and ownership.** Palo Alto Networks now owns both Portkey and Protect AI within Prisma AIRS [VF: A7-S014, A7-S016]. Stripe has agreed to acquire OpenRouter, with closing pending as of 8 October 2026 [VF: V1-S059, V1-S060]. IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. A gateway owned by a model vendor, a payments company or a security vendor is not neutral; that matters most for the component meant to keep you neutral [AJ].

**Security standards.**
- *OWASP.* The OWASP Top 10 for LLM Applications 2026 (released August–September 2026) is the operative list [VF: R-OWASP-LLM, V2-S056]; its full 2026 list was not retrieved. For traceability, the 2025 identifiers the gateway most directly addresses are LLM10 Unbounded Consumption (limits and budgets), LLM02 Sensitive Information Disclosure (DLP hooks) and LLM03 Supply Chain [R: A8-S040]. The Top 10 for Agentic Applications for 2026 starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042]; per-caller tool exposure at the gateway limits what a hijacked agent can reach [AJ].
- *NIST and ISO.* NIST AI 600-1 and ISO/IEC 42001 provide the control taxonomy and management-system wrapper [VF: R-NIST-AIRMF, A8-S044; R-ISO-42001, A8-S045].
- *ESMA.* ESMA expects ex-ante input controls and frequent ex-post output controls [VF: R-INTL-AI-ASSETMGMT, A8-S059]; the gateway is where both are invoked [AJ].

### C1.12 Worked-example slice (POV 3)

**What the commentary agent needs from C1 [AJ].** The deterministic workflow drafts the monthly Brinson-style attribution commentary (allocation, selection, currency) for a generic multi-asset fund. Every model call it makes goes through the gateway:
1. **One route, one identity.** The workflow calls a named route, `attribution-commentary-draft`, with its workload identity (C4). It never holds a provider key.
2. **Model routing with a residency constraint.** The route's primary model is served from an approved UK or EU region. The route will not send data anywhere else, even under load.
3. **A qualified fallback model.** The fallback is a different provider in the same approved region, and it has passed the same L9 regression suite of past commentaries. If both are unavailable, the route fails closed and the analyst is told the draft is delayed; no unqualified model is tried.
4. **Per-commentary cost attribution.** Each request carries tags for fund, period, commentary ID and workflow version, so C6 reports cost per commentary and per fund.
5. **Inline guards.** Pre-call: DLP on client identifiers (C3) and a prompt-attack check on retrieved documents (C2). Post-call: the numeric-grounding guard (C2) before the draft reaches the reviewer.
6. **Tool access through the gateway's MCP endpoint.** The workflow sees only the read-only attribution-engine tool and the retrieval tool; write tools are not exposed to this caller.
7. **Evidence.** The request record (route, model and version, region, fallback flag, tokens, cost, guard outcomes, trace ID) goes to L9 and to the C8 evidence pack, retained under the records policy and in region.

**What C1 must never do [AJ]:**
- fall back to a model outside the approved region, or to one that has not passed the route's regression suite
- serve a cached draft or paragraph from another fund or period (semantic cache is off on this route)
- let budgets or guards fail open because a dependency is down
- forward the workflow's token to an upstream tool server
- accept a provider-side model version change without recording it and triggering re-qualification
- become the place where drafting logic or numbers are generated; it routes and records, it does not author

### C1.13 Baseline position and hypothesis view

| Baseline entry | Position at end of Q3 2026 | Recommended |
|---|---|---|
| **The control as a whole** | Gateways now carry LLM, MCP and A2A traffic [VF: A6-S015, A6-S016, A6-S053, A6-S024, A6-S061] | A control-plane component: one firm-controlled gateway of record, two deployments, fail-closed [Rec] |
| OpenRouter (L2) | Hosted router with gateway-style governance (budgets, allowlists, ZDR, EU/US routing); Stripe acquisition agreed, pending [VF: A4-S111, A4-S109, V1-S059] | A model-access source behind the firm's gateway, not the gateway itself [Rec] |
| LiteLLM | Open-core LLM+MCP+A2A gateway; PyPI compromise 24 March 2026, clean 1.83.0 [VF: A6-S015, A6-S008, A6-S009] | Strategic, conditional: hardened, pinned, Enterprise-licensed [Rec] |
| Portkey | Acquired by Palo Alto Networks; now Prisma AIRS AI Gateway [VF: A6-S012, A6-S014] | Tactical; for Prisma AIRS estates [Rec] |
| Kong AI Gateway | AI Gateway 2.0 GA 1 September 2026; 2.2 on 30 September [VF: A6-S016, V2-S034] | Strategic where Kong is the API standard [Rec] |
| Cloudflare AI Gateway | Free core, DLP, Llama Guard guardrails, Unified Billing, new log pricing [VF: A6-S052, V2-S074] | Tactical; non-confidential workloads, BYOK [Rec] |
| Azure APIM AI gateway | GA policies; AI Gateway tier preview with no SLA [VF: A6-S020, V2-S073] | Strategic, conditional: where Azure is your primary cloud (CP3 Q2); GA policies only, not the preview tier [Rec] |
| "AWS AI gateway" | No product by that name found; AgentCore Gateway (MCP + new inference targets) and a LiteLLM-based Guidance [VF: A6-S021, A6-S022, A6-S105] | Strategic, conditional: where AWS is your primary cloud (CP3 Q2), for MCP tool governance; model routing elsewhere until inference targets are GA [Rec] |
| Apigee | Marketed as an AI gateway; MCP GA 31 March 2026 [VF: A6-S024, A6-S023] | Strategic, conditional: where Google Cloud is your primary cloud or Apigee is the standard (CP3 Q2) [Rec] |
| agentgateway, Envoy AI Gateway | agentgateway v1.6.0 (open foundation); Envoy AI Gateway renamed Agent Router (AAIF) [VF: A6-S062, A6-S063] | Tactical; neutral options for Kubernetes estates [Rec] |

**H1 (split L2 into serving → optimisation → gateway/routing, and promote the gateway to the control plane). Provisional view; verdict in synthesis.**

The evidence supports promotion on four counts.

- **The traffic is no longer only model traffic.** LiteLLM describes one control plane for LLMs, MCP servers and A2A agents with shared auth, rate limiting and a usage dashboard [VF: A6-S015]. Kong, Azure APIM, Apigee and agentgateway govern all three [VF: A6-S016, A6-S020, A6-S024, A6-S061]. AWS's AgentCore Gateway grew from the opposite direction, from tools to models [VF: A6-S074, A6-S105].
- **Vendors describe it as a control plane.** Cloudflare calls its product an "AI Application Control Plane" [VF: A6-S019]; Microsoft Foundry is integrating APIM as its AI gateway control plane [VF: A6-S020]; Kong runs AI Gateway 2.x with its own control plane [VF: A6-S016].
- **It is where the other controls are invoked.** Guardrails (C2), DLP (C3), identity and tool policy (C4), and cost attribution (C6) all run inline at the gateway [VF: A6-S017, A6-S053, A6-S026, A7-S010].
- **Security vendors are buying it.** Palo Alto Networks bought Portkey to put a gateway "in the traffic path" [VF: A6-S011].

The counter-evidence is twofold. Microsoft says the AI gateway is an extension of the existing API gateway, "not a separate offering" [VF: A6-S053], and Kong and Apigee are API-management products [VF: A6-S016, A6-S024]: the AI gateway may converge into API management rather than stand alone [AJ]. And the March 2026 LiteLLM compromise shows the cost of concentrating control: the more the gateway does, the larger the blast radius when it fails [VF: A6-S008] [AJ].

**Provisional recommendation.** Split L2 into model serving, inference optimisation and model access [AJ]. Promote the gateway out of L2 into the control plane as C1, renamed "AI traffic gateway" to cover model, tool and agent calls, with C2, C3, C4 and C6 invoked through it [AJ]. Draw it as a logical control that may be implemented on the firm's API-management platform, not as a mandatory separate product [AJ]. Keep agent logic out of it [AJ]. **Provisional; verdict in synthesis.**
