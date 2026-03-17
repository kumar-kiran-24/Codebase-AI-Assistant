from src.data_retriver.data_laoder import DataLoader
from src.data_retriver.data_splitter import DataSplitter
from src.data_retriver.dataembedder import DataEmbedder
from src.data_retriver.repodownolader import DataDownloader


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
import os 
from dotenv import load_dotenv

load_dotenv()

class Main:
    datadwnloader=DataDownloader()
    dataembedder=DataEmbedder()
    datasplitter=DataSplitter()
    dataloader=DataLoader()
    embeddings=HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )


    def initate_main(self,url):
        try:
            path=self.datadwnloader.downloader(repo_url=url)
            docs=self.dataloader.data_loader(path=path)
            chunks=self.datasplitter.dataSplitter(docs=docs)
            self.embedding_path=self.dataembedder.data_embedder(docs=chunks)
        except Exception as e:
            return {
                "error":e
            }

        
    def upload_folder(self,path):
        try:
            docs=self.dataloader.data_loader(path=path)
            chunks=self.datasplitter.dataSplitter(docs=docs)
            self.embedding_path=self.dataembedder.data_embedder(docs=chunks)
        except Exception as e:
            return{
                "error":e
            }
    

    def data_loader(self, question):
        try:
            client = QdrantClient(
                url=os.getenv("QDRANT_URL"),
                api_key=os.getenv("QDRANT_API_KEY"),
                check_compatibility=False
            )

            vectorstore = QdrantVectorStore(
                client=client,
                collection_name="codebase",
                embedding=self.embeddings
            )

            docs = vectorstore.similarity_search(question, k=5)

            print("Retrieved docs:", len(docs))

            context = "\n\n".join([
                f"FILE: {doc.metadata.get('source')}\n{doc.page_content}"
                for doc in docs
            ])



            return context

        except Exception as e:
            print("ERROR:", e)
            return "Error retrieving context"
            

    


        