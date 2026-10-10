# CP2 decisions

**Date:** 8 October 2026

| Q | User's answer | Rule applied from now on |
|---|---|---|
| Q1: NPV cap for hyperscaler services | "yes" (option b, hyperscaler presumption) | Services consumed through AWS, Azure or Google Cloud inherit platform IAM, SSO and audit logging as **verified by default**. Enterprise readiness scores **4** unless product-specific evidence shows a gap. Add a due-diligence note: "platform controls presumed (CP2 Q1); confirm per service". |
| Q2: Partial evidence on enterprise readiness | "as much as possible" (option c, lenient) | **Any one** verified control among SSO, RBAC and audit logs lifts the NPV cap, to a maximum of 3. Two or three verified, plus SCIM, an SLA or an admin API, can reach 4–5 on the anchors. |
| Q3: What "Strategic" requires | Option 1: judgement (as now) | Architect's judgement, normally FS ≥ 3.6 and no criterion at 1. A weakness of 2 is allowed if it is stated as a condition. |
| Q4: Certifications whose product scope is not stated | "use your default" (option a) | Company- or platform-level certifications whose product scope is not stated score **one point below** the anchor |
| Q5: Length | "keep that length; if it takes more, go for it" | No word cap per layer or per deep dive. Depth over brevity. |
| Q6: Format and failure stories | "yes" (option a) | Standardise deep dives on **L9's labelled-bullet format**. Keep **one "Illustrative scenario [AJ]" per layer**, in the main text. |
