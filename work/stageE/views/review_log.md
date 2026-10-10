# Stage E independent review log (views TS, SW, SU, AT, DV, AG)

**Reviewer:** independent Stage E reviewer. **Date:** 10 October 2026.

**Scope.** The six view Parts (`work/stageE/views/<VIEW>/view.md`) were checked against:

- the brief `work/stage0/11_stageE_views_brief.md`, including its "Vendor views" section for AT, DV and AG;
- the evidence: `05_Data/products.json`, `05_Data/regulatory_facts.json`, `05_Data/views.json`, `work/stageE/E1_regulation`, `work/stageE/E2_commercial` and `work/stageE/E3_agents_sdlc`;
- the per-view score files (`<VIEW>_scores.md`) and the FS synthesis (`work/stageC/synthesis.md`).

**Method.**

- Each `[VF]`/`[R]` claim in the sample was traced to its source row in `sources.csv` and to the fact cells that cite it (dataset records, E3 landscape records, E1/E2/E3 briefs).
- Every regulatory date in each view was checked against `regulatory_facts.json` and the E1 brief.
- Scores, ranks, fit changes and core-candidate counts were recomputed from `05_Data/views.json`.
- Tables were checked by script for L1 → L9 then C1 → C8 order, weekday names and American spellings.
- Each `<VIEW>-1.png` figure was opened and read.

Edits are minimal and keep their tags. No other file was changed. `python3 -I tools/check_tags.py . <file>` is clean on all six files after the edits.

## Edits

