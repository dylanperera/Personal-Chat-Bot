from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os

class BaseService(ABC):

    def __init__(self, url, token_env_var, user_env_var) -> None:
        load_dotenv()
        self.url = url
        self.token_env_var = token_env_var
        self.user_env_var = user_env_var
        self.token = os.getenv(token_env_var)
        self.user = os.getenv(user_env_var)
        self.tools = {}

    def register_tool(self, tool_description, func):
        if func.__name__ not in self.tools:
            self.tools[func.__name__] = {"function": func, "description": tool_description}

    def get_tools_description(self):
        tool_descriptions = []
        for tool in self.tools.values():
            tool_descriptions.append(tool["description"])

        return tool_descriptions
    