## C8. Model risk, governance and auditability

> **Executive summary.** This control answers the questions a regulator, auditor or board will ask about any GenAI system. What is it, and who owns it? Was it independently validated for this use? Is it still performing? Who approved this output, on what evidence? Can we reproduce what happened? The original graphic had no governance control [AJ]. The regulatory ground moved sharply in 2026. In the US, SR 26-2 superseded SR 11-7 on 17 April 2026 and expressly places generative and agentic AI **outside** its scope, leaving their governance to each firm's own risk practices [VF: R-US-MRM, A8-S001, A8-S002, V2-S049]. US firms therefore have to write their own GenAI standard. In the UK, PRA SS1/23 (effective 17 May 2024) is technology-agnostic and covers vendor models [VF: R-PRA-SS123, A8-S008]. In the EU, the AI Act's GPAI obligations became enforceable on 2 August 2026, and the Annex III high-risk duties moved to 2 December 2027 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011, A8-S019]. SS1/23 and the AI Act are therefore the operative anchors [AJ]. The vendor market is consolidating around "AI control plane" positioning: Collibra announced its acquisition of trail ML on 5 October 2026 [VF: A7-S101, A7-S105, V2-S044], and IBM added agent Enforcement Tracking to watsonx.governance on 11 August 2026 [VF: A7-S111]. Two findings shape the recommendation. First, the evidence that matters is produced elsewhere: by evaluation (L9), gateway logs (C1), prompt versions (C5) and security testing (C7). The eval suite *is* most of the validation evidence, provided it is independent, versioned and retained [AJ]. Second, no governance platform reaches Strategic on public evidence today; only one vendor, ValidMind, claims to map to SS1/23 [VF: A7-S052], and certification evidence is thin for most [AJ]. **Recommendation:** own the inventory schema and the evidence store (immutable, firm-controlled, joined by trace and version IDs); use OpenLineage for data lineage; then choose a governance workflow tool to fit the estate (ValidMind for MRM-led banks, watsonx.governance for IBM estates, Collibra where it is already the data catalogue, Credo AI for policy-led programmes) as a replaceable layer over that evidence [Rec].

### C8.1 Responsibility

**The problem this control owns.** It owns the firm's ability to show, at any time, that each AI system is known, classified, validated for its intended use, approved by an accountable person, monitored, changed under control, and reproducible from retained evidence [AJ]. The plan lists eleven jobs. They group into four:

- **Know.**
  - *Inventory:* every AI use case and the components that make it up.
  - *Classification:* materiality tier and regulatory category (MRM scope, EU AI Act risk class, outsourcing materiality).
  - *Lineage:* where the data came from and which model, prompt and index versions produced each output.
- **Assure.**
  - *Validation:* independent challenge before use and after material change.
  - *Explainability:* why an output says what it says.
  - *Monitoring:* thresholds, alerts and periodic review.
- **Decide.**
  - *Policy:* the firm's own standard, mapped to external obligations.
  - *Approval:* go-live, material changes and exceptions.
  - *Human approval of outputs* where the use case requires it.
  - *Change management:* triggers for re-validation.
- **Prove.**
  - *Evidence:* the audit evidence pack per use case and per output.
  - *Regulatory evidence:* the artefacts each regime expects, retained under the records policy.

**Hand-offs.** This control produces little evidence itself; it governs evidence produced by others [AJ]:

| From | What C8 receives [AJ] |
|---|---|
| L9 evaluation and observability | Eval results with dataset, metric and judge versions; traces; online monitoring; reviewer edits |
| C5 prompt and config management | Prompt, template and configuration versions; change events (for example webhooks on prompt commits [VF: A7-S076]) |
| C1 gateway | Model identifiers and versions actually called; request counts used to reconcile the inventory |
| C4 identity | Identity of the human approver and of the agent; delegation records |
| C7 security | Red-team findings, supply-chain records (scan results, artefact hashes, signatures), incidents |
| L8 ingestion | Data lineage (sources, document IDs, index versions), classification labels |
| C6 FinOps | Cost per task, needed for proportionality and materiality decisions |

C8 sends approvals and release decisions back to the release gate (L9 and the deployment pipeline), policy thresholds to L9 monitors, and exceptions and findings to owners [AJ].

**The governed unit.** For GenAI, the unit of governance is the **AI use case**, not the foundation model alone [AJ]. A use case record binds together the foundation model and its exact version, the prompt template, the retrieval configuration and index version, the tools and their permissions, the orchestration graph, the guardrail configuration and the eval suite. A change to any of them is a change to the governed system [AJ]. The definitional question of whether an LLM or agent is a "model" is answered in §C8.11.

### C8.2 Why it matters

Three things break when this control is weak [AJ]:

- **The firm cannot say what it is running.** Teams call models through personal keys, aliases resolve to new model versions without notice, and nobody can list which use cases depend on a deprecated model [AJ].
- **Validation evidence does not match production.** A validation report approved one model version and prompt; production runs another. The approval no longer means anything [AJ].
- **Outputs cannot be reproduced or defended.** When a client, auditor or regulator asks why a document said what it said, the firm cannot reconstruct the inputs, the model version, the retrieved context or the approver [AJ].

Regulators across jurisdictions expect ongoing monitoring and records:

- AI Act Article 26 requires deployers of high-risk systems to monitor operation and keep logs for at least six months [VF: R-EUAIA, A8-S016].
- ESMA expects "regular AI model testing" and ex-post output controls [VF: R-INTL-AI-ASSETMGMT, A8-S059].
- IOSCO's toolkit names human-intervention indicators for asset managers [VF: R-INTL-AI-ASSETMGMT, A8-S058].

The failure is usually discovered at the worst time: in an audit, a complaint or a supervisory review [AJ].

**Illustrative scenario [AJ].** Fourteen months after launch, an internal audit samples a client report produced with a GenAI drafting assistant. A client has queried one paragraph. The audit asks the team to show the validation that covered the model used, the prompt in force that day, the source documents retrieved and who approved the text. The validation report names a model version the provider has since retired; the application called a "latest" alias, so the gateway logs show three different versions over the period. The prompt lives in a notebook with no history. The retrieval index has been rebuilt twice and the old versions deleted. The approver's sign-off is an email "looks fine". The traces were on a 30-day vendor tier. Nobody can say whether the queried paragraph was grounded or invented. The firm re-reviews every report produced in the period by hand and reports the gap to its board risk committee. None of this needed new technology; it needed an inventory entry pinned to versions, an evidence pack per output and retention set by the records policy. The scenario is invented; it is not a reported incident.

### C8.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Inventory completeness | Share of model endpoints, keys and agents seen at the gateway that map to an inventory entry | 100%; unmapped traffic is blocked or raised as an exception | Gateway logs (C1) reconciled to inventory weekly |
| Version pinning | Share of production use cases calling a pinned model version, not an alias | 100% for material use cases | Gateway configuration and logs |
| Validation currency | Material use cases with a validation covering the current model, prompt, index and tool versions | 100% before go-live; re-validation within the agreed window after a trigger | Inventory vs change log |
| Re-validation lead time | Time from a material change (model, prompt, index, tool, vendor) to completed re-validation | Days, not months, for tier-1 | Change and validation records |
| Periodic review on time | Reviews completed by due date, by tier | ≥95% | Governance workflow |
| Evidence-pack completeness | Outputs with a complete pack (prompt version, model version, data snapshot, tool calls, eval results, approver, timestamps) | 100% for approved outputs | Automated check at release; sample audit |
| Reproducibility | Sampled past outputs whose evidence pack can be re-performed (same inputs, same checks, results within thresholds) | 100% of sample | Quarterly re-performance test |
| Monitoring breach handling | Threshold breaches triaged within SLA; breaches leading to suspension where policy requires | Per tier | L9 alerts linked to governance tickets |
| Human-intervention rate | Share of outputs edited or rejected by the approver, and edit size | Tracked; spikes reviewed | Reviewer diffs (L9) |
| Retention compliance | Logs and packs retained for the records-policy period (and ≥6 months where Article 26 applies) | 100% | Archive audit |
| Findings closure | Validation and audit findings closed by due date | ≥90% | Governance workflow |

