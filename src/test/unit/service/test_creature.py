import os

os.environ["CRYPTID_UNIT_TEST"] = "true"
import pytest

from model.creature import Creature
from error import Missing, Duplicate
from data import creature as data


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Handsome Himalayan",
    )


def test_create(sample):
    resp = data.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = data.create(sample)


def test_get_exists(sample):
    resp = data.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = data.get_one("boxturtle")


def test_modify(sample):
    sample.country = "CA"  # Canada!
    resp = data.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    bob: Creature = Creature(name="bob", country="US", area="*", description="some guy", aka="??")
    with pytest.raises(Missing):
        _ = data.modify(bob.name, bob)
