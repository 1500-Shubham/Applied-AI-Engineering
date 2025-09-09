from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

# dimension represents the size of the vector space in which the text data will be embedded.
# Higher dimensions can capture more nuances of the text but may require more computational resources.
embedding= OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

result= embedding.embed_query("Hello World")
print(result)

# If complete documents are to be embedded
documents = ["Hello world", "Bye bye", "My name is Shubham Keshari"]
embeddings = embedding.embed_documents(documents)
print(embeddings)