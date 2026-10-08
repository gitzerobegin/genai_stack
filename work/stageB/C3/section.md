## C3. DLP and PII protection

> **Executive summary.** This control finds, classifies and transforms sensitive data wherever it can enter or leave a GenAI system: at ingestion, in prompts, in tool results, in model outputs, in memory and in traces [AJ]. The original graphic has no such control; it shows ingestion, memory, retrieval and evaluation boxes that each copy data, and none of them says what happens to client identifiers [AJ]. Four things have changed in the candidate products. Presidio is no longer a Microsoft project: it is community-governed under the "Data Privacy Stack" organisation, MIT-licensed, and states that it is "not owned or operated by a commercial entity" [VF: A6-S040, V2-S030]. Microsoft folded "DSPM for AI" into a unified Purview Data Security Posture Management, generally available in May 2026, which needs Microsoft 365 E5 or the Purview Suite [VF: A6-S090, A6-S091, V2-S036]. Google's Sensitive Data Protection (formerly Cloud DLP) is positioned for GenAI prompts and responses and underpins Model Armor's sensitive-data screening [VF: A6-S066, A6-S067]. Protegrity's AI Team Edition is still documented as Tech Preview and deploys on AWS only, and Skyflow sells an "LLM Privacy Vault" with EU vaults, with no funding round verified after March 2024 [VF: A6-S093, A6-S095, A6-S096]. Meanwhile, DLP has started to appear inside gateways and guardrails: Cloudflare AI Gateway, Kong AI Gateway, Bedrock Guardrails and Model Armor all inspect prompts or responses for sensitive data [VF: A6-S052, A6-S016, A6-S072, A6-S067]. **Recommendation:** build one firm-owned privacy service (detect, transform and, under policy, re-identify) and call it from every enforcement point, rather than buying a different detector per layer. Use Presidio as the in-estate detection engine, with Google Sensitive Data Protection as the managed engine in a Google Cloud estate. Add a vault or tokenisation platform (Protegrity, Skyflow) only where reversible pseudonymisation at scale is required, and use Purview DSPM for posture over Microsoft 365 Copilot and SaaS AI apps in a Microsoft estate [Rec].

### C3.1 Responsibility

**The problem this control owns.** It ensures that personal data and confidential business data reach a model, a store or a third party only in the form that the firm's policy allows for that destination [AJ]. This breaks down into five jobs:

- **Classification.** Knowing which sources, documents and fields are sensitive, and how sensitive, before they are used [AJ]. Discovery and profiling across data stores is a product feature of Sensitive Data Protection and Purview DSPM [VF: A6-S066, A6-S091].
- **Detection.** Finding sensitive entities in free text, images and structured data at run time [AJ]. Presidio uses NER, regular expressions, rules and checksums with context [VF: A6-S068]. Sensitive Data Protection has more than 200 predefined detectors [VF: A6-S066].
- **Transformation.** Redacting, masking, generalising or tokenising the entity so that the downstream step still works [AJ]. Sensitive Data Protection offers masking, tokenisation and bucketing [VF: A6-S066]. Protegrity and Skyflow offer policy-based protect/unprotect and vault tokenisation [VF: A6-S082, A6-S081].
- **Controlled re-identification.** Reversing a token only for an entitled principal and a recorded purpose [AJ]. Skyflow detokenises under role-scoped credentials [VF: A6-S081], and Protegrity grants Unprotect per role and data element [VF: B-C3-S004].
- **Residency and evidence.** Keeping each copy of sensitive data in an approved location, and recording what was detected, transformed and re-identified [AJ].

**Where it sits in the flow.** C3 is not a box; it is a service called at six enforcement points [AJ]:

| Point | Layer | What C3 does there [AJ] |
|---|---|---|
| E1 Ingestion | L8 | Classify and detect before parsing, route by classification, and tag every chunk with classification and PII flags (the L8 metadata envelope) |
| E2 Prompt egress | C1 gateway | Detect and tokenise before any external model call; block what policy forbids |
| E3 Tool results | L4 | Transform tool outputs that carry client data before they enter the context window |
| E4 Model output | C1 / C2 | Detect sensitive data in responses (including leakage from retrieval or memory), re-identify placeholders only for entitled users |
| E5 Memory writes | L5 | Stop raw identifiers being written to long-term memory; keep memory erasable |
| E6 Telemetry | L9 | Redact at the firm-owned OTel Collector before traces leave the estate |

