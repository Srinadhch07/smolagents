import os

from smolagents import tool


@tool
def read_text_file(filepath: str) -> str:
    """
    Reads the contents of a text file.

    Args:
        filepath: Path to the text file to read.

    Returns:
        Contents of the text file as a string.
    """

    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


@tool
def write_text_file(filepath: str, content: str) -> str:
    """
    Writes content into a text file.

    Args:
        filepath: Path to the file to create or overwrite.
        content: Text content to write into the file.

    Returns:
        Success message indicating the file was saved.
    """

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Saved to {filepath}"


@tool
def list_files(directory: str = ".") -> str:
    """
    Lists files inside a directory.

    Args:
        directory: Path of the directory to scan.

    Returns:
        Newline-separated list of files and folders.
    """

    return "\n".join(os.listdir(directory))


@tool
def delete_file(filepath: str) -> str:
    """
    Deletes a file from the filesystem.

    Args:
        filepath: Path of the file to delete.

    Returns:
        Success message indicating the file was deleted.
    """

    os.remove(filepath)

    return f"{filepath} deleted."