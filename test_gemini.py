import os
from dotenv import load_dotenv
from google import genai
MODEL = "gemini-3.5-flash-lite"

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model=MODEL,
    contents="Say hello in one short sentence and tell me one thing an AI data analyst can do.",
)
print(response.text)