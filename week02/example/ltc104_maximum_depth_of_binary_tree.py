class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
