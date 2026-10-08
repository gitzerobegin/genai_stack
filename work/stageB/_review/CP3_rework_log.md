# CP3 rework log

**Date:** 8 October 2026
**Scope:** the user's Checkpoint 3 decisions (`checkpoints/CP3/06_CP3_Decisions.md`) and rubric rules 10–13 (`work/stage0/08_scoring_rubric.md`), applied to the drafted sections L9–L4 and C1–C8. L3, L2 and L1 were not touched.

## Summary

| | Before | After |
|---|---:|---:|
| Strategic | 29 | 43 |
| Tactical | 67 | 53 |
| Experimental | 8 | 8 |
| Not scored (L7 EthicalAgents, Ragoos) | 2 | 2 |

- **Tier changes:** 14, all Tactical → Strategic, conditional.
  - 3 under CP3 Q1: A2A, C4 MCP authorisation, and L4 MCP's rationale (L4 MCP was already Strategic).
  - 11 under CP3 Q2 / rule 10, including C4 Cedar. Cedar follows its enforcement point, AgentCore Gateway.
- **Score changes:** 1. L8 Google Document AI security fell from 5 to 4, because it was inconsistent with rule 8 (see below). Its FS total moved from 3.45 to 3.25 and its generic total from 3.55 to 3.40.
- **Q9:** verified only. C7 Prisma AIRS and C8 watsonx.governance already carry "candidate for Strategic after due diligence" in the section tier lines and the classification rationales. No change was needed.
- **Checks:**
  - `python3 -I tools/score.py … --write` was re-run on L8, L7, L6, L5, L4, C1, C2, C3 and C4.
  - `work/stageB/_review/all_scores.md` was regenerated for all 14 sections.
  - `python3 -I tools/check_tags.py .` on the 9 changed sections gives 0 unknown source IDs, 0 long untagged paragraphs and 0 banned words. The only "American spellings" it flags are product names that were already there (for example Azure API Center, Trust Center, PostgreSQL License, Elastic License, presidio-analyzer, Okta "Organization Owner", NVIDIA API Catalog).

## Changes

