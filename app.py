from app_agents.ChatAgent import ChatAgent
from tools.PushoverService import PushoverService
from context_extractors.Extractors import extract_data
from data_types.context_info import ContextInformation
import gradio as gr

if __name__ == "__main__":

    # Get the services
    svc = PushoverService()

    # Extract the content
    linkedin_profile = extract_data("context_information/Profile.pdf", ".pdf")
    summary = extract_data("context_information/summary.txt", ".txt")
    resume = extract_data("context_information/Dylan_Perera_Resume.pdf", ".pdf")

    context_info = ContextInformation(name="Dylan Perera", summary=summary, linkedin=linkedin_profile, resume=resume)


    agent = ChatAgent(tools=svc.tools, tool_descriptions=svc.get_tools_description(), context_info=context_info)

    #print(agent.agent_callback(message="can you tell me about yourself?", history=[]))

   

    # Gradio chat - call back will be a function defined by agent
    gr.ChatInterface(agent.agent_callback, type="messages").launch()