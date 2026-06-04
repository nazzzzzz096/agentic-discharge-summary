import json

from google import genai

from backend.config import GEMINI_API_KEY,MODEL_NAME

from backend.utils.json_parser import parse_json_response

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_diagnoses(text):

    prompt = f"""
    Extract all diagnoses mention in the text.
    Rules:
    - Return only JSON
    - Do not infer diagnoses.
    - Include only diagnoses explicitly mentioned.


    Example:
    {{
        "diagnoses":[
        "DKA",
        "Pyelonephritis"
        ]
    }}
    Text:
    {text}
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return parse_json_response(response.text)