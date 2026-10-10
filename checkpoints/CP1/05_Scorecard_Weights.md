# Scorecard weights (plan §8.1), for confirmation at CP1

Decision 3 in the execution prompt accepts the plan's weights. They are reproduced below, with the Stage A evidence that bears on them. Scoring itself happens in Stage B.

| Criterion | Generic enterprise | Regulated FS |
|---|---:|---:|
| Technical capability | 20% | 15% |
| Enterprise readiness | 15% | 15% |
| Security and compliance | 15% | 20% |
| Deployment flexibility (SaaS / VPC / self-hosted) | 15% | 15% |
| Ecosystem / integration | 10% | 5% |
| Reliability and maturity | 10% | 10% |
| Cost / total cost of ownership | 10% | 5% |
| Lock-in / portability / concentration risk | 5% | 15% |
| **Total** | **100%** | **100%** |

## Stage A evidence relevant to the weights

1. **Concentration risk is real, but sits in the cloud layer, not the model layer.** Under DORA, the first CTPP list (18 November 2025) and the UK CTP designations (13 July 2026) name hyperscalers (AWS, Google Cloud, Microsoft; Oracle in the UK). Neither names any AI model vendor. Model-vendor dependence is therefore governed through firms' own outsourcing and third-party rules, not through direct oversight of the vendor:
   - PRA PS7/26 and FCA PS26/2, with notifications from 18 March 2027
   - the new EBA guidelines (EBA/GL/2026/09)

   This supports the 15% FS weight on lock-in and concentration.
2. **Consolidation is a strategic-risk signal.** Many of the tools have changed owner or announced a deal in 2025–2026: Arize, Langfuse, Promptfoo, Portkey, Guardrails AI, Lakera, Protect AI, Helicone, Tavily, Voyage, Jina and OpenRouter (pending). These events feed the *Lock-in* and *Reliability and maturity* scores through dataset block G (strategic risk), not through a separate criterion.
3. **The US model-risk anchor has moved.** SR 11-7 was superseded on 17 April 2026 by SR 26-2 (with OCC Bulletin 2026-13 and FDIC FIL-15-2026), and generative and agentic AI are **out of scope** of the new guidance. PRA SS1/23 (effective 17 May 2024) still applies to AI models. The FS weights do not need to change, but the FS lens text must.
4. **Evidence gaps are large for smaller vendors.**
   - 1,557 of 4,620 fact cells are "Not publicly verified".
   - These are concentrated in certifications, EU regions, SSO/RBAC and pricing for start-ups.
   - Much of this is an artefact of the research environment: most vendor and trust-centre sites could not be fetched directly.
   - How NPV is scored matters as much as the weights: see question Q2 in the CP1 summary.
