# Enterprise GenAI Full-Stack Architecture: Consolidated Research and Execution Plan (v4)

| | |
|---|---|
| **Version** | v4.3: consolidates *Execution Plan v3* and *Enterprise GenAI Full-Stack Research Plan*; LinkedIn series (§15) revised to 24 paired posts over 3 months (13 weeks), 220–300 words each |
| **Date** | 8 October 2026 |
| **Status** | For review. Not yet executed |
| **Selected options** | 1b multi-agent workflow · 2a all four formats · 3a full template for missing layers · all three points of view |
| **Baseline input** | `AI_Full_Stack.jpg`: "The Full AI Stack Explained", 9 layers, about 80 tools |

---

## Contents

1. Objective
2. Research quality rules
3. Baseline assessment of the original diagram
4. Architecture hypotheses to test
5. The nine layers: scope and research questions
6. Cross-cutting enterprise controls (missing layers)
7. Product research method
8. Scorecard and classification
9. Layer analysis framework
10. Three points of view
11. Worked example: performance-attribution commentary agent
12. Synthesis: the enterprise architect's answer
13. Execution: multi-agent workflow
14. Deliverables and packaging
15. LinkedIn thought-leadership series (new)
16. Final document structure
17. Checkpoints
18. Points to confirm before execution

---

## 1. Objective

Update the supplied *AI Full Stack* diagram into a **current (October 2026) enterprise GenAI reference architecture** that is **vendor-aware but not vendor-driven**.

This is not a label refresh. The research will determine:

- which layers still make architectural sense, and which should be renamed, merged, split or repositioned
- which products remain strategically relevant, and which have been acquired, deprecated, renamed, superseded or reduced to tactical use
- which enterprise capabilities are missing from the original diagram
- what an enterprise architect would actually select for a serious production platform today, and what they would deliberately not select

Every layer and product will be presented through three distinct lenses:

> **What the original diagram says** → **What the current ecosystem actually looks like** → **What the recommended enterprise architecture should be**

---

## 2. Research quality rules

| # | Rule | Application |
|---|---|---|
| 1 | **Current information** | Prioritise October 2026 status. Every fact is date-stamped. |
| 2 | **Primary sources first** | Priority order: (1) official product docs; (2) official company announcements; (3) official security and compliance documentation (trust centres); (4) regulatory sources; (5) high-quality independent technical sources. |
| 3 | **No invented facts** | Anything that cannot be verified is marked **"Not publicly verified"**. No assumptions. |
| 4 | **Fact vs judgement** | Every claim carries a label: **Verified fact** (primary source) · **Reported** (secondary source) · **Architectural judgement** · **Recommendation**. |
| 5 | **The diagram is a hypothesis** | The original diagram is a starting point, not the truth. |
| 6 | **No product-name inflation** | Nothing is recommended because it is fashionable or because it appears in the graphic. |
| 7 | **Architecture before vendors** | Define what each layer must achieve first, then select products. |
| 8 | **Nothing taken on trust** | Labels in the graphic and the examples in the brief (GPT-6 Astra/Sol/Luna, Gemini 3.x, DeepSeek V4.1, Gemma 4, Llama 4) are all verified against primary sources before use. |
| 9 | **Model vendors as families** | Layer 1 covers each vendor's current lineup and tiers, not one version label, so the analysis survives the next release. |
| 10 | **Conflict-of-interest disclosure** | The author is an Anthropic model. Claude, the Claude Agent SDK, MCP and Agent Skills are scored on the same rubric as everything else, with an independent alternative named wherever one of them is recommended. |
| 11 | **Respect access restrictions** | Paywalled or blocked sources are cited by link only and are never worked around. |

---

## 3. Baseline assessment of the original diagram

**Step 1: inventory.** Record the following from `AI_Full_Stack.jpg`:

- layers
- products
- product categories
- implied relationships between products
- apparent positioning of each product
- duplications and ambiguities
- missing enterprise capabilities

**Known ambiguities to resolve.** Each is resolved or flagged "Not publicly verified":

| Entry in graphic | Working hypothesis |
|---|---|
| "QI4" with Z logo | Z.ai (Zhipu) GLM family |
| "EthicalAgents" (embeddings) | Unknown, may not exist |
| "Ragoos" (RAG re-rankers) | Unknown, may not exist |
| "Phoenix – Atrace" | Arize Phoenix (open source) |
| "Meta – Llama (new: Muse)" | Verify Meta's current documented model family |
| "Gemini – Gemini" | No version given; cover the current Gemini lineup |
| "Agent SDK" × 3 (OpenAI, Anthropic, Mistral) | Treat as three separate products |
| "Arize – RAG metrics" vs "Phoenix" | Separate the open-source Phoenix product from the commercial Arize AX platform |

**Output: the "What changed since the original diagram" table.** Columns: original label → current reality → classification flag → source.

---

## 4. Architecture hypotheses to test

The 9-layer structure is tested, not assumed. Each hypothesis gets a verdict (keep / rename / merge / split / reposition) and a rationale.

