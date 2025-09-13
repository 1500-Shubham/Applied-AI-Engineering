from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# inside directory everyfile load and convert
# works with differen Loaders

loader = DirectoryLoader(
    path='directory',
    glob='*.pdf', # yeh saare pdf load
    loader_cls=PyPDFLoader # using specific pdf loader
)

# docs = loader.load()
docs = loader.lazy_load() # if time jyada lag raha
# memory load pdf ek saaht load na kare 
# on demand load

# print(len(docs))
# print(docs[0].page_content[0:10])
for document in docs:
    print(document.metadata)
