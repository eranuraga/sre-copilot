"""
SRE Copilot Agent
"""

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT
from skills import load_skill

load_dotenv()

MCP_SERVER_URL = "http://127.0.0.1:8000/mcp"

agent = None  # We create this once, then reuse it for every question.


async def create_sre_agent():
    """Connect to the model and Kubernetes tools."""
    global agent

    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )
    print("Connected to Gemini        ✅")
    client = MultiServerMCPClient(
        {
            "kubernetes": {
                "transport": "streamable_http",
                "url": MCP_SERVER_URL,
            }
        }
    )
    print("Connected to MCP Server    ✅")
    tools = await client.get_tools()
    print(f"Loaded Tools               {len(tools)}")
    print("Type 'exit' to quit.")
    print("========================================")
    
    active_skill = load_skill("kubernetes-incident")
    system_prompt = f"""{SYSTEM_PROMPT}

    ---

    # Skill: kubernetes-incident

    {active_skill}
    """

    agent = create_agent(model, tools, system_prompt=system_prompt,)


async def ask_agent(question: str):
    """Send one question to the ready agent and return just its text."""
    if agent is None:
        raise RuntimeError("Run create_sre_agent() before asking a question.")

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    content = result["messages"][-1].content

    # Gemini may return either plain text or a list of content blocks.
    if isinstance(content, str):
        return content

    # The answer is stored here. Other fields, such as "extras", are metadata.
    return content[0]["text"]

async def watch_agent(question: str):
    input_payload = {
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    async for event in agent.astream_events(input_payload):
        print(event)
