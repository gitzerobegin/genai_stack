# Stage A notes: stream A2 (L7 Embeddings and reranking; L6 Vector and retrieval stores)

As of 7 October 2026. All facts carry source IDs from `sources.csv`; archive under `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A2/`.

**Research coverage.** The first pass ran out of the shared web-search budget part-way through L6. A **follow-up pass on 7 October 2026** (sources A2-S081 to A2-S145) then completed L6: S3 Vectors, Pinecone, Qdrant, Weaviate, Milvus/Zilliz, turbopuffer, Chroma, Elasticsearch/OpenSearch and MongoDB. It also filled L7 enterprise gaps for OpenAI, Cohere and Voyage. Vendor domains remain blocked for direct fetch (each tried once), so most primary sources are search-tool extracts with confidence capped at `medium`. Remaining `Not publicly verified` fields are listed in (e). Source IDs A2-S048 and A2-S049 are not allocated (numbering gap only).

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| OpenAI – Embeddings 3 | Still text-embedding-3-large / -3-small (launched 25 January 2024). No newer OpenAI embedding model and no OpenAI reranker found. | No change | A2-S001, A2-S002, A2-S035 |
| Gemini – Embedding 2 | gemini-embedding-2: GA 22 April 2026 (preview 10 March 2026). Natively multimodal (text, image, video, audio, PDF); Matryoshka 128–3,072 dims. Vertex AI docs are being renamed "Gemini Enterprise Agent Platform". | No change | A2-S004, A2-S005, A2-S039 |
| Voyage AI – Voyage-3 | Voyage AI was acquired by MongoDB (closed 17 February 2025). Current models are the Voyage 4 family (15 January 2026), voyage-code-4, voyage-context-4 and voyage-multimodal-3.5, plus rerank-3 (30 September 2026). voyage-4-nano is open weights (Apache 2.0). | Acquired; Version label wrong | A2-S033, A2-S006, A2-S007, A2-S034, A2-S071 |
| Cohere – Embed v3 + Rerank | Embed 5 Pro/Fast (30 September 2026) and Rerank 4 Pro/Fast (11 December 2025). Embed v4 is still listed. Aleph Alpha combination signed 16 September 2026, pending approval. | Superseded; Version label wrong | A2-S012, A2-S010, A2-S011, A2-S018 |
| Qwen3 – Embeddings | Qwen3-Embedding **and Qwen3-Reranker** (0.6B/4B/8B, Apache 2.0, June 2025), plus Qwen3-VL-Embedding/-Reranker (January 2026). Hosted versions on Model Studio. The graphic omits the reranker. | Mispositioned (partial: embed-only label) | A2-S020, A2-S021, A2-S022 |
| Jina AI – Embeddings v3 | Elastic acquired Jina AI (October 2025). Current models: jina-embeddings-v5-text (February 2026), v5-omni (May 2026) and jina-reranker-v3.5 (July 2026). Weights are CC-BY-NC-4.0. | Acquired; Version label wrong | A2-S023, A2-S024, A2-S025, A2-S026 |
| SBERT – Sentence transformers | sentence-transformers 6.1.0 (18 September 2026), Apache-2.0. Now maintained by Hugging Face (Tom Aarsen); originated at UKP Lab. It covers embeddings, rerankers, sparse and multi-vector (ColBERT-style) models. | No change (stewardship moved) | A2-S029, A2-S032, A2-S028 |
| NVIDIA – Embed | NVIDIA NeMo Retriever embedding and reranking NIMs: nemotron-3-embed-1b, llama-nemotron-embed(-vl)-1b-v2 and llama-nemotron-rerank(-vl) models. Production use needs NVIDIA AI Enterprise. | Renamed (ambiguous label resolved) | A2-S030, A2-S031, A2-S040, A2-S041 |
| EthicalAgents – embeddings | No such product found after 6 searches. The nearest match, Ethical Agentic AI Inc., is an AI-agent audit firm. | Not publicly verified | A2-S079 |
| Ragoos – RAG re-rankers | No such product found after 6 searches. Near-misses are a restaurant, RAGus.ai, RaGOO and Ragie. | Not publicly verified | A2-S080 |
| Postgres – + pgvector | pgvector 0.8.7 (5 October 2026), with 2026 CVE fixes in 0.8.2 and 0.8.7. pgvecto.rs is deprecated in favour of VectorChord. pgvectorscale continues under Tiger Data (formerly Timescale). | No change | A2-S061, A2-S062, A2-S063, A2-S064, A2-S066, A2-S067 |
| Pinecone – managed | Still managed, now with BYOC (GA; AWS/GCP/Azure) and Dedicated Read Nodes (GA April 2026). Repositioned as "knowledge infrastructure", with Nexus "knowledge engine for agents" GA 6 August 2026. Hosts its own and Cohere rerankers plus a sparse model. SOC 2 Type II, ISO 27001, HIPAA BAA. New CEO September 2025; SDK v10 (September 2026). | Mispositioned (descriptor understates BYOC/Nexus/integrated inference) | A2-S069, A2-S072, A2-S073, A2-S068, A2-S051, A2-S095, A2-S097, A2-S101 |
| Qdrant – open source | Server 1.19.2 (5 October 2026), Apache-2.0. Managed, Hybrid (in customer network) and Private Cloud. SOC 2 Type II and HIPAA. US$50M Series B (12 March 2026). | No change | A2-S102, A2-S108, A2-S106, A2-S105, A2-S107 |
| Milvus – vector search | Milvus 3.0 GA 29 July 2026 (3.0.2, 20 September 2026), re-architected as "lake-native" (indexes over object storage/open formats); Apache-2.0; LF AI & Data graduated. Zilliz Cloud repositioned as "Vector Lakebase" with BYOC, SOC 2 Type II and ISO 27001. | Version label n/a; scope widened (repositioned) | A2-S117, A2-S118, A2-S119, A2-S120 |
| Weaviate – open source | v1.39.7 (25 September 2026). Core still BSD-3-Clause, but a commercially licensed Enterprise Edition (`wl/`, licence key) is being introduced (1.40 RC). SOC 2 Type II, ISO 27001:2022, HIPAA on Premium Dedicated (AWS). BYOC available. | Mispositioned (descriptor "open source" now partial: open core) | A2-S109, A2-S115, A2-S111, A2-S112, A2-S113 |
| turbopuffer – cloud vector store | Serverless vector **and BM25 full-text** search with object storage as system of record; BYOC on AWS/GCP/Azure; SOC 2 Type 2, HIPAA BAA (Scale+), per-namespace CMEK (Enterprise). Customers include Atlassian, Cursor, Notion, Anthropic (press). | No change (descriptor understates full-text/BYOC) | A2-S056, A2-S124, A2-S125, A2-S123, A2-S126 |
| Elasticsearch – hybrid search | Elastic 9.5 (GA 4 August 2026): BBQ/DiskBBQ quantisation by default, RRF/linear hybrid retrievers, semantic_text defaulting to Jina v5, VectorDB index mode (preview). AGPLv3 licence option since 2024 alongside SSPL/ELv2. Acquired Jina AI. OpenSearch 3.9.0 (29 September 2026) is the fork alternative. | No change | A2-S133, A2-S132, A2-S023, A2-S136 |
| MongoDB – Atlas vector | MongoDB Vector Search now GA self-managed (Community and Enterprise Advanced, 8.2+, SSPL) as well as Atlas; hybrid search GA; native `$rerank` with Voyage rerankers (preview); Atlas Embedding and Reranking API with EU Geography. | No change (scope widened; "Atlas" label too narrow) | A2-S137, A2-S141, A2-S142, A2-S078 |
| Chroma – open source | chromadb 1.5.9 (5 May 2026), Apache-2.0, Rust core since 1.0 (March 2025). Chroma Cloud: SOC 2 Type II, regions AWS us-east-1 and GCP europe-west1, Team plan US$250/month, BYOC custom. "Open-source search/data infrastructure for AI". | No change | A2-S060, A2-S128, A2-S129, A2-S130, A2-S131 |
| S3 Vectors – AWS | Amazon S3 Vectors: preview July 2025, **GA December 2025**; ~34 Regions incl. GovCloud and European Sovereign Cloud; 2 billion vectors/index, 4,096 dims, 10,000 top-K; storage US$0.06/GB-month; integrates with Bedrock Knowledge Bases and OpenSearch. | No change (label correct) | A2-S081, A2-S083, A2-S084, A2-S087, A2-S089, A2-S093 |

