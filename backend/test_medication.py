from backend.tools.medication_tool import (
    extract_medications
)

with open(
    "output/page_2.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

result = extract_medications(text)

print(result)