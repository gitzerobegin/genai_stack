## 4. Tools, protocols and agent connectivity

> **Conflict-of-interest disclosure.** The author is an Anthropic model. The Model Context Protocol (MCP) and Agent Skills both originated at Anthropic [VF: A3-S018, A3-S028]. Both were scored on the same rubric as every other product in this section. Independent criticism of both is recorded in their deep dives, and an independent alternative is named wherever either is recommended [AJ].

> **Executive summary.** This layer is where an agent stops talking and starts acting: it calls tools, reads enterprise systems, browses, runs code and talks to other agents. Three things have changed since the original graphic. First, the protocols have moved to neutral homes. Anthropic donated MCP to the Agentic AI Foundation (AAIF) under the Linux Foundation on 9 December 2025 [VF: A3-S018, V1-S038], and A2A 1.0.0 (12 March 2026) joined AAIF in August 2026 [VF: A3-S079, A3-S116, A3-S117]. Agent Skills has no neutral governance body and is not an AAIF project on available evidence [VF: V1-S046, A3-S115]. Second, MCP has grown an enterprise security model. The 2026-07-28 specification is stateless, deprecates Dynamic Client Registration and puts method and tool names in HTTP headers so that gateways can authorise them, and the Enterprise-Managed Authorization extension has been stable since June 2026 [VF: A3-S015, A3-S057, A3-S017]. Authorisation itself is still optional in the specification [VF: A3-S055]. Third, ownership and risk have shifted among the tool vendors. Nebius closed its acquisition of Tavily on 19 February 2026 [VF: A3-S084, V1-S041], and Composio disclosed a May 2026 incident in which connected-account tokens and API keys were exposed [VF: B-L4-S007]. The graphic draws L4 as a row of tools. The real design problem is governing what those tools are allowed to do, on whose behalf [AJ]. **Recommendation:** standardise on MCP for agent-to-tool connectivity, but only behind a firm-owned tool gateway that enforces authorisation, an allow-listed private registry and per-tool policy. Expose authoritative data through read-only tools. Run generated code only in a microVM sandbox with egress control. Treat every SaaS tool (search, browser, integration broker) as an outsourced data flow [Rec]. Independent alternatives to MCP are OpenAPI-described tools exposed through a gateway, and A2A for agent-to-agent delegation [Rec].

### 4.1 Responsibility

**The problem this layer owns.** L4 turns an agent's intent into a controlled action on a system outside the model [AJ]. It has five jobs:

- **Tool invocation and external APIs.** Describe tools so a model can select them, validate arguments, call them and return results, including long-running work [AJ].
- **Enterprise-system connectivity.** Reach internal data stores, calculation engines and SaaS applications through a stable contract rather than bespoke glue [AJ].
- **Execution runtimes.** Provide isolated places to run generated code and drive web browsers [AJ].
- **Protocol interoperability.** Let tools and agents built on different frameworks and vendors work together (MCP for agent-to-tool, A2A for agent-to-agent) [AJ].
- **The missing sub-layer: identity, authorisation and tool governance.** Decide which agent, acting for which person, may call which tool with which arguments, with which credential, and record the decision [AJ]. This is hypothesis H3 (§4.13).

**Hand-offs.**
- *Above:* L3 orchestration decides when to call a tool; L4 decides whether the call is allowed and executes it. A deterministic workflow should name its tools explicitly; an autonomous agent selects from what L4 exposes, which is why the exposed set must be minimal [AJ].
- *Below and beside:* the tools reach data in L5 to L8 and enterprise systems of record. Tool spans go to L9 via OpenTelemetry, whose GenAI conventions cover tool execution and MCP [VF: A1-S061].
- *Control plane:* agent and user identity, token issuance and policy belong to C4; secrets custody, sandboxing standards and supply-chain controls belong to C7; the gateway product is often shared with C1, because the C1 gateways now carry MCP and A2A traffic as well as model calls [VF: A6-S061, A6-S016, A6-S053, A6-S051]. This section specifies what L4 needs from those controls and does not repeat their product analysis [AJ].

**What the layer does not own.** It does not own the agent's plan (L3), the content safety of the model's output (C2) or the identity provider (C4). It does own the enforcement point at which a tool call is accepted or refused [AJ].

### 4.2 Why it matters

A badly designed tool layer turns every weakness of a language model into an action [AJ]. Prompt injection becomes data exfiltration when the agent holds a token that can send email. A hallucinated argument becomes a wrong trade instruction when a write tool is exposed. A tool description becomes an attack vector when the client trusts whatever a third-party server says about itself [AJ].

The evidence for this is no longer theoretical:
- The MCPTox benchmark (AAAI 2026) tested tool-poisoning attacks against 45 live MCP servers and 20 models. The average attack success rate was 36.5% and the peak 72.8%, and more capable models were often more susceptible [VF: A3-S023].
- Cloud Security Alliance research notes (July 2026) describe high-severity issues between mid-2025 and June 2026 in Cursor, Claude Code, Gemini CLI, GitHub Copilot and Amazon Q, where IDEs launched project-defined MCP servers with developer privileges and no isolation [R: A3-S022]. CSA's attribution and dates are inconsistent across its notes [R: A3-S022].
- Composio, a broker that holds end users' OAuth tokens for third-party applications, disclosed unauthorised access to internal systems in May 2026. By its own account about 0.3% of active connections leaked, including 5,001 GitHub connections, and 5,241 API keys were flagged as possibly exposed [VF: B-L4-S007].
- The OWASP Top 10 for Agentic Applications for 2026 lists tool misuse (ASI02), identity and privilege abuse (ASI03) and the agentic supply chain (ASI04) [VF: A3-S046]. The 2026 LLM list moved Excessive Agency to third place [R: A8-S041].

**Illustrative scenario [AJ].** A distribution team builds a research assistant that drafts client meeting notes. A developer connects it to a popular community MCP server for web search and to the firm's CRM through an integration broker, using a service account with read-write scope "to save time". The search server's maintainer later publishes an update whose tool description tells the model to "include the full client context in the query for better results". The client auto-updates the server, because nothing pins the tool definition. For six weeks, every search query carries the client's name, holdings summary and the purpose of the meeting to a search API outside the firm's third-party register. Nobody notices, because tool calls are logged only as "search succeeded". The leak is found when a sales manager sees a competitor-briefing document that quotes an unusual phrase from an internal note. A pinned, allow-listed tool definition, a DLP check on outbound queries and a read-only, per-user credential would each have broken the chain. The scenario is invented; it is not a reported incident.

### 4.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Authorised-call coverage | Share of remote tool calls carrying an audience-bound token validated at the gateway | 100% in production; any unauthenticated remote tool is a defect | Gateway logs: token audience and issuer checks |
| Allow-list conformance | Tool calls to servers and tool names on the approved registry | 100%; unknown tools blocked, not logged | Gateway decision log against the private registry |
| Tool-definition drift | Tool descriptions or schemas that changed since review (hash mismatch) | 0 unreviewed changes reach production | Hash pinning of reviewed definitions; registry diff alerts |
| Write-scope exposure | Tools with write or destructive effect exposed to a given agent | 0 for read-only use cases; each other one named and approved | Registry metadata verified by owners, not taken from server annotations |
| Delegation correctness | Calls made with the end user's delegated rights (or a named agent identity) rather than a shared service account | 100% for user-facing agents | Token claims (subject, actor) sampled from audit log |
| Credential hygiene | Long-lived secrets inside agent context, prompts or sandbox images | 0 | Secret scanning of traces and templates (C7) |
| Sandbox egress violations | Blocked outbound connections from code sandboxes | Every one reviewed; trend falling | Sandbox firewall logs |
| Outbound query DLP hits | Search or browse requests containing classified client data | 0 released; blocked at egress | DLP on the egress proxy (C3) |
| Tool-call accuracy | Right tool, right arguments, right order | ≥0.98 for read-only data tools (as L9) | L9 trajectory evals |
| Tool latency and availability | p95 latency and success rate per tool | Per tool SLO | Gateway and OTel spans |
| Time to revoke | From decision to block a server, tool or credential until enforced everywhere | Under 1 hour | Drill: revoke a test tool and measure |

