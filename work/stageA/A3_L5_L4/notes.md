# Stage A notes: stream A3 (L5 Memory, L4 Tools, protocols and connectivity)

Research date: 7 October 2026. All source IDs refer to `work/stageA/A3_L5_L4/sources.csv`. Archive: `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A3/`.

**Conflict-of-interest disclosure.** The author is an Anthropic model. MCP and Agent Skills originated at Anthropic. Both were researched to the same standard as the other products, and independent criticism is recorded below (H3).

**Research-environment caveats.**
- The shared web-search budget (200 calls per turn, shared by all agents) ran out early in this stream's run. Later facts therefore come only from hosts the egress policy allowed:
  - pypi.org and registry.npmjs.org (package metadata and READMEs)
  - raw.githubusercontent.com (canonical raw files of public repositories; not a mirror or cache)
  - blog.modelcontextprotocol.io and registry.modelcontextprotocol.io
  - anthropic.com, claude.com and docs.claude.com
  - repository metadata from the GitHub MCP tool
- Vendor sites, trust centres and pricing pages could not be fetched directly: getzep.com, letta.com, cognee.ai, supermemory.ai, composio.dev, exa.ai, tavily.com, browserbase.com, e2b.dev, docs.aws.amazon.com, docs.cloud.google.com and sec.gov.
- **Gap-filling pass (7 Oct 2026, fresh search budget).** Sources A3-S084 to A3-S122 were added through targeted `WebSearch` with `allowed_domains` set to vendor sites and trust centres. They are recorded as search extracts (confidence capped at medium) or snapshots where the host was fetchable.

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| Mem0 – memory layer | Mem0 v2.x (mem0ai 2.2.1, 25 Sep 2026); open core. New April 2026 algorithm uses ADD-only extraction. On 14 Apr 2026, open-source v2.0.0 removed the graph stores, so graph memory is now Platform-only. | No change (scope shift: OSS and Platform diverge) | A3-S001, A3-S053, A3-S080, A3-S081 |
| Zep – graph memory | Zep is a managed "context graph" platform with a proprietary Context Graph Engine. Graphiti (Apache-2.0, 0.30.2) is the open-source core. Zep Community Edition is deprecated. | Deprecated (Community Edition); otherwise No change | A3-S003, A3-S059 |
| Letta – stateful agents | Letta (formerly MemGPT) has pivoted to Letta Code (0.34.4, 4 Oct 2026), a stateful agent harness with Letta Cloud, per the "Letta's Next Phase" post (Mar 2026). The V1 API server is retired to an archive branch, and the PyPI package `letta` is now the CLI. | Superseded (V1 server) / Mispositioned (agent harness, not a memory layer) | A3-S004, A3-S060, A3-S073, A3-S077, A3-S093 |
| Cognee – knowledge graphs | Cognee 1.6.3 (7 Oct 2026). Apache-2.0, with a licensed production Postgres graph and Cognee Cloud. | No change | A3-S005 |
| Supermemory – memory API | Supermemory v5 namespace-first API (SDK 5.0.0, 6 Oct 2026). Adds RAG, connectors and a self-hosted "Supermemory local". | No change (scope broader than memory) | A3-S012, A3-S064 |
| LangMem – long-term | LangMem 0.0.30. No PyPI release since 27 Oct 2025; it is a LangGraph library, not a service. | Not publicly verified (activity status) / Mispositioned (library inside L3) | A3-S006, A3-S054 |
| MCP – tools standard | Spec 2026-07-28 (stateless core). Governed by the Agentic AI Foundation (Linux Foundation) since 9 Dec 2025. Enterprise-Managed Authorization extension is stable. Registry is still preview (API v0.1). | No change (governance moved to a foundation) | A3-S015, A3-S018, A3-S017, A3-S036, A3-S042 |
| A2A – agent-to-agent | A2A 1.0.0 (12 Mar 2026) and 1.0.1 (26 May 2026), under the Linux Foundation; joined AAIF in Aug 2026. IBM ACP was merged into A2A in Aug 2025. | No change | A3-S078, A3-S079, A3-S040, A3-S032 |
| Agent Skills – reusable skills | Open format (SKILL.md), published as an open standard on 18 Dec 2025. Adopted by OpenAI Codex, Gemini CLI and others. Governance charter not found. | No change | A3-S029, A3-S061, A3-S033, A3-S034 |
| Composio – integrations | Composio SDK 0.25.0, with 2.0 in beta. Offers 1000+ toolkits, per-user sessions and auth brokering. | No change | A3-S008, A3-S063 |
| Exa – search API | Exa search API (exa-py 2.25.0, 1 Oct 2026). | No change | A3-S010 |
| Tavily – search API | Tavily API (tavily-python 0.8.5, 6 Oct 2026). Nebius announced the acquisition on 10 Feb 2026 and accounts for it as completed: fair value US$189.7M plus an ARR earnout; the press reported US$275M. | Acquired | A3-S084, A3-S085, A3-S086, A3-S087, A3-S009 |
| Browserbase – cloud browsers | Browserbase SDK 1.20.0 plus Stagehand 4.1.0. Standalone MCP server repository archived. | No change | A3-S013, A3-S076, A3-S054 |
| E2B – code sandboxes | E2B SDK 2.53.1. Runtime (Firecracker microVMs) is open source under Apache-2.0. Dedicated in-customer-cloud deployments are available. | No change | A3-S007, A3-S062 |

