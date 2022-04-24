from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fre_dict = {}
        ans = []
        for i in strs:
            has_i = "".join(sorted(i))
            fre_dict.setdefault(has_i, [])
            fre_dict[has_i].append(i)
        for k, v in fre_dict.items():
            ans.append(v)
        return ans


if __name__ == '__main__':
    input_test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    out = Solution().groupAnagrams(input_test)
    print(out)
