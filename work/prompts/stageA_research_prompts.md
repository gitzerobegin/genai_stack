# Stage A: research agent prompts (as executed on 7 October 2026)

Each prompt was run as a background `general-purpose` subagent. All eight point to the shared brief `work/stage0/05_stageA_research_brief.md`. Follow-up ("gap-filling") prompts are in `stageA_followup_prompts.md`.

---

## A1: L9 + L8

```text
You are Stage A research agent ① for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A1, STREAM_FOLDER = A1_L9_L8
Outputs: work/stageA/A1_L9_L8/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A1/

Scope — products (one record each; ids like L9-langfuse):
L9 Evaluation & Observability (8): Langfuse; LangSmith (LangChain); Braintrust; Arize Phoenix (open source); DeepEval (Confident AI); Promptfoo; Opik (Comet); Arize AX (commercial Arize platform — the graphic's "Arize – RAG metrics").
L8 Data extraction & ingestion (9): Firecrawl; Docling (IBM-originated, check governance e.g. LF AI); LlamaParse (LlamaIndex / LlamaCloud); Crawl4AI; MinerU (OpenDataLab); Reducto; Mistral OCR (current version); Unstructured (open-source lib vs Unstructured Platform); Apify.

Ambiguities you own: A4 (Phoenix "Atrace"), A8 (Arize vs Phoenix), A18 (Opik/Comet).
Hypotheses evidence you own: H7 (ingestion: lineage, classification, PII/DLP, permission/ACL metadata sync, incremental indexing — what do Unstructured, Reducto, LlamaCloud, Docling, Firecrawl actually offer?) and H8 (OpenTelemetry GenAI semantic conventions status as of 2026, OTel/OpenInference support in each L9 product, eval-in-CI, online evals).

Specifically check for each product: acquisitions or ownership changes in 2025–2026 (several eval/observability start-ups have been acquired — verify, do not assume), licence (MIT/Apache/ELv2/proprietary; open-core splits), self-hosting options, SOC 2 / ISO 27001 / HIPAA claims from trust centres, EU data region, pricing (dated). For PyPI-distributed tools (langfuse, deepeval, arize-phoenix, opik, docling, crawl4ai, mineru, unstructured, promptfoo is npm) use https://pypi.org/pypi/<pkg>/json for latest version + release date + licence.

Add up to 3 clearly material missing products per layer (e.g. Weights & Biases Weave, MLflow GenAI, Datadog LLM Observability, Azure Document Intelligence, AWS Textract, Google Document AI) only if material, with original_label null.

Finish with the ≤300-word summary described in the brief.
```

## A2: L7 + L6

```text
You are Stage A research agent ② for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A2, STREAM_FOLDER = A2_L7_L6
Outputs: work/stageA/A2_L7_L6/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A2/

Scope — products (one record each; ids like L7-cohere):
L7 Embeddings & reranking (10): OpenAI embeddings (graphic says "Embeddings 3"); Gemini Embedding (graphic "Embedding 2"); Voyage AI (graphic "Voyage-3"; verify ownership — reported MongoDB acquisition — and current model versions); Cohere Embed + Rerank (graphic "Embed v3 + Rerank"; current versions); Qwen3 Embedding / Qwen3 Reranker (Alibaba); Jina AI embeddings + reranker (graphic "v3"; verify current versions and any ownership change); Sentence-Transformers / SBERT (current maintainer, version via PyPI sentence-transformers); NVIDIA NeMo Retriever / NIM embedding & reranking ("NVIDIA Embed"); "EthicalAgents" (embeddings); "Ragoos" (RAG re-rankers).
For EthicalAgents and Ragoos: search seriously (several query variants, extended mode). If no credible primary source exists, create a record whose fields are "Not publicly verified", flag "Not publicly verified", and document every search you tried in notes.md. Do not invent a company.
L6 Vector & retrieval stores (10): PostgreSQL + pgvector (also note pgvectorscale / pgvecto.rs / VectorChord status); Pinecone; Qdrant; Milvus (open source) + Zilliz Cloud; Weaviate; turbopuffer; Elasticsearch (Elastic) — also note OpenSearch as a fork alternative; MongoDB Atlas Vector Search (incl. self-managed / Community availability); Chroma (OSS + Chroma Cloud); Amazon S3 Vectors (GA status, limits, pricing).

Ambiguities you own: A2, A3, A12, A13, A14, A16.
Hypotheses evidence you own: H5 (is "vector database" still the right abstraction? hybrid BM25+vector, full-text, vector features in general DBs, object-store vectors, vendor repositioning) and H6 (vendors shipping both embed and rerank; rerank built into vector DBs e.g. Pinecone/Elastic/Weaviate; late interaction ColBERT/ColPali; Matryoshka & quantised embeddings; multimodal embeddings).

For each product check: current version/models with dates, licence, deployment (SaaS / BYOC / self-hosted / on-prem), SOC 2 / ISO 27001 / HIPAA from trust centres, EU/UK region availability, CMK/BYOK, SSO/RBAC/audit logs, pricing (dated), acquisitions/funding 2025–2026, MTEB/benchmarks only if from primary or the MTEB leaderboard itself.

Add up to 3 clearly material missing products per layer only if material (e.g. Azure AI Search, Vertex AI Vector Search/RAG Engine, OpenSearch, Oracle AI Vector Search; Mixedbread, Google/Amazon rerankers), with original_label null.

Finish with the ≤300-word summary described in the brief.
```

