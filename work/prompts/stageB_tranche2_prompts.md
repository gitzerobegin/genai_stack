# Stage B, tranche 2: prompts as executed (8 October 2026, after CP2)

**Setup.** All eight agents ran in parallel as background `general-purpose` agents. Each writer prompt starts with the same preamble, then gives its outputs, product list and specific guidance:

```text
FIRST read and follow exactly: /home/user/genai_stack/work/stage0/07_stageB_writer_brief.md (files to read, 13-part template, CP2 deep-dive format, assessments.json format, hard rules) and work/stage0/08_scoring_rubric.md (including CP2 rules 6–9). Also read checkpoints/CP2/03_CP2_Decisions.md, and read work/stageB/L9/section.md as the reference example of tone, tagging and deep-dive format (approved at CP2).
```

| Agent | Scope | Outputs | Products | Key guidance (verbatim in the session transcript; summarised here) |
|---|---|---|---|---|
| **Rework** | Apply CP2 to L9, L8, L7 | `work/stageB/_review/CP2_rework_log.md`, plus edited sections and assessments | All L9–L7 | Re-score under rules 6–9: hyperscaler presumption; any one verified control lifts the cap to 3; certification scope at one point below the anchor; tiers by judgement. Update the x.8 tables and tier lines. Standardise the L8 and L7 deep dives to the L9 format. One illustrative scenario per layer. Up to 15 searches (B-REV-S028 onwards). Run `check_tags.py`. |
| **L6** | Retrieval and knowledge stores | `work/stageB/L6/` | pgvector, Pinecone, Qdrant, Milvus/Zilliz, Weaviate, turbopuffer, Elasticsearch, MongoDB, Chroma, S3 Vectors | Plan §5 L6 questions. H5 (rename to "Retrieval / Knowledge Stores"). The "do you need a dedicated vector DB?" decision. Licence and ownership nuance. **turbopuffer names Anthropic as a customer: disclose.** FS: filter before rank, multi-tenancy, residency, erasure, exit. Worked example: fund-level entitlement filters. |
| **L5** | Memory | `work/stageB/L5/` | Mem0, Zep, Letta, Cognee, Supermemory, LangMem, AgentCore Memory, Vertex Memory Bank | Memory types and where each physically lives (H4). Governance: retention, erasure, poisoning. Why memory comes last in the build order. FS: GDPR erasure, SS1/23 reproducibility. Worked example: governed, versioned "style memory"; no client identifiers. |
| **L4** | Tools, protocols, connectivity | `work/stageB/L4/` | MCP, A2A, Agent Skills, Composio, Exa, Tavily, Browserbase, E2B, AgentCore Gateway+Identity | **Conflict-of-interest disclosure for MCP and Agent Skills**: same rubric; record criticisms; name alternatives. H3. MCP 2026-07-28, Registry in preview, A2A 1.0. Tavily → Nebius. FS: least privilege, read-only tools, egress, sandboxing, OWASP Agentic 2026. Worked example: read-only MCP tools and sandboxed calculation. |
| **C1+C2** | Gateway, guardrails | `work/stageB/C1/`, `work/stageB/C2/` | C1: 9 gateways · C2: 6 guardrail products | H1. LiteLLM supply-chain compromise. Portkey → Palo Alto (US$117m filing figure only). Gateway as the enabler of exit plans. Guardrails cannot fix a workflow that should not be autonomous. OWASP 2026. Art. 26 logs. |
| **C3+C4** | DLP/PII, agent identity | `work/stageB/C3/`, `work/stageB/C4/` | C3: 5 · C4: 6 | DLP placement across L8, C1, L5 and L9. H7, H3. Presidio governance change. Purview DSPM. Entra Agent ID, Okta/Auth0, ID-JAG, MCP authorisation (disclosure). DUAA, adequacy, DPF. Worked example: tokenised client identifiers; on-behalf-of read-only scopes. |
| **C5+C6** | Prompt/config, FinOps | `work/stageB/C5/`, `work/stageB/C6/` | C5: 5 · C6: 5 | Prompts and embedding versions are production config. LaunchDarkly AgentControl. Promptfoo (acquisition announced only). Cost per task, not per token. **FOCUS 1.5 token column is deferred.** Helicone → Mintlify. SS1/23 change control. |
| **C7+C8** | AI security, model risk and governance | `work/stageB/C7/`, `work/stageB/C8/` | C7: 6 · C8: 6 | Indirect prompt injection; supply chain (LiteLLM); consolidation (filing figures only). **C8: SR 26-2 excludes GenAI**; SS1/23 and the EU AI Act are the anchors; "is an LLM/agent a model?"; H8 (the eval suite is the validation evidence); H7 lineage. Worked example: a per-commentary audit evidence pack. |

**To re-run this tranche:**
- **Writers:** copy the L6, L5 or L4 prompt pattern from `stageA_prime_and_stageB_prompts.md` (L9, L8, L7 writers), adding the preamble above and the product list and guidance from this table.
- **Controls:** each writer prompt covers two controls, using numbering `## C<n>. <name>` and C<n>.1 to C<n>.13.

## Tranche 2: interruptions and calibration reviewers

**Interruptions.** Two usage-limit (429) interruptions occurred. Each time, the stopped agents were resumed with `SendMessage`, for example: "Resume after the rate limit. Status on disk: … MISSING. Write … then give the final reply."

**Reviewers.** Two calibration reviewers ran in parallel. Both read the approved L9–L7 calibration (`checkpoints/CP2/02_Calibration_Review.md`, `work/stageB/_review/CP2_rework_log.md`) and the shared table `work/stageB/_review/all_scores.md`.

| | Reviewer A | Reviewer B |
|---|---|---|
| **Scope** | L6, L5, L4, C1, C2 | C3–C8 |
| **Focus** | Tier consistency (Pinecone vs MongoDB, MCP vs A2A, LiteLLM after its compromise, L6 scored above L7). Conflict-of-interest scoring for MCP, Agent Skills and turbopuffer. The L6 malformed tag. | C4 "all Strategic" tier inflation. MCP authorisation (conflict of interest). Pattern-vs-product tiering. C8 regulatory precision against `regulatory_facts.json`. |
| **Common steps** | At least 12 claim spot-checks per section; do-not-rely lists; `check_tags.py`; up to 15 searches | Same |
| **Source IDs** | B-REVA-S### | B-REVB-S### |
| **Output** | `work/stageB/_review/CP3_review_A.md` | `work/stageB/_review/CP3_review_B.md` |