### 4.4 How it works

**Tool contracts.** MCP defines how clients (agent hosts) discover and call tools, resources and prompts exposed by servers over JSON-RPC [VF: A3-S058, A3-S015]. Since the 2026-07-28 revision each request is self-describing and stateless, discovery via `server/discover` is optional, and long-running work uses the Tasks extension [VF: A3-S015, A3-S057]. The same revision deprecates Roots, Sampling, Logging, the legacy HTTP+SSE transport and Dynamic Client Registration, under a policy with a 12-month minimum deprecation window [VF: A3-S015, A3-S057, V2-S031]. Tool annotations (read-only, destructive, idempotent, open-world) are hints that clients must treat as untrusted unless the server is trusted [VF: A3-S020].

**Gateways and headers.** The 2026-07-28 revision puts method and tool names in `Mcp-Method` and `Mcp-Name` HTTP headers so that gateways, rate limiters and web application firewalls can route and authorise without parsing bodies [VF: A3-S015]. This is the protocol change that makes a tool-governance plane practical [AJ].

**Authorisation.** Authorisation is OPTIONAL for MCP implementations [VF: A3-S055]. When it is used, the MCP server is an OAuth 2.1 resource server; servers must publish Protected Resource Metadata (RFC 9728); clients must send Resource Indicators (RFC 8707) and use PKCE; servers must reject tokens not issued for them, and token passthrough is forbidden [VF: A3-S055, A3-S056, A3-S039]. The 2026-07-28 revision adds RFC 9207 issuer validation and issuer-bound client credentials, and replaces Dynamic Client Registration with Client ID Metadata Documents [VF: A3-S057]. OAuth 2.1 itself is still an IETF draft [VF: A6-S033].

**Enterprise-Managed Authorization (EMA).** The identity provider issues an Identity Assertion JWT Authorization Grant (ID-JAG) during single sign-on, which the client exchanges for an MCP access token. The aim is central policy and one audit trail without per-server consent screens [VF: A3-S017]. Okta Cross App Access was the first identity provider, and Okta Agent SSO (XAA) reached GA on 24 August 2026 [VF: A3-S017, A6-S099, V2-S035].

**Agent-to-agent.** A2A lets a client agent discover a remote agent through its Agent Card at `/.well-known/agent-card.json`, send messages and manage long-running tasks with streaming and push notifications [VF: A3-S078]. Agent Cards may be signed with JWS over canonicalised JSON, and clients should verify signatures when present [VF: A3-S078, A3-S031].

**Runtimes.** Code runs in sandboxes such as E2B's Firecracker microVMs, one per sandbox, with a per-sandbox egress firewall [VF: A3-S062]. Browsers run as remote sessions that Playwright or Puppeteer drive over the Chrome DevTools Protocol, as in Browserbase [VF: A3-S013].

```text
  Analyst / service ──SSO──► IdP (C4) ── ID-JAG / token exchange ─┐
                                                                   ▼
  L3 agent or workflow ──► MCP client ──► TOOL GATEWAY (L4 governance, often the C1 product)
                                          │ 1 authenticate caller, check token audience/issuer
                                          │ 2 allow-list: server + tool name + definition hash
                                          │ 3 policy (Cedar / OPA): who, which tool, which args
                                          │ 4 outbound credential from vault (C7), never from the model
                                          │ 5 audit + OTel span (L9); DLP on outbound args (C3)
             ┌──────────────┬─────────────┼───────────────┬───────────────────┐
             ▼              ▼             ▼               ▼                   ▼
     Internal read-only  Calculation   SaaS apps via   Web search /       Remote agents
     MCP servers         sandbox       per-user OAuth  browser (egress    (A2A, signed
     (data, engines)     (microVM,     (broker or      proxy, no client   Agent Cards)
                         egress deny)  gateway 3LO)    data)
```

The gateway is the design choice that matters most. Without it, every MCP client is its own policy engine, and the firm has as many security models as it has agent hosts [AJ].

### 4.5 Enterprise design principles

**Security: identity and least privilege**

- Make authorisation mandatory in your estate even though the specification makes it optional. Every remote MCP server sits behind the gateway and accepts only audience-bound tokens [Rec].
- Distinguish three identities on every call: the human (subject), the agent (actor) and the tool server (audience). The MCP roadmap of 22 August 2026 lists DPoP, Workload Identity Federation, ID-JAG and token exchange as agent-identity priorities, and states that today's model is "built around a person approving access in a browser" [VF: A3-S016]. Until those land, use EMA or token exchange for user-delegated calls and workload identity for autonomous ones [Rec].
- Never pass a user's upstream token through to a tool. The MCP specification forbids token passthrough and documents the confused-deputy risk [VF: A3-S056].
- Issue outbound credentials from a vault at call time. AgentCore Identity keeps refresh tokens in a vault [VF: A3-S047]. Vault Enterprise 2.1 made agentic IAM GA on 1 September 2026, enforcing the intersection of user permissions and agent ceiling policies and recording both in audit logs [VF: A7-S034, A7-S061]. Auth0 Token Vault brokers third-party API tokens for agents [VF: A6-S097]. Details are in C4 and C7 [AJ].
- Default deny at the tool level. AgentCore Policy evaluates every agent-to-tool call against Cedar policies before execution and filters denied tools out of `tools/list` [VF: A6-S026]. OPA is the vendor-neutral alternative policy engine [VF: A6-S046].
- Read-only by default. Classify each tool's effect yourself; do not rely on the server's annotations [VF: A3-S020] [Rec].

**Security: supply chain and tool integrity**

- Pin reviewed tool definitions by hash and block on change. OWASP's MCP Top 10 (MCP03:2025 Tool Poisoning) recommends signing manifests and hash-pinning reviewed definitions against rug pulls [VF: A3-S045].
- Run a private registry and allow-list. The official MCP Registry is still in preview, its API frozen at v0.1, and it moderates by denylisting [VF: A3-S019, A3-S042, A3-S036]. GitHub Copilot can be pointed at an organisation or enterprise MCP registry [VF: A3-S043], and Microsoft documents a private registry on Azure API Center enforced in Copilot and VS Code [VF: A3-S044].
- Never let a developer tool auto-launch project-defined MCP servers with developer privileges [R: A3-S022] [Rec].
- Treat skills as code. Anthropic warns that malicious skills can exfiltrate data and advises installing only from trusted sources [VF: A3-S072]. No signing or provenance mechanism exists in the Agent Skills format [VF: A3-S037, A3-S061].

**Sandboxing and egress**

- Run generated code only in a microVM or equivalent isolation with default-deny egress and domain allow-lists, as E2B provides [VF: A3-S062] [Rec].
- Route all web search and browsing through an egress proxy with DLP. Tavily's SDK accepts a custom HTTP session so that traffic can be proxied through an API gateway for central authentication, logging and policy [VF: A3-S009]. A search query is an outbound data transfer: it can reveal the firm's intent even when it contains no personal data [AJ].

**Scalability and resilience**

- Stateless MCP (2026-07-28) removes session affinity, so tool servers can sit behind ordinary load balancers [VF: A3-S015] [AJ].
- Each SaaS tool needs a fallback or a graceful "tool unavailable" path in the workflow. An agent that silently answers from model memory when a data tool fails is worse than one that stops [AJ].

**Governance and observability**

- Every tool has a named owner, a risk class (read, write, destructive, external egress), a reviewed definition hash and a change process [Rec].
- Emit one OTel span per tool call with tool name, server, arguments hash, decision and result size; full arguments go to the audit store only where policy allows [AJ].

**Cost.** Most cost lies in hosting servers, the gateway and the authorisation server, and in per-call SaaS fees [VF: A6-S021, A3-S100, A3-S088]. Tool-call volume, not token volume, drives SaaS tool spend [AJ].

**Portability.** Keep tool contracts as OpenAPI or MCP schemas in your own repository and generate whichever form a client needs. Hold credentials in your own vault rather than a broker's [Rec].

