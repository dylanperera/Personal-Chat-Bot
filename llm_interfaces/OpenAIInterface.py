from openai.types.responses import Response
from llm_interfaces.BaseLLMInterface import BaseLLMInterface
from openai import OpenAI
from dotenv import load_dotenv
import os

class OpenAIInterface(BaseLLMInterface):

    def __init__(self, model, tools) -> None:
        load_dotenv()
        super().__init__("", os.getenv("OPENAI_API_KEY"), model, tools)
        self.openai = OpenAI(api_key=self.token)

    def get_ai_response(self, messages) -> Response:
        return self.openai.responses.create(input=messages, model=self.model, tools=self.tools)