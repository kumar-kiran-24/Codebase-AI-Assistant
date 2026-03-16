import os 
from dotenv import load_dotenv


load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

class DataSplitter:


    def dataSplitter(self,docs):

        


        splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(docs)

        print("Total chunks:", len(chunks))
        return chunks

        





