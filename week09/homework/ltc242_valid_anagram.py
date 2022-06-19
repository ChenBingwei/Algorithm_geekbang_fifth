from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for ss in s:
            s_map[ss] += 1
        for tt in t:
            t_map[tt] += 1
        return s_map == t_map
