from tools.PushoverService import PushoverService
from context_extractors.Extractors import extract_data

if __name__ == "__main__":

    # Get the services
    svc = PushoverService()

    # Extract the content
    linkedin_profile = extract_data("context_information/Profile.pdf", "pdf")
    summary = extract_data("context_information/summary.txt", ".txt")


    svc.tools["record_contact_requested"]["function"]("testing")