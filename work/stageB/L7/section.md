## 7. Embeddings and reranking

> **Executive summary.** This layer turns text, and now images, audio and PDF pages, into vectors that a retrieval store can search. It then reorders the candidates so that the few passages handed to the model are the right ones. Three things have changed since the original graphic. First, every model vendor in this layer except OpenAI now offers both an embedding model and a reranker: Cohere, Voyage, Jina, NVIDIA and Qwen ship them together, and Google offers a separate Vertex ranking API [VF: A2-S012, A2-S010, A2-S006, A2-S034, A2-S025, A2-S026, A2-S030, A2-S031, A2-S020, B-REV-S026]. Second, two of the graphic's vendors now belong to database companies: Voyage AI to MongoDB since 17 February 2025 [VF: A2-S033, V1-S023], and Jina AI to Elastic since 9 October 2025 [VF: A2-S023, V1-S025]. Third, the stores themselves now host embedding and reranking [VF: A2-S101, A2-S141, A2-S133]. The architectural point that matters most is this: the embedding model version is production configuration, because changing it forces the whole corpus to be re-embedded [AJ]. **Recommendation:** build one governed retrieval-optimisation service that pins the embedding and reranker versions, keeps raw text and model-version metadata, and migrates by dual index. Choose the models by in-domain evaluation. For regulated data, prefer options that run in your own estate or in a verified region [Rec].

### 7.1 Responsibility

**The problem this layer owns** [AJ]:
- **Representation.** Encoding chunks and queries into a vector space in which "similar meaning" means "near". This covers dense vectors and, increasingly, sparse and multi-vector forms.
- **Precision at the top.** Reordering the first-stage candidates with a more expensive model (a cross-encoder or listwise reranker) so that the top 5–10 results are correct.
- **Version discipline.** Making sure every vector in an index came from one known model version with one known configuration (dimensions, quantisation, instructions).

**Hand-offs** [AJ]:

| Direction | Layer | What crosses the boundary |
|---|---|---|
| Below (input) | L8 ingestion | Clean chunks with lineage, classification and access-control metadata. L7 never decides who may see a chunk. |
| Beside | L6 stores | Vectors, sparse terms and metadata are written to the store. At query time the store does filtered first-stage retrieval and fusion. |
| Above | L3 orchestration, L1 models | A short, ranked, entitlement-filtered context list with scores and document identifiers. |
| Across | L9, C5, C8 | Retrieval metrics feed L9. Model and version identifiers are C5 configuration. Retrieved document IDs and scores go into the C8 evidence pack. |

**A boundary that has moved.** The reranker is no longer always an L7 service. MongoDB runs Voyage cross-encoders inside an aggregation stage (`$rerank`, public preview, 8.3+) [VF: A2-S141]. Pinecone hosts its own reranker, Cohere Rerank 3.5 and bge-reranker-v2-m3 [VF: A2-S101]. Elastic's `semantic_text` field embeds automatically and defaults to Jina v5 [VF: A2-S133]. The responsibility still belongs to L7 even when the compute runs in L6: someone must own the model choice, the version pin and the evaluation [AJ].

### 7.2 Why it matters

**What breaks when this layer is badly designed** [AJ]:

- **Silent relevance decay.** The system still returns something, so nobody notices it is wrong.
- **Mixed-version indexes.** Scores from two model versions are not comparable; quality drops without an error.
- **Unplanned re-embedding.** A model is retired or replaced and the corpus must be re-processed under time pressure.
- **Entitlement leakage through ranking.** A reranker will promote another client's document if unfiltered candidates reach it.
- **Cost surprises.** Full-precision 3,072-dimension vectors held in memory across a large corpus. Cohere's own worked example shows 100M chunks shrinking from about 819 GB to 3.2 GB once reduced dimensions and binary output are used [VF: A2-S013].

**Illustrative scenario [AJ].** A platform team upgrades its embedding model on a Friday, applying the new model to the ingestion pipeline and to the query path. Nobody re-embeds the existing 4 million chunks. New documents land in the new vector space; old documents remain in the old one. Queries are now embedded with the new model and compared against mostly old vectors. Nothing errors. Over the next fortnight the commentary assistant starts citing last month's market notes and missing the house style guide, which has not changed since the spring. The defect is found only when an analyst asks why the draft quotes a superseded style rule. Nothing records which model produced which vectors, so the team cannot tell which documents are affected and has to rebuild the whole index. The controls that would have stopped it are a model-version tag on every vector, a query path that refuses to mix versions, and a retrieval regression suite in L9 run on every configuration change.

### 7.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Recall@k (first stage) | Share of golden-set queries whose relevant chunk appears in the top k candidates (k = 50–100) | ≥ 0.95 on the in-domain golden set | L9 offline evaluation on a labelled query set, on every model or config change |
| nDCG@10 / precision@5 (after rerank) | Ranking quality of the final context list | Agreed baseline; no regression > 2 points on release | Same golden set, graded relevance labels |
| Entitlement-violation rate | Retrieved items the requester is not entitled to see | 0, as a hard gate | Synthetic cross-tenant probe queries in CI and production canaries |
| Version consistency | Share of vectors in a live index carrying the index's declared model-version tag | 100% | Index metadata audit job |
| p95 query-embedding latency | Time to embed one query | < 100 ms in-region | Gateway or service traces (OTel spans) |
| p95 rerank latency | Time to rerank the candidate set | < 300 ms for 50 candidates | Service traces; alert on breach |
| Cost per 1,000 queries | Embedding plus rerank cost | Tracked and budgeted per use case | C6 FinOps attribution |
| Full re-embed time | Wall-clock time to re-embed the corpus into a shadow index | Inside the agreed change window; tested twice a year | Dry-run migration |
| Multilingual parity gap | Recall gap between English and other in-scope languages | ≤ 5 points | Golden set stratified by language |

The targets are starting points for a firm to calibrate. They are not industry benchmarks [AJ].

### 7.4 How it works

**Two paths share one model configuration.** At ingestion, each chunk is embedded (dense) and, where used, encoded as sparse terms. Both are written to the store with metadata: source, classification, entitlements, model version and chunk hash. At query time the query is embedded with the same model version. The store runs a filtered dense search and a lexical (BM25) or sparse search, fuses the two lists, and passes the top candidates to a reranker that reads query and passage together [AJ].

```text
INGESTION (L8 -> L7 -> L6)
 chunk + lineage + ACL metadata
   -> embedding service [model=X, version=v3, dims=1024, quant=int8]
   -> dense vector + sparse terms + {model_version, chunk_hash, acl, fund_id}
   -> store index "commentary_v3"          (raw text retained)
QUERY (L3 -> L7/L6 -> L3)
 query + caller identity
   -> embed query with SAME model_version as target index
   -> L6: entitlement filter FIRST (acl, fund_id, client_id)
        -> dense ANN top-100  +  BM25/sparse top-100
        -> fuse (RRF or weighted)
   -> reranker [model=R, version=r2] on top-50 (already filtered)
   -> top-5..10 with doc_id, scores, versions  -> L3 / L1
   -> trace to L9 and the C8 evidence pack
```

