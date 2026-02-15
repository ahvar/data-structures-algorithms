from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy BFS approach to find minimum jumps.

        Time: O(n), Space: O(1)

        Example: nums = [2,3,1,1,4]
        i=0: farthest=2, current_end=0 -> jump=1, current_end=2
        i=1: farthest=4
        i=2: farthest=4, current_end=2 -> jump=2, current_end=4
        Result: 2 jumps
        """
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0  # End of range for current jump level
        farthest = 0  # Farthest position reachable so far

        # Don't need to check last index (already at destination)
        for i in range(len(nums) - 1):
            # Update farthest position reachable from index i
            farthest = max(farthest, i + nums[i])

            # When we reach end of current jump range, must make another jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early termination if we can reach the end
                if current_end >= len(nums) - 1:
                    break

        return jumps
