# E2: Commercial and licensing facts for the vendor-side views

**Stream:** Stage E, E2 (commercial). **Researched:** 9–10 October 2026. **Sources:** `work/stageE/E2_commercial/sources.csv` (E2-S001 to E2-S055); archive in `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/E2/`.

**How to use this brief.**

- There is one bullet per fact, and each bullet ends with its claim tag.
- A `VF` tag with an E2 ID means a primary source. Where it was read through a search-tool extract (access status `extract` in `sources.csv`), confidence is capped at medium.
- An `R` tag means a secondary source.
- Existing dataset IDs (A5-, V2-, A8-) are cited where `05_Data` already holds the fact; this brief does not repeat those facts at length.
- "(volatile; re-verify quarterly)" marks credits, prices, tiers and programme terms.
- The groups are TS, SW, SU (the original three views), then AT, DV, AG (the vendor start-up views added on 9 October 2026). A fact is placed in the view where it most changes the advice, and other views point back to it.
- Facts on the agentic SDLC landscape and on agent identity and interoperability standards belong to E3 and are not here.

---

## TS: Technology service provider

### TS.1 Building a service on hosted model APIs (terms)

- Anthropic's Commercial Terms (effective 17 June 2025) expressly permit the customer to use the Services "to power products and services Customer makes available to its own customers and end users". [VF: E2-S004]
- Under those terms, the customer retains its Inputs and owns its Outputs, and Anthropic assigns to it any right it has in Outputs. [VF: E2-S004]
- Anthropic "may not train models on Customer Content from Services". [VF: E2-S004]
- The customer may not use the Services to build a competing product or service, "including to train competing AI models or resell the Services except as expressly approved by Anthropic". It may not reverse engineer or duplicate the Services. [VF: E2-S004]
- The customer must notify its own users that factual assertions in Outputs should not be relied on without independent checking. [VF: E2-S004]
- Anthropic defends the customer against third-party IP claims arising from paid, authorised use and its Outputs, with exclusions for modified Outputs and for combinations with other technology. The customer indemnifies Anthropic for claims about its Inputs and for Usage Policy breaches by the customer or its users. [VF: E2-S004]
- Anthropic may suspend access if it believes a customer *or any of its users* breaches the Usage Policy. A provider therefore carries its tenants' misuse risk. [VF: E2-S004] [AJ]
- Anthropic's Usage Policy applies expressly to "the end users of products or services integrating Claude". [VF: E2-S005]
- All consumer-facing chatbots or agents that talk directly to external users must disclose that the user is interacting with AI, at least at the start of each session or in the interface. The disclosure need not name Anthropic or the model. [VF: E2-S005]
- For high-risk use cases, a qualified human must review an AI recommendation before it is delivered as advice or used for a decision, and the affected individual must be told that AI was used. [VF: E2-S005]
- The Usage Policy page read on 10 October 2026 carries an effective date of 12 November 2026, so an updated policy has been published ahead of its start date. (volatile; re-verify quarterly) [VF: E2-S005]
- Anthropic's DPA gives reasonable prior notice of new subprocessors and a right to object on data-protection grounds. It includes EU SCC Modules Two and Three and a UK Addendum. [VF: E2-S012]
- OpenAI's Services Agreement: the customer retains Input and owns Output, and OpenAI uses Customer Content only to provide the Services, comply with law, enforce its policies and prevent abuse. [VF: E2-S026]
- The same agreement bars using Output to develop models that compete with OpenAI, subject to a narrow permitted exception, and prohibits buying, selling or transferring API keys. No general resale ban appeared in the text retrieved. [VF: E2-S026]
- Google Cloud Service Specific Terms (last modified 8 October 2026): Google will not use Customer Data to train or fine-tune any AI/ML model without the customer's permission or instruction. [VF: E2-S007]
- Under the same terms, Generated Output is Customer Data, and Google asserts no ownership of new IP in it. [VF: E2-S007]
- Google Cloud generative AI services may not be used in any service "directed towards or ... likely to be accessed by individuals under the age of 18". Clinical use is also barred. [VF: E2-S007]
- The Gemini API (AI Studio) Additional Terms contain the same under-18 ban and a ban on developing competing models. They now also state that the API is for professional or business purposes, not consumer use. [VF: E2-S030]
- Google Cloud bars using an AI/ML service or its output to develop a similar or competing product. The bar does not apply on Vertex AI (Gemini Enterprise Agent Platform) unless a Google pre-trained model is used. Output may not be used to create models similar to a Google model, except through Google's own fine-tuning or distillation features. [VF: E2-S007]
- Google indemnifies unmodified Generated Output from indemnified generative AI services that use Google pre-trained models. The indemnity does not apply if the customer disables Google's citation or safety tools. [VF: E2-S007]
- Mistral's help centre says API users own their inputs and outputs. [VF: E2-S029]
- A clause tracker records a competing-product restriction in Mistral's terms for *image* outputs only. A reported May 2026 change in Mistral's data licence concerns consumer plans. Neither point was confirmed on mistral.ai. [R: E2-S029]
- What each hosted API provider does with API data, its retention and its residency options are already in the dataset: OpenAI [VF: A5-S006, V2-S079], Anthropic [VF: A5-S018, V2-S075], Google [VF: A5-S033], Mistral [VF: A5-S075].
- Read together, the three US model vendors permit building and selling a service on their APIs. They forbid using it to build a competing model, and Anthropic also forbids reselling raw access. A provider's own customer contract must flow down the usage policy, the AI-disclosure duty and the under-18 bar. [AJ]

