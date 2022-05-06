# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root is None:
            return False, False
        left_p, left_q = self.dfs(root.left)
        right_p, right_q = self.dfs(root.right)
        have_p = left_p or right_p or root.val == self.p.val
        have_q = left_q or right_q or root.val == self.q.val
        if have_p and have_q and self.ans is None:
            self.ans = root
        return have_p, have_q
