# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def __init__(self):
        self.seq = []

    def preorder(self, root: 'Node') -> List[int]:
        self.dfs(root)
        return self.seq

    def dfs(self, root):
        if root is None: return
        self.seq.append(root.val)
        for i in root.children:
            self.dfs(i)

    def preorder2(self, root: 'Node') -> List[int]:
        if root is None: return []
        stack = []
        stack.append(root)
        while stack:
            self.seq.append(stack[-1].val)
            out_node = stack.pop()
            if out_node.children:
                for i in out_node.children[-1::-1]:
                    stack.append(i)

        return self.seq
