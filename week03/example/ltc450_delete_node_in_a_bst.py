# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        if root.val == key:
            if root.left is None: return root.right
            if root.right is None: return root.left
            next_node = root.right
            while next_node.left:
                next_node = next_node.left
            root.right = self.deleteNode(root.right, next_node.val)
            root.val = next_node.val
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
