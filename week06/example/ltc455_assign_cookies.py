# https://leetcode.cn/problems/assign-cookies/

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        ans = 0
        for child in g:
            while j < len(s) and s[j] < child:
                j += 1
            if j < len(s):
                ans += 1
                j += 1
        return ans
