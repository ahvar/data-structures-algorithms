# Unique Paths II Implementation Guide

This problem uses dynamic programming.

Let `dp[col]` mean: the number of ways to reach the current row at column `col`.

The transition is simple:
- if a cell is an obstacle, set `dp[col] = 0`
- otherwise, if `col > 0`, add the left path count with `dp[col] += dp[col - 1]`

Why this works:
- `dp[col]` before the update is the number of ways from above
- `dp[col - 1]` after the update is the number of ways from the left

Initialize `dp[0] = 1` only if the starting cell is open. If `obstacleGrid[0][0] == 1`, return `0` immediately.

Process the grid from top-left to bottom-right. After the scan, `dp[-1]` is the answer.

## Complexity

Let `m` be the number of rows and `n` be the number of columns.

- Time complexity: O(m * n) because each cell is processed once.
- Space complexity: O(n) because we only store one row of DP values.

## Commented Solution

```python
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If the starting cell is blocked, there is no valid path.
        if obstacleGrid[0][0] == 1:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # dp[col] stores the number of ways to reach the current row at column col.
        dp = [0] * cols

        # There is exactly one way to stand on the starting cell when it is open.
        dp[0] = 1

        for row in range(rows):
            for col in range(cols):
                # A blocked cell cannot be part of any valid path.
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                # For an open cell outside the first column, add paths from the left.
                # dp[col] already represents paths from above.
                elif col > 0:
                    dp[col] += dp[col - 1]

        # The last entry holds the number of ways to reach the bottom-right corner.
        return dp[-1]
```