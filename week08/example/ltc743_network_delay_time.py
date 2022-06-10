# https://leetcode.cn/problems/network-delay-time/

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        for _ in range(n - 1):
            flag = False
            for x, y, z in times:
                if dist[y] > dist[x] + z:
                    flag = True
                    dist[y] = dist[x] + z
            if flag is False:
                break

        ans = max(dist[1:])
        return -1 if ans == float("inf") else ans


# Dijkstra
class Solution_II:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        ver_array = [[] for _ in range(n + 1)]
        edge_array = [[] for _ in range(n + 1)]
        for x, y, z in times:
            ver_array[x].append(y)
            edge_array[x].append(z)
        expand = [False for _ in range(n + 1)]
        for a in range(n - 1):
            tmp = float("inf")
            x = k
            for i in range(1, n + 1):
                if expand[i] is False and dist[i] < tmp:
                    tmp = dist[i]
                    x = i
            expand[x] = True
            for i in range(len(ver_array[x])):
                y = ver_array[x][i]
                z = edge_array[x][i]
                if dist[y] > dist[x] + z:
                    dist[y] = dist[x] + z

        ans = 0
        for i in dist[1:]:
            ans = max(ans, i)

        return -1 if ans == float("inf") else ans


class Solution_III:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = []
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        heapq.heappush(q, (0, k))
        ver_array = [[] for _ in range(n + 1)]
        edge_array = [[] for _ in range(n + 1)]
        for x, y, z in times:
            ver_array[x].append(y)
            edge_array[x].append(z)
        expand = [False for _ in range(n + 1)]
        while q:
            _, t_index = heapq.heappop(q)
            if expand[t_index]:
                continue
            expand[t_index] = True
            for i in range(len(ver_array[t_index])):
                y = ver_array[t_index][i]
                z = edge_array[t_index][i]
                if dist[y] > dist[t_index] + z:
                    dist[y] = dist[t_index] + z
                    heapq.heappush(q, (dist[y], y))
        ans = float("-inf")
        for i in range(1, n + 1):
            ans = max(ans, dist[i])
        return -1 if ans == float("inf") else ans
