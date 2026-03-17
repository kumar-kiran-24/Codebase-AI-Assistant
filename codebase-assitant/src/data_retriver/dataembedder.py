from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings
import os
from langchain_qdrant import QdrantVectorStore

import os
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path


class DataEmbedder:

    def __init__(self):

        BASE_DIR = Path.cwd()
        self.save =Path("/tmp/embeddings")

        self.embeddings_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.url = os.getenv("QDRANT_URL")
        self.api_key = os.getenv("QDRANT_API_KEY")

        self.client = QdrantClient(
            url=self.url,
            api_key=self.api_key
        )


    def data_embedder(self, docs):

    
        try:

            QdrantVectorStore.from_texts(
                    texts=["hello world", "test data"],
                    embedding=self.embeddings_model,
                    url=os.getenv("QDRANT_URL"),
                    api_key=os.getenv("QDRANT_API_KEY"),
                    collection_name="debug_test",
                    force_recreate=True
                                            )
        

            vectorstore =QdrantVectorStore.from_documents(
                    documents=docs,
                    embedding=self.embeddings_model,
                    url=os.getenv("QDRANT_URL"),
                    api_key=os.getenv("QDRANT_API_KEY"),
                    collection_name="codebase",
                    force_recreate=True
                )

         

            return vectorstore

        except Exception as e:
            return {"error": str(e)}


