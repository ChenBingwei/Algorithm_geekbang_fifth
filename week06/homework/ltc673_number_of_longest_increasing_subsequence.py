# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1 for _ in range(n)]
        count = [1 for _ in range(n)]
        max_len = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if f[j] + 1 > f[i]:
                        count[i] = count[j]
                        f[i] = max(f[i], f[j] + 1)
                    elif f[j] + 1 == f[i]:
                        count[i] += count[j]
            max_len = max(max_len, f[i])
        ans = 0
        for i in range(n):
            if f[i] == max_len:
                ans += count[i]
        return ans
