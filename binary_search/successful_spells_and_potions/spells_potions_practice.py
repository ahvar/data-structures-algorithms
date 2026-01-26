from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        if potions == None or len(potions) == 0:
            return []
        potions.sort()
        pairs = []
        for spell in spells:
            left = 0
            right = len(potions) - 1
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs.append(len(potions) - left)
        return pairs


if __name__ == "__main__":
    spells, potions, success = [5, 1, 3], [1, 2, 3, 4, 5], 7
    solution = Solution()
    print(solution.successfulPairs(spells, potions, success))
