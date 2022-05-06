from queue import Queue
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for a, b in edges:
            n = max(a, b, n)
        in_degree_list = [-1] + [0] * n
        edge_array = [[] for _ in range(n + 1)]

        for a, b in edges:
            in_degree_list[b] += 1
            edge_array[a].append(b)

        for a, b in edges[-1::-1]:
            # delete a -> b
            in_degree_list[b] -= 1
            edge_array[a].remove(b)  # distinct values
            if in_degree_list.count(0) == 1:  # first is 0
                # bfs
                root = in_degree_list.index(0)
                visited_number = 0  # root
                q = Queue()
                q.put(root)
                while not q.empty():
                    first_node = q.get()
                    visited_number += 1
                    for node in edge_array[first_node]:
                        q.put(node)
                if visited_number == n:
                    return [a, b]
            # add a -> b
            edge_array[a].append(b)
            in_degree_list[b] += 1
        return []
