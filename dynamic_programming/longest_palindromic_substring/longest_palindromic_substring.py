import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or not s:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        maxx = 1
        # every single char is a palindrome of len == 1
        for i in range(n):
            dp[i][i] = True

        # duplicate chars are palindromes of len == 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxx = 2
                start = i

        # base case
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    maxx = max(length, maxx)
                    start = i
        return s[start : start + maxx]