| Section | Product | Tier before | Tier after | Rule / decision | Text locations changed |
|---|---|---|---|---|---|
| L4 | L4-mcp | Strategic (conditional; "put to the human reviewer") | Strategic, conditional: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions | CP3 Q1 (reader's decision; one decision with C4-mcp-authorization) | `assessments.json` classification rationale; §4.7 MCP tier line (adds "Tier set by the reader at Checkpoint 3 (CP3 Q1); the author's reviewers had resolved the borderline call against the Anthropic-originated item."; the COI disclosure is kept); §4.8 "Tiers" scoring note; §4.13 MCP row |
| L4 | L4-a2a | Tactical | Strategic, conditional: where cross-team or cross-vendor agent delegation is in scope | CP3 Q1 | classification; §4.7 A2A tier line; §4.8 table row and "Tiers" note; §4.13 A2A row |
| L4 | L4-aws-agentcore-gateway-identity | Tactical (default where AWS is the agent platform) | Strategic, conditional: where AWS is your primary cloud | CP3 Q2, rule 10 (AWS's lead tool gateway and agent identity service); rule 11 for deployment 2. Kept consistent with C1. | classification; §4.7 tier line; §4.8 table row and "Tiers" note; §4.13 "(absent)" AgentCore row |
| C4 | C4-mcp-authorization | Tactical (mandatory where MCP is used) | Strategic, conditional: only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions; mandatory wherever MCP is the tool protocol | CP3 Q1 (one decision with L4-mcp) | classification; `fs_note`; top-of-section COI paragraph (kept, extended); deep-dive tier line (adds the CP3 Q1 sentence); C4.8 table row; "Why six Strategic" note (was "Why four"); "MCP authorisation" scoring note |
| C4 | C4-cedar | Tactical (enforcement point Tactical in C1) | Strategic, conditional: where AWS is your primary cloud and agents run on AgentCore Gateway | CP3 Q2, rule 10. AgentCore Policy is AWS's lead agent-policy service. CP3 review B held it Tactical only because AgentCore Gateway was Tactical, and that reason no longer holds. | classification; deep-dive tier line; C4.8 table row; "Why six Strategic" note; "Cedar and AgentCore Policy security" note |
| C1 | C1-aws-agentcore-gateway | Tactical | Strategic, conditional: where AWS is your primary cloud, for MCP and tool traffic; model routing stays elsewhere until inference targets are GA | CP3 Q2, rule 10. Maturity 2 is a stated condition (rule 9). Same tier as L4. | classification; deep-dive tier line; C1.8 table row; new "Hyperscaler lead services" scoring note; C1.13 "AWS AI gateway" row; MCP disclosure paragraph (protocol support of the Strategic gateways) |
| C1 | C1-azure-apim-ai-gateway | Tactical (revisit at AI Gateway tier GA) | Strategic, conditional: where Azure is your primary cloud; GA AI gateway policies in existing tiers, not the preview tier | CP3 Q2, rule 10 (Azure's lead AI gateway); rule 11 for lock-in 2 | classification; deep-dive tier line; C1.8 table row; scoring note; C1.13 APIM row; executive-summary recommendation |
| C1 | C1-google-apigee-ai-gateway | Strategic, conditional (Google Cloud or Apigee is the standard) | Strategic, conditional: where Google Cloud is your primary cloud or Apigee is already the API standard | Rule 10 wording only; no tier change | classification; deep-dive tier line; C1.13 Apigee row |
| C2 | C2-bedrock-guardrails | Tactical (default in AWS estates) | Strategic, conditional: where AWS is your primary cloud; Classic tier or region-constrained profiles for client data | CP3 Q2, rule 10 (AWS's lead guardrail service) | classification; deep-dive tier line; C2.8 table row; "No product is Strategic on score" note (rewritten); C2.13 row |
| C2 | C2-azure-ai-content-safety | Tactical (default in Azure estates) | Strategic, conditional: where Azure is your primary cloud; GA features only | CP3 Q2, rule 10 (Azure's lead guardrail service); rule 11 for cost 2 | classification; deep-dive tier line; C2.8 table row; scoring note; C2.13 row |
| C2 | C2-google-model-armor | Tactical | Strategic, conditional: where Google Cloud is your primary cloud | CP3 Q2, rule 10 (Google's lead guardrail service) | classification; deep-dive tier line; C2.8 table row; scoring note; C2.13 row |
| C3 | C3-microsoft-purview-dspm-ai | Tactical | Strategic, conditional: where Azure and Microsoft 365 are your primary cloud and E5 or the Purview Suite is licensed; posture evidence only, not prompt-path DLP | CP3 Q2, rule 10 (Microsoft's lead AI data-security posture service); rule 11 for deployment, cost and lock-in at 2 | classification; deep-dive tier line; C3.8 table row; "Calibration" note and new "Hyperscaler lead services" note; C3.13 Purview row |
| C3 | C3-google-sdp | Strategic, conditional (in a Google Cloud estate) | Strategic, conditional: where Google Cloud is your primary cloud | Rule 10 wording only; no tier change | classification; deep-dive tier line; C3.13 row |
| C4 | C4-entra-agent-id | Strategic, conditional (Entra is the workforce IdP) | Unchanged | Already conditional (CP3 Q6); no change | none |
| L5 | L5-aws-agentcore-memory | Tactical (default in an AgentCore estate) | Strategic, conditional: where AWS is your primary cloud and the agent runtime is AgentCore | CP3 Q2, rule 10 (AWS's lead managed agent memory); rule 11 | classification; executive-summary tier sentence; deep-dive tier line; §5.8 table row; "No independent product reaches Strategic" note; §5.13 "(absent)" row |
| L5 | L5-gcp-vertex-memory-bank | Tactical (default in a Google Cloud agent estate) | Strategic, conditional: where Google Cloud is your primary cloud and the agent runtime is Agent Engine; written residency confirmation | CP3 Q2, rule 10 (Google's lead managed agent memory) | classification; executive summary; deep-dive tier line; §5.8 table row; scoring note; §5.13 row |
| L6 | L6-s3-vectors | Tactical | Tactical, default in AWS estates (unchanged) | Rule 10 **not** applied. S3 Vectors is not AWS's lead vector-search service: AWS positions it as a durable tier behind OpenSearch [VF: A2-S092]. | classification rationale; deep-dive tier line; §6.13 row |
| L7 | L7-gemini-embedding | Tactical | Strategic, conditional: where Google Cloud is your primary cloud; not where UK-only processing is mandatory | CP3 Q2, rule 10 (Google's lead embedding model); rule 11 | classification; deep-dive tier line; §7.8 table row; new note in "Reading the scores" (contrast with Cohere, which is multi-cloud and stays Tactical at 3.70); §7.13 row |
| L8 | L8-google-document-ai | Tactical | Strategic, conditional: where Google Cloud is your primary cloud | CP3 Q2, rule 10 (Google's lead document-processing service); **rule 8 consistency fix: security 5 → 4** | classification; security rationale and `evidence_caps_applied`; new deep-dive "Security score" bullet; tier line; §8.8 table row (totals 3.55/3.45 → 3.40/3.25); "Security capped at 2" note; §8.13 hyperscaler row |

## Rule 8 inconsistency found and fixed

**L8 Google Document AI, security 5 → 4.**

- **Why it scored 5.** The CP2 rework kept it at 5 because the certifications are product-scoped and CMEK is supported.
- **Why that breaks rule 8.** A score of 5 needs **SOC 2 Type II** within the product's scope. The Google Cloud scope page (A1-S102) lists a "SOC 2 Report" without stating the type.
- **What other services score on the same evidence.** The same page gives security 4 for Sensitive Data Protection (C3), Model Armor (C2) and Apigee (C1), although those three are held at 4 for missing CMK evidence. In L5, AgentCore Memory is noted as having its "SOC 2 report type not stated".
- **Result.** Every hyperscaler-native service in L9–L4 and C1–C8 now scores 4 on security, which matches the CP3 Q2 decision text ("Security stays at 4").

## Candidates checked and not changed

- **No other hyperscaler-native managed service** was found in L9, C5, C6, C7 or C8.
  - The L9 products, LaunchDarkly, the FinOps tools, Vault, Prisma AIRS and the C8 platforms are not hyperscaler services.
  - MLflow has managed hyperscaler options but is a Linux Foundation open-source project.
- **Already Strategic, conditional:** C3 Google SDP, C1 Apigee and C4 Entra Agent ID. Only the first two had their wording aligned.
- **L7 Cohere** (FS 3.70, Tactical) is not hyperscaler-native, so rule 10 does not apply. It now ranks below Gemini Embedding (FS 3.20) on tier. The section states this asymmetry explicitly for the reader.

## Points for Stage C synthesis

- Rule 10 adds 11 "where this is your primary cloud" Strategic entries.
- Each cloud now has a conditional Strategic set:
  - **AWS:** AgentCore Gateway/Identity, Policy (Cedar), Memory, Bedrock Guardrails
  - **Azure:** APIM AI gateway, Content Safety, Purview DSPM, Entra
  - **Google Cloud:** Apigee, Model Armor, SDP, Memory Bank, Gemini Embedding, Document AI
- These sets read best as alternative per-cloud stacks, not as cumulative recommendations.
- The lowest Strategic FS totals in these sections are C1 AgentCore Gateway (3.00) and C3 Purview DSPM (3.05). Both carry narrowing conditions.
