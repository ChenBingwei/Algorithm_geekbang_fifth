from typing import List


class Solution:
    def __init__(self):
        self.fa = []
        self.m = 0
        self.n = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.fa = [i for i in range(self.m * self.n)]
        dx = [0, 1]
        dy = [-1, 0]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != "1":
                    continue
                for k in range(2):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni < 0 or nj < 0 or ni >= self.m or nj >= self.n:
                        continue

                    elif grid[ni][nj] == "1":
                        self._union_set(self._nums(ni, nj), self._nums(i, j))

        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and self.fa[self._nums(i, j)] == self._nums(i, j):
                    ans += 1
        return ans

    def _nums(self, i, j):
        return i * self.n + j

    def _find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self._find(self.fa[x])
        return self.fa[x]

    def _union_set(self, x, y):
        x = self._find(x)
        y = self._find(y)
        if x != y:
            self.fa[x] = y
