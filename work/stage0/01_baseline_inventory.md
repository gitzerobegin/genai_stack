# Stage 0: Baseline inventory of `AI_Full_Stack.jpg`

| | |
|---|---|
| **Input** | `inputs/AI_Full_Stack.jpg`: "The Full AI Stack Explained" |
| **Graphic's own claims** | "Updated for October 2026 · 9 layers · 80 tools"; attribution footer "Follow Harish Kumar for more AI" |
| **Inventory date** | 7 October 2026 |
| **Status of this file** | Transcription of the graphic only. Nothing here is a verified fact about the products; the graphic is a hypothesis (plan §2, rule 5). |

## 1. Layers as drawn

The graphic is a stack of nine coloured cylinders, numbered 1 (top) to 9 (bottom), each with a short tagline and an arrow to a box of product tiles. Number 1 is drawn at the **top**, yet the plan treats L1 as the base of the stack. The graphic does not draw dependencies between layers, so stack order is implied only by numbering.

| # | Layer label | Tagline | Tiles | Product descriptors as printed |
|---|---|---|---:|---|
| 1 | LLMs | The brain | 11 | OpenAI "GPT-6" · Claude "Opus 5.5" · Gemini "Gemini" · Grok (no version) · DeepSeek "V4" · Qwen "3.8" · Kimi "K3" · "QI4" (Z logo) "Q4" · Mistral "Medium 3.1" · Gemma "2.9" · Meta "Llama (new: Muse)" |
| 2 | Inference & Access | Where it runs | 9 | Hugging Face "models & APIs" · OpenRouter "multi-provider" · Together AI "open-source cloud" · Fireworks AI "fast inference" · Cerebras "ultra-scale cloud" · Ollama "run locally" · LM Studio "desktop app" · vLLM "high-throughput" · SGLang "efficient engine" |
| 3 | Agent Frameworks | The execution loop | 9 | LangGraph "workflow" · AI SDK "AI SDK" (triangle logo, i.e. Vercel) · Agent SDK (OpenAI logo) · Agent SDK (Anthropic logo) · Mistral "Agents SDK" · LlamaIndex "document agents" · Pydantic AI "type-safe" · CrewAI "multi-agent" · Agent Framework "Microsoft" |
| 4 | Tools & Protocols | How agents interact | 8 | MCP "tools standard" · A2A "agent-to-agent" · Agent Skills "reusable skills" · Composio "integrations" · Exa "search API" · Tavily "search API" · Browserbase "cloud browsers" · E2B "code sandboxes" |
| 5 | Memory | What it remembers | 6 | Mem0 "memory layer" · Zep "graph memory" · Letta "stateful agents" · Cognee "knowledge graphs" · Supermemory "memory API" · LangMem "long-term" |
| 6 | Vector Databases | Where knowledge lives | 10 | Postgres "+ pgvector" · Pinecone "managed" · Qdrant "open source" · Milvus "vector search" · Weaviate "open source" · turbopuffer "cloud vector store" · Elasticsearch "hybrid search" · MongoDB "Atlas vector" · Chroma "open source" · S3 Vectors "AWS" |
| 7 | Embeddings & Rerankers | Find the right context | 10 | OpenAI "Embeddings 3" · Gemini "Embedding 2" · Voyage AI "Voyage-3" · Cohere "Embed v3 + Rerank" · Qwen3 "Embeddings" · Jina AI "Embeddings v3" · SBERT "Sentence transformers" · NVIDIA "Embed" · EthicalAgents "embeddings" · Ragoos "RAG re-rankers" |
| 8 | Data Extraction | Make messy data usable | 9 | Firecrawl "web to LLM-ready" · Docling "doc parser" · LlamaParse "PDF / documents" · Crawl4AI "open crawler" · MinerU "PDF parser" · Reducto "enterprise docs" · Mistral OCR "OCR" · Unstructured "ETL for docs" · Apify "scrapers" |
| 9 | Evals & Observability | Know if it works | 8 | Langfuse "open source" · LangSmith "trace & eval" · Braintrust "evals platform" · Phoenix "Atrace" · DeepEval "LLM unit tests" · Promptfoo "red-teaming" · Opik "comet" · Arize "RAG metrics" |
| | **Total** | | **80** | Matches the graphic's "80 tools" claim |

