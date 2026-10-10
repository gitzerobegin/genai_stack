# The Enterprise GenAI Stack

<!-- Source for the stack graphic. Edit this file, then run:
       python3 -I tools/build_stack_graphic.py .            (Markdown -> HTML)
       NODE_PATH=$(npm root -g) node tools/render_graphic.js Enterprise_GenAI_Stack_Oct2026/08_Graphic/Enterprise_GenAI_Stack_Oct2026.html Enterprise_GenAI_Stack_Oct2026/08_Graphic/Enterprise_GenAI_Stack_Oct2026
     After a dataset refresh, add --sync to the first command: it updates every Tier from 05_Data/products.json and
     appends any new scored product to its layer table (edit its label and note afterwards).
     Layer order: L1 -> L9 under the control plane (user decision, 9 Oct 2026); keep sections in this order.
     Tiers: Strategic | Tactical | Experimental | Pattern (drawn dotted, not scored). Cloud: AWS | Azure | Google Cloud or blank.
     {N} {S} {T} {E} in the stats line are filled in from the tables. -->

- subtitle: The new baseline set by this review: reference architecture and product landscape for a regulated UK/EU asset manager · evidence as of 9 October 2026
- stats: **9** layers, L1 → L9; **8** enterprise controls; **{N}** products assessed; **1,449** sources; **{S}** Strategic · **{T}** Tactical · **{E}** Experimental
- legend-strategic: Strategic — platform default (most carry a condition)
- legend-tactical: Tactical — a stated niche or estate
- legend-experimental: Experimental — pilot only, outside regulated paths
- legend-cloud: Strategic only where that cloud is primary

## Control plane

- style: control
- subtitle: firm-owned policy and one evidence store, around every call

### C1 · AI traffic gateway

- duty: model, tool (MCP) and agent (A2A) calls

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C1-litellm | LiteLLM | Enterprise licence · pin and sign builds |  | Strategic |
| C1-kong-ai-gateway | Kong AI Gateway | where Kong is the API standard |  | Strategic |
| C1-google-apigee-ai-gateway | Apigee AI gateway | MCP support GA | Google Cloud | Strategic |
| C1-azure-apim-ai-gateway | Azure APIM AI gateway | GA policies only | Azure | Strategic |
| C1-aws-agentcore-gateway | AgentCore Gateway | MCP gateway | AWS | Strategic |
| C1-portkey | Portkey | Palo Alto Networks · Prisma AIRS |  | Tactical |
| C1-agentgateway | agentgateway | MCP / A2A on Kubernetes |  | Tactical |
| C1-envoy-ai-gateway | Envoy AI Gateway | Agent Router · in-cluster |  | Tactical |
| C1-cloudflare-ai-gateway | Cloudflare AI Gateway | non-confidential work, BYOK |  | Tactical |

### C2 · Guardrails

- duty: policy and tests owned by the firm

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C2-bedrock-guardrails | Bedrock Guardrails | standalone API from the gateway | AWS | Strategic |
| C2-google-model-armor | Model Armor | strict residency | Google Cloud | Strategic |
| C2-azure-ai-content-safety | Azure AI Content Safety | Prompt Shields on documents | Azure | Strategic |
| C2-nemo-guardrails | NeMo Guardrails | orchestrator · still 0.x |  | Tactical |
| C2-meta-llama-protections | Llama Guard / Prompt Guard | one detector among several |  | Tactical |
| C2-guardrails-ai | Guardrails AI | Harvey-owned · plan migration |  | Experimental |

### C3 · Privacy service (DLP / PII)

- duty: one API, six enforcement points

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C3-presidio | Presidio | behind a firm privacy-service API |  | Strategic |
| C3-google-sdp | Sensitive Data Protection | Google's DLP service | Google Cloud | Strategic |
| C3-microsoft-purview-dspm-ai | Purview DSPM for AI | posture, not prompt-path DLP | Azure | Strategic |
| C3-skyflow | Skyflow | vault tokenisation |  | Tactical |
| C3-protegrity | Protegrity | existing customers |  | Tactical |

### C4 · Identity and authorisation

- duty: every agent a registered identity

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C4-opa | OPA | policy decision point · CNCF |  | Strategic |
| C4-spiffe-spire | SPIFFE / SPIRE | workload identity · CNCF |  | Strategic |
| C4-cedar | Cedar | policy language · AgentCore Policy |  | Strategic |
| C4-okta-auth0-ai-agents | Okta / Auth0 for AI Agents | where Okta holds the workforce |  | Strategic |
| C4-entra-agent-id | Entra Agent ID | where Entra holds the workforce |  | Strategic |
| C4-mcp-authorization | MCP Authorization | Anthropic-originated · alt: OAuth on OpenAPI |  | Strategic |

### C5 · Configuration of record