The last two KPIs serve the IOSCO indicators on human intervention and output accuracy [VF: R-INTL-AI-ASSETMGMT, A8-S058] and ESMA's ex-post controls [VF: R-INTL-AI-ASSETMGMT, A8-S059] [AJ].

### C8.4 How it works

The control is a lifecycle wrapped around a firm-owned evidence store.

1. **Intake and classification.** A new use case is registered with owner, purpose, users, data classes, model and vendor, and autonomy level. It is then tiered by materiality and classified for each regime: MRM scope under the firm's standard, EU AI Act category (prohibited, Annex III high-risk, Article 50 transparency, minimal), and outsourcing materiality (SYSC 8, SS2/21, DORA) [AJ]. Governance tools automate parts of this: ModelOp offers self-service intake and risk tiering [VF: A7-S098]; Credo AI and watsonx.governance discover AI systems, including unmanaged agents, tools, MCP servers and models in watsonx.governance's case [VF: A7-S102, A7-S111].
2. **Development with evidence.** The team builds the eval suite alongside the system (L9). Test results and documentation artefacts are logged to the governance record; the ValidMind Library does this from Python development environments [VF: A7-S003].
3. **Independent validation.** A party independent of development reviews conceptual soundness (is an LLM appropriate, are the boundaries right?), re-performs or extends the evals, red-teams (C7), and records findings and use limitations [AJ]. SR 26-2 keeps "effective challenge by qualified, independent reviewers" for models in its scope [VF: R-US-MRM, A8-S001]. SS1/23 Principle 4 requires independent validation [VF: R-PRA-SS123, A8-S008].
4. **Approval.** An accountable owner approves go-live against the validation report, with conditions. SS1/23 allocates responsibility for the MRM framework to an SMF holder [VF: R-PRA-SS123, A8-S008].
5. **Release gate and production.** Only the approved combination of versions can deploy. Each output that needs human approval passes a gate, and the approver's identity is captured from C4 [AJ].
6. **Monitoring.** Online evaluations, drift and human-intervention metrics run against thresholds set in the governance record. A breach raises a ticket and, where the policy says so, suspends use [AJ]. ValidMind supports thresholds, alerts and workflow triggers on breach [VF: A7-S056]. watsonx.governance Enforcement Tracking retrieves agent evaluation metrics on a schedule and checks them against business-set thresholds [VF: A7-S111].
7. **Change management.** Defined triggers start re-validation: model version, prompt or template, retrieval index or embedding model, tools or permissions, guardrail configuration, vendor or hosting region, or a monitoring breach [AJ].
8. **Periodic review and attestation.** Each use case is reviewed on a cycle set by its tier. ValidMind's attestation feature lets owners or validators formally certify key details about a model at a point in time [VF: B-C8-S005].
9. **Retirement.** Evidence is retained after decommissioning for the records period [AJ].

```text
            ┌──────────────────────── C8 governance workflow (replaceable tool) ─────────────────────────┐
 intake ─► classify/tier ─► develop+evals ─► independent validation ─► approve ─► release ─► monitor ─► review/retire
              │  (MRM, AI Act,      │ (L9)          │ (L9 re-run, C7 red-team)   │ (SMF/owner)   ▲   │ thresholds
              │   outsourcing)      │               │                            │               │   ▼
              ▼                     ▼               ▼                            ▼          change triggers:
 ┌─────────────────────────────────────────────────────────────────────────────────────┐  model/prompt/index/
 │  FIRM-OWNED EVIDENCE STORE (immutable, records-policy retention)                     │  tool/vendor/breach
 │  inventory entry ─ version bundle (model, prompt, index, tools, guardrails, evals)    │
 │  validation reports ─ approvals ─ monitoring results ─ incidents ─ attestations       │
 │  per-output evidence packs  ◄── trace ID ── L9 traces / C1 gateway logs / C5 versions │
 │  data lineage  ◄── OpenLineage events from L8 pipelines (custom GenAI facets)        │
 └─────────────────────────────────────────────────────────────────────────────────────┘
```

The key design choice is that the **evidence store is firm-owned and the governance tool reads and writes to it** [AJ]. Governance platforms change hands and positioning quickly; evidence has to outlive them [AJ].

### C8.5 Enterprise design principles

**Governance**

- Govern the use case, not the model name. Pin every component version in the inventory entry, and treat a change to any of them as a change to the system [Rec].
- Tier by materiality. A tier-3 internal summariser should not need the validation depth of a client-facing or investment-decision use case [AJ]. SR 26-2 is explicitly risk-based and materiality-driven for in-scope models [VF: R-US-MRM, A8-S001]; the same logic suits a firm's own GenAI standard [AJ].
- Keep validation independent of the vendor whose model is under test. A model vendor's own evaluation tool weakens the independence claim; the L9 analysis applies this to Promptfoo, which OpenAI announced it would acquire on 9 March 2026 [VF: A1-S024, V2-S042] [AJ].
- Explainability for an LLM is mainly traceability and grounding, not feature attribution [AJ]. Show which sources, tool outputs and instructions produced each statement, and keep inference visibly separate from source data [AJ].

**Auditability and observability**

- Make the evidence pack automatic and complete by construction. The gateway, trace store, prompt registry and approval gate all write to it under one trace ID [AJ].
- Reconcile the inventory against the gateway. Any model traffic without an inventory entry is shadow AI [AJ].
- Store evidence immutably (WORM or an equivalent append-only store) under the records policy, not a vendor tier [AJ].

**Security and residency**

- Governance records hold use-case descriptions, risk assessments and sometimes sample data. Treat the governance platform as confidential and apply C3 rules [AJ]. ValidMind states that it does not store PII or customer data in documentation [VF: A7-S054].
- Prefer EU or UK hosting, or self-hosting, for governance records about client-facing systems [Rec].

**Scalability and cost**

- Automate evidence collection; manual evidence gathering does not scale beyond a few dozen use cases [AJ].
- Governance pricing units vary: per evaluation [VF: A7-S103], per instance and concurrent user [VF: A7-S103], or unpublished [VF: A7-S003, A7-S109].

**Portability**

- Keep the inventory schema, the evidence store and the eval suites in firm-controlled formats. Use the governance tool's APIs to read and write them, not as the system of record for raw evidence [Rec].
- Use OpenLineage for data lineage, so the catalogue or governance tool can change without re-instrumenting pipelines [Rec].

**Patterns [AJ]:** use case as governed unit with a pinned version bundle; evidence store with per-output packs keyed by trace ID; gateway-to-inventory reconciliation; change triggers wired to C5 and C1 events; thresholds held in governance and enforced by L9 monitors; periodic attestation; independent validation sandbox.

**Anti-patterns [AJ]:** inventory as a spreadsheet updated quarterly; model aliases ("latest") in production; validation by the development team only; approval by email; evidence held only inside a vendor platform; retention set by a free tier; treating a vendor's "EU AI Act policy pack" as compliance.

### C8.6 Product selection criteria

