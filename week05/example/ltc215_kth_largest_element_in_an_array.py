import heapq
import random
from typing import List


class Solution:

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        for num in nums[k:]:
            if hp[0] < num:
                heapq.heappop(hp)
                heapq.heappush(hp, num)
        return hp[0]

    def findKthLargest_quick_sort(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.quick_sort(nums, 0, n - 1, n - k)

    def quick_sort(self, nums, left, right, index):
        if left >= right:
            return nums[right]
        pivot = self.partition(nums, left, right)
        if index <= pivot:
            return self.quick_sort(nums, left, pivot, index)
        else:
            return self.quick_sort(nums, pivot + 1, right, index)

    def partition(self, nums, left, right):
        pivot = random.randint(left, right)
        pivot_value = nums[pivot]
        while left <= right:
            while nums[left] < pivot_value:
                left += 1
            while nums[right] > pivot_value:
                right -= 1
            if left == right:
                break
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return right
