# CP3 calibration review A: L6, L5, L4, C1 and C2

| | |
|---|---|
| **Date** | 8 October 2026 |
| **Scope** | `work/stageB/L6`, `L5`, `L4`, `C1`, `C2`: `section.md` and `assessments.json`. Reviewer B covers C3 to C8 in parallel. |
| **Reference** | The approved L9–L7 calibration (`checkpoints/CP2/02_Calibration_Review.md`, `work/stageB/_review/CP2_rework_log.md`) and rubric rules 1–9 (`work/stage0/08_scoring_rubric.md`) |
| **New sources** | 6, `B-REVA-S001` to `B-REVA-S006` in `work/stageB/_review/sources_added_A.csv`, archived as search-tool extracts (confidence medium) in `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/` |
| **Research budget** | 6 of 15 WebSearch calls; no direct fetches |
| **Tag check** | `tools/check_tags.py`: 0 unknown source IDs and 0 long untagged paragraphs in all five sections (L6 had 1 malformed tag and 3 long untagged paragraphs). The American spellings reported are proper nouns: "PostgreSQL License", "Llama 4 Community License", "Trust Center", "API Center". |
| **Not run** | `git`; `tools/build_dataset.py`; `work/stageB/_review/all_scores.md` was not regenerated (reviewer B is changing C3–C8 at the same time) |

## Summary

- **12 criterion changes on 11 products**: 7 up and 5 down. **1 tier change**: L4 AgentCore Gateway and Identity, from Strategic to Tactical (conditional default in AWS estates).
- **Totals moved** by between -0.20 and +0.15 FS. No other product crossed a tier boundary.
- **4 enterprise-readiness scores of 4 were kept and re-evidenced**: Qdrant, Milvus/Zilliz, Elasticsearch and MongoDB. Each needed SCIM, an SLA or an admin API under rule 7, and that evidence is now logged.
- **Conflict of interest.** Disclosures are present everywhere they should be. Two borderline calls were resolved against the Anthropic-related item: MCP security fell from 3 to 2, and turbopuffer cost from 4 to 3. MCP keeps a conditional Strategic tier at FS 3.55, which is the one open COI question (Q1).
- **L6 is higher than L7 for structural reasons, not inflation.** The cause is permissive self-hostable engines and mature incumbents under FS weights that favour deployment and lock-in (see (d)). The L6 `x.8` score table had not been pasted; it is now filled.
- **Accuracy.** 77 claims were spot-checked against fact cells: 16 in L6, 15 in L5, 16 in L4, 16 in C1 and 14 in C2. There were no factual errors. Fixes were confined to labels and wording: 4 tags, 1 wording change and 3 superseded NPV statements. All CP1 and CP2 decisions and do-not-rely items are respected.
- **Length.** Nothing was shortened. By the checker's count: L6 went from 10,773 to 11,450 words, L5 from 10,400 to 10,587, L4 from 9,879 to 10,184, C1 from 8,670 to 8,704, and C2 from 6,863 to 6,926.

## How rules 1–9 were applied (calibration findings)

1. **Rule 7 had drifted in two directions.** The approved precedent (CP2 rework) is fixed:
   - one verified control among SSO, RBAC and audit logs gives a maximum of 3;
   - all three, plus SCIM, an SLA or an admin API, give 4;
   - LlamaParse and Browserbase got 3 on SSO alone;
   - Firecrawl and Mistral OCR got 4 with their limitation stated as a condition.

   The drift was:
   - **Too strict:** L5 held Cognee and Supermemory at 2 "on the anchors" with SSO verified. L5 also held Mem0 and Zep at 3, and C1 held Portkey at 3, all with the three controls plus an SLA or SCIM, on evidence-quality grounds.
   - **Too lenient (unevidenced):** L6 gave Qdrant, Milvus and Elasticsearch 4 without the "plus" evidence; Milvus did not even have RBAC evidenced. Searches closed all three gaps, so those scores stand.
   - **Kong** (C1) went to 4 once Konnect SSO and roles were found.
