#!/usr/bin/env python3
"""Build the corrected "full stack" graphic from the dataset (one tile per assessed product).

Usage: python3 -I tools/build_stack_graphic.py <repo_root>
Writes work/stageD/stack_graphic.html; then render with
  NODE_PATH=$(npm root -g) node tools/render_graphic.js work/stageD/stack_graphic.html <out_dir>/Enterprise_GenAI_Stack_Oct2026
which writes .png (3200 px wide) and .pdf.

Tiles come from 05_Data/products.json (tier, flags, original label). Short labels and one-line notes are
curated below from the synthesis (Parts I, IV and XI); every product in the dataset must have a label.
"""
import html, json, os, sys

root = sys.argv[1]; os.chdir(root)
PKG = "Enterprise_GenAI_Stack_Oct2026"
prods = {p["id"]: p for p in json.load(open(PKG + "/05_Data/products.json", encoding="utf-8"))}

# id: (label, note, cloud)  cloud = AWS / Azure / Google Cloud where the Strategic tier is conditional on that cloud
L = {
 # C1 gateway
 "C1-litellm": ("LiteLLM", "Enterprise licence · pin and sign builds", ""),
 "C1-kong-ai-gateway": ("Kong AI Gateway", "where Kong is the API standard", ""),
 "C1-aws-agentcore-gateway": ("AgentCore Gateway", "MCP gateway", "AWS"),
 "C1-azure-apim-ai-gateway": ("Azure APIM AI gateway", "GA policies only", "Azure"),
 "C1-google-apigee-ai-gateway": ("Apigee AI gateway", "MCP support GA", "Google Cloud"),
 "C1-agentgateway": ("agentgateway", "MCP / A2A on Kubernetes", ""),
 "C1-envoy-ai-gateway": ("Envoy AI Gateway", "Agent Router · in-cluster", ""),
 "C1-cloudflare-ai-gateway": ("Cloudflare AI Gateway", "non-confidential work, BYOK", ""),
 "C1-portkey": ("Portkey", "Palo Alto Networks · Prisma AIRS", ""),
 # C2 guardrails
 "C2-bedrock-guardrails": ("Bedrock Guardrails", "standalone API from the gateway", "AWS"),
 "C2-azure-ai-content-safety": ("Azure AI Content Safety", "Prompt Shields on documents", "Azure"),
 "C2-google-model-armor": ("Model Armor", "strict residency", "Google Cloud"),
 "C2-nemo-guardrails": ("NeMo Guardrails", "orchestrator · still 0.x", ""),
 "C2-meta-llama-protections": ("Llama Guard / Prompt Guard", "one detector among several", ""),
 "C2-guardrails-ai": ("Guardrails AI", "Harvey-owned · hosted hub retired", ""),
 # C3 privacy
 "C3-presidio": ("Presidio", "behind a firm privacy-service API", ""),
 "C3-google-sdp": ("Sensitive Data Protection", "Google's DLP service", "Google Cloud"),
 "C3-microsoft-purview-dspm-ai": ("Purview DSPM for AI", "posture, not prompt-path DLP", "Azure"),
 "C3-protegrity": ("Protegrity", "existing customers", ""),
 "C3-skyflow": ("Skyflow", "vault tokenisation", ""),
 # C4 identity
 "C4-opa": ("OPA", "policy decision point · CNCF", ""),
 "C4-spiffe-spire": ("SPIFFE / SPIRE", "workload identity · CNCF", ""),
 "C4-cedar": ("Cedar", "policy language · AgentCore Policy", ""),
 "C4-mcp-authorization": ("MCP Authorization", "Anthropic-originated · alt: OAuth on OpenAPI", ""),
 "C4-entra-agent-id": ("Entra Agent ID", "where Entra holds the workforce", ""),
 "C4-okta-auth0-ai-agents": ("Okta / Auth0 for AI Agents", "where Okta holds the workforce", ""),
 # C5 configuration
 "C5-prompts-as-code": ("Prompts as code (Git)", "the configuration of record", ""),
 "C5-langfuse-prompts": ("Langfuse Prompts", "with Langfuse as L9 platform", ""),
 "C5-langsmith-prompts": ("LangSmith Prompts", "with LangSmith as L9 platform", ""),
 "C5-promptlayer": ("PromptLayer", "framework-neutral registry", ""),
 "C5-launchdarkly-ai-configs": ("LaunchDarkly AgentControl", "rollout between approved variants", ""),
 # C6 FinOps
 "C6-gateway-cost-attribution": ("Gateway cost attribution", "budgets that fail closed", ""),
 "C6-finops-focus": ("FinOps FOCUS", "open billing data standard", ""),
 "C6-vantage": ("Vantage", "reporting layer only", ""),
 "C6-cloudzero": ("CloudZero", "reporting layer only", ""),
 "C6-helicone": ("Helicone", "maintenance mode · migrate", ""),
 # C7 security
 "C7-hashicorp-vault": ("HashiCorp Vault", "IBM · agentic IAM · BUSL", ""),
 "C7-model-supply-chain-scanning": ("Model & package scanning", "safetensors by default", ""),
 "C7-lakera": ("Check Point AI Guardrails", "formerly Lakera Guard", ""),
 "C7-prisma-airs": ("Prisma AIRS", "Palo Alto estates", ""),
 "C7-hiddenlayer": ("HiddenLayer", "independent specialist", ""),
 "C7-openssf-model-signing": ("OpenSSF Model Signing", "sign weights you produce", ""),
 # C8 governance
 "C8-openlineage": ("OpenLineage", "+ firm GenAI facets", ""),
 "C8-validmind": ("ValidMind", "model-risk-led firms", ""),
 "C8-watsonx-governance": ("IBM watsonx.governance", "IBM estates", ""),
 "C8-credo-ai": ("Credo AI", "policy-led programmes", ""),
 "C8-collibra-ai-governance": ("Collibra AI Governance", "where Collibra is the catalogue", ""),
 "C8-modelop": ("ModelOp", "after full due diligence", ""),
 # L9
 "L9-langfuse": ("Langfuse", "ClickHouse-owned · self-host", ""),
 "L9-langsmith": ("LangSmith", "LangGraph estates · BYOC, EU", ""),
 "L9-mlflow-genai": ("MLflow GenAI", "where an ML platform exists", ""),
 "L9-braintrust": ("Braintrust", "eval-led teams", ""),
 "L9-deepeval": ("DeepEval", "CI metric library", ""),
 "L9-promptfoo": ("Promptfoo", "red-teaming · OpenAI deal announced", ""),
 "L9-opik": ("Opik", "Comet · Apache-2.0", ""),
 "L9-arize-phoenix": ("Arize Phoenix", "Dynatrace-owned · ELv2", ""),
 "L9-arize-ax": ("Arize AX", "Dynatrace-owned", ""),
 "L9-datadog-agent-observability": ("Datadog Agent Observability", "Datadog APM estates", ""),
 "L9-wandb-weave": ("W&B Weave", "CoreWeave-owned", ""),
 # L8
 "L8-docling": ("Docling", "default engine · LF AI & Data", ""),
 "L8-unstructured": ("Unstructured", "ACL-aware connectors", ""),
 "L8-google-document-ai": ("Google Document AI", "processor region confirmed", "Google Cloud"),
 "L8-llamaparse": ("LlamaParse", "parse and extract only", ""),
 "L8-reducto": ("Reducto", "hard documents", ""),
 "L8-mistral-ocr": ("Mistral OCR 4.1", "pin the model ID", ""),
 "L8-firecrawl": ("Firecrawl", "AGPL server · cloud with ZDR", ""),
 "L8-apify": ("Apify", "public data only", ""),
 "L8-crawl4ai": ("Crawl4AI", "pre-1.0 · pilots", ""),
 "L8-mineru": ("MinerU", "licence thresholds apply", ""),
 # L7
 "L7-sentence-transformers": ("Sentence Transformers", "graphic said “SBERT” · self-host", ""),
 "L7-gemini-embedding": ("Gemini Embedding 2", "EU endpoint excludes the UK", "Google Cloud"),
 "L7-cohere": ("Cohere Embed 5 + Rerank", "private deployment", ""),
 "L7-openai": ("OpenAI text-embedding-3", "text baseline", ""),
 "L7-voyage": ("Voyage AI", "MongoDB-owned", ""),
 "L7-jina": ("Jina AI", "Elastic-owned · CC-BY-NC weights", ""),
 "L7-qwen3-embedding": ("Qwen3 Embedding", "self-host after review", ""),
 "L7-nvidia-nemo-retriever": ("NVIDIA NeMo Retriever", "NVIDIA estates", ""),
 "L7-ethicalagents": ("EthicalAgents", "removed · could not be verified", ""),
 "L7-ragoos": ("Ragoos", "removed · could not be verified", ""),
 # L6
 "L6-pgvector": ("PostgreSQL + pgvector", "where Postgres is standard", ""),
 "L6-elasticsearch": ("Elasticsearch", "hybrid + document-level security", ""),
 "L6-mongodb-atlas-vector-search": ("MongoDB Vector Search", "GA self-managed too", ""),
 "L6-qdrant": ("Qdrant", "dedicated engine after a load test", ""),
 "L6-milvus-zilliz": ("Milvus / Zilliz", "very large corpora", ""),
 "L6-pinecone": ("Pinecone", "managed · BYOC", ""),
 "L6-weaviate": ("Weaviate", "licence in transition", ""),
 "L6-turbopuffer": ("turbopuffer", "many tenants · BYOC only", ""),
 "L6-chroma": ("Chroma", "prototypes and harnesses", ""),
 "L6-s3-vectors": ("S3 Vectors", "AWS cost tier · no BM25", ""),
 # L5
 "L5-aws-agentcore-memory": ("AgentCore Memory", "inside its own runtime", "AWS"),
 "L5-gcp-vertex-memory-bank": ("Memory Bank", "Agent Engine", "Google Cloud"),
 "L5-mem0": ("Mem0", "OSS behind a firm memory API", ""),
 "L5-zep": ("Zep / Graphiti", "Community Edition deprecated", ""),
 "L5-cognee": ("Cognee", "in-estate only", ""),
 "L5-letta": ("Letta", "now an agent harness", ""),
 "L5-supermemory": ("Supermemory", "v5 breaking change", ""),
 "L5-langmem": ("LangMem", "no release since Oct 2025", ""),
 # L4
 "L4-mcp": ("MCP", "behind a governed gateway · alt: OpenAPI", ""),
 "L4-a2a": ("A2A 1.0", "cross-team delegation · signed cards", ""),
 "L4-aws-agentcore-gateway-identity": ("AgentCore Gateway + Identity", "managed tool governance", "AWS"),
 "L4-agent-skills": ("Agent Skills", "script-free, internal · alt: AGENTS.md", ""),
 "L4-e2b": ("E2B", "microVM sandbox", ""),
 "L4-exa": ("Exa", "via egress proxy + DLP", ""),
 "L4-tavily": ("Tavily", "Nebius-owned", ""),
 "L4-browserbase": ("Browserbase", "only where no API exists", ""),
 "L4-composio": ("Composio", "May 2026 token incident · self-host", ""),
 # L3
 "L3-langgraph": ("LangGraph", "default · workflows + agents", ""),
 "L3-temporal": ("Temporal", "durable execution", ""),
 "L3-pydantic-ai": ("Pydantic AI", "typed agent steps", ""),
 "L3-microsoft-agent-framework": ("Microsoft Agent Framework", "GA · replaces AutoGen", ""),
 "L3-aws-strands-agentcore": ("Strands + AgentCore Runtime", "framework + managed runtime", "AWS"),
 "L3-google-adk": ("Google ADK", "on Agent Engine", "Google Cloud"),
 "L3-crewai": ("CrewAI", "use Flows for regulated work", ""),
 "L3-llamaindex": ("LlamaIndex", "retrieval toolkit", ""),
 "L3-openai-agents-sdk": ("OpenAI Agents SDK", "sandboxed sub-step · pre-1.0", ""),
 "L3-vercel-ai-sdk": ("Vercel AI SDK", "TypeScript app tier", ""),
 "L3-claude-agent-sdk": ("Claude Agent SDK", "Alpha · sandboxed only · alt: LangGraph", ""),
 "L3-mistral-agents": ("Mistral Agents API", "Workflows in beta", ""),
 # L2
 "L2-vllm": ("vLLM", "default engine · the exit route", ""),
 "L2-sglang": ("SGLang", "backup engine once CVE is fixed", ""),
 "L2-hugging-face": ("Hugging Face Hub", "governed weights · TGI archived", ""),
 "L2-fireworks-ai": ("Fireworks AI", "once ISO certificates confirmed", ""),
 "L2-together-ai": ("Together AI", "EU dedicated, ZDR on", ""),
 "L2-openrouter": ("OpenRouter", "behind the gateway · Stripe deal", ""),
 "L2-cerebras": ("Cerebras", "low latency, non-confidential", ""),
 "L2-ollama": ("Ollama", "developer tier", ""),
 "L2-lm-studio": ("LM Studio", "desktops only · no service use", ""),
 "L2-llm-d": ("llm-d", "CNCF sandbox · pilot", ""),
 "L2-nvidia-dynamo": ("NVIDIA Dynamo", "beta · pilot", ""),
 # L1
 "L1-openai": ("OpenAI GPT-6", "Astra · Sol · Luna · 6.1 Sol", ""),
 "L1-anthropic": ("Anthropic Claude", "hyperscaler EU route · tier set by reader", ""),
 "L1-mistral": ("Mistral", "Medium 3.5 · Large 3 · 3.1 retired", ""),
 "L1-google-gemma": ("Gemma 4", "graphic said “Gemma 2.9”", ""),
 "L1-google-gemini": ("Google Gemini 3.x", "pin versions · short lifetimes", "Google Cloud"),
 "L1-alibaba-qwen": ("Qwen 3.8", "self-host by policy", ""),
 "L1-deepseek": ("DeepSeek V4", "weights or in-tenant only", ""),
 "L1-zai-glm": ("Z.ai GLM-5.3", "graphic said “Q4”", ""),
 "L1-xai-grok": ("Grok 4.7 (SpaceXAI)", "via a hyperscaler only", ""),
 "L1-meta": ("Meta Muse / Llama", "block the contributor tier", ""),
 "L1-moonshot-kimi": ("Kimi K3", "custom licence", ""),
}
missing = sorted(set(prods) - set(L)); extra = sorted(set(L) - set(prods))
if missing or extra:
    sys.exit("label map out of step with products.json: missing %s, unknown %s" % (missing, extra))

