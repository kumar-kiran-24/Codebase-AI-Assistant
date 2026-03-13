import os 
from dotenv import load_dotenv


load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

class DataSplitter:


    def dataSplitter(self,docs):

        splitter=RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        docs=docs


        splitter = RecursiveCharacterTextSplitter(
            chunk_size=600,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(docs)

        print("Total chunks:", len(chunks))
        return chunks

        





