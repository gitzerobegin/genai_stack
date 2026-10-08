# CP2 calibration review: layers 9, 8 and 7

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Scope** | `work/stageB/L9`, `L8`, `L7`: `section.md` and `assessments.json` |
| **Reviewer role** | Stage B calibration reviewer (consistency, accuracy, labels). The writers' structure (x.1 to x.13) is kept. |
| **New sources** | 27, `B-REV-S001` to `B-REV-S027` in `work/stageB/_review/sources_added.csv`, archived in `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/` |
| **Research budget** | 19 of 40 WebSearch calls; 3 direct fetches (raw.githubusercontent.com) |

**Environment note.** `cloud.google.com` is no longer directly fetchable. It now redirects to `docs.cloud.google.com`, which the egress proxy denies. All Google Cloud evidence below is therefore a search-tool extract (confidence medium). `CONTEXT.md` and `MEMORY.md` still list `cloud.google.com` as fetchable; that should be corrected at the CP2 write-up.

## Summary

- **40 logged changes**: 12 score changes, 9 scores kept but re-evidenced, re-based or newly recorded, 1 tier-rationale change, and 18 text, label and accuracy entries (several of which bundle more than one edit). The detail is in the change log (a).
- **NPV caps: 8 lifted, 5 kept, 1 added.**
  - *Lifted* on enterprise readiness: OpenAI, Gemini Embedding, Jina (Elastic Inference Service route only), Unstructured, Reducto, Mistral OCR, Google Document AI and Apify.
  - *Kept:* Cohere and Voyage on enterprise readiness; Voyage, Reducto and Firecrawl on security.
  - *Added:* LlamaParse on enterprise readiness, because hosted organisations are flat (every member has the same access) and no audit log is documented.
- **Tier changes: none.** Totals moved by between -0.20 and +0.35 FS, and no product crossed a tier boundary.
- **Labels.** The checker's long untagged paragraphs fell from 7, 7 and 16 (L9, L8, L7) to 0. There are no unknown source IDs. The only American spellings reported are proper nouns ("Trust Center", "Elastic License", "MinerU Open Source License").

## Calibration rules applied across all three layers

These rules make the writers' practice explicit. Each is a reading of `work/stage0/08_scoring_rubric.md`, and calibration questions Q1, Q2 and Q4 ask the human to confirm or change them.

1. **Enterprise readiness: the evidence rule.** The primary evidence is SSO, RBAC and audit logs.
   - If fewer than two of the three are verified for the product, or for the platform it is consumed through, the NPV cap applies and the score is at most 2.
   - If two of the three are verified, the score is at most 3, and the missing control is named in the rationale.
   - If all three are verified, the score is 3. It may rise to 4 when SCIM, an admin API or an SLA is also verified; Mistral OCR and Firecrawl stay at 3 because audit export or role granularity is limited.
   - Platform-level evidence (Google Cloud IAM, Elastic Cloud) counts when the product is consumed through that platform.
2. **Security: the scope rule.** Company-level or platform-level certifications whose coverage of the product is not stated score one point below the anchor. 5 needs SOC 2 Type II and ISO 27001, plus CMK/BYOK, ISO 42001 or FedRAMP, within the product's scope. This is the L9 writer's own calibration, applied to all three layers.
3. **Rule 2 (self-hosted software and open weights).** Ten products are scored this way, and the basis is now recorded in `evidence_caps_applied` in every layer:
   - L9: DeepEval, Phoenix, MLflow and the Promptfoo CLI
   - L8: Docling, Crawl4AI and MinerU
   - L7: Sentence Transformers, NVIDIA NIM and Qwen3 weights
4. **Rule 3 (ownership change, minus 1 on lock-in).** This is applied consistently to Langfuse, Phoenix, AX, Promptfoo, Weave, Voyage and Jina. Cohere is not reduced: it is the combining party in the pending Aleph Alpha deal. Revisit when the deal closes.

## (a) Change log

### Scores

