# Stage A: follow-up (gap-filling) prompts

Each first-pass agent stopped early when the environment's shared web-search cap (about 200 calls per turn) ran out. These follow-ups were sent to the same agents with `SendMessage`, which gave each one a fresh search budget.

**To re-run in a fresh environment:** append the relevant block to the matching Stage A prompt, or send it as a second turn to that agent. On a machine without the search cap and with open egress, these gaps should mostly close in the first pass.

---

### A8: Regulation, items 6–12 and the Article 4 conflict

```text
Continue Stream A8: complete brief items 6–12 now (fresh search budget this turn). Priority order: (a) OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications (name, date); (b) NIST AI RMF 1.0 / AI 600-1 status and any 2025–2026 updates; ISO/IEC 42001, 42005, 42006 publication status; (c) PRA SS2/21, FCA SYSC 8 / FG16/5, EBA outsourcing guidelines — dates and AI relevance; (d) UK Data (Use and Access) Act 2025 commencement, EU–UK adequacy renewal, EU–US DPF challenges (e.g. Latombe General Court ruling and any appeal); (e) FCA/BoE AI statements 2024–2026 incl. AI Live Testing, any agentic-AI statements; IOSCO/ESMA on AI in asset management; (f) SEC predictive data analytics rule withdrawal; (g) amended AI Act Art. 4 wording conflict. Use WebSearch with allowed_domains for owasp.org, genai.owasp.org, nist.gov, iso.org, bankofengland.co.uk, fca.org.uk, eba.europa.eu, gov.uk, legislation.gov.uk, ico.org.uk, commission.europa.eu, sec.gov, iosco.org, esma.europa.eu. Update regulatory_facts.json, notes.md and sources.csv in place (keep IDs continuing from A8-S040), archive extracts as before, validate JSON, and reply with a ≤200-word delta summary. If the search budget runs out again, stop cleanly and say exactly which items remain.
```

### A2: L6 follow-up

```text
Continue Stream A2: complete the L6 follow-up pass now (fresh search budget this turn). Priority: (1) Amazon S3 Vectors — GA status/date, limits, pricing, regions, integration with Bedrock Knowledge Bases/OpenSearch (allowed_domains aws.amazon.com, docs.aws.amazon.com); (2) Pinecone certifications (trust centre) and price list; (3) Qdrant, Weaviate, Milvus/Zilliz, turbopuffer, Chroma — server version/date, licence, SOC 2/ISO/HIPAA, EU regions, BYOC/self-host, pricing; (4) Elasticsearch licence (AGPL option status) and vector/hybrid features; MongoDB Atlas Vector Search self-managed/Community availability; (5) if budget remains, L7 enterprise gaps (SSO/audit/CMK/ZDR) for Cohere, Voyage, OpenAI embeddings. Use WebSearch with allowed_domains on each vendor's domain (trust centres are often trust.<vendor>.com or <vendor>.trust.page / security pages). Update products.json, notes.md and sources.csv in place (IDs continue from A2-S079), archive extracts as before, validate JSON, and reply with a ≤200-word delta summary. If the search budget runs out again, stop cleanly and say exactly which items remain.
```

### A5: L1 gap-filling

```text
Continue Stream A5: run the gap-filling pass now (fresh search budget this turn). Priority: (1) Chinese-origin model sovereignty/regulatory position — Italy Garante DeepSeek action, Korea PIPC, Australia/US federal & state device bans, Taiwan, any US Commerce/NIST CAISI evaluation of DeepSeek or other PRC models, EU DPA actions; where each vendor's hosted API processes/stores data (privacy policies); whether DeepSeek/Qwen/Kimi/GLM open weights are offered via AWS Bedrock / Azure Foundry / Vertex (which allows non-China hosting). (2) For xAI, DeepSeek, Qwen, Kimi, GLM, Mistral, Meta: licence of current open weights, flagship + small API pricing from the vendor's own page, data retention/training policy, certifications (SOC 2/ISO), EU residency, HQ jurisdiction — use allowed_domains on each vendor domain (x.ai, docs.x.ai, api-docs.deepseek.com, deepseek.com, qwen.ai, alibabacloud.com, moonshot.ai, platform.moonshot.ai, z.ai, docs.z.ai, mistral.ai, docs.mistral.ai, trust.mistral.ai, ai.meta.com, llama.com, huggingface.co). (3) Resolve the GPT-6 Astra launch-date conflict from openai.com. (4) Re-check the Anthropic controversy claims (Pentagon supply-chain-risk designation and D.C. Circuit ruling; Bartz settlement) against court/government or major-outlet sources and label precisely. Update products.json, notes.md, sources.csv in place (IDs continue from A5-S048), archive as before, validate JSON, and reply with a ≤200-word delta summary. If the budget runs out, stop cleanly and list exactly what remains.
```

### A3: L5/L4 gap-filling

