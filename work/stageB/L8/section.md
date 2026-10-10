## 8. Data extraction, ingestion and web

> L8 turns source material (enterprise documents, scans, spreadsheets, slides, e-mails and web pages) into clean, structured, permission-tagged content that retrieval (L7/L6) and agents can trust. It is more than a shelf of parsers and scrapers, and the products have moved: LlamaParse is now the name of LlamaIndex's whole document platform [VF: A1-S080, V1-S008]; Mistral OCR is at version 4.1, with 4.0 retired on 30 September 2026 [VF: A1-S130, V1-S014]; Docling graduated within LF AI & Data in August 2026 [VF: V1-S091]; and Firecrawl's server is AGPL-3.0, with its enterprise controls offered only in the Cloud [VF: A1-S053, A1-S079]. Of the ten products assessed, only Unstructured's open-source connectors carry access-control metadata into the pipeline [VF: A1-S094], and none emits lineage [VF: A1-S094, A1-S096]. The parsers are commodity components; the enterprise value is in the control plane that wraps them [AJ]. **Recommendation:** standardise on a self-hosted, open document model (Docling as default, Unstructured ingest where connectors with ACLs are needed), put managed parsers and OCR engines behind that model as replaceable engines, and build the lineage, classification, entitlement and incremental-indexing envelope yourself [Rec].

### 8.1 Responsibility

L8 owns the path from an approved source to an indexed, governed unit of content: source → acquisition → parsing → OCR → structure extraction → cleaning → chunking → metadata → indexing (plan §5), across PDFs and scans, tables, PowerPoint and Excel, websites, e-mails, enterprise documents, structured data and multimodal documents [AJ].

The layer has two distinct jobs, and they are easily blurred [AJ]:

1. **Acquisition:** getting bytes from a source the firm is entitled to use. Web acquisition (Firecrawl, Crawl4AI, Apify) raises questions of law, terms of service, robots.txt and provenance. Enterprise acquisition (connectors into SharePoint, OneDrive, Confluence, S3) raises questions of entitlements and change detection [AJ].
2. **Document understanding:** turning bytes into faithful structure: text, reading order, tables, figures and their coordinates. Docling, LlamaParse, MinerU, Reducto, Unstructured, Mistral OCR and Google Document AI compete here [AJ].

**Hand-offs.**

- **Downwards (sources and C3).** L8 receives documents only from sources on an approved-source register, and it receives classification and PII policy from C3 [Rec].
- **Upwards (L7 and L6).** L8 hands over chunks wrapped in a metadata envelope (source, version, ACL principals, classification, PII flags, parser manifest, lineage run ID). L7 embeds those chunks and L6 stores them with the envelope intact, so that retrieval-time filtering can enforce entitlements [Rec].
- **Sideways (L4).** L8 is not the agent's live web tool. Firecrawl, Crawl4AI and Apify all expose agent-facing interfaces (MCP or search endpoints) that overlap L4 [VF: A1-S077, A1-S074, A1-S089]. Batch ingestion into a governed corpus belongs to L8. Runtime browsing by an agent belongs to L4 and is governed as a tool call [AJ].
- **To C8.** Lineage events and parse manifests flow to the governance and evidence store [Rec].

### 8.2 Why it matters

L8 failures surface as model failures [AJ]. A merged table cell becomes a "hallucinated" number; a permission that never reached the index becomes a data leak; a web page with hidden instructions becomes an indirect prompt injection; a parser upgrade silently shifts chunk boundaries [AJ]. ESMA expects "ex-ante input controls and frequent ex-post output controls" for AI used in investment services [VF: R-INTL-AI-ASSETMGMT; A8-S058, A8-S059]. In a RAG system, L8 is where the input controls live [AJ].

**Illustrative scenario [AJ].** A multi-asset fund's monthly factsheet has a performance table with fund, benchmark and relative columns. After a routine library upgrade, the parser starts merging two header cells, so the "relative" column shifts one place left for a single share class. Nothing fails: parsing succeeds, chunks are indexed and retrieval works. The commentary agent retrieves last quarter's factsheet as context and repeats a relative-return figure that is really the benchmark return. The reviewer checks the current month's numbers against the attribution engine but not the prior-period comparison that the draft quoted. Nothing in the pipeline records which parser version produced the chunk, so nobody can tell which other documents are affected. The firm has to re-parse and re-review a quarter's corpus by hand. The cause was an unpinned parser and the absence of any table-reconciliation check, not the LLM [AJ].

### 8.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Table cell exact-match | Share of numeric table cells reproduced exactly (value, sign, unit, row/column) | ≥ 99.5% on a golden set of house documents; 100% for any table feeding a published number | Golden set of factsheets and reports with hand-keyed tables; run on every parser or model change |
| Text fidelity (OCR) | Character error rate on scanned pages | Set per document class; track the trend after each engine change | Sampled pages against reference transcriptions |
| Structural fidelity | Correct reading order, headings and table boundaries | ≥ 95% of sampled pages judged correct | Reviewer sample, stratified by layout type |
| Envelope completeness | Share of indexed chunks carrying source ID, version, ACL, classification, parser manifest and lineage run ID | 100% (hard gate: no envelope, no index) | Index-time validation rule |
| ACL propagation lag | Time from a permission change at source to the index reflecting it | Under 1 hour for confidential sources; under 24 hours otherwise | Synthetic permission-change probes |
| Deletion propagation lag | Time from source deletion to removal from every index and cache | Under 24 hours | Tombstone probes |
| Residual PII rate | PII found after redaction in sampled chunks | Zero for classes that must be masked | Second-pass scanner on samples |
| Reproducibility | Share of re-parses with a pinned manifest that produce identical output hashes | 100% for self-hosted engines; documented exceptions for hosted ones | Periodic re-parse jobs |
| Unapproved-source ingestions | Documents ingested from sources not on the register | Zero | Register check at acquisition |
| Cost per 1,000 pages | All-in parse, OCR and compute cost | Budgeted per document class | FinOps tags (C6) |

### 8.4 How it works

![L8 ingestion: controls before and after replaceable parsing engines](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/L8-1.png){width=100%}

