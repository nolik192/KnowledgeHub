from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to KnowledgeHubAI!"}

@app.get("/status")
def get_status():
    return {"status": "KnowledgeHubAI is running smoothly."}

@app.get("/info")
def get_info():
    return {
        "name": "KnowledgeHubAI",
        "version": "1.0.0",
        "description": "A knowledge management and AI-powered application."
    }

@app.get("/whoami")
def get_whoami(name: str):
    return {"user": name}

@app.get("/squared")
def get_squared(x: float):
    return {"result": x ** 2}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}! Welcome to KnowledgeHubAI."}