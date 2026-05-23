from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):

            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return grid[r][c]
            grid[r][c] == "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)
        return island_count
