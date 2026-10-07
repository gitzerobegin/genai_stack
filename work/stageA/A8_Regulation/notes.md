# Stage A, stream A8: Regulation and standards notes

As of 7 October 2026. Stream ⑧. Records: `regulatory_facts.json` (18 records). Source log: `sources.csv` (39 sources). Archive: `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A8/` (27 search-tool extracts and 12 text snapshots).

**Research environment caveats.** Every regulator host was blocked by the egress proxy: occ.gov, federalreserve.gov, fdic.gov, bankofengland.co.uk, fca.org.uk, gov.uk, legislation.gov.uk, eur-lex, the EBA, ESMA, EIOPA and the Commission, plus nist.gov, iso.org, owasp.org and sec.gov. Regulator facts therefore come from search-tool extracts of regulator pages. Under the style guide, these count as primary sources capped at `medium`, and rise to `high` only when a second source agrees. The **shared web-search budget (200 calls per turn) ran out** partway through the stream. That left items 6 (partly) and 7 to 12 of the brief thinly covered or unverified (see (e)). The fetchable vendor compliance pages (cloud.google.com, anthropic.com, platform.claude.com) were snapshotted. Where they describe a regulation they are labelled **Reported**, because a vendor is not the regulator.

Conflict of interest: the author is an Anthropic model. Two sources are Anthropic's own (A8-S035 Code of Practice signature; A8-S036 data-residency docs). They are used as facts only, alongside a non-Anthropic source (Google Cloud) wherever possible.

---

## (a) What changed since the plan's assumptions

| Plan / brief assumption | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| "SR 11-7" is the US MRM reference | SR 11-7 was **superseded** on 17 April 2026 by Fed SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026. The new guidance has a narrower model definition, a risk-based approach and a US$30bn asset focus, and is explicitly non-enforceable. **Generative and agentic AI are out of scope**, and an AI RFI was announced but had not been found published | Superseded | A8-S001, A8-S002, A8-S003, A8-S005, A8-S007 |
| PRA SS1/23 | Still current. Effective 17 May 2024. No amendment found. The PRA ran AI/ML roundtables on applying it in October 2025 | No change | A8-S008, A8-S009 |
| EU AI Act high-risk obligations from August 2026 | The **Digital Omnibus**, Regulation (EU) 2026/1744 (OJ 24 July 2026, in force 27 July 2026), moved Annex III to **2 December 2027** and Annex I to **2 August 2028**. Article 4 (AI literacy) was softened. The Article 50(2) marking grace period runs to 2 December 2026 | Superseded (dates) | A8-S011, A8-S012, A8-S013, A8-S014 |
| GPAI obligations from August 2025 | Applies from 2 August 2025, and has been **enforceable by the Commission from 2 August 2026**. Legacy models must comply by 2 August 2027. The Code of Practice was published 10 July 2025 | No change (now enforceable) | A8-S015, A8-S019 |
| DORA critical ICT third-party providers (CTPPs) | First CTPP list on 18 November 2025: 19 providers, including AWS, Google Cloud and Microsoft. **No AI model vendor designated** | New fact | A8-S020, A8-S022, A8-S025 |
| UK critical third parties regime | First HMT designations in force 13 July 2026: AWS, Google Cloud, Microsoft and Oracle. **No AI model vendor designated** | New fact | A8-S023, A8-S024 |
| OWASP agentic list, NIST AI 600-1 updates, ISO 42005/42006, DPF litigation, Data (Use and Access) Act (DUAA) commencement, SEC predictive data analytics (PDA) rule | Could not be checked in this run | Not publicly verified | (none) |

## (b) Ambiguities owned

None of the inventory's A1–A19 ambiguities belong to stream ⑧. Stream ⑧ shares H8 with stream ①.

## (c) Hypothesis evidence

### H8: regulatory expectations of ongoing monitoring (sourced bullets, no verdicts)

