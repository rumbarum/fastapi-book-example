from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/hi")
def greet(who: str = Header()):
    return f"Hello? {who}?"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
