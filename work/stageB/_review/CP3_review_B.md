# CP3 calibration review B: controls C3 to C8

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Scope** | `work/stageB/C3` to `C8`: `section.md` and `assessments.json` (reviewer A covers L6, L5, L4, C1 and C2 in parallel) |
| **Basis** | Rubric rules 1 to 9 (`work/stage0/08_scoring_rubric.md`, rules 6 to 9 from `checkpoints/CP2/03_CP2_Decisions.md`); the approved L9 to L7 calibration (`checkpoints/CP2/02_Calibration_Review.md`, `work/stageB/_review/CP2_rework_log.md`); V1 and V2 §4 do-not-rely lists |
| **New sources** | 5, `B-REVB-S001` to `B-REVB-S005`, in `work/stageB/_review/sources_added_B.csv`; archived as search extracts in `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/` (direct fetch of vendor trust pages is blocked; confidence medium) |
| **Research budget** | 6 of 15 WebSearch calls, each chosen because it could move a score or a tier: Okta audit evidence, Google SDP CMEK, watsonx.governance certification scope, ValidMind SOC 2, Prisma AIRS certification scope, ModelOp certifications |
| **Tag check** | `tools/check_tags.py`: 0 unknown source IDs and 0 long untagged paragraphs in all six sections. American spellings reported are proper nouns only ("Trust Center", "Check Point AI Defense Plane", "Business Source License", Presidio's `analyzer` module) or the verb "license" |

## Summary

- **4 criterion-score changes on 4 products**, all in C4 and C5. Totals moved by between -0.05 and +0.20 FS.
  - C4 Okta/Auth0: enterprise readiness 3 → 4 (new reference-documentation evidence for System Log and an AI agent administrator role). FS 3.40 → 3.55.
  - C4 MCP authorisation: ecosystem 5 → 4. FS 3.50 → 3.45.
  - C4 Cedar / AgentCore Policy: security 3 → 4 (AgentCore SOC and ISO evidence already logged by C1 and L4). FS 3.50 → 3.70.
  - C5 Langfuse prompts: enterprise readiness 3 → 4, to match the CP2-reworked L9 Langfuse score. FS 3.70 → 3.85.
- **2 tier changes, both in C4, both down.**
  - **MCP authorisation: Strategic → Tactical** (mandatory wherever MCP is used). A borderline case below 3.6 with a 2 on reliability, resolved against the Anthropic-originated specification under the conflict-of-interest rule. It now matches OpenSSF Model Signing in C7 (an open specification at FS 3.50, Tactical).
  - **Cedar / AgentCore Policy: Strategic, conditional → Tactical** despite rising to FS 3.70. Its managed enforcement is tied to AgentCore Gateway, which C1 rates Tactical, and a policy engine cannot be more strategic than its enforcement point. OPA remains the Strategic, cloud-neutral policy engine.
- **"Every product in a control is Strategic" no longer holds.** C4 goes from 6 of 6 Strategic to 4 of 6. Entra (3.50) and Okta (3.55) remain the only Strategic products below 3.6 FS across C3 to C8, each on a stated condition (question Q1).
- **Caps kept after targeted searches:** watsonx.governance, ValidMind and ModelOp security stay capped at 2, and Prisma AIRS security stays at 3. Each search found no product-scoped attestation, and the negative finding is now logged.
- **Accuracy:** 104 claims spot-checked (at least 14 per section, 27 in C8). 17 text-correction entries, none of which changes a score: OWASP labels, SS1/23 scope wording, a do-not-rely Chinese-vendor price, the LiteLLM intrusion vector, the Promptfoo "now OpenAI-owned" wording, a DORA register precision, and stale ASI02 to ASI10 text in C7. C8 gained three regulatory bullets it lacked: the OWASP 2026 lists, the DORA CTPP and UK CTP designations, and EBA/GL/2026/09.
- **Length:** nothing was shortened. Words (checker count): C3 6,825 → 6,844; C4 7,232 → 7,814; C5 6,903 → 7,013; C6 6,842 → 6,875; C7 8,339 → 8,487; C8 9,863 → 10,175.

## How rules 1 to 9 were read across C3 to C8

1. **Rule 9 (tiers by judgement) and the 3.6 guide.** A Strategic product below 3.6, or with a criterion at 2, needs a stated condition *and* an architectural reason that a peer product in another section would also get.
   - I tested each such case against peers: MCP authorisation against OpenSSF Model Signing (C7) and A2A and Agent Skills (L4); Cedar against C1's AgentCore Gateway; Entra and Okta against L7 Cohere (FS 3.70, Tactical).
   - Two cases failed the peer test (MCP authorisation, Cedar), and two passed with a condition (Entra, Okta).
2. **Rule 7 (partial evidence), applied the L9 way.** All three controls (SSO, RBAC, audit) plus SCIM, an SLA or an admin API reach 4. Okta now meets this, and so does C5 Langfuse, which was still on its pre-rework score.
3. **Rule 8 (certification scope).** AgentCore Policy takes the AgentCore SOC and ISO scope evidence that C1 and L4 already use, held at 4 for the same reasons as in those sections. Prisma AIRS, HiddenLayer, LaunchDarkly, Collibra, Entra and Okta stay one below the anchor.
4. **Rule 1 (NPV cap) and V2 §4.** Credo AI stays capped at 2 because V2 §4 item 9 flags its SOC 2 Type II report. Read strictly, rule 1 treats a flagged claim as NPV. Lakera, Vantage and CloudZero, which have unflagged vendor-stated SOC 2 Type II, score 3.
5. **Rule 2 for patterns and specifications.** Enterprise readiness and security are capped at 4, and 3 is the norm without commercial support. There are two deliberate 4s: the C6 gateway pattern (commercial enterprise editions exist) and C5 prompts-as-code (approval and audit are the control's whole function, delivered by the firm's own source control). The gateway rationale already said so; the prompts-as-code rationale now does.
6. **Rule 3 on patterns.** The writers applied the Acquired flag and a lock-in reduction of 1 to all three patterns because a named example component changed owner: Promptfoo for prompts-as-code, Portkey for gateway cost attribution and ModelScan for scanning. This is consistent across the three sections, so it was kept and raised as Q3.

## (a) Change log

### Scores and tiers

| Section | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| C4 | Okta/Auth0 for AI Agents: enterprise readiness | 3 (CP2 Q2 cap: audit only on a training page) | 4 | Rule 7. Okta reference docs show System Log events for AI agents, a dedicated AI agent administrator role (create, update and delete agents, manage MCP servers, view logs) and the System Log management API. With SSO and the ownership and certification controls already verified, that is all three controls plus an admin API. Not 5: no SLA or agent-specific SCIM. | B-REVB-S001 (new), B-C4-S007 |
| C4 | Okta/Auth0: FS total and tier line | 3.40, Strategic, conditional | 3.55, Strategic, conditional (kept) | Follows the score; still below 3.6, condition unchanged (see Q1) | — |
| C4 | MCP authorisation: ecosystem | 5 | 4 | L4 scores MCP itself 5. For the *authorisation profile*, authorisation is optional and `adoption_signals` is NPV in the dataset; implementations are verified for only four gateways and IdPs | A6-S021, A6-S017, A6-S099, A6-S053; dataset cell NPV |
| C4 | MCP authorisation: tier | Strategic, conditional (FS 3.50, reliability 2) | **Tactical, mandatory wherever MCP is used** (FS 3.45) | Below 3.6 and a 2. The peer case, OpenSSF Model Signing (open specification, FS 3.50, required where firms produce weights), is Tactical. The durable control is the IdP (via EMA) plus the gateway PDP. Borderline, so resolved against the Anthropic-originated specification (CONTEXT §3 rule 5). The disclosure and independent alternatives (Kong, AgentCore Gateway, Azure APIM, plain OAuth 2.0 resource server) were already present and are kept. | rubric rule 9; CONTEXT §3.5 |
| C4 | Cedar / AgentCore Policy: security | 3 ("AgentCore certifications not searched") | 4 | AgentCore is in AWS SOC 1/2/3 scope, where GA features are in scope unless excluded, and in its ISO 27001 programmes. These are the sources C1 and L4 already use, held at 4 for the same reasons (garbled ISO wording, FedRAMP unresolved). | B-C1-S005, B-C1-S006, B-L4-S002 |
| C4 | Cedar / AgentCore Policy: tier | Strategic, conditional (FS 3.50) | **Tactical**, preferred PDP inside an AgentCore estate (FS 3.70) | Managed enforcement is tied to AgentCore Gateway, which C1 rates Tactical (FS 3.00). Reviewer A's in-progress L4 file also now shows AgentCore Gateway and Identity as Tactical (3.45). OPA stays the Strategic default; Cedar source stays portable. | A6-S026; C1 and L4 assessments |
| C5 | Langfuse prompts: enterprise readiness | 3 | 4 | The C5 writer copied the *pre-rework* L9 score. CP2 rework raised L9 Langfuse to 4 under rule 7 (SSO, RBAC, audit, SCIM, Org Management API). The section's own note says the C5 and L9 scores should match. | A7-S074, A1-S033; CP2_rework_log |
| C5 | Prompts-as-code: enterprise readiness rationale | "capped at 4 because no commercial support exists" | Explains why it sits at the rule 2 maximum while OPA, FOCUS and OpenLineage are 3 | The rationale misread rule 2; the score is kept | rubric rule 2 |

### Checked and kept (decision-relevant)

| Section | Item | Kept at | Why | Source |
|---|---|---|---|---|
| C4 | Entra Agent ID tier | Strategic, conditional (FS 3.50; deployment 2, cost 2) | The agent identity must sit in the directory that holds the delegating humans, and no realistic alternative is stronger. Conditions are stated. See Q1. | A6-S057, A6-S059 |
| C3 | Presidio tier | Strategic, conditional (FS 3.65) | Meets the guide and has no criterion at 2. The volunteer-governance risk is already in reliability (3), the limitations and the FS note. See Q4. | A6-S040, V2-S030 |
| C3 | Google SDP security | 4 | The search found only KMS-wrapped *de-identification* keys, not CMEK for the service's stored data. Rule 8's CMK route to 5 is not met. | B-C3-S002; search negative |
| C7 | Prisma AIRS security and tier | 3; Tactical, conditional | The Trust Center lists AIRS only under ENS. No SOC 2 or ISO 27001 product scope was found. See Q5. | B-REVB-S003 (new) |
| C8 | watsonx.governance security | 2 (cap) | No watsonx entry on IBM Cloud's SOC 2 Type 2 or ISO 27001 service lists. The cap rests on that absence of evidence, not on the contradictory FedRAMP page, which is now relied on in neither direction. See Q5. | B-REVB-S002 (new), B-C8-S002 |
| C8 | ValidMind security | 2 (cap) | Only "adherence to ... SOC 2" was found; there is no trust centre and no type. Its SS1/23 mapping is a vendor claim and correctly does not enter the score. Lowest FS (2.90) is consistent with ModelOp (2.95). | B-REVB-S004 (new), A7-S121 |
| C8 | ModelOp security | 2 (cap) | No attestation found. The installs-in-estate claim is a vendor statement. | B-REVB-S005 (new) |
| C8 | Credo AI security | 2 (cap) | Rule 1: V2 §4 item 9 flags its SOC 2 Type II report. Raised in Q5 because unflagged peers with vendor-stated SOC 2 Type II score 3. | V2 §4.9 |
| C5, C6, C7 | Acquired flag and lock-in reduction on patterns | Kept | Consistent across the three patterns. See Q3. | rubric rule 3 |
| C7 | Scanning pattern tier | Strategic (FS 3.60) | Core is "safetensors by default", which has years of production use; reliability 3 blends pre-1.0 scanners with that format | A7-S002, B-C7-S006 |

### Accuracy, do-not-rely and CP1 compliance (text only; no score effect)

| Section | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| C4 (×2), C7 | OWASP LLM 2026 "Excessive Agency ranked third" / "weights rankings against incident data" | `[VF: R-OWASP-LLM, …]` | `[R: …]`, "on a contributor's account" | The dataset labels the 2026 list contents Reported; V2 notes the ranking comes from a contributor quote. The release itself stays VF. | R-OWASP-LLM; V2-S056 |
| C5 (×2), C6 | OWASP 2025 identifiers (LLM07, LLM10) | `[VF: R-OWASP-LLM, A8-S040]` | `[R: A8-S040]`, "for traceability" | Same as the CP2 L7 fix; the 2025 numbering is Reported in the dataset | R-OWASP-LLM stage notes |
| C7 | OWASP Agentic: "the other nine entries were not retrieved" | Stale | ASI02 to ASI08 and ASI10 named from the C4 writer's source; ASI04 to ASI06 mapped to C7's jobs | Cross-section consistency with C4 | B-C4-S005 |
| C3, C4 | SS1/23 scope: "banks and PRA-designated firms" | Imprecise | "Banks, building societies and PRA-designated investment firms with internal-model approval"; the "operative anchor" sentence is split into fact and `[AJ]` | The fact cell states the narrower scope | R-PRA-SS123, A8-S008 |
| C5 | SS1/23 "is binding on…" | "binding" | "applies to …; insurers are not covered" | A supervisory statement sets expectations; the fact cell says "in scope" | A8-S008 |
| C4 | "US supervisory signal is observation-based" tagged `[VF: R-US-AGENCY-AI]` | Judgement tagged as fact | The OCC quotation is `[VF: A8-S004]`; the characterisation is `[AJ]` | Mixed claim; the dataset labels the characterisation as judgement | R-US-AGENCY-AI |
| C6 | Kimi K3 US$3 / US$0.30 tagged `[VF: A5-S069]` | VF | `[R: A5-S069]`, "Reported and not a decision input" | V2 §4.3: Chinese-vendor API prices | V2 §4 |
| C6 | DORA register "reported annually by 31 March from 2026" | Implied the firm reports | Competent authorities report registers to the ESAs annually by 31 March (reference date 31 December) | R-DORA status cell | A8-S021 |
| C7 | Executive summary: LiteLLM credentials "stolen through a compromised Trivy scanner" | Stated as settled | LiteLLM's attribution; other reports describe a hijacked maintainer account. Also aligned in C7.2 and C7.5. | V2 C1-litellm note | V2-S027 |
| C7 | Lock-in table: Promptfoo "now OpenAI-owned" | Implied completion | "OpenAI announced its acquisition on 9 March 2026; closing date not published; Promptfoo states it is part of OpenAI" | V2 §4.7 | V2-S042 |
| C7 | Prisma AIRS certifications | Company-level only | Adds the negative scope finding | New evidence | B-REVB-S003 |
| C8 | watsonx.governance, ValidMind, ModelOp certification bullets | — | Negative findings added; the watsonx text states that the FedRAMP page is relied on in neither direction | New evidence | B-REVB-S002, S004, S005 |
| C8 §11.6 | OWASP 2026 lists absent from the control that "is the regulated-FS lens" | — | New bullet: both 2026 lists, dates and the evidence-pack role | Brief x.11 standards list | R-OWASP-LLM, R-OWASP-AGENTIC |
| C8 §11.7 | DORA CTPP and UK CTP designations absent | — | New bullet: 18 November 2025 list (19 providers) and 13 July 2026 designations; no AI model provider; no governance-tool vendor found | Brief x.11 | R-DORA, R-UK-CTP |
| C8 §11.7 | EBA/GL/2026/09 absent | — | New bullet: finalised 18 September 2026; application date not fixed; two-year review of critical or important arrangements; AI SaaS sits under DORA | Brief x.11 | R-EBA-OUTSOURCING; V2-S054 |
| C4 | Okta deep dive, scoring notes and key facts; MCP and Cedar deep dives; C4.8 table and "Why six Strategic" note | Draft | Updated for the changes above; "Why four Strategic" explains that a given firm adopts at most three Strategic components | Consistency | — |
| C5 | §5.8 table and scoring notes; Langfuse tier line | Draft | Updated | Consistency | — |

### Accuracy spot-checks

Claims were checked against the cited fact cells in `products.json` and `regulatory_facts.json`, by source ID.

| Section | Claims checked | Examples (all matched unless listed under mismatches) | Mismatches found and fixed |
|---|---:|---|---|
| C3 | 15 | Presidio 2.2.364 (22 July 2026), MIT, rebrand in 2.2.363 (28 June 2026), MCR → GHCR, "not guaranteed to find all" warning; SDP SOC 2/ISO 27001 in scope, US$3.00/US$2.00 per GiB, US$2,500 discovery unit, 200+ detectors; Purview DSPM GA May 2026, classic until June 2026, FedRAMP High, E5/Purview Suite with Business Premium as `[R]`; Protegrity AI Team Edition 17 November 2025, Tech Preview, AWS-only (dependency cell), ISO 27001:2013 (2023) and no SOC 2; Skyflow SDK 2.1.3 (4 August 2026), v1 EOL 31 October 2026, US$30m (28 March 2024); DUAA in force 19 June 2026; UK adequacy to 27 December 2031; C-703/25 P pending | SS1/23 scope wording |
| C4 | 17 | Entra Agent ID GA April 2026, Agent 365 in E7 and as an add-on to E5/A5/Business Premium, Entra ID in FedRAMP High; Auth0 for AI Agents GA 19 November 2025, Auth for MCP and OBO GA May 2026; Okta for AI Agents GA 30 April 2026; XAA GA 24 August 2026 in core SSO; SDK "under heavy development"; SPIRE v1.15.3 (21 August 2026); OPA v1.21.1 (29 September 2026), graduated February 2021; Cedar 4.13.0 (15 September 2026); AgentCore Policy GA 3 March 2026, 13 Regions, US$0.000025 per request; MCP 2026-07-28 changes and revision list; AAIF donation 9 December 2025 and Lead Maintainers | OWASP 2026 ranking label; SS1/23 scope; OCC observation tag; stale Okta audit evidence |
| C5 | 14 | Langfuse SDK 4.17.0 (5 October 2026), Enterprise-gated features, regions; ClickHouse announcement 16 January 2026; LangSmith regions and no EU contracting entity; LaunchDarkly GA 28 May 2025, evals 11 March 2026, AgentControl 12 May 2026, pricing, certifications; PromptLayer SDK 1.5.16 (19 August 2026) and Enterprise Identity; Prompty 2.0.2 (16 September 2026); Dotprompt 0.2.0 (5 October 2026); promptfoo 0.124.0 (6 October 2026); Promptfoo "announced" | OWASP 2025 labels; SS1/23 "binding"; Langfuse score parity with L9 |
| C6 | 15 | Helicone → Mintlify 3 March 2026 and maintenance mode; npm last release 7 November 2025; Portkey → Palo Alto Networks 29 May 2026; AI Gateway GA 16 July 2026; LiteLLM 1.104.1; Portkey SDK 2.3.4; LiteLLM incident window (40 minutes or 3 hours); FOCUS 1.4 (4 June 2026); FOCUS 1.5 scope with the token-type column deferred (V2-S046); six releases since v0.5; CC BY 4.0; Claude and OpenAI list prices and modifiers (A5-S011, A5-S004) | Kimi K3 price (do-not-rely); OWASP 2025 label; DORA register wording |
| C7 | 16 | Lakera completion 22 October 2025 (no press value); Protect AI 22 July 2025; CalypsoAI US$145.2m (10-Q) and Portkey US$117m (10-K), both filing figures; Prisma AIRS 3.0 (23 March 2026), Koi (14 April 2026); HiddenLayer Series B (2 September 2026, US$100m) and certifications (13 February 2025); Vault agentic IAM GA 1 September 2026, 2.1.1/2.1.2 caveat present, BUSL, IBM 27 February 2025; scanner versions; model-signing 1.1.1; CTPP and UK CTP dates | LiteLLM vector; Promptfoo "now OpenAI-owned"; OWASP 2026 label; stale ASI list |
| C8 | 27 | See the regulatory precision table below; plus ValidMind Library 2.13.14 (3 September 2026); Credo Lens 1.1.8 (May 2023); watsonx AI Asset Discovery (9 July 2026) and Enforcement Tracking (11 August 2026), pricing; Collibra trail ML (5 October 2026, price undisclosed) and certification list; OpenLineage 1.53.0, Marquez 0.51.1, Airflow provider 2.20.2 | Missing OWASP, CTPP/CTP and EBA bullets (added) |

### C8 regulatory precision (each against `regulatory_facts.json`)

| Statement in C8 | Record and sources | Result |
|---|---|---|
| SR 26-2, OCC 2026-13 and FIL-15-2026 issued 17 April 2026; supersede SR 11-7 and SR 21-8; OCC rescissions | R-US-MRM; A8-S001, S002, S005, V2-S049 | Match |
| Non-enforceable guidance; most relevant above US$30bn total assets | R-US-MRM; A8-S002, S003 | Match |
| GenAI and agentic AI expressly out of scope; the firm's own practices govern them; RFI planned and not published by 7 October 2026 | R-US-MRM; A8-S001, S002, S003, S007 | Match |
| SR 26-2 model definition quotation | R-US-MRM key_obligations | Match |
| SS1/23 published 17 May 2023, effective 17 May 2024; scope (internal-model firms; insurers not covered); later narrowing | R-PRA-SS123; A8-S008, S061 | Match |
| SS1/23 five principles; SMF holder; audit-committee reporting; definition fragment and Principle 1.1(b) | R-PRA-SS123; A8-S008, S037, S061 | Match (the definition fragment is quoted only as far as it was extracted) |
| EU AI Act in force 1 August 2024 `[R]`; prohibitions and literacy 2 February 2025; GPAI 2 August 2025; enforcement powers and fines 2 August 2026; legacy GPAI 2 August 2027 | R-EUAIA; A8-S011, S012, S019 | Match; the entry-into-force date is correctly Reported |
| Regulation (EU) 2026/1744: OJ 24 July 2026, in force 27 July 2026; Annex III 2 December 2027; Annex I 2 August 2028 | R-EU-OMNIBUS-AI; A8-S011, V2-S050 | Match |
| Article 4 wording (as amended) and enforcement from 2 August 2026 | R-EUAIA; A8-S060 | Match, verbatim |
| Article 26 duties incl. six-month logs and financial-institution carve-in; Articles 12, 25, 27 and 72; 72(3) template power removed | R-EUAIA; A8-S016, S017, S011 | Match |
| Article 50 from 2 August 2026; 50(2) grace period to 2 December 2026 | R-EUAIA; A8-S018, V2-S078 | Match |
| Annex III 4(a)/(b), 5(b) (fraud excluded), 5(c) | R-EUAIA key_obligations | Match |
| GPAI Code of Practice 10 July 2025; named signatories; Anthropic disclosure | R-EU-GPAI-COP; A8-S015, S035 | Match |
| IOSCO FR/02/2026 (25 May 2026) indicators; ESMA 30 May 2024; joint ESMA–EBA consultation 25 February 2026 | R-INTL-AI-ASSETMGMT; A8-S058, S059, V2-S077 | Match |
| FCA has no AI-specific rules; FPC March 2026; 55% / 2% BoE analysis | R-UK-AI-STATEMENTS; A8-S055, S056 | Match |
| SEC PDA withdrawn by Commission action 12 June 2025 | R-SEC-ADVISERS; A8-S057, V2-S058 | Match (V2 correction applied) |
| NIST AI RMF 1.0 under revision, none published; AI 600-1 26 July 2024; function names `[R]`; "Super Intelligence" naming | R-NIST-AIRMF; A8-S043, S044, V2-S060 | Match |
| ISO/IEC 42001:2023, 42005:2025, 42006:2025 (7 July 2025) | R-ISO-42001; A8-S045, S046, S047, V2-S057 | Match |
| PS7/26 and PS26/2 notifications from 18 March 2027 | R-PRA-SS221, R-FCA-SYSC8; A8-S062, V2-S053 | Match |
| EU-UK adequacy to 27 December 2031; C-703/25 P pending | R-DATA-TRANSFERS; A8-S052, S053, V2-S055, V2-S059 | Match |
| DORA CTPP (18 November 2025), UK CTP (13 July 2026), EBA/GL/2026/09, OWASP 2026 lists | R-DORA, R-UK-CTP, R-EBA-OUTSOURCING, R-OWASP-LLM, R-OWASP-AGENTIC | **Absent from C8; added** with these record IDs |

### Do-not-rely enforcement (V1 and V2 §4)

| Item | Status across C3 to C8 |
|---|---|
| Deal values: filing figures only | Portkey US$117m (10-K) and CalypsoAI US$145.2m (10-Q) only; Lakera "press values not used"; trail ML "price undisclosed"; no Koi or Lakera press figures |
| Promptfoo "announced" | C5 and C8 correct; C7 lock-in row fixed |
| FOCUS 1.5 token column deferred | C6 correct throughout (V2-S046) |
| Vault 2.1.1 vs 2.1.2 caveat | C7 carries it; C4 cites only "GA in Vault Enterprise 2.1" |
| Helicone → Mintlify | C6 correct (acquired 3 March 2026, maintenance mode) |
| Chinese-vendor prices | C6 Kimi K3 relabelled `[R]` and marked not a decision input |
| Credo AI SOC 2 report date | Not relied on; cap kept (C8) |
| UK CTP self-assessment date; vendor benchmarks; D.C. Circuit scope; SpaceXAI | Not used in C3 to C8 |
| CP1 decisions (SR 26-2 carve-out, Annex III 2 December 2027, no model-vendor CTPP, PS7/26 18 March 2027, OWASP 2026 operative) | Applied in all six sections; every failure story is one "Illustrative scenario [AJ]" in x.2 |

## (b) Calibrated score tables (`tools/score.py` output after this review)

### C3
| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C3-presidio | 3 | 3 | 3 | 5 | 3 | 3 | 4 | 5 | 3.50 | 3.65 | Strategic |
| C3-google-sdp | 5 | 4 | 4 | 2 | 4 | 5 | 3 | 2 | 3.80 | 3.60 | Strategic |
| C3-microsoft-purview-dspm-ai | 3 | 4 | 4 | 2 | 4 | 3 | 2 | 2 | 3.10 | 3.05 | Tactical |
| C3-protegrity | 4 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2.90 | 2.75 | Tactical |
| C3-skyflow | 4 | 3 | 4 | 2 | 3 | 3 | 2 | 2 | 3.05 | 3.00 | Tactical |

### C4
| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C4-entra-agent-id | 5 | 4 | 4 | 2 | 4 | 3 | 2 | 3 | 3.55 | 3.50 | Strategic |
| C4-okta-auth0-ai-agents | 5 | 4 | 4 | 2 | 4 | 3 | 3 | 3 | 3.65 | 3.55 | Strategic |
| C4-spiffe-spire | 3 | 3 | 4 | 5 | 4 | 5 | 3 | 5 | 3.85 | 4.05 | Strategic |
| C4-mcp-authorization | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 4 | 3.50 | 3.45 | Tactical |
| C4-opa | 4 | 3 | 4 | 5 | 5 | 4 | 4 | 5 | 4.15 | 4.20 | Strategic |
| C4-cedar | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 3.75 | 3.70 | Tactical |

### C5
| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C5-langfuse-prompts | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3.95 | 3.85 | Strategic |
| C5-langsmith-prompts | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 3 | 4.00 | 3.95 | Strategic |
| C5-promptlayer | 4 | 4 | 3 | 4 | 3 | 3 | 2 | 3 | 3.40 | 3.40 | Tactical |
| C5-launchdarkly-ai-configs | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Tactical |
| C5-prompts-as-code | 3 | 4 | 3 | 5 | 3 | 3 | 4 | 4 | 3.60 | 3.65 | Strategic |

### C6
| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C6-gateway-cost-attribution | 4 | 4 | 3 | 5 | 4 | 3 | 4 | 3 | 3.85 | 3.70 | Strategic |
| C6-helicone | 3 | 2 | 2 | 3 | 3 | 1 | 4 | 3 | 2.60 | 2.50 | Experimental |
| C6-vantage | 3 | 3 | 3 | 2 | 4 | 3 | 3 | 3 | 2.95 | 2.90 | Tactical |
| C6-cloudzero | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2.70 | 2.65 | Tactical |
| C6-finops-focus | 3 | 3 | 3 | 5 | 4 | 4 | 5 | 5 | 3.80 | 3.85 | Strategic |

### C7
| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C7-lakera | 3 | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 3.10 | 3.00 | Tactical |
| C7-prisma-airs | 5 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.60 | 3.35 | Tactical |
| C7-hiddenlayer | 4 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3.10 | 3.10 | Tactical |
| C7-hashicorp-vault | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 3.80 | 3.65 | Strategic |
| C7-model-supply-chain-scanning | 3 | 3 | 3 | 5 | 4 | 3 | 5 | 4 | 3.65 | 3.60 | Strategic |
| C7-openssf-model-signing | 3 | 3 | 3 | 4 | 2 | 3 | 5 | 5 | 3.35 | 3.50 | Tactical |

### C8
| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C8-validmind | 4 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2.95 | 2.90 | Tactical |
| C8-credo-ai | 3 | 4 | 2 | 5 | 4 | 3 | 2 | 3 | 3.30 | 3.25 | Tactical |
| C8-watsonx-governance | 5 | 3 | 2 | 4 | 4 | 4 | 3 | 3 | 3.60 | 3.40 | Tactical |
| C8-modelop | 4 | 3 | 2 | 4 | 3 | 2 | 2 | 3 | 3.00 | 2.95 | Tactical |
| C8-collibra-ai-governance | 4 | 3 | 4 | 2 | 4 | 3 | 2 | 3 | 3.20 | 3.20 | Tactical |
| C8-openlineage | 3 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 3.80 | 3.85 | Strategic |

### Tier distribution

| Control | Strategic | Tactical | Experimental | Change from writers' drafts |
|---|---:|---:|---:|---|
| C3 | 2 | 3 | 0 | none |
| C4 | 4 | 2 | 0 | MCP authorisation and Cedar moved from Strategic to Tactical |
| C5 | 3 | 2 | 0 | none |
| C6 | 2 | 2 | 1 | none |
| C7 | 2 | 4 | 0 | none |
| C8 | 1 | 5 | 0 | none |
| **Total** | **14** | **18** | **1** | 33 products |

**Strategic entries below FS 3.6:** Entra Agent ID (3.50) and Okta/Auth0 (3.55). Both are conditional on being the workforce IdP (Q1).

**Rubric rule 5 (a 2 or lower in each control):** satisfied in every control. In C4 only OPA has no criterion below 3.

## (c) Cross-section observations

1. **Where the Strategic slots go.** Of the 14 Strategic entries in C3 to C8, eight are open-source projects, open specifications or patterns: Presidio, SPIFFE/SPIRE, OPA, prompts-as-code, gateway cost attribution, FOCUS, the scanning pattern and OpenLineage. Three are L9 platforms reused as registries (Langfuse, LangSmith) or a hyperscaler service (Google SDP). The rest are the two IdPs and Vault. No commercial product in C6, C7 (other than Vault) or C8 is Strategic. As in CP2 observation (c)1, the FS weights (15% deployment, 15% lock-in) drive this as much as the evidence does [AJ].
2. **Controls are mostly "design plus a replaceable tool".** C5, C6 and C8 each conclude that the record of truth must be firm-owned: Git, a FOCUS-shaped dataset and an evidence store. Their Strategic entries are the pattern or standard, and the commercial tools are Tactical. That is coherent, but it makes the tier tables read as "build, don't buy" for half the controls. The synthesis should say so explicitly rather than leave it to the tables [AJ].
3. **Evidence asymmetry persists.** The three C8 platforms capped on security (watsonx.governance, ValidMind, ModelOp), plus Credo AI under rule 1, are capped for missing public attestations, not for known weaknesses. A due-diligence request would likely move one or two of them. watsonx.governance would reach FS 3.60 to 3.80 with product-scoped SOC 2 or ISO, which would put it at or over the Strategic guide (Q5) [AJ].
4. **Cross-reviewer consistency points for the human (reviewer A's files, read-only here).**
   - **MCP.** L4 MCP (currently FS 3.55, Strategic, in reviewer A's in-progress file) and C4 MCP authorisation (now Tactical) differ in tier. The difference is defensible: the protocol is the de facto standard (ecosystem 5), while the authorisation profile is optional and draft-dependent. But the two should be presented together in synthesis.
   - **AgentCore.** C1 AgentCore Gateway is Tactical (3.00), and reviewer A's L4 AgentCore Gateway and Identity now also reads Tactical (3.45). The C4 Cedar change aligns with both. If reviewer A restores L4 to Strategic, Cedar's tier should be revisited with it.
   - **IBM concentration.** It is noted in both C7 (Vault) and C8 (watsonx.governance).
   - **Palo Alto Networks.** Its gateway (Portkey, C1) and its security platform (Prisma AIRS, C7) are cross-referenced consistently.
5. **`work/stageB/_review/all_scores.md` is now stale** for C4 and C5, and probably for reviewer A's sections. Regenerate it after both reviews, and re-run `tools/build_dataset.py` to propagate scores and the B-REVA and B-REVB sources.

## (d) Calibration questions for the human

**Q1. Entra Agent ID (FS 3.50) and Okta/Auth0 (FS 3.55): Strategic below the 3.6 guide?** Both score 2 on deployment because they are SaaS-only identity planes, and Entra also scores 2 on cost (Agent 365 licensing).
- **(a) Keep both Strategic, conditional (as now).** The agent identity must live in the directory that holds the delegating humans, so for a given firm one of them is unavoidable. This is the only place in C3 to C8 where Strategic sits below 3.6.
- **(b) Make both Tactical, and make "agent identities in the workforce IdP" the Strategic pattern.** The products become implementations of a pattern, as in C5, C6 and C7. This gives a cleaner rule, "no product below 3.6 is Strategic", at the cost of naming no Strategic IdP product.
- **(c) Keep Entra Strategic and make Okta Tactical**, or the reverse. Not recommended: the two differ by 0.05 FS and the condition is symmetric.

**Q2. MCP authorisation (FS 3.45, reliability 2) and Cedar/AgentCore Policy (FS 3.70): tiers set by enforcement point and conflict of interest.**
- **(a) As changed in this review.** MCP authorisation is Tactical but mandatory wherever MCP is used; the borderline call was resolved against the Anthropic-originated specification, and it matches OpenSSF Model Signing. Cedar is Tactical because its managed enforcement point (AgentCore Gateway) is Tactical in C1.
- **(b) Restore the writer's conditional Strategic for both.** "Strategic only where MCP is the tool protocol" and "only in an AgentCore estate". This restores C4 to 6 of 6 Strategic, and Cedar would then be the only Strategic component bound to a Tactical gateway.
- **(c) Split them.** Make MCP authorisation Strategic, conditional (if L4 MCP stays Strategic, treat the protocol and its authorisation profile as one decision) and keep Cedar Tactical.

**Q3. How should patterns and standards be tiered against products?** Prompts-as-code (FS 3.65), gateway cost attribution (3.70), the scanning pattern (3.60), FOCUS (3.85) and OpenLineage (3.85) are Strategic, while all commercial C6 and C8 tools are Tactical. The three patterns also carry an Acquired flag and a lock-in reduction because one example component changed owner (Promptfoo, Portkey, ModelScan).
- **(a) As now.** Patterns and standards are scored and tiered like products under rule 2, and rule 3 applies when a named component changed owner.
- **(b) Same tiers, but drop the Acquired flag and lock-in reduction on patterns** where the component is replaceable, and put the ownership note in the rationale. Each pattern gains +0.15 FS; no tier changes.
- **(c) Take patterns out of the product scorecards.** Present them as "required design" in x.5 and x.9, and score only products. C5, C6 and C8 would then have no Strategic product, and C7 only Vault.

**Q4. Presidio (FS 3.65): Strategic, conditional, with volunteer governance since June 2026?** It is MIT, in-estate and recall-testable, but it has no commercial support, its governance is new (a Technical Steering Committee of volunteers) and signed releases are not verified.
- **(a) Keep Strategic, conditional** as the in-estate engine behind a firm-owned privacy-service API, with recall tests in CI and a second detector on samples (as now).
- **(b) Make it Tactical** until the new governance shows a year of releases and security handling. Google SDP would then be C3's only Strategic engine, and only in Google Cloud estates.
- **(c) Keep it Strategic and require a firm fork-and-maintain plan** (pinned versions, internal mirror, named owner) as a stated condition.

**Q5. How should controls capped only by missing product-scoped certification be treated?** This covers watsonx.governance (security 2, FS 3.40; the FedRAMP page contradicts itself and is relied on in neither direction), Prisma AIRS (security 3, FS 3.35, "Strategic candidate in Palo Alto estates"), and ValidMind and Credo AI (security 2; ValidMind is the only SS1/23 claimant; Credo AI's SOC 2 report is flagged in V2 §4).
- **(a) As now.** Keep the caps and Tactical tiers, with "candidate for Strategic after due diligence" conditions on watsonx.governance and Prisma AIRS. Vendor regulatory mappings, such as ValidMind's SS1/23 claim, never enter the score.
- **(b) Treat these as due-diligence items rather than caps.** For platforms whose vendors share SOC 2 reports under NDA, score at the anchor minus one (3). watsonx.governance would move to 3.60 and become Strategic, conditional; ValidMind and Credo AI would move to about 3.10 and 3.45.
- **(c) Stricter.** Drop the "candidate for Strategic" wording entirely until a report has been read (MEMORY B4: no audit report has been read for any product).

## Files changed

- `work/stageB/C3/section.md`, `C4/section.md`, `C5/section.md`, `C6/section.md`, `C7/section.md`, `C8/section.md`
- `work/stageB/C4/assessments.json`, `work/stageB/C5/assessments.json` (scores, rationales, caps, classification, assessment prose; totals rewritten by `tools/score.py --write`). C3, C6, C7 and C8 were re-run through `score.py --write` with no value change.
- `work/stageB/_review/sources_added_B.csv` (new: B-REVB-S001 to S005)
- `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/B-REVB-S001.extract.txt` … `B-REVB-S005.extract.txt`
- `work/stageB/_review/CP3_review_B.md` (this file)

**Not run or not changed:**
- `tools/build_dataset.py` was not run; re-run it after both reviews.
- `all_scores.md` and `MEMORY.md` were not changed.
- No commit or push was made. One read-only `git status` was run by mistake while checking files.
