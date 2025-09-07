from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# Need Pipeline for local model

llm = HuggingFacePipeline.from_model_id(model_id="TheBloke_TinyLlama-1.1B-GPTQ", task="text-generation", model_kwargs={"temperature":0, "max_new_tokens":100})
model= ChatHuggingFace(llm=llm)
response= model.invoke("Hello, how are you?")
print("Response:", response.content)