**The mechanics that matter for decisions:**

- **Bi-encoder vs cross-encoder.** An embedding model encodes query and document separately, so documents can be pre-computed. That is fast, but it is coarse [AJ]. A reranker reads the query and each candidate together. That is slower, but more precise, which is why it is applied only to a short candidate list [AJ]. Current rerankers take long inputs: Cohere Rerank 4 handles 32K tokens and JSON documents [VF: A2-S009], and Voyage rerank-3 has a 32K-token context [VF: A2-S034]. Jina reranker v3.5 is listwise, scoring candidates jointly [VF: A2-S026].
- **Sparse plus dense.** Lexical matching catches exact identifiers that dense vectors blur: fund codes, ISINs, share-class names [AJ]. Fusion is now a store feature: Qdrant weighted RRF [VF: A2-S103], Elasticsearch RRF and linear retrievers [VF: A2-S133], MongoDB `$rankFusion`/`$scoreFusion` [VF: A2-S141], Pinecone "cascading retrieval" [VF: A2-S101] and pgvector `sparsevec` [VF: A2-S063]. Sentence Transformers trains Sparse Encoders [VF: A2-S029].
- **Evidence for the two-stage pattern.** Anthropic reports that contextual embeddings plus contextual BM25 cut top-20 retrieval failures by 49%, and that adding a reranker raised the cut to 67% [R: A2-S070]. The author is an Anthropic model, so this is one vendor's measurement on its own data. It shows direction, not a decision input [AJ].
- **Matryoshka dimensions and quantisation.** Several models let you truncate vectors and lower precision with a controlled loss:
  - Gemini Embedding 2: 128–3,072 dims [VF: A2-S005]
  - Cohere Embed 5: 256–2,048 dims; float, int8 and binary [VF: A2-S012]
  - voyage-4: 256–2,048 dims, with binary among its quantisation options [VF: A2-S007, A2-S006]
  - Qwen's hosted model: 64–2,048 dims [VF: A2-S022]
  - OpenAI: a `dimensions` parameter [VF: A2-S001]

  Stores quantise as well: Elasticsearch uses BBQ quantisation by default since 9.1 [VF: A2-S133]. Dimension and precision are therefore index-design parameters, and they must be recorded with the model version [AJ].
- **Shared embedding spaces.** Voyage 4 [VF: A2-S006], Cohere Embed 5 Pro/Fast [VF: A2-S012] and Jina v5-omni and v5-text [VF: A2-S025] put several model sizes in one space. You can index with the large model and query with the small one. This reduces re-embedding inside a family; it does nothing for a move between vendors [AJ].
- **Contextualised chunks and late interaction.** voyage-context-4 embeds a chunk with awareness of its surrounding document [VF: A2-S007]. Sentence Transformers v6 added a Multi-Vector Encoder for ColBERT-style late interaction [VF: A2-S029, A2-S028]. ColPali-style page-image retrieval was not evidenced in this research [NPV].
- **Multimodal.** Gemini Embedding 2 [VF: A2-S004], Jina v5-omni [VF: A2-S025], Cohere Embed 5 [VF: A2-S012], voyage-multimodal-3.5 [VF: A2-S007], NVIDIA VL models [VF: A2-S031] and Qwen3-VL [VF: A2-S021] embed images alongside text. This matters for scanned factsheets and charts; text-first corpora gain little [AJ].
- **Benchmarks.** The MTEB results repository was still maintained on 21 September 2026 [VF: A2-S046]. The live leaderboard could not be fetched, so this section asserts no current ranking [NPV]. Vendor scores quoted anywhere in this section are [R] and are not decision inputs.

### 7.5 Enterprise design principles

**Security** [AJ]
- Embeddings derived from client or personal data are a derivative of that data. Classify, retain and delete them with the source.
- Enforce entitlements in the store's pre-filter, before ANN search, fusion and reranking. Never post-filter after the reranker, and never rely on the reranker to "down-rank" forbidden content.
- The operative reference is the OWASP Top 10 for LLM Applications 2026 [VF: A8-S041]. Its full contents were not retrieved, so its identifier for this risk is not given [NPV]. For traceability, the 2025 list named it LLM08 "Vector and Embedding Weaknesses" [R: A8-S040].

**Scalability and cost** [AJ]
- Choose dimensions and quantisation per index tier, by measurement.
- Batch ingestion through Batch APIs where offered. OpenAI's Batch API halves the 3-large price, and Gemini's Batch is 50% of standard [VF: A2-S035, A2-S005].
- Cap the rerank candidate count (typically 25–100) and measure the recall it buys.

**Resilience** [AJ]
- Hosted embedding APIs are on the query path. An outage stops retrieval even if the store is healthy.
- Keep a warm fallback route for the same model, such as a second region or a marketplace deployment, or degrade to lexical search.
- Never fall back to a *different* embedding model against the same index.

**Governance and change** [Rec]
- Treat `{embedding model, version, dims, quantisation, instruction prefix}` and `{reranker model, version, candidate k}` as versioned C5 configuration, promoted through environments with an L9 regression gate.
- Write the configuration hash into every vector's metadata and every trace.

**Observability** [Rec]
- Emit spans for embed, retrieval, fusion and rerank with model version, latency and top document IDs.

**Portability** [Rec]
- Always store the raw chunk text and its hash next to the vector, so you can re-embed without re-parsing.
- Put an internal embedding-service interface in front of every provider.

**Patterns**

| Pattern | Use |
|---|---|
| Dual-index migration (blue/green) [Rec] | Build `index_v4` in shadow from stored raw text. Run both, compare on the golden set and on shadow traffic, switch the read alias, keep `index_v3` until the rollback window closes. |
| Hybrid first stage + cross-encoder rerank [Rec] | Default for enterprise text. Lexical catches identifiers; dense catches paraphrase; the reranker fixes the order. |
| Index-large / query-small in a shared space [AJ] | Cuts query latency and cost within one vendor family. |
| Domain fine-tune of an open model [AJ] | Use Sentence Transformers to adapt an Apache-2.0 model on in-domain pairs when vendor models underperform on house vocabulary [VF: A2-S029]. |

**Anti-patterns** [AJ]
- Mixing model versions in one index.
- Selecting a model from a leaderboard instead of an in-domain test.
- Post-rerank entitlement filtering.
- Letting a store auto-embed with a default model nobody pinned.
- Discarding raw text after embedding.
- Treating rerank scores as calibrated probabilities across queries.

