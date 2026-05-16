from app_agents.ChatAgent import ChatAgent
from tools.PushoverService import PushoverService
from context_extractors.Extractors import extract_data
from data_types.context_info import ContextInformation

if __name__ == "__main__":

    # Get the services
    svc = PushoverService()

    # Extract the content
    linkedin_profile = extract_data("context_information/Profile.pdf", ".pdf")
    summary = extract_data("context_information/summary.txt", ".txt")
    resume = extract_data("context_information/Dylan_Perera_Resume.pdf", ".pdf")

    context_info = ContextInformation(name="Dylan Perera", summary=summary, linkedin=linkedin_profile, resume=resume)


    agent = ChatAgent(tools=svc.tools, tool_descriptions=svc.get_tools_description(), context_info=context_info)

    agent.agent_callback(message="what is your brothers name?", history=[])

   

    # Gradio chat - call back will be a function defined by agent