2. **Rule 6 and deployment for hyperscaler-native services.** Every AWS-, Azure- or Google-only managed service scores 2 on deployment, except L4 AgentCore, which had 3. It is now 2, matching the same service in C1.
3. **Rule 8.** The writers applied it consistently. One rationale was re-based: Milvus/Zilliz security 4 is now justified by its combined record (Zilliz Cloud would reach 5; self-hosted Milvus hygiene is unevidenced), not by "the verifiers did not re-check".
4. **Rule 9 (tiers by judgement).**
   - Every Strategic call with a criterion at 2 now states its condition.
   - The only Strategic call below FS 3.6 in these five sections is MCP (3.55), and it is put to the human (Q1).
   - The principle that separates Pinecone (Tactical, 3.80) from MongoDB (Strategic, 3.65) is now written down in L6. A 2 is accepted as a Strategic condition only when it rides on an existing platform commitment: Elastic, MongoDB, Kong, Apigee, and LangSmith in L9. It is not accepted for a net-new proprietary dependency.
5. **Maturity across managed guardrails.** Bedrock Guardrails had maturity 4 with its maturity fact cell NPV, against 3 for Azure AI Content Safety, which has a verified GA date of August 2024. It is aligned at 3.
6. **Rules 1–5** (NPV cap, library rule, ownership −1, licence risk, a low score in every layer) are applied consistently in all five sections. Every section has scores of 2 or below.

## (a) Change log

### Scores and tiers

| Section | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| L6 | turbopuffer: cost_tco | 4 | 3 | The Enterprise tier that carries CMEK and private networking starts at US$4,096 a month plus a 35% usage premium, against a US$500 minimum for Pinecone Enterprise (cost 3). The borderline call is resolved against the Anthropic-related item. FS 3.20 → 3.15. | A2-S123, V1-S077, A2-S074 |
| L6 | Qdrant: enterprise_readiness | 4 (no "plus" evidence) | 4 (re-evidenced) | Cloud Management API (admin API); 99.9% SLA on Premium (99.95% multi-AZ) | B-REVA-S002 (new) |
| L6 | Milvus/Zilliz: enterprise_readiness | 4 (RBAC "not evidenced [NPV]") | 4 (re-evidenced) | Organisation, project and cluster RBAC with custom roles, plus SCIM, to go with SSO, audit logs and the 99.95% SLA | B-REVA-S001 (new) |
| L6 | Elasticsearch: enterprise_readiness | 4 (no "plus" evidence) | 4 (re-evidenced) | Elastic Cloud API with role-bearing organisation API keys and membership management (admin API). SCIM not found. | B-REVA-S003 (new) |
| L6 | MongoDB: enterprise_readiness | 4 (SCIM, SLA not verified) | 4 (re-evidenced) | Atlas Admin API, already logged in CP2 | B-REV-S028 |
| L6 | Milvus/Zilliz: security rationale | "SOC 2 under NDA; not re-checked by verifiers" | Combined-record rationale | The previous reason was not a rubric ground | rule 8 |
| L6 | Pinecone and MongoDB: tier rationale | Unrelated rationales | The shared principle is stated (existing platform commitment vs net-new dependency) | Comparable products tiered by one stated rule | rule 9 |
| L5 | Mem0: enterprise_readiness | 3 | 4 | SSO, audit logs and SLA on Enterprise; Platform roles. Rule 7, as for Firecrawl and Mistral OCR. Condition: the evidence is a pricing page, and the OSS has no organisation concept. FS 3.20 → 3.35. | A3-S049, A3-S080 |
| L5 | Zep: enterprise_readiness | 3 | 4 | IdP sign-in, RBAC and ABAC, audit logs, SLA. Condition: audit logs cover web-app actions only (Mistral OCR precedent). FS 3.35 → 3.50. | A3-S107, A3-S089 |
| L5 | Cognee: enterprise_readiness | 2 | 3 | Verified SSO lifts the cap to 3 (LlamaParse and Browserbase precedent); multi-tenant authentication and SLAs. FS 3.10 → 3.25. | A3-S005, A3-S095 |
| L5 | Supermemory: enterprise_readiness | 2 | 3 | Verified SSO lifts the cap to 3. FS 2.90 → 3.05; stays Experimental. | A3-S096 |
| L5 | AgentCore Memory: cost_tco | 2 ("pricing NPV") | 3 | Published unit pricing (changed 6 October 2026); matches Memory Bank. FS 3.15 → 3.20. | B-REVA-S005 (new) |
| L4 | MCP: security_compliance | 3 | 2 | The reasons for 2:<br>• authorisation is optional<br>• tool definitions cannot be signed<br>• a documented tool-poisoning class<br>• several High TypeScript SDK advisories in 2026, one sending OAuth credentials to an authorisation server chosen by the MCP server<br>On integrity it sits below A2A (optional card signing). The borderline call is resolved against the Anthropic item. FS 3.75 → 3.55. | A3-S055, A3-S023, B-REVA-S006 (new) |
| L4 | MCP: tier line and rationale | Strategic, conditional (gateway) | Strategic, conditional (gateway, allow-list, pinned definitions); FS 3.55 below the guide is stated, and the alternative is put to the human | Rule 9: below 3.6 with a 2 needs an explicit condition | Q1 |
| L4 | AgentCore Gateway and Identity: deployment_flexibility | 3 | 2 | AWS-managed only; the same service scores 2 in C1, as does every AWS-only managed service | A3-S047 |
| L4 | AgentCore Gateway and Identity: reliability_maturity | 4 | 3 | About one year GA; AgentCore Memory (same GA) is 3 | A3-S047, A3-S048 |
| L4 | AgentCore Gateway and Identity: **tier** | Strategic, conditional | **Tactical, conditional: the default tool gateway where AWS is the agent platform** | FS 3.70 → 3.45 with deployment 2. Consistent with C1-aws-agentcore-gateway, AgentCore Memory and Bedrock Guardrails. | rule 9; Q2 |
| C1 | Portkey: enterprise_readiness | 3 | 4 | SSO, SCIM, roles and audit logs. Rule 7, as for Firecrawl. The condition is stated: vendor pages, and post-acquisition terms not public. FS 3.35 → 3.50; stays Tactical. | B-C1-S001 to S003 |
| C1 | Kong AI Gateway: enterprise_readiness | 3 ("Konnect SSO/RBAC NPV") | 4 | Konnect SAML/OIDC SSO, teams and roles, and IdP mapping, plus audit logs and a 99.99% SLA. FS 3.65 → 3.80. | B-REVA-S004 (new) |
| C2 | Bedrock Guardrails: reliability_maturity | 4 | 3 | The maturity fact cell is NPV (priced since December 2024); Azure has a verified GA of August 2024 and scores 3. FS 3.45 → 3.35. | A6-S101, A6-S055 |

