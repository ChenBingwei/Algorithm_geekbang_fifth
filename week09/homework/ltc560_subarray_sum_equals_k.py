from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        pre = ans = 0
        for num in nums:
            pre += num
            if pre == k:
                ans += 1
            if pre - k in mp:
                ans += mp[pre - k]
            mp[pre] += 1
        return ans
