import json

with open("output/page_1.txt","r",encoding="utf-8") as f:

    text = f.read()


from backend.tools.diagnosis_tools import extract_diagnoses

result = extract_diagnoses(text)

print(result)