## 2. Product categories implied by the graphic

| Category (implied) | Where | Observation |
|---|---|---|
| Model vendor / model family | L1 | Mixes vendors (OpenAI, Meta), product brands (Claude, Gemini, Grok, Kimi) and open-weight families (Gemma, Qwen). Versions are given for some and omitted for others. |
| Model hub / marketplace | L2 (Hugging Face, OpenRouter) | Aggregators and routers sit beside serving engines. |
| Managed inference cloud | L2 (Together, Fireworks, Cerebras) | Hosted APIs for open-weight models. |
| Local runtime | L2 (Ollama, LM Studio) | Developer-desktop tools sit beside production engines. |
| Serving engine | L2 (vLLM, SGLang) | Self-hosted, GPU-level software. |
| Agent framework / SDK | L3 | Graph orchestration, vendor SDKs and multi-agent frameworks are all in one box. |
| Protocol / standard | L4 (MCP, A2A, Agent Skills) | Open specifications sit beside commercial SaaS. |
| Tool SaaS | L4 (Composio, Exa, Tavily, Browserbase, E2B) | Integration, search, browser and sandbox services. |
| Memory service | L5 | Memory layers, a stateful agent runtime (Letta) and a knowledge-graph engine (Cognee). |
| Vector / search store | L6 | Dedicated vector DBs sit beside general databases with vector features and an object store (S3 Vectors). |
| Embedding / reranker model | L7 | Model families from labs and hosted APIs. |
| Parser / OCR / crawler | L8 | Document parsers, OCR models, web crawlers and scraping marketplaces. |
| Eval / observability platform | L9 | Tracing platforms, eval libraries and red-teaming tools. |

## 3. Implied relationships

- **Vertical stack:** the numbering implies L1 (models) at the core and L9 (evals) as the last concern. The graphic draws no arrows between layers, only arrows from each layer to its product box.
- **Retrieval chain:** L8 → L7 → L6 is implied by adjacency (extract → embed → store). No connection to L5 memory is drawn.
- **Vendor spread across layers** (same company in several layers):
  - OpenAI: L1, L3 (Agent SDK), L7 (Embeddings)
  - Google: L1 (Gemini, Gemma), L7 (Gemini Embedding)
  - Anthropic: L1 (Claude), L3 (Agent SDK), and by origin L4 (MCP, Agent Skills)
  - Mistral: L1, L3 (Agents), L8 (OCR)
  - Alibaba Qwen: L1, L7
  - Arize: L9 twice (Phoenix and Arize)
  - LangChain: L3 (LangGraph), L5 (LangMem), L9 (LangSmith)
  - LlamaIndex: L3, L8 (LlamaParse)
  - NVIDIA: L7
  - Microsoft: L3
  - AWS: L6 (S3 Vectors)
- **Implied interchangeability:** each box reads as a menu of alternatives. Several tiles are actually complements, e.g. vLLM is often deployed underneath managed clouds, and Phoenix is a component of the Arize platform.

## 4. Apparent positioning, as stated by the graphic

The positioning is taken from the descriptor under each tile, e.g. Pinecone "managed", Qdrant "open source", Cerebras "ultra-scale cloud", Promptfoo "red-teaming", Langfuse "open source". These descriptors are single-word claims that Stage A must test. Examples:

- Is Promptfoo only red-teaming? It also does evals.
- Is Zep only "graph memory"?
- Is Cerebras "ultra-scale cloud", or a chip vendor with an inference API?

## 5. Duplications and ambiguities

