"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).

dp[i][j] means s[i..j]

"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ""
        # strings of length == 1 are palindromes
        if len(s) == 1: return s
        # strings of length == 2 with same characters
        if len(s) == 2 and s[0] == s[1]: return s
        n = len(s)
        maxx = 0
        start = 0
        dp = [ [False] * n for _ in range(n)]
        # Base Case 1: single characters are all palindromes of length == 1
        for i in range(n):
            dp[i][i] = True
        # Base Case 2: all length == 2 substrings with same characters
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxx = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + (length - 1)
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > maxx:
                        start = i
                        maxx = length

        return s[start:maxx + start]








if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)