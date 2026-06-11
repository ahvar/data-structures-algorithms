import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxx = 0
        start = 0

        # single char == substring == palindrome
        for i in range(n):
            dp[i][i] = True

        # len(substring) == 2 is palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxx = 2
                start = i

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    maxx = max(maxx, length)
                    start = i
        return s[start : start + maxx]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        self.solution.longestPalindrome(s="babad") == "bab"
