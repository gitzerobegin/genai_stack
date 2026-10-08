## 5. Memory

> **Executive summary.** This layer decides what an agent carries from one interaction to the next, where that state is stored, and who is allowed to change, inspect or erase it. Four things have changed since the original graphic. First, the independent products have moved apart: Mem0 removed every external graph store from its open-source build on 14 April 2026 and replaced it with entity linking, which is not a queryable graph [VF: A3-S053, A3-S081, V1-S043]; Zep deprecated its Community Edition, so Graphiti is the only open-source path [VF: A3-S059, V1-S044]; Letta pivoted to Letta Code, an agent harness, and retired its V1 server [VF: A3-S060, A3-S073, A3-S093]; and LangMem has had no release since 27 October 2025 [VF: A3-S006]. Second, the hyperscalers now ship memory as a platform feature: Amazon Bedrock AgentCore Memory has been GA since 13 October 2025 and Google's Memory Bank since December 2025 [VF: A3-S047, V1-S087, V1-S088]. Third, every product stores memory in ordinary vector, graph, relational or file stores [VF: A3-S053, A3-S003, A3-S005, A3-S064, A3-S006, A3-S073], so memory is a data-architecture problem as much as an agent feature [AJ]. Fourth, memory is now a named attack surface: OWASP's Agentic Top 10 includes memory and context poisoning (ASI06) [VF: B-L5-S001]. No product in this layer reaches Strategic tier [AJ]. **Recommendation:** treat agent memory as a governed record class held in the firm's own retrieval and data stores (L6), written only through an approved, logged write path with subject-scoped erasure and versioning. Build it last, after evaluation, gateway, retrieval, workflows and tools, as the plan's build order already says. Use the agent platform's native memory (AgentCore Memory or Memory Bank) where the runtime already lives there, and self-hosted Mem0 or Graphiti only behind the firm's own memory API [Rec].

### 5.1 Responsibility

**The problem this layer owns.** It manages state that outlives a single model call and is fed back into later calls [AJ]. That state is of different kinds, and the plan asks for them to be kept apart (plan §5, L5) [AJ]:

| Memory type | What it holds [AJ] | Typical lifetime [AJ] | Where it physically lives [AJ] | Product evidence |
|---|---|---|---|---|
| **Conversation** | The turns of the current dialogue | One session | Context window; session or event store | AgentCore short-term memory stores raw session events (messages, tool calls) [VF: A3-S111]; OpenAI's Conversations API persists conversation state as a durable object [VF: A3-S110] |
| **Working** | Scratchpad, plan, intermediate tool results for the task in hand | One task or run | Context window; orchestrator state (L3 checkpoint store, KV cache, Redis) | Letta tracks memory blocks and all context in a git-backed memory filesystem [VF: A3-S073]; Cognee uses a Redis-compatible cache [VF: A3-S005] |
| **Episodic** | Records of specific past events: "on 3 March the PM rejected this phrasing" | Months to years | Event log plus vector index; graph nodes with timestamps | Graphiti stores "episodes" with provenance [VF: A3-S003]; AgentCore offers an episodic extraction strategy [VF: A3-S111] |
| **Semantic** | Distilled facts and preferences: "Fund X calls its benchmark the 'reference index'" | Until contradicted or expired | Vector store plus relational fact table, or graph store | Mem0 stores facts in SQL, embeddings in a vector store and entities in an entity store [VF: A3-S053, A3-S080]; Memory Bank extracts facts and preferences and consolidates them [VF: A3-S109] |
| **Procedural** | How to do things: rules, refined prompts, skills | Versioned releases | Prompt and config store (C5), skill files, Git | LangMem includes prompt refinement to optimise agent behaviour [VF: A3-S006]; Mem0 lists procedural memory [VF: A3-S053] |
| **Organisational** | Shared, curated knowledge for a team or firm: glossaries, house style, approved positions | Records-policy lifetime | Document and knowledge stores (L6/L8), with owners and approval | No product here offers organisational approval workflows as a documented feature [NPV] |
| **Long-term (user/agent)** | Anything above that persists across sessions for a user, agent or entity | Policy-defined; often unbounded by default | Vector, graph and relational stores behind a memory API | AgentCore long-term records have no built-in time limit [VF: A3-S111]; Memory Bank TTL is optional and off by default [VF: A3-S109] |
| **Knowledge base** (not memory) | Authoritative, curated corpora: policies, factsheets, prior approved commentary | Records-policy lifetime | L6 retrieval stores fed by L8 ingestion | Out of scope for this layer; L6 and L8 own it [AJ] |

The useful distinction for an architect is not the cognitive label but **who writes the record and how authoritative it is** [AJ]. A knowledge base is written by an accountable owner through ingestion (L8). Memory is written by the agent, or by an extraction model, as a side effect of interactions. That makes memory the least authoritative and least reviewed data the agent reads, even though it is fed into the prompt in the same way as approved knowledge [AJ].

**Hand-offs.**
- **Up to L3 (orchestration):** the workflow decides when memory is read and when a write is proposed. Conversation and working memory are mostly L3's checkpoint state [AJ].
- **Down to L6/L7 (stores and embeddings):** long-term memory is physically a set of rows, vectors and graph edges in the same kinds of stores that serve retrieval [VF: A3-S053, A3-S003, A3-S005]. Embedding and reranking choices (L7) apply to memory recall too [AJ].
- **Sideways to the controls:** C3 (DLP/PII) screens what may be written; C4 (identity) scopes whose memory is read; C5 (prompt and config) holds procedural memory; C8 (governance) holds the retention schedule, erasure evidence and audit; L9 evaluates whether recalled memory helped or harmed [AJ].

**What the layer does not own.** It does not own authoritative business data. Numbers, holdings and client records come from systems of record through read-only tools (L4) and must never be served from memory [AJ].

### 5.2 Why it matters

A badly designed memory layer fails slowly and invisibly [AJ]. The agent's behaviour starts to depend on state that nobody reviewed: a mistaken "fact" extracted from one conversation is recalled in hundreds of later ones; a stale preference overrides a newer instruction; a client's name surfaces in another user's session because the scope key was too broad. Because memory is fed into the prompt like any other context, an injected instruction that lands in memory keeps working long after the original input has gone [AJ]. OWASP's GenAI Security Project describes memory and context poisoning (ASI06) in the same terms: attacker-controlled content that the system continues to trust over time, shaping later planning, tool use and behaviour [VF: B-L5-S001].

Memory also creates a regulatory object that did not exist before: a growing store of extracted personal and business information, created automatically, with no natural expiry [AJ]. AgentCore Memory long-term records have no built-in time limit, and AWS recommends a pruner using timestamp filters [VF: A3-S111]. Mem0's open-source extraction is now ADD-only, so memories accumulate rather than being overwritten [VF: A3-S081, A3-S053]. Graphiti invalidates old facts rather than deleting them, keeping history [VF: A3-S003]. Each design choice is defensible for recall quality, and each makes erasure and retention an explicit engineering task rather than a default [AJ].

Finally, memory breaks reproducibility [AJ]. A system whose output depends on what it has accumulated cannot be re-run to the same result unless the memory state at the time of the run was captured. That matters for model validation and for explaining a past output to a client or a regulator [AJ].

**Illustrative scenario [AJ].** A fund-reporting team enables "learn from feedback" memory on its commentary agent, using a hosted memory service with default settings. In month one, an analyst types a correction into the chat: "the currency effect was negative this month, not positive". The extraction model stores this as a durable fact about the fund: "currency effect: negative". Three months later, with the currency effect now positive in the attribution engine, the agent drafts "currency again detracted", because the recalled memory sits in the prompt next to the tool output and the model reconciles the conflict in the wrong direction. The numeric-faithfulness check catches the sign mismatch, but only for the sentence that contains a figure; two qualitative sentences pass. Separately, a client complaint in the same chat had mentioned a named individual, and the extraction model stored that too. When the client later exercises the right to erasure, the operations team finds that the memory store has no index by data subject, the long-term records have no expiry, and the vendor's deletion API works per record, not per person. The scenario is invented; it is not a reported incident. It shows three failures that the design in 5.4 and 5.5 prevents: memory used as a source of numbers, unscreened writes, and no subject-scoped lifecycle.

