from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        m = len(potions)
        pairs = []
        # sort potions so they are in order of increasing strength, thus
        # multiplying later potions with any spell will increase
        # liklihood of success
        potions.sort()
        # go through spells
        for spell in spells:
            left = 0  # first potion
            right = m - 1  # last potion
            idx = m
            while left <= right:
                mid = (right + left) // 2
                # if this potion is less than success, then all prior potions
                # will be less than success
                if potions[mid] * spell < success:
                    left += mid + 1
                # otherwise this potion and all those after it will be
                # successful
                else:
                    idx = mid
                    right = idx - 1  #
            pairs.append(m - idx)
        return pairs


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_potions(self):
        assert self.solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
