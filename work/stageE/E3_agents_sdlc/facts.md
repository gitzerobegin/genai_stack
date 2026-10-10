# E3 brief: agentic SDLC tools and third-party agents (Stage E, DV / AG / AT views)

**Stream:** E3. **Accessed:** 9 to 10 October 2026. **Sources:** `work/stageE/E3_agents_sdlc/sources.csv` (E3-S001 to E3-S082). **Landscape records:** `work/stageE/E3_agents_sdlc/products.json` (layer `DV`, no scores, no tier; not merged into the main dataset).

**Conflict of interest.** The author is an Anthropic model. Claude Code is recorded on the same evidence standard as every other tool. Wherever a view recommends Claude Code, name an independent alternative beside it: OpenAI Codex CLI and Gemini CLI (both open source), JetBrains Junie or Tabnine (self-hosted) [AJ].

**Access note.** Most vendor documentation hosts were blocked by the research environment's egress policy. Those facts come from search-tool extracts, so their confidence is capped at medium. GitHub's docs (from the github/docs repository), Claude Code docs, the OpenTelemetry, OpenSSF, AGENTS.md, AGNTCY, Codex and Gemini CLI repositories and npm/PyPI metadata were fetched directly [AJ].

**Status as of 10 October 2026.** Every fact below is the position on that date unless the bullet gives another date.

## DV: agentic SDLC landscape

### Landscape table (as of 10 October 2026)

| Product | Modes | Deployment | Model choice | Enterprise controls | Certifications |
|---|---|---|---|---|---|
| GitHub Copilot | IDE, CLI, app, cloud agent, code review, third-party agents | SaaS; GHE Cloud with data residency; not on GHES | Multi-vendor hosted; local and enterprise BYOK; FedRAMP-model policy | Enterprise/org AI policies, MCP allowlist, audit logs, OTel export, IP indemnity (conditional) | SOC 2 Type 2, ISO 27001, ISO 42001, SOC 1/3, CSA STAR 2 |
| Cursor | IDE, CLI, cloud agents, Bugbot | SaaS (no self-host found) | Multi-vendor; BYOK (chat only); BYOK blockable | SSO, SCIM, audit logs to SIEM/S3, enforced Privacy Mode, CMEK (cloud agents) | SOC 2 Type II, ISO 27001, ISO 42001, AIUC-1 |
| Claude Code (Anthropic; COI) | CLI, IDE, desktop, cloud sessions, CI, Code Review | SaaS; via Bedrock, Google Cloud, Foundry; customer runners for cloud sessions (beta) | Claude only, via Anthropic or three hyperscalers or a gateway | SSO, RBAC, compliance API, managed settings and MCP policy; ZDR per org; IP indemnity | Anthropic SOC 2 I/II, ISO 27001, ISO 42001 (dataset) |
| OpenAI Codex | CLI, IDE, app, cloud tasks | SaaS; local CLI with local models | OpenAI default; configurable providers incl. local | RBAC, SCIM (Enterprise), Compliance API (30-day logs), EKM, IP indemnity | OpenAI SOC 2, ISO 27001 family, ISO 42001 (dataset; Codex scope not stated) |
| Google (Code Assist, Gemini CLI, Antigravity) | IDE, CLI, agentic IDE | SaaS / Google Cloud; Gemini CLI local | Gemini; Claude optional (8 October 2026) | IAM, audit logging, VPC-SC (Code Assist), indemnity (Code Assist) | Code Assist ISO 27001/17/18/27701, SOC 1/2/3; Antigravity excluded from several |
| Kiro (AWS; Q Developer successor) | IDE, CLI, Web autonomous agent | SaaS | Auto routing; Claude models | IAM Identity Center, activity reports, KMS | NPV |
| Devin / Devin Desktop (Cognition; ex-Windsurf) | Cloud agent, IDE | SaaS; Cognition-hosted single-tenant VPC | NPV | SSO (SAML/OIDC), SCIM (Desktop), audit logs via API | SOC 2 Type II; FedRAMP High claim unverified |
| JetBrains AI / Junie | IDE, CLI (beta), GitHub Action, local | SaaS; on-prem, cloud or hybrid (AI Enterprise); on-device | Multi-vendor; BYOK; local model | ZDR by default; NPV for SSO/audit | SOC 2 Type II (incl. Junie) |
| Amp | Web threads in cloud machines, SDK | SaaS | Vendor-selected multi-model | SSO and SCIM via WorkOS | NPV |
| Tabnine (Tricentis) | IDE, agents, CLI | SaaS, VPC, on-prem, air-gapped | Model-agnostic; customer models; NIM | No training or storage; provenance check; indemnity (subject to terms) | SOC 2, ISO 27001, ISO 9001, GDPR |