CONTROLS = [("C1", "AI traffic gateway", "model, tool (MCP) and agent (A2A) calls"),
            ("C2", "Guardrails", "policy and tests owned by the firm"),
            ("C3", "Privacy service (DLP / PII)", "one API, six enforcement points"),
            ("C4", "Identity and authorisation", "every agent a registered identity"),
            ("C5", "Configuration of record", "prompts, pins and manifests in Git"),
            ("C6", "AI FinOps", "cost per task, budgets fail closed"),
            ("C7", "AI security", "secrets, supply chain, sandboxing"),
            ("C8", "Model risk and governance", "inventory, validation, evidence store")]
LAYERS = {  # revised name, original graphic name, one-line duty, fixes to the original
 "L9": ("Evaluation & observability plane", "9 · Evals & Observability", "evidence for every layer, from day one",
        "Repositioned from the bottom of the stack to a plane beside the controls. Phoenix and Arize are one owner now (Dynatrace)."),
 "L8": ("Ingestion & data preparation", "8 · Data Extraction", "approved sources, ACLs and lineage on every chunk",
        "Lineage, classification, DLP and ACL capture are built around replaceable parsers; runtime web access moves to L4."),
 "L7": ("Retrieval optimisation", "7 · Embeddings & Rerankers", "pinned embed + rerank, hybrid fusion, eval gate",
        "Embeddings and rerankers merged. EthicalAgents and Ragoos removed: they could not be verified."),
 "L6": ("Retrieval & knowledge stores", "6 · Vector Databases", "derived, entitlement-filtered, rebuildable index",
        "“Vector database” is now a feature: hybrid search ships almost everywhere. Prefer the platform you already run."),
 "L5": ("Memory service (part of L6)", "5 · Memory", "policy-gated writes, erasure by person",
        "No longer a separate infrastructure layer. Built last. Zep CE deprecated, Letta pivoted, LangMem stalled."),
 "L4": ("Tools & connectivity", "4 · Tools & Protocols", "nothing reachable except through the governed gateway",
        "Adds a mandatory tool-governance sub-layer. MCP and A2A moved to the Linux Foundation's AAIF."),
 "L3": ("Orchestration: workflows & agents", "3 · Agent Frameworks", "deterministic by default, durable, approval gates",
        "Workflow vs agent is the key decision. Adds durable execution. AutoGen superseded; Agent Builder shuts 30 Nov 2026."),
 "L2": ("Inference & model access", "2 · Inference & Access", "in-region access; vLLM as the private exit route",
        "Routing moves to the C1 gateway. TGI archived. Ollama and LM Studio are developer tools, not production."),
 "L1": ("Foundation-model portfolio", "1 · LLMs", "two unrelated vendors + small + open-weight, all pinned",
        "“Gemma 2.9” does not exist (Gemma 4). “Q4” is Z.ai GLM. Mistral Medium 3.1 retired. xAI is now SpaceXAI."),
}
PLANES = [("Agent plane", ["L3", "L4"]), ("Knowledge plane", ["L8", "L7", "L6", "L5"]), ("Model plane", ["L2", "L1"])]
PATTERNS = {"C5-prompts-as-code", "C6-gateway-cost-attribution", "C7-model-supply-chain-scanning"}
RANK = {"Strategic": 0, "Tactical": 1, "Experimental": 2, None: 3}

