# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        return self.get_next(root, p.val)

    def get_next(self, root, val):
        ans = None
        curr = root
        while curr:
            if curr.val == val:
                if curr.right:
                    ans = curr.right
                    while ans.left:
                        ans = ans.left
                break

            if curr.val < val:
                curr = curr.right
            else:
                if ans is None or ans.val > curr.val:
                    ans = curr
                curr = curr.left
        return ans