## (b) Ambiguities owned by A2

- **A2 (EthicalAgents): unresolved, flagged "Not publicly verified".** Searches tried on 7 October 2026 (extended mode unless stated):
  1. `"EthicalAgents" embeddings`
  2. `Ethical Agents AI embedding model company`
  3. `ethicalagents.ai`
  4. `EthicalAgents huggingface embedding model` (standard mode; huggingface.co, github.com, pypi.org)
  5. `"The Full AI Stack Explained" Harish Kumar embeddings rerankers EthicalAgents Ragoos`
  6. `"Ethical Agents" OR "EthicalAgent" embedding API vector reranking product`

  None returned a product. The closest name match is Ethical Agentic AI Inc. (ethicalagentic.ai), which audits and certifies AI agents and is not an embeddings vendor [A2-S079]. Other hits were unrelated: patents on "ethical walls", and arXiv ethics papers. No company has been invented. The tile is likely spurious, or describes something too small to be indexed.
- **A3 (Ragoos): unresolved, flagged "Not publicly verified".** Searches tried:
  1. `"Ragoos" reranker`
  2. `Ragoos RAG re-ranking startup`
  3. `ragoos.com OR ragoos.ai`
  4. `Ragoos` (standard mode; huggingface.co, github.com, pypi.org, producthunt.com, crunchbase.com, linkedin.com)
  5. `"Ragoos" AI OR RAG OR retrieval OR rerank`
  6. The graphic-title query in A2, item 5

  Hits were unrelated:
  - Ragoos pizza restaurant, Bengaluru
  - RAGus.ai, a web scraper
  - RaGOO, an unsupported genome tool
  - Ragos, a CNC machinery maker
  - Ragie, a RAG-as-a-service platform with LLM re-ranking [A2-S080]