| # | Hypothesis | Layers affected |
|---|---|---|
| H1 | L2 should split into **model serving → inference optimisation → model gateway/routing**, with the gateway promoted to a control-plane component | L2, C1 |
| H2 | An "agent framework" is not one layer. Architecture should distinguish **deterministic workflows** from **autonomous agents**. | L3 |
| H3 | Tools and protocols need an explicit **agent identity, authorisation and tool governance** sub-layer | L4, C4 |
| H4 | **Memory** may not be separate from retrieval and data architecture. Distinguish conversation, working, episodic, semantic, organisational and long-term memory from knowledge bases. | L5, L6 |
| H5 | "Vector database" should become **Retrieval / Knowledge Stores** | L6 |
| H6 | Embeddings and reranking form one **retrieval-optimisation** layer | L7 |
| H7 | Ingestion must include **lineage, classification, PII detection/DLP, access-control metadata and incremental indexing** | L8, C3 |
| H8 | Evaluation and observability are **cross-cutting**, not a downstream layer | L9 |

---

## 5. The nine layers: scope and research questions

**Analysis order: 9 → 1** (as originally requested). Layer numbering follows the graphic, with L1 as the base.

### L9 Evaluation and observability (treated as cross-cutting)

**Products (8):** Langfuse · LangSmith · Braintrust · Arize Phoenix · DeepEval · Promptfoo · Opik (Comet) · Arize AX. Others are added if found during research.

**Evaluation:**

- correctness, faithfulness and groundedness
- hallucination
- retrieval recall@k and precision@k
- answer relevance
- tool-call accuracy
- agent trajectory evaluation
- safety and red-teaming
- regression testing

**Observability:**

- traces, prompts, responses and tool calls
- latency, token usage and cost
- failures and model performance

**Production feedback:**

- user feedback, human evaluation and automated evaluation
- drift and regression detection
- model comparison

### L8 Data extraction, ingestion and web

**Products (9):** Firecrawl · Docling · LlamaParse · Crawl4AI · MinerU · Reducto · Mistral OCR · Unstructured · Apify

**Pipeline:** source → acquisition → parsing → OCR → structure extraction → cleaning → chunking → metadata → indexing

**Content types:**

- PDFs and scanned documents
- tables
- PowerPoint and Excel
- websites
- emails
- enterprise documents
- structured data
- multimodal documents

**Enterprise additions:** lineage, classification, PII detection and DLP, access-control metadata, incremental indexing

### L7 Embeddings and reranking

**Products (10):** OpenAI embeddings · Gemini Embedding · Voyage AI · Cohere Embed + Rerank · Qwen3 Embedding · Jina AI · Sentence-Transformers (SBERT) · NVIDIA NIM / NeMo Retriever · EthicalAgents (?) · Ragoos (?)

**Research:**

- embedding quality and multilingual performance
- domain adaptation and dimensionality (including Matryoshka embeddings and quantisation)
- retrieval quality, latency and cost
- cross-encoder reranking
- combining sparse and dense retrieval

**Key question:** should embeddings and reranking be treated as a single retrieval-optimisation layer? (H6)

### L6 Vector and retrieval stores

**Products (10):** PostgreSQL + pgvector · Pinecone · Qdrant · Milvus/Zilliz · Weaviate · turbopuffer · Elasticsearch · MongoDB Atlas Vector Search · Chroma · Amazon S3 Vectors

**Compare:**

- vector search and hybrid search
- metadata filtering, including performance under filters
- scale and latency
- operational complexity
- transactional integration and cloud-native integration
- multi-tenancy
- enterprise security

**Key question:** is "vector database" still the right abstraction? (H5)

### L5 Memory

**Products (6):** Mem0 · Zep · Letta · Cognee · Supermemory · LangMem

**Distinguish:**

- conversation memory
- working memory
- episodic memory
- semantic memory
- organisational memory
- long-term memory
- knowledge bases

**Also covers:** governance of what agents remember, including retention, the right to erasure, and contamination risk. (H4)

### L4 Tools, protocols and agent connectivity

**Products (8):** MCP · A2A · Agent Skills · Composio · Exa · Tavily · Browserbase · E2B

**Research:**

- tool invocation and external APIs
- browser automation and code execution
- connecting to enterprise systems
- identity propagation, permissions and sandboxing
- protocol interoperability

**Missing capabilities:**

- agent identity and authorisation
- secrets management
- delegated access
- tool governance
- least privilege

(H3)

### L3 Agent frameworks and orchestration

**Products (9):** LangGraph · LlamaIndex · Pydantic AI · CrewAI · OpenAI Agents SDK · Claude Agent SDK · Mistral Agents · Vercel AI SDK · Microsoft Agent Framework

**Assess:**

- agent state and state persistence
- workflows and planning
- tool calling
- human-in-the-loop
- multi-agent patterns
- durable execution and retries
- deterministic vs autonomous orchestration

