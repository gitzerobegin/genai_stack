# Stage A′ (verification) and Stage B (writers): prompts as executed

## Stage A′, verifier V2 (streams A5–A8)

Run on 8 October 2026 as a background `general-purpose` agent.

```text
You are Stage A′ adversarial verifier V2 for an enterprise GenAI stack review. Today is 8 October 2026.

FIRST read and follow exactly: /home/user/genai_stack/work/stage0/06_stageA_prime_verify_brief.md (it points to the other files you need).

VERIFIER = V2. Your assigned streams (folders under /home/user/genai_stack/work/stageA/):
- A5_L1 (foundation-model vendors — 11 records; highest priority: every model version/lineup/date, GPT-6 Astra/Sol/Luna, Claude Fable 5.1/Opus 5.5/Mythos claims, Gemini 3.x/4, Gemma 4, DeepSeek V4.1, Qwen 3.8, Kimi K3, GLM-5.x, Mistral Medium 3.5/Large 4, Meta Muse/Llama 4, xAI/SpaceX merger claim, Chinese-model regulatory actions, Anthropic controversy claims — label them precisely and neutrally; you are an Anthropic model, so be at least as sceptical of Anthropic claims as others)
- A6_C1_C4 (gateways, guardrails, DLP, agent identity — acquisitions: Portkey→Palo Alto, Guardrails AI→Harvey; LiteLLM PyPI compromise; Presidio governance; Entra Agent ID / AgentCore Policy GA; MCP 2026-07-28 auth changes)
- A7_C5_C8 (prompt mgmt, FinOps, AI security, governance — acquisitions: Lakera→Check Point, Protect AI→Palo Alto, Prompt Security→SentinelOne, CalypsoAI→F5, Pangea→CrowdStrike, Langfuse→ClickHouse, Promptfoo→OpenAI, Helicone→Mintlify, Collibra/trail ML; LaunchDarkly AgentControl rename; FOCUS token columns)
- A8_Regulation (regulatory_facts.json — SR 26-2 superseding SR 11-7 on 17 April 2026; EU Regulation 2026/1744 moving Annex III high-risk to 2 Dec 2027; DORA CTPP designations 18 Nov 2025; UK CTP designations 13 July 2026; PRA PS7/26 and FCA PS26/2; EBA guidelines 18 Sept 2026; EU–UK adequacy renewal; OWASP 2026 lists; ISO 42005/42006; SEC PDA withdrawal)

Output: work/stageA_verify/V2/verification_log.md and work/stageA_verify/V2/sources.csv; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/V2/. Edit the assigned products.json / regulatory_facts.json files in place per the brief.

Search budget: the environment caps web searches at about 200 per turn, shared with any other agent running concurrently. Prioritise in this order: (1) every "What changed" row and every acquisition/rename/deprecation claim; (2) regulatory dates/statuses; (3) model versions/dates; (4) certifications; (5) pricing. If the budget runs out, stop cleanly, write the log for what you checked, and list exactly what remains unchecked so you can be resumed.

Finish with the ≤250-word summary described in the brief.
```

## Stage A′, verifier V1 (streams A1–A4)

```text
You are Stage A′ adversarial verifier V1 for an enterprise GenAI stack review. Today is 8 October 2026.

FIRST read and follow exactly: /home/user/genai_stack/work/stage0/06_stageA_prime_verify_brief.md (it points to the other files you need).

VERIFIER = V1. Your assigned streams (folders under /home/user/genai_stack/work/stageA/):
- A1_L9_L8 (evals/observability + ingestion — Arize→Dynatrace US$915M; Phoenix Elastic License 2.0; Promptfoo→OpenAI; Langfuse→ClickHouse; LlamaParse rebrand; Firecrawl AGPL + Series B; MinerU 4.0 licence threshold; Crawl4AI licence; Mistral OCR 4.1; W&B→CoreWeave; OTel GenAI semconv status)
- A2_L7_L6 (embeddings + retrieval stores — Voyage→MongoDB, Voyage 4, rerank-3; Jina→Elastic, v5, CC-BY-NC; Cohere Embed 5 / Rerank 4 / Aleph Alpha deal; Pinecone Nexus/BYOC/certs/pricing; pgvector 0.8.7; S3 Vectors GA/pricing/limits; Milvus 3.0; Qdrant Series B; Elastic AGPL; MongoDB Community vector search; EthicalAgents/Ragoos not found — try once more yourself)
- A3_L5_L4 (memory + tools — Letta pivot; Zep OSS deprecation; Mem0 OSS graph removal; MCP donation to Agentic AI Foundation, spec 2026-07-28; A2A 1.0 and foundation move; Agent Skills status — you are an Anthropic model, be at least as sceptical of Anthropic-originated claims; Tavily→Nebius; certifications)
- A4_L3_L2 (frameworks + inference — OpenAI Agent Builder shutdown; Claude Agent SDK rename/licence; Mistral Workflows; Microsoft Agent Framework GA 2 April 2026 / Semantic Kernel / AutoGen; TGI maintenance; LangSmith Deployment rename; Ollama cloud; Cerebras IPO; Together/Fireworks funding and certs; OpenRouter; vLLM PyTorch Foundation; SGLang/RadixArk)

Output: work/stageA_verify/V1/verification_log.md and work/stageA_verify/V1/sources.csv; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/V1/. Edit the assigned products.json files in place per the brief.

Search budget: the environment caps web searches at about 200 per turn, shared with any other agent running concurrently (another verifier is running now). Prioritise: (1) every "What changed" row and every acquisition/rename/deprecation/licence-change claim; (2) versions/dates; (3) certifications; (4) pricing. If the budget runs out, stop cleanly, write the log for what you checked, and list exactly what remains unchecked so you can be resumed.

Finish with the ≤250-word summary described in the brief.
```

