## 6. Retrieval and knowledge stores (vector databases)

> **Executive summary.** This layer stores the vectors, text and metadata that an agent searches, and returns a small, permitted, relevant set of passages. It must do so fast, under filters, for many tenants, and with the same security and records discipline as any other store of client data [AJ]. Four things have changed since the original graphic. First, hybrid retrieval is now standard. turbopuffer ranks by vectors and BM25 [VF: A2-S056], Chroma Cloud offers vector, hybrid and full-text search [VF: A2-S060], Milvus ships BM25 [VF: A2-S054, A2-S117], and Elasticsearch, MongoDB, Qdrant and Pinecone all fuse sparse and dense results [VF: A2-S133, A2-S141, A2-S103, A2-S101]. Second, general-purpose databases have absorbed vector search: pgvector reached 0.8.7 on 1 October 2026 [VF: V1-S020, V1-S022], and MongoDB Vector Search is GA on self-managed Community and Enterprise Advanced as well as Atlas [VF: A2-S137, V1-S035]. Third, vectors are moving onto object storage: Amazon S3 Vectors has been GA since December 2025 [VF: A2-S081, V1-S030], Milvus 3.0 is "lake-native" [VF: A2-S118], and turbopuffer keeps all durable state in object storage [VF: A2-S124]. Fourth, vendors are repositioning above the store: Pinecone now sells Nexus, a "knowledge engine for agents" (GA 6 August 2026) [VF: A2-S073, V1-S029]. The term "vector database" now describes a feature more than a product category [AJ]. **Recommendation:** treat this layer as a retrieval and knowledge store that is always a *derived index*, never the system of record. Start with vectors inside the database or search engine you already run (PostgreSQL with pgvector, Elasticsearch or MongoDB). Move to a dedicated engine (Qdrant or Milvus, self-hosted or in your own cloud account) only when scale, filtered latency or tenant isolation demand it. Enforce entitlements as filters applied before ranking, in every case [Rec].

### 6.1 Responsibility

**The problem this layer owns.** It persists retrievable representations of approved content and answers the question "which of the passages this caller is allowed to see are most relevant to this query?" [AJ]. Six jobs make up the responsibility:

- **Indexing.** Store dense vectors, sparse or lexical terms, the raw chunk text (or a pointer to it) and metadata, and keep the index current as documents are added, changed and deleted [AJ].
- **Candidate retrieval.** Run approximate-nearest-neighbour (ANN) search and lexical search, and fuse the two [AJ]. pgvector provides HNSW and IVFFlat indexes over dense and sparse vectors [VF: A2-S063, A2-S061]. Elasticsearch combines BM25, quantised vectors and RRF or linear fusion [VF: A2-S133, A2-S042].
- **Filtering and entitlements.** Apply structured filters (fund, client, document class, date, approval status) so that ranking only ever sees permitted candidates [AJ].
- **Tenant isolation.** Keep one client's or fund's material physically or logically separate from another's [AJ].
- **Lifecycle.** Retention, deletion (including erasure requests), backup, restore and re-indexing after an embedding-model change [AJ].
- **Evidence.** Return stable document and chunk identifiers, versions and scores, so the evaluation layer (L9) and the evidence pack (C8) can show exactly what the model was given [AJ].

**Hand-offs.**

| Direction | Counterpart | What crosses the boundary [AJ] |
|---|---|---|
| Below | L8 ingestion | Parsed, chunked, classified documents with lineage, ACL metadata and PII flags (the H7 contract) |
| Beside | L7 embeddings and reranking | Vectors and sparse terms written with a model-version tag; at query time, first-stage candidates passed to the reranker |
| Above | L3 orchestration, L4 tools, L5 memory | A retrieval call carrying the caller's verified entitlements; results with IDs, scores and provenance |
| Across | C3 data governance, C4 identity, C8 audit | Classification and residency policy; caller identity and entitlements; retrieval logs |
| Across | L9 evaluation | Retrieval recall and precision, filtered-latency and leak tests |

**What the layer does not own.** It does not decide which content is approved for retrieval; that is L8 and C3 [AJ]. It does not own embedding-model choice or version policy, which belong to L7, even when the store runs the embedding model itself, as MongoDB Automated Embedding, Elastic `semantic_text` and Pinecone integrated inference do [VF: A2-S078, A2-S133, A2-S051] [AJ]. It does not own agent memory semantics (L5), although the same engines often host memory [AJ].

### 6.2 Why it matters

A badly designed retrieval store fails quietly [AJ]. The model receives plausible context and writes fluent text, so the failure surfaces as a wrong fact, a stale citation or, worst, another client's information in a draft [AJ]. Four failure modes dominate:

- **Entitlement leakage.** Permissions applied after ranking, or only in the application, let restricted passages reach the prompt. The model then repeats them [AJ].
- **Filter collapse.** A restrictive filter applied after ANN search leaves too few results, so recall drops or the system silently widens the filter [AJ].
- **Index drift.** Deletions, retractions and superseded versions do not propagate, so the agent cites withdrawn material, and an erasure request is honoured in the source but not in the vector copy [AJ].
- **Unplanned dependency.** A store chosen for a prototype becomes a critical system with no exit plan, no backup and no tested rebuild [AJ].

The layer also holds a copy of the firm's most sensitive unstructured content in a second representation [AJ]. Embeddings are derived from that content. They should be treated as data of the same classification as the text they came from, including for residency and erasure [AJ].

**Illustrative scenario [AJ].** A multi-asset team builds a commentary assistant on a single shared vector index holding prior commentaries for all its funds. Fund identity is a metadata field. The application retrieves the top 20 passages and then removes any that belong to other funds. For most funds this works. For a small segregated mandate, a query about currency hedging returns 20 passages from larger funds; after the post-filter, none remain, so a fallback path retries without the fund filter "to avoid an empty context". The draft for the segregated mandate's client report now quotes a hedging rationale written for a different client, including that client's benchmark name. A reviewer catches it, but only because the benchmark name is unfamiliar. The incident review finds three faults: the filter ran after ranking, the fallback removed it, and no test checked for cross-fund leakage. Filtering inside the search, a hard "no results" outcome instead of a fallback, and a leakage test in the L9 suite would each have prevented it. The scenario is invented; it is not a reported incident.

