from fastapi import FastAPI
import os
from pydantic import BaseModel
from gptauthor.console import create_new_story  

app = FastAPI()

#Define the request body schema                                                                                                                                  
class StoryRequest(BaseModel):                                                                                                                                    
    title: str                                                                                                                                                    
    genre: str                                                                                                                                                    
    description: str

@app.get("/clone")
def clone_repo():
    os.system("git clone https://github.com/smokewulf/gptauthor.git")
    return {"message": "Repository cloned successfully."}

@app.get("/commits")
def list_commits():
    commits = os.popen("git --git-dir=gptauthor/.git log --oneline").read()
    return {"commits": commits.splitlines()}

@app.post("/create_story")                                                                                                                                        
def create_story(story_request: StoryRequest):                                                                                                                    
    # Call the function from console.py to create a new story                                                                                                     
    result = create_new_story(story_request.title, story_request.genre, story_request.description)                                                                
    return {"message": result}
