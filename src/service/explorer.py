import os
from model.explorer import Explorer

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import explorer as data
else:
    from src.data import explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> Explorer | None:
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def replace(name, explorer: Explorer) -> Explorer:
    return data.replace(name, explorer)


def modify(name, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)


def delete(name: str) -> bool:
    return data.delete(name)
