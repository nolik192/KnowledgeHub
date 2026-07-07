from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()
books = []

class BookIn(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    @field_validator("pages")
    @classmethod
    def valid_pages(cls, v):
        if v <= 0:
            raise ValueError("pages must be a positive integer")
        return v

@app.get("/")
def root():
    return {"message": "Library API is running"}

@app.get("/books")
def list_books():
    return {"books": books}

@app.post("/books")
def add_book(book: BookIn):
    books.append(book.model_dump())   # model_dump() — Pydantic v2 (не .dict()!)
    return {"added": book.title, "total": len(books)}