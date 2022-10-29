import pytest
from challenge01 import Queue


def test_push(q):
    q.push(4)
    actual = q.peek()
    expected = 1
    assert actual == expected


def test_pop(q):
    actual = q.pop()
    expected = 1
    assert actual == expected


def test_peek():
    emptyQueue = Queue()
    actual = emptyQueue.peek()
    expected = "This queue is empty"
    assert actual == expected


def test_isEmpty(q):
    actual = q.isEmpty()
    expected = False
    assert actual == expected


@pytest.fixture
def q():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    return q