- **A12 (Cohere Embed v3 + Rerank): resolved, superseded twice.**
  - Embed v4 shipped in 2025. The changelog date conflicts: 15 April 2025 vs a 16 September 2025 heading [A2-S011].
  - Embed 5 shipped on 30 September 2026 as embed-v5.0-pro and embed-v5.0-fast [A2-S012, A2-S013].
  - Rerank went from v3.5 to Rerank 4 (v4.0-pro and v4.0-fast) on 11 December 2025 [A2-S010, A2-S009]. Rerank 3.5 is still offered on Azure [A2-S011].
- **A13 (version labels and Voyage ownership): resolved.**
  - **Voyage:** MongoDB acquisition confirmed. It closed 17 February 2025 and was announced 24 February 2025; consideration was US$160.9M [A2-S033]. "Voyage-3" is stale: Voyage 4 arrived 15 January 2026 [A2-S006, A2-S007, A2-S071] and rerank-3 on 30 September 2026 [A2-S034].
  - **Jina:** "v3" is stale. jina-embeddings-v5-text arrived in February 2026, v5-omni in May 2026 and reranker v3.5 in July 2026. Ownership changed: Elastic acquired Jina in October 2025 [A2-S023, A2-S025, A2-S026].
  - **OpenAI:** "Embeddings 3" is still current [A2-S001].
  - **Gemini:** "Embedding 2" is correct, GA 22 April 2026 [A2-S004].
- **A14 (NVIDIA Embed): resolved.** The tile is NVIDIA NeMo Retriever embedding and reranking NIM microservices.
  - Models: nemotron-3-embed-1b, llama-nemotron-embed-1b-v2 and llama-nemotron-embed-vl-1b-v2; rerankers llama-nemotron-rerank-vl-1b-v2, rerank-1b-v2 and rerank-500m-v2 [A2-S030, A2-S031].
  - Licensing: production needs NVIDIA AI Enterprise [A2-S040, A2-S041].
  - "NV-Embed" is not the current product name in NVIDIA's docs.
