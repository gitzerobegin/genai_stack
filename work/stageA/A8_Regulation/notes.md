# Stage A, stream A8: Regulation and standards notes

As of 7 October 2026. Stream ⑧.

- **Records:** `regulatory_facts.json` (20 records).
- **Source log:** `sources.csv` (62 sources).
- **Archive:** `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/A8/` (50 search-tool extracts and 12 text snapshots).

The work ran over two turns. The first turn covered items 1 to 5. The shared web-search budget ran out mid-stream, so items 6 to 12 were completed in a second turn (sources A8-S040 to A8-S062).

**Research environment caveats.**

- **Blocked hosts.** The egress proxy blocked every regulator and standards host: occ.gov, federalreserve.gov, fdic.gov, bankofengland.co.uk, fca.org.uk, gov.uk, legislation.gov.uk, eur-lex, curia, the EBA, ESMA, EIOPA, the Commission, nist.gov, iso.org, owasp.org, sec.gov, iosco.org and ico.org.uk.
- **How regulator facts were sourced.** Regulator facts come from search-tool extracts of those regulator pages. Under the style guide these count as primary, capped at `medium`. They rise to `high` only when a second source agrees.
- **Vendor pages.** The fetchable vendor compliance pages (cloud.google.com, anthropic.com, platform.claude.com) were snapshotted. Where they describe a regulation, they are labelled **Reported**.

**Conflict of interest.** The author is an Anthropic model. Two sources are Anthropic's own: A8-S035 (Code of Practice signature) and A8-S036 (data-residency docs). They are used as facts only, alongside non-Anthropic sources where possible.

---

## (a) What changed since the plan's assumptions

| Plan / brief assumption | Current reality (as of 7 October 2026) | Flag | Sources |
|---|---|---|---|
| "SR 11-7" is the US model risk management (MRM) reference | SR 11-7 was **superseded** on 17 April 2026 by Fed SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026. **Generative and agentic AI are out of scope.** The announced AI RFI had not been found published | Superseded | A8-S001, A8-S002, A8-S003, A8-S005, A8-S007 |
| PRA SS1/23 | Effective 17 May 2024. The PRA later narrowed its expectations to firms with internal-model (IM) approval. AI/ML roundtables were held in October 2025 | No change (scope narrowed) | A8-S008, A8-S009, A8-S061 |
| EU AI Act high-risk obligations from August 2026 | The Digital Omnibus, Regulation (EU) 2026/1744 (in force 27 July 2026), moved Annex III to **2 December 2027** and Annex I to **2 August 2028**. Article 4 was reworded | Superseded (dates) | A8-S011, A8-S012, A8-S014, A8-S060 |
| GPAI obligations from August 2025 | Enforceable by the Commission from 2 August 2026. The Code of Practice was published 10 July 2025 | No change | A8-S015, A8-S019 |
| DORA critical third-party providers (CTPPs) | First list on 18 November 2025: 19 providers. **No AI model vendor designated** | New fact | A8-S020, A8-S022 |
| UK critical third parties (CTP) regime | First designations in force 13 July 2026: AWS, Google Cloud, Microsoft and Oracle. **No AI model vendor designated** | New fact | A8-S023, A8-S024 |
| PRA SS2/21 | Revised by PS7/26 (March 2026). New material third-party notification and register requirements apply from **18 March 2027** | Superseded (revised) | A8-S048, A8-S062 |
| FCA SYSC 8 / FG16/5 | Unchanged in substance. FG16/5 dates from 2016, updated 2019. The FCA's PS26/2 material third-party reporting applies from **18 March 2027** | No change (new reporting layer) | A8-S049, A8-S062 |
| EBA outsourcing guidelines (2019) | Final replacement guidelines on non-ICT third-party risk issued **18 September 2026**, with a two-year transition. The 2019 guidelines are to be repealed | Superseded (pending application) | A8-S050 |
| Data (Use and Access) Act 2025 | All data protection provisions in force by 19 June 2026 (main tranche 5 February 2026) | New fact | A8-S051 |
| EU–UK adequacy | Renewed 19 December 2025, valid to 27 December 2031 | New fact | A8-S052 |
| EU–US Data Privacy Framework | Upheld by the General Court on 3 September 2025 (T-553/23). The appeal, C-703/25 P, is **pending** | New fact | A8-S053, A8-S054 |
| NIST AI RMF 1.0 / AI 600-1 | AI RMF 1.0 (January 2023) is **under revision**, with no new version published. AI 600-1 final (26 July 2024) unchanged | No change (revision pending) | A8-S043, A8-S044 |
| ISO/IEC 42001 (42005/42006 "if published") | 42001: December 2023. 42005: May 2025. 42006: July 2025. All published | New fact | A8-S045, A8-S046, A8-S047 |
| OWASP Top 10 for LLM Applications 2025 | The 2025 edition (November 2024) has been **superseded by a 2026 edition** (August–September 2026) | Version label wrong | A8-S040, A8-S041 |
| "OWASP Top 10 for Agentic Applications" | The correct name is "OWASP Top 10 for Agentic Applications for 2026", launched 9–10 December 2025 | Renamed (edition label) | A8-S042 |
| SEC predictive data analytics rule | Withdrawn 17 June 2025 | Deprecated | A8-S057 |