**Hand-offs.** C3 supplies classification policy and detectors to L8 [AJ]. It shares detectors and test sets with C2 guardrails, which own content safety and injection defence [AJ]. It relies on C4 for the identity and entitlement of whoever asks for re-identification, and on C7 (Vault or the firm's KMS) for the keys [AJ]. It passes detection and re-identification logs to C8 as evidence and to L9 as metrics [AJ].

**What the control does not own.** It does not decide who may read a source document; that is entitlement filtering in L6 and identity in C4 [AJ]. It does not decide whether a prompt is malicious; that is C2 [AJ].

### C3.2 Why it matters

GenAI multiplies copies of data [AJ]. One analyst question can place the same client identifier in a prompt, a retrieved chunk, a tool result, a model provider's processing region, a trace store, an evaluation dataset and a memory record [AJ]. Each copy has its own retention, location and access model, and each becomes a place an erasure request or a breach investigation must reach [AJ]. Badly designed, the control fails in four ways [AJ]:

- **Detection gaps.** Detectors miss domain identifiers (internal client codes, account numbers, mandate references) because they were tuned for generic PII. Presidio's own README warns that detection is not guaranteed to find all sensitive data [VF: A6-S068].
- **Single-point placement.** DLP sits only at the gateway, so ingestion, memory and traces carry raw data.
- **Irreversible damage to utility.** Blunt redaction removes the information the model needs ("[REDACTED] outperformed [REDACTED]"), so teams switch the control off.
- **Uncontrolled reversal.** Re-identification is done by whoever holds a key or token map, without a recorded purpose.

**Illustrative scenario [AJ].** A client-service team pilots an assistant that drafts replies to institutional clients. The gateway has a content-safety filter but no DLP. Analysts paste client letters that include the client's legal name, an account number and a named contact. The prompts go to a model API in a region outside the UK and EU, traces go to a SaaS observability tool on its default region, and the agent's memory stores "Client X prefers quarterly calls with Y". Six months later the named contact makes a subject access and erasure request. The firm can delete the CRM record, but it cannot list every trace, memory entry and evaluation case that holds the contact's name, and it cannot say under which transfer mechanism the prompts left the UK. Tokenising identifiers at the gateway and redacting at the collector would have kept the name out of four of the five stores. The scenario is invented; it is not a reported incident.

### C3.3 Goals and KPIs

| KPI | Definition | Target guidance [AJ] | How it is measured |
|---|---|---|---|
| Detection recall per entity class | Share of seeded sensitive entities found, by class (client name, account number, national ID, IBAN, contact details, internal client code) | ≥0.98 for identifiers that must never leave; per class, not averaged | Labelled test corpus in CI, re-run on every detector or model change |
| Detection precision | Share of detections that are true positives | Set per class; low precision drives users to bypass | Same test corpus plus sampled production review |
| Residual sensitive-data rate | Sensitive entities found by a second-pass scanner after transformation | Zero for "must mask" classes | Sampled chunks, prompts and traces scanned by an independent detector |
| Enforcement-point coverage | Share of model calls, ingestion jobs, memory writes and trace exports that pass through the privacy service | 100% for external egress | Gateway and collector logs reconciled to privacy-service logs |
| Untokenised egress | External model calls carrying a "must tokenise" identifier in clear | Zero; any event is an incident | Gateway post-call audit scan |
| Re-identification attribution | Detokenisation events with user, agent, purpose and policy decision recorded | 100% | Privacy-service audit log joined to C4 identity |
| Placeholder integrity | Outputs where a placeholder was altered, invented or dropped by the model | Zero accepted into final text | Deterministic check before re-identification |
| Added latency | p95 latency added by detection and transformation per call | Budget per use case, e.g. under 10% of model latency | Gateway spans |
| Erasure reach | Time and completeness to locate and erase a data subject across stores (memory, traces, eval sets, caches) | Within the statutory deadline, with evidence | Erasure runbook drills |
| Location conformance | Share of processing (model calls, DLP calls, traces) in approved regions | 100% for UK/EU personal data unless a transfer assessment exists | Configuration evidence and gateway routing logs |

### C3.4 How it works

**Mechanics.** Four steps run at each enforcement point, against one policy [AJ].

1. **Classify.** Labels come from the source (a sensitivity label, the approved-source register in L8) or from discovery jobs [AJ]. Sensitive Data Protection profiles BigQuery, Cloud SQL, Cloud Storage and Agent Platform data [VF: A6-S066]. Purview DSPM assesses AI interactions, prompts and responses for Microsoft 365 Copilot, Entra-registered AI apps and ChatGPT Enterprise [VF: A6-S091].
2. **Detect.** Pattern, checksum and context rules find structured identifiers; NER or LLM-based recognisers find names and free-text entities [AJ]. Presidio supports spaCy, Stanza or Hugging Face NER models and has added LLM-based recognisers (LangExtract) [VF: A6-S005, A6-S040, A6-S041]. Firm-specific identifiers need custom recognisers in every engine [AJ].
3. **Transform.** The method depends on whether the model needs the value and whether anyone must reverse it [AJ]:

| Method | Reversible? | Use for [AJ] | Product support |
|---|---|---|---|
| Redact (remove) | No | Values the model never needs (national ID, bank details) | All five products [VF: A6-S068, A6-S066, A6-S082, A6-S081] |
| Mask (partial) | No | Values a human may need to recognise, not the model | SDP masking [VF: A6-S066]; Protegrity masking [VF: A6-S082] |
| Generalise (bucket) | No | Values whose range matters (age band, AUM band) | SDP bucketing [VF: A6-S066] |
| Consistent placeholder or token | Yes, with a key or map | Identities the model must keep distinct ("CLIENT_A" vs "CLIENT_B") and a reviewer must see restored | SDP tokenisation with KMS-wrapped keys [VF: A6-S066, B-C3-S002]; Protegrity protect/unprotect [VF: A6-S082]; Skyflow vault tokens with authorised rehydration [VF: A6-S081, A6-S095] |

4. **Re-identify under policy.** After the model returns, placeholders are checked (none altered, none invented) and restored only for a principal entitled to see them, with the decision logged [AJ].

```text
                    ┌──────────────── Privacy service (firm-owned API) ────────────────┐
                    │ policy (classes → action per destination) · detectors · token keys │
                    │ (KMS/HSM, C7) · audit log (C8) · metrics (L9)                       │
                    └───▲──────────▲───────────▲───────────▲───────────▲──────────▲───────┘
                        │E1        │E2         │E3         │E4         │E5        │E6
  sources ─► L8 ingest ─┘   prompt ─┘  L4 tool ─┘  model   ─┘  L5 memory ─┘  OTel   ─┘
             classify,      at C1      results     output       writes        Collector
             tag chunks     gateway    in context  check +      (no raw IDs)  redaction
                            tokenise               re-identify                 (L9)
                                │
                                ▼
                     external model (L1/L2): sees CLIENT_A, ACCT_7, never the values
```

**Engine options behind the service.** An in-estate library (Presidio) keeps text inside the firm's boundary [VF: A6-S068]. A managed DLP API (Sensitive Data Protection) sends text to the cloud provider's service and is billed per GiB inspected [VF: A6-S065]. A vault (Skyflow) stores the sensitive values with the vendor and returns tokens [VF: A6-S081]. These are three different trust models, and the choice is a residency decision before it is a feature decision [AJ].

**The LLM-specific twist.** Traditional DLP blocks or masks. GenAI needs transformations that keep the text useful to a model and reversible for the reviewer, and it needs a second inspection of the output, because the model can reproduce sensitive data from retrieval, memory or its own training [AJ].

### C3.5 Enterprise design principles

**Security**

- Run detection for "must not leave" classes inside the estate, before any external call, and fail closed on external egress if the privacy service is unavailable [Rec].
- Keep token keys and maps in the firm's KMS, HSM or Vault (C7), not only in a vendor's service [Rec]. Sensitive Data Protection allows the de-identification key to be wrapped by a Cloud KMS key held globally or in the request region [VF: B-C3-S002].
- Treat re-identification as a privileged action with its own entitlement, checked through C4 and logged [Rec].
- Cover confidential business data, not only personal data. In an asset manager the most sensitive content is often holdings, client mandate terms and unpublished performance, none of which a PII detector looks for [AJ].
- Treat tokenised data as personal data in the records of processing and transfer assessments, because the firm can reverse it [AJ].

**Scalability and resilience**

- Detection adds latency on every call. Measure it per enforcement point and run pattern detectors before NER or LLM recognisers [AJ].
- Managed DLP is priced per volume: content inspection costs US$3.00 per GiB after the first free GiB, falling to US$2.00 above 1 TiB, as of 7 October 2026 [VF: A6-S065]. Model this against prompt and trace volumes [Rec].
- Self-hosted detection is horizontally scalable as stateless services, while a vault is a stateful dependency on the critical path [AJ].

**Governance**

- Write the policy once (entity classes, action per destination, re-identification rights) and enforce it at all six points [Rec].
- Version detectors and recognisers like models: test sets, recall per class, and release gates in CI [Rec].
- Log detections as types, counts and positions, never the values [AJ].
- Map every store that may hold personal data (prompts, traces, memory, eval sets, caches) into the erasure runbook [Rec].

**Observability and cost**

- Publish detection counts by class and enforcement point to L9; a sudden fall in detections is as suspicious as a rise [AJ].
- Purview DSPM requires Microsoft 365 E5 or the Purview Suite; the Business Premium add-on's coverage is reported inconsistently, so confirm licensing before relying on it [VF: A6-S091] [R: A6-S092].

**Portability**

- Put a thin, firm-owned API in front of the engines (detect, transform, re-identify) so that engines can be swapped or combined [Rec].
- Prefer reversible methods whose keys the firm holds; a vendor-held token map makes the vendor part of every future read of that data [AJ].

**Patterns [AJ]:** privacy service with a firm-owned API; consistent placeholders per conversation so the model can reason about distinct entities; double inspection (prompt and output); collector-side redaction for traces; classification carried in the chunk metadata envelope from L8; second-detector sampling to measure residual leakage.

**Anti-patterns [AJ]:** DLP only at the gateway; redacting everything so the output is useless; a different detector and policy per product; re-identification keys held by application teams; raw identifiers in eval datasets "because it is internal"; relying on a model provider's zero-retention promise instead of not sending the data.

### C3.6 Product selection criteria

| Scorecard criterion | What to evaluate in this control [AJ] |
|---|---|
| Technical (15% FS) | Detection quality for firm-specific and UK/EU identifiers; custom recognisers; modalities (text, images, structured); transformation range (redact, mask, bucket, token); reversible tokenisation; discovery and classification of stores; output inspection |
| Enterprise readiness (15%) | SSO, RBAC over policies and over re-identification, audit of every protect and unprotect, admin APIs; which of these are licence-gated |
| Security and compliance (20%) | SOC 2 Type II and ISO 27001 in the product's scope; customer-held keys; regional processing; because these products see the most sensitive data in the estate, 5 needs customer-managed keys or equivalent |
| Deployment flexibility (15%) | In-estate or self-hosted option for "must not leave" data; region choice for managed services |
| Ecosystem (5%) | Integration with gateways, guardrails, ingestion and the OTel Collector; APIs and SDKs |
| Reliability and maturity (10%) | GA status, release cadence, governance or funding stability |
| Cost / TCO (5%) | Per-GiB or per-record pricing at prompt and trace volumes; licence prerequisites (E5); operating cost of self-hosting |
| Lock-in / portability (15%) | Who holds the token map and keys; whether tokenised data can be detokenised in bulk on exit; proprietary labels |

### C3.7 Product deep dives

**Presidio (Data Privacy Stack; formerly Microsoft).**
- *What it is now:* an open-source PII detection and de-identification SDK for text, images (including DICOM) and structured data, with separate analyzer, anonymizer, image-redactor and structured modules [VF: A6-S068]. Versions 2.2.364 of presidio-analyzer and presidio-anonymizer were released on 22 July 2026 under MIT [VF: A6-S005, V2-S028].
- *Ownership:* the project moved from Microsoft to community governance under the Data Privacy Stack organisation with a Technical Steering Committee. It is maintained by contributors and volunteers and is not owned by a commercial entity. The rebrand landed in 2.2.363 (28 June 2026) and container images moved from MCR to GHCR [VF: A6-S040, A6-S041, V2-S030].
- *Project hygiene:* a published security policy uses GitHub private vulnerability reporting, with acknowledgement within 48 hours and coordinated advisories [VF: B-C3-S001]. Signed releases are not verified [NPV].
- *Strengths:* runs entirely in-estate, with a permissive licence and neutral governance; recognisers are code the firm can own and test [AJ].
- *Limitations:* the README warns that detection is not guaranteed to find all sensitive data [VF: A6-S068]. There is no commercial support, no built-in authentication on its REST services is documented, and there is no vault or discovery capability [NPV] [AJ]. The volunteer governance is new [VF: A6-S040].
- *Choose when:* you need in-estate detection behind your own privacy service, with custom recognisers for firm identifiers [AJ].
- *Avoid when:* you need a supported product with a contractual SLA, or a tokenisation vault [AJ].
- *Competitors:* Google Sensitive Data Protection, Bedrock Guardrails PII filters, Protegrity Data Discovery.
- *FS note:* pin versions, replace the default image references after the GHCR move, and measure recall per entity class in CI before every upgrade [Rec].
- **Tier: Strategic, conditional: as the in-estate engine behind a firm-owned privacy service, with recall testing and a second detector for sampling, because enterprise readiness is limited to what the firm builds around it [AJ]. Flag: Renamed** (ownership moved from Microsoft to community governance).

**Google Sensitive Data Protection (Google Cloud).**
- *What it is now:* the managed discovery, classification and de-identification service that includes the former Cloud DLP API [VF: A6-S066]. It profiles BigQuery, Cloud SQL, Cloud Storage and Agent Platform data, inspects content with more than 200 predefined detectors, and de-identifies by masking, tokenisation and bucketing; hybrid jobs reach external sources [VF: A6-S066, A6-S065].
- *GenAI position:* Google positions it to de-identify training and tuning data and to protect prompts and responses at run time, and it underpins Model Armor's sensitive-data screening [VF: A6-S066, A6-S067].
- *Certifications and keys:* it is listed in Google Cloud's SOC 2 and ISO/IEC 27001 scope [VF: A6-S070, A6-S071]. Tokenisation keys can be wrapped by a Cloud KMS key stored globally or in the region used for requests [VF: B-C3-S002]. The list of supported EU locations was not retrieved [NPV].
- *Pricing:* the first 1 GiB of content inspection per month is free, then US$3.00 per GiB to 1 TiB and US$2.00 per GiB above; discovery is consumption-based or US$2,500 per subscription unit per month, as of 7 October 2026 [VF: A6-S065].
- *Strengths:* the broadest managed detection and transformation set in this control, with product-scoped certifications [AJ].
- *Limitations:* there is no self-hosted option [VF: A6-S066]. The API is Google Cloud-specific [VF: A6-S066]. Text must be sent to the service for inspection [AJ].
- *Choose when:* Google Cloud is your data platform, or you use Model Armor and Apigee [AJ].
- *Avoid when:* policy forbids sending raw client text to a cloud service before it is tokenised [AJ].
- *Competitors:* Presidio, Purview DSPM, Bedrock Guardrails PII filters.
- *FS note:* pin processing and key location to an EU or UK-approved region and confirm it against the locations page; platform controls presumed (CP2 Q1); confirm per service [Rec].
- **Tier: Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2, rubric rule 10), because deployment flexibility and lock-in score 2 [AJ]. No flag.**

