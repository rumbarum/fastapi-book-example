# 3-24
# uvicorn hello5:app --reload
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/hi")
def greet(who: str = Header()):
    return f"Hello? {who}?"