- duty: prompts, pins and manifests in Git

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C5-langsmith-prompts | LangSmith Prompts | with LangSmith as L9 platform |  | Strategic |
| C5-langfuse-prompts | Langfuse Prompts | with Langfuse as L9 platform |  | Strategic |
| C5-prompts-as-code | Prompts as code (Git) | the configuration of record |  | Strategic |
| C5-promptlayer | PromptLayer | framework-neutral registry |  | Tactical |
| C5-launchdarkly-ai-configs | LaunchDarkly AgentControl | rollout between approved variants |  | Tactical |

### C6 · AI FinOps

- duty: cost per task, budgets fail closed

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C6-finops-focus | FinOps FOCUS | open billing data standard |  | Strategic |
| C6-gateway-cost-attribution | Gateway cost attribution | budgets that fail closed |  | Strategic |
| C6-vantage | Vantage | reporting layer only |  | Tactical |
| C6-cloudzero | CloudZero | reporting layer only |  | Tactical |
| C6-helicone | Helicone | maintenance mode · migrate |  | Experimental |

### C7 · AI security

- duty: secrets, supply chain, sandboxing

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C7-hashicorp-vault | HashiCorp Vault | IBM · agentic IAM · BUSL |  | Strategic |
| C7-model-supply-chain-scanning | Model & package scanning | safetensors by default |  | Strategic |
| C7-openssf-model-signing | OpenSSF Model Signing | sign weights you produce |  | Tactical |
| C7-prisma-airs | Prisma AIRS | Palo Alto estates |  | Tactical |
| C7-hiddenlayer | HiddenLayer | independent specialist |  | Tactical |
| C7-lakera | Check Point AI Guardrails | runtime detector · self-host for client data |  | Tactical |

### C8 · Model risk and governance

- duty: inventory, validation, evidence store

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| C8-openlineage | OpenLineage | + firm GenAI facets |  | Strategic |
| C8-watsonx-governance | IBM watsonx.governance | IBM estates |  | Tactical |
| C8-credo-ai | Credo AI | policy-led programmes |  | Tactical |
| C8-collibra-ai-governance | Collibra AI Governance | where Collibra is the catalogue |  | Tactical |
| C8-modelop | ModelOp | after full due diligence |  | Tactical |
| C8-validmind | ValidMind | model-risk-led firms |  | Tactical |

## Model plane

- style: plane

### L1 · Foundation-model portfolio

- duty: two unrelated vendors + small + open-weight, all pinned
- design: A two-vendor mid tier qualified on one suite, a small tier and a self-hosted open-weight tier; every version pinned.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L1-openai | OpenAI GPT-6 | Astra · Sol · Luna · 6.1 Sol |  | Strategic |
| L1-mistral | Mistral | Medium 3.5 · Large 3 · EU-hosted |  | Strategic |
| L1-anthropic | Anthropic Claude | hyperscaler EU route · tier set by reader |  | Strategic |
| L1-google-gemma | Gemma 4 | small open-weight tier · Apache 2.0 |  | Strategic |
| L1-google-gemini | Google Gemini 3.x | pin versions · short lifetimes | Google Cloud | Strategic |
| L1-xai-grok | Grok 4.7 (SpaceXAI) | via a hyperscaler only |  | Tactical |
| L1-deepseek | DeepSeek V4 | weights or in-tenant only |  | Tactical |
| L1-zai-glm | Z.ai GLM-5.3 | MIT Flash weights · after sanctions review |  | Tactical |
| L1-meta | Meta Muse / Llama | block the contributor tier |  | Tactical |
| L1-alibaba-qwen | Qwen 3.8 | self-host by policy |  | Tactical |
| L1-moonshot-kimi | Kimi K3 | custom licence |  | Experimental |

### L2 · Inference & model access

- duty: in-region access; vLLM as the private exit route
- design: The primary cloud's model service in an approved UK/EU region; one open-weight model on vLLM as the tested exit route.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| - | Primary cloud’s model service | Bedrock · Foundry · Gemini Enterprise Agent Platform, in region |  | Pattern |
| L2-vllm | vLLM | default engine · the exit route |  | Strategic |
| L2-fireworks-ai | Fireworks AI | once ISO certificates confirmed |  | Strategic |
| L2-sglang | SGLang | backup engine once CVE is fixed |  | Strategic |
| L2-hugging-face | Hugging Face Hub | governed open-weight supply |  | Strategic |
| L2-together-ai | Together AI | EU dedicated, ZDR on |  | Tactical |
| L2-openrouter | OpenRouter | behind the gateway · Stripe deal |  | Tactical |
| L2-ollama | Ollama | developer tier |  | Tactical |
| L2-cerebras | Cerebras | low latency, non-confidential |  | Tactical |
| L2-lm-studio | LM Studio | desktops only · no service use |  | Tactical |
| L2-llm-d | llm-d | CNCF sandbox · pilot |  | Experimental |
| L2-nvidia-dynamo | NVIDIA Dynamo | beta · pilot |  | Experimental |

