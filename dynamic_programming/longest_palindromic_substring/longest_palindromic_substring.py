import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:

    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1 or s == "" or len(s) == 2 and s[0] == s[1]:
            return s

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxx = 1
        start = i
        # each individual char is a substring
        for i in range(n):
            dp[i][i] = True
        # substrings of len 2 with identical chars
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxx = 2
        # substrings at least 3 chars in length
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i - 1][j + 1]:
                    dp[i][j] = True
                    maxx = max(maxx, length)
                    start = i
        return s[start : start + maxx]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        self.solution.longestPalindrome(s="babad") == "bab"
