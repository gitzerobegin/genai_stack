# CP4 and CP4b decisions (answered up front)

**Date:** 9 October 2026

The questions were asked before the drafts were produced, at the user's request. The tranche-3 review is in `work/stageB/_review/CP4_review_C.md`.

## CP4: calibration and synthesis

| Q | Decision (user) | Effect |
|---|---|---|
| CP4-1 Anthropic tier | **Neutral score, Strategic** | Re-score the departing criteria to neutral rubric values (reviewer C: cost 4, security 5), giving FS ≈ 3.80. L1 Anthropic becomes Strategic alongside OpenAI and Mistral. **The user made this decision.** The conflict-of-interest disclosure stays, and an independent alternative is always named. |
| CP4-2 Gemini under rule 10 | **Keep (no floor)** | Gemini stays Strategic, conditional on Google Cloud being the primary cloud |
| CP4-3 DeepSeek, Kimi, GLM via hyperscalers | **Keep credit (enterprise readiness 4)** | State the hosting caveat in the text: on Azure, Kimi and GLM run on Fireworks outside the tenant |
| CP4-4 Borderline tiers | **Upgrade all four to Strategic, conditional** | • Google ADK / Agent Engine: where Google Cloud is primary<br>• SGLang: qualified backup engine to vLLM, once CVE-2026-3059 is confirmed fixed<br>• Pydantic AI: Python teams wanting type-safe agents<br>• Fireworks AI: managed open-model inference, once its ISO certificates are confirmed |
| CP4-5 Lead reference stack | **A. Regulated enterprise** | Stacks B, C and D are presented as alternatives |
| CP4-6 Cloud in the worked example | **Stay cloud-neutral** | AWS, Azure and Google Cloud equivalents shown side by side |
| CP4-7 Avoid list | **Evidence-based only** | Deprecated or archived, unverifiable, unresolved security incident for client data, or a licence blocker |
| CP4-8 Roadmap horizon | **18 months** | Aligned to PS7/26 (18 March 2027) and EU AI Act Annex III (2 December 2027) |
| CP4-9 Claude Agent SDK maturity | **Both pre-1.0 SDKs at 2** | The Claude Agent SDK and OpenAI Agents SDK both score maturity 2. The Alpha label is noted. The Claude Agent SDK stays Experimental. |
| Hugging Face (reviewer Q5) | Not ticked | Stays Strategic, conditional (as drafted) |

## CP4b: LinkedIn series

| Q | Decision |
|---|---|
| Start date | **First Tuesday after CP5 sign-off**, at about 08:00 UK time. Tuesday is the stack post, Thursday the control post. |
| Clearance | **No pre-clearance needed.** Keep the compliance checklist per post, with no clearance batching. |
| Hashtags | **Topic-specific**, at most 2 per post |
| Already decided | 24 posts over 13 weeks · 220–300 words · vendor names only in the first comment · a visual brief per post · an anecdote slot plus a fallback version · British spelling · the `linkedin-post-generator` voice rules |

## Run mode

**Run to CP5 with no pauses at CP4 or CP4b.** Anecdote slots are left with prompts for the user to fill later. Stop earlier only if a genuinely new question appears.
