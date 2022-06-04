# https://leetcode.cn/problems/coin-change/submissions/

from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.depth = {}
        self.q = deque()

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        self.depth[amount] = 0
        self.q.append(amount)

        while self.q:
            amount_remain = self.q.popleft()
            for i in range(len(coins)):
                b = amount_remain - coins[i]
                if b < 0: continue
                if b in self.depth:
                    continue
                self.depth[b] = self.depth[amount_remain] + 1
                if b == 0:
                    return self.depth[b]
                self.q.append(b)

        return -1