**Key question:** is this a platform layer, or should architecture separate deterministic workflows from autonomous agents? (H2)

### L2 Inference, serving and model access

**Products (9):** Hugging Face · OpenRouter · Together AI · Fireworks AI · Cerebras · Ollama · LM Studio · vLLM · SGLang

**Research:** whether serving, optimisation and gateway/routing should be separated (H1).

**Gateway concerns:**

- routing, fallback and load balancing
- model selection
- rate limiting and caching
- cost controls
- policy enforcement
- observability
- provider abstraction

### L1 Foundation models / LLMs

**Vendors (11):** OpenAI · Anthropic (Claude) · Google Gemini · xAI (Grok) · DeepSeek · Alibaba Qwen · Moonshot (Kimi) · Z.ai (GLM) · Mistral · Google Gemma · Meta Llama

**Research:**

- frontier vs open-weight models
- general vs specialist models
- reasoning, multimodal, coding and small models
- model economics
- portability
- model-risk implications
- sovereignty and jurisdiction, e.g. the regulatory position of Chinese-origin models in a regulated firm

---

## 6. Cross-cutting enterprise controls (missing layers)

**Depth:** full layer template (§9) for each control.

**Products:** 4–6 per control. The products listed are **candidates to verify**, not final picks.

| # | Control | Scope | Candidate products |
|---|---|---|---|
| C1 | **AI / LLM gateway** | Routing, fallback, quotas, caching, policy enforcement, logging, provider abstraction | LiteLLM · Portkey · Kong AI Gateway · Cloudflare AI Gateway · cloud-native gateways (Azure API Management AI gateway, AWS/GCP equivalents) |
| C2 | **Guardrails** | Input/output controls, policy enforcement, jailbreak protection, content safety | NVIDIA NeMo Guardrails · Guardrails AI · Llama Guard / Prompt Guard · Bedrock Guardrails · Azure AI Content Safety |
| C3 | **DLP / PII** | Sensitive-data detection, masking, tokenisation, data residency | Microsoft Presidio · Google Sensitive Data Protection · Microsoft Purview · Protegrity · Skyflow |
| C4 | **Identity and access** | Agent identity, delegated authority, RBAC/ABAC, OAuth, workload identity, least privilege | Microsoft Entra Agent ID · Okta / Auth0 for AI agents · SPIFFE/SPIRE · OAuth 2.1 for MCP · policy engines (OPA, Cedar) |
| C5 | **Prompt and config management** | Prompt versioning, configuration, routing config, environment management | Langfuse Prompts · LangSmith Prompt Hub · PromptLayer · LaunchDarkly AI Configs · Git-based patterns |
| C6 | **AI FinOps** | Token economics, cost attribution, budgets, chargeback, optimisation | Gateway-native cost tracking · Helicone · Vantage · CloudZero · chargeback patterns |
| C7 | **AI security** | Secrets, supply chain, sandboxing, prompt injection, data exfiltration, agent abuse | Lakera · Palo Alto Prisma AIRS (Protect AI) · HiddenLayer · HashiCorp Vault · model/package scanning |
| C8 | **Model risk, governance and auditability** | Model inventory, validation, monitoring, approval, evidence, change management, lineage, policy, human approval, explainability, regulatory evidence | ValidMind · Credo AI · IBM watsonx.governance · ModelOp · Collibra AI Governance · OpenLineage |

**Total scope:** 80 graphic products plus about 40 control-plane products, roughly **120 product profiles**.

---

## 7. Product research method

For every product, the following is captured in a structured dataset of about 30 fields.

| Block | Fields |
|---|---|
| **A. Current status** | Current name, version or lineup, company, category, open source or proprietary, strategic direction |
| **B. Architecture** | What it actually does, where it sits in the stack, dependencies, integration model |
| **C. Deployment** | SaaS / managed cloud / VPC / private cloud / self-hosted / on-premises |
| **D. Enterprise characteristics** | SOC 2, ISO 27001, GDPR, data residency, encryption, SSO, RBAC, audit logs, enterprise support |
| **E. Commercial model** | Pricing, usage model, licence, free tier, enterprise pricing, infrastructure cost |
| **F. Ecosystem** | Integrations, community, adoption, maturity, developer experience |
| **G. Strategic risk** | Vendor lock-in, acquisition risk, funding risk, ecosystem dependency, proprietary API dependency, product maturity |
| **H. Assessment** | Key capabilities, strengths, limitations and risks, when to choose it, when to avoid it, nearest competitors (2–4), FS-specific note |
| **I. Classification** | Strategic / tactical / experimental, plus status flags (§8.2), with a one-line rationale |
| **J. Provenance** | Source URL for each fact, access date, confidence label |

---

## 8. Scorecard and classification

### 8.1 Weighted scorecard (1–5 per criterion)

