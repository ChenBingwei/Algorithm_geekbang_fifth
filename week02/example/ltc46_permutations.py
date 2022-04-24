from typing import List


class Solution:

    def permute(self, nums):
        n = len(nums)
        ans = []
        used = [False] * n
        a = []

        def recur(nums, pos):
            if pos == n:
                ans.append(a.copy())
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                a.append(num)
                used[i] = True
                recur(nums, pos + 1)
                used[i] = False
                a.pop()

        recur(nums, 0)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    expect_out = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(Solution().permute(nums))
    # assert Solution().permute(nums) == expect_out
