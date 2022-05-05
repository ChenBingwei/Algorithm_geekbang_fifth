# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.preorder = []
        self.inorder = []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder
        return self.build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def build(self, pre_l, pre_r, in_l, in_r):
        if pre_l > pre_r:
            return None
        root = TreeNode(self.preorder[pre_l])
        mid = self.inorder.index(self.preorder[pre_l])
        left_length = mid - in_l
        root.left = self.build(pre_l + 1, pre_l + 1 + left_length - 1, in_l, mid - 1)
        root.right = self.build(pre_l + 1 + left_length, pre_r, mid + 1, in_r)
        return root