## A3: L5 + L4

```text
You are Stage A research agent ③ for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A3, STREAM_FOLDER = A3_L5_L4
Outputs: work/stageA/A3_L5_L4/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A3/

Scope — products (one record each; ids like L5-mem0, L4-mcp):
L5 Memory (6): Mem0; Zep (incl. Graphiti); Letta (formerly MemGPT); Cognee; Supermemory; LangMem (LangChain).
L4 Tools, protocols & connectivity (8): Model Context Protocol (MCP — current spec version/date, governance (e.g. any move to a foundation), authorisation spec (OAuth 2.1, resource indicators), official registry); A2A protocol (Agent2Agent — governance under Linux Foundation? current version; relation to IBM ACP); Agent Skills (Anthropic-originated; is it now an open standard? who supports it?); Composio; Exa; Tavily (check any acquisition); Browserbase; E2B.

Conflict-of-interest reminder: MCP and Agent Skills originated at Anthropic, and you are an Anthropic model. Research them with the same scepticism as everything else and record independent adoption/criticism (including security criticisms of MCP) evenly.

Hypotheses evidence you own: H3 (agent identity, authorisation, tool governance: MCP auth spec, MCP gateways, A2A security model/agent cards signing, tool poisoning/prompt-injection incidents involving MCP, enterprise MCP registries/allow-listing) and H4 (memory vs retrieval: how each L5 product stores memory — vector + graph + KV, which databases underneath; memory types supported (episodic/semantic/procedural); deletion/retention/right-to-erasure features; built-in memory offered by model vendors (OpenAI, Anthropic memory tool, Google) and by agent platforms (e.g. AWS Bedrock AgentCore Memory, Vertex AI Memory Bank)).

For each product check: current version/date, licence, deployment options (SaaS / self-hosted / VPC), SOC 2 / ISO 27001 / HIPAA from trust centres, EU region, SSO/RBAC/audit logs, pricing (dated), funding/acquisitions 2025–2026. Use https://pypi.org/pypi/<pkg>/json for mem0ai, zep-cloud/graphiti-core, letta, cognee, langmem, e2b, composio, tavily-python, exa-py, mcp.

Add up to 3 clearly material missing products per layer only if material (e.g. AWS Bedrock AgentCore Memory/Gateway/Identity, Vertex AI Memory Bank, MCP gateways, Daytona/Modal sandboxes), with original_label null.

Finish with the ≤300-word summary described in the brief.
```

## A4: L3 + L2