- **A16 (Milvus vs Zilliz): resolved by covering both in record `L6-milvus-zilliz`.**
  - Milvus Lite, Standalone and Distributed are open source (Apache-2.0); Zilliz Cloud is the managed service. Code moves between them with minimal changes [A2-S054].
  - Zilliz maintains PyMilvus [A2-S053].
  - Follow-up: Milvus 3.0 GA 29 July 2026 (Apache-2.0, lake-native) [A2-S117, A2-S118]; Zilliz Cloud uses Milvus 3.0 as its engine ("Vector Lakebase"; 3.0 in Private Review for on-demand compute), with Serverless, Dedicated and BYOC tiers, SOC 2 Type II and ISO 27001 [A2-S118, A2-S119, A2-S120].

## (c) Hypothesis evidence (no verdicts)

### H5: is "vector database" still the right abstraction?

**Hybrid and full-text search in "vector" stores**
- turbopuffer's API ranks by ANN vector and by BM25 full-text, with filters [A2-S056].
- Chroma Cloud "powers serverless vector, hybrid, and full-text search" [A2-S060].
- Milvus Lite includes BM25 full-text search [A2-S054]; Milvus 2.6 sped up BM25 and 3.0 rebuilt sparse indexing (SINDI) [A2-S117].
- Qdrant 1.17 added weighted RRF [A2-S103]; Elasticsearch 9.x combines RRF and linear retrievers with BBQ-quantised vectors [A2-S133]; MongoDB hybrid search ($rankFusion/$scoreFusion) is GA [A2-S141]; OpenSearch 3.x added hybrid normalisation and RRF [A2-S136]; Pinecone offers sparse + dense "cascading retrieval" [A2-S101].
- pgvector supports sparse vectors (sparsevec) alongside dense ones [A2-S063].

**Vector features in general-purpose databases**
- PostgreSQL has pgvector, now at 0.8.7 [A2-S061], and extension forks: pgvectorscale (Tiger Data) and VectorChord, the successor to pgvecto.rs [A2-S064, A2-S066].
- MongoDB Search and Vector Search are GA for self-managed Community Edition and Enterprise Advanced (8.2+, SSPL) as well as Atlas [A2-S137].
- Elasticsearch, a search engine, adds vector and hybrid retrieval through hosted inference [A2-S023, A2-S042].

**Vendor repositioning**
- Pinecone now describes itself as "knowledge infrastructure for AI". Its Nexus "knowledge engine for agents" (GA 6 August 2026) compiles data into task-specific artifacts and is queried in KnowQL. It includes field-level access control, citations, PII-aware ingestion and lineage [A2-S073, A2-S074].
- Elastic calls itself "the Search AI Company" [A2-S023].
- Chroma calls itself "open-source data infrastructure for AI" [A2-S060] (homepage title: "open-source search infrastructure for AI" [A2-S131]).
- Milvus 3.0 is marketed as "lake-native" and Zilliz Cloud as a "Vector Lakebase" over object storage and open formats [A2-S118].
- Qdrant frames itself as "composable vector search as core infrastructure" [A2-S107].

**Object-store vectors**
- Amazon S3 Vectors: GA December 2025 as object storage with native vector indexes (2 billion vectors per index, 10,000 indexes per bucket); priced on storage (US$0.06/GB-month), PUTs and per-query data processed [A2-S081, A2-S082, A2-S083, A2-S087]. AWS positions it as a cheap tier that hands hot vectors to OpenSearch, and as a Bedrock Knowledge Bases store [A2-S092, A2-S093, A2-S089]. It has no native BM25 [A2-S083 lists vector/metadata operations only].
- turbopuffer keeps all durable state in object storage with SSD/memory caches (cold p50 874 ms vs cached 14 ms) [A2-S124].
- Milvus 3.0 builds indexes over vectors that stay in object storage/open formats [A2-S118].