| Scorecard criterion | What to evaluate in this control [AJ] |
|---|---|
| Technical (15% FS) | Coverage of inventory, classification, validation workflow, monitoring with thresholds, change triggers, approvals, attestation, lineage, policy mapping; ingestion of L9 eval results and traces; agent and GenAI support, not only classic ML |
| Enterprise readiness (15%) | SSO, RBAC and audit logs of who approved what; segregation of duties between developer, validator and approver; SCIM; workflow configurability; APIs |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in product scope; ISO 42001 as a signal; where governance records are hosted |
| Deployment flexibility (15%) | SaaS with EU or UK region; single-tenant or self-hosted for firms that will not put risk records in multi-tenant SaaS |
| Ecosystem (5%) | Connectors to ML platforms, catalogues, GRC tools; OpenLineage; SDKs |
| Reliability and maturity (10%) | Vendor stability; release cadence; positioning churn ("control plane" pivots); acquisitions |
| Cost / TCO (5%) | Pricing transparency; implementation effort |
| Lock-in / portability (15%) | Export of inventory, documentation and evidence; open formats; licence (AGPL library for ValidMind) |

**On vendor regulatory claims.** Every mapping of a product to a regulation below is a vendor claim, not an assessment [AJ]. The claims found, as of 7–8 October 2026, are:

| Vendor | EU AI Act | NIST AI RMF | ISO 42001 | SR 11-7 / SR 26-2 | PRA SS1/23 |
|---|---|---|---|---|---|
| ValidMind | Yes [VF: A7-S053] | Blog only [VF: A7-S121] | Blog only [VF: A7-S121] | SR 26-2 [VF: A7-S051] | Yes [VF: A7-S052] |
| Credo AI | Yes [VF: A7-S102] | Yes [VF: A7-S102] | Yes [VF: A7-S102] | Not found [VF: A7-S110] | Not found [NPV] |
| IBM watsonx.governance | Yes [VF: A7-S103] | Yes [VF: A7-S103] | Yes [VF: A7-S103] | SR 11-7 [VF: A7-S103] | Not found [NPV] |
| ModelOp | Yes [VF: A7-S098] | Yes [VF: A7-S098] | Yes [VF: A7-S098] | SR 11-7; some pages cite SR 26-2 [VF: A7-S098] | Not found [NPV] |
| Collibra | Yes [VF: A7-S099] | Yes [VF: A7-S099] | Collibra itself certified [VF: A7-S100] | Not found [NPV] | Not found [NPV] |

Two observations follow [AJ]. A mapping to SR 11-7 now points to a superseded instrument, and SR 26-2 excludes the GenAI systems these tools are increasingly sold to govern. Only one vendor claims SS1/23, the instrument most relevant to UK firms. A policy pack is a starting checklist, not evidence of compliance [AJ].

### C8.7 Product deep dives

**ValidMind (ValidMind Inc.).**
- *What it is now:* a model risk management and AI governance platform. The Library runs tests and logs documentation artefacts from Python model-development environments. The Platform holds a customisable model inventory and runs documentation, validation workflows, approvals and ongoing monitoring, with thresholds, alerts and workflow triggers on breach [VF: A7-S003, A7-S054, A7-S056]. It has LLM test extras and LLM features for test interpretation and document checking [VF: A7-S003, A7-S097]. Model attestation lets owners or validators certify key model details at a point in time [VF: B-C8-S005].
- *Versions and licence:* Library 2.13.14 was released on 3 September 2026 [VF: A7-S003, V2-S028]. The Library is dual-licensed AGPL-3.0 or ValidMind Commercial Licence; the Platform is proprietary [VF: A7-S003, A7-S051].
- *Regulatory mapping (vendor claims):* use-case guides map the platform to SR 26-2, PRA SS1/23, the EU AI Act (Article 9) and OSFI E-23 [VF: A7-S051, A7-S052, A7-S053, A7-S057]. It is the only vendor in this set that claims SS1/23 [VF: A7-S110] [AJ].
- *Deployment and security:* multi-tenant cloud, or single-tenant Virtual Private ValidMind on AWS, GCP or Azure, with private connectivity [VF: A7-S054, A7-S084]. RBAC, audit logs, data isolation and encryption in transit and at rest are documented [VF: A7-S055]. It claims to meet SOC 2, GDPR and CCPA requirements without stating a SOC 2 type, and no SOC 2 Type II report or ISO certificate was found [VF: A7-S121, B-C8-S005].
- *Strengths:* the closest fit to a bank-style MRM workflow (inventory, documentation, validation, monitoring) with GenAI test support [AJ].
- *Limitations:* certification evidence is a vendor statement [VF: A7-S121]. SSO and self-hosting are not publicly verified [NPV]. Pricing is not published [VF: A7-S003].
- *Choose when:* the second line runs a formal MRM function and wants GenAI to enter the same validation workflow as other models [AJ].
- *Avoid when:* you need a broad AI-policy and third-party AI register more than model validation, or you cannot obtain a SOC 2 Type II report [AJ].
- *Competitors:* watsonx.governance, ModelOp, Credo AI.
- *FS note:* request the SOC 2 Type II report before loading risk records; check whether AGPL obligations matter for any modified Library code you distribute [Rec].
- **Tier: Tactical. No flag.** It would move towards Strategic for MRM-led firms once certification evidence is obtained [AJ].

**Credo AI.**
- *What it is now:* an AI governance platform. It auto-discovers and catalogues AI systems in an AI Registry, applies pre-built policy packs (EU AI Act, NIST AI RMF, ISO 42001, SOC 2) drawn from a knowledge graph of more than 160 policies and 110 controls, and generates audit-ready evidence and audit trails [VF: A7-S102]. It is moving to agent governance with an Agent Registry and runtime governance, and integrates the AIUC-1 agent standard without issuing certification [VF: A7-S102]. It also has policy packs for OMB M-25, Colorado ADMT and NAIC AI [VF: A7-S102].
- *Positioning:* the vendor contrasts its enterprise governance with SR 11-7-style model risk management [VF: A7-S110].
- *Deployment and access:* SaaS on AWS (US) or Azure (EU), or self-hosted on Kubernetes, including air-gapped installs [VF: A7-S107, A7-S123]. SSO via OIDC (SAML via dex) for self-hosted, SCIM, audit logs with APIs and role scopes in tokens [VF: A7-S123].
- *Certifications:* the trust centre lists a SOC 2 Type II report [VF: A7-S107], but the verifier could not re-confirm its date or content [VF: V2-S064]. No ISO 27001 or 42001 certificate was found [VF: A7-S107].
- *Other:* the open-source Lens framework is deprecated; its last release was 1.1.8 in May 2023 [VF: A7-S092, A7-S093]. Funding is reported at about US$39–42m, with the last disclosed round in July 2024 [R: A7-S108].
- *Strengths:* the widest deployment choice in this set (EU SaaS, self-hosted, air-gapped) and strong identity controls [AJ].
- *Limitations:* light on model validation and monitoring; no SR 26-2 or SS1/23 mapping found [VF: A7-S110] [AJ].
- *Choose when:* the programme is policy- and compliance-led (EU AI Act classification, third-party AI risk) across many business units [AJ].
- *Avoid when:* the main need is quantitative validation of models [AJ].
- *Competitors:* Collibra AI Governance, watsonx.governance, ModelOp.
- *FS note:* self-host or use the Azure EU instance; obtain the current SOC 2 report directly [Rec].
- **Tier: Tactical. No flag.**

