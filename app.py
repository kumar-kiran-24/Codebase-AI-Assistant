from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from src.main import Main
from src.components.bot import Bot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*" ] , 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pathlib import Path
import shutil
import zipfile

class UserRequest(BaseModel):
    url: str

class Chat(BaseModel):
    question:str
    session_id:str

main=Main()
bot=Bot()

@app.post("/upload")
def upload(user: UserRequest):

    repo_url = user.url
    main.initate_main(url=repo_url)

@app.post("/chat")
def chat(user:Chat):
    question=user.question
    session_id=user.session_id


    context=main.data_loader(question=question)


    reposne=bot.initate_bot(question=question,session_id=session_id,context=context)

    print(reposne)

    return {
        "message":reposne
    }

UPLOAD_DIR = Path("/tmp/repo2")

@app.post("/upload-project")
async def upload_file(file:UploadFile=File(...)):
    zip_path = Path("/tmp/repo2.zip")

    with open(zip_path,"wb") as f:
        shutil.copyfileobj(file.file,f)
    
    if UPLOAD_DIR.exists():
        shutil.rmtree(UPLOAD_DIR)
    
    UPLOAD_DIR.mkdir(parents=True)

    with zipfile.ZipFile(zip_path,"r") as zip_ref:
        zip_ref.extractall(UPLOAD_DIR)
    
    main.upload_folder(path=UPLOAD_DIR)
    

    return{
        "messages":"Project uploades sucesfully",
        "path":str(UPLOAD_DIR)
    }


@app.post("/upload-files")
async def upload_files(files: List[UploadFile] = File(...)):

    save_path = Path("data/project")
    save_path.mkdir(parents=True, exist_ok=True)

    for file in files:
        file_location = save_path / file.filename

        with open(file_location, "wb") as f:
            f.write(await file.read())
    main.upload_folder(path=save_path)
    return {"message": "Files uploaded"}


if __name__=="__main__":
    uvicorn.run("app:app",reload=True,port=8000)

