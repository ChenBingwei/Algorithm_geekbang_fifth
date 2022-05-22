from queue import Queue
from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            if board[i][0] == "O":
                self.bfs(board, i, 0)
            if board[i][self.n - 1] == "O":
                self.bfs(board, i, self.n - 1)

        for j in range(self.n):
            if board[0][j] == "O":
                self.bfs(board, 0, j)
            if board[self.m - 1][j] == "O":
                self.bfs(board, self.m - 1, j)

        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j]:
                    board[i][j] = 'X'

    def bfs(self, grid, sx, sy):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        q = Queue()
        # 第一步：push起点
        q.put([sx, sy])
        self.visited[sx][sy] = True
        while not q.empty():
            now = q.get()
            x, y = now[0], now[1]
            # 扩展所有出边（四个方向）
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 任何时候访问数组前，判断合法性
                if nx < 0 or ny < 0 or nx >= self.m or ny >= self.n:
                    continue
                if grid[nx][ny] == 'O' and not self.visited[nx][ny]:
                    q.put([nx, ny])
                    # BFS：入队时标记visit
                    self.visited[nx][ny] = True