**Microsoft Purview Data Security Posture Management (formerly DSPM for AI).**
- *What it is now:* the unified Purview DSPM, generally available in May 2026, which absorbed the earlier DSPM for AI experience; the classic experiences remained until June 2026. Partner (non-Microsoft) data sources and the Data Security Posture Agent are still in preview [VF: A6-S090, V2-S036].
- *Coverage:* it discovers and assesses data-security risk in AI use, including interactions, prompts and responses for Microsoft 365 Copilot, Entra-registered AI apps and ChatGPT Enterprise; prompt and response coverage needs E5. Purview also covers Microsoft Foundry workloads [VF: A6-S091]. In US Government GCC, only Microsoft 365 Copilot and supported AI sites are available [VF: A6-S091].
- *Certifications:* the Microsoft Purview portal is in Microsoft's ISO/IEC 27001 scope for commercial and government clouds, and Purview is in Azure FedRAMP High scope; DSPM is not named separately [VF: B-C4-S008, A6-S056].
- *Licensing:* it requires Microsoft 365 E5 or the Purview Suite; community answers claim the Business Premium add-on also covers DSPM for AI, which an official licensing matrix does not confirm [VF: A6-S091] [R: A6-S092].
- *Strengths:* posture and visibility for the AI apps employees already use, inside the Microsoft compliance estate [AJ].
- *Limitations:* it is a posture and governance tool, not an inline tokenisation engine for custom applications; its feature list beyond AI coverage is not verified [NPV]. It runs as a Microsoft cloud service [VF: A6-S056]; no other deployment model is verified [NPV].
- *Choose when:* Microsoft 365 Copilot or ChatGPT Enterprise is in use and the firm already licenses E5 or the Purview Suite [AJ].
- *Avoid when:* you need run-time masking in a custom agent's prompt path [AJ].
- *Competitors:* Google Sensitive Data Protection (discovery), Protegrity Data Discovery, Skyflow.
- *FS note:* use it for shadow-AI and Copilot posture evidence; do not count it as the prompt-path DLP control for custom agents; platform controls presumed (CP2 Q1); confirm per service [Rec].
- **Tier: Strategic, conditional: where Azure and Microsoft 365 are your primary cloud and E5 or the Purview Suite is already licensed (CP3 Q2, rubric rule 10) [AJ]. Flag: Renamed** (DSPM for AI folded into unified DSPM). It is Microsoft's lead AI data-security posture service. The condition limits it to posture and Copilot evidence: it is not the prompt-path DLP control for custom agents, which stays with Presidio or Sensitive Data Protection. Deployment, cost and lock-in at 2 are accepted under rule 11 because the condition is an existing platform commitment [AJ].

