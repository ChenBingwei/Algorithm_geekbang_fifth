from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ans = []
        tmp_permutation = []

        def recur(nums, pos):
            if pos == n:
                ans.append(tmp_permutation.copy())
                return
            for i in range(n):
                if not used[i]:
                    tmp_permutation.append(nums[i])
                    used[i] = True
                    recur(nums, pos + 1)
                    used[i] = False
                    tmp_permutation.pop()

        recur(nums, 0)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    expect_out = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(Solution().permute(nums))
    # assert Solution().permute(nums) == expect_out
