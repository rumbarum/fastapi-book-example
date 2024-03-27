from unittest import mock
import mod2


def test_caller_a():
    with mock.patch("mod1.preamble", return_value=""):
        assert mod2.summer(5, 6) == "11"


def test_caller_b():
    with mock.patch("mod1.preamble") as mock_preamble:
        mock_preamble.return_value = ""
        assert mod2.summer(5, 6) == "11"


@mock.patch("mod1.preamble", return_value="")
def test_caller_c(mock_preamble):
    assert mod2.summer(5, 6) == "11"


@mock.patch("mod1.preamble")
def test_caller_d(mock_preamble):
    mock_preamble.return_value = ""
    assert mod2.summer(5, 6) == "11"
