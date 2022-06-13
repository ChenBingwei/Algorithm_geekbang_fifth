from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0]
        for i in range(1, n + 1):
            s.append(s[i - 1] + nums[i - 1])
        pre_min = [0]
        for i in range(1, n + 1):
            pre_min.append(min(pre_min[i - 1], s[i]))
        ans = - 10 ** 9
        for r in range(1, n + 1):
            ans = max(ans, s[r] - pre_min[r - 1])
        return ans