| Layer | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| L7 | OpenAI: enterprise readiness | 2 (cap) | 4 | The API platform documents SAML/OIDC SSO, SCIM (from 17 September 2026), organisation and project RBAC with custom roles, an Admin API and audit logs. Not 5: support and SLA are unverified, and audit logs exclude request content and have best-effort retention. | B-REV-S004, S005, S006 |
| L7 | Gemini Embedding: enterprise readiness | 2 (cap) | 3 | Platform evidence: IAM predefined, custom and endpoint-level roles; Cloud Audit Logs (Data Access logs must be enabled); SAML/OIDC federation. Coverage of this model, and SCIM, are not evidenced. | B-REV-S007, S008, S012 |
| L7 | Jina: enterprise readiness | 2 (cap) | 3 | Scored on the recommended Elastic Inference Service (EIS) route, where Elastic Cloud has SAML SSO and RBAC. The standalone Jina API (API keys only) would stay at 2. | B-REV-S019 |
| L7 | Cohere: enterprise readiness | 2 (cap) | 2 (cap kept) | The search found only Owner and User team roles, and no SSO or audit-log documentation for the hosted API | B-REV-S013 |
| L7 | Voyage: enterprise readiness and security | 2 / 2 (caps) | 2 / 2 (kept) | Access is by Atlas model API keys only. MongoDB's SOC 2 scope page does not name Voyage and excludes preview features. | B-REV-S018, S027 |
| L7 | Qwen3: basis of the enterprise-readiness and security scores | NPV cap | Rule 2, scores unchanged at 2 | The recommendation is self-host only, so the scores are re-based on the self-hosted rule. This matches Sentence Transformers and NVIDIA. | rubric rule 2 |
| L7 | Sentence Transformers: security rationale | "security policy NPV" | Policy and CVE route verified; score stays 3 | Signed releases are not verified | B-REV-S002 |
| L8 | Unstructured: enterprise readiness | 2 (cap) | 3 | SAML 2.0/OIDC SSO, and account and workspace roles mapped from IdP groups. No audit-log feature is documented. | B-REV-S016 |
| L8 | Reducto: enterprise readiness | 2 (cap) | 3 | The product docs list SSO/SAML and RBAC on Enterprise. The security cap stays (V1 §4). | B-REV-S017 |
| L8 | Mistral OCR: enterprise readiness | 2 (cap) | 3 | Enterprise SAML SSO, Admin, Billing and Member roles, Workspaces and SCIM, and audit logs on by default. Audit logs cannot be exported. | B-REV-S014, S015 |
| L8 | Google Document AI: enterprise readiness | 2 (cap) | 3 | IAM including deny policies, VPC Service Controls, IAM-governed audit logs, and platform SSO | B-REV-S010, S012 |
| L8 | Google Document AI: security | 4 | 5 | The certifications are product-scoped (A1-S102). CMEK and US/EU residency are now verified. CMEK needs allowlisting in some regions. | B-REV-S010, S011 |
| L8 | Apify: enterprise readiness | 2 (cap) | 3 | Customisable organisation roles, per-resource permissions and enforced 2FA, with SSO stated in the docs. No audit log was found. | B-REV-S025 |
| L8 | LlamaParse: enterprise readiness | 3 | 2 (cap) | The score had been 3 with only SSO verified. Hosted organisations are flat, roles exist only when self-hosted, and audit logs are not documented. | B-REV-S023 |
| L8 | Firecrawl: enterprise readiness | 3 (SSO only evidenced) | 3 (re-evidenced) | SAML/OIDC SSO, SCIM, Admin and Member roles, and SIEM audit logging | B-REV-S024 |
| L8 | Docling: security | 3 | 4 | Rule 2 hygiene is now verified: a security policy, OpenSSF badge participation and signed releases | B-REV-S001 |
| L8 | Crawl4AI: security basis | "not verified" | Verified advisory history; score stays 2 | 8 GHSA advisories (5 high) fixed in 0.9.3 and 0.9.4; only 0.9.x is supported | B-REV-S003 |
| L9 | Datadog: security | 5 | 4 | Scope rule: the certifications are company-level and the module's scope is not stated. This is the same treatment as Gemini, Cohere and Mistral OCR. | B-L9-S001 |
| L9 | Braintrust: enterprise readiness | 3 (SSO and audit NPV) | 3 (re-evidenced) | The score had been inconsistent with the cap rule. SSO/SAML, RBAC and Enterprise audit logs are now verified (the audit page is on a preview docs domain). | B-REV-S020, S021 |
| L9 | Opik: enterprise readiness | 3 (RBAC and audit NPV) | 3 (re-evidenced) | SSO and organisation and workspace roles are verified; audit logs are still NPV. This is the two-of-three case. | B-REV-S022 |
| L9 | DeepEval, Phoenix, MLflow, Promptfoo: `evidence_caps_applied` | empty | Rule 2 recorded | Recorded the same way as in L8 and L7 | rubric rule 2 |
| L9 | LangSmith: tier rationale | Strategic | Strategic, conditional | Lock-in 2 is accepted only in a LangGraph estate, with OTel dual-instrumentation as the exit route (see Q3) | — |

