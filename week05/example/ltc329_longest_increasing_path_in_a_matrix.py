# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/

from collections import deque
from typing import List


class Solution_BFS:
    def __init__(self):
        self.deg = []
        self.dist = []
        self.to = []
        self.m = 0
        self.n = 0
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        self.q = deque()

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        self.m = len(matrix)
        self.n = len(matrix[0])
        self.to = [[] for _ in range(self.m * self.n)]
        self.deg = [0 for _ in range(self.m * self.n)]
        self.dist = [0 for _ in range(self.m * self.n)]
        for i in range(self.m):
            for j in range(self.n):
                for k in range(4):
                    nx = i + self.dx[k]
                    ny = j + self.dy[k]
                    if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n:
                        continue
                    if matrix[nx][ny] > matrix[i][j]:
                        self.add_edge(self.num(i, j), self.num(nx, ny))

        for i in range(self.m * self.n):
            if self.deg[i] == 0:
                self.q.append(i)
                self.dist[i] = 1
        while self.q:
            x = self.q.popleft()
            for y in self.to[x]:
                self.deg[y] -= 1
                self.dist[y] = max(self.dist[y], self.dist[x] + 1)
                if self.deg[y] == 0:
                    self.q.append(y)
        ans = 0
        for i in range(self.m * self.n):
            ans = max(ans, self.dist[i])
        return ans

    def num(self, i, j):
        return i * self.n + j

    def add_edge(self, u, v):
        self.deg[v] += 1
        self.to[u].append(v)


class Solution_DFS:

    def __init__(self):
        self.m = None
        self.n = None
        self.matrix = None
        self.dx = None
        self.dy = None
        self.dist = None

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        self.dist = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(i, j))
        return ans

    def dfs(self, x, y) -> int:
        if self.dist[x][y] != 0:
            return self.dist[x][y]
        self.dist[x][y] = 1
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n:
                continue
            if self.matrix[nx][ny] > self.matrix[x][y]:
                self.dist[x][y] = max(self.dist[x][y], self.dfs(nx, ny) + 1)
        return self.dist[x][y]