**IBM watsonx.governance (IBM).**
- *What it is now:* the broadest platform here. It inventories AI use cases and models, evaluates models, prompt templates and agents, monitors them in production, and ties metrics to risks, controls and approvals. Compliance Accelerators map obligations to controls [VF: A7-S103, A7-S111, A7-S058]. 2026 additions include AI Asset Discovery (9 July 2026), which finds unmanaged agents, tools, MCP servers and models, and Enforcement Tracking (11 August 2026), which retrieves agent evaluation metrics on a schedule and checks them against governance thresholds, plus Guardium security metrics per use case [VF: A7-S111]. Factsheets capture model facts and can be exported to support audits [VF: B-C8-S003].
- *Versions:* continuous SaaS updates; v2.2.0 introduced policy packs; SDK ibm-watsonx-gov 1.5.2 (18 September 2026) [VF: A7-S103, A7-S058]. Regulatory horizon scanning (CUBE) was previewed at Think 2026 [VF: A7-S111].
- *Deployment:* SaaS on IBM Cloud or AWS, software in customer-managed AWS or Azure, and on-premises or hybrid [VF: A7-S103].
- *Access control:* on AWS, IAM controls access to service instances and the Governance console manages finer access; administrators manage users and roles; approval workflows leave an audit trail [VF: B-C8-S003].
- *Certifications:* the dataset records FedRAMP authorisation on AWS GovCloud from an IBM page [VF: A7-S103]. A Stage B search found the same IBM announcement saying IBM is "on our way to receiving the FedRAMP Moderate authorization", and no SOC 2 or ISO 27001 attestation naming watsonx.governance [VF: B-C8-S002]. Product-scoped certification is therefore not publicly verified [NPV].
- *Pricing (indicative, varies by country):* Lite free tier; Essentials pay-as-you-go at US$0.64 per model evaluation with about 100 free; GRC per-instance and per-concurrent-user charges; an AWS SaaS bundle at US$38,160; self-managed per virtual processor core [VF: A7-S103]. The source table was garbled, so confirm prices [VF: A7-S103].
- *Strengths:* agent-aware governance that consumes evaluation and security evidence automatically [AJ].
- *Limitations:* no PRA SS1/23 or SR 26-2 claim was found; the SR 11-7 accelerator maps to a superseded instrument [VF: A7-S103] [AJ]. The SDK is under IBM's licence for non-warranted programs [VF: A7-S058].
- *Choose when:* you run watsonx Orchestrate or OpenPages, or want one platform for discovery, evaluation and governance of agents [AJ].
- *Avoid when:* you want the governance tool independent of your agent runtime vendor [AJ].
- *Competitors:* ValidMind, ModelOp, Credo AI.
- *FS note:* obtain the SOC 2 and ISO scope letters naming watsonx.governance; if IBM also supplies Vault (C7), record IBM as one concentration point [Rec].
- **Tier: Tactical, conditional: a candidate for Strategic in IBM-centred estates once product-scoped certification is confirmed, because security is capped at 2 only by missing evidence [AJ]. No flag.**

**ModelOp Center (ModelOp).**
- *What it is now:* AI governance and lifecycle automation, positioned as an "Enterprise AI Command Center". It keeps an inventory of AI systems with self-service intake, risk tiering and approvals, and applies controls from internal policies and regulations through more than 25 governance process templates and more than 100 tests and controls. Risk-based workflows can block non-compliant actions [VF: A7-S098]. It claims to govern ML, GenAI, agentic, internal and third-party AI, with inline protections for agents against prompt injection, PII leakage and unsafe tool use [VF: A7-S098].
- *Deployment and access:* Kubernetes on Amazon EKS via AWS Marketplace, self-hosted, on-premises or hybrid [VF: A7-S109]. It integrates with enterprise identity providers using OAuth2 and SAML for role-based access [VF: B-C8-S001].
- *Certifications:* no SOC 2 or ISO 27001 evidence was found [VF: B-C8-S001] [NPV].
- *Company:* privately held in Chicago; it raised US$10m led by Baird Capital, date not confirmed [VF: A7-S104].
- *Regulatory mapping (vendor claims):* EU AI Act, NIST AI RMF, SR 11-7 (some pages cite SR 26-2), ISO 42001 and OSFI E-23 templates [VF: A7-S098, A7-S110].
- *Strengths:* lifecycle automation that can enforce, not only record [AJ].
- *Limitations:* the thinnest public evidence in this set: certifications, release cadence and SaaS availability are not publicly verified [NPV].
- *Choose when:* you want self-hosted governance automation with blocking workflows, and will do full due diligence [AJ].
- *Avoid when:* certification evidence is a gate at shortlisting [AJ].
- *Competitors:* watsonx.governance, ValidMind, Credo AI.
- *FS note:* require SOC 2 Type II and audit-log documentation before any pilot with production records [Rec].
- **Tier: Tactical. No flag.**

**Collibra AI Governance (Collibra).**
- *What it is now:* AI governance on Collibra's data intelligence platform, branded AI Command Center and positioned as "The Enterprise AI Control Plane" [VF: A7-S099, A7-S122]. It provides an AI use-case register and model and agent asset domains, links use cases to model versions and agents from integrated AI platforms, and runs EU AI Act and NIST AI RMF assessment templates with 46 controls mapped to EU AI Act, NIST and BCBS 239 articles [VF: A7-S099]. It added AIUC-1 templates in May 2026 and a code-first registry CLI [VF: A7-S122, A7-S099].
- *Ownership:* Collibra announced the acquisition of trail ML (Munich) on 5 October 2026, price undisclosed, to add agent-powered continuous assessment and runtime enforcement [VF: A7-S101, A7-S105, V2-S044]. The deal is three days old and may still move [VF: V2-S044] [AJ].
- *Certifications:* SOC 1, SOC 2, ISO 27001, 27017, 27018, ISO 42001 (January 2025, Schellman), FedRAMP, ITAR, HIPAA and TISAX, at company level [VF: A7-S106, A7-S100, V2-S064].
- *Deployment and access:* SaaS managed on AWS and GCP, with Cloud Sites [VF: A7-S122]. SAML 2.0 SSO with IdP group mapping and global roles [VF: B-C8-S004]. Self-hosting and the EU region list are not publicly verified [NPV].
- *Lineage:* Collibra documents an OpenLineage integration [VF: A7-S122].
- *Strengths:* the only product here that joins the AI inventory to the data catalogue and lineage, which matters for H7 [AJ].
- *Limitations:* SaaS only on current evidence; no model validation or monitoring workflow; pricing not published [NPV] [AJ].
- *Choose when:* Collibra is already your data catalogue of record and you want AI use cases linked to governed data [AJ].
- *Avoid when:* you need self-hosting, or a model-validation workflow [AJ].
- *Competitors:* Credo AI, watsonx.governance, ModelOp.
- *FS note:* the BCBS 239 mapping is useful for bank-owned managers; confirm EU hosting and the trail ML integration roadmap [Rec].
- **Tier: Tactical. No flag** (acquirer, not acquired).

**OpenLineage (LF AI & Data).**
- *What it is now:* an open specification for runtime data-lineage metadata. It defines run, job and dataset entities with consistent naming, extended by facets, and an event protocol for emitting lineage as jobs run; Marquez is the reference implementation [VF: A7-S041, A7-S043]. openlineage-python 1.53.0 (1 September 2026) adds explicit dataset-, field- and job-level lineage facets [VF: A7-S001, A7-S042, V2-S028].
- *Governance and licence:* an LF AI & Data Graduate project, Apache-2.0; Marquez is a separate Graduated project [VF: A7-S041, A7-S043].
- *Ecosystem:* Apache Airflow ships an OpenLineage provider (2.20.2, 29 September 2026); Spark, dbt and Flink integrations; GCP Lineage transport; Collibra integration [VF: A7-S045, A7-S041, A7-S042, A7-S122].
- *Strengths:* the neutral lineage interchange standard; it lets the catalogue and governance tools change without re-instrumenting pipelines [AJ].
- *Limitations:* no GenAI, LLM, embedding or vector facets were found in the changelog [VF: A7-S042]. Parse, chunk, embed and index steps must be modelled as generic jobs and datasets or as custom facets [AJ]. Marquez releases have slowed (0.51.1 in March 2025) [VF: A7-S044].
- *Choose when:* always, for L8 ingestion and index-build pipelines [Rec].
- *Avoid when:* you expect it to capture run-time LLM calls; that is OTel's job (L9) [AJ].
- *Competitors:* proprietary catalogue lineage; OTel GenAI conventions (complementary, run-time).
- *FS note:* define a firm GenAI facet set (source document IDs, classification tags, chunking and embedding model versions, index version) and publish it internally [Rec].
- **Tier: Strategic. No flag.**

