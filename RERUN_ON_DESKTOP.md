# Re-running or gap-filling this work on your own desktop

The cloud run was constrained in two ways:

1. **An egress allow-list.** Most vendor, trust-centre and regulator sites, plus github.com, were blocked from direct fetch.
2. **A web-search cap** of about 200 calls per agent turn, shared by all running agents.

A desktop with ordinary internet access removes both. Use it to:

- **upgrade the evidence:** turn search extracts into real snapshots and PDF originals, and close the "Not publicly verified" gaps
- **resume the pipeline** from the latest checkpoint
- **re-run any stage from scratch**

`MEMORY.md` records every step taken and `CONTEXT.md` is the project briefing. All agent prompts are in `work/prompts/`.

## 1. Set-up (once)

```bash
git clone https://github.com/gitzerobegin/genai_stack.git
cd genai_stack
git checkout claude/nice-meitner-0me752      # working branch
python3 -m venv .venv && source .venv/bin/activate
pip install requests beautifulsoup4 openpyxl python-docx python-pptx reportlab pypdf markdownify
# Optional, for the Stage D exports:
#   pandoc
#   LibreOffice (soffice)
# Claude Code: https://code.claude.com  (run `claude` in the repo root)
```

When you start Claude Code in the repo root, it reads `CLAUDE.md`, which points it to `CONTEXT.md` and `MEMORY.md`.

## 2. Close the evidence gaps (recommended before Stage B continues)

| Step | Command or prompt | Result |
|---|---|---|
| 2.1 Re-fetch blocked sources | `python3 -I tools/refetch_sources.py . --types primary-trust-centre,regulatory,primary-docs` (add `--dry-run` first; `--stream A5` to limit) | Direct snapshots or PDF originals for the 677 `extract` and 2 `link-only` sources; `work/gapfill/refetch_report.md` |
| 2.2 List unverified facts | `python3 -I tools/npv_report.py .` | `work/gapfill/npv_cells.csv`, `npv_by_product.md` (1,557 cells at CP1) |
| 2.3 Primary-source gap-fill | In Claude Code, run prompt **G1** from `work/prompts/gapfill_desktop_prompts.md`, once per stream. Agents can run in parallel; there is no shared search cap. | Facts upgraded to `conf: high`, or corrected |
| 2.4 Verifier leftovers | Prompt **G2** | Closes each verification log's §5 items |
| 2.5 Unprofiled products | Prompt **G3** | ServiceNow, OneTrust, Daytona, Modal, Azure AI Search, Vertex Vector Search |
| 2.6 Rebuild | `python3 -I tools/build_dataset.py .` then `python3 -I tools/build_what_changed.py . && python3 -I tools/build_cp1_what_changed.py .` | `products.json`/`.xlsx`, `bibliography.xlsx`, the "What changed" table, and the integrity report (expect 0 issues) |
| 2.7 Re-score | Re-run the Stage B writers for any layer whose evidence changed (prompts in `work/prompts/stageA_prime_and_stageB_prompts.md`), then `python3 -I tools/score.py work/stageB/<L>/assessments.json --write` | Scores reflect the new evidence; the NPV cap is lifted where facts are now verified |
| 2.8 Commit | `git add -A && git commit -m "Desktop gap-fill" && git push origin claude/nice-meitner-0me752` | |

**Rules still apply:**
- Never work around paywalls or logins.
- Keep the earlier extract files. `refetch_sources.py` keeps them and records both paths.

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
| Dataset / CP1 | | `tools/build_dataset.py`, `tools/build_what_changed.py`, `tools/build_cp1_what_changed.py` | `05_Data`, `06_References`, `checkpoints/CP1` |
| B Write | `work/stage0/07_stageB_writer_brief.md`, `08_scoring_rubric.md` | `work/prompts/stageA_prime_and_stageB_prompts.md` (writer prompts) | `work/stageB/<layer>/` |
| C, C2, D | Plan §12, §15, §14 | To be recorded in `MEMORY.md` as each stage runs | |

**Before re-running from scratch:**
- **Change the date line** in every prompt ("Today is …").
- **Stage A's source IDs restart at S001.** Re-run into a clean branch, or archive the old `work/stageA/` first.
