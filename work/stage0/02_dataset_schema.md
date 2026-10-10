# Stage 0: Product dataset schema (plan §7)

Every product is one JSON object. The final dataset (`05_Data/products.json` and `products.xlsx`) is an array of these objects, about 120 products with about 30 fields each.

## 1. Fact cells

Every factual field is a **fact cell**, not a bare string:

```json
{ "v": "Apache-2.0", "label": "Verified fact", "src": ["A4-S017"], "conf": "high" }
```

| Key | Meaning |
|---|---|
| `v` | The value. A string, number or list. Must be `"Not publicly verified"` when no source supports it. Never guessed. |
| `label` | One of `Verified fact` (primary source), `Reported` (secondary source), `Architectural judgement`, `Recommendation`, `Not publicly verified` |
| `src` | Source IDs from the stream's `sources.csv` (format `A<stream>-S<nnn>`). Required for `Verified fact` and `Reported`. Empty for judgements. |
| `conf` | `high` = primary source, current and unambiguous · `medium` = primary but undated/older, or several consistent secondary sources · `low` = single secondary source or inference |
| `asof` | Optional. Date the fact applies to, if different from the access date (e.g. a pricing page dated earlier) |

Blocks H (assessment) and I (classification) are written in Stage B. Stage A leaves them empty, except that `stage_a_notes` may hold observations for the writers.

## 2. Fields

| # | Block | Field | Type | Notes |
|---:|---|---|---|---|
| 1 | Key | `id` | string | `L9-langfuse`, `C1-litellm`, `L1-openai` |
| 2 | Key | `layer` | string | `L1`…`L9`, `C1`…`C8` |
| 3 | Key | `original_label` | string | Exactly as printed in the graphic (`null` for control-plane products) |
| 4 | A | `current_name` | fact | Official current product name |
| 5 | A | `company` | fact | Owner, plus parent company if acquired |
| 6 | A | `category` | fact | e.g. "serving engine", "managed vector DB", "eval platform" |
| 7 | A | `version_or_lineup` | fact | Latest release/version with date; for L1, the current model family and tiers |
| 8 | A | `licence_model` | fact | Open source (licence) / open core / proprietary / open weights (licence) / open specification |
| 9 | A | `strategic_direction` | fact | Recent announcements, roadmap and pivots (dated) |
| 10 | A | `status_events` | fact | Acquisitions, renames, deprecations or supersessions, with dates. Empty list if none found. |
| 11 | B | `what_it_does` | fact | Two or three sentences, from official docs |
| 12 | B | `stack_position` | fact | Where it actually sits; whether the graphic's placement is right |
| 13 | B | `dependencies` | fact | Runtime and infrastructure dependencies |
| 14 | B | `integration_model` | fact | API, SDK, protocol (MCP/OpenAI-compatible/OTel), connectors |
| 15 | C | `deployment` | object of facts | Keys: `saas`, `managed_cloud`, `vpc_byoc`, `private_cloud`, `self_hosted`, `on_prem`, each `Yes`/`No`/`Not publicly verified` |
| 16 | D | `certifications` | fact | SOC 2 Type I/II, ISO 27001/27701/42001, HIPAA, FedRAMP, C5, etc. |
| 17 | D | `gdpr_residency` | fact | GDPR/DPA availability, regions (EU/UK processing), zero data retention |
| 18 | D | `security_features` | fact | Encryption at rest/in transit, CMK/BYOK, private networking |
| 19 | D | `access_controls` | fact | SSO/SAML/OIDC, SCIM, RBAC, audit logs |
| 20 | D | `enterprise_support` | fact | SLA, support tiers, named enterprise plan |
| 21 | E | `pricing` | fact | Public pricing (dated), usage model and free tier. "Contact sales" where that is all that is published |
| 22 | E | `infra_cost_note` | fact | Self-hosting cost drivers (GPU, storage), where relevant |
| 23 | F | `ecosystem` | fact | Integrations, frameworks and clouds supported |
| 24 | F | `adoption_signals` | fact | GitHub stars, downloads, named customers, funding: dated and sourced |
| 25 | F | `maturity` | fact | Age, GA vs beta, release cadence |
| 26 | G | `strategic_risk` | object of facts | Keys: `lock_in`, `acquisition`, `funding`, `ecosystem_dependency`, `proprietary_api`, `maturity` |
| 27 | H | `assessment` | object | Stage B. Keys: `capabilities`, `strengths`, `limitations_risks`, `choose_when`, `avoid_when`, `competitors` (2–4), `fs_note` |
| 28 | I | `classification` | object | Stage B. `{tier: Strategic\|Tactical\|Experimental, flags: [...], rationale}` |
| 29 | I | `scores` | object | Stage B. Eight criteria, each scored 1–5, with weighted totals for the generic and FS weights (plan §8.1) |
| 30 | J | `sources` | list | Source IDs used for this product (union of all `src`) |
| 31 | — | `stage_a_notes` | string | Free text for writers, e.g. open questions or conflicting sources |
| 32 | — | `last_verified` | date | Access date of the newest source used |

**Status flags** (plan §8.2): `Deprecated`, `Acquired`, `Renamed`, `Superseded`, `Duplicated`, `Not recommended`, `Not publicly verified`.

## 3. Per-stream source log (`sources.csv`)

```text
id,url,title,publisher,source_type,accessed,access_status,archive_path,used_for
```

`source_type` is one of:

- `primary-docs`
- `primary-announcement`
- `primary-trust-centre`
- `regulatory`
- `independent-technical`
- `secondary-news`
- `secondary-aggregator`

`access_status` is one of:

- `original`: PDF saved
- `snapshot`: text extracted from a direct fetch
- `extract`: search-tool extract saved, because the host is blocked by the research environment's egress policy
- `link-only`: paywalled, blocked or failed. Cited by link only; never worked around.

## 4. Example (abridged)

```json
{
  "id": "L2-vllm",
  "layer": "L2",
  "original_label": "vLLM – high-throughput",
  "current_name": {"v": "vLLM", "label": "Verified fact", "src": ["A4-S031"], "conf": "high"},
  "company": {"v": "vLLM project (open source; originated UC Berkeley Sky Computing Lab)", "label": "Verified fact", "src": ["A4-S031"], "conf": "high"},
  "version_or_lineup": {"v": "Not publicly verified", "label": "Not publicly verified", "src": [], "conf": "low"},
  "deployment": {"saas": {"v": "No", "label": "Verified fact", "src": ["A4-S031"], "conf": "high"}, "self_hosted": {"v": "Yes", "label": "Verified fact", "src": ["A4-S031"], "conf": "high"}},
  "assessment": null, "classification": null, "scores": null,
  "sources": ["A4-S031"], "stage_a_notes": "", "last_verified": "2026-10-07"
}
```