### 5.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Write precision | Share of memory writes a reviewer judges correct, useful and in policy | ≥0.95 for any memory read by a regulated workflow | Sampled human review of the write log |
| Policy-violating writes | Writes containing prohibited classes (client identifiers, special-category data, numbers presented as facts) | Zero reach the store; every block logged | C3 DLP verdicts on the write path, reconciled with store contents |
| Recall usefulness | Share of recalled memories that the eval judges relevant to the task | Rising trend; falls trigger review | L9 evaluation of recalled items in traces |
| Harmful-recall rate | Runs where recalled memory contradicted an authoritative source or a newer instruction | Zero tolerated for numeric content; any case is a defect | L9 contradiction check: memory versus tool output |
| Provenance coverage | Memories carrying source interaction, writer identity, timestamp, approval status and version | 100% | Schema validation on write |
| Erasure completion time | Request received to deletion confirmed across store, indexes, revisions and backups (backups "beyond use") | Within the one-month UK GDPR response window [VF: B-L5-S005], with an internal target well inside it | Erasure job logs and evidence in C8 |
| Retention conformance | Records older than their retention class that still exist | Zero | Scheduled reconciliation of record ages against the schedule |
| Reproducibility | Runs whose memory state can be reconstructed exactly (snapshot ID or version hash in the trace) | 100% for regulated outputs | Trace completeness check (L9) |
| Scope-leak incidents | Memory recalled outside its scope (user, fund, team) | Zero | Red-team tests and production sampling |
| Memory cost per task | Extraction LLM calls, embeddings, storage and retrieval per completed task | Budget per use case | Gateway (C1) and C6 cost attribution |

The erasure KPI deserves emphasis. The ICO expects erasure from live systems and steps to deal with backups, which may be put "beyond use" until overwritten [VF: B-L5-S005]. Its storage-limitation guidance expects periodic review and deletion or anonymisation of data no longer needed [VF: B-L5-S006]. Memory products do not do this by default, so the KPI measures a capability the firm must build [AJ].

### 5.4 How it works

Every memory system has a write path and a read path, and the governance sits almost entirely on the write path [AJ].

**Write path.**
1. **Capture.** The orchestrator passes interaction events (messages, tool calls, reviewer edits) to the memory service. AgentCore stores these as short-term events, with expiry configurable between 7 and 365 days per the API reference (the stated minimum conflicts between pages) [VF: A3-S111].
2. **Extraction.** An LLM proposes candidate memories. Memory Bank uses Gemini models to extract facts, preferences and context asynchronously [VF: A3-S109]. AgentCore offers semantic, summary, user-preference, episodic and custom strategies [VF: A3-S111]. Mem0's April 2026 algorithm uses single-pass ADD-only extraction with entity linking [VF: A3-S081]. Cognee can extract locally with a small model (GLiNER) without an LLM key [VF: A3-S005].
3. **Consolidation.** New candidates are reconciled with existing memories. Memory Bank resolves contradictions and may delete contradicted memories or honour explicit "forget" instructions [VF: A3-S109]. Graphiti marks old facts invalid with validity windows rather than deleting them [VF: A3-S003]. Supermemory handles temporal changes and contradictions and forgets expired information automatically [VF: A3-S064].
4. **Storage.** The record is written to ordinary stores: SQL plus a third-party vector store plus an entity store (Mem0, default local Qdrant in open source) [VF: A3-S053, A3-S080]; Neo4j, FalkorDB or Neptune (Graphiti) [VF: A3-S003]; SQLite, LanceDB and an embedded graph package by default, or Neo4j, Neptune or Postgres/pgvector (Cognee) [VF: A3-S005]; a LangGraph BaseStore (LangMem) [VF: A3-S006]; a git-backed filesystem (Letta) [VF: A3-S073].

**Read path.** At the start of a step, the orchestrator queries memory by scope (user, agent, run, namespace) and by similarity, and injects the results into the prompt. Mem0 fuses semantic, BM25 and entity signals [VF: A3-S001]. Graphiti combines semantic, keyword and graph search [VF: A3-S003]. Memory Bank retrieves by exact scope with optional similarity search [VF: A3-S109]. These are the same hybrid retrieval techniques L6 and L7 use for knowledge bases [AJ].

**Where the governance controls belong [AJ].** The vendor products automate steps 2 to 4. An enterprise design inserts a policy gate between extraction and storage, keeps a write log, and attaches provenance and a retention class to each record:

```text
                         WRITE PATH (governed)                                    READ PATH
 interaction events ─► extraction (LLM) ─► POLICY GATE ──────────► memory store ─► scoped recall ─► prompt
 (L3 workflow,          proposes            │ C3 DLP: no client IDs,   │ rows (SQL)      │ by user/fund/
  reviewer edits)       candidate facts     │   no special-category    │ vectors (L6)    │ team scope (C4)
                                            │ type allow-list          │ graph edges     │ + similarity
                                            │ "no numbers as facts"    │ files/Git       │
                                            │ human approval for       │                 ▼
                                            │   organisational memory  │        trace: memory IDs +
                                            ▼                          │        version hash (L9)
                                     write log (C8) ◄──────────────────┤
                                     who, what, source, approval       │
                                                                       ▼
                         LIFECYCLE: retention class per record · TTL/pruner · subject index for erasure
                                    · revisions purge · snapshot per release for reproducibility
```

The **subject index** is the key design choice [AJ]. Every memory that may contain personal data must be findable by data subject, so that an erasure request can be satisfied by one query across rows, vectors, graph nodes, revisions and caches. AgentCore supports per-user erasure by listing and deleting a user's namespace records [VF: A3-S111]; Memory Bank purges by filter with a dry run [VF: A3-S109]; Mem0 has delete, delete_all and per-memory history in both open source and Platform [VF: A3-S080]. Each of these works only if scoping was designed for it from the first write [AJ].

### 5.5 Enterprise design principles

**Governance (the centre of gravity for this layer)**

- **Decide what may be remembered before choosing a product.** Write an allow-list of memory types per use case (for example "terminology preferences: yes; client facts: no; figures: never") and enforce it at the policy gate [Rec].
- **Separate proposal from commitment.** Organisational and procedural memory (house style, glossaries, prompt rules) should be proposed by the agent but committed only after human approval, as a versioned artefact [Rec]. Per-user preference memory can be committed automatically if it passes the gate and is user-visible and user-editable [AJ]. Anthropic's Claude app memory, for example, offers a user-editable memory summary, project-scoped memory and an admin switch to disable memory on Team and Enterprise plans [VF: A3-S071]. (Conflict-of-interest note: the author is an Anthropic model; the same pattern of user-visible, admin-controlled memory is available in ChatGPT, where memory can be switched off [VF: A3-S110].)
- **Every record carries provenance and a retention class.** Source interaction ID, writer (user, agent or extraction model and version), timestamp, approval status, scope, data-classification label and expiry [Rec].
- **Erasure is designed, not assumed.** Product behaviour differs widely. Vendor-hosted chat memory and chat history can be separate: deleting a ChatGPT chat does not delete its saved memories, and deleted memory logs may be kept for up to 30 days [VF: A3-S110]. Memory Bank keeps memory revisions for 365 days by default [VF: A3-S109]. AgentCore harness-managed memory cannot be deleted through the Memory APIs, and deleting the memory resource removes all its events and records [VF: A3-S111]. Test the erasure path end to end, including revisions and indexes, before go-live [Rec].
- **Memory never outranks authority.** In the prompt, memory is labelled as such and placed below tool outputs and approved knowledge. The workflow, not the model, resolves conflicts in favour of the authoritative source [Rec].
- **Auditability of recall.** Record which memory IDs and versions were injected into each run, so a past output can be explained and reproduced [Rec]. Zep's audit logs cover web-app member actions only, not API or SDK calls [VF: A3-S107], so recall auditing must come from the firm's own traces in that case [AJ].

