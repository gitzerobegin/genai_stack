# Stage A, stream A5: L1 foundation-model vendors (model families)

As of 7 October 2026. Researcher disclosure: this stream was researched by an Anthropic model. Anthropic records were held to the same sourcing rules, and its controversies are recorded alongside its lineup.

**Update (gap-filling pass, sources A5-S048 to A5-S087).** A second pass with a fresh search budget covered the gaps listed in (e) of the first pass:

- the regulatory position of Chinese-origin models
- vendor-domain searches for xAI, DeepSeek, Qwen, Kimi, GLM, Mistral and Meta
- the date of GPT-6 Astra
- court sources for the Anthropic controversies

Vendor and regulator hosts are still egress-blocked, so these new sources are search-tool extracts of the primary pages. Unless a second source agrees, confidence is capped at medium. The text below has been updated in place; the first-pass constraint note is kept for the record.

**First-pass research constraint (historical).** The shared WebSearch budget for this turn (200 calls, shared across all agents) ran out after 21 searches by this stream. At that point the research had covered OpenAI, Anthropic and Google (Gemini, Gemma), and none of the other vendors.

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
| Grok (no version) | **Grok 4.7** was launched on 21 September 2026 at US$2/US$6 per 1M with a 500K context. xAI merged into SpaceX (2 February 2026) and was rebranded **SpaceXAI** (July 2026) (Reported). | Not publicly verified (graphic gives no version); vendor Acquired | A5-S079, A5-S081, A5-S027 |
| DeepSeek "V4" | V4 preview 24 April 2026: V4-Pro 1.6T/49B active, V4-Flash 284B/13B, 1M context, MIT licence. V4-Pro GA 13 August. **V4.1-Flash** (10 September 2026) replaced V4-Flash in the API. V4.1-Pro has not been released. | Version label wrong (stale at point-release level) | A5-S063, A5-S064, A5-S065 |
| Qwen "3.8" | **Qwen3.8** is current. API: qwen3.8-max (0902 snapshot), qwen3.8-flash, omni-flash. Open weights: Qwen3.8-27B, Qwen3.8-2.4T-A95B, Qwen3.8-Flash-Next (26 August 2026). Verified from Alibaba Cloud pages: the 2.4T flagship weights launched August 2026; Qwen3.8-27B is Apache 2.0. | No change | A5-S066, A5-S068, A5-S038 |
| Kimi "K3" | **Kimi K3** launched 16 July 2026, with weights released by 27 July. It is a 2.8T MoE with a 1M context, under the custom Kimi K3 License. Pricing is US$3/US$15 per 1M. Available on Bedrock. | No change | A5-S038, A5-S039, A5-S040, A5-S041 |
| "QI4" (Z logo) "Q4" | No model named QI4 or Q4 was found. The Z logo matches **Z.ai GLM**. The current family is GLM-5.x: GLM-5.3 and GLM-5.3-Flash (August 2026) and GLM-5.2 (open weights, June 2026, about 744–754B, 1M context). | Version label wrong | A5-S038, A5-S041, A5-S042, A5-S043, A5-S044 |
| Mistral "Medium 3.1" | Superseded by **Mistral Medium 3.5** (28 April 2026; 128B; Modified MIT). **Mistral Large 4** entered public preview on 6 October 2026, with weights promised by the end of October. Large 3 (December 2025) is Apache 2.0. | Superseded | A5-S074, A5-S076, A5-S038 |
| Gemma "2.9" | No Gemma 2.9 exists. The current family is **Gemma 4**: E2B, E4B, 26B MoE and 31B released 31 March / 2 April 2026, and 12B on 3 June 2026. Licence is **Apache 2.0**. | Version label wrong | A5-S034, A5-S035 |
| Meta "Llama (new: Muse)" | **Muse** comes from Meta Superintelligence Labs. Muse Spark was announced in April 2026. Versions 1.1 (9 July), 1.2 (5 August) and 1.3 (2 September) are served through the Meta Model API, now GA. **Muse Glimmer 30B** (August 2026) is Apache 2.0. Llama 4 remains the latest Llama, under the Llama 4 Community License. | Renamed | A5-S077, A5-S078, A5-S027 |

## (b) Ambiguities owned by this stream

**A1: "QI4" with Z logo, descriptor "Q4".**

- Resolved as the Z.ai GLM family; the label itself could not be verified.
- No source mentions a QI4 or Q4 model.
- The Z.ai SDK is published under the author "Z.ai" [A5-S047], and its Hugging Face organisation is `zai-org` (GLM-5.2, GLM-Image) [A5-S041].
- Current models are GLM-5.3, GLM-5.3-Flash and GLM-5.2 [A5-S038, A5-S042].
- The label is most likely garbled.

