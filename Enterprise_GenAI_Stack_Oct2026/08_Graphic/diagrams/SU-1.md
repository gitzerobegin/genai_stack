# Start-up architecture: one thin control plane, built in the first fortnight
Caption: A small team runs one product on one cloud account and one Postgres database. Every model call passes through a pinned gateway that holds the routes, per-tenant budgets and model pins. The model writes only inside deterministic workflow code, and the code checks every output before a person sees it. Traces and evaluations leave from day one through OpenTelemetry. The dashed box holds what the first enterprise customer will ask for, which is added then and not before.

```mermaid
flowchart TD
  classDef later fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:5 4;
  classDef own fill:#EEF3F8,stroke:#2E6DA4,stroke-width:2px;
  U["Customer users<br/>each customer organisation is one tenant"]
  subgraph APP["The product: one codebase, one cloud account"]
    direction TB
    AUTH["C4 sign-in and tenant context<br/>hosted customer identity, MFA"]:::own
    WF["L3 workflow code<br/>deterministic steps first,<br/>one bounded model step per task"]:::own
    TOOLS["L4 connectors to customers' systems<br/>read-only, per-tenant delegated OAuth,<br/>tokens in own secrets store (C7)"]
    PG[("L6 Postgres + pgvector<br/>app data, vectors, evidence log (C8),<br/>tenant_id on every row")]
    CHK["C2 deterministic checks<br/>figures match source data,<br/>placeholders intact, denied topics"]:::own
  end
  subgraph GW["C1 gateway: open-source proxy, version-pinned"]
    KEYS["Routes and model pins from Git (C5)<br/>per-tenant keys and budgets (C6)<br/>redaction before export (C3)"]
  end
  subgraph MOD["L1 / L2 models: first-party APIs or the credit-giving cloud"]
    direction TB
    M1["Mid tier<br/>primary vendor"]
    M2["Mid tier<br/>qualified fallback,<br/>second vendor"]
    M3["Small tier<br/>triage and batch"]
  end
  OBS["L9 traces and evaluations<br/>OpenTelemetry spans from workflow and gateway<br/>to a managed platform; eval set and prompts<br/>in Git, CI gate"]
  OUT["Draft shown to the user,<br/>who edits and decides"]
  LATER["Added at the first enterprise deal:<br/>SSO and SCIM, EU processing route,<br/>dedicated-tenant option, SOC 2,<br/>AI questionnaire, data export"]:::later
  U --> APP
  AUTH --> WF
  WF --> TOOLS
  WF <--> PG
  WF --> KEYS
  KEYS --> MOD
  WF --> CHK --> OUT
  WF --> OBS
  OBS ~~~ LATER
```
