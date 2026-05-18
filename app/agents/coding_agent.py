import os

from smolagents import CodeAgent, LiteLLMModel

from app.tools.code_tools import (
    create_directory,
    write_text_file,
    append_text_file,
    read_text_file,
    delete_file,
    list_files,
    list_files_recursive,
    file_exists,
    directory_exists,
    search_in_files,
    run_python_file,
    validate_python_syntax,
    run_shell_command,
    get_current_directory,
)

groq_token = os.getenv("GROQ_API_KEY")

model = LiteLLMModel(
    model_id="groq/llama-3.3-70b-versatile",
    api_key=groq_token,
)

coding_agent = CodeAgent(
    tools=[
        create_directory,
        write_text_file,
        append_text_file,
        read_text_file,
        delete_file,
        list_files,
        list_files_recursive,
        file_exists,
        directory_exists,
        search_in_files,
        run_python_file,
        validate_python_syntax,
        run_shell_command,
        get_current_directory,
    ],
    model=model,
    max_steps=15,
    name="coding_agent",
    description=(
        "Handles all coding tasks: writing, reading, editing, and running Python files. "
        "Can create directories, search in files, validate syntax, and scaffold new agents or tools."
    ),
)
