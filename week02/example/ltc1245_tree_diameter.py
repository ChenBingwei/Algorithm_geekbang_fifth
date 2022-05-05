from queue import Queue
from typing import List


class Solution:
    def __init__(self):
        self.edge_array = []
        self.max_node = 0

    def treeDiameter(self, edges: List[List[int]]) -> int:
        for x, y in edges:
            self.max_node = max(x, y)
        self.max_node += 1
        self.edge_array = [[] for _ in range(self.max_node)]
        for x, y in edges:
            self.edge_array[x].append(y)
            self.edge_array[y].append(x)
        node, depth = self.findFarthest(0)
        node2, depth2 = self.findFarthest(node)
        return depth2

    def findFarthest(self, node):
        q = Queue()
        q.put(node)
        depth_list = [-1] * self.max_node
        depth_list[node] = 0
        while not q.empty():
            front_node = q.get()
            for i in self.edge_array[front_node]:
                if depth_list[i] != -1:
                    continue
                depth_list[i] = depth_list[front_node] + 1
                q.put(i)
        ans = node
        for k, v in enumerate(depth_list):
            if v > depth_list[ans]:
                ans = k
        return (ans, depth_list[ans])
