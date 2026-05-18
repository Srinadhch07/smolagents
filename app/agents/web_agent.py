from smolagents import ToolCallingAgent
from smolagents import CodeAgent,LiteLLMModel
import os
groq_token = os.getenv("GROQ_API_KEY")
model = LiteLLMModel( model_id="groq/llama-3.3-70b-versatile", api_key=groq_token)
from app.tools.web_tools import (
    fetch_webpage,
    extract_links,
    get_status_code
)

research_agent = ToolCallingAgent(
    tools=[
        fetch_webpage,
        extract_links,
        get_status_code
    ],
    model=model,
    max_steps=5,
    name="research_agent",
    description="Handles research tasks"
)