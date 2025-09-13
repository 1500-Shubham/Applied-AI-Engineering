# (R1 , R2, R3) run one result
# R4 and R5 run another result
# example: (prompt -> llm) , (prompt -> llm) -> combine results 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

# RunnableParallel takes a dictionary of runnables
parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'linkedin': prompt2 | model | parser
})

result = parallel_chain.invoke({'topic': 'langchain'})
# print(result)
print(result['tweet'])