*Figure: Every source starts on the approved-source register, passes acquisition and pre-parse controls (with a quarantine exit) before swappable parsing and OCR engines run, and leaves validated, enveloped chunks for incremental indexing with lineage sent to C8. Editable source: `08_Graphic/diagrams/L8-1.md`.* [AJ]

**Content-type coverage.** Docling covers PDF, DOCX/XLSX/PPTX, legacy Office, HTML, CSV, images, audio and video [VF: A1-S111]. MinerU covers PDF, Office, EPUB, OFD, HTML and CSV [VF: A1-S055]. LlamaParse claims 130+ formats [VF: A1-S080]. E-mail (with attachments and thread structure) is not documented as a first-class format for any L8 product in the fact base [NPV]. Structured data should bypass document parsing and enter through governed data pipelines or L4 tools [AJ].

**Mechanics by stage.**

- **Acquisition.** Firecrawl respects robots.txt by default [VF: A1-S053]. Its X and LinkedIn data are routed through third-party providers at separate prices [VF: A1-S077, A1-S053], so the provenance of that content is one step further removed [AJ]. On the enterprise side, Unstructured's SharePoint, OneDrive and Confluence connectors compute a `permissions_version` SHA-256 digest of the ACL at index time. In incremental mode (`reprocess_all=false`, `reprocess_on_permission_change=true`), a change to the ACL alone triggers reprocessing [VF: A1-S094]. The connectors also record an unavailable permission fetch separately from an empty permission set [VF: A1-S094]. That distinction is what stops a failed lookup from being read as "public" [AJ].
- **Parsing and OCR.** Mistral OCR 4 returns paragraph-level bounding boxes, structural block labels and block-level confidence scores [VF: A1-S130, A1-S135]. Google Document AI's Layout Parser includes initial chunking [VF: A1-S101]. MinerU 4.0 adds citation locators for agent reading [VF: A1-S055]. Keep coordinates, confidence scores and locators rather than flattening to Markdown; reconciliation and citations depend on them [AJ].
- **Validation.** No product in this layer offers reconciliation of parsed tables against an authoritative source; that has to be built [AJ]. Firecrawl offers an opt-in prompt-injection check for JSON extraction [VF: A1-S077]. No equivalent was found in the document parsers [AJ].
- **Lineage.** OpenLineage defines run, job and dataset entities extended by facets [VF: A7-S041]. Its changelog has no GenAI-, LLM-, embedding- or vector-specific facets [VF: A7-S042], so parse, chunk, embed and index steps must be modelled as generic jobs or custom facets [AJ]. OpenLineage supports user-supplied tags facets, which can carry classification labels [VF: A7-S042]. Apache Airflow ships an OpenLineage provider [VF: A7-S045], so an Airflow-orchestrated ingestion pipeline can emit lineage without new tooling [AJ].

### 8.5 Enterprise design principles

**Security.**

- Treat every ingested document as untrusted input. The OWASP Top 10 for Agentic Applications for 2026 lists ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC; A8-S042]. Indirect injection through documents an agent reads is the L8 route to it [AJ].
- Scan before parsing, and quarantine anything that fails [Rec].
- Run parsers with no outbound network access, so that a malicious document cannot exfiltrate data [Rec].

**Data protection.**

- Classify and apply DLP before content reaches any third-party engine, not at the prompt [Rec].
- Presidio (MIT, now community-governed under Data Privacy Stack) and Google Sensitive Data Protection are the C3 candidates for this step [VF: A6-S040, A6-S066].
- Presidio's own README warns that it is not guaranteed to find all sensitive data [VF: A6-S068]. Sampling for residual PII is therefore a KPI, not an option [AJ].

**Entitlements.**

- Capture ACLs at acquisition, carry them on every chunk, and fail closed when the permission fetch fails [Rec].
- The Unstructured connector pattern (ACL digest, separate "unavailable" state, reprocess on change) is the reference behaviour to require of any connector, bought or built [Rec].

**Reproducibility.**

- Pin every engine version and model ID, and write them into a parse manifest stored with the output [Rec].
- Store parsed outputs, not just raw documents. Docling had reached 2.135.0 by 7 October 2026 [VF: A1-S008], and Mistral retired OCR 4.0 on 30 September 2026 [VF: A1-S130]. A hosted model that has been retired cannot reproduce last quarter's parse [AJ].

**Scalability and cost.**

- Route by document class: a cheap OCR tier for simple scans and expensive agentic tiers only for complex layouts [Rec].
- Published prices differ by more than an order of magnitude between engines. Document AI Enterprise OCR costs US$1.50 per 1,000 pages [VF: A1-S101]. Mistral OCR 4.1 costs US$4 per 1,000 pages [VF: A1-S130]. Reducto Parse costs US$10 per 1,000 pages [VF: A1-S113]. LlamaParse tiers run from 1 to 45 credits per page [VF: A1-S116]. All prices are as of 7 October 2026.

**Portability and observability.** Keep one canonical document model in-house with engines behind an adapter; a passing golden-set regression run is the switching test. Emit lineage events and pipeline metrics (quarantine rate, confidence distribution, reconciliation failures) to L9 and C8 [Rec].

**Patterns** [Rec]:
- Approved-source register as the only entry point.
- Dual-parse reconciliation for tables that feed numbers.
- Incremental indexing on content hash plus ACL digest, with tombstones for deletions.
- Quarantine queue with human release.
- Parse manifest with every output.

**Anti-patterns** [AJ]:
- Letting a vendor's managed index become the system of record for entitled content.
- Using a model "latest" alias in production.
- Flattening tables to prose before validation.
- Treating an agent's live web fetches as ingestion.
- Indexing first and classifying later.
- Using marketplace scrapers on any non-public data.

### 8.6 Product selection criteria

| Scorecard criterion | What to evaluate in L8 |
|---|---|
| Technical capability | Table and layout fidelity on *your* golden set; format coverage; coordinates and confidence output; connector ACL capture |
| Enterprise readiness | SSO, RBAC and audit on the hosted service; support terms; for libraries, an API-server mode |
| Security and compliance | SOC 2 Type II and ISO 27001 scoped to the parsing service (and BYOC installs); retention controls; training-use terms; CVE handling for open source |
| Deployment flexibility | Self-hosted, in-VPC or air-gapped options; EU and UK processing regions; network-isolated operation |
| Ecosystem | Connectors to your sources and stores; orchestration and lineage hooks (Airflow, OpenLineage) |
| Reliability and maturity | Deprecation and model-retirement windows; governance (foundation, single maintainer, venture-backed) |
| Cost / TCO | Price per 1,000 pages by tier; GPU needs for self-hosting; licence thresholds; operations burden (browsers, proxies, anti-bot) |
| Lock-in / portability | Open output format; ability to re-parse elsewhere; licence (AGPL, custom thresholds, attribution); platform reach into L6/L3 |