**What re-embedding actually costs.** The API bill is the small part. A corpus of 2 million chunks at about 500 tokens each is roughly 1 billion tokens. At list prices as of 7 October 2026 that is about US$130 with OpenAI text-embedding-3-large, about US$60 with voyage-4, or about US$120 with Cohere Embed 5 Pro [VF: A2-S001, A2-S007, A2-S013]. The arithmetic is the author's own [AJ]. The real costs are elsewhere [AJ]:
- running a second index in parallel
- re-running the retrieval evaluation and any downstream answer-quality evaluation
- revalidation and change-control evidence
- the migration window

This is why model version belongs in production configuration and in the exit plan.

### 7.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical capability | Recall and nDCG on **your** golden set, in your languages and document types; reranker availability; Matryoshka and quantisation; context length; sparse, multi-vector and multimodal support; domain models |
| Enterprise readiness | SSO, RBAC and audit logs for the console and API keys; per-project keys; usage reporting; support and model-retirement notice periods (ask for them in writing) |
| Security and compliance | SOC 2 Type II and ISO 27001 scope covering the **embedding endpoint**; ZDR; CMK; DPA; sub-processors |
| Deployment flexibility | In-region processing (UK and EU separately); VPC or marketplace deployment; self-hosting and air-gap |
| Ecosystem | Native support in your L6 store; Sentence Transformers or vLLM compatibility for open models; marketplace availability |
| Reliability and maturity | GA vs preview status; deprecation policy; model-retirement history; ownership stability |
| Cost / TCO | Per-token price, Batch discount, rerank pricing basis (per search or per token), GPU and licence cost if self-hosted, storage effect of dimensions |
| Lock-in / portability | Weights availability and licence; shared-space families; store bundling; re-embedding cost |

**Enterprise controls for hosted embedding APIs are unevenly documented.** The CP2 review found SSO, RBAC and audit-log documentation for the OpenAI API platform [VF: B-REV-S004, B-REV-S005, B-REV-S006], IAM and audit logging on Google Cloud [VF: B-REV-S007, B-REV-S008], and SSO and RBAC on Elastic Cloud for the Elastic Inference Service route [VF: B-REV-S019]. Cohere documents only Owner and User team roles for its hosted platform [VF: B-REV-S013], and Voyage's Atlas API is accessed by model API keys [VF: B-REV-S018], which Atlas organisation and project roles govern [VF: B-REV-S028]. Under the user's CP2 answers, any one verified control lifts the NPV cap to 3 (rule 7), and services consumed through AWS, Azure or Google Cloud inherit the platform's IAM, SSO and audit logging as presumed, scoring 4 (rule 6). On that basis Gemini Embedding scores 4 through Vertex AI, Cohere 4 through Microsoft Foundry or SageMaker (3 on its direct API), and Voyage 3 on Atlas [AJ]. These controls usually come from the platform account already contracted for L1, so verify them per endpoint in due diligence; platform controls presumed (CP2 Q1); confirm per service [Rec].

### 7.7 Product deep dives

Each deep dive gives the current state as tagged facts, then judgement. Totals are FS-weighted.

**OpenAI embeddings: text-embedding-3-large / -3-small (OpenAI).**
- *What it is now:* OpenAI's embeddings are still the text-embedding-3 generation, released 25 January 2024; no newer model was found as of 7 October 2026 [VF: A2-S001, A2-S002]. 3-large defaults to 3,072 dimensions, can be shortened with `dimensions`, and accepts 8,192 tokens [VF: A2-S001, A2-S003]. Prices are US$0.13 per 1M tokens for 3-large (US$0.065 on Batch) and US$0.02 for 3-small [VF: A2-S001, A2-S035]. No OpenAI reranker was found [VF: A2-S001].
- *Residency and certifications:* the endpoint is ZDR-eligible and in scope for EU storage and processing, which requires Modified Abuse Monitoring or ZDR; the UK is storage-only [VF: A2-S144]. Certifications include SOC 2 Type 2, ISO/IEC 27001 and 27701, and a HIPAA BAA [VF: A2-S036, A2-S144].
- *Access control:* the API platform documents SAML/OIDC SSO, SCIM, organisation and project roles with custom roles, an Admin API and audit logs of administrative events [VF: B-REV-S004, B-REV-S005, B-REV-S006].
- *Strengths:* a stable, cheap, well-controlled text baseline [AJ].
- *Limitations:* it is text-only, hosted-only and has no reranker. The generation is ageing, and its successor's timing is unknown [AJ]. Audit logs exclude request content and are kept on a best-effort basis [VF: B-REV-S006], so they must be exported to the firm's archive [Rec].
- *Choose when:* OpenAI is already the approved L1 provider and EU processing under ZDR suffices [AJ].
- *Avoid when:* UK processing or self-hosting is required [AJ].
- *Competitors:* Gemini Embedding, Cohere, Voyage.
- *FS note:* exit means re-embedding everything [AJ].
- **Tier: Tactical. Flag: none.** FS 3.20.

**Gemini Embedding 2 (Google).**
- *What it is now:* gemini-embedding-2 went GA on 22 April 2026 [VF: A2-S004]. It maps text, images, video, audio and PDFs into one space across 100+ languages, with Matryoshka output from 128 to 3,072 dims [VF: A2-S004, A2-S005]. It runs on the Gemini API and on Vertex AI, now documented as Gemini Enterprise Agent Platform, with global, us and eu endpoints [VF: A2-S039]. The eu multi-region excludes the UK and Switzerland [VF: A2-S039]. Text costs US$0.20 per 1M tokens online and US$0.10 on Batch (as of 7 October 2026) [VF: A2-S038].
- *Certifications:* Generative AI on Vertex AI holds SOC 2, ISO/IEC 27001, ISO/IEC 42001, HIPAA and FedRAMP High, but per-model coverage is not confirmed [VF: A2-S043]. Under CP2 rule 8 that scores security 4, not 5 [AJ].
- *Access control:* access runs through Google Cloud IAM (predefined, custom and endpoint-level roles) and Cloud Audit Logs, where Data Access logs for predict calls must be switched on [VF: B-REV-S007, B-REV-S008]. Under the CP2 hyperscaler presumption (rule 6), enterprise readiness scores 4 [AJ]; platform controls presumed (CP2 Q1); confirm per service [Rec].
- *Strengths:* a natively multimodal option with strong platform certifications [AJ].
- *Limitations:* it is hosted-only and has been GA for under six months. The `task_type` parameter is unsupported [VF: A2-S005]. Google's reranker is a separate service, the Vertex ranking API (semantic-ranker models, with version 005 in preview from 1 September 2026) [VF: B-REV-S026].
- *Choose when:* the estate is Google Cloud-centred and the content is multimodal [AJ].
- *Avoid when:* UK-only processing is mandatory [AJ].
- *Competitors:* Cohere, Voyage, Jina.
- *FS note:* Google Cloud EMEA Limited is a designated DORA CTPP and UK CTP [VF: A8-S020, A8-S023]. Consuming the model through Vertex AI therefore places it with a designated provider, but the firm's own SYSC 8 or SS2/21 duties remain [AJ].
- **Tier: Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10) [AJ]. Flag: none.** FS 3.20. It is Google's lead embedding model, consumed through Vertex AI; the condition excludes estates where UK-only processing is mandatory, because the eu multi-region excludes the UK [VF: A2-S039]. Deployment and lock-in at 2 are accepted under rule 11 because the condition is an existing platform commitment, and the dual-index migration route in this section limits the re-embedding cost of exit [AJ].

