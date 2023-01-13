# Write your test here
from challenge02 import first_repeated_word
import pytest

def test1_first_repeated_word():
    expected = "ASAC"
    actual = first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
    assert actual == expected

def test2_first_repeated_word():
    expected = "no repetition"
    actual = first_repeated_word("I am learning programming at ASAC.")
    assert actual == expected

def test3_first_repeated_word():
    expected = "Python"
    actual = first_repeated_word("Python is Python")
    assert actual == expected

