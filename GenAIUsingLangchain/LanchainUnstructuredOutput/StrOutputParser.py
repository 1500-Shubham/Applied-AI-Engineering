# Return LLM results as a string
# easy to use when you want to return a simple string
# LLM return can have metadata, content attributes like result.content
# This parser will return result.content but what was the need of this parser then?
# Jab result.content hi milna tha


# Task: To compare normal result.content with STR Output Parser
# Topic -> LLM -> Detailed Output -> LLM -> Summary of 5 lines

# NORMAL OUTPUT RESULT>CONTENT
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

# print(result1.content)


# STR OUTPUT PARSER
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   
# Works well with chains as internally it takes result.content

parser = StrOutputParser()

# because of parser we dont need to do result.content
# we can directly pass result to next template
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'black hole'})

print(result)  # directly prints the content without needing .content
