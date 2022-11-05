class Node:
    '''class node to initialise nodes for the tree'''

    def __init__(self, value):
        '''constructor to initialise the values'''
        self.value = value
        self.left = None
        self.right = None


class Tree:
    '''class tree to define root'''

    def __init__(self):
        self.root = None


def buildTree(preorder, inorder):
    '''this function creates the tree by looping through it using recursion
    and comparing the values to the root value and so on'''
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = Node(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind + 1:])
        return root
