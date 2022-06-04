# https://leetcode.cn/problems/lemonade-change/

from typing import List


class Solution:
    def __init__(self):
        self.coins = {
            20: 0,
            10: 0,
            5: 0
        }

    def lemonadeChange(self, bills: List[int]) -> bool:
        for bill in bills:
            self.coins[bill] += 1
            if not self.check(bill - 5):
                return False
        return True

    def check(self, bill):
        for i in [20, 10, 5]:
            while bill >= i and self.coins[i] > 0:
                bill -= i
                self.coins[i] -= 1

        return bill == 0
