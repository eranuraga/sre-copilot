from mcp.server.fastmcp import FastMCP
mcp = FastMCP("kubernetes-mock")

@mcp.tool()
def get_cluster_info() -> dict:
  """Return mocked Kubernetes cluster information."""
  return {
    "cluster_name": "dev-cluster",
    "region": "us-ashburn-1",
    "status": "healthy",
    "nodes": 3
  }

if __name__ == "__main__":
  mcp.run(
    transport="streamable-http"
  )