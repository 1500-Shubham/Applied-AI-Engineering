from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
# run streamlit app with: streamlit run LangchainPrompt/prompt_ui.py
from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
# for dynamic prompt

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.1", task="text-generation")
model= ChatHuggingFace(llm=llm)


# template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],
validate_template=True
# validation ensures all placeholders are provided when invoking the template
)
# Extra: save and load prompt template
template.save('template.json')
# can save and load prompt template
# from langchain_core.prompts import PromptTemplate,load_prompt
# template = load_prompt('template.json')

# Fill the placeholders in the template with user inputs
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input})
# now use this prompt with LLM


if st.button("Generate Response"):
    response = model.invoke(prompt)
    st.write(response.content)
    # st.write(f"Generating a **{length_input}**, **{style_input}** explanation for the research paper titled '**{paper_input}**'...")

# If want to use chains
# First template create using invoke then passing the prompt to model, can do in single step using chains
if st.button("Generate Response using Chains"):
    chain = template | model
    # these are langchain pipes so automatically passing output of one to input of another
    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input})
    st.write(response.content)