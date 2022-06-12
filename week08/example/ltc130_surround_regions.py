from typing import List


class Solution:
    def __init__(self):
        self.fa = []
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        self.m = 0
        self.n = 0

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        outside = self.m * self.n
        for i in range(self.m * self.n + 1):
            self.fa.append(i)

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'X':
                    continue
                for k in range(4):
                    ni = i + self.dx[k]
                    nj = j + self.dy[k]
                    if ni < 0 or nj < 0 or ni >= self.m or nj >= self.n:
                        self.union_set(self.nums(i, j), outside)
                    elif board[ni][nj] == 'O':
                        self.union_set(self.nums(i, j), self.nums(ni, nj))

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O' and (self.find(self.nums(i, j)) != self.find(outside)):
                    board[i][j] = 'X'

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

    def nums(self, i, j):
        return i * self.n + j