| Criterion | Generic enterprise weight | Regulated FS weight (proposed) |
|---|---:|---:|
| Technical capability | 20% | 15% |
| Enterprise readiness | 15% | 15% |
| Security and compliance | 15% | 20% |
| Deployment flexibility (SaaS / VPC / self-hosted) | 15% | 15% |
| Ecosystem / integration | 10% | 5% |
| Reliability and maturity | 10% | 10% |
| Cost / total cost of ownership | 10% | 5% |
| Lock-in / portability / concentration risk | 5% | 15% |
| **Total** | **100%** | **100%** |

The FS weights move points towards security, portability and concentration risk, reflecting DORA third-party risk and SR 11-7 / PRA SS1/23 expectations. You can tune these at Checkpoint 1.

### 8.2 Classification

- **Strategic:** suitable as a core enterprise platform component.
- **Tactical:** useful for specific scenarios, but not a foundational dependency.
- **Experimental:** promising, but immature, changing fast, or unsuitable as a critical dependency.

**Status flags:** Deprecated · Acquired · Renamed · Superseded · Duplicated · Not recommended · Not publicly verified

---

## 9. Layer analysis framework

The same template applies to all 9 layers and all 8 controls.

1. **Responsibility.** The problem the layer owns, and how it hands off to the layers above and below.
2. **Why it matters.** What breaks when the layer is badly designed, with a concrete production failure story.
3. **Goals and KPIs.** For example: recall@k, precision@k, faithfulness, accuracy, p95 latency, throughput, availability, cost per task, token efficiency, failure rate, mean time to recover.
4. **How it works.** Technical mechanics and data flow, with a small diagram.
5. **Enterprise design principles.** Security, scalability, resilience, governance, observability, cost and portability. Includes patterns and anti-patterns.
6. **Product selection criteria.** What an architect should evaluate, mapped to the scorecard.
7. **Product deep dives.** Every product in the layer, per §7.
8. **Comparison table.** Products side by side, with scorecard results and key facts.
9. **Decision tree.** An "if X, choose Y" guide that an architect can actually use, rather than a catalogue. Example:

   ```text
   Need self-hosting?
     ├─ No  → Managed API / managed inference
     └─ Yes → GPU capacity available?
              ├─ Yes → vLLM / SGLang on own infrastructure
              └─ No  → Private-VPC managed inference
   ```

10. **Lock-in classification.** Acceptable / manageable (a thin abstraction is enough) / unacceptable (regulatory, operational, systemic or switching-cost risk).
11. **Regulated FS lens.** See §10.
12. **Worked-example slice.** See §11.
13. **Original → current → recommended.** A summary for the layer.

---

## 10. Three points of view

The views are layered rather than written three times. POV 1 is the main body of each section, POV 2 is a subsection in every layer, and POV 3 adds the worked example.

### POV 1: Generic enterprise

Priorities:

- reliability
- scalability
- security
- cost
- portability
- developer productivity

### POV 2: Regulated financial services

| Theme | Coverage |
|---|---|
| **Model risk management**: SR 11-7 and PRA SS1/23 | Governance, validation, monitoring, documentation, model inventory, change control; how an LLM or agent fits the definition of a "model" |
| **EU AI Act** | Risk classification, GPAI provider vs deployer obligations, current implementation timeline, documentation, transparency, monitoring |
| **Operational resilience**: DORA, PRA/FCA outsourcing | ICT third-party risk, critical third parties, exit plans |
| **Data residency** | UK, EU and regional processing, cross-border transfers, provider processing locations |
| **Auditability** | Complete trace of prompt, model version, data, tool calls, approvals and outputs; reproducibility and retention |
| **Vendor concentration risk** | Dependence on one LLM provider, cloud concentration, proprietary APIs, switching costs |
| **Standards** | NIST AI RMF, ISO/IEC 42001, OWASP Top 10 for LLM and agentic applications, FCA/PRA AI statements |

### POV 3: Regulated FS plus the worked example

Everything in POV 2, made concrete through the performance-attribution agent in §11.

---

## 11. Worked example: performance-attribution commentary agent

**Scenario (to confirm, see §18):** an agent drafts the monthly performance-attribution commentary for a multi-asset fund. It covers Brinson-style allocation and selection effects, currency, and benchmark-relative return. A portfolio manager or analyst reviews and approves the draft before release.

### 11.1 Request trace

```text
Authorised analyst request
      ↓  Identity / policy (C4, C2)
Agent orchestration (L3): deterministic workflow, not a free agent
      ↓
Authoritative portfolio data via read-only tools (L4 → attribution engine)
      ↓
Retrieval of prior commentary and house style (L8 → L7 → L6)
      ↓
LLM drafting via the gateway (L2/C1 → L1)
      ↓
Automated evaluation: numeric faithfulness, groundedness, style (L9)
      ↓
Human approval gate
      ↓
Final commentary
      ↓
Audit evidence pack (C8): prompt, model version, data snapshot, tool calls, evals, approver
```

### 11.2 Per-layer slice