---

## Stage B, writer prompts (layers 9–7, the CP2 tranche)

All three writers use `work/stage0/07_stageB_writer_brief.md` and `work/stage0/08_scoring_rubric.md`. To write any other layer or control, copy one of these prompts and change three things: the layer id, the product list and the layer-specific guidance.

### L9

```text
You are the Stage B writer for LAYER = L9 (Evaluation and observability, treated as cross-cutting). Today is 8 October 2026.

FIRST read and follow exactly: /home/user/genai_stack/work/stage0/07_stageB_writer_brief.md (it lists every file you must read, the 13-part section template, the assessments.json format and the hard rules). Also read work/stage0/08_scoring_rubric.md.

Outputs: work/stageB/L9/section.md and work/stageB/L9/assessments.json (create the folder). Section numbering: "## 9. Evaluation and observability (cross-cutting)" with subsections 9.1–9.13.

Your products (11, from Enterprise_GenAI_Stack_Oct2026/05_Data/products.json, layer L9): L9-langfuse, L9-langsmith, L9-braintrust, L9-arize-phoenix, L9-arize-ax, L9-deepeval, L9-promptfoo, L9-opik, L9-mlflow-genai, L9-datadog-agent-observability, L9-wandb-weave. Layer notes: work/stageA/A1_L9_L8/notes.md (sections a, b, c-H8, d, e).

Layer-specific guidance:
- Distinguish evaluation (offline/CI, online, human, LLM-as-judge, red-teaming), observability (traces, cost, latency) and production feedback loops; cover the research questions in plan §5 L9 (faithfulness/groundedness, retrieval recall@k/precision@k, tool-call accuracy, agent trajectory evaluation, safety/red-teaming, regression, drift).
- Treat the hypothesis H8 (evals/observability are cross-cutting, not a downstream layer) — give the evidence and a provisional view in 9.13; the verdict comes in synthesis.
- OpenTelemetry GenAI semantic conventions (status: Development) and OpenInference are the portability lever — make the abstraction strategy concrete.
- Ownership consolidation is central here: Arize (Phoenix + AX) → Dynatrace (completed 1 Oct 2026); Langfuse → ClickHouse (announced 16 Jan 2026); Promptfoo → OpenAI (announced 9 Mar 2026, closing not published — do not say "completed"); W&B → CoreWeave. Note the conflict-of-interest angle of a model vendor owning an eval/red-team tool.
- Licence nuance: Phoenix is ELv2 (source-available, not OSI open source); Langfuse is MIT core with enterprise-gated SCIM/audit/RBAC.
- FS lens: this layer produces the validation and monitoring evidence that SS1/23 and AI Act Art. 26 deployer duties rely on; audit-evidence retention, reproducibility, data residency of traces (traces contain client data), and SR 26-2's GenAI exclusion meaning firms must set their own standard.
- Worked example: numeric-faithfulness evals (every figure in the draft matches the attribution engine output), groundedness against approved sources, house-style checks, regression suite of past commentaries, reviewer-edit feedback loop, evidence pack retention.

Finish with the ≤200-word final reply described in the brief.
```

### L8

