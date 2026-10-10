# The technology service provider's GenAI architecture: one estate, every call tenant-aware
Caption: The provider runs one control plane for all tenants: tenant identity travels in every token, the gateway meters, limits and routes per tenant, the privacy service redacts each request before the gateway, the model and knowledge planes are partitioned by tenant in three tiers (pooled by default, bridged for regulated or residency-bound tenants, siloed for tenants who pay for single-tenancy), and every span carries the tenant ID so cost, margin and customer evidence can be reported per tenant.

```mermaid
flowchart TD
  classDef note fill:#FBF4E4,stroke:#D4A13A,stroke-dasharray:4 3;
  T["Tenant end users and tenant admins<br/>customer identity; per-tenant AI settings and opt-out"]
  subgraph CP["Provider control plane: one estate, tenant-aware"]
    direction LR
    ID["C4 identity<br/>tenant + user + agent<br/>in every token"]
    APP["L3 workflow per feature<br/>tenant ID on every step"]
    PG["C3 privacy service + C2 screen<br/>per-tenant policy;<br/>redact before the gateway"]
    GW["C1 gateway<br/>key, quota, budget per tenant<br/>route by tenant residency"]
    ID --> APP --> PG --> GW
  end
  CFG["C5 manifest: global release<br/>plus tenant overlays"]:::note
  CFG -.-> CP
  T --> CP
  subgraph MP["Model plane: L1, L2, in three tenancy tiers"]
    direction LR
    M1["Pooled (default)<br/>shared deployments: Vendor A<br/>mid + small tier, Vendor B<br/>fallback, Batch / Flex for async"]
    M2["Bridged<br/>shared deployments with<br/>dedicated capacity or<br/>region for the tenant"]
    M3["Siloed<br/>dedicated deployment, or<br/>the tenant's own model<br/>account; fine-tuned models"]
    M1 ~~~ M2 ~~~ M3
  end
  subgraph KP["Knowledge and tools: L4 to L8, in the same three tiers"]
    direction LR
    K1["Pooled (default)<br/>shared index, tenant filter<br/>injected from the token"]
    K2["Bridged<br/>partition or namespace<br/>per tenant + own key"]
    K3["Siloed<br/>own index and key,<br/>deployment stamp"]
    TL["Tenant tools via L4 gateway<br/>delegated per-tenant tokens"]
    K1 ~~~ K2 ~~~ K3 ~~~ TL
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