Vendor accuracy claims, such as Unstructured's statement that its API gives 2x table content accuracy and 58% less invented content than the open-source library, are reported claims only [R: A1-S075]. They should not be used as decision inputs [AJ].

### 8.7 Product deep dives

#### Document understanding

**Docling (LF AI & Data Foundation; started by IBM Research).**
- *What it is now:* Docling is an MIT-licensed toolkit that parses PDF, Office (including legacy Office), ODF, HTML, images, audio and video into a unified DoclingDocument, with OCR, VLM pipelines, ASR and hybrid chunking [VF: A1-S057, A1-S111]. IBM Research Zurich started it, IBM donated it to LF AI & Data in March 2025, and it reached Graduate tier in August 2026 [VF: A1-S057, V1-S091]. It runs as a library, CLI, docling-serve REST API (stable v1) or MCP server, and IBM offers a managed "Docling for IBM watsonx" [VF: A1-S082, A1-S110]. The current version is 2.135.0, released 7 October 2026 [VF: A1-S008].
- *Project hygiene:* it publishes a security policy with private vulnerability reporting, takes part in the OpenSSF Best Practices badge programme and signs its releases on PyPI, Quay.io and GHCR [VF: B-REV-S001].
- *Strengths:* neutral governance, a permissive licence and local processing [VF: A1-S057]. The DoclingDocument can serve as the firm's canonical document model [AJ].
- *Limitations:* the README and docs navigation show no ACL, PII or lineage features [VF: A1-S057]. Individual models carry their own licences [VF: A1-S057]. Releases are very frequent, so pinning is mandatory [AJ].
- *Choose when:* documents must stay in your estate and you want an open format that outlives engine changes [AJ].
- *Avoid when:* you have no platform team to run a Python service [AJ].
- *Competitors:* Unstructured, MinerU, LlamaParse.
- *FS note:* the default engine for confidential and client documents, provided the parse manifest is recorded [Rec].
- **Tier: Strategic. Flag: none.** Inherits host controls.

**Unstructured (Unstructured Technologies).**
- *What it is now:* the Apache-2.0 `unstructured` library (0.27.16, 5 October 2026) and `unstructured-ingest` connectors stay free [VF: A1-S011, A1-S075, A1-S095]. The commercial offering is the Transform v2 API, with shared pay-as-you-go, dedicated and in-VPC Business tiers [VF: A1-S117, V1-S019]. The vendor lists SOC 2 Type 2, ISO 27001, HIPAA and GDPR, and has announced CMMC 2.0 Level 2 [VF: A1-S117, V1-S090].
- *Strengths:* it is the only L8 product with verified permission-aware ingestion: the ACL digest, reprocessing on permission change, and a separate "permission unavailable" state [VF: A1-S094]. It also offers a broad set of connectors out to vector stores and warehouses [VF: A1-S094].
- *Limitations:*
  - SAML 2.0 and OIDC SSO with account- and workspace-level roles are documented for Business deployments, but no workspace audit log is documented [VF: B-REV-S016].
  - The best models are API-only [VF: A1-S075].
  - The library is still pre-1.0 after four years [VF: A1-S011].
  - The per-page price conflicts between US$0.015 and US$0.03 [VF: A1-S117, A1-S118].
  - Usage analytics are on by default [VF: A1-S075].
  - In the ingest changelog, "redaction" means credentials in error logs, not PII in content [VF: A1-S094].
- *Choose when:* entitlement-preserving ingestion from SharePoint, OneDrive or Confluence matters [AJ].
- *Avoid when:* you need a documented, exportable audit log on the hosted service today [AJ].
- *Competitors:* Docling, LlamaParse, Reducto.
- *FS note:* run the open-source connectors in your estate and use the ACL digest as the entitlement source of truth for the index [Rec].
- **Tier: Strategic. Flag: Renamed.**

**LlamaParse (LlamaIndex, Inc.).**
- *What it is now:* LlamaParse is now LlamaIndex's whole document platform: Parse, Extract, Index, Split and Agents, previously marketed as LlamaCloud [VF: A1-S080, A1-S081, V1-S008]. LlamaIndex says its primary focus has shifted from the open-source framework to LlamaParse [VF: A1-S080]. Regions are NA and EU, with in-region EU storage and processing, an EU DPA and SCCs. BYOC is available on Azure, AWS and GCP, along with Helm self-hosting and on-premises installs [VF: A1-S115]. It holds SOC 2 Type II, offers a HIPAA pipeline with a BAA on request, and supports OIDC SSO for self-hosted installs [VF: A1-S115, A1-S116]. Pricing runs from Free to Enterprise, with parse tiers from 1 to 45 credits per page [VF: A1-S116].
- *Access control:* the managed service supports SSO through SAML and OIDC, but on the hosted service every organisation member has the same access to projects and resources; named roles exist only in self-hosted installs, and audit logs are not documented [VF: B-REV-S023]. Under CP2 rule 7, verified SSO lifts the enterprise-readiness cap to 3; flat hosted roles and the missing audit log keep it there [AJ].
- *Strengths:* breadth of formats (130+) and flexible residency [VF: A1-S080, A1-S115].
- *Limitations:* permission sync, PII detection and lineage were not found [VF: A1-S080]. The legacy SDKs were deprecated in 2026 [VF: A1-S013]. Whether the SOC 2 report covers BYOC installs is not stated [NPV]. The platform reaches into L6 (Index) and L3 (Agents) [VF: A1-S080].
- *Choose when:* you want managed parsing with an EU region or BYOC [AJ].
- *Avoid when:* its Index would become your system of record [AJ].
- *Competitors:* Reducto, Unstructured, Docling.
- *FS note:* use Parse and Extract only, and keep indexing in your own L6 store [Rec].
- **Tier: Tactical. Flag: Renamed.**

