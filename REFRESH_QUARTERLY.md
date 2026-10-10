# Refreshing the review every quarter

This guide updates the current edition to a new edition, in any month (for example December 2026 or January 2027). It re-checks what has changed, re-scores only what needs it, and rebuilds every deliverable. It does not redo the research from scratch. For a full re-run, see `RERUN_ON_DESKTOP.md` §4.

| | |
|---|---|
| **Baseline** | The current edition in `edition.json` (first edition: October 2026, "The view at end of Q3 2026"). `tools/new_edition.py` records its commit as `previous`, so every comparison runs against it without arguments |
| **Edition setting** | `edition.json` at the repo root: package folder, month, quarter, label, evidence date, edition number. Every build tool, the deck and the figures read it; no tool is edited by hand for a new edition |
| **Prompts** | `work/prompts/refresh_prompts.md` (R0–R6) |
| **Where to run** | Your desktop with Claude Code is best: open internet, no search cap. A cloud session also works, but blocked sites fall back to search extracts (MEMORY.md B1, B2). |
| **Effort** | Roughly a third of the original run: one monitor sweep, eight delta agents, two verifiers, re-scoring only for changed layers, a synthesis update and a rebuild |
| **Reader checkpoints** | RCP1 facts · RCP2 tiers · RCP3 package |

## 1. Start the refresh

```bash
git clone https://github.com/gitzerobegin/genai_stack.git && cd genai_stack   # or: git pull
git checkout claude/nice-meitner-0me752
git checkout -b refresh-2026-12            # one branch per edition (any month)
```

Then open Claude Code in the repo folder (`claude`) and say:

```text
Read CONTEXT.md, MEMORY.md and REFRESH_QUARTERLY.md. Run refresh R<N> for the <Month YYYY> edition,
following the steps in REFRESH_QUARTERLY.md and the prompts in work/prompts/refresh_prompts.md.
Stop at each refresh checkpoint (RCP1, RCP2, RCP3) for my decisions.
```

That single instruction is enough: Claude Code reads this file and runs the steps below. The rest of this guide is the detail, if you want to run or check steps yourself.

## 2. Start the new edition (one command)

```bash
python3 -I tools/new_edition.py . --month 2026-12 --dry-run                          # preview
python3 -I tools/new_edition.py . --month 2026-12 --evidence-date "8 December 2026"  # do it
```

It moves the package folder (`Enterprise_GenAI_Stack_Oct2026` → `Enterprise_GenAI_Stack_Dec2026`), renames the stack graphic files, writes `edition.json` (the old edition becomes `previous`, with its commit), relabels the master's sources and the package README, and updates the package name in the guides, briefs and refresh prompts. The label follows the month: a run in the first month of a quarter (January, April, July, October) is "The view at end of Q<n> <year>" for the quarter just closed; any other month is "The view in <Month> <year>" (for example "The view in December 2026"). Pass `--label` and `--as-at` to choose other wording. Dated facts ("as of 8 October 2026") are evidence and are left for the refresh to re-verify. The LinkedIn series and its book keep their own first edition.

After any rebuild, `python3 -I tools/check_edition.py .` (also the last step of `rebuild_all.sh`) lists every file that still names the previous edition: **LABEL** counts should be 0; **DATED** mentions ("Q3 2026", "October 2026") are for R1–R4 to decide one by one.

A desktop re-run of the same edition (`RERUN_ON_DESKTOP.md`) does not start a new edition: skip this step.

