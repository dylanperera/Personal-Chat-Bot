from abc import ABC, abstractmethod
from fastapi.openapi.models import Response

class BaseLLMInterface(ABC):
    
    def __init__(self, url, token, model, tools) -> None:
        self.url = url
        self.token = token
        self.model = model
        self.tools = tools

    @abstractmethod
    def get_ai_response(self, messages) -> Response | str :
        pass