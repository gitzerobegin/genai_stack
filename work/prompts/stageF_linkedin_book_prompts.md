# Stage F prompts: the LinkedIn series as a book (verbatim, run 10 October 2026)

Brief: `work/stage0/12_stageF_linkedin_book_brief.md`. Five writers ran in parallel, five posts each; then `python3 -I tools/build_linkedin_book.py .`.

## Book chapters 00-04

```text
You are a chapter writer for a book based on a LinkedIn thought-leadership series about the enterprise GenAI stack. Repo: /home/user/genai_stack. Today is 10 October 2026.

Your chapters are posts 0, 1, 2, 3 and 4. Write each to work/stageF/linkedin_book/chapters/chNN.md, where NN is the two-digit post number. Post 0 becomes the Introduction, so use the heading "## Introduction: <headline>".

Read these first:
1. work/stage0/12_stageF_linkedin_book_brief.md. This is the brief: the chapter template, length and rules. Follow it exactly.
2. CONTEXT.md. Its rules apply: never use training memory as a fact source; label every claim; use British spelling; follow the conflict-of-interest rule.
3. work/stageC2/linkedin_series.md, for your posts. From each post use:
   - the "Fallback version", verbatim as "The post", minus the hashtags;
   - "Theme and source" and "Tension";
   - the "First comment", which lists the facts and source IDs behind the post;
   - the "Suggested visual".
4. The visual sources, Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.md. The "# Title" line is the figure title and the "Caption:" line is the caption.
5. The evidence each post draws on:
   - work/stageB/<L#|C#>/section.md for posts 1 to 18;
   - work/stageC/synthesis.md for posts 0 and 19 to 24.

   Facts and source IDs are tagged inline there ([VF: id], [R: id]). Reuse those tags exactly and do not invent IDs. IDs from Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json (e.g. R-EUAIA) are also valid.

Voice: Bing Zhang. Calm, senior, specific and understated, in short, varied sentences. Credit teams.
- No hype words ("game-changer", "excited", "thrilled"), no emoji and no engagement bait.
- No invented personal anecdotes or metrics.
- Write for a thoughtful technology or risk leader who has not read the review.
- "Behind the post" may name vendors and products, treated even-handedly. Wherever an Anthropic product or standard is named, name an independent alternative beside it.

Each chapter must stand alone. Do not mention weekdays, posting days, "this week", "next post" or the posting schedule. To point to another chapter, write "Chapter N".

After writing each chapter:
- run `python3 -I tools/check_tags.py . work/stageF/linkedin_book/chapters/chNN.md`. It must show no unknown source IDs and no long untagged paragraphs; fix anything it reports and re-run;
- check the word count: 1,700–2,300 words per chapter, or 1,500–2,000 for the Introduction.

Do not edit any other file and do not run git.

Report back, for each chapter: the title, word count, tag counts, and any place where the evidence was thin.
```

## Book chapters 05-09

```text
You are a chapter writer for a book based on a LinkedIn thought-leadership series about the enterprise GenAI stack. Repo: /home/user/genai_stack. Today is 10 October 2026.

Your chapters are posts 5, 6, 7, 8 and 9. Write each one to work/stageF/linkedin_book/chapters/chNN.md, where NN is the two-digit post number.

Read these first:
1. work/stage0/12_stageF_linkedin_book_brief.md. This is your brief: the chapter template, the length and the rules. Follow it exactly.
2. CONTEXT.md. Its rules apply: never use training memory as a fact source; label every claim; use British spelling; follow the conflict-of-interest rule.
3. work/stageC2/linkedin_series.md, for your posts. From each post use:
   - the "Fallback version", verbatim as "The post", minus hashtags;
   - "Theme and source" and "Tension";
   - the "First comment", which lists the facts and source IDs behind the post;
   - the "Suggested visual".
4. The visual sources, Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.md. The "# Title" line is the figure title and the "Caption:" line is the caption.
5. The evidence each post draws on: work/stageB/<L#|C#>/section.md for posts 1–18, and work/stageC/synthesis.md for posts 0 and 19–24.
   - Facts and source IDs are tagged inline there ([VF: id], [R: id]). Reuse those tags exactly and never invent IDs.
   - IDs from Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json (for example R-EUAIA) are also valid.

Voice: Bing Zhang. Calm, senior, specific and understated, with short, varied sentences. Credit teams.
- No hype words ("game-changer", "excited", "thrilled"), no emoji and no engagement bait.
- No invented personal anecdotes or metrics.
- Write for a thoughtful technology or risk leader who has not read the review.
- "Behind the post" may name vendors and products, treated even-handedly. Wherever an Anthropic product or standard is named, name an independent alternative beside it.

Each chapter must stand alone. Do not mention weekdays, posting days, "this week", "next post" or the posting schedule. To point to another chapter, write "Chapter N".

After writing each chapter:
- Run `python3 -I tools/check_tags.py . work/stageF/linkedin_book/chapters/chNN.md`. It must report no unknown source IDs and no long untagged paragraphs. Fix anything it flags and run it again.
- Check the length: 1,700–2,300 words per chapter.

Do not edit any other file and do not run git.

Report back, for each chapter: the title, word count, tag counts, and any place where the evidence was thin.
```

