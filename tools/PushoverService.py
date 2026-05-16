import requests
import os

from tools.BaseService import BaseService

class PushoverService(BaseService):
    def __init__(self) -> None:
        super().__init__("https://api.pushover.net/1/messages.json", "PUSHOVER_TOKEN", "PUSHOVER_USER")

        record_contact_requested_definition_json = {
            "type": "function",
            "name": "record_contact_requested",
            "description": "Use this function when the user would like to get in contact with me. If they provide an email address to get in contact with, call this tool",
            "parameters": {
                "type":"object",
                "properties": {
                    "email": {
                        "type":"string",
                        "description": "User email address for me to get in contact with"
                    },
                    "name":
                    {
                        "type": "string",
                        "description": "Name of the user who would like to get in contact"
                    },
                    "notes":
                    {
                        "type":"string",
                        "description": "Any notes the user might have left"
                    }
                },
                "required": ["email"],
                "additionalProperties": False
            }
        }

        record_unknown_response_definition_json = {
            "type": "function",
            "name": "record_unknown_response",
            "description": "Use this function when you don't know how to respond to a question or don't know the answer to",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type":"string",
                        "description": "message the user sent that the agent/model could not answer with the given context"
                    }
                }
            }
        }

        self.register_tool(record_contact_requested_definition_json, self.record_contact_requested)
        self.register_tool(record_unknown_response_definition_json, self.record_unknown_response)

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

if __name__ == "__main__":
    svc = PushoverService()

    try:

        print("Testing record_contact_requested...")
        print(
            svc.record_contact_requested(
                email="test@example.com",
                name="Quick Test",
                notes="Testing inside same file",
            )
        )

        print("Testing record_unknown_response...")
        print(svc.record_unknown_response("Sample unknown question"))

        print("All tests passed.")
    except Exception as e:
        print(f"Test failed: {e}")