**A5: "Meta – Llama (new: Muse)".**

- Gap-pass update: verified from Meta's own pages. Muse Spark was announced in April 2026; the Meta Model API preview opened on 9 July 2026; Spark 1.3 shipped on 2 September; Muse Glimmer 30B is Apache 2.0 [A5-S077, A5-S078].
- First pass: resolved at Reported level only; Muse exists.
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
- Astra date, resolved in the gap pass:
  - 3 September 2026 is the launch date: the ChatGPT release notes headline "Introducing GPT-6 Astra", with access first for a limited set of organisations [A5-S083].
  - 4 September is API and Pro/Enterprise availability (OpenAI forum post).
  - 8 September is the AWS Bedrock GA date.
  - 10 September is only the date of the research-index entry.
- Status conflict for Astra: OpenAI says Astra is "not yet generally available", while AWS says it is GA on Bedrock.
- There is no "GPT-6 Terra".

**A11: version labels.**

| Label | Finding | Sources |
|---|---|---|
| Qwen 3.8 | Correct (Reported) | A5-S038, A5-S040, A5-S041 |
| Kimi K3 | Correct (Reported) | A5-S038–S041 |
| DeepSeek V4 | Correct at generation level. V4.1-Flash (10 September 2026) is verified from DeepSeek [A5-S064]; there is no V4.1-Pro. | A5-S064 |
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

**Sovereignty facts from the first pass.** For the regulatory position, see (c2) below.

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
- The D.C. Circuit upheld the second designation 2–1 under FASCSA on 25 September 2026 (No. 26-1049; Katsas and Rao, Henderson dissenting). The ruling is stayed while a rehearing petition can be filed. The California ruling (on the other designation) stands. Now sourced to the court opinion via a search extract [A5-S084], with CNBC [A5-S025].
- Bartz v. Anthropic: the US$1.5bn settlement received final approval on 20 July 2026. Sources: the settlement administrator and the Washington Post [A5-S085], plus SEC filings [A5-S026]. Judge Alsup had earlier held that training itself was fair use, but that building a library from pirated books was not.

## (c2) Chinese-origin models: sovereignty and regulatory position (gap pass; facts only)

**Italy.**

- On 30 January 2025 the Garante imposed an urgent limitation on DeepSeek's processing of Italian users' data [A5-S048].
- Findings: breaches of GDPR Arts 6 and 31, Chapter III and Art. 32. Data is stored in the PRC, and the companies claimed EU law did not apply.
- No record was found of the limitation being lifted or of a fine.

**Korea.**

- PIPC: DeepSeek app downloads were suspended from 15 February 2025 [A5-S053].
- On 24 April 2025 the PIPC found that prompts and device data had been sent without consent to four overseas firms (three in China, one in the US).

**Germany and the EU.**

- Berlin DPA: on 27 June 2025 it reported the DeepSeek app to Apple and Google as illegal content under DSA Art. 16, citing unlawful transfers to China [A5-S058].
- France, the Netherlands, Luxembourg and Portugal are also reviewing DeepSeek [A5-S058].

**Australia.**

- PSPF Direction 001-2025 (4 February 2025) is mandatory for non-corporate Commonwealth entities [A5-S054].
- It requires removing DeepSeek from government systems and devices. It does not cover private firms.

**Taiwan.**

- Government agencies are barred from DeepSeek (February 2025) [A5-S059].
- In November 2025 the National Security Bureau assessed five PRC models (DeepSeek, Tongyi/Qwen, Doubao, Yiyan, Yuanbao) and found security and bias failings in all five.
- A report that all PRC AI is banned in government agencies is unconfirmed.

**US federal.**

- FY2026 NDAA s.1532 bans DoD use or acquisition of DeepSeek/High Flyer AI, with waivers available. Whether it covers contractors is not confirmed [A5-S057].
- s.6604 requires removing DeepSeek from intelligence-community systems [A5-S057].
- The No DeepSeek on Government Devices Act is still in committee [A5-S055].
- Several Commerce bureaus bar DeepSeek on their devices [A5-S056].
- No ban on private-sector use exists as of October 2026. There are House investigations, a reported revival of executive-action plans (Axios, 20 July 2026), and a pending "No Adversarial AI Act" [A5-S060].

**US states.**

- Texas (31 January 2025), New York (10 February), Virginia and Iowa ban DeepSeek on state devices [A5-S056].

**UK.**

