from rich import print as rprint

import pprint
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = sum([dp[i][j - 1], dp[i - 1][j]])

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    m = 3
    n = 7
    solution = Solution()
    rprint(solution.uniquePaths(m, n))