**Security**

- Treat memory as a persistent prompt-injection vector. Screen writes for instructions as well as for PII, and red-team the memory path against ASI06 [VF: B-L5-S001] [Rec].
- Enforce scope at the identity layer (C4), not by convention. Memory Bank's scope is immutable and retrieval returns only exact-scope matches [VF: A3-S109], which is the right default [AJ].
- Use customer-managed keys where available. AgentCore Memory encrypts at rest with an AWS-owned key by default and accepts a customer-managed KMS key, set at creation [VF: B-L5-S002]. Memory Bank lists CMEK, but not on its global endpoint [VF: B-L5-S004]. Zep offers BYOK on Enterprise [VF: A3-S089, A3-S090].
- Restrict who can read memory directly. AWS's security reference architecture recommends limiting IAM access to memory APIs such as ListMemoryRecords and DeleteMemoryRecord [VF: B-L5-S002]. A memory store is a concentrated index of what users said, so treat it like a trace store [AJ].

**Scalability, resilience and cost**

- Extraction is LLM spend on every interaction. Mem0's self-hosted cost is driven by the vector store, LLM extraction calls and the embedder [VF: A3-S080]. Memory Bank bills LLM usage for memory generation separately from its per-memory charges [VF: A3-S109, V1-S088]. Graphiti's README warns of LLM rate-limit errors at default concurrency [VF: A3-S003]. Run extraction asynchronously and only for workflows that need it [Rec].
- Memory must degrade gracefully: if the memory service is down, the workflow runs without it rather than failing [AJ].

**Observability and evaluation**

- Every recall and every write is a span in the trace (L9), carrying memory IDs and the gate verdict [Rec].
- Evaluate memory as a retrieval component: relevance of recalled items, and contradiction with authoritative sources [AJ].

**Portability**

- Put a thin firm-owned memory API (write, recall, forget-by-subject, snapshot) in front of any product, and keep the canonical record in a store the firm controls [Rec]. Mem0 open source already supports 14 or more vector stores, including PGVector, Elasticsearch, OpenSearch and MongoDB [VF: A3-S080, A3-S053], so the backing store can be the firm's existing L6 platform [AJ].

**Patterns [AJ]:** policy-gated write path; subject index for erasure; "style memory" as a versioned, approved artefact in Git or the prompt store; memory snapshot hash recorded per run; memory below authority in prompt assembly; hyperscaler memory only inside that hyperscaler's agent runtime.

**Anti-patterns [AJ]:** free-form "remember everything" memory on regulated workflows; memory as a source of figures; one shared memory scope across clients or funds; vendor default retention ("none") left in place; graph "invalidation" mistaken for erasure; memory switched on before evaluation and tracing exist; extraction sent to an unassessed third-party LLM.

**Why memory is built last.** The plan's day-one build order puts memory in phase 6, after governance (0), evaluation and observability (1), model access through the gateway (2), retrieval and knowledge (3), agent workflows (4) and tools (5) (plan §12.6). The reasoning holds up [AJ]:
- Memory changes behaviour over time, so its effect can only be measured once evaluation and tracing exist (phase 1) [AJ].
- Extraction is a model call, so it should route through the gateway, with its residency and logging controls (phase 2) [AJ].
- Memory is stored and recalled with retrieval infrastructure, so the L6 store, embeddings and access model should be settled first (phase 3) [AJ].
- The write and read points are steps in a workflow, and the safe pattern is a deterministic workflow that decides when to remember (phase 4) [AJ].
- Authoritative data must already flow through read-only tools before memory is added, so that memory never becomes the easiest place to find a number (phase 5) [AJ].
- Many first use cases, including the worked example, deliver most of their value without long-term memory at all: retrieval of approved knowledge plus session state is enough [AJ].

### 5.6 Product selection criteria

| Scorecard criterion | What to evaluate in this layer [AJ] |
|---|---|
| Technical (15% FS) | Coverage of the memory types in 5.1; extraction quality and control (custom prompts, type allow-lists); consolidation and contradiction handling; temporal validity; scoping model; hybrid recall; deletion granularity (record, subject, namespace, revisions); procedural memory |
| Enterprise readiness (15%) | SSO, RBAC and audit logs that cover API reads and writes, not only console actions; admin APIs; SLA; multi-tenancy that maps to funds, teams and clients |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in the product's scope; CMK/BYOK; residency; DPA; erasure and retention features; screening hooks on the write path |
| Deployment flexibility (15%) | Self-host or BYOC so memory, which concentrates personal data, can stay in-estate; choice of backing store |
| Ecosystem (5%) | Framework integrations (LangGraph, ADK, Strands, CrewAI); MCP; supported vector and graph stores |
| Reliability and maturity (10%) | Release cadence and breaking changes (four of the six original products changed architecture or cadence materially in 2025–26); funding stage; pre-1.0 status |
| Cost / TCO (5%) | Extraction LLM spend, per-memory pricing, storage; licence gates on production features |
| Lock-in / portability (15%) | Whether the canonical record sits in a store you own; export; proprietary graph engines; Platform-only features |

**Vendor benchmark scores are not decision inputs.** Mem0 reports LoCoMo 92.5 and LongMemEval 94.4 for its managed platform [R: A3-S081], and Supermemory claims first place on LongMemEval, LoCoMo and ConvoMem [R: A3-S064]. Test recall on your own data instead [Rec].

### 5.7 Product deep dives

**Mem0 (Mem0).**
- *What it is now:* an open-core agent memory layer. The Apache-2.0 open-source library and self-hosted server extract facts from conversations and agent actions, scope them by user_id, agent_id and run_id, and retrieve them with entity-aware ranking; add, search, get, update, delete, delete_all and per-memory history exist in both the open-source and hosted clients [VF: A3-S001, A3-S080]. mem0ai 2.2.1 was released on 25 September 2026 [VF: A3-S001].
- *Open source and Platform diverge:* open-source v2.0.0 (14 April 2026) removed all external graph backends (Neo4j, Memgraph, Kuzu, Apache AGE, Neptune) and replaced them with built-in entity linking, which is a parallel entity collection that boosts retrieval, not a queryable graph [VF: A3-S053, A3-S081, V1-S043]. Graph memory, memory decay, temporal reasoning, Dream consolidation, webhooks and memory export are Platform-only [VF: A3-S080]. The open-source extraction is now ADD-only [VF: A3-S081].
- *Certifications and deployment:* Mem0's own pages conflict on SOC 2: Type I on the homepage, Type II "in progress" in one article and Type II "for Enterprise" in one guide; HIPAA is claimed and no trust-centre report was seen [VF: A3-S051, A3-S106]. No managed EU region was found [VF: A3-S106]. The vendor states private Kubernetes deployment in the customer's VPC, on-premises and air-gapped options, and BYOK encryption [VF: A3-S049, A3-S051].
- *Access control:* the Enterprise plan lists SSO and audit logs; the Platform has organisations and projects with member roles and a project-wide event feed of add, search and delete events; open source has no organisation or project concept [VF: A3-S049, A3-S080].
- *Strengths:* the widest choice of backing stores, so the canonical memory record can sit in the firm's existing L6 platform [VF: A3-S080, A3-S053] [AJ]. The largest open-source community in the layer, at 66,777 GitHub stars on 7 October 2026 [VF: A3-S054].
- *Limitations:* the security evidence is vendor marketing only, and the SOC 2 type is unresolved [VF: A3-S106]. April 2026 brought breaking changes [VF: A3-S081]. ADD-only extraction means memories accumulate unless the firm prunes them [VF: A3-S081] [AJ]. The vendor ships an "OSS-to-Platform" migration skill [VF: A3-S081], which signals the commercial direction [AJ].
- *Choose when:* you want a framework-neutral memory API that you self-host on your own vector store, with your own policy gate in front [AJ].
- *Avoid when:* you need the managed Platform for regulated data before a SOC 2 Type II report is in hand, or you need a queryable graph in open source [AJ].
- *Competitors:* Zep/Graphiti, Supermemory, AgentCore Memory, Cognee.
- *FS note:* self-host the open-source server against your approved vector store, put the policy gate and subject index in your own wrapper, and request the SOC 2 report before any Platform use [Rec].
- **Tier: Tactical. Flag: none.**

