# Idea Behind Runnables

from abc import ABC, abstractmethod
import random
# in python we need ABC module to create abstract class
# abstract class is a class that cannot be instantiated
# it is used to define interface for other classes

class Runnable(ABC):
    # abstract method for abstract classs
    # abstract method is a way to define interface in python
    # other classes inheriting this class must implement this method
  @abstractmethod
  def invoke(input_data):
    pass
  
  import random

class NakliLLM(Runnable):

  def __init__(self):
    print('LLM created')

  def invoke(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}

#This method is going to be deprecated
  def predict(self, prompt):

    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]

    return {'response': random.choice(response_list)}
  

class NakliPromptTemplate(Runnable):

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def invoke(self, input_dict):
    return self.template.format(**input_dict)

  def format(self, input_dict):
    return self.template.format(**input_dict)

class NakliStrOutputParser(Runnable):

  def __init__(self):
    pass

  def invoke(self, input_data):
    return input_data['response']

class RunnableConnector(Runnable):

  def __init__(self, runnable_list):
    self.runnable_list = runnable_list

  def invoke(self, input_data):

    for runnable in self.runnable_list:
      input_data = runnable.invoke(input_data)

    return input_data

# Made all components using same Function 
# And Creating A Chain using RunnableConnector class

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)
llm = NakliLLM()
parser = NakliStrOutputParser()
chain = RunnableConnector([template, llm, parser])
print(chain.invoke({'length':'long', 'topic':'india'}))

template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)

llm = NakliLLM()
parser = NakliStrOutputParser()
chain1 = RunnableConnector([template1, llm])
# chain1 output is llm giving in dictionary{reponse: 'joke'}
# used by chain2 template
chain2 = RunnableConnector([template2, llm, parser])
final_chain = RunnableConnector([chain1, chain2])
print(final_chain.invoke({'topic':'cricket'}))