**Protegrity.**
- *What it is now:* an enterprise data-protection platform for discovery, tokenisation and masking, with semantic guardrails for GenAI [VF: A6-S082]. Data Discovery classifies PII in unstructured text; Find and Redact, Protect and Unprotect apply Protegrity protection policies; a Semantic Guardrail API scans conversations for PII and risk [VF: A6-S082].
- *Editions:* AI Team Edition launched on 17 November 2025 for agentic workflows, but its documentation still says Tech Preview and deployment is AWS-specific; an April 2026 release says "available now" [VF: A6-S093]. The AI Developer Edition Python module is MIT-licensed; protegrity-developer-python 1.1.1 was released on 16 December 2025 [VF: A6-S082].
- *Access control and audit (core platform):* the Enterprise Security Administrator manages policies centrally. Permissions (Protect, Unprotect, Reprotect) are set per role and data element; a role without a data element cannot use it; administrative roles include Security Administrator, Security Officer and a read-only viewer; audit logs capture authorised and unauthorised access attempts at all protection points and all policy changes [VF: B-C3-S004]. These ESA facts do not automatically apply to AI Team Edition [VF: B-C3-S004]. SSO is not verified [NPV].
- *Certifications:* ISO 27001:2013 certification for its ISMS was announced in August 2023; current renewal is not verified, and no Protegrity SOC 2 report was found [VF: A6-S094, B-C3-S003].
- *Strengths:* role-per-data-element unprotect rights and audit at every protection point are what reversible tokenisation in a regulated firm needs [AJ].
- *Limitations:* the AI editions are not clearly GA [VF: A6-S093]. Pricing is not published [NPV]. Tokenised data depends on Protegrity policies to reverse [AJ].
- *Choose when:* Protegrity already tokenises your structured data and you want the same tokens and policies in the AI path [AJ].
- *Avoid when:* you are not on AWS for the AI editions, or need a current SOC 2 Type II report as a gate [AJ].
- *Competitors:* Skyflow, Google Sensitive Data Protection, Presidio.
- *FS note:* request the current ISO certificate and any SOC 2 report, and treat AI Team Edition as a pilot until it is GA [Rec].
- **Tier: Tactical** (core platform for existing customers; AI Team Edition Experimental until GA) [AJ]. **No flag.**

