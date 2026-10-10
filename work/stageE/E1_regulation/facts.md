# E1 regulation brief for the Stage E view writers

**As of 9 October 2026.** The new records are in `work/stageE/E1_regulation/regulatory_facts.json` and are merged into `05_Data/regulatory_facts.json`:

- R-EU-CRA
- R-EU-PLD
- R-EU-NIS2
- R-EU-DATA-ACT
- R-EU-AIA-ROLES
- R-US-STATE-AI
- R-UK-SOFTWARE

The sources are listed in `sources.csv`, as E1-S001 to E1-S057. The EU, UK and US hosts were all blocked to direct fetch, so every source is a search-tool extract. A fact backed by a single extract is therefore at most medium confidence.

The existing records still hold their own facts; cite them, do not restate them:

- R-EUAIA: AI Act dates, Article 25(1) triggers, deployer duties
- R-EU-OMNIBUS-AI
- R-DORA
- R-DATA-TRANSFERS

## All views (TS, SW, SU and the vendor start-ups)

- The Cyber Resilience Act's reporting duty has applied since 11 September 2026. Its main obligations, including conformity assessment and CE marking, apply from 11 December 2027 (R-EU-CRA). [VF: E1-S001, E1-S002]
- Under the CRA, manufacturers send an early warning within 24 hours of becoming aware of an actively exploited vulnerability or a severe incident, and a notification within 72 hours. The final report is due 14 days after a fix (for a vulnerability) or one month after the notification (for an incident). [VF: E1-S003]
- CRA reports go through ENISA's Single Reporting Platform, which went live on 11 September 2026. Exploitation known before that date does not have to be reported retrospectively. [VF: E1-S006, E1-S003]
- The revised Product Liability Directive treats software as a product "irrespective of the mode of its supply or usage", including cloud and SaaS. It applies to products placed on the market from 9 December 2026, which is also the transposition deadline (R-EU-PLD). [VF: E1-S010, E1-S011, E1-S012]
- The AI Liability Directive proposal was withdrawn (OJ notice of 6 October 2025). The PLD is the EU's no-fault route for AI harm. [VF: E1-S014]
- Commentary reads the PLD as covering AI systems as software, including systems that keep learning after release. [R: E1-S015]
- Whoever supplies an AI system under its own name is that system's provider, even when the model comes from another vendor (R-EUAIA, Article 25(1)). [VF: A8-S016]
- An integrator becomes the provider of a modified GPAI model only if its modification uses more than one third of the original model's training compute. Even then, its duties cover only the modification (R-EU-AIA-ROLES). [VF: E1-S034]
- From 12 January 2027, cloud and SaaS providers may not charge for switching, data egress included. Until then, switching charges are capped at cost (R-EU-DATA-ACT). [VF: E1-S025, E1-S026]
- US state AI duties mostly apply only where a product makes, or helps make, consequential decisions about individuals (R-US-STATE-AI). [AJ]

## TS: technology service provider

- NIS2 Annex I names cloud computing, data centre and CDN providers, managed service providers and managed security service providers. Medium-sized and large providers are in scope (R-EU-NIS2). [VF: E1-S017, E1-S018]
- Under NIS2, large Annex I entities are "essential" and medium-sized ones "important". Cloud, MSP and MSSP providers fall under the Member State of their main EU establishment. [VF: E1-S016]
- NIS2 significant incidents are reported in three steps: an early warning within 24 hours, a notification within 72 hours and a final report within one month. [VF: E1-S016, E1-S017]
- NIS2 Article 21 measures include supply-chain security with direct suppliers. Implementing Regulation (EU) 2024/2690 requires these providers to keep a supply-chain security policy, which reaches model API vendors. [VF: E1-S016, E1-S019]
- NIS2 holds management bodies liable and requires them to be trained. Fines are at least EUR 10m or 2% of turnover for essential entities, and EUR 7m or 1.4% for important ones. [VF: E1-S016]
- A NIS2 amendment proposal (COM(2026) 13, 20 January 2026) would let the Commission restrict the outsourcing of operational control to managed service providers. It has not been adopted. [R: E1-S020]
- A hosted service is not itself a CRA product unless it is the remote data processing of a product the company also supplies, such as an installable client, SDK or connector. [VF: E1-S001] [R: E1-S007]
- Data Act switching rules apply to SaaS:
  - at most two months' notice to start a switch;
  - a 30-day transition with assistance;
  - free open interfaces;
  - export of the customer's data in a machine-readable format.

  [VF: E1-S025, E1-S026]
