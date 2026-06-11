from typing import List


class Solution:
    def minHarvestRate(self, apples: List[int], h: int) -> int:
        if not apples:
            return 0
        if h < len(apples):
            return -1

        left = 1
        right = max(apples)

        def hours_needed(rate):
            total = 0
            for a in apples:
                total += (a + rate - 1) // rate
            return total

        while left < right:
            mid = (left + right) // 2
            needed = hours_needed(mid)
            if needed <= h:
                right = mid
            else:
                left = mid + 1
        return left