## (b) Ambiguities owned

The inventory assigns no A-numbered ambiguities (A1–A19) to stream ③. Related clarifications:
- **"Agent Skills" (Anthropic-originated).** This is the SKILL.md open format at agentskills.io, not a product. Licence per the primary repository is Apache-2.0 for code and CC-BY-4.0 for docs [A3-S061]. Secondary sources say MIT [A3-S035]; the primary source was used.
- **Letta.** The graphic implies a memory product. Primary sources show an agent harness: the Letta V1 server is retired [A3-S060, A3-S073].
- **Zep.** The "graph memory" descriptor fits. The open-source path is now Graphiti only [A3-S003, A3-S059].

## (c) Hypothesis evidence

### H3: agent identity, authorisation and tool governance

**MCP authorisation specification (2026-07-28)**
- Authorisation is OPTIONAL for MCP implementations [A3-S055].
- When used:
  - Authorisation is based on OAuth 2.1 (draft-13), and the MCP server acts as the OAuth resource server [A3-S055].
  - Servers MUST implement Protected Resource Metadata (RFC 9728) [A3-S055].
  - Clients MUST implement Resource Indicators (RFC 8707), using the canonical server URI [A3-S055].
  - Servers MUST validate that tokens were issued for them as the audience [A3-S055].
  - PKCE is required [A3-S039].
- Token passthrough is explicitly forbidden, and confused-deputy risks are documented [A3-S056].
- Changes in 2026-07-28:
  - RFC 9207 issuer validation (SEP-2468) [A3-S057]
  - issuer-bound client credentials (SEP-2352) [A3-S057]
  - Dynamic Client Registration deprecated in favour of Client ID Metadata Documents [A3-S015, A3-S057]
- RFC 8707 has been mandatory for clients since 2025-06-18, to stop malicious servers obtaining tokens [A3-S039].

**Enterprise-Managed Authorization (EMA)**
- The extension was declared stable on 18 Jun 2026 [A3-S017].
- The IdP issues an Identity Assertion JWT Authorization Grant (ID-JAG) during SSO, which the client exchanges for an MCP access token. The aim is central policy and one audit trail, with no per-server consent [A3-S017].
- Okta (Cross App Access) is the first IdP [A3-S017].
- Clients: Anthropic's Claude products and VS Code [A3-S017].
- Servers: Asana, Atlassian, Canva, Figma, Granola, Linear and Supabase [A3-S017].

**MCP roadmap (22 Aug 2026)**
- Agent identity is a priority area [A3-S016]:
  - DPoP
  - Workload Identity Federation
  - ID-JAG
  - standard token exchange
  - work with the IETF OAuth and WIMSE working groups
- The roadmap states that today's model is "built around a person approving access in a browser" [A3-S016].

