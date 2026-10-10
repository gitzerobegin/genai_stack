# Re-running or gap-filling this work on your own desktop

The cloud run was constrained in two ways:

1. **An egress allow-list.** Most vendor, trust-centre and regulator sites, plus github.com, were blocked from direct fetch.
2. **A web-search cap** of about 200 calls per agent turn, shared by all running agents.

A desktop with ordinary internet access removes both. Use it to:

- **upgrade the evidence:** turn search extracts into real snapshots and PDF originals, and close the "Not publicly verified" gaps
- **resume the pipeline** from the latest checkpoint
- **re-run any stage from scratch**

`MEMORY.md` records every step taken and `CONTEXT.md` is the project briefing; follow its **House conventions** (layer order L1 → L9, Veyan branding, Mermaid diagrams, the new-baseline framing, the edition label in `edition.json`, with no diagram-relative content). All agent prompts are in `work/prompts/`.

**Which edition?** A desktop gap-fill or re-run improves the **current** edition (`edition.json`: package folder, label, evidence date) and needs no other step: every tool reads the folder and label from that file. If you are producing a **new** edition (a later month, for example December 2026), start it first with `python3 -I tools/new_edition.py . --month 2026-12` and follow `REFRESH_QUARTERLY.md`. Either way, `bash tools/rebuild_all.sh` ends with `tools/check_edition.py`, which lists anything that still names a previous edition.

## 1. Set-up (once)

```bash
git clone https://github.com/gitzerobegin/genai_stack.git
cd genai_stack
git checkout claude/nice-meitner-0me752      # working branch
python3 -m venv .venv && source .venv/bin/activate
pip install requests beautifulsoup4 openpyxl python-docx python-pptx reportlab pypdf markdownify
# For rebuilding the deliverables (step 2.8, tools/rebuild_all.sh):
#   pandoc                      (Word and EPUB exports)
#   LibreOffice with its Python UNO bridge (the deck PDF, and PDFs only on request with --pdf: tools/docx2pdf.py,
#     tools/print/print_pdf.py; on Debian/Ubuntu: apt install libreoffice python3-uno; on macOS run the
#     scripts with LibreOffice's bundled python: /Applications/LibreOffice.app/Contents/Resources/python)
#   Node.js 18+ with Playwright (figures and covers): npm install -g playwright && npx playwright install chromium
#   (cd tools/deck && npm install)       # pptxgenjs 3.12.0 for the deck
#   (cd tools/diagrams && npm install)   # mermaid 11.17.2 for the chapter diagrams
#   fonts: Inter (figures, covers); Calibri/Arial or their metric twins Carlito/Liberation (documents)
# Claude Code: https://code.claude.com  (run `claude` in the repo root)
```

When you start Claude Code in the repo root, it reads `CLAUDE.md`, which points it to `CONTEXT.md` and `MEMORY.md`.

## 2. Close the evidence gaps

