# Stage A notes: stream A1 (L9 Evaluation and observability; L8 Data extraction and ingestion)

As of 7 October 2026. All source IDs refer to `work/stageA/A1_L9_L8/sources.csv`. Archive: `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A1/`.

**Research-environment caveat.** The shared web-search budget (200 calls per turn, shared by all agents) was used up part-way through this stream, after the L9 acquisition, Langfuse, LangSmith, Braintrust and Arize searches. After that, facts come only from hosts this environment can fetch directly: PyPI and npm metadata, raw GitHub content (vendor repositories, licence files and docs sources), docs.datadoghq.com and cloud.google.com. Most gaps in (e) come from this limit, not from vendors failing to publish.

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| Langfuse – open source | Owned by ClickHouse, Inc. since January 2026. The core is MIT, but the product is open core: SCIM, audit logs, retention and project RBAC need an Enterprise licence key when self-hosted. Python SDK 4.17.0 (5 October 2026). | Acquired | A1-S021, A1-S022, A1-S023, A1-S033, A1-S001 |
| LangSmith – trace & eval | Still LangChain-owned. LangSmith has grown into an agent platform: Engine (beta), Fleet (renamed from Agent Builder), Sandboxes, LLM Gateway and Deployment. It offers BYOC and self-hosting on Enterprise. | No change (scope broadened) | A1-S034, A1-S039, A1-S035 |
| Braintrust – evals platform | Independent; raised a US$80M Series B (February 2026). It now markets itself as "active observability for agents" (Topics, Loop, Gateway) and offers a hybrid data plane. | No change (repositioned) | A1-S028, A1-S043, A1-S041 |
| Phoenix – Atrace | Arize Phoenix under Elastic License 2.0, which is source-available, not OSI open source. Arize was acquired by Dynatrace (completed 1 October 2026). arize-phoenix 20.19.0. | Acquired | A1-S044, A1-S045, A1-S048, A1-S004 |
| DeepEval – LLM unit tests | Apache-2.0 framework from Confident AI. 4.2.8 (2 October 2026). Agentic and trajectory metrics have been added. | No change | A1-S005, A1-S051, A1-S068 |
| Promptfoo – red-teaming | Acquired by OpenAI (announced 9 March 2026; the README says "now part of OpenAI"). Still MIT. It does evals and red teaming, so the "red-teaming" descriptor is incomplete. 0.124.0. | Acquired | A1-S024, A1-S025, A1-S062, A1-S020 |
| Opik – comet | Opik by Comet ML. The whole platform is Apache-2.0, and self-hosting has no user management. 2.2.94. | No change | A1-S050, A1-S067, A1-S069, A1-S071 |
| Arize – RAG metrics | This is Arize AX, the commercial platform (Free / Pro US$50 / Enterprise), now a Dynatrace company. "RAG metrics" understates its scope. It duplicates the Arize vendor with the Phoenix tile. | Acquired; Duplicated | A1-S046, A1-S047, A1-S045 |
| Firecrawl – web to LLM-ready | The server is AGPL-3.0 and the SDKs are MIT. Agent, Browser and enterprise controls are Cloud-only. SOC 2 Type II, ZDR and PII redaction. API v2. | No change (licence note) | A1-S053, A1-S076, A1-S079 |
| Docling – doc parser | MIT. Hosted by the LF AI & Data Foundation; originated at IBM Research Zurich. 2.135.0. Managed option via IBM watsonx. | No change (governance moved to foundation) | A1-S057, A1-S008, A1-S110 |
| LlamaParse – PDF / documents | LlamaParse is now the name of LlamaIndex's whole document platform (Parse, Extract, Index, Split, Agents), replacing the LlamaCloud branding. The old SDKs are deprecated, and the company's focus has shifted to LlamaParse. | Renamed | A1-S080, A1-S081, A1-S013, A1-S014 |
| Crawl4AI – open crawler | Apache-2.0 with an attribution clause. v0.9.4 (23 September 2026). A hosted Crawl4AI Cloud API has launched. | No change | A1-S009, A1-S056, A1-S074 |
| MinerU – PDF parser | MinerU 4.0 (4.0.10, 29 September 2026). Its custom licence is Apache-2.0 plus commercial-licence thresholds (more than 100M MAU or US$20M monthly revenue) and an attribution duty. It parses many formats, not just PDF. | Version label wrong (scope broader); licence note | A1-S010, A1-S054, A1-S055 |
| Reducto – enterprise docs | Proprietary API (Parse, Extract, Split, Edit, Classify, Pipeline) with EU and AU regional endpoints. Security posture not verified. | Not publicly verified | A1-S090, A1-S092, A1-S093 |
| Mistral OCR – OCR | OCR API (/v1/ocr) with annotations, tables and confidence scores. The current model version is not verified. | Not publicly verified | A1-S083, A1-S084 |
| Unstructured – ETL for docs | The Apache-2.0 library and ingest connectors are still free. The commercial offering is now the "Transform v2 API". Connectors emit ACL digests for incremental reprocessing. | Renamed (commercial API) | A1-S075, A1-S094, A1-S011 |
| Apify – scrapers | Actor platform with an MCP server. SOC 2 Type II. Hosted only in AWS us-east-1. | No change | A1-S085, A1-S086, A1-S089 |