## (b) Ambiguities owned

None of the inventory's A1–A19 ambiguities belong to stream ⑧. Stream ⑧ shares H8 with stream ①.

## (c) Hypothesis evidence

### H8: regulatory expectations of ongoing monitoring (sourced bullets, no verdicts)

**United States**

- **SR 26-2 / OCC Bulletin 2026-13.** Risk-based MRM keeps effective challenge and the assessment of model risk individually and in aggregate. Immaterial models must still be identified and monitored for whether they become material. [VF: A8-S001]
- **Scope carve-out.** Generative and agentic AI models are out of scope. Firms' own risk management and governance should determine controls for them. [VF: A8-S002]
- **Supervisory observation.** Banks use GenAI and agentic AI "with guardrails and human-in-the-loop accountability". [VF: A8-S004]
- **Third-party guidance.** The interagency third-party guidance names "ongoing monitoring" as a lifecycle stage. [R: A8-S033]

**United Kingdom**

- **PRA SS1/23.** The principles cover the model lifecycle, including independent validation and model risk mitigants. [VF: A8-S008]
- **October 2025 PRA roundtable.** The roundtable covered "ongoing model monitoring", risk appetite and tiering for AI/ML. [VF: A8-S009]
- **Financial Policy Committee (March 2026).** The FPC judged that agentic AI risks are "likely to increase, potentially rapidly". It commissioned Bank and FCA work on agentic AI. [VF: A8-S056]

**European Union**

- **EU AI Act Article 72 (providers).** Providers must run a post-market monitoring system that actively and systematically collects and analyses performance data over the system's lifetime, including data from deployers. [VF: A8-S017]
- **Article 72(3) template.** The Omnibus removed the Commission's power to adopt the Article 72(3) template. [VF: A8-S011]
- **Article 26(5) (deployers).** Deployers must monitor against the instructions for use, suspend use and notify where there is risk, and keep logs for at least six months within their financial-services records. [VF: A8-S016]
- **Article 12 (logging).** The provider's logging must support post-market monitoring and deployer monitoring. [VF: A8-S016]
- **DORA.** Ongoing monitoring of ICT risks extends to ICT third-party services. [R: A8-S025]
- **GPAI Article 55.** Providers of systemic-risk models must run evaluations including adversarial testing, and report incidents. [VF: A8-S019]
- **ESMA (MiFID II firms, 2024).** ESMA expects "regular AI model testing", monitoring of AI systems, ex-ante controls on inputs and "sufficiently frequent ex-post controls". [VF: A8-S059]

**International**

- **IOSCO supervisory toolkit (May 2026).** The toolkit gives supervisory indicators for asset managers: accuracy of AI-supported valuations against benchmarks, AI-driven mis-selling incidents, and the "level and frequency of human intervention in AI-driven investment process". [VF: A8-S058]

### How an LLM or agent fits the definition of a "model" (sourced bullets)

**United States**

- **2026 definition.** A model is "a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates". This excludes simple arithmetic and deterministic rule-based software. [VF: A8-S002]
- **Separate scope carve-out.** "Generative AI and agentic AI models are novel and rapidly evolving" and are out of scope. The principles apply to "non-generative, non-agentic AI models". [VF: A8-S001, A8-S002]
- **The carve-out names them as models.** The carve-out calls GenAI/agentic systems "models" while excluding them from scope. Whether they meet the definition is therefore left open rather than denied. [AJ]

**United Kingdom (SS1/23)**

- **Definition.** Firms adopt SS1/23's definition: a quantitative method, system or approach applying statistical, economic, financial or mathematical theories. The rest of the sentence was not extracted. "Models are a subset of quantitative methods." [VF: A8-S061]
- **Principle 1.1(b).** Relevant MRM aspects can be applied to material, complex deterministic methods that are not models. [VF: A8-S061]
- **Scope.** The principles apply to all models used to inform business decisions, including vendor models. [VF: A8-S008]
- **Inventory.** The inventory is expected to include AI/ML models. [VF: A8-S037]
- **Classification in practice.** Members of the Bank of England's AI Consortium report that GenAI is "often classified as high risk" under SS1/23-type frameworks. [VF: A8-S010]
- **Earlier US context.** A 2022 OCC testimony said AI tools "would be considered models". It was seen in search results but not archived. [NPV]

