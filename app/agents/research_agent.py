from smolagents import ToolCallingAgent
from smolagents import CodeAgent,LiteLLMModel
import os
groq_token = os.getenv("GROQ_API_KEY")
model = LiteLLMModel( model_id="groq/llama-3.3-70b-versatile", api_key=groq_token)

research_agent = ToolCallingAgent(
    tools=[
        web_search_tool,
        summarize_tool
    ],
    model=model,
    max_steps=5,
    name="research_agent",
    description="Handles web research and summarization"
)