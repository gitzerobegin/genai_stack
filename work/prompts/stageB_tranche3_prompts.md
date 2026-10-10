# Stage B, tranche 3 and the CP3 rework: prompts as executed (8 October 2026, after CP3)

**Setup.** Four background `general-purpose` agents. Each writer starts with the standard preamble:

```text
FIRST read and follow exactly: work/stage0/07_stageB_writer_brief.md and work/stage0/08_scoring_rubric.md (ALL rules 1–13). Read checkpoints/CP2/03_CP2_Decisions.md and checkpoints/CP3/06_CP3_Decisions.md. Use work/stageB/L9/section.md as the reference example; skim work/stageB/_review/all_scores.md for calibration. No word cap. ≤10 searches; sources B-<L>-S###.
```

| Agent | Scope | Outputs | Key guidance |
|---|---|---|---|
| **CP3 rework** | Apply CP3 Q1 and Q2 across all 14 drafted sections | `work/stageB/_review/CP3_rework_log.md`, edited sections and assessments, regenerated `all_scores.md` | **Q1:** L4 MCP and C4 MCP authorisation become one decision, Strategic (conditional), with a note that the reader set the tier. L4 A2A becomes Strategic (conditional). Tier changes only, no score changes. **Q2 (rule 10):** the lead hyperscaler service in each category becomes Strategic, conditional on it being the primary cloud. Keep the two AgentCore gateway records consistent. **Q9:** verify only. Run `score.py` and `check_tags.py`. |
| **L3 writer** | Agent frameworks and orchestration (12 products) | `work/stageB/L3/` | **Conflict-of-interest disclosure for the Claude Agent SDK**: Alpha status, Claude-only, Commercial Terms, a subprocess per session, Managed Agents excluded from ZDR; borderline calls resolved against it; alternatives named. H2 (workflows vs agents). Microsoft Agent Framework GA; OpenAI Agent Builder shutdown; LangSmith Deployment rename; Mistral Workflows built on Temporal. Worked example: a deterministic graph with one judgement step, durable execution and an approval gate. |
| **L2 writer** | Inference, serving and model access (11 products) | `work/stageB/L2/` | H1 split: serving, optimisation, access. Self-hosting is a capacity and operating-model decision. OpenRouter → Stripe (pending; no press values). Hugging Face is four products; TGI archived. Cerebras IPO. ZDR defaults. LM Studio licence. vLLM under the PyTorch Foundation. Managed model access via the hyperscalers as a pattern. Rule 2 for self-hosted engines. |
| **L1 writer** | Foundation-model vendor families (11) | `work/stageB/L1/` | **Most acute conflict of interest: Anthropic.** Disclosure at the top and in the deep dive; borderline calls against Anthropic; controversies stated precisely (D.C. Circuit holding only, not scope; the Fable 5 suspension; Bartz; distillation only as "Anthropic alleges"). No vendor benchmarks. Lineups as corrected at CP1. Treat models as a portfolio. Chinese-origin vendors: hosted API vs self-hosted weights, data location, Entity List, device bans. FS lens: SS1/23, SR 26-2's GenAI exclusion, GPAI vs deployer duties, concentration, exits. |

**After this tranche:** a calibration reviewer for L3–L1, then Stage C synthesis (lead architect plus one reviewer), then CP4.