The facts behind each row carry tags in the bullets below and in `products.json`.

### Key facts

- **GitHub Copilot: agents.** All plans except Free include the Copilot cloud agent. The cloud agent works in an ephemeral GitHub-hosted environment and opens pull requests [VF: E3-S001, E3-S008].
- **GitHub Copilot: third-party agents.** Third-party agents (Anthropic Claude, OpenAI Codex) run on GitHub in public preview under the same protections [VF: E3-S003].
- **GitHub Copilot: scanning of agent code.** Code written by agents is scanned by CodeQL, secret scanning and the advisory database before the pull request is finalised, without a GHAS licence [VF: E3-S003].
- **GitHub Copilot: MCP governance.** The recommended MCP allowlist is the enterprise managed-settings file (GA). A custom MCP registry is in public preview, with weaker enforcement that users can bypass [VF: E3-S004].
- **GitHub Copilot: instructions and telemetry.** Copilot reads AGENTS.md as agent instructions [VF: E3-S007]. It exports OpenTelemetry traces, metrics and events of agent sessions, without prompt content by default [VF: E3-S081].
- **GitHub Copilot: deployment.** Copilot is not available for GitHub Enterprise Server [VF: E3-S001]. Local BYOK clients can work without the Copilot API, for air-gapped users [VF: E3-S002].
- **GitHub Copilot: data use.** Copilot does not train on Business or Enterprise data [VF: E3-S011, E3-S012].
- **GitHub Copilot: Claude Fable retention.** Claude Fable 5 / 5.1 retain data by default for safety classifiers. ZDR for them is only available through a time-bound exemption to the end of 2026 [VF: E3-S011].
- **GitHub Copilot: IP indemnity.** Indemnity depends on the public-code filter, and that filter does not apply to the coding agent [VF: E3-S010].
- **GitHub Copilot: organisation.** GitHub was folded into Microsoft CoreAI after its CEO's departure was announced in August 2025 [R: E3-S013].
- **Cursor: ownership.** Cursor (Anysphere) is now part of SpaceX: the Cursor blog dated 14 August 2026 says the acquisition is complete. SpaceX filings value the deal at US$60B [VF: E3-S029]. SpaceX also owns xAI, so the editor and a frontier-model vendor now share an owner [AJ].
- **Cursor: data controls.** Privacy Mode can be enforced org-wide and means no training on customer data. Models whose provider retains data need admin approval, and ZDR does not apply to BYOK keys [VF: E3-S032, E3-S030].
- **Cursor: enterprise controls.** The Enterprise plan offers SCIM, audit logs streamable to a SIEM or S3, and CMEK for cloud-agent data [VF: E3-S027, E3-S028].
- **Cursor: certifications.** Cursor lists SOC 2 Type II, ISO 27001:2022, ISO 42001:2023 and AIUC-1 [VF: E3-S026].
- **Claude Code: models and hosting.** Claude Code uses Claude models only. Inference runs through Anthropic, Amazon Bedrock, Claude Platform on AWS, Google Cloud Agent Platform or Microsoft Foundry, or a customer LLM gateway [VF: E3-S014, E3-S079].
- **Claude Code: data and retention.** Commercial use means no training and 30-day retention. ZDR is per organisation for qualified Enterprise customers [VF: E3-S015].
- **Claude Code: self-hosted runners.** Cloud sessions can run on customer-operated runners (public beta, off by default) [VF: E3-S018].
- **Claude Code: managed MCP.** Administrators can restrict or fix the MCP servers users run through managed settings [VF: E3-S019].
- **Claude Code: embedding conditions.** A vendor that embeds Claude Code must ship it unmodified, and each end user must authenticate with their own credentials [VF: E3-S016]. This bears directly on a DV start-up that wants to wrap Claude Code [AJ].
- **OpenAI Codex: licence and models.** The Codex CLI is open source (Apache-2.0) [VF: E3-S020]. It can use custom model providers, including local models through `--oss` [VF: E3-S025].
- **OpenAI Codex: audit coverage.** The Compliance API covers CLI and IDE usage, but not every hosted file operation, command or approval. Compliance logs are kept for 30 days [VF: E3-S023].
- **OpenAI Codex: retention.** Cloud mode is not strict ZDR [VF: E3-S024].
- **Google: Code Assist end of sale.** New Gemini Code Assist Standard and Enterprise subscriptions stopped on 9 October 2026, and Google is moving users to Antigravity [VF: E3-S033].
- **Google: Antigravity enterprise status.** AI developer tools (Antigravity 2.0, Antigravity CLI) have been GA in Gemini Enterprise since 18 August 2026. The standalone Antigravity IDE is not supported for enterprise deployment [VF: E3-S037].
- **Google: certification gap.** Antigravity-based products are excluded from several certifications, including ISO 27001 and SOC 2 [VF: E3-S034]. This is a material assurance gap for enterprise buyers in Q4 2026 [AJ].
- **Google: Claude models.** Since 8 October 2026, administrators can enable Claude Opus 5.5 and Sonnet 5.5 in Google's AI developer tools [VF: E3-S039].
- **Amazon: Q Developer wind-down.** New Q Developer subscriptions closed on 15 May 2026, and the product reaches end of support on 30 April 2027. Kiro is the successor [VF: E3-S040].
- **Amazon: Kiro data use.** Kiro Pro tiers used through IAM Identity Center are excluded from content use and telemetry [VF: E3-S041].
- **Cognition: Windsurf rename.** Windsurf, acquired by Cognition in 2025, was renamed Devin Desktop on 2 June 2026 [VF: E3-S045].
- **Cognition: dedicated deployment.** Devin's dedicated deployment is a Cognition-hosted single-tenant VPC [VF: E3-S044].
- **JetBrains: Junie.** Junie is LLM-agnostic with BYOK, reads AGENTS.md, and its GitHub Action runs on the customer's own runners [VF: E3-S050, E3-S051].
- **JetBrains: AI Enterprise.** AI Enterprise offers on-premises deployment [VF: E3-S047]. Junie has its own SOC 2 Type II report [VF: E3-S048].
- **Amp: spin-out and models.** Amp has spun out of Sourcegraph as an independent company [VF: E3-S053]. Amp chooses the models itself, and it reads AGENTS.md and supports MCP [VF: E3-S054].
- **Tabnine: ownership.** Tricentis announced its acquisition of Tabnine on 30 July 2026 [VF: E3-S056].
- **Tabnine: deployment and terms.** Tabnine supports VPC, on-premises and fully air-gapped installs on Kubernetes with customer-chosen models [VF: E3-S055]. It offers IP indemnity subject to terms, and no training on customer code [VF: E3-S057].
- **AGENTS.md.** AGENTS.md is an open format for guiding coding agents [VF: E3-S060]. OpenAI donated it to the Agentic AI Foundation (Linux Foundation) at the AAIF's launch on 9 December 2025 [VF: E3-S061].
  - Copilot, Cursor, Claude Code, Junie and Amp document that they read AGENTS.md [VF: E3-S007, E3-S031, E3-S017, E3-S051, E3-S054].
  - Kiro uses its own steering files instead [VF: E3-S042].