- **US (SR 26-2 / OCC 2026-13).**
  - Risk-based MRM still keeps effective challenge and the assessment of model risk individually and in aggregate.
  - Models treated as immaterial must still be identified and monitored for whether they become material. [VF: A8-S001]
  - GenAI and agentic AI models are outside scope. Firms' own risk management and governance should determine controls for tools not covered. [VF: A8-S002]
- **US supervisory observation.** Banks use GenAI and agentic AI in limited use cases "with guardrails and human-in-the-loop accountability". [VF: A8-S004]
- **US third-party guidance.** The interagency third-party guidance names "ongoing monitoring" as a lifecycle stage. [R: A8-S033]
- **UK PRA (SS1/23).**
  - The principles span the model lifecycle, including independent validation and model risk mitigants. [VF: A8-S008]
  - The October 2025 PRA roundtable on AI/ML under SS1/23 explicitly covered "ongoing model monitoring", risk appetite, tiering, explainability and independent validation. It noted that AI/ML models "introduce higher uncertainty". [VF: A8-S009]
- **EU AI Act, provider side (Article 72).**
  - Providers of high-risk systems must run a post-market monitoring system that actively and systematically collects and analyses performance data over the lifetime of the system, including data from deployers.
  - The monitoring plan forms part of the technical documentation. [VF: A8-S017]
  - The Omnibus removed the Commission's power to adopt a harmonised template for the Article 72(3) plan. [VF: A8-S011]
- **EU AI Act, deployer side (Article 26(5)).**
  - Deployers monitor operation against the instructions for use, inform providers, and suspend use and notify where there is risk.
  - Deployers keep logs for at least six months. Financial institutions keep them within their financial-services documentation. [VF: A8-S016]
- **EU AI Act, logging capability (Article 12).** Providers must build in logging that records events relevant to risk identification, post-market monitoring and deployer monitoring. [VF: A8-S016]
- **DORA.** Financial entities must engage in ongoing monitoring of ICT risks, extending to ICT third-party services. [R: A8-S025]
- **GPAI (Article 55).** Systemic-risk model providers must run model evaluations including adversarial testing, and report serious incidents. [VF: A8-S019]

### How an LLM or agent fits the definition of a "model" (sourced bullets)

- **US definition (2026).** A model is "a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates". This excludes simple arithmetic and "deterministic rule-based processes and software where there are no statistical, economic, or financial theories underpinning their design or use". [VF: A8-S002]
- **US scope carve-out.** This is separate from the definition: "Generative AI and agentic AI models are novel and rapidly evolving" and are not within the scope of the guidance. The principles apply to "non-generative, non-agentic AI models". [VF: A8-S002, A8-S001]
  - The search tool's reading was that a GenAI system might meet the definition and still be out of scope. That reading is interpretation, not regulator text. [AJ]
- **Earlier US position.** In a 2022 OCC testimony (seen in search results, not archived), an OCC official said many AI tools "would be considered models" under the earlier MRM guidance. This is recorded as context only. [NPV]
- **UK (SS1/23).**
  - The principles "are applicable to all types of models that are used to inform business decisions, whether developed in-house or externally (including vendor models)".
  - They are technology-agnostic, with sub-principles on managing risks from AI techniques. [VF: A8-S008]
  - The inventory is expected to include AI/ML models. Explainability and transparency are complexity factors. [VF: A8-S037]
- **UK GenAI classification.** BoE AI Consortium members (3 June 2026) noted that GenAI systems "are often classified as high risk under frameworks such as SS1/23". [VF: A8-S010]
- **SS1/23 exact definition.** The exact SS1/23 definition text was not extracted in this run. [NPV]
- **EU AI Act framing.** The Act regulates "AI systems" and "general-purpose AI models", not "models" in the MRM sense. An operator that builds and uses its own system is both provider and deployer. [VF: A8-S016]

## (d) Instruments an enterprise architect would expect that the plan's list omits

