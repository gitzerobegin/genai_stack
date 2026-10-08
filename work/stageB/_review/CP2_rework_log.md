# CP2 rework log: layers 9, 8 and 7

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Scope** | `work/stageB/L9`, `L8`, `L7`: `section.md` and `assessments.json` |
| **Basis** | `checkpoints/CP2/03_CP2_Decisions.md` (Q1 to Q6); rubric rules 6 to 9 in `work/stage0/08_scoring_rubric.md` |
| **New sources** | 1: `B-REV-S028` (MongoDB Docs, Voyage model API keys and Atlas roles), a search-tool extract because the direct fetch failed at the proxy. Archived at `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/B-REV-S028.extract.txt` and logged in `work/stageB/_review/sources_added.csv` |
| **Research budget** | 1 of 15 WebSearch calls; 1 direct fetch attempt (failed at the proxy, so the extract was archived instead) |
| **Tag check** | `tools/check_tags.py`: 0 unknown source IDs and 0 long untagged paragraphs in all three layers. The American spellings reported are proper nouns: "Trust Center", "Elastic License", "NVIDIA API Catalog", and MongoDB's role names "Organization Owner" and "Organization Read Only". |

## Summary

- **14 score changes** across 12 products: 13 on enterprise readiness and 1 on security. Thirteen go up and one goes down (W&B Weave security, from 5 to 4).
- **NPV caps on enterprise readiness:** 4 lifted (LlamaParse, Cohere, Voyage and, as a rule 2 judgement rather than a cap, Phoenix). None remain on any hosted product in the three layers.
- **Security caps kept:** Voyage, Reducto and Firecrawl. Rule 6 does not change security, and rule 8 is unchanged.
- **Tier changes: none.** Cohere now scores FS 3.70, which meets the usual Strategic guide. It stays Tactical on its stated condition (see "Tiers").
- **Format:** the deep dives in L8 and L7 now use L9's labelled-bullet format. Each layer still has exactly one "Illustrative scenario [AJ]", in x.2.
- **Length:** every section grew. By `wc -w`, L9 went from 7,395 to 7,705 words, L8 from 7,481 to 7,885, and L7 from 7,547 to 8,010. Nothing was shortened.

## How rules 6 to 9 were applied

1. **Rule 6, hyperscaler presumption (Q1).** I applied it where the scored or recommended route is a service consumed through AWS, Azure or Google Cloud:
   - Gemini Embedding, through Vertex AI
   - Google Document AI
   - Cohere, through Microsoft Foundry and SageMaker [VF: A2-S012]
   - MLflow, as managed on SageMaker and Azure ML [VF: A1-S103]

   Each rationale and each deep dive carries the note "platform controls presumed (CP2 Q1); confirm per service".

   I did not apply it to:
   - SaaS products that merely run on a hyperscaler (Apify on AWS us-east-1; W&B Dedicated Cloud; Elastic Cloud for Jina)
   - NVIDIA NIM, because no hyperscaler-consumed route is in the fact base
   - Voyage's scored Atlas route. Its AWS Marketplace in-VPC route would score 4, and the rationale says so.
2. **Rule 7, partial evidence (Q2).**
   - Any one verified control among SSO, RBAC and audit logs lifts the NPV cap to 3.
   - All three controls plus SCIM, an SLA or an admin API reach 4.
   - For consistency with OpenAI, Datadog, LangSmith and Weave, which already scored 4 on that basis, I raised Langfuse, Mistral OCR and Firecrawl to 4. Each one's limitation is stated as a condition.
3. **Rule 8, certification scope (Q4).** I checked every security score against it (table below). One change: W&B Weave. Its ISO certifications are listed at W&B site level, so their Weave scope is not stated.
4. **Rule 9, tiers by judgement (Q3).** Tiers were kept, with their stated conditions. No product crossed a boundary in a way that its stated rationale does not already cover.

## (a) Score changes

