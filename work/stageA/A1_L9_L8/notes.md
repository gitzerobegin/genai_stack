# Stage A notes: stream A1 (L9 Evaluation and observability; L8 Data extraction and ingestion)

As of 7 October 2026. All source IDs refer to `work/stageA/A1_L9_L8/sources.csv`. Archive: `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A1/`.

**Research-environment caveat.** In the first pass, the shared web-search budget ran out part-way through the stream. After that, facts came only from directly fetchable hosts: PyPI and npm, raw GitHub content, docs.datadoghq.com and cloud.google.com. A **gap-filling pass** (sources A1-S112 to A1-S139) used a fresh search budget to add certifications, regions, pricing, funding, the current Mistral OCR version, DeepEval's OTel support and the W&B Weave record. Gap-fill sources are search-tool extracts of vendor pages, because the vendor hosts block direct fetches, so their confidence is capped at medium.

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| Langfuse – open source | Owned by ClickHouse, Inc. since January 2026. The core is MIT, but the product is open core: SCIM, audit logs, retention and project RBAC need an Enterprise licence key when self-hosted. Python SDK 4.17.0 (5 October 2026). | Acquired | A1-S021, A1-S022, A1-S023, A1-S033, A1-S001 |
| LangSmith – trace & eval | Still LangChain-owned. LangSmith has grown into an agent platform: Engine (beta), Fleet (renamed from Agent Builder), Sandboxes, LLM Gateway and Deployment. It offers BYOC and self-hosting on Enterprise. SOC 2 Type II, ISO 27001:2022 and HIPAA (BAA); US or EU region. | No change (scope broadened) | A1-S034, A1-S039, A1-S035, A1-S126 |
| Braintrust – evals platform | Independent; raised a US$80M Series B (February 2026). It now markets itself as "active observability for agents" (Topics, Loop, Gateway) and offers a hybrid data plane. | No change (repositioned) | A1-S028, A1-S043, A1-S041 |
| Phoenix – Atrace | Arize Phoenix under Elastic License 2.0, which is source-available, not OSI open source. Arize was acquired by Dynatrace (completed 1 October 2026). arize-phoenix 20.19.0. | Acquired | A1-S044, A1-S045, A1-S048, A1-S004 |
| DeepEval – LLM unit tests | Apache-2.0 framework from Confident AI. 4.2.8 (2 October 2026). Agentic and trajectory metrics have been added. | No change | A1-S005, A1-S051, A1-S068 |
| Promptfoo – red-teaming | Acquired by OpenAI (announced 9 March 2026; the README says "now part of OpenAI"). Still MIT. It does evals and red teaming, so the "red-teaming" descriptor is incomplete. 0.124.0. | Acquired | A1-S024, A1-S025, A1-S062, A1-S020 |
| Opik – comet | Opik by Comet ML. The whole platform is Apache-2.0, and self-hosting has no user management. 2.2.94. | No change | A1-S050, A1-S067, A1-S069, A1-S071 |
| Arize – RAG metrics | This is Arize AX, the commercial platform (Free / Pro US$50 / Enterprise), now a Dynatrace company. "RAG metrics" understates its scope. It duplicates the Arize vendor with the Phoenix tile. | Acquired; Duplicated | A1-S046, A1-S047, A1-S045 |
| Firecrawl – web to LLM-ready | The server is AGPL-3.0 and the SDKs are MIT. Agent, Browser and enterprise controls are Cloud-only. SOC 2 Type II, ZDR and PII redaction. API v2. Raised a US$75M Series B and launched Alexandria, an agent data library (22 September 2026). The privacy policy places data in the US. | No change (repositioned towards agent data; licence note) | A1-S053, A1-S076, A1-S079, A1-S129, A1-S134 |
| Docling – doc parser | MIT. Hosted by the LF AI & Data Foundation; originated at IBM Research Zurich. 2.135.0. Managed option via IBM watsonx. | No change (governance moved to foundation) | A1-S057, A1-S008, A1-S110 |
| LlamaParse – PDF / documents | LlamaParse is now the name of LlamaIndex's whole document platform (Parse, Extract, Index, Split, Agents), replacing the LlamaCloud branding. The old SDKs are deprecated, and the company's focus has shifted to LlamaParse. | Renamed | A1-S080, A1-S081, A1-S013, A1-S014 |
| Crawl4AI – open crawler | Apache-2.0 with an attribution clause. v0.9.4 (23 September 2026). A hosted Crawl4AI Cloud API has launched. | No change | A1-S009, A1-S056, A1-S074 |
| MinerU – PDF parser | MinerU 4.0 (4.0.10, 29 September 2026). Its custom licence is Apache-2.0 plus commercial-licence thresholds (more than 100M MAU or US$20M monthly revenue) and an attribution duty. It parses many formats, not just PDF. | Version label wrong (scope broader); licence note | A1-S010, A1-S054, A1-S055 |
| Reducto – enterprise docs | Proprietary API (Parse, Extract, Split, Edit, Classify, Pipeline). Vendor-stated SOC 2 Type II, HIPAA BAA, ZDR options, and VPC, on-prem or air-gapped deployment. EU and AU endpoints. US$75M Series B (a16z, October 2025). | No change | A1-S092, A1-S112, A1-S113, A1-S114 |
| Mistral OCR – OCR | Current model is OCR 4.1 (`mistral-ocr-latest`, July 2026) at US$4 per 1,000 pages. OCR 4.0 was retired on 30 September 2026. Self-hosting is available to enterprise customers, and the API is EU-hosted. | Version label wrong (unversioned; now OCR 4.1) | A1-S130, A1-S135, A1-S083 |
| Unstructured – ETL for docs | The Apache-2.0 library and ingest connectors are still free. The commercial offering is now the "Transform v2 API", with a dedicated or in-VPC Business tier. The vendor lists SOC 2 Type 2, ISO 27001 and HIPAA. Connectors emit ACL digests for incremental reprocessing. | Renamed (commercial API) | A1-S075, A1-S094, A1-S011, A1-S117 |
| Apify – scrapers | Actor platform with an MCP server. SOC 2 Type II. Hosted only in AWS us-east-1. | No change | A1-S085, A1-S086, A1-S089 |

