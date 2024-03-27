from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()


@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "Hello? World?"
