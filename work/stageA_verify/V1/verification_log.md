# Stage A′ verification log: verifier V1

Streams checked: A1_L9_L8, A2_L7_L6, A3_L5_L4, A4_L3_L2. Verification date: 8 October 2026.
Sources: `work/stageA_verify/V1/sources.csv` (V1-S001 to V1-S098). Archive: `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/V1/` (98 files).

**Method.** Each claim got a fresh search, scoped to the vendor's domain where possible. Extended mode was used for recent facts. Free primary checks covered the rest:

- the PyPI JSON API and the npm registry, for about 60 package versions and dates;
- raw GitHub licence and changelog files, for Crawl4AI, Firecrawl, MinerU and pgvector;
- GitHub repository metadata via the GitHub MCP search tool, for archive flags;
- a direct fetch of docs.claude.com.

About 110 web searches were used, and the budget was stopped early to leave headroom for V2. Anthropic-originated claims (the Claude Agent SDK, MCP, Agent Skills) got the same or stricter scrutiny, and independent corroboration was sought for each.

**Integrity note for the orchestrator.** Edited records now cite `V1-S…` IDs. `tools/build_dataset.py` reads only `work/stageA/*/sources.csv`, so it will report these IDs as "unknown source" until it also reads `work/stageA_verify/*/sources.csv`. All V1 IDs cited in the products files (96 of 98; V1-S012 and V1-S072 are cited only in this log) resolve in the V1 `sources.csv`. All four products files are valid JSON (21, 20, 17 and 23 records).

## 1. Summary

A row may bundle several claims. For example, each "PyPI re-check" row covers 6 to 13 package versions.

| Stream | Rows checked | Confirmed | Corrected | Downgraded | Unresolvable | Notes |
|---|---:|---:|---:|---:|---:|---|
| A1 (L9/L8) | 26 | 22 | 2 | 2 | 0 | Plus about 8 package versions re-checked on PyPI |
| A2 (L7/L6) | 28 | 24 | 3 | 0 | 1 | The unresolvable row is EthicalAgents/Ragoos, still not found. Includes 1 negative acquisition sweep |
| A3 (L5/L4) | 17 | 15 | 2 | 0 | 0 | Plus 13 package versions re-checked |
| A4 (L3/L2) | 29 | 24 (1 upgraded) | 4 | 1 | 0 | Plus about 15 package versions re-checked |
| **Total** | **100** | **85** | **11** | **3** | **1** | |

"Confirmed" includes confirmations where V1 added a primary source or raised `conf`. "Corrected" includes filling a "Not publicly verified" cell with a newly sourced fact.

## 2. Claim table