## (b) Ambiguities owned

- **A4 "Phoenix – Atrace".** Resolved as **Arize Phoenix**. No product or feature called "Atrace" appears in Arize's README, docs or licence. The descriptor is most likely a garbled "Arize trace/tracing", since Phoenix's first listed capability is OpenTelemetry-based tracing (A1-S066). One correction to the graphic's framing: Phoenix is ELv2 source-available, not OSI open source (A1-S048, A1-S107, A1-S046).
- **A8 "Arize – RAG metrics" vs "Phoenix".** Resolved as two products from one vendor:
  - **Phoenix** is self-hosted, ELv2, has no feature gates and community support, and uses SQLite or PostgreSQL.
  - **Arize AX** is commercial SaaS or a licensed private deployment, running on the proprietary adb database. It adds Signal, SSO/RBAC/audit trails, multi-tenancy and SLAs.
  - Both use the same OTel/OpenInference instrumentation (A1-S046, A1-S047, A1-S066).
  - Both have been part of Dynatrace since 1 October 2026 (A1-S045).
  - The graphic's "RAG metrics" understates AX.
- **A18 "Opik – comet".** Resolved: Opik is developed by **Comet ML, Inc.** It ships either as a standalone Apache-2.0 product or as part of the Comet MLOps platform, hosted by Comet or self-hosted (A1-S071, A1-S050). "comet" names the owner, not a capability. No acquisition of Comet was found, but the search budget ran out before a dedicated query, so this is not conclusive.

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
- LlamaParse (formerly LlamaCloud): the platform includes Index ("ingest, index, and RAG pipelines"), Extract, Split and Classify-style functions (A1-S080). Permission sync, PII and lineage features could **not be verified**.
- Reducto: the API has Classify, Split, Extract, Pipeline and Webhook resources, plus EU and AU endpoints (A1-S092, A1-S093). PII, ACL and lineage features could **not be verified**.
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
  - **DeepEval:** OTel support not verified.
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
- Regulatory expectations (SR 11-7, PRA SS1/23, EU AI Act post-market monitoring) were not researched in this stream; they belong to stream ⑧.

## (d) Missing products an enterprise architect would expect

- **MLflow (GenAI)**: open-source AI engineering platform with OTel-based tracing, evaluation, prompt registry and AI Gateway. Managed by Databricks, SageMaker, Azure ML, Nebius and OpenShift AI (A1-S103, A1-S019). *Added to products.json.*
- **Datadog Agent Observability** (LLM Observability): APM-integrated LLM and agent tracing, evaluations and sensitive-data redaction; billed per LLM span (A1-S097, A1-S098, A1-S099). *Added.*
- **W&B Weave**: tracing and evaluation toolkit for agents by Weights & Biases; weave 0.53.11, Apache-2.0 (A1-S104, A1-S018). *Not added*, because its ownership (a reported CoreWeave acquisition of W&B) could not be verified in this run.
- **Google Cloud Document AI**: hyperscaler OCR, parsing and extraction, in scope for ISO 27001/27017/27018, SOC 1/2/3 and PCI DSS. Published per-page pricing (A1-S101, A1-S102). *Added.*
- **Azure AI Document Intelligence** and **AWS Textract**: the equivalent hyperscaler services. Not added, because learn.microsoft.com and docs.aws.amazon.com were blocked and the search budget was exhausted.
- **LiteParse** (LlamaIndex): Apache-2.0 open-source local text parser (A1-S080). Not material enough to add.

## (e) Gaps

- **Web-search budget exhausted** part-way through the stream. The following were therefore not verified:
  - Arize AX SOC 2, ISO 27001 and EU region
  - Confident AI, Comet/Opik Cloud, LlamaParse, Reducto, Unstructured Platform and Mistral certifications, residency and pricing
  - Firecrawl, Reducto, Crawl4AI and Confident AI funding
  - the current Mistral OCR model version
- **Blocked hosts** (cited only where an extract or repository copy existed): most vendor sites, docs.mistral.ai, docs.unstructured.io, learn.microsoft.com, docs.aws.amazon.com, ir.dynatrace.com, github.com UI and API.
- **Axios on Braintrust's valuation** is paywalled. It is cited link-only (A1-S027), and its valuation figure is labelled Reported.
- **Promptfoo deal closing date.** OpenAI's release said closing was subject to conditions. The README "now part of OpenAI" is treated as evidence of completion, but no dated closing notice was found.
- **Langfuse acquisition date.** 16 January 2026 per comparisons; one wiki says 26 January.
- **Arize completion date.** 1 October 2026 per Dynatrace; one trade report says 2 October.
- **Datadog Trust Hub** (A1-S100) snapshot did not render a certification list, so Datadog certifications are NPV.
- **Not verified for most products:** GitHub star counts, download counts and named customers (only vendor-stated Langfuse and Opik figures were captured).
- **Unstructured version mismatch:** the unstructured-ingest changelog lists 1.11.21, while PyPI's latest is 1.11.19 (23 September 2026).
