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

def extract_followup(text):

    prompt = f"""
    Extract complete follow-up instructions.

    Return JSON only.

    Format:

    {{
        "followup":[]
    }}

    Rules:
    - Extract only complete follow-up instructions.
    - Extract review dates.
    - Extract return precautions.
    - Extract follow-up visits.
    - Do not return isolated laboratory names.
    - Do not return partial phrases.
    - Do not infer instructions.
    - Preserve the wording as closely as possible.

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