from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_s = len(s)
        len_word = len(words[0])
        len_words = len(words) * len_word
        ans = []
        for i in range(len_s):
            if len_s - i < len_words:
                break
            sub_str = s[i:i + len_words]

            # valid_compare
            if self.valid_compare(sub_str, words):
                ans.append(i)

        return ans

    def valid_compare(self, s, words):
        words_fre_dict = {}
        for word in words:
            words_fre_dict.setdefault(word, 0)
            words_fre_dict[word] += 1

        sub_str_dict = {}
        for i in range(0, len(s), len(words[0])):
            sub_str = s[i:i + len(words[0])]
            sub_str_dict.setdefault(sub_str, 0)
            sub_str_dict[sub_str] += 1

        return sub_str_dict == words_fre_dict


if __name__ == '__main__':
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    expect_out = [6, 9, 12]
    assert expect_out == Solution().findSubstring(s, words)