- **MCP adoption.** MCP is supported by Copilot, Cursor, Claude Code, Gemini CLI, Kiro, Junie and Amp [VF: E3-S001, E3-S030, E3-S019, E3-S035, E3-S042, E3-S051, E3-S054].
  - Enterprise MCP allowlisting is now a standard admin control in Copilot, Cursor, Claude Code and Antigravity [VF: E3-S004, E3-S030, E3-S019, E3-S037].
- **2025–26 consolidation.** Ownership changes in this period:
  - Cursor to SpaceX [VF: E3-S029];
  - Windsurf to Cognition [VF: E3-S045];
  - Tabnine to Tricentis [VF: E3-S056];
  - Amp out of Sourcegraph [VF: E3-S053].

  Two incumbents are retiring products: Gemini Code Assist [VF: E3-S033] and Q Developer [VF: E3-S040]. A DV start-up should expect its integration partners to change hands or names within a year [AJ].
- **Integration point for a DV start-up.** The common surfaces are MCP servers, AGENTS.md and skills content, PR-based review bots, and GitHub's third-party agent slot (currently Claude and Codex only) [AJ].

### Secure development and supply chain for AI-generated code

- **NIST SSDF.** SSDF v1.2 (SP 800-218 Rev. 1) is still a draft. The initial public draft was published on 17 December 2025, and NIST still called it a draft on 20 May 2026 [VF: E3-S063].
  - The draft adds practice groups PO.6 (continuous improvement) and PS.4 (robust updates).
  - No practice specific to AI code generation was found [VF: E3-S063].