| # | Entry in graphic | Problem | Working hypothesis (plan §3) | Stage A owner |
|---|---|---|---|---|
| A1 | "QI4" with Z logo, descriptor "Q4" | Name not recognisable | Z.ai (Zhipu) GLM family | ⑤ L1 |
| A2 | "EthicalAgents" (embeddings) | Unknown product | May not exist; flag "Not publicly verified" if no primary source | ② L7 |
| A3 | "Ragoos" (RAG re-rankers) | Unknown product | May not exist; same treatment | ② L7 |
| A4 | "Phoenix – Atrace" | Descriptor is garbled | Arize Phoenix, open source (descriptor probably "Arize" or "tracing") | ① L9 |
| A5 | "Meta – Llama (new: Muse)" | Unclear whether "Muse" is a real Meta model family | Verify Meta's currently documented model family | ⑤ L1 |
| A6 | "Gemini – Gemini" | No version | Cover the current Gemini lineup | ⑤ L1 |
| A7 | "Agent SDK" × 3 | The same label covers three products | OpenAI Agents SDK, Claude Agent SDK and Mistral Agents API/SDK, treated separately | ④ L3 |
| A8 | "Arize – RAG metrics" vs "Phoenix" | Same company, two tiles | Separate open-source Phoenix from the commercial Arize AX platform | ① L9 |
| A9 | "Gemma 2.9" | Version label looks implausible: Gemma 3 was public by 2025 | Verify the current Gemma generation | ⑤ L1 |
| A10 | "OpenAI GPT-6" | GPT-6 status unclear; early search signals conflict | Verify current OpenAI lineup and tiers; the brief also names "GPT-6 Astra/Sol/Luna" | ⑤ L1 |
| A11 | "Qwen 3.8", "Kimi K3", "DeepSeek V4", "Mistral Medium 3.1", "Claude Opus 5.5" | Version labels need primary-source verification | Verify each as part of a model family | ⑤ L1 |
| A12 | "Cohere Embed v3 + Rerank" | Possibly superseded by Embed v4 / Rerank v3.5+ | Verify current versions | ② L7 |
| A13 | "Voyage AI Voyage-3", "Jina Embeddings v3", "OpenAI Embeddings 3", "Gemini Embedding 2" | Version labels may be stale; Voyage AI's acquisition by MongoDB needs confirming | Verify current versions and ownership | ② L7 |
| A14 | "NVIDIA Embed" | Ambiguous: NV-Embed model, NeMo Retriever or NIM microservices | Treat as NVIDIA NeMo Retriever / NIM embedding and reranking | ② L7 |
| A15 | "AI SDK" (triangle logo) | Logo only | Vercel AI SDK | ④ L3 |
| A16 | "Milvus – vector search" | Open-source Milvus vs managed Zilliz Cloud | Cover both | ② L6 |
| A17 | "Mistral Agents SDK" | Unclear whether this is a distinct SDK or the Agents API in Mistral's SDK | Verify | ④ L3 |
| A18 | "Opik – comet" | Product of Comet ML | Opik by Comet | ① L9 |
| A19 | "Hugging Face – models & APIs" | Hub, Inference Providers, Inference Endpoints and TGI are all different products | Separate them in the profile | ④ L2 |

## 6. Missing enterprise capabilities (first pass)

The following are absent from the graphic. Stage A confirms products for each, and Stage B gives each the full layer template (plan §6).

| Missing capability | Plan control |
|---|---|
| AI / LLM gateway: routing, quotas, policy, logging | C1 (L2 shows routers but no enterprise gateway) |
| Guardrails: input/output safety, jailbreak defence | C2 |
| DLP / PII detection, masking, residency | C3 |
| Agent identity, delegated authority, authorisation, secrets | C4 |
| Prompt and configuration management | C5 |
| AI FinOps: cost attribution, budgets, chargeback | C6 |
| AI security: prompt injection, supply chain, sandboxing, exfiltration | C7 |
| Model risk management, governance, inventory, audit evidence, lineage | C8 |

The graphic also leaves out:

- human-in-the-loop and approval workflow (it appears only implicitly in L3)
- data lineage
- feature/knowledge-graph stores beyond Cognee
- model fine-tuning and adaptation (no layer for training or fine-tuning)
- semantic caching
- workflow durability (durable execution engines)
- an explicit user-facing application / experience layer