**Zep and Graphiti (Zep).**
- *What it is now:* Zep is a managed "context infrastructure" platform built on a proprietary Context Graph Engine; Graphiti is the Apache-2.0 temporal knowledge-graph framework underneath [VF: A3-S003, A3-S059]. Graphiti builds bi-temporal graphs: entities, facts with validity windows, episodes with provenance, and communities; old facts are invalidated rather than deleted; retrieval is hybrid semantic, keyword and graph search [VF: A3-S003]. zep-cloud 3.30.0 was released on 24 September 2026 with a 4.0.0b1 pre-release on 6 October 2026; graphiti-core is at 0.30.2 (8 September 2026) [VF: A3-S002, A3-S003].
- *Community Edition:* deprecated and unsupported; its code sits in a legacy folder under Apache-2.0. The deprecation date is not confirmed by an official source [VF: A3-S059, V1-S044].
- *Certifications and deployment:* SOC 2 Type II and a HIPAA BAA on the Enterprise plan only, not on Flex or Flex Plus [VF: A3-S089, A3-S090]. BYOK and BYOC (AWS, GCP, Azure) on Enterprise [VF: A3-S089, A3-S090]. US hosting by default, with EU residency on request; DPAs with EU customers; right-to-be-forgotten and time-based retention purge (Zep Archive) [VF: A3-S107]. No ISO 27001 was found [NPV].
- *Access control:* IdP-based sign-in (SAML not named), RBAC for the dashboard and ABAC policies for data reads and writes. Audit logs cover web-app member actions only, not API or SDK calls; Enterprise keeps audit and API logs for one year [VF: A3-S107].
- *Strengths:* the closest match in the layer to what a regulated firm needs from episodic and semantic memory: validity windows, provenance per episode, and history that survives updates [VF: A3-S003] [AJ]. Broad framework integrations, including Google ADK, Microsoft Agent Framework, LangGraph and Strands [VF: A3-S059].
- *Limitations:* "invalidate, not delete" preserves history, which is good for audit and awkward for erasure; erasure needs the platform's explicit right-to-be-forgotten feature or a delete in Graphiti's graph store [VF: A3-S003, A3-S107] [AJ]. Compliance is tier-gated [VF: A3-S089]. Graphiti is pre-1.0 and the SDK 4.0 is in beta [VF: A3-S003, A3-S002]. Self-hosted Graphiti needs Neo4j, FalkorDB or Neptune, and the Kuzu backend is deprecated [VF: A3-S003].
- *Choose when:* temporal reasoning and provenance matter, for example memory of how a client mandate or a fund's terminology changed over time; Graphiti self-hosted on Neo4j or Neptune where data must stay in-estate [AJ].
- *Avoid when:* you need API-level audit logs from the vendor, ISO 27001, or a supported self-hosted version of the full Zep platform [AJ].
- *Competitors:* Graphiti versus Cognee for self-hosted graph memory; Zep Cloud versus Mem0 Platform and Memory Bank.
- *FS note:* prefer self-hosted Graphiti on an approved graph store, and test that erasure removes invalidated facts and episodes, not only current ones. For Zep Cloud, buy Enterprise only and request EU residency [Rec].
- **Tier: Tactical. Flag: Deprecated (Community Edition).**

**Letta (Letta).**
- *What it is now:* a stateful agent harness, not a standalone memory library. Letta (formerly MemGPT) announced "Letta's Next Phase" in March 2026: Letta Code is a model-agnostic harness with a git-backed memory filesystem (MemFS), and the legacy server memory tools, templates, server-side sleep-time agents and tool rules are deprecated [VF: A3-S093, A3-S073, V1-S042]. The V1 API server was retired to an archive branch and the PyPI package `letta` now installs the Letta Code CLI [VF: A3-S060, A3-S004]. Letta Code 0.34.4 was released on 4 October 2026 [VF: A3-S004, A3-S077].
- *Memory model:* memory blocks and all context are tracked in MemFS, which can sync to a GitHub repository; message search works across agents [VF: A3-S073]. AgentFile (.af) export and import were removed [VF: A3-S073].
- *Certifications and deployment:* no SOC 2 or trust centre was found [VF: A3-S118]. Letta Cloud is the default backend storing agent state; `letta server` runs agents locally or self-hosted [VF: A3-S073, A3-S060]. The privacy policy states no specific retention periods [VF: A3-S118].
- *Access control:* RBAC and SAML/OIDC SSO on the Enterprise tier, plus permission modes for agent actions [VF: A3-S091, A3-S073]. Audit logs are not documented [NPV].
- *Strengths:* memory as files under version control is the most reviewable memory model in the layer: every change is a diff [VF: A3-S073] [AJ].
- *Limitations:* the architecture has changed twice in eighteen months, and Letta Code is pre-1.0 with eight releases between 29 September and 4 October 2026 [VF: A3-S077, A3-S004]. It is not a drop-in memory layer for other frameworks [VF: A3-S073]. Git history keeps deleted content unless history is rewritten, which complicates erasure [AJ]. Funding found is a US$10M seed in September 2024 [R: A3-S092].
- *Choose when:* you are evaluating a stateful coding or operations agent where the harness and its memory come together, outside regulated client data [AJ].
- *Avoid when:* you need a memory service for an existing LangGraph, ADK or Strands workflow, or certifications [AJ].
- *Competitors:* LangGraph with LangMem, AgentCore (runtime plus memory), Google ADK with Memory Bank.
- *FS note:* the git-backed memory idea is worth copying for "style memory" in your own repository; the product itself is not a regulated-workflow dependency today [Rec].
- **Tier: Experimental. Flag: Superseded (V1 server replaced by Letta Code).**

**Cognee (Cognee).**
- *What it is now:* an open-source memory platform that turns documents, code and conversations into a knowledge graph plus vectors, with remember, recall, improve and forget operations; retrieval selects graph, vector or code context [VF: A3-S005]. Version 1.6.3 was released on 7 October 2026 [VF: A3-S005].
- *Licence and stores:* the library is Apache-2.0; the production-ready Postgres-as-graph store is a licensed product; Cognee Cloud is the managed service [VF: A3-S005]. Defaults are SQLite, LanceDB and an embedded graph package, with optional Neo4j, Amazon Neptune and Postgres/pgvector [VF: A3-S005].
- *Certifications and data protection:* Cognee states that it does not hold SOC 2, ISO 27001 or equivalent certification and recommends self-hosting in the customer's certified environment [VF: A3-S095]. It is an EU company with GDPR processes audited by heyData, a DPA on request, support for access, erasure and portability rights, encryption at rest and in transit, a private mode with zero external API calls, and air-gapped self-hosting [VF: A3-S095].
- *Deployment and access:* Cloud, Enterprise BYOC in the customer's EU cloud account, self-hosted, on-premises and air-gapped [VF: A3-S005, A3-S095]. Multi-tenant mode with authenticated users by default, and Enterprise SSO, SLAs and a dedicated support engineer [VF: A3-S005, A3-S095]. RBAC and audit logs are not documented [NPV].
- *Strengths:* the clearest in-estate option: graph and vector memory on the firm's own Postgres or Neo4j, with local extraction possible [VF: A3-S005] [AJ]. It spans memory and knowledge ingestion, which fits the H4 view that they share infrastructure [AJ].
- *Limitations:* no certification, by the vendor's own statement [VF: A3-S095]. The production Postgres graph is licensed, not open [VF: A3-S005]. Seed-stage funding, with aggregators disagreeing on the amount [R: A3-S094].
- *Choose when:* you need memory or a graph-backed knowledge layer fully in-estate or air-gapped, in the EU, and can provide the controls yourself [AJ].
- *Avoid when:* you want a managed service to carry certification evidence [AJ].
- *Competitors:* Graphiti, Mem0 open source, Supermemory local.
- *FS note:* self-host only, on an approved Postgres or Neo4j, behind the firm's identity proxy and audit logging; treat Cognee Cloud as out of scope for client data until certified [Rec].
- **Tier: Tactical. Flag: none.**