## Agent plane

- style: plane

### L3 · Orchestration: workflows & agents

- duty: deterministic by default, durable, approval gates
- design: Workflows by default with one bounded model step, durable execution, and approval interrupts only a named human can resume.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L3-langgraph | LangGraph | default · workflows + agents |  | Strategic |
| L3-temporal | Temporal | durable execution |  | Strategic |
| L3-microsoft-agent-framework | Microsoft Agent Framework | GA · Microsoft and .NET estates |  | Strategic |
| L3-pydantic-ai | Pydantic AI | typed agent steps |  | Strategic |
| L3-google-adk | Google ADK | on Agent Engine | Google Cloud | Strategic |
| L3-aws-strands-agentcore | Strands + AgentCore Runtime | framework + managed runtime | AWS | Strategic |
| L3-openai-agents-sdk | OpenAI Agents SDK | sandboxed sub-step · pre-1.0 |  | Tactical |
| L3-crewai | CrewAI | use Flows for regulated work |  | Tactical |
| L3-llamaindex | LlamaIndex | retrieval toolkit |  | Tactical |
| L3-vercel-ai-sdk | Vercel AI SDK | TypeScript app tier |  | Tactical |
| L3-claude-agent-sdk | Claude Agent SDK | Alpha · sandboxed only · alt: LangGraph |  | Experimental |
| L3-mistral-agents | Mistral Agents API | Workflows in beta |  | Experimental |

### L4 · Tools & connectivity

- duty: nothing reachable except through the governed gateway
- design: Read-only tools for authoritative data behind a tool-governance sub-layer: private registry, pinned definitions, policy, audit.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L4-a2a | A2A 1.0 | cross-team delegation · signed cards |  | Strategic |
| L4-mcp | MCP | behind a governed gateway · alt: OpenAPI |  | Strategic |
| L4-aws-agentcore-gateway-identity | AgentCore Gateway + Identity | managed tool governance | AWS | Strategic |
| L4-browserbase | Browserbase | only where no API exists |  | Tactical |
| L4-e2b | E2B | microVM sandbox |  | Tactical |
| L4-agent-skills | Agent Skills | script-free, internal · alt: AGENTS.md |  | Tactical |
| L4-exa | Exa | via egress proxy + DLP |  | Tactical |
| L4-tavily | Tavily | Nebius-owned |  | Tactical |
| L4-composio | Composio | May 2026 token incident · self-host |  | Experimental |

## Knowledge plane

- style: plane

### L5 · Memory service (part of L6)

- duty: policy-gated writes, erasure by person
- design: A governed record class stored in L6: write gate, subject index, erasure and a snapshot per run. Built last.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L5-aws-agentcore-memory | AgentCore Memory | inside its own runtime | AWS | Strategic |
| L5-gcp-vertex-memory-bank | Memory Bank | Agent Engine | Google Cloud | Strategic |
| L5-zep | Zep / Graphiti | Graphiti self-hosted |  | Tactical |
| L5-mem0 | Mem0 | OSS behind a firm memory API |  | Tactical |
| L5-cognee | Cognee | in-estate only |  | Tactical |
| L5-supermemory | Supermemory | proprietary memory + knowledge API |  | Experimental |
| L5-letta | Letta | agent harness |  | Experimental |
| L5-langmem | LangMem | no release since Oct 2025 |  | Experimental |

### L6 · Retrieval & knowledge stores

- duty: derived, entitlement-filtered, rebuildable index
- design: Hybrid search inside a platform you already run; a dedicated vector engine only when a load test proves the need.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L6-elasticsearch | Elasticsearch | hybrid + document-level security |  | Strategic |
| L6-milvus-zilliz | Milvus / Zilliz | very large corpora |  | Strategic |
| L6-pgvector | PostgreSQL + pgvector | where Postgres is standard |  | Strategic |
| L6-qdrant | Qdrant | dedicated engine after a load test |  | Strategic |
| L6-mongodb-atlas-vector-search | MongoDB Vector Search | GA self-managed too |  | Strategic |
| L6-pinecone | Pinecone | managed · BYOC |  | Tactical |
| L6-weaviate | Weaviate | licence in transition |  | Tactical |
| L6-s3-vectors | S3 Vectors | AWS cost tier · no BM25 |  | Tactical |
| L6-turbopuffer | turbopuffer | many tenants · BYOC only |  | Tactical |
| L6-chroma | Chroma | prototypes and harnesses |  | Tactical |

### L7 · Retrieval optimisation

