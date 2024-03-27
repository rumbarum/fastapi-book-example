import os
import pytest
from model.explorer import Explorer
from error import Missing, Duplicate

# 아래 줄에 있는 data.init에 메모리 DB를 사용하도록 data 모듈을 가져오기 전에 설정한다.
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
# data 모듈 이름 겹쳐서 에러남
from src.data import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Claude Hande",
        country="FR",
        description="보름달이 뜨면 만나기 힘듦",
    )


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)


def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("Newt Scamander")


def test_modify(sample):
    sample.country = "South Korea"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    one: Explorer = Explorer(name="snurfle", country="RU", description="some one")
    with pytest.raises(Missing):
        _ = explorer.modify(one.name, one)


def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is True


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)
