from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])
        d = defaultdict(int)
        ans = 0
        for num in prefix:
            if num - k in d:
                ans += d[num - k]
            d[num] += 1
        return ans

class Solution_II:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * (n+1)
        for i in range(1,n+1):
            s[i] = s[i-1] + nums[i-1] % 2
        count = [0] * (n+1)
        count[s[0]] += 1
        ans = 0
        for i in range(1,n+1):
            if s[i] - k >=0:
                ans += count[s[i] - k]
            count[s[i]] += 1
        return ans