| Layer | What it means for this agent |
|---|---|
| L8 | Parsing factsheets, prior commentaries and market notes |
| L7 / L6 | Retrieving comparable past commentary and the house style guide |
| L5 | Memory of fund-specific terminology and the PM's past edits, under governance |
| L4 | MCP tools onto attribution engine outputs (read-only); a sandbox for any calculation |
| L3 | Deterministic workflow graph with a human approval gate |
| L2 / L1 | Model routing; residency constraints on client data; fallback model |
| L9 | Evals that numbers match the attribution output; regression suite; reviewer feedback loop |
| Controls | Gateway logging, DLP on client identifiers, agent identity, prompt versioning, cost per commentary, model inventory and validation evidence |

### 11.3 Boundaries

**What the agent may do:**

- draft narrative text
- explain attribution effects
- reference market context from approved sources
- propose wording for human review

**What the agent must never do:**

- generate or alter authoritative numbers. Every figure must come from approved sources and be traceable.
- present inference as source data. Inference must always be distinguishable.
- publish without human approval when approval is mandatory
- produce an output that cannot be reproduced, or discard evaluation evidence. Both must be retained.

---

## 12. Synthesis: the enterprise architect's answer

> **"If I were building a serious enterprise GenAI platform today, which products would I actually select, and which would I deliberately NOT select?"**

### 12.1 Reference architecture

One diagram showing the 9 layers plus the 8 controls, with one request traced end to end.

### 12.2 Four reference stacks

Each stack lists what to build now and what **not** to build yet.

| Stack | Priority |
|---|---|
| **A. Regulated enterprise** | Self-hosting, private deployment, governance |
| **B. Cloud-native managed** | Speed, scalability, managed services, developer productivity |
| **C. Open-source first** | Portability, control, avoiding vendor lock-in |
| **D. Minimal start-small** | The minimum viable enterprise platform, with an explicit "do not build yet" list |

### 12.3 Build vs buy

For each major component:

- **Build** when differentiation, proprietary workflow, unique domain needs or strategic control justify it.
- **Buy** when the capability is a commodity, the infrastructure is complex, or the security, compliance and maintenance burden is high.
- **Hybrid** where appropriate.

### 12.4 Abstraction strategy

- **Abstract** model routing, observability, evaluation, credentials, policy, and retrieval interfaces.
- **Avoid over-abstracting** agent frameworks, simple API calls, application-specific orchestration, and straightforward database access.
- **Multi-vendor** is identified where it is truly necessary (models, gateway, evals, concentration risk) and avoided where it only adds complexity.

### 12.5 Vendor lock-in by layer

Each layer is classified as acceptable, manageable or unacceptable, with the rationale.

### 12.6 Day-one build order

| Phase | Focus |
|---|---|
| 0 | Governance and architecture |
| 1 | Evaluation and observability |
| 2 | Model access (gateway first) |
| 3 | Retrieval and knowledge |
| 4 | Agent workflows |
| 5 | Tools and enterprise integration |
| 6 | Memory |
| 7 | Advanced optimisation |

The roadmap includes a specific argument for why evaluation and observability must exist from day one rather than being added after production.

### 12.7 Final recommendation categories

Strategic choices · Tactical choices · Experimental choices · Products to avoid · Products to monitor

---

## 13. Execution: multi-agent workflow

The session guideline is fewer than 10 agents per workflow. The run is split into stages that are launched separately, with your review between them.

| Stage | Agents | Work | Output |
|---|---|---|---|
| **0. Baseline** | Lead architect (Claude) | Inventory the graphic, resolve ambiguities, set up the dataset schema, write the style guide | Inventory, schema, hypotheses H1–H8 |
| **A. Research** | 8 in parallel: ① L9+L8 · ② L7+L6 · ③ L5+L4 · ④ L3+L2 · ⑤ L1 · ⑥ Controls C1–C4 · ⑦ Controls C5–C8 · ⑧ Regulation and standards | Product facts per §7 (blocks A–G and J), with sources saved | Product fact JSON + source log + downloaded references |
| **A′. Verify** | 2 adversarial checkers | Re-check high-risk claims (versions, pricing, acquisitions, certifications, regulatory dates) against primary sources | Verified dataset + "What changed" table |
| **B. Write** | 8 parallel writers on the same template and style guide | Layer analysis (§9) + product deep dives (blocks H–I) + POV 2/3 subsections | Draft sections |
| **C. Synthesise** | Lead architect + 1 reviewer agent | Hypothesis verdicts, reference architecture, four stacks, build vs buy, abstraction, lock-in, roadmap, final recommendation; editorial pass for one voice and calibrated scoring | Final master content |
| **C2. LinkedIn series** | Lead architect (one voice, so no parallel writers) | 24-post, 13-week series (two posts a week) per §15, written in Bing's voice using the `linkedin-post-generator` voice rules and drawing only on verified facts from the dataset | LinkedIn section of the Word document + content calendar |
| **D. Package** | Lead architect | Doc, Word/PDF, explorer, deck, dataset, ZIP | Deliverables (§14) |

**Cost note:** a heavy run, likely several million tokens in total. This is an estimate, not a quote. Stage A is the largest cost. Cheapest lever: merge the Stage B writers from 8 to 4.