**Reducto (Reducto, private).**
- *What it is now:* Reducto is a proprietary API with Parse, Extract, Split, Edit, Classify and Pipeline resources, webhooks, and EU and AU endpoints [VF: A1-S092, A1-S093]. Vendor pages state SOC 2 Type I and II, HIPAA BAAs, 24-hour auto-deletion, `retention=0` on Enterprise, no training on customer data, and VPC, on-prem and air-gapped deployment [VF: A1-S112]. It has raised US$108M in total, including a Series B led by a16z in October 2025 [VF: A1-S114, V1-S018]. Pricing is US$10 per 1,000 pages for Parse and US$20 for Extract [VF: A1-S113].
- *Strengths:* extraction-oriented API design and deployment options on paper [AJ].
- *Limitations:* the security claims come from vendor-authored pages that contradict each other on ZDR eligibility, and the verifier lists them as not to be relied on. Request the SOC 2 report and BAA directly [VF: A1-S112]. SSO/SAML and RBAC are Enterprise-only features in the product docs [VF: B-REV-S017]. No PII, ACL or lineage features were found [VF: A1-S093].
- *Choose when:* complex layouts justify a managed extraction API and due diligence produces the reports [AJ].
- *Avoid when:* the reports cannot be obtained [AJ].
- *Competitors:* LlamaParse, Google Document AI, Unstructured.
- *FS note:* score it on evidence received, not on vendor pages [Rec].
- **Tier: Tactical. Flag: none.**

**MinerU (OpenDataLab MinerU Team).**
- *What it is now:* the MinerU 4.0 line (4.0.10, 29 September 2026) parses PDF, images, Office, OpenDocument, EPUB, OFD, HTML and CSV. It offers four tiers (Flash, Basic, Standard, Advanced), a document library with citation locators, and a router [VF: A1-S010, A1-S055]. It parses locally by default and uploads nothing unless `--remote` is set [VF: A1-S055].
- *Licence:* the "MinerU Open Source License" is Apache-2.0 plus additional terms. A separate commercial licence is required above 100M MAU or US$20M monthly revenue, measured group-consolidated. Online services must give attribution, and rights terminate automatically on breach [VF: A1-S054, V1-S003]. The commercial price is not published [VF: A1-S054].
- *Strengths:* local-first operation, citation locators, and telemetry that excludes document content and can be disabled [VF: A1-S055].
- *Limitations:* the Standard and Advanced tiers need a GPU with 8 GB+ VRAM [VF: A1-S055]. A 3.x to 4.0 migration happened in 2026 [VF: A1-S055].
- *Choose when:* you are under the thresholds or hold a commercial licence. It can also serve as a second parser for reconciliation [AJ].
- *Avoid when:* a large group has no commercial licence [AJ].
- *Competitors:* Docling, Unstructured, LlamaParse.
- *FS note:* many large asset managers will exceed the group revenue threshold, so legal review comes first [AJ].
- **Tier: Experimental. Flag: none.**

**Mistral OCR (Mistral AI).**
- *What it is now:* the current model is OCR 4.1 (`mistral-ocr-4-1`, aliases `mistral-ocr-latest` and `mistral-ocr-4`), part of Mistral Document AI. Vendor pages disagree on whether it was released in July or August 2026; the changelog marked it GA on 26 August 2026 [VF: A1-S130, V1-S014]. OCR 4.0 was retired on 30 September 2026. OCR 3 remains for existing integrations, and the original Mistral OCR is no longer maintained [VF: A1-S130, V1-S014]. Pricing is US$4 per 1,000 pages, or US$2 in batch [VF: A1-S130, V1-S010]. The managed API is EU-hosted, and enterprise customers can self-manage it as a single container, in a private cloud or on-premises [VF: A1-S135].
- *Certifications and access control:* Mistral holds SOC 2 Type II, ISO 27001:2022 and ISO 27701:2019 at company level, and the OCR scope is not confirmed [VF: A1-S136]. Enterprise plans add SAML SSO, organisation roles with isolated Workspaces and SCIM provisioning, and audit logs that cannot be exported [VF: B-REV-S014, B-REV-S015]. All three controls plus SCIM score enterprise readiness 4 under CP2 rule 7; the company-level certifications score security 3 under rule 8 [AJ].
- *Strengths:* EU residency, block-level confidence scores, and price [VF: A1-S130, A1-S135].
- *Limitations:* model-version churn is the operational risk: about five weeks passed between 4.1 GA and 4.0 retirement [VF: A1-S130, V1-S014]. That window is short for a regulated re-validation cycle [AJ]. Self-hosting terms and sizing are unpublished [NPV]. Audit logs that cannot be exported cannot be held in the firm's own archive, so ask for an export route in due diligence [Rec].
- *Choose when:* you need an EU or self-managed OCR engine behind your own pipeline [AJ].
- *Avoid when:* you cannot re-validate within weeks [AJ].
- *Competitors:* Google Document AI, Docling's built-in OCR, Reducto.
- *FS note:* pin the dated model ID and treat each retirement as a change-control event [Rec].
- **Tier: Tactical. Flag: none.**

