# Kubernetes Incident Investigation

When investigating an unhealthy workload:

1. Check pods.
2. If pods are unhealthy, inspect events.
3. If events suggest node issues, inspect nodes.
4. Correlate the evidence.
5. Summarize the likely root cause.
6. Suggest the next action.

When summarizing an unhealthy workload, use this response format:

- Symptom
- Likely root cause
- Evidence
- Next action

Keep the response practical and SRE-focused.
Use the tools to support the conclusion.
If the cause is not fully proven, say so clearly.