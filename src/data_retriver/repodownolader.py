from git import Repo
from pathlib import Path
import shutil


class DataDownloader:

    def downloader(self, repo_url):
        try:


            path = Path("data/repo")

            # create parent directory
            path.parent.mkdir(parents=True, exist_ok=True)

            # delete repo if it already exists
            if path.exists():
                shutil.rmtree(path)

            # clone the repository
            Repo.clone_from(repo_url, path)



            return path
        except Exception as e:
            return {
                "error":e
            }