```text
You are Stage A research agent ④ for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A4, STREAM_FOLDER = A4_L3_L2
Outputs: work/stageA/A4_L3_L2/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A4/

Scope — products (one record each; ids like L3-langgraph, L2-vllm):
L3 Agent frameworks & orchestration (9): LangGraph (+ LangGraph Platform / LangSmith Deployment naming); LlamaIndex (Workflows / agents); Pydantic AI; CrewAI (Crews vs Flows; CrewAI Enterprise/AMP); OpenAI Agents SDK; Claude Agent SDK (Anthropic; formerly Claude Code SDK — verify); Mistral Agents (Agents API / SDK — is there a distinct "Agents SDK"?); Vercel AI SDK (the triangle logo "AI SDK"); Microsoft Agent Framework (relationship to Semantic Kernel and AutoGen; GA status).
L2 Inference, serving & model access (9): Hugging Face (separate Hub, Inference Providers, Inference Endpoints, TGI status — e.g. maintenance mode?); OpenRouter; Together AI; Fireworks AI; Cerebras (chips vs inference cloud; IPO/funding status); Ollama (incl. any cloud offering); LM Studio (licence/commercial-use terms); vLLM (governance e.g. PyTorch Foundation; latest version via https://pypi.org/pypi/vllm/json); SGLang (governance; LMSYS/RadixArk).

Conflict-of-interest reminder: the Claude Agent SDK is Anthropic's and you are an Anthropic model. Same rubric, same scepticism; record its limitations and licence terms evenly.

Ambiguities you own: A7 (three "Agent SDK" tiles), A15 (AI SDK = Vercel), A17 (Mistral Agents SDK), A19 (Hugging Face product split).
Hypotheses evidence you own: H1 (serving vs inference optimisation vs gateway/routing: do vendors position these as distinct categories? optimisation tooling such as NVIDIA Dynamo, llm-d, LMCache, TensorRT-LLM, speculative decoding, quantisation; routers like OpenRouter vs enterprise gateways) and H2 (deterministic workflows vs autonomous agents: how LangGraph, Microsoft Agent Framework workflows, CrewAI Flows, Pydantic AI graphs, LlamaIndex Workflows, OpenAI/Claude SDKs separate them; durable execution integrations such as Temporal, DBOS, Restate; vendor guidance on "workflows vs agents").

For each product check: current version/date, licence, deployment options, SOC 2 / ISO 27001 / HIPAA from trust centres (for the hosted services: Together, Fireworks, Cerebras, OpenRouter, Hugging Face, LangSmith/LangGraph Platform, CrewAI), data retention / zero-data-retention policies, EU region, SSO/RBAC/audit logs, pricing (dated), funding/acquisitions 2025–2026. Use PyPI JSON for langgraph, llama-index, pydantic-ai, crewai, openai-agents, claude-agent-sdk, mistralai, agent-framework, vllm, sglang.

Add up to 3 clearly material missing products per layer only if material (e.g. Google ADK, AWS Strands/Bedrock AgentCore Runtime, Temporal; NVIDIA NIM/Dynamo, Groq, Amazon Bedrock/Azure AI Foundry/Vertex AI as managed model access), with original_label null.

Finish with the ≤300-word summary described in the brief.
```

## A5: L1 foundation models