**Skyflow.**
- *What it is now:* a data privacy vault. It stores sensitive data and returns tokens, detokenises under role-scoped credentials, and its Detect APIs de-identify text and files [VF: A6-S081]. Its LLM Privacy Vault tokenises or masks data before it reaches models, prompts, RAG, tools, traces and agent workflows, with authorised rehydration [VF: A6-S095].
- *Residency:* EU data privacy vaults are offered, and vault infrastructure is described as available in more than 100 countries [VF: A6-S095].
- *Certifications:* the security page lists ISO 27001:2022, SOC 2 Type II and PCI DSS Level 1; the reports themselves are not public [VF: B-C3-S005, A6-S095].
- *Version and company:* Python SDK 2.1.3 was released on 4 August 2026, and SDK v1 reaches end of life on 31 October 2026 [VF: A6-S081]. The latest verified funding is a US$30m Series B extension on 28 March 2024; no later round or acquisition was found [VF: A6-S096, A6-S095].
- *Strengths:* the only product here built around reversible tokenisation of LLM traffic with residency by vault region [AJ].
- *Limitations:* the vendor holds the sensitive values, so it is on the critical path of every re-identification [AJ]. Self-hosting is not verified [NPV]. SSO and audit logs are not verified [NPV]. Pricing is not published [NPV].
- *Choose when:* you need reversible pseudonymisation across many applications with per-region vaults, and accept a specialist vendor as a data processor [AJ].
- *Avoid when:* policy requires identifiers to stay in the firm's own estate [AJ].
- *Competitors:* Protegrity, Google Sensitive Data Protection, a firm-built token service.
- *FS note:* migrate off SDK v1 before 31 October 2026, test bulk detokenisation as part of the exit plan, and assess the vendor's financial resilience as a material outsourcing [Rec].
- **Tier: Tactical. No flag.**

### C3.8 Comparison table

Output of `tools/score.py` (FS weights favour security, deployment and lock-in):

| Product | Tech | Ent | Sec | Deploy | Eco | Mature | Cost | Lock-in | Generic | FS | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C3-presidio | 3 | 3 | 3 | 5 | 3 | 3 | 4 | 5 | 3.50 | 3.65 | Strategic |
| C3-google-sdp | 5 | 4 | 4 | 2 | 4 | 5 | 3 | 2 | 3.80 | 3.60 | Strategic |
| C3-microsoft-purview-dspm-ai | 3 | 4 | 4 | 2 | 4 | 3 | 2 | 2 | 3.10 | 3.05 | Strategic |
| C3-protegrity | 4 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2.90 | 2.75 | Tactical |
| C3-skyflow | 4 | 3 | 4 | 2 | 3 | 3 | 2 | 2 | 3.05 | 3.00 | Tactical |

