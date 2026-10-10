# Stage 0: Style guide

This guide applies to every writer, every stage and every deliverable.

## 1. Voice

- **Who is speaking:** a GenAI and enterprise architect with 20 years' experience, advising a senior technology leader in regulated asset management. The voice is calm, specific and sceptical of hype.
- **Architecture before vendors.** Each section states what the layer must achieve before naming any product.
- **Decisions over catalogues.** Prefer "choose X when…, avoid when…" to feature lists.
- **No product-name inflation.** Nothing is recommended because it is popular or because it appears in the graphic.

## 2. Spelling and mechanics

- **British spelling:** organisation, optimise, behaviour, licence (noun) / license (verb), programme (except computer program), modelling, catalogue, centre, analyse, defence.
- **Dates** in the form "7 October 2026". **Currency** as "US$" or "£", with the unit stated (per 1M tokens, per month).
- **Numbers:** use numerals for metrics. Every metric carries a source or a label.
- **Product names** follow the vendor's own casing: turbopuffer, pgvector, vLLM, SGLang, LangGraph.
- **No emojis** in any deliverable.

## 3. Claim labelling (plan §2, rule 4)

Every substantive claim carries one label:

| Label | When | Inline form in prose |
|---|---|---|
| **Verified fact** | Primary source: vendor docs, announcement, trust centre or regulator | `[VF: A4-S031]` |
| **Reported** | Secondary source: press, analyst, aggregator | `[R: A4-S044]` |
| **Architectural judgement** | Author's reasoning | `[AJ]` |
| **Recommendation** | Author's advice | `[Rec]` |
| **Not publicly verified** | No source could confirm it | `[NPV]` |

- In the master document the labels are written as small bracketed tags. The final exports may restyle them, but they must keep them.
- A sentence that mixes fact and judgement is split into two sentences.

## 4. Sourcing

- **Primary first:**
  1. official docs
  2. official announcements
  3. trust centres
  4. regulators
  5. high-quality independent technical sources
- **Date stamps:** every fact carries an access date (in `sources.csv`). Facts that move fast (versions, prices, certifications, regulatory dates) also carry an "as of" date in the prose: "as of 7 October 2026".
- **Search extracts:** if a primary source could only be read through a search-tool extract, because the host was blocked by the research environment, it is still a primary source. Its confidence is capped at `medium` unless a second source agrees.
- **Paywalled or blocked sources** are cited by link only. Never work around them.

## 5. Conflict of interest (plan §2, rule 10)

- The author is an Anthropic model.
- Anthropic products (Claude models, Claude Agent SDK) and Anthropic-originated standards (MCP, Agent Skills) use exactly the same rubric as everything else.
- Wherever one of them is recommended, the text names at least one independent alternative.
- A one-line disclosure appears at the top of the master document and in L1, L3 and L4.

## 6. Structure of every layer and control section (plan §9)

1. Responsibility
2. Why it matters, with a production failure story
3. Goals and KPIs
4. How it works, with a small diagram
5. Enterprise design principles, patterns and anti-patterns
6. Product selection criteria
7. Product deep dives
8. Comparison table
9. Decision tree
10. Lock-in classification
11. Regulated FS lens (POV 2)
12. Worked-example slice (POV 3)
13. Original → current → recommended

## 7. Scoring discipline

- Scores run from 1 to 5 against the plan's §8.1 rubric. **5 means best in class for an enterprise**, not "has the feature".
- **Calibration anchors:**
  - 3 = adequate for production with known caveats
  - 2 = material gap
  - 1 = disqualifying gap for an enterprise
- Missing evidence lowers the enterprise-readiness and security scores. It never raises them.

## 8. Words to avoid

- revolutionary
- game-changing
- cutting-edge
- seamless
- best-in-class (except in scoring definitions)
- leverage (as a verb)
- "it's important to note"
- unsupported superlatives
