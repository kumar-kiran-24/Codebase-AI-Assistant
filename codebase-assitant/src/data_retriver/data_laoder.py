import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader

class DataLoader:
    def __init__(self):
        self.ignore_files = [
            "pnpm-lock.yaml",
            "package-lock.json",
            "yarn.lock"
        ]

        self.ignore_folders = [
            "node_modules",
            ".next",
            "dist",
            "build",
            "__pycache__",
            ".git"
        ]

    def should_include(self, file_path):
    
        if any(folder in file_path for folder in self.ignore_folders):
            return False

      
        if os.path.basename(file_path) in self.ignore_files:
            return False

        return True

    def data_loader(self, path):
        try:
            repo_path = path

            extensions = [
                    
                        "*.py",


                        "*.js", "*.ts", "*.jsx", "*.tsx", "*.mjs", "*.cjs",

                    
                        "*.java", "*.kt", "*.kts",

                        
                        "*.c", "*.cpp", "*.h", "*.hpp",

                    
                        "*.cs",

                    
                        "*.go",

                    
                        "*.rs",

                    
                        "*.rb",

                        
                        "*.php",

                    
                        "*.swift",

                    
                        "*.dart",

                        "*.sh", "*.bash", "*.zsh",

                    
                        "*.dockerfile", "Dockerfile", "*.tf",

                        # 📄 Config (important but controlled)
                        "*.json", "*.yaml", "*.yml",

                        # 📝 Docs (optional but useful)
                        "*.md"
                    ]

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

                loaded_docs = loader.load()

                # FILTER HERE
                for doc in loaded_docs:
                    source = doc.metadata.get("source", "")

                    if not self.should_include(source):
                        continue

                    documents.append(doc)

        except Exception as e:
            return {"error": e}

        return documents