**Supermemory (Supermemory).**
- *What it is now:* a memory and context engine API that bundles memory extraction, user profiles, hybrid RAG search, connectors (Google Drive, Gmail, Notion, OneDrive, GitHub) and file processing [VF: A3-S064]. It handles temporal changes and contradictions and forgets expired information automatically [VF: A3-S064]. The v5 namespace-first API shipped with Python SDK 5.0.0 on 6 October 2026, a breaking change from 3.x [VF: A3-S012].
- *Licence:* the repository is MIT and the SDK Apache-2.0, but the self-hosted server binary is not open source (free for individuals within a lite licence); the hosted API is proprietary [VF: A3-S066, A3-S012, A3-S096].
- *Certifications and deployment:* SOC 2 from the Scale tier and HIPAA on Enterprise per the pricing page; the report type is not confirmed there [VF: A3-S096]. GDPR access and erasure workflows and a DPA on request; no managed EU region was found [VF: A3-S122, A3-S096]. Dedicated deployments in the customer's AWS, GCP or Azure account, organisational self-hosting on Scale and Enterprise, and air-gapped self-hosting on Enterprise [VF: A3-S122, A3-S096].
- *Access control:* SSO on Enterprise with protocols not documented; namespaces isolate content [VF: A3-S096, A3-S012]. RBAC and audit logs are not documented [NPV].
- *Strengths:* one API for memory and retrieval, with explicit forget operations (`forget`, `forget_matching`, namespace delete) [VF: A3-S012, A3-S064].
- *Limitations:* bundling memory, RAG and connectors behind one proprietary API blurs the line between agent-written memory and owner-curated knowledge, which is the line governance depends on [AJ]. The API changed major version two days before this review [VF: A3-S012]. Seed funding only [R: A3-S097].
- *Choose when:* a team prototype needs memory plus RAG quickly, outside regulated data [AJ].
- *Avoid when:* you need memory and knowledge to have different owners, approvals and retention, or a stable API [AJ].
- *Competitors:* Mem0, Zep, Cognee.
- *FS note:* not for client or personal data until the SOC 2 report type, audit logging and EU residency are confirmed [Rec].
- **Tier: Experimental. Flag: none.**

**LangMem (LangChain).**
- *What it is now:* an MIT library of memory utilities for LangGraph agents: extraction from conversations, hot-path memory tools, a background memory manager that consolidates knowledge, and prompt refinement [VF: A3-S006]. It persists through the LangGraph BaseStore; the InMemoryStore loses data on restart [VF: A3-S006].
- *Activity:* version 0.0.30 was released on 27 October 2025, with no newer PyPI release by 7 October 2026, although the repository was still being updated [VF: A3-S006]. Whether LangChain has replaced it with built-in LangGraph or LangSmith memory features could not be verified [NPV].
- *Strengths:* the clearest example of procedural memory as a first-class idea (prompt refinement), and no service to operate [VF: A3-S006] [AJ].
- *Limitations:* pre-1.0 and apparently stalled [VF: A3-S006]. Tied to LangGraph store abstractions [VF: A3-S006]. Security and access control inherit entirely from the store and platform [AJ].
- *Choose when:* you are already on LangGraph and want reference patterns for background consolidation, accepting that you may need to maintain the code [AJ].
- *Avoid when:* you need a supported dependency [AJ].
- *Competitors:* LangGraph's own store with custom code, Mem0 (LangGraph integration), Zep.
- *FS note:* do not let automatic prompt refinement change production prompts; route any proposed change through C5 change control [Rec].
- **Tier: Experimental. Flag: Not publicly verified (activity status).**

**Amazon Bedrock AgentCore Memory (AWS).**
- *What it is now:* a managed memory service in Amazon Bedrock AgentCore, GA since 13 October 2025 [VF: A3-S047, V1-S087]. Short-term memory stores raw session events; long-term memory extracts records through semantic, summary, user-preference, episodic or custom strategies, grouped by namespaces and retrieved by semantic search [VF: A3-S111]. A self-managed strategy gives control of the extraction and consolidation pipeline, and extraction from non-conversational JSON payloads was added in August 2026 [VF: A3-S047, A3-S111, V1-S087]. The AgentCore harness auto-provisions managed memory [VF: A3-S048].
- *Lifecycle:* event expiry for short-term events; no built-in TTL for long-term records, with AWS recommending a pruner based on timestamp filters; per-user erasure by listing and deleting namespace records; DeleteMemoryRecord and BatchDeleteMemoryRecords; harness-managed memory cannot be deleted through the Memory APIs [VF: A3-S111].
- *Security and certifications:* encryption at rest with KMS, with a customer-managed key set at creation; AWS Config and Security Hub (control BedrockAgentCore.3) can flag memories without a customer-managed key [VF: B-L5-S002]. AgentCore is listed in AWS's scope for SOC 1, 2 and 3 and ISO/IEC 27001:2022 and related ISO standards, and is HIPAA eligible; Memory is covered as a generally available feature rather than named, and the SOC 2 report type is not stated in the evidence [VF: B-L5-S003]. VPC and PrivateLink are supported [VF: A3-S047].
- *Access control:* platform controls presumed (CP2 Q1); confirm per service. AWS guidance recommends restricting IAM access to the memory APIs [VF: B-L5-S002].
- *Strengths:* the most explicit lifecycle documentation in the layer, including AWS's own guidance on retention policies, and CMK enforcement through standard AWS compliance tooling [VF: A3-S111, B-L5-S002] [AJ].
- *Limitations:* AWS only, with a proprietary API [VF: A3-S047]. Pricing was not verified [NPV]. The absence of a long-term TTL means retention is the firm's job [VF: A3-S111]. EU Region availability for Memory was not individually verified [NPV].
- *Choose when:* the agent runs on AgentCore or Strands in AWS, and you will build the policy gate and pruner around it [AJ].
- *Avoid when:* you need memory portable across clouds, or the agent runtime is elsewhere [AJ].
- *Competitors:* Memory Bank, Mem0 self-hosted on Amazon S3 Vectors or OpenSearch, Zep BYOC.
- *FS note:* set a customer-managed key at creation (it cannot be changed later for harness-managed memory [VF: B-L5-S002]), deploy the pruner on day one, and confirm the Region list before storing UK or EU personal data [Rec].
- **Tier: Tactical, conditional: default memory store inside an AWS AgentCore estate. Flag: none.**

