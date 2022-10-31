import pytest
from challenge01 import *


def test_delete():
    '''check if the delete node function is working'''
    llist = LinkedList()
    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(1)
    node4 = Node(9)
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.append(node4)
    deleteNode(node2)

    expected = [4,1,9]
    actual = llist.printAll()
    assert actual == expected


def test_empty():
    '''cjeck if the error message works in case there is no nodes in the linked list'''

    llist = LinkedList()

    expected = "The linked list is empty"
    actual = llist.printAll()

    assert actual ==expected