**Patterns [AJ]:** tool gateway with default deny; private registry with hash-pinned definitions; read-only data tools onto systems of record; per-user delegated tokens via EMA or token exchange; microVM sandbox with egress allow-list; egress proxy with DLP for search and browse; deterministic workflow that names its tools.

**Anti-patterns [AJ]:** a shared service account with write scope behind a user-facing agent; community MCP servers installed straight from a public index; trusting tool annotations; long-lived API keys in prompts or sandbox images; a SaaS broker holding every user's OAuth tokens with no exit plan; client data in web-search queries; the model computing figures that an engine already produces.

### 4.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Coverage of the plan's questions: tool invocation, enterprise connectivity, browser and code execution, identity propagation, protocol interoperability; for protocols, the authorisation profile and long-running work; for runtimes, isolation and egress control |
| Enterprise readiness (15%) | SSO, RBAC and audit logs of tool calls (including denied ones); SCIM; SLA; admin APIs; for open specifications, what they enable in your estate (central IdP policy, registry control) |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in product scope; incidents and their remediation; credential custody; for specifications, the security model (mandatory or optional authorisation, signing, provenance) and project hygiene |
| Deployment flexibility (15%) | Self-host, BYOC or VPC for anything that touches client data; region choice for SaaS tools; air-gap for sandboxes |
| Ecosystem (5%) | MCP support on both sides; client adoption; OpenAPI conversion; OTel export |
| Reliability and maturity (10%) | Spec stability and deprecation policy; release cadence; pre-1.0 SDKs; ownership changes |
| Cost / TCO (5%) | Per-call pricing; minimum commitments; operations burden of self-hosting gateways and sandboxes |
| Lock-in / portability (15%) | Open specification and neutral governance; who holds the credentials; whether tool contracts live in your repository |

### 4.7 Product deep dives

**Model Context Protocol (AAIF / Linux Foundation; originated at Anthropic).**
- *Conflict of interest:* MCP originated at Anthropic and the author is an Anthropic model. It was scored on the same rubric as A2A and the commercial products, and the criticisms below are recorded in full [AJ].
- *What it is now:* an open protocol for connecting agent hosts to tools, resources and prompts [VF: A3-S058]. The current revision is 2026-07-28, with Tier 1 SDKs in TypeScript, Python, Go and C#; the Python `mcp` package is at 2.3.0 (2 October 2026) and the TypeScript SDK at 1.32.1 (5 October 2026) [VF: A3-S015, A3-S011, A3-S074, V1-S037]. The specification and SDKs are MIT-licensed [VF: A3-S058, A3-S011].
- *Governance:* Anthropic donated MCP to the Agentic AI Foundation, a directed fund of the Linux Foundation, on 9 December 2025. The maintainer structure was unchanged and AAIF does not set technical direction [VF: A3-S018, V1-S038]. Both Lead Maintainers are Anthropic staff; an AWS engineer joined the Core Maintainers in April 2026 [VF: A3-S082]. AAIF had 247 members by August 2026, including Visa and Wells Fargo as Gold members [VF: A3-S041].
- *Security model:* authorisation is optional; when used, it is a strict OAuth 2.1 profile with audience-bound tokens, PKCE, RFC 9728 metadata and RFC 9207 issuer validation, and token passthrough is forbidden [VF: A3-S055, A3-S056, A3-S057]. EMA (stable 18 June 2026) gives central IdP control; Anthropic's clients and VS Code support it, as do servers including Asana, Atlassian, Canva, Figma, Linear and Supabase [VF: A3-S017, V1-S045].
- *Criticisms:* authorisation is optional in the specification [VF: A3-S055]. Tool annotations are only hints [VF: A3-S020]. Tool poisoning succeeded in 36.5% of attempts on average in MCPTox [VF: A3-S023]. OWASP maintains an MCP Top 10 in which tool and schema poisoning is MCP03 [VF: A3-S045]. Researchers argue that prompt-injection filtering plus OAuth correctness is not enough, citing newer variants (MCP-ITP, ShareLock, Potemkin) [VF: A3-S024]. IDE clients from several vendors, including Anthropic's Claude Code, had high-severity issues from auto-launching project-defined servers [R: A3-S022]. The official Registry has been in preview since 8 September 2025, its "Registry API v1 GA" item is at the "Ideating" stage with no target date, and `/v1` returned 404 on 7 October 2026 [VF: A3-S019, A3-S114, A3-S036]. The 2026-07-28 revision contained breaking changes [VF: A3-S015]. Adoption figures (about 0.5bn monthly SDK downloads, July 2026) are project-reported [VF: A3-S015] [AJ]. The TypeScript SDK published several High-severity advisories in 2026, including GHSA-6qxp-vccf-f47h (30 September 2026), in which an OAuth client could send stored refresh tokens and client secrets to an authorisation server named by a malicious MCP server; the fix also requires `expectedIssuer` to be configured [VF: B-REVA-S006].
- *Strengths:* the de facto agent-to-tool contract, now with an enterprise-grade authorisation profile and gateway-friendly headers [AJ]. Launch partners for 2026-07-28 include AWS, Cloudflare, Google Cloud and Microsoft Foundry [VF: A3-S015].
- *Limitations:* the security that matters in a regulated firm (mandatory authorisation, allow-listing, definition pinning, policy) lives outside the specification, in gateways and registries [AJ]. Technical direction is concentrated in one vendor's staff [VF: A3-S082] [AJ].
- *Choose when:* you need one contract for tools across several agent frameworks and model vendors [AJ].
- *Avoid when:* you would connect clients directly to third-party servers without a gateway and registry [AJ].
- *Independent alternatives:* OpenAPI-described tools exposed through a gateway and called through each model's native function calling; AgentCore Gateway, Apigee and APIM can convert existing APIs into tools [VF: A6-S021, A6-S024, A6-S053]. Vendor-neutral private registries (Azure API Center, GitHub's enterprise registry setting) can hold the allow-list whichever protocol wins [VF: A3-S043, A3-S044].
- *Competitors:* A2A (complementary, agent-to-agent), OpenAPI tool definitions, vendor function-calling schemas.
- *FS note:* adopt the protocol, not the ecosystem: internal servers only, behind the gateway, with authorisation mandatory and definitions pinned [Rec].
- **Tier: Strategic, conditional: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions [AJ]. No flag.** Tier set by the reader at Checkpoint 3 (CP3 Q1); the author's reviewers had resolved the borderline call against the Anthropic-originated item [AJ]. MCP and its authorisation profile (C4) are one decision with one tier. FS 3.55 is below the 3.6 guide and security scores 2, which is why every part of the condition is mandatory; the independent alternative remains OpenAPI-described tools behind the same gateway [AJ].

**Agent2Agent Protocol (A2A Project, AAIF / Linux Foundation).**
- *What it is now:* an open protocol for communication between opaque agent applications. Specification 1.0.0 was released on 12 March 2026 and 1.0.1 on 26 May 2026; the Python SDK `a2a-sdk` is at 1.2.2 (5 October 2026) [VF: A3-S078, A3-S079, A3-S075, V1-S039]. Specification and SDKs are Apache-2.0 [VF: A3-S075, A3-S025].
- *Governance:* Google contributed A2A to the Linux Foundation in 2025, and it was accepted as a Growth Stage AAIF project (AAIF announcement 17 August 2026; A2A blog 27 August 2026) with its own TSC [VF: A3-S065, A3-S116, A3-S117, V1-S039]. The TSC has eight companies: Google, Microsoft, Cisco, AWS, Salesforce, ServiceNow, SAP and IBM [VF: A3-S065]. IBM's Agent Communication Protocol was merged into A2A in August 2025 [VF: A3-S032].
- *Security model:* Agent Cards may be signed (JWS over RFC 8785 canonical JSON), and clients should verify signatures when present. Version 1.0 added device-code and PKCE flows and removed implicit and password flows. An authenticated extended Agent Card is available only after the client authenticates [VF: A3-S078, A3-S079, A3-S031]. The protocol "does not define the scope, representation, validity, or revocation semantics" of authorisation obtained in the AUTH_REQUIRED state [VF: A3-S078].
- *Strengths:* the most neutral governance in this layer, with an eight-company TSC [AJ]. It handles long-running delegated tasks that MCP's tool model was not designed for [AJ].
- *Limitations:* card signing is optional, so trust in a remote agent's identity is not guaranteed by the protocol [AJ]. Version 1.0 broke the interaction protocol (the Agent Card stayed backward-compatible) [VF: A3-S079, A3-S030], and some SDKs lag the card restructuring according to implementer reports [R: A3-S030].
- *Choose when:* agents owned by different teams or vendors must delegate work to each other [AJ].
- *Avoid when:* a deterministic workflow calling tools would do; most regulated use cases today are in that category [AJ].
- *Competitors:* MCP (agent-to-tool), framework-native multi-agent APIs (L3), agentgateway's A2A gateway [VF: A6-S061].
- *FS note:* require signed Agent Cards and verify them; bound and revoke delegated authority yourself, because the protocol does not [Rec].
- **Tier: Strategic, conditional: where cross-team or cross-vendor agent delegation is in scope (CP3 Q1) [AJ]. No flag.** Signed Agent Cards must be verified, and delegated authority scoped and revocable by the firm, because the protocol does not define it. Where a deterministic workflow calling tools would do, as in most regulated use cases today, A2A is not needed at all [AJ].

