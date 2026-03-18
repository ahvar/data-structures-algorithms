class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * m for _ in range(n)]
        for i in range(n):
            grid[i][0] = 1

        for i in range(m):
            grid[0][i] = 1

        for i in range(n):
            for j in range(m):
                grid[i][j] = sum(grid[i - 1][j], grid[i][j - 1]) + 1
        return grid[i - 1][j - 1]
