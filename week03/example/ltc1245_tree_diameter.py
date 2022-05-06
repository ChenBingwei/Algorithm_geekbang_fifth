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


class Solution2:

    def __init__(self):
        self.edge_dict = {}
        self.visited = {}
        self.max_depth = 0
        self.dest_node = 0

    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        for x, y in edges:
            self.edge_dict.setdefault(x, [])
            self.edge_dict.setdefault(y, [])
            self.edge_dict[x].append(y)
            self.edge_dict[y].append(x)
        self.visited = {x: False for x in self.edge_dict}
        self.dfs_find_furthest(0, 0)
        self.max_depth = 0
        self.dfs_find_furthest(self.dest_node, 0)
        return self.max_depth

    def dfs_find_furthest(self, node, depth):
        if self.visited[node]:
            return
        self.visited[node] = True
        if self.max_depth < depth:
            self.max_depth = depth
            self.dest_node = node
        for i in self.edge_dict[node]:
            self.dfs_find_furthest(i, depth + 1)
        self.visited[node] = False
