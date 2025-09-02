import dotenv
import os

from langchain.openai import OpenAI
# Load environment variables from .env file
dotenv.load_dotenv()

print("Environment variables loaded successfully.",os.getenv("OPENAI_API_KEY"))

# The OpenAI class in LangChain internally looks for the environment variable OPENAI_API_KEY.
llm= OpenAI(model='text-davinci-003',temperature=0.7,max_retries=3)

# Basic LLM call
response= llm.invoke("What is the capital of India?")
print(response)