**Voyage AI (MongoDB, Inc.).**
- *What it is now:* MongoDB acquired Voyage AI, closing on 17 February 2025 for US$160.9M [VF: A2-S033, V1-S023]. The Voyage 4 family launched on 15 January 2026 in one shared embedding space; voyage-4-nano is open weights under Apache 2.0 [VF: A2-S006, A2-S071]. Alongside it sit voyage-context-4, voyage-code-4, voyage-multimodal-3.5, and the domain models voyage-finance-2 and voyage-law-2 [VF: A2-S007]. rerank-3 and rerank-3-lite were announced on 30 September 2026 [VF: A2-S034], but MongoDB's lifecycle page lists them as Preview [VF: V1-S024]. voyage-4 costs US$0.06 per 1M tokens, rerank-3 US$0.05 and rerank-3-lite US$0.02 (as of 7 October 2026) [VF: A2-S007, A2-S034]. The Atlas Embedding and Reranking API offers an EEA Geography at a 10% premium [VF: A2-S142].
- *Certifications:* certifications rest on a homepage listing [R: A2-S044]. MongoDB's SOC 2 scope page does not name Voyage and excludes preview features [VF: B-REV-S027].
- *Access control:* on Atlas, model API keys are governed by organisation and project roles: Organization Owner, Project Owner and Project Model Owner can create, edit or delete them, read-only roles can only view them, and an Admin API endpoint manages them [VF: B-REV-S028]. SSO and audit logging of key use are not stated [NPV]. One verified control lifts the enterprise-readiness cap to 3 under CP2 rule 7; the AWS Marketplace in-VPC route [VF: A2-S044] would score 4 under the hyperscaler presumption (rule 6) [AJ].
- *Strengths:* a broad lineup against this layer's questions, including a finance-domain model [AJ].
- *Limitations:* certification scope is unverified, key integrations are in preview, and the roadmap is now coupled to MongoDB [AJ].
- *Choose when:* MongoDB is the store [AJ].
- *Avoid when:* the firm needs the store vendor and the embedding vendor to be different companies [AJ].
- *Competitors:* Cohere, Jina, Qwen3.
- *FS note:* obtain the SOC 2 report before client data flows [Rec].
- **Tier: Tactical. Flag: Acquired.** FS 3.05.

**Cohere Embed 5 and Rerank 4 (Cohere Inc.).**
- *What it is now:* Embed 5 (Pro and Fast, 30 September 2026) embeds text, images and mixed pages into one vector [VF: A2-S012]. It supports 100+ languages and a 128K-token context, with 256–2,048 dims and float, int8 or binary output [VF: A2-S012]. Rerank 4 (11 December 2025) adds a 32K-token context and handles JSON [VF: A2-S010, A2-S009]. Embed 5 Pro costs US$0.12 and Fast US$0.08 per 1M text tokens; the rerank price was not found [VF: A2-S013].
- *Deployment and certifications:* deployment options are SaaS, Microsoft Foundry, SageMaker, VPC, Model Vault single-tenant and on-premises [VF: A2-S012, A2-S015]. Cohere holds SOC 2 Type II, ISO 27001 and ISO 42001 [VF: A2-S014]. Enterprise logs are deleted after 30 days by default, and ZDR is available on request [VF: A2-S145].
- *Access control:* the hosted platform documents only Owner and User team roles [VF: B-REV-S013]; SSO/SAML and audit-log documentation for the hosted API was not found [NPV]. Enterprise readiness is scored on the Microsoft Foundry and SageMaker routes, where the CP2 hyperscaler presumption (rule 6) gives 4; the direct hosted API would score 3 under rule 7 [AJ]. Platform controls presumed (CP2 Q1); confirm per service [Rec].
- *Ownership:* a business combination with Aleph Alpha was signed on 16 September 2026 and is pending regulatory approval [VF: A2-S018, V1-S028].
- *Strengths:* the widest deployment range of the hosted vendors here, from SaaS to on-premises [AJ].
- *Limitations:* access controls on the direct hosted API are unverified, and the ownership event is pending [AJ].
- *Choose when:* embed and rerank must run in your VPC or data centre with vendor support [AJ].
- *Avoid when:* you cannot obtain access-control evidence in due diligence [AJ].
- *Competitors:* Voyage, Jina, NVIDIA.
- *FS note:* Cohere states it has no access to prompts in private or partner deployments [VF: A2-S145]. Record the Aleph Alpha approval as an ownership event in the third-party register [Rec].
- **Tier: Tactical. Flag: none.** FS 3.70 on the Foundry and SageMaker routes. It is a Strategic candidate: the score meets the usual Strategic guide, but the stated condition is not yet met: Strategic once per-service due diligence confirms the Foundry or SageMaker controls (the CP2 Q1 presumption is not that evidence) and the Aleph Alpha combination is recorded as an ownership event [AJ].

**Qwen3-Embedding and Qwen3-Reranker (Alibaba Group).**
- *What it is now:* Qwen3-Embedding and Qwen3-Reranker come in 0.6B, 4B and 8B sizes [VF: A2-S020]. They were released in June 2025 under Apache 2.0, with a 32K context and 119 languages [VF: A2-S020]. Qwen3-VL-Embedding and -Reranker followed in January 2026 [VF: A2-S021, V1-S093]. Hosted versions run on Alibaba Cloud Model Studio, where the regions listed are Singapore, Hong Kong and Beijing; no EU region was verified [VF: A2-S022]. Qwen's June 2025 claim that the 8B model ranked first on MTEB multilingual is vendor-reported and was not re-verified [R: A2-S020].
- *Strengths:* a permissive embed-plus-rerank pair that can run entirely inside the firm's estate [AJ].
- *Limitations:* it is a Chinese-origin model. No support or certifications are verified, and the 8B size needs GPUs [AJ].
- *Choose when:* self-hosting is required and a provenance review approves it [AJ].
- *Avoid when:* policy excludes such weights, or only the hosted API would be used [AJ].
- *Competitors:* Sentence Transformers with other open models, NVIDIA, Jina.
- *FS note:* self-hosted, the weights create no cross-border transfer. The hosted route is not suitable for EU or UK client data on the verified regions [AJ].
- **Tier: Tactical. Flag: none.** FS 3.15. Scored under rubric rule 2 as self-hosted weights, because the hosted route is not recommended [AJ].

