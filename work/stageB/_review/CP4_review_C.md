# CP4 calibration review C: L3, L2 and L1

| | |
|---|---|
| **Date** | 9 October 2026 |
| **Scope** | `work/stageB/L3`, `L2`, `L1`: `section.md` and `assessments.json` (tranche 3), calibrated against the 14 approved sections (L9–L4, C1–C8) |
| **Basis** | Rubric rules 1–13 (`work/stage0/08_scoring_rubric.md`); CP2 and CP3 decisions; the approved precedents in `CP3_review_A.md`, `CP3_review_B.md` and `CP3_rework_log.md`; V1 and V2 §4 do-not-rely lists; CP1 ambiguity resolutions for the L1 lineups |
| **New sources** | 2: `B-REVC-S001` (PyPI JSON API, direct read of the registry) and `B-REVC-S002` (NVD/OSV/GHSA for CVE-2026-3059, search extract), in `work/stageB/_review/sources_added_C.csv`, archived in `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/` |
| **Research budget** | 1 of 10 WebSearch calls, plus one direct registry read. Both were chosen because they bear on a score: SGLang security (2 or 3) and the Claude Agent SDK maturity comparison |
| **Tag check** | `tools/check_tags.py` on all three sections: 0 unknown source IDs, 0 long untagged paragraphs, 0 banned words. The "American spellings" reported are proper nouns or quotations only: "Trust Center", "Department of Defense", "Llama 4 Community License", "Kimi K3 License", "Qwen3.8-Max License", "SEE LICENSE IN README.md", Cerebras' "Organization Admin" role, and llm-d's "optimizations" quotation |
| **Not run** | `git`; `tools/build_dataset.py` |

## Conflict-of-interest statement

The reviewer is an Anthropic model. L1 scores Anthropic and L3 scores the Claude Agent SDK. **This review changed no Anthropic score in either direction.** Where a score for an Anthropic item appears to depart from the rubric, the neutral-rubric value is shown in a question for the reader (Q1, Q4) and the decision is left to the reader. The only edits to Anthropic records are documentation: they record that four criteria, not three, were resolved against Anthropic in L1, and they point to the questions. The review also removed one item that cut against a competitor on Anthropic's word alone (see the change log): the distillation allegation in the Kimi `limitations_risks` list.

## Summary

- **One tier change; no criterion-score changes.**
  - **L3 Google ADK moves from Tactical to Strategic, conditional: where Google Cloud is your primary cloud.** This is a rule 10 parity fix. ADK on Agent Engine is Google's lead agent framework and runtime, and the L5 Memory Bank precedent already names Agent Engine as Google's agent runtime. Strands with AgentCore (AWS) was Strategic under rule 10 at FS 3.25, and Microsoft Agent Framework (Azure) is Strategic on score. ADK was left as the only Tactical "default in that estate", with no other Google service in the category. Scores are unchanged, at FS 3.35. Q6 asks whether to re-base its scores on Agent Engine.
- **Text and evidence fixes (no score effect):**
  - SGLang CVE-2026-3059: NVD and OSV reference a fix in 0.5.10, which conflicts with the GitHub advisory. The text and rationale were updated, the NPV line was retired, and the 2-or-3 decision is put to the reader (Q5).
  - llm-d: the "experimental" wording conflicts with the v0.7 release note.
  - Kimi: the distillation allegation was moved out of the limitations list.
  - Anthropic documentation: four borderline calls, not three.
  - Claude Agent SDK maturity note: PyPI classifier evidence added.
- **Accuracy:** 63 claims were spot-checked: L1 24, L3 20, L2 19. There were **no factual errors**. There were three precision corrections (SGLang patch status; llm-d scheduling status; an L1 miscount in a scoring note), and every L1 precision requirement holds (see (c)).
- **Calibration verdict.** Rules 1–13 are applied consistently in all three sections, with three exceptions:
  - the ADK tier, now fixed;
  - two Anthropic scores whose stated reasons go beyond the rubric (cost and security in L1), put to the reader as Q1;
  - one Anthropic score applied more strictly than its peers (Claude Agent SDK maturity), put to the reader as Q4.

  "Resolve borderline against" is documented on every Anthropic call. Two of the six calls are not genuinely borderline, because their peers support the score given: L1 technical 4 and ecosystem 4. Two are departures rather than borderline calls: L1 cost 3 and security 4.
- **Tier distribution after this review.**
  - L3: 5 Strategic, 5 Tactical, 2 Experimental.
  - L2: 2 Strategic, 7 Tactical, 2 Experimental.
  - L1: 4 Strategic, 6 Tactical, 1 Experimental.
  - All 17 sections: 54 Strategic, 71 Tactical, 13 Experimental, 2 unscored.

## How rules 1–13 were read across L3, L2 and L1

