# Control-plane product list (plan §6, C1–C8), for confirmation at CP1

These are the eight cross-cutting controls missing from the original graphic. The plan's candidates were verified in Stage A and Stage A′, and some products were added during research. **Products added during research are marked ➕.** Full fact records are in `Enterprise_GenAI_Stack_Oct2026/05_Data/products.json` and `.xlsx`.

## Totals

| | Count |
|---|---:|
| Control-plane records (C1–C8) | 48 |
| Graphic layers (L1–L9) | 92: 80 tiles plus 12 material additions |
| **All product records** | **140** (the plan estimated about 120) |

## C1: AI / LLM gateway (9)

| Record | Status as of 8 October 2026 |
|---|---|
| LiteLLM (proxy + enterprise) | Open core, MIT plus a proprietary enterprise package. Also an MCP/A2A gateway. **PyPI supply-chain compromise 24 March 2026** (1.82.7/1.82.8). |
| Portkey → **Prisma AIRS AI Gateway** | **Acquired by Palo Alto Networks**, closed 29 May 2026. |
| Kong AI Gateway | AI Gateway 2.0 GA 1 September 2026, and 2.2 GA 30 September 2026. Covers LLM, MCP and A2A traffic. |
| Cloudflare AI Gateway | Free core service. 2026 additions: spend limits, DLP and guardrails. |
| Azure API Management AI gateway | Policies are GA. The dedicated AI Gateway tier is in preview, with no SLA. |
| AWS (no product named "AI gateway") | Bedrock AgentCore Gateway (MCP) is gaining LLM targets. AWS also publishes a LiteLLM-based guidance pattern. |
| Google Apigee as AI gateway | Token limits, semantic cache, Model Armor and MCP (GA March 2026). |
| ➕ agentgateway | Linux Foundation open-source project for LLM, MCP and A2A traffic. |
| ➕ Agent Router (formerly Envoy AI Gateway) | Renamed and moved to the Agentic AI Foundation. |

## C2: Guardrails (6)

| Record | Status |
|---|---|
| NVIDIA NeMo Guardrails | 0.24.x, Apache-2.0, still Beta (0.x). The microservice is under NVIDIA AI Enterprise. |
| Guardrails AI | **Acquired by Harvey**, 9 September 2026. The hosted hub was retired in August 2026. |
| Meta Llama Guard 4 / Prompt Guard 2 / LlamaFirewall | No release since 2025. Maturity risk. |
| Amazon Bedrock Guardrails | Prompt-attack, PII and grounding filters, plus Automated Reasoning. US$0.15 per 1,000 text units for content filters. |
| Azure AI Content Safety (Prompt Shields) | Prompt Shields is GA. Task Adherence is in preview. |
| ➕ Google Model Armor | Free up to 2M tokens/month. Integrated with Apigee and MCP. |

## C3: DLP / PII (5)

| Record | Status |
|---|---|
| Presidio | **No longer a Microsoft project.** Now community-governed under "Data Privacy Stack", MIT. |
| Google Sensitive Data Protection | Formerly Cloud DLP. Underpins Model Armor. |
| Microsoft Purview DSPM (for AI) | Folded into the unified Purview DSPM, GA May 2026. Needs E5 or the Purview Suite. |
| Protegrity | AI Team Edition is still in Tech Preview. |
| Skyflow | LLM Privacy Vault, EU vaults. Last verified funding: 2024. |

## C4: Identity and access for agents (6)

| Record | Status |
|---|---|
| Microsoft Entra Agent ID | GA April 2026. Security features need Agent 365. |
| Okta / Auth0 for AI Agents | Auth0 for AI Agents GA November 2025. Okta for AI Agents GA April 2026. Agent SSO (Cross App Access) GA 24 August 2026. |
| SPIFFE / SPIRE | CNCF graduated. |
| MCP authorisation (spec 2026-07-28) + Enterprise-Managed Authorization | DCR deprecated. The enterprise IdP extension (ID-JAG) is Stable. OAuth 2.1 itself is still an IETF draft. |
| OPA | CNCF graduated. |
| Cedar / Amazon Verified Permissions / AgentCore Policy | AgentCore Policy GA 3 March 2026. Policies are now authored in Dogwood, a Cedar superset. |

## C5: Prompt and config management (5)

| Record | Status |
|---|---|
| Langfuse Prompt Management | Langfuse is **part of ClickHouse** (announced 16 January 2026). Prompt RBAC and audit features are Enterprise-only. |
| LangSmith prompt management | Commits, environments and GitHub sync. EU region. |
| PromptLayer | Independent. Self-hosting available on Enterprise. |
| LaunchDarkly AI Configs → **AgentControl** | Renamed in 2026. FedRAMP Moderate (Federal instance). |
| Prompts-as-code (Prompty, Dotprompt, Promptfoo configs) | Pattern. **Promptfoo's acquisition by OpenAI was announced** 9 March 2026. |

## C6: AI FinOps (5)

| Record | Status |
|---|---|
| Gateway / provider-native cost tracking and chargeback | Pattern. |
| Helicone | **Acquired by Mintlify** (March 2026). Now in maintenance mode. |
| Vantage | Integrations for Anthropic, OpenAI and Claude Enterprise. |
| CloudZero | AI cost allocation (vendor claims). |
| FinOps FOCUS | v1.4 ratified June 2026. AI model-identity fields are planned for v1.5; a token-type column is deferred. |

## C7: AI security (6)

| Record | Status |
|---|---|
| Lakera → **Check Point AI Guardrails** | **Acquired by Check Point**, completed 22 October 2025. |
| Palo Alto Prisma AIRS 3.0 | Has absorbed Protect AI (July 2025), Koi (April 2026) and Portkey (May 2026). |
| HiddenLayer | Independent. US$100m Series B on 2 September 2026. |
| HashiCorp Vault (IBM) | Agentic IAM GA in Enterprise 2.1. BUSL licence. |
| Model / package scanning (ModelScan, picklescan, fickling, safetensors) | Pattern and tools. |
| ➕ OpenSSF Model Signing | v1.0 (April 2025). |

Other AI-security start-ups were also acquired in September 2025; these are recorded in the notes, not as records: Prompt Security → SentinelOne, CalypsoAI → F5, Pangea → CrowdStrike.

## C8: Model risk, governance and auditability (6)

| Record | Status |
|---|---|
| ValidMind | Only vendor found that claims mapping to PRA SS1/23. Its docs also cite SR 26-2. |
| Credo AI | SaaS (US/EU) or air-gapped deployment. SOC 2 Type II. |
| IBM watsonx.governance | Agent Enforcement Tracking (August 2026). Pricing published. |
| ModelOp | Templates for EU AI Act, NIST, SR 11-7 and E-23. Certifications not verified. |
| Collibra AI Governance | ISO 42001 (corporate). **Acquired trail ML** on 5 October 2026. |
| OpenLineage / Marquez | LF AI & Data Graduate. No GenAI- or RAG-specific facets yet. |

Candidates named in the plan but not yet profiled: ServiceNow AI Control Tower and OneTrust AI Governance.

## Material additions in the graphic layers (12)

| Layer | Additions |
|---|---|
| L9 | MLflow GenAI, Datadog Agent Observability, W&B Weave (CoreWeave) |
| L8 | Google Document AI |
| L5 | AWS AgentCore Memory, Vertex AI Memory Bank |
| L4 | AWS AgentCore Gateway + Identity |
| L3 | Google ADK, AWS Strands / AgentCore Runtime, Temporal |
| L2 | NVIDIA Dynamo, llm-d |