**Gateways**
- Spec 2026-07-28 requires `Mcp-Method`/`Mcp-Name` headers so that gateways, rate limiters and WAFs can route and authorise on headers [A3-S015].
- Ecosystem quotes name governance gateways or platforms [A3-S015]:
  - Microsoft Foundry toolbox: unified MCP endpoint "centralizing governance, identity, and observability"
  - FastMCP Horizon: "MCP governance platform"
  - Runlayer
  - AWS AgentCore
  - Cloudflare
- AWS AgentCore Gateway [A3-S047, A3-S048]:
  - fronts MCP servers with IAM or OAuth
  - three-legged OAuth for MCP targets reached GA in April 2026
  - VPC egress for Gateway and Identity
  - AgentCore Identity provides a refresh-token vault

**Registries and allow-listing**
- The official MCP Registry launched in preview on 8 Sep 2025. It supports public and private sub-registries, with moderation by denylisting [A3-S019].
- The API froze at v0.1 on 24 Oct 2025 [A3-S042].
- On 7 Oct 2026, `/v0.1/servers` responded and `/v0.2` and `/v1` returned 404, so no GA endpoint was observed [A3-S036, A3-S021].
- GitHub documents configuring an MCP registry for an organisation or enterprise in Copilot [A3-S043].
- Microsoft documents a private registry on Azure API Center, enforced in GitHub Copilot and VS Code [A3-S044].

**Tool annotations**
- Annotations (readOnly, destructive, idempotent, openWorld) are hints that clients MUST treat as untrusted unless the server is trusted [A3-S020].

**Independent criticism of MCP**
- MCPTox benchmark (45 live servers, 20 LLMs, AAAI 2026) [A3-S023]:
  - average tool-poisoning attack success 36.5%, peak 72.8%
  - more capable models were often more susceptible
- Cloud Security Alliance research notes (July 2026) [A3-S022]:
  - high-severity issues from mid-2025 to June 2026 in Cursor, Claude Code, Gemini CLI, GitHub Copilot and Amazon Q, where IDEs launch project-defined MCP servers with developer privileges and no isolation
  - a reported Microsoft disclosure (30 Jun 2026) of tool-description poisoning that exfiltrated an SSH key
  - attribution and dates are inconsistent across CSA notes
- OWASP MCP Top 10 [A3-S045]:
  - MCP03:2025 covers tool poisoning and schema poisoning
  - recommends signing tool manifests and pinning reviewed definitions with hashes (against rug pulls)
- Newer attack variants (MCP-ITP, ShareLock, Potemkin) and the argument that prompt-injection filtering plus OAuth correctness are insufficient [A3-S024].
- OWASP Top 10 for Agentic Applications 2026 (released Dec 2025) [A3-S046]:
  - ASI02 tool misuse
  - ASI03 identity and privilege abuse
  - ASI04 agentic supply chain
  - OWASP also runs an "Agentic Skills Top 10" project

**MCP governance**
- Anthropic donated MCP to AAIF (Linux Foundation) on 9 Dec 2025. The maintainer structure is unchanged, and AAIF does not set technical direction [A3-S018].
- Both Lead Maintainers are Anthropic staff. An AWS engineer joined the Core Maintainers in April 2026 [A3-S082].
- AAIF had 247 members by August 2026, including Visa and Wells Fargo as Gold members [A3-S041].

**A2A security model**
- Agent Cards MAY be signed with JWS (RFC 7515) over RFC 8785 canonical JSON. Clients SHOULD verify signatures when present [A3-S078, A3-S031].
- OAuth flows were modernised: device code and PKCE added, implicit and password flows removed [A3-S079].
- An authenticated extended Agent Card is available after the client authenticates [A3-S078].
- The protocol "does not define the scope, representation, validity, or revocation semantics" of authorisation obtained in the AUTH_REQUIRED state [A3-S078].
- The TSC has eight companies [A3-S065].
- A2A joined AAIF as a separate project with its own TSC. AAIF announced it on 17 Aug 2026, and the A2A blog of 27 Aug 2026 confirms acceptance as a Growth Stage project [A3-S116, A3-S117, A3-S040].

