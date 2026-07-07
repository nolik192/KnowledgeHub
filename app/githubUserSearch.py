from fastapi import FastAPI
import httpx
import pydantic
from pydantic import field_validator

app = FastAPI()

class UserRequest(pydantic.BaseModel):
    username: str   
    repository_count: int
    @field_validator("username")
    @classmethod
    def validate_username(cls, v):
        if not v:
            raise ValueError("Username cannot be empty")
        return v
    
@app.post("/github_user/{username}")
async def get_github_user(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        if response.status_code != 200:
            return {"error": "User not found"}
        data = response.json()
    return {
        "username": data["login"],
        "repository_count": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"]
    }