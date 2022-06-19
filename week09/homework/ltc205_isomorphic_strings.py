class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_str = s[i]
            t_str = t[i]
            if (s_str in s_map and s_map[s_str] != t_str) or (t_str in t_map and t_map[t_str] != s_str):
                return False
            s_map[s_str] = t_str
            t_map[t_str] = s_str
        return True