| Layer | Product | Criterion | Before | After | Rule | Evidence |
|---|---|---|---:|---:|---|---|
| L9 | Langfuse | enterprise_readiness | 3 | 4 | 7 (all three controls plus SCIM) | A1-S033 |
| L9 | Arize Phoenix | enterprise_readiness | 2 | 3 | 7 (two of three verified: roles and OAuth2 IdP login; scored under rule 2) | A1-S105 |
| L9 | MLflow (GenAI) | enterprise_readiness | 3 | 4 | 6 (SageMaker and Azure ML managed routes; within the rule 2 cap of 4) | A1-S103 |
| L9 | W&B Weave | security_compliance | 5 | 4 | 8 (ISO certifications at W&B site level; Weave scope not stated) | A1-S137 |
| L8 | LlamaParse | enterprise_readiness | 2 (cap) | 3 | 7 (SSO verified; flat hosted roles and no audit log hold it at 3) | A1-S116, B-REV-S023 |
| L8 | Mistral OCR | enterprise_readiness | 3 | 4 | 7 (SSO, roles, audit logs and SCIM; audit logs not exportable, stated as a condition) | B-REV-S014, B-REV-S015 |
| L8 | Google Document AI | enterprise_readiness | 3 | 4 | 6 | B-REV-S010, B-REV-S012 |
| L8 | Firecrawl | enterprise_readiness | 3 | 4 | 7 (SSO, roles, SIEM audit logs and SCIM; built-in roles only) | B-REV-S024 |
| L7 | Gemini Embedding 2 | enterprise_readiness | 3 | 4 | 6 | B-REV-S007, B-REV-S008, B-REV-S012 |
| L7 | Cohere | enterprise_readiness | 2 (cap) | 4 | 6 on the Foundry and SageMaker routes; the direct API would be 3 under rule 7 (Owner and User roles) | A2-S012, B-REV-S013 |
| L7 | Voyage | enterprise_readiness | 2 (cap) | 3 | 7 (Atlas organisation and project roles govern model API keys; Admin API) | **B-REV-S028 (new)** |

### Totals that moved

| Product | Generic, before → after | FS, before → after |
|---|---|---|
| L9 Langfuse | 3.80 → 3.95 | 3.70 → 3.85 |
| L9 Phoenix | 3.50 → 3.65 | 3.35 → 3.50 |
| L9 MLflow | 4.10 → 4.25 | 4.10 → 4.25 |
| L9 Weave | 3.55 → 3.40 | 3.55 → 3.35 |
| L8 LlamaParse | 3.25 → 3.40 | 3.05 → 3.20 |
| L8 Mistral OCR | 3.15 → 3.30 | 3.10 → 3.25 |
| L8 Document AI | 3.40 → 3.55 | 3.30 → 3.45 |
| L8 Firecrawl | 3.10 → 3.25 | 2.85 → 3.00 |
| L7 Gemini | 3.15 → 3.30 | 3.05 → 3.20 |
| L7 Cohere | 3.45 → 3.75 | 3.40 → 3.70 |
| L7 Voyage | 3.25 → 3.40 | 2.90 → 3.05 |

### Checked and kept (recorded in `evidence_caps_applied` where relevant)

| Layer | Product | Criterion and score kept | Why |
|---|---|---|---|
| L9 | Datadog | enterprise_readiness 4 | Re-evidenced. The Roles API is an admin API (B-L9-S003), so this is all three controls plus an admin API under rule 7. Security 4 is consistent with rule 8. |
| L9 | Opik | security 4 | SOC 2 and ISO 27001 are listed against the Opik Enterprise plan (A1-S122), so the product scope is stated. Enterprise readiness 3: two of three controls, no audit log. |
| L9 | Braintrust | enterprise_readiness 3 | All three controls, but no SCIM, SLA or admin API |
| L9 | LangSmith, AX | 4 | Already consistent with rule 7 |
| L9 | DeepEval, Promptfoo | 3 | Rule 2 |
| L8 | Unstructured, Reducto, Apify | enterprise_readiness 3 | One or two controls; no documented audit log |
| L8 | Crawl4AI, MinerU | enterprise_readiness 2 | No SSO, RBAC or audit control verified (library rule; Crawl4AI uses token auth only) |
| L8 | Docling | enterprise_readiness 3 | Library rule |
| L8 | Document AI | security 5 | Product-scoped certifications plus CMEK |
| L8 | Mistral OCR | security 3 | Company-level certifications, one point below the anchor |
| L7 | OpenAI | 4 / 4 | Already consistent |
| L7 | Jina | enterprise_readiness 3, security 3 | Elastic Inference Service route: SSO and RBAC verified, audit logs not; scope rule applied |
| L7 | Qwen3 | 2 | Rule 2 |
| L7 | NVIDIA | 3 | No hyperscaler route in the fact base |
| L7 | Sentence Transformers | 3 | Rule 2 |

### Q4 consistency check

Company-level or platform-level certifications whose product scope is not stated score one point below the anchor:

| Product | Security score |
|---|---:|
| Datadog | 4 |
| Gemini | 4 |
| Cohere | 4 |
| Weave (changed) | 4 |
| Mistral OCR | 3 |
| Jina | 3 |

Product-scoped certifications are scored at face value:

