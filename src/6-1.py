from fastapi import FastAPI, Depends, Query

app = FastAPI()


# 의존성 함수:
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "valid": True}


# 경로 함수 / 웹 엔드포인트:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user
