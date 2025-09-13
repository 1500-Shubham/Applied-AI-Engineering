# PDF -> Each Pages -> [doc0,doc1,doc3] all Document object converts

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('PDF.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)