**Not assessed.** ServiceNow AI Control Tower and OneTrust AI governance could not be researched, so their materiality is not established [VF: A7-S098] [NPV].

### C8.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C8-validmind | 4 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2.95 | 2.90 | Tactical |
| C8-credo-ai | 3 | 4 | 2 | 5 | 4 | 3 | 2 | 3 | 3.30 | 3.25 | Tactical |
| C8-watsonx-governance | 5 | 3 | 2 | 4 | 4 | 4 | 3 | 3 | 3.60 | 3.40 | Tactical |
| C8-modelop | 4 | 3 | 2 | 4 | 3 | 2 | 2 | 3 | 3.05 | 2.95 | Tactical |
| C8-collibra-ai-governance | 4 | 3 | 4 | 2 | 4 | 3 | 2 | 3 | 3.25 | 3.20 | Tactical |
| C8-openlineage | 3 | 3 | 3 | 5 | 5 | 4 | 4 | 5 | 3.85 | 3.85 | Strategic |

**Scoring notes [AJ]:**
- **NPV caps.** Security is capped at 2 for four products:
  - ValidMind: SOC 2 type not stated; no report found (B-C8-S005).
  - Credo AI: the SOC 2 Type II report is listed in V2 section 4 as not re-confirmed.
  - watsonx.governance: no product-scoped SOC 2 or ISO found, and the FedRAMP wording conflicts (B-C8-S002).
  - ModelOp: no certifications found (B-C8-S001).

  These caps reflect public evidence, not a finding that controls are absent. They are the first thing to resolve in due diligence.
- **Partial evidence (rule 7).**
  - ValidMind: RBAC and audit logs verified, SSO not, so 3.
  - watsonx.governance: roles and an approval audit trail verified, so 3.
  - ModelOp: SAML/OAuth2 and role-based access verified, so 3.
  - Collibra: SAML SSO and roles verified, audit logs not, so 3.
  - Credo AI has SSO, SCIM, audit-log APIs and role scopes, so 4.
- **Hyperscaler presumption (rule 6)** was not applied. watsonx.governance on AWS is IBM's service on AWS, not an AWS service.
- **Certification scope (rule 8).** Collibra's company-level list would reach the anchor for 5 (SOC 2, ISO 27001, ISO 42001, FedRAMP); its product scope is not stated, so it scores 4.
- **Self-hosted specification (rule 2).** OpenLineage is scored on project hygiene (Apache-2.0, foundation governance, monthly releases; no security policy file was found), with enterprise readiness and security at 3.
- **Cost.** Unpublished pricing scores 2. watsonx.governance publishes pricing, so 3. OpenLineage is free but needs a backend, so 4.
- **Tiers.** No governance platform reaches FS 3.6 on public evidence. watsonx.governance (3.40) has the strongest technical coverage and would reach about 3.6 to 3.8 with product-scoped certification. That is why its Tactical tier carries a condition rather than a dismissal.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| ValidMind | Library AGPL-3.0 or commercial; Platform proprietary [VF: A7-S003] | Multi-tenant SaaS; single-tenant VPV on AWS/GCP/Azure [VF: A7-S054, A7-S084] | SOC 2 claimed, type not stated [VF: A7-S121, B-C8-S005] | Not publicly verified [NPV] | ValidMind Inc., independent [VF: A7-S051] |
| Credo AI | Proprietary [VF: A7-S107] | SaaS (AWS US, Azure EU); self-hosted; air-gapped [VF: A7-S107, A7-S123] | SOC 2 Type II listed, not re-confirmed [VF: A7-S107, V2-S064] | Azure Europe [VF: A7-S107] | Independent; last round July 2024 [R: A7-S108] |
| watsonx.governance | Proprietary; SDK IBM ILAN [VF: A7-S058] | SaaS (IBM Cloud, AWS), self-managed, on-prem [VF: A7-S103] | FedRAMP on GovCloud wording conflicts; SOC 2/ISO not product-scoped [VF: A7-S103, B-C8-S002] | Not publicly verified [NPV] | IBM [VF: A7-S058] |
| ModelOp | Proprietary [VF: A7-S109] | EKS via AWS Marketplace, self-hosted, on-prem, hybrid [VF: A7-S109] | Not publicly verified [NPV] | Not publicly verified [NPV] | Private (Chicago) [VF: A7-S104] |
| Collibra AI Governance | Proprietary SaaS [VF: A7-S122] | SaaS on AWS and GCP [VF: A7-S122] | SOC 1/2, ISO 27001/27017/27018, ISO 42001, FedRAMP, HIPAA (company) [VF: A7-S106, A7-S100] | Not publicly verified [NPV] | Collibra; acquirer of trail ML (announced 5 Oct 2026) [VF: A7-S101, V2-S044] |
| OpenLineage | Apache-2.0 [VF: A7-S041] | Self-hosted consumers (Marquez) [VF: A7-S043] | Not applicable (open specification) | In-estate [AJ] | LF AI & Data Graduate project [VF: A7-S041] |

### C8.9 Decision tree

```text
STEP 0 [Rec] (not optional, no product decision):
  - Write the firm's GenAI model-risk standard (scope, tiers, validation depth, triggers,
    evidence pack, retention), to SS1/23 quality, whatever your jurisdiction.
  - Build the firm-owned evidence store and inventory schema (use case = governed unit,
    pinned version bundle, per-output evidence packs keyed by trace ID).
  - Emit OpenLineage from ingestion and index-build pipelines, with firm GenAI facets.

STEP 1 [Rec]: Which governance workflow tool?
  Is there a formal second-line MRM function that already validates models?
  ├─ Yes → Do you want GenAI in the same validation workflow as other models?
  │        ├─ Yes → ValidMind (obtain SOC 2 Type II first)
  │        │        (alt: watsonx.governance if IBM is already in the estate)
  │        └─ No  → keep the MRM tool; add a policy/registry tool below
  └─ No  → What is the programme led by?
           ├─ Policy and compliance (AI Act classification, third-party AI) → Credo AI
           │      (EU SaaS or self-hosted)
           ├─ Data governance (Collibra is the catalogue of record)          → Collibra AI Governance
           ├─ Agent runtime on IBM (watsonx Orchestrate, OpenPages)          → watsonx.governance
           └─ Need enforcement in the lifecycle, self-hosted                 → ModelOp (full due diligence)

STEP 2 [Rec]: Residency and hosting of governance records
  Must risk records stay in-estate or in UK/EU?
  ├─ Yes → self-hosted (Credo AI, ModelOp, watsonx.governance software), or ValidMind VPV,
  │        or Credo AI on Azure EU
  └─ No  → SaaS acceptable; confirm regions in contract

STEP 3 [Rec]: Checks before any tool goes live
  SOC 2 Type II and ISO 27001 scope letters naming the product?
  Export of inventory, documentation and evidence in an open format, tested?
  Inventory reconciled against gateway (C1) traffic?
  Evidence packs written to the firm's archive, not only to the vendor?
```