**Google Cloud Document AI (Google Cloud; added).**
- *What it is now:* Document AI provides processors for Enterprise Document OCR, Form Parser, Layout Parser (with chunking), Custom Extractor, classifier/splitter and Summarizer [VF: A1-S101]. It is in scope for Google Cloud's ISO 27001/27017/27018, SOC 1/2/3 and PCI DSS [VF: A1-S102]. OCR costs US$1.50 per 1,000 pages (US$0.60 above 5M pages), and Layout Parser costs US$10 [VF: A1-S101].
- *Access control:* access runs through Google Cloud IAM, including deny policies, with VPC Service Controls, IAM-governed Cloud Audit Logs and SAML/OIDC federation at platform level [VF: B-REV-S010, B-REV-S012]. Under the CP2 hyperscaler presumption (rule 6), enterprise readiness scores 4 [AJ]; platform controls presumed (CP2 Q1); confirm per service [Rec].
- *Strengths:* certifications and price [VF: A1-S101, A1-S102]. Google Cloud EMEA Limited is designated under both DORA and the UK CTP regime [VF: R-DORA, R-UK-CTP; A8-S020, A8-S023].
- *Limitations:* outputs are Google-specific, and the service requires Google Cloud [VF: A1-S101]. It offers us and eu multi-regions, regional processors, CMEK (allowlisted in some regions), VPC Service Controls and IAM deny policies [VF: B-REV-S010, B-REV-S011]. Azure AI Document Intelligence and AWS Textract are the equivalent services but are not in the fact base [NPV].
- *Choose when:* GCP is your approved cloud [AJ].
- *Avoid when:* you are reducing hyperscaler concentration [AJ].
- *Competitors:* Mistral OCR, Reducto, and the Azure and AWS equivalents.
- *FS note:* under the UK CTP regime, regulated firms remain responsible for their own due diligence and contingency planning [VF: R-UK-CTP; A8-S023].
- *Security score (CP3 rework):* 4, not 5. The scope page names a "SOC 2 Report" without stating Type II [VF: A1-S102], and rule 8 needs SOC 2 Type II in the product's scope for a 5; the same Google scope evidence gives 4 for Sensitive Data Protection (C3), Model Armor (C2) and Apigee (C1) [AJ].
- **Tier: Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. Flag: none.** It is Google's lead document-processing service. Confirm the processor region, and keep outputs in the firm's canonical document model so that processor lock-in (2) stays an engine choice [AJ].

#### Web acquisition

**Firecrawl (Firecrawl; PyPI author Mendable.ai).**
- *What it is now:* Firecrawl is a web data API (v2) covering scrape, crawl, map, search, extract and parse, plus Agent, Browser and Interact [VF: A1-S077, A1-S079]. The server is AGPL-3.0 and the SDKs are MIT. Agent, Browser, dashboards and enterprise controls are Cloud-only [VF: A1-S053, A1-S079, V1-S002]. Per-request options include PII redaction (+4 credits per page), ZDR (+1) and a prompt-injection check for JSON extraction. Enterprise adds SSO, SCIM, key restrictions and a DPA [VF: A1-S076, A1-S077], plus Admin and Member roles and SIEM audit logging of scrape events [VF: B-REV-S024]. The privacy policy places servers and data in the US [VF: A1-S134]. Firecrawl announced Alexandria and a US$75M Series B on its blog in September 2026; its changelog dates the round 20 August [VF: A1-S129].
- *Scoring note:* SSO, roles and audit logging plus SCIM score enterprise readiness 4 under CP2 rule 7; built-in roles only keep it below 5. Security stays capped at 2 because the certification claims are vendor-only [AJ].
- *Strengths:* the richest set of per-request controls among the web tools [AJ].
- *Limitations:* the security claims are vendor pages only, and the verifier says not to rely on them [VF: A1-S076]. Self-hosting means owning auth, TLS, persistence and anti-bot services [VF: A1-S079]. AGPL obligations apply to modified network services [VF: A1-S053].
- *Choose when:* you need batch ingestion of approved public sources [AJ].
- *Avoid when:* EU or UK processing is required, or when you plan to modify the server without legal review [AJ].
- *Competitors:* Crawl4AI, Apify.
- *FS note:* public data only, unless the SOC 2 report has been reviewed [Rec].
- **Tier: Tactical. Flag: none.**

**Crawl4AI (open-source project by UncleCode).**
- *What it is now:* Crawl4AI is an open-source crawler that produces Markdown or structured data. It ships as a library, CLI, Docker REST server and MCP server, plus the hosted Crawl4AI Cloud [VF: A1-S074]. The current version is 0.9.4, released 23 September 2026 [VF: A1-S009]. The licence is Apache-2.0 with an appended attribution requirement for distributions and public uses, and legal review is advised [VF: A1-S056, V1-S001]. The self-hosted server requires an API token on every endpoint by default [VF: A1-S074].
- *Strengths:* free, self-hosted, and inside your estate [VF: A1-S074].
- *Limitations:* the project is pre-1.0 and started with a single maintainer [VF: A1-S009, A1-S074]. No venture funding has been disclosed; this comes from an aggregator only [R: A1-S132]. The project publishes a security policy and advisories: eight advisories, five rated high (SSRF, arbitrary file write, secret leakage, XSS), were fixed in 0.9.3 and 0.9.4 in August and September 2026, and only 0.9.x is supported [VF: B-REV-S003]. Pin 0.9.4 or later [Rec].
- *Choose when:* you are prototyping, or crawling a few approved public sources [AJ].
- *Avoid when:* it would be a critical dependency [AJ].
- *Competitors:* Firecrawl, Apify.
- *FS note:* record the attribution clause in the open-source register [Rec].
- **Tier: Experimental. Flag: none.**

**Apify (Apify Technologies s.r.o.).**
- *What it is now:* Apify runs serverless "Actors" with a proxy, datasets and queues, the Apify Store marketplace and an MCP server [VF: A1-S087, A1-S089]. It holds SOC 2 Type II [VF: A1-S085, V1-S089]. It is hosted only in AWS us-east-1, and no EU region is documented [VF: A1-S086, V1-S089]. Third-party Store Actors are outside Apify's control [VF: A1-S086]. Paid plans run from US$19 to US$999 per month, plus compute units [VF: A1-S133].
- *Strengths:* a ready-made Actor for many long-tail sites [AJ]. The MCP server exposes Store Actors directly to AI agents [VF: A1-S089], which makes Apify as much an L4 tool as an L8 pipeline component [AJ].
- *Limitations:* it has a single region, its Actors and storage are platform-specific [VF: A1-S087], and no audit log was found, although organisation roles and per-resource permissions are documented and SSO is stated [VF: B-REV-S025].
- *Choose when:* you need public-data collection that never touches client data [AJ].
- *Avoid when:* any personal or confidential data is involved [AJ].
- *Competitors:* Firecrawl, Crawl4AI.
- *FS note:* treat each Actor as third-party code that needs review [Rec].
- **Tier: Tactical. Flag: none.**

### 8.8 Comparison table

