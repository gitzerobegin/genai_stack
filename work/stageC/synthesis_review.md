# Stage C review of the synthesis

| | |
|---|---|
| **Date** | 9 October 2026 |
| **Target** | `work/stageC/synthesis.md` (edited in place; the lead architect's voice kept) |
| **Checked against** | `CONTEXT.md`; `work/stage0/09_stageC_synthesis_brief.md`; CP1–CP4 decision files; `work/stageB/_review/all_scores.md` (with the CP4 changes) and `CP4_review_C.md`; §4 of the V1 and V2 verification logs; `05_Data/products.json` and `regulatory_facts.json`; the 17 sections in `work/stageB/*/section.md`; `checkpoints/CP1/02_What_Changed_Since_Original_Diagram.md` |
| **Web searches** | None. No factual correction needed one, so `work/stageC/sources_added.csv` was not created. |
| **Tag check** | `python3 -I tools/check_tags.py . work/stageC/synthesis.md`: 28,231 words; VF 488, R 4, AJ 185, Rec 90, NPV 12; **0 unknown IDs; 0 long untagged paragraphs**; no banned words. The only "American spelling" flagged is the proper noun "API Center". |
| **Tables** | Every pipe table checked by script: column counts match the header in every row, a separator row follows every header, and blank lines surround each table. |

## 1. Change log

| # | Location | Before | After | Reason |
|---:|---|---|---|---|
| 1 | Preamble, tier-change lead-in | "These are treated as final even where a section file still shows the earlier tier" | The L1, L2 and L3 sections and `all_scores.md` now show the final tiers; the drafted column is kept for traceability | Sections have now been updated with the CP4 tiers (task 1) |
| 2 | Preamble table, header | "Section draft" / "Final tier (CP4)" | "Drafted tier (before CP4)" / "Final tier (CP4, reader's decision)", with the decision number on each row | The column no longer describes the section files. Reader-set tiers are now attributed to the reader. |
| 3 | Preamble table, Anthropic | "FS ≈ 3.80 … with a qualified non-Anthropic fallback; an independent alternative always named" | "FS 3.80 … (CP4-1) … one of two vendors …; independent alternatives GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5" | `all_scores.md` gives exactly 3.80. The condition now matches the L1 §1.7 tier line, and the alternatives are named. |
| 4 | Preamble table, Google ADK | Drafted tier: "Strategic, conditional (CP4 review)" | "Tactical, conditional, FS 3.35 (reviewer C proposed Strategic)" | The drafted tier was Tactical (`CP4_review_C.md` line 92); the reader confirmed Strategic at CP4-4 |
| 5 | Preamble table, Fireworks AI and Claude Agent SDK | No drafted FS | Added FS 3.65 and FS 2.65 respectively | Traceability against `all_scores.md` and L3 §3.8 |
| 6 | Preamble, tier counts | "rule 10 (hyperscaler lead services)" | Rule 10 glossed; source named as `all_scores.md` | Recount confirmed 58 / 67 / 13 / 2 and 19 Strategic items below FS 3.6. The gloss is for the executive reader. |
| 7 | Part I, top | (none) | New "In brief" block of five tagged bullets: the problem, the recommendation, the lead stack, the regulatory clock, the conflict-of-interest caveat | Part I must stand alone for an MD-level reader (task 4). It adds no new facts; the dates are from `regulatory_facts.json`. |
| 8 | I.1 finding 2 | "SpaceX acquired xAI on 2 February 2026" | Adds "and the model vendor now operates as SpaceXAI (formerly xAI)" | V2 §4 item 1 naming rule. The wording matches L1 §1.7 [V2-S011]. |
| 9 | I.2 default-choices table, L1 row | AWS: "Claude Sonnet 5.5 or a GPT-6 tier on Bedrock, the other as fallback". Google: "Claude Sonnet 5.5 … as fallback". Neutral: Anthropic with no route note. | AWS: EU region, "confirm GPT-6 EU availability", Mistral as an alternative fallback. Google: Mistral named as the independent alternative (confirm model and region). Neutral: "hyperscaler route only". | GPT-6 Astra on Bedrock is in-Region only in two US Regions [A5-S008, V2-S079]; L1 §1.9 says "confirm EU availability" and names Mistral on Google Cloud as the independent alternative. Conflict-of-interest rule. |
| 10 | I.3 Keep table, Docling/Unstructured | "MIT under LF AI & Data, graduated August 2026; ACL-digest connectors" | The attributes are split by product | As written, the MIT licence and LF AI & Data status read as applying to Unstructured, which is Apache-2.0 [A1-S011] |
| 11 | I.3 Keep table, MCP and A2A | "Strategic only behind a governed gateway (CP3)" | Adds "reader's decision" and the independent alternative to MCP (OpenAPI tools behind the same gateway) | Conflict of interest: an Anthropic-originated standard in a recommendation must have an alternative named beside it, and a reader-set tier must be attributed |
| 12 | I.3 Keep table, model vendors | "The portfolio candidates; the tier comes with its route condition" | Adds that Anthropic's tier was set by the reader at CP4 and that Anthropic is never the only qualified vendor | Conflict-of-interest attribution |
| 13 | I.4 "Tiers carry conditions" | "The five hyperscaler AgentCore records (L3, L4, L5, C1, C4) … security 4 and deployment 2 agree across all of them" | "The four AgentCore records (L3, L4, L5, C1), together with AgentCore Policy inside the C4 Cedar record … agree across the four records" | The C4 Cedar record scores deployment 4, not 2 (`all_scores.md`). Only four records are AgentCore records. |
| 14 | I.4 hyperscaler model services | "in the same sense as rule 10" | Rule 10 glossed in a parenthesis | Readability: Part I stands alone |
| 15 | I.4 departures | "except in four places"; bullet: "The L1, L2 and L3 section texts still show the pre-CP4 tiers … the reader's CP4 decisions prevail here" | "except in three places … No score or tier is changed"; the bullet is replaced by a "Tiers and sections agree" paragraph | The statement was no longer true (task 1). The L1 §1.7, L2 §2.8 and L3 §3.7–3.8 sections now carry the CP4 tiers. |
| 16 | III H3, resulting change | "Strategic only behind this sub-layer (CP3)" | "(the reader's CP3 decision; MCP originated at Anthropic)" | Reader-set tier attribution; conflict of interest |
| 17 | V.2 GPAI Code of Practice | "xAI signed only the Safety and Security chapter" | "xAI (now SpaceXAI) signed only …" | V2 §4 item 1 naming rule. `R-EU-GPAI-COP` says xAI; the parenthesis reconciles the two. |
| 18 | V.6 concentration table | "Fable 5 was suspended 12 June – 1 July 2026" | "Claude Fable 5 was made unavailable from 12 June to 1 July 2026" | The fact cell [V2-S004] says "made unavailable (service disruption) … restored from 1 July". "Suspended" implies a cause the fact does not state. |
| 19 | VI.2 L1 row | AWS: "a GPT-6 tier or Mistral fallback (independent alternative to Claude named)". Google: "Claude Sonnet 5.5 via Google Cloud EU fallback". | AWS: Bedrock EU; "GPT-6 tier (confirm EU availability) or Mistral as the independent fallback". Google: adds Mistral as the independent alternative. | As for row 9 (L1 §1.12 table) |
| 20 | VI.2 note heading | "Why the L1 row names Claude only for AWS" | "… names Claude as primary only for AWS" | The same row also names Claude as the Google Cloud fallback |
| 21 | VII preamble | Anthropic entries: "a Claude model, MCP or Agent Skills" | Adds the Claude Agent SDK and the reader's CP4/CP3 tier attribution. New paragraph "Only profiled products are named": access patterns are not scored, and platform features (API Center, inference profiles) are cited features | Task 1 rule on profiled products; task 3 attribution |
| 22 | Stack A, C1 | "Kong AI Gateway hybrid (S)" | "(S, cond.: Kong is the API standard)" | XI.1 and C1 make Kong conditional; the tier must travel with its condition |
| 23 | Stack A, C2 alternative | "Check Point AI Guardrails (T, via Lakera)" | "Check Point AI Guardrails, formerly Lakera Guard (T)" | Product name as in the C7 record (`C7-lakera`) |
| 24 | Stack A, L3 alternative | "Pydantic AI (S, cond.) for typed steps; DBOS" | "…; no profiled alternative to Temporal (DBOS not profiled)" | DBOS has no product record; a stack cell may name only profiled products |
| 25 | Stack A, L5 alternative; Stack C, L5 | "Graphiti self-hosted or Mem0 OSS (T)" | "Graphiti self-hosted (Zep record, T) …" | Graphiti is profiled only inside `L5-zep`; this makes the record and tier traceable |
| 26 | Stack A, L4 | Azure "APIM + API Center private registry"; Google "Apigee MCP" | Tiers added: "APIM AI gateway (S, cond.)", "Apigee MCP (S, cond.)" | Tier consistency with the other cells |
| 27 | Stack A, L1 | AWS "Claude Sonnet 5.5 or a GPT-6 tier on Bedrock EU; the other as fallback"; Google "… Claude … fallback" | AWS "… in an EU region (confirm GPT-6 EU availability); the other, or Mistral, as fallback"; Google adds Mistral | As for row 9: "Bedrock EU" for GPT-6 is not verified [A5-S008, V2-S079] |
| 28 | Stack B, L6 (AWS) | "S3 Vectors (T) as cost tier behind OpenSearch" | "… behind a search engine (OpenSearch not profiled [NPV])" | OpenSearch has no product record |
| 29 | Stack B, L4 | "APIM + API Center registry"; "Apigee MCP"; "OpenAPI tools (alternative to MCP)" | Tiers added; "alternative to the Anthropic-originated MCP" | Tier consistency; conflict-of-interest wording aligned with Stack A |
| 30 | Stack B, L2 | "Bedrock / Foundry / Gemini Enterprise Agent Platform" | Each marked "(pattern, not scored)" | These have no product records (I.4); the cells must say so |
| 31 | Stack B, L1 | AWS "Claude Sonnet 5.5 (S, cond.) or GPT-6 tier (S); the other as fallback"; Google "Claude Sonnet 5.5 fallback" | AWS: "GPT-6 tier (S, confirm EU availability); the other, or Mistral, as fallback". Google: "Claude Sonnet 5.5 (S, cond.) or Mistral fallback". | As for row 9; Claude's tier condition shown |
| 32 | Stack C, L1 | "… gpt-oss-120b"; licence column "Apache-2.0 / Modified MIT / Apache-2.0" | "gpt-oss-120b (OpenAI record, S)"; licences spelt out per model (Medium 3.5 Modified MIT; Large 3 Apache-2.0) | The licence list did not map one-to-one onto the four models named (`L1-mistral` licence_model) |
| 33 | Stack D, L2/L1 (AWS) | "Bedrock: Claude Sonnet 5.5 or GPT-6 tier, the other as fallback" | "… or a GPT-6 tier (confirm EU availability), the other or Mistral as fallback" | As for row 9; independent alternative to Claude |
| 34 | IX.3 table | "the Fable 5 suspension" | "the three-week Fable 5 outage" | As for row 18 |
| 35 | IX.4, L4 acceptable | "Skills format" | "Skills format (Anthropic-maintained; alternative: C5 packages or AGENTS.md) [VF: A3-S115]" | Conflict of interest: Agent Skills named with an alternative |
| 36 | X.3 reason 3 | "a Gemini Flash version lives about five months" | "recent Gemini Flash versions live about five to six months" | Matches L1 §1.4 [B-L1-S003] and V.6 |
| 37 | XI.1 FinOps FOCUS | "1.4 ratified, 1.5 adds model identity" | "1.4 ratified 4 June 2026; 1.5 (no ratification date) adds model-identity properties, and a token-type column is deferred" | V2 §4 item 11 (FOCUS 1.5 token column deferred); `C6-finops-focus` strategic_direction |
| 38 | XI.1 Anthropic, condition | "FS ≈ 3.80, tier set by the reader at CP4" | "FS 3.80, tier set by the reader at CP4 (CP4-1)" | Exact value from `all_scores.md` |
| 39 | XI.1 Anthropic, reason | "Product-scoped SOC 2, ISO 27001 and ISO 42001; in-tenant on all three hyperscalers" | "… with the API, Bedrock and Google Cloud routes in scope (Azure-hosted Foundry deployment still in process); available on all three hyperscalers" (+V2-S063) | The `L1-anthropic` certifications cell lists the Azure-hosted Foundry deployment as "In-Process Q4 2026". "In-tenant on all three" overstated the evidence in Anthropic's favour. |
| 40 | XI.1 MCP and MCP authorisation | "(CP3)" | "(tier set by the reader, CP3)" | Reader-set tier attribution |
| 41 | XI.1 Pydantic AI, SGLang, Fireworks AI; XI.4 Claude Agent SDK | "(CP4)" | "(reader's decision, CP4-4)"; "(reader's decision, CP4-9)" | Reader-set tier attribution |
| 42 | XI.3 GLM row | "MIT Flash weights only, after sanctions review" | Adds "on Azure it runs on Fireworks outside the tenant (CP4-3)" [A5-S087] | CP4-3 requires the hosting caveat to be stated; it was on the Kimi row but not the GLM row |
| 43 | XI.5 intro | (none) | A sentence noting that two avoid rows (Chinese-origin vendor APIs; billing intermediation) rest on grounds next to the four CP4-7 grounds, kept as [AJ] | CP4-7 says "evidence-based only" on four named grounds. The departure is now stated, as the brief's rule 2 requires. |
| 44 | XI.6 FOCUS 1.5 | "Add model-identity columns" | "Map the new model-identity properties; keep token splits in SKUs, because the input/output token-type column is deferred" | 1.5 adds properties "with no new columns" [V2-S046]; V2 §4 item 11 |
| 45 | XI.6 D.C. Circuit | "D.C. Circuit rehearing on the Anthropic FASCSA designation" | "D.C. Circuit holding on Anthropic's FASCSA designation (upheld 25 September 2026; effect stayed pending a rehearing petition)" | V2 §4 item 2: state the holding only. "Rehearing" as the item name implied that a rehearing was under way; the fact cell says a petition is pending. |

## 2. Accuracy spot-check (45 claims; [VF]/[R] against the fact cells and sections)

Every item below matched its cited fact cell or section. Items marked † were corrected (see §1).

| # | Claim (location) | Source checked | Result |
|---:|---|---|---|
| 1 | Dynatrace completed the Arize acquisition on 1 October 2026 (I.1) | `L9-arize-ax` status_events [V1-S005] | Match |
| 2 | ClickHouse announced the Langfuse acquisition on 16 January 2026 (I.1) | `L9-langfuse`, `C5-langfuse-prompts` [A1-S021, V2-S041] | Match |
| 3 | Promptfoo "announced 9 March 2026", no closing published (I.1, H8, XI) | V1/V2 §4 wording; L9 | Match: never written as completed |
| 4 | Nebius closed the Tavily acquisition on 19 February 2026 (I.1) | `L4-tavily` [A3-S084, V1-S041] | Match; no deal value used |
| 5 | Stripe agreed to buy OpenRouter on 19 August 2026, closing pending (I.1, XI) | `L2-openrouter` [V1-S059, V1-S060] | Match; no price used |
| 6 | SpaceX acquired xAI on 2 February 2026 (I.1) | L1 §1.7 [V2-S011] | Match † (naming) |
| 7 | GPT-6 family: Astra, Sol, Luna, plus GPT-6.1 Sol (I.1) | `L1-openai` current_name [A5-S002] | Match |
| 8 | Fable 5.1 sits above Opus, Sonnet and Haiku 5.5 (I.1) | `L1-anthropic` lineup [A5-S010, A5-S019] | Match |
| 9 | Mistral Medium 3.1 retired 31 August 2026 (I.1) | L1 §1.7 [B-L1-S002] | Match |
| 10 | Gemini Flash released 13 August 2026 retires 28 January 2027; 3.7 Flash (I.1, X.1) | L1 §1.7 [B-L1-S003] | Match; lifetime wording aligned † |
| 11 | Microsoft Agent Framework GA 2 April 2026; AutoGen in maintenance (I.1, XI.5) | `L3-microsoft-agent-framework` [A4-S008] | Match (the 3 April conflict is on the do-not-rely list; the synthesis uses 2 April, as the section does) |
| 12 | Agent Builder shuts down 30 November 2026 (I.1, X.1) | `L3-openai-agents-sdk` [A4-S054] | Match |
| 13 | MCP donated to AAIF on 9 December 2025 (I.1) | `L4-mcp` [A3-S018] | Match |
| 14 | A2A 1.0.0 joined AAIF in August 2026 (I.1) | `L4-a2a` [A3-S079, A3-S116] | Match |
| 15 | Entra Agent ID GA April 2026 (XI.1) | `C4-entra-agent-id` [V2-S032] | Match |
| 16 | Okta for AI Agents GA 30 April 2026; Agent SSO 24 August 2026 (XI.1) | `C4-okta-auth0-ai-agents` [A6-S100, V2-S035] | Match |
| 17 | AgentCore Policy GA 3 March 2026 (XI.1) | C4 §C4.7, C1 [A6-S026] | Match |
| 18 | S3 Vectors GA since December 2025 (I.1) | `L6-s3-vectors` [A2-S081] | Match |
| 19 | LangMem has had no release since 27 October 2025 (I.1, XI.4) | `L5-langmem` [A3-S006] | Match |
| 20 | Malicious LiteLLM 1.82.7/1.82.8 on 24 March 2026; signed images from 1.83.0 (I.1, XI.1) | `C1-litellm` [A6-S008, A6-S009] | Match |
| 21 | Composio's May 2026 token and key exposure (I.1, XI.5) | L4 [B-L4-S007] | Match |
| 22 | TGI repository archived 21 March 2026 (I.1, XI.5) | `L2-hugging-face` [V1-S054] | Match |
| 23 | Helicone acquired by Mintlify on 3 March 2026; maintenance mode (XI) | `C6-helicone` [A7-S112] | Match |
| 24 | Phoenix ELv2; Firecrawl server AGPL-3.0; Jina weights non-commercial (I.1) | `L9-arize-phoenix`, `L8-firecrawl`, `L7-jina` | Match |
| 25 | Claude Agent SDK governed by Anthropic's Commercial Terms (I.1) | `L3-claude-agent-sdk` licence_model [A4-S092] | Match |
| 26 | Docling MIT, LF AI & Data Graduate August 2026 (I.3, XI.1) | `L8-docling` [V1-S091, A1-S057] | Match † (attribution split) |
| 27 | pgvector 0.8.7 (XI.1) | `L6-pgvector` [V1-S020] | Match |
| 28 | Kong AI Gateway 2.x GA (XI.1) | C1 §C1.7 [A6-S016, V2-S034] | Match |
| 29 | Apigee MCP support GA 31 March 2026 (XI.2) | `C1-google-apigee-ai-gateway` [A6-S023] | Match |
| 30 | Gemini 3.8 Flash price doubles on 1 January 2027 (X.1) | `L1-google-gemini` pricing [V2-S010] | Match (US$0.75/3.75 → US$1.50/7.50) |
| 31 | OpenAI removes GPT-5.1 and GPT-5.4-Nano on 1 April 2027 (X.1) | L1 §1.7 [B-L1-S001] | Match |
| 32 | Claude retirements "not sooner than" September/October 2027 (X.1) | L1 §1.9 [A5-S010] | Match |
| 33 | Claude Sonnet 5.5 and GPT-6.1 Sol at US$2/US$10 per 1M tokens (VI.2) | `L1-anthropic`, `L1-openai` pricing [A5-S011, A5-S004] | Match |
| 34 | GPT-6 Astra on Bedrock in-Region only in two US Regions; OpenAI's UK endpoint stores but does not process in the UK (V.4, VI.2) | `L1-openai` gdpr_residency [A5-S008, V2-S079] | Match; drove corrections † 9, 19, 27, 31, 33 |
| 35 | Fable 5 unavailable 12 June – 1 July 2026 (V.6) | `L1-anthropic` status_events [V2-S004] | Wording corrected † |
| 36 | Anthropic certification scope (XI.1) | `L1-anthropic` certifications [A5-S021, V2-S063] | Corrected † (Azure-hosted Foundry in process) |
| 37 | OpenAI's ISO 42001 scope does not name the API Platform (V.7) | `L1-openai` certifications [A5-S007] | Match |
| 38 | FOCUS 1.4 ratified; 1.5 model identity; token column deferred (XI) | `C6-finops-focus` [V2-S046, A7-S116] | Corrected † |
| 39 | SGLang CVE-2026-3059: NVD/OSV reference a fix in 0.5.10, GitHub advisory none (XI.1, XI.6) | L2 §2.7 [B-L2-S009, B-REVC-S002] | Match |
| 40 | SGLang hosted by LMSYS, Apache-2.0 (Stack C) | `L2-sglang` [A4-S065, A4-S010] | Match |
| 41 | Mistral licences: Medium 3.5 Modified MIT, Large 3 Apache-2.0 (Stack C) | `L1-mistral` licence_model [A5-S074] | Clarified † |
| 42 | Mem0 removed external graph stores from its open-source build (I.1) | L5 [A3-S053] | Match |
| 43 | DeepSeek V4 sold directly by Azure; Kimi and GLM via Fireworks outside the tenant (I.4, XI) | `L1-deepseek` deployment [A5-S087] | Match; GLM caveat added † |
| 44 | D.C. Circuit upheld the FASCSA designation 25 September 2026, effect stayed (XI.6) | `L1-anthropic` status_events [A5-S084] | Holding only † |
| 45 | 39 of 80 tiles flagged: 9 acquired, 9 mispositioned, 8 renamed, 8 version label, 6 NPV, 4 duplicated, 3 superseded, 2 deprecated (I.1) | Recount of `checkpoints/CP1/02_*` rows 1–80 | Match |

**Tier and count consistency.** Recounted from `all_scores.md`: 58 Strategic, 67 Tactical, 13 Experimental and 2 not scored, with 19 Strategic items below FS 3.6. XI.1 (41 items) plus XI.2 (17) gives 58; XI.3 has 67 rows and XI.4 has 13. Every "(S/T/E)" label in Part VII matches `all_scores.md`.

**Regulatory statements** were checked against `regulatory_facts.json`; all match:

| Instrument | What the synthesis states |
|---|---|
| R-US-MRM | SR 26-2 issued 17 April 2026; supersedes SR 11-7 and SR 21-8; GenAI and agentic AI expressly out of scope; the US$30bn relevance threshold; RFI unpublished at 7 October |
| R-PRA-SS123 | Effective 17 May 2024; internal-model scope; Principle 1.1(b) |
| R-EUAIA / R-EU-OMNIBUS-AI | GPAI enforcement from 2 August 2026; Annex III from 2 December 2027; Annex I from 2 August 2028; Regulation (EU) 2026/1744 in force 27 July 2026; Article 50(2) grace period to 2 December 2026; Articles 25, 26 and 27 |
| R-EU-GPAI-COP | Signatories, and the xAI chapter-only signature |
| R-DORA | CTPP list of 18 November 2025: 19 providers, no model vendor; register by 31 March |
| R-UK-CTP | Designations from 13 July 2026: AWS, Google Cloud, Microsoft, Oracle; no model vendor |
| R-PRA-SS221 / R-FCA-SYSC8 | PS7/26 and PS26/2 from 18 March 2027 |
| R-EBA-OUTSOURCING | EBA/GL/2026/09 finalised 18 September 2026 |
| R-DATA-TRANSFERS | Adequacy to 27 December 2031; C-703/25 P pending |
| Other records | R-NIST-AIRMF, R-OWASP-LLM/AGENTIC, R-INTL-AI-ASSETMGMT, R-SEC-ADVISERS and R-UK-AI-STATEMENTS |

## 3. Do-not-rely enforcement (V1 and V2 §4)

| Item | Status in the synthesis |
|---|---|
| Press deal values and valuations | None used anywhere. The only figure is the SR 26-2 US$30bn threshold, which is a regulatory fact. |
| Promptfoo | Always "announced" (9 March 2026), with closing in "monitor" |
| OpenRouter | Always "pending" |
| Vendor benchmarks | None used as inputs; IV.3 row 23 rejects them explicitly |
| FOCUS 1.5 token column | Now stated as deferred (XI.1, XI.6) † |
| D.C. Circuit | Holding only, with no scope claim † |
| SpaceXAI | "SpaceXAI (formerly xAI)", with no rebrand date † |
| Distillation allegation | Not mentioned in the synthesis, so it is never presented as fact |
| Fireworks ISO | Never relied on; the tier is conditional on confirming the certificates |
| Agent Skills | Never called foundation-governed; "Anthropic-maintained" |
| Microsoft Agent Framework date | 2 April 2026, as in the section |
| Chinese-vendor API prices | None used |

## 4. Conflict-of-interest check

- **Disclosure.** It is present at the top of the synthesis and is now also summarised in Part I "In brief".
- **Alternatives named.** Every recommendation or stack cell naming Claude, the Claude Agent SDK, MCP, MCP authorisation or Agent Skills now names an independent alternative in the same cell or row. Corrections † 9, 11, 19, 27, 31, 33 and 35.
- **Not above its tier.**
  - Anthropic appears only as Strategic, conditional, with its route condition. It is never the sole vendor or listed first.
  - One overstatement in Anthropic's favour ("in-tenant on all three hyperscalers") was removed † 39.
  - The Claude Agent SDK stays Experimental throughout.
- **Reader-set tiers attributed to the reader.**
  - Claude: CP4-1.
  - MCP and MCP authorisation: CP3.
  - SGLang, Fireworks AI, Pydantic AI and Google ADK: CP4-4.
  - The Claude Agent SDK maturity score: CP4-9.

## 5. Items left for the lead architect (not changed)

- **Agent Skills in Stack D.** Stack D "Do NOT build yet" lists Agent Skills without an alternative. It is an exclusion, not a recommendation, so no alternative is needed.
- **I.1 density.** I.1 keeps its ten numbered findings at full length. The new "In brief" block gives the MD-level reader a two-minute entry point; shortening the findings further would have meant removing tagged substance.
- **XI.5 avoid-list grounds.** The two avoid rows noted in change 43 are a judgement call against CP4-7. The reader may prefer to move them to "monitor".