- No government-wide ban [A5-S061].
- A Lords written answer (HL4479) says DeepSeek inputs "will be sent to China and thus [are] subject to Chinese law" [A5-S061].
- DWP bars DeepSeek on its devices [A5-S061].

**US Commerce/NIST CAISI evaluations.**

| Model | Finding | Source |
|---|---|---|
| DeepSeek R1/V3.1 (30 September 2025) | Lags US models; much more susceptible to agent hijacking and jailbreaks; censorship risk | A5-S049 |
| DeepSeek V4 Pro (1 May 2026) | About 8 months behind the frontier; more cost-efficient than models of similar capability | A5-S050 |
| Kimi K2 Thinking | Heavily censored in Chinese | A5-S051 |
| Kimi K3 (with UK AISI, July 2026) | Below frontier cyber capability; safeguards did not stop attempted exploit development | A5-S051 |
| GLM-5.2 (July 2026) | Around GPT-5.2 level; assists agentic exploit development | A5-S052 |
| GLM-5.3 (September 2026) | Most cyber-capable open-weight model; about 4 months behind the frontier | A5-S052 |
| Qwen | No CAISI evaluation found | A5-S051 |

**Export controls.**

- Zhipu AI (Z.ai) has been on the US Entity List since 16 January 2025 (90 FR 4619), with a presumption of denial for EAR items [A5-S072].

**Where each vendor's own API holds data.**

| Vendor | Where the hosted API holds data | Sources |
|---|---|---|
| DeepSeek | Stores data in the PRC; terms are under PRC law; API training position not stated | A5-S062 |
| Alibaba Model Studio | Region-bound: Frankfurt EU scope, Singapore International, US Virginia, Beijing mainland. Says it never trains on customer data. | A5-S067 |
| Moonshot | International API stores data in Singapore; mainland platform in the PRC. An API page says no training; the privacy policy conflicts. | A5-S070 |
| Z.ai | Data generally processed in Singapore (Singapore operating entity). The current DPA says API content is not stored. | A5-S073 |

**Hosting outside the vendor (non-China options).**

- **Microsoft Foundry:** sells DeepSeek V4-Pro and V4-Flash directly, processed in the customer's geography, DataZone or Global [A5-S087]. Kimi K3 and GLM-5.x on Foundry run through Fireworks, with inference outside the customer's Azure tenant [A5-S087].
- **AWS Bedrock:** Kimi K3 via cross-Region profiles only; GLM 5.3 (from 5 October 2026, cross-Region only); GLM 5 in-Region in places including London; DeepSeek V3.2/V3.1/R1 but not V4; Qwen3 in EU and UK regions, but not Qwen3.8 [A5-S086].
- **Google Cloud:** DeepSeek V3.x/R1, Kimi K2-Thinking, Qwen3, GLM-4.7/5/5.2 [A5-S027].
- **Self-hosting:** open weights are available under MIT (DeepSeek V4), Apache 2.0 (Qwen3.8-27B), the Kimi K3 License, and MIT or MIT-with-MaaS-condition (GLM-5.3-Flash and GLM-5.3) [A5-S063, A5-S066, A5-S069, A5-S071].

## (d) Products the graphic misses (not added to products.json)

- **MiniMax (M2, M3, H3):** a Chinese-origin open-weight vendor. M2 is on Google Cloud; M3 had day-0 KTransformers support on 21 June 2026. Anthropic names MiniMax among the alleged distillers. [A5-S027, A5-S042, A5-S046]
- **NVIDIA Nemotron 3 (Nano, Super, Ultra):** open models with SGLang day-0 support (Ultra June 2026). Relevant to sovereign or self-hosted stacks. [A5-S039]
- **Amazon Nova and Microsoft first-party models:** not researched (search budget exhausted).

## (e) Gaps after the gap pass

What remains unverified after the gap pass:

- The Garante's final decision or any fine, and current status of the Korea and Berlin cases.
- Whether NDAA s.1532 covers contractors.
- The licence of Qwen3.8-2.4T-A95B.
- Certifications (SOC 2/ISO) for DeepSeek, Alibaba Model Studio, Moonshot, Z.ai and the Meta Model API.
- Meta Model API data terms.
- The status of DeepSeek V4-Pro after 14 September 2026 (DeepSeek's own pages conflict).
- The Mistral Large 4 licence and price.
- Whether the SpaceXSI rename happened.
- The exact launch dates of GLM-5.3 and Qwen3.8-Max.
- The texts of the D.C. Circuit opinion and the Bartz order. Both were read only through search extracts, because the court sites are blocked.

## (e-first-pass) Gaps recorded in the first pass (largely superseded)

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
