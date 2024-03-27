from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
