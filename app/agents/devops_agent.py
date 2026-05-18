from smolagents import LiteLLMModel
from smolagents import ToolCallingAgent
import os
groq_token = os.getenv("GROQ_API_KEY")
model = LiteLLMModel( model_id="groq/llama-3.3-70b-versatile", api_key=groq_token)

from tools.devops_tools import (
    run_shell_command,
    docker_ps,
    kubectl_get_pods
)

devops_agent = ToolCallingAgent(
    tools=[
        run_shell_command,
        docker_ps,
        kubectl_get_pods
    ],
    model=model,
    max_steps=5,
    name="devops_agent",
    description="Handles infrastructure operations"
)