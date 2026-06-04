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


def extract_procedures(text: str) -> dict:
    """
    Extract procedures performed during admission.

    Args:
        text (str):
            Medical document text.

    Returns:
        dict:
            {
                "procedures": []
            }

    Notes:
        - Extract only procedures explicitly mentioned.
        - Do not infer procedures.
        - Return empty list if none found.
    """

    prompt = f"""
    Extract procedures performed.

    Return JSON only.

    Format:

    {{
        "procedures":[]
    }}

    Rules:
    - Extract only explicitly mentioned procedures.
    - Do not infer.

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