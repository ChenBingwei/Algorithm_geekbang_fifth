class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        left = 0
        right = n - 1
        s_list = list(s)
        while left <= right:
            if not self.is_englisht_letter(s[left]):
                left += 1
                continue
            if not self.is_englisht_letter(s[right]):
                right -= 1
                continue
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return "".join(s_list)

    def is_englisht_letter(self, s):
        return ord(s) in range(ord("a"), ord("z") + 1) or ord(s) in range(ord("A"), ord("Z") + 1)
