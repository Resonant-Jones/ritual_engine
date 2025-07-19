from rowboat.agents import FunctionCallingAgent
from rowboat.runner import ToolRunner
from rowboat.tool_protocol import tool
import requests

@tool
def trigger_ritual(name: str) -> str:
    """Call a ritual by name using the Ritual Engine."""
    res = requests.post("http://localhost:8000/rituals/trigger", json={"name": name})
    return res.json().get("result", "No response.")

agent = FunctionCallingAgent(
    name="ThreadspaceAgent",
    description="An agent who can trigger rituals and work with memory.",
    tools=[trigger_ritual],
    model="gpt-4"  # or 'ollama/llama3' if local
)

runner = ToolRunner(agent)

if __name__ == "__main__":
    query = "Please activate the midnight mirror ritual."
    result = runner.run(query)
    print(result)
