# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def __init__(self) -> None:
        self.str_combination = ""
        self.alphabet = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.digits = ""
        self.ans = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits
        self.dfs(0)
        return self.ans

    def dfs(self, index):
        if index == len(self.digits):
            self.ans.append(self.str_combination)
            return

        for alpha in self.alphabet[self.digits[index]]:
            self.str_combination += alpha
            self.dfs(index + 1)
            self.str_combination = self.str_combination[:-1]
