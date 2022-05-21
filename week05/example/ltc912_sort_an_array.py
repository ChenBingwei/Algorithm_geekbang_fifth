import random
from typing import List


class Solution:
    # merge sort
    def sortArray_merge_sort(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] > nums[j]:
                temp.append(nums[j])
                j += 1
            else:
                temp.append(nums[i])
                i += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left:right + 1] = temp

    # quick sort
    def sortArray_quick_sort(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, arr, l, r):
        if l >= r:
            return
        pivot = self.partition(arr, l, r)
        self.quick_sort(arr, l, pivot)
        self.quick_sort(arr, pivot + 1, r)

    def partition(self, a, l, r):
        pivot = random.randrange(l, r + 1)
        pivot_val = a[pivot]
        while l <= r:
            while a[l] < pivot_val:
                l += 1
            while a[r] > pivot_val:
                r -= 1
            if l == r:
                break
            if l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
        return r
