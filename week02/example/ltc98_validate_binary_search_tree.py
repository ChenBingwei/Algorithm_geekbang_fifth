# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self.check_tree(root, float('-inf'), float('inf'))

    def check_tree(self, root, min_value, max_value):
        if root is None: return True
        if root.val < min_value or root.val > max_value: return False
        return self.check_tree(root.left, min_value, root.val - 1) and \
               self.check_tree(root.right, root.val + 1, max_value)