- A Digital Omnibus carve-out for custom-made services and SME SaaS under pre-September 2025 contracts is still only a proposal. [VF: E1-S027] [R: E1-S028]
- TS chat and generation features carry the provider duties under AI Act Article 50: tell people they are talking to an AI, and mark generated content machine-readably. Systems already on the market before 2 August 2026 have until 2 December 2026 to comply with the marking duty (R-EU-AIA-ROLES). [VF: E1-S035, E1-S036]
- The UK Cyber Security and Resilience Bill would bring medium and large managed service providers into the NIS Regulations, with registration with the ICO within three months of commencement. It was still before the Lords as of 9 October 2026 (R-UK-SOFTWARE). [VF: E1-S021, E1-S022, E1-S023]
- Agents that can delete or corrupt a person's data are the main PLD exposure for a hosted service. Business-to-business losses mostly fall outside it. [AJ]

## SW: software product company

- Installed software, SDKs and on-premises editions are CRA products, and the vendor is their manufacturer. From 11 December 2027 each EU release needs:
  - a conformity assessment;
  - an EU declaration of conformity;
  - the CE marking.

  [VF: E1-S001, E1-S002]
- Under the CRA, the support period must reflect the product's expected use and be at least five years, unless expected use is shorter. Its end month and year are stated at the time of purchase. [VF: E1-S001]
- Under the CRA, manufacturers document components, including in a software bill of materials. The SBOM need not be published. [VF: E1-S001]
- A vendor-run endpoint that the product needs in order to work counts as its "remote data processing" and is in CRA scope (Article 3(2), recitals 11 and 12). [VF: E1-S001]
- Open-weight models and open-source libraries bundled into a commercial product become components the manufacturer must document and patch. [AJ]
- A CRA product that is also a high-risk AI system is deemed to meet the cybersecurity requirement of AI Act Article 15 when it meets CRA Annex I and declares the protection level. Accuracy and robustness still apply. [R: E1-S008]
- Under the PLD, vendors remain liable for defects arising after release from software within their control, including a lack of safety-relevant security updates. Component makers share liability. [VF: E1-S010]
- PLD disclosure orders and the presumption for technical complexity make release history, evaluation records and logs the main defence. [VF: E1-S010] [R: E1-S013]
- Where a customer builds a high-risk system on the vendor's component, AI Act Article 25(4) requires a written agreement covering information, technical access and assistance (R-EU-AIA-ROLES). [VF: E1-S033]
- Free and open-source components are exempt from Article 25(4), but only while they are not monetised; paid support counts as monetisation. GPAI models are never exempt. [VF: E1-S033]
- In the UK there is no statute equivalent to the CRA. The voluntary Software Security Code of Practice (14 principles, launched 7 May 2025, with self-assessment) is the buyer's reference. [VF: E1-S051, E1-S052]
- The UK PSTI regime covers only consumer connectable products; enterprise devices are out of scope. [VF: E1-S053, E1-S054]
- From 1 January 2027, Colorado customers can expect to ask the vendor, as developer, for documentation of:
  - intended uses;
  - training-data categories;
  - known limitations;
  - instructions for human review.

  [VF: E1-S038, E1-S039]

## SU: start-up

