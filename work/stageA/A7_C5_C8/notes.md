# Stage A notes: stream A7 (controls C5 to C8)

Stream A7 · folder `A7_C5_C8` · as of 7 October 2026 · 22 records · 97 sources (`A7-S001` to `A7-S097`)

**Research-environment caveat.** The web-search budget, shared by all eight agents (200 calls per turn), ran out partway through this stream, after the C7 acquisition checks. The C8 commercial vendors (Credo AI, ModelOp, Collibra, IBM watsonx.governance), C6 FinOps vendors (Vantage, CloudZero), Helicone's ownership, LaunchDarkly and FinOps for AI guidance could not be searched. Vendor sites were blocked by egress policy.

The rest of the evidence comes from three places:

- PyPI JSON, the npm registry and the Docker Hub API
- Files in vendors' public GitHub repositories, fetched from `raw.githubusercontent.com` (documentation sources, READMEs, changelogs and licences). These are primary vendor material.
- One Anthropic docs page

Where none of these reached a fact, the fact is marked *Not publicly verified*. Nothing was filled in from memory.

## (a) What changed since the original diagram

None of these controls appears in the graphic. "Original label" is therefore "(none – C*n* control)" for every row.

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| (none – C5) Langfuse Prompt Management | Prompt management is part of Langfuse v4. The core is MIT-licensed; protected prompt labels, RBAC and audit logs are Enterprise-only. Langfuse has been part of ClickHouse since January 2026. | Acquired | A7-S071, A7-S074, A7-S075 |
| (none – C5) LangSmith prompt management | Prompts are managed as commits, with Staging/Production environments, prompt owners, webhooks and GitHub sync. EU region is europe-west4. SOC 2 Type 2. | No change | A7-S076, A7-S077, A7-S078 |
| (none – C5) PromptLayer | Independent. Prompt Registry with release labels. Self-hosted or in the customer's AWS account (Enterprise). SSO and SCIM via WorkOS. SDK 1.5.16 (19 August 2026). | No change | A7-S004, A7-S085, A7-S086, A7-S087 |
| (none – C5) LaunchDarkly AI Configs | Runtime model, parameter and prompt configuration through the LaunchDarkly SDK. AI SDK 1.2.0 (17 July 2026). Certifications and pricing not verified. | Not publicly verified | A7-S059, A7-S089 |
| (none – C5) Prompts-as-code pattern | Prompty v2 (Microsoft, MIT), Dotprompt (Google, Apache-2.0) and Promptfoo configs. Promptfoo is now part of OpenAI and remains MIT. | Acquired (Promptfoo) | A7-S067, A7-S066, A7-S068, A7-S022 |
| (none – C6) Gateway-native cost tracking / chargeback | Includes LiteLLM spend tracking and Anthropic's Usage & Cost Admin API. Portkey was acquired by Palo Alto Networks on 29 May 2026, and Palo Alto's AI Gateway went GA on 16 July 2026. | Acquired (Portkey) | A7-S010, A7-S070, A7-S016, A7-S028 |
| (none – C6) Helicone | Positions itself as an AI gateway and observability platform under Apache-2.0. npm releases stopped in November 2025. A reported acquisition could not be verified. | Not publicly verified | A7-S046, A7-S047 |
| (none – C6) Vantage | Cloud cost platform with a hosted MCP server. AI-spend features not verified. | Not publicly verified | A7-S090 |
| (none – C6) CloudZero | Cost allocation platform with a Kubernetes agent. AI-spend features not verified. | Not publicly verified | A7-S091 |
| (none – C6) FinOps FOCUS | FOCUS v1.4 was announced in June 2026 under CC BY 4.0. No AI- or token-specific columns were found in the changelog. | No change | A7-S048, A7-S049, A7-S096 |
| (none – C7) Lakera | Check Point announced the acquisition on 16 September 2025 and completed it in Q4 2025. The product is now "Check Point AI Guardrails", inside the AI Defense Plane (23 March 2026). AI Agent Security is in early access. | Acquired; Renamed | A7-S012, A7-S013, A7-S024, A7-S025, A7-S026 |
| (none – C7) Palo Alto Prisma AIRS | Version 3.0 (23 March 2026). Protect AI was acquired on 22 July 2025, Koi on 14 April 2026 and Portkey on 29 May 2026. AI Gateway GA 16 July 2026. | Acquired (Protect AI) | A7-S014, A7-S016, A7-S027, A7-S028 |
| (none – C7) HiddenLayer | Independent. Raised a US$100m Series B in September 2026. Agent Harness Security launched August 2026. ISO 27001 and SOC 2 Type 2 (February 2025). | No change | A7-S017, A7-S030 |
| (none – C7) HashiCorp Vault | IBM-owned since 27 February 2025. Vault 2.1.1 (16 September 2026). Agentic IAM is GA in Enterprise 2.1. Licence is BUSL 1.1. | Acquired | A7-S032, A7-S034, A7-S060, A7-S061 |
| (none – C7) Model/package scanning | Current versions: ModelScan 0.8.8, picklescan 1.0.5, fickling 0.1.12, safetensors 0.8.0. The Hugging Face Hub scans with ClamAV, picklescan, Protect AI and JFrog. Guardian has moved into Prisma AIRS (secondary sources). | Acquired (Protect AI) | A7-S002, A7-S006, A7-S037, A7-S039 |
| (none – C7) OpenSSF Model Signing (added) | OMS v1.0 released April 2025; model-signing 1.1.1. | No change | A7-S038, A7-S040 |
| (none – C8) ValidMind | Library 2.13.14, dual AGPL/commercial licence. Documentation maps the platform to SR 26-2 (which supersedes SR 11-7), SS1/23, the EU AI Act and E-23. Offered as SaaS or single-tenant VPV. | No change | A7-S003, A7-S051, A7-S052, A7-S053, A7-S054 |
| (none – C8) Credo AI | The open-source Lens library is deprecated (last release May 2023). The platform could not be verified. | Not publicly verified | A7-S092, A7-S093 |
| (none – C8) IBM watsonx.governance | SDK 1.5.2 (18 September 2026) evaluates prompt templates and model risk. Everything else not verified. | Not publicly verified | A7-S058, A7-S094 |
| (none – C8) ModelOp | No source reachable. | Not publicly verified | (none) |
| (none – C8) Collibra AI Governance | No source reachable. | Not publicly verified | (none) |
| (none – C8) OpenLineage / Marquez | OpenLineage 1.53.0 (1 September 2026), spec 2-0-2, an LF AI & Data Graduate project. The latest Marquez release is 0.51.1 (March 2025). | No change | A7-S001, A7-S041, A7-S043, A7-S044 |

