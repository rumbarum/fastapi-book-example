from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)


# 나머지 엔드포인트. 현재는 아무 일도 하지 않는다.
@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)


@router.patch("/{name}")
def modify(name: str, explorer: Explorer) -> Explorer:
    return service.modify(name, explorer)


@router.put("/{name}")
def replace(name: str, explorer: Explorer) -> Explorer:
    return service.replace(name, explorer)


@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
