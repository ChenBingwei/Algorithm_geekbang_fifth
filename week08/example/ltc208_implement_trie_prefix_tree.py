class Trie:

    def __init__(self):
        self.root = [0, {}]

    def insert(self, word: str) -> None:
        self._find(word, True, False)

    def search(self, word: str) -> bool:
        return self._find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix, False, True)

    def _find(self, word, is_insert, is_prefix):
        curr = self.root
        for w in word:
            if w not in curr[1]:
                if not is_insert:
                    return False
                curr[1][w] = [0, {}]
            curr = curr[1][w]
        if is_insert:
            curr[0] += 1
        if is_prefix:
            return True
        return curr[0] > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie_II:
    def __init__(self):
        self.root = [0, [None] * 26]

    def insert(self, word: str) -> None:
        self._find(word, True, False)

    def search(self, word: str) -> bool:
        return self._find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix, False, True)

    def _find(self, word, is_insert, is_prefix):
        curr = self.root
        for w in word:
            if curr[1][ord(w) - ord("a")] is None:
                if not is_insert:
                    return False
                curr[1][ord(w) - ord("a")] = [0, [None] * 26]
            curr = curr[1][ord(w) - ord("a")]
        if is_insert:
            curr[0] += 1
        if is_prefix:
            return True
        return curr[0] > 0