```text
You are the Stage B writer for LAYER = L8 (Data extraction, ingestion and web). Today is 8 October 2026.

FIRST read and follow exactly: /home/user/genai_stack/work/stage0/07_stageB_writer_brief.md (it lists every file you must read, the 13-part section template, the assessments.json format and the hard rules). Also read work/stage0/08_scoring_rubric.md.

Outputs: work/stageB/L8/section.md and work/stageB/L8/assessments.json (create the folder). Section numbering: "## 8. Data extraction, ingestion and web" with subsections 8.1–8.13.

Your products (10, from Enterprise_GenAI_Stack_Oct2026/05_Data/products.json, layer L8): L8-firecrawl, L8-docling, L8-llamaparse, L8-crawl4ai, L8-mineru, L8-reducto, L8-mistral-ocr, L8-unstructured, L8-apify, L8-google-document-ai. Layer notes: work/stageA/A1_L9_L8/notes.md (sections a, b, c-H7, d, e).

Layer-specific guidance:
- Cover the pipeline in plan §5 L8 (source → acquisition → parsing → OCR → structure extraction → cleaning → chunking → metadata → indexing) and the content types (PDFs/scans, tables, PowerPoint/Excel, websites, emails, enterprise documents, structured data, multimodal).
- Hypothesis H7 (ingestion must include lineage, classification, PII/DLP, access-control metadata, incremental indexing): evidence shows Unstructured connectors carry ACL metadata and reprocess on permission change, Firecrawl offers PII redaction/ZDR, and no L8 product offers lineage; OpenLineage has no GenAI facets. Make the "enterprise additions" concrete as an architecture (what you build around the parser), provisional view in 8.13.
- Separate web acquisition (Firecrawl, Crawl4AI, Apify — with legal/ToS/robots and data-provenance considerations) from document parsing (Docling, LlamaParse, MinerU, Reducto, Unstructured, Mistral OCR, Document AI). Consider whether these should be one layer.
- Licence nuance is decision-relevant: Firecrawl server AGPL-3.0 with cloud-only enterprise features and US data location; MinerU 4.0 custom licence with commercial thresholds; Crawl4AI Apache-2.0 plus attribution clause; Docling MIT under LF AI & Data (Graduate Aug 2026); LlamaParse is now LlamaIndex's whole platform (renamed from LlamaCloud). Mistral OCR 4.1 (GA 26 Aug 2026; OCR 4.0 retired 30 Sep 2026) — model-version churn as an operational risk. Unstructured: do NOT repeat "FedRAMP" (no authorisation found).
- FS lens: ingestion is where data residency, PII classification and entitlements are decided (not at the prompt); third-party processing of client documents under PS7/26 / DORA; reproducibility (parser version pinning) for audit.
- Worked example: parsing fund factsheets, prior commentaries, market notes; tables must be extracted exactly (a parsing error becomes a "hallucinated" number); entitlement metadata; never ingest unapproved sources.

Finish with the ≤200-word final reply described in the brief.
```

### L7

```text
You are the Stage B writer for LAYER = L7 (Embeddings and reranking). Today is 8 October 2026.

FIRST read and follow exactly: /home/user/genai_stack/work/stage0/07_stageB_writer_brief.md (it lists every file you must read, the 13-part section template, the assessments.json format and the hard rules). Also read work/stage0/08_scoring_rubric.md.

Outputs: work/stageB/L7/section.md and work/stageB/L7/assessments.json (create the folder). Section numbering: "## 7. Embeddings and reranking" with subsections 7.1–7.13.

Your products (from Enterprise_GenAI_Stack_Oct2026/05_Data/products.json, layer L7): L7-openai, L7-gemini-embedding, L7-voyage, L7-cohere, L7-qwen3-embedding, L7-jina, L7-sentence-transformers, L7-nvidia-nemo-retriever, plus L7-ethicalagents and L7-ragoos which per CP1 decision Q4(a) are REMOVED: include them in assessments.json with tier null, flags ["Not publicly verified"], scores null, and mention them in one line only in the section. Layer notes: work/stageA/A2_L7_L6/notes.md (sections a, b, c-H6, d, e).

Layer-specific guidance:
- Cover plan §5 L7: embedding quality and multilingual performance; domain adaptation; dimensionality (Matryoshka) and quantisation; retrieval quality, latency and cost; cross-encoder reranking; sparse + dense hybrid; also late interaction (ColBERT/ColPali) and multimodal embeddings where evidenced.
- Hypothesis H6 (embeddings and reranking form one retrieval-optimisation layer): evidence — Cohere, Voyage, Jina, NVIDIA, Qwen ship both; rerankers hosted inside stores (Pinecone, MongoDB $rerank, Elastic semantic_text defaulting to Jina v5). Provisional view in 7.13.
- Ownership: Voyage → MongoDB (Feb 2025); Jina → Elastic (9 Oct 2025) — embedding models increasingly bundled with databases, which changes lock-in analysis. Cohere–Aleph Alpha combination signed 16 Sep 2026, pending approval. Jina weights are CC-BY-NC-4.0 (non-commercial) — material for self-hosting. NVIDIA NIM production use needs NVIDIA AI Enterprise. Voyage rerank-3 is Preview on MongoDB's lifecycle page.
- Key architectural point to make concretely: changing an embedding model forces re-embedding the corpus — embedding model version is production configuration (links to C5) and a portability cost; recommend dual-index migration patterns, storing raw text, model-version metadata.
- Do not rely on vendor benchmark claims or MTEB rankings you could not verify (the MTEB site was blocked); say so and recommend in-domain evaluation (links to L9).
- FS lens: embeddings of client data are personal/confidential data derivatives — residency (OpenAI EU processing/ZDR, Voyage EU via Atlas, Cohere 30-day/ZDR), Chinese-origin open weights (Qwen3) self-hosted vs hosted API, concentration.
- Worked example: retrieving comparable past commentary and the house style guide; finance-domain terminology; reranking to put the right fund and period first; never retrieve another fund's or client's data (entitlement filtering happens before rerank).

Finish with the ≤200-word final reply described in the brief.
```
