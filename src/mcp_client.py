import asyncio
from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

load_dotenv()

MCP_SERVER_URL = "http://127.0.0.1:8000/mcp"

async def main():
    print("Connecting to MCP Server...")
    # Connect to the MCP Server
    # as is used for assigning the values returned by the function to a variable
    async with streamablehttp_client(MCP_SERVER_URL) as (read_stream, write_stream, _):
     print("Connected!")

     # Create an MCP session
     async with ClientSession(read_stream, write_stream) as session:
        # Initialize the connection 
        await session.initialize()
        print("\nSession Initialized")
        print("\nGetting list of tools...")
        tools = await session.list_tools()

        for tools in tools.tools:
           print(f"{tools.name}")
        
        print("\n Getting Cluster Info..")
        cluster_info = await session.call_tool("get_cluster_info")
        print(cluster_info.content)

        print("\n Getting Pod Info...")
        pod_info = await session.call_tool("get_pods")
        print(pod_info.content)
   

# Start the program
asyncio.run(main())
