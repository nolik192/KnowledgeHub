from fastapi.testclient import TestClient
#from app.FastAPILibrary import app
from app.FastAPILibrary import app
client = TestClient(app)

def test_root_works():
    response = client.get("/")
    assert response.status_code == 200

def test_add_book():
    response = client.post("/books", json={
        "title": "Чистый код", "author": "Мартин", "year": 2008, "pages": 464
    })
    assert response.status_code == 200
    assert response.json()["added"] == "Чистый код"

def test_negative_pages_rejected():
    response = client.post("/books", json={
        "title": "Плохая", "author": "X", "year": 2020, "pages": -10
    })
    assert response.status_code == 422
