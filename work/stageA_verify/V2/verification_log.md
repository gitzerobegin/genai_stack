# Stage A′ verification log: verifier V2

Verifier V2 · streams A5_L1, A6_C1_C4, A7_C5_C8, A8_Regulation · as of 8 October 2026 · 79 new sources (`V2-S001` to `V2-S079`)

**Conflict-of-interest disclosure.** This verifier is an Anthropic model. Anthropic claims were re-read from Anthropic's own pages and then held to the same test as every other vendor. No Anthropic claim was upgraded on Anthropic's word alone. Anthropic's allegation against Chinese labs stays labelled as an unadjudicated competitor allegation.

## 1. Summary

**Method.**

- I used about 92 web searches (out of the shared budget of about 200 per turn) plus direct fetches.
- The direct fetches came from these hosts, which are not blocked:
  - anthropic.com and platform.claude.com
  - the PyPI JSON API
  - proxy.golang.org
  - raw.githubusercontent.com
- Each claim was re-searched with a new query. Where possible I restricted the search to the vendor's or regulator's domain.
- Each row in section 2 is one check. Some rows bundle several closely related claims.

| Stream | Check rows | Confirmed | Corrected | Downgraded | Unresolvable |
|---|---:|---:|---:|---:|---:|
| A5_L1 (foundation models) | 38 | 29 | 8 | 1 | 0 |
| A6_C1_C4 (gateway, guardrails, DLP, identity) | 21 | 20 | 1 | 0 | 0 |
| A7_C5_C8 (prompts, FinOps, AI security, governance) | 17 | 14 | 1 | 1 | 1 |
| A8_Regulation | 16 | 16 | 0 | 0 | 0 |
| **Total** | **92** | **79** | **10** | **2** | **1** |

**How to read the outcomes.**

- **Confirmed** rows often refined dates or added detail. Examples:
  - the EBA reference EBA/GL/2026/09
  - the 12 June 2025 SEC withdrawal action
  - ISO/IEC 42006 published on 7 July 2025
  - the Entra Agent ID GA month
- **Corrected** means a value was changed or an omitted material event was added.
- **Unresolvable** means the value was kept but flagged in `stage_a_notes`.

**Files edited in place.** Every edit was followed by JSON validation, and every new `src` ID resolves in `work/stageA_verify/V2/sources.csv`. The files are:

- `work/stageA/A5_L1/products.json`
- `work/stageA/A6_C1_C4/products.json`
- `work/stageA/A7_C5_C8/products.json`
- `work/stageA/A8_Regulation/regulatory_facts.json`

**How the edits are marked.**

- Each edited record has a note in `stage_a_notes` beginning `[V2 verification 8 October 2026]`.
- `last_verified` is set to 2026-10-08 where the field exists.

**What was not edited.** I left the `notes.md` files alone because the brief does not authorise editing them. Section 3 lists the "What changed" rows that the writers or the stream owners must update.

**Archive.** All sources are archived in `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/V2/` (79 files):

- 10 direct snapshots (`.txt`)
- 69 search-tool or direct-fetch extracts (`.extract.txt`)

Some files are direct fetches but carry the generic "direct fetch blocked" header from `save_extract.py`. These are V2-S028 (PyPI) and V2-S061 (Go proxy). Their `FOUND VIA` line says they were direct fetches.

## 2. Verification table

