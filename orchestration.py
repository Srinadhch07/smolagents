# master_agent.py

from app.agents.coding_agent import coding_agent
# from app.agents.research_agent import research_agent
from app.agents.file_agent import file_agent

class MasterAgent:

    def route(self, user_request: str):

        request = user_request.lower()

        if any(x in request for x in [
            "code",
            "bug",
            "python",
            "fix",
            "implement"
        ]):
            return coding_agent

        # elif any(x in request for x in [
        #     "research",
        #     "search",
        #     "find",
        #     "summarize"
        # ]):
        #     return research_agent

        elif any(x in request for x in [
            "file",
            "csv",
            "pdf",
            "document"
        ]):
            return file_agent

        # else:
        #     return research_agent

    def run(self, user_request: str):

        selected_agent = self.route(user_request)

        print(f"Selected agent: {selected_agent.name}")

        result = selected_agent.run(user_request)

        return result