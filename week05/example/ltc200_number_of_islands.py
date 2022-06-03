# https://leetcode.cn/problems/number-of-islands/

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] is False:
                    ans += 1
                    # bfs
                    q = deque()
                    q.append((i, j))
                    visited[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                continue
                            if visited[nx][ny]:
                                continue
                            if grid[nx][ny] == "0":
                                continue
                            q.append((nx, ny))
                            visited[nx][ny] = True
        return ans
