from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        m = len(potions)
        potions.sort()
        pairs = []
        for spell in spells:
            left = 0
            right = m - 1
            idx = m
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] <= success:
                    left = mid + 1
                else:
                    idx = mid
                    right = idx - 1
            pairs.append(m - idx)
        return pairs