**Agent Skills (SKILL.md format; originated at Anthropic, Anthropic-maintained).**
- *Conflict of interest:* Agent Skills originated at Anthropic and the author is an Anthropic model. It was scored on the same rubric as everything else [AJ].
- *What it is now:* an open packaging format for procedural knowledge: folders with a `SKILL.md` file (name and description required) plus optional scripts, references and assets [VF: A3-S061, A3-S037]. Agents load only names and descriptions at start-up, read the full skill when a task matches, and may execute bundled scripts [VF: A3-S061]. Anthropic launched it on 16 October 2025 and published it as an open standard on 18 December 2025 [VF: A3-S028, A3-S029, V1-S040]. Repository code is Apache-2.0 and documentation CC-BY-4.0 [VF: A3-S061].
- *Adoption:* the agentskills.io showcase lists 46 clients, including OpenAI Codex, Gemini CLI, GitHub Copilot, VS Code and Cursor; OpenAI's and Google's own documentation confirm support [VF: A3-S113, A3-S033, A3-S034, V1-S047].
- *Governance (criticism):* there is no neutral governance body [VF: V1-S046]. The maintainers are Anthropic employees, listing requests are reviewed by the Anthropic team, and an AAIF project proposal (issue #47, September 2026) has not been accepted on available evidence [VF: A3-S112, A3-S115]. The specification is a "living document" with no tagged releases [VF: A3-S115].
- *Security (criticism):* no signing or provenance mechanism exists in the format [VF: A3-S037, A3-S061]. Anthropic warns that malicious skills can exfiltrate data [VF: A3-S072], and the Gemini CLI documentation gives similar advice [VF: A3-S034]. OWASP runs an "Agentic Skills Top 10" project [VF: A3-S046].
- *Strengths:* plain files that any team can review in Git; progressive disclosure keeps context small [AJ].
- *Limitations:* a skill can carry executable code, so it is a software supply-chain item, not a document [AJ]. Organisation-wide provisioning is a vendor feature (for example Claude Team and Enterprise admins), not part of the standard [VF: A3-S029].
- *Choose when:* you want to package house procedures (style rules, report templates, review checklists) once and use them across several agent clients [AJ].
- *Avoid when:* skills would come from outside the firm, or would carry scripts that run with the agent's credentials [AJ].
- *Independent alternatives:* Git-versioned instruction and prompt packages managed under C5; AGENTS.md, which was a founding AAIF project alongside MCP [VF: V1-S038]. The AAIF "Skills Over MCP" working group is exploring delivery of skills through MCP [VF: A3-S038].
- *Competitors:* AGENTS.md, C5 prompt management, MCP prompts.
- *FS note:* internally authored, Git-reviewed, script-free skills only, until the format has signing, versioning and neutral governance [Rec].
- **Tier: Tactical, conditional: internally authored skills only. Flag: none.** Governance and versioning keep it out of Strategic [AJ].

**Composio.**
- *What it is now:* a managed tool-integration platform: 1000+ toolkits, per-user sessions whose tools an agent calls, OAuth and connected-account handling, and per-session restriction of toolkits, tools, auth configurations and accounts [VF: A3-S063, A3-S008]. The Python SDK is 0.25.0 (29 September 2026), with 2.0.0b0 in pre-release; SDKs are MIT and the platform is proprietary [VF: A3-S008, A3-S067, V1-S098].
- *Governance features (vendor-stated):* an "MCP Gateway" with SAML/OIDC SSO and SCIM on Enterprise, action-level policy-as-code, and per-call audit logs including denied calls, with 7-day to 1-year retention and SIEM export [VF: A3-S119, A3-S098]. Composio's own pages conflict on whether audit logs hold metadata only or inputs and outcomes [NPV].
- *Certifications:* Composio states SOC 2 Type II and ISO/IEC 27001:2022 [VF: A3-S098]. These claims come from vendor marketing pages only, with no trust-centre report seen (V1 verification log, section 4), so they count as not publicly verified for scoring [NPV].
- *Incident:* Composio disclosed unauthorised access to internal systems in May 2026, reportedly via a takeover of employees' Gmail OAuth tokens. It revoked OAuth2 tokens across about 100 toolkits and all user GitHub tokens, deleted API keys created before 22 May 2026, and asked customers to rotate keys and have end users rotate credentials at each provider; it said the full scope was not yet known [VF: B-L4-S007].
- *Deployment and residency:* the managed cloud is hosted in the US; EU-only residency needs self-hosted Enterprise, which also offers VPC and on-premises options [VF: A3-S119, A3-S098].
- *Strengths:* the broadest catalogue of SaaS connectors with per-user authentication [AJ].
- *Limitations:* it holds end users' OAuth tokens for third-party applications, which makes it a high-value target and a high switching cost [AJ]. The SDK is pre-1.0 [VF: A3-S008].
- *Choose when:* a low-risk internal productivity agent needs many SaaS connectors quickly, self-hosted [AJ].
- *Avoid when:* the agent touches client data, or you cannot self-host in-region [AJ].
- *Competitors:* AgentCore Gateway and Identity, Auth0 Token Vault (C4), Kong AI Gateway MCP controls (C1).
- *FS note:* do not let a third party hold staff OAuth tokens to firm systems on its multi-tenant cloud; if used, self-host and keep the token vault in your estate [Rec].
- **Tier: Experimental. No flag.** Security evidence and the May 2026 incident keep it out of production use for regulated data [AJ].

**Exa.**
- *What it is now:* a web search API for AI with date and domain filters, page contents and highlights, generated answers and structured output via `output_schema`; `exa-py` is at 2.25.0 (1 October 2026) [VF: A3-S010]. It has an MCP server [VF: A3-S054].
- *Certifications and terms:* SOC 2 Type II (security, confidentiality, availability) with a 2026 bridge letter, HIPAA BAA for eligible Enterprise customers, and a DPA with EU SCCs and the UK Addendum; zero data retention on Enterprise [VF: A3-S100, A3-S121]. SSO and SCIM for the Exa dashboard are on Enterprise [VF: A3-S121].
- *Pricing:* US$7 per 1,000 searches, with one page saying from US$4 per 1,000 (conflict), as of 7 October 2026 [VF: A3-S100].
- *Funding:* a US$250M Series C at a US$2.2B valuation in May 2026 [R: A3-S101].
- *Strengths:* a well-funded, independent search index with structured output [AJ].
- *Limitations:* SaaS only; no EU processing region was found [VF: A3-S121]. Self-hosting or VPC deployment is not publicly verified [NPV].
- *Choose when:* agents need public-web research on non-confidential questions [AJ].
- *Avoid when:* queries could contain client, holdings or deal information [AJ].
- *Competitors:* Tavily, Firecrawl and Apify (L8).
- *FS note:* enable zero data retention, route through the egress proxy with DLP, and register it as an ICT third-party service [Rec].
- **Tier: Tactical. No flag.**

**Tavily (Nebius).**
- *What it is now:* a search, extract, crawl, map and research API for agents; `tavily-python` 0.8.5 and `@tavily/core` 0.7.14 were released on 6 October 2026 [VF: A3-S009, A3-S083]. It has an MCP server [VF: A3-S054].
- *Ownership:* Tavily announced it was joining Nebius on 10 February 2026; the acquisition closed on 19 February 2026, making Tavily a wholly owned subsidiary [VF: A3-S084, A3-S085, V1-S041]. Nebius's Q1 2026 filing gives a fair value of US$189.7M plus an ARR-based earnout [VF: A3-S086]. Tavily says its API, data policies and zero data retention are unchanged [VF: A3-S084].
- *Certifications and access:* the Trust Center states a SOC 2 Type II report by an independent auditor, available on request [VF: B-L4-S005]. Teams have Owner, Admin and Member roles [VF: B-L4-S006]. SSO was not found [NPV]. The Enterprise plan includes uptime and support SLAs [VF: A3-S088].
- *Pricing:* 1,000 free credits per month, then US$0.008 per credit pay-as-you-go [VF: A3-S088].
- *Strengths:* the SDK accepts a custom HTTP session so traffic can be proxied through the firm's gateway [VF: A3-S009]. That is the right design for egress control [AJ].
- *Limitations:* no EU processing region was found [VF: A3-S088]. Its roadmap is now tied to a neocloud provider [AJ].
- *Choose when:* you want search plus extraction and crawling in one API, proxied through your gateway [AJ].
- *Avoid when:* you need EU processing or roadmap certainty independent of Nebius [AJ].
- *Competitors:* Exa, Firecrawl (L8).
- *FS note:* refresh third-party due diligence after the change of control and plan any contract change around PS7/26 notification lead times [Rec].
- **Tier: Tactical. Flag: Acquired.**

**Browserbase.**
- *What it is now:* managed headless-browser infrastructure for agents. Sessions are driven by Playwright or Puppeteer over CDP, and Stagehand (MIT) adds AI-driven interaction and extraction [VF: A3-S013, A3-S068]. The Python SDK is 1.20.0 (24 September 2026) and Stagehand 4.1.0 (9 September 2026) [VF: A3-S013, A3-S076]. The standalone MCP server repository is archived [VF: A3-S054, V1-S081].
- *Certifications and residency:* SOC 2 Type II reports for 2025 and 2026, a 2026 penetration test, HIPAA with a BAA on Scale or Enterprise, a DPA, and US, EU or Asia residency controls for large enterprise customers [VF: A3-S102].
- *Access and logging:* SAML 2.0 SSO on Enterprise, configured with Browserbase support [VF: B-L4-S004]. Session recordings can be disabled, and on Enterprise they go to the customer's own S3 bucket [VF: B-L4-S004]. An admin audit log of member actions was not found [NPV].
- *Deployment:* SaaS, with VPC connectivity and private-cloud options for large enterprise customers [VF: A3-S102].
- *Strengths:* isolated remote browsers with recordings under the customer's retention [AJ].
- *Limitations:* the browser service is proprietary [VF: A3-S013]. Plan naming for SSO and the BAA is inconsistent across its pages [VF: B-L4-S004, A3-S102].
- *Choose when:* an agent must operate a website that has no API [AJ].
- *Avoid when:* an API or a read-only data tool exists; browser automation is the most fragile and least auditable way to reach a system [AJ].
- *Competitors:* self-hosted Playwright in your own sandbox, Firecrawl and Apify browser features (L8).
- *FS note:* allow-list target domains and never give the browser session credentials to client-facing systems [Rec].
- **Tier: Tactical. No flag.**

**E2B.**
- *What it is now:* sandboxes for AI-generated code, each a Firecracker microVM with its own cgroup and network namespace, a per-sandbox egress firewall with domain allow and deny lists, short-lived workload identity tokens, and secrets that never cross the API, logs or spans [VF: A3-S062]. `e2b` 2.53.1 and `e2b-code-interpreter` 2.10.3 were released on 6 October 2026 [VF: A3-S007]. The runtime (control plane, orchestrator, in-VM agent) is Apache-2.0 and the SDK MIT [VF: A3-S007, A3-S062].
- *Deployment:* E2B Cloud (US default; EU and APAC on Pro and above, enabled by support; regions do not share state); BYOC on AWS and GCP keeping traffic and logs in the customer VPC; dedicated deployments in the customer's account. Azure BYOC appears on the Enterprise page but not in the docs [VF: A3-S120, A3-S104, A3-S062, V1-S096]. Self-hosting is for evaluation; the vendor says it is not a production pattern [VF: A3-S062].
- *Certifications:* SOC 2 Type II covering E2B software and the control plane (not the customer's BYOC account), HIPAA BAA on Enterprise, penetration test and DPA [VF: A3-S104, A3-S120, V1-S096].
- *Access control:* SSO, SCIM and RBAC are listed as "planned" on an Enterprise page about 437 days old; team access works through workspace and project membership; lifecycle events are retained for 7 days by default [VF: B-L4-S003, A3-S120].
- *Pricing:* Pro US$150 per month plus usage; Enterprise from a US$3,000 monthly minimum; per-second billing [VF: A3-S104].
- *Strengths:* the strongest isolation and egress model among the runtimes reviewed, with an open-source runtime as an exit route [AJ].
- *Limitations:* enterprise identity controls are not yet evidenced [VF: B-L4-S003].
- *Choose when:* any generated code must run, including derived calculations [AJ].
- *Avoid when:* you need SSO and RBAC on the console today and cannot compensate with BYOC and your cloud's IAM [AJ].
- *Competitors:* AgentCore and LangSmith sandboxes [VF: A1-S039]; Daytona and Modal are not profiled [NPV].
- *FS note:* use BYOC or the EU region, default-deny egress, and treat sandbox outputs as unverified until reconciled [Rec].
- **Tier: Tactical. No flag.** It is the reference pattern for the sandbox; enterprise identity controls keep it short of Strategic [AJ].

**Amazon Bedrock AgentCore Gateway and Identity (AWS).**
- *What it is now:* Gateway turns APIs (OpenAPI, Smithy), Lambda functions and existing MCP servers into MCP tools behind one endpoint, with IAM or custom JWT inbound authentication; Identity provides identity-aware authorisation, a refresh-token vault and OAuth integrations [VF: A3-S047, A6-S021, A6-S074]. AgentCore reached GA in October 2025; three-legged OAuth for MCP targets and VPC egress for Gateway and Identity followed in April 2026 [VF: A3-S047, A3-S048]. Gateway supports MCP 2026-07-28, 2025-11-25, 2025-06-18 and 2025-03-26 [VF: A6-S105].
- *Overlap:* the same service is profiled in C1 (`C1-aws-agentcore-gateway`). This record covers the Gateway-plus-Identity pair as an L4 governance component [AJ].
- *Policy:* AgentCore Policy (GA 3 March 2026, 13 Regions including Ireland) attaches a Cedar engine to a Gateway, evaluates every tool call before execution, filters denied tools from `tools/list`, and logs decisions to CloudWatch [VF: A6-S026, V2-S033].
- *Certifications:* AWS lists AgentCore in SOC 1, 2 and 3 scope [VF: B-L4-S001] and against ISO 27001, 27017, 27018 and 27701; one AWS page says AgentCore "aligns" with these programmes pending third-party review, so the ISO scope should be confirmed in AWS Artifact [VF: B-L4-S002]. The token vault supports a customer-managed KMS key [VF: A6-S074].
- *Pricing:* US$0.005 per 1,000 Gateway API invocations and US$0.02 per 100 tools indexed per month [VF: A6-S021].
- *Strengths:* the most complete managed implementation of the H3 sub-layer found: tool conversion, inbound identity, outbound credential vault and pre-execution policy in one service [AJ].
- *Limitations:* AWS only, with no self-hosted option [VF: A3-S047]. Enterprise controls are presumed from the AWS platform (CP2 Q1); confirm per service [AJ].
- *Choose when:* AWS is the primary agent platform [AJ].
- *Avoid when:* tools and agents span several clouds and you want one policy point; use a cloud-neutral gateway (agentgateway, Kong) instead [VF: A6-S061, A6-S016] [AJ].
- *Competitors:* Azure APIM AI gateway, Apigee, Kong AI Gateway, agentgateway (C1); Composio.
- *FS note:* AWS EMEA SARL is a designated critical third party under both DORA and the UK CTP regime, so this service sits inside an already overseen relationship [VF: R-DORA, R-UK-CTP]; it adds to AWS concentration [AJ].
- **Tier: Strategic, conditional: where AWS is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. No flag.** FS 3.45. It is AWS's lead managed tool gateway and agent identity service; AWS-only deployment (2) is accepted under rule 11 because the condition is an existing platform commitment. The same tier applies to the same service in C1, and to AgentCore Memory (L5) and Bedrock Guardrails (C2) [AJ].

### 4.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L4-mcp | 4 | 3 | 2 | 5 | 5 | 3 | 4 | 4 | 3.70 | 3.55 | Strategic |
| L4-a2a | 3 | 3 | 3 | 5 | 4 | 3 | 4 | 5 | 3.60 | 3.70 | Strategic |
| L4-agent-skills | 3 | 2 | 2 | 5 | 4 | 2 | 5 | 3 | 3.20 | 3.00 | Tactical |
| L4-composio | 4 | 3 | 2 | 4 | 4 | 2 | 3 | 2 | 3.15 | 2.90 | Experimental |
| L4-exa | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 3 | 2.70 | 2.70 | Tactical |
| L4-tavily | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 2 | 2.65 | 2.55 | Tactical |
| L4-browserbase | 4 | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 3.35 | 3.35 | Tactical |
| L4-e2b | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 4 | 3.35 | 3.35 | Tactical |
| L4-aws-agentcore-gateway-identity | 4 | 4 | 4 | 2 | 4 | 3 | 4 | 3 | 3.55 | 3.45 | Strategic |

**Scoring notes [AJ]:**
- *Open specifications (rule 2).* MCP, A2A and Agent Skills were scored on project hygiene and on what they enable in the firm's estate, capped at 4. MCP security is 2 (it was 3 before the CP3 review): authorisation is optional, tool definitions cannot be signed, tool poisoning is a documented attack class, and the TypeScript SDK had several High advisories in 2026, one of which sent OAuth credentials to an authorisation server chosen by the MCP server [VF: A3-S055, A3-S023, B-REVA-S006]. Advisories are published with fixes, which is good hygiene, but on protocol integrity MCP sits below A2A, so the borderline call was resolved against the Anthropic-originated item. A2A is 3 because card signing is optional and delegated authority has no revocation semantics; Agent Skills is 2 because skills carry executable code with no signing or provenance.
- *Evidence caps.* Composio security is capped at 2: V1 §4 lists its security claims as vendor marketing only, and the May 2026 incident would independently hold it at 2. E2B enterprise readiness is capped at 2: SSO, SCIM and RBAC are "planned" and no customer audit log was found (B-L4-S003). Tavily (RBAC roles, B-L4-S006) and Browserbase (SAML SSO, B-L4-S004) were lifted to 3 under CP2 rule 7 by one verified control each.
- *Hyperscaler presumption (rule 6).* AgentCore enterprise readiness is 4: platform controls presumed (CP2 Q1); confirm per service. Security is 4, not 5, because the ISO wording is inconsistent across AWS pages (rule 8). At the CP3 review, deployment fell from 3 to 2 (AWS-managed only) and maturity from 4 to 3 (one year of GA), to match the same service in C1 and AgentCore Memory in L5.
- *Deployment 1.* Exa and Tavily are SaaS-only with no processing region choice found.
- *Ownership change (rule 3).* Tavily's lock-in was reduced by 1 for the Nebius acquisition.
- *Tiers (CP3 decisions).* The reader set the protocol tiers at Checkpoint 3 (CP3 Q1). MCP is Strategic, conditional at 3.55 FS: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions; it is one decision with the C4 authorisation profile. A2A is Strategic, conditional at 3.70 FS: only where cross-team or cross-vendor agent delegation is in scope. Criterion scores were not changed by either decision. AgentCore Gateway and Identity is Strategic, conditional: where AWS is your primary cloud, under rubric rule 10 (CP3 Q2), as AWS's lead service in this category; the same service in C1 has the same tier.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| MCP | MIT specification and SDKs [VF: A3-S058, A3-S011] | Open specification; implementations anywhere [AJ] | Not applicable (specification) | In-estate when self-hosted [AJ] | AAIF / Linux Foundation since 9 Dec 2025; Anthropic-originated [VF: A3-S018] |
| A2A | Apache-2.0 [VF: A3-S075] | Open specification [AJ] | Not applicable | In-estate when self-hosted [AJ] | AAIF Growth Stage project, Aug 2026; eight-company TSC [VF: A3-S116, A3-S065] |
| Agent Skills | Apache-2.0 code; CC-BY-4.0 docs [VF: A3-S061] | Plain files in any client [VF: A3-S061] | Not applicable | Not applicable | Anthropic-maintained; no neutral body [VF: A3-S115, V1-S046] |
| Composio | SDK MIT; platform proprietary [VF: A3-S067, A3-S063] | SaaS (US), VPC, self-host, on-prem (Enterprise) [VF: A3-S098, A3-S119] | Vendor-stated SOC 2 Type II, ISO 27001 [VF: A3-S098]; May 2026 incident [VF: B-L4-S007] | Self-host only [VF: A3-S119] | Independent; US$25M Series A [R: A3-S099] |
| Exa | SDK MIT; API proprietary [VF: A3-S010] | SaaS [VF: A3-S010] | SOC 2 Type II; HIPAA BAA [VF: A3-S100] | None found; SCCs [VF: A3-S121] | Independent; Series C May 2026 [R: A3-S101] |
| Tavily | JS SDK MIT; API proprietary [VF: A3-S083] | SaaS [VF: A3-S009] | SOC 2 Type II (Trust Center) [VF: B-L4-S005] | None found [VF: A3-S088] | Nebius, closed 19 Feb 2026 [VF: V1-S041] |
| Browserbase | SDK Apache-2.0; Stagehand MIT; service proprietary [VF: A3-S013, A3-S068] | SaaS; VPC and private cloud for large enterprise [VF: A3-S102] | SOC 2 Type II; HIPAA BAA [VF: A3-S102] | EU residency for large enterprise [VF: A3-S102] | Independent; US$40M Series B [R: A3-S103] |
| E2B | Runtime Apache-2.0; SDK MIT [VF: A3-S062, A3-S007] | Cloud, BYOC (AWS, GCP), dedicated [VF: A3-S120, A3-S062] | SOC 2 Type II (control plane); HIPAA BAA [VF: A3-S104] | EU region (Pro+) [VF: A3-S120] | Independent; US$21M Series A [VF: A3-S105] |
| AgentCore Gateway + Identity | Proprietary [VF: A3-S047] | AWS managed; VPC, PrivateLink [VF: A3-S047, A3-S048] | SOC 1/2/3 scope; ISO listed (wording varies) [VF: B-L4-S001, B-L4-S002] | Policy in Ireland; Gateway regions not verified [VF: A6-S026] [NPV] | AWS [VF: A3-S047] |

### 4.9 Decision tree

```text
STEP 0 [Rec] (not optional): one tool gateway (L4 governance; often the C1 product) with
authorisation mandatory, a private allow-listed registry, hash-pinned tool definitions,
default-deny policy (Cedar or OPA), vault-issued outbound credentials (C7), OTel spans (L9).

STEP 1 [Rec]: How does the agent reach this capability?
  Internal system of record or calculation engine?
  ├─ Yes → Build a READ-ONLY MCP server (or OpenAPI tool) owned by the system's team.
  │        Write needed? → separate tool, separate approval, human confirmation step (L3).
  └─ No  → SaaS application?
           ├─ Yes → Does the user's own access matter (per-user data)?
           │        ├─ Yes → Per-user delegated OAuth via EMA / token exchange (C4);
           │        │        credential vault in your estate. Broker (Composio) only if
           │        │        self-hosted and the data are not client data.
           │        └─ No  → Named agent identity with least-privilege scope.
           └─ No  → Public web?  → STEP 3.   Code to run? → STEP 4.   Another agent? → STEP 5.

STEP 2 [Rec]: Which gateway?
  AWS is the agent platform          → AgentCore Gateway + Identity + Policy
  Azure / Microsoft estate           → APIM AI gateway + Entra Agent ID (see C1, C4)
  Multi-cloud or self-hosted needed  → agentgateway or Kong AI Gateway (see C1)
  (Re-assess when MCP agent-identity work, DPoP and WIF, is published.)

STEP 3 [Rec]: Web search or browsing
  Could the query or page context contain client, holdings or deal data?
  ├─ Yes → Do not use external search. Use approved internal sources (L6–L8).
  └─ No  → Search API via egress proxy + DLP, ZDR enabled:
           EU processing required? → none found for Exa/Tavily; use L8 self-hosted crawl.
           Otherwise              → Exa (independent) or Tavily (Nebius-owned).
           Site has no API and must be operated? → Browserbase (domain allow-list,
           recordings to own bucket) or self-hosted Playwright in a sandbox.

STEP 4 [Rec]: Code execution
  Generated code at all? → microVM sandbox, default-deny egress, no standing secrets:
    E2B BYOC (AWS/GCP) or EU region; AgentCore or LangSmith sandboxes if already on them.
  Result is a figure that will be published? → reconcile to the authoritative engine (L9).

STEP 5 [Rec]: Agent-to-agent
  Can a deterministic workflow (L3) call tools instead? → Yes: do that.
  Otherwise → A2A 1.0 with signed Agent Cards verified, scoped and revocable delegation,
              through a gateway that understands A2A (agentgateway, Kong, APIM).

STEP 6 [Rec]: Packaging procedures
  House procedures for several agent clients → Agent Skills, internally authored,
  Git-reviewed, no scripts; alternative: C5 prompt packages or AGENTS.md.
```

### 4.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Agent-to-tool protocol (MCP) | **Acceptable** | MIT specification under a foundation, with Tier 1 SDKs in four languages [VF: A3-S058, A3-S018, A3-S015]; maintainer concentration is a governance risk, not a switching cost [AJ] | Keep tool contracts in your repository as MCP or OpenAPI schemas |
| Agent-to-agent protocol (A2A) | **Acceptable** | Apache-2.0, eight-company TSC [VF: A3-S075, A3-S065] | Gateway with A2A support |
| Tool gateway and policy | **Manageable** | Proprietary gateways (AgentCore, APIM) speak MCP on both sides [VF: A6-S021, A6-S053]; policies are the switching cost | Policies in Cedar or OPA kept in Git [VF: A6-S045, A6-S046] |
| Credential custody (user OAuth tokens) | **Unacceptable in a third party's multi-tenant cloud** | A broker that holds every user's tokens is a concentrated breach target and hard to exit, as the Composio incident shows [VF: B-L4-S007] [AJ] | Vault in your estate (C7); EMA or token exchange (C4) |
| Search APIs | **Acceptable** | Stateless calls; easy to swap behind one interface [AJ] | One internal "web search" tool fronting any provider |
| Browser service | **Manageable** | Playwright, CDP and Stagehand (MIT) are portable [VF: A3-S013, A3-S068] | Scripts in Playwright; avoid vendor-only features |
| Code sandbox | **Manageable** | E2B runtime is Apache-2.0, so an exit to self-hosting exists [VF: A3-S062] | One "run code" tool interface |
| Skills format | **Acceptable for the format; governance risk** | Plain Markdown folders, but an Anthropic-maintained specification [VF: A3-S061, A3-S115] | Keep skills in Git; no vendor-only discovery paths |
| Public MCP Registry | **Do not depend on it** | Preview, API v0.1, moderation by denylisting [VF: A3-S019, A3-S042] | Private registry (API Center, GitHub enterprise registry) [VF: A3-S043, A3-S044] |

### 4.11 Regulated FS lens (POV 2)

**Model risk.**
- *SS1/23.* SS1/23 covers vendor models and requires independent validation (Principle 4); Principle 1.1(b) allows its MRM aspects to apply to material, complex deterministic quantitative methods that are not models [VF: R-PRA-SS123, A8-S008, A8-S061]. An attribution engine is such a method or a model in its own right [AJ]. The consequence for L4: an agent must call the validated engine through a tool and never recompute what the engine produces, or the firm has created an unvalidated shadow model [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001, A8-S002]. The firm's own tool-governance standard therefore has to stand on its own [AJ].
- *Validation scope.* The tool set exposed to an agent is part of the system being validated. Adding a tool is a material change that should trigger re-testing [AJ].

**EU AI Act.**
- *Deployer duties.* Article 26 requires deployers of high-risk systems to keep logs for at least six months and monitor operation; Annex III duties apply from 2 December 2027 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011]. Most asset-management uses, including attribution commentary, are not Annex III [AJ].
- *Practical effect.* Tool calls are the actions an auditor will ask about first. Log them to Article 26 grade regardless of classification [Rec].

**DORA, the UK CTP regime and outsourcing.**
- *Every SaaS tool is an ICT third-party service.* DORA requires a register of information covering all ICT third-party arrangements, with Article 30 terms where a critical or important function is supported [VF: R-DORA, A8-S021]. Exa, Tavily, Browserbase, E2B Cloud and Composio each belong in the register [AJ].
- *Designated providers.* AWS, Google Cloud and Microsoft entities are designated under DORA and the UK CTP regime; no AI model provider is [VF: R-DORA, R-UK-CTP, A8-S021, A8-S023]. None of the independent tool vendors in this layer is designated, so oversight rests entirely on the firm [AJ].
- *Notifications.* PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. Tavily's change of control and any switch away from a broker should be planned with that lead time [Rec].
- *Exit.* SS2/21 expects documented, tested exit plans [VF: R-PRA-SS221, A8-S048]. A broker that holds end-user tokens has the hardest exit in this layer [AJ].

**Residency, data egress and auditability.**
- *Search egress.* FG16/5 expects data location and effective access for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. No EU processing region was found for Exa or Tavily [VF: A3-S121, A3-S088], and Composio's managed cloud is US-hosted [VF: A3-S119]. EU-to-US transfers rely on the Data Privacy Framework or SCCs, and appeal C-703/25 P is pending [VF: R-DATA-TRANSFERS, A8-S053]. A search query can disclose confidential intent (a planned trade, a client's concern) even without personal data, so the control is "no client context in outbound queries", enforced at the egress proxy [AJ].
- *Auditability.* Each tool call needs: subject, agent identity, tool, definition hash, arguments (or their hash), policy decision, result reference and timestamp [AJ].

