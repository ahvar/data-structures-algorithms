"""Apple harvest implementation guide.

Implementation steps:
1. Model the answer as a harvest rate k apples per hour,
and search for the smallest k that lets Bobby finish within h hours.

2. Initialize the search range from 1 up to the largest value in apples,
because Bobby cannot harvest slower than 1 apple per hour and never needs
a rate higher than the biggest tree.

3. Repeatedly choose the middle rate in that range as the current candidate.

4. For that candidate, walk through every tree and compute how many
whole hours that tree would take at the current rate.

5. Use ceiling division for each tree so partial final hours are counted
correctly, since Bobby still loses the rest of that hour before moving on.

6. Add those per-tree hours to get the total time needed for the
current candidate rate.

7. If the total time is less than or equal to h, record that this
rate is valid and continue searching the lower half for a slower valid rate.

8. If the total time is greater than h, discard that rate and the entire
lower half, then continue searching the upper half.

9. Stop when the search bounds meet; that value is the minimum valid
harvest rate.

Why binary search works:
- If a rate is fast enough, any larger rate is also fast enough.
- If a rate is too slow, any smaller rate is also too slow.

Expected complexity:
- Time: O(n log m), where n is the number of trees and m is the largest apple count on any tree.
- Space: O(1) extra space.
"""

from typing import List


class Solution:
    def minHarvestRate(self, apples: List[int], h: int) -> int:

        if h < len(apples):
            return -1

        left = 0
        right = max(apples) - 1

        def hours_needed(rate):
            total = 0
            for apples_on_tree in apples:
                total += (apples_on_tree + rate - 1) // rate
            return total

        while left < right:
            mid = (left + right) // 2
            needed = hours_needed(mid)

            if needed <= h:
                right = mid
            else:
                left = mid + 1

        return left
