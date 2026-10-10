# Where an AI tool plugs into the customer's control plane
Caption: The buyer owns the control plane; the start-up's tool is one call-out inside it. The customer's workflow reaches the tool only through the gateway of record (and from ingestion and trace export), the tool runs in the customer's account or behind a private endpoint, takes its policy from the customer's Git, and writes spans, verdict records and usage to the customer's own collector, evidence store and cost dataset. The vendor plane ships signed releases and never sees customer content.

```mermaid
flowchart TD
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  classDef tool fill:#FDF1D6,stroke:#D4A13A,stroke-width:3px;
  U["Customer staff and agents<br/>C4: SSO, SCIM, agent identity,<br/>on-behalf-of token"]
  subgraph CUST["Customer estate: the buyer owns the control plane"]
    direction TB
    subgraph CP["Control plane"]
      direction LR
      WF["L3 workflow<br/>calls only the gateway"]
      GW["C1 gateway of record<br/>pre-call and post-call hooks"]
      POL["C5 policy as code in Git<br/>C4 policy decision"]
    end
    TOOL["The start-up's AI tool<br/>container in the customer's account,<br/>or EU SaaS behind a private endpoint<br/>also called from L8 ingestion and L9 export"]:::tool
    MP["L1 / L2 model plane<br/>the customer's own model accounts"]
    subgraph EV["Evidence plane: the customer's stores"]
      direction LR
      OT["L9 OTel Collector<br/>gen_ai spans, pinned version"]
      EVS["C8 evidence store<br/>verdict record per trace ID"]
      FIN["C6 cost dataset<br/>usage per use case"]
    end
  end
  VEN["Start-up's vendor plane<br/>signed images, SBOM, licence, support<br/>no customer content"]:::note
  U --> WF --> GW
  GW -- "request: text, policy ID, trace ID" --> TOOL
  TOOL -- "allow / block / transform" --> GW
  GW --> MP
  POL -.-> TOOL
  TOOL --> OT
  TOOL --> EVS
  TOOL --> FIN
  VEN -. "releases only" .-> TOOL
```
