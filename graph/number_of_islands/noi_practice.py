from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == "0":
                return grid[row][col]

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)
        return island_count
