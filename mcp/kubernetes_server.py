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
  """
Returns all Kubernetes pods with their namespace, node, status, restart count, and labels.

Use this tool when investigating workload health,
CrashLoopBackOff, service failures, or pod-level issues.
  """
  return [
        {
        "name": "checkout",
        "namespace": "default",
        "node": "worker-node-1",
        "status": "Running",
        "restarts": 0
        },
        {
        "name": "payment",
        "namespace": "payments",
        "node": "worker-node-3",
        "status": "CrashLoopBackOff",
        "restarts": 12
        },
        {
        "name": "inventory",
        "namespace": "default",
        "node": "worker-node-2",
        "status": "Running",
        "restarts": 1
        }
    ]

@mcp.tool()
def get_nodes():
  """
Returns all Kubernetes nodes with readiness, CPU usage, memory usage, and version.

Use this tool when investigating whether node health
may be causing pod or service failures.
  """

  return [
        {
            "name": "worker-node-1",
            "status": "Ready",
            "cpu_usage": "42%",
            "memory_usage": "58%",
            "k8s_version": "v1.31.2"
        },
        {
            "name": "worker-node-2",
            "status": "Ready",
            "cpu_usage": "73%",
            "memory_usage": "81%",
            "k8s_version": "v1.31.2"
        },
        {
            "name": "worker-node-3",
            "status": "NotReady",
            "cpu_usage": "0%",
            "memory_usage": "0%",
            "k8s_version": "v1.31.2"
        }
    ]

@mcp.tool()
def get_events():
  """
Returns recent Kubernetes events.

Use this tool when diagnosing why a service, pod,
deployment, or node is failing.
  """

  return [
        {
            "type": "Warning",
            "reason": "BackOff",
            "object": "payment-76f98c9d6b-x2msl",
            "message": "Back-off restarting failed container",
            "age": "2m"
        },
        {
            "type": "Warning",
            "reason": "NodeNotReady",
            "object": "worker-node-3",
            "message": "Node worker-node-3 is not ready",
            "age": "5m"
        },
        {
            "type": "Normal",
            "reason": "ScalingReplicaSet",
            "object": "checkout",
            "message": "Scaled replica set from 2 to 3",
            "age": "12m"
        },
        {
            "type": "Normal",
            "reason": "Pulled",
            "object": "inventory",
            "message": "Successfully pulled container image",
            "age": "20m"
        }
    ]

@mcp.tool()
def get_namespaces():
  """
  Returns all Kubernetes namespaces and their current status.
  Use this tool to determine which namespaces exist,whether a namespace is active,
  and to understand where workloads are deployed.
  """

  return [
        {
            "name": "default",
            "status": "Active"
        },
        {
            "name": "kube-system",
            "status": "Active"
        },
        {
            "name": "monitoring",
            "status": "Active"
        },
        {
            "name": "payments",
            "status": "Active"
        },
        {
            "name": "dev",
            "status": "Active"
        }
    ]

if __name__ == "__main__":
  mcp.run(
    transport="streamable-http"
  )