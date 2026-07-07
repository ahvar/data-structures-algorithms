from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            best = float("inf")
            for jump in range(1, 4):
                prev = i - jump
                if prev < 0:
                    continue
                candidate = dp[prev] + costs[i - 1] + jump * jump
                best = min(best, candidate)
            dp[i] = best
        return dp[n]
