# Refreshing the review every quarter

This guide updates the October 2026 edition to a new edition (for example January 2027). It re-checks what has changed, re-scores only what needs it, and rebuilds every deliverable. It does not redo the research from scratch. For a full re-run, see `RERUN_ON_DESKTOP.md` §4.

| | |
|---|---|
| **Baseline** | October 2026 edition, CP5 sign-off package: commit `79907bd` on `claude/nice-meitner-0me752` |
| **Prompts** | `work/prompts/refresh_prompts.md` (R0–R6) |
| **Where to run** | Your desktop with Claude Code is best: open internet, no search cap. A cloud session also works, but blocked sites fall back to search extracts (MEMORY.md B1, B2). |
| **Effort** | Roughly a third of the original run: one monitor sweep, eight delta agents, two verifiers, re-scoring only for changed layers, a synthesis update and a rebuild |
| **Reader checkpoints** | RCP1 facts · RCP2 tiers · RCP3 package |

## 1. Start the refresh

```bash
git clone https://github.com/gitzerobegin/genai_stack.git && cd genai_stack   # or: git pull
git checkout claude/nice-meitner-0me752
git checkout -b refresh-2027-01            # one branch per edition
```

Then open Claude Code in the repo folder (`claude`) and say:

```text
Read CONTEXT.md, MEMORY.md and REFRESH_QUARTERLY.md. Run refresh R<N> for the <Month YYYY> edition,
following the steps in REFRESH_QUARTERLY.md and the prompts in work/prompts/refresh_prompts.md.
Stop at each refresh checkpoint (RCP1, RCP2, RCP3) for my decisions.
```

That single instruction is enough: Claude Code reads this file and runs the steps below. The rest of this guide is the detail, if you want to run or check steps yourself.

## 2. Rename the package and the dates

The package folder name carries the edition date. Rename it first, so new snapshots land in the right place:

```bash
OLD=Enterprise_GenAI_Stack_Oct2026; NEW=Enterprise_GenAI_Stack_Jan2027
git mv $OLD $NEW
grep -rl "$OLD" tools CLAUDE.md CONTEXT.md README.md RERUN_ON_DESKTOP.md work/stage0 work/prompts \
  | xargs sed -i "s/$OLD/$NEW/g"          # on macOS: sed -i '' "s/.../.../g"
grep -rn "October 2026\|Q3 2026" tools $NEW/08_Graphic   # titles, subtitles, deck, figures: change to the new edition
# Book metadata: tools/print/book.json -> edition, evidence_date, short_subtitle, subtitle ("The view at end of Q4 2026")
# REFRESH_QUARTERLY.md is left out on purpose: step 4 needs the old path for the comparison.
```

Keep the old ZIP inside the renamed folder only if you want both editions in one place. Otherwise remove it; the baseline commit keeps it.

## 3. Facts (R0, R1, R2) → checkpoint RCP1

| Step | What | Output |
|---|---|---|
| R0 | Monitor sweep: every XI.6 monitor item, every passed or upcoming calendar date (X.1), every conditional tier set by the reader (e.g. SGLang CVE fix, Fireworks ISO certificates), the "not yet profiled" list, and the volatile Stage E facts (start-up credits, US state AI-law dates, CRA/PLD milestones, model licence terms, the coding-agent landscape, agent marketplaces and agent-identity standards) | `work/refresh/R<N>/R0/monitor_sweep.md` |
| R1 | Eight delta agents (A1–A8) in parallel, plus the three Stage E streams (E1 regulation, E2 commercial, E3 agentic SDLC and agent standards) for the further views. They update `work/stageA/*/products.json` in place, add new sources as `R<N>-<stream>-S###`, add only material new entrants, and A8 updates the regulatory facts | `work/refresh/R<N>/<stream>/changes.md`, `sources.csv` |
| R2 | Two verifiers re-check every change to certifications, residency, ownership, licence, incidents and pricing, plus a 25% sample of the rest | `work/refresh/R<N>/V1`, `V2` |
| Build | `python3 -I tools/build_dataset.py .` (expect 0 issues) and `python3 -I tools/npv_report.py .` | Updated dataset and bibliography |

**RCP1:** review the material changes (the summaries from R0 and R1) before any re-scoring.

## 4. Tiers (R3) → checkpoint RCP2

1. Re-score only the layers with material changes (R3 writer prompt), then run the calibration reviewer. Then `python3 -I tools/build_views.py .` to refresh the six further views' scores (change `work/stageE/views/views.json` weights only by a reader decision).
2. Produce the change table:
   ```bash
   python3 -I tools/diff_tiers.py . 79907bd \
     --base-path Enterprise_GenAI_Stack_Oct2026/05_Data/products.json \
     --path Enterprise_GenAI_Stack_Jan2027/05_Data/products.json \
     --out work/refresh/R<N>/tier_changes.md
   ```