### TS.2 Cost levers for running GenAI at scale

**Batch**

- Anthropic: the Batch API costs 50% less on input and output, and the discount stacks with caching and data-residency multipliers. (volatile; re-verify quarterly) [VF: V2-S002, A5-S011]
- OpenAI: Batch is 50% off (for example, gpt-6-astra batch costs US$5 input and US$25 output per 1M). (volatile; re-verify quarterly) [VF: A5-S004]
- Gemini API: Batch is 50% off. (volatile; re-verify quarterly) [VF: A5-S032]
- Vertex: Flex/Batch is about 50% of standard (Gemini 3.1 Pro Preview costs US$1.00 input per 1M at 200K tokens or fewer). (volatile; re-verify quarterly) [VF: A5-S027]
- Amazon Bedrock: batch inference is 50% below on-demand for select models. (volatile; re-verify quarterly) [VF: E2-S032]
- Azure OpenAI Global Batch and Data Zone Batch cost 50% less than Global Standard, with a 24-hour target turnaround. Jobs are not expired if they run longer, and completed work is billed. [VF: E2-S018]

**Caching**

- Anthropic: a cache read costs 0.1x the base input price (0.05x on Opus 5.5 and Sonnet 5.5, 0.025x on Fable 5.1). A 5-minute cache write costs 1.25x and a 1-hour write 2x. (volatile; re-verify quarterly) [VF: V2-S002]
- OpenAI: cached input is about 90–95% below base input (gpt-6.1-sol US$0.10 vs US$2.00; gpt-6-luna US$0.01 vs US$0.10), and cache writes are now charged separately. (volatile; re-verify quarterly) [VF: A5-S004]
- Gemini API: the cache read for 3.1 Pro is US$0.20 per 1M (90% below input), plus US$4.50 per 1M tokens per hour of storage. (volatile; re-verify quarterly) [VF: A5-S032]
- Azure OpenAI: cache reads are discounted on Standard deployments and up to 100% discounted on Provisioned deployments. Caching is on by default and needs a prefix of at least 1,024 identical tokens. [VF: E2-S019]
- On Azure OpenAI GPT-5.6 and later, cache writes can be charged. Caches are not shared between Azure subscriptions. [VF: E2-S019]
- Bedrock: the "up to 90%" prompt-caching saving appears only in third-party sources in this run. [R: E2-S032]

**Priority, Flex and reserved capacity**

