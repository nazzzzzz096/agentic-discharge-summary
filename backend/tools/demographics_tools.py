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


def extract_demographics(text: str) -> dict:
    """
    Extract patient demographic information from source text.

    Args:
        text (str):
            OCR extracted medical document text.

    Returns:
        dict:
            {
                "patient_name": str,
                "age": str,
                "gender": str
            }

    Notes:
        - Never infer missing values.
        - Return "MISSING" when information
          is unavailable in the source text.
        - Output is intended for clinician review.
    """

    prompt = f"""
    Extract patient demographics.

    Return JSON only.

    Format:

    {{
        "patient_name":"",
        "age":"",
        "gender":""
    }}

    Rules:
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