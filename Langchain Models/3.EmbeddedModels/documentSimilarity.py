from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents =[
    "Virat Kohli is a great cricketer",
    "Rohit Sharma is an excellent batsman",
    "Sachin Tendulkar is a legendary cricketer",
    "MS Dhoni is a successful captain"
]

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
doc_embedding = embedding.embed_documents(documents)

query= "tell aabout virat kohli"
query_embedding = embedding.embed_query(query)

similarity = cosine_similarity([query_embedding], doc_embedding)
similarity = np.array(similarity[0])
index = np.argmax(similarity)
print(f"Most similar document to the query '{query}' is: '{documents[index]}')")