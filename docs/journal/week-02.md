# Week 2 — From Proof of Concept to Structured Agent 🤖

## 🎯 Summary

This week transformed SRE Copilot from a proof of concept into a structured AI agent.

---

## 💻 What I Built

- An interactive command-line interface for SRE Copilot.
- Improved exception handling for a more reliable user experience.
- A clearer separation between the agent's identity in `prompts.py` and its domain expertise in `skills.md`.

---

## 🐍 Python and LangChain Concepts Used

- Shared application state with `global`.
- LangChain event streaming with `astream_events()`.
- LangSmith for observing LangChain orchestration.

---

## 🧠 What I Learned

I learned how shared application state works with `global`, and how to observe LangChain's orchestration using `astream_events()` and LangSmith.

Separating the agent's identity in `prompts.py` from its domain expertise in `skills.md` showed how prompt engineering can change reasoning behavior without changing business logic.

By improving tool descriptions, prompts, and skills, the agent progressed from describing symptoms to correlating evidence and recommending next actions.

---
