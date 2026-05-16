from typing import Any
from openai.types.responses import Response, ResponseFunctionToolCall, ResponseOutputItem
from app_agents.BaseAgent import BaseAgent
from data_types.context_info import ContextInformation
from llm_interfaces.OpenAIInterface import OpenAIInterface
import json


class ChatAgent(BaseAgent):
    
    def __init__(self, tools: [], tool_descriptions: [], context_info: ContextInformation) -> None:

        open_ai = OpenAIInterface(model="gpt-4o-mini", tool_descriptions=tool_descriptions)

        super().__init__(llm_interface=open_ai, tools=tools)

        self.system_prompt =f"""
        # Identity:\
            You are a chat bot on a website about me, so you will will act like me. You are now {context_info.name}.\
            You will communicate in a professional tone, answering questions about me related to my education (such as my major, courses, and projects), experiences (both research and jobs), skills, projects, and hobbies.\
            Your responsibility is to represent {context_info.name} for interactions on the website as faithfully as possible. \
                
        # Instructions:\
            You will process the message/question entered by the user using only information provided which will include linkedin profile, resume, and summary of me. This information is provided in the context section below.\
            You should respond in a professional-tone, soft-spoken, and be engaging in order to fully represent {context_info.name}.\
            Treat every conversation as if you are taking to a potential client or future employer who came across the website.\
            Do not respond aggresively or say anything in-appropriate.\
            Only respond to questions about me.\
            If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and if they'd like their name and any notes, then record it using your record_contact_requested tool.\
            If the user asks a question and you don't know the response to it, use your record_unknown_response tool to record the message the user had sent, even if it's about something trivial or unrelated to career.\

        # Context:
            ## Summary:\
            {context_info.summary}\
            ## Linkedin:\
            {context_info.linkedin}\
            ## Resume:\
            {context_info.resume}\n

        With the context and information above, please chat with the user, always staying in character as {context_info.name}.
        """

    def handle_tool_call(self, item:ResponseOutputItem):
        response: list = []

        try:
            tool_name = item.name
            tool_args = json.loads(item.arguments)
            result = self.tools[tool_name]["function"](**tool_args)
            response.append({"type": "function_call_output", "output": json.dumps(result), "call_id": item.call_id})
        except:
            response.append({"type": "function_call_output", "output": "Tool call failed", "call_id": item.call_id})
        finally:
            return response
        
    # Call back function the gradio chat will call
    def agent_callback(self, message, history) -> dict:
        history_cleaned = list(map(lambda x: {"role":x["role"], "content":x["content"]}, history))

        messages = [{"role":"system", "content": self.system_prompt}] + history_cleaned + [{"role":"user", "content":message}]

        not_done = True

        response:dict | None = None

        while not_done:
        
            llm_response: Response = self.llm_interface.get_ai_response(messages)

            for item in llm_response.output:

                if item.type == "function_call":
                    messages += llm_response.output
                    tool_call_response = self.handle_tool_call(item)
                    messages.extend(tool_call_response)
                    
                elif item.type == "message":
                    response = {"role":"assistant", "content":item.content[0].text}
                    not_done = False
    
        return response
