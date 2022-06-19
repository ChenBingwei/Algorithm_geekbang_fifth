class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for a in s:
            if ord(a) in range(ord("A"), ord("Z") + 1):
                ans += chr(ord(a) - ord("A") + ord("a"))
            else:
                ans += a
        return ans