- OpenAI: Priority processing (renamed "Fast mode" on 30 July 2026) is pay-as-you-go at a premium per-token rate with a 99.9% uptime SLA. Flex processing is billed at Batch rates and may return 429 when capacity is short. (volatile; re-verify quarterly) [VF: E2-S031]
- OpenAI Reserved Tier (Enterprise, via sales; Scale Tier remains for models before GPT-5.6): capacity is bought per model in dollars per minute. It can be spent across Standard and Fast modes and regions, and excludes Batch and Flex. Overage is billed pay-as-you-go. [VF: E2-S033]
- Anthropic: Priority Tier capacity commitments "are no longer available for purchase". Existing commitments run to contract end, and guaranteed capacity is now a sales conversation. The remaining tiers are Standard and Batch. [VF: E2-S006]
- Amazon Bedrock has four per-request service tiers: Reserved, Priority (75% premium to Standard), Standard and Flex (50% discount). (volatile; re-verify quarterly) [VF: E2-S032]
- Bedrock Reserved is bought per tokens-per-minute for 1 or 3 months (minimum 100,000 input and 10,000 output TPM, through the account team). Provisioned Throughput is billed hourly per model unit. [VF: E2-S032]
- Azure Foundry offers Standard, Batch, Priority processing (pay per token at a priority rate, with a per-model latency target) and Provisioned throughput. Provisioned is billed per PTU per hour or through Azure reservations, with a minimum PTU count per model. [VF: E2-S017]
- PTU quota does not guarantee capacity. Provisioned comes as Global, Data Zone (US or EU) and Regional deployments. [VF: E2-S017]
- Optional "spillover" sends overflow from a provisioned deployment to a standard one. It is not supported for Azure DeepSeek or Meta Llama models. [VF: E2-S017]
- Vertex Provisioned Throughput is sold in GSUs. Per-GSU prices fall with commitment length (1 week US$7.14, 1 year about US$2.74 global, per hour as listed), with a 10% higher non-global price. (volatile; re-verify quarterly) [VF: A5-S027]
- Google is crediting 50% of Provisioned Throughput spend on Gemini 3.6–3.8 Flash from 13 August to 31 December 2026. (volatile; re-verify quarterly) [VF: A5-S027]
- Together AI sells PTUs, and Fireworks sells batch at 50% plus reserved capacity. [VF: A4-S131, A4-S135]

### TS.3 Multi-tenant isolation guidance

- The Azure Architecture Center (29 April 2026) treats models with the same sensitivity as their training data. It distinguishes tenant-specific, shared and tuned shared models, and says tenants must agree before their data trains a shared model. [VF: E2-S015]
- Azure's "Multitenancy and Azure OpenAI" sets out four isolation models: a dedicated instance per tenant; a shared instance with a dedicated deployment per tenant; a shared instance and deployment; and a tenant-provided resource. They are compared for data and performance isolation. [VF: E2-S016]
- The same guidance warns that a shared Azure OpenAI resource gives no security segmentation per model deployment. It says: do not share an instance when using fine-tuned models. [VF: E2-S016]
- PTUs can be assigned to specific customers. Responses API response IDs should be stored under tenant-scoped keys. Batch jobs should be separated by tenant, because jobs are managed at job level. [VF: E2-S016]
- Azure's tenancy-models guide contrasts automated single-tenant deployments (strongest isolation, no noisy neighbour, low cost efficiency) with fully multitenant and partitioned models. [VF: E2-S053]
- AWS ML Blog: multi-tenant RAG on Bedrock Knowledge Bases follows the silo, pool and bridge patterns from AWS's SaaS Tenant Isolation Strategies whitepaper. Silo allows a per-tenant data source and per-tenant KMS keys. [VF: E2-S050]
- AWS's multi-tenant agents post (May 2026) uses metadata tenant filters and namespaces in the pool model, with automatic tenant-filter injection and result sanitisation. [VF: E2-S050]
- No AWS Prescriptive Guidance document dedicated to multi-tenant generative AI was found in this run. [NPV]
- OWASP LLM08:2025 (Vector and Embedding Weaknesses) names cross-context leakage in multi-tenant vector stores. Its mitigation is a permission-aware vector database. [VF: E2-S051]
- OWASP's current list is the GenAI LLM Top 10 2026, published 4 August 2026 per the project repository. The dataset records a conflicting 2 September 2026 press date. [VF: E2-S022, V2-S056]
- No OWASP item dedicated to tenant isolation was found. [NPV]
- Gateway virtual keys per tenant give per-tenant budgets and spend reports (LiteLLM, Portkey, Kong). [VF: A7-S070, A6-S015]

### TS.4 Customer assurance a provider is asked for

