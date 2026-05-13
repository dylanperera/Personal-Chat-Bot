from pydantic import BaseModel

class ContextInformation(BaseModel):
    name: str
    summary: str
    linkedin: str
    resume: str