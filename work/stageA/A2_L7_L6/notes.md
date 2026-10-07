# Stage A notes: stream A2 (L7 Embeddings and reranking; L6 Vector and retrieval stores)

As of 7 October 2026. All facts carry source IDs from `sources.csv`; archive under `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A2/`.

**Research-coverage warning.** The web-search budget, which all Stage A agents share, ran out partway through this stream, while L6 (Pinecone) was being researched. Vendor domains are blocked by the egress policy: pinecone.io, qdrant.tech, milvus.io, zilliz.com, weaviate.io, turbopuffer.com, elastic.co, mongodb.com, trychroma.com, aws.amazon.com, postgresql.org, sec.gov, wikipedia and huggingface.co were each tried once and were all refused. As a result:

- **L7** is researched in full.
- **L6** rests on the searches completed before the cut-off (pgvector, pgvectorscale/VectorChord, Pinecone, Elastic trust centre, MongoDB/Voyage) and on PyPI pages for client SDKs.
- **Amazon S3 Vectors** was not researched at all.

Fields marked `Not publicly verified` in L6 mostly mean *not researched*, not *absent*. Stage B must not score them as gaps without a follow-up pass. Source IDs A2-S048 and A2-S049 are not allocated (numbering gap only).

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
| Pinecone – managed | Still managed, now with BYOC (AWS/GCP/Azure) and Dedicated Read Nodes (GA April 2026). Repositioned as "knowledge infrastructure", with Nexus "knowledge engine for agents" GA 6 August 2026. New CEO in September 2025. SDK v10 (September 2026). | Mispositioned (descriptor understates BYOC/Nexus) | A2-S069, A2-S072, A2-S073, A2-S068, A2-S051 |
| Qdrant – open source | Client 1.19.1 (16 September 2026). Qdrant Cloud adds server-side inference on paid plans. Server facts were not researched. | No change (limited evidence) | A2-S052 |
| Milvus – vector search | Covers both open-source Milvus and Zilliz Cloud. PyMilvus 3.0.2 (September 2026); Milvus Lite 3.2.1 has been rebuilt with BM25. Server version unverified. | No change (limited evidence) | A2-S053, A2-S054 |
| Weaviate – open source | Client 4.23.1 (7 September 2026). Nothing else was verified. | Not publicly verified (not researched) | A2-S055 |
| turbopuffer – cloud vector store | Active SDK (2.11.0, 7 October 2026). The API offers ANN vector **and BM25 full-text** ranking. | No change (descriptor understates full-text) | A2-S056 |
| Elasticsearch – hybrid search | Elastic, "the Search AI Company", acquired Jina AI and serves Jina models on Elastic Inference Service next to ELSER. Server is 9.x (inferred from the client). OpenSearch is the fork alternative. | No change | A2-S023, A2-S042, A2-S057, A2-S058, A2-S045 |
| MongoDB – Atlas vector | Vector Search now ships with Voyage embedding and reranking built in: Automated Embedding is in public preview on Community Edition, and the Atlas Embedding and Reranking API is in public preview. | No change (scope widened) | A2-S078, A2-S077, A2-S008 |
| Chroma – open source | chromadb 1.5.9 (5 May 2026), Apache-2.0. Chroma Cloud offers serverless vector, hybrid and full-text search. Chroma describes itself as "open-source data infrastructure for AI". | No change | A2-S060 |
| S3 Vectors – AWS | Not researched (search budget exhausted; AWS domains blocked). | Not publicly verified | — |

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
  - Zilliz Cloud commercial details are not verified.

## (c) Hypothesis evidence (no verdicts)

### H5: is "vector database" still the right abstraction?

**Hybrid and full-text search in "vector" stores**
- turbopuffer's API ranks by ANN vector and by BM25 full-text, with filters [A2-S056].
- Chroma Cloud "powers serverless vector, hybrid, and full-text search" [A2-S060].
- Milvus Lite includes BM25 full-text search [A2-S054].
- pgvector supports sparse vectors (sparsevec) alongside dense ones [A2-S063].

**Vector features in general-purpose databases**
- PostgreSQL has pgvector, now at 0.8.7 [A2-S061], and extension forks: pgvectorscale (Tiger Data) and VectorChord, the successor to pgvecto.rs [A2-S064, A2-S066].
- MongoDB Vector Search runs on Atlas and on Community Edition [A2-S078].
- Elasticsearch, a search engine, adds vector and hybrid retrieval through hosted inference [A2-S023, A2-S042].

