from app.agents.coding_agent import coding_agent
from app.agents.file_agent import file_agent

# -----------------------------------------------------------------------
# Add more agents here as you build them, e.g.:
#   from app.agents.research_agent import research_agent
# -----------------------------------------------------------------------

CODING_KEYWORDS = [
    "code", "bug", "python", "fix", "implement", "write", "create file",
    "script", "function", "class", "debug", "error", "syntax", "module",
    "agent", "tool", "scaffold", "generate",
]

FILE_KEYWORDS = [
    "file", "csv", "pdf", "document", "read", "folder", "directory",
    "list files", "rename", "move", "copy",
]


class MasterAgent:
    """
    Routes user requests to the appropriate specialised agent.

    Routing priority (first match wins):
        1. coding_agent  — code, bugs, file generation, scaffolding
        2. file_agent    — file/document operations
        3. coding_agent  — default fallback (most capable for unknown tasks)
    """

    def route(self, user_request: str):
        request = user_request.lower()

        if any(kw in request for kw in CODING_KEYWORDS):
            return coding_agent

        if any(kw in request for kw in FILE_KEYWORDS):
            return file_agent

        # Default fallback — coding agent is the most capable
        return coding_agent

    def run(self, user_request: str) -> str:
        selected_agent = self.route(user_request)
        print(f"\n[MasterAgent] Routing to: {selected_agent.name}\n")

        try:
            result = selected_agent.run(user_request)
            return result
        except Exception as e:
            return f"[MasterAgent] Agent '{selected_agent.name}' raised an error:\n{e}"
