class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        tmp_str = ""
        for ss in s:
            if ss != " ":
                if tmp_str:
                    tmp_str += ss
                else:
                    tmp_str = ss
            elif tmp_str:
                ans = tmp_str + " " + ans
                tmp_str = ""
        if tmp_str:
            ans = tmp_str + " " + ans
        return ans[:-1]