## (b) Ambiguities owned

- **A4 "Phoenix – Atrace".** Resolved as **Arize Phoenix**. No product or feature called "Atrace" appears in Arize's README, docs or licence. The descriptor is most likely a garbled "Arize trace/tracing", since Phoenix's first listed capability is OpenTelemetry-based tracing (A1-S066). One correction to the graphic's framing: Phoenix is ELv2 source-available, not OSI open source (A1-S048, A1-S107, A1-S046).
- **A8 "Arize – RAG metrics" vs "Phoenix".** Resolved as two products from one vendor:
  - **Phoenix** is self-hosted, ELv2, has no feature gates and community support, and uses SQLite or PostgreSQL.
  - **Arize AX** is commercial SaaS or a licensed private deployment, running on the proprietary adb database. It adds Signal, SSO/RBAC/audit trails, multi-tenancy and SLAs.
  - Both use the same OTel/OpenInference instrumentation (A1-S046, A1-S047, A1-S066).
  - Both have been part of Dynatrace since 1 October 2026 (A1-S045).
  - The graphic's "RAG metrics" understates AX.
- **A18 "Opik – comet".** Resolved: Opik is developed by **Comet ML, Inc.** It ships either as a standalone Apache-2.0 product or as part of the Comet MLOps platform, hosted by Comet or self-hosted (A1-S071, A1-S050). "comet" names the owner, not a capability. No acquisition of Comet was found in this run. The Comet Trust Center lists SOC 2 Type 2, ISO/IEC 27001:2022 and ISO 9001 (A1-S122).

## (c) Hypothesis evidence

### H7: ingestion must include lineage, classification, PII/DLP, access-control metadata and incremental indexing

- Unstructured ingest connectors (SharePoint, OneDrive, Confluence):
  - They compute a `permissions_version` SHA-256 ACL digest at index time. Under incremental mode (`reprocess_all=false`, `reprocess_on_permission_change=true`), an ACL-only change triggers reprocessing.
  - An unavailable permission fetch is recorded separately from an empty permission set.
  - The ACL digest was introduced for OneDrive/SharePoint in 1.8.0, Teams channel files were added in 1.10.0, and Confluence incremental indexing (content version plus ACL digest) was added in 1.11.1. (A1-S094)
- In the unstructured-ingest changelog, "redaction" refers to **credentials in error logs**, not PII in document content. No content-PII detection was found in the open-source ingest changelog (A1-S094).
- Firecrawl:
  - It offers per-request PII redaction (`redactPII`, +4 credits/page), Zero Data Retention (+1 credit/page) and an opt-in prompt-injection check for JSON extraction (A1-S076, A1-S077).
  - Enterprise adds SSO/SCIM, IP and key restrictions, and a DPA (A1-S076).
  - No document-level ACL metadata or lineage was found.
- Docling:
  - It produces a unified DoclingDocument with hybrid chunking and runs locally, as a REST service or as a managed IBM watsonx service (A1-S057, A1-S110, A1-S111).
  - No ACL, PII or lineage features appear in its README or docs navigation (A1-S057).
- LlamaParse (formerly LlamaCloud):
  - The platform includes Index ("ingest, index, and RAG pipelines"), Extract, Split and Classify (A1-S080).
  - It offers an EU region where data stays in-region, BYOC and self-hosting via Helm, and OIDC SSO for self-hosted installs (A1-S115).
  - Permission sync, PII detection and lineage features were **not found**.
