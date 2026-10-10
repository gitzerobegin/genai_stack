# The agent inside the customer's stack: the integration contract
Caption: The start-up ships a signed release (container, manifest, Agent Card, evaluation suite, SBOM) that runs in the customer's cloud account. Every dependency the agent has is a customer-owned interface: the customer's IdP registers the agent and issues a short-lived on-behalf-of token per tool; model calls go through the customer's AI gateway to the customer's chosen models; tool calls go through the customer's tool gateway under deny-by-default policy; telemetry, evidence and cost land in the customer's stores. The vendor receives only opt-in health metadata.

```mermaid
flowchart TD
  classDef vendor fill:#E8F0F8,stroke:#2E6DA4,stroke-width:2px;
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  subgraph OUT["Outside the customer's account"]
    direction LR
    V["Agent start-up<br/>signed release: container, manifest,<br/>Agent Card, evaluation suite, SBOM"]:::vendor
    U["Named business user<br/>signs in through the customer's IdP"]
  end
  subgraph CS["Customer's cloud account: the agent runs here"]
    direction TB
    AG["Agent runtime (L3)<br/>deterministic workflow + one bounded agent step<br/>registered agent identity, no standing secrets"]
    CFG["C5 customer overlay in Git<br/>thresholds, model pins, tool list"]:::note
    subgraph CP["Customer control plane: the integration contract"]
      direction LR
      ID["C4 identity<br/>agent ID + sponsor<br/>OBO token per tool"]
      GW["C1 AI gateway<br/>customer's model route,<br/>region and budget"]
      TG["L4 tool gateway<br/>MCP or OpenAPI tools<br/>allow-list + policy"]
      PR["C3 privacy service<br/>redact before<br/>any model call"]
    end
    subgraph EV["Customer evidence plane"]
      direction LR
      OT["L9 OTel collector<br/>gen_ai.* spans"]
      ES["C8 evidence store<br/>one record per output"]
      FN["C6 cost per task<br/>FOCUS-shaped"]
    end
  end
  subgraph DS["Behind the customer's gateways"]
    direction LR
    M["Customer's model portfolio (L1, L2)<br/>two vendors, in region"]
    SOR["Systems of record<br/>read-only tools"]
  end
  V -- "marketplace or private offer" --> AG
  U --> ID
  CFG -.-> AG
  AG --> CP
  GW --> M
  TG --> SOR
  AG --> EV
  OT --> ES
  OT --> FN
  AG -. "opt-in health metadata only" .-> V
```
