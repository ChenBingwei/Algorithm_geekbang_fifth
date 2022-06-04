# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(prices[i] - prices[i - 1], 0)
        return ans