- Reducto:
  - The API has Classify, Split, Extract, Pipeline and Webhook resources, plus EU and AU endpoints (A1-S092, A1-S093).
  - Retention controls: API data auto-deletes within 24 hours, `retention=0` is available on Enterprise, and there is no training on customer data. VPC and air-gapped deployment are offered (A1-S112).
  - PII, ACL and lineage features were **not found**.
- Unstructured Platform: a Business tier offers a dedicated instance or in-VPC deployment with full data isolation (A1-S117).
- MinerU: local-first by default, with no upload unless `--remote` is set, and an explicit privacy rule to keep sensitive documents local (A1-S055). No ACL or lineage features.
- Lineage standard: OpenLineage is an open standard for run/job/dataset lineage metadata and an LF AI & Data Graduate project (A1-S096). None of the L8 product READMEs fetched mention OpenLineage or lineage. A grep of the Unstructured ingest changelog and the Docling, Firecrawl, Crawl4AI, MinerU and LlamaIndex READMEs found zero "lineage" matches (local check, 7 October 2026).
- Datadog Agent Observability scans and redacts sensitive data in LLM traces (A1-S097). This is relevant to C3 DLP at the observability tier, not at ingestion.

### H8: evaluation and observability are cross-cutting

- OpenTelemetry GenAI semantic conventions:
  - Status is still **"Development"**, not stable, as of 7 October 2026 (A1-S058).
  - In semconv v1.42.0, all `gen_ai.*`, `openai.*` and `mcp.*` definitions were deprecated in the core repository and moved to a dedicated repository, `open-telemetry/semantic-conventions-genai` (A1-S060).
  - The new repository covers client inference, agents, tool execution, retrieval, evaluation and MCP (A1-S061). It defines a `gen_ai.evaluation.result` event with evaluation name, score value, label and explanation (A1-S059).
- OTel and OpenInference support by product:
  - **Langfuse:** OTLP/HTTP (no gRPC). The SDKs are OTel-based. It maps `gen_ai.*` but its own attributes take precedence (A1-S032).
  - **LangSmith:** OTLP ingest, traces only per an older article. It originally required OpenLLMetry conventions; newer guides use GenAI conventions. Native format is recommended for performance (A1-S037).
  - **Braintrust:** OTLP trace endpoints in US and EU (A1-S042).
  - **Phoenix and AX:** built on OTel plus OpenInference (Apache-2.0) (A1-S049, A1-S066).
  - **Opik:** OTel over HTTP only (A1-S070).
  - **Promptfoo:** built-in OTLP receiver; uses GenAI semantic conventions (A1-S064).
  - **MLflow:** tracing built on OpenTelemetry (A1-S103).
  - **Datadog:** accepts OTel 1.37+ GenAI conventions or OpenInference (A1-S098).
  - **Mistral SDK:** opt-in OTel spans following GenAI conventions (A1-S084).
  - **DeepEval / Confident AI:** OTLP/HTTP endpoint (no gRPC); native ConfidentSpanExporter; framework OTel span processors; `run_otel` exports evaluation-run spans; regional endpoint via `CONFIDENT_OTEL_URL` (A1-S121).
  - **W&B Weave:** OTLP/HTTP protobuf endpoint plus a dedicated agents endpoint; Collector forwarding supported (A1-S139).
- Eval-in-CI:
  - LangSmith pytest plugin, enabled by default (A1-S108)
  - Phoenix pytest plugin (A1-S106)
  - Opik PyTest integration (A1-S067)
  - DeepEval, a "Pytest-like" framework that runs in any CI/CD (A1-S068)
  - Promptfoo with GitHub Actions, GitLab and Jenkins (A1-S065)
  - Braintrust Eval GitHub Action posting PR comments (A1-S109)
- Online evaluation and production coupling:
  - Opik online evaluation rules (LLM-as-a-judge on production traces) (A1-S072)
  - Langfuse LLM-as-a-judge and evaluators over ingested traces (A1-S073)
  - LangSmith Engine clusters production failures and proposes fixes or PRs (A1-S039)
  - Braintrust Topics, Loop and Patterns over production logs (A1-S043)
  - Arize AX Signal (A1-S046)
  - Datadog evaluations and Insights (A1-S097, A1-S099)
- Guardrail coupling:
  - Opik Guardrails (A1-S067)
  - Promptfoo planned in OpenAI Frontier for risk/compliance monitoring (A1-S024)
  - Firecrawl's prompt-injection check at ingestion (A1-S077)
