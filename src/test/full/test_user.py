import pytest
from fastapi.testclient import TestClient
from model.user import SignInUser, PrivateUser, PublicUser
from main import app

client = TestClient(app)


@pytest.fixture
def sample_sign_in() -> SignInUser:
    return SignInUser(name="elsa", password="123")


@pytest.fixture
def sample_public() -> PublicUser:
    return PublicUser(name="elle")


def test_create(sample_sign_in):
    resp = client.post("/user", json=sample_sign_in.model_dump())
    assert resp.status_code == 201


def test_create_duplicate(sample_sign_in):
    resp = client.post("/user", json=sample_sign_in.model_dump())
    assert resp.status_code == 409


def test_get_one(sample_sign_in):
    resp = client.get(f"/user/{sample_sign_in.name}")
    assert resp.json() == sample_sign_in.dict(exclude={"password"})


def test_get_one_missing():
    resp = client.get("/user/bobcat")
    assert resp.status_code == 404


def test_modify(sample_sign_in, sample_public):
    resp = client.patch(f"/user/{sample_sign_in.name}", json=sample_public.model_dump())
    assert resp.json() == sample_public.model_dump()


def test_modify_missing(sample_public):
    resp = client.patch("/user/dumbledore", json=sample_public.model_dump())
    assert resp.status_code == 404


def test_delete(sample_public):
    resp = client.delete(f"/user/{sample_public.name}")
    assert resp.json() is None
    assert resp.status_code == 200


def test_delete_missing(sample_public):
    resp = client.delete(f"/user/{sample_public.name}")
    assert resp.status_code == 404
