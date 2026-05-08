import requests
from dotenv import load_dotenv
import os

class PushoverService():
    def __init__(self) -> None:
        load_dotenv()
        self.token = os.getenv("PUSHOVER_TOKEN")
        self.user = os.getenv("PUSHOVER_USER")
        self.url = "https://api.pushover.net/1/messages.json"

    # Function to send message
    def record_message(self, message):
        payload = {
            "token": self.token,
            "user": self.user,
            "message": message
        }

        resp = requests.post(url = self.url, data = payload)

        data = resp.json()
        if data.get("status") != 1:
            raise RuntimeError(f"Pushover failed: {data}")
            
        return data

    # Tool/function for sending message to me when the user wants to get in contact
    def record_contact_requested(self, email, name="Name not provided", notes="Not provided"):
        resp = self.record_message(f"{name} would like to get in contact with you. The provided email was {email} and notes: {notes}")
        return resp

    # Tool/function for sending message to me when the agent doesnt know how to answer a question
    def record_unknown_response(self, message):
        resp = self.record_message(f"Unable to answer the following question: {message}")
        return resp