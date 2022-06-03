from collections import defaultdict
from typing import List


class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.n = 0
        self.used = []
        self.used_up = defaultdict(bool)
        self.used_down = defaultdict(bool)
        self.permutation = []
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.used = [False for _ in range(self.n)]
        self.dfs(0)
        self.result = []

        for l in self.ans:
            pattern = [["." for _ in range(self.n)] for _ in range(self.n)]
            for i, j in enumerate(l):
                pattern[i][j] = "Q"
                pattern[i] = "".join(pattern[i])
            self.result.append(pattern)
            # for i in range(self.n):
            #     pattern[i] = "".join(pattern[i])
        return self.result

    def dfs(self, row):
        if row == self.n:
            self.ans.append(self.permutation.copy())
            return

        for col in range(self.n):
            if not self.used[col] and not self.used_up[row + col] and not self.used_down[row - col]:
                self.used[col] = True
                self.used_down[row - col] = True
                self.used_up[row + col] = True
                self.permutation.append(col)
                self.dfs(row + 1)
                self.permutation.pop()
                self.used_up[row + col] = False
                self.used_down[row - col] = False
                self.used[col] = False