- **NIST SP 800-218A.** This profile (July 2024) covers developing generative AI models, not using coding assistants [VF: E3-S064].
- **No federal guidance on coding assistants.** No NIST or CISA guidance specific to AI coding assistants or AI-generated code was found [NPV].
- **Five Eyes agentic AI guidance.** The nearest guidance is "Careful Adoption of Agentic AI Services" (CISA, NSA, ASD ACSC, CCCS, NCSC-NZ, NCSC-UK; 1 May 2026) [VF: E3-S065].
  - It recommends incremental deployment, least privilege, strong identity, monitoring and human oversight.
  - It points to OWASP and MITRE ATLAS taxonomies [VF: E3-S065].
- **OpenSSF guide.** OpenSSF's "Security-Focused Guide for AI Code Assistant Instructions" (1 August 2025) says the developer remains responsible for AI-written code [VF: E3-S062]. It asks for:
  - review, tests and static analysis;
  - defences against hallucinated packages ("slopsquatting");
  - pinned dependencies, SBOMs (SPDX/CycloneDX) and in-toto attestations [VF: E3-S062].
- **SLSA.** The SLSA v1.2 Source Track (L1–L4) issues source provenance attestations recording who made each change and which controls applied [VF: E3-S077].
  - No SLSA field or profile for AI-authored or agent-authored commits was found [NPV].
  - Recording the agent identity and the directing human in commit trailers and PR metadata is the practical stop-gap [Rec].
- **OWASP agentic list.** The full OWASP Agentic Top 10 (2026) entry list was retrieved. It completes `R-OWASP-AGENTIC`, which held only ASI01 [VF: E3-S072; A8-S042]:
  - ASI01 Agent Goal Hijack;
  - ASI02 Tool Misuse;
  - ASI03 Identity and Privilege Abuse;
  - ASI04 Agentic Supply Chain Vulnerabilities;
  - ASI05 Unexpected Code Execution;
  - ASI06 Memory and Context Poisoning;
  - ASI07 Insecure Inter-Agent Communication;
  - ASI08 Cascading Failures;
  - ASI09 Human-Agent Trust Exploitation;
  - ASI10 Rogue Agents.
- **OWASP items most relevant to coding agents.** ASI01 (instructions hidden in issues, READMEs or dependencies), ASI02, ASI04 (MCP servers, packages, skills), ASI05 (agent shell execution) and ASI03 (developer tokens held by agents) [AJ].
  - OWASP's Q3 2026 exploit roundup tags a malicious PyPI package case as ASI04 and ASI05 [VF: E3-S072].

## AG: standards and mechanisms for running a third-party agent inside an enterprise stack

