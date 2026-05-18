import os

from smolagents import CodeAgent, LiteLLMModel

from app.tools.code_tools import (
    read_text_file,
    write_text_file,
    list_files,
    file_exists,
    get_current_directory,
)

# -----------------------------------------------------------------------
# FILE AGENT
# Handles file-focused tasks: reading CSVs, PDFs, documents, renaming,
# moving, or summarising files.
#
# TODO (use coding_agent to build this out):
#   - Add tools/file_tools.py with CSV reader, PDF reader, etc.
#   - Replace the placeholder tools below with those specialised tools.
# -----------------------------------------------------------------------

groq_token = os.getenv("GROQ_API_KEY")

model = LiteLLMModel(
    model_id="groq/llama-3.3-70b-versatile",
    api_key=groq_token,
)

file_agent = CodeAgent(
    tools=[
        read_text_file,
        write_text_file,
        list_files,
        file_exists,
        get_current_directory,
    ],
    model=model,
    max_steps=10,
    name="file_agent",
    description=(
        "Handles file-related tasks: reading, summarising, and writing files. "
        "Supports text, CSV, and basic document operations."
    ),
)
