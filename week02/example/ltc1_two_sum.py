from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i, v in enumerate(nums):
            if target - v in target_dict:
                return [target_dict[target - v], i]
            target_dict[v] = i
        return []


if __name__ == '__main__':
    nums = [
        [2, 7, 11, 15],
        [3, 2, 4],
        [3, 3]
    ]
    target = [
        9,
        6,
        6
    ]
    expect_res = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]
    for i, v in enumerate(nums):
        assert expect_res[i] == Solution().twoSum(v, target[i])
