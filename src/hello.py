# 3-1, 3-2
# uvicorn hello:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
def greet():
    return "Hello? World?"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)
