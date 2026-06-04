# backend/utils/json_parser.py

import json

def parse_json_response(response_text):

    response_text = response_text.replace(
        "```json",
        ""
    )

    response_text = response_text.replace(
        "```",
        ""
    )

    response_text = response_text.strip()

    return json.loads(response_text)