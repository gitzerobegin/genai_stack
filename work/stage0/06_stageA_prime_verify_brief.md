# Stage A′: Adversarial verification brief (two verifiers)

You are an adversarial fact-checker. Today is **7 October 2026**. Stage A research agents have produced a fact base. Your job is to **try to break their high-risk claims**: assume each one may be wrong, stale, or resting on a low-quality source, and re-check it against primary sources.

## Read first (repo root `/home/user/genai_stack`)

- `work/stage0/05_stageA_research_brief.md`: research environment, archiving tools and source rules. They all apply to you.
- `work/stage0/02_dataset_schema.md`: fact-cell format
- `work/stage0/03_style_guide.md`: labels and British spelling
- The stream folders assigned to you under `work/stageA/`: `products.json` (or `regulatory_facts.json`), `notes.md` and `sources.csv`

## What counts as high-risk (check all of these)

1. **Versions and lineups:** model versions, product versions, release dates, GA vs preview.
2. **Pricing:** any price figure.
3. **Acquisitions, mergers, renames, deprecations, shutdowns, funding rounds.**
4. **Certifications:** SOC 2 Type I/II, ISO 27001/42001, HIPAA, FedRAMP; data-residency regions.
5. **Regulatory dates and statuses:** in force, applies from, postponed, designated.
6. **Licences:** especially changes (e.g. open source → source-available).
7. **Any claim that rests only on a `secondary-aggregator` source**, or on a single source of any type.
8. **Every "What changed" row in each `notes.md`.**

## Method

- **For each claim, run a fresh, independent search.** Prefer `allowed_domains` set to the vendor's or regulator's domain, and use extended mode for recent facts. Do not reuse the Stage A agent's query.
- **Outcome per claim:**
  - **Confirmed:** keep it. Add your new source ID to `src` if you used a new source, and raise `conf` if justified.
  - **Corrected:** fix the value in place, set the correct label/conf/src, and log the old value and new value with sources.
  - **Downgraded:** the evidence is weaker than claimed. Lower the label (Verified fact → Reported, or → Not publicly verified) and/or `conf`.
  - **Unresolvable:** set the value to `"Not publicly verified"` if no source supports it.
- **You may edit `products.json` / `regulatory_facts.json` in your assigned folders directly.** Keep the JSON valid, and validate it after each batch of edits.
- **Archive new sources** with `tools/snapshot.py` or `tools/save_extract.py` into `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/<VERIFIER>`.
  - Use source IDs `V1-S001…` or `V2-S001…`.
  - Log them in `work/stageA_verify/<VERIFIER>/sources.csv`, using the same columns as Stage A.
  - Cite them from the edited records.
- **Do not run git.**

## Outputs

`work/stageA_verify/<VERIFIER>/verification_log.md` contains:

- A summary: claims checked, confirmed, corrected, downgraded and unresolvable, by stream.
- A table: `| Record id | Field | Claim (before) | Outcome | After | Sources |`
- **Corrections to the "What changed" rows**, listed explicitly.
- A list of claims you think the writers must not rely on.

**Final reply:** at most 250 words, covering the counts, the 5 most consequential corrections, and the residual risks.
