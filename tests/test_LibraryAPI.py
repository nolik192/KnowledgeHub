from fastapi.testclient import TestClient
from app.FastAPILibrary import app

client = TestClient(app)

# 1
def test_root():
    assert client.get("/").status_code == 200

# 2
def test_add_book_works():
    r = client.post("/books", json={
        "title": "Тест", "author": "Автор", "year": 2021, "pages": 100
    })
    assert r.status_code == 200
    assert r.json()["added"] == "Тест"

# 3
def test_bad_pages():
    r = client.post("/books", json={
        "title": "X", "author": "Y", "year": 2021, "pages": 0
    })
    assert r.status_code == 422

# 4
def test_list_after_add():
    client.post("/books", json={
        "title": "Уникальная", "author": "Z", "year": 2022, "pages": 200
    })
    r = client.get("/books")
    titles = [b["title"] for b in r.json()["books"]]
    assert "Уникальная" in titles