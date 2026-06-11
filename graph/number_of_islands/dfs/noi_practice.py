from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0

        def search(row, col):
            if grid[row][col] == "1":
                return True
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == "0":
                return grid[row][col]

            search(row + 1, col)
            search(row - 1, col)

            search(row, col + 1)
            search(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    island_count += 1
                    search(row, col)

        return island_count
