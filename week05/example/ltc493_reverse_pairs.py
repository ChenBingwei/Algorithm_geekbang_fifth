from typing import List


class Solution:
    def __init__(self) -> None:
        self.reverser_pair_num = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.reverser_pair_num

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.calculate(nums, left, mid, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right + 1] = temp

    def calculate(self, nums, left, mid, right):
        j = mid
        for i in range(left, mid + 1):
            while j < right and nums[i] > 2 * nums[j + 1]:
                j += 1
            self.reverser_pair_num += j - mid