### 6.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Entitlement leakage | Results returned that the caller is not entitled to see | Zero; any occurrence is a severity-1 incident | Adversarial test queries per tenant in CI (L9); production sampling against the entitlement service |
| Filtered recall@k | Recall@k measured with production-like filters applied, not on the unfiltered index | Within an agreed tolerance of unfiltered recall for the same queries | Labelled query set run with and without filters |
| p95 latency under filter | Retrieval latency at the 95th percentile for the most selective realistic filter | Budget per use case (interactive versus batch) | Load test with tenant-skewed data |
| Hybrid uplift | Change in recall or groundedness from adding lexical retrieval and fusion | Positive on the firm's own corpus before adoption | A/B evaluation in L9 |
| Freshness lag | Time from approval in the source to searchability | Hours for commentary corpora; minutes where markets data drives content | Canary documents written and queried |
| Deletion propagation time | Time from deletion or retraction in the source to absence from results and from the index | Within the records-policy and erasure service levels | Canary deletions; index scan |
| Rebuild time (RTO) | Time to rebuild the index from the source of truth with the pinned embedding model | Inside the exit-plan tolerance; tested twice a year | Timed dry run |
| Residency conformance | Share of vector, text and backup copies held in approved regions | 100% | Configuration evidence and cloud inventory |
| Patch latency | Time from a store CVE to production fix | Days for high severity (pgvector's 0.8.7 fix was CVSS 8.8 [VF: V1-S022]) | Vulnerability management records |
| Cost per 1,000 queries and per GB-month | Loaded cost including idle capacity | Budget per use case | Billing and capacity data |

### 6.4 How it works

**Write path.** L8 delivers chunks with metadata. L7 produces dense vectors and, where used, sparse vectors or lexical terms. The store writes vectors, text or text pointers, and metadata to an index, often partitioned by tenant [AJ]. Engines differ in where durable state lives. pgvector stores vectors in PostgreSQL tables beside relational data [VF: A2-S061]. turbopuffer writes to a write-ahead log in object storage and serves from SSD and memory caches [VF: A2-S124]. S3 Vectors stores vectors in vector indexes inside vector buckets [VF: A2-S094, A2-S083]. Milvus 3.0 builds indexes over vectors kept in object storage and open formats [VF: A2-S118].

**Query path.** A query carries the caller's entitlements from C4. The store applies the filter, runs ANN and lexical search over the permitted candidates, fuses them, and returns a few dozen candidates to the L7 reranker [AJ]. Fusion is now a store feature: Qdrant weighted RRF [VF: A2-S103], Elasticsearch RRF and linear retrievers [VF: A2-S133], MongoDB `$rankFusion` and `$scoreFusion` [VF: A2-S141] and Pinecone cascading retrieval with a sparse model [VF: A2-S101].

**Filtering mechanics.** There are three broad approaches [AJ]:

- *Post-filtering* runs ANN first and discards disallowed results. It is cheap, and it is the cause of filter collapse and of leakage when combined with fallbacks [AJ].
- *Pre-filtering or filter-aware traversal* restricts the search to permitted candidates as it runs. Qdrant added ACORN-based filtered search in 1.16 [VF: A2-S103]. pgvector 0.8.0 added iterative index scans and better cost estimation for index selection when filtering [VF: V1-S020]. Elastic reports DiskBBQ at least three times faster with restrictive filters in 9.4 [R: A2-S133].
- *Partitioning* gives each tenant its own namespace, collection or index, so the filter becomes an address. Pinecone and turbopuffer route every query to a namespace [VF: A2-S051, A2-S056], turbopuffer isolates namespaces as prefixes in object storage [VF: A2-S124], Qdrant has tiered multitenancy with tenant promotion [VF: A2-S103], and Chroma scopes access control to the tenant, with databases beneath it [VF: B-L6-S008].

```text
WRITE (L8 -> L7 -> L6)
  approved doc --> chunk + metadata {doc_id, version, fund_id, client_id,
                   classification, region, retention_until, embed_model_version}
            --> dense vector (+ sparse terms)
            --> STORE: partition = tenant (namespace / collection / schema)
                       index    = ANN (HNSW / IVF / centroid / DiskANN-type) + BM25
                       payload  = text or pointer to source of truth (L8)

QUERY (L3 -> C4 -> L6 -> L7 -> L3)
  caller identity --> C4 entitlements {fund_ids, client_ids, max_classification}
            --> L6: select partition(s) the caller may use
                    filter INSIDE the search (never after ranking)
                    ANN + BM25 --> fusion (RRF / linear) --> top-N candidates + IDs
            --> L7 reranker --> top-k passages + provenance
            --> L3 prompt assembly;  retrieval log (IDs, versions, scores) --> C8 / L9

LIFECYCLE
  source delete / retraction / erasure --> delete by ID --> compaction / vacuum
  embedding model change --> shadow index --> evaluate (L9) --> cut over --> drop old
  backup = rebuild-from-source (primary) + store snapshot (secondary)
```

**Storage economics.** Memory-resident graph indexes give low latency at a high RAM cost [AJ]. Quantisation and disk-based indexes trade some recall for cost: Elastic's BBQ has been the default since 9.1 [VF: A2-S133], Qdrant added TurboQuant quantisation and a low-memory mode in 1.18 [VF: A2-S102], and Weaviate previews 4-bit rotational quantisation [VF: A2-S110]. Object-storage-first designs push the trade further. turbopuffer reports a cold-query p50 of 874 ms against 14 ms cached on 1M documents [R: A2-S124]. S3 Vectors has no provisioned compute and is priced per GB stored, per PUT and per query [VF: A2-S087]. Vendor latency figures are context, not decision inputs [AJ].

### 6.5 Enterprise design principles

**Security and entitlements**

- **Filter before rank, inside the store.** Entitlements arrive from C4 as signed claims and become mandatory filter clauses. The application must not be able to omit them, and there is no "retry without filter" path [Rec].
- **Do not rely on the store for row-level permissions you have not tested.** turbopuffer states that permissions must be implemented with filters because it has no built-in row- or document-level RBAC [VF: B-L6-S002]. Most engines are in the same position: they provide the filter mechanism, and the firm provides the policy [AJ].
- **Use engine-native document security where it exists.** Elasticsearch offers field- and document-level security (Platinum tier when self-managed) [VF: A2-S134]. Qdrant issues JWT keys scoped to read or read-write on individual collections [VF: B-L6-S007]. Weaviate supports RBAC with custom roles and OIDC users and groups [VF: B-L6-S009].
- **Lock down self-hosted defaults.** Chroma removed its built-in authentication in 1.0 [VF: A2-S131]. Milvus Lite has no authentication, users, roles or TLS [VF: A2-S054]. Qdrant 1.19.2 now warns at start-up when no API keys are configured [VF: A2-S102]. None of these should run on a shared network without an authenticating proxy [Rec].
- **Patch the store like a database.** pgvector 0.8.7 fixed an IVFFlat index-build buffer overflow rated CVSS 8.8 that could allow code execution by a user able to create such indexes [VF: V1-S022, A2-S061]. 0.8.2 fixed a parallel HNSW build overflow (CVE-2026-3172) [VF: A2-S062, V1-S020]. Managed hosts lag upstream: the latest Amazon RDS release seen carries pgvector 0.8.2 [VF: B-L6-S004], while Cloud SQL moved to 0.8.5 in August 2026 [VF: B-L6-S005]. Restrict index-creation privileges and track the host's pgvector version, not only the upstream one [Rec].
- **Encrypt with keys you control where the data is client-confidential.** Customer-managed keys are documented for Pinecone (project level) [VF: A2-S096], turbopuffer (per namespace, Enterprise) [VF: A2-S123, V1-S077], Zilliz Cloud (Business Critical) [VF: A2-S120], Elastic Cloud Hosted (Enterprise) [VF: A2-S134], MongoDB Atlas [VF: A2-S139], Chroma Cloud [VF: B-L6-S008] and S3 Vectors (per bucket or index) [VF: A2-S090]. Atlas covers search indexes with CMK only on dedicated Search Nodes [VF: A2-S139], and S3 Vectors keys cannot be changed after index creation [VF: A2-S090].

**Scalability and performance**

- Measure recall and latency *with filters and tenant skew*, on your own corpus. Unfiltered benchmarks overstate both [AJ].
- Prefer partitioning by tenant when tenants are numerous and roughly independent; prefer a shared index with a mandatory filter when cross-tenant search by authorised staff is a real requirement [AJ].
- Keep the raw text and the embedding-model version beside every vector, so the index can be rebuilt without re-parsing (the L7 rule) [Rec].

**Resilience, backup and exit**

- **The source of truth is outside the store.** The primary recovery path is a rebuild from L8's approved corpus with the pinned embedding model. Store snapshots are the secondary path [Rec].
- **Test the rebuild.** Rebuild time is an exit-plan metric, because SS2/21 expects documented and tested exit plans [VF: R-PRA-SS221, A8-S048] [AJ].
- **Watch upgrade paths.** Qdrant cannot skip 1.16 on upgrade because of a storage migration [VF: A2-S102]. Milvus 3.0 is not guaranteed compatible with 2.6 servers [VF: A2-S117]. Pinecone's Python SDK v10 introduced breaking API changes [VF: A2-S051, A2-S072]. Weaviate supports only its latest three minor versions [VF: A2-S109].

**Governance and lifecycle**

- Deletion must propagate within a defined service level, and must be verified by canary [Rec]. Engines differ in how deletes become physical: pgvector's 2026 fixes include HNSW vacuuming corrections [VF: V1-S020], which is a reminder that deletion depends on background maintenance [AJ].
- Retention metadata (`retention_until`) should travel with each chunk, and a scheduled job should delete expired chunks [Rec].
- Record which documents, versions and chunks each answer used, in the evidence pack (C8) [Rec].

**Observability and cost**

- Emit retrieval spans (query, filter, partition, candidate IDs, scores, latency) to the L9 collector, with text redacted where necessary [Rec].
- Pricing units differ widely: read and write units (Pinecone) [VF: A2-S099], data scanned and returned (turbopuffer) [VF: A2-S123], GiB written, stored and queried (Chroma) [VF: A2-S128], per-query data processed (S3 Vectors) [VF: A2-S087], hourly Search Nodes (MongoDB) [VF: A2-S140] and plain database compute (pgvector) [AJ]. Model the firm's query mix before committing [Rec].

**Patterns [AJ]:** vectors in the existing operational database for modest corpora; a search engine for lexical-heavy corpora; tenant-partitioned dedicated engine for many clients; object-store cold tier behind a hot tier; rebuild-from-source as the backup; retrieval logs into the evidence pack.

**Anti-patterns [AJ]:** post-filter permissions; an unfiltered fallback; the vector store as the only copy of approved content; a prototype store (embedded, unauthenticated) promoted to production; one shared index for segregated mandates without leak tests; embedding inside the store with an unpinned model; a "knowledge engine" adopted as the system of record without an export route.

### 6.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Dense and sparse vectors; BM25 and fusion; filter-aware search and recall under selective filters; multi-tenancy model; scale (vectors per index, tenants); deletes and updates; quantisation and disk indexes; transactional integration with operational data |
| Enterprise readiness (15%) | SSO, RBAC with scoped keys, audit logs of data access, SCIM, SLA; whether controls cover the data plane as well as the console |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 within the product's scope; CMK/BYOK granularity (project, index, namespace); private networking; HIPAA as a proxy for mature controls; CVE handling for self-hosted engines |
| Deployment flexibility (15%) | SaaS, BYOC (data plane in the firm's account), self-host, on-premises and air-gap; UK and EU regions |
| Ecosystem (5%) | Open query interfaces (SQL, OpenAPI, standard drivers); framework support; hyperscaler integration |
| Reliability and maturity (10%) | Years in production; release cadence; breaking upgrades; governance (foundation versus single vendor) |
| Cost / TCO (5%) | Pricing unit and minimums; idle cost; operations burden; RAM versus disk versus object storage economics |
| Lock-in / portability (15%) | Licence (permissive, AGPL, SSPL, open core, proprietary); proprietary query language; bundled embedding; export and rebuild path |

**Two calibration rules applied in this layer [AJ].** First, *no ISO 27001 means a security score of at most 3*, whatever else is present; this applies to Qdrant, turbopuffer and Chroma. Second, *store-only engines are scored on the store*, so a vendor's adjacent products (Nexus, Voyage models, Jina models) affect lock-in but do not raise the technical score.

### 6.7 Product deep dives

**PostgreSQL with pgvector (open-source project).**
- *What it is now:* an extension that adds vector types, including `sparsevec`, and HNSW and IVFFlat ANN indexes to PostgreSQL, so vectors live beside relational data and SQL filters [VF: A2-S063, A2-S061]. Version 0.8.7 was released on 1 October 2026 and announced on 5 October [VF: V1-S020, V1-S022]. The extension is under the PostgreSQL License, which is permissive and OSI-approved [VF: V1-S021].
- *Security record:* two 2026 fixes matter. 0.8.2 (February) fixed a parallel HNSW build buffer overflow, CVE-2026-3172 [VF: A2-S062, V1-S020]. 0.8.7 fixed an IVFFlat index-build buffer overflow (CVE-2026-103484, CVSS 8.8) that can allow arbitrary code execution by a user able to create IVFFlat indexes [VF: V1-S022, A2-S061]. Stage A noted that the CVE number format looks unusual [VF: A2-S061]; cite the PostgreSQL.org announcement rather than the number alone [Rec].
- *Managed hosting:* Amazon RDS and Aurora PostgreSQL support pgvector, and Aurora can serve as a Bedrock Knowledge Base [VF: B-L6-S004]. Azure Database for PostgreSQL requires the extension to be allowlisted, adds a DiskANN index, and cannot index vectors over 2,000 dimensions; Azure manages the extension version [VF: B-L6-S005]. Cloud SQL moved to pgvector 0.8.5 on 27 August 2026, and AlloyDB adds a ScaNN index to a customised pgvector [VF: B-L6-S005].
- *Filtering:* 0.8.0 added iterative index scans and improved index selection when filtering [VF: V1-S020].
- *Strengths:* transactional integration (vectors, metadata and entitlement tables in one ACID database) and the lowest operational increment for any firm that already runs PostgreSQL well [AJ].
- *Limitations:* HNSW indexes are memory-hungry, so cost tracks database RAM [AJ]. There is no BM25 ranking in the extension itself; hybrid needs `sparsevec` or application-side fusion [VF: A2-S063] [AJ]. Large-scale behaviour under heavy write and filter load is not evidenced in the fact base [NPV]. Adjacent forks add scale features: pgvectorscale (Tiger Data, formerly Timescale) and VectorChord, which succeeded the deprecated pgvecto.rs [VF: A2-S064, A2-S066, A2-S065, A2-S067].
- *Choose when:* the corpus is in the millions of chunks rather than billions, PostgreSQL is a standard platform, and entitlements already live in relational tables [AJ].
- *Avoid when:* you need thousands of isolated tenants with independent scaling, or low-latency search over a very large corpus under selective filters [AJ].
- *Competitors:* MongoDB Vector Search, Elasticsearch, Qdrant.
- *FS note:* run on the firm's managed PostgreSQL in a UK or EU region; track the host's pgvector version against upstream CVEs; restrict index-creation rights [Rec].
- **Tier: Strategic. No flag.** Scored under rubric rule 2 (self-hosted software), with host controls presumed on the hyperscaler services (CP2 Q1).

**Pinecone (Pinecone Systems).**
- *What it is now:* a fully managed vector and document index with metadata filtering, namespaces and server-side embedding [VF: A2-S051]. It hosts rerankers (pinecone-rerank-v0, Cohere Rerank 3.5, bge-reranker-v2-m3) and a sparse model for cascading retrieval [VF: A2-S101]. Dedicated Read Nodes became GA in April 2026 [VF: A2-S072]. Python SDK 10.0.0 (3 September 2026) introduced schema-based document indexes and breaking changes [VF: A2-S051, A2-S072].
- *Repositioning:* Pinecone describes itself as knowledge infrastructure for AI. Nexus, GA on 6 August 2026, compiles enterprise data into task-specific knowledge artifacts for agents, queried in KnowQL, with field-level access control, citations, PII-aware ingestion and lineage [VF: A2-S073, V1-S029]. Nexus integrates with Microsoft OneLake (June 2026) [VF: A2-S073]. Ash Ashutosh became CEO in September 2025; the founder, Edo Liberty, is Chief Scientist [VF: A2-S068, A2-S072].
- *Certifications and deployment:* SOC 2 Type II (2025 report, zero deviations), ISO/IEC 27001:2022 and HIPAA with a BAA on request [VF: A2-S095, V1-S078]. CMEK is set at project level and cannot be reversed; AWS PrivateLink is GA for serverless indexes [VF: A2-S096, A2-S097]. BYOC was announced GA in late September 2026 on AWS, GCP and Azure. It requires the Enterprise plan, supports Dedicated Read Node indexes only, and gives the vendor no SSH, VPN or inbound access [VF: A2-S069, V1-S034]. Some features (Assistant, Inference, on-demand indexes) were not available in BYOC as of late August [VF: V1-S034]. EU serverless regions include AWS eu-west-1 (Ireland) and eu-central-1 (Frankfurt) and GCP europe-west4 (Netherlands); the Starter plan is limited to AWS us-east-1 [VF: B-L6-S003].
- *Access control:* SAML SSO and SCIM, RBAC for users, service accounts and API keys, and audit logs on Enterprise or the HIPAA add-on [VF: A2-S097, A2-S098].
- *Pricing (as of 7 October 2026):* Builder US$20 per month, Standard minimum US$50 and Enterprise minimum US$500 per month, with read and write units priced per million; BYOC adds a platform fee, a per-node rate and the firm's own cloud costs, and BYOC nodes are billed whether idle or busy [VF: A2-S074, A2-S099, A2-S069].
- *Strengths:* the most complete managed-service control set among the dedicated vendors here (SOC 2 Type II, ISO 27001, CMEK, SCIM, audit logs), with BYOC for residency [AJ].
- *Limitations:* the API and the service are proprietary [VF: A2-S051]. Nexus and KnowQL extend the platform into ingestion and knowledge compilation, which deepens coupling [AJ]. The last disclosed funding round was in 2023 [VF: A2-S075]. Nexus benchmark figures are vendor-reported and not relied on here [AJ].
- *Choose when:* you want a managed dedicated store at scale, with enterprise identity and keys, and can accept Enterprise pricing for BYOC [AJ].
- *Avoid when:* you need self-hosting or air-gap, or would let Nexus become the only place where curated knowledge exists [AJ].
- *Competitors:* Zilliz Cloud (Milvus), Qdrant Cloud, turbopuffer.
- *FS note:* use BYOC or an EU region; keep the source of truth and raw text outside; treat Nexus as a separate decision with its own exit plan [Rec].
- **Tier: Tactical. No flag.** It scores 3.80 FS, above the Strategic guide. It is held at Tactical because lock-in scores 2 and the vendor is widening its scope into L5 and L8, so it should not be a foundational dependency without a decided exit route [AJ].

**Qdrant (Qdrant Solutions GmbH).**
- *What it is now:* an Apache-2.0 vector search engine written in Rust, with dense and sparse vectors, payload filtering, hybrid fusion, multitenancy and quantisation [VF: A2-S108, A2-S052, A2-S103]. Server 1.19.2 was released on 5 October 2026 [VF: A2-S102]. Recent releases added ACORN filtered search and tiered multitenancy (1.16), weighted RRF and audit access logging (1.17), and TurboQuant quantisation and a low-memory mode (1.18) [VF: A2-S103, A2-S102].
- *Deployment:* Managed Cloud on AWS, GCP and Azure; Hybrid Cloud with clusters in the customer's network, managed through the Qdrant Cloud console (Enterprise plan); Private Cloud, including air-gapped; and self-hosting [VF: A2-S106, A2-S105, A2-S108].
- *Certifications and residency:* SOC 2 Type II and HIPAA, with the BAA documented for Managed Cloud only; ISO 27001 was not found [VF: A2-S105, V1-S069]. EU customers can keep data in EU regions exclusively [VF: A2-S105].
- *Access control:* Qdrant Cloud has Base, Admin and Owner roles plus custom roles. SSO (SAML, OIDC, Okta, Azure AD and others) is an add-on for the Premium tier. Database access uses admin, read-only or JWT keys scoped to individual collections [VF: B-L6-S007].
- *Funding:* a US$50M Series B on 12 March 2026, led by AVP [VF: A2-S107, V1-S032].
- *Strengths:* filter-aware search and per-collection keys suit entitlement-heavy retrieval; the widest deployment range here, including air-gap [AJ].
- *Limitations:* no ISO 27001 [VF: V1-S069]. Upgrades cannot skip 1.16 [VF: A2-S102]. Managed pricing evidence is thin and may be stale [VF: A2-S106].
- *Choose when:* you need a dedicated engine in your own estate or cloud account, with strong filtering and tenant isolation [AJ].
- *Avoid when:* ISO 27001 is a hard procurement gate for a vendor-operated service [AJ].
- *Competitors:* Milvus/Zilliz, Weaviate, Pinecone.
- *FS note:* self-host or use Hybrid Cloud for client data; issue collection-scoped keys per service; turn on audit access logging [Rec].
- **Tier: Strategic. No flag.**

**Milvus and Zilliz Cloud (LF AI & Data; Zilliz).**
- *What it is now:* Milvus is an Apache-2.0 distributed vector database and a graduated LF AI & Data project; Zilliz created it, maintains it and sells Zilliz Cloud [VF: A2-S118, A2-S053]. Milvus 3.0 reached GA on 29 July 2026 (3.0.2 on 20 September), and the 2.6 line is still patched [VF: A2-S117, V1-S031]. It supports dense and sparse vectors (SINDI sparse index), BM25 full-text search, JSON path indexing, faceted search and online schema changes [VF: A2-S117, A2-S054].
- *Repositioning:* 3.0 is "lake-native": indexes over vectors kept in object storage and open formats (Loon engine, Vortex columnar format), with External Collections for lakehouse workflows. Zilliz Cloud is now a "Vector Lakebase" [VF: A2-S118].
- *Certifications and deployment:* Zilliz Cloud holds SOC 2 Type II (scope includes Free, Serverless, Dedicated and BYOC; report under NDA) and ISO/IEC 27001 [VF: A2-S119, A2-S120]. CMEK and HIPAA eligibility come with Business Critical; SSO, audit logs and private endpoints with Enterprise Dedicated, which carries a 99.95% uptime SLA [VF: A2-S120]. BYOC puts the data plane in the customer's cloud account under a shared-responsibility model [VF: A2-S119]. EU regions include AWS Frankfurt and Ireland, GCP Frankfurt and Azure Germany West Central and North Europe [VF: A2-S121]. Milvus itself runs as Lite, Standalone or Distributed, with the same API as Zilliz Cloud [VF: A2-S054].
- *Strengths:* foundation governance with a permissive licence, plus a certified managed and BYOC route from the same codebase [AJ].
- *Limitations:* 3.0 is ten weeks old and not guaranteed compatible with 2.6 servers [VF: A2-S117]. Milvus Lite has no authentication or TLS [VF: A2-S054]. Zilliz's last disclosed raise was in 2022 [VF: A2-S122]. Distributed Milvus is a substantial operational commitment [AJ]. RBAC on Zilliz Cloud is not evidenced in the fact base [NPV].
- *Choose when:* the corpus is very large, you want open-source portability with a managed or BYOC option, or you want vectors to sit with lakehouse data [AJ].
- *Avoid when:* a small team must self-operate it, or you need 3.0 features before the 3.x line has matured [AJ].
- *Competitors:* Qdrant, Pinecone, Weaviate.
- *FS note:* stay on 2.6 or a validated 3.0.x until your regression suite passes; Zilliz BYOC for residency; never expose Lite beyond a laptop [Rec].
- **Tier: Strategic. No flag.**

**Weaviate (Weaviate B.V.).**
- *What it is now:* a vector database that combines vector search with structured filtering and hybrid search [VF: A2-S110]. Version 1.39.7 was released on 25 September 2026, and 1.39 made the Boost API and MMR diversity GA and previewed 4-bit rotational quantisation [VF: A2-S109, A2-S110].
- *Licence change:* most code is BSD-3-Clause, but enterprise features under `wl/` are moving to a separate commercial licence with a licence key, in 1.40.0-rc.1 (19 September 2026). 1.40 is still a release candidate, and licence-key enforcement is off by default per the pull request [VF: A2-S115, V1-S070]. No official announcement was found [VF: A2-S115].
- *Certifications and deployment:* SOC 2 Type II (via Drata) and ISO 27001:2022; HIPAA on Premium Dedicated (AWS) with a BAA; BYOC certification scope not stated [VF: A2-S111, A2-S112, A2-S113, A2-S114]. Shared Cloud runs in AWS US East and Europe (Frankfurt); Premium Dedicated in about 40 regions [VF: A2-S111]. Self-hosting is supported [VF: A2-S115].
- *Access control:* RBAC with custom roles, OIDC users and groups, and automatic audit logging of authorisation decisions [VF: B-L6-S009]. The docs say console RBAC for Weaviate Cloud will come in a future release [VF: B-L6-S009].
- *Strengths:* mature hybrid search and an ISO-certified managed service [AJ].
- *Limitations:* the open-core transition is unannounced and incomplete, so the scope of the free edition is uncertain [AJ]. Only the latest three minors are supported [VF: A2-S109]. Pricing tier names conflict between pages [VF: A2-S111]. The last confirmed funding round was in 2023 [R: A2-S116].
- *Choose when:* you already run Weaviate, or need hybrid search with an ISO-certified dedicated service [AJ].
- *Avoid when:* your licence policy needs certainty about which features stay BSD [AJ].
- *Competitors:* Qdrant, Milvus/Zilliz, Elasticsearch.
- *FS note:* obtain a written statement of which security features will sit under the commercial licence before standardising [Rec].
- **Tier: Tactical. No flag.**

**turbopuffer.**
- *Conflict of interest:* Anthropic, the author's developer, is reported as a turbopuffer customer [R: A2-S126]. The product is scored on the same rubric as every other product, and an independent alternative is named below [AJ].
- *What it is now:* a proprietary serverless search service with namespaced ANN vector search (a centroid-based SPFresh index), BM25 full-text ranking and filters [VF: A2-S056, A2-S124]. All durable state sits in object storage, and compute nodes are stateless [VF: A2-S124]. Python SDK 2.11.0 was released on 7 October 2026 [VF: A2-S056].
- *Deployment and security:* SaaS in public regions on AWS, GCP and Azure, including Frankfurt, with customer data kept in the selected region [VF: B-L6-S002]. BYOC runs in the customer's Kubernetes cluster on AWS, GCP or Azure, and every vendor operation needs manual customer approval [VF: A2-S125]. SOC 2 Type 2, a HIPAA BAA on Scale and Enterprise, and per-namespace CMEK and private networking on Enterprise (from US$4,096 per month with a 35% usage premium) [VF: A2-S123, V1-S077].
- *Access control:* SSO for the dashboard on Scale and Enterprise [VF: B-L6-S002]. There is no built-in document-level RBAC; permissions are implemented as filters [VF: B-L6-S002]. BYOC API keys are all admin keys for their organisation, and audit logs with SIEM integration were an opt-in beta in March 2026 [VF: B-L6-S002]. ISO 27001 was not found [NPV].
- *Strengths:* object-storage economics and per-namespace keys suit very large, many-tenant corpora [AJ].
- *Limitations:* cold queries are much slower than cached ones [R: A2-S124]. Revenue and funding figures are from press and an aggregator only [R: A2-S126, A2-S127]. Key scoping is coarse [VF: B-L6-S002].
- *Choose when:* you have very many tenants or a very large corpus with skewed access, and want BYOC with per-tenant keys [AJ].
- *Avoid when:* you need fine-grained key scopes, ISO 27001 or self-hosting [AJ].
- *Independent alternative:* Milvus 3.0 or Zilliz Cloud BYOC for an object-storage-oriented design [VF: A2-S118, A2-S119].
- *Competitors:* Pinecone, Milvus/Zilliz, S3 Vectors.
- *FS note:* BYOC only for client data; one namespace and one key per client; warm-up policy for latency-sensitive tenants [Rec].
- **Tier: Tactical. No flag.**

**Elasticsearch (Elastic N.V.).**
- *What it is now:* a distributed search engine combining BM25, dense and sparse vectors (BBQ and DiskBBQ quantisation, default since 9.1) and hybrid retrievers (RRF, and linear with l2_norm) [VF: A2-S133]. `semantic_text` fields chunk and embed automatically, defaulting to Jina v5, and support MMR [VF: A2-S133]. Elastic 9.5 reached GA on 4 August 2026, adding a VectorDB index mode in technical preview [VF: A2-S133, V1-S085].
- *Licence and ownership:* source is available under AGPLv3 (an OSI licence added in 2024), SSPL 1.0 or the Elastic License 2.0; paid features are proprietary; clients are Apache-2.0 [VF: A2-S132]. Elastic acquired Jina AI, completing on 9 October 2025 [VF: A2-S023, V1-S025]. OpenSearch 3.9.0 (29 September 2026, Apache-2.0) is the fork alternative [VF: A2-S136].
- *Certifications and deployment:* Elastic Cloud holds ISO 27001, 27017 and 27018 and SOC 2 Type II [VF: A2-S045]. Customer-managed keys (AWS KMS, Azure Key Vault, Google Cloud KMS) are available on Elastic Cloud Hosted with an Enterprise subscription; Serverless BYOK is on the roadmap [VF: A2-S134]. Private Link and Private Service Connect are supported, including London [VF: A2-S134]. EU and UK regions span AWS, GCP and Azure [VF: A2-S135]. Self-managed and on-premises deployment is supported [VF: A2-S132].
- *Access control:* SAML/OIDC SSO, RBAC, field- and document-level security and audit logging (Platinum when self-managed) [VF: A2-S134]. Elastic Cloud SAML SSO and RBAC were confirmed in the CP2 review [VF: B-REV-S019]; the Cloud subscription tier for audit logging is not confirmed [VF: A2-S134].
- *Strengths:* the strongest lexical-plus-vector retrieval in this set, and document-level security that maps directly onto entitlement-aware retrieval [AJ].
- *Limitations:* the security features that matter here sit in paid tiers [VF: A2-S134]. Cluster pricing is not verified [NPV]. Elastic now bundles embedding models (Jina), which couples L6 and L7 [VF: A2-S023] [AJ].
- *Choose when:* Elastic or OpenSearch is already a platform, or the corpus is lexical-heavy (identifiers, tickers, fund codes) [AJ].
- *Avoid when:* you would introduce it only for vectors, with no search team to run it [AJ].
- *Competitors:* OpenSearch (no record), MongoDB Vector Search, Weaviate.
- *FS note:* use document-level security for entitlements; pin the `semantic_text` model explicitly; choose the AGPL distribution only after legal review [Rec].
- **Tier: Strategic, conditional: where Elastic is already an operated platform, because cost scores 2 [AJ]. No flag.**

**MongoDB Vector Search (MongoDB, Inc.).**
- *What it is now:* vector and full-text search inside the document database through `$vectorSearch` and `$search`, with hybrid fusion (`$rankFusion`, `$scoreFusion`) GA [VF: A2-S137, A2-S141]. `$rerank` runs Voyage cross-encoders in the aggregation pipeline (public preview, 8.3+, at most 1,000 documents), and Automated Embedding uses Voyage models (public preview) [VF: A2-S141, A2-S078]. Search and Vector Search became GA for self-managed Community Edition and Enterprise Advanced on MongoDB 8.2+ (around July 2026) [VF: A2-S137, V1-S035]. MongoDB has owned Voyage AI since 17 February 2025 [VF: A2-S033, V1-S023].
- *Licence:* Atlas is a proprietary managed service; Community Edition and the `mongot` search binary are under SSPL; Enterprise Advanced is commercial [VF: A2-S137].
- *Certifications and security:* Atlas holds ISO/IEC 27001:2022, SOC 2 Type II, PCI DSS, HITRUST and CSA STAR, has had a HIPAA examination, and Atlas for Government has FedRAMP Moderate [VF: A2-S138]. MongoDB's SOC 2 scope page does not name Voyage and excludes preview features [VF: B-REV-S027]. Customer key management is available (not on Free or Flex), but search indexes are covered only with dedicated Search Nodes [VF: A2-S139].
- *Access control:* SAML SSO for the Atlas UI and OIDC for database users, organisation and project roles, custom database roles, and database auditing on M10 and larger clusters (not Free or Flex), with log retention of 30 days [VF: B-L6-S001].
- *Residency:* the customer chooses the cluster region. The Atlas Embedding and Reranking API offers an EEA Geography at a 10% premium, but Automated Embedding and native reranking do not yet support Geography targeting [VF: A2-S142, A2-S139, A2-S140].
- *Strengths:* transactional integration where the operational data is already in MongoDB [AJ].
- *Limitations:* SSPL for self-managed and Voyage-native features couple L6 and L7 [VF: A2-S137, A2-S141]. The newest retrieval features are preview [VF: A2-S141]. Atlas's 30-day log retention is shorter than most records policies [VF: B-L6-S001] [AJ].
- *Choose when:* MongoDB is the system of record for the documents being retrieved [AJ].
- *Avoid when:* you would adopt MongoDB only for retrieval, or would rely on preview reranking or embedding in regulated flows [AJ].
- *Competitors:* pgvector, Elasticsearch, Pinecone.
- *FS note:* use dedicated Search Nodes so CMK covers the indexes; export audit logs to the firm's archive; keep Voyage features off until GA and Geography-scoped [Rec].
- **Tier: Strategic, conditional: only where MongoDB is already the operational store, because lock-in scores 2 [AJ]. No flag.**

**Chroma (Chroma).**
- *What it is now:* an Apache-2.0 embedded or client-server database for documents and embeddings with a small API, in-memory, persistent or client-server mode [VF: A2-S060]. Chroma Cloud adds serverless vector, hybrid and full-text search [VF: A2-S060]. The latest PyPI release is chromadb 1.5.9 (5 May 2026) [VF: A2-S060]. Chroma 1.0 (March 2025) was a Rust rewrite that removed the built-in authentication implementations [VF: A2-S131].
- *Cloud:* SOC 2 Type II [VF: A2-S130, V1-S086]. Multi-tenant regions are AWS us-east-1 and GCP europe-west1 (Belgium); BYOC and single-tenant clusters are custom-priced [VF: A2-S129, A2-S128]. CMEK is GA [VF: B-L6-S008]. The Team plan costs US$250 per month plus usage (as of 7 October 2026) [VF: A2-S128, V1-S086].
- *Access control:* access control is scoped to the tenant, and API keys can be scoped to one database [VF: B-L6-S008]. Customer-facing roles, SSO and audit logs are not documented [NPV].
- *Strengths:* the fastest path from notebook to working retrieval [AJ].
- *Limitations:* no PyPI release for five months at the time of research [VF: A2-S060]. Seed-funded (US$18M) [VF: A2-S131]. One EU region and no UK region for the multi-tenant cloud [VF: A2-S129].
- *Choose when:* prototypes, evaluation harnesses and embedded single-user tools [AJ].
- *Avoid when:* the data is client-confidential or the system is production-critical [AJ].
- *Competitors:* pgvector, Qdrant, turbopuffer.
- *FS note:* do not self-host the open-source server without an authenticating proxy; do not promote a Chroma prototype without a re-platforming decision [Rec].
- **Tier: Tactical. No flag.** Enterprise readiness capped at 2 (customer SSO, roles and audit logs NPV).

**Amazon S3 Vectors (AWS).**
- *What it is now:* object storage with native vector storage and similarity queries, organised as vector indexes in vector buckets [VF: A2-S094, A2-S092]. It went GA in December 2025 after a July 2025 preview [VF: A2-S081, V1-S030]. An index holds up to 2 billion vectors (1 to 4,096 dimensions) with up to 50 metadata keys, a bucket up to 10,000 indexes, and queries return up to 10,000 results since June 2026 [VF: A2-S083, A2-S086, V1-S030]. It has no native BM25 or full-text search [VF: A2-S083].
- *Integration:* a vector store for Bedrock Knowledge Bases (35 metadata keys, 1 KB metadata limit), a storage engine for OpenSearch managed clusters, and an export source for OpenSearch Serverless [VF: A2-S089, A2-S093]. AWS positions it as a low-cost durable tier that hands hot vectors to OpenSearch [VF: A2-S092].
- *Security and access:* SSE-S3 by default; SSE-KMS with customer-managed keys per bucket or index, immutable after index creation; PrivateLink endpoints; IAM-based access [VF: A2-S090, A2-S091]. CloudTrail can log S3 Vectors data events (PutVectors, GetVectors, DeleteVectors, ListVectors, QueryVectors), but data events are off by default [VF: B-L6-S006]. Compliance-programme scope and HIPAA eligibility for S3 Vectors specifically were not confirmed [VF: A2-S090, B-L6-S006].
- *Regions and price:* about 34 Regions, including AWS GovCloud (US) and the AWS European Sovereign Cloud (Germany) [VF: A2-S084, A2-S085]. Storage is US$0.06 per GB-month, with per-PUT and per-query charges; AWS's worked example of 50M vectors and 1M queries costs US$178.61 per month (as of 7 October 2026) [VF: A2-S087, V1-S030].
- *Strengths:* very low cost per stored vector with no capacity to manage, inside the firm's existing AWS controls [AJ].
- *Limitations:* AWS-only API [VF: A2-S092]. Vector and metadata only, so hybrid needs OpenSearch [VF: A2-S083, A2-S093]. Limits and prices changed several times in 2026 [VF: A2-S086, A2-S088].
- *Choose when:* you are AWS-centred and need a cheap, durable tier for large or infrequently queried corpora, or a Bedrock Knowledge Base [AJ].
- *Avoid when:* you need lexical search, low tail latency or a multi-cloud exit route [AJ].
- *Competitors:* turbopuffer, Milvus 3.0, pgvector on Aurora.
- *FS note:* enable CloudTrail data events on regulated indexes; set the KMS key at index creation; record S3 Vectors under the AWS CTPP concentration entry [Rec].
- **Tier: Tactical. No flag.** Enterprise readiness at 4 under the hyperscaler presumption: platform controls presumed (CP2 Q1); confirm per service.

### 6.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
SCORE_TABLE_PLACEHOLDER

**Scoring notes [AJ]:**
- **NPV cap applied once:** Chroma's enterprise readiness is capped at 2, because customer-facing SSO, roles and audit logs are not documented (only tenant-scoped access and database-scoped keys were found) [VF: B-L6-S008].
- **Caps lifted by this writer's searches (CP2 Q2):** MongoDB (SSO, roles and auditing [VF: B-L6-S001]), Qdrant (Cloud RBAC, SSO add-on and collection-scoped keys [VF: B-L6-S007]), Weaviate (RBAC, OIDC and audit logging [VF: B-L6-S009]) and turbopuffer (dashboard SSO [VF: B-L6-S002]). turbopuffer stays at 3, not higher, because keys are admin-level and roles are undocumented.
- **Hyperscaler presumption (CP2 Q1):** S3 Vectors enterprise readiness is 4. pgvector's enterprise readiness of 4 relies on the managed PostgreSQL host (RDS, Aurora, Cloud SQL, AlloyDB, Azure) [VF: B-L6-S004, B-L6-S005]; platform controls presumed (CP2 Q1), confirm per service.
- **Certification scope (CP2 Q4):** S3 Vectors security is 4, not 5, because no compliance-programme scope statement for S3 Vectors was found [VF: B-L6-S006]. MongoDB is 4 because the Atlas certifications are platform-level and the SOC 2 scope excludes preview features [VF: B-REV-S027]. Milvus/Zilliz is 4 because the SOC 2 report is under NDA and Zilliz certifications were not re-checked by the verifiers.
- **No ISO 27001, maximum 3:** Qdrant, turbopuffer and Chroma.
- **Rule 2 (self-hosted software):** pgvector is scored on project hygiene (two CVEs fixed promptly, permissive licence) and on what it enables inside the firm's own PostgreSQL.
- **Ownership change:** no L6 product changed owner in 2025–26. MongoDB and Elastic are acquirers (Voyage AI, Jina AI), which affects L7 lock-in, not L6 scores.
- **Strategic despite a 2:** Elasticsearch (cost 2) and MongoDB (lock-in 2) are Strategic only on the conditions in their deep dives. Pinecone (3.80 FS) is Tactical by judgement, explained in its deep dive.
- **Low scores** are present in every column except ecosystem and maturity: S3 Vectors deployment 2, Chroma maturity 2, and four lock-in scores of 2 (Pinecone, turbopuffer, MongoDB, S3 Vectors).

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| pgvector | PostgreSQL License (permissive, OSI) [VF: V1-S021] | Self-host, on-prem; managed on RDS/Aurora, Azure, Cloud SQL/AlloyDB [VF: A2-S061, B-L6-S004, B-L6-S005] | Inherits host; not applicable to the extension [AJ] | Host region choice [AJ] | Open-source project [VF: A2-S050] |
| Pinecone | Proprietary; SDK Apache-2.0 [VF: A2-S051] | SaaS on AWS/GCP/Azure; BYOC (Enterprise, DRN only) [VF: A2-S069, V1-S034] | SOC 2 Type II, ISO 27001:2022, HIPAA BAA [VF: A2-S095, V1-S078] | AWS Ireland and Frankfurt, GCP Netherlands [VF: B-L6-S003] | Independent; CEO change Sept 2025 [VF: A2-S068] |
| Qdrant | Apache-2.0; cloud offerings commercial [VF: A2-S108] | SaaS, Hybrid Cloud, Private Cloud incl. air-gap, self-host [VF: A2-S106] | SOC 2 Type II, HIPAA (Managed Cloud BAA); no ISO 27001 found [VF: A2-S105, V1-S069] | EU-only regions available [VF: A2-S105] | Independent; Series B Mar 2026 [VF: A2-S107] |
| Milvus / Zilliz | Apache-2.0; Zilliz Cloud commercial [VF: A2-S118] | Lite/Standalone/Distributed; Zilliz SaaS and BYOC [VF: A2-S054, A2-S119] | Zilliz: SOC 2 Type II, ISO 27001; HIPAA-eligible tier [VF: A2-S119, A2-S120] | Frankfurt, Ireland, Germany West Central, North Europe [VF: A2-S121] | LF AI & Data graduated; Zilliz maintainer [VF: A2-S118] |
| Weaviate | BSD-3 core; `wl/` commercial in 1.40 RC [VF: A2-S115, V1-S070] | SaaS, Dedicated, BYOC, self-host [VF: A2-S111, A2-S114] | SOC 2 Type II, ISO 27001:2022, HIPAA (Premium, AWS) [VF: A2-S111, A2-S112, A2-S113] | Frankfurt (Shared); ~40 Dedicated regions [VF: A2-S111] | Independent [VF: A2-S115] |
| turbopuffer | Proprietary; SDK MIT [VF: A2-S056] | SaaS, dedicated, BYOC [VF: A2-S125, B-L6-S002] | SOC 2 Type 2, HIPAA BAA (Scale+) [VF: A2-S125, V1-S077] | Frankfurt and others [VF: B-L6-S002] | Independent; little outside capital [R: A2-S126] |
| Elasticsearch | AGPLv3 / SSPL / ELv2; paid features proprietary [VF: A2-S132] | Cloud Hosted and Serverless, self-managed, on-prem [VF: A2-S135, A2-S132] | Elastic Cloud ISO 27001/27017/27018, SOC 2 Type II [VF: A2-S045] | Many EU and UK regions [VF: A2-S135] | Elastic N.V.; acquirer of Jina [VF: A2-S023] |
| MongoDB Vector Search | Atlas proprietary; Community and `mongot` SSPL [VF: A2-S137] | Atlas on AWS/Azure/GCP; self-managed Community and EA [VF: A2-S140, A2-S137] | Atlas ISO 27001:2022, SOC 2 Type II, PCI DSS, HITRUST; FedRAMP Moderate (Gov) [VF: A2-S138] | Region choice; EEA Geography for Embedding API [VF: A2-S142] | MongoDB, Inc.; acquirer of Voyage [VF: A2-S033] |
| Chroma | Apache-2.0 [VF: A2-S060] | Embedded, self-host, Cloud, single-tenant, BYOC [VF: A2-S060, A2-S128] | Chroma Cloud SOC 2 Type II [VF: A2-S130, V1-S086] | GCP Belgium only (multi-tenant) [VF: A2-S129] | Independent; seed-funded [VF: A2-S131] |
| S3 Vectors | Proprietary AWS service [VF: A2-S092] | AWS regional service [VF: A2-S084] | S3 Vectors scope not confirmed [VF: A2-S090, B-L6-S006] | EU Regions and European Sovereign Cloud [VF: A2-S084] | AWS (designated CTPP) [VF: R-DORA, A8-S021] |

### 6.9 Decision tree

The central question is whether a dedicated vector database is needed at all [AJ]. Most regulated asset-management corpora (commentaries, research notes, policies, style guides) are in the range that an existing database or search engine handles, and every additional store is another copy of confidential content to secure, retain, back up and exit [AJ].

```text
STEP 0 [Rec]: Non-negotiables, whatever the store
  - Source of truth for approved content lives in L8/C3, not in the store.
  - Entitlements from C4 are applied as filters INSIDE the search; no unfiltered fallback.
  - Every chunk carries doc_id, version, tenant ids, classification, region,
    retention_until and embed_model_version; raw text (or pointer) kept.
  - Rebuild-from-source is tested twice a year; it is the primary backup and exit route.

STEP 1 [Rec]: Do you need a dedicated vector database at all?
  Is the content already in, or naturally owned by, an operated database or search platform?
  ├─ PostgreSQL is a firm standard
  │     → pgvector on the managed PostgreSQL service (UK/EU region),
  │       entitlement tables joined in SQL; track host pgvector version vs CVEs
  ├─ Elastic (or OpenSearch) is an operated platform, or the corpus is lexical-heavy
  │     (ISINs, tickers, fund codes, share-class names)
  │     → Elasticsearch hybrid (BM25 + vectors, RRF) with document-level security
  │       (OpenSearch if licence policy requires Apache-2.0)
  ├─ MongoDB is the system of record for these documents
  │     → MongoDB Vector Search on dedicated Search Nodes (CMK), Voyage features off
  │       until GA and Geography-scoped
  ├─ AWS-centred, Bedrock Knowledge Bases, large or rarely queried corpus
  │     → S3 Vectors as the cost tier; OpenSearch in front if hybrid or low
  │       latency is needed; CloudTrail data events on
  └─ None of these → go to STEP 2

STEP 2 [Rec]: Which trigger makes a dedicated engine necessary?
  Proceed only if at least one is evidenced in a load test on your own data:
  (a) filtered p95 latency or filtered recall fails the budget in the existing platform
  (b) tenants must be isolated at scale (hundreds or more clients/funds with separate
      keys, quotas or deletion), beyond what schemas or indexes can manage cleanly
  (c) corpus size or write rate makes the existing platform's RAM or ops cost
      disproportionate
  No trigger → stay in STEP 1.

STEP 3 [Rec]: Dedicated engine, by where it must run
  Must run in your own estate or air-gapped?
  ├─ Yes → Qdrant (self-host or Private Cloud; collection-scoped JWT keys)
  │        or Milvus (Standalone/Distributed; LF AI & Data governance) for very large corpora
  └─ No, but data plane must be in your cloud account (BYOC)?
       ├─ Open-source engine preferred (exit by self-hosting)
       │     → Qdrant Hybrid Cloud, or Zilliz Cloud BYOC (Milvus)
       ├─ Managed, proprietary, strongest control set → Pinecone Enterprise BYOC
       │     (Dedicated Read Nodes only; Nexus is a separate decision)
       └─ Very many tenants, object-storage economics, per-tenant keys
             → turbopuffer BYOC (author conflict disclosed; alternative: Zilliz BYOC)
  Vendor-hosted SaaS acceptable (non-confidential corpora)?
       → any of the above in a UK/EU region; Weaviate if hybrid plus ISO 27001
         managed service matters and the licence position is settled

STEP 4 [Rec]: Prototypes and harnesses
  Notebook, evaluation harness, single-user tool, non-confidential data
       → Chroma (embedded) or pgvector in a local container. Never promoted to
         production without returning to STEP 1.

STEP 5 [Rec]: Checks before go-live
  Leak test per tenant passes (zero)?  Filtered recall within tolerance?
  Deletion canary within SLA?  Rebuild time inside exit-plan tolerance?
  All copies (vectors, text, backups, caches) in approved regions?
  Store recorded in the outsourcing / ICT register with an exit plan?
```

### 6.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Vector index and data | **Acceptable**, if rebuildable | Vectors are derived; with raw text and the pinned model kept outside, any index can be rebuilt (the L7 rule) [AJ] | Rebuild-from-source pipeline; per-chunk metadata contract |
| Query API | **Manageable** | Proprietary APIs (Pinecone, turbopuffer, S3 Vectors) [VF: A2-S051, A2-S056, A2-S092] versus SQL (pgvector) and open-source engines (Qdrant, Milvus) [VF: A2-S108, A2-S118] | A thin internal retrieval interface (query, filters, tenant, top-k, returns IDs and scores) used by L3; no store SDK in agent code |
| Filter and entitlement logic | **Unacceptable if only in the store's proprietary syntax** | The entitlement policy is the firm's control and must survive a store change [AJ] | Policy held in C4; compiled into each store's filter syntax by the retrieval service |
| Licence | **Manageable** | Permissive (pgvector, Qdrant, Milvus, Chroma) [VF: V1-S021, A2-S108, A2-S118, A2-S060]; AGPL, SSPL or ELv2 (Elastic) [VF: A2-S132]; SSPL (MongoDB) [VF: A2-S137]; open core in transition (Weaviate) [VF: A2-S115, V1-S070] | Licence review before standardising; OpenSearch as the Elastic exit [VF: A2-S136] |
| Store-bundled embedding and reranking | **Manageable**, becoming **unacceptable** if the model is unpinned | Leaving the store then also means re-embedding (L7 §7.10) [AJ] | Pin the model explicitly; keep embedding in the L7 service where possible |
| Knowledge-engine layer (Pinecone Nexus, KnowQL) | **Unacceptable as the only home of curated knowledge; manageable as a derived layer** | It compiles data into vendor-specific artifacts queried in a proprietary language [VF: A2-S073] | Keep curated sources and lineage in L8/C3; treat compiled artifacts as disposable |
| Object-store format | **Manageable** | Milvus 3.0 uses open formats [VF: A2-S118]; turbopuffer's and S3 Vectors' formats are proprietary [AJ] | Rebuild route regardless of format |
| Hyperscaler-native stores | **Manageable**, with concentration noted | S3 Vectors is AWS-only and AWS is a designated CTPP [VF: A2-S092, R-DORA, A8-S021] | Exit plan names an alternative store and the rebuild time |

### 6.11 Regulated FS lens (POV 2)

**Model risk.**
- *What is in scope.* A retrieval store is not a model under SS1/23 or SR 26-2 [AJ]. SS1/23 applies to banks and PRA-designated investment firms with internal-model approval [VF: R-PRA-SS123, A8-S008]. SR 26-2 superseded SR 11-7 on 17 April 2026 and places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001, A8-S002].
- *Why it still matters.* The retrieval configuration (index, filters, fusion, embedding version) determines what the generative system sees, so it is part of the system that the firm's own validation must cover [AJ]. Changes to it should trigger the same regression suite as a model change (L9) [Rec].

**EU AI Act.**
- *Deployer logging.* Article 26 requires deployers of high-risk systems to keep logs for at least six months [VF: R-EUAIA, A8-S011]. Annex III duties apply from 2 December 2027 under Regulation (EU) 2026/1744 [VF: R-EU-OMNIBUS-AI, A8-S011].
- *Scope here.* Commentary drafting is not Annex III [AJ]. Recording retrieved document IDs per output is nevertheless the cheapest way to make any output reproducible [Rec].

**Operational resilience and outsourcing.**
- *Register.* For EU entities, a vector-database SaaS is an ICT third-party service that belongs in the DORA register of information, with Article 30 terms and an exit strategy where it supports a critical or important function [VF: R-DORA, A8-S021] [AJ].
- *Concentration.* The first DORA CTPP list (18 November 2025) includes AWS, Google Cloud and Microsoft [VF: R-DORA, A8-S020, A8-S021]. The UK designated the same three and Oracle on 8 July 2026, in force 13 July [VF: R-UK-CTP, A8-S023]. No vector-store vendor is designated [AJ]. However, Pinecone, Zilliz, Qdrant Cloud, Weaviate Cloud, turbopuffer, MongoDB Atlas, Elastic Cloud and Chroma Cloud all run on those hyperscalers [VF: A2-S069, A2-S121, A2-S105, A2-S111, A2-S125, A2-S140, A2-S135, A2-S129], so their outages correlate with the cloud platform's [AJ]. Record the underlying cloud for every L6 service [Rec].
- *Notification lead time.* PRA PS7/26 and FCA PS26/2 require notification of material third-party arrangements from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. A new SaaS vector store supporting an important business service should be planned with that lead time [Rec].
- *Exit.* SS2/21 expects documented and tested exit plans, including stressed exit [VF: R-PRA-SS221, A8-S048]. For this layer the exit plan is the rebuild: approved source corpus, pinned embedding model, rebuild runbook and measured rebuild time [Rec]. Export features are a secondary route [AJ].

**Residency, transfers and erasure.**
- *Vector copies are personal or confidential data.* Embeddings derived from documents that contain client or personal data should inherit that classification [AJ]. Residency must cover the vectors, the raw text payload, caches, replicas and backups [AJ].
- *Location controls.* FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. EU-to-US transfers rely on the Data Privacy Framework or SCCs, and the annulment appeal (C-703/25 P) is pending [VF: R-DATA-TRANSFERS, A8-S053]. Several services pin data to a chosen region: turbopuffer [VF: B-L6-S002], Chroma [VF: A2-S129], Qdrant for EU customers [VF: A2-S105] and S3 Vectors [VF: A2-S084].
- *Right to erasure.* An erasure request must reach the index, not only the source [AJ]. Deletion must be verified by search and, where the engine compacts lazily, by physical removal [AJ]. S3 Vectors exposes DeleteVectors and can log it in CloudTrail [VF: B-L6-S006].
- *Retention.* Retention should be driven by the records policy. Atlas keeps database logs and audit messages for 30 days, so audit logs must be exported to the firm's archive [VF: B-L6-S001] [Rec].

**Auditability.**
- Log every retrieval (caller, entitlement claims, filter, partition, document and chunk IDs with versions, scores) to the evidence store [Rec]. Engine-side access logs help: Qdrant audit access logging [VF: A2-S103], Weaviate RBAC audit logs [VF: B-L6-S009], Pinecone audit logs on Enterprise [VF: A2-S097], MongoDB database auditing [VF: B-L6-S001] and S3 Vectors CloudTrail data events [VF: B-L6-S006].

**Standards.**
- *OWASP.* The OWASP Top 10 for LLM Applications 2026 is the operative list [VF: R-OWASP-LLM, V2-S056]; its full entries were not retrieved [VF: R-OWASP-LLM, A8-S041]. For traceability, the 2025 list named "Vector and Embedding Weaknesses" as LLM08 [R: A8-S040]. Test for cross-tenant retrieval, poisoned documents and embedding inversion against the 2026 list [Rec]. The Top 10 for Agentic Applications for 2026 starts with ASI01 Agent Goal Hijack [VF: R-OWASP-AGENTIC, A8-S042]; poisoned retrieved content is one route to it [AJ].
- *NIST and ISO.* NIST AI RMF 1.0 and AI 600-1 [VF: R-NIST-AIRMF, A8-S043, A8-S044] and ISO/IEC 42001 [VF: R-ISO-42001, A8-S045] provide the control taxonomy and management-system wrapper. None of the L6 vendors in the fact base lists ISO 42001 [AJ].
- *ESMA.* ESMA expects ex-ante input controls [VF: R-INTL-AI-ASSETMGMT, A8-S059]. An entitlement-filtered, approved-only index is an ex-ante input control [AJ].

### 6.12 Worked-example slice (POV 3)

**What the commentary agent needs from L6 [AJ].** The agent drafts the monthly Brinson-style attribution commentary (allocation, selection, currency, benchmark-relative return) for a generic multi-asset fund. Authoritative numbers come from the attribution engine through read-only L4 tools; L6 supplies only words and context. It needs:

1. **Three logical collections, one store.**
   - *Prior commentaries:* approved monthly commentaries for this fund, with fund, share class, period, author, approver, approval date and version.
   - *House style guide and glossary:* firm-wide, versioned, with an "effective from" date.
   - *Approved market notes:* house views and market summaries approved for external use, with an expiry date.
2. **Fund-level entitlement filters, applied inside the search.** Each request carries the analyst's entitlements from C4 (permitted fund IDs, client IDs and maximum classification). The store returns only chunks whose `fund_id` is in that set, or which are tagged firm-wide (style guide, approved market notes). Segregated mandates get their own partition (schema, collection or namespace) so that isolation does not depend on a filter clause alone.
3. **A hard empty result.** If no permitted passage meets the relevance threshold, the store returns nothing and the workflow drafts from the attribution output and the style guide only, flagging "no comparable commentary". There is no retry without filters.
4. **Hybrid retrieval.** Lexical matching for fund names, benchmark names, share-class codes and currency pairs; dense retrieval for phrasing; fusion in the store; rerank in L7.
5. **Freshness and expiry.** Market notes past their expiry date and superseded style-guide versions are excluded by filter, so the agent cannot cite a withdrawn view.
6. **Provenance for the evidence pack.** Each retrieved passage returns document ID, version, chunk ID, approval date and score, written to the C8 evidence pack alongside the trace ID, so the reviewer can see which past commentary shaped which sentence.
7. **Retention aligned to the records policy.** Each chunk carries `retention_until` from the records policy. Expired chunks are deleted by a scheduled job, and deletion is verified by canary query. Store snapshots follow the same retention.
8. **Residency.** For a UK or EU fund, the store, its replicas and its backups sit in UK or EU regions; for most firms that means pgvector on the firm's managed PostgreSQL, or Elastic if already run.

**Recommended configuration [Rec].** pgvector on the firm's managed PostgreSQL in a UK or EU region, with one schema per segregated mandate and a shared schema for pooled funds and firm-wide material. Entitlements are joined from the firm's entitlement table inside the same SQL statement. If Elastic is already the firm's search platform, use it with document-level security instead. Move to a dedicated engine only if the load test in §6.9 step 2 fails.

**What L6 must never do [AJ]:**
- return another fund's or client's material, by filter omission, by fallback or by a shared partition for segregated mandates
- serve numbers: attribution figures in past commentaries are context, never a source for this month's figures
- keep content after its retention date, or keep a vector copy after the source has been deleted or erased
- hold the only copy of an approved commentary or style guide
- run an unauthenticated store, or hold client content in a region the residency policy does not allow

### 6.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| "Vector DBs" layer with ten tiles | Vectors are a feature of databases, search engines and object storage, and some vendors sell knowledge engines above the store [VF: A2-S137, A2-S133, A2-S081, A2-S073] | "Retrieval and knowledge stores": a derived-index layer with entitlement filtering, tenant isolation and rebuild-from-source as defining duties [Rec] |
| Postgres + pgvector | pgvector 0.8.7 (1 October 2026), two 2026 CVE fixes, managed on all three hyperscalers [VF: V1-S020, V1-S022, B-L6-S004, B-L6-S005] | Strategic default where PostgreSQL is standard [Rec] |
| Pinecone "managed" | Managed plus BYOC (late September 2026); Nexus knowledge engine; CEO change [VF: V1-S034, A2-S073, A2-S068] | Tactical: managed dedicated store with BYOC; Nexus a separate decision [Rec] |
| Qdrant "open source" | Apache-2.0; Hybrid and air-gapped Private Cloud; Series B [VF: A2-S108, A2-S106, A2-S107] | Strategic dedicated engine for in-estate use [Rec] |
| Milvus "vector search" | Milvus 3.0 lake-native; Zilliz Cloud "Vector Lakebase" [VF: A2-S118, A2-S117] | Strategic dedicated engine for very large corpora; 3.0 after validation [Rec] |
| Weaviate "open source" | Open core in transition (`wl/` commercial licence, 1.40 RC) [VF: A2-S115, V1-S070] | Tactical until the licence position is settled [Rec] |
| turbopuffer "cloud vector store" | Vector plus BM25 on object storage; BYOC; Anthropic reported as a customer [VF: A2-S056, A2-S124, A2-S125; R: A2-S126] | Tactical: many-tenant, cost-sensitive corpora, BYOC only [Rec] |
| Elasticsearch "hybrid search" | Elastic 9.5; AGPL option; Jina models bundled [VF: A2-S133, A2-S132, A2-S023] | Strategic where already operated; OpenSearch as fork alternative [Rec] |
| MongoDB "Atlas vector" | MongoDB Vector Search, self-managed GA as well as Atlas; hybrid GA; Voyage reranking preview [VF: A2-S137, A2-S141] | Strategic where MongoDB is the operational store [Rec] |
| Chroma "open source" | Apache-2.0; Chroma Cloud with SOC 2 Type II; no PyPI release since May 2026 [VF: A2-S060, A2-S130] | Tactical: prototypes and harnesses [Rec] |
| S3 Vectors "AWS" | GA December 2025; 2 billion vectors per index; no BM25 [VF: A2-S081, A2-S083, V1-S030] | Tactical: AWS cost tier and Bedrock Knowledge Bases [Rec] |
| (absent) | Azure AI Search, Vertex AI Vector Search, OpenSearch, Oracle and SQL Server vector support are not in the fact base, except OpenSearch inside the Elastic record [VF: A2-S136] [NPV] | Assess in a follow-up pass; Azure- or Google-centred firms should evaluate their platform's native option at STEP 1 [Rec] |

**H5 ("vector database" should become "Retrieval / Knowledge Stores"). Provisional view; verdict in synthesis.**

The evidence supports the hypothesis on four counts.

- **Hybrid is standard.** Lexical and vector retrieval with fusion now ship in turbopuffer, Chroma Cloud, Milvus, Elasticsearch, MongoDB, Qdrant, Pinecone and Weaviate [VF: A2-S056, A2-S060, A2-S054, A2-S133, A2-S141, A2-S103, A2-S101, A2-S110]. A store that only does vector similarity, such as S3 Vectors, is positioned by its own vendor as a tier behind a search engine [VF: A2-S092, A2-S093].
- **General-purpose databases absorbed the feature.** PostgreSQL through pgvector, MongoDB including self-managed Community Edition, and Elasticsearch all offer vector retrieval in the platform firms already run [VF: A2-S061, A2-S137, A2-S133].
- **Storage is moving to object stores.** S3 Vectors, Milvus 3.0 and turbopuffer put durable vectors in object storage [VF: A2-S081, A2-S118, A2-S124].
- **Vendors are repositioning above the store.** Pinecone sells Nexus as a "knowledge engine for agents" [VF: A2-S073]; Chroma calls itself data infrastructure for AI [VF: A2-S060]; Elastic calls itself "the Search AI Company" [VF: A2-S023]; Qdrant frames composable vector search as core infrastructure [VF: A2-S107].

Retrieval-quality evidence points the same way. Anthropic's Contextual Retrieval study reports that combining contextual embeddings with contextual BM25 cut top-20 retrieval failures by 49%, and adding reranking by 67% [R: A2-S070]. Anthropic is the author's developer, so this is a conflict of interest; the figure is vendor-reported and not a decision input [AJ].

The counter-evidence is that dedicated engines still differentiate on filtered search, tenant isolation and scale [VF: A2-S103, A2-S124, A2-S117], so the category does not disappear; it becomes one implementation option inside a wider layer [AJ]. "Knowledge store" also risks overlapping with L5 memory and L8 ingestion, because Nexus reaches into both [VF: A2-S073] [AJ].

**Provisional recommendation.** Rename the layer "Retrieval and knowledge stores" [AJ]. Define it by responsibility (a derived, entitlement-filtered, rebuildable index over approved content) rather than by engine type, and show four implementation options beneath it: vectors in the operational database, search engines, dedicated vector engines, and object-store tiers [AJ]. Knowledge-engine products should sit at the boundary with L5 and L8, with their curated outputs treated as derived data [AJ]. **Provisional; verdict in synthesis.**