| View | Section | Before | After | Reason |
|---|---|---|---|---|
| TS | XIII.2 finding 5 | "Shared prefix caches and tiered KV stores can carry one request's context into another's [VF: A4-S091, A4-S090, A4-S089]" | "Prefix-cache-aware routing and tiered KV-cache stores are now standard in serving stacks [VF: A4-S091, A4-S090, A4-S089], and a cache shared across tenants can carry one request's context into another's [AJ]" | The three sources (LMCache, Dynamo and llm-d READMEs) describe KV-cache features. None reports cross-request leakage, so the leakage point is the author's judgement and is now tagged [AJ]. |
| TS | XIII.6 regulation table, Article 50 row, Date column | "2 Dec 2026" | "Since 2 Aug 2026; marking for systems already on the market by 2 Dec 2026" | Article 50 has applied since 2 August 2026. 2 December 2026 is only the marking grace period for systems already on the market (R-EUAIA, R-EU-OMNIBUS-AI). |
| TS | XIII.8 lock-in | "the Fable 5 outage [VF: V2-S004]" | "the suspension of Fable 5 access from 12 June to 1 July 2026 [VF: V2-S004]" | The dataset records an access suspension (L1-anthropic), not an outage. The wording now matches the source and the dates. |
| SW | XIV.3 what moves | "Managed single-cloud services with deployment 2 fall by 0.15" | "Managed single-cloud or API-only services with deployment 2 fall by 0.15" | OpenAI embeddings, one of the four named, is an API service, not a single-cloud service. The scores are correct. |
| SU | XV.2 finding 9 | "Langfuse, Promptfoo and Helicone all changed owner in 2026 [VF: A1-S021, A1-S024, A7-S112]" | "Langfuse and Helicone changed owner in 2026, and OpenAI announced its acquisition of Promptfoo, with no closing published [VF: A1-S021, A7-S112, A1-S024]" | Promptfoo's sale is announced but not closed (L9-promptfoo; synthesis Part I finding 2). |
| SU | XV.8 lock-in table | "Four neutral tools changed owner in 2026" | "Three neutral tools changed owner in 2026 and a fourth's sale was announced" | Same reason as the row above. |
| SU | XV.8 multi-vendor | "A three-week Fable 5 outage" | "The suspension of Fable 5 access from 12 June to 1 July 2026" | Suspension, not outage (V2-S004). This also aligns SU with TS and DV. |
| SU | XV.6 United States | "consequential decisions about individuals [VF: R-US-STATE-AI] [AJ]" | "consequential decisions about individuals (R-US-STATE-AI) [AJ]" | The E1 brief tags this generalisation [AJ]. The record supports Colorado's scope, not a statement about state laws in general, so the extra [VF] over-claimed. |
| SU | XV.11 monitor table, last row | "The agentic-SDLC evidence (Stage E, E3), not yet available … when published … [NPV]" | "Guidance on coding agents for the start-up's own engineering; the E3 research found no NIST or CISA guidance specific to AI coding assistants [NPV] \| Apply the E3 evidence (Part XVII covers the vendor side) and adopt guidance when published" | The row was stale: E3 is now available (facts dated 10 October 2026). The NPV now names the actual gap that E3 records. |
| AT | XVI.5 integration contract, C4 row | "MCP Enterprise-Managed Authorization where agents call it" | adds "(Anthropic-originated; alternative OAuth 2.0 on an OpenAPI interface)" | Conflict-of-interest rule: an independent alternative beside each Anthropic-originated standard recommended in a row. |
| DV | XVII.2 finding 6 | "…which also owns xAI, and Grok 4.5 was trained alongside Cursor [VF: E3-S029, V2-S011]" | "…which also owns xAI [VF: E3-S029, V2-S011]; Grok 4.5 was reportedly trained alongside Cursor, per SpaceX filings read only through a search summary [R: E3-S029]" | E3 records the SpaceX SEC filings as not read directly (sec.gov blocked; NPV list). The joint-training claim rests on them, so it is now reported, not verified. |
| DV | XVII.3 how to read the fit | "E2B stays situational on enterprise readiness 2" | "E2B stays situational (3.45, below the 3.6 threshold; enterprise readiness 2)" | The fit rule demotes on the score threshold or on a criterion at 1. E2B is situational because 3.45 < 3.6, not because of a 2. |
| DV | XVII.5 integration table, L4 row | "MCP server under managed allow-lists" | adds "(alternative: OpenAPI tools behind the same gateway)" | Conflict-of-interest rule (alternative in the same row). |
| DV | XVII.7 reference stack, L4 row | "Agent Skills (T) optional" | "Agent Skills (T; Anthropic-maintained, alternative AGENTS.md or C5 packages) optional" | Conflict-of-interest rule. The alternative matches synthesis XI.3. |
| DV | XVII.7 reference stack, C4 row | "MCP Authorization (S, cond.)" | "MCP Authorization (S, cond.; alternative OAuth resource-server pattern on OpenAPI tools)" | Conflict-of-interest rule. The alternative matches synthesis XI.1. |
| DV | XVII.8 lock-in | "the Fable 5 outage ran from 12 June to 1 July 2026" | "Fable 5 access was suspended from 12 June to 1 July 2026" | Suspension, not outage (V2-S004). |
| DV | XVII.8 incumbents table, Cursor row | "Joint training with SpaceX/xAI [VF: E3-S029]" | "Joint training with SpaceX/xAI reported [R: E3-S029]" | Same reason as finding 6. |
| AG | XVIII.5 integration table, C4 row | "EMA for MCP tools" | adds "(Anthropic-originated; alternative OAuth 2.0 resource servers on OpenAPI tools)" | Conflict-of-interest rule. |
| AG | XVIII.9 roadmap | "Article 50(2) marking deadline" | "Article 50(2) marking grace period ends for systems already on the market; a new launch has none" | 2 December 2026 is a grace-period end for systems already on the market, not a general deadline (R-EUAIA). |

**Edits per view:** TS 3 · SW 1 · SU 5 · AT 1 · DV 7 · AG 2 (19 in total).

## What was sampled, per view

**All views.**

- *Regulatory dates:* every date was checked against R-EU-CRA, R-EU-PLD, R-EU-NIS2, R-EU-DATA-ACT, R-EU-AIA-ROLES, R-EUAIA/R-EU-OMNIBUS-AI, R-US-STATE-AI, R-UK-SOFTWARE, R-PRA-SS221 and R-DORA. The dates are:
  - CRA reporting from 11 Sep 2026, main obligations from 11 Dec 2027;
  - PLD from 9 Dec 2026;
  - Data Act from 12 Jan 2027;
  - Article 50 marking grace to 2 Dec 2026;
  - Annex III from 2 Dec 2027;
  - CPPA ADMT and Colorado from 1 Jan 2027 (Colorado stayed);
  - UK notifications from 18 Mar 2027;
  - the UK CS&R Bill still before the Lords.

  Apart from the two Article 50 framings fixed above, all are correct.