**Agent Skills supply-chain risk**
- Anthropic warns that malicious skills can exfiltrate data, and advises installing only from trusted sources and auditing bundled code [A3-S072].
- Gemini CLI documentation gives similar advice [A3-S034].
- No signing or provenance mechanism was found in the format [A3-S061, A3-S037].

**Composio as credential broker**
- Per-user sessions hold connected accounts. Toolkits, tools, auth configs and connected accounts can be restricted per session [A3-S008, A3-S063].

**E2B sandbox controls**
- One Firecracker microVM per sandbox [A3-S062].
- Egress firewall with domain allow and deny lists [A3-S062].
- Secrets never cross the API, logs or spans [A3-S062].
- Workload identity tokens [A3-S062].

**Vendors as MCP gateway or governance products**
- Composio markets an "MCP Gateway" with [A3-S119, A3-S098]:
  - SAML/OIDC SSO and SCIM
  - action-level policy-as-code
  - per-call audit logs, including denied calls
- Zep describes ABAC policies on memory reads and writes. Its audit logs cover web-app actions only [A3-S107].

**Not verified:** Microsoft Entra Agent ID, Okta/Auth0 for AI agents beyond EMA, and SPIFFE for agents (search budget exhausted; stream ⑥ also covers C4).

### H4: memory vs retrieval

**Storage underneath each product**
- **Mem0** [A3-S053, A3-S080, A3-S081]:
  - SQL database for facts, a third-party vector DB for embeddings and an entity store
  - OSS Python default is local Qdrant, with 14+ vector stores supported
  - graph backends (Neo4j, Memgraph, Kuzu, Apache AGE) removed from OSS on 14 Apr 2026; graph memory is Platform-only
  - Platform docs say entity extraction and linking run on all plans, while the graph dashboard requires Pro or Enterprise [A3-S050]
- **Zep/Graphiti** [A3-S003]:
  - Graphiti needs Neo4j, FalkorDB or Neptune (with OpenSearch Serverless for full text); Kuzu is deprecated
  - Zep Cloud uses a proprietary Context Graph Engine
- **Cognee** [A3-S005]:
  - defaults to SQLite, LanceDB and the "ladybug" graph package
  - optional Neo4j, Neptune and Postgres/PGVector
  - single-Postgres mode is a demo in OSS, with a licensed production version
- **Supermemory** [A3-S064]:
  - local build embeds a graph engine with local embeddings in a single data directory
- **LangMem** [A3-S006]:
  - persists via the LangGraph BaseStore; InMemoryStore loses data on restart
- **Letta** [A3-S073]:
  - memory blocks and all context tracked in a git-backed MemFS, with Letta Cloud as the default store

**Memory types as documented**
- Mem0 lists procedural memory (Python), memory expiration (`expiration_date`) and entity scoping (user/agent/run). No explicit episodic/semantic taxonomy was found in the docs [A3-S053, A3-S080].
- Graphiti stores "episodes" with provenance, plus facts with validity windows and bi-temporal tracking [A3-S003].
- Supermemory keeps user profiles (stable facts and recent activity) and memories [A3-S064].
- LangMem distinguishes hot-path memory tools from a background manager, and includes prompt refinement (procedural) [A3-S006].

**Retrieval convergence**
- Mem0 fuses semantic, BM25 and entity signals [A3-S001].
- Graphiti uses hybrid semantic, keyword and graph search [A3-S003].
- Supermemory's default "Hybrid" mode combines RAG and memory in one query, with connectors and OCR/transcription [A3-S064].
- Cognee retrieval selects graph, vector or code context [A3-S005].

**Deletion and retention**
- **Mem0** [A3-S080, A3-S053, A3-S081]:
  - delete, delete_all and per-memory history in OSS and Platform; Platform adds batch_delete (up to 1000)
  - `delete_linked` option on delete
  - memory decay (Platform)
  - OSS extraction is ADD-only, so memories accumulate rather than being overwritten
- **Graphiti** invalidates old facts rather than deleting them, keeping history [A3-S003].
- **Cognee** `forget` removes an item or dataset [A3-S005].
- **Supermemory** [A3-S012, A3-S064]:
  - `memories.forget`, `forget_matching` and namespace delete
  - automatic forgetting of expired facts