def tile(pid):
    p = prods[pid]; label, note, cloud = L[pid]
    cl = p.get("classification") or {}; tier = cl.get("tier") if p.get("scores") else None
    flags = cl.get("flags") or []
    cls = {"Strategic": "s", "Tactical": "t", "Experimental": "e"}.get(tier, "x")
    tags = []
    if p["layer"].startswith("L") and not p.get("original_label"): tags.append(("new", "NEW"))
    # practice/pattern records inherit flags from the products they cover; an ownership tag would mislead
    if "Acquired" in flags and pid not in PATTERNS: tags.append(("acq", "ACQUIRED"))
    if "Renamed" in flags: tags.append(("ren", "RENAMED"))
    if cloud: tags.append(("cloud", cloud))
    t = "".join('<span class="tag %s">%s</span>' % (c, html.escape(x)) for c, x in tags)
    return ('<div class="tile %s"><div class="tags">%s</div><div class="nm">%s</div><div class="nt">%s</div></div>'
            % (cls, t, html.escape(label), html.escape(note)))

def tiles(layer):
    ids = [i for i, p in prods.items() if p["layer"] == layer]
    ids.sort(key=lambda i: (RANK.get(((prods[i].get("classification") or {}).get("tier") if prods[i].get("scores") else None), 3),
                            -((prods[i].get("scores") or {}).get("fs_total") or 0), L[i][0].lower()))
    return "".join(tile(i) for i in ids)

