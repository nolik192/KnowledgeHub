from fastapi.testclient import TestClient
from app.FilmsFastAPI import app

client = TestClient(app)

def test_add_movie_works():
    r = client.post("/movies", json={
        "title": "Inception", "year": 2010, "rating": 8.8
    })
    assert r.status_code == 200
    assert r.json()["message"] == "Movie added successfully"
    assert r.json()["movie"]["title"] == "Inception"

def test_bad_rating():
    r = client.post("/movies", json={
        "title": "Bad Movie", "year": 2020, "rating": 11
    })
    assert r.status_code == 422

def test_list_after_add():
    client.post("/movies", json={
        "title": "The Matrix", "year": 1999, "rating": 8.7
    })
    r = client.get("/movies")
    titles = [m["title"] for m in r.json()["movies"]]
    assert "The Matrix" in titles