## (b) Ambiguities owned

Stream A7 owns none of A1–A19 in the baseline inventory. One cross-stream item is relevant here: the A-flag on Promptfoo, which L9 owns. Promptfoo is now part of OpenAI and remains open source under MIT [A7-S068]. The announcement was reported in March 2026 [A7-S022, secondary]. The exact closing date was not verified.

## (c) Hypothesis evidence

### H7 (lineage, classification, PII in ingestion and governance)

- OpenLineage is a "Graduate project" of LF AI & Data. It defines run, job and dataset entities, which facets extend [A7-S041].
- OpenLineage version 1.53.0 (1 September 2026) adds:
  - explicit lineage facets for exact dataset-, field- and job-level relationships
  - Spark column-lineage transformation descriptions [A7-S042, A7-S001]
- A text search of the OpenLineage changelog for "llm", "genai", "embedding", "vector" and "prompt" returned nothing [A7-S042]. No GenAI- or RAG-specific lineage facets were found. RAG steps (parse, chunk, embed, index) would have to be modelled as generic jobs and datasets or as custom facets.
- OpenLineage supports user-supplied tag facets in the Python and Java clients, and captures dbt tags and `meta` [A7-S042]. This is a possible carrier for classification labels such as "PII" or "confidential". Integration with DLP tools was not verified.
- Adoption signals:
  - Apache Airflow ships an OpenLineage provider (2.20.2, 29 September 2026) [A7-S045].
  - The Marquez reference implementation has about 1.12 million Docker pulls, but its last image was released in March 2025 [A7-S044, A7-S043].
- GCP Lineage and GCS transports exist in the Java client [A7-S042]. Cloud catalogues are therefore one possible place where OpenLineage events end up.
- Governance tools and classification:
  - ValidMind says it does not store PII or customer data in documentation [A7-S054].
  - Collibra and Credo AI could not be verified, so classification and PII integration in governance tools remains *Not publicly verified* for them.
- Supply-chain lineage for models: OpenSSF Model Signing gives integrity and signer verification [A7-S040]. Commentary notes it does not establish provenance (secondary).

### H8 (governance tools consuming eval and monitoring evidence; regulatory monitoring expectations)

- ValidMind (vendor claims):
  - Its Library logs test results and documentation artefacts to the Platform [A7-S003].
  - The Platform provides ongoing monitoring with metrics over time, thresholds and alerts, and can trigger workflows on a threshold breach [A7-S056].
  - It offers LLM-specific test extras [A7-S003] and LLM features for test interpretation and document checking [A7-S097].
