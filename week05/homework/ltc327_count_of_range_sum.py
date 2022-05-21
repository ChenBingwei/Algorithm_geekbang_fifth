from typing import List


class Solution:
    def __init__(self) -> None:
        self.range_num = 0

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        new_nums = []
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            # s(i,j) i==j场景
            if lower <= tmp_sum <= upper:
                self.range_num += 1
            new_nums.append(tmp_sum)
        self.merge_sort(new_nums, 0, len(new_nums) - 1, lower, upper)
        return self.range_num

    def merge_sort(self, arr, l, r, lower, upper):
        if l >= r:
            return
        mid = l + (r - l) // 2
        self.merge_sort(arr, l, mid, lower, upper)
        self.merge_sort(arr, mid + 1, r, lower, upper)
        self.calculate(arr, l, mid, r, lower, upper)
        self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        i = l
        j = mid + 1
        tmp = []
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1
        while i <= mid:
            tmp.append(arr[i])
            i += 1
        while j <= r:
            tmp.append(arr[j])
            j += 1
        arr[l:r + 1] = tmp

    def calculate(self, arr, l, mid, r, lower, upper):
        left = right = mid + 1
        for i in range(l, mid + 1):
            while left <= r and arr[left] - arr[i] < lower:
                left += 1
            while right <= r and arr[right] - arr[i] <= upper:
                right += 1
            self.range_num += right - 1 - left + 1





