# The agentic-SDLC product inside the customer's stack: the customer's identity, models, tools and evidence; the vendor's agent loop
Caption: The start-up ships an agent runner that executes in the customer's account or on the customer's CI runners, with a thin vendor control plane that never holds source code. Every model call goes through the customer's gateway to the customer's model endpoint, every tool call through the customer's tool gateway, every credential comes from the customer's vault, and the only way the agent changes code is a pull request that the customer's CI checks and a named human merges. Spans, cost per task and an evidence record go to the customer's collector and evidence store.

```mermaid
flowchart TD
  classDef vendor fill:#FBF4E4,stroke:#D4A13A,stroke-width:2px;
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  ENG["Customer engineer assigns a task<br/>SSO through the customer's IdP"]
  subgraph SDLC["Customer software-delivery chain"]
    direction LR
    REPO["Repository<br/>branch protection<br/>AGENTS.md"]
    CI["Customer CI<br/>tests, SAST,<br/>secret scanning"]
    REV["Review<br/>named human merges"]
    REPO --> CI --> REV
  end
  subgraph RUN["Vendor agent runner in the customer's account or CI runners"]
    direction LR
    LOOP["L3 agent loop<br/>plan, edit, test"]
    SBX["L4 sandbox<br/>microVM, default-deny egress"]
    LOOP --> SBX
  end
  VCP["Vendor control plane (SaaS)<br/>licences, job metadata, no code"]:::note
  subgraph CP["Customer GenAI control plane"]
    direction LR
    ID["C4 agent identity<br/>on behalf of the engineer"]
    GW["C1 gateway<br/>to customer model endpoint<br/>L1, L2: no retention"]
    TG["L4 tool gateway<br/>MCP allow-list"]
    VLT["C7 vault<br/>short-lived tokens"]
  end
  subgraph EV["Customer evidence plane"]
    direction LR
    OT["L9 OTel spans<br/>to customer collector"]
    COST["C6 cost<br/>per task"]
    EVD["C8 evidence record<br/>per agent action"]
  end
  ENG --> RUN
  VCP -.-> RUN
  RUN --> CP
  RUN -->|"pull request only"| SDLC
  RUN --> EV
  CP --> EV
  class LOOP,SBX vendor;
```
