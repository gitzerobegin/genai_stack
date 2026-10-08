# Gap-filling prompts for an environment with open internet access

Use these on a desktop running Claude Code, where vendor, trust-centre and regulator sites can be fetched directly and web search is not capped at about 200 calls. They close the evidence gaps left by the cloud run. The full procedure is in `RERUN_ON_DESKTOP.md`.

## G1: Primary-source verification of unverified and medium-confidence facts (one agent per stream)

Run once for each stream. Example for A5:

```text
You are a Stage A gap-filling agent for stream A5 (folder work/stageA/A5_L1). Today is <DATE>.
Read work/stage0/05_stageA_research_brief.md, work/stage0/02_dataset_schema.md and work/stage0/03_style_guide.md.
This environment HAS open internet access: fetch primary pages directly (WebFetch or python3 -I tools/snapshot.py) instead of relying on search extracts.

Input: work/gapfill/npv_cells.csv (rows for your stream's product ids) and the cells in work/stageA/A5_L1/products.json whose conf is "medium" because they rest on a search extract (access_status "extract" in sources.csv).

For each cell, in priority order (certifications > data residency / retention > access controls > pricing > versions > adoption):
1. Fetch the vendor's primary page (docs, trust centre, pricing, release notes, regulator page) directly and archive it with tools/snapshot.py into Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/G-A5/.
2. If it confirms the value, add the new source id (G-A5-S001…) to src and raise conf to "high". If it contradicts the value, correct it and log old → new. If nothing supports it, keep "Not publicly verified".
3. Log new sources in work/gapfill/A5/sources.csv (same columns as Stage A).
Never work around paywalls or logins; cite those by link only.
Do not run git. Validate the JSON at the end. Write work/gapfill/A5/gapfill_log.md (table: record | field | before | after | source) and reply with counts.
```

**Streams and folders:**

| Stream | Folder |
|---|---|
| A1 | A1_L9_L8 |
| A2 | A2_L7_L6 |
| A3 | A3_L5_L4 |
| A4 | A4_L3_L2 |
| A5 | A5_L1 |
| A6 | A6_C1_C4 |
| A7 | A7_C5_C8 |
| A8 | A8_Regulation (uses `regulatory_facts.json`; prioritise downloading regulator PDFs as originals) |

**Note:** `tools/build_dataset.py` reads `work/stageA/*/sources.csv`, `work/stageA_verify/*/sources.csv` and `work/stageB/*/sources_added.csv`. Before rebuilding, either append the G sources to the stream's `sources.csv`, or extend the glob to include `work/gapfill/*/sources.csv`.

## G2: Items the verifiers listed as unchecked

```text
Read §5 ("Not checked") of work/stageA_verify/V1/verification_log.md and work/stageA_verify/V2/verification_log.md.
Verify each listed claim against primary sources (direct fetch allowed in this environment), edit the products.json / regulatory_facts.json cells in place per work/stage0/06_stageA_prime_verify_brief.md, and append the results to the same verification logs under a new heading "## 7. Desktop gap-fill (<DATE>)".
```

## G3: Products named in the plan but not yet profiled

```text
Research and add records (schema work/stage0/02_dataset_schema.md) for: ServiceNow AI Control Tower and OneTrust AI Governance (C8); Daytona and Modal sandboxes (L4); Azure AI Search and Vertex AI Vector Search (L6). Put them in the matching stream's products.json with original_label null.
```
