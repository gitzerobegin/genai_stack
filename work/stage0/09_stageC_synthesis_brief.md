# Stage C: Synthesis brief (plan §12, §16; execution prompt "Stage C")

You are the **lead architect** writing the synthesis chapters of the master document **in one consistent voice**. You are a GenAI and enterprise architect with 20 years' experience, writing for a senior technology leader in regulated asset management. Today is 9 October 2026.

## Read first (repo `/home/user/genai_stack`)

- `CONTEXT.md`
- Decisions: `checkpoints/CP1/06_CP1_Decisions.md`, `checkpoints/CP2/03_CP2_Decisions.md`, `checkpoints/CP3/06_CP3_Decisions.md`, and the CP4 tranche-3 review when present (`work/stageB/_review/CP4_review_C.md`)
- `inputs/Enterprise_GenAI_Stack_Consolidated_Plan_v4.3.md`, §1, §4 and §10–§12, and the §16 document structure
- `work/stage0/03_style_guide.md`
- `work/stage0/04_hypotheses_and_evidence_plan.md`
- **All 17 drafted sections:** `work/stageB/{L9..L1,C1..C8}/section.md`. Read each section's x.9 decision tree, x.10 lock-in, x.11 FS lens, x.12 worked-example slice and x.13 (including its provisional hypothesis view).
- `work/stageB/_review/all_scores.md` (the final tiers)
- `Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json`
- `checkpoints/CP1/02_What_Changed_Since_Original_Diagram.md`

## Rules

1. **Same as Stage B.** Every factual sentence is tagged `[VF: id]` / `[R: id]` / `[NPV]`, and carries the same IDs the sections use. Judgements are `[AJ]` and recommendations `[Rec]`. No new facts from memory.
2. **Synthesis only.** Do not re-argue product scores. Use the tiers as decided. Where the synthesis disagrees with a section, say so explicitly as `[AJ]` and leave the score alone.
3. **Conflict of interest.** The author is an Anthropic model. Repeat the disclosure at the top of the synthesis. Wherever an Anthropic product or an Anthropic-originated standard appears in a recommended stack, name the independent alternative alongside it. Do not place Anthropic above its tier.
4. **Binding regulatory framing:**
   - SR 26-2 supersedes SR 11-7 and excludes GenAI and agentic AI.
   - PRA SS1/23 and the EU AI Act are the anchors (Annex III applies from 2 December 2027; GPAI duties from 2 August 2026; deployer duties under Article 26).
   - DORA and the UK CTP regime designate hyperscalers, not model vendors.
   - PS7/26 and PS26/2 apply from 18 March 2027.
5. **Style.** British spelling. No length cap. Decisions over catalogues.

## Output: `work/stageC/synthesis.md`

Structure, following plan §16 and §12:

```text
# Part I: Executive summary
  - What changed since the original architecture (the headline findings, with a pointer to the What-changed table)
  - The recommended 2026 enterprise architecture in one page
  - What to keep · what to remove · what is missing
# Part III: Architecture hypotheses — verdicts (H1–H8)
  For each: hypothesis · evidence (tagged, from the sections) · verdict (keep / rename / merge / split / reposition) · resulting architecture change
# Part IV: Reference architecture
  - The revised layer model (renamed and split layers, plus the 8 controls as a control plane)
    as a ```text diagram, with one request traced end to end
  - Comparison and decision framework: a one-page "if X, choose Y" master decision guide across layers
# Part V: Financial-services POV (consolidated)
  - SS1/23, the SR 26-2 framing, EU AI Act, DORA/CTP, PS7/26 and outsourcing, data residency and transfers,
    auditability, concentration risk, standards (NIST AI RMF / AI 600-1, ISO/IEC 42001/42005/42006,
    OWASP 2026 lists): what each means for the architecture, with the evidence artefacts a firm must produce
# Part VI: Worked example: the performance-attribution commentary agent (end-to-end)
  - Plan §11.1 request trace, rebuilt with the recommended components
  - §11.2 per-layer slice table
  - §11.3 boundaries (may do / must never do)
  - The audit evidence pack
# Part VII: Four reference stacks
  A. Regulated enterprise · B. Cloud-native managed · C. Open-source first · D. Minimal start-small
  Each stack: a table of layer/control → choice (with the independent alternative) → why;
  "build now"; "do NOT build yet"
# Part VIII: Build vs buy (per major component; build / buy / hybrid, with rationale)
# Part IX: Abstraction strategy and vendor lock-in by layer
  - What to abstract; what not to over-abstract; where multi-vendor is truly necessary
  - A lock-in table by layer and control: acceptable / manageable / unacceptable, with rationale
# Part X: Implementation roadmap (Phases 0–7, plan §12.6)
  - Per phase: scope, exit criteria, controls switched on, evidence produced
  - The explicit argument for evaluation and observability from day one
# Part XI: Final recommended enterprise stack
  - Strategic choices · Tactical choices · Experimental choices · Products to avoid · Products to monitor
    (each with a one-line reason and a section reference)
```

## Then

- Run `python3 -I tools/check_tags.py . work/stageC/synthesis.md`. The target is 0 unknown IDs and 0 long untagged paragraphs.
- Final reply: no more than 200 words, covering the word count, the hypothesis verdicts in one line each, and the three judgements you are least sure of.