counts = {"Strategic": 0, "Tactical": 0, "Experimental": 0}
for p in prods.values():
    t = (p.get("classification") or {}).get("tier")
    if p.get("scores") and t in counts: counts[t] += 1

def layer_row(code):
    name, was, duty, fix = LAYERS[code]
    extra = ""
    if code == "L2":
        extra = ('<div class="tile p"><div class="tags"><span class="tag pat">PATTERN · NOT SCORED</span></div>'
                 '<div class="nm">Primary cloud’s model service</div><div class="nt">Bedrock · Foundry · Gemini Enterprise Agent Platform, in region</div></div>')
    return ('<div class="row"><div class="lab"><div class="code">%s</div><div class="ln">%s</div><div class="was">was: %s</div>'
            '<div class="duty">%s</div><div class="fix">%s</div></div><div class="grid">%s%s</div></div>'
            % (code, html.escape(name), html.escape(was), html.escape(duty), html.escape(fix), extra, tiles(code)))

cards = "".join('<div class="card"><div class="ch"><span class="code">%s</span> %s<span class="cs">%s</span></div><div class="grid g3">%s</div></div>'
                % (c, html.escape(n), html.escape(s), tiles(c)) for c, n, s in CONTROLS)
planes = "".join('<div class="plane"><div class="ph">%s</div>%s</div>' % (n, "".join(layer_row(c) for c in codes)) for n, codes in PLANES)