**Memory Bank (Google Cloud; Vertex AI Agent Engine, now Gemini Enterprise Agent Platform).**
- *What it is now:* a managed long-term memory service. It uses Gemini models to extract facts, preferences and context asynchronously from conversation history, consolidates them with existing memories (resolving contradictions), and retrieves them by scope, such as user ID, with optional similarity search [VF: A3-S108, A3-S109]. Public preview on 8 July 2025, GA in December 2025, and charged from 28 January 2026 at US$0.25 per 1,000 memories stored and US$0.50 per 1,000 retrieved, with LLM usage billed separately (as of 8 October 2026) [VF: A3-S108, V1-S088]. Newer documentation calls it "Agent Platform Memory Bank" [VF: A3-S109].
- *Lifecycle:* immutable scope with exact-scope retrieval; optional TTL (default none) and memory revisions kept 365 days by default; delete by name and purge by filter with a dry run; deleting the Agent Runtime instance deletes its built-in memories [VF: A3-S109].
- *Security and residency:* Google's enterprise security table lists VPC Service Controls, CMEK and data residency at rest for Memory Bank, but CMEK cannot be used with the global endpoint (GA 17 June 2026), and Google's data residency terms list Memory Bank among exclusions, which conflicts with the feature table [VF: B-L5-S004]. Platform certifications for generative AI on Vertex AI include SOC 2, ISO/IEC 27001 and ISO/IEC 42001, with scope stated per product or feature [VF: A2-S043, A5-S028]; Memory Bank's inclusion is not stated [NPV].
- *Access control:* platform controls presumed (CP2 Q1); confirm per service.
- *Strengths:* consolidation with contradiction handling and an explicit, immutable scope model, both useful against stale or leaked memories [VF: A3-S109] [AJ]. Transparent unit pricing [VF: V1-S088].
- *Limitations:* Google Cloud only; extraction depends on Gemini [VF: A3-S108]. Memories are tied to the Agent Runtime instance [VF: A3-S109]. The residency position needs written confirmation [VF: B-L5-S004]. Consolidation may delete contradicted memories automatically [VF: A3-S109], which is good for freshness and needs logging for audit [AJ].
- *Choose when:* the agent runs on ADK or Agent Engine in Google Cloud [AJ].
- *Avoid when:* you need cross-cloud portability or a guaranteed UK or EU at-rest location before Google confirms it [AJ].
- *Competitors:* AgentCore Memory, Mem0, Zep.
- *FS note:* use a regional endpoint with CMEK, set a TTL and a shorter revision retention, and obtain written confirmation of data residency for Memory Bank [Rec].
- **Tier: Tactical, conditional: default memory store inside a Google Cloud agent estate. Flag: Renamed.**

### 5.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5-mem0 | 4 | 3 | 2 | 4 | 4 | 3 | 4 | 3 | 3.40 | 3.20 | Tactical |
| L5-zep | 5 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.60 | 3.35 | Tactical |
| L5-letta | 3 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 2.85 | 2.75 | Experimental |
| L5-cognee | 4 | 2 | 2 | 5 | 3 | 3 | 3 | 3 | 3.20 | 3.10 | Tactical |
| L5-supermemory | 4 | 2 | 2 | 5 | 4 | 2 | 3 | 2 | 3.15 | 2.90 | Experimental |
| L5-langmem | 3 | 2 | 2 | 4 | 3 | 1 | 4 | 3 | 2.75 | 2.65 | Experimental |
| L5-aws-agentcore-memory | 4 | 4 | 4 | 2 | 3 | 3 | 2 | 2 | 3.20 | 3.15 | Tactical |
| L5-gcp-vertex-memory-bank | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Tactical |

**Scoring notes [AJ]:**
- **No product reaches Strategic.** The highest FS total is 3.35 (Zep), below the 3.6 guide. The independent products are held back by certification evidence (Mem0, Cognee, Supermemory, Letta) or lock-in (Zep Cloud), and the hyperscaler services by deployment and lock-in. This is consistent with the recommendation that memory be a governed record class on the firm's own stores rather than a strategic vendor dependency.
- **CP2 Q1 hyperscaler presumption** gives AgentCore Memory and Memory Bank enterprise readiness of 4. Their security is scored under rule 8: AgentCore's certifications are service-level and in scope (SOC 2 type not stated); Memory Bank's are platform-level with its inclusion not stated. Both score 4, not 5.
- **Evidence caps and anchors.** Mem0 security is 2: the vendor confirms SOC 2 Type I, and its Type II claims conflict. Letta security is capped at 2 (no certification found). Cognee states it holds no certification, so it is scored as self-hosted software under rule 2 (its own recommended deployment); Cognee Cloud on its own would score 1. Supermemory security is 2 because the SOC 2 report type is unconfirmed. Cognee and Supermemory enterprise readiness is 2 on the anchors: the cap is lifted by verified SSO (CP2 Q2), but RBAC and audit logs are not documented.
- **LangMem** is scored as a library under rule 2, and its maturity is 1: pre-1.0 with no release in eleven months.
- **No ownership-change reduction** applies in this layer; no acquisition was found for any of the eight products.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 7–8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| Mem0 | Apache-2.0 OSS; Platform proprietary [VF: A3-S001, A3-S080] | SaaS, private K8s/VPC, self-host, on-prem; air-gap claimed [VF: A3-S049, A3-S051] | SOC 2 Type I; Type II claims conflict; HIPAA claimed [VF: A3-S051, A3-S106] | No managed EU region found; self-host [VF: A3-S106] | Independent; US$24M Oct 2025 [R: A3-S052] |
| Zep / Graphiti | Zep proprietary; Graphiti Apache-2.0 [VF: A3-S003, A3-S059] | SaaS, BYOC (Enterprise); Graphiti self-host [VF: A3-S089, A3-S003] | SOC 2 Type II, HIPAA (Enterprise only) [VF: A3-S089, A3-S090] | On request [VF: A3-S107] | Independent; no 2025–26 round found [VF: A3-S090] |
| Letta | Apache-2.0 (Letta Code); Letta Cloud [VF: A3-S004, A3-S073] | SaaS, self-host server [VF: A3-S073, A3-S060] | None found [VF: A3-S118] | Not publicly verified [NPV] | Independent; US$10M seed 2024 [R: A3-S092] |
| Cognee | Apache-2.0; licensed Postgres graph [VF: A3-S005] | SaaS, BYOC, self-host, on-prem, air-gap [VF: A3-S005, A3-S095] | None, by vendor statement [VF: A3-S095] | EU company; BYOC in customer EU account [VF: A3-S095] | Independent; seed Feb 2026 [R: A3-S094] |
| Supermemory | MIT repo, Apache-2.0 SDK; server binary not open [VF: A3-S066, A3-S096] | SaaS, dedicated, customer cloud, self-host (Scale+), air-gap [VF: A3-S096, A3-S122] | SOC 2 (type unconfirmed), HIPAA Enterprise [VF: A3-S096] | No managed EU region found [VF: A3-S122] | Independent; seed [R: A3-S097] |
| LangMem | MIT [VF: A3-S006] | Library [VF: A3-S006] | Not applicable (library) [AJ] | Inherits store [AJ] | LangChain [VF: A3-S006] |
| AgentCore Memory | Proprietary service [VF: A3-S047] | AWS managed; VPC, PrivateLink [VF: A3-S047] | AgentCore in SOC 1/2/3 and ISO 27001 scope; HIPAA eligible [VF: B-L5-S003] | 15 AgentCore Regions; EU not individually verified [VF: A3-S048] | AWS [VF: A3-S047] |
| Memory Bank | Proprietary service [VF: A3-S108] | Google Cloud managed [VF: A3-S108] | Platform SOC 2, ISO 27001, ISO 42001; Memory Bank scope not stated [VF: A2-S043] [NPV] | Listed, but conflicts with residency terms [VF: B-L5-S004] | Google Cloud [VF: A3-S108] |

### 5.9 Decision tree

The tree is applied in four steps. Step 0 and step 4 are not product choices [Rec].

