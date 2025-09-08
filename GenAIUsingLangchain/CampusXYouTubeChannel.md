# Gen AI
- Field generate content - text, images, music - learning patterns - human creativity mimic
- Foundation Models(LLMs) : User Perspective(Using models) and Builder Perspective(Creating Model)
    - User Perspective : Agent AI, RAG(LLM use own wok pipeline create), Vector Databases, Prompt Engineering, Fine Tuning
    - Builder Perspective : Pretraining, Quantization,FineTuning

# Builder Perspective (Create Foundation Model) : Data Scientist
- Transformer Architecture
- Types of Transformer Encoder(BERT) and Decoder(GPT)
- Pretraining - Training objectives, tokenization strategies
- Optmization - model compression, quantization
- Fine-Tuning - Task Specific(Performance improve), Instruction Tuning and Continual pretraining
- Evaluation and Deployment

# User Perspective (Use Foundation Model) : Software Developers
- Building Basic LLM - APIS LLM : Langchain Hugging Face, Ollama
- Improving LLM Response
    - Prompt Engineering
    - RAG (LLM ko apna private dikha ke response)
    - Fine Tuning
- Agents AI : Chatbots that work karke dede ticket book
    - LLM tools dete ho woh access karke actual work
- LLMOps : Deploy application that we make LLM based
- Miscellaneous : Working audio video inpe work

# Langchain (Library or Framework)
- Build LLM Apps (Models use karenge direct - User Side)
- Chatbots, question-answering systems, RAG, agents
- Other tools connect- database , aws, along with llm model connection

## Langchain Fundamentals
- Semantic Search -> Sentence (Doc Embedding (100,1))and Query hamara(Embedding (100,1)) jo near hua woh sentence answer 
- LLM local setup hard since these are trained on internet to get ouput in local computer high computational cost
    - use APIs (OpenAI, Google)
- Langchain mein tasks functions, sentence embedding (NLP Models integrate) AWS, DB, LLM API - sab ek saath combine
    - build in plug and play OPENAPI switch GEMINI langchain easy 
- Concept of chains : Series of task convert into chain (ek output dusre ka automatically input ban jata)
- Model egnostic Development : Open API use ya GEMINI, AWS or GCP single line code change
    - just need to focus on logic
- Every Task: Langchain bahut saare variety de dega Upload karne ke kafi tarike etc.
- Memory and State Handling: Pichla Query ka output use next query mein kiski baat kar rahe the.
- What you can build?
    - Conversation Chatbots: handle more users together 
    - AI Knowledge Assistants: knowledge of my data, like my website data pata hai student can ask doubt
    - AI Agents: Chatbots hai but access other tools through API access like trip ticket info and book tickets 
    - summarization and research helper: Chatgpt direct books upload nahi, company personal data pe chatbots personal bana lo langchain lo
## Langchain Components
- 1) Models
    - interface which help in interacting AI Models (APIS Like)
    - standard interface diya OPENAI APIS or CLAUSE APIS inko integrate karne ka simple tarika
    - Differnet models use in interface (WEBSITE GIVEN Langchain) way
        -Language Models
            - LLM (text in text out)
            - Chat Models
        - Embedding Models
        (text in vector feature out). Useful in semantic search
- 2) Prompts
    - input provided to LLM
    - Code: Prompt = PromtTemplate("create your prompt object")
        - Dynamic Prompt {value can change dynamically placeholder rakh diya}
        - Role-Based Promot (system: you are enginner user: you prompt)
        - Few Shot Prompting( show LLM example then ask question)
- 3) Chains
    - Pipelines build 
    - Input -> LLM -> translate -> LLM -> Summary
    - Chains (autmatically one stage output as input of other stage), no need manually 
        - Sequence Chains 
        - Complex Chains like parallel chain, conditional chain
- 4) Memory
    - LLM API calls are stateless
    - First Query -> Got Response
    - Second Query based on first then Langchain memory of first query
    - Store last n queries something like this in memory
- 5) Indexes
    - connects your application to external knowledge like DB, PDF, websites
    - Components of indexes
        - Doc Loader
        - Text Splitter
        - Vector store
        - Retrievers 
    - my company private data Questions wont answer as CHATGPT is not trained on these data
    - Solution: LLM -> Connect to external knowledge connect and ask questions on that
- 6) AI Agents
    - Chatbot but with access to other tools like booking system
    - Tools : Calculator and Weather API
        - Multiply Delhi temp by 3
        - Extract Meaning: Delhi Temp -> tool
        - Extract Meaning: multiple 3 -> calculator tool