**Jina AI (Elastic N.V.).**
- *What it is now:* Elastic completed its acquisition of Jina AI on 9 October 2025 [VF: A2-S023, V1-S025]. The current models are [VF: A2-S025, A2-S026, V1-S026]:
  - jina-embeddings-v5-text (February 2026; 32,768-token context)
  - jina-embeddings-v5-omni (May 2026; text, image, audio, video and PDF, with text vectors identical to v5-text)
  - jina-reranker-v3.5 (July 2026)
- *Licence and routes:* weights are CC-BY-NC-4.0. Commercial use runs through the Jina API, marketplaces, Elastic Inference Service or an on-premises licence, which supports air-gapped Docker [VF: A2-S024, A2-S042, A2-S045]. `semantic_text` defaults to Jina v5 [VF: A2-S133]. API per-token rates were not retrieved [VF: A2-S042].
- *Certifications and access control:* Elastic Cloud holds ISO 27001 and SOC 2 Type II; whether the hosted Jina API is in scope is not confirmed [VF: A2-S045]. Elastic Cloud documents SAML SSO and RBAC at platform level; whether they govern EIS calls specifically is not stated [VF: B-REV-S019].
- *Strengths:* the zero-integration path inside Elasticsearch, with multimodal and air-gap options [AJ].
- *Limitations:* the licence is non-commercial. Pricing is opaque, and the ownership change ties it to Elastic [AJ].
- *Choose when:* Elastic is the store [AJ].
- *Avoid when:* the plan assumes free self-hosting of the weights [AJ].
- *Competitors:* Voyage, Cohere, Qwen3.
- *FS note:* get the licence route confirmed in writing [Rec].
- **Tier: Tactical. Flag: Acquired.** FS 3.15, scored on the Elastic Inference Service route.

**Sentence Transformers (Hugging Face).**
- *What it is now:* sentence-transformers 6.1.0 was released on 18 September 2026 under Apache-2.0 [VF: A2-S029, A2-S032]. It is maintained by Hugging Face and originated at UKP Lab [VF: A2-S028, V1-S092]. It computes and trains [VF: A2-S029]:
  - dense embeddings
  - Cross-Encoder reranker scores
  - Sparse Encoders
  - ColBERT-style Multi-Vector Encoders

  More than 15,000 pre-trained models on Hugging Face load through it [VF: A2-S029].
- *Strengths:* one permissive toolkit for every technique in this layer, and the practical route to domain fine-tuning and to exit from any hosted API [AJ].
- *Limitations:* it is a library, not a model, and it has no verified commercial support [NPV]. It publishes a security policy with private reporting and CVE issuance through GitHub advisories [VF: B-REV-S002]. Each Hub model carries its own licence [AJ].
- *Choose when:* retrieval must run in the firm's estate, or needs fine-tuning [AJ].
- *Avoid when:* there is no team to operate serving [AJ].
- *Competitors:* NVIDIA NeMo Retriever, Qwen3, Cohere private deployment.
- *FS note:* it inherits host controls [AJ].
- **Tier: Strategic. Flag: none.** FS 3.70. Rule 2 caps were applied.

**NVIDIA NeMo Retriever embedding and reranking NIMs (NVIDIA).**
- *What it is now:* the graphic's "NVIDIA – Embed" tile is now the set of NeMo Retriever NIM microservices [VF: A2-S030, A2-S031]:
  - Embedding NIM 2.3, with nemotron-3-embed-1b (added in 2.2) and the llama-nemotron-embed text and VL models [VF: A2-S031, V1-S094]
  - Reranking NIM 2.0.0, with text and multimodal rerankers [VF: A2-S030]
- *Deployment and licensing:* they deploy via Helm or Docker on supported GPUs, in any cloud or data centre [VF: A2-S031, A2-S040]. Production use requires NVIDIA AI Enterprise, from US$4,500 per GPU per year (as of 7 October 2026) [VF: A2-S040]. Model licences vary by model [VF: A2-S041]. The Helm chart warns that a text-only reranker silently degrades multimodal reranking [VF: A2-S031].
- *Strengths:* a supported, self-hosted runtime for embed and rerank [AJ].
- *Limitations:* it deepens GPU-vendor coupling, and per-GPU licences make it expensive at low volume [AJ].
- *Choose when:* the firm already runs NVIDIA AI Enterprise [AJ].
- *Avoid when:* retrieval volume is small [AJ].
- *Competitors:* Sentence Transformers, Qwen3, Cohere private deployment.
- *FS note:* self-hosting keeps the retrieval path in-estate; the AI Enterprise subscription becomes the third-party arrangement to register [AJ].
- **Tier: Tactical. Flag: Renamed.** FS 2.95.

### 7.8 Comparison table

Output of `tools/score.py` (scores 1–5; totals are weighted averages):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7-openai | 3 | 4 | 4 | 2 | 3 | 4 | 4 | 2 | 3.30 | 3.20 | Tactical |
| L7-gemini-embedding | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Strategic |
| L7-voyage | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 2 | 3.40 | 3.05 | Tactical |
| L7-cohere | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3.75 | 3.70 | Tactical |
| L7-qwen3-embedding | 4 | 2 | 2 | 4 | 3 | 3 | 4 | 4 | 3.20 | 3.15 | Tactical |
| L7-jina | 4 | 3 | 3 | 4 | 4 | 3 | 2 | 2 | 3.30 | 3.15 | Tactical |
| L7-sentence-transformers | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 3.80 | 3.70 | Strategic |
| L7-nvidia-nemo-retriever | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 2 | 3.00 | 2.95 | Tactical |
| L7-ethicalagents | – | – | – | – | – | – | – | – | n/a | n/a | not scored |
| L7-ragoos | – | – | – | – | – | – | – | – | n/a | n/a | not scored |

