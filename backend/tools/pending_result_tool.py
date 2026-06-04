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

def extract_pending_results(text):

    prompt = f"""
    Extract pending or awaited results.

    Examples:
    - report awaited
    - pending result
    - follow-up lab pending
    - culture report awaited

    Return JSON only.

    Format:

    {{
        "pending_results":[]
    }}

    Rules:
    - Do not infer.
    - Extract only explicitly mentioned pending results.
    - Return the complete pending-result statement.
    - Do not shorten the result name.
    - Preserve the full pending-result statement.
    - Include associated test names.

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