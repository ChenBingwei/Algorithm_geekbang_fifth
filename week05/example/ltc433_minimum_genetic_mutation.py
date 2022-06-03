# https://leetcode.cn/problems/minimum-genetic-mutation/

from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        str_list = ["A", "C", "G", "T"]
        hash_bank = set()
        for b in bank:
            hash_bank.add(b)
        if end not in hash_bank:
            return -1
        depth = {start: 0}
        q = deque()
        q.append(start)
        while q:
            cur_str = q.popleft()
            for i in range(8):
                for j in range(4):
                    if cur_str[i] == str_list[j]:
                        continue
                    tmp_list = list(cur_str)
                    tmp_list[i] = str_list[j]
                    ns = "".join(tmp_list)
                    if ns not in hash_bank:
                        continue
                    if ns in depth:
                        continue
                    if ns == end:
                        return depth[cur_str] + 1
                    q.append(ns)
                    depth[ns] = depth[cur_str] + 1
        return -1