- SOC 2 is still assessed against the AICPA's 2017 Trust Services Criteria with points of focus revised in October 2022. The criteria themselves did not change in 2022. [R: E2-S048]
- ISO/IEC 27001:2013 certificates expired or were withdrawn by 31 October 2025. Certification is now against ISO/IEC 27001:2022 only, so a 2013 certificate in a questionnaire answer is a red flag. [R: E2-S046]
- ISO/IEC 42001 status (42001:2023, 42005:2025, 42006:2025) is held in the dataset and not repeated here. [VF: A8-S045, A8-S046, A8-S047, V2-S057]
- CSA published the AI Controls Matrix (AICM v1.0) with a control-by-control mapping to ISO/IEC 42001 on 20 August 2025. AICM v1.1 followed in July 2026. [VF: E2-S047]
- CSA launched STAR for AI on 23 October 2025. Level 1 is a published AI-CAIQ self-assessment. Level 2 is ISO/IEC 42001 certification plus a "Valid-AI-ted" scored AI-CAIQ. [VF: E2-S047]
- The AI-CAIQ (the AI questionnaire built on AICM) is the standard "AI questionnaire" format a buyer can send or point to. [VF: E2-S047] [AJ]
- Model vendors' own assurance (SOC 2, ISO 27001/42001, CSA STAR level) is in the dataset: Anthropic STAR Level 2 [VF: A5-S021]; OpenAI STAR Level 1 and the 42001 scope caveat [VF: A5-S007, V2-S062]; Google Cloud 42001 [VF: A5-S028]; Mistral SOC 2 and ISO 27001 [VF: A5-S075].

---

## SW: Software product company

### SW.1 Redistribution and embedding terms for open-weight models

**Llama 4 (Llama 4 Community License, effective 5 April 2025)**

- Anyone distributing Llama Materials, or a product that contains them, must:
  - ship a copy of the licence;
  - display "Built with Llama" prominently;
  - keep a Notice file reading "Llama 4 is licensed under the Llama 4 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved."; and
  - start the name of any distributed model trained or fine-tuned from Llama with "Llama".

  [VF: E2-S001]
- Licensees whose products had more than 700 million monthly active users in the month before the Llama 4 release date must request a licence from Meta, which Meta grants at its discretion. [VF: E2-S001]
- Use must follow the Llama 4 Acceptable Use Policy, which the licence incorporates by reference. Section 2 does not apply to recipients of an integrated end-user product. [VF: E2-S001]
- The licence carries California governing law and courts, and the licensee indemnifies Meta. [VF: E2-S001]
- The Acceptable Use Policy grants **no rights to the multimodal Llama 4 models** to individuals domiciled in, or companies with a principal place of business in, the EU. End users of a product that incorporates them are excepted. [VF: E2-S002]
- Llama 4 Scout and Maverick are multimodal, so an EU-headquartered software vendor cannot ship them itself. [AJ]
- The AUP also bars unlicensed professional practice (financial, legal, medical) and failing to disclose known dangers of an AI system to end users. [VF: E2-S002]

**Muse**

- Muse Glimmer 30B is reported as Apache 2.0 and ungated, with no monthly-active-user cap (released 10 August 2026). [R: E2-S028, A5-S078]
- Muse Spark is API-only. Its API data terms are not verified. [VF: A5-S077] [NPV]

**Gemma**

- Gemma 4 is Apache 2.0. [VF: A5-S034, V2-S020]
- Gemma 4 drops the custom Gemma Terms of Use and its usage-policy condition. [R: E2-S055]
- Earlier Gemma generations still under the Gemma Terms of Use require, on distribution outside a hosted service:
  - a Notice file pointing to the terms;
  - the Section 3.2 use restrictions passed on as enforceable terms;
  - a copy of the agreement for recipients; and
  - compliance with the Gemma Prohibited Use Policy.

  [VF: E2-S023]

**Qwen**

- Qwen3.8-27B is Apache 2.0. [VF: A5-S066]
- The Qwen3.8-2.4T flagship weights carry a custom Qwen3.8-Max License. "Model as a service" or "AI work assistant" businesses with more than US$50m revenue over 12 months need a separate licence. [R: E2-S025, V2-S014]
- Internal use is exempt only if neither the model nor its outputs or capabilities reach third parties. Very large products (100m MAU or US$20m monthly revenue) must display the model name. [R: E2-S025]

**Mistral**

- Mistral Large 3 and Ministral 3 are Apache 2.0. Medium 3.5 is "Modified MIT" with revenue-based exceptions. The Large 4 licence is not yet published. [VF: A5-S074, A5-S076, V2-S018]
- The Medium 3.5 Modified MIT threshold is reported as about US$20m global consolidated *monthly* revenue, above which a commercial licence or the API is needed. Secondary sources conflict, and the licence file was not read. [R: E2-S027]
- Mistral's weights page groups older models under Apache 2.0, the Mistral Research License (commercial use needs a separate licence) and the Non-Production License (Codestral: testing, research and evaluation only). Mistral says it is moving away from MRL for general-purpose models. [VF: E2-S054]

