# https://leetcode.cn/problems/triangle/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0 for _ in range(n)] for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    f[i][j] = f[i - 1][j] + triangle[i][j]
                elif j == i:
                    f[i][j] = f[i - 1][j - 1] + triangle[i][j]
                else:
                    f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
        ans = int(1e4)
        for s in f[n - 1]:
            ans = min(ans, s)
        return ans


class Solution_II:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0 for _ in range(n)]
        f[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i, -1, -1):
                if j == 0:
                    f[j] = f[j] + triangle[i][j]
                elif j == i:
                    f[j] = f[j - 1] + triangle[i][j]
                else:
                    f[j] = min(f[j], f[j - 1]) + triangle[i][j]
        return min(f)
