from abc import ABC, abstractmethod
from llm_interfaces.BaseLLMInterface import BaseLLMInterface

class BaseAgent(ABC):

    def __init__(self, llm_interface: BaseLLMInterface, tools: []) -> None:
        self.llm_interface = llm_interface
        self.tools = tools

    # Function for agent to handle tool calls
    @abstractmethod
    def handle_tool_call():
        pass
    
    # Function for agent to respond to message
    @abstractmethod
    def agent_callback():
        pass