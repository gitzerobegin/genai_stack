# LinkedIn thought-leadership series: the enterprise GenAI stack, layer by layer

**Author:** Bing Zhang · **Drafted:** 9 October 2026 · **Status:** weeks 1–9 drafted (posts #1–#18); weeks 10–13 and reactive templates to follow after the synthesis

## Series introduction

**Purpose.** A 13-week series that turns the Enterprise GenAI Full-Stack Architecture Review into a public body of work. Each week pairs one stack layer with the control that makes it safe in production. The aim is to show judgement rather than vendor knowledge: the trade-offs, the operating-model decisions and the evidence a regulated firm needs. One generic worked example runs through every post: an agent that drafts the monthly Brinson-style performance-attribution commentary for a multi-asset fund, with a portfolio manager approving every draft.

**Cadence.** Two posts a week, at about 08:00 UK time. **Tuesday** is the stack post and **Thursday** is the control post. The series starts on the **first Tuesday after CP5 sign-off**. Dates are filled in at sign-off; each post below is labelled "Week N, Tuesday/Thursday". Week 13 is a buffer for a reactive post or a slipped week.

**How to use the anecdote slots.**
- Each full post has one bracketed line, `[Anecdote slot: …]`, where the "honest part" goes. It is sized for one or two sentences (about 25–35 words), so replacing it keeps the post within 220–300 words.
- Use only a real experience of your own: a mistake you own, or credit to the people who did the work. The prompt under each post says what kind of story fits. Keep it free of internal system names, client details and real internal metrics.
- If you have no suitable story, post the **fallback version**. It is complete as it stands and needs no personal story.
- The **short variant** also stands alone. Use it for a lighter week or a repost.
- Hashtags are listed separately. Add them as the last line of whichever version you post.

**Compliance note (applies to every post).**
- These are **personal views**. They do not imply employer endorsement or describe any firm's actual vendor choices.
- No confidential or internal information: no internal systems, client data, programme names or real internal metrics.
- The worked example is **generic and illustrative**. It does not describe any real firm's platform.
- Post bodies are **vendor-neutral**. Vendor and product names appear **only in the first comment**, and every vendor is treated in the same factual way.
- No pre-clearance is needed (CP4b), but keep the per-post compliance check.

**Conflict of interest.** The drafts were prepared with help from an AI model made by Anthropic. Post bodies name no vendor. In first comments, Anthropic products (Claude, the Claude Agent SDK, MCP's origin, Agent Skills) are listed in the same way as every other vendor's. Whether to say in the first comment of post #1 that you used AI drafting assistance is your choice. A suggested line is given there.

**Sourcing.** Every fact in a post traces to a chapter of the review (`work/stageB/<layer>/section.md`) or to `Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json`. The section and source IDs are in each first comment. Numbers marked as targets are starting points from the review's KPI tables, not industry benchmarks. Illustrative scenarios from the chapters are not used as if they were real incidents.

**Re-verify before posting.** Over three months, versions, ownership, prices and regulatory dates move. Check each post's "Re-verify" list in the week before it goes out.

**Word counts.** Each full post and fallback version is 220–300 words, including the anecdote slot as drafted. Each short variant is 120–150 words. These were checked with a script (see the end of this file).

### Calendar, weeks 1–9

| Week | Tuesday (stack) | Thursday (control) |
|---|---|---|
| 1 | #1 L9 Evaluation and observability | #2 C8 Model risk, governance and audit |
| 2 | #3 L8 Ingestion | #4 C3 DLP and PII |
| 3 | #5 L7 Embeddings and reranking | #6 C5 Prompt and configuration management |
| 4 | #7 L6 Retrieval stores | #8 C7 AI security |
| 5 | #9 L4 Tools and protocols | #10 C4 Agent identity and access |
| 6 | #11 L3 Orchestration | #12 C2 Guardrails |
| 7 | #13 L2 Inference and access | #14 C1 AI gateway |
| 8 | #15 L1 Foundation models | #16 C6 AI FinOps |
| 9 | #17 L5 Memory (deliberately last) | #18 Regulated reality: EU AI Act and DORA |

---

## Week 1

### Post 1 · Week 1, Tuesday · L9 Evaluation and observability

**Pair:** Post 2 (C8, Week 1 Thursday). **Bridge:** Tuesday argues that evaluation must exist from day one; Thursday shows that the same eval suite, run independently and kept, is the validation evidence a model-risk function needs.

**Theme and source:** Evaluation and observability as a cross-cutting plane, not a downstream box. `work/stageB/L9/section.md` (executive summary, §9.2, §9.3, §9.9, §9.11–§9.13).

**Tension:** The layer that ages slowest is the one most teams build last, and evals added after go-live measure the damage, not the quality.

#### Full post

Most diagrams of the AI stack put evaluation in the last box. It is the layer that ages slowest — and the one most teams build last.

That ordering is the trap. Evals added after go-live measure the damage, not the quality. When a drafted figure turns out to be wrong, the question becomes which outputs were affected, and nobody can answer it if the prompt version was never recorded and the traces expired on a vendor's free tier.

Over the next three months I will walk through the enterprise GenAI stack one layer at a time, each paired with the control that makes it safe in production. I am starting here deliberately.

Evaluation and observability are not a box at the end. They are a plane across the whole stack. Instrument once, on an open telemetry standard, and keep the evaluation harness and the evidence store in your own hands. The products on top are replaceable: five of the eleven assessed in this space now belong to, or are being bought by, larger platform vendors.

The one signal I would start with is numeric faithfulness: the share of figures in a generated draft that match the authoritative source under an agreed rounding rule. The target is 100%, and any miss blocks the release. A language-model judge does not get a vote on numbers.

The leadership move is sequencing. Fund the eval suite before the first feature, and run it on every change of model, prompt or index.

[Anecdote slot: one or two sentences on a quality problem that surfaced late because nobody was measuring it, and what you or the team changed afterwards.]

Diagrams keep changing. What you measured, and can still prove, is what lasts.

#### Short variant

Most diagrams of the AI stack put evaluation in the last box. It is the layer that ages slowest, and the one most teams build last.

Evals added after go-live measure the damage, not the quality. When a drafted figure turns out to be wrong, the real question is which outputs were affected. Without recorded prompt versions and retained traces, nobody can answer it.

Treat evaluation as a plane across the stack, not a downstream box. Instrument once, on an open standard. Own the eval harness and the evidence store; the tools on top are replaceable.

The signal I would start with is numeric faithfulness: every figure in a draft matches the authoritative source, or the release is blocked.

Fund the eval suite before the first feature. Diagrams keep changing. What you measured, and can still prove, is what lasts.

#### Anecdote slot

- **Where:** the bracketed line before the closing paragraph (the "honest part").
- **Prompt:** a time a quality or data problem was found late, by a user, an auditor or a reviewer, because measurement was added after launch. What did it cost to reconstruct what had happened? What did you change: an earlier test, a retained record, a release gate? Own the decision you would make differently, or credit the person who pushed for measurement first.
- **Fits:** a delivery or platform story from any era, not necessarily AI. A reporting, data-quality or release-testing lesson works well.
- **Avoid:** internal system names, real defect counts, client impact details.

#### Fallback version

Most diagrams of the AI stack put evaluation in the last box. It is the layer that ages slowest — and the one most teams build last.

That ordering is the trap. Evals added after go-live measure the damage, not the quality. When a drafted figure turns out to be wrong, the question becomes which outputs were affected, and nobody can answer it if the prompt version was never recorded and the traces expired on a vendor's free tier.

This series walks through the enterprise GenAI stack one layer at a time, each paired with the control that makes it safe in production. It starts here deliberately.

Evaluation and observability are not a box at the end. They are a plane across the whole stack. Instrument once, on an open telemetry standard, and keep the evaluation harness and the evidence store in your own hands. The products on top are replaceable: five of the eleven assessed in this space now belong to, or are being bought by, larger platform vendors.

The one signal worth starting with is numeric faithfulness: the share of figures in a generated draft that match the authoritative source under an agreed rounding rule. The target is 100%, and any miss blocks the release. A language-model judge does not get a vote on numbers.

The leadership move is sequencing. Fund the eval suite before the first feature, and run it on every change of model, prompt or index.

The honest caveat: the shared telemetry conventions for GenAI are still marked as in development. That is an argument for owning the harness, not for waiting.

Diagrams keep changing. What you measured, and can still prove, is what lasts.

#### Suggested visual

Two-panel diagram. Left: the original nine-layer stack with "Evals and observability" as the last box. Right: the same stack with evaluation and observability redrawn as a vertical plane running alongside every layer, labelled "firm-owned telemetry and evidence spine", with products drawn as replaceable plug-ins. A small callout shows the one metric: "Numeric faithfulness: 100%, any miss blocks." Source: L9 §9.13 and the H8 provisional view.

#### First comment

Personal views. Notes and sources for this post: the Enterprise GenAI Stack review, L9 Evaluation and observability (executive summary, §9.3 KPIs, §9.9 decision tree, §9.13).
- Ownership changes behind "five of the eleven": Dynatrace completed its acquisition of Arize (Phoenix and AX) on 1 October 2026 [A1-S045, V1-S005]; ClickHouse announced its acquisition of Langfuse on 16 January 2026 [A1-S021, V2-S041]; OpenAI announced its acquisition of Promptfoo on 9 March 2026, with no closing date published [A1-S024, V1-S006]; W&B Weave has been part of CoreWeave since 5 May 2025 [A1-S131].
- OpenTelemetry GenAI semantic conventions are at "Development" status [A1-S058].
- Products assessed in this layer: Langfuse, LangSmith, MLflow, Braintrust, Arize Phoenix and AX, DeepEval, Promptfoo, Opik, Datadog Agent Observability, W&B Weave. The pattern matters more than the pick: one platform of record, plus two CI red-team tools, one of them independent of any model vendor.
- Optional disclosure line: "I used an AI drafting assistant (Anthropic's Claude) to help structure this series; the views and the edits are mine."

#### Hashtags

#AIEvaluation #LLMOps

#### Re-verify before posting

- Arize/Dynatrace completion and the Langfuse/ClickHouse status
- Whether OpenAI's Promptfoo acquisition has closed
- OpenTelemetry GenAI conventions still at "Development"
- The "five of the eleven" count, against the final L9 table

#### Compliance check

- Personal views, no employer reference: yes
- No internal systems or metrics; the 100% target is a review KPI, not a firm figure: yes
- Worked example generic: yes
- Vendors named only in the first comment, with ownership facts stated neutrally: yes

---

### Post 2 · Week 1, Thursday · C8 Model risk, governance and audit

**Pair:** Post 1 (L9, Week 1 Tuesday). **Bridge:** Tuesday's eval suite becomes Thursday's validation evidence, but only if someone independent challenges it, it is versioned, and it is retained.

**Theme and source:** Model-risk governance for LLM systems after SR 26-2's carve-out. `work/stageB/C8/section.md` (executive summary, §C8.2, §C8.3, §C8.9, §C8.11–§C8.13).

**Tension:** Your eval suite *is* your validation evidence. What model-risk discipline means when the "model" is an agent and the main US guidance has stepped aside.

#### Full post

In April, the US supervisory guidance that had shaped model risk management since 2011 was replaced. Its successor, SR 26-2, places generative and agentic AI expressly outside its scope.

It is tempting to read that as relief. It is the opposite. The governance burden has not gone; it has moved to the firm. Each firm now has to write its own standard for LLM systems, and the UK's SS1/23, which is technology-agnostic and covers vendor models, is the most complete benchmark to write it against.

Here is what makes it tractable. Much of the validation evidence already exists if Tuesday's evaluation work is done properly. The eval suite is the validation evidence, on three conditions: someone independent of the developers challenges and extends it; it is versioned with the results it produced; and it is kept beyond any vendor's retention tier. A developer's test suite on its own is development testing, not validation.

The signal I would put in front of a risk committee is validation currency: the share of material use cases whose validation covers the model, prompt, index and tool versions running today. Below 100% means an approval that no longer describes production.

The leadership move is choosing the governed unit. Not the model — the use case, with the foundation model recorded as a vendor component and every version pinned. That one decision makes the inventory, re-validation triggers and audit evidence line up.

[Anecdote slot: one or two sentences on an audit or validation request that exposed a gap between what was approved and what was running, and who closed it.]

Regulation will catch up. The evidence you keep in the meantime is what it will ask for.

#### Short variant

In April, the US guidance that had shaped model risk management since 2011 was replaced. Its successor, SR 26-2, places generative and agentic AI outside its scope.

That is not relief. The burden has moved to the firm, which now writes its own standard. The UK's SS1/23 is the most complete benchmark to write it against.

Much of the evidence already exists. The eval suite is the validation evidence, if someone independent challenges it, it is versioned with its results, and it outlives any vendor's retention tier.

The signal for a risk committee is validation currency: the share of material use cases whose validation covers the versions actually running. Anything below 100% is an approval that no longer describes production.

Govern the use case, not the model. Regulation will catch up; the evidence you keep meanwhile is what it will ask for.

#### Anecdote slot

- **Where:** the bracketed line before the closing paragraph.
- **Prompt:** an audit, validation or regulatory request where the approved artefact and the running system had drifted apart: a different version, a missing record, an approval by email. Who noticed, and who did the work to close it? Credit them by role. If the drift happened on your watch, say what you changed in the operating model rather than in the tooling.
- **Fits:** the "audit outcomes as a symptom of operating-model design" theme. Any technology domain works.
- **Avoid:** audit ratings, finding counts, regulator names linked to your firm.

#### Fallback version

In April, the US supervisory guidance that had shaped model risk management since 2011 was replaced. Its successor, SR 26-2, places generative and agentic AI expressly outside its scope.

It is tempting to read that as relief. It is the opposite. The governance burden has not gone; it has moved to the firm. Each firm now has to write its own standard for LLM systems, and the UK's SS1/23, which is technology-agnostic and covers vendor models, is the most complete benchmark to write it against.

Here is what makes it tractable. Much of the validation evidence already exists if the evaluation work is done properly. The eval suite is the validation evidence, on three conditions: someone independent of the developers challenges and extends it; it is versioned with the results it produced; and it is kept beyond any vendor's retention tier. A developer's test suite on its own is development testing, not validation.

The signal worth putting in front of a risk committee is validation currency: the share of material use cases whose validation covers the model, prompt, index and tool versions running today. Below 100% means an approval that no longer describes production.

The leadership move is choosing the governed unit. Not the model — the use case, with the foundation model recorded as a vendor component and every version pinned. That one decision makes the inventory, re-validation triggers and audit evidence line up.

The honest caveat: on public evidence, no governance platform yet does this end to end. The inventory schema and the evidence store are things a firm owns, whatever it buys.

Regulation will catch up. The evidence you keep in the meantime is what it will ask for.

#### Suggested visual

One-page "evidence pack" graphic for the worked example: eight tiles (prompt version, model version, data snapshot, tool calls, eval results, approver identity, timestamps, final output), all keyed to one trace ID and feeding an immutable archive. A side panel shows "governed unit = use case" with the model as a vendor component. Source: C8 §C8.12.

#### First comment

Personal views. Sources: the Enterprise GenAI Stack review, C8 Model risk, governance and auditability (§C8.3 KPIs, §C8.11 regulated FS lens, §C8.12 worked example).
- SR 26-2 / OCC Bulletin 2026-13 / FDIC FIL-15-2026, issued 17 April 2026, supersede SR 11-7 and exclude generative and agentic AI [R-US-MRM: A8-S001, A8-S002, V2-S049]. The agencies' planned AI request for information had not been published as of 7 October 2026 [A8-S003, A8-S007].
- PRA SS1/23: technology-agnostic, covers vendor models, five principles [R-PRA-SS123: A8-S008, A8-S061].
- Governance workflow tools assessed (none reaches Strategic on public evidence): ValidMind, IBM watsonx.governance, Credo AI, Collibra AI Governance (trail ML acquisition announced 5 October 2026), ModelOp. OpenLineage is the recommended lineage standard.

#### Hashtags

#ModelRisk #AIGovernance

#### Re-verify before posting

- SR 26-2 status, and whether the agencies' AI/GenAI request for information has been published (update the post if it has)
- SS1/23 scope statements
- Collibra–trail ML completion

#### Compliance check

- Personal views; no statement about any firm's MRM framework: yes
- No internal audit details: yes (anecdote prompt warns against them)
- Worked example generic: yes
- Vendors named only in the first comment, evenly: yes

---
