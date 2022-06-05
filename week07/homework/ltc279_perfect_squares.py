# https://leetcode.cn/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        f = [float("inf") for _ in range(n + 1)]
        f[0] = 0
        idx = 1
        while idx * idx <= n:
            for j in range(1, n + 1):
                if j - idx * idx >= 0:
                    f[j] = min(f[j - idx * idx] + 1, f[j])

            idx += 1
        return f[n]