**Reading the scores** [AJ]:
- The hosted vendors spread from 3.05 to 3.70 FS. OpenAI (3.20), Gemini and Jina (3.15, Elastic route) rose at CP2 review once their platform access controls were evidenced. The CP2 rework then applied the user's answers: Gemini rose to 3.20 under the hyperscaler presumption, Cohere to 3.70 on its Foundry and SageMaker routes, and Voyage to 3.05 once Atlas roles over model API keys were verified [VF: B-REV-S028]. No hosted vendor is now capped on enterprise readiness.
- Cohere's 3.70 meets the usual Strategic guide, but it stays Tactical on its stated condition: per-service due diligence must confirm the presumed platform controls, and the Aleph Alpha combination is pending. It is the layer's first upgrade candidate.
- Gemini Embedding (3.20) is Strategic, conditional, "where Google Cloud is your primary cloud" under rubric rule 10 (CP3 Q2), which applies to the lead hyperscaler service in a category with no criterion at 1; its scores are unchanged. Cohere is a multi-cloud vendor, not a hyperscaler-native service, so rule 10 does not apply to it, and it ranks above Gemini on score for any firm that is not Google-centred.
- The spread on security (2 to 4) reflects how well certifications are evidenced, not a judgement of real security posture.
- Voyage's technical lead does not survive the FS weighting until its certification scope is evidenced.
- Qwen3 and NVIDIA are scored as self-hosted software under rule 2, like Sentence Transformers.

**Key facts** (as of 7 October 2026):

| Product | Licence | Deployment | Certifications | EU residency | Ownership status |
|---|---|---|---|---|---|
| OpenAI | Proprietary, hosted only [VF: A2-S001] | SaaS [VF: A2-S001] | SOC 2 Type 2, ISO 27001/27701, HIPAA BAA [VF: A2-S036, A2-S144] | EU storage and processing with MAM or ZDR; UK storage-only [VF: A2-S144] | Unchanged |
| Gemini Embedding 2 | Proprietary, hosted only [VF: A2-S004] | Gemini API, Vertex AI [VF: A2-S039] | Vertex GenAI: SOC 2, ISO 27001, ISO 42001, HIPAA, FedRAMP High; per-model scope unconfirmed [VF: A2-S043] | 'eu' multi-region, excludes UK and CH [VF: A2-S039] | Unchanged (Google) |
| Voyage AI | Proprietary; voyage-4-nano Apache 2.0 [VF: A2-S071] | SaaS, Atlas, AWS/Azure marketplaces, in-VPC SageMaker [VF: A2-S033, A2-S044] | SOC 2, HIPAA listed on homepage [R: A2-S044] | Atlas EEA Geography, +10% [VF: A2-S142] | Acquired by MongoDB, 17 Feb 2025 [VF: A2-S033] |
| Cohere | Proprietary [VF: A2-S015] | SaaS, Foundry, SageMaker, VPC, Model Vault, on-prem [VF: A2-S012, A2-S015] | SOC 2 Type II, ISO 27001, ISO 42001 [VF: A2-S014] | 30-day default deletion, ZDR on request; EU region not verified [VF: A2-S145] | Aleph Alpha combination signed 16 Sep 2026, pending [VF: A2-S018] |
| Qwen3 Embedding/Reranker | Apache 2.0 weights; hosted proprietary [VF: A2-S020] | Self-host; Model Studio [VF: A2-S020, A2-S022] | Not publicly verified [NPV] | No EU hosted region verified; self-host in-estate [VF: A2-S022] | Unchanged (Alibaba) |
| Jina AI | CC-BY-NC-4.0 weights; commercial via Elastic [VF: A2-S024, A2-S042] | API, Elastic Inference Service, on-prem/air-gap [VF: A2-S042] | Elastic Cloud ISO 27001, SOC 2 Type II; Jina API scope unconfirmed [VF: A2-S045] | Region details not verified [VF: A2-S024] | Acquired by Elastic, 9 Oct 2025 [VF: V1-S025] |
| Sentence Transformers | Apache-2.0 [VF: A2-S029] | Self-host, on-prem [VF: A2-S029] | Not applicable (library) [AJ] | In-estate [AJ] | Stewardship moved to Hugging Face [VF: A2-S028] |
| NVIDIA NeMo Retriever | Proprietary container plus per-model licences [VF: A2-S041] | Self-host on supported GPUs; NVIDIA API Catalog for development [VF: A2-S040, A2-S031] | Not applicable to self-hosted containers [AJ] | In-estate [AJ] | Unchanged (NVIDIA) |

### 7.9 Decision tree

```text
START: a corpus to make retrievable (one decision per corpus / index)
1. Does the corpus contain client, personal or confidential data?
   ├─ No  → go to 3 (any approved hosted API is acceptable)
   └─ Yes → 2
2. Where may it be processed?
   ├─ Only inside our estate (or air-gapped)
   │    ├─ Need vendor support?
   │    │    ├─ Yes, NVIDIA AI Enterprise already licensed → NVIDIA NeMo Retriever NIMs
   │    │    ├─ Yes, otherwise → Cohere private / on-prem deployment
   │    │    │                   (or Jina on-prem licence if Elastic is the store)
   │    │    └─ No → Sentence Transformers serving an Apache-2.0 model
   │    │            (Qwen3 only after provenance review; voyage-4-nano is another option)
   ├─ UK processing required
   │    └─ None of the hosted APIs here verified UK processing for embeddings
   │       → treat as "own estate" (above) or a VPC/marketplace deployment in a UK
   │         region (Cohere on SageMaker/Foundry, Voyage on SageMaker); confirm the region
   └─ EU processing acceptable
        ├─ Store is MongoDB → Voyage via Atlas EEA Geography (accept preview status,
        │                    obtain the SOC 2 report)
        ├─ Store is Elasticsearch → Jina via Elastic Inference Service (pin the model)
        ├─ Google-centred estate, multimodal → Gemini Embedding 2 on the 'eu' endpoint
        ├─ OpenAI already approved, text-only → text-embedding-3 on an EU project with ZDR
        └─ Otherwise → Cohere (SaaS with ZDR, or VPC)
3. Do we need a reranker? (almost always yes for precision-critical answers)
   ├─ Same vendor offers one and it passes in-domain eval → use it
   ├─ Embedding vendor has none in the same API (OpenAI; Google's is the Vertex ranking API)
   │    → Cohere Rerank 4, Voyage rerank-3 (Preview), or a self-hosted cross-encoder
   └─ Store hosts it (MongoDB $rerank, Pinecone, Elastic) → acceptable if the
        model version is pinned and logged, and entitlement filtering precedes it
4. Exact identifiers matter (fund codes, ISINs, share classes)?
   └─ Yes → hybrid first stage (BM25/sparse + dense, fused) before rerank
5. Scanned pages, charts or images matter?
   └─ Yes → multimodal model (Gemini Embedding 2, Cohere Embed 5, Jina v5-omni,
            voyage-multimodal-3.5, NVIDIA VL), chosen by in-domain eval
6. Always: pin versions in C5, keep raw text, tag vectors with model_version,
   and migrate by dual index behind an L9 regression gate.
```

