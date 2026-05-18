import subprocess

from smolagents import tool


@tool
def run_shell_command(command: str) -> str:
    """
    Executes a restricted shell command safely.

    Args:
        command: Shell command to execute.

    Returns:
        Standard output and standard error from the command execution.
    """

    allowed = [
        "ls",
        "pwd",
        "whoami",
        "df",
        "free",
        "ps"
    ]

    if command.split()[0] not in allowed:
        return "Command not allowed."

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    return f"""
STDOUT:
{result.stdout}

STDERR:
{result.stderr}
"""


@tool
def docker_ps() -> str:
    """
    Lists currently running Docker containers.

    Args:
        None

    Returns:
        Output of the 'docker ps' command.
    """

    result = subprocess.run(
        ["docker", "ps"],
        capture_output=True,
        text=True
    )

    return result.stdout


@tool
def kubectl_get_pods() -> str:
    """
    Lists Kubernetes pods in the current namespace.

    Args:
        None

    Returns:
        Output of the 'kubectl get pods' command.
    """

    result = subprocess.run(
        ["kubectl", "get", "pods"],
        capture_output=True,
        text=True
    )

    return result.stdout