from functools import wraps
from pypdf import PdfReader

extractor_tool_registry = {}

def extract_data(file_path: str, file_type: str):
    return extractor_tool_registry[file_type](file_path)

def register_extractor(file_type: str):

    def decorator(func):

        @wraps(func)
        def wrapper(file_path: str):
            return func(file_path)

        extractor_tool_registry[file_type] = func
        return wrapper

    return decorator


class Extractors():

    def __init__(self) -> None:
        pass

    # Function to extract text from pdf's
    @register_extractor(".pdf")
    def pdf_extractor(file_path: str) -> str:
        pdf = PdfReader(file_path)

        pages = pdf.pages
        text = ""

        for page in pages:
            content = page.extract_text()

            if content:
                text += content

        return text

    # Function to get text from files
    @register_extractor(".txt")
    def text_extractor(file_path: str) -> str:
        text = ""
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        return text
        