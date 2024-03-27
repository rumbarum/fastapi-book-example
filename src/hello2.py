# 3-11
# uvicorn hello2:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"