## Book chapters 10-14

```text
You are a chapter writer for a book based on a LinkedIn thought-leadership series about the enterprise GenAI stack. Repo: /home/user/genai_stack. Today is 10 October 2026.

Your chapters are posts 10, 11, 12, 13 and 14. Write each one to work/stageF/linkedin_book/chapters/chNN.md, where NN is the two-digit post number.

Read these first:
1. work/stage0/12_stageF_linkedin_book_brief.md. This is your brief: the chapter template, the length and the rules. Follow it exactly.
2. CONTEXT.md. Its rules apply: never use training memory as a fact source; label every claim; use British spelling; follow the conflict-of-interest rule.
3. work/stageC2/linkedin_series.md, for your posts. From each post use:
   - the "Fallback version", verbatim as "The post", minus hashtags;
   - "Theme and source" and "Tension";
   - the "First comment", which lists the facts and source IDs behind the post;
   - the "Suggested visual".
4. The visual sources, Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.md. The "# Title" line is the figure title and the "Caption:" line is the caption.
5. The evidence each post draws on: work/stageB/<L#|C#>/section.md for posts 1–18, and work/stageC/synthesis.md for posts 0 and 19–24.
   - Facts and source IDs are tagged inline there ([VF: id], [R: id]). Reuse those tags exactly and never invent IDs.
   - IDs from Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json (for example R-EUAIA) are also valid.
   - Post 10 is the regulation chapter. Use regulatory_facts.json and synthesis Part V. Say that it is not legal advice.

Voice: Bing Zhang. Calm, senior, specific and understated, with short, varied sentences. Credit teams.
- No hype words ("game-changer", "excited", "thrilled"), no emoji and no engagement bait.
- No invented personal anecdotes or metrics.
- Write for a thoughtful technology or risk leader who has not read the review.
- "Behind the post" may name vendors and products, treated even-handedly. Wherever an Anthropic product or standard is named, name an independent alternative beside it.

Each chapter must stand alone. Do not mention weekdays, posting days, "this week", "next post" or the posting schedule. To point to another chapter, write "Chapter N".

After writing each chapter:
- Run `python3 -I tools/check_tags.py . work/stageF/linkedin_book/chapters/chNN.md`. It must report no unknown source IDs and no long untagged paragraphs. Fix anything it flags and run it again.
- Check the length: 1,700–2,300 words per chapter.

Do not edit any other file and do not run git.

Report back, for each chapter: the title, word count, tag counts, and any place where the evidence was thin.
```

## Book chapters 15-19