| Record id | Field | Claim (before) | Outcome | After | Sources |
|---|---|---|---|---|---|
| **Stream A1** | | | | | |
| L9-arize-phoenix / L9-arize-ax | status_events, company | Dynatrace acquisition US$915M; completed 1 Oct 2026 ("one report says 2 October") | Confirmed (conf medium->high) | Completed 1 October 2026 per Dynatrace IR release (4:05 p.m. EDT); signed 13 Aug 2026; US$915M (~US$815M cash). The "2 October" variant is a time-zone/wire artefact; drop it | V1-S005 |
| L9-arize-phoenix | licence_model | Elastic License 2.0, not OSI | Confirmed | Unchanged; PyPI license field Elastic-2.0 | V1-S013 |
| L9-promptfoo | status_events | Acquired by OpenAI (announced 9 Mar 2026) | Confirmed (announcement) / Downgraded (completion) conf high->medium | Announcement confirmed; no dated closing notice found; "part of OpenAI" rests on README | V1-S006 |
| L9-langfuse | status_events | ClickHouse acquisition, January 2026 (16 Jan per third parties) | Confirmed | 16 January 2026 per ClickHouse blog; terms undisclosed; licensing unchanged per Langfuse | V1-S007 |
| L9-langfuse | version_or_lineup | langfuse 4.17.0 (5 Oct 2026) | Confirmed | PyPI | (PyPI re-check) |
| L8-llamaparse | current_name / status_events | LlamaCloud renamed LlamaParse; old SDKs deprecated | Confirmed | LlamaIndex docs "LlamaParse (formerly LlamaCloud)"; llama-parse and llama-cloud-services deprecated in favour of llama-cloud 2.x | V1-S008 |
| L8-firecrawl | licence_model | Server AGPL-3.0 | Confirmed | LICENSE file is GNU AGPL v3 | V1-S002 |
| L8-firecrawl | adoption_signals | US$75M Series B, Smash Capital, 22 Sep 2026 | Confirmed (primary) | Blog dated 22 Sep 2026; changelog entry dated 20 Aug; Form D first sale 31 Aug 2026 for US$82.06M preferred (RuntimeWire) | V1-S015, V1-S009 |
| L8-mineru | licence_model, version | 4.0.10 (29 Sep 2026); Apache-2.0 + >100M MAU / >US$20M monthly revenue threshold + attribution | Confirmed | LICENSE.md text matches; PyPI licence expression LicenseRef-MinerU-Open-Source-License | V1-S003, V1-S004 |
| L8-crawl4ai | licence_model | Apache-2.0 with attribution requirement | Confirmed | LICENSE appends an "Attribution Requirement" for all distributions, publications or public uses; note this extra term sits outside standard Apache-2.0 | V1-S001 |
| L8-crawl4ai | version_or_lineup | v0.9.4, 23 Sep 2026 | Confirmed | PyPI | (PyPI re-check) |
| L8-mistral-ocr | version_or_lineup | OCR 4.1, launched July 2026 (16 or 26 July); OCR 4.0 retired 30 Sep 2026 | Corrected (detail) | OCR 4.1 released July 2026 (model page 16 July; changelog 26 July), changelog marks it GA on 26 August 2026 (governance page gives 13 August); OCR 4.0 deprecated 26-29 Sep, retired 30 Sep 2026 | V1-S014, V1-S010 |
| L8-mistral-ocr | pricing | US$4 per 1,000 pages; batch US$2; annotated US$5 | Confirmed | | V1-S010 |
| L9-wandb-weave | status_events | CoreWeave completed 5 May 2025 | Confirmed (conf medium->high) | | V1-S011 |
| (A1 notes H8) | OTel GenAI semconv | Development status; moved to semantic-conventions-genai in v1.42.0 | Confirmed | Core semconv now at 1.44.0; new repo has no tagged release | V1-S012 |
| L9-deepeval, L9-opik, L8-docling, L8-unstructured | version_or_lineup | PyPI versions | Confirmed | deepeval 4.2.8; opik 2.2.94 (7 Oct); docling 2.135.0; unstructured-ingest 1.11.19 | (PyPI re-check) |
| L9-langsmith | status_events / strategic_direction | Fleet renamed from Agent Builder | Confirmed | Changelog "Agent Builder is now LangSmith Fleet"; self-hosted v0.15 renames agentBuilder* keys | V1-S016 |
| L9-braintrust | adoption_signals | US$80M Series B, Feb 2026 | Confirmed (Reported, secondary) | 17 Feb 2026, led by ICONIQ at US$800M post-money (Axios, paywalled) | V1-S017 |
| L8-reducto | adoption_signals | US$75M Series B (a16z, Oct 2025) | Confirmed | 14 Oct 2025 (Cooley). A single-source report of a US$51M Series B-1 (Aug 2026, US$1.04B) is NOT to be relied on | V1-S018 |
| L8-unstructured | current_name / category | Commercial offering now "Transform v2 API" | Confirmed | transform.unstructured.io/api/v2 Parse/Extract | V1-S019 |
| L9-langsmith | certifications | SOC 2 II, ISO 27001:2022, HIPAA (BAA) | Confirmed (medium) | ISO 27001 stated on Engine security page; BAA rests on older Academy FAQ | V1-S068 |
| L8-firecrawl | certifications | SOC 2 Type II, ZDR, PII redaction | Confirmed (vendor marketing only; conf stays medium) | No trust-centre report seen | V1-S080 |
| L9-arize-ax | certifications | SOC 2 II; ISO 27001 (A-LIGN, c. Aug 2026); HIPAA; PCI DSS 4.0; CSA STAR L1 | Partially confirmed | Official compliance docs list SOC 2 II, PCI DSS 4.0, HIPAA, CSA STAR L1 but NOT ISO 27001; ISO 27001 appears only on the self-hosted marketing page; HIPAA only on Enterprise tier. Keep conf medium; writers should hedge ISO 27001 | V1-S084 |
| L8-apify | certifications / gdpr_residency | SOC 2 Type II; AWS us-east-1 only | Confirmed | Auditor Prescient Security | V1-S089 |
| L8-unstructured | certifications | SOC 2 Type 2, ISO 27001, HIPAA | Confirmed + enriched | API docs also list CMMC 2.0 Level 2 (certified, 110/110) and "adherence" to FedRAMP; FedRAMP authorisation NOT evidenced - writers must not claim FedRAMP | V1-S090 |
| L8-docling | status_events | Governance moved to LF AI & Data (date not verified) | Corrected (filled) | Donated March 2025 as Incubation project (induction announced 29 Apr 2025); Graduate tier August 2026 | V1-S091 |
| **Stream A2** | | | | | |
| L7-voyage | status_events | Acquired by MongoDB, closed 17 Feb 2025 (announced 24 Feb 2025) | Confirmed | 10-K: acquisition date 17 Feb 2025, US$160.9M (US$141.4M stock + US$19.5M cash) | V1-S023 |
| L7-voyage | version_or_lineup | Voyage 4 (15 Jan 2026); rerank-3 / rerank-3-lite (30 Sep 2026) | Confirmed, with caveat | Blog says available now; MongoDB lifecycle page lists rerank-3 as Preview. Add caveat | V1-S024 |
| L7-jina | status_events | Elastic acquisition "7-9 October 2025" | Confirmed (narrowed) | Completion announced 9 October 2025 (IR) | V1-S025 |
| L7-jina | version_or_lineup, licence_model | v5-text (Feb 2026), v5-omni (May 2026), CC-BY-NC-4.0 | Confirmed | v5-text 18 Feb 2026; v5-omni 7 May 2026; CC-BY-NC-4.0, commercial via Elastic | V1-S026 |
| L7-cohere | version_or_lineup | Embed 5 Pro/Fast 30 Sep 2026; Rerank 4 11 Dec 2025 | Confirmed | | V1-S027, V1-S033 |
| L7-cohere | status_events | Aleph Alpha definitive agreement 16 Sep 2026, pending approval | Confirmed | Valuation and Schwarz financing figures conflict in press; do not quote | V1-S028 |
| L6-pinecone | status_events | Nexus GA 6 Aug 2026 | Confirmed | Data plane runs in customer cloud (AWS/GCP/Azure) | V1-S029 |
| L6-pgvector | version_or_lineup, status_events | 0.8.7 released 5 October 2026 | Corrected | 0.8.7 released 1 October 2026 (CHANGELOG); PostgreSQL.org announcement 5 October 2026; fixes CVE-2026-103484 (IVFFlat build buffer overflow, CVSS 8.8) | V1-S020, V1-S022 |
| L6-pgvector | licence_model | "Open source (extension licence not verified)" conf low | Corrected | PostgreSQL License (permissive, OSI) | V1-S021 |
| L6-s3-vectors | version_or_lineup, status_events | GA Dec 2025; 2bn vectors/index; 31 Regions after Mar 2026 | Confirmed | Some AWS copy says 1bn; 2bn is authoritative (limits page) | V1-S030 |
| L6-s3-vectors | pricing | Storage US$0.06/GB-month etc. | Confirmed (partial) | US$0.06/GB-month seen only as example in AWS blog; full rate card not re-read; keep conf medium | V1-S030 |
| L6-milvus-zilliz | version_or_lineup | 3.0.0 GA 29 Jul 2026 | Confirmed | Release notes 29 Jul; Zilliz PR 16 Jul; blog 27 Jul | V1-S031 |
| L6-qdrant | adoption_signals | US$50M Series B, 12 Mar 2026, AVP | Confirmed | Total funding US$87.8M | V1-S032 |
| L7-sentence-transformers, L6-chroma, L6-pinecone (SDK) | version_or_lineup | 6.1.0 (18 Sep); chromadb 1.5.9 (5 May); pinecone 10.0.0 (3 Sep) | Confirmed | PyPI re-check | (PyPI) |
| L6-pinecone | deployment.vpc_byoc | BYOC GA on AWS/GCP/Azure | Confirmed (date added) | GA announced late September 2026; Enterprise plan required; some features (Assistant, Inference, on-demand indexes) were not yet available in BYOC as of late August | V1-S034 |
| L6-mongodb-atlas-vector-search | version_or_lineup | Self-managed Search/Vector Search GA on 8.2+ (Community + EA, SSPL) | Confirmed | | V1-S035 |
| L7-ethicalagents, L7-ragoos | all | Not found | Confirmed (still not found after fresh extended searches) | Keep Not publicly verified | V1-S036 |
| L6-qdrant | certifications | SOC 2 Type II and HIPAA | Confirmed | BAA documented for Managed Cloud only | V1-S069 |
| L6-weaviate | licence_model | BSD-3 core + commercial Enterprise Edition (wl/, licence key), 1.40 RC | Confirmed | 1.40.0 still RC; licence-key enforcement off by default per PR | V1-S070 |
| (sweep) | status_events | No acquisitions of other independents | Negative check | See V1-S072 | V1-S072 |
| L7-gemini-embedding | version_or_lineup | GA 22 Apr 2026 (preview 10 Mar 2026); Vertex AI docs renamed Gemini Enterprise Agent Platform | Confirmed | | V1-S073 |
| L6-turbopuffer | certifications / security_features | SOC 2 Type 2; HIPAA BAA (Scale+); per-namespace CMEK (Enterprise); BYOC | Confirmed | Enterprise tier from US$4,096/month +35% usage premium | V1-S077 |
| L6-pinecone | certifications | SOC 2 II (2025, zero deviations), ISO 27001:2022, HIPAA BAA | Confirmed (conf medium->high) | Trust Center primary | V1-S078 |
| L6-elasticsearch | version_or_lineup | Elastic 9.5 GA; VectorDB index mode (preview) | Confirmed | VectorDB index mode and auto-calibration are technical preview | V1-S085 |
| L6-chroma | certifications / pricing / gdpr_residency | SOC 2 II; Team US$250/month; us-east-1 and europe-west1 | Confirmed | | V1-S086 |
| L7-sentence-transformers | company / status_events | Now maintained by Hugging Face (transition c. late 2025) | Confirmed | | V1-S092 |
| L7-qwen3-embedding | status_events | Qwen3-VL-Embedding/-Reranker January 2026 | Confirmed | Paper 8 Jan 2026; 2B and 8B | V1-S093 |
| L7-nvidia-nemo-retriever | status_events | "Embedding NIM 2.3: nemotron-3-embed-1b" | Corrected (minor) | Model added in NIM release 2.2; 2.3 is current | V1-S094 |
| **Stream A3** | | | | | |
| L4-mcp | version_or_lineup / status_events | Spec 2026-07-28 released 28 Jul 2026; stateless core; DCR, Roots, Sampling, Logging, HTTP+SSE deprecated | Confirmed | | V1-S037 |
| L4-mcp | company / status_events | Donated to AAIF (Linux Foundation) 9 Dec 2025 | Confirmed | AAIF formed 9 Dec 2025 with MCP, goose, AGENTS.md | V1-S038 |
| L4-mcp | status_events | EMA extension stable (18 Jun 2026) | Confirmed (stable status); exact date not re-checked | | V1-S045 |
| L4-a2a | version_or_lineup | 1.0.0 on 12 Mar 2026 | Confirmed | Tag dated 2026-03-12; first stable spec | V1-S039 |
| L4-a2a | status_events / company | Joined AAIF (17 Aug 2026 announcement; A2A blog 27 Aug) | Confirmed | Secondary coverage dates move 17-20 Aug 2026; A2A blog confirms Growth Stage project | V1-S039, V1-S038 |
| L4-agent-skills | status_events | Published as open standard 18 Dec 2025 | Confirmed (secondary + Anthropic-originated) | Independent adoption confirmed in OpenAI Codex docs. Governance: NOT an AAIF project on available evidence; secondary claims that Anthropic "stewards it through AAIF" are unsupported | V1-S040, V1-S046, V1-S047 |
| L5-mem0 | status_events | v2.0.0 (14 Apr 2026) removed graph stores; graph memory Platform-only | Confirmed (nuance) | OSS replaces graph with built-in entity linking (not a queryable graph); detailed deletions logged under v2.0.1 in SDK changelog | V1-S043 |
| L5-zep | status_events | Community Edition deprecated (date not verified) | Confirmed | Official post: no further updates or support; repo stays Apache-2.0 in legacy/. Date still unconfirmed (third parties: April 2025) | V1-S044 |
| L5-letta | strategic_direction | "Letta's Next Phase" (March 2026) | Confirmed | Post exists, dated March 2026; server-side features retired. "V1 server retired to archive branch" not re-confirmed by search (rests on Stage A GitHub evidence) | V1-S042 |
| L4-tavily | status_events | Nebius acquisition announced 10 Feb 2026, accounted as completed | Confirmed + enriched | Closed 19 February 2026 (Nebius 20-F); US$275M is Bloomberg-reported only | V1-S041 |
| L5-*/L4-* | version_or_lineup | PyPI versions (mem0ai 2.2.1, letta 0.34.4, cognee 1.6.3, graphiti 0.30.2, zep-cloud 3.30.0, langmem 0.0.30 (27 Oct 2025), tavily 0.8.5, exa-py 2.25.0, composio 0.25.0, e2b 2.53.1, browserbase 1.20.0, mcp 2.3.0, a2a-sdk 1.2.2) | Confirmed | PyPI re-check 8 Oct 2026 | (PyPI) |
| L5-aws-agentcore-memory | status_events / maturity | AgentCore GA Oct 2025 incl. Memory | Confirmed | GA 13 Oct 2025; now 15 Regions; 2026 feature additions | V1-S087 |
| L5-gcp-vertex-memory-bank | status_events / maturity | "GA (date not verified)" | Corrected | GA announced December 2025 (release notes, alongside 16 Dec 2025 pricing update) | V1-S088 |
| L5-gcp-vertex-memory-bank | pricing | rates not captured | Corrected (filled) | US$0.25 per 1,000 memories stored; US$0.50 per 1,000 retrieved; LLM billed separately; charging from 28 Jan 2026 | V1-S088 |
| L4-e2b | certifications / deployment.vpc_byoc | SOC 2 Type II (control-plane scope); BYOC AWS/GCP (Azure conflict) | Confirmed | | V1-S096 |
| L4-composio | version_or_lineup | 0.25.0; 2.0.0b0 pre-release 31 Aug 2026 | Confirmed | PyPI | V1-S098 |
| L4-composio | certifications | SOC 2 Type II, ISO 27001:2022 (vendor-stated) | Confirmed (vendor marketing only) | | (search, not archived) |
| **Stream A4** | | | | | |
| L3-openai-agents-sdk | status_events | Agent Builder shuts down 30 Nov 2026 | Confirmed | Deprecation announced 3 Jun 2026; Evals dashboard/API and v1/prompts also shut 30 Nov 2026 | V1-S051 |
| L3-claude-agent-sdk | status_events | Renamed from Claude Code SDK 29 Sep 2025 | Confirmed (minor nuance) | claude-agent-sdk 0.1.0 first uploaded 28 Sep 2025 (UTC); public rename 29 Sep 2025 | V1-S049 |
| L3-claude-agent-sdk | licence_model | MIT repo LICENSE but use governed by Anthropic Commercial Terms | Confirmed | Docs "License and terms" section, fetched directly | V1-S048 |
| L3-microsoft-agent-framework | status_events | 1.0.0 GA 2 Apr 2026 | Confirmed | PyPI 1.0.0 uploaded 2026-04-02 16:39 UTC; some Microsoft posts say 3 April | V1-S050, V1-S052 |
| L2-hugging-face | status_events | TGI maintenance mode as of 11 Dec 2025 | Corrected (incomplete) | Add: TGI GitHub repository archived (read-only) on 21 March 2026; last push 21 Mar 2026; latest release v3.3.7 | V1-S054, V1-S055 |
| L3-langgraph | status_events | LangGraph Platform renamed LangSmith Deployment 14 Oct 2025 | Confirmed | | V1-S056 |
| L2-cerebras | status_events | IPO priced 13 May 2026 at US$185, Nasdaq CBRS | Confirmed | Shares traded below IPO price c. early Oct 2026 after lock-up (secondary) | V1-S053 |
| L2-together-ai | status_events | US$800M Series C at US$8.3B, 1 Jul 2026 | Confirmed (conf medium->high) | | V1-S057 |
| L2-fireworks-ai | status_events | US$1.505B Series D at US$17.5B, Jul 2026 | Confirmed | 15-16 July 2026 | V1-S058 |
| L3-* / L2-* | version_or_lineup | PyPI versions (langgraph 1.2.14, llama-index-core 0.14.25, pydantic-ai 2.54.0, openai-agents 0.23.1, mistralai 3.1.0, agent-framework 1.20.0, vllm 0.31.0 (5 Oct), sglang 0.5.21) | Confirmed | crewai advanced to 1.15.25 on 7 Oct 2026 23:52 UTC (after Stage A check of 1.15.24) | (PyPI) |
| L2-openrouter | status_events / company / strategic_risk.acquisition | [] "Not publicly verified"; What-changed flag "No change" | Corrected (major) | Stripe signed agreement to acquire OpenRouter, announced 19 Aug 2026; closing expected "in the coming weeks"; no completion notice found as of 8 Oct 2026. Press-reported value US$7-8B+ (undisclosed). OpenRouter to keep brand and product | V1-S059, V1-S060 |
| L2-openrouter | adoption_signals | US$113M Series B (Reported, low; "secondary source") | Upgraded | Company press release 26 May 2026 confirms US$113M led by CapitalG -> Verified fact; US$1.3B valuation remains press-reported | V1-S061 |
| L2-openrouter | pricing | 5.5% fee on credit purchases | Confirmed (detail) | 5.5% non-crypto (US$0.80 min), 5.0% crypto; BYOK 5% fee to be replaced by subscription | V1-S062 |
| L2-sglang | status_events | RadixArk US$100M seed, 5 May 2026, US$400M post | Confirmed (conf medium->high) | Business Wire release | V1-S063 |
| L2-vllm | status_events | PyTorch Foundation-hosted since 7 May 2025 | Confirmed (conf medium->high) | | V1-S064 |
| L3-mistral-agents | version_or_lineup / maturity | mistralai-workflows 3.15.0 Beta, built on Temporal | Confirmed | Announcement says v3.0 "publicly available"; docs say Public Preview; PyPI classifier Beta | V1-S065 |
| L2-ollama | pricing / status_events | Ollama Cloud hosts larger models | Confirmed + enriched | 31 Aug 2026 usage-based pricing: Free / Pro US$20 / Max US$100 / Team US$500 per month; US+EU compute, ZDR (vendor claim) | V1-S066 |
| L2-fireworks-ai | certifications | SOC 2 II, HIPAA, ISO 27001/27701/42001 | Confirmed with conflict | One Fireworks docs page still lists the three ISO certifications as "(in progress)"; request certificates from trust.fireworks.ai | V1-S067 |
| L2-ollama | adoption_signals | Not publicly verified | Corrected (filled) | US$65M raise reported by SiliconANGLE (9 Jul 2026); Reported, medium | V1-S071 |
| L2-ollama | pricing | "pricing page referenced, not retrieved" | Corrected (filled) | See V1-S066 | V1-S066 |
| L3-pydantic-ai | status_events | v2.0.0 on 23 Jun 2026 | Confirmed (conf medium->high) | v1 security fixes for at least 6 months after v2 | V1-S074 |
| L3-crewai | current_name / status_events | "CrewAI Enterprise rebranded CrewAI AMP" (Verified fact, medium) | Downgraded (conf low) | No explicit rename notice found; rests on inference from /enterprise/ doc paths and older naming | V1-S075 |
| L2-lm-studio | licence_model | Proprietary; free for internal business use; commercial-licence requirement removed | Confirmed | Change dates to c. July 2025 | V1-S076 |
| L2-together-ai | certifications | SOC 2 Type 2, ISO 27001:2022; HIPAA inconsistent | Confirmed | Latest SOC 2 Type 2 report 17 Jun 2026; ISO 27001 via A-LIGN; customer BAA not confirmed | V1-S079 |
| L3-openai-agents-sdk | status_events | Hosted Agents API public beta 10 Sep 2026 | Confirmed | Computer use added 29 Sep 2026 | V1-S083 |
| L3-vercel-ai-sdk | version_or_lineup | ai 7.0.131; 7.0 released 25 Jun 2026; Apache-2.0 | Confirmed | 7.0.0 published 25 Jun 2026; now 7.0.132 (7 Oct) | V1-S082 |
| L3-google-adk, L3-aws-strands-agentcore, L3-temporal, L2-nvidia-dynamo | version_or_lineup | 2.11.0; 1.58.1; 1.34.0; 1.5.1 | Confirmed | PyPI re-check | (PyPI) |
| L2-cerebras | certifications | SOC 2 Type 2; HIPAA not listed; EU capacity targeted end-2026 | Confirmed | Trust centre lists SOC 2 Type 2, GDPR, CCPA only | V1-S095 |
| L2-hugging-face | certifications | SOC 2 Type 2; BAA via Enterprise plan | Confirmed (scope caveat) | BAA not explicitly tied to Inference Endpoints | V1-S097 |

