class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n-1,-1,-1):
            if s[i] == " " and ans > 0:
                return ans
            if s[i] != " ":
                ans += 1
        return ans
