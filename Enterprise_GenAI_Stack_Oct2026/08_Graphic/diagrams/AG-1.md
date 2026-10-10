# The agent inside the customer's stack: the integration contract
Caption: The start-up ships a signed release (container, manifest, Agent Card, evaluation suite, SBOM) that runs in the customer's cloud account. Every dependency the agent has is a customer-owned interface: the customer's IdP registers the agent and issues a short-lived on-behalf-of token per tool; model calls go through the customer's AI gateway to the customer's chosen models; tool calls go through the customer's tool gateway under deny-by-default policy; telemetry, evidence and cost land in the customer's stores. The vendor receives only opt-in health metadata.

```mermaid
flowchart TD
  classDef vendor fill:#E8F0F8,stroke:#2E6DA4,stroke-width:2px;
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  V["Agent start-up<br/>signed release: container,<br/>manifest, Agent Card,<br/>evaluation suite, SBOM"]:::vendor
  U["Named business user<br/>signs in through<br/>the customer's IdP"]
  subgraph RUN["Customer's cloud account: the agent runs here"]
    direction LR
    CFG["C5 customer overlay in Git<br/>thresholds, model pins,<br/>tool list"]:::note
    AG["L3 agent runtime<br/>deterministic workflow +<br/>one bounded agent step<br/>registered agent identity,<br/>no standing secrets"]
    CFG -.-> AG
  end
  subgraph CP["Customer control plane: the integration contract"]
    direction LR
    ID["C4 identity<br/>agent ID + sponsor<br/>OBO token per tool"]
    PR["C3 privacy service<br/>redact before any model call"]
    TG["L4 tool gateway<br/>MCP or OpenAPI tools<br/>allow-list + policy"]
    GW["C1 AI gateway<br/>customer's model route,<br/>region and budget"]
  end
  subgraph EV["Customer evidence plane"]
    direction LR
    OT["L9 OTel collector<br/>gen_ai.* spans"]
    ES["C8 evidence store<br/>one record per output"]
    FN["C6 cost per task<br/>FOCUS-shaped"]
    OT --> ES
    OT --> FN
  end
  subgraph DS["Behind the customer's gateways"]
    direction LR
    SOR["Systems of record<br/>read-only, via the<br/>L4 tool gateway"]
    M["Customer's model portfolio<br/>L1, L2: two vendors, in region,<br/>via the C1 AI gateway"]
  end
  HM["To the start-up:<br/>opt-in health<br/>metadata only"]:::note
  V -->|"marketplace or<br/>private offer"| RUN
  U --> RUN
  RUN --> CP
  RUN --> EV
  RUN -.-> HM
  CP --> DS
```
