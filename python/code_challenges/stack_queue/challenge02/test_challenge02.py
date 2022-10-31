import pytest
from challenge02 import is_valid


def test_is_valid_1():
    actual = is_valid("()")
    expected = True
    assert actual == expected


def test_is_valid_2():
    actual = is_valid("()[]{}")
    expected = True
    assert actual == expected


def test_is_valid_3():
    actual = is_valid("(}")
    expected = False
    assert actual == expected


def test_is_valid_4():
    actual = is_valid("[(hello)()]")
    expected = True
    assert actual == expected


def test_is_valid_5():
    actual = is_valid("[{(())}]")
    expected = True
    assert actual == expected


