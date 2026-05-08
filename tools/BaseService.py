from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os

class BaseService(ABC):

    def __init__(self, url, token, user) -> None:
        load_dotenv()
        self.url = url
        self.token = os.getenv(token)
        self.user = os.getenv(user)
        self.tools = {}

    def tool_decorator(self, tool_description, func):
        if func.__name__ not in self.tools:
            self.tools[func.__name__] = {"function": func, "description": tool_description}


    