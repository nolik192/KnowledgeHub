from fastapi import FastAPI
import pydantic
from pydantic import field_validator

app = FastAPI()
movies = []
class Film(pydantic.BaseModel):
    title: str
    year: int
    rating: float
    @field_validator("rating")
    @classmethod
    def validate_rating(cls, v):
        if v < 0 or v > 10:
            raise ValueError("Rating can be from 0 to 10 only")
        return v
    
@app.post("/movies")
async def AddMovies(film: Film):
    movies.append(film)
    return {"message": "Movie added successfully", "movie": film}

@app.get("/movies")
async def GetMovies():
    return {"movies": movies}

@app.get("/movies/{title}")
async def GetMovieByTitle(title: str):
    for movie in movies:
        if movie.title == title:
            return {"movie": movie}
    return {"error": "Movie not found"}