1. **Rule 1 (NPV cap).** Applied correctly:
   - Qwen enterprise readiness 2.
   - Security 2 for Qwen, Kimi, GLM, Meta, Ollama and LM Studio.
   - Mistral Agents enterprise readiness 2.
   - DeepSeek security 1 is the anchor-1 case ("unremediated serious incident": the continuing Garante limitation plus PRC storage), not a cap. That is consistent with the anchor.
2. **Rule 2 (libraries and open software).**
   - All L3 libraries sit at 3 or 4 on enterprise readiness and security. Microsoft Agent Framework reaches 4 on Microsoft's LTS commitment.
   - In L2, vLLM reaches 4 on enterprise readiness via Red Hat AI Inference. SGLang and llm-d hold at 3, below the cap.
   - Gemma security is scored on hygiene.
   - All are consistent with L9 DeepEval and L6 pgvector.
3. **Rule 3 (ownership change).**
   - Applied: Grok (SpaceX), lock-in −1, flag Acquired; OpenRouter (Stripe, pending), lock-in −1, flag Acquired.
   - Correctly not applied: SGLang. RadixArk is a steward, not an acquirer.
4. **Rule 4 (licence risk).** Applied to the thresholds in Medium 3.5, Llama 4, Kimi K3, the Qwen3.8 flagship and GLM-5.3, and to the Claude Agent SDK's Commercial Terms.
5. **Rule 5 (a low score in each layer).** Met in all three: L3 has six products with a 2 or below, L2 seven, and L1 seven. The L1 scoring note said "eight" and was corrected.
6. **Rule 6 (hyperscaler presumption).**
   - L1 applies it wherever the family's *current generation* is operated by a cloud. That test is applied consistently:
     - Qwen3.8 is on no hyperscaler, so it scores 2.
     - Meta qualifies through Muse Spark 1.3 on Foundry.
     - Kimi and GLM qualify through Bedrock cross-Region routes.
     - DeepSeek qualifies through Foundry direct sale.
   - Whether a cross-Region-only route should qualify is a judgement for the reader (Q3).
7. **Rule 7 (partial evidence).**
   - Raised to 4: OpenRouter, Fireworks, Hugging Face, LangGraph (LangSmith) and Temporal. Each has all three controls plus SCIM, an SLA or an admin API.
   - Held at 3 on one or two controls: CrewAI and Cerebras.
   - All match the CP3 review A precedent.
8. **Rule 8 (certification scope).**
   - One below the anchor where scope is not stated: Mistral (L1 and L3), Together and Cerebras.
   - LangGraph is held at 4 because ISO 27001 scope is unconfirmed.
   - Fireworks is held at 3 because its ISO claims are on the V1 §4 list.
   - Hyperscaler-native services stay at 4: Gemini and AgentCore.
   - **One departure:** Anthropic meets the rule-8 test for 5 but is scored 4 (Q1).
9. **Rules 9 and 11 (Strategic by judgement; a 2 only on an existing platform commitment).**
   - SGLang (FS 3.65, security 2, no platform commitment) is correctly Tactical under rule 11.
   - Gemini (deployment and lock-in 2) and AgentCore are correctly allowed under rule 11, because the condition is the primary cloud.
10. **Rule 10 (hyperscaler lead services).**
    - Applied to Gemini (L1), following the approved L7 Gemini Embedding precedent: Strategic at FS 3.20, with no FS floor (C1 AgentCore Gateway is Strategic at 3.00).
    - Applied to AgentCore (L3).
    - **Not applied to Google ADK, now fixed.**
    - Q2 asks whether rule 10 should cover model families at all.
11. **Rules 12 and 13.** Applied as written:
    - Fireworks is Tactical, "candidate for Strategic after due diligence", like Prisma AIRS and watsonx.governance (CP3 Q9).
    - Pricing and vendor-page evidence is accepted for a 4, with limitations stated.

## (a) Change log

### Tiers and scores

| Section | Item | Before | After | Reason | Text locations changed |
|---|---|---|---|---|---|
| L3 | `L3-google-adk`: **tier** | Tactical, conditional: default framework in a Google Cloud estate (FS 3.35) | **Strategic, conditional: where Google Cloud is your primary cloud** (FS 3.35; scores unchanged) | Rule 10 parity. ADK on Agent Engine is Google's lead agent framework and runtime. AWS (Strands with AgentCore, Strategic under rule 10 at 3.25) and Azure (Microsoft Agent Framework, Strategic at 3.65) each have one. L5 Memory Bank is already Strategic "where the agent runtime is Agent Engine". The rule-10 "Tactical, default in that estate" wording applies only when another service is the lead, and there is none. No criterion at 1. | `assessments.json` classification; §3.7 tier line (with a change note); §3.8 table row and "Tiers versus totals" note; §3.13 "(absent)" row; executive-summary recommendation |

No criterion score was changed in L3, L2 or L1.

### Accuracy, evidence and documentation (no score effect)