### Standards status table (as of 10 October 2026)

| Mechanism | Status | Source |
|---|---|---|
| A2A Agent Card signing | Optional (JWS, "MAY") in A2A 1.0.0; 1.0.1 latest | Dataset: A3-S078, A3-S079 |
| MCP authorisation | OAuth 2.1 profile, optional in MCP; spec 2026-07-28 | Dataset: A3-S015, A6-S032, V2-S031 |
| MCP Enterprise-Managed Authorization | Stable extension (18 June 2026) using ID-JAG | Dataset: A3-S017, A6-S079 |
| MCP Registry | API frozen at v0.1; v1 GA "Ideating" | Dataset: A3-S036, A3-S042, A3-S114 |
| ID-JAG (IETF) | Active OAuth WG draft -04 (21 May 2026), AI-agent appendix; not an RFC | E3-S073 |
| IETF agent auth | Individual draft (draft-klrc-aiagent-auth-01); WIMSE discussion at IETF 126 | E3-S074 |
| OpenID Foundation | AIIM Community Group whitepaper (7 October 2025); CG writes no specifications | E3-S075, E3-S076 |
| SPIFFE for agents | No official agent profile; OIDF cites SPIFFE/SPIRE as a model | E3-S076; dataset A6-S087 |
| OpenTelemetry GenAI and agent spans | Status "Development" (not stable); moved to its own repository; no tagged release | E3-S066 to E3-S069 |
| AGNTCY directory | Active open-source project (agntcy-dir 1.5.0, June 2026); governance home not confirmed | E3-S070, E3-S071, E3-S078 |
| AGENTS.md | AAIF (Linux Foundation) project since 9 December 2025 | E3-S061 |

### Key facts

- **A2A signing.** A2A Agent Card signing exists but is optional, so a buying enterprise must require and verify signatures itself [VF: A3-S078] [AJ]. Nothing new was found beyond the dataset's `L4-a2a` record.
- **MCP authorisation and registry.** These are covered by the dataset's `L4-mcp` and `C4-mcp-authorization` records (Enterprise-Managed Authorization stable; registry still v0.1) [VF: A3-S017, A3-S036, A3-S114]. They were not re-researched.
- **ID-JAG.** ID-JAG is now titled "Identity Assertion JWT Authorization Grant". It is an active OAuth WG draft (-04, 21 May 2026, expiring 22 November 2026) [VF: E3-S073].
  - Its AI-agent appendix treats the agent as an OAuth client trusted by both the enterprise IdP and the tool's authorisation server [VF: E3-S073].
  - MCP Enterprise-Managed Authorization and Okta Cross App Access build on this draft [VF: A6-S079, A6-S080].
- **Other IETF agent work.** Agent authorisation beyond ID-JAG is still an individual Informational draft that maps existing IETF technologies to agents [VF: E3-S074].
  - IETF 126 WIMSE slides flag that CIBA does not fit mid-task user consent [VF: E3-S074].
  - No agent-specific IETF RFC exists as of 10 October 2026 [NPV].
- **OpenID Foundation.** The AIIM Community Group published "Identity Management for Agentic AI" on 7 October 2025. It flags recursive delegation without scope attenuation as an open risk [VF: E3-S075].
  - The Community Group does not produce specifications [VF: E3-S075].
- **SPIFFE.** No official SPIFFE/SPIRE profile for AI agents was found [NPV]. OIDF's March 2026 response to NIST cites SPIFFE/SPIRE as a model for agent workload identity [VF: E3-S076].
- **OpenTelemetry GenAI conventions.** The conventions moved from the core semantic-conventions repository to `open-telemetry/semantic-conventions-genai` [VF: E3-S066].
  - The agent spans (`create_agent`, `invoke_agent`, `invoke_workflow`, `execute_tool`) and the MCP conventions are all at status **Development** [VF: E3-S067, E3-S068].
  - The new repository has no tagged release yet [VF: E3-S069].
  - A third-party agent vendor should emit `gen_ai.*` spans but pin a version and expect renames [Rec].
