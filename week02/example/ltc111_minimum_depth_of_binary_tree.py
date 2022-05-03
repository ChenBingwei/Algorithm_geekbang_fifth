# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)

        if root.left and not root.right:
            return 1 + self.minDepth(root.left)

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
