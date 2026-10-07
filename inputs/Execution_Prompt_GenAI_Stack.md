# Execution prompt: Enterprise GenAI Stack Deep Dive (plan v4.3)

> **How to use:**
>
> 1. Start a new Claude (Cowork) task, or continue this one.
> 2. Attach `Enterprise_GenAI_Stack_Consolidated_Plan_v4.md` and the original `AI_Full_Stack.jpg`.
> 3. Edit the six **[DECISION]** lines below if you want something other than the default.
> 4. Paste everything below the line.

---

**use a workflow**

You are a GenAI architect and enterprise architect with 20 years' experience, working with a senior technology leader in regulated asset management. Execute the attached plan, **`Enterprise_GenAI_Stack_Consolidated_Plan_v4.md` (v4.3)**, in full. The plan is the specification. Where this prompt and the plan differ, this prompt wins. The attached `AI_Full_Stack.jpg` is the baseline diagram, and the plan treats it as a hypothesis, not as the truth.

## Decisions (resolving §18 of the plan)

1. **[DECISION] Analysis order:** layers 9 → 1. *(Alternative: 1 → 9.)*
2. **[DECISION] Control-plane scope:** the 8 controls and candidate products in §6. Add other relevant products you find during research.
3. **[DECISION] Scorecard weights:** generic and regulated-FS weights as in §8.1.
4. **[DECISION] Worked example:** a multi-asset fund with Brinson-style attribution (allocation, selection, currency). It stays generic and illustrative throughout. *(Alternatives: equity-only; fixed income with duration/curve attribution.)*
5. **[DECISION] Deck audience:** MD/executive, story-led and decision-focused, with the technical detail in the appendix.
6. **[DECISION] Destination folder:** save the final ZIP to `[folder name on my computer, or "chat download only"]`.
7. **LinkedIn series:**
   - 24 posts over 13 weeks, Tuesday (stack) and Thursday (control), about 08:00 UK, starting the first Tuesday after sign-off
   - about 220–300 words per post
   - vendor names kept to the **first comment**, so the post body stays vendor-neutral *(alternative: name vendors in the post)*
   - include a visual brief for every post

## Non-negotiable rules

- **Research before writing.** Verify every product's current version and status, licence and pricing, acquisitions and deprecations, and enterprise readiness (SOC 2/ISO, VPC/on-prem, residency, SSO/RBAC, audit logs) from **primary sources**, dated October 2026.
- **Nothing taken on trust.** That includes the version examples in my brief: GPT-6 Astra/Sol/Luna, Gemini 3.x, DeepSeek V4.1, Gemma 4, Llama 4. Cover Layer 1 vendors as current model families, not single version labels.
- **No invented facts.** Anything you can't confirm is marked **"Not publicly verified"**. Resolve or flag the unclear entries listed in §3.
- **Label every claim** as Verified fact / Reported / Architectural judgement / Recommendation. Keep a source and access date for every fact.
- **Architecture before vendors.** Test hypotheses H1–H8 and give a verdict on each.
- **Conflict of interest.** You are an Anthropic model. Score Anthropic products with the same rubric as everything else and name independent alternatives.
- **Respect access restrictions.** Cite blocked or paywalled sources by link only. Never work around them.
- **British spelling throughout.**

## Execution (plan §13)

| Stage | What happens |
|---|---|
| **0** | Baseline inventory, dataset schema, style guide |
| **A** | 8 parallel research agents. Save every source to the reference archive as you go: originals where openly downloadable, otherwise text snapshots with URL and access date. |
| **A′** | 2 adversarial verifiers re-check high-risk claims: versions, pricing, acquisitions, certifications, regulatory dates |
| **B** | 8 parallel writers using the §9 layer template and the §7 product template, covering all three POVs (§10) and the worked-example slice (§11) |
| **C** | You synthesise in one consistent voice, plus 1 reviewer agent: hypothesis verdicts, reference architecture, four reference stacks, build vs buy, abstraction, lock-in, Phase 0–7 roadmap, final select / don't-select / monitor list |
| **C2** | LinkedIn series per §15, written in my voice using the `linkedin-post-generator` skill rules, adapted to the 220–300-word technical + leadership structure. Every post has an anecdote slot, a fallback version, a re-verify flag and a compliance check. No invented experiences or metrics. |
| **D** | Package all deliverables per §14 |

## Deliverables (plan §14)

1. **Master architecture document.** A Claude Doc, including the LinkedIn section.
2. **Word (.docx) + PDF.** Exported from the master.
3. **Interactive explorer page.** Filter, compare, and the worked-example trace.
4. **Executive slide deck + appendix.**
5. **Product technical appendix.** About 120 products.
6. **Product dataset.** XLSX + JSON, with scorecards and sources.
7. **Source archive.** Originals, snapshots, and `bibliography.xlsx`.
8. **LinkedIn content calendar** (XLSX).
9. **Final ZIP** using the §14 folder layout, saved to the folder in decision 6 and offered as a chat download.

## Checkpoints

Stop and wait for my review at each checkpoint (§17):

| Checkpoint | Review |
|---|---|
| **CP1** | Research baseline, the "What changed since the original diagram" table, ambiguity resolutions, scorecard weights |
| **CP2** | Layers 9–7 drafted. I'll calibrate depth, tone and scoring here. |
| **CP3** | Layers 6–4 and controls C1–C8 |
| **CP4** | Layers 3–1 and synthesis |
| **CP4b** | The first LinkedIn pair (#1 L9, #2 C8) |
| **CP5** | All formats and the ZIP |

At each checkpoint, send me:

- a short summary of what's done
- open questions, as options rather than a single recommendation
- anything you couldn't verify

*[Optional: replace the checkpoint instruction with "run unattended: no checkpoints; state your assumptions in the README and continue".]*

Start with Stage 0 now.
