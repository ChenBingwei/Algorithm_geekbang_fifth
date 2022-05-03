from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp_combine = []
        ans = []

        def recur(num):
            if len(tmp_combine) > k or len(tmp_combine) + (n - num + 1) < k:
                return

            if num == n + 1:
                if len(tmp_combine) == k: ans.append(tmp_combine.copy())
                return
            # if len(tmp_combine) == k:
            #     ans.append(tmp_combine.copy())
            #     return
            # if num > n:
            #     return
            # next
            recur(num + 1)
            # save and next
            tmp_combine.append(num)
            recur(num + 1)
            tmp_combine.pop()

        recur(1)
        return ans


if __name__ == '__main__':
    out = Solution().combine(4, 2)
    print(out)
