# https://leetcode.cn/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        now = 0
        n = len(nums)
        while now < n - 1:
            # [now + 1, right]
            right = now + nums[now]
            if right >= n - 1:
                return ans + 1
            next_now = now
            next_right = right
            for i in range(now + 1, right + 1):
                if i + nums[i] > next_right:
                    next_right = i + nums[i]
                    next_now = i
            ans += 1
            now = next_now
        return ans