- Consolidation signal: APM vendors now own or offer L9 products:
  - Dynatrace acquired Arize for US$915M (A1-S044)
  - Datadog Agent Observability (A1-S097)
  - ClickHouse owns Langfuse (A1-S021)
  - OpenAI owns Promptfoo (A1-S024)
  - CoreWeave owns Weights & Biases / Weave (completed 5 May 2025) (A1-S131)
- Regulatory expectations (SR 11-7, PRA SS1/23, EU AI Act post-market monitoring) were not researched in this stream; they belong to stream ⑧.

## (d) Missing products an enterprise architect would expect

- **MLflow (GenAI)**: open-source AI engineering platform with OTel-based tracing, evaluation, prompt registry and AI Gateway. Managed by Databricks, SageMaker, Azure ML, Nebius and OpenShift AI (A1-S103, A1-S019). *Added to products.json.*
- **Datadog Agent Observability** (LLM Observability): APM-integrated LLM and agent tracing, evaluations and sensitive-data redaction; billed per LLM span (A1-S097, A1-S098, A1-S099). *Added.*
- **W&B Weave**: tracing and evaluation toolkit for agents by Weights & Biases, part of CoreWeave since 5 May 2025. Weave 0.53.11 SDK is Apache-2.0. Deployment options are multi-tenant cloud, Dedicated Cloud and Self-Managed. SOC 2 Type II and ISO 27001/27017/27018 (A1-S104, A1-S018, A1-S131, A1-S137, A1-S138). *Added in the gap-fill pass.*
- **Google Cloud Document AI**: hyperscaler OCR, parsing and extraction, in scope for ISO 27001/27017/27018, SOC 1/2/3 and PCI DSS. Published per-page pricing (A1-S101, A1-S102). *Added.*
- **Azure AI Document Intelligence** and **AWS Textract**: the equivalent hyperscaler services. Not added, because learn.microsoft.com and docs.aws.amazon.com were blocked and the search budget was exhausted.
- **LiteParse** (LlamaIndex): Apache-2.0 open-source local text parser (A1-S080). Not material enough to add.

## (e) Gaps

- **Resolved in the gap-filling pass** (sources A1-S112 to A1-S139):
  - Arize AX: SOC 2, ISO 27001, EU region (Belgium)
  - certifications, regions and pricing for Confident AI, Comet/Opik, LlamaParse, Reducto, the Unstructured Platform and Mistral
  - Braintrust (no ISO 27001 found) and LangSmith (ISO 27001:2022)
  - funding for Firecrawl and Reducto
  - Mistral OCR 4.1
  - DeepEval OTel support
  - Weave ownership
- **Still open:**
  - **Crawl4AI funding:** only an aggregator (Tracxn) says it is unfunded; labelled Reported/low.
  - **Mistral OCR:** certification scope is company-level only; self-hosting licence terms and hardware sizing are not published.
  - **Firecrawl:** whether an EU processing region exists (sources conflict; the privacy policy says US).
  - **Datadog:** certifications.
  - **Platform access controls:** RBAC and SSO for the Unstructured Platform and Reducto SaaS.
  - **Confident AI:** funding.
  - **Audit scope:** whether vendor SOC 2 reports cover customer-run BYOC or self-hosted installs (LlamaParse, Confident AI, Reducto).
- **Conflicts recorded in stage_a_notes:**
  - Unstructured per-page rate (US$0.015 vs US$0.03)
  - Confident AI pricing (flat vs per-seat) and plan gating
  - Reducto ZDR tier eligibility and pricing framing (per page vs credits)
  - Firecrawl Series B date (blog 22 September 2026 vs changelog 20 August 2026)
  - Mistral OCR 4.1 launch date (16 vs 26 July 2026)
  - Comet Opik Pro price (US$19 now vs US$39 in a 2025 blog)
- **Vendor-authored pages:** the Reducto security claims come from llms.reducto.ai, an AI-oriented vendor site with internal inconsistencies. Request the SOC 2 report and BAA directly.
- **Blocked hosts** (cited via search extracts only): most vendor sites and trust centres, docs.mistral.ai, docs.unstructured.io, developers.llamaindex.ai, learn.microsoft.com, docs.aws.amazon.com, ir.dynatrace.com, github.com UI and API.
- **Axios on Braintrust's valuation** is paywalled. It is cited link-only (A1-S027), and its valuation figure is labelled Reported.
- **Promptfoo deal closing date.** OpenAI's release said closing was subject to conditions. The README "now part of OpenAI" is treated as evidence of completion, but no dated closing notice was found.
- **Langfuse acquisition date.** 16 January 2026 per comparisons; one wiki says 26 January.
- **Arize completion date.** 1 October 2026 per Dynatrace; one trade report says 2 October.
- **Not verified for most products:** GitHub star counts, download counts and named customers.
- **Unstructured version mismatch:** the unstructured-ingest changelog lists 1.11.21, while PyPI's latest is 1.11.19 (23 September 2026).