### C8.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Evidence store (packs, traces, eval results) | **Unacceptable if vendor-held only** | It is the regulatory record; it must outlive any tool and meet the records policy and, where applicable, Article 26 retention [VF: R-EUAIA, A8-S016] | Firm-owned immutable archive keyed by trace ID; tools write to it |
| Inventory and classification data | **Manageable** | Replaceable if exported regularly in an open schema; harder where the tool's knowledge graph or templates hold the logic [VF: A7-S102] | Firm schema; nightly export; API-based sync |
| Validation documentation | **Manageable** | Documents are portable if exported; workflow history is the sticky part [AJ] | Export to the archive at each approval |
| Policy packs and control mappings | **Acceptable** | They are vendor interpretations, and the firm should own its own mapping anyway [AJ] | Firm control library mapped to SS1/23, AI Act, NIST, ISO 42001 |
| Lineage | **Acceptable on OpenLineage** | Open specification, Apache-2.0, neutral governance [VF: A7-S041] | OpenLineage events with firm GenAI facets |
| Governance runtime enforcement (blocking, Enforcement Tracking) | **Manageable** | Coupling to an agent runtime (watsonx Orchestrate [VF: A7-S111]) or a lifecycle engine (ModelOp [VF: A7-S098]) raises switching cost | Thresholds held in governance, enforced by L9 monitors and the release gate |

### C8.11 Regulated FS lens (POV 2)

This control *is* the regulated-FS lens for the stack. Every regulatory statement below carries its record ID.

**1. United States: SR 26-2 and the GenAI carve-out.**
- *The instrument.* SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026 were issued on 17 April 2026. They supersede and replace SR 11-7 (2011) and SR 21-8 (2021), and the OCC rescinded its related bulletins and handbook booklet [VF: R-US-MRM, A8-S001, A8-S002, A8-S005, V2-S049].
- *Who it binds.* It is supervisory guidance, not enforceable in itself, and is expected to be most relevant to banking organisations with more than US$30bn in total assets [VF: R-US-MRM, A8-S002, A8-S003].
- *What it keeps.* Risk-based, materiality-driven MRM; immaterial models identified and monitored for change; effective challenge by qualified, independent reviewers; model risk assessed individually and in aggregate [VF: R-US-MRM, A8-S001, A8-S002].
- *What it excludes.* Generative and agentic AI models are expressly out of scope. For tools and systems not covered, the firm's own risk-management and governance practices should determine controls [VF: R-US-MRM, A8-S001, A8-S002].
- *What may come next.* The agencies said they plan to issue a request for information on MRM and AI, including generative and agentic AI. None had been found published as of 7 October 2026 [VF: R-US-MRM, R-US-AGENCY-AI, A8-S003, A8-S007].
- *Supervisory observation.* The OCC observes banks adopting GenAI and agentic AI in limited use cases "with guardrails and human-in-the-loop accountability" [VF: R-US-AGENCY-AI, A8-S004].
- *Other levers.* The interagency third-party guidance names ongoing monitoring as a lifecycle stage [R: R-US-TPRM, A8-S033]. The SEC's predictive data analytics proposal was withdrawn by Commission action on 12 June 2025 [VF: R-SEC-ADVISERS, A8-S057, V2-S058].
- *Consequence [AJ].* The carve-out does not remove the governance need; it moves the burden to the firm. A US bank-owned manager now has no supervisory template for LLM agents and must write its own standard. Writing it to SS1/23 quality, and keeping the same inventory, validation and monitoring evidence for LLM components, is the safest course, because the planned RFI may reintroduce expectations.

**2. United Kingdom: SS1/23, SM&CR and technology-neutral supervision.**
- *Scope.* SS1/23 was published on 17 May 2023 and took effect on 17 May 2024. It applies to banks, building societies and PRA-designated investment firms with internal-model approval for credit, market or counterparty credit risk capital; insurers are not covered. The PRA later narrowed its expectations to internal-model firms and said it would address other firms later [VF: R-PRA-SS123, A8-S008, A8-S061].
- *The five principles.* (1) model identification and classification, with a complete inventory including AI/ML models; (2) governance, with an SMF holder responsible for the MRM framework and MRM effectiveness reported to the audit committee; (3) development, implementation and use; (4) independent validation; (5) risk mitigants [VF: R-PRA-SS123, A8-S008, A8-S037].
- *Breadth.* It covers all models used to inform business decisions, in-house or vendor, and is technology-agnostic, with explainability and transparency as complexity factors for AI [VF: R-PRA-SS123, A8-S008, A8-S061].
- *AI in practice.* The PRA's October 2025 roundtables covered ongoing monitoring, risk appetite and tiering for AI/ML [VF: R-PRA-SS123, A8-S009]. Members of the Bank of England's AI Consortium report that GenAI is "often classified as high risk" under SS1/23-type frameworks [VF: R-PRA-SS123, A8-S010].
- *FCA position.* The FCA has made no new AI-specific rules; it relies on existing frameworks such as Consumer Duty and SM&CR [VF: R-UK-AI-STATEMENTS, A8-S055].
- *System-wide view.* The FPC judged in March 2026 that GenAI and agentic AI are not yet adopted in a way that presents systemic risk, but that the risks are likely to increase, potentially rapidly [VF: R-UK-AI-STATEMENTS, A8-S056]. A 2025 Bank of England analysis found 55% of AI use cases had some autonomous decision-making and 2% were fully autonomous [VF: R-UK-AI-STATEMENTS, A8-S055].
- *Consequence [AJ].* SS1/23 is not binding on most FCA solo-regulated asset managers. It is still the most complete UK benchmark, and bank-affiliated managers will inherit it. A named senior manager accountable for AI use (SM&CR) is the operative UK lever.

**3. How an LLM or agent fits the definition of a "model".**

The definitions:
- *SR 26-2.* A model is "a complex quantitative method, system, or approach that applies statistical, economic, or financial theories to process input data into quantitative estimates". Simple arithmetic and deterministic rule-based software without such theories are excluded [VF: R-US-MRM, A8-S002].
- *SR 26-2 scope.* Separately, the guidance applies to "non-generative, non-agentic AI models" and places generative and agentic AI models out of scope [VF: R-US-MRM, A8-S001, A8-S002].
- *SS1/23.* Firms adopt SS1/23's definition: a quantitative method, system or approach applying statistical, economic, financial or mathematical theories. The rest of the sentence was not extracted. "Models are a subset of quantitative methods." [VF: R-PRA-SS123, A8-S061].
- *SS1/23 Principle 1.1(b).* Relevant MRM aspects can be applied to material, complex deterministic quantitative methods that are not models [VF: R-PRA-SS123, A8-S061].
- *EU AI Act.* The Act regulates "AI systems" and "general-purpose AI models", not models in the MRM sense. A firm that builds and uses its own system is both provider and deployer [VF: R-EUAIA, A8-S016].
- *Earlier US view.* A 2022 OCC testimony reportedly said AI tools "would be considered models"; it was not archived [NPV].

The architect's answer [AJ]:
- **A foundation model is a model by construction.** It is a statistical method that processes input data into outputs. Its outputs are mostly text, not "quantitative estimates", which is where a literal reading of the US definition strains. SR 26-2 sidesteps the argument by calling GenAI and agentic AI "models" and then excluding them, which defers the question rather than answering it.
- **An agent is a system that contains a model.** The orchestration graph, tools and prompts are deterministic or semi-deterministic logic around a statistical core. SS1/23 Principle 1.1(b) already allows MRM disciplines to extend to material, complex methods that are not models. That is the cleanest UK hook for governing the whole agent, not only the LLM inside it.
- **Where the LLM transforms or explains quantitative estimates, treat it as in scope.** The attribution commentary is the worked example: an LLM turning model outputs into client-facing narrative informs business decisions and client communication, and the firm should govern it as a model-dependent use case.
- **The governed unit is therefore the use case**, with the foundation model recorded as a vendor model component. This works under all three regimes: SS1/23 (vendor model in the inventory, use case tiered), the firm's own standard under SR 26-2's carve-out, and the AI Act (AI system classified by intended purpose).