## 3. Corrections to the "What changed" rows (notes.md, not edited; writers must apply)

1. **A4, OpenRouter.** The row currently reads "No change (scope widened toward C1)". It should read **"Acquired (pending)"**:
   - Stripe and OpenRouter announced on 19 August 2026 that Stripe has agreed to acquire OpenRouter.
   - Closing was expected "in the coming weeks", but no completion notice had appeared by 8 October 2026.
   - The price is undisclosed. Press reports put it at US$7B to more than US$8B.
   - Stage A had dismissed this as an "uncorroborated tracker" claim.
   - The US$113M Series B (26 May 2026) is confirmed by the company's own release, so it can now be labelled Verified fact rather than Reported.
   - Sources: V1-S059, V1-S060, V1-S061.
2. **A4, Hugging Face / TGI.** Add that the TGI GitHub repository was **archived (read-only) on 21 March 2026**. This goes beyond "maintenance mode as of 11 December 2025". Sources: V1-S054, V1-S055.
3. **A2, Postgres + pgvector.** Change "pgvector 0.8.7 (5 October 2026)" to **"0.8.7, released 1 October 2026 (announced 5 October)"**. It fixes CVE-2026-103484 (CVSS 8.8). The extension licence is the **PostgreSQL License**. Sources: V1-S020, V1-S021, V1-S022.
4. **A1, Mistral OCR.** Change "OCR 4.1 (`mistral-ocr-latest`, July 2026)" to **"OCR 4.1, released July 2026, GA 26 August 2026"**. Mistral's own pages give 16 July, 26 July and 13 August. OCR 4.0 was retired on 30 September 2026, as Stage A said. Source: V1-S014.
5. **A1, Promptfoo.** "Acquired by OpenAI" should read **"acquisition announced 9 March 2026"**. No closing notice exists; the "part of OpenAI" wording in the README is the only sign that the deal completed. Source: V1-S006.
6. **A1, Phoenix and Arize.** The Dynatrace completion date is **1 October 2026**, per the Dynatrace IR release. Drop the "2 October" variant. Source: V1-S005.
7. **A3, Tavily.** Add **"closed 19 February 2026"**, from Nebius's FY2025 Form 20-F. US$275M is a figure reported by Bloomberg, not disclosed by Nebius. Source: V1-S041.
8. **A4, CrewAI.** "CrewAI AMP, formerly CrewAI Enterprise" is an inference. No explicit rename notice was found, so present it as "earlier materials call it CrewAI Enterprise". Source: V1-S075.
9. **A3, Mem0.** Graph memory is Platform-only. However, open-source v2 replaced the graph stores with built-in **entity linking**, which is not a queryable graph. The SDK changelog files the deletions under v2.0.1. Source: V1-S043.
10. **A2, Voyage AI.** rerank-3 / rerank-3-lite (30 September 2026) are listed as **Preview** on MongoDB's model lifecycle page, although the Voyage blog says "available now". Source: V1-S024.
11. **A2, Pinecone.** BYOC was announced **generally available in late September 2026**. It requires the Enterprise plan, and some features (for example Assistant, Inference and on-demand indexes) were not yet available in BYOC as of late August. Sources: V1-S034, V1-S029.
12. **A2, NVIDIA Embed.** nemotron-3-embed-1b was added in Embedding NIM **2.2**; 2.3 is the current version. Source: V1-S094.
13. **A1, Docling.** Governance moved to the foundation in **March 2025**, when IBM donated it as an Incubation project. Graduate tier followed in **August 2026**. Source: V1-S091.
14. **A1, Unstructured.** Add **CMMC 2.0 Level 2**. Do **not** carry over the "FedRAMP adherence" wording from the API docs: no FedRAMP authorisation was found. Source: V1-S090.
15. **A3, Agent Skills.** The 18 December 2025 open-standard date is confirmed, and so is independent adoption (OpenAI Codex docs). However, there is **no neutral governance body**. Agent Skills is not an AAIF-hosted project on available evidence. Sources: V1-S040, V1-S046, V1-S047.
16. **A2, Jina AI.** The Elastic acquisition was completed on **9 October 2025**, not "7-9 October". Source: V1-S025.