- *Scoring:* the weights match `views.json`. Each core-candidate count (TS 48, SW 48, SU 57, AT 56, DV 63, AG 56, against FS 45 of 138) and each list of fit changes was recomputed and matches.
- *Layer order:* every L/C table is in order.
- *Spelling and weekdays:* no weekday is named and no American spellings were found ("Authorization" appears only in proper names).

**TS (about 45 claims).**

- *Commercial terms:* E2-S004/S005/S026/S007/S030; capacity tiers E2-S031/S006/S017/S033/S032; V2-S004.
- *Pricing:* A5-S004/S011/S027/S075, V2-S002, A2-S087, A6-S067.
- *Isolation guidance:* E2-S015/S016/S050/S051/S053.
- *Product facts:* A2-S103, A6-S025, A6-S099, A7-S072, A6-S008, A7-S070, A6-S015, B-L4-S007, B-L5-S001, A1-S048, A1-S024, A1-S045, A1-S021, A6-S011, V1-S059, A7-S112, A4-S006, B-REVC-S001, B-C6-S004/S005, B-L1-S003, V2-S010.
- *Assurance:* A5-S021, A5-S007, V2-S062, A5-S028, A8-S045, E2-S046/S048/S047.
- *Other checks:* the worked-example arithmetic (US$0.016 and US$0.010) is correct.

**SW (about 50 claims).**

- *Licences:* A2-S132, A2-S137, A7-S060, A2-S024, A4-S145, A2-S050, V1-S021, A1-S048, A1-S008, A1-S011, A1-S051, A1-S052, A6-S001, A6-S030/S038, A3-S058, A7-S008/S065, A7-S096, A6-S088, A6-S045, A1-S050, A1-S056, A5-S069/S071, A7-S003, A2-S041, A6-S017, A3-S005, A2-S020, A4-S092.
- *Model lifecycle and routes:* B-L1-S001/S002/S003, A5-S010, A5-S032, A3-S055, A6-S049/S063, A4-S010, B-L2-S005/S006/S008, A1-S135, A7-S024, E2-S001/S002/S034/S036/S020/S038.
- *Regulation:* E1 CRA, PLD, AI Act and UK claims.
- *Other checks:* rank movements (L1, L6, L7, L9, C7) match `SW_scores.md`.

**SU (about 45 claims).**

- *Credits:* E2-S008/S009/S010/S011/S042/S044/S045.
- *Pricing:* A4-S144, A6-S052, A6-S007, A1-S047/S031/S123, A4-S135, A3-S104, A2-S001, A2-S007, A1-S116, A6-S098, A7-S074, A7-S103.
- *Product facts:* A2-S044/S143, A4-S055, A4-S123, A4-S054, A4-S005.
- *Regulation and transfers:* A8-S018, A8-S053, E1 US-state and AI Act SME claims (E1-S029–S047).
- *Other checks:* the movers and overrides match `SU_scores.md` (16 up, 4 down). The cost example (about US$4.50 and US$2.30) recomputes correctly.

**AT (about 50 claims; also checked against the vendor-view rules).**

- *Gateway hooks:* A6-S015/S016/S017/S020/S024.
- *Ownership events:* A1-S045, V1-S005, A1-S021, V2-S041, A1-S024, A7-S014/S012/S016/S017/S032, A6-S011/S012/S028, V2-S025/S029/S036/S047/S048, A2-S018/S023/S033, A1-S131, A1-S028/S038, A7-S101.
- *Integration contract evidence:* A6-S036, A1-S094/S096, A1-S059, V2-S046, A6-S065, A6-S068.
- *Standards and incumbent controls:* E3-S004/S010/S011/S026/S032/S066–S069/S073.
- *Commercial and regulatory:* E2-S035/S047/S049/S052/S053; E1 DORA, CRA and PLD claims.
- *Vendor-view structure:* section 5 is an L1 → L9, C1 → C8 integration contract; section 6 is buyer questions; section 7 is the start-up's own stack; section 8 covers incumbents.
- *Other checks:* the component table scores and ranks match `views.json`.

**DV (about 55 claims; also checked against E3 and the vendor-view rules).**

