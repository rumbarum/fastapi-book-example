import os

os.environ["UNIT_TEST"] = "true"
import mod2


def test_summer_fake():
    assert mod2.summer(5, 6) == "11"
