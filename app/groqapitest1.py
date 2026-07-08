import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Chat:
    def __init__(self, system=None):
        self.history = []
        if system:
            self.history.append({"role": "system", "content": system})

    def send(self, prompt):
        self.history.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.history,
        )
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply


DOCS_SYSTEM = """Ты — ассистент по документации. Правила:
- Отвечай ТОЛЬКО на основе предоставленного контекста.
- Если ответа нет в контексте — честно скажи: «В документации этого нет.»
- Никогда не придумывай факты, не строй догадок.
- Формат ответа: маркированный список пунктов (каждый пункт с «- »).
- Если ответ однозначен и состоит из одного факта — всё равно оформи как список из одного пункта."""


def answer_with_context(context: str, question: str) -> str:
    prompt = f"""Контекст:
{context}

Вопрос: {question}"""
    chat = Chat(system=DOCS_SYSTEM)
    return chat.send(prompt)


if __name__ == "__main__":
    docs = """
    FastAPI — это современный веб-фреймворк для Python, основанный на стандартных аннотациях типов.
    Он поддерживает асинхронный код через async/await.
    Автоматически генерирует документацию Swagger UI по адресу /docs.
    Минимальная поддерживаемая версия Python — 3.8.
    """

    print("=== Вопрос, ответ на который ЕСТЬ в контексте ===")
    answer = answer_with_context(docs, "По какому адресу доступна документация Swagger?")
    print(answer)

    print("\n=== Вопрос, ответа на который НЕТ в контексте ===")
    answer = answer_with_context(docs, "Сколько звёзд у FastAPI на GitHub?")
    print(answer)

    print("\n=== Проверка формата списка ===")
    answer = answer_with_context(docs, "Какие ключевые особенности FastAPI?")
    print(answer)