### Accuracy and CP1 compliance

| Layer | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| L7 | Executive summary | "every serious vendor except OpenAI and Google now ships an embedding model and a reranker" | Every model vendor except OpenAI offers both; Google's is the separate Vertex ranking API | Factual error, and inconsistent with the section's own "[NPV] not researched" | B-REV-S026 |
| L7 | H6 evidence count | "Five of the seven verified model vendors" | "Six of the seven" | Same correction | B-REV-S026 |
| L7 | Gemini deep dive; decision tree; §7.13 "missing" row | "Vertex ranking API not researched [NPV]" | Ranking API described: semantic-ranker 004, with 005 in preview | New evidence | B-REV-S026 |
| L7 | OWASP 2025 identifiers (3 places) | Tagged `[VF: A8-S040]` | `[R: A8-S040]`, framed "for traceability". The 2026 list is stated as operative. | Matches the dataset's "Reported" label; CP1 makes the OWASP 2026 names operative | R-OWASP-LLM |
| L7 | Cohere access controls | Negative finding tagged `[VF: A2-S145]` | Owner and User roles `[VF: B-REV-S013]`; SSO and audit logs `[NPV]` | Mislabel: an absence of evidence was tagged as a verified fact | B-REV-S013 |
| L7 | §7.6 "public evidence is thin" | Stated that every hosted vendor was capped | Rewritten to show which controls are evidenced and which are not | Superseded by the review | B-REV-S004 to S019 |
| L7 | OpenAI, Gemini, Voyage, Jina, Sentence Transformers deep dives | Access-control or certification gaps marked NPV | New verified facts added; tier lines updated (FS 3.20, 3.05, 3.15) | New evidence | B-REV-S002, S004 to S008, S019, S027 |
| L8 | Mistral OCR 4.1 release | "released in July 2026 and reached GA on 26 August 2026" | Vendor pages disagree (July or August); the changelog marks GA on 26 August | The exact date is on the V1 §4 do-not-rely list | V1 §4 |
| L8 | OWASP bullet in §8.11 | Led with the 2025 list | Leads with the 2026 list; the 2025 IDs are kept for traceability `[R]` | CP1 OWASP 2026 names | R-OWASP-LLM |
| L8 | Tag in §8.13 | `[VF: A1-S101; NPV]` (the checker reported "NPV" as an unknown ID) | `[VF: A1-S101] [NPV]` | Malformed tag | — |
| L8 | Docling, Unstructured, LlamaParse, Reducto, Mistral OCR, Document AI, Firecrawl, Crawl4AI and Apify deep dives; caps list; key-facts row for Document AI | NPV statements on access controls and hygiene | Replaced with verified facts. Crawl4AI now advises pinning 0.9.4 or later. | New evidence | B-REV-S001, S003, S010, S011, S014 to S017, S023 to S025 |
| L8 | Unstructured security rationale | No mention of FedRAMP | States that the "FedRAMP alignment" wording is not relied on | V1 §4 | B-REV-S016 |
| L9 | Braintrust, Opik and Datadog deep dives; §9.8 scoring notes | Silent on access control, or "no cap triggered" only | Access-control facts added; scope rule explained | New evidence and consistency | B-REV-S020 to S022 |

### Labels and style

| Layer | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| L9, L8, L7 | Long untagged paragraphs | 7 / 7 / 16 | 0 / 0 / 0 | List lead-ins were joined to their lists, so each list carries its lead-in's tag. Decision-tree steps were tagged `[Rec]` (L9), or blank lines inside the code block were removed (L7). Four paragraphs were given tags (L8 §8.1, L7 Context, Cohere "choose/avoid", L7 "pick by recall"). | style guide §3 |
| L7 | Superlatives | "most complete native-multimodal option", "broadest lineup", "most FS-shaped" | "a natively multimodal option", "a broad lineup", "the widest deployment range of the hosted vendors here" | Unsupported superlatives | style guide §8 |
| L7 | Jina and Sentence Transformers model lists | Tag stranded at the start of the following paragraph | Tag moved to the lead-in sentence | Readability | — |
| L9 | LangSmith | "the broadest commercial feature set in this layer" | "a broad commercial feature set" | Unsupported superlative | style guide §8 |
| L7 | NVIDIA table | "API catalog" | "NVIDIA API Catalog" (product name) | The checker flagged an American spelling | — |