- A start-up selling downloadable software or an SDK into the EU is a CRA manufacturer from its first sale. Micro and small enterprises are spared only the fine for missing the 24-hour early warning. [VF: E1-S001]
- Open-source software stewards have lighter CRA duties and are not fined. Their reporting starts on 11 December 2027. [VF: E1-S004, E1-S003]
- AI Act Article 62 measures for SMEs and start-ups include:
  - priority access to sandboxes;
  - tailored training;
  - dedicated channels;
  - conformity-assessment fees reduced in proportion to size.

  [VF: E1-S029]
- Sandbox participation is free for SMEs and start-ups. [VF: E1-S030]
- SMEs, start-ups and small mid-caps may file simplified technical documentation on a Commission template. [VF: E1-S032]
- AI Act fines on SMEs and start-ups are capped at the lower of the percentage or the fixed amount. [VF: E1-S031]
- These reliefs cut cost, not obligations; role analysis and Article 50 disclosure are still needed from launch. [AJ]
- The Code of Practice on Transparency of AI-generated Content is a voluntary, accepted way to show Article 50 compliance; about 190 organisations had signed it by August 2026. [VF: E1-S037]
- Texas TRAIGA has been in effect since 1 January 2026. It prohibits AI developed or deployed with intent to cause harm or to discriminate unlawfully; disparate impact alone is not enough. The AG may seek penalties of up to USD 200,000 for an uncurable violation. [VF: E1-S042, E1-S043]
- Texas offers a sandbox for testing AI systems for up to 36 months. [VF: E1-S043]
- California SB 53 applies only to frontier developers with more than USD 500m revenue. The AI Transparency Act (operative 2 August 2026) applies only to generative systems with more than 1,000,000 monthly users. Most start-ups fall below both. [VF: E1-S044, E1-S045]
- California's CPPA rules require businesses that use ADMT for significant decisions to comply from 1 January 2027. [VF: E1-S047]
- Colorado's original AI Act was repealed and replaced by SB 26-189 (signed 14 May 2026). The new law is narrower, centred on notice and review, and drops the duty of care and impact assessments. [VF: E1-S038] [R: E1-S041]
- A federal court order of 27 April 2026 stays enforcement of the Colorado law until rulemaking is complete. [VF: E1-S040, E1-S050]
- Executive Order 14365 (11 December 2025) set up a DOJ task force to challenge state AI laws. No federal preemption statute was found. [VF: E1-S049]

## AT: start-up selling AI tools into the enterprise GenAI stack

Examples are gateways, evaluation, guardrails and retrieval components. Customers are regulated and large enterprises, so most duties arrive through the customer.

- A tool that is itself an AI system supplied under the vendor's name makes the vendor its provider. A component that is not an AI system still falls under Article 25(4) written agreements when it goes into a customer's high-risk system (R-EUAIA; R-EU-AIA-ROLES). [VF: A8-S016, E1-S033]
- Installed or self-hosted tools and SDKs sold in the EU are CRA products. A SaaS-only tool is in CRA scope only as the remote processing of a product (R-EU-CRA). [VF: E1-S001]
- R-DORA already records that EU financial entities must include Article 30 contract provisions for every ICT service. The content of those clauses, which the vendor will be asked to sign, is new in E1. The minimum clauses are:
  - service description;
  - subcontracting conditions;
  - data locations;
  - data protection and return of data on exit;
  - service levels;
  - incident assistance;
  - cooperation with authorities;
  - termination rights;
  - resilience training.

  [VF: A8-S021, E1-S055]
- For critical or important functions, DORA adds exit strategies and audit and inspection rights, including on site. [VF: E1-S055, E1-S056]
- DORA subcontracting rules require the vendor to identify all subcontractors, such as model API providers. Access and audit rights must pass down the chain, and the customer must be able to object to material changes. [VF: E1-S057]
- PLD exposure is mostly indirect for an AT vendor: a component supplier is liable where its defective component caused the product to be defective (R-EU-PLD). [VF: E1-S010]
- A NIS2 customer will put supply-chain security terms on the tool vendor (R-EU-NIS2). [VF: E1-S016]

## DV: start-up selling agentic SDLC and developer tools