**Retrieval quality evidence.** Anthropic's Contextual Retrieval study:
- Combining contextual embeddings with contextual BM25 cut top-20 retrieval failures by 49%.
- Adding a reranker raised the cut to 67%, taking the failure rate from 5.7% to 1.9% [A2-S070]. (Anthropic is the author's parent company; this is a conflict of interest.)

### H6: should embeddings and reranking be one retrieval-optimisation layer?

**Vendors shipping both embed and rerank**
- Cohere: Embed 5 and Rerank 4 [A2-S012, A2-S010].
- Voyage: Voyage 4 and rerank-3 [A2-S006, A2-S034].
- Jina: v5 embeddings and reranker v3.5 [A2-S025, A2-S026].
- NVIDIA: embed and rerank NIMs [A2-S030, A2-S031].
- Qwen: Qwen3-Embedding and Qwen3-Reranker, plus VL variants [A2-S020, A2-S021].
- Sentence Transformers: bi-encoder, cross-encoder, sparse and multi-vector models in one library [A2-S029].
- OpenAI and Google: in this run, only embeddings were evidenced for each [A2-S001, A2-S004].

**Embedding and reranking moving into stores**
- MongoDB: Automated Embedding with Voyage, the Atlas Embedding and Reranking API [A2-S078, A2-S077], and an index-less `$rerank` aggregation stage using Voyage cross-encoders (preview, MongoDB 8.3+) [A2-S141].
- Elastic: Elastic Inference Service serves Jina embeddings next to ELSER, and Elastic acquired Jina's rerankers [A2-S042, A2-S023].
- Pinecone: server-side embedding via `create_for_model` [A2-S051]; hosted rerankers pinecone-rerank-v0, Cohere Rerank 3.5 and bge-reranker-v2-m3, plus sparse model pinecone-sparse-english-v0 [A2-S101].
- Elastic: semantic_text now defaults to Jina v5 embeddings; 9.5 previews a multimodal semantic field on jina-embeddings-v5-omni [A2-S133].
- Qdrant Cloud: server-side inference [A2-S052].

**Late interaction.** Sentence Transformers v6 added a Multi-Vector Encoder for ColBERT-style late interaction [A2-S029, A2-S028]. ColPali-specific evidence was not gathered.

**Contextualised chunk embeddings**
- Voyage's voyage-context-4 [A2-S007].
- Anthropic's contextual-embedding technique [A2-S070].

**Matryoshka and quantisation**
- Gemini Embedding 2: MRL, 128–3,072 dims [A2-S005].
- Cohere Embed 5: 256–2,048 dims, float/int8/binary. Cohere's worked example shows 100M chunks shrinking from about 819 GB to 3.2 GB [A2-S012, A2-S013].
- Voyage 4: binary quantisation options [A2-S006].
- OpenAI: `dimensions` parameter [A2-S001].
- Qwen hosted model: 64–2,048 dims [A2-S022].

**Multimodal embeddings are now mainstream**
- Gemini Embedding 2 (text, image, video, audio, PDF) [A2-S004].
- Jina v5-omni [A2-S025].
- Cohere Embed 5 (text and images) [A2-S012].
- Voyage multimodal-3.5 [A2-S007].
- NVIDIA embed-vl and rerank-vl [A2-S031].
- Qwen3-VL [A2-S021].

**Shared embedding spaces across tiers.** These let a team index with a large model and query with a small one:
- Voyage 4 [A2-S006]
- Cohere Embed 5 Pro/Fast [A2-S012]
- Jina v5-omni text vectors, which match v5-text exactly [A2-S025]

**Benchmarks.** MTEB is still maintained: its results repository was updated on 21 September 2026 [A2-S046]. The live leaderboard (Hugging Face) could not be fetched, so no current ranking is asserted. Vendor-reported scores are labelled as such in the records.

## (d) Products the graphic misses

None of the candidates below was added to `products.json`: the search budget ran out before primary sources could be gathered. Each is a candidate for a follow-up pass.

- **L6: Azure AI Search.** Microsoft's managed hybrid (BM25 + vector + semantic ranker) retrieval service; the default for Azure-centred enterprises. Not researched.
- **L6: Vertex AI Vector Search / Agent Retrieval (Google).** Google docs now include an "Agent Retrieval" vector-search-2 section with automatic embedding generation. It appeared only as a URL in a search result list (docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/embeddings/autogenerating-embeddings, seen in the search behind A2-S038). Not researched.
- **L6: OpenSearch (incl. Amazon OpenSearch Service).** The fork alternative to Elasticsearch, noted in `L6-elasticsearch`. OpenSearch 3.9.0 released 29 September 2026; hybrid/RRF, quantisation and a 2026 roadmap for composable reranking pipelines [A2-S136]; S3 Vectors integration [A2-S093]. Not given its own record (kept inside L6-elasticsearch).
- **L6: Oracle AI Vector Search / SQL Server vector type.** General-purpose databases with vector support, relevant to H5. Not researched.
- **L7: Amazon Bedrock embeddings and Rerank API.** AWS-native embed and rerank. A Bedrock Rerank API announcement (December 2024) appeared in a search result list only. Not researched.
- **L7: Google Vertex AI ranking API.** Google's reranker, which would complete the Gemini embed-plus-rerank pairing. Not researched.
- **L7: Mixedbread and ZeroEntropy.** Independent embedding and reranker vendors. ZeroEntropy appeared in a directory listing during the Ragoos searches. Not researched.

## (e) Gaps: what could not be verified, and why

The first pass exhausted the shared web-search budget. The follow-up pass on 7 October 2026 closed most L6 gaps. These items remain open:

1. **S3 Vectors.** HIPAA eligibility and certification scope of S3 Vectors specifically. CloudTrail data-event coverage. Exact region list (count approximate, ~34). Non-US-region price variation.
2. **Pinecone.** CMEK cloud coverage beyond AWS. The pricing-page snapshot may be stale (the storage rate conflicts: US$0.33 vs US$0.25/GB import). Frankfurt region launch date.
3. **Qdrant.** ISO 27001 (not found). SSO/RBAC for Qdrant Cloud. Current managed pricing (structured-data figures only).
4. **Weaviate.** Whether the Enterprise Edition licence PR is merged and shipped in a stable release; no official announcement found. Whether BYOC is in certification scope. Tier naming/pricing conflicts. 2025–2026 funding.
5. **Milvus/Zilliz.** Zilliz Dedicated price per unit (captured figure anomalous). BYOC pricing. Zilliz Cloud 2.6 GA date conflict.
6. **turbopuffer.** Region list. Funding amounts; revenue is from an aggregator only.
7. **Chroma.** CMEK details (changelog title only). Reason for no PyPI release since May 2026.
8. **Elasticsearch.** Which Elastic Cloud subscription includes SSO/audit logging (self-managed: Platinum). Cluster pricing.
9. **MongoDB.** GA date of self-managed Search (inferred c. July 2026 from page age). GA status of EU Geography (preview at launch; later roundup says GA). rerank-3 support in `$rerank` docs. Search Node price tables conflict.
10. **pgvector.** Extension licence. The CVE number in 0.8.7 (CVE-2026-103484) looks unusual. Managed-Postgres host features. pgvectorscale latest version (last seen 0.6, March 2025).
11. **L7 enterprise controls.**
    - Cohere SSO/SAML and audit-log export (not found).
    - Voyage/Atlas API SOC 2 report scope; MongoDB points to a separate VoyageAI Trust Portal.
    - CMK for hosted embedding APIs (none found for OpenAI, Cohere or Voyage).
    - Jina API SOC 2 scope.
    - Qwen-hosted EU region.
12. **Prices not found.** Cohere Rerank per-search price and Jina API per-token price.
13. **Benchmarks.** Live MTEB leaderboard blocked; no current rank asserted.
14. **Missing-product candidates.** Azure AI Search, Vertex AI Vector Search/Agent Retrieval, Oracle/SQL Server vectors, Bedrock embeddings/Rerank, Vertex ranking API and Mixedbread/ZeroEntropy were not researched.
15. **Conflict of interest.** Anthropic (the author's parent) is a named turbopuffer customer [A2-S126] and authored A2-S070 and A2-S071.
