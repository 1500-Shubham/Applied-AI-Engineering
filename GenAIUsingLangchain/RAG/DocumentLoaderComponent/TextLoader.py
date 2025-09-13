# TEXT file -> Document Obj convert
# useCase: LogFiles, YoutubeSubtitle

from langchain_community.document_loaders import TextLoader


loader = TextLoader('text.txt', encoding='utf-8')
docs = loader.load()
# converted into document object
#ALL Loaders convert into list


print(len(docs),type(docs))

content= docs[0].page_content
metadata=docs[0].metadata
print(content[0:20])