Scores are integers from 1 to 5. Totals are weighted averages from `tools/score.py` (generic and FS weights, plan §8.1).

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8-docling | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4.00 | 4.05 | Strategic |
| L8-unstructured | 4 | 3 | 4 | 5 | 4 | 3 | 3 | 4 | 3.80 | 3.85 | Strategic |
| L8-llamaparse | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.40 | 3.20 | Tactical |
| L8-reducto | 4 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | 3.05 | 2.90 | Tactical |
| L8-mistral-ocr | 3 | 4 | 3 | 4 | 3 | 2 | 4 | 3 | 3.30 | 3.25 | Tactical |
| L8-google-document-ai | 4 | 4 | 4 | 2 | 3 | 3 | 4 | 2 | 3.40 | 3.25 | Strategic |
| L8-firecrawl | 4 | 4 | 2 | 3 | 4 | 3 | 3 | 2 | 3.25 | 3.00 | Tactical |
| L8-crawl4ai | 3 | 2 | 2 | 4 | 3 | 2 | 4 | 4 | 2.90 | 2.90 | Experimental |
| L8-mineru | 4 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2.80 | 2.70 | Experimental |
| L8-apify | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 2 | 2.65 | 2.55 | Tactical |

**Evidence caps applied [AJ]:**
- **Enterprise readiness (CP2 rules 6 and 7):** no hosted product is now capped at 2. The CP2 review lifted the caps on Unstructured, Reducto, Mistral OCR, Google Document AI and Apify after finding SSO and role documentation [VF: B-REV-S016, B-REV-S017, B-REV-S014, B-REV-S010, B-REV-S025]. The CP2 rework then applied the user's CP2 answers:
  - LlamaParse rises from 2 to 3: verified SSO lifts the cap (rule 7), and flat hosted roles with no documented audit log hold it at 3 [VF: B-REV-S023].
  - Mistral OCR and Firecrawl rise from 3 to 4: each has SSO, roles and audit logs plus SCIM (rule 7) [VF: B-REV-S014, B-REV-S015, B-REV-S024]. The conditions are Mistral's non-exportable audit logs and Firecrawl's built-in roles.
  - Google Document AI rises from 3 to 4 under the hyperscaler presumption (rule 6); platform controls presumed (CP2 Q1); confirm per service.
  - Unstructured, Reducto and Apify stay at 3, because each has one or two of the three controls and no documented audit log. Crawl4AI and MinerU stay at 2 under the library rule, with no SSO, RBAC or audit control verified.
- **Security capped at 2:** Firecrawl and Reducto, because their security claims are vendor-only and flagged in V1 §4. Rule 8 (certification scope): Mistral OCR's company-level certifications score 3. Document AI's product-scoped certifications with CMEK scored 5 until the CP3 rework, which lowered it to 4 because the SOC 2 report type is not stated [VF: A1-S102], consistent with the other Google services in C1–C3.
- **Library rule** (scored on project hygiene; inherits host controls): Docling (security 4, on a verified security policy and signed releases [VF: B-REV-S001]), Crawl4AI (2, on its advisory history [VF: B-REV-S003]) and MinerU.

**Key facts** (as of 7–8 October 2026)

| Product | Licence | Deployment | Certifications | EU residency | Ownership status |
|---|---|---|---|---|---|
| Docling | MIT; models own licences [VF: A1-S057] | Library, REST, MCP, IBM-managed [VF: A1-S082, A1-S110] | n/a (library) | In-estate [AJ] | LF AI & Data Graduate, Aug 2026 [VF: V1-S091] |
| Unstructured | Apache-2.0 OSS; proprietary API [VF: A1-S011, A1-S075] | OSS, SaaS, dedicated, in-VPC [VF: A1-S117] | SOC 2 Type 2, ISO 27001, HIPAA, CMMC 2.0 L2 (vendor-listed) [VF: A1-S117, V1-S090] | Hosted region NPV; in-estate via OSS | Independent [NPV] |
| LlamaParse | Proprietary; SDK MIT [VF: A1-S014] | SaaS NA/EU, BYOC, self-host, on-prem [VF: A1-S115] | SOC 2 Type II; HIPAA BAA [VF: A1-S115] | EU region [VF: A1-S115] | LlamaIndex, Inc.; renamed from LlamaCloud [VF: A1-S080] |
| Reducto | Proprietary; SDK Apache-2.0 [VF: A1-S090] | SaaS, VPC, on-prem, air-gap (vendor) [VF: A1-S112] | SOC 2 Type I/II, HIPAA (vendor-only) [VF: A1-S112] | EU endpoint [VF: A1-S092] | Private; US$108M raised [VF: A1-S114] |
| Mistral OCR | Proprietary model [VF: A1-S135] | EU API; self-managed (enterprise) [VF: A1-S135] | Company-level SOC 2 II, ISO 27001, 27701 [VF: A1-S136] | EU-hosted API [VF: A1-S135] | Mistral AI [VF: A1-S083] |
| Google Document AI | Proprietary [VF: A1-S101] | Managed SaaS [VF: A1-S101] | ISO 27001/17/18, SOC 1/2/3, PCI DSS [VF: A1-S102]; CMEK [VF: B-REV-S011] | us/eu multi-regions [VF: B-REV-S010] | Google Cloud [VF: A1-S101] |
| Firecrawl | AGPL-3.0 server; MIT SDKs [VF: A1-S053, V1-S002] | Cloud; reduced self-host [VF: A1-S079] | SOC 2 Type II (vendor-only) [VF: A1-S076] | US per privacy policy [VF: A1-S134] | Venture-backed, Series B 2026 [VF: A1-S129] |
| Crawl4AI | Apache-2.0 + attribution clause [VF: A1-S056] | Library, Docker, hosted cloud [VF: A1-S074] | NPV | In-estate [AJ] | Open-source project; unfunded per aggregator [R: A1-S132] |
| MinerU | Custom: Apache-2.0 + thresholds [VF: A1-S054] | Local, self-host, remote service [VF: A1-S055] | NPV | In-estate by default [VF: A1-S055] | OpenDataLab MinerU Team [VF: A1-S054] |
| Apify | Proprietary; client Apache-2.0 [VF: A1-S016] | SaaS only [VF: A1-S087] | SOC 2 Type II [VF: A1-S085] | None; AWS us-east-1 only [VF: A1-S086] | Apify Technologies s.r.o. [VF: A1-S016] |

### 8.9 Decision tree

![L8 decision tree: ingesting public web and enterprise documents](Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/L8-2.png){width=100%}