### Accuracy, labels and text

| Section | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| L6 | §6.8 score table | `SCORE_TABLE_PLACEHOLDER` | `tools/score.py` output | The table was missing | — |
| L6 | §6.13 turbopuffer row | `[VF: A2-S056, A2-S124, A2-S125; R: A2-S126]` | `[VF: …] [R: A2-S126]` | Malformed tag (the checker read "R: A2-S126" as an ID) | — |
| L6 | §6.4 diagram; §6.12 list | 3 long untagged paragraphs | Diagram blocks tagged `[AJ]`/`[Rec]`; list lead-in joined to its list | Label rule (the CP2 precedent) | style guide §3 |
| L6 | Milvus deep dive | "RBAC on Zilliz Cloud is not evidenced [NPV]" | Access-control facts added; the NPV line was removed | New evidence | B-REVA-S001 |
| L6 | Qdrant and Elastic access control | No admin API or SLA | Cloud API, SLA and the key-offboarding caveat (Qdrant); Cloud API, SAML-only org SSO and no SCIM (Elastic) | New evidence | B-REVA-S002, S003 |
| L6 | turbopuffer deep dive | Cost not discussed | Enterprise entry price against Pinecone; COI resolution noted | COI review | A2-S123, A2-S074 |
| L6 | §6.8 scoring notes | — | Added: the rule 7 basis for the 4s, the turbopuffer COI note, and "why L6 scores above L7" (including pgvector maturity 4 despite 0.x) | Transparency | — |
| L5 | AgentCore Memory limitations | "Pricing was not verified [NPV]" | Unit prices as of 8 October 2026 | New evidence | B-REVA-S005 |
| L5 | §5.8 scoring notes | Cognee and Supermemory "2 on the anchors"; highest FS 3.35 | Rule 7 notes for Mem0, Zep, Cognee and Supermemory; highest FS 3.50 | Score changes | — |
| L4 | §4.2 and §4.11 OWASP | "Excessive Agency third" `[VF: R-OWASP-LLM, V2-S056]` | `[R: A8-S041]` | The dataset labels it Reported (a sponsor quote in the press release) | R-OWASP-LLM |
| L4 | §4.11 EU AI Act | "Most asset-management uses … are not Annex III [VF: R-EUAIA]" | `[AJ]` | A judgement tagged as fact | — |
| L4 | MCP deep dive and scoring notes | Silent on SDK advisories | 2026 advisories added; security 2 basis explained | New evidence | B-REVA-S006 |
| L4 | AgentCore tier line; §4.13 row | "Strategic in AWS estates" | "Tactical: default tool gateway in AWS estates" | Tier change | — |
| C1 | Kong deep dive | "Konnect SSO and RBAC are not in the fact base [NPV]" | Verified SSO, teams and roles | New evidence | B-REVA-S004 |
| C1 | §C1.8 scoring notes | Kong and Portkey "held at 3" | The rule 7 basis for 4 is explained | Score changes | — |
| C2 | §C2.11 OWASP | `[VF: R-OWASP-LLM, A8-S041]` | `[R: A8-S041]`, "is reported to rank" | As in L4 | R-OWASP-LLM |
| C2 | Executive summary | "Guardrails AI was acquired by Harvey … after retiring its hosted hub" | "Harvey announced its acquisition … after the project had retired hosted remote inference" | Matches the deep dive and the key-facts wording; no date is stated (V2 §4 item 10) | A6-S028, V2-S071 |
| C2 | §C2.8 scoring notes | — | A managed-service maturity note (Bedrock aligned to 3) | Score change | — |