### 7.10 Lock-in classification

| Lock-in source | Class | Rationale | Abstraction to use |
|---|---|---|---|
| Reranker choice | **Acceptable** [AJ] | Stateless and applied at query time. Swapping it needs no re-index, only re-evaluation. | Internal `rerank(query, candidates)` interface; reranker version in C5 |
| Embedding model (hosted, proprietary) | **Manageable** [AJ] | Vectors are model-specific, so switching means re-embedding [AJ]. The API bill for that is small; evaluation and revalidation are the real cost (§7.5). | Internal embedding service; raw text stored; `model_version` on every vector; dual-index migration runbook tested twice a year [Rec] |
| Shared-space families (Voyage 4, Cohere Embed 5, Jina v5) | **Manageable** [AJ] | They reduce re-embedding inside the family [VF: A2-S006, A2-S012, A2-S025], but deepen commitment to one vendor. | Same as above; treat the family as one supplier in the exit plan |
| Store-bundled embedding and reranking (MongoDB Automated Embedding and `$rerank`, Elastic `semantic_text`, Pinecone integrated inference) | **Manageable**, becoming **unacceptable** if the model is unpinned or raw text is not retained [AJ] | Store and embedding model then change together, so leaving the store also means re-embedding. MongoDB's native reranking and automated embedding are still preview and do not yet support Geography targeting [VF: A2-S141, A2-S142]. | Pin the model explicitly; retain raw text outside the store; export path tested |
| Non-commercial weights self-hosted without a licence (Jina CC-BY-NC-4.0) | **Unacceptable** [AJ] | Licence breach risk [VF: A2-S024]. | Use the licensed routes, or choose an Apache-2.0 model |
| GPU-vendor runtime (NVIDIA AI Enterprise) | **Manageable** [AJ] | The runtime ties retrieval to the licence [VF: A2-S040]. Open-licensed models can move to another runtime, but per-model licences vary [VF: A2-S041]. | Serve behind the same internal interface; keep a Sentence Transformers or vLLM fallback |

### 7.11 Regulated FS lens (POV 2)

**Model risk.** SR 26-2 superseded SR 11-7 on 17 April 2026, and it expressly excludes generative and agentic AI. Firms are left to govern those under their own frameworks (R-US-MRM) [VF: A8-S001, A8-S002, A8-S003]. PRA SS1/23 is the operative UK anchor where it applies. It covers vendor models and requires a complete inventory that includes AI/ML (R-PRA-SS123) [VF: A8-S008]. For this layer [AJ]:
- Record the embedding model and the reranker in the inventory as components of each GenAI system, not as stand-alone "models".
- Treat a change to either as a material change that triggers the L9 retrieval regression and sign-off.
- Retrieval quality is part of the system's validation evidence. An unvalidated embedding swap is an unvalidated system change.

**EU AI Act.** Annex III high-risk duties apply from 2 December 2027 under Regulation (EU) 2026/1744, and GPAI obligations have been enforceable since 2 August 2026 (R-EUAIA, R-EU-OMNIBUS-AI) [VF: A8-S011, A8-S012]. The worked example is not an Annex III use, and a firm consuming embedding APIs is a deployer [AJ]. Whether any embedding model is itself a GPAI model was not established [NPV]. Article 26 deployer logging folds into financial-services record-keeping (R-EUAIA) [VF: A8-S016]; logging the retrieval step is good practice regardless [AJ].

**DORA, CTP and outsourcing.**

- DORA's first CTPP list (18 November 2025) and the UK's first CTP designations (8 July 2026) cover hyperscalers, but no model vendor (R-DORA, R-UK-CTP) [VF: A8-S020, A8-S021, A8-S023, A8-S024].
- An embedding API consumed through Vertex AI, or a marketplace deployment, therefore sits on a designated provider. A direct Voyage, Cohere, Jina or OpenAI contract does not, which leaves oversight with the firm [AJ].
- Every hosted embedding or rerank service is an ICT third-party arrangement for the DORA register [AJ].
- PRA PS7/26 and FCA PS26/2 require third-party notifications from 18 March 2027 (R-PRA-SS221, R-FCA-SYSC8) [VF: A8-S062, V2-S053]. A new embedding vendor that supports an important business service may need notification lead time [AJ].

**Residency.** The key-facts table in §7.8 gives the verified position per vendor. For UK firms two points dominate: OpenAI's UK region is storage-only for embeddings [VF: A2-S144], and Gemini's 'eu' endpoint excludes the UK [VF: A2-S039]. No hosted API in this layer verified UK processing, so UK-only data points to in-estate or UK-region VPC deployment [AJ].

**Treat embeddings as the same class of data as the text they encode** [AJ]. Vectors computed from client documents can leak information about that text, so they inherit its classification, retention and deletion obligations [AJ]. A right-to-erasure request must reach the vector index as well as the document store [Rec]. For EU/UK personal data sent to US-hosted APIs, the transfer basis rests on the Data Privacy Framework or SCCs. The DPF appeal C-703/25 P was pending as of 7 October 2026 (R-DATA-TRANSFERS) [VF: A8-S053, V2-S059].

**Chinese-origin open weights.**

- Qwen3 weights are Apache 2.0 [VF: A2-S020].
- Self-hosted, they create no data transfer [AJ]. They do need a model-provenance and supply-chain review, which is consistent with the OWASP supply-chain risk (LLM03 in the 2025 list) [R: A8-S040] [AJ].
- The hosted Model Studio API is a different decision, because its regions are Singapore, Hong Kong and Beijing [VF: A2-S022].

**Concentration.** Database companies now own two of the graphic's vendors (Voyage and Jina) [VF: A2-S033, A2-S023]. Choosing MongoDB with Voyage, or Elastic with Jina, concentrates L6 and L7 on one supplier. Their outages and ownership events then become correlated [AJ]. IOSCO names concentration among few AI technology providers as a supervisory concern (R-INTL-AI-ASSETMGMT) [VF: A8-S058]. For important business services, either accept the bundle consciously and record it in the exit plan, or keep the embedding vendor independent of the store [Rec].

**Auditability.** For every retrieval, the C8 evidence pack should hold [Rec]:
- query hash
- embedding model and version
- index version
- filter predicate (entitlements)
- candidate count
- reranker version
- final document IDs and scores

That is enough to show what the model was shown, and to reproduce it while the index version is retained.

**Standards.**