| Step | Command or prompt | Result |
|---|---|---|
| 2.1 Re-fetch blocked sources | `python3 -I tools/refetch_sources.py . --types primary-trust-centre,regulatory,primary-docs` (add `--dry-run` first; `--stream A5` to limit) | Direct snapshots or PDF originals for the 798 `extract` and 2 `link-only` sources (as of CP5); `work/gapfill/refetch_report.md` |
| 2.2 List unverified facts | `python3 -I tools/npv_report.py .` | `work/gapfill/npv_cells.csv`, `npv_by_product.md` (1,557 cells at CP5) |
| 2.3 Primary-source gap-fill | In Claude Code, run prompt **G1** from `work/prompts/gapfill_desktop_prompts.md`, once per stream. Agents can run in parallel; there is no shared search cap. | Facts upgraded to `conf: high`, or corrected |
| 2.4 Verifier leftovers | Prompt **G2** | Closes each verification log's §5 items |
| 2.5 Unprofiled products | Prompt **G3** | ServiceNow, OneTrust, Daytona, Modal, Azure AI Search, Vertex Vector Search |
| 2.6 Rebuild | `python3 -I tools/build_dataset.py .`, then `python3 -I tools/diff_tiers.py . <previous-edition commit>` to list tier and score changes against the previous edition | `products.json`/`.xlsx`, `bibliography.xlsx`, the integrity report (expect 0 issues) and `work/refresh/tier_changes.md` |
| 2.7 Re-score | Re-run the Stage B writers for any layer whose evidence changed (prompts in `work/prompts/stageA_prime_and_stageB_prompts.md`), then `python3 -I tools/score.py work/stageB/<L>/assessments.json --write` | Scores reflect the new evidence; the NPV cap is lifted where facts are now verified |
| 2.8 Rebuild the deliverables | `bash tools/rebuild_all.sh` (everything, in order: dataset, tag check, diagrams, LinkedIn visuals, stack graphic, explorer, LinkedIn document, deck, master, print and Kindle edition, appendix; Word documents only, no PDF from any .docx and no ZIP). `bash tools/rebuild_all.sh --quick` also skips the deck PDF and the print edition. Update `tools/deck/tiers.json` and slide text first if tiers changed | Refreshed `01_Report` … `08_Graphic`, `01_Report/Print/` |
| 2.9 Update the synthesis and the views | If a tier changed, ask Claude Code to update `work/stageC/synthesis.md` (Parts I, VII and XI) and, after `python3 -I tools/build_views.py .`, the six view Parts (`work/stageE/views/<VIEW>/view.md`, prompt R4b in `work/prompts/refresh_prompts.md`) to match, run `python3 -I tools/check_tags.py . work/stageC/synthesis.md`, then repeat 2.8 | Report, explorer and deck agree with the new scores |
| 2.10 Commit | No ZIP: push every file. `git add -A && git commit -m "Desktop gap-fill" && git push origin claude/nice-meitner-0me752` | |

**Rules still apply:**
- Never work around paywalls or logins.
- Keep the earlier extract files. `refetch_sources.py` keeps them and records both paths.

## 2b. Edit text, figures or the book

Every deliverable is generated, so edit the source and rebuild (`bash tools/rebuild_all.sh`, or the single command shown):

