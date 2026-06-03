import google.generativeai as genai
from config import MODEL_NAME,GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model=genai.GenerativeModel(MODEL_NAME)

response=model.generate_content("Reply: Gemini Connection Successful")

print(response.text)

