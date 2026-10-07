# Stage A, stream A5: L1 foundation-model vendors (model families)

As of 7 October 2026. Researcher disclosure: this stream was researched by an Anthropic model. Anthropic records were held to the same sourcing rules, and its controversies are recorded alongside its lineup.

**Research constraint (read first).** The shared WebSearch budget for this turn (200 calls, shared across all agents) ran out after 21 searches by this stream. At that point the research had covered OpenAI, Anthropic and Google (Gemini, Gemma), and none of the other vendors.

- All other vendor hosts and all regulator hosts are egress-blocked: x.ai, deepseek.com, mistral.ai, alibabacloud.com, qwen.ai, moonshot.ai, z.ai, llama.com, ai.meta.com, huggingface.co, AWS and Microsoft docs, garanteprivacy.it, gov.uk, nist.gov and others.
- The xAI, DeepSeek, Qwen, Kimi, GLM, Mistral and Meta records therefore rest on four kinds of source:
  - Google Cloud's directly fetched generative AI pricing page (primary, for Google-hosted availability) [A5-S027]
  - the LiteLLM 1.104.1 price/context map from PyPI (aggregator) [A5-S038]
  - dated release notes in open-source serving and fine-tuning project READMEs on PyPI (independent technical) [A5-S039–A5-S044]
  - vendor SDK metadata on PyPI [A5-S047]
- **No vendor primary page was read for these seven vendors.** Their records are labelled `Reported`, mostly at `conf: low/medium`.
- The sovereignty and regulatory research for Chinese-origin models (bans, regulator statements, CAISI) could not be done. See (e).

## (a) What changed since the original diagram

| Original label | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| OpenAI "GPT-6" | GPT-6 is a tiered family: **GPT-6 Astra** (gated flagship, early September 2026), **GPT-6 Sol** and **GPT-6 Luna** (22 September), **GPT-6.1 Sol** (29 September). GPT-5.6 Sol/Terra/Luna (9 July 2026) is still offered. Open weights: gpt-oss-120b/20b (Apache 2.0). | No change (label correct; incomplete as a single label) | A5-S001, A5-S002, A5-S003, A5-S004, A5-S005, A5-S008, A5-S009 |
| Claude "Opus 5.5" | Opus 5.5 is current (22 September 2026) but is not the top tier. **Claude Fable 5.1** (1 September 2026) is the top GA model. **Mythos 5.1** is the same model with looser safeguards (trusted access only). Sonnet 5.5 (28 September) and Haiku 5.5 (7 October) complete the 5.5 family. | No change (label correct; not the flagship) | A5-S010, A5-S012, A5-S016, A5-S019, A5-S020 |
| Gemini "Gemini" | Production lineup is **Gemini 3.x**: 3.1 Pro (still preview), 3.8 Flash (GA 2 September 2026) and 3.5 Flash-Lite. **Gemini 4 Argon** was announced 30 September 2026 with restricted access. Gemini 3.5 Pro was never released (reported cancelled). | Not publicly verified (graphic gives no version) | A5-S027, A5-S030, A5-S031, A5-S032, A5-S036 |
| Grok (no version) | Newest model in the xAI API list and on Google Cloud is **Grok 4.7**. Also offered: 4.6, 4.5, 4.3, 4.20, 4.1 Fast and grok-code-fast-1. Release dates were not verified. | Not publicly verified (graphic gives no version; lineup Reported only) | A5-S027, A5-S038 |
| DeepSeek "V4" | Family is **DeepSeek-V4** (V4-Pro about 1.6T; V4-Flash about 284B; 1M context), released around April 2026 as open weights. The snapshots dated 0731 and 0813 come from the model IDs. **V4.1-Flash** is listed by Microsoft Foundry, Together and OpenRouter (aggregator only). | No change (generation correct; point release V4.1 Reported) | A5-S038, A5-S039, A5-S042, A5-S044 |
| Qwen "3.8" | **Qwen3.8** is current. API: qwen3.8-max (0902 snapshot), qwen3.8-flash, omni-flash. Open weights: Qwen3.8-27B, Qwen3.8-2.4T-A95B, Qwen3.8-Flash-Next (26 August 2026). No Alibaba primary source was read. | No change (Reported) | A5-S038, A5-S040, A5-S041 |
| Kimi "K3" | **Kimi K3** is current: open weights released July 2026 (ms-swift 22 July; SGLang day-0 27 July), 1M context, US$3/US$15 per 1M on Moonshot's API, and available on Bedrock. | No change (Reported) | A5-S038, A5-S039, A5-S040, A5-S041 |
| "QI4" (Z logo) "Q4" | No model named QI4 or Q4 was found. The Z logo matches **Z.ai GLM**. The current family is GLM-5.x: GLM-5.3 and GLM-5.3-Flash (August 2026) and GLM-5.2 (open weights, June 2026, about 744–754B, 1M context). | Version label wrong | A5-S038, A5-S041, A5-S042, A5-S043, A5-S044 |
| Mistral "Medium 3.1" | Medium 3.1 existed but was superseded by **Mistral Medium 3.5** (model card 26.04, April 2026). Other current models: Large 3 (25.12), Small 4.0 (26.03), Ministral 3, Magistral, Devstral 2, OCR 4.1. | Superseded | A5-S038, A5-S027 |
| Gemma "2.9" | No Gemma 2.9 exists. The current family is **Gemma 4**: E2B, E4B, 26B MoE and 31B released 31 March / 2 April 2026, and 12B on 3 June 2026. Licence is **Apache 2.0**. | Version label wrong | A5-S034, A5-S035 |
| Meta "Llama (new: Muse)" | **Muse** is a real Meta family. Muse Spark 1.1–1.3 is offered through Meta's API (1M context) and Microsoft Foundry. Muse Glimmer 30B is open weights (support dated 11 August 2026). **Llama 4** Scout and Maverick remain the latest Llama; no Llama 5 was found. | Renamed (Reported: frontier brand moved from Llama to Muse) | A5-S038, A5-S040, A5-S027, A5-S047 |

