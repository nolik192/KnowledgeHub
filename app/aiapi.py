import httpx

async def ask_llm(prompt, system=None):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            "http://localhost:11434/api/chat",
            json={"model": "qwen2.5:7b", "messages": messages, "stream": False}
        )
    return response.json()["message"]["content"]

if __name__ == "__main__":
    import asyncio
    result = asyncio.run(ask_llm(input("Enter your prompt: ")))
    print(result)