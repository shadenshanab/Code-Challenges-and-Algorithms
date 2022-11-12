class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

def sortedArrayToBST(nums: list[int]):
    total_nums = len(nums)
    if not total_nums:
        return None

    mid_node = total_nums // 2
    return TreeNode(
        nums[mid_node],
        sortedArrayToBST(nums[:mid_node]),
        sortedArrayToBST(nums[mid_node + 1 :]),
    )