## (b) Ambiguities owned by this stream

**A1: "QI4" with Z logo, descriptor "Q4".**

- Resolved as the Z.ai GLM family; the label itself could not be verified.
- No source mentions a QI4 or Q4 model.
- The Z.ai SDK is published under the author "Z.ai" [A5-S047], and its Hugging Face organisation is `zai-org` (GLM-5.2, GLM-Image) [A5-S041].
- Current models are GLM-5.3, GLM-5.3-Flash and GLM-5.2 [A5-S038, A5-S042].
- The label is most likely garbled.

**A5: "Meta – Llama (new: Muse)".**

- Resolved at Reported level: Muse exists.
- The LiteLLM map lists `meta/muse-spark-1.1/1.2/1.3`, citing ai.developer.meta.com pricing: 1,048,576 context, US$1.25/US$4.25 per 1M, plus a "contributor" variant at US$0.10/US$0.20. Microsoft Foundry lists `muse-spark-1.3` [A5-S038].
- ms-swift added support for "Muse-Glimmer-30B" (`modelscope.cn/models/meta-models/...`) on 11 August 2026 [A5-S040].
- Llama 4 Scout and Maverick are still sold on Google Cloud [A5-S027].
- No Meta announcement was readable. Dates, licences and the meaning of "contributor" pricing are unverified.

**A6: "Gemini – Gemini" (no version).**

- Resolved: the current lineup is Gemini 3.1 Pro (preview), 3.8 Flash (GA 2 September 2026), 3.5 Flash-Lite (21 July 2026) and the 3.8 Live/TTS models [A5-S030, A5-S027, A5-S032].
- The frontier model Gemini 4 Argon (30 September 2026) is restricted to trusted cyber defenders [A5-S031].
- The brief's "Gemini 3.x" is verified.

**A9: "Gemma 2.9".**

- Resolved: the label is wrong. Gemma 4 is current (31 March / 2 April 2026; 12B on 3 June 2026), under Apache 2.0 [A5-S034, A5-S035].
- Gemma 3 is still deployable on Google Cloud and Bedrock [A5-S027, A5-S038].
- The brief's "Gemma 4" is verified.

**A10: "OpenAI GPT-6".**

- Resolved: verified. GPT-6 Astra, Sol and Luna exist, and so does GPT-6.1 Sol [A5-S002, A5-S004].
- Independent corroboration: AWS Bedrock GA notices and model cards [A5-S008], Microsoft Foundry [A5-S009], CNBC and Axios (3 September 2026) [A5-S003].
- **Honest conflict with the caller's early signal.** The caller suggested "GPT-6 Astra" might rest on thin sources. A search restricted to openai.com returned OpenAI's own pages (gpt-6-astra, introducing-gpt-6-sol-and-luna, introducing-gpt-6-1-sol, pricing, Deployment Safety Hub system card). I therefore treat Astra as verified.
- openai.com itself is egress-blocked, so the wording rests on search extracts plus the AWS and Microsoft pages.
- GPT-5.6 Sol/Terra/Luna (9 July 2026) is also verified [A5-S001].
- Date conflicts for Astra: 3 September (release notes, CNBC), 8 September (Bedrock model card) and 10 September (research index).
- Status conflict for Astra: OpenAI says Astra is "not yet generally available", while AWS says it is GA on Bedrock.
- There is no "GPT-6 Terra".

