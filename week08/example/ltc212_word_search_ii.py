from typing import List


class Solution:

    def __init__(self):
        self.trie = [0, {}]
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, 1, -1, 0]
        self.visit = None
        self.ans = set()
        self.string_list = []
        self.m = None
        self.n = None

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self._trie_insert(word)

        self.m = len(board)
        self.n = len(board[0])
        self.visit = [[False] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.visit[i][j] = True
                self._dfs(board, i, j, self.trie)
                self.visit[i][j] = False
        return list(self.ans)

    def _dfs(self, board, x, y, curr):
        ch = board[x][y]
        if ch not in curr[1]:
            return
        curr_child = curr[1][ch]
        self.string_list.append(ch)

        if curr_child[0] > 0:
            self.ans.add(''.join(self.string_list))
        if not curr_child[1]:
            curr[1].pop(ch)
            del curr_child
        else:
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                if nx < 0 or ny < 0 or nx >= self.m or ny >= self.n:
                    continue
                if self.visit[nx][ny]:
                    continue

                self.visit[nx][ny] = True
                self._dfs(board, nx, ny, curr_child)
                self.visit[nx][ny] = False
        self.string_list.pop()

    def _trie_insert(self, word):
        curr = self.trie
        for w in word:
            if w not in curr[1]:
                curr[1][w] = [0, {}]
            curr = curr[1][w]
        curr[0] += 1
