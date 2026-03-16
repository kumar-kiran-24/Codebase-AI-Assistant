from src.data_retriver.data_laoder import DataLoader
from src.data_retriver.data_splitter import DataSplitter
from src.data_retriver.dataembedder import DataEmbedder
from src.data_retriver.repodownolader import DataDownloader

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class Main:
    datadwnloader=DataDownloader()
    dataembedder=DataEmbedder()
    datasplitter=DataSplitter()
    dataloader=DataLoader()
    embeddings=HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )


    def initate_main(self,url):
        path=self.datadwnloader.downloader(repo_url=url)
        docs=self.dataloader.data_loader(path=path)
        chunks=self.datasplitter.dataSplitter(docs=docs)
        self.embedding_path=self.dataembedder.data_embedder(docs=chunks)
    def upload_folder(self,path):
        docs=self.dataloader.data_loader(path=path)
        chunks=self.datasplitter.dataSplitter(docs=docs)
        self.embedding_path=self.dataembedder.data_embedder(docs=chunks)
    
    def data_loader(self,question):
        self.embedding_path="embeddings"
        
        db=FAISS.load_local(
            self.embedding_path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

        results=db.similarity_search(query=question,k=3)
        print(results)
        
        return results
    

if __name__=="__main__":
    main=Main()

    main.data_loader(question="code for the ragchatbot",url="https://github.com/kumar-kiran-24/EDWINNOVA-CHATBOT")

        

    
    


        