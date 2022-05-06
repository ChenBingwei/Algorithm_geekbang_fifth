from typing import List


class Solution:

    def __init__(self):
        self.edge_array = []
        self.max_n = 0
        self.visited = []
        self.have_cycle = False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for a, b in edges:
            self.max_n = max(self.max_n, a, b)
        self.edge_array = [[] for _ in range(self.max_n + 1)]
        self.visited = [False] * (self.max_n + 1)
        for a, b in edges:
            self.edge_array[a].append(b)
            self.edge_array[b].append(a)

            self.dfs(a, 0)
            if self.have_cycle:
                return [a, b]
        return []

    def dfs(self, node, farther):
        self.visited[node] = True
        for i in self.edge_array[node]:
            if i == farther: continue
            if not self.visited[i]:
                self.dfs(i, node)
            else:
                self.have_cycle = True
                return
        self.visited[node] = False