These cells were also corrected in the products files but do not appear in any "What changed" row:

- Vertex Memory Bank: GA December 2025, priced at US$0.25 per 1,000 memories stored and US$0.50 per 1,000 retrieved (V1-S088).
- Ollama Cloud: pricing published 31 August 2026 (V1-S066), and a US$65M round reported in July 2026 (V1-S071).
- Arize AX: ISO 27001 hedged (V1-S084).
- Fireworks: one docs page still lists the ISO certifications as "in progress" (V1-S067).

## 4. Claims the writers must not rely on

- **OpenRouter as "independent" or "No change".** It is under a pending acquisition by Stripe. Treat any Stripe deal value as press-reported only.
- **Promptfoo acquisition as "completed".** Say "announced 9 March 2026".
- **Arize AX ISO 27001.** It is not on the official AX compliance page; ask for the certificate.
- **Fireworks ISO 27001 / 27701 / 42001.** Fireworks' own pages conflict ("achieved" vs "in progress").
- **Unstructured "FedRAMP".** It is a vague "adherence" claim with no authorisation found.
- **"HIPAA" claims without a confirmed customer BAA** for Together AI, Hugging Face Inference Endpoints, Cerebras and Firecrawl. Each is vendor wording only, or the BAA scope is unclear.
- **Firecrawl, Composio and Reducto security claims.** These come from vendor marketing pages only, with no trust-centre report seen.
- **Valuations and secondary funding figures:**
  - Braintrust US$800M (Axios, paywalled)
  - Cohere–Aleph Alpha ~US$20B and the Schwarz financing amount
  - Reducto Series B-1 US$51M / US$1.04B (single aggregator)
  - Tavily US$275M
  - OpenRouter US$1.3B
  - Cerebras post-IPO price moves
  - Pinecone "exploring a sale" (secondhand)
