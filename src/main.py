from fastapi import FastAPI
from web import creature, explorer

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

from fastapi import File


@app.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"


from fastapi import UploadFile


@app.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"


from fastapi.responses import FileResponse


@app.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)


from typing import Generator
from fastapi.responses import StreamingResponse


def gen_file(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()


@app.get("/download_big/{name}")
async def download_big_file(name: str):
    gen_expr = gen_file(path=name)
    response = StreamingResponse(
        content=gen_expr,
        status_code=200,
    )
    return response


from pathlib import Path
from fastapi.staticfiles import StaticFiles

# main.py 파일이 있는 디렉토리:
top = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=f"{top}/static", html=True), name="free")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
