from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
load_dotenv()

# key name for Anthropic is ANTHROPIC_API_KEY
model= ChatAnthropic(model="claude-2", temperature=0, max_completion_tokens=100)
response= model.invoke("Hello, how are you?")
print("Response:", response.content)