---

## 14. Deliverables and packaging

| # | Deliverable | Description |
|---|---|---|
| 1 | **Master architecture document** (Claude Doc, editable and shareable) | Executive summary, architecture, nine-layer analysis, controls, product analysis, comparison tables, decision trees, reference architectures, regulatory analysis, worked example, roadmap, **LinkedIn thought-leadership series (§15)** |
| 2 | **Word (.docx) + PDF** | Exported from the master, so identical to it, including the LinkedIn section |
| 3 | **Interactive explorer** (hosted page + offline HTML) | Click a layer; inspect, filter and compare products; view strategic/tactical/experimental status, deployment options and enterprise characteristics; worked-example trace |
| 4 | **Executive slide deck** | About 25–30 slides covering architecture, major technology shifts, recommended stack, decision framework, regulatory considerations and reference architectures; .pptx/PDF |
| 5 | **Technical appendix** | Full product-level analysis for about 120 products |
| 6 | **Product dataset** | XLSX + JSON, about 120 products × about 30 fields, with sources and scorecards |
| 7 | **Source archive** | See below |
| 8 | **LinkedIn content calendar** (XLSX) | 24 posts over 13 weeks: posting date and time, pair, theme, hook, status, cleared status, re-verify date, visual, link to the full post in the Word document. Also usable as a tracker for posts and responses. |
| 9 | **Final ZIP** | Everything above, also saved to a folder on your computer if you name one |

**Source archive contents:**

- **Originals** where legally and openly downloadable: regulatory texts, standards summaries, official PDFs and whitepapers.
- **Snapshots** of web pages: extracted text plus URL and access date.
- **`bibliography.xlsx`**: maps each claim to its source.

**ZIP layout:**

```text
Enterprise_GenAI_Stack_Oct2026/
├── 00_README.md          contents, method, as-of date, confidence legend
├── 01_Report/            Master_Architecture.docx, .pdf
├── 02_Appendix/          Product_Technical_Appendix.docx, .pdf
├── 03_Slides/            Executive_Deck.pptx, .pdf
├── 04_Explorer/          explorer.html (offline) + link.txt
├── 05_Data/              products.xlsx, products.json, scorecards.xlsx
├── 06_References/        originals/, snapshots/, bibliography.xlsx
└── 07_LinkedIn/          LinkedIn_Series.docx (standalone copy of §15), Content_Calendar.xlsx
```

---

## 15. LinkedIn thought-leadership series

### 15.1 Purpose

A three-month, ready-to-post series that turns the research into a public body of work. It positions you as an **agentic transformation leader** who combines technical depth with leadership judgement: someone who has thought through the full enterprise stack and its controls, including the regulated and operating-model realities, rather than someone who repeats vendor diagrams.

It will appear as a dedicated section in the Word document. A standalone copy and a content calendar go in the ZIP.

### 15.2 Voice and style

The series follows the `linkedin-post-generator` voice rules, extended for posts that combine technical content with leadership.

- **Governing rule:** share the lesson, credit the team, let the numbers do the bragging. No claims of brilliance.
- **Structure (technical + leadership):**
  1. **Hook** (1–2 lines): a concrete, surprising line.
  2. **The trap** (2–3 lines): what most teams get wrong at this layer.
  3. **The technical core** (4–6 lines): how the layer or control actually works, and the one metric that shows whether it is "good". Examples are recall@k, p95 latency or cost per task.
  4. **The leadership move** (2–4 lines): the decision, trade-off or operating-model change an architect or leader has to make.
  5. **The honest part** (1–2 lines): a mistake owned, or credit given.
  6. **Takeaway** (1–2 lines): a reusable principle, with a quiet invitation to reflect.
- **Format:**
  - **about 220–300 words**, longer than the skill's 120–200 default because these posts carry technical content
  - British spelling
  - no emojis and at most 2 hashtags
  - no headers or bullets inside the post
  - no engagement bait such as "Agree?" or "Comment below"
- **Story over claims.** Expertise shows through specific trade-offs, failure stories and decisions, not by stating that you're an expert.
- **No invented experience or metrics.** The research can supply the insight but not your lived experience. Each post therefore has:
  - an **anecdote slot** for a real experience of yours, with a prompt describing what kind of story fits
  - a **fallback version** written as an architectural observation, so the post works without a personal story

### 15.3 Series design: 3 months (13 weeks), paired posts

**Principle.** Every week has **two posts: one stack layer, then one related control**. The control post builds on that week's layer post, so each week reads as a pair: the capability, then the control that makes it safe in production.

**Cadence.** **Tuesday** (stack) and **Thursday** (control), at about 08:00 UK. Mid-week slots usually reach a professional audience best, and two posts a week is sustainable alongside a day job.

**Volume.** 24 planned posts plus a buffer week:

| Weeks | Phase | Posts |
|---|---|---|
| 1–8 | The stack and its controls | 16 |
| 9–12 | The architect's answer: memory, regulation, synthesis and close | 8 |
| 13 | Buffer, for a reactive post or a slipped week | 0–2 |

