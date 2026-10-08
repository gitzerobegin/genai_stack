# Scoring rubric (plan §8.1, with the CP1 Q2 decision)

## Scale and weights

- Each criterion is scored **1 to 5 (integers)**.
- **5 means best in class for an enterprise**, not merely "has the feature".
- Totals are weighted averages on the same 1–5 scale, computed by `tools/score.py`:

| Criterion | Key | Generic | FS |
|---|---|---:|---:|
| Technical capability | technical | 20% | 15% |
| Enterprise readiness | enterprise_readiness | 15% | 15% |
| Security and compliance | security_compliance | 15% | 20% |
| Deployment flexibility | deployment_flexibility | 15% | 15% |
| Ecosystem / integration | ecosystem | 10% | 5% |
| Reliability and maturity | reliability_maturity | 10% | 10% |
| Cost / TCO | cost_tco | 10% | 5% |
| Lock-in / portability / concentration | lockin_portability | 5% | 15% |

## Anchors

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| **Technical** | Missing a core function of the layer | Covers the core function competently; gaps in advanced features | Leading depth across the layer's research questions (plan §5), evidenced in primary docs |
| **Enterprise readiness** | No SSO, RBAC, audit or support documented | SSO, RBAC and audit logs on an enterprise tier; named support | All of these plus SCIM, SLA, admin APIs, multi-tenancy and enterprise contracts |
| **Security and compliance** | No certification, or an unremediated serious incident | SOC 2 Type II, encryption at rest and in transit, a DPA | SOC 2 Type II **and** ISO 27001, plus some of: ISO 42001, HIPAA, FedRAMP, CMK/BYOK, ZDR, regional residency |
| **Deployment flexibility** | One SaaS region only | SaaS plus one of VPC/BYOC/self-hosting | SaaS, BYOC/VPC, self-host/on-prem and air-gap |
| **Ecosystem** | Isolated | Mainstream integrations | De-facto standard; open interfaces (OTel, OpenAI-compatible, SQL, MCP) with broad adoption |
| **Reliability and maturity** | Pre-1.0 or beta, maintenance mode, or archived | GA with a steady release cadence | Years of production use, stable governance, LTS or foundation-hosted |
| **Cost / TCO** | Opaque and expensive, or a heavy operations burden | Transparent and competitive | Free or permissive OSS with light operations, or clearly efficient pricing |
| **Lock-in / portability** | Proprietary format and API, no export, unstable ownership | Proprietary but on standard interfaces; data exportable | Open standard, open source, permissive licence, neutral governance |

## Evidence rules

**1. NPV cap (CP1 Q2a).**
- If the primary evidence for **enterprise readiness** or **security and compliance** is "Not publicly verified", that criterion is **capped at 2**. Primary evidence means: for enterprise readiness, SSO/RBAC/audit; for security and compliance, certifications.
- Record each cap in `evidence_caps_applied`.
- Vendor-only claims that a verifier flagged in section 4 of a verification log count as NPV for this rule.

**2. Self-hosted libraries and open specifications** (e.g. DeepEval, Docling, SBERT, pgvector, OPA). Vendor certifications are not applicable, so do not apply the NPV cap. Instead:
- score security on project hygiene: security policy, CVE handling, signed releases, licence clarity, supply-chain incidents;
- score enterprise readiness on what the library enables inside your own estate, plus any commercial support offer;
- note "inherits host controls";
- cap both criteria at 4 unless a commercial support or hardened distribution exists.

**3. Ownership change** (acquired, or acquisition announced, in 2025–26).
- Reduce **lockin_portability** by 1 unless the product is permissively licensed open source with neutral governance.
- Mention the change in the reliability rationale.
- Add the flag `Acquired`.

**4. Licence risk.** AGPL, BUSL, ELv2, CC-BY-NC or custom commercial thresholds count as a lock-in and cost consideration. They do not disqualify a product; state them.

**5. Calibrate within the layer.**
- At least one product should usually score 2 or below on some criterion. If none does, justify it.
- Avoid giving every product a 4.

## CP2 calibration rules (binding from 8 October 2026; see `checkpoints/CP2/03_CP2_Decisions.md`)

**6. Hyperscaler presumption (Q1).** A service consumed through AWS, Azure or Google Cloud inherits platform IAM, SSO and audit logging as verified. Enterprise readiness is 4 unless there is evidence of a product-specific gap. Add the note "platform controls presumed (CP2 Q1); confirm per service". Security still follows rule 8.

**7. Partial evidence (Q2).** Any one verified control among SSO, RBAC and audit logs lifts the NPV cap, to a maximum of 3. Use the anchors above 3: all three controls plus SCIM, an SLA or admin APIs can reach 4–5.

**8. Certification scope (Q4).** Company- or platform-level certifications whose coverage of the product is not stated score one point below the anchor. A security score of 5 needs SOC 2 Type II **and** ISO 27001 within the product's scope, **plus** at least one of: CMK/BYOK, ISO 42001, FedRAMP.

**9. Strategic tier (Q3).** Architect's judgement, normally FS ≥ 3.6 and no criterion at 1. A criterion at 2 is allowed if stated as a condition, e.g. "Strategic only if X is your standard".

## CP3 rules (binding from 8 October 2026; see `checkpoints/CP3/06_CP3_Decisions.md`)

**10. Hyperscaler lead services (CP3 Q2).** The lead service in a category on AWS, Azure or Google Cloud is **Strategic, conditional "where this is your primary cloud"**. It must have no criterion at 1. Other hyperscaler services are Tactical, "default in that estate". Security stays at 4 under rule 8.

**11. Strategic with a criterion at 2 (CP3 Q5).** Allowed only when the condition is an existing platform commitment, e.g. "where Elastic, MongoDB or Kong is already operated". A net-new proprietary dependency with lock-in 2 stays Tactical.

**12. Evidence for 4 (CP3 Q3).** Any primary vendor page counts, with the limitation stated as a condition.

**13. Certification caps (CP3 Q9).** Keep the caps. A platform capped only for missing product-scoped certification may carry "candidate for Strategic after due diligence". Vendor regulatory-mapping claims never raise a score.

## Tiers (plan §8.2)

| Tier | Definition |
|---|---|
| **Strategic** | Suitable as a core enterprise platform component. Usually an FS total of 3.6 or more, with no criterion at 1. |
| **Tactical** | Useful for specific scenarios, but not a foundational dependency. |
| **Experimental** | Promising but immature, changing fast, or unsuitable as a critical dependency. |

- The tier is a judgement informed by the score, not computed from it. State the rationale.
- **Flags:** Deprecated · Acquired · Renamed · Superseded · Duplicated · Not recommended · Not publicly verified
