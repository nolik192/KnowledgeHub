from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city: str):
    # публичное API погоды без ключа (wttr.in)
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://wttr.in/{city}?format=j1")
        data = response.json()
    current = data["current_condition"][0]
    return {
        "city": city,
        "temp_C": current["temp_C"],
        "description": current["weatherDesc"][0]["value"]
    }