| Product | Security score |
|---|---:|
| Langfuse | 4 |
| LangSmith | 4 |
| AX | 4 |
| Opik | 4 |
| OpenAI | 4 |
| Unstructured | 4 |
| Document AI | 5 |

## (b) Tiers

**No tier changes.**

**Cohere is the only judgement call.**
- It scores FS 3.70 with no criterion below 3, so it meets the rule 9 guide.
- It stays **Tactical** on the condition its earlier rationale stated: "Strategic once due diligence closes the access-control gap".
- The CP2 Q1 presumption is not that due diligence, and the Aleph Alpha combination is still pending.
- The deep dive, the classification rationale, §7.8 and §7.13 now present it as a "Strategic candidate".

**The other tiers that sit near a boundary are unchanged:**
- Langfuse (3.85) and MLflow (4.25) were already Strategic.
- Phoenix (3.50), Weave (3.35) and Document AI (3.45) stay Tactical for the reasons already stated.

## (c) Format changes

**L8 §8.7.**
- The headings changed from "**Docling (Strategic).**" with bold run-in labels to "**Name (owner).**", using the owner from the dataset `company` field.
- The bullets now use italic labels: *What it is now*, *Strengths*, *Limitations*, *Choose when*, *Avoid when*, *Competitors* and *FS note*. Extra labelled bullets were added where they carry existing content: *Project hygiene* (Docling), *Licence* (MinerU), *Access control* (LlamaParse, Document AI), *Certifications and access control* (Mistral OCR) and *Scoring note* (Firecrawl).
- Each deep dive closes with "**Tier: … Flag: ….**". Tier and flags had been in the heading; Docling's "Flags. None" bullet became the closing line.
- "Choose when / Avoid when", previously one bullet, is now two.
- The *Document understanding* and *Web acquisition* sub-headings are kept.

**L7 §7.7.**
- The `####` headings with bold paragraph labels were converted to the same labelled-bullet format.
- Long "What it is" paragraphs were split into labelled bullets, without dropping any sentence or tag: *Residency and certifications*, *Access control*, *Certifications*, *Deployment and certifications*, *Ownership*, *Licence and routes*, *Deployment and licensing*.
- The FS total is kept after each closing tier line.

**Tags.** All tags were preserved. Choose/avoid lines that had no tag gained `[AJ]`.

**Illustrative scenarios.** There is exactly one "Illustrative scenario [AJ]" per layer, in §9.2, §8.2 and §7.2, and none was moved.

## (d) Prose updated for changed scores or caps

**L9.**
- Phoenix: the access-control bullet adds OAuth2 IdP login [VF: A1-S105] and the rule 7 basis.
- MLflow: the limitations bullet adds the presumption on SageMaker and Azure ML, and the due-diligence note.
- Datadog: adds the Roles API [VF: B-L9-S003].
- Weave: the certifications bullet adds the scope reasoning.
- §9.8: new score table; a "CP2 rework" note; the scope-rule note now includes Weave.

**L8.**
- Deep dives for LlamaParse, Mistral OCR, Document AI and Firecrawl.
- §8.8: new score table; the "Evidence caps applied" list was rewritten, and a rule 8 note was added.

**L7.**
- §7.6: the "Enterprise controls … unevenly documented" paragraph now reflects rules 6 and 7 and B-REV-S028.
- Deep dives for Gemini, Voyage and Cohere.
- §7.8: new score table and "Reading the scores".
- §7.13: the Cohere row.

**Executive summaries.** No executive summary cited a changed score, so none was edited.

**Assessments JSON.**
- For each changed product: criteria, rationale lines and `evidence_caps_applied`.
- Classification rationale for Phoenix, Weave and Cohere.
- Assessment prose:
  - Cohere: limitations and avoid-when
  - Voyage: limitations
  - Mistral OCR: limitations
  - Document AI: limitations (stale "IAM not captured" text replaced)
  - MLflow: FS note

## (e) New score tables (`tools/score.py --write` output)

### L9

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9-langfuse | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 3.95 | 3.85 | Strategic |
| L9-langsmith | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 2 | 3.95 | 3.80 | Strategic |
| L9-braintrust | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.40 | 3.20 | Tactical |
| L9-arize-phoenix | 4 | 3 | 3 | 4 | 4 | 4 | 4 | 3 | 3.65 | 3.50 | Tactical |
| L9-arize-ax | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 2 | 3.85 | 3.70 | Tactical |
| L9-deepeval | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 4 | 3.75 | 3.70 | Tactical |
| L9-promptfoo | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 3 | 3.70 | 3.55 | Tactical |
| L9-opik | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 3.75 | 3.75 | Tactical |
| L9-mlflow-genai | 4 | 4 | 3 | 5 | 5 | 5 | 4 | 5 | 4.25 | 4.25 | Strategic |
| L9-datadog-agent-observability | 3 | 4 | 4 | 2 | 4 | 3 | 2 | 3 | 3.15 | 3.20 | Tactical |
| L9-wandb-weave | 3 | 4 | 4 | 4 | 3 | 3 | 3 | 2 | 3.40 | 3.35 | Tactical |