**Scoring notes [AJ]:**
- *Hyperscaler presumption (CP2 Q1).* Sensitive Data Protection and Purview DSPM score 4 on enterprise readiness, with the note "platform controls presumed (CP2 Q1); confirm per service".
- *Certification scope (CP2 Q4).* Sensitive Data Protection's SOC 2 and ISO 27001 are product-scoped, but customer-managed keys for its stored profiles and EU locations are not verified, so it scores 4, not 5. Purview DSPM scores 4: the Purview portal is in ISO 27001 scope and Purview in FedRAMP High scope, but DSPM is not named and commercial SOC 2 scope does not name the portal.
- *Partial evidence (CP2 Q2).* Protegrity's enterprise readiness is 3 on verified RBAC and audit (ESA), with SSO not verified. Skyflow's is 3 on role-scoped credentials only.
- *Security below 3.* Protegrity scores 2: its only verified certification is ISO 27001:2013 announced in 2023 with renewal unverified, and no SOC 2 report was found. This is an anchor-based score, not an NPV cap.
- *Self-hosted library (rule 2).* Presidio is scored on project hygiene and on what it enables in-estate; both criteria are capped at 4.
- *Ownership.* Presidio's move to community governance does not reduce lock-in, because it is MIT with neutral governance (rule 3 exemption).
- *Calibration.* Every product scores 2 or below on at least one criterion. Presidio, Sensitive Data Protection and Purview DSPM are Strategic only on stated conditions.
- *Hyperscaler lead services (CP3 Q2, rubric rule 10).* Purview DSPM moves from Tactical to Strategic, conditional: where Azure and Microsoft 365 are your primary cloud, as Microsoft's lead service for AI data-security posture with no criterion at 1. Its FS total (3.05) is unchanged and is among the lowest Strategic totals in C1–C8 (AgentCore Gateway in C1 is 3.00); the condition, posture evidence only, carries that weakness. Sensitive Data Protection's condition is reworded to "where Google Cloud is your primary cloud". Security stays at 4 for both under rule 8.

**Key facts.**

| Product | Licence | Deployment | Certifications (as of 8 October 2026) | EU residency | Ownership status |
|---|---|---|---|---|---|
| Presidio | MIT [VF: A6-S005] | Self-hosted library or Docker services [VF: A6-S068] | Not applicable (library); security policy [VF: B-C3-S001] | In-estate [VF: A6-S068] | Community (Data Privacy Stack), formerly Microsoft [VF: A6-S040] |
| Google SDP | Proprietary service; clients Apache-2.0 [VF: A6-S066, A6-S083] | SaaS (Google Cloud); no self-host [VF: A6-S066] | SOC 2, ISO 27001 in scope [VF: A6-S070, A6-S071] | Regional processing possible; EU list not verified [VF: B-C3-S002] [NPV] | Google Cloud [VF: A6-S066] |
| Purview DSPM | Proprietary SaaS; E5 or Purview Suite [VF: A6-S091] | SaaS [VF: A6-S056] | Purview portal ISO 27001; Purview FedRAMP High [VF: B-C4-S008, A6-S056] | Not publicly verified [NPV] | Microsoft [VF: A6-S056] |
| Protegrity | Proprietary; AI Developer Edition module MIT [VF: A6-S082] | Containerised self-host; AI Team Edition AWS-only [VF: A6-S082, A6-S093] | ISO 27001:2013 (2023); no SOC 2 found [VF: A6-S094, B-C3-S003] | Not publicly verified [NPV] | Independent; no 2025–26 deal found [VF: A6-S093] |
| Skyflow | Proprietary SaaS [VF: A6-S081] | Hosted vaults [VF: A6-S081] | ISO 27001:2022, SOC 2 Type II, PCI DSS L1 listed [VF: B-C3-S005] | EU vaults [VF: A6-S095] | Independent; last funding March 2024 [VF: A6-S096] |

### C3.9 Decision tree

```text
STEP 0 [Rec] (not optional): one firm-owned privacy-service API (detect / transform /
re-identify), one policy (entity classes → action per destination), keys in the firm's
KMS/HSM or Vault (C7), called at E1 ingestion, E2 prompt, E3 tool results, E4 output,
E5 memory writes, E6 trace export.

STEP 1 [Rec]: Detection engine behind the API
  May raw client text leave the estate for inspection?
  ├─ No  → Presidio in-estate + firm recognisers (client codes, account numbers);
  │        second detector on samples for residual-leakage KPI
  └─ Yes → Is Google Cloud the data platform?
           ├─ Yes → Sensitive Data Protection (pinned region, KMS-wrapped keys);
           │        Presidio as the in-estate pre-filter for "must not leave" classes
           └─ No  → Presidio; or the cloud guardrail's PII filter where already in the
                    gateway path (e.g. Bedrock Guardrails on AWS), behind the same API

STEP 2 [Rec]: Transformation
  Does anyone need the original value back after the model call?
  ├─ No  → redact / mask / bucket in the privacy service
  └─ Yes → Volume and number of applications?
           ├─ One or few apps   → consistent per-conversation placeholders; map held
           │                      in the firm's store, keys in KMS; deterministic check
           │                      before re-identification
           ├─ Already a Protegrity customer → Protegrity policies and tokens (core
           │                      platform; AI Team Edition only after GA)
           └─ Many apps, per-region vaults acceptable as a processor → Skyflow (EU vault)

STEP 3 [Rec]: Posture over SaaS AI (Copilot, ChatGPT Enterprise)
  Microsoft 365 E5 / Purview Suite already licensed? → Purview DSPM
  Otherwise → CASB/SSE tooling (outside this control's scope) plus usage policy

STEP 4 [Rec]: Checks before go-live
  Recall per class ≥ target on the firm's test set?  Output inspection on?
  Collector redaction on?  Erasure runbook covers memory, traces, eval sets, caches?
```

