from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
# key name for Hugging Face is HUGGINGFACE_ACCESS_TOKEN
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.1", task="text-generation")
model= ChatHuggingFace(llm=llm)

response= model.invoke("Hello, how are you?")
print("Response:", response.content)
