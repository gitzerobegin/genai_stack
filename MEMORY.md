# MEMORY: run log, current position, blockers

> This is the durable record of everything done in this project, so it can be audited, resumed or re-executed elsewhere. It is updated at every checkpoint.
>
> - Briefing: `CONTEXT.md`
> - Re-running with open internet: `RERUN_ON_DESKTOP.md`
> - Every agent prompt, verbatim: `work/prompts/`

## Current position

| | |
|---|---|
| **Last updated** | 9 October 2026 |
| **Stage** | **CP5 delivered and reworked to the house conventions; print/Kindle edition added** |
| **Branch** | `claude/nice-meitner-0me752` on `github.com/gitzerobegin/genai_stack` |
| **Summary** | `checkpoints/CP5/00_CP5_Summary.md` |

| Item | State |
|---|---|
| CP1–CP4b | Delivered; decisions in `checkpoints/CP1/06_*`, `CP2/03_*`, `CP3/06_*`, `CP4/00_*` |
| Stage B | 17 chapters (presented L1 → L9, then C1–C8; every flow a Mermaid figure in `08_Graphic/diagrams/`); three calibration rounds; final tiers 58 Strategic / 67 Tactical / 13 Experimental / 2 unscored |
| Stage C | `work/stageC/synthesis.md` (Parts I, III–XII, about 28,000 words; Part XII = what changed since the popular stack diagram), reviewed (45 edits, `work/stageC/synthesis_review.md`) |
| Stage C2 | `work/stageC2/linkedin_series.md`: Post 0 (introduction) + 24 posts (weeks run L1 → L9) + 3 reactive templates; a visual per post in `08_Graphic/linkedin/P00–P24`; only home `07_LinkedIn/` |
| Stage D | Master (docx/pdf/md), print and Kindle edition (`01_Report/Print/`), appendix, 28-slide deck, offline explorer, dataset, bibliography, calendar, graphics, ZIP `Enterprise_GenAI_Stack_Oct2026/Enterprise_GenAI_Stack_Oct2026.zip` |
| Claude Doc | Executive summary + synthesis (CP5-2): https://claude.ai/code/artifact/74918687-c7fb-43e9-86fb-c729062bf9c6 |
| CP5 decision | XI.5: the two avoid rows outside the CP4-7 grounds moved to "monitor" (user, 9 October 2026); applied everywhere |
| Rebuild | `bash tools/rebuild_all.sh` rebuilds every deliverable in order (`--quick` skips PDFs) |
| Next | Finish Stage E (research E1–E3 → six view writers → reviewer), then rebuild everything (`bash tools/rebuild_all.sh`), including the print edition. Before selling the book: complete `01_Report/Print/Publishing_Kit.md` §3 (author, ISBNs, AI disclosure, proof copy). User sign-off. Then, optionally, the desktop gap-fill (`RERUN_ON_DESKTOP.md`) and a rebuild. Next edition: `REFRESH_QUARTERLY.md` (baseline commit `79907bd`). After sign-off, enter the series start Tuesday in `Content_Calendar.xlsx` cell E1. |

## Run log

### Session 1: cloud container (claude.ai/code)