| To change | Edit | Then run |
|---|---|---|
| Report text | `work/stageC/synthesis.md` (Parts I, III–XII), `work/stageB/<L1…C8>/section.md` (chapters), `work/stageD/method.md` (Part II) | `python3 -I tools/check_tags.py . <file>` then `python3 -I tools/build_master.py .` |
| A chapter diagram | `Enterprise_GenAI_Stack_Oct2026/08_Graphic/diagrams/<L1-1…C8-2>.md` (Mermaid) | `NODE_PATH=$(npm root -g) node tools/render_diagrams.js <file.md>` |
| A LinkedIn post visual | `08_Graphic/linkedin/P<NN>.md` (HTML fragment or Mermaid; P00 is the series introduction) | `NODE_PATH=$(npm root -g) node tools/render_post_visuals.js <file.md>` |
| A LinkedIn post | `work/stageC2/linkedin_series.md` (also update the matching book chapter's "The post") | `python3 -I tools/build_linkedin_calendar.py .` then `python3 -I tools/build_linkedin_book.py .` |
| The worked example's build steps | `work/stageC2/worked_example_build.json` | `python3 -I tools/sync_worked_example.py .`, then re-render the post visuals and rebuild the calendar and the book |
| A book chapter | `work/stageF/linkedin_book/chapters/chNN.md` (book metadata: `tools/print/linkedin_book.json`) | `python3 -I tools/check_tags.py . <file>` then `python3 -I tools/build_linkedin_book.py .` |
| The stack graphic | `08_Graphic/Enterprise_GenAI_Stack_Oct2026.md` | `python3 -I tools/build_stack_graphic.py .` then `node tools/render_graphic.js …` (see `REFRESH_QUARTERLY.md` §6) |
| The one-page architecture | `08_Graphic/Architecture_One_Page.html` | `node tools/render_graphic.js` on it |
| Book title, author, ISBNs, blurb, trim, margins | `tools/print/book.json` | `python3 -I tools/build_print_edition.py .` (after `build_master.py`); read `01_Report/Print/Build_Summary.md` and `Publishing_Kit.md` |
| Word styling and branding | `tools/make_reference_docx.py` (writes `tools/templates/reference.docx`) | rebuild the documents |

Where each section lives (one home each): the LinkedIn series is only in `07_LinkedIn`; product fact sheets are only in `02_Appendix`. The old tile-by-tile table against the original diagram is provenance only (`work/stageD/archive/diagram_provenance.xlsx`); it is not a deliverable and is not rebuilt in a re-run.

## 3. Resume the pipeline

Check `MEMORY.md` → "Current position" for the latest checkpoint. Then, in Claude Code:

```text
Read CONTEXT.md and MEMORY.md. Continue the plan from the current position, following
inputs/Execution_Prompt_GenAI_Stack.md and the CP decisions recorded in checkpoints/. Stop at the next checkpoint.
```

## 4. Re-run from scratch, stage by stage

| Stage | Inputs | Prompts | Outputs |
|---|---|---|---|
| 0 Baseline | `inputs/*` | Done by the lead. Files in `work/stage0/` 01–06 can be reused as they are. | `work/stage0/` |
| A Research | `work/stage0/05_stageA_research_brief.md` | `work/prompts/stageA_research_prompts.md` (8 agents in parallel), then `stageA_followup_prompts.md` if any gaps remain | `work/stageA/<stream>/` |
| A′ Verify | `work/stage0/06_stageA_prime_verify_brief.md` | `work/prompts/stageA_prime_and_stageB_prompts.md` (V1, V2) | `work/stageA_verify/V1`, `V2` |
| Dataset / CP1 | | `tools/build_dataset.py`, `tools/diff_tiers.py` (provenance only: `tools/build_what_changed.py`, `tools/build_cp1_what_changed.py`) | `05_Data`, `06_References`, `work/refresh/` (provenance: `work/stageD/archive/`) |
| B Write | `work/stage0/07_stageB_writer_brief.md`, `08_scoring_rubric.md` | `work/prompts/stageA_prime_and_stageB_prompts.md` (writer prompts) | `work/stageB/<layer>/` |
| C, C2, D | Plan §12, §15, §14 | To be recorded in `MEMORY.md` as each stage runs | |
| F LinkedIn book | `work/stage0/12_stageF_linkedin_book_brief.md`, `work/stageC2/linkedin_series.md`, `work/stageC2/worked_example_build.json` | `work/prompts/stageF_linkedin_book_prompts.md` (five chapter writers in parallel, five posts each) | `work/stageF/linkedin_book/chapters/ch00–ch32.md` (ch25–ch32 = Part IV, the seven-lenses posts, from the view chapters) → `python3 -I tools/build_linkedin_book.py .` → `07_LinkedIn/Book/` |
| E Further views | `work/stage0/11_stageE_views_brief.md`, `work/stageE/views/views.json` | `work/prompts/stageE_views_prompts.md`: research agents E1 (regulation), E2 (commercial) and E3 (agentic SDLC and agent standards) in parallel, then `python3 -I tools/build_views.py .`, then six view writers (TS, SW, SU, AT, DV, AG) and one reviewer | `work/stageE/E1_regulation/`, `E2_commercial/`, `E3_agents_sdlc/`, `views/<VIEW>/view.md`, `05_Data/views.xlsx`; Parts XIII–XVIII of the master |

**Before re-running from scratch:**
- **Change the date line** in every prompt ("Today is …").
- **Stage A's source IDs restart at S001.** Re-run into a clean branch, or archive the old `work/stageA/` first.