- NIST AI 600-1 is the GenAI profile for the AI RMF (R-NIST-AIRMF) [VF: A8-S043, A8-S044].
- ISO/IEC 42001 certification is a supplier signal (R-ISO-42001). Cohere [VF: A2-S014] and Generative AI on Vertex AI [VF: A2-S043] hold it.
- The OWASP Top 10 for LLM Applications 2026 and the Top 10 for Agentic Applications for 2026 are the operative lists (R-OWASP-LLM, R-OWASP-AGENTIC) [VF: A8-S041, A8-S042]. For traceability, the 2025 list's LLM08, "Vector and Embedding Weaknesses", is the direct mapping for this layer, because the 2026 identifiers were not retrieved [R: A8-S040].

### 7.12 Worked-example slice (POV 3)

**Context.** The performance-attribution commentary agent drafts the monthly commentary for a generic multi-asset fund. It explains Brinson-style allocation, selection and currency effects against the benchmark. A portfolio manager approves every draft (plan §11) [AJ].

**What the agent needs from L7** [AJ]:
1. **Comparable past commentary.** The fund's own approved commentaries for prior periods, and approved commentaries from comparable periods (for example, months with a large currency effect). These serve as style and structure exemplars.
2. **The house style guide and terminology glossary.** For example: "allocation effect" vs "asset allocation contribution", how interaction is reported, and rounding and sign conventions.
3. **Approved market-context notes** for the period, from L8's approved sources.

**How the layer serves this** [AJ]:
- **Hybrid retrieval.** Lexical retrieval matters because queries carry exact tokens: the fund code, share-class names and period labels ("Q3 2026"). Dense retrieval matters because "the overweight in Japanese equities detracted" must match "the allocation to Japan cost relative performance".
- **Domain terminology.** Run an in-domain bake-off on 100–300 labelled queries written by analysts. Compare a general model, a finance-domain model and a fine-tuned open model:
  - Voyage publishes voyage-finance-2 [VF: A2-S007].
  - Sentence Transformers supports fine-tuning [VF: A2-S029].

  Pick by recall@20 and nDCG@10, not by vendor claims [Rec].
- **Reranking for the right fund and period.** The reranker receives the instruction-style query with the fund name, the period and the attribution theme. It is evaluated on whether the top 3 contains this fund's most recent comparable commentary and the current style guide. Metadata boosts for `fund_id` and `period` are applied in fusion. They are not left to the reranker alone.
- **Entitlement first.** The store filters on `fund_id`, `client_id`, document classification and approval status *before* ANN search, BM25 and reranking. The reranker only ever sees documents the analyst is entitled to.

**What it must never do** [AJ]:
- **Retrieve another fund's or client's data.** Cross-fund probes run in CI and must return zero hits.
- **Supply numbers.** Retrieved past commentary contains old figures. Those figures must never flow into the new draft as data. All figures come from the attribution engine through L4 tools, and the L9 numeric-faithfulness eval checks that every number in the draft traces to that output.
- **Retrieve unapproved drafts** or superseded style-guide versions. Approval status and validity dates are filter fields.
- **Run on an unpinned model.** The commentary index carries one `model_version`, and the evidence pack records it alongside the reranker version and the retrieved document IDs.

### 7.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| OpenAI – Embeddings 3 | Still text-embedding-3 (January 2024); no reranker found [VF: A2-S001, A2-S002] | Tactical text baseline where OpenAI is already approved; pair with a separate reranker [Rec] |
| Gemini – Embedding 2 | gemini-embedding-2 GA 22 April 2026; multimodal; EU endpoint excludes UK [VF: A2-S004, A2-S039] | Strategic, conditional: where Google Cloud is your primary cloud and UK-only processing is not mandatory (CP3 Q2) [Rec] |
| Voyage AI – Voyage-3 | MongoDB-owned; Voyage 4 family, rerank-3 (Preview) [VF: A2-S033, A2-S006, V1-S024] | Tactical; preferred where MongoDB is the store, after SOC 2 scope is evidenced [Rec] |
| Cohere – Embed v3 + Rerank | Embed 5 and Rerank 4; Aleph Alpha combination pending [VF: A2-S012, A2-S010, A2-S018] | Tactical (FS 3.70 on Foundry or SageMaker); Strategic candidate for private or hyperscaler deployment once per-service due diligence confirms the presumed access controls [Rec] |
| Qwen3 – Embeddings | Embedding **and** Reranker, Apache 2.0, plus VL variants [VF: A2-S020, A2-S021] | Tactical; self-host only, after provenance review [Rec] |
| Jina AI – Embeddings v3 | Elastic-owned; v5 text/omni, reranker v3.5; CC-BY-NC weights [VF: A2-S023, A2-S025, A2-S024] | Tactical inside Elastic estates; licensed routes only [Rec] |
| SBERT – Sentence transformers | 6.1.0, Apache-2.0, Hugging Face; dense, cross-encoder, sparse, multi-vector [VF: A2-S029] | **Strategic** as the self-hosting, fine-tuning and exit toolkit [Rec] |
| NVIDIA – Embed | NeMo Retriever embed and rerank NIMs; AI Enterprise needed for production [VF: A2-S031, A2-S040] | Tactical for NVIDIA-standardised estates [Rec] |
| EthicalAgents; Ragoos | Not publicly verified; removed per CP1 Q4(a) [VF: A2-S079, A2-S080] | Do not use |
| (missing) | Amazon Bedrock embeddings and Rerank, Mixedbread and ZeroEntropy were not researched in this run [NPV]; the Vertex AI ranking API exists but was not scored [VF: B-REV-S026] | Candidates for a follow-up pass; not recommended or rejected here [AJ] |
| Layer: "Embeddings" and "RAG re-rankers" as separate tiles | Vendors ship both; stores host both [VF: A2-S101, A2-S141, A2-S133] | One governed retrieval-optimisation service: pinned versions, raw text retained, dual-index migration, in-domain eval gate [Rec] |

**H6, provisional; verdict in synthesis.** The evidence supports treating embedding and reranking as one **retrieval-optimisation** concern [AJ]:

- Six of the seven verified model vendors offer both; Google's reranker is a separate Vertex service [VF: A2-S012, A2-S010, A2-S006, A2-S034, A2-S025, A2-S026, A2-S030, A2-S020, B-REV-S026].
- Sentence Transformers covers both in one library [VF: A2-S029].
- The two are evaluated together, and they are versioned together.

The same evidence also shows the compute moving into L6, because MongoDB, Pinecone and Elastic host embedding and reranking natively [VF: A2-S141, A2-S101, A2-S133]. The provisional view is to **merge** the graphic's "Embeddings" and "RAG re-rankers" into one retrieval-optimisation layer, defined by responsibility rather than by where the compute runs [AJ]. That layer owns model choice, version pinning, hybrid fusion policy and the retrieval evaluation gate, whether the models run as APIs, in the firm's own estate, or inside the store. Embedding-model versioning should be named explicitly as a governed configuration item, because it is the one decision in this layer that carries a corpus-wide migration cost [AJ].