| # | When | Step | Result |
|---:|---|---|---|
| 1 | 7 October | Read plan v4.3, the execution prompt and the graphic. Copied them into `inputs/`. | |
| 2 | 7 October | Probed the network | **Blocked:** most hosts (vendor sites, trust centres, regulators, github.com web, nist.gov, eur-lex). **Allowed:** anthropic.com, docs.claude.com, cloud.google.com, pypi.org; later found raw.githubusercontent.com and the npm registry. WebSearch works server-side. WebFetch follows the same egress policy. |
| 3 | 7 October | Wrote `tools/snapshot.py` (direct fetch) and `tools/save_extract.py` (archive a search extract) | |
| 4 | 7 October | **Stage 0:** `work/stage0/01_baseline_inventory.md` (80 tiles, ambiguities A1–A19), `02_dataset_schema.md`, `03_style_guide.md`, `04_hypotheses_and_evidence_plan.md`, `05_stageA_research_brief.md` | Committed |
| 5 | 7 October | First `git push` | **Blocked:** 403, because the Claude GitHub App had read-only access. The user fixed the GitHub access and the push then succeeded. |
| 6 | 7 October | **Stage A:** launched 8 background research agents (prompts in `work/prompts/stageA_research_prompts.md`) | All 8 stopped early: **the WebSearch cap (about 200 calls per turn, shared across agents) ran out** after about 20–25 searches each |
| 7 | 7–8 October | Sent the gap-filling follow-ups (`work/prompts/stageA_followup_prompts.md`) to all 8 agents with SendMessage, which gave a fresh budget | All 8 completed. Remaining gaps are in each `notes.md` §(e). |
| 8 | 8 October | `tools/build_dataset.py`: first merge | 140 products, 20 regulatory records, 942 sources, 0 integrity issues |
| 9 | 8 October | **Stage A′:** verifiers V2 (A5–A8) and V1 (A1–A4) (prompts in `work/prompts/stageA_prime_and_stageB_prompts.md`) | 192 checks: 164 confirmed, 21 corrected, 5 downgraded, 2 unresolvable. **No fabricated claims.** |
| 10 | 8 October | Extended `build_dataset.py` to read the verifier sources. Wrote `tools/build_what_changed.py` and `tools/build_cp1_what_changed.py`, which apply 42 verifier corrections. | 145-row "What changed" table; 1,119 sources |
| 11 | 8 October | **CP1 pack:** `checkpoints/CP1/00–05`, `Enterprise_GenAI_Stack_Oct2026/00_README.md` | Pushed. Stopped for review. |
| 12 | 8 October | The user approved all options (a). Recorded in `checkpoints/CP1/06_CP1_Decisions.md`. | |
| 13 | 8 October | Wrote `work/stage0/07_stageB_writer_brief.md`, `08_scoring_rubric.md` and `tools/score.py`. Extended `build_dataset.py` to overlay `work/stageB/*/assessments.json` and `sources_added.csv`. | |
| 14 | 8 October | **Stage B, tranche 1:** writers for L9, L8 and L7 in parallel (prompts in `work/prompts/stageA_prime_and_stageB_prompts.md`) | L8 done. L9 and L7 running. |
| 15a | 8 October | All three writers done. `tools/check_tags.py` added: all tag IDs resolve. **Calibration issue:** L7 capped enterprise readiness for every hosted vendor, while L9 closed similar gaps by searching. A calibration reviewer was launched over L9–L7 (prompt in the `work/prompts/stageA_prime_and_stageB_prompts.md` appendix). | Reviewer running |
| 15b | 8 October | The calibration reviewer finished. Built the CP2 pack (draft `.md` plus a pandoc `.docx`), rebuilt the dataset (1,151 sources, 0 issues), and pushed. **Stopped for CP2.** | |
| 16 | 8 October | User's CP2 answers recorded. Rubric rules 6–9 and the brief (no length cap, deep-dive format) updated. Launched 8 agents: 1 rework and 7 writers. | Running |
| 17 | 8 October | All 8 tranche-2 agents stopped with an API 429 "session limit" (resets 12:30 UTC) before writing any output. At 18:13 UTC, after the user said "continue", all 8 were resumed with SendMessage (context kept). | Running |
| 18 | 8 October | **Second 429 interruption** (reset 23:10 UTC) hit 5 agents. Saved on disk: complete L6, C1, C3, C5, C6 (sections and assessments); C7 and C8 sections; C2 assessments; L4 and L5 done earlier. At 18:40 UTC, after the user said "continue", resumed only the 3 agents with work left: C2 section, C4 (all), C7 and C8 assessments. | Running |
| 19 | 8 October | Tranche 2 writers all complete: L6, L5, L4, C1–C8 (about 92,000 words; 74 products scored). Built the shared table `work/stageB/_review/all_scores.md`. Launched calibration reviewers A (L6–L4, C1–C2) and B (C3–C8). Tool globs now read `sources_added*.csv`. | Reviewers running |
| 20 | 8 October | Reviewers A and B finished. Built the CP3 pack (pandoc `.docx`); rebuilt the dataset (1,234 sources, 0 issues; 104 scored: 29 Strategic, 67 Tactical, 8 Experimental). **Stopped for CP3.** | |
| 21 | 8 October | CP3 answers recorded (`checkpoints/CP3/06_CP3_Decisions.md`). Rubric rules 10–13 added. Launched the CP3 rework agent and the L3, L2 and L1 writers (prompts in `work/prompts/stageB_tranche3_prompts.md`). | Running |
| 22 | 8 October | **Third 429 interruption** (reset 23:40 UTC) hit all 4 tranche-3 agents early. Only the L2 and L3 search extracts were saved (committed). At 23:42 UTC, after the user confirmed the reset, all 4 were resumed with explicit on-disk status. | Running |
| 23 | 9 October | The CP3 rework finished: tiers moved to 43/53/8. The L3, L2 and L1 writers finished: about 33,400 words; L1 has Anthropic Tactical 3.55 with the conflict-of-interest disclosure; L3 has the Claude Agent SDK as Experimental. The L3 and L1 writers ran git themselves, contrary to the brief; no harm done. Launched the CP4 calibration reviewer C for L3–L1. Wrote the Stage C synthesis brief `work/stage0/09_stageC_synthesis_brief.md`. | Reviewer running |
| 24 | 9 October | The user answered the CP4, CP4b and CP5 questions up front (`checkpoints/CP4/00_CP4_CP4b_Decisions.md`) and chose to run to CP5 without pauses. A fourth 429 interruption (reset 04:40 UTC) was resumed at 05:43. CP4 rework done: 58 Strategic, 67 Tactical, 13 Experimental. LinkedIn posts 1–18 done. Synthesis written through Part IX. Packaging tools built: `tagfmt.py`, `build_master.py` (footnote-style docx, 3,556 footnotes), `build_appendix.py` (docx/pdf, 661 pp), `build_explorer.py` (offline HTML, tested headless), `build_linkedin_calendar.py`, plus pptxgenjs in `tools/deck`. GitHub Release is not possible from this session (no tool; gh token invalid), so the user chose to commit the ZIP on the working branch. | Running |
| 25 | 9 October | Synthesis reviewer finished (45 edits). `build_master.py` now puts the disclosure and final-tier table before the executive summary, numbers the method as Part II and keeps the LinkedIn H1. `tagfmt.py` no longer converts tags inside inline code. New `tools/docx2pdf.py` converts through LibreOffice UNO and refreshes the table of contents (plain `soffice --convert-to` left it empty); master and appendix use it. Claude Doc created with the executive summary and synthesis. Package README, `06_References/originals/README.txt`, CP5 summary and ZIP done. **Stopped at CP5.** | Delivered |
| 26 | 9 October | User decision at CP5: move the two XI.5 rows (Chinese-origin vendors' own APIs for client data; billing intermediation) to the XI.6 monitor list. Applied to the synthesis, the Claude Doc (thread answered), deck slide 16, then rebuilt explorer, master and ZIP. | Delivered |
| 27 | 9 October | At the user's request: wrote `REFRESH_QUARTERLY.md` (quarterly refresh procedure, checkpoints RCP1–RCP3), `work/prompts/refresh_prompts.md` (R0–R6) and `tools/diff_tiers.py` (tier and score changes against a baseline commit; tested). Builders now also read `work/refresh/*/*/sources*.csv` (R<N>- IDs) and `work/gapfill/*/sources*.csv` (G- IDs). | Done |
| 28 | 9 October | At the user's request: drew the corrected stack graphic, `08_Graphic/Enterprise_GenAI_Stack_Oct2026.png` (3200 px wide), `.pdf` and `.html`, generated from `products.json` by `tools/build_stack_graphic.py` and rendered by `tools/render_graphic.js` (Playwright). It has 140 tiles, the control plane, the Part IV layer names and the per-layer corrections, with no logos. ZIP rebuilt. | Done |
| 29 | 9 October | At the user's request: regenerated the stack graphic to show the architecture as it stands. It no longer uses the earlier graphic as a baseline: no "was" labels, corrections, NEW/ACQUIRED/RENAMED tags or "what changed" box, and the 2 unverifiable records are left out. Each layer shows its key design choice; the footer gives the architecture in one sentence. 138 tiles. ZIP rebuilt. | Done |
| 30 | 9 October | At the user's request: the stack graphic is now editable. `08_Graphic/Enterprise_GenAI_Stack_Oct2026.md` is the source (header, planes, layer text, one table row per tile). `tools/build_stack_graphic.py` turns it into the `.html`, which can also be edited directly; `--sync` refreshes tiers from `products.json` and appends new products (tested). PNG and PDF re-rendered with identical text. | Done |
| 31 | 9 October | House conventions set by the user and recorded in `CONTEXT.md`/`CLAUDE.md`: framing "the view at end of Q3 2026", with diagram-relative content only under "What changed since the popular stack diagram" (synthesis Part XII, chapter x.13, one deck slide); layer order L1 → L9 everywhere (`tools/sort_layer_tables.py`; LinkedIn weeks reordered); Veyan branding with the full lockup (`tools/make_brand_assets.py`, `brand/`, branded `reference.docx`, deck theme, explorer, graphics). | Done |
| 32 | 9 October | All 34 ASCII flows in the 17 chapters became Mermaid figures (`08_Graphic/diagrams/<L1-1…C8-2>.md` → `.png`/`.html` via `tools/render_diagrams.js`, mermaid 11.17.2) by four agents; one agent was cut off by a usage limit and resumed. The one-page architecture became `08_Graphic/Architecture_One_Page.html`. Densest figures: L3-2 and C7-2. | Done |
| 33 | 9 October | One home per section: the LinkedIn series and the tile-by-tile what-changed annex were removed from the master (they live in `07_LinkedIn` and `05_Data/what_changed.xlsx`); a duplicated synthesis title block and the IV.1 repeat of the I.2 figure were removed; IV.1 now states the model and XII.5 maps it to the popular stack diagram; stale LinkedIn "pair" references in L1, L3, C7 and C8 rewritten; I.4 references corrected to I.3. | Done |
| 34 | 9 October | LinkedIn Post 0 (series introduction, Week 0 Thursday; word counts checked) and a visual for every post (P00–P24, 1080 × 1350, `tools/render_post_visuals.js`; P02–P24 by four agents, all vendor-neutral, checked by eye). Visuals are embedded in `LinkedIn_Series.docx` and placed in the master's chapters and Parts (`build_master.py` CHAPTER_VIS/SYN_VIS; P17 under 9.13). | Done |
| 35 | 9 October | Print/Kindle edition: `tools/build_print_edition.py` + `tools/print/print_pdf.py` (LibreOffice UNO page styles: 8.5 × 11 in, mirrored margins, recto Part openers, running heads, roman front matter), `tools/print/book.json`, full-wrap cover from the page count, EPUB, `Build_Summary.md` (KDP checks) and `Publishing_Kit.md`. KDP figures came from web-search extracts (kdp.amazon.com not reachable) and are marked to verify. Also: `tools/rebuild_all.sh`; deck theme writer made portable (`tools/deck/apply_theme.js`); `docx2pdf.py` handles .pptx; guides updated. Claude Doc brought in line (IV.1, VI–VIII, XI tables re-ordered, Part XII appended). | Done |
| 36 | 9 October | User request: further views. Stage E set up: `work/stageE/views/views.json` (weights per view over the same criterion scores) and `tools/build_views.py` → `05_Data/views.xlsx`/`.json`, `work/stageE/views/<VIEW>_scores.md`; brief `work/stage0/11_stageE_views_brief.md`; prompts `work/prompts/stageE_views_prompts.md`; master Parts XIII–XVIII; dataset tools read `work/stageE/*` sources and regulatory records. Views: TS technology service provider, SW software product company, SU start-up (adopters); AT AI-tools, DV agentic-SDLC and AG agent-provider start-ups (vendors selling into the enterprise stack). Core candidates by view: FS 45, TS 48, SW 48, SU 57, AT 56, DV 63, AG 56 (of 138). | Running |
| 37 | 9 October | A container restart stopped the print layout and research agents E1 (regulation) and E2 (commercial); E1 and E2 were resumed with the vendor-view scope added; E3 (agentic SDLC landscape, agent standards) launched. All views added to the desktop and quarterly procedures (RERUN 2.9 and stage table, REFRESH R0/R1/R3/R4b, refresh prompts R4b, `rebuild_all.sh`, CONTEXT decision 7, CLAUDE.md). The print layout will be re-run after the view Parts are written. | Running |
| 15 | 8 October | At the user's request: wrote `MEMORY.md`, `CONTEXT.md`, `CLAUDE.md`, `RERUN_ON_DESKTOP.md`, `work/prompts/*`, `tools/npv_report.py` and `tools/refetch_sources.py` | The user asked for GitHub (not Bitbucket) as the destination |

## Blocked or degraded, and how to fix it

| # | Blocker | Impact | Fix |
|---:|---|---|---|
| B1 | **Egress allow-list** in the cloud container | 677 of 1,119 sources are search extracts, not page snapshots. **0 PDF originals.** Confidence is capped at medium for those facts. | On the desktop: `python3 -I tools/refetch_sources.py .` (see `RERUN_ON_DESKTOP.md` §2), or widen Network access in the cloud environment's settings |
| B2 | **WebSearch cap**: about 200 calls per agent turn, shared | Every stream needed a second pass. The verifiers checked 192 claims rather than all of them. | On the desktop, run the G1 and G2 prompts; there is no shared cap |
| B3 | **1,557 of 4,620 product fact cells are "Not publicly verified"** | Mostly start-up certifications, EU regions, SSO/RBAC and pricing. Under CP1 Q2(a), these cap the enterprise-readiness and security scores at 2. | `tools/npv_report.py`, then prompt G1. Re-score the affected layers afterwards. |
| B4 | **No audit report read directly** | All SOC 2, ISO and HIPAA statements are vendor statements or trust-centre listings | Request reports through each vendor's trust centre (an NDA is usually needed); not automatable |
| B5 | GitHub push was 403 at first | Resolved by the user | n/a |
| B6 | No Bitbucket credentials | Not needed: the user chose GitHub | n/a |
| B7 | The Veyans MCP server failed to connect | None; it is not used | n/a |
| B9 | **Account usage limit**: HTTP 429 "session limit" | All 8 tranche-2 agents stopped mid-read; no output lost | Resume agents with SendMessage after the reset time; on the desktop, run fewer agents in parallel if the limit is tight |
| B8 | `cloud.google.com` now redirects to `docs.cloud.google.com` (blocked) | Google facts come from search extracts | Desktop re-fetch |

## Known residual risks (carried forward)

- **Claims the writers must not rely on:** V1 and V2 `verification_log.md` §4.
- **Unchecked items:** V1 and V2 `verification_log.md` §5.
- **Date conflicts still open:**
  - GPT-6 Astra GA status (OpenAI says not GA; AWS says GA on Bedrock)
  - GLM-5.3 release (14 or 18 August)
  - Guardrails AI cutoff (6 or 25 August)
  - OWASP LLM 2026 publication (August or September)
- **Not yet profiled:** ServiceNow AI Control Tower, OneTrust (C8); Daytona, Modal (L4); Azure AI Search, Vertex AI Vector Search (L6).

## Key numbers at CP1

| Measure | Value |
|---|---|
| Records | 140 products (80 graphic tiles, 48 controls, 12 additions) and 20 regulatory records |
| Sources | 1,119, of which 440 are direct snapshots, 677 search extracts and 2 link-only. 92% are primary. |
| Fact-cell labels | 2,740 Verified fact, 113 Reported, 210 Architectural judgement, 1,557 NPV |
| Graphic tiles flagged out of date | 39 of 80 |

## Reproducing the derived files

```bash
python3 -I tools/build_dataset.py .            # 05_Data + bibliography + integrity report
python3 -I tools/build_what_changed.py .       # raw "What changed" rows from notes.md §(a)
python3 -I tools/build_cp1_what_changed.py .   # applies the verifier corrections → checkpoints/CP1/02_*, 05_Data/what_changed.xlsx
python3 -I tools/score.py work/stageB/<L>/assessments.json --write
python3 -I tools/npv_report.py .               # gap list
python3 -I tools/build_explorer.py .           # 04_Explorer/explorer.html (needs the synthesis)
python3 -I tools/build_master.py .             # 01_Report (add --no-pdf to skip the slow PDF step)
python3 -I tools/build_appendix.py .           # 02_Appendix
python3 -I tools/build_linkedin_calendar.py .  # 07_LinkedIn (add --start YYYY-MM-DD to fix dates)
NODE_PATH=$PWD/tools/deck/node_modules node tools/deck/build_deck.js .   # 03_Slides (npm install pptxgenjs@3.12.0 in tools/deck first)
```
