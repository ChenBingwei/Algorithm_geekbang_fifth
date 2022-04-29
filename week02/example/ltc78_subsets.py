from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []

        def recur(nums, i):
            if i == n:
                res.append(subset.copy())
                return

            recur(nums, i + 1)
            subset.append(nums[i])
            recur(nums, i + 1)
            subset.pop()

        recur(nums, 0)
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
