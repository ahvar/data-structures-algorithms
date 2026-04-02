from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == "0":
                return grid[row][col]

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        count = 0
        for row in range(n):
            for col in range(m):
                if dfs(row, col) == "1":
                    count += 1
                    dfs(row, col)

        return count