```text
Continue Stream A3: run the gap-filling pass now (fresh search budget this turn). Priority: (1) Tavily acquisition status (allowed_domains tavily.com plus major news); (2) certifications/EU region/SSO/pricing/funding for Zep, Letta, Cognee, Supermemory, Composio, Exa, Browserbase, E2B — try trust centres (trust.<vendor>.com, <vendor>.trust.page, security pages) via WebSearch allowed_domains; (3) vendor/platform built-in memory: Vertex AI Memory Bank (cloud.google.com is directly fetchable), OpenAI memory / Responses API conversation state, Anthropic memory tool (docs.claude.com fetchable), AgentCore Memory strategies and deletion; (4) Agent Skills governance/versioning (agentskills.io or equivalent); (5) resolve the date conflicts (A2A 1.0, A2A foundation move, MCP Registry GA). Update products.json, notes.md, sources.csv in place (IDs continue from your last), archive as before, validate JSON, reply with a ≤200-word delta summary. If budget runs out, stop cleanly and list exactly what remains.
```

### A7: C5–C8 gap-filling

```text
Continue Stream A7: run the gap-filling pass now (fresh search budget this turn). Note: stream ⑧ has independently sourced SR 26-2 / OCC 2026-13 / FDIC FIL-15-2026 (17 April 2026) superseding SR 11-7 — you may cite that in notes but keep your own records sourced from your own searches. Priority: (1) ModelOp, Collibra AI Governance, Credo AI platform, IBM watsonx.governance — current product status, deployment, certifications, pricing model, and regulatory-framework support claims (EU AI Act, NIST AI RMF, ISO 42001, SR 11-7/SR 26-2, PRA SS1/23) via WebSearch allowed_domains on each vendor's domain; (2) Helicone acquisition/status; Vantage and CloudZero AI-cost features; FinOps Foundation "FinOps for AI" guidance; (3) LaunchDarkly AI Configs status, certifications, pricing; (4) Prisma AIRS data-processing regions and FedRAMP status. Update products.json, notes.md, sources.csv in place (IDs continue from A7-S098), archive as before, validate JSON, reply with a ≤200-word delta summary. If budget runs out, stop cleanly and list exactly what remains.
```

### A4: L2 gap-filling

```text
Continue Stream A4: run the L2 gap-filling pass now (fresh search budget this turn). Priority: (1) Together AI, Fireworks AI, Cerebras, OpenRouter — certifications (SOC 2/ISO/HIPAA via trust centres), data retention / ZDR policy, EU region availability, pricing examples (dated), funding/IPO status (Cerebras IPO) — WebSearch with allowed_domains on each vendor domain (together.ai, docs.together.ai, fireworks.ai, docs.fireworks.ai, cerebras.ai, inference-docs.cerebras.ai, openrouter.ai) plus major news for funding; (2) LM Studio licence/commercial-use terms (lmstudio.ai); (3) vLLM governance (PyTorch Foundation membership) and SGLang/RadixArk relationship; (4) CrewAI funding from a primary or major-outlet source; (5) LangSmith ISO 27001 conflict — resolve from trust.langchain.com or equivalent. Update products.json, notes.md, sources.csv in place (IDs continue from A4-S129), archive as before, validate JSON, reply with a ≤200-word delta summary. If budget runs out, stop cleanly and list exactly what remains.
```

### A1: L9/L8 gap-filling

```text
Continue Stream A1: run the gap-filling pass now (fresh search budget this turn). Priority: (1) certifications (SOC 2/ISO 27001/HIPAA), EU region, pricing (dated) for Reducto, LlamaParse platform, Unstructured Platform, Confident AI (DeepEval cloud), Comet/Opik Cloud, Arize AX, Braintrust, LangSmith, Firecrawl, Apify — via WebSearch allowed_domains on each vendor domain/trust centre; (2) current Mistral OCR model version and pricing (mistral.ai, docs.mistral.ai); (3) DeepEval OTel support; (4) funding for Firecrawl, Reducto, Crawl4AI from primary or major-outlet sources; (5) Weights & Biases Weave ownership (CoreWeave acquisition) — add the record only if confirmed and material. Update products.json, notes.md, sources.csv in place (IDs continue from A1-S112), archive as before, validate JSON, reply with a ≤200-word delta summary. If budget runs out, stop cleanly and list exactly what remains.
```

### A6: C1–C4 gap-filling

```text
Continue Stream A6: run the gap-filling pass now (fresh search budget this turn). Priority: (1) Microsoft Purview DSPM for AI — current name, GA status, licensing (learn.microsoft.com via search); (2) Protegrity and Skyflow — corporate status (acquisitions/funding 2025–26), certifications, deployment; (3) Okta / Auth0 for AI Agents — product names, GA dates, Cross App Access status, pricing; (4) Bedrock Guardrails and Azure AI Content Safety pricing (dated) and Prompt Shields status; (5) Amazon Verified Permissions status; AgentCore Gateway LLM-inference targets GA status; (6) Llama Guard / Prompt Guard / LlamaFirewall latest versions; (7) trust-centre certifications for LiteLLM Enterprise, Kong, Cloudflare AI Gateway, NeMo Guardrails (NVIDIA). Use WebSearch with allowed_domains on each vendor domain. Update products.json, notes.md, sources.csv in place (IDs continue from A6-S090), archive as before, validate JSON, reply with a ≤200-word delta summary. If budget runs out, stop cleanly and list exactly what remains.
```
