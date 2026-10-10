# Stage F brief: the LinkedIn series as a book

**Added:** 10 October 2026, at the user's request: "a sellable book in docx format for Amazon based on the LinkedIn posts: Enterprise GenAI stack thought-leadership series".

| | |
|---|---|
| **Working title** | *The Enterprise GenAI Stack, Layer by Layer: a thought-leadership series on building GenAI that regulated firms can trust* (`tools/print/linkedin_book.json`) |
| **Author voice** | Bing Zhang: understated, specific, British spelling, no hype. Credit teams, own mistakes, let numbers speak (`anthropic-skills:linkedin-post-generator` rules). |
| **Source of truth** | `work/stageC2/linkedin_series.md` (Post 0, Posts 1–24 and the seven-lenses Posts 25–32, with their first comments and sources). Evidence comes from the review (for Part IV, the view chapters `work/stageE/views/<V>/view.md`, Parts XIII–XVIII): `work/stageB/<L#/C#>/section.md`, `work/stageC/synthesis.md`, `Enterprise_GenAI_Stack_Oct2026/05_Data/*`. |
| **Format** | 6 × 9 in trade paperback (KDP) and Kindle EPUB. Word (.docx) is the editable master. Built by `tools/build_linkedin_book.py`. |
| **Length** | About 45,000–55,000 words: 25 chapters of about 1,700–2,300 words, plus front and back matter |

## Structure

- **Front matter:** half title, title page, copyright page (with the AI-assistance disclosure), contents, preface, how to read this book.
- **Part I: The argument.** The Introduction, from Post 0.
- **Part II: Nine layers and the controls that make them safe.** Chapters 1–18, from Posts 1–18 in series order. Each layer chapter is followed by the control that pairs with it.
- **Part III: Putting it together.** Chapters 19–24, from Posts 19–24.
- **Part IV: One stack, seven lenses** (added 10 October 2026). Chapters 25–32, from Posts 25–32: an opener, one chapter per other view (TS, SW, SU, AT, DV, AG) and a close on what stays the same. These chapters have no worked-example step; in its place each has "In your lens", tracing what changes for that reader.
- **Back matter:**
  - Appendix A: the series at a glance (chapter, layer or control, the signal to measure, the target);
  - Appendix B: glossary;
  - About the author.

## Each chapter: `work/stageF/linkedin_book/chapters/chNN.md` (NN = post number, 00–32)

```
## <N>. <headline: the post's visual title or its tension, 4–9 words>      (Post 0: "## Introduction: <headline>")

*<Layer or control code and name>, from Post <N> of the series.*

### The post
<the post's fallback version, verbatim: it needs no personal story; no hashtags, no "[Anecdote slot]">

![<visual title>](Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.png){width=4.4in}

*Figure <N>. <visual caption>* [AJ]

### Behind the post
<800–1,100 words: the reasoning and the evidence, drawn from the review's chapter for this layer or control and the synthesis. Explain the mechanism, the trade-off and what changed in 2025–26. Vendor and product names are allowed here, treated even-handedly. Every fact tagged.>

### What good looks like
<150–250 words: the signal (KPI) from the post, how to measure it, and the target, marked as a starting point, not a benchmark.>

### Objections worth taking seriously
<250–350 words: two or three honest counter-arguments, each with an answer.>

### Questions for your team
<5–7 bullets a leader could take into a meeting tomorrow.>

### In one line
<one sentence>
```

## Rules

- **Facts.** Never use training memory as a fact source. Every fact cites an existing source ID from the post's first comment, the chapter or the dataset, in the form `[VF: id]` or `[R: id]`. Judgement is `[AJ]` and advice is `[Rec]`. The build turns tags into footnotes, so in the book they read like a sourced business book.
- **Writing.** No invented anecdotes, client names, internal systems or metrics. The worked example is generic and illustrative.
- **Neutrality.** The author used an AI model made by Anthropic. Wherever an Anthropic product or standard is named, name an independent alternative beside it.
- **Timing.** Never name a weekday or a posting schedule. A chapter must read well on its own, in any order.
- **Style.** British spelling. Order layers L1 → L9, then C1 → C8. No ASCII diagrams.
- **Checks.** Run `python3 -I tools/check_tags.py . <file>`. It must report no unknown source IDs and no long untagged paragraphs.