### Accuracy spot-checks

Claims were checked against the cited fact cells, by source ID, with `products.json` and `regulatory_facts.json`.

| Layer | Claims checked | Examples | Mismatches found |
|---|---:|---|---|
| L9 | 26 | Arize close 1 Oct 2026 and US$915M (Dynatrace release, primary); ClickHouse/Langfuse 16 Jan 2026; Promptfoo "announced, closing not published"; W&B 5 May 2025; SDK versions and dates (Langfuse, Phoenix, DeepEval, Promptfoo, Opik, MLflow); LangSmith certifications, regions and self-host sizing; Braintrust CMK, data plane and Series B; AX certifications and the ISO caveat; Opik certifications and price; Weave certifications and regions; free-tier retention (15, 30 and 60 days); OTel status; SR 26-2 and Annex III dates | None. Wording only (superlative). |
| L8 | 24 | Docling graduation August 2026 and version 2.135.0; Unstructured certifications, with FedRAMP correctly omitted; LlamaParse rename, regions and SSO; Reducto US$108M and pricing; MinerU licence thresholds; Mistral OCR pricing, retirement and certification scope; Document AI pricing and certification scope; Firecrawl AGPL, US data and Series B dates; Crawl4AI version and licence; Apify region and pricing; DORA (19 CTPPs); PS7/26 date | Mistral OCR release date (V1 §4); malformed tag; OWASP framing |
| L7 | 22 | Voyage US$160.9M (10-K, not press); rerank-3 Preview; OpenAI prices, ZDR, residency and certifications; Gemini GA date, dimensions, eu region and prices; Cohere Embed 5, Rerank 4, certifications and the Aleph Alpha status; Qwen3 sizes and regions; Jina close and licence; NVIDIA pricing; UK CTP designation 8 July 2026 (in force 13 July); re-embedding arithmetic | Reranker claim; OWASP labels; Cohere negative finding tagged VF |

Checked against the verifiers' "do not rely" lists and CP1:
- No do-not-rely item is stated as fact. Promptfoo is "announced", Unstructured has no FedRAMP, vendor benchmarks are `[R]` and not decision inputs, and no press deal values are used. The Arize and Voyage figures come from filings or primary releases.
- CP1 decisions are applied in all three layers: SR 26-2 with the GenAI exclusion, Annex III from 2 December 2027, OWASP 2026 as operative, and EthicalAgents and Ragoos as one line in L7 §7.13 (unscored).
- Every failure story is marked "Illustrative scenario [AJ]".

## (b) Final calibrated scores (`tools/score.py` output)

### L9: Evaluation and observability

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9-langfuse | 4 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3.80 | 3.70 | Strategic |
| L9-langsmith | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 2 | 3.95 | 3.80 | Strategic |
| L9-braintrust | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 2 | 3.40 | 3.20 | Tactical |
| L9-arize-phoenix | 4 | 2 | 3 | 4 | 4 | 4 | 4 | 3 | 3.50 | 3.35 | Tactical |
| L9-arize-ax | 4 | 4 | 4 | 5 | 4 | 3 | 3 | 2 | 3.85 | 3.70 | Tactical |
| L9-deepeval | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 4 | 3.75 | 3.70 | Tactical |
| L9-promptfoo | 4 | 3 | 3 | 5 | 4 | 3 | 4 | 3 | 3.70 | 3.55 | Tactical |
| L9-opik | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 4 | 3.75 | 3.75 | Tactical |
| L9-mlflow-genai | 4 | 3 | 3 | 5 | 5 | 5 | 4 | 5 | 4.10 | 4.10 | Strategic |
| L9-datadog-agent-observability | 3 | 4 | 4 | 2 | 4 | 3 | 2 | 3 | 3.15 | 3.20 | Tactical |
| L9-wandb-weave | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 2 | 3.55 | 3.55 | Tactical |

