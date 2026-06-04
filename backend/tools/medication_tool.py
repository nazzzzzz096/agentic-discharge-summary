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

def extract_medications(text):

    prompt = f"""
    Extract all medications.

    Return JSON only.

    Format:

    {{
        "medications":[
            {{
                "name":"",
                "dose":"",
                "frequency":"",
                "duration":""
            }}
        ]
    }}

    Rules:
    - Do not infer.
    - Extract only explicitly mentioned medications.
    - Extract dose if available.
    - Extract frequency if available.
    - Extract duration if available.
    - Preserve medication names exactly as written.
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