**4. EU AI Act.**
- *Timeline.* The Act entered into force on 1 August 2024 [R: R-EUAIA, A8-S012]. Prohibitions and AI literacy have applied since 2 February 2025. GPAI obligations applied from 2 August 2025, and the Commission's enforcement powers over GPAI (fines up to 3% of global turnover) from 2 August 2026. GPAI models placed on the market before 2 August 2025 must comply by 2 August 2027 [VF: R-EUAIA, A8-S011, A8-S019].
- *The Digital Omnibus.* Regulation (EU) 2026/1744 was published on 24 July 2026 and entered into force on 27 July 2026. It moved Annex III high-risk obligations to 2 December 2027 and Annex I to 2 August 2028 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011, V2-S050]. GPAI, prohibitions and general transparency timelines are unchanged [VF: R-EU-OMNIBUS-AI, A8-S011].
- *Article 4 literacy (as amended, effective 27 July 2026).* "Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf". The obligation "does not require providers or deployers to guarantee any specific level of AI literacy of any individual". National market surveillance authorities enforce it from 2 August 2026 [VF: R-EUAIA, A8-S060].
- *Annex III points relevant to financial services.* 4(a) and 4(b) employment and worker management; 5(b) creditworthiness and credit scoring (fraud detection excluded); 5(c) risk assessment and pricing for natural persons in life and health insurance [VF: R-EUAIA, A8-S017].
- *Article 26 (deployers of high-risk systems).* Use per instructions; competent human oversight; relevant and representative input data where controlled; logs kept for at least six months (financial institutions within their financial-services documentation); monitoring and informing the provider; suspension and notification on risk; serious-incident reporting; informing workers and affected persons [VF: R-EUAIA, A8-S016].
- *Related articles.*
  - Article 12 provider logging must support post-market and deployer monitoring [VF: A8-S016].
  - Article 27 requires a fundamental rights impact assessment for Annex III 5(b) and 5(c) [VF: R-EUAIA, A8-S017].
  - Under Article 25, a deployer becomes a provider if it rebrands or substantially modifies a high-risk system, or changes an AI system's intended purpose (including a GPAI system) so that it becomes high-risk [VF: R-EUAIA, A8-S016].
  - Article 72 puts post-market monitoring on providers. The Omnibus removed the Commission's power to adopt the Article 72(3) template [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S017, A8-S011].
- *Article 50 transparency.* It has applied since 2 August 2026. Deployers must disclose AI-generated text published to inform the public on matters of public interest, unless it has been human-reviewed under editorial responsibility. Generative systems already on the market have until 2 December 2026 for the Article 50(2) marking duty [VF: R-EUAIA, A8-S018, V2-S078].
- *GPAI providers.* Articles 53 and 55 require GPAI providers to keep technical documentation and inform downstream providers. The Code of Practice was published on 10 July 2025; signatories include Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI and OpenAI [VF: R-EU-GPAI-COP, A8-S015, A8-S035]. Anthropic, the author's developer, is a signatory; this is recorded as fact only [AJ].
- *Consequence for an asset manager [AJ].* A firm using third-party LLMs is normally a deployer. Attribution commentary, research summaries and operations are not Annex III uses. The live duties are therefore literacy, Article 50 where content is published, prohibitions, and vendor documentation under Article 53. HR uses and any credit or life and health insurance pricing would be high-risk from 2 December 2027. Build Article 26-grade logging and monitoring anyway: the same artefacts serve SS1/23, outsourcing and audit.

**5. International supervisory texts for asset managers.**
- *IOSCO.* IOSCO's Supervisory Toolkit (FR/02/2026, dated 25 May 2026) lists indicators for asset managers: the accuracy of AI-supported valuations against benchmarks, AI-driven mis-selling incidents, and the "level and frequency of human intervention in AI-driven investment process". It also flags AI-washing and concentration risk from reliance on a few AI technology providers [VF: R-INTL-AI-ASSETMGMT, A8-S058, V2-S077].
- *ESMA.* ESMA's statement of 30 May 2024 says management bodies remain responsible for decisions whether taken by people or AI tools. It expects robust governance, regular AI model testing and monitoring, ex-ante input controls and frequent ex-post output controls, and due diligence on third-party AI [VF: R-INTL-AI-ASSETMGMT, A8-S059]. A joint ESMA-EBA consultation (25 February 2026) covers management-body suitability, including understanding of AI [VF: R-INTL-AI-ASSETMGMT, A8-S059].
- *Consequence [AJ].* Substantiating AI claims in marketing (against AI-washing) is a C8 evidence artefact. It belongs in the inventory entry.

**6. Standards.**
- *NIST.* AI RMF 1.0 (26 January 2023) remains current but is under revision; no revised version had been published as of 7 October 2026. AI 600-1, the Generative AI Profile, was released on 26 July 2024 [VF: R-NIST-AIRMF, A8-S043, A8-S044, V2-S060]. The function names Govern, Map, Measure and Manage are Reported, not confirmed in the extracts [R: R-NIST-AIRMF, A8-S043]. Cite NIST documents by their published titles, because NIST pages now use "Super Intelligence" terminology [VF: R-NIST-AIRMF, V2-S060].
- *ISO.* ISO/IEC 42001:2023 sets requirements for an AI management system and does not mandate specific AI controls. ISO/IEC 42005:2025 gives guidance on AI system impact assessments. ISO/IEC 42006:2025 (7 July 2025) sets requirements for bodies certifying against 42001 [VF: R-ISO-42001, A8-S045, A8-S046, A8-S047, V2-S057].
- *Consequence [AJ].* 42001 is the management-system wrapper for this whole control. 42005 is a usable template for Article 27-style impact assessments. 42006 makes vendor 42001 certificates more comparable, which matters when Collibra and other vendors cite them.

**7. The governance tool is itself a third party.**
- *Outsourcing duties.* SaaS governance platforms hold risk assessments and validation records. Under DORA they are ICT third-party services for the register of information [VF: R-DORA, A8-S021]. Under SYSC 8 and FG16/5, data location, effective access and exit plans apply [VF: R-FCA-SYSC8, A8-S049]. UK material arrangements need notification from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062, V2-S053].
- *Change of control.* Collibra's trail ML acquisition (announced 5 October 2026) and the general consolidation mean contracts may change [VF: A7-S101, V2-S044]. Plan due-diligence refresh with notification lead time [Rec].
- *Data transfers.* EU-to-US transfers of personal data in governance records rely on the DPF (appeal C-703/25 P pending) or SCCs. EU-UK adequacy runs to 27 December 2031 [VF: R-DATA-TRANSFERS, A8-S052, A8-S053, V2-S055, V2-S059].

**8. Auditability: what "complete" means.** The plan's POV 2 defines it: a complete trace of prompt, model version, data, tool calls, approvals and outputs, with reproducibility and retention [AJ]. §C8.12 makes it concrete.

### C8.12 Worked-example slice (POV 3)

**The inventory entry [AJ].** One record for "Monthly attribution commentary, multi-asset fund range":

| Field | Example content [AJ] |
|---|---|
| Use case and owner | Draft monthly Brinson-style attribution commentary; owner: head of performance reporting |
| Accountable senior manager | Named SMF (SM&CR) for AI use in client reporting |
| Materiality tier | Tier 1: client-facing, regulated communication, uses model outputs (attribution engine) |
| MRM scope | In scope under the firm's GenAI standard; attribution engine separately inventoried as a quantitative model |
| EU AI Act category | Not Annex III; Article 50 assessed (human editorial review applies); deployer of GPAI |
| Outsourcing | LLM provider and gateway SaaS recorded in the register; materiality assessed under SYSC 8 / DORA |
| Version bundle | Model ID and pinned version; fallback model ID and version; prompt template version; retrieval index version and embedding model; tool list and scopes; guardrail and detector configuration; eval suite version; judge model version |
| Validation | Independent validation report reference, date, findings, use limitations ("no figures generated by the model") |
| Approval | Go-live approver, date, conditions |
| Monitoring | Thresholds: numeric faithfulness 100%; groundedness ≥ agreed level; human-intervention rate tracked; breach actions |
| Change triggers | Any version-bundle change; provider deprecation notice; monitoring breach; incident |
| Review cycle | Periodic review and attestation each quarter (tier 1) |
| AI claims | Wording used externally about AI assistance, substantiated (IOSCO AI-washing) |