## Langchain Models
- Language Models (All Code inside folder)
    - LLMs
        - general purpose model: text generazation, summarization, code questions answer
        - single Text in and single Text out
        - trained on text books 
        - GPT 3
    - Chat Models
        - conversational task. multiple messages as input
        - memory and context rakhta hai 
        - trained on text and fine tuned on chat datasets
        - understands system user and assistant roles
            - you are qualified doctor bata ke data se output
        - conversation AI, AI tutors
        - GPT 4

## Langchain Prompts
- input instruction or queries to a model to give output
- Two Types:
    - Text Based - String used for communication
    - Multimodal : Image , Text, Video
- Prompt important as it decides output from LLM.
- Static vs Dynamic Prompt : PromptTemplate
    - created different files for this
    - dynamic has {} input accoring change the nature
        - Create Template Prompt Class
            - Through we could have use string and placeholder 
            - Using Prompt Template is a standarized way toh 
            - Prompt Template Reusable save in template.json and load anywhere
            - Prompt validation kar lega automatically
        - Create prompt generator and template py file for easiness
- Messages in Prompt : Useful in creating Chatbots conversational : ChatPromptTemplate
    - Static Messages
        - SystemMessages
        - HumanMessages
        - AI Messages
        - Created messages.py to understand these three types
        - Instead of hardcoding System Human AI use these messages to chat with LLM 
    - Dynamic Messages : ChatPromptTemplate
        - ex. System Message: you are expert in {{domain}} dynamic kar raha mai
        - Human Message : Explain {topic}
    - Message Placeholder : used inside ChatPromptTemplate to dynamically insert chat history or list of messages during runtime
        - While building chatbots: chat history generally stored
        - Solve this problem: All History is stores as message placeholder
    - ChatPromptTemplate use this messagePlaceholder (for history)
    - see message_placeholder.py for the basic code

## Langchain Structured Output
- LLM can interact with Database, APIS, other systems (because of structure output)
- Practice in which LLM can return data in strucutre format like JSON, can help integrate with other tools with LLM.
    - Use Cases: AI Agents(other tools input format ke hisab se), DataExtraction(LLM output store in Database with your table type), 
- Generally LLM input text and ouput unstructed output simply text 
- Want Json enforced output {"even1":"msg1", like this in structure way}
### Two Types of LLMS based on output
##### 1) LLM generating structured output -> with_structured_output fucntion
    - before model.invoke use this method
    - Format declare : Typed Dict, Pydantic, Json_Schema
        - Typed Dict: Define keys and values should exist, ensures dictinoary in python looks like, but jaruri nahi LLM return in that format
            - Tell Class Person {name: String, age:Int}  now no ambiguity
            - LLM internally generates a prompt statign the keys of typed dict and return in that way
        - Pydantic: data validation and data parsing library in Python. Ensures data you work is correct, structured and type-safe
            - Basic example
            - Defaul Values
            - Optional Fields
            - Type Coerve auto conversion
            - Built in validataion ex. email
            - Constrain like this range using Field Fucntion (constrain, description)
            - Can convert pydantic to dict or json
        - Json Schema: If multiple backend sprinboot and python universal data format
            - pydantic or typed dict only python
            
##### 2) LLM's Not generating (Open Source) structured output -> Output Parsers function
- Output Parser in Langchai raw LLM Responses into structered formats like JSON, CSV, Pydnatic models and more.
- can be used along with LLM returning structured output (with_Structure function replace) and LLM not wale case
- Types Of Output Parser Mainly used in Langchain
    - 1) String 
        - indirectly uses result.content (normal response from LLM)
        - useful in creating chains baar baar result.content ko paas na karna ho next template mein
    - 2) Json 
        - Forces LLM to return json format
         response
        - With Prompt Template send this parser as a variable, partial variable(since not filled during runtime) see code
        - Parser parses result.content into json
        - Problem: Json return hoga but not a fixed schema, yeh key aur aise values do mereko
            - Solution: Use structured output parser
    - 3) Structured 
        - Extract Structured Json based on predefined fixed schema 
        - Problem: Can't Do Data Validation, maine bola schema {age ,name, city} wanted {str,str,int} ho but koi tarika nahi only prompt mein likh sakta but llm zaruri nahi waise ho
            - Solution: Use Pydantic
    - 4) Pydantic (Best)
        - Is Structured Output parser with use of Pydantic Models to form schema which ensures data validation

## Chains in Langchain
- What and Why
    - Application is build in steps 1st response 2nd response dependent on 1st 
    - prompt - llm - response - process - output to user
    - Problem: Each step manually handle, prompt design, user input, response, then usme se pakde kafi lengthy process
    - Chains Pipeline create (Prompt design send to llm and send the output to another) each step output works as input to next step
    - input - pipeline - output thats it
    - linear sequential example hai yeh
- Types of Chain See Code easy to understand
    - 1) Linear
    - 2) Parallel
    - 3) Conditional


