"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0])# cols
        dp = [[0] * (n) for _ in range(m ) ]
        dp[0][0] = grid[0][0] # base case
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    solution = Solution()
    print(solution.minPathSum(grid))
