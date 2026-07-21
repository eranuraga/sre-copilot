# Day 5 — Making SRE Copilot Interactive 💬

## 🎯 Goal

Create an interactive command-line interface for SRE Copilot and learn how to safely read the final answer returned by Gemini.

---

## 🐍 Python Concepts Used

- `async` and `await`
- `asyncio.run()`
- Infinite loops with `while True`
- Importing functions from another file
- Global variables
- Lists and dictionaries
- Error handling with `RuntimeError`

---

## 💻 What I Built

I created a CLI loop where a user can ask multiple questions without restarting the application.

```python
async def main():
    await create_sre_agent()

    while True:
        question = input("SRE Copilot > ")
        response = await ask_agent(question)
        print(response)
```

The agent is initialized once at startup:

```python
await create_sre_agent()
```

Then each user question is sent to Gemini:

```python
response = await ask_agent(question)
```

---

## 🤖 Understanding Gemini Responses

Gemini does not always return only a simple string.

Sometimes the final message content looks like this:

```python
[
    {
        "type": "text",
        "text": "The payments pod is in CrashLoopBackOff.",
        "extras": {
            "signature": "..."
        }
    }
]
```

The `extras` field is Gemini metadata. It is not part of the user-facing answer.

To return only the readable answer:

```python
content = result["messages"][-1].content

if isinstance(content, str):
    return content

return content[0]["text"]
```

---

## 🧠 Important Learning

The final response passes through several layers:

```text
User Question
   │
   ▼
main.py
   │
   ▼
ask_agent()
   │
   ▼
LangChain Agent
   │
   ▼
Gemini Response
   │
   ▼
Extract only the text
   │
   ▼
Print answer in terminal
```

LangChain returns the complete message object, including metadata. My application should extract and print only the `text` field.

---

## ⚠️ Debugging Lesson

When debugging, printing this:

```python
print(content)
```

shows the entire Gemini response, including `extras`.

For the final application, print only:

```python
print(response)
```

where `response` is the text returned by `ask_agent()`.
