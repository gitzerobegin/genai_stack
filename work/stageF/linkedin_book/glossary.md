# Appendix C: Glossary

| Term | Meaning in this book |
|---|---|
| Agent | Software in which a model chooses some of its own steps or tool calls. In this book, most enterprise "agents" should be workflows with one bounded model step. |
| Agentic workflow | A fixed sequence of steps, decided in advance, in which a model performs one or more bounded steps. |
| AI gateway | The single firm-controlled point through which every model, tool and agent call passes: routing, fallback, budgets, policy and logging (control C1). |
| Attribution commentary | The written explanation of why a fund performed as it did against its benchmark, usually in terms of allocation, selection and currency effects. |
| Autonomy budget | How many decisions a model may make on its own in a given use case. The worked example's budget is one: drafting. |
| Control plane | The firm-owned controls around the stack (C1 to C8): gateway, guardrails, privacy, identity, configuration, cost, security and governance. |
| Data loss prevention (DLP) | Detecting and blocking sensitive data, such as client identifiers, before it reaches a model, a log or an outside party. |
| Deterministic check | A test written in code that gives the same answer every time, such as comparing every figure in a draft with the source system. |
| Embedding | A numerical representation of text used to find passages with similar meaning. |
| Evaluation suite | The versioned set of test cases, checks and thresholds a GenAI system must pass before release, and keep passing in production. |
| Evidence pack | The record kept for each output: prompt and model versions, data snapshot, tool calls, evaluation results, approver and timestamps, keyed to one trace ID. |
| Fallback model | A second model, preferably from a different vendor, qualified on the same evaluation suite and ready to take over. |
| Fine-tuning | Further training of a model on the firm's own data. This book treats it as "not yet" for most regulated use cases. |
| Foundation model | A large pre-trained model, hosted by a vendor or run from open weights, that the rest of the stack builds on (layer L1). |
| Guardrail | A check on what goes into or comes out of a model: deterministic rules, small classifiers or model-based judges (control C2). |
| Human in the loop | A named person who must approve an output before it takes effect. In the worked example, a portfolio manager. |
| Ingestion | Turning source documents into indexed, permissioned, traceable chunks that retrieval can use (layer L8). |
| Lock-in | The cost of leaving a vendor. Some lock-in is a good trade; lock-in over the firm's own records is not. |
| MCP | The Model Context Protocol, an open standard for connecting models to tools. Its independent alternative in this book is tools described with OpenAPI behind the same gateway. |
| Memory | Information an agent keeps between runs. This book recommends building it last, on purpose. |
| Model risk | The risk of loss from decisions based on a model that is wrong or misused, and the governance that manages it (control C8). |
| Observability | Recording what a system did, in enough detail to explain, measure and improve it, on a telemetry pipeline the firm owns (layer L9). |
| Open weights | A model whose trained parameters can be downloaded and run in the firm's own estate, under a licence. |
| Prompt injection | Hidden instructions in text a model reads, such as a retrieved document, that try to make it act against its instructions. |
| Release manifest | The versioned list of every setting that can change an output: prompts, model versions, retrieval settings, tools, guardrail policy and evaluation thresholds (control C5). |
| Reranker | A model that re-orders retrieved passages by relevance before they reach the drafting model (layer L7). |
| Retrieval | Finding the passages a model needs, from a store the firm controls, under the user's permissions (layers L6 and L7). |
| Signal | The one measure a chapter recommends tracking for its layer or control, with a starting target. |
| Trace | The linked record of every step in one run, from request to approved output. |
| Vector database | A store for embeddings. This book argues that many firms can use a database they already run instead of adding one. |
