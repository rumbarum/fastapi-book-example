import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


@app.get("/who2")
def greet2(name: str = Form()):
    return f"Hello, {name}?"


from pathlib import Path
from fastapi.staticfiles import StaticFiles

# main.py 파일이 있는 디렉토리:
top = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=f"{top}/static", html=True), name="free")


@app.post("/who2")
def greet3(name: str = Form()):
    return f"Hello, {name}?"


from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

top = Path(__file__).resolve().parent

template_obj = Jinja2Templates(directory=f"{top}/template")

# 미리 정의된 친구들 목록을 가져온다
from fake.creature import _creatures as fake_creatures
from fake.explorer import _explorers as fake_explorers


@app.get("/list")
def explorer_list(request: Request):
    return template_obj.TemplateResponse(
        "list.html", {"request": request, "explorers": fake_explorers, "creatures": fake_creatures}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
