class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            grid[i][0] = 1

        for i in range(n):
            grid[0][i] = 1

        for i in range(1, m):

            for j in range(i, n):
                grid[i][j] = sum(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]
