# Stage C2: LinkedIn series brief (plan §15, CP4b decisions)

You write a 24-post LinkedIn series in **Bing Zhang's** voice, in **one consistent voice**. Bing Zhang is the user: a senior technology leader (Executive Director, asset-management technology; AI-native and agentic engineering leadership).

## Inputs (repo `/home/user/genai_stack`)

- `inputs/Enterprise_GenAI_Stack_Consolidated_Plan_v4.3.md` §15: purpose, structure, 13-week design, per-post elements, guardrails and checklist. It is binding, except where the decisions below differ.
- `checkpoints/CP4/00_CP4_CP4b_Decisions.md`:
  - start on the first Tuesday after CP5 sign-off, about 08:00 UK
  - Tuesday is the stack post, Thursday the control post
  - no pre-clearance needed
  - topic-specific hashtags, at most 2
  - vendor names in the first comment only
  - a visual brief for every post
- The source chapters for each post: `work/stageB/<L or C>/section.md`. For weeks 10–12: `work/stageC/synthesis.md`.
- Facts: only those already in the sections or synthesis, with their tags. Put a source pointer in the first comment.

## Bing's voice (from the `linkedin-post-generator` skill; binding)

**The rule that governs everything:** share the lesson, credit the team, let the numbers do the bragging. Never claim brilliance.

| Rule | Detail |
|---|---|
| Spelling | British throughout |
| Register | Understated, senior, calm. Authority comes from specificity. |
| Words to avoid | game-changer, excited, thrilled, humbled, crushing it, 10x |
| Numbers | Stand unadorned. **No invented metrics or experiences.** |
| Credit | Credit the team; own the failure |
| Sentences | Short and varied. Em-dashes for the pivot. Whitespace between short paragraphs. |
| Specificity | Concrete over abstract: name the move, not the virtue |
| Formatting | No emojis. No headers or bullets inside the post. Prose only. |
| Ending | No engagement bait. A quiet, reflective close. |

Signature themes to draw on where relevant:
- AI and agentic transformation in a regulated environment
- making invisible prevention work visible to executives
- audit outcomes as a symptom of operating-model design
- turning external deadlines into refresh mandates
- developing leaders through delivery

## Structure for this series (plan §15.2: technical plus leadership, about 220–300 words)

1. **Hook** (1–2 lines)
2. **The trap** (2–3 lines)
3. **The technical core** (4–6 lines): how the layer or control works, and the ONE metric that shows whether it is "good"
4. **The leadership move** (2–4 lines)
5. **The honest part** (1–2 lines): an owned mistake or credit given. This is where the anecdote slot sits.
6. **Takeaway** (1–2 lines): a quiet invitation to reflect

## Per-post block (plan §15.4)

Write the posts to `work/stageC2/linkedin_series.md`. Each post has these elements:

- Post number, week and day (dates are filled in at sign-off: write "Week N, Tuesday/Thursday")
- Pair link and a bridge sentence
- Theme, with a link to the source section
- Tension (one line)
- **Full post** (220–300 words, ready to paste). It must be **vendor-neutral**, with no product names in the body.
- **Short variant** (120–150 words)
- **Anecdote slot**: a prompt describing what kind of real story fits. Never invent the story.
- **Fallback version**: the full post written as an architectural observation, so it needs no personal story
- **Suggested visual**: a brief for a diagram or carousel drawn from the deck or explorer
- **First comment**: sources, further reading and the vendor names, kept out of the post body
- **Hashtags**: at most 2, specific to the topic
- **Re-verify before posting**: the product, version or regulatory facts in the post
- **Compliance check**: personal views; no confidential information; the worked example is generic; vendors treated even-handedly

## Series order (plan §15.3 table; binding)

| Week | Tuesday | Thursday |
|---|---|---|
| 1 | L9 | C8 |
| 2 | L8 | C3 |
| 3 | L7 | C5 |
| 4 | L6 | C7 |
| 5 | L4 | C4 |
| 6 | L3 | C2 |
| 7 | L2 | C1 |
| 8 | L1 | C6 |
| 9 | L5 Memory | Regulated reality: EU AI Act and DORA |
| 10 | Worked example | Start small |
| 11 | Build vs buy | Where not to abstract |
| 12 | Which lock-in is acceptable | Close: what I'd select and deliberately not select |
| 13 | Buffer | |

Also write **2–3 reactive templates**: a model launch, an acquisition and a regulatory milestone.

## Conflict of interest

The drafting model is Anthropic's. Posts are vendor-neutral in the body. In first comments, treat Anthropic exactly like other vendors.

## Quality checklist (plan §15.6 plus the skill checklist)

Run it on every post, and rewrite anything that fails:
- 220–300 words
- British spelling
- no emojis
- at most 2 hashtags
- no engagement bait
- one measurable signal named
- one leadership decision a reader can apply
- team credit or an owned mistake, or a clear slot for one
- no invented numbers
- links naturally to its pair partner
- facts traceable to the sections