- IBM's watsonx.governance SDK "evaluate[s] metrics, prompt templates, get[s] model insights and perform[s] model risk evaluation" [A7-S058]. This is a governance product consuming eval evidence.
- Langfuse links prompt versions to traces to analyse performance by version [A7-S071]. LangSmith fires webhooks on prompt commits [A7-S076]. Both are hooks for feeding change events into governance or evaluation in CI.
- Prisma AIRS AI Red Teaming produces findings and "recommends runtime security policies", and allows verdicts to be overridden in reports [A7-S027, A7-S028]. These are security-evaluation outputs that governance tools could consume.
- **Regulatory development (high importance; source is a vendor document):**
  - ValidMind's documentation states that **SR 26-2**, "Interagency Guidance on Model Risk Management for Banking Organizations", was issued by the Federal Reserve, FDIC and OCC on **17 April 2026**. It is said to **supersede SR 11-7** and to **explicitly exclude generative AI and agentic AI from its scope**, while keeping principles such as ongoing monitoring [A7-S051].
  - The regulator's page (federalreserve.gov) was blocked, and search was unavailable for confirmation.
  - Stage B and stream ⑧ must confirm this before the master document cites SR 11-7 as current.
- ValidMind's documentation also describes:
  - PRA SS1/23, with five principles and proportionality [A7-S052]
  - OSFI E-23, with a 2027 effective date and enhanced AI/ML requirements [A7-S057]
  - EU AI Act Article 9 risk-management mapping [A7-S053]
- C8 vendor claims for NIST AI RMF and ISO/IEC 42001: none found in the pages fetched (*Not publicly verified*).

## (d) Products the graphic misses (material to these controls)

- **OpenSSF Model Signing (OMS)**: open specification for signing models (v1.0, April 2025). Added to `products.json` as `C7-openssf-model-signing` [A7-S040].
- **Palo Alto Networks AI Gateway (from Portkey)**: GA 16 July 2026. Belongs to C1/C6; noted for the C1 stream [A7-S016, A7-S028].
- **Anthropic Usage & Cost Admin API**: provider-native cost data by workspace, API key and model. Included as part of the C6 pattern record [A7-S070].
- **Other AI-security start-ups acquired in 2025–2026** (C7 candidates; not added as records):
  - Prompt Security → SentinelOne (closed 5 September 2025) [A7-S018]
  - CalypsoAI → F5 (closed 26 September 2025; now F5 AI Guardrails) [A7-S019]
  - Pangea → CrowdStrike (closed 26 September 2025; AI Detection and Response) [A7-S020]
  - Robust Intelligence → Cisco (2024; foundation of Cisco AI Defense) [A7-S021]
  - Reported only: Aim Security → Cato Networks (2025), TrojAI → A10 Networks (around June 2026), Aegis → Upwind (September 2026), Promptfoo → OpenAI (March 2026) [A7-S022, secondary]
- **fickling** (Trail of Bits pickle analyser, LGPLv3+): included in the scanning pattern record [A7-S064].
- **ServiceNow AI Control Tower and OneTrust AI governance**: not assessed. Their sites were blocked and search was exhausted, so materiality was not established.

## (e) Gaps

1. **Search budget exhausted.** No searches were possible for:
   - ValidMind (funding, certifications), Credo AI, ModelOp, Collibra AI Governance, IBM watsonx.governance (deployment, certifications, pricing)
   - ServiceNow and OneTrust
   - Vantage and CloudZero AI-cost features
   - FinOps Foundation "FinOps for AI" guidance
   - Helicone acquisition status
   - LaunchDarkly AI Configs (GA date, certifications, pricing)
   - PromptLayer and LangSmith pricing
2. **Blocked hosts** (cited by link only where used): langfuse.com, validmind.com, credo.ai, modelop.com, ibm.com, collibra.com, finops.org, focus.finops.org, docs.litellm.ai, portkey.ai, helicone.ai, vantage.sh, cloudzero.com, launchdarkly.com, promptlayer.com, paloaltonetworks.com, checkpoint.com, hiddenlayer.com, huggingface.co, sec.gov, federalreserve.gov, occ.gov, fdic.gov, bankofengland.co.uk, openlineage.io, docs.cloud.google.com, learn.microsoft.com, docs.aws.amazon.com.
3. **SR 26-2** rests on ValidMind documentation, not the regulator. It needs primary confirmation.
4. **Cloud-provider cost tags and labels** for Bedrock, Azure OpenAI and Vertex AI (C6 pattern): not verified.
5. **Certification levels.** Lakera, PromptLayer and Helicone claim "SOC 2" without stating the type. No trust-centre report was reachable. HiddenLayer's certification evidence is dated February 2025.
6. **Prisma AIRS data location.** Sources conflict: US-only inspection versus EU, Japan and Singapore regions for Model Security, and a Japan local cloud. Its FedRAMP status is not confirmed.
7. **Deal values** (Lakera US$300m versus US$201.8m; Protect AI about US$500m) are secondary and were not used as facts.
8. **ModelOp and Collibra** records contain no verified facts. Stage B should either refresh them or drop them.
