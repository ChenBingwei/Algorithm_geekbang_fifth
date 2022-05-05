# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        seq = []
        queue = []
        queue.append([root, 0])
        while queue:
            node, depth = queue.pop(0)
            if depth >= len(seq):
                seq.append([])
            seq[depth].append(node.val)
            if not node.children:
                continue
            for i in node.children:
                queue.append([i, depth + 1])
        return seq

    def levelOrder2(self, root):
        if root is None:
            return []
        from queue import Queue
        q = Queue()
        seq = []
        q.put((root, 0))
        while not q.empty():
            node, depth = q.get()
            if depth >= len(seq):
                seq.append([])
            seq[depth].append(node.val)
            if not node.children:
                continue
            for child in node.children:
                q.put((child, depth + 1))
        return seq
