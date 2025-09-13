# R1 R2 can connect to create a sequence of runnables
# example: (prompt -> llm) -> chain create

# syntax: sequence = R1 | R2 | R3
# OR use RunnableSequence([R1, R2, R3]) imported

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    input_variables=["product"],
    template="Write a creative product description for {product}",
)
print(prompt)
parser = StrOutputParser()
chain = prompt | model | parser
# OR
# chain = RunnableSequence([prompt, model, parser])
result = chain.invoke({"product": "langchain"})
print(result)