- duty: pinned embed + rerank, hybrid fusion, eval gate
- design: Choose models by in-domain evaluation; pin every version; keep raw text so a model switch is a re-embed, not a rebuild.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L7-sentence-transformers | Sentence Transformers | self-hosting and fine-tuning toolkit |  | Strategic |
| L7-gemini-embedding | Gemini Embedding 2 | EU endpoint excludes the UK | Google Cloud | Strategic |
| L7-cohere | Cohere Embed 5 + Rerank | private deployment |  | Tactical |
| L7-openai | OpenAI text-embedding-3 | text baseline |  | Tactical |
| L7-jina | Jina AI | Elastic-owned · CC-BY-NC weights |  | Tactical |
| L7-qwen3-embedding | Qwen3 Embedding | self-host after review |  | Tactical |
| L7-voyage | Voyage AI | MongoDB-owned |  | Tactical |
| L7-nvidia-nemo-retriever | NVIDIA NeMo Retriever | NVIDIA estates |  | Tactical |

### L8 · Ingestion & data preparation

- duty: approved sources, ACLs and lineage on every chunk
- design: A built control envelope (source register, classification, parse manifest, lineage, incremental indexing) around replaceable parsers.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L8-docling | Docling | default engine · LF AI & Data |  | Strategic |
| L8-unstructured | Unstructured | ACL-aware connectors |  | Strategic |
| L8-google-document-ai | Google Document AI | processor region confirmed | Google Cloud | Strategic |
| L8-mistral-ocr | Mistral OCR 4.1 | pin the model ID |  | Tactical |
| L8-llamaparse | LlamaParse | parse and extract only |  | Tactical |
| L8-firecrawl | Firecrawl | AGPL server · cloud with ZDR |  | Tactical |
| L8-reducto | Reducto | hard documents |  | Tactical |
| L8-apify | Apify | public data only |  | Tactical |
| L8-crawl4ai | Crawl4AI | pre-1.0 · pilots |  | Experimental |
| L8-mineru | MinerU | licence thresholds apply |  | Experimental |

## Evaluation & observability plane

- style: eval
- subtitle: L9 joins C8 as one evidence plane with two owners

### L9 · Evaluation & observability plane

- duty: evidence for every layer, from day one
- design: One firm-owned OpenTelemetry spine, Git-versioned evaluation sets, one platform of record, and two red-team tools, one independent of the model vendor.

| ID | Product | Note | Cloud | Tier |
|---|---|---|---|---|
| L9-mlflow-genai | MLflow GenAI | where an ML platform exists |  | Strategic |
| L9-langfuse | Langfuse | ClickHouse-owned · self-host |  | Strategic |
| L9-langsmith | LangSmith | LangGraph estates · BYOC, EU |  | Strategic |
| L9-opik | Opik | Comet · Apache-2.0 |  | Tactical |
| L9-arize-ax | Arize AX | Dynatrace-owned |  | Tactical |
| L9-deepeval | DeepEval | CI metric library |  | Tactical |
| L9-promptfoo | Promptfoo | red-teaming · OpenAI deal announced |  | Tactical |
| L9-arize-phoenix | Arize Phoenix | Dynatrace-owned · ELv2 |  | Tactical |
| L9-wandb-weave | W&B Weave | CoreWeave-owned |  | Tactical |
| L9-braintrust | Braintrust | eval-led teams |  | Tactical |
| L9-datadog-agent-observability | Datadog Agent Observability | Datadog APM estates |  | Tactical |

## Footer: The architecture in one sentence

Build a firm-owned control and evidence plane first; run regulated work as deterministic workflows with one bounded model step and a named human approver; consume models as a two-vendor portfolio through the primary cloud; treat every product beneath that plane as replaceable.

- **One gateway of record** for all model, tool and agent traffic: in region, deployed twice, failing closed.
- **Every agent a registered identity**, acting for a named person through short-lived tokens; deny by default.
- **One privacy service** at six points: ingestion, prompt, tool results, output, memory writes and trace export.
- **Git as the configuration of record**: prompts, model pins and tool lists released as one approved manifest.
- **Build order:** governance and evaluation, then models through the gateway, retrieval, workflows, tools — memory last.

## Footer: How to read it

- Tiers are for a regulated asset manager, scored on one eight-criterion rubric with regulated-FS weights. A Strategic tier carries its condition; the condition is the decision.
- Cloud-tagged items are alternatives chosen by primary cloud, not a shopping list.
- Disclosure: researched and drafted with an Anthropic model. Anthropic items were scored on the same rubric; their tiers were set by the reader, and an independent alternative is named for each.
- Personal research, not any firm’s platform. Every tile is backed by sourced facts in the dataset and the product appendix.

## Source

Source: Enterprise GenAI Full-Stack Architecture review, October 2026 — 05_Data/products.json (tiers), 06_References/bibliography.xlsx (sources). Product names are trademarks of their owners; no logos used.
