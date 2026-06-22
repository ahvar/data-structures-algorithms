from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] will store the minimum total cost needed to reach step i.
        dp = [0] * (n + 1)

        # Step 0 is the starting point, so its cost is 0.
        dp[0] = 0

        # Fill the DP table from step 1 up to step n.
        for i in range(1, n + 1):
            # Start with an infinitely large answer for this step.
            best = float("inf")

            # Try reaching step i from the previous 1, 2, or 3 steps.
            for jump in range(1, 4):
                prev = i - jump

                # Ignore jumps that would come from a negative step.
                if prev < 0:
                    continue

                # The problem examples imply that step i uses costs[i - 1].
                # The jump cost is destination step cost plus jump_length^2.
                jump_cost = costs[i - 1] + jump * jump

                # Total cost = cost to reach prev step + cost of this jump.
                candidate = dp[prev] + jump_cost

                # Keep the cheapest way to reach step i.
                best = min(best, candidate)

            # Save the minimum cost for step i.
            dp[i] = best

        # The answer is the minimum cost to reach the final step n.
        return dp[n]
