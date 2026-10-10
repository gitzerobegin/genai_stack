# Ambiguity resolutions (plan §3; inventory A1–A19)

| | |
|---|---|
| **As of** | 8 October 2026 |
| **Basis** | Stage A notes, section (b) of each stream, and the Stage A′ verification logs |

Source IDs resolve in `Enterprise_GenAI_Stack_Oct2026/06_References/bibliography.xlsx`.

## Resolved

| # | Entry in graphic | Resolution | Confidence | Key sources |
|---|---|---|---|---|
| A1 | "QI4" (Z logo), "Q4" | **Z.ai GLM family.** No model named QI4 or Q4 exists, so the label is garbled. Current models: GLM-5.3 (API mid-August 2026), GLM-5.3-Flash (26 August 2026, MIT) and GLM-5.2 (open weights, June 2026). | Family: high. Label: not publicly verified. | A5-S038, A5-S041, A5-S042, A5-S047, V2-S016, V2-S021 |
| A4 | "Phoenix – Atrace" | **Arize Phoenix.** "Atrace" is most likely a garbled "Arize trace/tracing". Two corrections to the graphic: Phoenix is Elastic License 2.0, which is source-available, not OSI open source; and Arize is now part of Dynatrace (completed 1 October 2026). | High | A1-S044, A1-S045, A1-S048, A1-S066, V1-S005 |
| A5 | "Meta – Llama (new: Muse)" | **Muse is real.** Muse Spark comes from Meta Superintelligence Labs (April 2026), versions 1.1–1.3 are served through the Meta Model API (GA September 2026), and Muse Glimmer 30B has open weights under Apache 2.0. Llama 4 is still the latest *Llama*. | Medium | A5-S077, A5-S078, V2-S019 |
| A6 | "Gemini – Gemini" (no version) | **Gemini 3.x is the production lineup:** 3.1 Pro (preview), 3.8 Flash (GA 2 September 2026) and 3.5 Flash-Lite. **Gemini 4 Argon** was announced 30 September 2026 with restricted access. | Medium-high | A5-S027, A5-S030, A5-S031, A5-S032 |
| A7 | "Agent SDK" × 3 | **Three separate products:**<br>• OpenAI Agents SDK (MIT, provider-agnostic). Distinct from OpenAI's hosted Agents API (beta) and from Agent Builder (shuts down 30 November 2026).<br>• Claude Agent SDK, renamed from Claude Code SDK. Its repo licence is MIT but use is governed by Anthropic's Commercial Terms.<br>• Mistral: see A17. | High | A4-S005, A4-S027, A4-S028, A4-S054, A4-S055 |
| A8 | "Arize – RAG metrics" vs "Phoenix" | **Two products from one vendor.** Phoenix is self-hosted under ELv2. Arize AX is the commercial SaaS or private-deployment product. Both are now Dynatrace companies. "RAG metrics" understates AX. | High | A1-S045, A1-S046, A1-S047 |
| A9 | "Gemma 2.9" | **Wrong label.** No Gemma 2.9 exists. Gemma 4 is current (31 March / 2 April 2026, with 12B on 3 June 2026) under Apache 2.0. | High | A5-S034, A5-S035 |
| A10 | "OpenAI GPT-6" | **The label is correct, but GPT-6 is a family:**<br>• GPT-6 Astra: gated flagship, launched 3 September 2026. OpenAI says it is "not yet generally available"; AWS says it is GA on Bedrock.<br>• GPT-6 Sol and Luna: 22 September.<br>• GPT-6.1 Sol: 29 September.<br>• GPT-5.6 Sol/Terra/Luna (July 2026) is still offered.<br>There is no "GPT-6 Terra". | Medium-high. openai.com is blocked in this environment, so this rests on search extracts plus AWS and Microsoft pages. | A5-S001–S004, A5-S008, A5-S009, A5-S083 |
| A11 | Version labels | The table below gives each label's status. | Mixed | A5 notes (b); V2 log §3 |
| A12 | "Cohere Embed v3 + Rerank" | **Superseded twice.** Embed v4 (2025), then Embed 5 Pro/Fast (30 September 2026). Rerank 4 Pro/Fast (11 December 2025). | High | A2-S010–S013 |
| A13 | Voyage / Jina / OpenAI / Gemini embedding labels | **Voyage:** owned by MongoDB since February 2025; now Voyage 4 (January 2026); rerank-3 is in Preview.<br>**Jina:** owned by Elastic since 9 October 2025; now v5 models, with weights under CC-BY-NC-4.0.<br>**OpenAI "Embeddings 3":** still current.<br>**Gemini "Embedding 2":** correct; GA 22 April 2026. | High | A2-S001, A2-S004, A2-S006, A2-S023, A2-S033, V1-S024, V1-S025 |
| A14 | "NVIDIA Embed" | **NVIDIA NeMo Retriever** embedding and reranking NIM microservices (Embedding NIM 2.3). Production use needs NVIDIA AI Enterprise. | High | A2-S030, A2-S031, A2-S040, V1-S094 |
| A15 | "AI SDK" (triangle logo) | **Vercel AI SDK**: npm `ai` 7.x, Apache-2.0. | High | A4-S022, A4-S070 |
| A16 | "Milvus – vector search" | **Covered as one record:** open-source Milvus (3.0, "lake-native", Apache-2.0, LF AI & Data) plus the managed Zilliz Cloud ("Vector Lakebase", BYOC). | High | A2-S054, A2-S117–S120 |
| A17 | "Mistral Agents SDK" | **No distinct product by that name.** Mistral offers an Agents API, called through the `mistralai` SDKs, plus Mistral Workflows, a beta built on Temporal. Proposed relabel: "Mistral Agents API (+ Workflows)". | High | A4-S007, A4-S057, A4-S058, A4-S061 |
| A18 | "Opik – comet" | **Opik by Comet ML, Inc.** The whole platform is Apache-2.0. "comet" names the owner, not a capability. | High | A1-S050, A1-S071 |
| A19 | "Hugging Face – models & APIs" | **Four products in one tile:**<br>• Hub<br>• Inference Providers (a router)<br>• Inference Endpoints (managed dedicated serving)<br>• TGI: in maintenance mode, with its repository archived 21 March 2026. HF recommends vLLM or SGLang instead. | High | A4-S072–S083, V1-S054, V1-S055 |

