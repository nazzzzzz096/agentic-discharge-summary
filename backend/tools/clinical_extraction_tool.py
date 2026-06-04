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


def extract_clinical_data(text):
    """
    Extract all structured clinical data
    in a single Gemini call.
    """

    prompt = f"""
Extract clinical information.

Rules:
- Never return null.
- Use "MISSING" for unavailable fields.
- Return JSON only.
- Extract ALL diagnoses.
- Include principal diagnoses.
- Include secondary diagnoses.
- Include chronic conditions documented in past history.
- Include imaging findings documented as diagnoses.
- Do not limit the number of diagnoses.
- Extract all discharge medications.
- Extract all procedures explicitly documented.
- Extract discharge condition if documented.
Return JSON only.

Format:

{{
    "diagnoses": [],

    "medications": [
        {{
            "name":"",
            "dose":"",
            "frequency":"",
            "duration":""
        }}
    ],

    "pending_results": [],

    "hospital_course":"",

    "followup":[],

    "demographics": {{
        "patient_name":"",
        "age":"",
        "gender":""
    }},

    "dates": {{
        "admission_date":"",
        "discharge_date":""
    }},

    "allergies":[],

    "procedures":[],

    "condition_at_discharge":""
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