**gpt-oss**

- gpt-oss is distributed under Apache 2.0 [VF: E2-S003]. Broad use, modification and commercial redistribution are allowed "subject to our gpt-oss usage policy" [VF: E2-S024, A5-S005].
- The gpt-oss-120b repository carries a short USAGE_POLICY file, whose text was not retrieved in this run. [VF: E2-S024] [NPV]

**DeepSeek**

- DeepSeek V4 open weights are MIT. [VF: A5-S063]
- Older DeepSeek-V3 weights use the DeepSeek License Agreement v1.0. It permits commercial use and SaaS hosting, but requires its Attachment A use restrictions to be included as enforceable terms in any downstream agreement, with notice to users. [VF: E2-S013, E2-S014]

**What a vendor must do (across the licences above)**

- Apache 2.0 and MIT models need the licence and notices shipped.
- Llama, older Gemma, older DeepSeek and the Qwen3.8-Max licence also require flowing usage restrictions into the vendor's EULA, attribution or naming duties, and threshold checks.
- An EU-domiciled vendor should exclude Llama 4 multimodal models altogether.

[AJ]

### SW.2 Hosted-model option for customers who bring their own account

- The Azure Architecture Center lists the "tenant-provided Azure OpenAI resource" as a pattern for customers with their own quota, content-filter policy, PTUs or fine-tuned models. [VF: E2-S016]
- Competing-model and resale restrictions on the hosted APIs (TS.1) apply to the vendor only when the vendor holds the API account. Where the customer brings its own account, the customer's terms govern. [AJ]

### SW.3 Selling through cloud marketplaces (programme and private-offer mechanics)

- AWS Marketplace private offers:
  - each offer is tied to named buyer accounts (up to 25 per offer);
  - an Organizations management account can extend terms to member accounts;
  - AMI and container licences can be shared through AWS License Manager;
  - a new private offer can amend an existing SaaS contract.

  [VF: E2-S034]
- Seller "request private offer" buttons for AMI, SaaS, container and CloudFormation listings require membership of APN Customer Engagements (ACE). [VF: E2-S034]
- Microsoft Marketplace: 100% of Azure-benefit-eligible purchases count toward the customer's Azure consumption commitment. Private offers carry negotiated, off-list pricing. [VF: E2-S036]
- Microsoft multiparty private offers cover SaaS, Azure VM and Azure Application offers and need a transactable public plan. Their geography is stated inconsistently (US only, or US, UK and Canada). [VF: E2-S036]
- Google Cloud Marketplace lists AI agents, SaaS, APIs, VM and GKE products, AI models and datasets. Qualifying purchases draw down Google Cloud commitments. [VF: E2-S020]
- Google private offers support monthly, quarterly, annual and custom instalments, upfront payment up to five years ahead with annual amortised drawdown, and contracts up to seven years (announced 16 October 2024). [VF: E2-S038]
- Google Cloud Marketplace private offers can also transact third-party foundation models deployable to Vertex AI, including Provisioned Throughput. [VF: E2-S038]
- Marketplace fee levels were not recorded, by design. Third-party reports of Google revenue-share rates were seen but are not cited.

---

## SU: Start-up

### SU.1 Start-up programmes (as stated on 9–10 October 2026)

**Google for Startups Cloud Program**

- Credits: US$2,000 for pre-funded start-ups; up to US$200,000 for Seed to Series A; up to US$350,000 for AI-first start-ups. (volatile; re-verify quarterly) [VF: E2-S009]
- How the AI tier is paid: 100% up to US$250,000 in year 1, then 20% up to a further US$100,000 in year 2, over two years. (volatile; re-verify quarterly) [VF: E2-S010]
- AI-tier eligibility:
  - using or planning to use Gemini as the foundation of the product;
  - Pre-Seed or Seed funding within the last five years, or Series A within the last 12 months;
  - founded within five years;
  - no more than US$5,000 in prior Google Cloud credits.

  [VF: E2-S010]
- Programme credits cover Google models such as Gemini and Gemma. **Third-party models are billed directly and are not covered.** [VF: E2-S010]

**AWS Activate**