**Order.** Stack layers run 9 → 1, as originally requested, with one exception: **L5 Memory moves to week 9**. This mirrors the build-order roadmap (§12.6), where memory is built last. The move is deliberate and is explained in that post.

| Wk | Tue (stack / synthesis) | Thu (control / synthesis) | The pair's tension |
|---|---|---|---|
| **1** | **L9 Evals and observability** (opens the series) | **C8 Model risk, governance and audit** | Popular AI-stack diagrams age in months. The layer that ages slowest is the one most teams build last: evals added after go-live measure the damage, not the quality. → Your eval suite *is* your validation evidence. What SR 11-7-style thinking means when the "model" is an agent. |
| **2** | **L8 Ingestion** | **C3 DLP / PII** | Most "hallucinations" in enterprise RAG start in a PDF table parser. → Data residency and PII decisions are made at ingestion, not at the prompt. |
| **3** | **L7 Embeddings and reranking** | **C5 Prompt and config management** | Retrieval quality is a two-stage problem, and most teams tune only one stage. → Embedding versions and prompts are both production configuration, so they need versioning, review and rollback. |
| **4** | **L6 Retrieval stores** | **C7 AI security** | You may not need a vector database, but you do need retrieval you can measure. → Every retrieved document is untrusted input. Indirect prompt injection is a supply-chain problem. |
| **5** | **L4 Tools and protocols** | **C4 Agent identity and access** | MCP made connecting tools easy, and that is exactly why tool governance now matters. → "Who did this?" needs an answer when the actor is an agent. Least privilege for non-humans. |
| **6** | **L3 Orchestration** | **C2 Guardrails** | Most enterprise "agents" should be deterministic workflows with one judgement step. → Guardrails cannot fix a workflow that should never have been autonomous. |
| **7** | **L2 Inference and access** | **C1 AI gateway** | Self-hosting is a capacity and operating-model decision, not just a cost decision. → The most boring component is the one that makes model switching, and exit plans, possible. |
| **8** | **L1 Foundation models** | **C6 AI FinOps** | Treat models as a portfolio, not a bet. → Cost per task, not cost per token, is the metric executives understand. |
| **9** | **L5 Memory** (deliberately last) | **Regulated reality: EU AI Act and DORA** | What an agent remembers is a governance question before it is a technical one, which is why memory comes last. → Concentration risk turns multi-vendor from a preference into a requirement. |
| **10** | **The worked example** | **Start small** | What the attribution-commentary agent must *never* do matters more than what it can do. → The most valuable part of a reference architecture is the "do not build yet" list. |
| **11** | **Build vs buy** | **Where *not* to abstract** | Build where you differentiate, buy where you would only be maintaining. → Frameworks on top of frameworks. |
| **12** | **Which lock-in is acceptable** | **Close: what I'd select, and what I'd deliberately not select** | Some lock-in is a good trade, and the skill is knowing which. → The full stack on one page, plus a lesson about leading the transformation. |
| **13** | Buffer | Buffer | A reactive post on a market event, or a catch-up week if one slips |

**The worked example runs through the whole series.** The performance-attribution commentary agent is the recurring, generic illustration, so the 24 posts read as one connected story rather than 24 separate tips.

**Reactive templates.** 2–3 templates for market events such as a model launch, an acquisition or a regulatory milestone. Each links back to the relevant layer and can go into the week 13 buffer, or replace a Thursday slot if the timing matters.

### 15.4 What each post includes in the Word document

| Element | Content |
|---|---|
| Week, day and suggested date/time | Tuesday / Thursday, about 08:00 UK by default. Adjustable. |
| Pair link | The partner post (stack ↔ control) and a one-line bridge sentence linking them |
| Theme and link to the source section | Cross-reference to the layer or control in the master document |
| Tension | One line stating the angle |
| **Full post** (about 220–300 words) | Ready to paste |
| **Short variant** (about 120–150 words) | For a lighter week, or for reposting |
| Anecdote slot and prompt | Where your real experience goes, with what kind of story fits |
| Fallback | Version with no anecdote needed |
| Suggested visual | Diagram or carousel drawn from the deck or explorer, e.g. the layer diagram or decision tree |
| First comment | Optional sources and further-reading link, kept out of the post body |
| Hashtags | At most 2 |
| **Re-verify before posting** | Any product, version or regulatory fact in the post, flagged for re-check in the week before posting. Over 3 months, versions, pricing and regulatory dates will move, especially for posts in weeks 8–12. |
| Compliance check | See §15.5 |

### 15.5 Professional and compliance guardrails

As a senior employee of a regulated firm, you will likely need these posts to align with your employer's social-media and external-communications policy. Every post is therefore written to:

