from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        m = len(potions)
        potions.sort()
        results = []
        for spell in spells:
            left = 0
            right = m - 1
            idx = m
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    idx = mid
                    right = idx - 1
                else:
                    left = mid + 1
            results.append(m - idx)
        return results