*Figure: Nothing is ingested from an unregistered source; public-web ingestion turns on permission, licence and processing location, while enterprise documents are routed by permissions, where content may be processed, scans and quotable tables. Editable source: `08_Graphic/diagrams/L8-2.md`.* [AJ]

### 8.10 Lock-in classification

| Class | Where it applies | Rationale | Abstraction to use |
|---|---|---|---|
| **Acceptable** | Docling; the Unstructured open-source library and connectors; OCR engines (Mistral OCR, Document AI OCR) used purely as OCR | Docling is MIT under neutral governance [VF: A1-S057], and Unstructured's library is Apache-2.0 [VF: A1-S011]. An OCR engine's text-plus-coordinates output is easy to swap once a golden set exists [AJ]. | A canonical document model (DoclingDocument or an in-house JSON schema) and an engine adapter interface [Rec] |
| **Manageable** | LlamaParse Parse/Extract; Reducto; Firecrawl Cloud; Unstructured Transform API | All four have proprietary APIs or credit models [VF: A1-S116, A1-S093, A1-S079]. Outputs can be converted into your model, so switching costs a re-parse plus a regression run [AJ]. | The same adapter; store your own copy of every parsed output; keep the parse manifest [Rec] |
| **Unacceptable** | A vendor-managed index (for example LlamaParse Index) as the system of record for entitled content; Apify Actors in core pipelines; MinerU above its thresholds without a commercial licence; a modified Firecrawl server exposed without AGPL compliance | These create regulatory or legal exposure. An index outside your L6 store weakens entitlement and erasure control. Third-party Actors are outside Apify's control [VF: A1-S086]. MinerU rights terminate on breach [VF: A1-S054]. | Keep indexing in your own L6 store; keep licences in the OSS register; scrape only via reviewed code [Rec] |

### 8.11 Regulated FS lens (POV 2)

**Ingestion is where data decisions are made.** Residency, PII classification and entitlements are decided when a document is acquired and parsed; once a document has gone to a third-party parser and been indexed without its ACL, no prompt-level control can undo that [AJ].

**Model risk (SS1/23, SR 26-2).**

- SS1/23 applies to vendor models and is technology-agnostic [VF: R-PRA-SS123; A8-S008]. Its Principle 1.1(b) lets firms apply relevant MRM aspects to material, complex deterministic quantitative methods that are not models [VF: R-PRA-SS123; A8-S061].
- SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly excludes generative and agentic AI. For out-of-scope tools, the firm's own governance applies [VF: R-US-MRM; A8-S001, A8-S002].
- Parsers are not themselves "models" in either definition [AJ]. They are, however, data-preparation components whose errors flow straight into an LLM's inputs. The inventory should record parser and OCR engine versions as dependencies of each AI use case [Rec].

**EU AI Act.**

- Annex III high-risk duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EUAIA; A8-S011, A8-S012]. The commentary agent is not an Annex III use case [AJ]. Where a high-risk deployment does arise, Article 26 requires relevant and representative input data where the deployer controls it, and logs kept for at least six months [VF: R-EUAIA; A8-S016, A8-S017, A8-S018].
- Separately, ESMA expects ex-ante input controls and due diligence on third-party AI [VF: R-INTL-AI-ASSETMGMT; A8-S059]. L8 validation and the approved-source register are those controls [AJ].

**Third parties (DORA, PS7/26, SYSC 8).**

- **DORA.** DORA requires a register of information covering all ICT third-party arrangements, and Article 30 contract terms [VF: R-DORA; A8-S021]. For an EU entity, every SaaS parser or crawler is such an arrangement [AJ].
- **Concentration.** The first CTPP list (19 providers) includes hyperscalers such as Google Cloud EMEA Limited, and no AI model provider [VF: R-DORA; A8-S020, A8-S022]. Specialist L8 vendors are therefore overseen only through the firm's own third-party risk management [AJ].
- **UK.** PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8; A8-S062]. A hosted parser that processes client documents for an important business service could be such an arrangement [AJ].
- **FCA FG16/5.** The guidance covers data location, effective access, concentration and exit [VF: R-FCA-SYSC8; A8-S049]. Exit is cheap only if the firm holds its own parsed outputs in an open model [AJ].
- **Due-diligence gap.** Whether vendor SOC 2 reports cover BYOC or self-hosted installs (LlamaParse, Reducto) is not stated [NPV].

**Residency and transfers.**

- Firecrawl's privacy policy places data in the US [VF: A1-S134], and Apify is hosted only in us-east-1 [VF: A1-S086]. For EU or UK personal data, the transfer basis would rest on the EU–US Data Privacy Framework or SCCs, and the DPF appeal C-703/25 P is pending [VF: R-DATA-TRANSFERS; A8-S053, V2-S059].
- EU-resident options exist: the Mistral OCR API, LlamaParse's EU region and Reducto's EU endpoint [VF: A1-S135, A1-S115, A1-S092]. Fully in-estate options also exist: Docling, MinerU and the Unstructured open-source library [VF: A1-S057, A1-S055, A1-S075].

**Auditability and reproducibility.**

- An audit pack has to show which parser version produced each chunk the agent saw [AJ].
- Hosted model retirement removes the ability to re-run a parse. Mistral retired OCR 4.0 on 30 September 2026 [VF: A1-S130].
- Retain parsed outputs, manifests and lineage events for the same period as the commentary record [Rec].

**Standards.**

- **NIST AI 600-1** (final, 26 July 2024) sets out GenAI-specific risks and suggested actions [VF: R-NIST-AIRMF; A8-S044]. Mapping those actions onto ingestion provenance controls is the firm's task [AJ].
- **ISO/IEC 42001** sets requirements for an AI management system [VF: R-ISO-42001; A8-S045]. The ingestion controls above sit inside it [AJ].
- **OWASP.** The operative list is the Top 10 for LLM Applications 2026, which supersedes the 2025 list [VF: R-OWASP-LLM; A8-S041]. Its full contents were not retrieved, so 2026 identifiers are not given here [NPV]. For traceability, the 2025 entries LLM04 Data and Model Poisoning and LLM08 Vector and Embedding Weaknesses are the ones exposed at ingestion [R: R-OWASP-LLM; A8-S040] [AJ]. The Top 10 for Agentic Applications for 2026 lists ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC; A8-S042]; indirect injection through documents an agent reads is one route to it [AJ].
- **IOSCO.** IOSCO flags concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT; A8-S058].

