from google import genai

from backend.config import (
    GEMINI_API_KEY,
    MODEL_NAME
)

from backend.utils.json_parser import (
    parse_json_response
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def extract_hospital_course(text):

    prompt = f"""
    Extract the Hospital Course section.

    Rules:
    - Return JSON only.
    - Do not summarize.
    - Extract only information explicitly present.
    - If not found return empty string.

    Format:

    {{
        "hospital_course":""
    }}

    Text:
    {text}
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return parse_json_response(
        response.text
    )