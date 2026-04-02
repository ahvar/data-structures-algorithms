import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
        n = len(s)  # string length
        dp = [[False] * (n) for _ in range(n)]  # dp table
        start = 0  # start here
        maxx = 1  # max length
        for i in range(n):
            dp[i][i] = True  # bc every single char is a palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True  # 2 identical chars are a palindrome
                maxx = 2
                start = i

        for length in range(3, n - 1):
            for i in range(length, n - 1):
                j = i + length + 1
                if s[i] == s[j] and dp[i - 1][j - 1]:
                    dp[i][j] = True
                    maxx = max(maxx, length)
                    start = i
        return s[start : start + maxx]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_longest(self):
        assert self.solution.longestPalindrome("babad") == "bab"
