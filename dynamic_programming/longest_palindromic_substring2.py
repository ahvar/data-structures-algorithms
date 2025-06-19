"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).


"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i

        for i in range(3,n+1): # for len(substrings) >= 3
            for j in range(n - i + 1): # length of string - the beginning of the substring
                j = j + (i - 1) # why ?
                if s[i] == s[j]  and dp[i+1][j-1]:
                    dp[i][j] = True
                    if i > max_len:
                        start = i
                        max_len = i
                
        return s[start:start + max_len]



if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)