- **Vendor-reported benchmark claims:** Pinecone Nexus τ-Knowledge 47.4%, Voyage rerank-3 gains, Cohere Embed 5 "highest average", Firecrawl Alexandria "+21%".
- **"CrewAI AMP formerly CrewAI Enterprise"** as a confirmed rename.
- **Agent Skills as foundation-governed.** It is an Anthropic-originated, vendor-hosted specification. MCP and A2A are AAIF projects; Agent Skills is not, on available evidence.
- **Exact dates where vendor pages conflict:**
  - Mistral OCR 4.1 (July vs August 2026)
  - Microsoft Agent Framework 1.0 (2 April per PyPI; some Microsoft posts say 3 April)
  - Zep Community Edition deprecation date (unconfirmed)
  - Firecrawl Series B (blog 22 September vs changelog 20 August)

## 5. Not checked by V1 (budget stopped cleanly; resume here)

Every V1-assigned What-changed row was checked except those noted below. The remaining unchecked items, in priority order:

1. **Pricing (mostly unchecked):**
   - A1: Langfuse, LangSmith, Braintrust, Opik (US$19 vs US$39 conflict), Confident AI, Firecrawl credit tiers, LlamaParse credits, Reducto, Unstructured per-page rate (US$0.015 vs US$0.03), Apify, Google Document AI
   - A2: Pinecone rate card, S3 Vectors full rate card (only the US$0.06/GB-month example was re-seen), Qdrant, Zilliz, Weaviate, MongoDB Search Nodes, Cohere Embed 5 / Rerank, Voyage, Jina, Gemini Embedding 2
   - A3: Mem0, Zep, Supermemory, Composio, Exa, Tavily, Browserbase, E2B
   - A4: Together, Fireworks, Cerebras, OpenRouter plan tiers (Business 8%), LM Studio Enterprise, Hugging Face
