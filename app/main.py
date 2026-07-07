# app/main.py
from fastapi import FastAPI

app = FastAPI()

# временное хранилище в памяти (потом заменим на БД)
tasks = ["Выучить FastAPI", "Построить RAG", "Найти работу"]

@app.get("/")
def read_root():
    return {"message": "Task API работает"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.get("/tasks/{index}")
def get_task(index: int):
    if 0 <= index < len(tasks):
        return {"task": tasks[index]}
    return {"error": "Задача не найдена"}