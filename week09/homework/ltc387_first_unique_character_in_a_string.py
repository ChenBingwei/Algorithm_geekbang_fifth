from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for ss in s:
            count[ss] += 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


