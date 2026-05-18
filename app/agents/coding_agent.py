
from smolagents import CodeAgent,LiteLLMModel
import os
groq_token = os.getenv("GROQ_API_KEY")
model = LiteLLMModel( model_id="groq/llama-3.3-70b-versatile", api_key=groq_token)
from app.tools.code_tools import (
        create_directory,
        write_text_file,
        append_text_file,
        read_text_file,
        delete_file,
        list_files,
        file_exists,
        search_in_files,
        run_python_file,
        validate_python_syntax,
        run_shell_command
)
groq_token = os.getenv("GROQ_API_KEY")

coding_agent = CodeAgent(
    tools=[
        create_directory,
        write_text_file,
        append_text_file,
        read_text_file,
        delete_file,
        list_files,
        file_exists,
        search_in_files,
        run_python_file,
        validate_python_syntax,
        run_shell_command
    ],
    model=model,
    max_steps=5,
    name="coding_agent",
    description="Handles coding, debugging, and software tasks"
)