import pytest

from challenge01 import TreeNode, findTarget


def test_TreeNode_one():

    TreeNode1 = TreeNode(7)
    TreeNode1.left = TreeNode(2)
    TreeNode1.left.left = TreeNode(1)
    TreeNode1.left.right = TreeNode(5)
    TreeNode1.right = TreeNode(9)
    TreeNode1.right.right = TreeNode(14)
    actual = findTarget(TreeNode1, 3)
    expected = True
    assert actual == expected


def test_TreeNode_two():

    TreeNode1 = TreeNode(7)
    TreeNode1.left = TreeNode(2)
    TreeNode1.left.left = TreeNode(1)
    TreeNode1.left.right = TreeNode(5)
    TreeNode1.right = TreeNode(9)
    TreeNode1.right.right = TreeNode(14)
    actual = findTarget(TreeNode1, 4)
    expected = False
    assert actual == expected


def test_TreeNode_three():

    test = TreeNode()
    actual = findTarget(test, 7)
    excepted = False
    assert excepted == actual
