# Day 4 — Our First AI Agent! 🚀

## 🎯 Goal

Build the first version of SRE Copilot using LangChain, Gemini, and my existing FastMCP server.

---

## 🐍 Python Concepts Used

- Modules (`agent.py`, `mcp_client.py`)
- Async functions
- Imports
- Function calls
- Objects and classes (`ListToolsResult`, `AIMessage`)

---

## 🤖 AI Concepts Learned

### 1. AI Agent Architecture

```text
User
   │
   ▼
LangChain Agent
   │
   ▼
Gemini LLM
   │
   ▼
MCP Client
   │
   ▼
FastMCP Server
   │
   ▼
Tool
```

### 2. Where Tools Come From

I learned that tools are written by developers and registered with the MCP server using decorators like:

```python
@mcp.tool()
```

The MCP client discovers these tools using:

```python
session.list_tools()
```

LangChain then receives those discovered tools and makes them available to the LLM.

### 3. Tool Selection

The LLM does not use hardcoded `if` statements. Instead, it receives tool metadata:

- Tool name
- Description
- Input schema

It compares the meaning of the user's question with the tool descriptions and chooses the best matching tool.

Example:

```text
User:
Is my cluster healthy?

LLM selects:
get_cluster_health()
```

This is because its description best matches the user's intent.

### 4. Importance of Docstrings

I realized that docstrings are not only documentation for developers. They also become instructions that help the LLM decide when to use a tool.

Better docstrings lead to better tool selection.

### 5. Separation of Responsibilities

I learned why the project should have separate modules.

`agent.py` is responsible for:

- LangChain
- Gemini
- User interaction

`mcp_client.py` is responsible for:

- Connecting to MCP
- Listing tools
- Calling tools

Each module has a single responsibility.

---

## 💻 Code Written

Created the first AI agent.

```python
agent = create_agent(
    model=model,
    tools=tools
)
```

Successfully asked:

```text
Which cluster am I connected to?
```

The agent automatically selected the correct MCP tool and produced a natural language response.

---

## 💡 Biggest Learning

An AI Agent is not magic.

- The LLM is given a list of available tools together with their descriptions.
- It reasons about which tool best matches the user's request.
- LangChain orchestrates the tool execution.
- The tool returns structured data.
- The LLM converts that structured data into a natural language response.

---

## 🚀 Production Engineering Notes

Today's architecture is:

```text
User
   │
   ▼
LangChain Agent
   │
   ▼
Gemini
   │
   ▼
MCP Client
   │
   ▼
FastMCP Server
   │
   ▼
Tool
```

This architecture can later be extended with:

- Kubernetes API
- Prometheus
- Grafana
- OCI APIs
- ServiceNow
- GitHub

without changing how the agent itself works.
