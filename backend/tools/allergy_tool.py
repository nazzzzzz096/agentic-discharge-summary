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


def extract_allergies(text: str) -> dict:
    """
    Extract documented allergies.

    Args:
        text (str):
            Medical document text.

    Returns:
        dict:
            {
                "allergies": []
            }

    Notes:
        - Extract only explicitly documented allergies.
        - Do not infer allergies.
        - Return MISSING if unavailable.
    """

    prompt = f"""
    Extract allergies.

    Return JSON only.

    Format:

    {{
        "allergies":[]
    }}

    Rules:
    - Extract only documented allergies.
    - Do not infer.
    - Return MISSING if unavailable.

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