No ZIP is made or committed (user decision, 10 October 2026): every file is pushed to GitHub, and the baseline commit keeps the previous edition.

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
   python3 -I tools/diff_tiers.py . --out work/refresh/R<N>/tier_changes.md
   # compares with the previous edition recorded in edition.json (its commit and package folder)
   ```
3. **RCP2:** decide every tier change the reviewer flagged, and any tier you set at an earlier checkpoint (Anthropic, MCP, A2A, SGLang, Fireworks, Pydantic AI, Google ADK). Record the decisions in `checkpoints/R<N>/`.

## 5. Synthesis and posts (R4, R5)

- **R4b. Further views.** Update Parts XIII–XVIII (`work/stageE/views/{TS,SW,SU,AT,DV,AG}/view.md`) with prompt R4b: new view scores, changed E1/E2 facts, the views' worked examples and roadmaps. Run `check_tags.py` on each.
- **R4.** Update the synthesis in place: the tier table and counts, Part I, the stacks, the Part XI lists, and the calendar. Update Part XII ("The new baseline at a glance") so that it describes the new edition's baseline, and add to it a short "Changes since <previous edition>" section built from the `tools/diff_tiers.py` output (step 4). Compare only with the previous edition, never with the original diagram (house convention 2). Then run the independent synthesis reviewer and `python3 -I tools/check_tags.py . work/stageC/synthesis.md`.
- **R5b. The LinkedIn book.** Update the chapters whose posts or evidence changed (prompt R5b), keep `worked_example_build.json` in step, and rebuild with `python3 -I tools/build_linkedin_book.py .`. A new edition of the book needs new ISBNs if its content changes materially (`07_LinkedIn/Book/Publishing_Kit.md`).
- **R5 (optional).** Write 2–4 LinkedIn posts on the most material changes. Give each new post a visual: copy a similar `08_Graphic/linkedin/P<NN>.md`, edit it and render it with `node tools/render_post_visuals.js`. If counts changed, update Post 0 (the series introduction) and its visual P00. If any view's weights or core-candidate counts changed (`work/stageE/views/views.json`), update the seven-lenses Posts 25–32, their visuals P25–P32 and book chapters ch25–ch32.

## 6. Package (R6) → checkpoint RCP3

Counts, tiers, sources and the edition label in the deck, graphics, books and Explorer come from the dataset and `edition.json`. First update only the slide text that states findings or dated facts (`tools/deck/build_deck.js`; `check_edition.py` lists what still names the previous quarter). Then rebuild everything in one go:

```bash
bash tools/rebuild_all.sh        # dataset, tag check, diagrams, post visuals, stack graphic (--sync), explorer,
                                 # LinkedIn document, deck, master, print and Kindle edition, appendix (Word only; no ZIP),
                                 # then the edition check (tools/check_edition.py)
```

`build_stack_graphic.py --sync` (inside the script) refreshes tiers in the stack graphic from the dataset and adds new products to its Markdown; check the labels afterwards. To run steps one at a time, see the commands inside `tools/rebuild_all.sh` and `RERUN_ON_DESKTOP.md` §2b.

Then:
- update `<PKG>/00_README.md` (as-of date and counts);
- read `01_Report/Print/Build_Summary.md`. Every KDP check should say OK; the spine width follows the new page count automatically. If you sell the book, upload the new `Interior.docx` (KDP converts it), `Cover_Paperback.pdf` and `Ebook.epub`; the spine uses an estimated page count, so confirm it in KDP's previewer (or build `Interior.pdf` with `python3 -I tools/build_print_edition.py . --pdf`) as a new edition (see `Publishing_Kit.md` §6);
- update or copy the Claude Doc;
- add a run-log row and a new "Current position" to `MEMORY.md`;
- commit and push the refresh branch.

**RCP3:** sign-off.

## Keeping it on a schedule

- **Ask Claude to remind you:** for example, "remind me on 9 January 2027 to start the quarterly refresh". A Claude Code session can set a scheduled reminder or Routine for that date.
- **Calendar:** add a quarterly entry pointing to this file.
- **Natural trigger dates:** the Part X.1 calendar has several, for example 18 March 2027 (PS7/26 and PS26/2 notifications begin) and 2 December 2027 (EU AI Act Annex III duties).

## What stays the same between editions

- The house conventions in `CONTEXT.md`: layer order L1 → L9, the new-baseline framing, the edition label from `edition.json` ("The view at end of Q<n> <year>", or "The view in <Month> <year>" off the quarter boundary), with no diagram-relative content (each edition is compared with the previous edition only), Veyan branding with the full lockup, and Mermaid diagrams (no ASCII art). The label is set once by `tools/new_edition.py`; no tool carries it.

- **One home per section.** The LinkedIn series lives only in `07_LinkedIn`, and product fact sheets only in `02_Appendix`. The master links to both and repeats neither. The old tile-by-tile table against the original diagram is provenance only (`work/stageD/archive/diagram_provenance.xlsx`) and is not refreshed.
- **Seven views.** The regulated-FS master view (Parts I–XII) plus six further views (Parts XIII–XVIII): technology service provider, software product company, start-up, and the vendor start-ups selling AI tools, agentic SDLC tools and agents. Each is refreshed every edition (`work/stage0/11_stageE_views_brief.md`).
- **The book.** `tools/build_print_edition.py` turns the master into the print and Kindle editions. Its settings are in `tools/print/book.json`; the subtitle, edition line, evidence date, year and source count are filled from `edition.json` and the dataset (`{VIEW_LABEL_TC}`, `{EDITION}`, `{N_SOURCES}` …).
- Scoring rubric rules 1–13 and the weights, unless you change them at RCP2.
- The CP decisions recorded in `checkpoints/`. For example, Stack A is the lead stack, the review is cloud-neutral, and the two routes moved to "monitor" at CP5 stay there.
- The source-ID scheme. Old IDs never change; each refresh adds `R<N>-…` IDs, so every edition stays traceable.
