# Write your test here
import pytest
from challenge03 import sortedArrayToBST

def test_tree1():
    nums = []
    actual = sortedArrayToBST(nums)
    expected = None
    assert actual == expected

def test_tree2():
    nums = [-2,-1,0,1,2]
    actual = sortedArrayToBST(nums).value
    expected = 0
    assert actual == expected

def test_tree3():
    nums = [1,4,6,7,13,15,16]
    actual = sortedArrayToBST(nums).value
    expected = 7
    assert actual == expected

def test_tree4():
    nums = [1,9]
    actual = sortedArrayToBST(nums).value
    expected = 9
    assert actual == expected