- **Anthropic memory tool** includes a `delete` command, and the developer executes it against their own storage [A3-S069].

**Built-in vendor and platform memory**
- **Anthropic memory tool** [A3-S069]:
  - client-side: Claude requests file operations under `/memories` and the application executes them on storage the developer controls
  - handlers must reject paths outside `/memories`
- **Claude app memory** [A3-S071]:
  - launched for Team/Enterprise on 11 Sep 2025, and for Pro/Max on 23 Oct 2025
  - project-scoped memory, a user-editable memory summary and incognito chats
  - Enterprise admins can disable memory
- **AWS AgentCore Memory** [A3-S047, A3-S048, A3-S111]:
  - GA October 2025, with a self-managed strategy for extraction and consolidation
  - VPC and PrivateLink supported; the AgentCore harness auto-provisions managed memory
  - short-term raw events with event expiry (7–365 days per the API reference; the stated minimum value conflicts)
  - long-term strategies: semantic, summary, user preference, episodic and custom
  - no built-in TTL for long-term records; AWS recommends a pruner using timestamp filters
  - DeleteMemoryRecord and BatchDeleteMemoryRecords; per-user erasure by listing and deleting the user's namespace records
  - deleting the memory resource removes all records; harness-managed memory cannot be deleted via the Memory APIs
- **Vertex AI Agent Engine Memory Bank** (newer docs: "Agent Platform Memory Bank") [A3-S108, A3-S109]:
  - public preview 8 Jul 2025, now GA (exact date not captured); billing from 28 Jan 2026
  - Gemini-based asynchronous extraction, with consolidation that resolves contradictions
  - immutable scope with exact-match retrieval and similarity search
  - optional TTL (default none; memory revisions 365 days)
  - delete by name and purge by filter with a dry run; consolidation may delete memories on a contradiction or an explicit "forget"
  - deleting the Agent Runtime instance deletes its built-in memories
- **OpenAI** [A3-S110]:
  - API: the Conversations API persists conversation state as a durable object, and Responses chains turns via previous_response_id
  - `store:false` is enforced for zero-data-retention (ZDR) organisations; no official default retention period for stored objects was found
  - ChatGPT memory can be switched off, and saved memories are stored separately from chats, so deleting a chat does not delete its memories
  - deleted memory logs may be kept for up to 30 days; turning off "reference chat history" schedules deletion within 30 days
  - Business and Enterprise workspace content is not used for training by default
- **Vendor-level erasure and retention features found in the gap-fill pass:**
  - Zep: Archive, right-to-be-forgotten and time-based purge [A3-S107]
  - Cognee: access, erasure and portability supported, with per-tenant Postgres in its cloud [A3-S095]
  - Supermemory: access and erasure workflows [A3-S122]

## (d) Products the graphic misses

**Added to products.json (`original_label: null`)**
- **L5: Amazon Bedrock AgentCore Memory.** Platform-native managed agent memory [A3-S047, A3-S048, A3-S111].
- **L5: Vertex AI Agent Engine Memory Bank.** Google platform-native managed memory [A3-S108, A3-S109]. The original docs URL is cited by link only, as the host is blocked [A3-S070].
- **L4: Amazon Bedrock AgentCore Gateway and Identity.** Managed MCP gateway and agent credential vault [A3-S047, A3-S048, A3-S015].

**Noted, not profiled (insufficient verified facts)**
- **Anthropic memory tool and Claude memory.** Model-vendor built-in memory [A3-S069, A3-S071]. Recorded as H4 evidence rather than a product record.
- **MCP gateways and governance platforms.** Microsoft Foundry toolbox, FastMCP Horizon, Runlayer [A3-S015]; Okta Cross App Access as the EMA IdP [A3-S017].
- **Private MCP registries.** Azure API Center and GitHub Copilot registry configuration [A3-S043, A3-S044].
- **Daytona, Modal and other sandboxes.** Not verified (no search budget).

## (e) Gaps: what could not be verified, and why