**Least privilege for non-human actors.**
- *Supervisory direction.* The NCCoE published a concept paper on software and AI agent identity and authorisation in February 2026, and CAISI's January 2026 agent-security RFI informs a planned SP 800-53 control overlay for AI agent systems [VF: R-NIST-AIRMF, A8-S006]. The OCC observes banks adopting agentic AI in limited use cases "with guardrails and human-in-the-loop accountability" [VF: R-US-AGENCY-AI, A8-S004].
- *What to do.* Give each agent its own identity with an owner and sponsor, as Entra Agent ID models it [VF: A6-S057], and grant tools to that identity, never to a shared service account [Rec].

**Concentration.** IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058]. In L4 the concentration is in governance, not in vendors: both Lead Maintainers of MCP are Anthropic staff [VF: A3-S082], and Agent Skills is Anthropic-maintained [VF: A3-S115]. A firm that also uses Anthropic models should note that one vendor then influences the model, the tool protocol and the skills format [AJ]. This author is an Anthropic model, and the point applies in full [AJ].

**Standards.**
- *OWASP.* Map tool controls to the Top 10 for Agentic Applications for 2026, which starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042] and includes ASI02 tool misuse, ASI03 identity and privilege abuse and ASI04 agentic supply chain [VF: A3-S046]. Map model-side controls to the Top 10 for LLM Applications 2026, operative from August–September 2026 [VF: R-OWASP-LLM, V2-S056]; Excessive Agency is reported as third in it [R: A8-S041]. Use OWASP's MCP Top 10 for server reviews [VF: A3-S045].
- *NIST and ISO.* NIST AI RMF and AI 600-1 give the risk taxonomy [VF: R-NIST-AIRMF, A8-S043, A8-S044]; ISO/IEC 42001 gives the management system [VF: R-ISO-42001, A8-S045].
- *ESMA.* ESMA expects "ex-ante input controls and frequent ex-post output controls" [VF: R-INTL-AI-ASSETMGMT, A8-S059]. Gateway policy is the ex-ante control on actions [AJ].

