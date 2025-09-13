from langchain.text_splitter import CharacterTextSplitter

text ="I am checking text splitting"
splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0, # different chunks mein kitne character common rakhna hia
    separator=''
)
# splitting text directly
text_parts = splitter.split_text(text)
print(text_parts)

#Splitting document object with document loader
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('/Users/shubhamkeshari/Documents/VSCode/Applied-AI-Engineering/GenAIUsingLangchain/DocumentLoaderComponent/PDF.pdf')
docs = loader.load()
result = splitter.split_documents(docs)
print(result[1].page_content)
# reult is itself Document Object docs+Text both splitted now