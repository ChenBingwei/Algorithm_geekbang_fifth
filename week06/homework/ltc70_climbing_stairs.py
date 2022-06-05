# https://leetcode.cn/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


class Solution_II:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 0
        ans = 1
        for i in range(1, n + 1):
            x, y = y, ans
            ans = x + y
        return ans