### C3.10 Lock-in classification

| Element | Classification [AJ] | Rationale | Abstraction to use [Rec] |
|---|---|---|---|
| Detection engine | **Acceptable** | Detectors are replaceable if the test set and recognisers are the firm's | Privacy-service API; recognisers and test corpus in Git |
| Policy (classes and actions) | **Manageable** | Every product has its own policy model (Protegrity data elements [VF: B-C3-S004], Purview labels) | Firm-owned policy as code, compiled into engine configuration |
| Token map and keys held by a vendor | **Unacceptable unless bulk detokenisation on exit is contractually and technically tested** | A vendor-held map makes the vendor part of every future read of the data [AJ]; Skyflow detokenises under its own credentials [VF: A6-S081] | Keys in the firm's KMS/HSM; contractual exit with tested bulk export |
| Managed DLP API | **Manageable** | Proprietary API [VF: A6-S066]; outputs are portable text | Same API; per-region configuration |
| Posture tooling (Purview) | **Acceptable** | Governance view, not in the data path [AJ] | None needed beyond exportable reports |

### C3.11 Regulated FS lens (POV 2)

**Data protection and transfers.**
- *UK regime.* UK GDPR as amended by the Data (Use and Access) Act 2025 applies; the ICO states all DUAA data protection provisions were in force as of 19 June 2026, including changes to the third-country transfer test (s.85) and automated decision-making (s.80) [VF: R-DATA-TRANSFERS, A8-S051, V2-S076].
- *EU–UK.* The EU renewed its UK adequacy decisions on 19 December 2025, valid until 27 December 2031 [VF: R-DATA-TRANSFERS, A8-S052, V2-S055].
- *EU–US.* The Data Privacy Framework remains in effect, but the appeal C-703/25 P against the General Court's judgment is pending as of 7 October 2026 [VF: R-DATA-TRANSFERS, A8-S053, A8-S054, V2-S059]. Tokenising identifiers before a US-hosted model call reduces the personal data exposed to that transfer risk [AJ].
- *Processing location as a priced control.* At least one first-party LLM API (Anthropic's Claude API) offers a US-only inference option at 1.1 times the price for Claude 4.6 and later, with workspace geography currently US only [VF: R-DATA-TRANSFERS, A8-S036]. The author is an Anthropic model; this is cited only as evidence that processing location is now a contract and configuration item, and other providers' equivalents are assessed in L1 and L2 [AJ].
- *Residency of prompts and logs.* Prompts, traces and memory are personal-data stores in their own right [AJ]. Residency must be configured for each: the model endpoint (L2/C1), the trace store (L9), the memory store (L5) and the DLP service itself [Rec].

**EU AI Act.**
- Article 26 requires deployers of high-risk systems to keep logs for at least six months and monitor operation; Annex III duties apply from 2 December 2027 [VF: R-EUAIA, R-EU-OMNIBUS-AI, A8-S011]. Long retention of logs that contain personal data conflicts with minimisation unless the logs are tokenised [AJ]. Tokenised traces with a controlled re-identification path satisfy both [Rec].

**Supervisory expectations.**
- ESMA expects "ex-ante input controls and frequent ex-post output controls" [VF: R-INTL-AI-ASSETMGMT, A8-S059]. Prompt-side tokenisation is the input control; output inspection is the output control [AJ].
- FG16/5 expects data location, effective access and exit planning for outsourced IT [VF: R-FCA-SYSC8, A8-S049]. A vault vendor holding client identifiers is an outsourcing with data-location and exit implications [AJ].

**Operational resilience and concentration.**
- DORA's CTPP list and the UK CTP designations cover hyperscalers and no AI model provider [VF: R-DORA, A8-S021; R-UK-CTP, A8-S023]. A managed DLP service from the same hyperscaler as the model and the data platform adds to that concentration [AJ].
- PRA PS7/26 and FCA PS26/2 require material third-party notifications from 18 March 2027 [VF: R-PRA-SS221, R-FCA-SYSC8, A8-S062]. A specialist vault on the critical path of client-data access is a candidate for material classification [AJ].
- SS2/21 expects documented and tested exit plans [VF: R-PRA-SS221, A8-S048]. For a vault, the exit test is bulk detokenisation [AJ].

**Model risk.** PRA SS1/23 applies to banks, building societies and PRA-designated investment firms with internal-model approval, and is technology-agnostic [VF: R-PRA-SS123, A8-S008]; SR 26-2 places generative and agentic AI outside its scope [VF: R-US-MRM, A8-S001]. SS1/23 and the EU AI Act are therefore the operative anchors [AJ]. NER and LLM-based detectors are models whose recall drifts with data, so they should be inventoried and tested as such [AJ].

**Standards.** The OWASP 2025 list identified Sensitive Information Disclosure as LLM02, kept here for traceability [R: A8-S040]; the 2026 Top 10 for LLM Applications, released August–September 2026, is the operative list [VF: R-OWASP-LLM, V2-S056]. NIST AI 600-1 and ISO/IEC 42001 provide neutral risk and management-system frameworks [VF: R-NIST-AIRMF, A8-S044; R-ISO-42001, A8-S045].

### C3.12 Worked-example slice (POV 3)

**What the commentary agent needs from C3 [AJ].** The agent drafts the monthly Brinson-style attribution commentary for a generic multi-asset fund. Most of its inputs are fund-level numbers, which are confidential but not personal data. Client identifiers appear when a commentary is produced for a segregated mandate, and personal data appears in the approval record. It needs six things:
1. **Tokenise before any model call.** Client names, mandate references, account numbers and named client contacts are replaced with consistent placeholders (CLIENT_A, MANDATE_1) at the gateway, so the model can write "the mandate's currency overlay" without seeing who the client is. Fund-level attribution figures are not tokenised; they are confidential data whose protection is the model endpoint's residency and contract.
2. **Detect again in the output.** The draft is inspected before re-identification. Any clear-text identifier that was not in the approved inputs blocks the draft. Placeholders must match the input set exactly: none invented, none altered.
3. **Re-identify only for the reviewer.** Placeholders are restored in the reviewer's view, under the reviewing PM's entitlement checked through C4, and the re-identification is logged.
4. **Clean retrieval and memory.** Prior commentaries indexed by L8 carry classification flags; segregated-mandate commentaries are retrievable only for the same mandate. Long-term memory of the PM's edits stores style preferences, never client identifiers.
5. **Redacted traces and evidence.** The OTel Collector redacts before export; the C8 evidence pack stores the tokenised prompt and the token-map reference, so the run is reproducible without copying clear identifiers into the archive.
6. **Location evidence.** Configuration evidence that the model endpoint, trace store and DLP calls ran in approved regions.

**What C3 must never allow [AJ]:**
- an untokenised client name or account number in a prompt to an external model
- a model-invented or altered placeholder being "re-identified" into the final text
- re-identification by the agent itself, or by anyone without the entitlement
- raw identifiers in traces, memory or the regression dataset
- the privacy service failing open on an external call

### C3.13 Original → current → recommended

| Original (graphic) | Current (October 2026) | Recommended |
|---|---|---|
| Absent from the graphic; ingestion (L8), memory (L5), vector stores (L6) and evals (L9) each copy data with no stated protection | DLP appears piecemeal inside gateways and guardrails (Cloudflare, Kong, Bedrock Guardrails, Model Armor) [VF: A6-S052, A6-S016, A6-S072, A6-S067] | A cross-cutting privacy service with one policy, called at six enforcement points [Rec] |
| "Microsoft Presidio" (plan candidate) | Community-governed Presidio under Data Privacy Stack, MIT [VF: A6-S040, V2-S030] | Strategic, conditional: in-estate detection engine [Rec] |
| Google Sensitive Data Protection (candidate) | Managed DLP positioned for GenAI; underpins Model Armor [VF: A6-S066, A6-S067] | Strategic, conditional: where Google Cloud is your primary cloud (CP3 Q2) [Rec] |
| Microsoft Purview (candidate) | DSPM for AI folded into unified DSPM, GA May 2026; E5 or Purview Suite [VF: A6-S090, A6-S091] | Strategic, conditional: where Azure and Microsoft 365 are your primary cloud (CP3 Q2); AI posture, not prompt-path DLP [Rec] |
| Protegrity (candidate) | AI Team Edition Tech Preview, AWS-only; ESA RBAC and audit [VF: A6-S093, B-C3-S004] | Tactical for existing customers [Rec] |
| Skyflow (candidate) | LLM Privacy Vault with EU vaults; funding last verified 2024 [VF: A6-S095, A6-S096] | Tactical: reversible tokenisation where a vendor vault is acceptable [Rec] |

**H7 (ingestion must include lineage, classification, PII/DLP, access-control metadata and incremental indexing). Provisional view; verdict in synthesis.**

The C3 evidence supports H7 on the DLP and classification elements, with a refinement on ownership [AJ].

- **Supporting.** None of the L8 products provides a full classification and PII step; only partial features exist (Firecrawl PII redaction, Unstructured ACL capture) [VF: A1-S076, A1-S094]. The C3 products all apply at ingestion as well as at run time: Sensitive Data Protection profiles stores and de-identifies training data, Presidio is designed for pipelines, and Skyflow de-identifies before ingestion [VF: A6-S066, A6-S068, A6-S081]. Once a document is parsed by a third party and indexed without classification, no downstream control can undo it [AJ].
- **Refinement.** Ingestion is only one of six enforcement points. Prompts, tool results, outputs, memory and traces need the same policy [AJ]. The products' own positioning spans these points: Skyflow names prompts, RAG, tools, traces and agent workflows [VF: A6-S095], and Google names prompts and responses at run time [VF: A6-S066].
- **Counter-evidence.** DLP is being absorbed into gateways and guardrails [VF: A6-S052, A6-S016, A6-S072, A6-S067], which could argue for placing it in C1 or C2 rather than in ingestion [AJ].

**Provisional recommendation.** Keep H7, read as "ingestion must call C3 and carry its classification in the chunk metadata envelope". The policy and engines belong in C3 as a cross-cutting service; L8 owns the call and the metadata; C1, L5 and L9 call the same service [AJ]. **Provisional; verdict in synthesis.**