## Not resolvable: recommended for removal from the stack

| # | Entry | Outcome |
|---|---|---|
| A2 | "EthicalAgents" (embeddings) | **Not publicly verified.**<br>• Six search variants by the A2 researcher, plus a repeat by verifier V1, found no embeddings product.<br>• The closest name match, Ethical Agentic AI Inc., is an AI-agent audit firm.<br>• No company was invented. (A2-S079) |
| A3 | "Ragoos" (RAG re-rankers) | **Not publicly verified.**<br>• Six search variants found no such product.<br>• Near-misses: RAGus.ai (scraper), RaGOO (genomics) and Ragie (RAG-as-a-service). (A2-S080) |

## A11: version labels in Layer 1

| Graphic label | Finding (8 October 2026) |
|---|---|
| OpenAI "GPT-6" | **Correct.** Tiered family: Astra, Sol, Luna, plus 6.1 Sol. |
| Claude "Opus 5.5" | **Correct, but not the top tier.**<br>• Claude Fable 5.1 (1 September 2026) is the top GA model.<br>• Mythos 5.1 is the same model with looser safeguards, for trusted access only.<br>• Sonnet 5.5 and Haiku 5.5 complete the family.<br>• Disclosure: the author is an Anthropic model; the same rubric applies. |
| Grok (no version) | Grok 4.7 (21 September 2026). The vendor is now part of SpaceX (2 February 2026). |
| DeepSeek "V4" | **Correct at generation level.**<br>• V4.1-Flash (10 September 2026) replaced V4-Flash.<br>• V4-Pro is still offered, after a planned phase-out was reversed.<br>• No V4.1-Pro exists. |
| Qwen "3.8" | **Correct (Reported).** The Qwen3.8 flagship weights are under a custom licence. |
| Kimi "K3" | **Correct.** Launched 16 July 2026 under the custom Kimi K3 License. |
| Mistral "Medium 3.1" | **Stale.** Medium 3.5 (April 2026) is current, and Large 4 is in preview (6 October 2026). |
| Gemma "2.9" | **Wrong.** Gemma 4 is current. |

## Brief examples checked (plan §2, rule 8)

| Example in the brief | Status |
|---|---|
| GPT-6 Astra / Sol / Luna | Verified |
| Gemini 3.x | Verified |
| DeepSeek V4.1 | Partly. V4.1-Flash exists; there is no V4.1-Pro. |
| Gemma 4 | Verified |
| Llama 4 | Verified as the latest Llama. Meta's current frontier family is Muse. |
