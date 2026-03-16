import os 
from dotenv import load_dotenv


load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

class DataSplitter:


    def dataSplitter(self,docs):
        try:

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000,
                chunk_overlap=100
            )

            chunks = splitter.split_documents(docs)


            return chunks
        except Exception as e:
            return {
                "error":e
            }

        