```text
You are Stage A research agent ⑤ for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A5, STREAM_FOLDER = A5_L1
Outputs: work/stageA/A5_L1/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A5/

Scope — Layer 1 foundation-model vendors as MODEL FAMILIES, not single version labels (plan §2 rule 9). One record per vendor (ids like L1-openai), 11 records:
OpenAI (graphic "GPT-6"); Anthropic Claude (graphic "Opus 5.5"); Google Gemini (graphic gives no version); xAI Grok; DeepSeek (graphic "V4"); Alibaba Qwen (graphic "3.8"); Moonshot Kimi (graphic "K3"); Z.ai / Zhipu GLM (graphic "QI4" with Z logo, descriptor "Q4"); Mistral (graphic "Medium 3.1"); Google Gemma (graphic "2.9"); Meta Llama (graphic "Llama (new: Muse)").

For each vendor record, version_or_lineup must list the current lineup and tiers as of October 2026 (flagship / mid / small / reasoning / multimodal / coding / open-weight), each with release date and source, and state whether the graphic's label is correct, stale, or unverifiable.

The brief also names these examples, which must be verified, not trusted: "GPT-6 Astra/Sol/Luna", "Gemini 3.x", "DeepSeek V4.1", "Gemma 4", "Llama 4". Early searches suggest OpenAI's GPT-5.6 family (Sol/Terra/Luna, July 2026) exists and that "GPT-6 Astra" rests on thin, likely low-quality sources — verify both against openai.com (use WebSearch with allowed_domains ["openai.com"]) and record conflicts honestly. Do the same with each vendor's own domain (anthropic.com and docs.claude.com are directly fetchable; ai.google.dev / blog.google / deepmind.google, x.ai, api-docs.deepseek.com, qwen.ai / alibabacloud.com, moonshot.ai / kimi.com, z.ai / bigmodel.cn, mistral.ai, ai.meta.com / llama.com via search). Also check Hugging Face model cards via search for open-weight licences.

For each vendor also capture: open weights vs API-only and the licence (MIT, Apache 2.0, Llama licence, Gemma terms, Qwen licence, modified-MIT etc.); API pricing for flagship and small tiers (dated, per 1M tokens); availability via hyperscalers (AWS Bedrock, Azure AI Foundry, Google Vertex AI) — this matters for residency; data retention / zero-data-retention / training-on-customer-data policy; enterprise certifications (SOC 2, ISO 27001, ISO 42001) from trust centres; EU/UK data residency options; context window; jurisdiction / headquarters.

Also research the sovereignty and regulatory position of Chinese-origin models (DeepSeek, Qwen, Kimi, GLM) for a regulated UK/EU/US financial firm: government restrictions/bans (e.g. US state/federal device bans, Italy Garante, Korea, Australia), regulatory statements, the US Commerce/NIST CAISI evaluation of DeepSeek if any, and the distinction between using the vendor's hosted API (data in China) vs self-hosting the open weights. Record facts only; judgements come later.

Conflict-of-interest reminder: you are an Anthropic model. Research Anthropic with exactly the same rigour and scepticism; record limitations, pricing and any controversies evenly. Note: the session context indicates "Claude Opus 5.5" exists, but you must still source it from anthropic.com/docs.claude.com.

Ambiguities you own: A1, A5, A6, A9, A10, A11.

Finish with the ≤300-word summary described in the brief.
```

## A6: Controls C1–C4

```text
You are Stage A research agent ⑥ for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A6, STREAM_FOLDER = A6_C1_C4
Outputs: work/stageA/A6_C1_C4/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A6/

These are cross-cutting enterprise CONTROLS missing from the original graphic, so original_label is null for every record. The candidate products below are candidates to verify, not final picks; add other relevant products you find (at most 2 extra per control, only if material). Records may be products, open specifications or named patterns; set category accordingly. Ids like C1-litellm.

C1 AI / LLM gateway (routing, fallback, quotas, caching, policy, logging, provider abstraction): LiteLLM (proxy; open source vs enterprise); Portkey (check any acquisition); Kong AI Gateway; Cloudflare AI Gateway; Azure API Management AI gateway capabilities; AWS equivalent (e.g. Bedrock cross-region inference / AgentCore Gateway / API Gateway patterns — find what AWS actually offers); Google Apigee AI gateway / Vertex equivalent.
C2 Guardrails (input/output controls, jailbreak protection, content safety): NVIDIA NeMo Guardrails; Guardrails AI; Meta Llama Guard (current version) / Prompt Guard / LlamaFirewall; Amazon Bedrock Guardrails; Azure AI Content Safety (Prompt Shields).
C3 DLP / PII (detection, masking, tokenisation, residency): Microsoft Presidio; Google Sensitive Data Protection (Cloud DLP); Microsoft Purview (DSPM for AI); Protegrity; Skyflow.
C4 Identity & access for agents (agent identity, delegated authority, RBAC/ABAC, OAuth, workload identity, least privilege): Microsoft Entra Agent ID; Okta / Auth0 for AI Agents (incl. Cross App Access); SPIFFE/SPIRE; OAuth 2.1 / MCP authorisation spec (and related IETF drafts for agent identity/on-behalf-of); policy engines OPA and AWS Cedar (incl. Amazon Verified Permissions / Bedrock AgentCore Policy if real).

Hypotheses evidence you own: H1 (gateway promoted to control plane: what gateway products actually provide — policy, quotas, budgets, guardrail hooks, logging, semantic caching, MCP gateway features) and H3 (agent identity, authorisation and tool governance sub-layer: what exists today, maturity, standards work).

For each record: current version/status/GA vs preview (dated), company and any acquisitions 2025–2026 (verify; e.g. reported acquisitions of AI-security/gateway start-ups), licence, deployment options (SaaS / self-hosted / VPC), SOC 2 / ISO 27001 from trust centres, EU region, SSO/RBAC/audit logs, pricing (dated). Use PyPI JSON for litellm, nemoguardrails, guardrails-ai, presidio-analyzer.

Finish with the ≤300-word summary described in the brief.
```

