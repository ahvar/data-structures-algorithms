from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        if not potions:
            return []
        potions.sort()
        n = len(potions)
        pairs = []
        for spell in spells:
            left = 0
            right = n - 1
            idx = n
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    idx = mid
                    right = idx - 1
                else:
                    left = mid + 1
            pairs.append(n - idx)
        return pairs


if __name__ == "__main__":
    spells, potions, success = [5, 1, 3], [1, 2, 3, 4, 5], 7
    solution = Solution()
    print(solution.successfulPairs(spells, potions, success))
