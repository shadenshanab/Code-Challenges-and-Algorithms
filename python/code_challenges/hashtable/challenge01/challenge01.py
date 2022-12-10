class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# root = [7,2,9,1,5,null,14], k = 3
test = TreeNode(7)
test.right = TreeNode(2)
test.left = TreeNode(9)
test.right.right = TreeNode(1)
test.right.left = TreeNode(5)
test.left.left = TreeNode(14)


print(test.value)


def findTarget(Node, k):
    '''
     Node type: TreeNode
     k type : int
     rtype: boolean
    '''
    l = set()

    def dfs(node):
        if not node:
            return False
        y = k - node.value
        if y in l:
            return True
        else:
            l.add(node.value)
        return dfs(node.left) or dfs(node.right)

    return dfs(Node)


print(findTarget(test, 15))