**European Union**

- **EU AI Act framing.** The Act regulates "AI systems" and "general-purpose AI models", not "models" in the MRM sense. A firm that builds and uses its own system is both provider and deployer. [VF: A8-S016]

## (d) Instruments an enterprise architect would expect that the plan's list omits

- **PRA PS7/26 and FCA PS26/2 (operational incident and material third-party reporting, from 18 March 2027).** New LLM vendor contracts may need pre-notification. [VF: A8-S062] (in R-PRA-SS221 and R-FCA-SYSC8)
- **IOSCO FR/02/2026 and the ESMA 2024 AI statement.** These are the most asset-management-specific supervisory AI texts found. [VF: A8-S058, A8-S059] (R-INTL-AI-ASSETMGMT)
- **US Interagency Guidance on Third-Party Relationships.** [R: A8-S033] (R-US-TPRM)
- **NIST agent-specific work.** This covers the CAISI agent-security RFI, the NCCoE agent identity concept paper and the Cyber AI Profile. [VF: A8-S006, A8-S044]
- **OWASP Agent Control Standard (announced September 2026).** [VF: A8-S041]
- **EU Code of Practice on Transparency of AI-generated Content, and the Article 50 guidelines (July 2026).** [VF: A8-S018]
- **ESMA cloud-outsourcing guidelines for UCITS management companies and AIFMs.** Not researched. [NPV]

## (e) Gaps: what could not be verified, and why

All regulator hosts were blocked, so every regulator fact rests on search extracts.

1. **PRA SS2/21:** the original 31 March 2022 effective date, and any AI-specific wording. Not confirmed.
2. **EBA:** the reference number of the new third-party guidelines (the search tool said EBA/GL/2026/09) and their exact application date. Not confirmed. ESMA cloud guidelines were not researched.
3. **Data (Use and Access) Act:** the exact wording of the new UK transfer test (s.85) and the automated decision-making changes (s.80). Not extracted.
4. **Latombe appeal (C-703/25 P):** the content of the 4 June 2026 order is unknown. The reported Microsoft intervention is unverified.
5. **NIST:** the AI RMF function names (Govern, Map, Measure, Manage) are not confirmed in extracts and are labelled Reported/low. The tentative NISTIR 8605D is not asserted.
6. **OWASP:** the full 2026 LLM list was not retrieved. ASI02–ASI10 were not retrieved. The 2026 LLM release date conflicts (3 August vs 2 September 2026).
7. **UK AI statements:** the FPC's July 2026 agentic-AI assessment and the FCA 2024 "AI Update" contents were not retrieved. FSB AI work was not researched.
8. **SEC:** the reasons for the PDA withdrawal, adviser Rule 204-2 and any AI-washing enforcement were not researched.
9. **Minor items:**
   - the Lead Overseer for each CTPP;
   - the UK CTP self-assessment deadline;
   - publication of the US AI RFI (none found);
   - the full SS1/23 model-definition sentence (truncated in the extract).
10. **Resolved:** the Article 4 wording conflict. The EUR-Lex text says "Providers and deployers of AI systems shall take measures to support the development of AI literacy…", with no guaranteed level. Both earlier readings were partly right. [VF: A8-S060]

## Five most important regulatory facts for the architecture

1. **SR 11-7 is gone.** SR 26-2 (17 April 2026) excludes GenAI and agentic AI pending an AI RFI. Firms must govern LLM agents under their own frameworks. [VF: A8-S001, A8-S002]
2. **EU AI Act Annex III deferred to 2 December 2027.** GPAI enforcement and Article 50 transparency still apply from 2 August 2026. [VF: A8-S011, A8-S012, A8-S019]
3. **Hyperscalers are CTPPs/CTPs, LLM vendors are not.** From 18 March 2027, UK firms must also pre-notify material third-party arrangements. Direct model APIs leave the oversight and exit-planning burden on the firm. [VF: A8-S020, A8-S023, A8-S062]
4. **Transfers to US-hosted LLM APIs rest on legally contested ground.** EU→US transfers rely on the DPF, which is under pending appeal (C-703/25 P), or on SCCs. EU→UK adequacy is secure to 2031. Processing-location controls and DLP at the gateway matter. [VF: A8-S052, A8-S053]
5. **Ongoing monitoring is a cross-jurisdiction expectation.** It appears in:
   - AI Act Article 26 (logs kept at least six months; monitor and suspend) and Article 72;
   - PRA SS1/23 as applied to AI;
   - ESMA's ex-post controls;
   - IOSCO's human-intervention indicators.

   [VF: A8-S016, A8-S009, A8-S058, A8-S059]