| Record id | Field | Claim (before) | Outcome | After | Sources |
|---|---|---|---|---|---|
| L1-anthropic | version_or_lineup | Fable 5.1 (1 Sep 2026) top GA; Opus 5.5 22 Sep; Sonnet 5.5 28 Sep; Haiku 5.5 7 Oct; Mythos 5.1 trusted access; 1M ctx/128K out | Confirmed (direct fetch) | unchanged; conf high | V2-S001, V2-S003, V2-S004 |
| L1-anthropic | pricing | Fable 5.1 US$10/50; Opus 5.5 US$4/20; Sonnet 5.5 US$2/10; Haiku 5.5 US$0.10/0.50 (<=100K) | Confirmed (direct fetch) | unchanged | V2-S002 |
| L1-anthropic | status_events | (missing) Fable 5 access unavailable 12 Jun 2026, restored 1 Jul 2026 | Corrected (added omitted event) | added "9 Jun 2026 Fable 5; 12 Jun 2026 access suspended; 1 Jul 2026 restored" | V2-S004 |
| L1-anthropic | status_events | D.C. Cir. upheld FASCSA designation 2-1 on 25 Sep 2026 (No. 26-1049), stayed; N.D. Cal. ruling stands | Confirmed (secondary law-firm sources; opinion not read) | unchanged; label kept, note scope dispute | V2-S005 |
| L1-anthropic | status_events | Draft S-1 confidentially submitted 1 Jun 2026 | Confirmed (secondary) | unchanged | V2-S006 |
| L1-anthropic | status_events | Bartz final approval 20 Jul 2026, US$1.5bn | Confirmed; judge is Martinez-Olguin (not Alsup) | detail added | V2-S007 |
| L1-openai | version_or_lineup | GPT-6 Astra 3 Sep 2026 staged; "not yet GA" at launch; API 4 Sep | Confirmed; later broad rollout to Plus/Pro/Business/Enterprise and API | unchanged; note broadened availability | V2-S008 |
| L1-openai | pricing | gpt-6-astra US$10/US$50 | Confirmed | unchanged | V2-S008 |
| L1-google-gemini | version_or_lineup | Gemini 4 Argon announced 30 Sep 2026, restricted (Fairwind) | Confirmed (date from Stage A; announcement page found) | unchanged | V2-S009 |
| L1-google-gemini | version_or_lineup | 3.8 Flash GA 2 Sep 2026; 3.1 Pro still preview | Confirmed | unchanged; pricing note intro to 31 Dec 2026 then US$1.50/7.50 | V2-S010 |
| L1-xai-grok | status_events/company | xAI merged into SpaceX 2 Feb 2026 | Confirmed (primary x.ai post + TechCrunch) | label Reported->Verified fact for merger | V2-S011 |
| L1-xai-grok | company | SpaceXAI rebrand ~6 Jul 2026 | Downgraded (date conflict: July vs 7 May 2026; no primary) | date "mid-2026 (July per Wikipedia; 7 May per other)"; Reported/low | V2-S011 |
| L1-xai-grok | company | further rename to SpaceXSI "unconfirmed" | Corrected | Musk announced 4 Oct 2026 SpaceXAI will become SpaceXSI; not yet effected as of 5-8 Oct (Reported) | V2-S011 |
| L1-xai-grok | version_or_lineup/pricing | Grok 4.7 21 Sep 2026, US$2/6, 500K | Confirmed (record already carries the >200K tier) | src added | V2-S012 |
| L1-deepseek | version_or_lineup / status_events | V4-Pro status after 14 Sep 2026 "conflicting" | Corrected | Phase-out reversed: pricing-page footnote (17 Sep 2026) says V4-Pro API continues, billing unchanged; V4.1-Flash 10 Sep confirmed; no V4.1-Pro date. Reported/medium | V2-S013 |
| L1-alibaba-qwen | licence_model | Qwen3.8-2.4T-A95B licence unconfirmed | Corrected (Reported) | custom "Qwen3.8-Max License"; MaaS >US$50m TTM revenue needs separate licence; weights 12 Aug 2026; hosted Max 3 Aug 2026 | V2-S014 |
| L1-alibaba-qwen | version_or_lineup | Qwen3.8 current; 27B Apache 2.0 | Confirmed (secondary) | dates added | V2-S014 |
| L1-moonshot-kimi | version_or_lineup / licence | K3 16 Jul 2026; weights by 27 Jul; 2.8T; Kimi K3 License | Confirmed (secondary only); add 104B active | unchanged; conf stays medium | V2-S015 |
| L1-zai-glm | version_or_lineup | GLM-5.3 "~late August 2026" | Corrected (refined) | GLM-5.3 API 18 Aug 2026, weights 28 Aug 2026 (bespoke licence); GLM-5.3-Flash 26 Aug 2026 (MIT) | V2-S016 |
| L1-mistral | version_or_lineup | Large 4 public preview 6 Oct 2026; weights by end Oct; ~1T/49-52B | Confirmed (secondary); weights date 27 Oct per VentureBeat | unchanged | V2-S017 |
| L1-mistral | version_or_lineup / licence | Medium 3.5 28 Apr 2026, 128B, Modified MIT v26.04, US$1.5/7.5 | Confirmed (primary docs extract); context 256K | conf medium kept | V2-S018 |
| L1-meta | version_or_lineup | Meta Model API GA globally (Meta Connect 2026) | Confirmed (Meta developer recap; Connect 23-24 Sep 2026); pre-Connect page still said preview | unchanged | V2-S019 |
| L1-meta | version_or_lineup | Muse Spark 1.3 2 Sep 2026; Glimmer 30B Apache 2.0 | Confirmed (1.3 primary; Glimmer licence secondary only) | unchanged | V2-S019 |
| L1-google-gemma | version_or_lineup / licence | Gemma 4 31 Mar 2026; 12B 3 Jun 2026; Apache 2.0 | Confirmed (primary) | licence conf medium -> high | V2-S020 |
| L1-zai-glm | status_events | GLM-5.3 release date; CAISI GLM-5.3 Sep 2026 | Confirmed CAISI; release date conflict: 14 Aug (CAISI) vs 18 Aug (secondary) | record both; prefer CAISI | V2-S021, V2-S016 |
| L1-moonshot-kimi | (notes c2) | CAISI/UK AISI Kimi K3 July 2026 findings | Confirmed | unchanged | V2-S021 |
| L1-anthropic / notes | (c) | Distillation allegation, ~24,000 accounts, 23 Feb 2026 | Confirmed as Anthropic allegation (unadjudicated) | unchanged | V2-S022 |
| notes (c2) Italy | | Garante limitation 30 Jan 2025; no lifting/fine found | Confirmed (no change found as of May 2026) | unchanged | V2-S023 |
| L1-openai | version_or_lineup | GPT-6 Sol/Luna 22 Sep 2026; GPT-6.1 Sol 29 Sep (US$2/10); ChatGPT broad rollout 7 Oct | Confirmed | unchanged | V2-S024 |
| C1-portkey | status_events | Acquired by Palo Alto Networks, closed 29 May 2026; US$117m (10-K) | Confirmed (press release + 10-K/10-Q via extract) | unchanged; announcement-date (30 Apr) not independently confirmed; one outlet says 2 Jun | V2-S025 |
| C2-guardrails-ai | status_events | Acquired by Harvey 9 Sep 2026 | Confirmed (Harvey blog + press); terms undisclosed | conf raised to high | V2-S026 |
| C1-litellm | status_events | PyPI compromise 24 Mar 2026 (1.82.7/1.82.8); clean v1.83.0 30 Mar 2026 | Confirmed; PyPI upload 31 Mar 05:08 UTC (30 Mar US time); 1.82.7/8 removed from PyPI | unchanged (note UTC date) | V2-S027, V2-S028 |
| C1-litellm | version_or_lineup | litellm 1.104.1 MIT | Confirmed (PyPI, 7 Oct 2026) | unchanged | V2-S028 |
| C2-guardrails-ai | version_or_lineup | 0.11.0 Apache-2.0 | Confirmed (PyPI 14 Aug 2026) | unchanged | V2-S028 |
| C3-presidio | version_or_lineup | 2.2.364 (22 Jul 2026) MIT | Confirmed (PyPI) | unchanged | V2-S028 |
| C2-nemo-guardrails | version_or_lineup | 0.24.1 (16 Sep 2026) Apache-2.0 | Confirmed (PyPI) | unchanged | V2-S028 |
| C1-envoy-ai-gateway | current_name / status_events | Renamed Agent Router; moved to Agentic AI Foundation | Confirmed (README re-fetched); repo moved to theagentrouter/agent-router; CRDs/images unchanged | unchanged | V2-S029 |
| C3-presidio | company / status_events | Community-governed under Data Privacy Stack (formerly Microsoft); MIT | Confirmed (transition doc re-fetched) | unchanged | V2-S030 |
| C4-mcp-authorization | version_or_lineup | 2026-07-28: stateless, RFC 9207 iss, DCR deprecated, 12-month deprecation window | Confirmed; Stage A omitted that Roots, Sampling and Logging are deprecated and SSE resumability removed | strategic_direction note added | V2-S031 |
| C4-entra-agent-id | maturity / status_events | GA in 2026 ("What's new page dated 1 May 2026") | Corrected (refined) | GA listed under April 2026 in Entra release log; Agent 365 licensing (E7 incl.; add-on E5/A5/Business Premium) | V2-S032 |
| C4-cedar | status_events | AgentCore Policy GA 3 Mar 2026 (Cedar-based) | Confirmed (GA March 2026, 13 Regions); Dogwood question resolved: Dogwood is open-source, Cedar-compatible superset now used for authoring | note added | V2-S033 |
| C1-kong-ai-gateway | version_or_lineup | AI Gateway 2.0 GA 1 Sep 2026; 2.1.0 and 2.2.0 (30 Sep 2026) | Confirmed (2.0 GA from Kong post, day from third party; 2.2 GA press release 30 Sep 2026); the notes.md row omits 2.2 | src added | V2-S034 |
| C4-okta-auth0-ai-agents | maturity / status_events | Agent SSO GA 24 Aug 2026 (conflict with May 2026) | Confirmed 24 Aug 2026 (press release + OIE release notes August 2026); conflict resolved | conf raised | V2-S035 |
| C3-microsoft-purview-dspm-ai | status_events | Unified DSPM GA May 2026; DSPM for AI folded in | Confirmed; partner sources and DSP Agent still preview; licensing conflict persists | unchanged | V2-S036 |
| L1-google-gemini / C1-google-apigee-ai-gateway | status_events | Vertex AI renamed Gemini Enterprise Agent Platform (date not verified) | Corrected (date found) | rename documented in 22 April 2026 release notes | V2-S037 |
| C7-lakera | status_events | Check Point announced 16 Sep 2025, completed Q4 2025 | Confirmed; closing 22 Oct 2025 (search summary of Check Point releases); ~US$201.8m per 20-F (second-hand) | date refined | V2-S038 |
| C7-prisma-airs | status_events | Protect AI acquired 22 Jul 2025 | Confirmed (PANW IR release) | unchanged | V2-S039 |
| C7-hiddenlayer | strategic_risk.acquisition | Peers acquired: Prompt Security, CalypsoAI, Pangea | Confirmed: Prompt Security->SentinelOne closed 5 Sep 2025; CalypsoAI->F5 closed 26 Sep 2025 (US$145.2m); Pangea->CrowdStrike closed 26 Sep 2025 | dates added | V2-S040 |
| C5-langfuse-prompts | company / status_events | Part of ClickHouse since January 2026 | Confirmed (16 Jan 2026 announcement; no licence change planned) | conf raised | V2-S041 |
| C5-prompts-as-code | company / status_events | Promptfoo now part of OpenAI (closing date unverified) | Confirmed: OpenAI announced agreement 9 Mar 2026; README says "now part of OpenAI"; closing date still not public | announcement date added; label Verified (primary) | V2-S042 |
| C6-helicone | status_events | Acquired by Mintlify 3 Mar 2026; maintenance mode | Confirmed (both vendors' posts) | unchanged | V2-S043 |
| C8-collibra-ai-governance | status_events | Acquired trail ML 5 Oct 2026 | Confirmed (secondary press, multiple) | unchanged | V2-S044 |
| C5-launchdarkly-ai-configs | current_name | Renamed AgentControl (launch post 12 May 2026); API unchanged | Confirmed rename and API continuity (primary docs); date not independently re-confirmed | unchanged | V2-S045 |
| C6-finops-focus | version_or_lineup / strategic_direction | FOCUS 1.4 (June 2026); "FOCUS 1.5 is scoped for AI model identity and input/output tokens" | Corrected | 1.4 ratified 4 Jun 2026. 1.5 confirmed scope: AI pricing dimensions on SkuPriceDetails and four model properties (ModelDeveloper/Family/Id/Version), no new columns; input/output token-type column deferred (split carried by SKU/SkuMeter); no 1.5 ratification date | V2-S046 |
| C7-hiddenlayer | adoption_signals / funding | US$100m Series B Sep 2026; >US$155m total | Confirmed (2 Sep 2026; Delta-v lead; secondary) | date added | V2-S047 |
| C7-prisma-airs | status_events | Koi 14 Apr 2026; AI Gateway GA 16 Jul 2026 | Confirmed | unchanged | V2-S048 |
| R-US-MRM | status_and_dates | SR 26-2 issued 17 Apr 2026 supersedes SR 11-7 and SR 21-8; GenAI/agentic out of scope | Confirmed (Fed primary extract) | unchanged | V2-S049 |
| R-EUAIA / R-EU-OMNIBUS-AI | status_and_dates | 2026/1744 OJ 24 Jul 2026, in force 27 Jul; Annex III 2 Dec 2027; Annex I 2 Aug 2028 | Confirmed (secondary, consistent); regulation dated 8 Jul 2026 | unchanged | V2-S050 |
| R-DORA | status_and_dates | First CTPP list 18 Nov 2025, 19 providers; no AI model vendor | Confirmed (ESA release + law firms); full PDF list not re-read | unchanged | V2-S051 |
| R-UK-CTP | status_and_dates | First designations made 8 Jul, announced 10 Jul, in force 13 Jul 2026: AWS, Google Cloud, Microsoft, Oracle | Confirmed (SI 2026/777) | unchanged | V2-S052 |
| R-PRA-SS221 / R-FCA-SYSC8 | status_and_dates | PS7/26 (Mar 2026) revised SS2/21; FCA PS26/2; MTP notification and register from 18 Mar 2027 | Confirmed (PRA/FCA primary pages via extract); FCA PS26/2 published 18 Mar 2026 | unchanged | V2-S053 |
| R-EBA-OUTSOURCING | status_and_dates | Final 18 Sep 2026; reference "EBA/GL/2026/09" unconfirmed; application date not confirmed | Confirmed; reference EBA/GL/2026/09 now corroborated; application date still not fixed (awaiting translations) | gap closed for reference number | V2-S054 |
| R-DATA-TRANSFERS | status_and_dates | EU-UK adequacy renewed 19 Dec 2025, valid to 27 Dec 2031 | Confirmed | unchanged | V2-S055 |
| R-OWASP-LLM | status_and_dates | 2026 edition Aug-Sep 2026 (2 Sep vs 3 Aug) | Confirmed; conflict persists (press release dated 2 Sep, URL 1 Sep, archive 3 Aug) | unchanged | V2-S056 |
| R-OWASP-AGENTIC | status_and_dates | Launched 9-10 Dec 2025 | Confirmed (OWASP post 9 Dec 2025) | unchanged | V2-S056 |
| R-ISO-42001 | status_and_dates | 42005 May 2025; 42006 July 2025 | Confirmed (ISO catalogue; 42006 published 7 Jul 2025) | conf medium -> high | V2-S057 |
| R-SEC-ADVISERS | status_and_dates | Withdrawn by notice of 17 Jun 2025 | Confirmed with refinement: Commission withdrawal action 12 Jun 2025 (FR notice 17 Jun 2025 per Stage A source) | note added | V2-S058 |
| R-DATA-TRANSFERS | status_and_dates | C-703/25 P pending; Microsoft intervention unverified | Confirmed pending; Microsoft intervention now Reported (late June 2026) | note added | V2-S059 |
| R-NIST-AIRMF | status_and_dates | AI RMF 1.0 under revision; no new version | Confirmed | unchanged | V2-S060 |
| C4-opa / C4-spiffe-spire / C1-agentgateway / C1-envoy-ai-gateway | version_or_lineup | OPA v1.21.1; SPIRE v1.15.3; agentgateway v1.6.0; Agent Router v1.2.0 | Confirmed (Go module proxy, timestamps match) | unchanged | V2-S061 |
| C7-hashicorp-vault | version_or_lineup | Vault 2.1.1 (16 Sep 2026) | Downgraded (possibly stale): git tag v2.1.2 exists (Go proxy) though changelog on main stops at 2.1.1 | note added; conf medium | V2-S061 |
| L1-openai | certifications | SOC 2 Type 2 (1 Jul 2025-30 Jun 2026); ISO 27001/17/18/701; ISO 42001; CSA STAR L1 | Confirmed; ISO 42001 scope wording does not name the API Platform | note added | V2-S062 |
| L1-anthropic | certifications | SOC 2 I/II, ISO 27001:2022, ISO 42001, CSA STAR L2; Foundry "in process Q4 2026" | Confirmed with nuance: Foundry hosted on Anthropic is in scope; Foundry hosted on Azure in process Q4 2026; Claude for Government N/A | refined | V2-S063 |
| C8-collibra-ai-governance | certifications | SOC 2, ISO 27001, ISO 42001 | ISO 42001 confirmed (22 Jan 2025, Schellman) | unchanged | V2-S064 |
| C8-credo-ai | certifications | SOC 2 Type II report dated 31 Dec 2025 | Not re-confirmed (vendor page content not captured; third-party only) | unchanged (residual risk) | V2-S064 |
| C5-launchdarkly-ai-configs | certifications | SOC 2 Type II, ISO 27001/27701, FedRAMP Moderate | Confirmed (vendor pages) | unchanged | V2-S065 |
| L1-anthropic | version_or_lineup | Mythos 5.1 is the same model as Fable 5.1 with different safeguards | Confirmed (launch post, direct fetch) | unchanged | V2-S066 |
| C7-lakera | current_name | "Check Point AI Guardrails" inside AI Defense Plane (23 Mar 2026) | Confirmed (datasheet + docs); no dated rename announcement | unchanged | V2-S067 |
| L1-anthropic | status_events | N.D. Cal. ruled one designation illegal (August 2026) | Corrected (refined) | 27 Aug 2026, Judge Rita F. Lin, No. 3:26-cv-01996 (First Amendment retaliation; due process; APA) | V2-S068 |
| notes (c2) US federal | | NDAA s.1532: whether it covers contractors not confirmed | Corrected (Reported/low) | tracker says prohibition in force ~17 Jan 2026 for DoD and its contractors (DoD contract performance), waivers available; statute not read | V2-S069 |
| L1-xai-grok | status_events | EU DSA proceedings 26 Jan 2026 | Confirmed | unchanged | V2-S070 |
| C2-guardrails-ai | status_events | Hosted hub install and remote inference retired 25 Aug 2026 | Confirmed with conflict: repo HUB_UPDATE.md says hard cutoff 25 Aug 2026 for both; docs-site 0.11 migration guide says 6 Aug 2026 | note conflict; conf medium | V2-S071, V2-S072 |
| C1-azure-apim-ai-gateway | version_or_lineup | AI Gateway tier public preview, East US 2/Sweden Central, free, no SLA | Confirmed | unchanged | V2-S073 |
| C1-cloudflare-ai-gateway | pricing | Unified Billing 5%; new log pricing from 24 Sep 2026 | Confirmed; add unified per-GB log pricing from 1 Dec 2026 (blog) | refined | V2-S074 |
| L1-anthropic | gdpr_residency | inference_geo only global/us; workspace geo only us | Confirmed (direct fetch) | unchanged | V2-S075 |
| L1-openai | gdpr_residency | EU storage+processing with MAM/ZDR; UK storage only | Confirmed | unchanged | V2-S079 |
| R-DATA-TRANSFERS | status_and_dates | DUAA main tranche 5 Feb 2026; all DP provisions in force 19 Jun 2026 | Confirmed with nuance: Information Commission governance provisions still to follow (not DP-substantive) | unchanged | V2-S076 |
| R-INTL-AI-ASSETMGMT | status_and_dates | IOSCO FR/02/2026 (May 2026) | Confirmed: dated 25 May 2026 | date refined | V2-S077 |
| R-EUAIA | status_and_dates | Art. 50 from 2 Aug 2026; 50(2) legacy systems to 2 Dec 2026 | Confirmed (new Art. 111(4)); add new Art. 5(1)(ba)/(bb) prohibitions from 2 Dec 2026 | refined | V2-S078 |
| C7-model-supply-chain-scanning / C7-openssf-model-signing / C8-validmind / C8-openlineage / C5-promptlayer / C5-langfuse-prompts | version_or_lineup | modelscan 0.8.8, picklescan 1.0.5, fickling 0.1.12, safetensors 0.8.0; model-signing 1.1.1; validmind 2.13.14; openlineage-python 1.53.0; promptlayer 1.5.16; langfuse 4.17.0 | Confirmed (PyPI JSON, dates match) | src added | V2-S028 |
| C2-meta-llama-protections | version_or_lineup | llamafirewall 1.0.3 (29 May 2025) latest | Confirmed (PyPI) | src added | V2-S028 |
| C1-google-apigee-ai-gateway | stage_a_notes | Vertex AI renamed Gemini Enterprise Agent Platform (undated) | Confirmed; dated April 2026 (22 April release notes) | no field edit (note only in log) | V2-S037 |

## 3. Corrections to the "What changed" rows (notes.md), listed explicitly

The stream owners or the writers should apply these. I did not edit the notes.md files.

**A5_L1**

1. **Grok row.**
   - Before: "xAI merged into SpaceX (2 February 2026) and was rebranded SpaceXAI (July 2026) (Reported)."
   - After: "SpaceX acquired xAI in an all-stock deal announced and closed on 2 February 2026. xAI's own post confirms this, so it is now Verified. The AI unit was rebranded SpaceXAI in mid-2026, but the date is unverified: sources say July or 7 May. On 4 October 2026 Musk announced that SpaceXAI will be renamed SpaceXSI. This had not taken effect by 5 October 2026." [V2-S011]
   - The gap note "Whether the SpaceXSI rename happened" is now answered: announced, not yet effected.
2. **DeepSeek row.** Add: "The V4-Pro phase-out planned for 14 September 2026 was reversed. DeepSeek's pricing-page note of 17 September says the V4-Pro API continues with billing unchanged." [V2-S013] The gap note "status of DeepSeek V4-Pro after 14 September" is resolved.
3. **Qwen row.**
   - Hosted Qwen3.8-Max launched on 3 August 2026.
   - The Qwen3.8-2.4T-A95B weights followed on 12 August 2026 under a custom "Qwen3.8-Max License", not Apache 2.0. Large MaaS providers need a separate licence.
   - Status: Reported. [V2-S014] The gap note "licence of Qwen3.8-2.4T-A95B" is resolved at Reported level.
4. **GLM ("QI4") row.**
   - Before: "GLM-5.3 and GLM-5.3-Flash (August 2026)."
   - After: "GLM-5.3 API launched in mid-August 2026: NIST CAISI says 14 August, the press says 18 August. Its weights followed around 28 August under a bespoke licence. GLM-5.3-Flash was released on 26 August 2026 under MIT." [V2-S021, V2-S016] The gap note "exact launch dates of GLM-5.3" is resolved, with the 14 vs 18 August conflict recorded.
5. **Claude row.** The row is correct. Two things should be added to the record and the narrative:
   - Claude Fable 5 access was suspended on 12 June 2026 and restored on 1 July 2026. [V2-S004]
   - The N.D. Cal. ruling date is 27 August 2026 (Judge Rita F. Lin). [V2-S068]
6. **Meta row.** "Meta Model API, now GA" is confirmed. Meta announced GA at Connect on 23–24 September 2026. [V2-S019]
7. **Mistral row.** The row is correct. Add that the Large 4 weights are targeted for 27 October 2026 (VentureBeat), and that the preview is API-only. [V2-S017]
8. **Section (c2) of the A5 notes, US federal.**
   - Before: "Whether it covers contractors is not confirmed."
   - After (Reported/low): "A policy tracker says the s.1532 prohibition took effect for DoD and its contractors, when performing DoD contracts, around 17 January 2026. Waivers are available." [V2-S069]
   - Separately, NIST pages now carry the title "CAISSI (Center for Advancing Innovation and Standards for Super Intelligence)". [V2-S021]

**A6_C1_C4**

1. **Kong row.** Add "AI Gateway 2.2 GA (30 September 2026)". [V2-S034] The record already lists 2.2.0.
2. **Guardrails AI row.**
   - Before: "retired on 25 August 2026."
   - After: "The repository notice gives a hard cutoff of 25 August 2026. The docs-site 0.11 migration guide gives 6 August 2026." [V2-S071, V2-S072]
3. **Microsoft Entra Agent ID row.**
   - Before: "GA in 2026 (What's new page dated 1 May 2026)."
   - After: "GA in April 2026 (Entra release log). Security features need Agent 365, which is included in M365 E7 and sold as an add-on to E5/A5/Business Premium." [V2-S032]
4. **Okta row.** The GA conflict (May vs 24 August 2026) is resolved in favour of 24 August 2026. [V2-S035]
5. **Cedar / AgentCore Policy row.** Add "GA in 13 Regions". Also add: "Policies are now authored in Dogwood, an open-source superset of Cedar." [V2-S033]
6. **MCP authorisation row.** Add: "2026-07-28 also makes the protocol stateless, removes SSE resumability, and deprecates the Roots, Sampling and Logging features." [V2-S031]
7. **LiteLLM row.** v1.83.0 is dated 30 March in US time; PyPI shows the upload at 31 March 2026, 05:08 UTC. The exposure window is about 40 minutes per LiteLLM and about 3 hours per Snyk. [V2-S027, V2-S028]
8. **Apigee row.** The Vertex AI → Gemini Enterprise Agent Platform rename is dated April 2026 (22 April release notes). [V2-S037]

**A7_C5_C8**

1. **FinOps FOCUS row.**
   - Before: "FOCUS 1.5 is scoped for AI model identity and input/output tokens."
   - After: "FOCUS 1.4 was ratified on 4 June 2026. FOCUS 1.5 has no ratification date. Its confirmed AI scope is pricing dimensions on SkuPriceDetails plus four model properties (ModelDeveloper, ModelFamily, ModelId, ModelVersion), with no new columns. A first-class input/output token-type column is deferred, so tokens stay in ConsumedUnit/ConsumedQuantity and separate SKUs." [V2-S046]
2. **Prompts-as-code row (Promptfoo).** Add: "OpenAI announced the acquisition on 9 March 2026. The closing date has not been published." [V2-S042]
3. **Langfuse row.**
   - Before: "since January 2026".
   - After: "ClickHouse announced the acquisition on 16 January 2026." [V2-S041]
4. **Lakera row.** The completion date is 22 October 2025 (Check Point Q3 2025 results), not "Q4 2025" in the vague sense. The consideration of about US$201.8m comes from the 20-F at second hand. [V2-S038]
5. **HashiCorp Vault row.**
   - Before: "Vault 2.1.1 (16 September 2026)".
   - After: "2.1.1 is the latest version documented in the changelog, but a v2.1.2 git tag exists." Check before citing. [V2-S061]
6. **HiddenLayer row.** The Series B is dated 2 September 2026. [V2-S047]

**A8_Regulation**

1. **EBA row.** The reference EBA/GL/2026/09 is now corroborated. "Two-year transition" should read: "The application date is not yet fixed because translations are pending. Critical or important arrangements must be reviewed within two years of the application date." [V2-S054]
2. **SEC PDA row.**
   - Before: "Withdrawn 17 June 2025."
   - After: "Withdrawn by Commission action on 12 June 2025; the notice was published on 17 June 2025." [V2-S058]
3. **ISO row.** ISO/IEC 42006 was published on 7 July 2025. [V2-S057]
4. **OWASP LLM 2026 row.** The date conflict stands: the press release is dated 2 September 2026 (its URL path says 1 September), and the archive says 3 August 2026. Cite it as "August–September 2026". [V2-S056]

## 4. Claims the writers must not rely on (or must caveat)

1. **SpaceXAI / SpaceXSI naming and dates.** Use "SpaceXAI (formerly xAI)". Do not state a rebrand date. Do not call the company SpaceXSI. [V2-S011]
2. **The practical scope of the D.C. Circuit ruling on Anthropic (No. 26-1049).** Sources disagree on whether the ruling covers only DoW contracts and DoW contractor performance, or all federal sales. The opinion itself was not read, and en banc review may follow. State the holding and avoid any scope claim. [V2-S005]
3. **Chinese-vendor API prices and most Moonshot, Qwen and Meta Muse Glimmer details.** These rest on aggregators, the LiteLLM price map or secondary blogs. Label them Reported and do not use them as decision inputs. [A5-S038; V2-S014, V2-S015]
4. **"DeepSeek V4 Pro about 8 months behind the frontier" (CAISI).** I could not see this figure in NIST's own text. A third-party blog states it. [V2-S021]
5. **Gemini 4 Argon "1M-token output limit".** Google describes the limit inconsistently. [V2-S009]
6. **Acquisition prices from press.** These are not from filings:
   - Koi: about US$400m
   - Lakera: US$201.8m (from the 20-F at second hand) or about US$300m
   - Portkey: about US$700m (press)

   Use the filing figures where they exist: Portkey US$117m (10-K) and CalypsoAI US$145.2m (10-Q). [V2-S025, V2-S038, V2-S040, V2-S048]
7. **Promptfoo's acquisition closing date.** It is not public. Write "announced 9 March 2026; Promptfoo states it is part of OpenAI". [V2-S042]
8. **HashiCorp Vault "2.1.1 latest".** [V2-S061]
9. **Credo AI's "SOC 2 Type II report dated 31 December 2025".** This was not re-confirmed. [V2-S064]
10. **Guardrails AI hub and hosted-inference cutoff date.** The sources conflict (6 or 25 August 2026). [V2-S071, V2-S072]
11. **"FOCUS 1.5 adds input/output token columns".** The release-scope page says this is deferred. [V2-S046]
12. **UK CTP self-assessments "due mid-October 2026".** This comes from a single commentary. [V2-S052]
13. **All vendor benchmark figures.** These include the Anthropic Fable 5.1, OpenAI Astra, Google Argon, Mistral Large 4 and DeepSeek V4.1-Flash launch posts. All are vendor-reported, so use them as Reported at most.
14. **Anthropic's distillation allegation (about 24,000 accounts).** This is a competitor's unadjudicated allegation, and the author is an Anthropic model. Present it only as "Anthropic alleges". [V2-S022]
15. **Meta Model API "contributor" tier.** Meta uses prompts and completions on this tier to train its models. Writers should present this as a data-use condition, not as a cheaper price point. [V2-S019]

## 5. Not checked (budget/time), so they can be resumed

Search use was about 92 of the shared budget of about 200. I stopped to leave headroom for concurrent agents. These items carry only their Stage A evidence:

- **A5.**
  - Gemini 4 Argon's exact date (30 September 2026). The announcement was found, but its day was not independently re-dated.
  - Gemini 3.5 Pro reported as "cancelled".
  - The GPT-5.6 price cuts of 30 July 2026.
  - gpt-oss-safeguard.
  - OpenAI's Daybreak programme.
  - Anthropic Enterprise Frontier Safeguards timing beyond "later this fall".
  - Grok's older models, xAI data terms and certifications.
  - DeepSeek, Qwen, Kimi and GLM API prices.
  - Data-location terms for Alibaba Model Studio, Moonshot and Z.ai.
  - Mistral certifications and residency.
  - Llama 4 status.
  - The Korea PIPC, Berlin DPA, Australia PSPF, Taiwan and US state-device actions.
  - Zhipu's Entity List date (16 January 2025).
  - The Microsoft Foundry and Bedrock hosting matrices for Chinese models.
- **A6.**
  - LiteLLM SOC 2 (September 2026) and ISO 27001.
  - Kong and Cloudflare certifications.
  - Model Armor and Sensitive Data Protection pricing.
  - Bedrock Guardrails pricing.
  - Azure Content Safety pricing and dates.
  - Protegrity AI Team Edition status.
  - Skyflow certifications, funding, and SDK v1 end of life (31 October 2026).
  - Apigee MCP GA (31 March 2026).
  - AgentCore Gateway inference targets and token rate limits.
  - Auth0 for AI Agents GA (19 November 2025) and Okta for AI Agents GA (30 April 2026).
  - cedar-policy 4.13.0.
  - Purview licensing.
- **A7.**
  - LangSmith (EU region, SOC 2).
  - PromptLayer deployment and SSO.
  - Vantage and CloudZero.
  - ModelOp funding.
  - watsonx.governance pricing (US$0.64 per evaluation).
  - ValidMind's SR 26-2 mapping.
  - HiddenLayer ISO 27001 and SOC 2.
  - LaunchDarkly pricing and the 12 May 2026 rename date.
  - Prisma AIRS regions and FedRAMP.
  - Check Point AI Agent Security early-access date (10 April 2026).
  - Lakera's "c. US$300m" figure.
- **A8.**
  - GPAI Code of Practice signatories and the 17 July 2026 taskforce.
  - R-US-AGENCY-AI: the Fed statement of 26 March 2026, the OCC Spring 2026 Risk Perspective, and the RFI still unpublished.
  - Details of PRA SS1/23 and the roundtables.
  - DORA register-of-information dates.
  - R-US-TPRM (remains Not publicly verified).
  - R-UK-AI-STATEMENTS: the FCA AI Live Testing cohort, the FPC and the BoE/FCA survey.
  - ESMA's 2024 statement and briefings.

## 6. Residual risks

- **Most regulator and vendor facts are still read through search-tool extracts.** The only exceptions are Anthropic, PyPI, Go proxy and GitHub-raw sources, which were fetched directly. Under the style guide, confidence stays capped at medium unless a second source agrees.
- **Political naming changes are under way in the US.** The 29 September 2026 executive order replaces "AI" with "super intelligence" in federal communications, and NIST pages and SpaceXAI are already affected. Instrument and agency names may change after this review date, so cite documents by their published titles.
- **Several high-impact items are days old.** These are Mistral Large 4 (6 October), the SpaceXSI announcement (4 October), Collibra/trail ML (5 October) and Claude Haiku 5.5 (7 October). They may move before publication.
