from fastapi import FastAPI\nimport os\n\napp = FastAPI()\n\n@app.get('/clone')\ndef clone_repo():\n    os.system('git clone https://github.com/smokewulf/gptauthor.git')\n    return {'message': 'Repository cloned successfully.'}\n\n@app.get('/commits')\ndef list_commits():\n    # Fetch commits from the repo\n    commits = os.popen('git --git-dir=gptauthor/.git log --oneline').read()\n    return {'commits': commits.splitlines()}