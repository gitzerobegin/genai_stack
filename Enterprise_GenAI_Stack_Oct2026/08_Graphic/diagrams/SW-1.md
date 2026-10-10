# SW architecture: the vendor's release plane and the product inside the customer's estate
Caption: The vendor qualifies every supported model, gates every redistributed component and ships a signed release; in the customer's estate the AI feature uses the product's own permissions, calls the model through the customer's gateway or cloud account (or a bundled open-weight model on air-gapped sites), and sends telemetry and audit events to the customer's own tools.

```mermaid
flowchart TD
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  subgraph V["1 · Vendor: build and release plane (CRA manufacturer, AI Act provider)"]
    direction LR
    V1["Support matrix<br/>hosted models via the customer's<br/>account + one bundled open-weight model"]
    V2["Release qualification<br/>one evaluation suite on every<br/>supported model, every release"]
    V3["Licence and supply-chain gate<br/>redistribution review, SBOM,<br/>model scanning, signing"]
    V4["Signed release<br/>installer, container or marketplace image,<br/>model pack, SBOM, support period"]
    V1 --> V2 --> V3 --> V4
  end
  subgraph P["2 · Customer estate: the product as deployed (self-managed, on-premises, air-gapped or marketplace)"]
    direction LR
    P2["AI feature<br/>product's own permissions<br/>and audit log; one<br/>bounded model step"]
    PR["C3 redaction<br/>before any<br/>external call"]
    P3["Retrieval in the<br/>product's own database,<br/>permission-filtered;<br/>chunks screened (C2)"]
    P4["Model adapter<br/>OpenAI-compatible<br/>endpoint setting"]
    P5["Output checks,<br/>AI label and machine-<br/>readable marking"]
    P6["Telemetry exporter<br/>OTel GenAI spans,<br/>redaction on"]
    BR["Bundled route for<br/>air-gapped sites:<br/>vLLM + open-weight<br/>model, shipped in<br/>the release"]
    P2 --> PR --> P3 --> P4 --> P5 --> P6
    P4 -.-> BR
  end
  subgraph C["3 · Customer's own control plane: the product plugs in and never replaces it"]
    direction LR
    C4["Customer IdP<br/>SSO and SCIM (C4)"]
    C1["Customer gateway (C1)<br/>or hyperscaler account:<br/>Bedrock, Foundry or Gemini<br/>Enterprise Agent Platform"]
    C9["Customer OTel collector,<br/>SIEM and evidence store<br/>(L9, C8)"]
    C4 ~~~ C1 ~~~ C9
  end
  V -- "customer installs or subscribes" --> P
  P -- "SSO and SCIM · model calls · OTel spans and audit events" --> C
  N["Back channel to the vendor: vulnerability and incident handling<br/>(CRA early warning 24 h, notification 72 h); opt-in support telemetry only"]:::note
  C -.-> N
```
