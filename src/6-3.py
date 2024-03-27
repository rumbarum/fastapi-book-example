from fastapi import FastAPI, Depends, Query

app = FastAPI()


# 의존성 함수:
def check_dep(name: str = Query(...), gender: str = Query(...)):
    if not name:
        raise


# 경로 함수 / 웹 엔드포인트:
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
