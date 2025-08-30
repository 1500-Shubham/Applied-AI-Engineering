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

# Langchain
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
- Memory and State Handling: Pichla Query ka output use next query mein kiski baat kar rahe the