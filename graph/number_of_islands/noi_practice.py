from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return grid[r][c]

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)



        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    
        return island_count