### L8

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8-docling | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4.00 | 4.05 | Strategic |
| L8-unstructured | 4 | 3 | 4 | 5 | 4 | 3 | 3 | 4 | 3.80 | 3.85 | Strategic |
| L8-llamaparse | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.40 | 3.20 | Tactical |
| L8-reducto | 4 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | 3.05 | 2.90 | Tactical |
| L8-mistral-ocr | 3 | 4 | 3 | 4 | 3 | 2 | 4 | 3 | 3.30 | 3.25 | Tactical |
| L8-google-document-ai | 4 | 4 | 5 | 2 | 3 | 3 | 4 | 2 | 3.55 | 3.45 | Tactical |
| L8-firecrawl | 4 | 4 | 2 | 3 | 4 | 3 | 3 | 2 | 3.25 | 3.00 | Tactical |
| L8-crawl4ai | 3 | 2 | 2 | 4 | 3 | 2 | 4 | 4 | 2.90 | 2.90 | Experimental |
| L8-mineru | 4 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2.80 | 2.70 | Experimental |
| L8-apify | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 2 | 2.65 | 2.55 | Tactical |

### L7

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7-openai | 3 | 4 | 4 | 2 | 3 | 4 | 4 | 2 | 3.30 | 3.20 | Tactical |
| L7-gemini-embedding | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Tactical |
| L7-voyage | 5 | 3 | 2 | 3 | 4 | 3 | 4 | 2 | 3.40 | 3.05 | Tactical |
| L7-cohere | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3.75 | 3.70 | Tactical |
| L7-qwen3-embedding | 4 | 2 | 2 | 4 | 3 | 3 | 4 | 4 | 3.20 | 3.15 | Tactical |
| L7-jina | 4 | 3 | 3 | 4 | 4 | 3 | 2 | 2 | 3.30 | 3.15 | Tactical |
| L7-sentence-transformers | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 3.80 | 3.70 | Strategic |
| L7-nvidia-nemo-retriever | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 2 | 3.00 | 2.95 | Tactical |
| L7-ethicalagents | – | – | – | – | – | – | – | – | n/a | n/a | not scored |
| L7-ragoos | – | – | – | – | – | – | – | – | n/a | n/a | not scored |

### Tier distribution (unchanged)

| Layer | Strategic | Tactical | Experimental | Not scored |
|---|---:|---:|---:|---:|
| L9 | 3 | 8 | 0 | 0 |
| L8 | 2 | 6 | 2 | 0 |
| L7 | 1 | 7 | 0 | 2 |

**Calibration note (rubric rule 5).** Every layer still has scores of 2 or below:
- L9: four lock-in scores of 2, and Datadog on deployment and cost
- L8: Apify deployment 1; the security caps on Reducto and Firecrawl
- L7: several 2s on deployment, lock-in and security

## (f) Judgements the human may want to revisit

1. **Cohere scored on its hyperscaler route.** This follows the Jina precedent of scoring the recommended route. On the direct API it would be 3, giving FS 3.55. The tier is kept Tactical despite FS 3.70.
2. **Rule 7 "4" lifts for Langfuse, Mistral OCR and Firecrawl.** These are consistent with OpenAI, Datadog and Weave. Mistral's non-exportable audit logs are the weakest case.
3. **Weave security from 5 to 4.** This is a strict reading of rule 8: the ISO scope is not stated on the Weave page.
4. **MLflow presumption.** It covers only the SageMaker and Azure ML routes. Databricks-managed MLflow is not presumed.

## Files changed

- `work/stageB/L9/section.md`, `work/stageB/L8/section.md`, `work/stageB/L7/section.md`
- `work/stageB/L9/assessments.json`, `work/stageB/L8/assessments.json`, `work/stageB/L7/assessments.json` (totals rewritten by `tools/score.py --write`)
- `work/stageB/_review/sources_added.csv` (B-REV-S028 appended)
- `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/B-REV-S028.extract.txt`
- `work/stageB/_review/CP2_rework_log.md` (this file)

**Not run:**
- `git`
- `tools/build_dataset.py`: re-run it to propagate the new scores and B-REV-S028 into `05_Data/`.

**Not updated:** `MEMORY.md`.