### L8: Data extraction, ingestion and web

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8-docling | 4 | 3 | 4 | 4 | 4 | 4 | 5 | 5 | 4.00 | 4.05 | Strategic |
| L8-unstructured | 4 | 3 | 4 | 5 | 4 | 3 | 3 | 4 | 3.80 | 3.85 | Strategic |
| L8-llamaparse | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 2 | 3.25 | 3.05 | Tactical |
| L8-reducto | 4 | 3 | 2 | 4 | 2 | 3 | 3 | 2 | 3.05 | 2.90 | Tactical |
| L8-mistral-ocr | 3 | 3 | 3 | 4 | 3 | 2 | 4 | 3 | 3.15 | 3.10 | Tactical |
| L8-google-document-ai | 4 | 3 | 5 | 2 | 3 | 3 | 4 | 2 | 3.40 | 3.30 | Tactical |
| L8-firecrawl | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 2 | 3.10 | 2.85 | Tactical |
| L8-crawl4ai | 3 | 2 | 2 | 4 | 3 | 2 | 4 | 4 | 2.90 | 2.90 | Experimental |
| L8-mineru | 4 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 2.80 | 2.70 | Experimental |
| L8-apify | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 2 | 2.65 | 2.55 | Tactical |

### L7: Embeddings and reranking

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7-openai | 3 | 4 | 4 | 2 | 3 | 4 | 4 | 2 | 3.30 | 3.20 | Tactical |
| L7-gemini-embedding | 4 | 3 | 4 | 2 | 3 | 3 | 3 | 2 | 3.15 | 3.05 | Tactical |
| L7-voyage | 5 | 2 | 2 | 3 | 4 | 3 | 4 | 2 | 3.25 | 2.90 | Tactical |
| L7-cohere | 4 | 2 | 4 | 4 | 4 | 3 | 3 | 3 | 3.45 | 3.40 | Tactical |
| L7-qwen3-embedding | 4 | 2 | 2 | 4 | 3 | 3 | 4 | 4 | 3.20 | 3.15 | Tactical |
| L7-jina | 4 | 3 | 3 | 4 | 4 | 3 | 2 | 2 | 3.30 | 3.15 | Tactical |
| L7-sentence-transformers | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 4 | 3.80 | 3.70 | Strategic |
| L7-nvidia-nemo-retriever | 3 | 3 | 3 | 4 | 3 | 3 | 2 | 2 | 3.00 | 2.95 | Tactical |
| L7-ethicalagents | – | – | – | – | – | – | – | – | n/a | n/a | not scored |
| L7-ragoos | – | – | – | – | – | – | – | – | n/a | n/a | not scored |

### Tier distribution

| Layer | Strategic | Tactical | Experimental | Not scored |
|---|---:|---:|---:|---:|
| L9 | 3 | 8 | 0 | 0 |
| L8 | 2 | 6 | 2 | 0 |
| L7 | 1 | 7 | 0 | 2 |

## (c) Cross-layer observations

**Depth.**
- All three sections follow x.1 to x.13 and run to about 7,500 words each (checker count, including tables and tags). That is 15–20% over the brief's 4,000 to 6,500. The review added about 2–4%.
- Deep dives often exceed 250 words. Examples are Unstructured and Mistral OCR in L8, and Cohere and Jina in L7.
- The decision trees are the strongest part of each section. They are specific, testable and usable by an architect [AJ].

**Format.** The three writers use three deep-dive formats:
- L9 uses italic labelled bullets.
- L8 uses bold labelled bullets with nested limitation lists.
- L7 uses bold paragraph headings.

All three work. A single format would make the master document easier to scan [AJ].

**Tone.**
- The tone is consistent: calm and sceptical, with no banned words.
- The residual issue was superlatives in "Strengths" lines (fixed).
- L7 uses `[AJ]` most heavily. L9 is the most densely sourced (207 VF tags).
- Each layer's worked-example slice ends with a "must never" list, which reads well across layers.

**Scoring.**
1. **Structural pattern.** Self-hostable, permissively licensed or foundation-governed components take every Strategic slot:
   - L9: MLflow, Langfuse
   - L8: Docling, Unstructured OSS
   - L7: Sentence Transformers

   LangSmith is the exception. This follows from the FS weights (15% deployment, 15% lock-in), which CP1 kept. The human should be aware that the weights, not only the evidence, drive this [AJ].
2. **L7 is structurally compressed.** Hosted embedding APIs score 2 on deployment and 2 on lock-in (vectors force re-embedding), so even well-controlled vendors cannot pass about 3.4 FS. That is defensible for FS, but L7 will show no hosted vendor as Strategic [AJ].
3. **Evidence asymmetry remains the biggest scoring driver.** Eleven of the 12 score changes in this review came from finding documentation that was not in the dataset, not from any change in the products. Only Datadog's came from a rule. The NPV rule penalises vendors whose documentation the search tools index poorly (Cohere, Voyage) [AJ].
4. **Tier and score overlap.** Three Tactical products score 3.70 to 3.75 FS: AX, DeepEval and Opik. That is level with Strategic Langfuse (3.70) and Sentence Transformers (3.70). Each has a stated rationale, but the overlap shows that tiers are judgements, not thresholds (Q3).
5. **Low scores.** Every layer has scores of 2 or below:
   - L9: Phoenix enterprise readiness; Datadog deployment and cost; four lock-in scores of 2
   - L8: Apify deployment 1
   - L7: several scores of 2
