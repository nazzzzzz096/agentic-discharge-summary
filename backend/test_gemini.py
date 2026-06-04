from google import genai
from backend.config import MODEL_NAME,GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


response=client.models.generate_content(model=MODEL_NAME,contents="Reply: Gemini Connection Successful")

print(response.text)

