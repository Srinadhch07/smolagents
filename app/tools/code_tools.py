import os
import subprocess

from smolagents import tool


@tool
def directory_exists(path: str) -> str:
    """
    Checks whether directory exists.

    Args:
        path: Directory path.

    Returns:
        True or False.
    """
    return str(os.path.isdir(path))


@tool
def list_files_recursive(directory: str = ".") -> str:
    """
    Lists files recursively, ignoring .git, .venv, __pycache__.

    Args:
        directory: Directory to scan.

    Returns:
        Newline-separated file list.
    """
    ignored = {".git", ".venv", "__pycache__"}
    collected = []

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignored]
        for file in files:
            collected.append(os.path.join(root, file))

    return "\n".join(collected) if collected else "No files found."


@tool
def get_current_directory() -> str:
    """
    Returns current working directory.

    Args:
        None

    Returns:
        Current working directory path.
    """
    return os.getcwd()


@tool
def create_directory(path: str) -> str:
    """
    Creates a directory recursively if it does not exist.

    Args:
        path: Directory path to create.

    Returns:
        Success message.
    """
    os.makedirs(path, exist_ok=True)
    return f"Directory '{path}' created successfully."


@tool
def write_text_file(filepath: str, content: str) -> str:
    """
    Writes content into a text file, creating parent directories if needed.

    Args:
        filepath: Path of the file to create or overwrite.
        content: Text content to write into the file.

    Returns:
        Success message.
    """
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return f"File '{filepath}' written successfully."


@tool
def append_text_file(filepath: str, content: str) -> str:
    """
    Appends content into a text file, creating parent directories if needed.

    Args:
        filepath: File path to append content into.
        content: Content to append.

    Returns:
        Success message.
    """
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(content)

    return f"Content appended to '{filepath}'."


@tool
def read_text_file(filepath: str) -> str:
    """
    Reads a text file and returns its contents.

    Args:
        filepath: File path to read.

    Returns:
        File contents as string.
    """
    if not os.path.exists(filepath):
        return f"Error: File '{filepath}' does not exist."

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


@tool
def delete_file(filepath: str) -> str:
    """
    Deletes a file.

    Args:
        filepath: File path to delete.

    Returns:
        Success message.
    """
    if not os.path.exists(filepath):
        return f"Error: File '{filepath}' does not exist."

    os.remove(filepath)
    return f"File '{filepath}' deleted successfully."


@tool
def list_files(directory: str = ".") -> str:
    """
    Lists all files recursively in a directory.

    Args:
        directory: Root directory to scan.

    Returns:
        Newline-separated file list.
    """
    if not os.path.isdir(directory):
        return f"Error: Directory '{directory}' does not exist."

    collected = []
    for root, _, files in os.walk(directory):
        for file in files:
            collected.append(os.path.join(root, file))

    return "\n".join(collected) if collected else "No files found."


@tool
def file_exists(filepath: str) -> str:
    """
    Checks whether a file exists.

    Args:
        filepath: File path to check.

    Returns:
        'True' or 'False'.
    """
    return str(os.path.exists(filepath))


@tool
def search_in_files(directory: str, keyword: str) -> str:
    """
    Searches for a keyword inside all text files in a directory.

    Args:
        directory: Directory to search in.
        keyword: Keyword to search for (case-insensitive).

    Returns:
        Matching file paths and lines, up to 200 results.
    """
    if not os.path.isdir(directory):
        return f"Error: Directory '{directory}' does not exist."

    matches = []

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for idx, line in enumerate(f.readlines()):
                        if keyword.lower() in line.lower():
                            matches.append(f"{path}:{idx+1}: {line.strip()}")
            except Exception:
                pass

    if not matches:
        return f"No matches found for '{keyword}' in '{directory}'."

    return "\n".join(matches[:200])


@tool
def run_python_file(filepath: str) -> str:
    """
    Executes a Python file and returns stdout and stderr.

    Args:
        filepath: Python file path to execute.

    Returns:
        STDOUT and STDERR combined output.
    """
    if not os.path.exists(filepath):
        return f"Error: File '{filepath}' does not exist."

    result = subprocess.run(
        ["python", filepath],
        capture_output=True,
        text=True,
        timeout=60
    )

    return f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"


@tool
def validate_python_syntax(filepath: str) -> str:
    """
    Validates Python syntax of a file without executing it.

    Args:
        filepath: Python file path to validate.

    Returns:
        'Syntax valid.' or error details.
    """
    if not os.path.exists(filepath):
        return f"Error: File '{filepath}' does not exist."

    result = subprocess.run(
        ["python", "-m", "py_compile", filepath],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return "Syntax valid."

    return f"Syntax error:\n{result.stderr}"


@tool
def run_shell_command(command: str) -> str:
    """
    Runs a safe, read-only shell command from an allowlist.

    Args:
        command: Shell command to execute. Allowed: ls, pwd, whoami, tree, cat, echo, find, head, tail, wc.

    Returns:
        Command STDOUT and STDERR, or an error if command is not allowed.
    """
    allowed = ["ls", "pwd", "whoami", "tree", "cat", "echo", "find", "head", "tail", "wc"]
    first = command.strip().split()[0]

    if first not in allowed:
        return f"Command '{first}' not allowed. Allowed commands: {', '.join(allowed)}"

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        timeout=30
    )

    return f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