**A11: version labels.**

| Label | Finding | Sources |
|---|---|---|
| Qwen 3.8 | Correct (Reported) | A5-S038, A5-S040, A5-S041 |
| Kimi K3 | Correct (Reported) | A5-S038–S041 |
| DeepSeek V4 | Correct at generation level; "DeepSeek V4.1" exists only as V4.1-Flash in aggregator listings | A5-S038 |
| Mistral Medium 3.1 | Stale; Medium 3.5 is current | A5-S038 |
| Claude Opus 5.5 | Correct, but Fable 5.1 is the top GA tier | A5-S010, A5-S019 |

## (c) Evidence for hypotheses

No hypothesis (H1–H8) is assigned to stream ⑤. Evidence for the plan §5 L1 research questions follows, as facts only.

**Frontier vs open weight.**

- OpenAI, Anthropic and Google Gemini frontier tiers are API-only [A5-S003, A5-S010, A5-S032].
- OpenAI's open weights are gpt-oss (August 2025, Apache 2.0) [A5-S005].
- Google's open-weight line is Gemma 4 (Apache 2.0) [A5-S034].
- DeepSeek V4, Kimi K3, GLM-5.2 and part of Qwen3.8 are published as open weights on Hugging Face or ModelScope [A5-S041, A5-S040].
- Meta now pairs an API flagship (Muse Spark) with a smaller open model (Muse Glimmer 30B) [A5-S038, A5-S040].

**Gated capability tiers.**

- OpenAI Astra: rated "Critical" for cyber, gated, and off by default for enterprise workspaces [A5-S002, A5-S003].
- Anthropic: Mythos 5.1 is trusted-access only; Fable 5.1 carries extra safeguards [A5-S016].
- Google: Gemini 4 Argon first went to cyber defenders through the Fairwind programme [A5-S031].

**Model economics (per 1M input/output tokens, 7 October 2026).**

| Tier | Model and price | Sources |
|---|---|---|
| Flagship | GPT-6 Astra US$10/US$50 | A5-S004 |
| Flagship | Claude Fable 5.1 US$10/US$50 | A5-S011 |
| Flagship | Claude Opus 5.5 US$4/US$20 | A5-S011 |
| Flagship | Gemini 3.1 Pro US$2/US$12 | A5-S032 |
| Mid | GPT-6.1 Sol US$2/US$10 | A5-S004 |
| Mid | Sonnet 5.5 US$2/US$10 | A5-S011 |
| Mid | Gemini 3.8 Flash US$0.75/US$3.75 (introductory) | A5-S027 |
| Small | GPT-6 Luna US$0.10/US$0.50 | A5-S004 |
| Small | Haiku 5.5 US$0.10/US$0.50 | A5-S011 |
| Small | Gemini 3.5 Flash-Lite US$0.30/US$2.50 | A5-S027 |
| Chinese open-weight, own APIs | DeepSeek V4-Pro US$1.32/US$3.96 | A5-S038 (aggregator) |
| Chinese open-weight, own APIs | GLM-5.3 US$1.40/US$4.40 | A5-S038 (aggregator) |
| Chinese open-weight, own APIs | Kimi K3 US$3/US$15 | A5-S038 (aggregator) |
| Chinese open-weight, own APIs | Qwen3.8-max US$2/US$6 | A5-S038 (aggregator) |

**Portability across hyperscalers.**

- Claude: Bedrock, Google Cloud and Microsoft Foundry [A5-S010].
- OpenAI GPT-6: Bedrock and Foundry, not Google Cloud. Only gpt-oss is on Google Cloud [A5-S008, A5-S009, A5-S027].
- Gemini: Google Cloud only (no other-cloud listing found).
- Grok: all three clouds [A5-S027, A5-S038].

**Residency.**

- OpenAI EU: storage and processing in region, with MAM or ZDR approval. OpenAI UK: storage only [A5-S006].
- Anthropic first-party inference geography is "global" or "us" only, and workspace (storage) geography is "us" only. EU processing is available via Google Cloud EU multi-region and Bedrock regional endpoints [A5-S013, A5-S011, A5-S027].
- Google: generative AI data-at-rest residency in the UK and several EU countries (2023 commitment) [A5-S029].

