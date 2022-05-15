from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 0
        for weight in weights:
            left = max(left, weight)
            right += weight
        while left < right:
            mid = (left + right) // 2
            if self.valid_ship_capacity(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def valid_ship_capacity(self, weights, days, capacity):
        day = 1
        weight = 0
        for w in weights:
            if weight + w <= capacity:
                weight += w
            else:
                if w > capacity: return False
                day += 1
                weight = w

        return day <= days