### 4.12 Worked-example slice (POV 3)

**What the commentary agent needs from L4 [AJ].** The agent drafts the monthly Brinson-style attribution commentary (allocation, selection, currency, benchmark-relative return) for a generic multi-asset fund. It is a deterministic workflow, not a free agent, and it needs exactly four tools:

1. **`get_attribution_results` (read-only MCP tool onto the attribution engine output).** Parameters: fund identifier, period, attribution model version. Returns the engine's published effects with a snapshot identifier and hash. The tool reads only the engine's approved output store; it cannot trigger a re-run or change parameters. The snapshot hash goes into the trace, so L9 can compare every figure in the draft with it [AJ].
2. **`get_fund_reference_data` (read-only MCP tool onto the fund data store).** Benchmark name, share-class currencies, sector and asset-class labels, and period dates. No client identifiers are returned [AJ].
3. **`calculate` (sandboxed, E2B-style).** Used only if the draft needs a derived figure the engine does not publish, such as a sum of two effects or a contribution in basis points. Code runs in a microVM with no network egress and no credentials, on inputs passed from tool 1. The result is labelled "derived" and reconciled to the engine's totals before use; if reconciliation fails, the workflow stops and asks the analyst [AJ].
4. **`search_approved_commentary` (retrieval, L6–L8).** Prior commentaries and the house style guide from the firm's own index [AJ].