| Section | Item | Before | After | Reason | Source |
|---|---|---|---|---|---|
| L2 | SGLang CVE-2026-3059: §2.5, §2.7, §2.8 scoring note and key-facts row; `assessments.json` limitation and security rationale | "lists no patched version in the advisory"; "Whether 0.5.21 closes CVE-2026-3059 was not verified [NPV]" | The GitHub advisory lists none, while NVD gives the range 0.5.5–0.5.9 and references the v0.5.10 release and a fix PR, and OSV records a fixed commit. On those references 0.5.21 should include the fix (the patch itself was not read). Security stays 2 pending Q5. | New evidence weakens one of the two grounds for security 2 | B-REVC-S002 (new) |
| L1 | §1.8 scoring note (rule 5) | "Criteria at 2 or below appear for eight of the eleven families" | "seven … (Gemini, Grok, DeepSeek, Qwen, Kimi, GLM and Meta)" | Miscount, checked against the table | — |
| L2 | llm-d deep dive | "with experimental predicted-latency scheduling" | The README feature list says experimental; its v0.7 release note says GA | Internal conflict in A4-S089, now stated | A4-S089 |
| L1 | `L1-moonshot-kimi` `limitations_risks` | "Anthropic alleges that Moonshot distilled Claude; unadjudicated competitor allegation" | "Context only, not a scored limitation: … not used in any score" | COI hygiene. The section says the allegation is not an input to any score (V2 §4 item 14), but the JSON listed it as a limitation of a competitor | V2-S022 |
| L1 | `L1-anthropic` classification rationale; §1.7 tier line | "three borderline calls resolved against Anthropic (technical, ecosystem, cost)" | Records security as the fourth call held below the rubric value (rule-8 threshold met). States that the CP4 review changed no Anthropic score and put the tier to the reader (Q1). | The scoring notes already said this; the tier line and rationale did not | §1.8 scoring notes |
| L3 | §3.8 "Conflict-of-interest calls on the Claude Agent SDK" | "the OpenAI Agents SDK … has no recorded Alpha classifier" | "declares no Development Status classifier on PyPI [VF: B-REVC-S001]"; the question is put to the reader at CP4 | Evidence for the one distinguishing fact behind maturity 1 vs 2 | B-REVC-S001 (new) |
| All | `work/stageB/_review/all_scores.md` | Generated 8 October | Regenerated 9 October: ## L9 … ## L1, ## C1 … ## C8, each with the `tools/score.py` table. The only diff is the ADK tier. | Task 4 | — |

### Checked and kept