page = """<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>The Enterprise GenAI Stack, corrected (October 2026)</title>
<style>
:root{--navy:#1B2A41;--teal:#0E7C7B;--teal2:#E6F3F2;--amber:#C9822B;--ink:#1F2933;--mute:#5B6B7A;--line:#D5DEE6;--bg:#F6F8FA}
*{box-sizing:border-box}body{margin:0;background:#fff;font-family:Inter,Arial,sans-serif;color:var(--ink);width:1600px}
.wrap{padding:36px 40px 28px}
h1{font-size:46px;letter-spacing:-.5px;margin:0;color:var(--navy);font-weight:800}
.sub{font-size:19px;color:var(--mute);margin-top:6px}
.stats{display:flex;gap:10px;margin:16px 0 12px;flex-wrap:wrap}
.stat{background:var(--bg);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:15px}
.stat b{color:var(--navy)}
.legend{display:flex;gap:18px;align-items:center;font-size:14px;color:var(--mute);margin-bottom:18px;flex-wrap:wrap}
.sw{display:inline-block;width:26px;height:16px;border-radius:4px;vertical-align:-3px;margin-right:6px}
.sw.s{background:var(--teal)}.sw.t{background:#fff;border:2px solid var(--teal)}.sw.e{background:#fff;border:2px dashed var(--amber)}.sw.x{background:#EEF1F4;border:1px solid #C3CCD5}
.sec{border-radius:16px;padding:16px 18px 18px;margin-bottom:16px}
.ctrl{background:#EEF2F7;border:2px solid var(--navy)}
.sh{display:flex;align-items:baseline;gap:12px;margin-bottom:12px}
.sh .t1{font-size:22px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:.5px}
.sh .t2{font-size:15px;color:var(--mute)}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 12px 12px}
.ch{font-weight:700;font-size:16px;color:var(--navy);margin-bottom:8px}
.ch .code{display:inline-block;background:var(--navy);color:#fff;border-radius:6px;padding:1px 7px;font-size:13px;margin-right:4px}
.cs{font-weight:400;color:var(--mute);font-size:13px;margin-left:8px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-content:start}
.grid.g3{grid-template-columns:repeat(3,1fr)}
.tile{border-radius:9px;padding:7px 9px 8px;min-height:62px;position:relative}
.tile .nm{font-weight:700;font-size:15px;line-height:1.15}
.tile .nt{font-size:12px;line-height:1.25;margin-top:2px}
.tile.s{background:var(--teal);color:#fff}.tile.s .nt{color:#DDF1EF}
.tile.t{background:#fff;border:2px solid var(--teal);color:var(--ink)}.tile.t .nt{color:var(--mute)}
.tile.e{background:#FFFBF4;border:2px dashed var(--amber);color:var(--ink)}.tile.e .nt{color:#8A5A1E}
.tile.x{background:#EEF1F4;border:1px solid #C3CCD5;color:#7D8B98}.tile.x .nm{text-decoration:line-through}
.tile.p{background:#fff;border:2px dotted #8795A3;color:var(--ink)}.tile.p .nt{color:var(--mute)}
.tags{display:flex;gap:4px;flex-wrap:wrap;min-height:0}
.tag{font-size:9.5px;font-weight:700;letter-spacing:.4px;border-radius:4px;padding:1px 5px;margin-bottom:3px}
.tile.s .tag{background:rgba(255,255,255,.18);color:#fff}
.tag.new{background:#E3ECF8;color:#1E4E8C}.tag.acq{background:#FBEBDD;color:#9A4E12}.tag.ren{background:#ECE6F6;color:#5B3E8E}
.tag.cloud{background:#E7F0EC;color:#245C46}.tag.pat{background:#EEF1F4;color:#4C5B69}
.tile.s .tag.cloud,.tile.s .tag.new,.tile.s .tag.acq,.tile.s .tag.ren{background:rgba(255,255,255,.2);color:#fff}
.eval{background:#F3F0FA;border:2px solid #5B4B9A}
.eval .sh .t1{color:#3F3378}
.plane{background:var(--bg);border:1px solid var(--line);border-radius:16px;padding:12px 16px 6px;margin-bottom:14px}
.ph{font-size:20px;font-weight:800;color:var(--navy);text-transform:uppercase;letter-spacing:.5px;margin:2px 0 10px}
.row{display:grid;grid-template-columns:300px 1fr;gap:14px;padding:10px 0;border-top:1px solid var(--line)}
.ph + .row{border-top:0}
.lab .code{display:inline-block;background:var(--navy);color:#fff;font-weight:800;border-radius:6px;padding:2px 8px;font-size:14px}
.lab .ln{font-size:19px;font-weight:800;color:var(--navy);margin-top:5px;line-height:1.15}
.lab .was{font-size:12.5px;color:var(--mute);margin-top:3px;font-style:italic}
.lab .duty{font-size:13px;color:var(--teal);font-weight:600;margin-top:5px}
.lab .fix{font-size:12px;color:var(--ink);margin-top:6px;line-height:1.3;border-left:3px solid var(--amber);padding-left:7px}
.eval .row{border-top:0;padding:0}
.foot{display:grid;grid-template-columns:1.25fr 1fr;gap:14px;margin-top:4px}
.box{border:1px solid var(--line);border-radius:12px;padding:12px 16px;font-size:13.5px;line-height:1.45;background:#fff}
.box h3{margin:0 0 6px;font-size:16px;color:var(--navy)}
.box ul{margin:0;padding-left:18px}
.small{font-size:12px;color:var(--mute);margin-top:12px}
</style></head><body><div class="wrap">
<h1>The Enterprise GenAI Stack — corrected and extended</h1>
<div class="sub">The “Full AI Stack Explained” graphic, re-researched for a regulated UK/EU asset manager · as of 9 October 2026</div>
<div class="stats"><span class="stat"><b>9</b> layers re-drawn</span><span class="stat"><b>+8</b> enterprise controls</span>
<span class="stat"><b>140</b> products assessed</span><span class="stat"><b>39 of 80</b> original tiles out of date</span>
<span class="stat"><b>1,255</b> sources</span><span class="stat"><b>%(S)d</b> Strategic · <b>%(T)d</b> Tactical · <b>%(E)d</b> Experimental</span></div>
<div class="legend"><span><span class="sw s"></span>Strategic (most are conditional)</span><span><span class="sw t"></span>Tactical (a stated niche or estate)</span>
<span><span class="sw e"></span>Experimental (pilot only)</span><span><span class="sw x"></span>Removed (unverifiable)</span>
<span><span class="tag new">NEW</span> not in the original</span><span><span class="tag acq">ACQUIRED</span> owner changed 2025–26</span>
<span><span class="tag ren">RENAMED</span></span><span><span class="tag cloud">AWS</span> Strategic only where that cloud is primary</span></div>

<div class="sec ctrl"><div class="sh"><span class="t1">Control plane — missing from the original</span><span class="t2">firm-owned policy and one evidence store, around every call</span></div>
<div class="cards">%(CARDS)s</div></div>

<div class="sec eval"><div class="sh"><span class="t1">Evaluation &amp; observability plane</span><span class="t2">L9 joins C8 as one evidence plane with two owners</span></div>%(L9)s</div>

%(PLANES)s

<div class="foot"><div class="box"><h3>What changed since the original graphic</h3><ul>
<li><b>39 of 80 tiles</b> were out of date: 9 acquired, 9 mispositioned, 8 renamed, 8 wrong version, 6 not verifiable, 4 duplicated, 3 superseded, 2 deprecated (some tiles carry several).</li>
<li><b>Missing entirely:</b> the control plane (C1–C8), durable execution, tool governance, and the hyperscaler agent stacks.</li>
<li><b>Re-drawn:</b> L2 split and routing moved to the gateway; workflows separated from agents; memory merged into the stores; embeddings and reranking merged; evaluation moved from the bottom of the stack to a plane beside the controls.</li>
<li><b>Ownership moved:</b> Dynatrace–Arize, ClickHouse–Langfuse, OpenAI–Promptfoo (announced), MongoDB–Voyage, Elastic–Jina, Nebius–Tavily, Stripe–OpenRouter (pending), SpaceX–xAI.</li></ul></div>
<div class="box"><h3>How to read it</h3><ul>
<li>Tiers are for a regulated asset manager, scored on one rubric with regulated-FS weights. A Strategic tier carries a condition; the condition is the decision.</li>
<li>Build order: control and evidence plane first, then models through the gateway, retrieval, workflows, tools — memory last.</li>
<li>Disclosure: researched and drafted with an Anthropic model. Anthropic items were scored on the same rubric; their tiers were set by the reader, and an independent alternative is named for each.</li>
<li>Personal research, not any firm’s platform. Every tile is backed by sourced facts in the dataset and the product appendix.</li></ul></div></div>
<div class="small">Source: Enterprise GenAI Full-Stack Architecture review, October 2026 — 05_Data/products.json (tiers and flags), bibliography.xlsx (sources). Original graphic: “The Full AI Stack Explained” (October 2026). Product names are trademarks of their owners; no logos used.</div>
</div></body></html>""" % {"S": counts["Strategic"], "T": counts["Tactical"], "E": counts["Experimental"], "CARDS": cards,
                           "L9": layer_row("L9"), "PLANES": planes}
os.makedirs("work/stageD", exist_ok=True)
open("work/stageD/stack_graphic.html", "w", encoding="utf-8").write(page)
print("tiles", len(prods), "counts", counts)
