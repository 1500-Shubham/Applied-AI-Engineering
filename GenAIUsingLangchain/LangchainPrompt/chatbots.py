from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.1", task="text-generation")
model= ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content='You are a helpful chatbots assistant'),
]

while True:
    user_input=input("You:")
    messages.append(HumanMessage(content=user_input))
    if user_input == 'exit' or user_input == 'quit' or user_input == 'q':
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("AI:",result.content)

print(messages)
