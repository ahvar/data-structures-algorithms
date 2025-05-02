"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[len(dp)-1], dp[len(dp) - 2])


if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))