**How the calls are governed.**
- The analyst signs in; the IdP issues an ID-JAG through EMA (or equivalent token exchange), so each tool call carries the analyst as subject and the commentary agent as actor [AJ].
- The gateway allow-lists exactly these four tools for this agent identity, checks each definition hash, and applies a Cedar or OPA policy: fund identifiers must be within the analyst's entitlements [AJ].
- Tool servers are owned by the data and engine teams, versioned in Git and change-controlled; adding a tool or a parameter is a model change under the firm's MRM process [AJ].
- Every call produces an audit record (subject, actor, tool, hash, arguments, decision, snapshot ID) that joins the C8 evidence pack [AJ].

**What L4 must never do [AJ]:**
- expose any write, update or publish tool to the drafting agent; publication happens after human approval, outside the agent
- let the model compute a figure that the engine already produces, or use a sandbox result that has not been reconciled to the engine
- send fund names, holdings, client names or the commentary's purpose to an external web search or browser service
- install a community MCP server or a third-party skill into this workflow
- use a shared service account or a long-lived key; credentials are issued per call from the vault
- let a tool description or annotation decide the tool's risk class

### 4.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| "Tools and protocols" row of eight tiles | Protocols under foundations; gateways in C1 now carry MCP and A2A traffic [VF: A3-S018, A3-S116, A6-S061, A6-S016] | L4 split into connectivity (protocols, tools, runtimes) and a tool-governance sub-layer bound to C1 and C4 [Rec] |
| MCP "tools standard" | Spec 2026-07-28: stateless, header routing, DCR deprecated, EMA stable; authorisation optional; Registry preview v0.1; AAIF-governed [VF: A3-S015, A3-S057, A3-S017, A3-S055, A3-S036, A3-S018] | Strategic, conditional: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions (CP3 Q1); alternative: OpenAPI tools via gateway [Rec] |
| A2A "agent-to-agent" | 1.0.0 (12 Mar 2026), 1.0.1; AAIF Growth Stage; optional card signing [VF: A3-S079, A3-S117, A3-S078] | Strategic, conditional: where cross-team or cross-vendor agent delegation is in scope (CP3 Q1); signed cards required [Rec] |
| Agent Skills "reusable skills" | Open format, 46 clients; Anthropic-maintained, no neutral body, no versions, no signing [VF: A3-S113, A3-S115, V1-S046, A3-S037] | Tactical: internal, script-free skills only; alternative: C5 packages or AGENTS.md [Rec] |
| Composio "integrations" | Broker plus MCP gateway; US-hosted cloud; May 2026 token-exposure incident [VF: A3-S063, A3-S119, B-L4-S007] | Experimental; self-hosted only, never for client data [Rec] |
| Exa "search API" | Search API with structured output; SOC 2 Type II; no EU region found [VF: A3-S010, A3-S100, A3-S121] | Tactical, via egress proxy with DLP, non-confidential queries only [Rec] |
| Tavily "search API" | Nebius-owned since 19 Feb 2026 [VF: V1-S041] | Tactical; refresh due diligence [Rec] |
| Browserbase "cloud browsers" | Browsers plus Stagehand; standalone MCP server archived [VF: A3-S013, A3-S054] | Tactical, only where no API exists [Rec] |
| E2B "code sandboxes" | Firecracker microVMs, egress firewall, Apache-2.0 runtime, BYOC [VF: A3-S062, A3-S120] | Tactical; reference sandbox pattern for derived calculations [Rec] |
| (absent) | AgentCore Gateway + Identity + Policy: managed tool gateway, token vault, Cedar policy [VF: A3-S047, A6-S026] | Strategic, conditional: where AWS is your primary cloud (CP3 Q2); cloud-neutral alternatives in C1 [Rec] |