- **AGNTCY.** AGNTCY's Agent Directory Service is a federated, open-source registry using the OASF schema across A2A and MCP. It added an MCP server on 19 February 2026, and Cisco staff author its Internet-Draft [VF: E3-S078, E3-S070].
  - The Python SDK release 1.5.0 is dated 22 June 2026 [VF: E3-S071].
- **Five Eyes guidance and agent vendors.** The guidance expects strong identity, least privilege and monitoring for each agent [VF: E3-S065]. A vendor selling agents should arrive with per-agent identity (Entra Agent ID, Okta, SPIFFE), scoped delegated tokens and OTel traces [Rec].
- **What a third-party agent needs, in summary.** Each item is covered by an existing dataset record:
  - registration as a workload identity (C4: `C4-entra-agent-id`, `C4-okta-auth0-ai-agents`, `C4-spiffe-spire`);
  - tool access through MCP with Enterprise-Managed Authorization (`C4-mcp-authorization`);
  - delegation through A2A with signed cards the buyer verifies (`L4-a2a`);
  - telemetry in OTel GenAI conventions (L9).

  The weakest of these is telemetry, because those conventions are not yet stable [AJ].

## AT: relevant to start-ups selling AI tools into the enterprise stack

- **Enterprise baseline.** The coding-agent incumbents now ship SSO/SCIM, audit export, MCP allowlists, ZDR options and ISO 42001 [VF: E3-S010, E3-S026, E3-S027, E3-S004]. An AT start-up's tool will be measured against that baseline in procurement [AJ].
- **Certifications.** ISO/IEC 42001 is now common among AI developer tools: GitHub Copilot, Cursor, Anthropic and Google Gemini [VF: E3-S010, E3-S026, A5-S017, E3-S034].
- **AIUC-1.** AIUC-1 appears as an attestation on Cursor's security page [VF: E3-S026]. E2 covers assurance frameworks.
- **Agent-ready tools.** A tool that wants to be called by coding agents should ship an MCP server that works with managed allowlists, plus AGENTS.md or skill guidance [AJ].
- **ZDR conditions.** ZDR is not uniform across model providers. Some Anthropic models retain data by default for safety review, and Copilot and Cursor surface them as non-ZDR or exemption-only [VF: E3-S011, E3-S032]. A tool that brokers model calls must pass these conditions through to its customers [AJ].

## Open / not publicly verified

- Copilot: SSO/SCIM mechanics, exact seat prices, and the cloud-agent and CLI retention period [NPV].
- Cursor: self-hosted or VPC option, IP indemnity and pricing [NPV].
- Claude Code: SCIM [NPV].
- Codex: MCP support was not re-verified in this run, and the certification scope specific to Codex is not stated [NPV].
- Google: Jules enterprise status, pricing and certifications (aggregator sources only); Antigravity IP indemnity [NPV].
- Kiro: certifications, IP indemnity, AGENTS.md support and retention period [NPV].
- Devin / Devin Desktop:
  - model choice, MCP and AGENTS.md support, and IP indemnity [NPV];
  - on-premises deployment, mentioned but not documented [NPV];
  - FedRAMP High (claimed, no authorisation evidence) [NPV];
  - the exact Windsurf acquisition date [NPV].
- JetBrains: SSO/SCIM, audit logs, IP indemnity, air-gapped support, ISO 27001 [NPV].
- Amp: certifications, IP indemnity, self-hosting, CLI/editor modes, spin-out date and legal name [NPV].
- Tabnine: MCP and AGENTS.md support, SSO/SCIM, audit logs; SOC 2 type not stated on the Trust Center [NPV].
- Cursor/SpaceX: the deal date and terms in SpaceX's SEC filings (sec.gov blocked; Cursor's blog and the search summary used) [NPV].
- Guidance: any NIST or CISA guidance specific to AI coding assistants; the final SSDF v1.2; an SLSA provenance field for AI-authored commits [NPV].
- Identity standards: an official SPIFFE agent profile; WIMSE adoption of an agent draft; AGNTCY's governance home [NPV].