- read clearly as **personal views**, with no implication of employer endorsement or of any firm's actual vendor choices
- contain **no confidential or internal information**: no internal systems, client data, programme names or real internal metrics
- keep the **worked example generic and illustrative**, not a description of any real firm's platform
- discuss vendors **evenly and factually**, with no endorsement that could read as commercial promotion
- stay **pre-clearance ready**: the calendar includes a "cleared" status column. If your firm requires review, posts can be submitted in monthly batches (weeks 1–4, 5–8, 9–13), which keeps the series at least a month ahead of the clearance queue.

### 15.6 Quality checklist (applied to every post)

- The hook earns the next line without hype.
- The technical core is accurate and names one measurable signal.
- There is a leadership decision or reframe a reader could apply tomorrow.
- Team credit or an owned mistake is present, or there is a clear slot for one.
- Numbers stand without adjectives, and none are invented.
- 220–300 words, British spelling, no emojis, at most 2 hashtags, no engagement bait.
- The post links naturally to its pair partner.
- Facts are traceable to the verified dataset.
- The compliance guardrails in §15.5 are met.

---

## 16. Final document structure

```text
EXECUTIVE SUMMARY
├── What changed since the original architecture
├── Recommended 2026 enterprise architecture
├── What to keep · what to remove · what is missing
│
METHOD & QUALITY RULES (confidence legend, scorecard, classification)
│
9-LAYER ARCHITECTURE (analysed 9 → 1)
├── 9. Evaluation & Observability (cross-cutting)
├── 8. Data Extraction & Ingestion
├── 7. Embeddings & Reranking
├── 6. Retrieval / Knowledge Stores
├── 5. Memory
├── 4. Tools, Protocols & Connectivity
├── 3. Agent Orchestration
├── 2. Inference & Model Access
└── 1. Foundation Models
│
CROSS-CUTTING ENTERPRISE CONTROLS
├── C1 AI Gateway · C2 Guardrails · C3 DLP/PII · C4 Identity & Access
└── C5 Prompt/Config · C6 FinOps · C7 AI Security · C8 Model Risk, Governance & Audit
│
ARCHITECTURE HYPOTHESES: VERDICTS (H1–H8)
COMPARISON & DECISION FRAMEWORK
FINANCIAL SERVICES POV (SR 11-7, PRA SS1/23, EU AI Act, DORA, residency, concentration)
PERFORMANCE-ATTRIBUTION AGENT (end-to-end trace)
FOUR REFERENCE STACKS
BUILD vs BUY
ABSTRACTION STRATEGY & VENDOR LOCK-IN
IMPLEMENTATION ROADMAP (Phases 0–7)
FINAL RECOMMENDED ENTERPRISE STACK (select / don't select / monitor)
LINKEDIN THOUGHT-LEADERSHIP SERIES (24 paired posts over 13 weeks + reactive templates + calendar)
APPENDIX: PRODUCT DEEP DIVES (~120)
```

---

## 17. Checkpoints

Work stops at each checkpoint for your review.

| # | After | You review |
|---|---|---|
| CP1 | Stage 0 + A + A′ | Inventory, "What changed" table, ambiguity resolutions, control-plane product list, scorecard weights |
| CP2 | Layers 9–7 drafted | Depth, tone and scoring calibration. Adjust the template here, before it is applied to the remaining layers. |
| CP3 | Layers 6–4 + controls C1–C8 | Content |
| CP4 | Layers 3–1 + synthesis | Hypothesis verdicts, reference stacks, final recommendation |
| CP4b | First pair of LinkedIn posts (#1 L9 and #2 C8) | Voice, the 220–300-word technical + leadership structure, and the anecdote-slot approach, before the remaining 22 are written |
| CP5 | All formats + ZIP | Final package |

---

## 18. Points to confirm before execution

1. **Analysis order.** Write layers 9 → 1, as originally requested, or 1 → 9, matching the numbering in the attached research plan?
2. **Control-plane scope.** Are the 8 controls and their candidate products in §6 right? Add any vendors you want covered, kept generic.
3. **Scorecard weights.** Accept the generic weights from the research plan and the proposed FS weights in §8.1?
4. **Worked example.** Multi-asset fund with Brinson-style attribution, or equity-only, or fixed income (duration/curve attribution)?
5. **Deck audience.** MD/executive (story-led, decision-focused) or a technical architecture forum?
6. **Destination folder.** Which folder on your computer should the ZIP go to, if any?
7. **LinkedIn series.**
   - **(a) Start date and day:** default is the first Tuesday after delivery and sign-off, at about 08:00 UK.
   - **(b) Cadence:**
     - **(i)** 2 posts a week, Tuesday and Thursday, for 13 weeks, as in §15.3.
     - **(ii)** 3 posts a week: the same 24 posts finish in about 8 weeks, leaving a longer buffer.
     - **(iii)** 1 post a week: only the 18 core posts (stack, controls and close), over about 4.5 months.
   - **(c) Vendor names:** name vendors in posts, or keep posts vendor-neutral, with names only in the first comment?
   - **(d) Visuals:** include a carousel or image brief per post?

**To start:** reply **"approved, use a workflow"** with any changes, and Stage 0 begins.
