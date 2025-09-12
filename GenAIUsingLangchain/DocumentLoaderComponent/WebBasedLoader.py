# web page conent load and convert to Document Object
# Text content from webpage

from langchain_community.document_loaders import WebBaseLoader
url = 'https://www.w3schools.com/html/html_basic.asp'
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)