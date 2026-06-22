from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        arr = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = arr[-1][1]
            if start <= last_end:
                arr[-1][1] = max(last_end, end)
            else:
                arr.append[[start, end]]
        return arr
