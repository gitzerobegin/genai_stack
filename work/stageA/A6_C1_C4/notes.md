# Stage A, stream A6: controls C1 to C4 (gateway, guardrails, DLP/PII, agent identity and access)

As of 7 October 2026. These are control-plane records, so none of them appears in the graphic and `original_label` is `null` for all 26. Source IDs refer to `sources.csv` in this folder. The archive is at `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A6/`.

**Research-environment caveat.** The shared WebSearch budget ran out partway through C2. Searches had already covered C1 and part of C2. Everything after that came from hosts that could be fetched directly: raw GitHub (vendor documentation repositories such as MicrosoftDocs, cloudflare-docs and the modelcontextprotocol spec, plus project changelogs), PyPI, npm, the Go module proxy and cloud.google.com. All of these are primary sources. AWS, Okta/Auth0, Protegrity, Skyflow and Microsoft Purview product pages could not be reached, so those records have more "Not publicly verified" cells.

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| (not in graphic) LiteLLM | Open-core gateway. litellm 1.104.1 (MIT) plus the proprietary litellm-enterprise package. The proxy also acts as an MCP gateway and an A2A agent gateway. PyPI supply-chain compromise on 24 March 2026 (1.82.7/1.82.8); clean v1.83.0 released 30 March 2026. | No change | A6-S001, A6-S002, A6-S008, A6-S009, A6-S015 |
| (not in graphic) Portkey | Acquired by Palo Alto Networks: announced 30 April 2026, closed 29 May 2026, US$117m per the 10-K. Now branded "Prisma AIRS AI Gateway". The open-source gateway (MIT) is moving to Gateway 2.0. | Acquired | A6-S011, A6-S012, A6-S014, A6-S049 |
| (not in graphic) Kong AI Gateway | Kong AI Gateway 2.0 became GA on 1 September 2026 as a dedicated runtime in Konnect. The AI plugins stay on Kong Gateway 3.14 LTS, and Kong recommends migrating before 3.18. | No change | A6-S016, A6-S017 |
| (not in graphic) Cloudflare AI Gateway | Free core service. 2026 additions: spend limits, identity-based budgets, DLP, Llama Guard 3 8B guardrails, Unified Billing (5% fee), and new log pricing from 24 September 2026. | No change | A6-S019, A6-S052 |
| (not in graphic) Azure API Management AI gateway | Policies in existing tiers are GA. The dedicated "AI Gateway tier" is in public preview: East US 2 and Sweden Central only, free, no SLA. It covers LLM, MCP and A2A traffic. | No change | A6-S020, A6-S053 |
| (not in graphic) AWS "AI gateway" | AWS has no product by that name. Bedrock AgentCore Gateway (an MCP gateway, GA October 2025) now has LLM inference targets, token-aware rate limits and principal rules in its API model. AWS also publishes a LiteLLM-based Guidance pattern. | Not publicly verified (GA status of the inference targets) | A6-S021, A6-S022, A6-S074 |
| (not in graphic) Google Apigee AI gateway | Apigee is marketed as an AI gateway: token limits, semantic cache, Model Armor, MCP (GA 31 March 2026). Vertex AI has been renamed "Gemini Enterprise Agent Platform". | No change | A6-S023, A6-S024, A6-S025, A6-S070 |
| (not in graphic) agentgateway | Linux Foundation open-source gateway for LLM, MCP and A2A traffic, v1.6.0 (2 October 2026). | No change | A6-S061, A6-S062 |
| (not in graphic) Envoy AI Gateway | Renamed "Agent Router" and moved to the Agentic AI Foundation. v1.2.0 (6 October 2026). | Renamed | A6-S063, A6-S064 |
| (not in graphic) NVIDIA NeMo Guardrails | 0.24.1 (16 September 2026), Apache-2.0, still classed as Beta (0.x). Adds a new IORails engine. | No change | A6-S003, A6-S036 |
| (not in graphic) Guardrails AI | Acquired by Harvey on 9 September 2026. Hosted hub install and remote inference were retired on 25 August 2026; validators now ship on PyPI. Library 0.11.0 (Apache-2.0). | Acquired | A6-S004, A6-S028, A6-S037 |
| (not in graphic) Meta Llama Guard / Prompt Guard / LlamaFirewall | The newest releases found are Llama Guard 4 12B and Prompt Guard 2 (29 April 2025) and llamafirewall 1.0.3 (29 May 2025). Nothing newer was found. | No change | A6-S006, A6-S030, A6-S031, A6-S039 |
| (not in graphic) Amazon Bedrock Guardrails | Content filters (CLASSIC and STANDARD tiers, including PROMPT_ATTACK), denied topics, PII filters, contextual grounding, Automated Reasoning, cross-region profiles, and a standalone ApplyGuardrail API. Prices not verified. | No change | A6-S072, A6-S073 |
| (not in graphic) Azure AI Content Safety | Prompt Shields GA (August 2024). Task Adherence for agent tool use in preview (November 2025). Can be called from the APIM AI gateway on LLM, MCP and A2A traffic. | No change | A6-S054, A6-S055, A6-S020 |
| (not in graphic) Google Model Armor | Google's guardrail service. Free up to 2M tokens/month, then US$0.10 per 1M tokens. Integrated with Apigee and Google MCP servers. | No change | A6-S067 |
| (not in graphic) "Microsoft Presidio" | No longer a Microsoft project. It is now community-governed under the "Data Privacy Stack" organisation (MIT; 2.2.364, 22 July 2026). Images have moved to GHCR. | Renamed | A6-S005, A6-S040, A6-S041 |
| (not in graphic) Google Sensitive Data Protection | Formerly Cloud DLP. Positioned for protecting GenAI prompts and responses, and underpins Model Armor. Content inspection is US$3/GiB after 1 GiB free. | No change | A6-S065, A6-S066 |
| (not in graphic) Microsoft Purview (DSPM for AI) | Current name, status and pricing could not be verified. Purview is in Azure FedRAMP High scope. | Not publicly verified | A6-S056, A6-S059 |
| (not in graphic) Protegrity | "AI Developer Edition" SDK with Semantic Guardrail (1.1.1, December 2025). Corporate status not verified. | Not publicly verified | A6-S082 |
| (not in graphic) Skyflow | Vault and Detect SDK 2.1.3 (August 2026). SDK v1 reaches end of life on 31 October 2026. Corporate status not verified. | Not publicly verified | A6-S081 |
| (not in graphic) Microsoft Entra Agent ID | GA in 2026 (What's new page dated 1 May 2026). Security features require Microsoft Agent 365 licences. The agent registry is converging into Agent 365. | No change | A6-S057, A6-S058, A6-S059 |
| (not in graphic) Okta / Auth0 for AI Agents | Auth0 AI SDKs (Python 1.0.2, JS 6.0.2, "under heavy development"). Okta Cross App Access is based on the ID-JAG IETF draft. Product branding and GA not verified. | Not publicly verified | A6-S076, A6-S077, A6-S078, A6-S080 |
| (not in graphic) SPIFFE/SPIRE | SPIRE v1.15.3 (21 August 2026). CNCF graduated, Apache-2.0. | No change | A6-S042, A6-S043, A6-S087 |
| (not in graphic) OAuth 2.1 / MCP authorisation | MCP spec revision 2026-07-28: stateless protocol, RFC 9207 issuer validation, Dynamic Client Registration deprecated. The Enterprise-Managed Authorization extension (ID-JAG) is Stable. OAuth 2.1 itself is still an IETF draft. | No change | A6-S032, A6-S033, A6-S035, A6-S079 |
| (not in graphic) OPA | v1.21.1 (29 September 2026). CNCF graduated, Apache-2.0. | No change | A6-S046, A6-S048, A6-S088 |
| (not in graphic) Cedar / AgentCore Policy | Cedar 4.13.0 (15 September 2026, Apache-2.0). AgentCore Policy (Cedar-based) GA 3 March 2026. Amazon Verified Permissions not verified. | No change | A6-S026, A6-S044, A6-S045 |

## (b) Ambiguities owned

The baseline inventory assigns none of A1–A19 to stream ⑥. The open questions in the brief are resolved as follows:

- **Portkey acquisition:** confirmed. Palo Alto Networks completed it on 29 May 2026 [A6-S011, A6-S012]. The consideration figures conflict: the 10-K gives US$117m, the 10-Q gave US$140m including replacement awards, and press reported about US$700m [A6-S012]. Use the 10-K figure.
- **Other 2025–2026 acquisitions in scope:** Guardrails AI was acquired by Harvey on 9 September 2026 [A6-S028]. Presidio was not acquired; it moved from Microsoft to community governance [A6-S040]. No 2025–2026 acquisitions could be verified for LiteLLM, Kong, Protegrity or Skyflow (not publicly verified; search budget exhausted).
- **What AWS actually offers for C1:**
  - Bedrock AgentCore Gateway. It is an MCP gateway with inference targets, rate limits and rules [A6-S021, A6-S074].
  - A LiteLLM-based reference architecture, the Multi-Provider Generative AI Gateway Guidance [A6-S022].
  - Cross-region inference used for resilience [A6-S022].
  - Amazon API Gateway MCP proxy support. Only the December 2025 title is known [A6-S021].
- **Is "Bedrock AgentCore Policy" real?** Yes. It was GA on 3 March 2026 and is Cedar-based [A6-S026]. The API model also refers to AI-generated "Dogwood" policy statements [A6-S074]; their relationship to Cedar is unverified.
- **Current Llama Guard version:** Llama Guard 4 (12B), with Prompt Guard 2. No newer release was found [A6-S030, A6-S031].

## (c) Hypothesis evidence

### H1: gateway promoted to control plane (what gateways actually provide)

- **LiteLLM.**
  - Describes one control plane for LLMs, MCP servers and A2A agents, sharing auth, rate limiting and a usage dashboard [A6-S015].
  - Budgets can be set per key, user, team and customer, with TPM/RPM/parallel limits [A6-S015].
  - Guardrails can run pre-call, during the call or post-call, across chat, embeddings, MCP and A2A routes [A6-S015].
  - Semantic cache on Redis, Valkey or Qdrant. The docs warn that it "goes badly wrong on agentic traffic" [A6-S015].
  - Every limit is unset by default, and `max_budget` fails open without a database [A6-S015].
- **LiteLLM supply chain.** The March 2026 PyPI compromise shows that the gateway is itself a high-value supply-chain target [A6-S008, A6-S010].
- **Portkey.**
  - Palo Alto Networks bought it explicitly to place a gateway "in the traffic path" of Prisma AIRS, to inspect AI traffic at runtime, route requests, track tokens and govern agent interactions [A6-S011].
  - The open-source gateway offers fallbacks, retries, load balancing, guardrails in configs, and an MCP Gateway with a single auth layer [A6-S049].
- **Kong.**
  - AI Gateway 2.0 is a separate AI runtime with its own control plane and admin API [A6-S016].
  - Features: MCP Server Bundling with per-caller tool exposure, principal-aware policies, and modality-aware cost governance [A6-S016].
  - Guardrail plugins include semantic prompt/response guards, PII sanitisation, AWS/Azure/GCP guardrail services, NVIDIA NeMo Guardrails, and a custom third-party guardrail plugin (3.14) [A6-S017].
- **Cloudflare.** Caching, rate limiting, DLP, Llama Guard guardrails, dynamic routing and fallback, cost-based spend limits, identity-based budgets, and unified billing across providers [A6-S019, A6-S052].
- **Azure API Management.**
  - `llm-token-limit` (TPM and quotas per counter key), `llm-emit-metric`, semantic caching and `llm-content-safety` are GA [A6-S020, A6-S053].
  - Content safety now covers MCP tool-call arguments and A2A payloads, and a Prompt Shields option is available [A6-S020].
  - Microsoft describes the AI gateway as an extension of the existing API gateway, "not a separate offering" [A6-S053].
  - Microsoft Foundry is integrating it as an AI gateway control plane (preview) [A6-S020].
- **Apigee.** Token limit enforcement, LLM auditing and logging, semantic caching, multicloud model routing with circuit breaking, Model Armor, and MCP support (GA 31 March 2026) [A6-S023, A6-S024]. A semantic-cache SSRF fix shipped on 30 September 2026 [A6-S025].
- **AWS AgentCore Gateway.**
  - Target types: MCP, HTTP and inference (LLM provider) [A6-S074].
  - Rate limits cover request rates, token consumption and concurrent connections [A6-S074].
  - Rules provide principal-based access control and routing [A6-S074].
  - REQUEST and RESPONSE interception points [A6-S074].
  - A Cedar policy engine can be attached to authorise every tool call [A6-S026, A6-S074].
- **Open source beyond LiteLLM.** agentgateway (Linux Foundation) bundles an LLM gateway, MCP gateway and A2A gateway [A6-S061]. Agent Router (formerly Envoy AI Gateway) offers credentials, routing, quotas, failover and usage attribution on Envoy Gateway [A6-S063].
- **Gateways tracking the MCP spec directly.** Both AgentCore Gateway and Kong 2.1.0 list support for MCP revision 2026-07-28 [A6-S021, A6-S017].

### H3: agent identity, authorisation and tool-governance sub-layer

- **MCP authorisation (2026-07-28).**
  - The MCP server is an OAuth 2.1 resource server and MUST publish Protected Resource Metadata (RFC 9728) [A6-S033].
  - Clients MUST send RFC 8707 resource indicators [A6-S033].
  - Servers MUST validate the token audience. Token passthrough is forbidden and the confused-deputy problem is addressed [A6-S033, A6-S034].
  - Authorisation is still OPTIONAL [A6-S033].
- **MCP 2026-07-28 changes** [A6-S032]:
  - Adds RFC 9207 `iss` validation.
  - Binds client credentials to the issuer.
  - Deprecates Dynamic Client Registration in favour of Client ID Metadata Documents.
  - Adopts a feature lifecycle policy with a 12-month deprecation window.
- **Enterprise-Managed Authorization extension (Stable).**
  - The corporate IdP decides which MCP servers an employee can use [A6-S035, A6-S079].
  - The flow uses the Identity Assertion JWT Authorization Grant (`draft-ietf-oauth-identity-assertion-authz-grant`, a profile of `draft-ietf-oauth-identity-chaining`), RFC 8693 token exchange and RFC 7523 [A6-S035, A6-S079].
  - Okta's Cross App Access MCP sample uses the same grant [A6-S080].
- **Microsoft Entra Agent ID (GA).**
  - Identity constructs: agent identity blueprints, agent identities, agent users, and sponsors/owners/managers [A6-S057, A6-S058].
  - OAuth flows: `client_credentials` for autonomous agents, `jwt-bearer` for On-Behalf-Of, and no interactive flows [A6-S060].
  - Controls extended to agents: Conditional Access, ID Governance access packages, ID Protection, network controls and audit logs [A6-S058].
  - Third-party agents (AWS Bedrock, n8n) are supported via a sidecar SDK or workload identity federation [A6-S057].
  - Licensing is tied to Microsoft Agent 365 [A6-S059].
- **Auth0 AI SDKs.** Delegated API calls on users' behalf, authorisation for RAG, and asynchronous human approval via OpenID CIBA. The SDKs are flagged "under heavy development" [A6-S076, A6-S078].
- **Policy-based tool governance (AWS).**
  - AgentCore Policy (GA 3 March 2026) is deny-by-default for gateway tool calls [A6-S026].
  - Policies use identity claims and tool arguments [A6-S026].
  - Partial evaluation removes denied tools from `tools/list` [A6-S026].
  - Natural-language policies are converted to Cedar and checked by automated reasoning [A6-S026].
  - Decisions are logged to CloudWatch [A6-S026].
- **Workload and policy building blocks are mature.**
  - SPIRE is CNCF graduated and issues SPIFFE IDs/SVIDs via the Workload API for mTLS/JWT trust [A6-S087].
  - OPA is CNCF graduated, v1.21.1 [A6-S046, A6-S048].
  - Cedar is Apache-2.0 and designed for RBAC/ABAC and automated reasoning [A6-S045].
- **Gateways implementing tool governance.**
  - Kong: MCP access controls and scope-based tool filtering (3.13/3.14); token exchange; MCP bundling with per-caller tool exposure [A6-S016, A6-S017].
  - LiteLLM: MCP access by key/team, with tool filtering per key; A2A agents are open to all callers until an allowlist is defined [A6-S015].
  - Portkey: MCP Gateway providing centralised auth [A6-S049].
  - Azure APIM: credential manager OAuth for MCP servers [A6-S053].
- **Guardrails moving towards agent behaviour.**
  - Azure Task Adherence (preview) detects misaligned or premature agent tool use [A6-S055].
  - LlamaFirewall AlignmentCheck audits agent reasoning for goal hijacking [A6-S039].

## (d) Products the graphic misses that an architect would expect

Added to `products.json` (marked `"original_label": null`):

- **agentgateway** (C1): Linux Foundation open-source LLM/MCP/A2A gateway [A6-S061].
- **Agent Router, formerly Envoy AI Gateway** (C1): Kubernetes-native AI gateway in the Agentic AI Foundation [A6-S063].
- **Google Model Armor** (C2): Google Cloud guardrail service used inline by Apigee and MCP servers [A6-S067].

Noted but not added:

- **Microsoft Agent 365:** agent registry and licence vehicle for Entra agent security [A6-S058, A6-S059].
- **Amazon Bedrock AgentCore Identity:** token vault and credential providers. Free via Runtime/Gateway; US$0.010 per 1,000 token/API-key requests otherwise [A6-S021, A6-S074].
- **Amazon API Gateway MCP proxy support:** December 2025, title only [A6-S021].
- **Cloudflare One DLP:** the source of the full DLP profiles in AI Gateway [A6-S052].
- **F5 AI Guardrails:** integration in NeMo Guardrails 0.24.0 [A6-S036].

## (e) Gaps

- **Search budget.** The shared WebSearch budget (200 calls per turn) was exhausted during C2, so trust centres and pricing pages could not be searched for C2 to C4. The following are therefore **not publicly verified**:
  - Bedrock Guardrails prices and certifications.
  - Azure AI Content Safety unit prices and the current 2026 naming.
  - Microsoft Purview DSPM for AI: name, GA status, features, pricing.
  - Protegrity and Skyflow: certifications, EU regions, pricing, corporate events.
  - Okta/Auth0 product branding, GA dates and pricing.
  - Amazon Verified Permissions.
  - Agent 365 prices.
  - Any agent-specific SPIFFE work.
  - IETF agent-identity drafts beyond those cited by MCP.
- **Trust centres.** These were not reachable for any vendor. Certifications are recorded only where a vendor page, extract or Google compliance-scope page states them:
  - Portkey and Kong: vendor claims via search extract.
  - Apigee, Model Armor and SDP: Google SOC 2 and ISO 27001 scope pages.
  - APIM, Entra and Purview: Azure FedRAMP scope.
- **Adoption signals.** GitHub stars could not be verified anywhere because github.com and its API are blocked. LiteLLM download volumes are secondary only [A6-S010].
- **Unconfirmed GA status.** AWS AgentCore Gateway inference targets and rate limits, and Bedrock `InvokeGuardrailChecks`, appear in the AWS API model (botocore, 7 October 2026), but their GA status is unconfirmed [A6-S074, A6-S073].
- **OPA maintainers.** A reported 2025 move of OPA's maintainers (Styra) to Apple was not verified.
- **Kong.** Pricing and the date of the reported US$175m round were not verified [A6-S018].
- **Undated or stale primary pages.** Portkey's pricing page may be stale (search tool flagged about 470 days) [A6-S013]. The Azure Content Safety Learn pages are dated 16 September 2025 [A6-S054].
