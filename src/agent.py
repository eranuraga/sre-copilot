"""
SRE Copilot Agent

This file will become the entry point
for our AI Agent.
"""

import asyncio
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = "http://127.0.0.1:8000/mcp"

async def main():
    #1 Create the model
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
        )
    
    #2 Connect to MCP Servers and Get Tools as Langchain Tools
    mcp_client = MultiServerMCPClient(
        {
            "kubernetes": {
                "transport": "streamable_http",
                "url": MCP_SERVER_URL,
            }
        }
    )
    tools = await mcp_client.get_tools()

    #3 Create the agent
    agent = create_agent(model, tools)

    #4 Ask a question 
    result = await agent.ainvoke(
        {
            "messages": 
            [{"role": "user",
              "content": "Which Cluster I'm connected to ?"
              }]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())


