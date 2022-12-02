import pytest
from challenge02 import *

def test_empty():
    '''test an empty linked list'''
    llist = LinkedList()

    expected = "linked list is empty"
    actual = llist.printAll()

    assert actual ==expected
def test_middle_node_even():
    '''test even number middle node'''
    llist = LinkedList()
    node1 = Node(66)
    node2 = Node(45)
    node3 = Node(29)
    node4 = Node(72)
    node5 = Node(12)
    node6 = Node(99)
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.append(node4)
    llist.append(node5)
    llist.append(node6)

    expected = node4
    actual = llist.middleNode()
    assert actual == expected

def test_middle_node_odd():
    '''test odd number middle node'''
    llist = LinkedList()
    node1 = Node(66)
    node2 = Node(45)
    node3 = Node(29)
    node4 = Node(72)
    node5 = Node(12)
    llist.append(node1)
    llist.append(node2)
    llist.append(node3)
    llist.append(node4)
    llist.append(node5)

    expected = node3
    actual = llist.middleNode()
    assert actual == expected

    
