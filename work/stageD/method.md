# Method and quality rules

> **Disclosure.** This document was researched and drafted by an Anthropic model (Claude), working as an agent for the reader. Anthropic products, and standards that originated at Anthropic, were scored on the same rubric as everything else:
> - Claude models and the Claude Agent SDK
> - MCP and Agent Skills
>
> Borderline calls on Anthropic-related items were resolved against them. Where the reader overrode a tier at a checkpoint, the text says so, and an independent alternative is always named.

## How the work was done

The review followed a staged plan with human checkpoints:

| Stage | What happened | Output |
|---|---|---|
| 0 Baseline | Inventory of the popular stack diagram, the review's inspiration and baseline (80 tiles, 9 layers); 19 ambiguities; dataset schema; style guide; hypotheses H1–H8 | `work/stage0/` |
| A Research | Eight parallel research streams, primary sources first, every fact archived with URL and access date | `work/stageA/` |
| A′ Verify | Two adversarial verifiers re-checked high-risk claims: versions, prices, acquisitions, certifications and regulatory dates | `work/stageA_verify/` |
| B Write | Seventeen chapters (9 layers and 8 cross-cutting controls) on a 13-part template, each with a scored product assessment | `work/stageB/` |
| B review | Calibration reviews across all chapters for scoring consistency, accuracy spot-checks and label coverage | `work/stageB/_review/` |
| C Synthesis | Hypothesis verdicts, reference architecture, four stacks, build vs buy, lock-in, roadmap and final recommendations | `work/stageC/` |
| C2 | A LinkedIn series in the reader's voice: an introduction post and 24 posts, each with a visual | `work/stageC2/`, `07_LinkedIn/` |
| D Package | This document, the technical appendix, slides, the explorer, the dataset and the source archive | `Enterprise_GenAI_Stack_Oct2026/` |

The reader reviewed and decided at each checkpoint (CP1–CP5). Every decision is recorded in `checkpoints/`, and the full run log is in `MEMORY.md`.

## Evidence base (as built)

| Measure | Value |
|---|---|
| Product records | {N_PRODUCTS}: the 80 tiles of the popular stack diagram, 48 control-plane products and 12 material additions |
| Products scored | {N_SCORED}. Tiers: {N_STRATEGIC} Strategic · {N_TACTICAL} Tactical · {N_EXPERIMENTAL} Experimental |
| Regulatory and standards records | {N_REG} |
| Sources logged | {N_SOURCES} |
| Direct page snapshots | {N_SNAPSHOT} |
| Search-tool extracts | {N_EXTRACT} |
| Link-only sources | {N_LINK} |
| Fact cells marked "Not publicly verified" | {N_NPV} of {N_CELLS} |

## Claim labels

Every substantive sentence carries a label. In this Word/PDF edition the label is shown as a small grey superscript, and verified or reported facts carry a footnote with their sources.

| Label | Meaning |
|---|---|
| **VF**, Verified fact | From a primary source: vendor documentation, an announcement, a trust centre or a regulator |
| **R**, Reported | From a secondary source, such as press or an aggregator |
| **AJ**, Architectural judgement | The author's reasoning |
| **Rec**, Recommendation | The author's advice |
| **NPV**, Not publicly verified | No source could confirm it. Such facts were never guessed. |

Each footnote names the source ID, title, URL and access date. Sources marked "search-tool extract" were read through a dated web-search extract, because the research environment blocked direct fetching of most vendor and regulator sites. Their confidence is capped at *medium*. All sources resolve in `06_References/bibliography.xlsx`.

## Scorecard

Each product is scored 1–5 on eight criteria. The totals are weighted averages on the same scale.

| Criterion | Generic weight | Regulated-FS weight |
|---|---:|---:|
| Technical capability | 20% | 15% |
| Enterprise readiness | 15% | 15% |
| Security and compliance | 15% | 20% |
| Deployment flexibility | 15% | 15% |
| Ecosystem and integration | 10% | 5% |
| Reliability and maturity | 10% | 10% |
| Cost and TCO | 10% | 5% |
| Lock-in, portability and concentration | 5% | 15% |

The calibration rules agreed at the checkpoints are in `work/stage0/08_scoring_rubric.md`, rules 1–13. In summary:
- Unverified security or enterprise-readiness evidence caps that criterion.
- Any one verified access control lifts the cap to 3.
- Services consumed through a hyperscaler inherit platform controls.
- Certifications whose product scope is not stated score one point below the anchor.
- A change of ownership reduces the lock-in score.

**Tiers:**

| Tier | Definition |
|---|---|
| **Strategic** | Suitable as a core platform component, often with a stated condition |
| **Tactical** | Useful for specific scenarios, but not a foundational dependency |
| **Experimental** | Promising, but immature or unsuitable as a critical dependency |

**Status flags:** Acquired · Renamed · Superseded · Deprecated · Duplicated · Not recommended · Not publicly verified.

## Limitations

- **No audit reports were read.** Every SOC 2, ISO and HIPAA statement is a vendor statement or a trust-centre listing.
- **Many facts rest on search-tool extracts** rather than page snapshots. Re-running the gap-fill on a machine with open internet access is described in `RERUN_ON_DESKTOP.md`.
- **Products and regulation move quickly.** Every fact is dated, and the LinkedIn series flags the facts to re-verify before each post.
- **Vendor benchmark figures were never used as decision inputs.**