**Sovereignty facts available (the regulatory side is not covered).**

- Anthropic bars sales to entities controlled from China (4 September 2025) [A5-S045].
- Anthropic alleges that DeepSeek, Moonshot and MiniMax distilled Claude through about 24,000 fraudulent accounts (23 February 2026) [A5-S046]. This is a competitor's allegation and a conflict of interest.

**Hosted vs self-hosted Chinese models.** These availability facts bear on the distinction between the vendor's own API and other ways of running the model:

- Microsoft Foundry hosts DeepSeek V4-Pro, V4-Flash and V4.1-Flash, plus Kimi K2.x and Fireworks-operated Kimi K3 and GLM-5.x [A5-S038].
- Bedrock hosts Kimi K3 (global/US), Kimi K2.5 (including eu-north-1), DeepSeek V3.2 (including the `eu.` profile), GLM-5 (US) and Qwen3 (including eu-west-2 London) [A5-S038].
- Google Cloud hosts DeepSeek V3.1/V3.2/R1, Kimi K2-Thinking, Qwen3 and GLM-4.7/5/5.2 [A5-S027].
- DeepSeek-V4-Flash has been run on a single Ascend NPU with CPU offload [A5-S042].

**Anthropic public-sector risk.**

- The US Department of Defense designated Anthropic a "supply chain risk".
- A California district court ruled the designation illegal (August 2026).
- The D.C. Circuit upheld it 2–1 on 25 September 2026 [A5-S025] (secondary source).

## (d) Products the graphic misses (not added to products.json)

- **MiniMax (M2, M3, H3):** a Chinese-origin open-weight vendor. M2 is on Google Cloud; M3 had day-0 KTransformers support on 21 June 2026. Anthropic names MiniMax among the alleged distillers. [A5-S027, A5-S042, A5-S046]
- **NVIDIA Nemotron 3 (Nano, Super, Ultra):** open models with SGLang day-0 support (Ultra June 2026). Relevant to sovereign or self-hosted stacks. [A5-S039]
- **Amazon Nova and Microsoft first-party models:** not researched (search budget exhausted).

## (e) Gaps: what could not be verified, and why

**1. Chinese-origin sovereignty and regulation: entirely unverified.** The shared search budget was exhausted, and the regulator sites (Garante, PIPC, gov.uk, NCSC, commerce.gov, nist.gov, congress.gov, EDPB) are all egress-blocked. Not verified:

- the Italy Garante action on DeepSeek
- Korea and Australia restrictions
- US federal and state device bans (e.g. Texas)
- proposed US federal legislation
- any US Commerce/NIST CAISI evaluation of DeepSeek
- the Entity List status of Zhipu
- vendor privacy policies and data location (servers in China) for the DeepSeek, Moonshot, Alibaba and Z.ai hosted APIs

A follow-up run with search budget is required before Stage B uses any of this.

**2. Vendor primary pages for seven vendors.** xAI, DeepSeek, Alibaba Qwen, Moonshot, Z.ai, Mistral and Meta: lineup dates, licences (MIT, Apache, Qwen licence, modified-MIT, Llama/Muse licences), certifications, retention/ZDR, EU residency and headquarters/jurisdiction are all unverified. Hugging Face model cards could not be read.

**3. xAI.** Release dates, trust centre, data terms, any corporate restructuring and any regulatory actions concerning Grok are unverified.

**4. Mistral.** EU-sovereignty positioning, headquarters, data terms, certifications and open-weight licences are unverified.

**5. Meta Muse.** Launch announcement, licence, whether Muse Spark weights are closed, and what the "contributor" price tier means (possibly data sharing) are all unverified.

**6. OpenAI.** No direct fetch was possible. Access controls (SSO/SCIM/RBAC), enterprise support SLAs and CMK were not researched.

**7. Anthropic.** Enterprise support tiers and SLA are not captured. Trust-centre scope comes from a search extract because trust.anthropic.com did not respond.

**8. Gemini.** Pricing for Gemini 4 Argon and its API availability date are not published.

**9. Archive notes.**

- A5-S039 to A5-S044 and A5-S047 are direct fetches from the PyPI JSON API, excerpted with `save_extract.py`. That tool's fixed header says "direct fetch blocked", which is inaccurate for these files.
- A5-S014 and A5-S015 were client-rendered pages with no captured body, and nothing relies on them.
- A5-S029 dates from 2023.
