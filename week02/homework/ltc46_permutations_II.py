from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]):
        n = len(nums)
        ans = []
        used = [False] * n
        a = []
        # 方便去重
        nums.sort()

        def recur(nums, pos):
            if pos == n:
                # python中需进行浅拷贝或深拷贝
                ans.append(a.copy())
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                # 去重
                if i > 0 and num == nums[i - 1] and not used[i - 1]:
                    continue
                a.append(num)
                used[i] = True
                recur(nums, pos + 1)
                used[i] = False
                a.pop()

        recur(nums, 0)
        return ans


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # expect_out = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    nums = [1, 1, 2]
    expect_out = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    # print(Solution().permuteUnique(nums))

    assert Solution().permuteUnique(nums) == expect_out