**Vendor repositioning**
- Pinecone now describes itself as "knowledge infrastructure for AI". Its Nexus "knowledge engine for agents" (GA 6 August 2026) compiles data into task-specific artifacts and is queried in KnowQL. It includes field-level access control, citations, PII-aware ingestion and lineage [A2-S073, A2-S074].
- Elastic calls itself "the Search AI Company" [A2-S023].
- Chroma calls itself "open-source data infrastructure for AI" [A2-S060].

**Object-store vectors.** Amazon S3 Vectors was not researched this run. This is a gap.

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
- MongoDB: Automated Embedding with Voyage, and the Atlas Embedding and Reranking API [A2-S078, A2-S077]. A native reranking and hybrid search announcement was seen by title only [A2-S078].
- Elastic: Elastic Inference Service serves Jina embeddings next to ELSER, and Elastic acquired Jina's rerankers [A2-S042, A2-S023].
- Pinecone: server-side embedding via `create_for_model` [A2-S051]. Pinecone hosted rerank models were not verified this run.
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
- **L6: OpenSearch (incl. Amazon OpenSearch Service).** The fork alternative to Elasticsearch, noted in `L6-elasticsearch`. opensearch-py 3.2.0 (27 April 2026, Apache-2.0) [A2-S058]. Server facts not researched.
- **L6: Oracle AI Vector Search / SQL Server vector type.** General-purpose databases with vector support, relevant to H5. Not researched.
- **L7: Amazon Bedrock embeddings and Rerank API.** AWS-native embed and rerank. A Bedrock Rerank API announcement (December 2024) appeared in a search result list only. Not researched.
- **L7: Google Vertex AI ranking API.** Google's reranker, which would complete the Gemini embed-plus-rerank pairing. Not researched.
- **L7: Mixedbread and ZeroEntropy.** Independent embedding and reranker vendors. ZeroEntropy appeared in a directory listing during the Ragoos searches. Not researched.

## (e) Gaps: what could not be verified, and why

1. **Shared web-search budget exhausted (200 calls per turn across all agents).** Hit while researching Pinecone. Everything below in this list follows from that, because no further searches were possible.
2. **Amazon S3 Vectors.** Entirely unresearched: GA status, limits, pricing, regions. Highest-priority follow-up.
3. **Qdrant, Weaviate, Milvus/Zilliz, turbopuffer, Chroma.** Server versions and server licences (Qdrant, Weaviate), managed-cloud pricing, BYOC/hybrid offerings, SOC 2/ISO/HIPAA, EU regions, SSO/RBAC/audit logs, CMK, and 2025–2026 funding are unverified. Only PyPI client facts are verified.
4. **Pinecone.** Price list (beyond the US$20/month Builder tier), certifications, CMK, SSO/RBAC/audit logs and built-in reranking are not verified. The Frankfurt region is known from a headline only.
5. **Elasticsearch.** Server version (inferred 9.x from the client) and licence (Elastic License/SSPL/AGPL options) not verified. Cluster pricing not verified.
6. **MongoDB Vector Search.** Certifications, pricing, GA status of self-managed vector search, and the content of the "native reranking and hybrid search" announcement are not verified.
7. **pgvector.** Extension licence not verified this run, and the CVE number in 0.8.7 (CVE-2026-103484) looks unusual. pgvectorscale's latest version was not found (last seen 0.6, March 2025).
8. **L7 enterprise controls.** Not found for:
   - SSO/RBAC/audit logs for Voyage, Cohere and Jina
   - HIPAA BAAs for Cohere and Voyage
   - EU residency for Voyage, Cohere-hosted and Qwen-hosted endpoints
   - CMK for any embedding API
   - Whether OpenAI's EU residency covers `/embeddings`
   - Whether the hosted Jina API is in Elastic's SOC 2 scope
9. **Prices not found:** Cohere Rerank per-search price and Jina API per-token price.
10. **Benchmarks.** The live MTEB leaderboard (huggingface.co) is blocked, so no current rank is asserted.
11. **Direct fetch blocked.** All vendor domains except pypi.org, cloud.google.com/blog, anthropic.com and docs.claude.com are blocked by policy. Primary sources were therefore read through search-tool extracts, which caps confidence at `medium` unless a second source agrees.