`assessments.json`: criteria, per-criterion rationales, `evidence_caps_applied` and classification rationales were updated for every product above, along with assessment prose for Milvus, Qdrant, AgentCore Memory, MCP and Kong. Totals were rewritten by `python3 -I tools/score.py … --write`. All five files are valid JSON.

## (b) Calibrated score tables (`tools/score.py` output)

### L6: Retrieval and knowledge stores

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6-pgvector | 4 | 4 | 3 | 5 | 5 | 4 | 5 | 5 | 4.25 | 4.20 | Strategic |
| L6-pinecone | 4 | 4 | 5 | 4 | 3 | 4 | 3 | 2 | 3.85 | 3.80 | Tactical |
| L6-qdrant | 4 | 4 | 3 | 5 | 4 | 3 | 4 | 4 | 3.90 | 3.85 | Strategic |
| L6-milvus-zilliz | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 5 | 4.10 | 4.25 | Strategic |
| L6-weaviate | 4 | 3 | 4 | 5 | 4 | 3 | 3 | 3 | 3.75 | 3.70 | Tactical |
| L6-turbopuffer | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 2 | 3.30 | 3.15 | Tactical |
| L6-elasticsearch | 5 | 4 | 5 | 4 | 5 | 5 | 2 | 3 | 4.30 | 4.25 | Strategic |
| L6-mongodb-atlas-vector-search | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 3.80 | 3.65 | Strategic |
| L6-chroma | 3 | 2 | 3 | 4 | 3 | 2 | 4 | 4 | 3.05 | 3.10 | Tactical |
| L6-s3-vectors | 3 | 4 | 4 | 2 | 3 | 3 | 5 | 2 | 3.30 | 3.15 | Tactical |

### L5: Memory

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5-mem0 | 4 | 4 | 2 | 4 | 4 | 3 | 4 | 3 | 3.55 | 3.35 | Tactical |
| L5-zep | 5 | 4 | 3 | 4 | 4 | 3 | 3 | 2 | 3.75 | 3.50 | Tactical |
| L5-letta | 3 | 3 | 2 | 3 | 3 | 2 | 4 | 3 | 2.85 | 2.75 | Experimental |
| L5-cognee | 4 | 3 | 2 | 5 | 3 | 3 | 3 | 3 | 3.35 | 3.25 | Tactical |
| L5-supermemory | 4 | 3 | 2 | 5 | 4 | 2 | 3 | 2 | 3.30 | 3.05 | Experimental |
| L5-langmem | 3 | 2 | 2 | 4 | 3 | 1 | 4 | 3 | 2.75 | 2.65 | Experimental |
| L5-aws-agentcore-memory | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Tactical |
| L5-gcp-vertex-memory-bank | 4 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.30 | 3.20 | Tactical |

