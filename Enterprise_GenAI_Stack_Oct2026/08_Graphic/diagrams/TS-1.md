# The technology service provider's GenAI architecture: one estate, every call tenant-aware
Caption: The provider runs one control plane for all tenants: tenant identity travels in every token, the gateway meters, limits and routes per tenant, the knowledge plane is partitioned by tenant (pooled by default, siloed for tenants who pay for it), and every span carries the tenant ID so cost, margin and customer evidence can be reported per tenant.

```mermaid
flowchart TD
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  T["Tenant end users and tenant admins<br/>customer identity; per-tenant AI settings and opt-out"]
  subgraph CP["Provider control plane: one estate, tenant-aware"]
    direction LR
    ID["C4 identity<br/>tenant + user + agent<br/>in every token"]
    APP["L3 workflow per feature<br/>tenant ID on every step"]
    GW["C1 gateway<br/>key, quota, budget per tenant<br/>route by tenant residency"]
    PG["C2 / C3 policy per tenant<br/>redact before any model"]
    ID --> APP --> GW --> PG
  end
  CFG["C5 manifest: global release<br/>plus tenant overlays"]:::note
  CFG -.-> CP
  T --> CP
  subgraph MP["Shared model plane: L1, L2"]
    direction LR
    M1["Vendor A<br/>mid + small tier<br/>reserved for peak"]
    M2["Vendor B<br/>qualified fallback"]
    M3["Batch / Flex<br/>for async work"]
    BYO["Tenant's own<br/>model account<br/>(optional)"]
    M1 ~~~ M2 ~~~ M3 ~~~ BYO
  end
  subgraph KP["Knowledge and tools: L4 to L8, partitioned by tenant"]
    direction LR
    K1["Pooled index<br/>tenant filter injected"]
    K2["Siloed index + key<br/>for tenants who pay"]
    TL["Tenant tools via L4 gateway<br/>delegated per-tenant tokens"]
    K1 ~~~ K2 ~~~ TL
  end
  CP --> MP
  MP ~~~ KP
  CP --> KP
  subgraph EV["Evidence and margin: L9, C6, C8"]
    direction LR
    OT["L9 OTel spans<br/>tagged with tenant ID"]
    FIN["C6 cost per tenant<br/>margin per feature"]
    ASR["C8 evidence and<br/>customer assurance pack"]
    OT --> FIN
    OT --> ASR
  end
  MP --> EV
  KP --> EV
```
