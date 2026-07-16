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

@mcp.tool()
def get_pods():
  """Return mocked Kubernetes cluster information."""
  return [
        {
            "name": "checkout",
            "status": "Running"
        },
        {
            "name": "payment",
            "status": "CrashLoopBackOff"
        }
    ]

if __name__ == "__main__":
  mcp.run(
    transport="streamable-http"
  )