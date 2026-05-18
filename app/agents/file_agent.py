from smolagents import ToolCallingAgent
from smolagents import CodeAgent,LiteLLMModel
import os
groq_token = os.getenv("GROQ_API_KEY")
model = LiteLLMModel( model_id="groq/llama-3.3-70b-versatile", api_key=groq_token)


from app.tools.file_tools import (
    read_text_file,
    write_text_file,
    list_files,
    delete_file
)

file_agent = ToolCallingAgent(
    tools=[
        read_text_file,
        write_text_file,
        list_files,
        delete_file
    ],
    model=model,
    max_steps=5,
    name="file_agent",
    description="Handles file operations"
)