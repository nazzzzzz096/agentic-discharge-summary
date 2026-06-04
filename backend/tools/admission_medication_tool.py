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

def extract_admission_medications(text):

    prompt = f"""
    Extract medications that the patient
    was taking before admission.

    Return JSON only.

    Format:

    {{
        "admission_medications":[]
    }}

    Rules:
    - Do not infer.
    - Extract only explicitly mentioned
      pre-admission medications.

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