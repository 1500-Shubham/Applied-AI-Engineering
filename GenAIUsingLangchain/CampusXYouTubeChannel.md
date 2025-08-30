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
        - LLM (text in text out)
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
