from typing import List


class Solution:

    def __init__(self):
        self.fa = []

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        for i in range(n):
            self.fa.append(i)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.union_set(i, j)

        ans = 0
        for i in range(n):
            if self.find(i) == i:
                ans += 1
        return ans

    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