- **US Interagency Guidance on Third-Party Relationships: Risk Management.** This is the US counterpart to SS2/21 and SYSC 8 for bank-affiliated managers. [R: A8-S033] (record R-US-TPRM)
- **EU Code of Practice on Transparency of AI-generated Content and the Commission's Article 50 guidelines (C(2026) 5054, July 2026).** These are directly relevant to client-facing chat and published commentary. [VF: A8-S018]
- **NIST CAISI RFI on AI agent security (Federal Register, 8 January 2026).** This is the first US standards-body workstream specific to agents. [VF: A8-S006]
- **ESMA cloud-outsourcing guidelines.** These are the relevant EU outsourcing guidance for UCITS management companies and AIFMs. Not researched. [NPV]

## (e) Gaps: what could not be verified, and why

All of the gaps below stem from regulator hosts being blocked and the shared search budget being exhausted before these items were reached. Each needs a follow-up run.

1. **PRA SS2/21 and FCA SYSC 8 / FG16/5.** The regulator texts, effective and update dates, and the "stressed exit" wording. The current content rests only on Google Cloud's summaries (Reported).
2. **EBA outsourcing guidelines.** The reference number, and their status after DORA (repealed or revised for ICT arrangements?). ESMA's cloud guidelines were not covered.
3. **Data transfers.** Commencement of the Data (Use and Access) Act 2025, renewal of the EU adequacy decision for the UK, and the status of the EU–US Data Privacy Framework and its court challenges. All are unverified.
4. **NIST.** The AI RMF 1.0 and NIST AI 600-1 dates, and any 2025–2026 updates. Unverified (nist.gov blocked).
5. **ISO/IEC 42005 and 42006.** Publication status unverified. The 42001:2023 edition is known only from a vendor page.
6. **OWASP.** The Top 10 for LLM Applications 2025, and the exact name and date of the agentic Top 10. Unverified.
7. **Regulator AI statements.**
   - FCA: the AI update, AI Lab and live testing, and any 2026 statements on agentic AI. Unverified.
   - BoE/FCA AI survey: unverified.
   - IOSCO, FSB and ESMA statements on AI in asset management: unverified.
   - BoE's 2026 response to the Treasury Committee: exists by title only.
8. **SEC.** Withdrawal of the predictive data analytics proposal, and any adviser AI statements. Unverified.
9. **Minor gaps.**
   - Lead Overseer allocation per CTPP.
   - The exact deadline for the UK CTP self-assessment.
   - Publication of the US AI RFI after the latest source (none found).
   - Wording of the amended Article 4 of the AI Act. One extract conflicts with the commentary; the commentary was preferred and the conflict is noted in R-EUAIA.

## Five most important regulatory facts for the architecture

1. **SR 11-7 is gone.** SR 26-2 (17 April 2026) excludes GenAI and agentic AI from US MRM guidance pending an AI RFI. Firms must govern LLM agents under their own frameworks, so MRM-grade inventory and monitoring stay a design requirement. [VF: A8-S001, A8-S002]
2. **EU AI Act Annex III high-risk deferred to 2 December 2027** by Regulation (EU) 2026/1744. GPAI enforcement (from 2 August 2026) and Article 50 transparency (from 2 August 2026) are **not** deferred. [VF: A8-S011, A8-S012, A8-S019]
3. **Hyperscalers are under direct oversight.** They are DORA CTPPs (18 November 2025) and UK CTPs (13 July 2026), but **no LLM vendor is designated in either regime**. Direct model APIs leave the full third-party oversight burden on the firm. [VF: A8-S020, A8-S023]
4. **Deployer logging is set out in the Act.** Deployers of high-risk AI keep logs for at least six months within their financial-services record-keeping, and must monitor and suspend on risk. This defines the minimum L9 trace-retention and kill-switch capability. [VF: A8-S016]
5. **PRA SS1/23 covers vendor models and AI.** It applies to "all types of models … including vendor models". UK supervisors report that GenAI is often tiered high-risk under it, which drives validation and monitoring effort for L1 choices. [VF: A8-S008, A8-S010]
