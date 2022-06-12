from typing import List


class Solution:
    def __init__(self):
        self.fa = []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        for i in range(0, n + 1):
            self.fa.append(i)

        for x, y in edges:
            if self.find(x) != self.find(y):
                self.union_set(x, y)
            else:
                return [x, y]
        return []

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