```text
STEP 0 [Rec]: Do you need long-term memory at all?
  Can the use case be met by session state (L3) + retrieval of approved knowledge (L6)?
  ├─ Yes → No L5 product. Keep conversation/working memory in the orchestrator's
  │        checkpoint store. Revisit after evaluation shows a gap.
  └─ No  → Write the memory allow-list (types, scopes, retention classes, prohibited
           content) and get it approved by data protection and the model owner.

STEP 1 [Rec]: Which kind of memory?
  Organisational / procedural (style, glossary, rules)?
  ├─ Yes → NOT agent memory. Versioned artefact in Git or the prompt store (C5),
  │        proposed by the agent, approved by a human, retrieved like knowledge (L6).
  └─ No  → per-user / per-entity episodic or semantic memory → STEP 2

STEP 2 [Rec]: Where does the agent runtime live?
  ├─ AWS AgentCore / Strands  → AgentCore Memory (CMK at creation, pruner on day one)
  ├─ Google ADK / Agent Engine → Memory Bank (regional endpoint + CMEK, TTL set,
  │                              residency confirmed in writing)
  └─ Elsewhere / multi-cloud / in-estate required
        Need temporal validity and provenance (how facts changed over time)?
        ├─ Yes → Graphiti self-hosted on Neo4j / FalkorDB / Neptune
        │        (Zep Cloud Enterprise only if managed is acceptable and API audit
        │         logs are not required from the vendor)
        └─ No  → Air-gapped or graph-plus-documents in one store?
                 ├─ Yes → Cognee self-hosted (no vendor certification: you supply controls)
                 └─ No  → Mem0 open source on your approved vector store (pgvector,
                          OpenSearch, Elasticsearch, MongoDB), behind your own API

STEP 3 [Rec]: Wrap whatever you chose
  Firm-owned memory API: write (via policy gate), recall (scoped), forget-by-subject,
  snapshot. Write log to C8. Every recall and write as a span in L9 traces.

STEP 4 [Rec]: Checks before go-live
  Erasure test across rows, vectors, graph, revisions, caches, backups ("beyond use")?
  Retention classes enforced by TTL or pruner?   No client identifiers in memory (C3)?
  Memory snapshot ID recorded per run?   ASI06 memory-poisoning red-team passed?
  Numbers never read from memory (L9 contradiction check)?
```

Letta, Supermemory and LangMem do not appear as defaults. Letta is a harness, not a memory service; Supermemory merges memory and knowledge behind one proprietary API; LangMem is stalled [AJ].

### 5.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Canonical memory records | **Unacceptable if only in a vendor's proprietary store** | Memory is a regulated record: erasure, retention and evidence must survive a vendor exit. Zep Cloud uses a proprietary graph engine [VF: A3-S003]; Mem0 makes memory export Platform-only [VF: A3-S080]; Memory Bank memories are deleted with the Agent Runtime instance [VF: A3-S109] | Canonical record in the firm's own L6 store, or a regular export to it |
| Memory API | **Manageable** | Every product exposes add, search and delete; the semantics differ (ADD-only, invalidate, consolidate) [VF: A3-S081, A3-S003, A3-S109] | Thin firm-owned interface: write, recall, forget-by-subject, snapshot |
| Extraction model | **Manageable** | Memory Bank depends on Gemini [VF: A3-S108]; Graphiti defaults to OpenAI [VF: A3-S003]; Mem0 needs an LLM and an embedder [VF: A3-S001] | Route extraction through the gateway (C1); pin the model and prompt version |
| Hyperscaler memory inside its own agent runtime | **Acceptable** | The runtime already binds the agent to that cloud, which DORA and the UK CTP regime oversee as designated providers [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023] | Firm-owned memory API and periodic export, so memory can move with the agent |
| Organisational and procedural memory | **Unacceptable outside the firm's version control** | It is policy-bearing content that changes output for every user [AJ] | Git or prompt store (C5) with approval history |
| Graph engine choice | **Manageable** | Graphiti supports Neo4j, FalkorDB and Neptune, and deprecated Kuzu when it became unmaintained [VF: A3-S003] | Prefer a graph store the firm already operates |

### 5.11 Regulated FS lens (POV 2)

**Data protection: erasure, retention and minimisation.**
- *The right to erasure.* Article 17(1) GDPR gives a data subject the right to obtain erasure without undue delay where one of the listed grounds applies, and Article 17(3) sets exceptions, including legal claims [VF: B-L5-S007]. Under UK GDPR the ICO expects erasure from live systems, steps for backups ("beyond use" until overwritten), clarity to the individual about what happens, and a response within one month; the ICO notes that this guidance is under review following the Data (Use and Access) Act [VF: B-L5-S005]. The DUAA's data protection provisions are in force [VF: R-DATA-TRANSFERS, A8-S051].
- *Storage limitation.* Personal data must be kept no longer than necessary, with periodic review and erasure or anonymisation, including in backups [VF: B-L5-S006, B-L5-S007].
- *What this means for memory.* A memory store is personal-data processing by default, because extraction picks up names, preferences and circumstances from conversation [AJ]. Defaults in this layer run against storage limitation: no long-term TTL in AgentCore [VF: A3-S111], no default TTL in Memory Bank [VF: A3-S109], ADD-only accumulation in Mem0 open source [VF: A3-S081], invalidation rather than deletion in Graphiti [VF: A3-S003]. The firm must therefore set retention classes, minimise at the write gate, and keep a subject index [Rec].
- *Records-keeping versus erasure.* Some content an agent sees may also be a business record the firm must keep. Whether a records obligation overrides an erasure request is a legal question for each record class [AJ]. The architectural answer is to keep memory and records apart: records belong in the records archive (C8), and memory holds only what the agent needs, under shorter retention [Rec].
- *Transfers.* Extraction calls send conversation content to a model. For EU and UK personal data sent to US-hosted services, the lawful basis rests on the Data Privacy Framework or SCCs, and the C-703/25 P appeal is pending [VF: R-DATA-TRANSFERS, A8-S053]. Run extraction on in-region models through the gateway [Rec].

**Model risk and reproducibility.**
- *SS1/23.* PRA SS1/23 requires independent validation (Principle 4) and covers vendor models; it applies to banks and PRA-designated firms with internal-model approval and is the natural benchmark for others [VF: R-PRA-SS123, A8-S008].
- *The memory problem for validation.* A system whose behaviour changes with accumulated memory is a moving target: the validated system and the running system diverge every time memory is written [AJ]. Two responses work. Either the memory used by a regulated workflow is frozen per release (versioned "style memory" that changes only through change control), or every run records a memory snapshot so validators can reproduce any output [Rec]. Free-form self-updating memory on a model-risk-relevant workflow should be treated as a material change process, with monitoring thresholds, not as configuration [AJ].
- *SR 26-2.* SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly excludes generative and agentic AI, leaving governance to the firm's own risk-management practices [VF: R-US-MRM, A8-S001, A8-S002]. Memory governance is therefore the firm's own standard to set in the US as well [AJ].

**EU AI Act.**
- *Logging duties.* Article 26 requires deployers of high-risk systems to keep logs for at least six months and to monitor operation; financial institutions fold logging into existing financial-services documentation [VF: R-EUAIA, A8-S011]. Annex III duties apply from 2 December 2027 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011].
- *Application to memory.* For any high-risk use, the log must show what the system recalled, not only what it was asked, because recalled memory is part of the input [AJ]. Most asset-management uses, including attribution commentary, are not Annex III [AJ]. Building recall logging anyway serves MRM and complaints handling [Rec].

**Operational resilience and outsourcing.**
- *Memory SaaS is an ICT third-party service.* A hosted memory service holding client conversation data belongs in the DORA register of information, with Article 30 terms and an exit plan if it supports a critical or important function [VF: R-DORA, A8-S021] [AJ]. In the UK, SYSC 8 and FG16/5 expect data location, effective access and exit planning [VF: R-FCA-SYSC8, A8-S049].
- *Designations.* The DORA CTPP list and UK CTP designations include AWS and Google Cloud and no AI model provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. AgentCore Memory and Memory Bank therefore sit under overseen providers; the independent memory vendors do not, which places more due-diligence weight on the firm [AJ].
- *Notification lead time.* PRA PS7/26 and FCA PS26/2 require material third-party notifications from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062].
- *Exit.* SS2/21 expects documented, tested exit plans [VF: R-PRA-SS221, A8-S048]. For memory, exit means exporting records with provenance and re-creating the subject index elsewhere; test it once [Rec].

**Security standards and contamination risk.**
- *OWASP.* The OWASP Top 10 for Agentic Applications for 2026 includes memory and context poisoning (ASI06) and starts with ASI01 Agent Goal Hijack [VF: B-L5-S001; R-OWASP-AGENTIC, A8-S042]. The Top 10 for LLM Applications 2026 is the operative LLM list [VF: R-OWASP-LLM, V2-S056]; for traceability, the 2025 list's LLM04 Data and Model Poisoning and LLM08 Vector and Embedding Weaknesses map to memory stores [R: A8-S040].
- *Controls.* Screen writes for embedded instructions, never let memory carry tool permissions, keep scope at the identity layer, and red-team the memory path [Rec].

