from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        farthest = -1
        start = 0
        ans = []
        for interval in intervals:
            left, right = interval[0], interval[1]
            if left <= farthest:
                farthest = max(right, farthest)
            else:
                if farthest != -1:
                    ans.append([start, farthest])
                start = left
                farthest = right
        ans.append([start, farthest])
        return ans

    def merge_2(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))
        events.sort(key=lambda x: (x[0], x[1]))
        count = 0
        start = 0
        ans = []
        for x, y in events:
            if count == 0:
                start = x
            count += y
            if count == 0:
                ans.append([start, x - 1])
        return ans
