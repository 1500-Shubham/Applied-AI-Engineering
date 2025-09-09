from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# Problem: Json return hoga but not a fixed schema, yeh key aur aise values do mereko

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="swiss-ai/Apertus-8B-Instruct-2509",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
print(type(template))
chain = template | model | parser
# here parser is basically taking result.content and parsing it into json

result = chain.invoke({'topic':'black hole'})
print(type(result))
print(result)

#OR big way instead of chain
prompt = template.format(topic='black hole')
print(prompt)
# Give me 5 facts about black hole 
#  Return a JSON object.
response = model.invoke(prompt)
parsed = parser.parse(response.content)
print(parsed)
