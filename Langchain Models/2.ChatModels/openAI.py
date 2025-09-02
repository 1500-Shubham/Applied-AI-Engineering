from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   
load_dotenv()

# temperature is a parameter that controls the randomness of the model's output. A temperature of 0 makes the output more deterministic, while higher values (like 0.7) make it more random.
# max_completion_tokens sets the maximum number of tokens the model can generate in its response.
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,max_completion_tokens=100)
result= model.invoke("Hello, how are you?")
print(result)# Make sure to set your OPENAI_API_KEY in the .env file or environment variables

# Here result will contain the response from the model
# Example:  
#content, usage, total_tokens = result.content, result.usage, result.total_tokens
print("Response:", result.content)