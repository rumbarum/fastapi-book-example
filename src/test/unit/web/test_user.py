from fastapi import HTTPException
import pytest
import os

os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.user import SignInUser, PublicUser, PrivateUser
from web import user
from error import Missing, Duplicate


@pytest.fixture
def sample_sign_in() -> SignInUser:
    return SignInUser(name="Pa Tuohy", password="...")


@pytest.fixture
def sample_public() -> PublicUser:
    return PublicUser(name="Bob")


@pytest.fixture
def fakes() -> list[PublicUser]:
    return user.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 404
    assert "Duplicate" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.msg


def test_create(sample_sign_in):
    public_user = PublicUser(name=sample_sign_in.name)
    assert user.create(sample_sign_in) == public_user


def test_create_duplicate(fakes):
    with pytest.raises(Exception) as exc:
        sign_in_user = SignInUser(name=fakes[0].name, password="...")
        resp = user.create(sign_in_user)
        assert_duplicate(exc)


def test_get_one(fakes):
    assert user.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(Exception) as exc:
        resp = user.get_one("Buffy")
        assert_missing(exc)


def test_modify(fakes, sample_public):
    assert user.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample_public):
    with pytest.raises(HTTPException) as exc:
        resp = user.modify(sample_public.name, sample_public)
        assert_missing(exc)


def test_delete(fakes):
    assert user.delete(fakes[0].name) is None


def test_delete_missing(sample_public):
    with pytest.raises(HTTPException) as exc:
        resp = user.delete("Wally")
        assert_missing(exc)
