from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            best = float("inf")

            for jump in range(1, 4):
                prev = i - jump

                if prev < 0:
                    continue

                jump_cost = costs[i - 1] + jump * jump

                candidate = dp[prev] + jump_cost

                best = min(best, candidate)

            dp[i] = best

        return dp[n]