### L4: Tools, protocols and agent connectivity

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L4-mcp | 4 | 3 | 2 | 5 | 5 | 3 | 4 | 4 | 3.70 | 3.55 | Strategic |
| L4-a2a | 3 | 3 | 3 | 5 | 4 | 3 | 4 | 5 | 3.60 | 3.70 | Tactical |
| L4-agent-skills | 3 | 2 | 2 | 5 | 4 | 2 | 5 | 3 | 3.20 | 3.00 | Tactical |
| L4-composio | 4 | 3 | 2 | 4 | 4 | 2 | 3 | 2 | 3.15 | 2.90 | Experimental |
| L4-exa | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 3 | 2.70 | 2.70 | Tactical |
| L4-tavily | 3 | 3 | 3 | 1 | 3 | 3 | 3 | 2 | 2.65 | 2.55 | Tactical |
| L4-browserbase | 4 | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 3.35 | 3.35 | Tactical |
| L4-e2b | 4 | 2 | 3 | 4 | 4 | 3 | 3 | 4 | 3.35 | 3.35 | Tactical |
| L4-aws-agentcore-gateway-identity | 4 | 4 | 4 | 2 | 4 | 3 | 4 | 3 | 3.55 | 3.45 | Tactical |

### C1: AI / LLM gateway

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C1-litellm | 5 | 4 | 3 | 4 | 5 | 3 | 4 | 4 | 4.05 | 3.90 | Strategic |
| C1-portkey | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 3.60 | 3.50 | Tactical |
| C1-kong-ai-gateway | 5 | 4 | 4 | 4 | 4 | 3 | 2 | 3 | 3.85 | 3.80 | Strategic |
| C1-cloudflare-ai-gateway | 3 | 3 | 3 | 2 | 4 | 3 | 4 | 2 | 3.00 | 2.80 | Tactical |
| C1-azure-apim-ai-gateway | 4 | 4 | 4 | 2 | 4 | 3 | 3 | 2 | 3.40 | 3.25 | Tactical |
| C1-aws-agentcore-gateway | 3 | 4 | 4 | 2 | 3 | 2 | 4 | 2 | 3.10 | 3.00 | Tactical |
| C1-google-apigee-ai-gateway | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 3.80 | 3.65 | Strategic |
| C1-agentgateway | 4 | 3 | 2 | 4 | 3 | 3 | 4 | 5 | 3.40 | 3.45 | Tactical |
| C1-envoy-ai-gateway | 3 | 2 | 2 | 3 | 3 | 3 | 4 | 5 | 2.90 | 3.00 | Tactical |

### C2: Guardrails

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C2-nemo-guardrails | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 4 | 3.50 | 3.45 | Tactical |
| C2-guardrails-ai | 3 | 2 | 2 | 3 | 3 | 2 | 4 | 3 | 2.70 | 2.60 | Experimental |
| C2-meta-llama-protections | 3 | 2 | 2 | 5 | 4 | 2 | 4 | 3 | 3.10 | 2.95 | Tactical |
| C2-bedrock-guardrails | 5 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.50 | 3.35 | Tactical |
| C2-azure-ai-content-safety | 4 | 4 | 4 | 2 | 4 | 3 | 2 | 2 | 3.30 | 3.20 | Tactical |
| C2-google-model-armor | 4 | 4 | 4 | 2 | 4 | 3 | 5 | 2 | 3.60 | 3.35 | Tactical |

### Tier distribution

| Section | Strategic | Tactical | Experimental | Change |
|---|---:|---:|---:|---|
| L6 | 5 | 5 | 0 | none |
| L5 | 0 | 5 | 3 | none |
| L4 | 1 | 7 | 1 | AgentCore: Strategic → Tactical |
| C1 | 3 | 6 | 0 | none |
| C2 | 0 | 5 | 1 | none |

## (c) Accuracy spot-checks

Claims were checked against the cited fact cells in `products.json` and `regulatory_facts.json`, and against archived extracts where a figure is not in a cell.