- Founders tier: US$1,000, rising to up to US$5,000 for select start-ups; no affiliation needed; requires a paid-tier AWS account. (volatile; re-verify quarterly) [VF: E2-S042]
- Portfolio tier: up to US$200,000 through an Activate Provider (VC, accelerator or incubator). AWS's own pages are inconsistent (one says US$100,000). (volatile; re-verify quarterly) [VF: E2-S042]
- Portfolio eligibility: pre-Series B, last round within 12 months, founded within 10 years, working website. Further credits above US$200,000 are offered to AI start-ups. [VF: E2-S042]

**Microsoft for Startups**

- Up to US$150,000 in credits "across eligible Azure services". (volatile; re-verify quarterly) [VF: E2-S011]
- Tier mechanics (about US$5,000 self-serve; higher tiers through usage or an Investor Network referral) come from third-party guides only, and the official eligibility page was not reached. [R: E2-S043]

**Anthropic, Claude for Startups**

- Open to bootstrapped, pre-seed and venture-backed start-ups. [VF: E2-S008]
- Start-ups backed by a partner VC may receive up to US$100K in extra API credits through the VC. (volatile; re-verify quarterly) [VF: E2-S008]
- Members get higher rate limits and Applied AI office hours. The "Startup Stack" of third-party discounts is worth up to US$45,000. [VF: E2-S008]
- The page says the programme is "over capacity" on its free Claude Team and US$1,000 API-credit offers and is re-reviewing applications. (volatile; re-verify quarterly) [VF: E2-S008]
- Credits apply only to the first-party Claude API, not to Bedrock or Vertex. [VF: E2-S008]

**NVIDIA Inception**

- Free, with no fees or equity, open at any stage and with no cohorts. [VF: E2-S044]
- Benefits: Deep Learning Institute credits, preferred hardware and software pricing, cloud credits through partners, and investor connections. A Premier tier opens after Series A. [VF: E2-S044]

**OpenAI and Mistral**

- No official OpenAI start-up credits page was found. Third parties say credits flow through VC partners or perks marketplaces, with conflicting amounts. [R: E2-S045] [NPV]
- Mistral's start-up programme ("Mistralship", about €30,000) could not be confirmed on mistral.ai; a secondary source reports its page returned 404 in August 2026. [R: E2-S045] [NPV]

**Reading the programmes together**

- Hyperscaler credits mostly do not pay for third-party frontier models: Google says so explicitly, and Anthropic's credits do not work on Bedrock or Vertex.
- A start-up that plans to live on credits is therefore steered towards the credit-giver's own models.
- Keep the model behind a gateway so the choice stays reversible.

[AJ]

### SU.2 Terms that bite early

- The Gemini API terms and Google Cloud generative AI terms bar any service likely to be used by under-18s. This decides the matter for consumer or education start-ups on Google models. [VF: E2-S030, E2-S007]
- Anthropic's Usage Policy requires AI disclosure in consumer-facing chatbots and extra guidelines for products serving minors. [VF: E2-S005]
- Cost levers (batch at 50%, caching at 90% or more off cached input) are listed under TS.2. For a start-up they are the cheapest margin improvement available. (volatile; re-verify quarterly) [VF: V2-S002, A5-S004, A5-S032] [AJ]

### SU.3 First enterprise questionnaire

- Expect requests for SOC 2 (2017 TSC with 2022 points of focus), ISO/IEC 27001:2022 and, increasingly, a CSA AI-CAIQ or STAR for AI entry. Details are in TS.4. [R: E2-S048, E2-S046] [VF: E2-S047]

---

## AT: Start-up selling AI tools into the enterprise GenAI stack

### AT.1 Assurance buyers ask a tool vendor for

- SOC 2 Type II, ISO/IEC 27001:2022 and ISO/IEC 42001 are the baseline the dataset records for established tool vendors (examples: Kong, Arize AX, W&B Weave, LangSmith). [VF: A6-S109, A1-S124, A1-S137, A1-S036]
- STAR for AI Level 1 (an AI-CAIQ self-assessment) is a low-cost, public, AI-specific answer. Level 2 requires ISO/IEC 42001 certification. [VF: E2-S047]
- Tool vendors in the dataset sometimes say "HIPAA-ready" or "vendor-stated" ISO 27001 without a certificate, and verifiers downgraded those claims. [VF: A6-S109, A1-S124]

### AT.2 Deployment patterns buyers ask for

