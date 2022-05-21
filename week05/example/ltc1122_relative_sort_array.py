from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2orders = {}
        for i in range(len(arr2)):
            arr2orders[arr2[i]] = i
        ans = sorted(arr1, key=lambda x: arr2orders.get(x, len(arr2) + x))
        return ans

    # count sort
    def relativeSortArray_count_sort(self, arr1: List[int], arr2: List[int]) -> List[int]:
        array_count = [0] * 1001
        ans = []
        for i in arr1:
            array_count[i] += 1
        for i in arr2:
            while array_count[i] > 0:
                ans.append(i)
                array_count[i] -= 1
        for i in range(len(array_count)):
            while array_count[i] > 0:
                ans.append(i)
                array_count[i] -= 1
        return ans