| Section | Checked | Examples | Mismatches |
|---|---:|---|---|
| L6 | 16 | pgvector 0.8.7 (1 Oct, announced 5 Oct) and both CVEs; Pinecone Nexus GA 6 Aug, SDK v10, BYOC, pricing minima; Qdrant 1.19.2 and US$50M Series B; Milvus 3.0 GA 29 Jul and 3.0.2; Zilliz 99.95% SLA; Weaviate 1.39.7 and 1.40.0-rc.1; turbopuffer price tiers and 874 ms vs 14 ms (vendor `[R]`); Elastic 9.5 GA 4 Aug and Jina close 9 Oct 2025; MongoDB–Voyage 17 Feb 2025; Chroma 1.5.9 and Team US$250; S3 Vectors GA Dec 2025, US$0.06/GB-month, US$178.61 example, ~34 Regions; UK CTP 8/13 July; SS1/23 scope; Article 26 six months | None factual. Malformed tag; missing table; one NPV superseded. |
| L5 | 15 | Mem0 v2.0.0 14 Apr, 2.2.1, 66,777 stars, Starter US$19 and Pro US$249; Zep 3.30.0, 4.0.0b1, graphiti-core 0.30.2, Flex prices; Letta Code 0.34.4 and US$10M seed `[R]`; Cognee 1.6.3 and no certification; Supermemory SDK 5.0.0 on 6 Oct; LangMem 0.0.30 on 27 Oct 2025; AgentCore GA 13 Oct 2025; Memory Bank preview 8 Jul 2025, GA Dec 2025, prices from 28 Jan 2026; ICO erasure; SR 26-2 | None factual. One NPV superseded. |
| L4 | 16 | MCP donation 9 Dec 2025; spec 2026-07-28; SDK 2.3.0 and 1.32.1; EMA stable 18 Jun; Registry v0.1; Lead Maintainers; A2A 1.0.0/1.0.1 and AAIF dates; Agent Skills 18 Dec 2025 and no tagged releases; Composio 0.3%, 5,001 and 5,241; Tavily close 19 Feb and US$189.7M filing value (not the press US$275M); Exa pricing conflict; Browserbase SDK 1.20.0; E2B pricing and SOC 2 scope; AgentCore Policy GA 3 Mar | OWASP "third" tagged VF (dataset: Reported); Annex III judgement tagged VF |
| C1 | 16 | LiteLLM 1.104.1, incident 24 Mar, v1.83.0 upload 31 Mar 05:08 UTC; Portkey completed 29 May, US$117m (10-K, not press); Prisma AIRS GA 16 Jul; Kong 2.0 GA 1 Sep, 2.1.0 and 2.2.0; Cloudflare per-GB log pricing 1 Dec; APIM preview regions and no SLA; Apigee MCP GA 31 Mar and prices; agentgateway v1.6.0; Agent Router v1.2.0 and rename; Stripe–OpenRouter pending | None factual. One NPV superseded. |
| C2 | 14 | NeMo 0.24.1 on 16 Sep and US$4,500/GPU/year; Guardrails AI 0.11.0, the 6 or 25 Aug conflict stated, Harvey 9 Sep; Llama Guard 4 / Prompt Guard 2 on 29 Apr 2025 and llamafirewall 1.0.3 on 29 May 2025; Bedrock PII entities and per-policy prices; Azure Prompt Shields GA Aug 2024 and Task Adherence preview Nov 2025; Model Armor price and Madrid/Paris 27 Mar 2026 | OWASP "third" tagged VF; "acquired" wording |

**Do-not-rely lists and CP1/CP2 decisions.** These were checked in all five sections:

- SR 26-2 is used with the GenAI exclusion, and SR 11-7 appears only as superseded.
- Annex III is dated 2 December 2027, and commentary drafting is described as not Annex III, tagged `[AJ]`.
- The OWASP 2026 names are operative. The 2025 identifiers are kept `[R]` "for traceability".
- Deal values come from filings only: Portkey US$117m (10-K) and Tavily US$189.7M (Nebius filing). The press figure of US$275M is not used.
- OpenRouter is "agreed, pending", and Agent Skills is not described as foundation-governed.
- Composio's certifications are treated as NPV.
- The Guardrails AI cutoff conflict is stated, not resolved.
- Vendor benchmarks (Mem0, Supermemory, turbopuffer, Anthropic Contextual Retrieval) are `[R]` and not used as decision inputs.
- No D.C. Circuit, distillation or FOCUS-token claim appears in these sections.
- Promptfoo appears only as an L9 tile name in C2 §C2.13.
- Each section has exactly one "Illustrative scenario [AJ]", in x.2, and all deep dives use the CP2 labelled-bullet format.

## (d) Cross-section observations

