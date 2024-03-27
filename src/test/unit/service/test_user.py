from fastapi import HTTPException
import pytest
import os

os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.user import SignInUser, PublicUser, PrivateUser
from service import user
from error import Missing, Duplicate


@pytest.fixture
def sample_sign_in() -> SignInUser:
    return SignInUser(name="Tom", password="1234")


@pytest.fixture
def sample_public() -> PublicUser:
    return PublicUser(name="Jerry")


@pytest.fixture
def fakes() -> list[PublicUser]:
    return user.get_all()


def test_create(sample_sign_in):
    public_user = PublicUser(name=sample_sign_in.name)
    assert user.create(sample_sign_in) == public_user


def test_create_duplicate(fakes):
    with pytest.raises(Exception) as exc:
        fake_user = SignInUser(name=fakes[0].name, password="1234")
        _ = user.create(fake_user)
        assert isinstance(exc, Duplicate) == True


def test_get_one(fakes):
    assert user.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(Exception) as exc:
        _ = user.get_one("bobcat")
        assert isinstance(exc, Missing) == True