## A7: Controls C5–C8

```text
You are Stage A research agent ⑦ for an enterprise GenAI stack review. Today is 7 October 2026.

FIRST read the shared brief and follow it exactly: /home/user/genai_stack/work/stage0/05_stageA_research_brief.md (it tells you which other files to read, the schema, sourcing/archiving rules, and the restricted network).

Your stream: STREAM = A7, STREAM_FOLDER = A7_C5_C8
Outputs: work/stageA/A7_C5_C8/{products.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A7/

These are cross-cutting enterprise CONTROLS missing from the original graphic, so original_label is null for every record. The candidate products below are candidates to verify, not final picks; add other relevant products you find (at most 2 extra per control, only if material). Records may be products, open specifications or named patterns; set category accordingly. Ids like C8-validmind.

C5 Prompt & config management: Langfuse Prompt Management (feature of Langfuse — another agent profiles Langfuse as a whole; keep this record to the prompt-management capability); LangSmith Prompt Hub / prompt management; PromptLayer; LaunchDarkly AI Configs; Git-based prompts-as-code pattern (e.g. Promptfoo configs, .prompty, Dotprompt — find what is documented).
C6 AI FinOps: gateway-native cost tracking (pattern — e.g. LiteLLM/Portkey spend tracking, cloud provider cost tags); Helicone (check any acquisition/status); Vantage; CloudZero; FinOps Foundation FOCUS specification and FinOps for AI guidance; chargeback patterns.
C7 AI security (secrets, supply chain, sandboxing, prompt injection, exfiltration, agent abuse): Lakera (verify reported acquisition by Check Point); Palo Alto Networks Prisma AIRS (incl. Protect AI acquisition); HiddenLayer; HashiCorp Vault (IBM); model/package scanning (e.g. ModelScan, picklescan, Hugging Face malware scanning, Protect AI Guardian, safetensors) — and check whether other AI-security start-ups (e.g. Prompt Security, CalypsoAI, Robust Intelligence, Pangea) were acquired 2025–2026.
C8 Model risk, governance & auditability: ValidMind; Credo AI; IBM watsonx.governance; ModelOp; Collibra AI Governance; OpenLineage (LF AI & Data spec; Marquez). Also consider ServiceNow AI Control Tower or OneTrust AI governance only if material.

Hypotheses evidence you own: H7 (lineage — OpenLineage adoption and any GenAI/RAG lineage extensions; classification/PII integration in governance tools) and support for H8 (governance tools that consume eval/monitoring evidence).

For each record: current version/status (dated), company and any acquisitions 2025–2026 (verify; never assume), licence, deployment (SaaS / self-hosted / VPC / on-prem), SOC 2 / ISO 27001 / ISO 42001 from trust centres, EU region, SSO/RBAC/audit logs, pricing (dated), and for C8 tools: explicit support claims for SR 11-7, PRA SS1/23, EU AI Act, NIST AI RMF, ISO 42001 (record as vendor claims). Use PyPI JSON for openlineage-python, modelscan, validmind, promptlayer, helicone where they exist.

Finish with the ≤300-word summary described in the brief.
```

## A8: Regulation and standards

