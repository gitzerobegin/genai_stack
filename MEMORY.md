# MEMORY: run log, current position, blockers

> This is the durable record of everything done in this project, so it can be audited, resumed or re-executed elsewhere. It is updated at every checkpoint.
>
> - Briefing: `CONTEXT.md`
> - Re-running with open internet: `RERUN_ON_DESKTOP.md`
> - Every agent prompt, verbatim: `work/prompts/`

## Current position

| | |
|---|---|
| **Last updated** | 8 October 2026 |
| **Stage** | **Stage B, tranche 2 in progress** (after CP2 decisions), heading to **Checkpoint 3** |
| **Branch** | `claude/nice-meitner-0me752` on `github.com/gitzerobegin/genai_stack` |

| Item | State |
|---|---|
| CP1 | Delivered. User replied "approved, proceed" (option (a) on Q1–Q8) |
| L8 writer | **Done**: `work/stageB/L8/section.md`, `assessments.json`. Tiers: 2 Strategic, 6 Tactical, 2 Experimental. |
| L9 writer | **Done**: 11 scored (3 Strategic, 8 Tactical); 5 new sources (B-L9-S001…S005) |
| L7 writer | **Done**: 8 scored (1 Strategic, 7 Tactical); EthicalAgents and Ragoos unscored |
| Calibration review | **Done**: 40 changes, 8 caps lifted, 5 kept, 1 added, no tier changes, 27 sources (B-REV-S001…S027). `work/stageB/_review/CP2_review.md` |
| CP2 pack | `checkpoints/CP2/00_CP2_Summary.md`, `01_Draft_Layers_9-7.md`/`.docx`, `02_Calibration_Review.md` |
| CP2 decisions | Q1 hyperscaler presumption; Q2 lenient (any one control lifts the cap to 3); Q3 judgement; Q4 one point below anchor; Q5 no length cap; Q6 L9 deep-dive format, one illustrative scenario per layer. `checkpoints/CP2/03_CP2_Decisions.md`; rubric rules 6–9 |
| Tranche 2 (running) | Rework of L9–L7 **done** (14 score changes, no tier changes; `work/stageB/_review/CP2_rework_log.md`); writers for L6, L5, L4, C1+C2, C3+C4, C5+C6, C7+C8 (prompts in `work/prompts/stageB_tranche2_prompts.md`) |
| Next | Merge, run a calibration reviewer across tranche 2 (and a cross-check of L9–L7), build the CP3 pack, push, **stop at CP3** |
| After CP2 | Stage B tranche 2: L6, L5, L4 and C1–C8, then **CP3**. Tranche 3: L3, L2, L1 and Stage C synthesis, then **CP4**. Then C2 LinkedIn pair 1–2 (**CP4b**), the rest of C2, and Stage D packaging (**CP5**). |

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
```