| Section | Item | Kept at | Why |
|---|---|---|---|
| L1 | Gemini tier | Strategic, conditional (FS 3.35) | Rule 10, as for L7 Gemini Embedding (3.20), which the reader approved at CP3. There is no FS floor in rule 10. Deployment and lock-in 2 are allowed under rule 11. See Q2. |
| L1 | DeepSeek, Kimi, GLM enterprise readiness 4 | 4 | Rule 6 as written. Each current model is operated by a cloud: Foundry direct (DeepSeek); Bedrock cross-Region (Kimi K3, GLM-5.3). Foundry's Fireworks pass-through is correctly *not* used as the basis. See Q3. |
| L1 | Qwen enterprise readiness 2 | 2 | Qwen3.8 is on no hyperscaler; only the earlier Qwen3 is [VF: A5-S086]. The current-generation test is the same one that admits Meta through Muse Spark 1.3 on Foundry. |
| L1 | DeepSeek security 1 | 1 | Anchor 1: an unremediated serious regulatory finding (Garante, still continuing in May 2026) plus PRC storage. The self-hosted route is stated separately ("about 3 under rule 2"). |
| L1 | Meta flag "Renamed" | Renamed | Matches CP1 What-changed row 80 |
| L1 | Mistral and Gemma Strategic | Strategic (3.85, 3.80) | No criterion below 3; roles stated |
| L3 | Pydantic AI | Tactical (3.55) | Below the guide, with no stated platform condition; v2 ten months after v1. The same 3.55 boundary as Anthropic (Q1) and as L4 MCP (Strategic only by the reader's CP3 decision). |
| L3 | Claude Agent SDK technical 3 and deployment 3 (labelled "borderline, resolved down") | 3 and 3 | On peers these are not borderline. The OpenAI Agents SDK has Temporal and DBOS durability integrations [VF: A4-S052], and provider-agnostic models allow an air-gapped deployment; the Claude Agent SDK has neither [VF: A4-S027, A4-S122]. Neutral values: 3 and 3. |
| L2 | SGLang tier | Tactical (3.65) | Rule 11: a 2 without a platform-commitment condition. Q5 asks about the 2. |
| L2 | Hugging Face Strategic, conditional (3.60); Fireworks Tactical (3.65) | As drafted | The distinction is stated. HF is Strategic only as the governed open-weight *supply* source, with no client inference data. Fireworks processes client data, its ISO claims are not relied on, and residency is US-only self-serve (rule 13 "candidate"). See Q5. |
| L2 | OpenRouter | Tactical, Acquired (pending); lock-in 2 | Rule 3; no press deal value used |

## (b) Calibrated score tables (`tools/score.py` output, after this review)

### L3: Agent frameworks and orchestration

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3-langgraph | 5 | 4 | 4 | 5 | 5 | 4 | 4 | 3 | 4.40 | 4.20 | Strategic |
| L3-llamaindex | 3 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3.25 | 3.15 | Tactical |
| L3-pydantic-ai | 4 | 3 | 3 | 4 | 4 | 3 | 4 | 4 | 3.60 | 3.55 | Tactical |
| L3-crewai | 3 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3.25 | 3.20 | Tactical |
| L3-openai-agents-sdk | 4 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3.45 | 3.30 | Tactical |
| L3-claude-agent-sdk | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 2 | 2.75 | 2.65 | Experimental |
| L3-mistral-agents | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2.60 | 2.55 | Experimental |
| L3-vercel-ai-sdk | 3 | 3 | 3 | 4 | 4 | 2 | 4 | 3 | 3.25 | 3.15 | Tactical |
| L3-microsoft-agent-framework | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 3.80 | 3.65 | Strategic |
| L3-google-adk | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 3.45 | 3.35 | Strategic |
| L3-aws-strands-agentcore | 4 | 4 | 4 | 2 | 4 | 3 | 3 | 2 | 3.40 | 3.25 | Strategic |
| L3-temporal | 4 | 4 | 3 | 5 | 4 | 4 | 3 | 4 | 3.90 | 3.90 | Strategic |

### L2: Inference, serving and model access

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2-vllm | 5 | 4 | 3 | 5 | 5 | 4 | 4 | 5 | 4.35 | 4.30 | Strategic |
| L2-sglang | 5 | 3 | 2 | 5 | 4 | 3 | 4 | 4 | 3.80 | 3.65 | Tactical |
| L2-nvidia-dynamo | 4 | 3 | 2 | 4 | 3 | 2 | 3 | 3 | 3.10 | 3.00 | Experimental |
| L2-llm-d | 4 | 3 | 2 | 4 | 4 | 2 | 3 | 5 | 3.30 | 3.35 | Experimental |
| L2-ollama | 3 | 2 | 2 | 4 | 4 | 2 | 4 | 4 | 3.00 | 2.95 | Tactical |
| L2-lm-studio | 2 | 2 | 2 | 2 | 2 | 2 | 4 | 3 | 2.25 | 2.25 | Tactical |
| L2-hugging-face | 4 | 4 | 3 | 3 | 5 | 3 | 4 | 4 | 3.70 | 3.60 | Strategic |
| L2-openrouter | 4 | 4 | 3 | 2 | 4 | 3 | 3 | 2 | 3.25 | 3.05 | Tactical |
| L2-together-ai | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 3.50 | 3.50 | Tactical |
| L2-fireworks-ai | 4 | 4 | 3 | 4 | 4 | 3 | 3 | 4 | 3.65 | 3.65 | Tactical |
| L2-cerebras | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2.85 | 2.80 | Tactical |

### L1: Foundation models

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1-openai | 5 | 4 | 4 | 4 | 5 | 4 | 4 | 3 | 4.25 | 4.05 | Strategic |
| L1-anthropic | 4 | 4 | 4 | 3 | 4 | 3 | 3 | 3 | 3.60 | 3.55 | Tactical |
| L1-google-gemini | 5 | 4 | 4 | 2 | 3 | 3 | 3 | 2 | 3.50 | 3.35 | Strategic |
| L1-xai-grok | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 2 | 3.50 | 3.25 | Tactical |
| L1-deepseek | 4 | 4 | 1 | 4 | 4 | 2 | 3 | 4 | 3.25 | 3.15 | Tactical |
| L1-alibaba-qwen | 4 | 2 | 2 | 4 | 4 | 3 | 3 | 3 | 3.15 | 3.00 | Tactical |
| L1-moonshot-kimi | 3 | 4 | 2 | 3 | 3 | 2 | 2 | 3 | 2.80 | 2.80 | Experimental |
| L1-zai-glm | 4 | 4 | 2 | 4 | 3 | 2 | 3 | 3 | 3.25 | 3.15 | Tactical |
| L1-mistral | 4 | 4 | 3 | 5 | 4 | 3 | 4 | 4 | 3.90 | 3.85 | Strategic |
| L1-google-gemma | 3 | 4 | 3 | 5 | 4 | 4 | 4 | 4 | 3.80 | 3.80 | Strategic |
| L1-meta | 3 | 4 | 2 | 4 | 4 | 2 | 3 | 3 | 3.15 | 3.05 | Tactical |

## (c) Accuracy spot-checks

Claims were checked against the cited fact cells in `products.json` and `regulatory_facts.json`, the CP1 ambiguity resolutions and the archived extracts.

| Section | Checked | Examples | Mismatches |
|---|---:|---|---|
| L1 | 24 | GPT-6 Astra 3 Sep (API 4 Sep, Bedrock GA 8 Sep), Sol and Luna 22 Sep, 6.1 Sol 29 Sep, GPT-5.6 still offered, no "Terra" in GPT-6; Astra/Sol/Luna prices; OpenAI SOC 2/ISO scope and ISO 42001 wording; Fable 5.1 1 Sep, Opus 5.5 22 Sep, Sonnet 5.5 28 Sep, Haiku 5.5 7 Oct; Anthropic certificate scope incl. Foundry-on-Azure "In-Process Q4 2026"; inference geography global/us only and the Bedrock/Google EU +10%; Fable 5 suspension 12 Jun–1 Jul; N.D. Cal. 27 Aug and D.C. Cir. No. 26-1049 25 Sep (2–1, stayed); Gemini 3.1 Pro preview since 19 Feb, 3.8 Flash GA 2 Sep, 3.5 Flash-Lite 21 Jul, Argon 30 Sep, 3.8 Flash price doubling 1 Jan 2027; 3.7 Flash retirement 28 Jan 2027 (B-L1-S003); Grok 4.7 21 Sep; SpaceX close 2 Feb; Mistral Large 4 preview 6 Oct, Medium 3.5 28 Apr, Medium 3.1 retired 31 Aug (B-L1-S002); Gemma 4 dates; Muse dates and the contributor tier; DeepSeek V4-Pro 1.6T/49B, V4.1-Flash 10 Sep, phase-out reversal 17 Sep; Qwen3.8 dates and Bedrock Qwen3 regions; Kimi K3 16/27 Jul and cross-Region profiles; GLM-5.3 14/18 Aug, Flash 26 Aug MIT, Bedrock 5 Oct, Entity List 16 Jan 2025; GPAI CoP signatories and xAI's single chapter; DORA 18 Nov 2025 and UK CTP 13 Jul 2026; adequacy to 27 Dec 2031 and C-703/25 P | One miscount in the §1.8 scoring note ("eight" families with a 2 or below; there are seven). Fixed. |
| L3 | 20 | langgraph 1.2.14 (6 Oct), 1.0 17 Oct 2025, Platform → LangSmith Deployment 14 Oct 2025, LSU pricing 1 Oct 2026, ISO 27001 "claimed, scope unconfirmed"; llama-index-core 0.14.25 and workflows 2.25.0; Pydantic AI 2.0.0 23 Jun 2026 and the v1 six-month fixes; crewai 1.15.24 and 1.0 20 Oct 2025; SOC 2 June 2026 and HIPAA "Type 1"; openai-agents 0.23.1; Agent Builder deprecation 3 Jun, **shutdown 30 Nov 2026**; Assistants sunset 26 Aug; Agents API beta 10 Sep; Claude Agent SDK rename 29 Sep 2025, 0.2.164 Alpha (PyPI now 0.2.165, still Alpha: B-REVC-S001); MAF 1.0 2 Apr (3 Apr conflict stated), 1.20.0; AutoGen last release 30 Sep 2025; ADK 2.0 19 May 2026 and 2.11.0; Strands 1.58.1 and 1.0 15 Jul 2025; AgentCore GA 13 Oct 2025; Temporal Cloud 14 AWS + 6 GCP regions; temporalio 1.34.0; mistralai 3.1.0 / 3.0.0 / workflows 3.15.0 Beta; ai 7.0.131 and majors; Workflow SDK 5.1.0 | None |
| L2 | 19 | vllm 0.31.0 and PyTorch Foundation 7 May 2025; vLLM 2026 CVEs; sglang 0.5.21, RadixArk US$100M seed 5 May 2026; CVE-2026-3059 (now with NVD fix reference); ai-dynamo 1.5.1 Beta and the 1.0 README conflict; NVAIE one-month branches; llm-d CNCF sandbox March 2026, v0.7 May 2026, founders; Ollama Cloud plans 31 Aug 2026; LM Studio terms; **TGI archived 21 Mar 2026 at v3.3.7**; HF SOC 2 scope and BAA not tied to Endpoints; **OpenRouter–Stripe agreed 19 Aug 2026, pending, no price used**; US$113M Series B; 5.5% fee; Cerebras IPO 13 May 2026 and no HIPAA; Together SOC 2/ISO vendor-stated and inconsistent HIPAA; Fireworks ISO conflict not relied on; Fireworks Series D July 2026 | Two precision points: SGLang patch status; llm-d scheduling status. Both fixed. |

**L1 precision requirements (all hold).**
- *Lineups and dates:* as corrected at CP1/A′. GPT-6 is a family with no Terra. Fable 5.1 is the top GA tier. Gemma 4, not 2.9. GLM, not "QI4". Medium 3.5 supersedes 3.1. Muse is real, and Llama 4 is still the latest Llama.
- *SpaceXAI:* "SpaceXAI (formerly xAI)" with no rebrand date. The further rename is described only as "announced on 4 October 2026 and had not taken effect", and "SpaceXSI" appears nowhere.
- *D.C. Circuit:* the holding only (upheld, 2–1, stayed pending rehearing), with an explicit "makes no claim about scope" in §1.7 and §1.11.
- *Distillation:* only as "Anthropic alleges", and now also outside the Kimi limitations list in the JSON.
- *Benchmarks:* no vendor benchmark is used as an input, and the rationales say so.
- *Chinese-vendor prices:* Reported only, in the §1.4 table, and "not decision inputs" in the cost rationales.
- *GPT-6 Astra:* the GA conflict (OpenAI "not yet generally available" vs AWS GA) is stated as a conflict.
- *DeepSeek V4-Pro:* still offered, with the reversal of 17 September cited. No V4.1-Pro.
- *CAISI:* GLM-5.3's "about four months behind" is CAISI's verified finding. The DeepSeek "8 months" figure (V2 §4 item 4) is not used.

**L2 and L3 precision requirements (all hold).**
- *OpenRouter:* "agreed, pending", with the press value excluded explicitly.
- *TGI:* archived (21 March 2026) and in maintenance mode, with HF recommending vLLM or SGLang.
- *Agent Builder:* shutdown 30 November 2026, in the executive summary, the deep dive, the FS note and the key facts.
- *CrewAI:* "earlier materials call it CrewAI Enterprise, but no explicit rename notice was found". No Renamed flag is applied.

## (d) Cross-layer observations

1. **Each cloud now has a complete conditional Strategic agent stack.** These read as alternative per-cloud stacks, not as cumulative recommendations, as the CP3 rework log notes.
   - *AWS:* Strands with AgentCore (L3), AgentCore Gateway and Identity (L4), AgentCore Memory (L5), AgentCore Gateway (C1), Bedrock Guardrails (C2), Cedar/AgentCore Policy (C4).
   - *Google:* ADK with Agent Engine (L3, after this review), Memory Bank (L5), Gemini Embedding (L7), Document AI (L8), Gemini (L1), Apigee (C1), Model Armor (C2), SDP (C3).
   - *Microsoft:* Microsoft Agent Framework (L3, on score), APIM AI gateway (C1), Content Safety (C2), Purview DSPM (C3), Entra Agent ID (C4).
2. **Strategic below 3.6 is now common, and Tactical above 3.6 also exists.**
   - 18 Strategic items sit below FS 3.6. All of them rest on rule 10 (14 items, including L1 Gemini, L3 AgentCore and L3 ADK) or on a reader decision (CP3 Q1: MCP and MCP authorisation; CP3 Q6: Entra and Okta).
   - Conversely, five Tactical items score FS ≥ 3.6 with no criterion below 3: L9 Opik 3.75, L9 DeepEval 3.70, L6 Weaviate 3.70, L7 Cohere 3.70 and L2 Fireworks 3.65.
   - So "FS ≥ 3.6 with no 2s" has never made a product Strategic automatically. The Anthropic tier (Q1) is a judgement under rule 9 whichever scores are used.
3. **L1 mixes routes across criteria.**
   - Enterprise readiness is scored on the best hyperscaler route (rule 6).
   - Security is scored on the vendor's own certifications (the section's stated method), and for DeepSeek on its hosted API (1).
   - This is internally consistent across all eleven families, but it means that a Chinese-origin family's FS total describes neither its acceptable route nor its unacceptable one. Q3 offers a cleaner alternative.
   - Synthesis should present the tier condition (route) as the decision, not the total.
