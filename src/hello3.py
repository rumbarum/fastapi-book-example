# 3-15
# uvicorn hello3:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"
