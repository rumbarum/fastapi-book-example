import os
import pytest
from model.user import PublicUser, PrivateUser, SignInUser
from error import Missing, Duplicate
from service.user import get_hash

# set this before data.init import below
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import user


@pytest.fixture
def sample_sign_in() -> SignInUser:
    return SignInUser(name="Mike", password="1234")


@pytest.fixture
def sample_public() -> PublicUser:
    return PublicUser(name="John")


def test_create(sample_sign_in):
    private_user = PrivateUser(name=sample_sign_in.name, hash=get_hash(sample_sign_in.password))
    resp = user.create(private_user)
    assert resp.name == sample_sign_in.name


def test_create_duplicate(sample_sign_in):
    private_user = PrivateUser(name=sample_sign_in.name, hash=get_hash(sample_sign_in.password))
    with pytest.raises(Duplicate):
        _ = user.create(private_user)


def test_get_one(sample_sign_in):
    public_user = PublicUser(name=sample_sign_in.name)
    resp = user.get_one(sample_sign_in.name)
    assert resp == public_user


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = user.get_one("boxturtle")


def test_modify(sample_sign_in, sample_public):
    resp = user.modify(sample_sign_in.name, sample_public)
    assert resp == sample_public


def test_modify_missing():
    one: PublicUser = PublicUser(name="James")
    the_other: PublicUser = PublicUser(name="Bond")
    with pytest.raises(Missing):
        _ = user.modify(one.name, the_other)


def test_delete(sample_public):
    resp = user.delete(sample_public.name)
    assert resp is None


def test_delete_missing(sample_public):
    with pytest.raises(Missing):
        _ = user.delete(sample_public.name)