**The audit evidence pack per commentary [AJ].** Written automatically to the firm's immutable archive at approval, keyed by trace ID:
1. **Prompt version:** template ID and version, the system prompt hash, and the rendered prompt (redacted per C3).
2. **Model version:** provider, model ID and exact version as returned by the gateway (not the alias requested), parameters (temperature, max tokens), region of processing.
3. **Data snapshot:** attribution-engine output snapshot hash and run ID; holdings and benchmark as-of dates; retrieved document IDs, versions and trust tiers; index version.
4. **Tool calls:** each call with arguments, response hash, latency and the identity used (agent and on-behalf-of analyst, from C4 and the secrets broker in C7).
5. **Eval results:** numeric-faithfulness result per figure, groundedness scores, style checks, detector verdicts, with metric code and judge versions and thresholds.
6. **Approver identity:** the portfolio manager's authenticated identity, the decision, the edit diff between draft and final, and the reason code.
7. **Timestamps:** request, each step, eval completion, approval and release, from a synchronised clock.
8. **Final output:** the released text and its hash, and the distribution record.

**Validation and periodic review [AJ].**
- *Before go-live.* The independent validator reviews conceptual soundness: is an LLM appropriate when every number comes from the engine? Are the boundaries enforced by design? The validator then re-runs the L9 regression suite of 24 to 36 months of approved commentaries, adds its own challenge cases (sign flips, overweight and underweight swaps, currency-effect confusions, injected market notes from C7), and runs a second, vendor-independent red-team tool.
- *Approval conditions.* Version pinning; 100% numeric faithfulness; human approval on every commentary.
- *Quarterly review.* Monitoring trends, the human-intervention rate and edit types, incidents, provider change notices and a re-performance sample, followed by an attestation [VF: B-C8-S005].
- *Re-validation.* Any change to the version bundle triggers it. A new model version gets the full regression suite and the validator's challenge set before approval.

**This is LinkedIn pair 1 in practice [AJ].** The eval suite is the validation evidence: the same versioned datasets and checks that gate releases in L9 are what the validator re-performs and what the archive retains. The suite becomes validation evidence only under three conditions. Someone independent of the developers must challenge it and extend it. It must be versioned with the results it produced. And it must be retained beyond any vendor tier. A developer's test suite on its own is development testing, not validation.

**Reproducibility [AJ].** An LLM call may not reproduce the same text twice. For this use case, reproducibility therefore means **re-performance of the evidence**, not bit-identical regeneration:
- the original inputs are retained: the prompt, the data snapshot and the retrieved documents;
- the original output and every check result are retained;
- a re-run on the pinned model, while it remains available, passes the same thresholds;
- if the provider has retired the version, the firm can show the retained evidence and the re-qualification of the replacement against the same suite.

Pinning versions and keeping a fallback model qualified on the same suite is also the SS2/21 exit route [VF: R-PRA-SS221, A8-S048] [AJ].

**Retention [AJ].** The use case is not Annex III, so Article 26's six-month minimum does not apply directly [VF: R-EUAIA, A8-S016]. The records policy for client communications governs, and the evidence pack follows it. Where a firm also runs a high-risk use, the same archive meets the six-month floor.

**What C8 must never allow [AJ]:**
- a commentary released without a complete evidence pack and a recorded approver
- production calls to a model alias, or to a model version not named in the inventory entry
- a validation that covers a different model, prompt or index version from production
- evidence that exists only inside a vendor tool or on a time-limited tier
- a vendor's policy pack presented to the board as proof of compliance
- the developers acting as the only validators of their own eval suite

### C8.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| (absent) No governance control | SR 11-7 superseded by SR 26-2, which excludes GenAI and agentic AI [VF: R-US-MRM, A8-S001]; SS1/23 in force [VF: R-PRA-SS123, A8-S008]; AI Act GPAI enforceable 2 Aug 2026, Annex III 2 Dec 2027 [VF: R-EUAIA, A8-S011] | A firm GenAI model-risk standard to SS1/23 quality; use case as governed unit; firm-owned evidence store [Rec] |
| (absent) ValidMind | MRM platform with GenAI tests; only SS1/23 claimant; AGPL library [VF: A7-S003, A7-S052] | Tactical: MRM-led firms, after SOC 2 Type II evidence [Rec] |
| (absent) Credo AI | Policy-led registry and packs; EU SaaS and air-gapped self-host [VF: A7-S102, A7-S107, A7-S123] | Tactical: policy- and compliance-led programmes [Rec] |
| (absent) IBM watsonx.governance | Agent discovery and Enforcement Tracking (2026) [VF: A7-S111] | Tactical, conditional Strategic for IBM estates once certification scope is confirmed [Rec] |
| (absent) ModelOp | Lifecycle automation with blocking workflows; thin public evidence [VF: A7-S098; NPV] | Tactical, after full due diligence [Rec] |
| (absent) Collibra AI Governance | "Enterprise AI Control Plane"; trail ML acquisition announced 5 Oct 2026; OpenLineage integration [VF: A7-S122, A7-S101, V2-S044] | Tactical: where Collibra is the catalogue of record [Rec] |
| (absent) OpenLineage | Graduate LF AI & Data spec; no GenAI facets [VF: A7-S041, A7-S042] | Strategic lineage standard, with firm GenAI facets [Rec] |

**H8 (evaluation is cross-cutting). Provisional view; verdict in synthesis.** The C8 evidence supports H8 strongly.
- Governance products now consume evaluation evidence directly. watsonx.governance Enforcement Tracking retrieves agent evaluation metrics against thresholds [VF: A7-S111]. ValidMind's Library logs tests to the governance record and monitors against thresholds [VF: A7-S003, A7-S056]. IBM's SDK evaluates metrics and prompt templates [VF: A7-S058].
- The regulators' expectations converge on ongoing monitoring: Article 26 and Article 72 [VF: R-EUAIA, A8-S016, A8-S017], the PRA's AI roundtables [VF: R-PRA-SS123, A8-S009], ESMA's ex-post controls [VF: R-INTL-AI-ASSETMGMT, A8-S059] and IOSCO's indicators [VF: R-INTL-AI-ASSETMGMT, A8-S058].
- The counter-evidence is that independence is weakening at the tool level, with OpenAI's announced acquisition of Promptfoo [VF: A1-S024, V2-S042].

The provisional reading: evaluation (L9) and governance (C8) are one evidence plane with two owners. L9 produces the evidence; C8 sets thresholds, approves and retains [AJ]. **Provisional; verdict in synthesis.**

**H7 (lineage, classification and PII belong in ingestion). Provisional view; verdict in synthesis.** The evidence is mixed.
- *For.* OpenLineage is the neutral lineage standard, with Airflow, Spark, dbt and Flink coverage [VF: A7-S041, A7-S045]. Its tag facets can carry classification labels [VF: A7-S042]. Collibra links an AI use-case register to model versions and integrates OpenLineage, the first verified bridge between AI governance and data lineage [VF: A7-S099, A7-S122]. Its BCBS 239 control mapping ties AI governance to risk-data lineage [VF: A7-S099].
- *Against.* No GenAI-specific lineage facets exist [VF: A7-S042]. Run-time lineage for LLM calls lives in OTel traces (L9), not OpenLineage [AJ].

The provisional reading: lineage for GenAI has two halves, joined in the evidence pack by index version and document IDs. Build-time lineage is OpenLineage from L8 pipelines, with firm GenAI facets. Run-time lineage is OTel GenAI traces [AJ]. **Provisional; verdict in synthesis.**
