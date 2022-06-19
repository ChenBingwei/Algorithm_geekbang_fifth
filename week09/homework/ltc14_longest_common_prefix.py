from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        while True:
            is_break = False
            ss = ""
            for s in strs:
                if i == len(s):
                    is_break = True
                    break
                if not ss:
                    ss = s[i]
                if s[i] != ss:
                    is_break = True
                    break
            if is_break:
                break
            ans += ss
            i += 1
        return ans