**H3 (tools and protocols need an explicit agent identity, authorisation and tool-governance sub-layer). Provisional view; verdict in synthesis.**

The evidence supports the hypothesis on five counts.

- **The protocol has made room for it but does not supply it.** MCP 2026-07-28 exposes method and tool names in headers for gateways, deprecates Dynamic Client Registration and tightens issuer validation [VF: A3-S015, A3-S057]. Authorisation remains optional and annotations remain hints [VF: A3-S055, A3-S020]. Enforcement therefore has to live somewhere outside the protocol [AJ].
- **Enterprise identity is arriving as an extension.** EMA is stable and Okta Agent SSO is GA [VF: A3-S017, V2-S035]. The MCP roadmap names agent identity (DPoP, Workload Identity Federation, token exchange) as a priority and admits that today's model assumes a person approving access in a browser [VF: A3-S016].
- **There is still no trustworthy public allow-list.** The official Registry is preview at API v0.1 and moderates by denylisting [VF: A3-S019, A3-S042, A3-S036]. Enterprises are building private registries in GitHub and Azure API Center [VF: A3-S043, A3-S044].
- **Products for the sub-layer now exist.** AgentCore Gateway, Identity and Policy implement it as a managed service [VF: A3-S047, A6-S026]. The C1 gateways (Kong, agentgateway, APIM, LiteLLM) govern MCP and A2A traffic [VF: A6-S016, A6-S061, A6-S053, A6-S051], and Vault Enterprise has GA agentic IAM [VF: A7-S034].
- **A2A leaves the same gap.** Card signing is optional and delegated-authority semantics are undefined [VF: A3-S078].

The counter-evidence is that the products implementing the sub-layer are the C1 gateways and C4 identity services, not new L4 products. A separate box in L4 could duplicate them [AJ].

**Provisional recommendation.** Keep H3, implemented as a **tool-governance sub-layer inside L4** that is the enforcement point (gateway, private registry, definition pinning, policy evaluation, audit), with policy and identity decisions owned by C4, credentials by C7, and the gateway product shared with C1 [AJ]. Draw it between L3 and the tools, so that no tool is reachable except through it [AJ]. **Provisional; verdict in synthesis.**