2. **Certifications not re-checked:**
   - A1: Langfuse Cloud, Braintrust, Opik/Comet, Confident AI, LlamaParse, Reducto, Mistral, W&B, Datadog
   - A2: Weaviate (SOC 2 / ISO / HIPAA), Zilliz, MongoDB Atlas, Elastic Cloud, Cohere (ISO 42001), Voyage trust portal, Jina API
   - A3: Mem0, Zep, Letta Cloud, Supermemory, Exa, Tavily, Browserbase
   - A4: OpenRouter (SOC 2 Type 2, no BAA), LM Studio
3. **Versions and dates not re-checked:**
   - Qdrant server 1.19.2 (5 October 2026): the GitHub releases API was not reachable.
   - Weaviate 1.39.7.
   - Milvus 3.0.2.
   - Elastic 9.5 GA date (4 August 2026) and OpenSearch 3.9.0.
   - LangGraph 1.0 (17 October 2025) and CrewAI 1.0 (20 October 2025) dates.
   - Pydantic AI 1.0 date.
   - Supermemory v5 API features.
   - Cognee licensed Postgres graph.
   - MCP Registry v0.1 status and the 8 April 2026 maintainer changes.
   - A2A 1.0.1 date.
   - MCP EMA "18 June 2026" date: stable status was confirmed, the date was not.
   - Letta "V1 server retired to archive branch" (the repository itself is not archived).
   - LangMem activity status.
   - Google ADK 2.0 date; NVIDIA Dynamo and llm-d status.
   - Together and Fireworks "ZDR default" claims.
   - OpenAI "Assistants API sunset 26 August 2026".
   - Mistral SDK 3.0.0 changes.
4. **Other:**
   - Datadog Agent Observability and Google Document AI records: nothing checked.
   - Ollama US$65M round: details beyond the SiliconANGLE headline are unconfirmed.
   - Cerebras EU region status.
