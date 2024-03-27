# 3-21
# uvicorn hello4:app --reload
from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"
