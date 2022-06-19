class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewset = set(jewels)
        for s in stones:
            if s in jewset:
                ans += 1
        return ans
