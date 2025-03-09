from fastapi import FastAPI
import os
from pydantic import BaseModel
from gptauthor.console import create_new_story  

app = FastAPI()

@app.get("/clone")
def clone_repo():
    os.system("git clone https://github.com/smokewulf/gptauthor.git")
    return {"message": "Repository cloned successfully."}

@app.get("/commits")
def list_commits():
    commits = os.popen("git --git-dir=gptauthor/.git log --oneline").read()
    return {"commits": commits.splitlines()}