1. **Conflict of interest.**
   - *Disclosures.* All the expected disclosures are present:
     - L4 has a top-of-section disclosure, plus COI bullets in the MCP and Agent Skills deep dives, and the concentration point in §4.11.
     - C1 has an MCP disclosure.
     - L6 has a turbopuffer COI bullet and a COI note on Anthropic's Contextual Retrieval figure, which is tagged `[R]`.
     - L5 has a COI note beside the Claude memory example, with ChatGPT as the alternative.
   - *Scoring.*
     - Agent Skills (FS 3.00, three criteria at 2) is scored below every peer and was not changed.
     - MCP and turbopuffer each had one borderline criterion, and both were resolved against the Anthropic-related item.
   - *Open question.* MCP's tier: it is Strategic at 3.55, while A2A is Tactical at 3.70. See Q1.
2. **One product, two records.** AgentCore Gateway is scored in both L4 (with Identity) and C1. After this review, the two records agree on enterprise readiness, security, deployment and cost.
   - They still differ on technical: L4 judges it as a tool gateway (4), C1 as a model gateway (3).
   - They differ on maturity: C1 is 2 because its LLM inference targets have no GA statement.
   - They differ on ecosystem and lock-in: L4 credits MCP on both sides and portable Cedar policies.

   Synthesis should present one product view, or explain the lens difference. Langfuse (L9 and C5) and MCP (L4 and C4-mcp-authorization) raise the same question in reviewer B's scope.
3. **A consistent hyperscaler-native pattern.** Every AWS-, Azure- or Google-only managed service in these five sections now scores 2 on deployment and is Tactical "default in that estate". There are nine such services:
   - S3 Vectors, AgentCore Memory and Memory Bank
   - AgentCore Gateway and Identity
   - APIM and C1 AgentCore
   - Bedrock Guardrails, Azure Content Safety and Model Armor

   Apigee is the exception: its hybrid runtime scores 4 on deployment, so it is Strategic, conditional. If the human prefers "Strategic, conditional: where X is the primary cloud" for these services, that is Q2.
4. **Strategic below FS 3.6.** In these five sections only MCP (3.55) remains. In C3–C8 several Strategic calls sit below 3.6: C4 Okta (3.40), Entra Agent ID (3.50), MCP authorization (3.50) and Cedar (3.50). Reviewer B should apply the same rule 9 test.

   C4-mcp-authorization is also Anthropic-related. Its security score of 3 is defensible on its own (the OAuth profile is the strong part of MCP), but it should be read next to L4 MCP's 2 and GHSA-6qxp-vccf-f47h (B-REVA-S006).
5. **Why L6 sits above L7.** The L6 maximum is FS 4.25 and the L7 maximum is 3.70. The gap is justified:
   - Four L6 engines are permissive or foundation-governed and self-hostable: pgvector, Qdrant, Milvus and Chroma.
   - Elastic and MongoDB are mature incumbents with product-scoped certifications and CMK.
   - L7's hosted APIs are structurally held at deployment 2 and lock-in 2, because vectors force re-embedding.

   L6 also has its share of low scores: S3 Vectors deployment 2; Chroma maturity 2; four lock-in scores of 2; and Elastic cost 2. The two highest totals are no higher than L9 MLflow (4.25). The one generous-looking item, pgvector maturity 4 at version 0.x, is explained in §6.8.
6. **Evidence asymmetry persists.**
   - Eight of the 12 criterion changes, and the four re-evidenced 4s, rest on rule 7 consistency or new access-control evidence, not on any change in the products.
   - The six new sources are search extracts (confidence medium).
   - Pricing-page evidence (Mem0) and vendor marketing pages (Portkey) now count towards a 4. Q3 asks whether that should continue.
7. **`all_scores.md` is stale.** It was not regenerated, to avoid colliding with reviewer B. Rebuild it from all 16 `assessments.json` files once both reviews land, then run `tools/build_dataset.py`.

## (e) Calibration questions for the human