- IDE plug-ins, CLIs, agents and SDKs installed on customer machines are CRA products. The CRA applies to:
  - the 24/72-hour reporting duty, now;
  - the SBOM and support period, from 11 December 2027;
  - the remote data processing back end on which they depend.

  (R-EU-CRA) [VF: E1-S001, E1-S003]
- A coding agent that writes code into a customer's product makes the DV vendor a supplier of components to that customer's CRA products. The customer, as manufacturer, will ask for vulnerability information. [AJ]
- AI Act provider duties follow R-EU-AIA-ROLES. Code assistants are not listed as high-risk, so the live duties are Article 50 disclosure and the provider role. [VF: E1-S035] [AJ]
- DORA Article 30 clauses (as in the AT group) apply when a financial entity buys the tool as an ICT service (R-DORA). [VF: A8-S021, E1-S055]
- PLD exposure is low for business-to-business tooling, but data destroyed by an agent is a recoverable type of damage under the PLD. [AJ]

## AG: start-up selling agents to enterprises

- An agent supplied under the vendor's name makes the vendor its AI-system provider (R-EUAIA). Article 50(1) disclosure applies if the agent talks to people (R-EU-AIA-ROLES). [VF: A8-S016, E1-S035]
- If a customer deploys the agent in an Annex III use, such as hiring or credit scoring, high-risk duties apply from 2 December 2027 (R-EUAIA, R-EU-OMNIBUS-AI). [VF: A8-S011]
- If the customer rebrands the agent or changes its purpose, the customer can become the provider. The vendor must then cooperate and supply information (R-EUAIA, Article 25(2)). [VF: A8-S016, E1-S033]
- Agents sold as installable software are CRA products. A hosted agent platform serving EU businesses may itself be a NIS2 entity, as a TS provider would be (R-EU-CRA, R-EU-NIS2). [VF: E1-S001, E1-S017]
- DORA Article 30 and the subcontracting rules apply as in the AT group. An agent supporting a critical or important function will face audit, exit and subcontracting clauses (R-DORA). [VF: E1-S055, E1-S056, E1-S057]
- PLD exposure is the highest of the vendor views: agents act on systems, and the PLD presumes defectiveness where complexity makes proof excessively difficult (R-EU-PLD). [VF: E1-S010]
- US agents that assist consequential decisions trigger developer documentation duties in Colorado (from 1 January 2027) and CPPA ADMT duties in California (R-US-STATE-AI). [VF: E1-S038, E1-S047]

## Not publicly verified / open

- The exact allocation of the CRA's EUR 15m / 2.5% fine tier across obligations (Article 64(2)). Sources differ. [NPV]
- The Commission CRA guidance annex C(2026) 5252 was not read in full, so its precise line on SaaS and on support periods is unknown. [NPV]
- The content of the CRA Delegated Regulation (EU) 2026/881. [NPV]
- PLD Article 15 (no contractual exclusion) and the PLD limitation periods were not extracted. [NPV]
- Whether fine-tuned weights, embeddings or agent configurations count as Data Act "exportable data" or "digital assets". [NPV]
- The fallback for the GPAI one-third test when the original model's compute is unknown. [NPV]
- The AI Act Article 3(68) wording ("downstream provider"). [NPV]
- Per-Member-State transposition status of NIS2 and the PLD. [NPV]
- The current Lords stage of the UK Cyber Security and Resilience Bill (sources differ), its Royal Assent date, and whether managed service providers get 24-hour / 72-hour reporting under it. [NPV]
- The effective dates of the California AI bills signed in September 2026 (SB 947, SB 951, SB 813, AB 1405, SB 1050, AB 1979, SB 503, SB 1119, SB 867). [NPV]
- California AB 2013 rests on secondary sources only. [NPV]
- Whether Commerce published its evaluation of "onerous" state AI laws under EO 14365. [NPV]
- The outcome of X.AI LLC v. Weiser after rulemaking. [NPV]
- Texas TRAIGA cure-period detail, which came from bill versions before enrolment. [NPV]