3. **RCP2:** decide every tier change the reviewer flagged, and any tier you set at an earlier checkpoint (Anthropic, MCP, A2A, SGLang, Fireworks, Pydantic AI, Google ADK). Record the decisions in `checkpoints/R<N>/`.

## 5. Synthesis and posts (R4, R5)

- **R4b. Further views.** Update Parts XIII–XVIII (`work/stageE/views/{TS,SW,SU,AT,DV,AG}/view.md`) with prompt R4b: new view scores, changed E1/E2 facts, the views' worked examples and roadmaps. Run `check_tags.py` on each.
- **R4.** Update the synthesis in place: the tier table and counts, Part I, the stacks, the Part XI lists, and the calendar. Add a closing "What changed since <previous edition>" part. Then run the independent synthesis reviewer and `python3 -I tools/check_tags.py . work/stageC/synthesis.md`.
- **R5b. The LinkedIn book.** Update the chapters whose posts or evidence changed (prompt R5b), keep `worked_example_build.json` in step, and rebuild with `python3 -I tools/build_linkedin_book.py .`. A new edition of the book needs new ISBNs if its content changes materially (`07_LinkedIn/Book/Publishing_Kit.md`).
- **R5 (optional).** Write 2–4 LinkedIn posts on the most material changes. Give each new post a visual: copy a similar `08_Graphic/linkedin/P<NN>.md`, edit it and render it with `node tools/render_post_visuals.js`. If counts changed, update Post 0 (the series introduction) and its visual P00.

## 6. Package (R6) → checkpoint RCP3

First update `tools/deck/tiers.json` and any slide text that names tiers, counts or dates. Then rebuild everything in one go:

```bash
bash tools/rebuild_all.sh        # dataset, tag check, diagrams, post visuals, stack graphic (--sync), explorer,
                                 # LinkedIn document, deck, master, print and Kindle edition, appendix, ZIP
```

`build_stack_graphic.py --sync` (inside the script) refreshes tiers in the stack graphic from the dataset and adds new products to its Markdown; check the labels afterwards. To run steps one at a time, see the commands inside `tools/rebuild_all.sh` and `RERUN_ON_DESKTOP.md` §2b.

Then:
- update `<PKG>/00_README.md` (as-of date and counts);
- read `01_Report/Print/Build_Summary.md`. Every KDP check should say OK; the spine width follows the new page count automatically. If you sell the book, upload the new `Interior.pdf`, `Cover_Paperback.pdf` and `Ebook.epub` as a new edition (see `Publishing_Kit.md` §6);
- update or copy the Claude Doc;
- add a run-log row and a new "Current position" to `MEMORY.md`;
- commit and push the refresh branch.

**RCP3:** sign-off.

## Keeping it on a schedule

- **Ask Claude to remind you:** for example, "remind me on 9 January 2027 to start the quarterly refresh". A Claude Code session can set a scheduled reminder or Routine for that date.
- **Calendar:** add a quarterly entry pointing to this file.
- **Natural trigger dates:** the Part X.1 calendar has several, for example 18 March 2027 (PS7/26 and PS26/2 notifications begin) and 2 December 2027 (EU AI Act Annex III duties).

## What stays the same between editions

- The house conventions in `CONTEXT.md`: layer order L1 → L9, "the view at end of Q<n> <year>" framing with diagram-relative content only under "What changed since the popular stack diagram", Veyan branding with the full lockup, and Mermaid diagrams (no ASCII art). Update the quarter wording (for example "The view at end of Q4 2026") in `tools/deck/build_deck.js`, `tools/build_master.py`, `tools/make_reference_docx.py`, the graphics' sources and the synthesis.

- **One home per section.** The LinkedIn series lives only in `07_LinkedIn`. The tile-by-tile what-changed table lives only in `05_Data/what_changed.xlsx`, summarised in synthesis Part XII. The master links to both and repeats neither.
- **Seven views.** The regulated-FS master view (Parts I–XII) plus six further views (Parts XIII–XVIII): technology service provider, software product company, start-up, and the vendor start-ups selling AI tools, agentic SDLC tools and agents. Each is refreshed every edition (`work/stage0/11_stageE_views_brief.md`).
- **The book.** `tools/build_print_edition.py` turns the master into the print and Kindle editions. Its settings are in `tools/print/book.json`.
- Scoring rubric rules 1–13 and the weights, unless you change them at RCP2.
- The CP decisions recorded in `checkpoints/`. For example, Stack A is the lead stack, the review is cloud-neutral, and the two routes moved to "monitor" at CP5 stay there.
- The source-ID scheme. Old IDs never change; each refresh adds `R<N>-…` IDs, so every edition stays traceable.
