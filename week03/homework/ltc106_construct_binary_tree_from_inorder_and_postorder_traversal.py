# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.inorder = []
        self.postorder = []
        self.inorder_index = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.postorder = postorder
        # Both inorder and postorder consist of different values
        for i, v in enumerate(self.inorder):
            self.inorder_index[v] = i
        return self.build(0, len(inorder) - 1, 0, len(postorder) - 1)

    def build(self, inorder_left, inorder_right, postorder_left, postorder_right):
        if postorder_right < postorder_left:
            return
        root = TreeNode(self.postorder[postorder_right])
        inorder_mid = self.inorder_index[self.postorder[postorder_right]]
        inorder_left_length = inorder_mid - inorder_left
        root.left = self.build(inorder_left, inorder_left + inorder_left_length - 1,
                               postorder_left, postorder_left + inorder_left_length - 1)
        root.right = self.build(inorder_mid + 1, inorder_right,
                                # postorder_left + inorder_left_length -1 + 1, postorder_right - 1)
                                postorder_left + inorder_left_length, postorder_right - 1)
        return root