```text
You are Stage A research agent ⑧ (Regulation and standards) for an enterprise GenAI stack review aimed at a regulated asset manager (UK/EU/US exposure). Today is 7 October 2026.

FIRST read the shared brief and follow it (sourcing, archiving, labels, restricted network): /home/user/genai_stack/work/stage0/05_stageA_research_brief.md. Your output schema differs from the product schema — see below. Also read plan §10 (POV 2) in inputs/Enterprise_GenAI_Stack_Consolidated_Plan_v4.3.md.

Your stream: STREAM = A8, STREAM_FOLDER = A8_Regulation
Outputs: work/stageA/A8_Regulation/{regulatory_facts.json,notes.md,sources.csv}; archive into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A8/ (and PDFs to Enterprise_GenAI_Stack_Oct2026/06_References/originals/ via tools/snapshot.py where a host is fetchable; most regulator hosts are blocked in this environment — then use save_extract.py and cite by link).

regulatory_facts.json = array of records:
{"id":"R-EUAIA", "instrument": fact, "jurisdiction": fact, "issuer": fact, "type": fact (law/regulation/supervisory statement/guidance/standard/framework), "status_and_dates": fact (in force / applies from / any amendments or proposed delays, with dates), "key_obligations": fact (list), "relevance_to_genai_agents_asset_mgmt": fact or Architectural judgement (label honestly), "stack_layers_affected": ["L9","C8",...], "evidence_artefacts_expected": fact (what a firm must be able to show), "sources": [...], "stage_a_notes": ""}
(fact = {"v","label","src","conf"} per the schema file.)

Instruments to cover (verify current status as of October 2026 — do not rely on memory; some have been revised, delayed or superseded):
1. US SR 11-7 (Fed/OCC model risk guidance) — check whether it has been revised, replaced or supplemented by 2026, and US agency statements on AI.
2. PRA SS1/23 model risk management principles (effective date; how it treats AI/LLMs).
3. EU AI Act — full implementation timeline (prohibitions, AI literacy, GPAI obligations Aug 2025, high-risk Aug 2026/2027), status of the Digital Omnibus / any postponement of high-risk obligations, GPAI Code of Practice, provider vs deployer obligations, Annex III categories relevant to financial services (creditworthiness, insurance pricing, employment), and transparency obligations (Art. 50).
4. DORA — application date, ICT third-party risk, register of information, CTPP designations (have any cloud/AI providers been designated as critical ICT third-party providers? when?).
5. UK critical third parties regime (BoE/PRA/FCA) — any HMT designations to date.
6. PRA SS2/21 outsourcing & third-party risk; FCA SYSC 8; EBA outsourcing guidelines — relevance to AI providers; exit planning.
7. Data residency/transfers: UK GDPR & Data (Use and Access) Act 2025; EU–UK adequacy status; EU–US Data Privacy Framework status (any court challenges); relevance to LLM API processing locations.
8. NIST AI RMF 1.0 and the Generative AI Profile (NIST AI 600-1); any 2025–2026 updates.
9. ISO/IEC 42001 (and 42005/42006 if published).
10. OWASP Top 10 for LLM Applications (2025 version) and OWASP Top 10 for Agentic Applications (verify name/date).
11. FCA and PRA/Bank of England AI statements 2024–2026 (e.g. FCA AI update, AI Lab / live testing, BoE/FCA AI survey, any 2026 statements on agentic AI); also IOSCO/FSB/ESMA statements on AI in asset management if material.
12. Any SEC/US developments relevant to AI use by investment advisers (e.g. withdrawn predictive data analytics rule) — facts only.

Also collect, as sourced bullets in notes.md, the evidence for H8 (regulatory expectations of ongoing monitoring) and for how an LLM or agent fits the definition of a "model" under SR 11-7 / SS1/23.

Label discipline is critical: regulatory dates and statuses must be Verified fact from regulator/official journal sources wherever possible; law-firm briefings are "Reported" (independent-technical) and acceptable as corroboration.

Finish with the ≤300-word summary described in the brief (instruments count, sources, the 5 most important regulatory facts for the architecture, top unverifiable items).
```