**Q1. MCP and A2A: what security score, and which tier?**
MCP (Anthropic-originated) has security 2 after this review and is Strategic, conditional, at FS 3.55. A2A is Tactical at FS 3.70, with no criterion at 2.
- **(a) As applied.** MCP security 2; MCP Strategic, conditional (gateway, mandatory authorisation, allow-list, pinned definitions), because it is the layer's de facto tool contract. A2A Tactical, "Strategic candidate when agent delegation is in scope".
- **(b) Both Tactical.** The strategic element is the firm's tool gateway (C1/C4), not either protocol. MCP stays the recommended default contract, but no Anthropic-originated item holds a tier above a higher-scoring peer.
- **(c) Restore MCP security to 3** (FS 3.75, the writer's original), and make A2A Strategic, conditional on cross-team or cross-vendor delegation being in scope.

**Q2. Hyperscaler-native managed services: which tier, and what security score?**
This covers the writers' open questions on "Bedrock Guardrails conditional Strategic" and "hyperscaler memory security 4 vs 3", and the L4 AgentCore tier change.
- **(a) As applied.** All AWS-, Azure- or Google-only services are Tactical, "default in that estate". Security is 4 under rule 8, where certifications name the parent service but not the feature.
- **(b) Strategic, conditional: where X is the primary cloud**, for the lead service in each category: Bedrock Guardrails (3.35), AgentCore Gateway (3.45), AgentCore Memory and Memory Bank (3.20). Security stays at 4.
- **(c) Stricter scope.** Where certifications do not name the feature (AgentCore Memory, Memory Bank, Bedrock Guardrails, S3 Vectors, Azure Content Safety), security scores 3, not 4. This lowers each by 0.20 FS. Tiers stay Tactical.

**Q3. Rule 7 at 4: does any vendor page count?**
This review raised Mem0 (pricing page), Zep, Portkey (marketing pages) and Kong to 4, and Cognee and Supermemory to 3, for consistency with Firecrawl and Mistral OCR. Composio was kept at 3, because its audit-log claims conflict.
- **(a) As applied.** Any primary vendor page counts. The limitation is stated as a condition.
- **(b) Docs-grade evidence for a 4.** The "plus" (SCIM, an SLA or an admin API) must come from product documentation or a trust centre, not pricing or marketing pages. Mem0 and Portkey return to 3; Firecrawl (L8) should be re-checked on the same test.
- **(c) Revert the L5 and C1 raises.** Keep the writers' stricter reading, and amend the rubric so that one control gives 2 on the anchors. This would also reverse LlamaParse and Browserbase.

**Q4. Products with incidents or no certification: LiteLLM, Composio and Cognee.**
- **(a) As applied.**
  - LiteLLM: Strategic, conditional (hardened, pinned, Enterprise-licensed; security and maturity 3 after the remediated March 2026 PyPI compromise).
  - Composio: Experimental, no flag.
  - Cognee: Tactical, self-host only.
- **(b) Stricter.**
  - LiteLLM Tactical until 12 months pass with no further incident, or a third-party assurance report is published (Kong and Apigee remain Strategic options).
  - Composio flagged "Not recommended" for client data.
  - Cognee Experimental, as it is seed-stage with no certification.
- **(c) Mixed.** Keep LiteLLM and Cognee as now. Flag Composio "Not recommended", because a broker that held users' OAuth tokens disclosed a token-exposure incident in May 2026 whose full scope it said was not yet known (B-L4-S007).

**Q5. Can a criterion at 2 be a Strategic condition?**
- **(a) As applied.** Only when the condition is an existing platform commitment: Elastic (cost 2), MongoDB (lock-in 2), Kong (cost 2), Apigee (lock-in 2), and LangSmith in L9. Pinecone (FS 3.80, lock-in 2, a net-new proprietary dependency) stays Tactical.
- **(b) Score-led.** Pinecone becomes Strategic, conditional on a decided exit route (rebuild-from-source tested). The others are unchanged.
- **(c) Stricter.** Strategic requires no criterion below 3. Elastic, MongoDB, Kong, Apigee, MCP and LangSmith would become Tactical "default where already operated".

## Files changed

- `work/stageB/L6/section.md`, `L5/section.md`, `L4/section.md`, `C1/section.md`, `C2/section.md`
- `work/stageB/L6/assessments.json`, `L5/…`, `L4/…`, `C1/…`, `C2/…` (totals rewritten by `tools/score.py --write`)
- `work/stageB/_review/sources_added_A.csv` (new; picked up by the `sources_added*.csv` glob in both `check_tags.py` and `build_dataset.py`)
- `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/B-REVA-S001.extract.txt` … `B-REVA-S006.extract.txt`
- `work/stageB/_review/CP3_review_A.md` (this file)

**Not changed:** `MEMORY.md`, `work/stageB/_review/all_scores.md`, and anything in C3–C8. `git` was not run.
