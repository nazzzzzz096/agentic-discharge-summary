
from backend.tools.ocr_tools import (
    extract_text
)

text = extract_text(
    "output/page_1.png"
)

print(text[:2000])