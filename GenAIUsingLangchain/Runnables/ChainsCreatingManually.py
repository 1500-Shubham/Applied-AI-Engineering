# Old Way Each Component has there own function
# And Creating A Chain was manual since using that function

import random

class NakliLLM:

  def __init__(self):
    print('LLM created')

  def predict(self, prompt):

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}
  

class NakliPromptTemplate:

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    # format is used when string has {value to feed}
    return self.template.format(**input_dict)

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)
prompt = template.format({'length':'short','topic':'india'})
llm = NakliLLM()
print(llm.predict(prompt))


## Now Creating A Chain using these component function
class NakliLLMChain:

  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt

  def run(self, input_dict):

    # Both the important function inside this function
    final_prompt = self.prompt.format(input_dict)
    result = self.llm.predict(final_prompt)

    return result['response']

chain = NakliLLMChain(llm, template)
print(chain.run({'length':'short', 'topic': 'india'}))