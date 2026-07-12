# Day 1

## Goal

- Setup development environment
- Connect to Gemini
- Verify first LLM call

---

## Python Topics

- Variables
- Virtual Environment
- f-strings

---

## Tools Installed

```bash
python3 -m venv .venv

pip install langchain
pip install langgraph
pip install langchain-google-genai
pip install mcp
pip install python-dotenv
pip install requests
pip install pytest
```

---

## Code

client = genai.Client(...)

---

## What I Learned
LangChain is just an orchestration framework.
Gemini SDK is different from LangChain.
Environment variables should never be committed.

---