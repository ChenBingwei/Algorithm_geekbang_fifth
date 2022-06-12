from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        max_dist = 10 ** 9
        d = [[max_dist for _ in range(n)] for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for from_i, toi, weighti in edges:
            d[from_i][toi] = d[toi][from_i] = weighti

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        ans = 0
        min_neighbour = max_dist
        for i in range(n):
            neighbour = 0
            for j in range(n):
                if j == i:
                    continue
                if d[i][j] <= distanceThreshold:
                    neighbour += 1

            if neighbour < min_neighbour or (neighbour == min_neighbour and i > ans):
                ans = i
                min_neighbour = neighbour
        return ans
