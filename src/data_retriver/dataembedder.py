from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

import os
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path


class DataEmbedder:

    def __init__(self):

        BASE_DIR = Path.cwd()
        self.save = BASE_DIR / "embeddings"

        self.embeddings_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

    def data_embedder(self, docs):

        print("Initializing embeddings...")

        self.save.mkdir(parents=True, exist_ok=True)

        db = FAISS.from_documents(
            docs,
            self.embeddings_model
        )

        db.save_local(str(self.save))

        return self.save


