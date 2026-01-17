import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) == 0:
            return ""
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
        n = len(s)
        start = 0
        maxx = 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxx = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    maxx = max(maxx, length)
                    start = i
        return s[start : start + maxx]


if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    pp.pprint(solution.longestPalindrome(s))
