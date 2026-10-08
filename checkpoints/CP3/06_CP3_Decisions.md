# CP3 decisions

**Date:** 8 October 2026

| Q | Decision (user) | Rule applied from now on |
|---|---|---|
| Q1 MCP, MCP authorisation, A2A | **All three Strategic, conditional** | MCP and its authorisation profile are one decision: Strategic only behind a gateway with mandatory authorisation, an allow-list and pinned tool definitions. A2A is Strategic only where cross-team or cross-vendor agent delegation is in scope. **The user made this decision.** The conflict-of-interest disclosure stays: MCP originated at Anthropic, and the author is an Anthropic model. |
| Q2 Hyperscaler-native services | **Strategic, conditional "where this is your primary cloud"**, for the lead service in each category | Security stays at 4 (rule 8). Applied with judgement: no criterion at 1, and the service must be the cloud's lead offering in that category. |
| Q3 Evidence for enterprise readiness 4 | Option (a): **any primary vendor page counts**, with the limitation stated as a condition | |
| Q4 LiteLLM, Composio, Cognee | **As now** | LiteLLM: Strategic, conditional (hardened, pinned, Enterprise). Composio: Experimental. Cognee: Tactical, self-host only. |
| Q5 Criterion at 2 under Strategic | Option (a): allowed when the condition is an **existing platform commitment** | Pinecone stays Tactical |
| Q6 Entra / Okta below 3.6 | Option (a): **keep both Strategic, conditional** (directory-bound) | |
| Q7 Patterns and standards | Option (a): **scored and tiered like products** | Rule 3 still applies when a named component changed owner |
| Q8 Presidio | Option (a): **Strategic, conditional** | Behind a firm-owned privacy-service API, with recall tests in CI |
| Q9 Certification-capped platforms | **Keep the caps and Tactical tiers**, adding "candidate for Strategic after due diligence" to watsonx.governance and Prisma AIRS | Vendor regulatory claims never raise a score |