4. **Hyperscaler model services are not scored anywhere.** L2's recommendation defaults to "managed model access … through the hyperscaler estate you already operate", but Bedrock, Foundry and Vertex model access have no records. Under rule 10 each would be Strategic, conditional on its cloud. Stage C should state this, or treat them as covered by the L1 family records and the C1 gateways.
5. **The same vendor sits in different tiers by layer, and the lens differences are stated.**
   - Anthropic: L1 Tactical (Q1); Claude Agent SDK Experimental; MCP Strategic (the reader's CP3 decision); Agent Skills Tactical.
   - OpenAI: L1 Strategic; Agents SDK Tactical.
   - Mistral: L1 Strategic; Agents API Experimental; OCR (L8).
   - Google: Gemini, Gemma, ADK and Gemini Embedding all Strategic, conditional.
   - The pattern is that model families score above their vendors' agent SDKs, which are pre-1.0 or Alpha (OpenAI, Anthropic) or beta (Mistral). The exceptions are Microsoft and Google, whose frameworks are 1.x/2.x GA.
6. **AgentCore now has five records** (L3, L4, L5, C1, C4).
   - Security 4 and deployment 2 agree everywhere.
   - Cost differs: L3 3 (runtime pricing NPV) against L4 4. Lock-in differs: L3 2 against L4 3.
   - These follow evidence and lens and are not errors, but synthesis should give one AgentCore view.
7. **The "resolve borderline against" rule, as practised.**
   - Six Anthropic criteria were resolved against Anthropic across L1 and L3, plus the CP3 MCP and turbopuffer calls.
   - On peers, two of the six are not borderline: L1 technical 4 and ecosystem 4 are the neutral values.
   - Two are departures larger than a borderline call: L1 cost 3 and security 4.
   - One is applied more strictly than its peers: Claude Agent SDK maturity 1.
   - The rule was designed to break genuine ties. Applied as here, it can move a tier, so the tier is the reader's decision (Q1).

## (e) Questions for the human

**Q1. Anthropic (L1): which scores, and which tier? (conflict of interest: the reviewer is an Anthropic model and has not changed these scores).**

As drafted: technical 4, enterprise readiness 4, security 4, deployment 3, ecosystem 4, maturity 3, cost 3, lock-in 3. That gives FS 3.55 and generic 3.60, Tactical. The writer resolved four calls against Anthropic.

The reviewer's neutral-rubric reading:
- **Technical 4 and ecosystem 4 are the neutral values.** On peers they are not borderline:
  - OpenAI and Gemini cover more plan §5 questions, including open weights and audio or image output.
  - OpenAI's API is the de facto interface.
- **Cost: neutral value 4.**
  - Anthropic's list prices are identical to OpenAI's at every tier: Fable 5.1 = Astra (US$10/US$50); Sonnet 5.5 = GPT-6.1 Sol (US$2/US$10); Haiku 5.5 = Luna (US$0.10/US$0.50) [VF: A5-S011, A5-S004]. OpenAI scores 4.
  - A regional premium does not hold a peer at 3: Mistral (10% EU endpoint) and Grok (1.1x US endpoint) both score 4.
  - The "dearer recommended default" is a deployment choice, not a vendor price.
- **Security: neutral value 5.**
  - Rule 8's test for 5 is met: SOC 2 Type II, ISO 27001 and ISO 42001, with scope covering the API, Bedrock and Google Cloud, plus CMEK documented [VF: A5-S021, V2-S063, A5-S013].
  - Pinecone and Elasticsearch score 5 on similar evidence.
  - The writer's reasons for 4 are real but go beyond the rule: no first-party EU/UK inference, and the Fable ZDR conflict. The anchor lists residency and ZDR as optional extras.
- **Maturity 3 is defensible** on the June 2026 suspension of the top tier. The rationale's "four models in five weeks" is not, because OpenAI shipped four GPT-6 models in four weeks and scores 4 on maturity.

The resulting totals are:
- cost 4 only: FS **3.60** (generic 3.70);
- cost 4 and security 5: FS **3.80** (generic 3.85);
- the writer's own neutral case (technical 5, ecosystem 5, cost 4): also FS 3.80.

Tactical items at FS ≥ 3.6 with no 2s exist (Opik, Cohere, Fireworks), and Gemini is Strategic at 3.35 under rule 10.

- **(a) As drafted.** Scores as drafted, FS 3.55, Tactical. The conflict-of-interest rule is read as licence to resolve any arguable call against the author's company.
- **(b) Neutral-rubric scores and Strategic, conditional.** Cost 4 and security 5, FS 3.80. Strategic, conditional on consumption through a hyperscaler EU or UK region with a qualified non-Anthropic fallback. This parallels OpenAI (Strategic, 4.05).
- **(c) Neutral-rubric scores but Tactical on judgement.** Cost 4 and security 5, FS 3.80, but kept Tactical. The stated reason is the absence of first-party EU/UK processing plus the June 2026 suspension, as Cohere is held Tactical at 3.70 on a stated reason. The table then shows the true score and the tier carries the judgement.

**Q2. Does rule 10 apply to model families (Gemini Strategic at FS 3.35)?**

Rule 10 was written for platform services. Its one approved model application is L7 Gemini Embedding (Strategic at 3.20). Applied to Gemini, rule 10 puts Gemini above Anthropic (3.55) and Grok (3.25) in tier while it scores lower. The section states that this is a platform rule, not a quality judgement.
- **(a) As drafted.** Rule 10 covers a cloud's lead first-party model family; no FS floor.
- **(b) Platform services only.** Gemini and Gemini Embedding become Tactical, "default where Google Cloud is primary". Model families are tiered on score and judgement alone.
- **(c) Keep rule 10 for models, with a portfolio condition.** The condition: "Strategic only as one of two qualified mid-tier vendors on that cloud". This matches L1's own two-vendor recommendation. No tier change.

**Q3. Hyperscaler presumption for Chinese-origin families (DeepSeek, Kimi, GLM at enterprise readiness 4).**

The routes that support the 4 are:
- DeepSeek: Microsoft Foundry sells V4 directly, in the customer's geography.
- Kimi K3: Bedrock US, India and global cross-Region profiles only.
- GLM-5.3: Bedrock cross-Region only. GLM 5 runs in-Region in London.

On Foundry, Kimi and GLM run on Fireworks outside the tenant, and that route is correctly not used. The vendors' own APIs would score 2.
- **(a) As drafted.** Any cloud-operated route qualifies, including cross-Region profiles; a pass-through does not.
- **(b) In-region only.** The presumption applies only where the current model is cloud-operated in an approved UK/EU region:
  - Kimi drops to enterprise readiness 2 (FS 2.80 → 2.50);
  - GLM drops to 2 (FS 3.15 → 2.85);
  - DeepSeek is unchanged, subject to confirming EU Data Zone availability.
  - No tier changes.
- **(c) Vendor as counterparty.** Score enterprise readiness on the vendor's own API for all Chinese-origin families, matching how their security is scored:
  - DeepSeek 2.85, Kimi 2.50, GLM 2.85.
  - The hyperscaler route moves into the tier condition only.
  - No tier changes.

**Q4. Claude Agent SDK maturity: 1 or 2? (conflict of interest: the reviewer has not changed this score).**

The SDK self-classifies "Development Status: 3 - Alpha" [VF: B-REVC-S001]. The OpenAI Agents SDK is also pre-1.0 (0.23.1) but declares no status classifier, and scores 2. Across the corpus, pre-1.0 products mostly score 2–4:
- LlamaIndex 2, llm-d 2, SGLang 3, vLLM 4.
- The only 1 is LangMem, at 0.0.x with no release in a year.

The neutral-rubric value is 2: FS 2.65 → 2.75, generic 2.75 → 2.85. The tier stays Experimental. Its technical 3 and deployment 3 are peer-consistent and need no change.
- **(a) As drafted.** Maturity 1. The vendor's own Alpha label is a distinguishing fact.
- **(b) Neutral value 2.** Treat the Alpha classifier as already reflected in tier and limitations; FS 2.75.
- **(c) Strict anchor for both.** The Claude Agent SDK and the OpenAI Agents SDK both score 1 on maturity. The OpenAI Agents SDK falls to FS 3.20 and stays Tactical.

**Q5. The 3.55–3.65 band in L2 and L3: SGLang, Fireworks, Hugging Face and Pydantic AI.**

The products in the band are:
- SGLang (3.65, Tactical): security 2 rested on "no patched version listed" and disclosure-response concerns. NVD and OSV now reference a fix in 0.5.10 [VF: B-REVC-S002], while the GitHub advisory still lists none.
- Fireworks (3.65): Tactical, "candidate".
- Hugging Face (3.60): Strategic, conditional, for the Hub as the supply source.
- Pydantic AI (3.55): Tactical.

- **(a) As drafted.** SGLang security 2 and Tactical (rule 11). The rest unchanged.
- **(b) SGLang security 3.** The fix is referenced, but disclosure concerns remain, which matches vLLM's 3. This gives FS 3.85 with no criterion below 3: Strategic, conditional, as the qualified second engine at ≥ 0.5.10 with internal ports isolated. The rest unchanged.
- **(c) Stricter.** Hugging Face becomes Tactical. Its security 3 (no ISO 27001) is the same as Fireworks', so vLLM is the only Strategic product in L2. SGLang stays as in (a).

**Q6. Google ADK after the rule-10 tier change: re-base its scores on Agent Engine?**

The AWS record (Strands with AgentCore) is scored as a managed service: rule 6 enterprise readiness 4, rule 8 security 4, deployment 2. The Google record is scored as a library: rule 2 enterprise readiness 3, security 3, deployment 4.
- **(a) As now.** Tier Strategic, conditional; library scores kept (FS 3.35). The record's fact cells describe the library, with Agent Engine as the deployment target.
- **(b) Re-base on ADK plus Agent Engine.** Enterprise readiness 4 (rule 6) and security 4 (rule 8, Agent Platform SOC 2 and ISO 42001 scope) give FS 3.70. Deployment stays 4, because the ADK library is portable.
- **(c) Revert both to Tactical.** Neither a framework nor its runtime is a rule-10 "lead service" in the sense the reader approved at CP3. AgentCore and ADK both become Tactical, "default in that estate". Microsoft Agent Framework stays Strategic on score.

## Files changed

- `work/stageB/L3/section.md`, `work/stageB/L3/assessments.json`: ADK tier; Claude Agent SDK note. Totals were rewritten by `python3 -I tools/score.py … --write`.
- `work/stageB/L2/section.md`, `work/stageB/L2/assessments.json`: SGLang CVE evidence; llm-d wording.
- `work/stageB/L1/section.md`, `work/stageB/L1/assessments.json`: Anthropic documentation; Kimi allegation entry.
- `work/stageB/_review/all_scores.md` (regenerated)
- `work/stageB/_review/sources_added_C.csv` (new)
- `Enterprise_GenAI_Stack_Oct2026/06_References/snapshots/B/B-REVC-S001.extract.txt`, `B-REVC-S002.extract.txt`
- `work/stageB/_review/CP4_review_C.md` (this file)

**Not changed:** `MEMORY.md`, any score outside L3/L2/L1, and any Anthropic score. `git` was not run. `tools/build_dataset.py` should be re-run after the reader's CP4 answers.
