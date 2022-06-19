from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> List:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left = 0
        right = n - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
