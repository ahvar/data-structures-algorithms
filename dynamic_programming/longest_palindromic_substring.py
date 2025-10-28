"""
Given a string s, return the longest palindromic substring in s.
A string is palindromic if it reads the same forward and backward.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:

    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) == 0:
            return ""
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxx = 1
        start = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxx = 2
                start = i

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length  # end of current substring
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    maxx = max(length, maxx)
                    start = i
        return s[start : start + maxx]


if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    pp.pprint(solution.longestPalindrome(s))
