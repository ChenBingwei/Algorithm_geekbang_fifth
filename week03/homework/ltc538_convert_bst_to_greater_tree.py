# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root):
        dest_num = 0

        def dfs(root):
            nonlocal dest_num
            if root is None:
                return
            dfs(root.right)
            dest_num += root.val
            root.val = dest_num
            dfs(root.left)

        dfs(root)

        return root
