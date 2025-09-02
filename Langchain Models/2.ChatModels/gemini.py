from langchain_google_genai import ChatGemini
from dotenv import load_dotenv
import os
load_dotenv()
# key name for Gemini is GOOGLE_API_KEY
model= ChatGemini(model="gemini-1.5-turbo", temperature=0
, max_completion_tokens=100)
response= model.invoke("Hello, how are you?")
print("Response:", response.content)