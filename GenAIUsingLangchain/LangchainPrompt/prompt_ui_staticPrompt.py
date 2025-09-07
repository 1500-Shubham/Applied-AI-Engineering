from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
# run streamlit app with: streamlit run LangchainPrompt/prompt_ui.py
from dotenv import load_dotenv
load_dotenv()

st.header("Langchain Prompt UI")
user_input= st.text_input("Enter your prompt here:")
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.1", task="text-generation")
model= ChatHuggingFace(llm=llm)
if st.button("Generate Response"):
    response = model.invoke(user_input)
    st.write(response.content)