**Resolved in the gap-filling pass**
- **Tavily.** Acquired by Nebius: announced 10 Feb 2026 and treated as completed in Nebius's Q1 2026 filing [A3-S084, A3-S085, A3-S086]. The deal value conflicts: filing fair value US$189.7M versus the press figure of US$275M [A3-S087]. CB Insights dates it May 2026 (secondary).
- **A2A 1.0 date.** 12 Mar 2026 (changelog [A3-S079]); AAIF [A3-S116] and Google [A3-S026] also say March 2026. The Linux Foundation release of 9 Apr 2026 [A3-S025] is the first-anniversary announcement, not the release.
- **A2A move to AAIF.** AAIF announced it on 17 Aug 2026 [A3-S116], and the A2A blog confirmed it on 27 Aug 2026 [A3-S117]. No primary source supports the secondary "20 Aug" date [A3-S040].
- **MCP Registry GA.** Not reached. The working-group charter lists "Registry API v1 GA" as Ideating with no target date [A3-S114]. On 7 Oct 2026 the `/v0.1` path was live and `/v1` returned 404 [A3-S036].
- **Agent Skills governance and versioning.** The spec is a living document with no tagged releases [A3-S115]. Contributions are handled via GitHub Discussions, and listing requests are reviewed by the Anthropic team [A3-S112]. The maintainers are Anthropic employees, and AAIF onboarding has been proposed (issue #47, Sep 2026) but acceptance is not confirmed [A3-S115]. The showcase lists 46 clients [A3-S113].
- **Certifications, pricing and funding.** Now sourced for the products below. All of it comes from vendor pages via search extract, so confidence is medium at most.

| Product | Certifications | Pricing | Funding |
|---|---|---|---|
| Zep | SOC 2 Type II + HIPAA, Enterprise only [A3-S089, A3-S090] | Sourced [A3-S089] | No 2025–26 round found |
| Letta | No certification found [A3-S118] | Sourced [A3-S091] | US$10M seed 2024 [A3-S092] |
| Cognee | States it holds no SOC 2 or ISO [A3-S095] | Sourced [A3-S095] | US$7.5M seed Feb 2026 [A3-S094] |
| Supermemory | SOC 2 from Scale tier [A3-S096] | Sourced [A3-S096] | Seed US$2.6–3M [A3-S097] |
| Composio | SOC 2 Type II + ISO 27001:2022 [A3-S098] | Sourced [A3-S098] | US$25M Series A [A3-S099] |
| Exa | SOC 2 Type II [A3-S100, A3-S121] | Sourced [A3-S100] | Series C US$250M [A3-S101] |
| Browserbase | SOC 2 Type II [A3-S102] | Sourced [A3-S102] | US$40M Series B [A3-S103] |
| E2B | SOC 2 Type II [A3-S104, A3-S120] | Sourced [A3-S104] | US$21M Series A [A3-S105] |

- **Platform memory (H4).** AgentCore Memory, Vertex Memory Bank and OpenAI are now sourced [A3-S108, A3-S109, A3-S110, A3-S111].

**Still open**
- **Mem0 SOC 2 type.** Mem0's own pages conflict (Type I; Type II "in progress"; Type II for Enterprise) [A3-S106]. No managed EU region was found.
- **Trust-centre reports.** No report was read directly; every trust-centre claim is a vendor statement via search extract. Report types are not confirmed for Tavily and Supermemory.
- **EU managed regions not found.** Exa, Supermemory, Composio (US-hosted, with EU residency via self-hosting), Mem0 and Letta. Zep offers EU residency on request; E2B and Browserbase do offer EU regions.
- **Vertex AI Memory Bank.** Exact GA date and price rates not captured. AgentCore Memory pricing and certifications not verified.
- **SSO/RBAC detail.**
  - E2B lists SSO, SCIM and RBAC as "planned" on a page about 436 days old.
  - Zep's support for SAML is not named.
  - Supermemory's SSO protocols are undocumented.
- **Not researched (search budget prioritised elsewhere):** Microsoft Entra Agent ID, Okta/Auth0 for AI agents beyond EMA, SPIFFE for agents, and Daytona/Modal sandboxes.
- **Self-reported figures.** MCP adoption figures are reported by the project itself [A3-S015, A3-S018]. Vendor benchmark claims (Mem0, Supermemory) are unverified.
