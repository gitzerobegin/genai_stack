# Stage A: Shared research brief, for all eight research agents

You are one of eight parallel research agents. You are building the **fact base** for an enterprise GenAI reference architecture review dated **7 October 2026**. You write facts (plan §7 blocks A–G and J), not opinions. Assessment and classification come later, in Stage B.

## Read first (repo root: `/home/user/genai_stack`)

1. `inputs/Enterprise_GenAI_Stack_Consolidated_Plan_v4.3.md`: §2 (quality rules), §3, §5/§6 (your scope), §7
2. `work/stage0/01_baseline_inventory.md`: the graphic as transcribed, and the ambiguities A1–A19
3. `work/stage0/02_dataset_schema.md`: **the exact output schema**
4. `work/stage0/03_style_guide.md`: British spelling and claim labels
5. `work/stage0/04_hypotheses_and_evidence_plan.md`: the evidence your stream must collect

## Non-negotiable rules

- **Your training data predates today.** Do not rely on memory for any version, price, certification, acquisition or date. Every fact in your output must come from a search or fetch you make in this run, and must carry a source ID. Memory may only suggest *what to search for*.
- **No invented facts.** If you cannot confirm something, write `"Not publicly verified"` with label `Not publicly verified`. An honest gap is worth more than a plausible guess.
- **Primary sources first:**
  1. vendor docs
  2. vendor announcements/blog
  3. trust centre
  4. regulator
  5. high-quality independent technical sources

  Search engines in 2026 return many low-quality AI-generated "news" and aggregator pages, such as aitoolly, apiyi, llmreference and random subdomains. Treat these as `secondary-aggregator`, label any claim that rests on them **Reported** with `conf: low`, and never use one as the only source for a version, price, acquisition or certification. Try hard to find the vendor's own page.
- **Conflicts:** if sources disagree, record both in `stage_a_notes` and use the primary one.
- **Respect access restrictions.** If something is paywalled, login-gated or blocked, cite it by link only. Never work around it: no mirrors, caches or archive.org copies of paywalled content.
- **British spelling** in all prose.

## Research environment (important)

- **`WebSearch` works.** It is your main tool.
  - Use `mode: "standard"` by default, and `"extended"` for hard or very recent facts (versions, pricing, acquisitions, certifications).
  - Use `allowed_domains` to target primary sources, e.g. `allowed_domains: ["qdrant.tech"]`.
  - Issue independent searches in parallel in one turn.
- **Direct fetching is mostly blocked** by the environment's egress policy.
  - **Known to work:** `www.anthropic.com`, `docs.claude.com`, `cloud.google.com`, `pypi.org`.
  - **PyPI JSON API:** `curl -s https://pypi.org/pypi/<package>/json` gives the latest version, release dates, licence and project URLs. It is excellent primary evidence for open-source Python packages.
  - **Known blocked:** github.com, api.github.com, most vendor sites, nist.gov, eur-lex and others.
  - `WebFetch` follows the same policy. Try a new domain at most once. If it returns `EGRESS_BLOCKED`, do not retry that domain.

## Archiving every source you rely on

The source archive is a deliverable. Every source cited in your output is recorded in your `sources.csv` and archived.

| Situation | Command |
|---|---|
| Host fetchable | `python3 -I tools/snapshot.py <ID> "<URL>" Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/<STREAM>`. This saves a text snapshot, or the PDF original under `06_References/originals/`. Exit code 2 means "link-only". |
| Host blocked (most cases) | Save the search-tool text you relied on: write it to a temp file in your scratch area, then run `python3 -I tools/save_extract.py <ID> "<URL>" Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/<STREAM> "<query used>" < tmpfile`. Paste the extract as returned; do not embellish it. |

- **Source IDs** are `<STREAM>-S001`, `<STREAM>-S002`, … in order of first use, e.g. `A4-S031`.
- **`sources.csv` columns:** `id,url,title,publisher,source_type,accessed,access_status,archive_path,used_for`. Quote any field that contains commas.
- **Archive paths** are relative to the repo root.

## Outputs (write only inside your own folders)

| Path | Content |
|---|---|
| `work/stageA/<STREAM_FOLDER>/products.json` | A valid JSON **array** of product records per the schema. Fill fields 1–26, 30, 31 and 32. Leave `assessment`, `classification` and `scores` as `null`. |
| `work/stageA/<STREAM_FOLDER>/notes.md` | See the list below |
| `work/stageA/<STREAM_FOLDER>/sources.csv` | The source log |
| `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/<STREAM>/` | Your archive files |

`notes.md` contains:

- (a) **"What changed since the original diagram" rows**, one per product, in the form `| Original label | Current reality (as of date) | Flag | Sources |`. Flag is one of: No change / Renamed / Acquired / Superseded / Deprecated / Duplicated / Mispositioned / Version label wrong / Not publicly verified.
- (b) Resolution of each ambiguity you own (A-numbers from the inventory), with evidence.
- (c) Evidence for the hypotheses assigned to your stream, as sourced bullet points with no verdicts.
- (d) Products you found that the graphic misses and that an enterprise architect would expect. Name, one line, source. Add at most 3 per layer to `products.json` only if they are clearly material, and mark them `"original_label": null`.
- (e) Gaps: what you could not verify, and why.

## Working rules

- **Do not run git.** Do not edit files outside your folders.
- **Be thorough but efficient.** About 4–8 searches per product is typical. Pricing pages, trust centres (look for `trust.<vendor>.com` or `/security`) and release notes are high-value.
- At the end, validate your JSON: `python3 -c "import json;d=json.load(open('work/stageA/<STREAM_FOLDER>/products.json'));print(len(d))"`. Also check that every `src` ID appears in `sources.csv`.
- **Final reply:** a summary of at most 300 words covering the number of products, sources and archive files, the five most important changes versus the graphic, and the top unverifiable items.