```text
You are a chapter writer for a book based on a LinkedIn thought-leadership series about the enterprise GenAI stack. Repo: /home/user/genai_stack. Today is 10 October 2026.

Your chapters are posts 15, 16, 17, 18 and 19. Write each one to work/stageF/linkedin_book/chapters/chNN.md, where NN is the two-digit post number.

Read these first:
1. work/stage0/12_stageF_linkedin_book_brief.md. This is your brief: the chapter template, the length and the rules. Follow it exactly.
2. CONTEXT.md. Its rules apply: never use training memory as a fact source; label every claim; use British spelling; follow the conflict-of-interest rule.
3. work/stageC2/linkedin_series.md, for your posts. From each post use:
   - the "Fallback version", verbatim as "The post", minus hashtags;
   - "Theme and source" and "Tension";
   - the "First comment", which lists the facts and source IDs behind the post;
   - the "Suggested visual".
4. The visual sources, Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.md. The "# Title" line is the figure title and the "Caption:" line is the caption.
5. The evidence each post draws on: work/stageB/<L#|C#>/section.md for posts 1–18, and work/stageC/synthesis.md for posts 0 and 19–24 (Post 19 draws on Part VI).
   - Facts and source IDs are tagged inline there ([VF: id], [R: id]). Reuse those tags exactly and never invent IDs.
   - IDs from Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json (for example R-EUAIA) are also valid.

Voice: Bing Zhang. Calm, senior, specific and understated, with short, varied sentences. Credit teams.
- No hype words ("game-changer", "excited", "thrilled"), no emoji and no engagement bait.
- No invented personal anecdotes or metrics.
- Write for a thoughtful technology or risk leader who has not read the review.
- "Behind the post" may name vendors and products, treated even-handedly. Wherever an Anthropic product or standard is named, name an independent alternative beside it.

Each chapter must stand alone. Do not mention weekdays, posting days, "this week", "next post" or the posting schedule. To point to another chapter, write "Chapter N".

Chapter 17 (L9): the post contrasts evaluation with "the last box" of the popular stack diagram. Keep that contrast brief. Present the stack as it is at the end of Q3 2026.

After writing each chapter:
- Run `python3 -I tools/check_tags.py . work/stageF/linkedin_book/chapters/chNN.md`. It must report no unknown source IDs and no long untagged paragraphs. Fix anything it flags and run it again.
- Check the length: 1,700–2,300 words per chapter.

Do not edit any other file and do not run git.

Report back, for each chapter: the title, word count, tag counts, and any place where the evidence was thin.
```

## Book chapters 20-24

```text
You are a chapter writer for a book based on a LinkedIn thought-leadership series about the enterprise GenAI stack. Repo: /home/user/genai_stack. Today is 10 October 2026.

Your chapters are posts 20, 21, 22, 23 and 24. Write each one to work/stageF/linkedin_book/chapters/chNN.md, where NN is the two-digit post number.

Read these first:
1. work/stage0/12_stageF_linkedin_book_brief.md. This is your brief: the chapter template, the length and the rules. Follow it exactly.
2. CONTEXT.md. Its rules apply: never use training memory as a fact source; label every claim; use British spelling; follow the conflict-of-interest rule.
3. work/stageC2/linkedin_series.md, for your posts. From each post use:
   - the "Fallback version", verbatim as "The post", minus hashtags;
   - "Theme and source" and "Tension";
   - the "First comment", which lists the facts and source IDs behind the post;
   - the "Suggested visual".
4. The visual sources, Enterprise_GenAI_Stack_Oct2026/08_Graphic/linkedin/P<NN>.md. The "# Title" line is the figure title and the "Caption:" line is the caption.
5. The evidence each post draws on: work/stageC/synthesis.md. Use Parts VII (Stack D), VIII, IX.1–IX.4 and XI, plus the chapters it cites in work/stageB/*/section.md.
   - Facts and source IDs are tagged inline there ([VF: id], [R: id]). Reuse those tags exactly and never invent IDs.
   - IDs from Enterprise_GenAI_Stack_Oct2026/05_Data/regulatory_facts.json (for example R-EUAIA) are also valid.

Voice: Bing Zhang. Calm, senior, specific and understated, with short, varied sentences. Credit teams.
- No hype words ("game-changer", "excited", "thrilled"), no emoji and no engagement bait.
- No invented personal anecdotes or metrics.
- Write for a thoughtful technology or risk leader who has not read the review.
- "Behind the post" may name vendors and products, treated even-handedly. Wherever an Anthropic product or standard is named, name an independent alternative beside it.

Each chapter must stand alone. Do not mention weekdays, posting days, "this week", "next post" or the posting schedule. To point to another chapter, write "Chapter N".

Chapter 24 closes the book. After the chapter template's "In one line" section, add a short "### Where this leaves you" of 200–300 words. It draws the whole argument together: own the control plane and rent the components.

After writing each chapter:
- Run `python3 -I tools/check_tags.py . work/stageF/linkedin_book/chapters/chNN.md`. It must report no unknown source IDs and no long untagged paragraphs. Fix anything it flags and run it again.
- Check the length: 1,700–2,300 words per chapter, or up to 2,600 for chapter 24.

Do not edit any other file and do not run git.

Report back, for each chapter: the title, word count, tag counts, and any place where the evidence was thin.
```