### 8.12 Worked-example slice (POV 3)

The performance-attribution commentary agent drafts monthly Brinson-style commentary (allocation, selection, currency) for a generic multi-asset fund. A portfolio manager approves every draft. L8 supplies three corpora [AJ]:

| Corpus | Source class | L8 treatment [Rec] |
|---|---|---|
| Fund factsheets (prior months) | Internal, approved; contains tables | Self-hosted Docling. Dual-parse every performance table and reconcile it against the stored attribution output for that period; quarantine on any mismatch. Tag every numeric cell as `document_derived=true`. |
| Prior commentaries and house style guide | Internal, entitlement-restricted per fund and client | Connector with ACL capture (Unstructured ingest pattern). Chunks carry fund ID, client restrictions and approval status. Draft commentaries are excluded; only approved versions are indexed. |
| Market notes | Third-party research and public sources on the register only | Licence and redistribution terms recorded on the register entry. Web content is acquired in batch by a self-hosted crawler and injection-scanned. No live web fetching by the agent. |

**What the agent needs from L8** [AJ]:
- Retrievable prior commentary with citations back to a specific document version.
- House-style passages that are current, not superseded.
- Market context only from approved sources.
- Enough metadata for the evidence pack (C8) to record which chunks, from which document versions, parsed by which engine versions, were in context.

**What L8 must never do** [Rec]:
- **Supply a number as authoritative.** Every figure in the commentary comes from the attribution engine through read-only L4 tools. Numbers parsed from documents are context only, and the L9 numeric-faithfulness eval checks the draft against the engine output, not against parsed text. A parsing error must never be able to become a published figure.
- **Ingest from a source that is not on the register.** This includes an analyst's ad-hoc upload of a broker note whose licence has not been checked.
- **Index a document without its ACL, or index it as "public" when the permission fetch failed.**
- **Send client-identifying content to a parser outside the approved residency.**
- **Lose the parse manifest.** Without it, last month's draft cannot be reproduced.

### 8.13 Baseline position and hypothesis view

| Baseline entry | Position at end of Q3 2026 | Recommended |
|---|---|---|
| **The layer as a whole** | Two distinct jobs, web acquisition and document understanding, plus agent-facing web tools that overlap L4 [VF: A1-S077, A1-S089] | Keep one L8 layer with two sub-layers (acquisition; document understanding) under a shared ingestion control plane; move runtime web access to L4 [Rec] |
| Firecrawl | AGPL server, Cloud-only enterprise controls, US data [VF: A1-S053, A1-S079, A1-S134] | Tactical for public sources [Rec] |
| Docling | MIT, LF AI & Data Graduate (August 2026), 2.135.0 [VF: V1-S091, A1-S008] | Strategic default engine and canonical model [Rec] |
| LlamaParse | Renamed: the whole LlamaIndex platform (formerly LlamaCloud) [VF: A1-S080] | Tactical; Parse/Extract only, indexing kept in-house [Rec] |
| Crawl4AI | Pre-1.0; Apache-2.0 plus attribution clause [VF: A1-S009, A1-S056] | Experimental; self-hosted pilots [Rec] |
| MinerU | 4.0, multi-format, custom licence [VF: A1-S055, A1-S054] | Experimental pending licence review [Rec] |
| Reducto | Proprietary API, vendor-only security evidence [VF: A1-S112] | Tactical after due diligence [Rec] |
| Mistral OCR | OCR 4.1 (GA 26 August 2026); 4.0 retired 30 September 2026 [VF: A1-S130, V1-S014] | Tactical OCR engine; pin model ID [Rec] |
| Unstructured | Free OSS plus Transform v2 API; ACL-digest connectors [VF: A1-S075, A1-S094] | Strategic for connectors and entitlement capture [Rec] |
| Apify | Actor platform, MCP, US-only [VF: A1-S089, A1-S086] | Tactical; public data only [Rec] |
| Hyperscaler document AI | Google Document AI assessed; Azure and AWS equivalents not verified [VF: A1-S101] [NPV] | Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2) [Rec] |
| Lineage, classification, PII, entitlements, incremental indexing | Partial in products: Unstructured ACL digest [VF: A1-S094]; Firecrawl PII redaction and ZDR [VF: A1-S076]; no lineage in any L8 product; OpenLineage has no GenAI facets [VF: A7-S042] | A built ingestion control plane (below) [Rec] |

**Hypothesis H7 (provisional; verdict in synthesis).** The evidence supports H7, with one refinement: the enterprise additions are not product features to buy but a control plane to build around replaceable parsers [AJ]. Only partial capabilities exist in products:

- Unstructured captures ACLs and reprocesses on permission change [VF: A1-S094].
- Firecrawl offers PII redaction and ZDR on web content [VF: A1-S076].
- Pinecone, in L6, advertises PII-aware ingestion and lineage in Nexus [VF: A2-S073, A2-S074].
- No L8 product emits lineage [VF: A1-S094, A1-S096].
- OpenLineage has no GenAI-specific facets [VF: A7-S042], so parse, chunk, embed and index steps need custom facets [AJ].

The provisional architecture has six components [Rec]:
1. **Approved-source register.** The single entry point. It records owner, licence or ToS, legal basis, default classification and residency.
2. **Acquisition contract.** Every connector, bought or built, must emit a content hash, source version and ACL snapshot or digest. It must have a distinct "permission unavailable" state that fails closed.
3. **Pre-parse classification and DLP** using a C3 engine (Presidio or a cloud DLP service). This step decides which parsers a document may be routed to.
4. **Parse manifest.** Engine, version, model ID and config hash, stored with the canonical document model output.
5. **Metadata envelope on every chunk**, enforced as an index gate: source, version, ACL principals, classification, PII flags, manifest, and lineage run ID.
6. **Lineage and incremental indexing.** OpenLineage events with custom facets, emitted from the orchestrator (for example the Airflow OpenLineage provider). The index diffs on content hash and ACL digest, and tombstones propagate deletions to L6 and caches.

The open question for synthesis is whether this control plane is an L8 sub-layer or part of C3/C8. The provisional view is that it lives in L8, with policies supplied by C3 and evidence consumed by C8 [AJ].
