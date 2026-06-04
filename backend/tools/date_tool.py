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


def extract_dates(text: str) -> dict:
    """
    Extract admission and discharge dates.

    Args:
        text (str):
            Medical document text.

    Returns:
        dict:
            {
                "admission_date": str,
                "discharge_date": str
            }

    Notes:
        - Do not infer dates.
        - Return MISSING when absent.
    """

    prompt = f"""
    Extract admission and discharge dates.

    Return JSON only.

    Format:

    {{
        "admission_date":"",
        "discharge_date":""
    }}

    Rules:
    - Do not infer dates.
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