- The dataset records BYOC or customer-VPC editions as a common enterprise ask for tool vendors (examples: Fireworks hybrid BYOC, turbopuffer BYOC on AWS, GCP and Azure, Together dedicated and VPC). [VF: A4-S152, A2-S125, A4-S130]
- Private connectivity on AWS: the SaaS provider exposes an endpoint service behind a Network Load Balancer, and the customer creates an interface VPC endpoint. AWS recommends one endpoint per Availability Zone. [VF: E2-S052]
- PrivateLink-powered SaaS can be bought through AWS Marketplace. [VF: E2-S052]
- Private connectivity on Azure: a Private Link service sits behind a Standard Load Balancer and is shared with customers by alias. [VF: E2-S049]
- The provider accepts or rejects each private-endpoint connection and can restrict visibility or auto-approve specific subscriptions (docs dated 10 August 2026). [VF: E2-S049]
- Automated single-tenant ("deployment stamp") editions give the strongest isolation at the lowest cost efficiency. That is the trade-off a tool start-up makes when a regulated buyer asks for a dedicated instance. [VF: E2-S053] [AJ]

### AT.3 Marketplace route

- AWS, Microsoft and Google marketplace mechanics are in SW.3: private offers, and drawdown against the buyer's cloud commitment. [VF: E2-S034, E2-S036, E2-S020, E2-S038]
- Drawdown against an existing cloud commitment removes a new-vendor budget line for the buyer. [VF: E2-S036, E2-S020] [AJ]

---

## DV: Start-up selling agentic SDLC and developer tools

Only cost levers for token-heavy coding workloads are here. The product landscape is covered by E3.

- Coding agents resend long, stable prefixes (repository context, tool definitions), so prompt caching is the dominant lever. [AJ]
- Caching prices:
  - Anthropic: cache reads cost 0.05x the base price on Opus 5.5 and Sonnet 5.5; 1-hour cache writes cost 2x. [VF: V2-S002]
  - OpenAI: cached input on gpt-6.1-sol costs US$0.10 vs US$2.00 per 1M. [VF: A5-S004]
  - Azure OpenAI: a 1,024-token minimum prefix; `prompt_cache_key` improves matching. [VF: E2-S019]

  (volatile; re-verify quarterly)
- Azure OpenAI caveats:
  - above about 15 requests per minute for the same prefix and key, some requests miss the cache;
  - caches clear within 5–10 minutes of inactivity and always within an hour;
  - GPT-5.6 and later can charge for cache writes.

  [VF: E2-S019]
- Interactive coding needs low latency, so batch rarely fits. Flex (OpenAI, at Batch rates) and Bedrock Flex (50% off) suit background agents such as test generation and migrations, which can tolerate 429s or delay. (volatile; re-verify quarterly) [VF: E2-S031, E2-S032] [AJ]
- OpenAI Fast/Priority mode and Bedrock Priority (75% premium) buy latency for interactive sessions. Anthropic no longer sells Priority Tier commitments. (volatile; re-verify quarterly) [VF: E2-S031, E2-S032, E2-S006]

---

## AG: Start-up selling agents to enterprises

### AG.1 Distribution routes for agents (existence, launch, listing requirements)

**AWS Marketplace**

- The "AI Agents and Tools" category (AI agents, MCP servers, A2A servers) was announced at AWS Summit New York on 16 July 2025. [VF: E2-S035]
- Sellers register through AWS Partner Central. Listings are either a SaaS API-based product pointing at the seller's endpoint and integrated with Marketplace APIs, or a container run on Amazon Bedrock AgentCore Runtime. [VF: E2-S035]
- API-based listings support free trials and the SaaS Co-Sell Benefit. [VF: E2-S035]

**Microsoft 365 Agent Store**

- Introduced on 19 May 2025 (Build 2025), with partner agents such as Jira, Monday.com and Miro. [VF: E2-S021]
- Partners submit through Partner Center under "Apps and agents for Microsoft 365 and Copilot". After Microsoft approves, the agent is listed in the commercial marketplace and appears in the Agent Store once an admin enables it. [VF: E2-S040]
- Microsoft says every partner agent is validated. App Compliance Program certification is optional. Declarative agents built with Agents Toolkit cannot be submitted to the commercial marketplace. [VF: E2-S040]

**Google Cloud Marketplace and Gemini Enterprise Agent Gallery**

