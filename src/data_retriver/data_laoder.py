from langchain_community.document_loaders import DirectoryLoader, TextLoader

class DataLoader:
    def __init__(self):
        pass

    def data_loader(self,path):
        repo_path = path
        extensions = ["*.py", "*.js", "*.ts", "*.java", "*.cpp", "*.md", "*.json"]

        documents = []

        for ext in extensions:
            loader = DirectoryLoader(
                repo_path,
                glob=f"**/{ext}",
                loader_cls=TextLoader,
                loader_kwargs={
                    "encoding": "utf-8",
                    "autodetect_encoding": True
                },
                show_progress=True
            )

            documents.extend(loader.load())
        
        return documents