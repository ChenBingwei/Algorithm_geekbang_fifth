import heapq
from typing import List


class Pairs:
    def __init__(self, num, index):
        self.num = num
        self.index = index

    def __lt__(self, other):
        return self.num > other.num


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        priority_queue = []
        ans = []
        for index, num in enumerate(nums):
            heapq.heappush(priority_queue, Pairs(num, index))
            if index >= k - 1:
                while priority_queue[0].index <= index - k:
                    heapq.heappop(priority_queue)
                ans.append(priority_queue[0].num)

        return ans
