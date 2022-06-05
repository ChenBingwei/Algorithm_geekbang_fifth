# https://leetcode.cn/problems/jump-game-ii/

from typing import List


class Solution:
    # 超时
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        f = [int(float("inf")) for _ in range(n)]
        f[0] = 0

        for i in range(n):
            for j in range(i):
                if i - j <= nums[j]:
                    f[i] = min(f[i], f[j] + 1)
        return f[n - 1]


class Solution_II:
    def jump(self, nums: List[int]) -> int:
        max_len = 0
        end = 0
        ans = 0
        n = len(nums)
        for i in range(n - 1):
            max_len = max(max_len, i + nums[i])
            if i == end:
                end = max_len
                ans += 1
        return ans
