from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols

        dp[0] = 1

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    dp[col] == 0
                elif col > 0:
                    dp[col] += dp[col - 1]
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
