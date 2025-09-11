# convert python functions into Runnables
# Indirectly now this Runnable can be part of other chains
# example: Data -> LLM -> Give Sentiment
# Now a fucntion for preprocessing Data -> function -> LLM -> Give Sentiment


# Problem: joke -> topic -> Number of words function and parallely joke print
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda
load_dotenv()

def word_count(text):
    return len(text.split())

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


joke_gen_chain = RunnableSequence(prompt1, model, parser)

lambda_word_count = RunnableLambda(word_count)

# joke aaya joke_gen_chain se woh input in dono ke liye
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': lambda_word_count
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result= final_chain.invoke({'topic':'cricket'})

# capture between joke
print(result['word_count'], "Joke", result['joke'])
