from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = -1
        right = len(matrix) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] <= target:
                left = mid
            else:
                right = mid - 1
        if right == -1:
            return False
        columm = right
        left = 0
        right = len(matrix[columm]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[columm][mid] == target:
                return True
            if matrix[columm][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