- Announced 14 October 2025. [VF: E2-S037]
- Listing a partner agent:
  - onboarding needs only a link to an A2A Agent Card;
  - validated agents are procured by IT and added to the customer's Agent Gallery;
  - entitlements are pushed to the partner through Pub/Sub and the Partner Procurement API.

  [VF: E2-S037]
- There is a "Google Cloud Ready - Gemini Enterprise" designation. Pricing can be subscription, usage-based, custom or outcome-based. [VF: E2-S037]
- Partner docs requirements:
  - an Agent Card aligned to the A2A specification, stored in Cloud Storage;
  - discoverable in Gemini Enterprise;
  - uses Model Garden models by default;
  - supports A2A interoperability;
  - no professional services or hardware billed through the listing.

  [VF: E2-S039]

**Salesforce AgentExchange**

- Launched 4 March 2025 inside Agentforce on the AppExchange model, with more than 200 partners. [VF: E2-S041]
- Salesforce said launch listings had passed "rigorous security and customer reviews". [VF: E2-S041]
- The review criteria were not found. [NPV]

**Reading the routes together**

- Each marketplace imposes its host platform's agent protocol or runtime: A2A Agent Cards for Google, a Microsoft 365 app package for Microsoft, AgentCore or an API-based SaaS listing for AWS, Agentforce components for Salesforce.
- An agent start-up that wants more than one route should keep a protocol-neutral core with thin adapters.

[AJ]

### AG.2 Terms that follow an agent into the enterprise

- Agents built on Claude carry the Usage Policy's high-risk human-in-the-loop and disclosure requirements and the consumer-facing AI-disclosure rule into the customer deployment. [VF: E2-S005]
- Agents built on Google generative AI carry the under-18 and clinical-use restrictions, which Google may enforce by suspension. [VF: E2-S007]
- Google indemnifies Generated Output, but not the actions or tasks an AI agent performs. [VF: E2-S007]

---

## Open / not publicly verified

1. **Microsoft for Startups.** The official eligibility criteria and tier mechanics were not reached (third-party only). [NPV]
2. **OpenAI start-up programme.** No official page was found; amounts conflict. [NPV]
3. **Mistral start-up programme.** Its existence and terms could not be confirmed. [NPV]
4. **AWS Activate Portfolio ceiling.** AWS's own pages say US$100,000 or US$200,000. [NPV]
5. **Mistral Medium 3.5 Modified MIT.** The exact threshold wording (monthly vs annual revenue, about US$20m) was not read from the licence file. [NPV]
6. **Mistral Large 4.** The licence is unpublished as of 6 October 2026. [NPV]
7. **gpt-oss USAGE_POLICY.** The text of the file was not retrieved. [NPV]
8. **Qwen3.8-Max License.** The licence file was not read; secondary reports only. [NPV]
9. **Muse Glimmer licence.** Apache 2.0 rests on secondary sources; the model card was not reached. [NPV]
10. **Meta Model API (Muse Spark).** Commercial and data-use terms are unknown. [NPV]
11. **OpenAI Services Agreement.** The current wording on resale, and the full permitted exception to the competing-model ban, were not confirmed against openai.com. [NPV]
12. **Mistral Commercial Terms.** The full text of competing-model and data-licence clauses was not confirmed on mistral.ai. [NPV]
13. **Amazon Bedrock prompt-caching discount.** No figure was found on an AWS page. [NPV]
14. **AWS Prescriptive Guidance.** No document dedicated to multi-tenant generative AI was found; only ML Blog posts. [NPV]
15. **OWASP and tenant isolation.** No item dedicated to tenant isolation was found beyond LLM08. [NPV]
16. **Salesforce AgentExchange.** Security-review criteria and listing requirements were not found. [NPV]
17. **Microsoft Agent Store validation checklist.** The detail ("Must fix" items) is third-party only. [NPV]
18. **Microsoft multiparty private offers.** The current geographic availability was not established (sources conflict). [NPV]
19. **Marketplace fees.** Fee and revenue-share levels on any of the three hyperscaler marketplaces were not recorded, by design.
20. **SOC 2 framework status.** This rests on audit-firm summaries; the AICPA page was blocked. [NPV]
21. **IAF ISO/IEC 27001 transition notice.** The primary IAF document was not read; this rests on certification-body material. [NPV]
22. **Anthropic Usage Policy.** The page shows an effective date of 12 November 2026; the differences from the version in force today were not compared. [NPV]