**Supervisory expectations for asset managers.** ESMA expects ex-ante input controls and frequent ex-post output controls, and IOSCO's toolkit names the level and frequency of human intervention as an indicator [VF: R-INTL-AI-ASSETMGMT, A8-S058, A8-S059]. A human-approved write gate for organisational memory is an ex-ante input control in exactly that sense [AJ].

**Standards.** NIST AI RMF and AI 600-1 provide a neutral taxonomy for data-related GenAI risks [VF: R-NIST-AIRMF, A8-S043, A8-S044]. ISO/IEC 42001 provides the management-system wrapper in which a memory retention and erasure policy sits [VF: R-ISO-42001, A8-S045].

### 5.12 Worked-example slice (POV 3)

**What the commentary agent needs from L5 [AJ].** The agent drafts the monthly Brinson-style attribution commentary (allocation, selection, currency, benchmark-relative return) for a generic multi-asset fund. The plan asks L5 for "memory of fund-specific terminology and the PM's past edits, under governance" (plan §11.2). Read carefully, that is not free-form agent memory at all. It is a governed, versioned **style memory**:

1. **Fund terminology glossary.** Preferred names for the benchmark, sleeves and asset classes, and phrases the PM always uses or never uses. Stored as a versioned file per fund (for example YAML in Git or the prompt store, C5), retrieved by fund ID, owned by the PM or product specialist.
2. **Style rules distilled from past edits.** The PM's edits are already captured as diffs on each trace by L9. A monthly job clusters recurring edits ("replaced 'outperformed' with 'returned more than' in 9 of 12 drafts") and proposes new style rules. The proposals are a pull request, not a memory write: the PM approves, rejects or amends them, and the approved version becomes the next release of style memory.
3. **Scoped episodic notes, if any.** Short notes such as "Q3 commentary must mention the mandate change agreed in July", entered by a person, with an expiry date. The agent may propose them; a person commits them.
4. **Recall by version.** Each run reads one pinned version of the glossary and style rules. The version hash is recorded in the trace and the evidence pack (C8), so any commentary can be regenerated with the memory it actually used. Validators review style memory changes as configuration changes.
5. **Session state only for the draft in hand.** Working memory for the current draft lives in the L3 workflow checkpoint and is discarded after approval, apart from what the evidence pack retains.

**Product implication [AJ].** This slice needs no L5 product. Git or the prompt store, plus the L6 retrieval path and the L9 edit capture, deliver it with better governance than any memory service in 5.7. A memory product becomes useful only if the firm later adds per-user preference memory across many agents, at which point the decision tree in 5.9 applies.

**What L5 must never do [AJ]:**
- remember client identifiers, holdings by client, or any personal data from the drafting conversation; C3 screens the write path and the allow-list excludes them
- serve a number, sign or direction ("detracted", "overweight") from memory; every figure comes from the attribution engine through the read-only L4 tool, and L9's contradiction check fails any draft where a recalled memory disagrees with tool output
- override the authoritative attribution output or an approved source when memory and data conflict; the workflow resolves conflicts in favour of the source, not the model
- change style memory without a human approval and a new version
- let a memory written for one fund be recalled for another; scope is the fund ID, enforced at C4
- keep memory after its retention class expires, or survive an erasure request in revisions, caches or graph history

### 5.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| A separate "memory" layer with six tiles | Products sit on vector, graph, relational and file stores [VF: A3-S053, A3-S003, A3-S005, A3-S006, A3-S073]; hyperscalers bundle memory into agent platforms [VF: A3-S047, A3-S108] | A governed memory service (policy gate, subject index, lifecycle) over the firm's L6 stores; organisational memory as versioned artefacts in C5 [Rec] |
| Mem0 "memory layer" | Open core; OSS graph stores removed for entity linking; Platform-only graph, decay and export [VF: A3-S081, V1-S043, A3-S080] | Tactical: self-hosted OSS behind the firm's API [Rec] |
| Zep "graph memory" | Proprietary Zep Cloud; Graphiti is the OSS path; Community Edition deprecated [VF: A3-S003, A3-S059] | Tactical: Graphiti self-hosted where temporal provenance matters [Rec] |
| Letta "stateful agents" | Letta Code agent harness; V1 server retired [VF: A3-S060, A3-S073, A3-S093] | Experimental; belongs with L3 harnesses [Rec] |
| Cognee "knowledge graphs" | Apache-2.0 graph-plus-vector memory; licensed Postgres graph; no certification [VF: A3-S005, A3-S095] | Tactical: in-estate or air-gapped only [Rec] |
| Supermemory "memory API" | Memory plus RAG plus connectors behind one proprietary API; v5 breaking change [VF: A3-S064, A3-S012] | Experimental [Rec] |
| LangMem "long-term" | LangGraph library; no release since 27 October 2025 [VF: A3-S006] | Experimental; reference patterns only [Rec] |
| (absent) | AgentCore Memory (GA October 2025) and Memory Bank (GA December 2025) [VF: V1-S087, V1-S088] | Tactical defaults inside their own agent runtimes [Rec] |

**H4 (memory may not be separate from retrieval and data architecture). Provisional view; verdict in synthesis.**

The evidence supports the hypothesis on four counts.

- **Memory products are retrieval stacks with an extraction step.** Every product stores memory in the same kinds of stores that L6 governs: SQL plus vector plus entity store (Mem0), Neo4j, FalkorDB or Neptune (Graphiti), SQLite, LanceDB, Postgres/pgvector or Neptune (Cognee), a LangGraph store (LangMem), a git-backed filesystem (Letta) [VF: A3-S053, A3-S003, A3-S005, A3-S006, A3-S073]. Recall uses the same hybrid semantic, keyword and graph search as knowledge retrieval [VF: A3-S001, A3-S003, A3-S064, A3-S005].
- **The products are converging with RAG.** Supermemory's default mode combines RAG and memory in one query, with connectors and file processing [VF: A3-S064]. Cognee ingests documents, code and conversations into one graph [VF: A3-S005]. Zep ingests chat history and business data into the same graph [VF: A3-S003].
- **The platforms are absorbing memory.** AWS and Google ship memory as a feature of their agent platforms; the AgentCore harness provisions memory automatically [VF: A3-S048, A3-S108]. Model vendors ship memory in their own products and APIs: Anthropic's memory tool executes file operations on storage the developer controls [VF: A3-S069], and OpenAI persists conversation state through its Conversations API [VF: A3-S110].
- **The independent layer is thinning.** Mem0 removed graph stores from open source [VF: A3-S081, V1-S043], Zep deprecated its Community Edition [VF: A3-S059], Letta pivoted to an agent harness [VF: A3-S093], and LangMem has not released in eleven months [VF: A3-S006].

The counter-evidence is real. Memory has a write path that retrieval does not have: extraction from interactions, consolidation, contradiction handling and decay [VF: A3-S109, A3-S003, A3-S064]. Its governance is also different in kind. Knowledge bases are written by accountable owners and retained under the records policy; memory is written by an agent, is per-subject, and must be erasable per person [AJ]. Both hyperscalers chose to expose memory as a distinct service, not as a feature of their vector stores [VF: A3-S047, A3-S108].

**Provisional recommendation.** Memory should not be a separate infrastructure layer in the reference architecture [AJ]. Physically, it belongs with retrieval and data stores (L6), and its organisational and procedural forms belong with prompt and configuration management (C5) [AJ]. Logically, a thin **memory service** remains worth drawing, because it carries the controls that are unique to memory: the policy-gated write path, the subject index, retention and erasure, and per-run snapshots [AJ]. The suggested verdict is **merge physically into "Retrieval, knowledge and memory stores", keep memory governance as an explicit logical component tied to C3 and C8, and build it last** [AJ]. **Provisional; verdict in synthesis.**