6. **Ownership.** Seven products carry the Acquired flag and the lock-in reduction. The rule is applied consistently.

## (d) Calibration questions for the human

**Q1. How strict should the NPV cap be for hyperscalers whose controls are well known but not in our dataset?**
- **(a) As applied now.** Platform-level evidence counts only when found in a primary source and logged. Gemini Embedding and Document AI score 3 on enterprise readiness, because SCIM and SLA were not evidenced. Each future hyperscaler product needs a logged search.
- **(b) Hyperscaler presumption.** Treat Google Cloud, Azure and AWS platform IAM, audit logging and SSO as verified by default at 4, with a due-diligence note per service. This would raise Gemini and Document AI to 4, and later Azure and Bedrock services.
- **(c) Strict.** Require product-specific evidence. Without it, cap at 2. This would reverse the Gemini, Document AI and Jina lifts.

**Q2. What does partial evidence earn on enterprise readiness?**
- **(a) As applied.** Two of SSO, RBAC and audit logs verified: maximum 3. One or none: capped at 2.
- **(b) Strict anchor.** All three are needed for 3. Unstructured, Reducto, Apify, Opik and Jina would return to 2.
- **(c) Lenient.** Any one verified control lifts the cap, to a maximum of 3. LlamaParse would return to 3.

**Q3. What should "Strategic" require?**
- **(a) As now.** Judgement, usually FS 3.6 or more, with no criterion at 1. A criterion at 2 is allowed if it is stated as a condition. LangSmith stays Strategic, conditional on LangGraph. AX, DeepEval and Opik stay Tactical at 3.70 to 3.75.
- **(b) Stricter.** FS 3.6 or more, and no criterion below 3. LangSmith becomes Tactical.
- **(c) Threshold-led.** FS 3.6 or more makes a product Strategic unless a named disqualifier applies (an acquisition under a week old, or "a library, not a platform"). DeepEval and Opik would need explicit disqualifiers or become Strategic.

**Q4. How should company-level certifications be scored when the product's scope is not stated?**
- **(a) As applied.** One point below the anchor. Datadog, Gemini and Cohere score 4; Mistral OCR scores 3.
- **(b) Face value.** Count company-level certifications in full. Datadog, Gemini and Cohere score 5; Mistral OCR scores 4.
- **(c) Strict.** Cap at 3 until the product's scope is seen in the report itself (B4 in MEMORY: no audit report has been read).

**Q5. Length per layer and per deep dive.**
- **(a)** Accept about 7,500 words per layer and deep dives of up to about 300 words for tranche 2 (L6, L5, L4 and C1 to C8). The master document would be roughly 130,000 words.
- **(b)** Hold to 6,500 per layer and 150–250 words per deep dive. Move the key-facts tables and scoring notes to an appendix. This needs a trim pass of about 15% on L9 to L7.
- **(c)** Cap layers at 5,000 words with a fuller appendix. The deck and LinkedIn series draw on the short form.

**Q6. Deep-dive format and failure stories.**
- **(a)** Standardise on one deep-dive format (proposed: L9's labelled bullets) and keep one "Illustrative scenario [AJ]" per layer, as now.
- **(b)** Keep the writers' formats. Keep the failure stories.
- **(c)** Standardise the format, and move the failure stories to an appendix or the deck. They are invented, so they may read as weaker evidence in a regulated-audience document.

## Files changed

- `work/stageB/L9/section.md`, `work/stageB/L8/section.md`, `work/stageB/L7/section.md`
- `work/stageB/L9/assessments.json`, `work/stageB/L8/assessments.json`, `work/stageB/L7/assessments.json` (totals rewritten by `tools/score.py --write`)
- `work/stageB/_review/sources_added.csv` (new), `work/stageB/_review/CP2_review.md` (this file)
- `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/B-REV-S001.txt` … `B-REV-S027.extract.txt` (27 archives)

`tools/build_dataset.py` will pick up `_review/sources_added.csv` through its `work/stageB/*/sources_added.csv` glob. Re-run it before the CP2 pack is built. `git` was not run.
