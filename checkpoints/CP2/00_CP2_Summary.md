# Checkpoint 2: layers 9–7 drafted (calibration point)

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Status** | Stopped for review. The template, depth, tone and scoring set here will be applied to tranche 2: L6, L5, L4 and C1–C8. |

## 1. What is done

| Item | Detail |
|---|---|
| **Drafts** | §9 Evaluation and observability, §8 Data extraction, ingestion and web, and §7 Embeddings and reranking. Each follows the 13-part template (plan §9), covers all three points of view and includes the worked-example slice. About 22,500 words in total. |
| **Product assessments** | 29 products scored on the 8-criterion scorecard (generic and FS totals), each with strengths, limitations, "choose when", "avoid when", competitors, an FS note, a tier and flags. EthicalAgents and Ragoos are recorded but not scored (CP1 Q4). |
| **Calibration review** | One reviewer agent worked across all three layers and made 40 logged changes:<br>• 12 score changes<br>• 8 evidence caps lifted, 5 kept, 1 added<br>• 18 accuracy, label and style fixes<br>• **No tier changes**<br>It found 27 new sources. Long untagged paragraphs went from 30 to 0, and every source tag resolves. |
| **Dataset** | `products.json` and `.xlsx` now carry the assessments and scores for L9–L7. Total sources: 1,151. Integrity check: 0 issues. |

### Files for your review

| File | What it is |
|---|---|
| `checkpoints/CP2/01_Draft_Layers_9-7.md` | The draft. A `.docx` copy is alongside for reading in Word. |
| `checkpoints/CP2/02_Calibration_Review.md` | Change log, final score tables, cross-layer observations and calibration questions |
| `work/stageB/<layer>/assessments.json` | Product-level assessment data |

## 2. Results at a glance

| Layer | Strategic | Tactical | Experimental | Highest FS score |
|---|---|---|---|---|
| L9 Evals and observability | MLflow, LangSmith (conditional on LangGraph), Langfuse | Opik, Arize AX, DeepEval, Promptfoo, W&B Weave, Phoenix, Datadog, Braintrust | – | MLflow 4.10 |
| L8 Ingestion | Docling, Unstructured | Document AI, Mistral OCR, LlamaParse, Reducto, Firecrawl, Apify | Crawl4AI, MinerU | Docling 4.05 |
| L7 Embeddings and reranking | Sentence Transformers | Cohere, OpenAI, Jina, Qwen3, Gemini, NVIDIA, Voyage | – | Sentence Transformers 3.70 |

**What drives the results.** Self-hostable, permissively licensed or foundation-governed components take almost every Strategic slot. The FS weights produce this: deployment counts for 15% and lock-in for 15%. Hosted embedding APIs cannot rise above about 3.4 FS, because switching models forces re-embedding the corpus [AJ]. Most of the remaining score differences come from **how much evidence could be found**, not from product differences. This is why Q1, Q2 and Q4 matter.

## 3. Calibration questions, with options

These come from `02_Calibration_Review.md` §(d), which has the full detail.

**Q1: The "Not publicly verified" cap for hyperscaler services**
- **(a)** As applied now: platform evidence counts only when it is logged.
- **(b)** Presume that AWS, Azure and GCP platform controls (IAM, audit logging, SSO) are in place, and score 4.
- **(c)** Strict: product-specific evidence, or the cap of 2.

**Q2: Partial evidence on enterprise readiness**
- **(a)** As applied: two of SSO, RBAC and audit logs verified means a maximum of 3.
- **(b)** All three are needed for 3.
- **(c)** Any one verified control lifts the cap.

**Q3: What "Strategic" requires**
- **(a)** As now: judgement, normally FS 3.6 or more, with stated conditions allowed.
- **(b)** FS 3.6 or more and no criterion below 3. LangSmith would become Tactical.
- **(c)** Threshold-led, with named disqualifiers.

**Q4: Company-level certifications whose product scope is not stated**
- **(a)** As applied: one point below the anchor.
- **(b)** Take them at face value.
- **(c)** Cap at 3 until the audit report itself has been read.

**Q5: Length**
- **(a)** Accept about 7,500 words per layer (the master document would be about 130,000 words).
- **(b)** Trim to 6,500 per layer and move the key-facts tables to the appendix.
- **(c)** Cap at 5,000 words per layer, with a fuller appendix.

**Q6: Deep-dive format and failure stories**
- **(a)** Standardise on L9's labelled-bullet format, and keep one illustrative scenario per layer.
- **(b)** Keep each writer's format.
- **(c)** Standardise the format, and move the invented scenarios out of the main text.

## 4. What could not be verified

- **Unverified evidence.** Remaining "Not publicly verified" items in these layers are named in each product's `evidence_caps_applied`. Examples: Cohere and Voyage enterprise controls, Voyage, Reducto and Firecrawl security scope, and LlamaParse audit logging.
- **Benchmarks.** No MTEB or vendor benchmark was used as a decision input. The MTEB site was blocked, and the vendor figures are not independently verified.
- **Environment change.** `cloud.google.com` now redirects to `docs.cloud.google.com`, which is blocked. Google facts in this tranche therefore come from search extracts.
- **Desktop gap-fill.** The re-run on an open-internet machine (`RERUN_ON_DESKTOP.md`) would most improve L7 and L8, where the evidence caps are most frequent.