- *E3 sources:* nearly every cited ID, E3-S001 to S082, including the landscape records in `E3_agents_sdlc/products.json` (Copilot, Cursor, Claude Code, Codex, Google, Kiro, Devin, Junie, Amp, Tabnine).
- *Other sources:* A4-S063, A3-S062, E2-S031/S032/S019, V2-S002, A5-S004.
- *Other checks:* the GHES claim for Claude Code cloud sessions is supported by the E3 record (DV-claude-code.ecosystem). The cost example (US$0.024 per call, US$4.70 against US$18) is correct. The scores and the 20-up, 2-down fit changes match.

**AG (about 45 claims; also checked against E3 and the vendor-view rules).**

- *Identity and agent standards:* V2-S032/S035, A6-S100/S026/S058/S060/S076/S078/S079/S099, A3-S017/S019/S020/S042/S045/S055/S056/S078/S016, E3-S065/S072/S073/S075.
- *Platforms and marketplaces:* E2-S021/S035/S037/S039/S040/S041, A4-S055/S116/S123, B-L3-S006, A1-S035, A8-S004, A7-S033.
- *Other checks:* the cost example (US$0.022 per exception, US$440 a month) is correct. The scores and fit changes (12 up, 1 down) match.

**Consistency with the FS synthesis and between views.**

- The Anthropic tier condition and its alternatives (GPT-6.1 Sol, Gemini 3.8 Flash, Mistral Medium 3.5) are quoted identically in all six views.
- The ownership events agree with synthesis Part I finding 2. The Promptfoo wording is now "announced" everywhere.
- The Fable 5 event is now described as an access suspension in all views.
- The master tiers quoted in the views match synthesis Part XI.

## Figures (`08_Graphic/diagrams/<VIEW>-1.png`)

- **TS-1, SW-1, AT-1, DV-1:** legible at page width. Labels are readable and the plane grouping is clear.
- **SU-1:** legible. Two group labels ("The product: one codebase…", "L1 / L2 models…") are crossed by edges.
- **AG-1:** the least legible. It is a wide landscape figure and its node text is small once scaled to page width. Two edge labels ("opt-in health metadata only", "marketplace or private offer") sit on top of each other. The "Behind the customer's gateways" label is crossed by an edge.

All figures carry the "VEYAN · THE VIEW AT END OF Q3 2026" kicker as text. None shows the V-and-eye icon of the full lockup. Figures were not edited (out of scope for this review).

## Open questions for the reader

1. **Length.** AT runs to about 8,650 words, against the brief's 5,000–7,000. DV (about 7,020) and AG (about 7,030) are now just over 7,000 after the alternatives were added. Should AT be cut (for example, the incumbent table in XVI.8 or the category map in XVI.5), or should the vendor views get a higher limit?
2. **AG-1 legibility.** Should AG-1 be re-laid out top-to-bottom, like DV-1, with the overlapping edge labels separated? Should SU-1's crossed group labels also be fixed? This needs an edit to the Mermaid sources, which are outside this review's remit.
3. **Brand lockup in figures.** The view figures show the Veyan word mark as a text kicker, without the V-and-eye icon that the house convention requires for the full lockup. Is the kicker acceptable for diagrams, or should the renderer add the icon?
4. **TS-1 vs text.** The TS text defines three tenancy tiers (pooled, bridged, siloed), but TS-1 shows only pooled and siloed. TS-1 also places C2/C3 after C1 in the flow, while the worked example puts the privacy service "before the gateway". Should the figure be aligned?
5. **SW-1 placement.** SW-1 places the bundled vLLM route inside "Customer's own control plane". It shows "Guard, AI disclosure and output marking" before the model adapter in the flow. Is that the intended reading?
6. **Cursor–Grok joint training.** The E3 landscape record labels this "Verified fact" against E3-S029, but the E3 brief's NPV list says the SpaceX filings were not read directly. I downgraded it to [R] in DV. Should the E3 record's label be aligned (an E3 edit, not made here)?
7. **"Most state AI laws" generalisation.** SU now tags it [AJ], following E1. AT (XVI.6) and the TS table carry similar wording backed only by the Colorado and California records. They are left as they are because they are tagged [AJ] or limited to named states. Confirm this is acceptable.
8. **Gemma 4 tier notation.** AG writes "Gemma 4 (S, cond.)"; the other views write "(S)". Both are defensible, since synthesis XI.1 gives Gemma a condition ("small, self-hosted open-weight tier"). Pick one form for the book.
