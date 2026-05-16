from abc import ABC, abstractmethod
from fastapi.openapi.models import Response

class BaseLLMInterface(ABC):
    
    def __init__(self, url, token, model, tool_descriptions) -> None:
        self.url = url
        self.token = token
        self.model = model
        self.tool_descriptions = tool_descriptions

    @abstractmethod
    def get_ai_response(self, messages) -> Response | str :
        pass