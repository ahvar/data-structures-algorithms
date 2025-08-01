"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).


"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # trivial cases
        if len(s) == 0: return ""
        n = len(s)
        if n == 1 or n == 2 and s[0] == s[1]: return s

        # dp[i][j] will be True if s[i...j] is palindromic
        # so we need an n x n table
        dp = [[0] * (n) for _ in range(n)]
        
        # track the best palindrome seen so far
        start = 0
        longest = 1 # every single char is a palindrome of length 1


        # Base Case 1: every single character is a palindrome
        for i in range(1,n): dp[i][i] = True

        # Base Case 2: every single two char substring is a palindrome if the two chars are equal
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                longest = 2

        # General Case: substrings of length 3 up to n
        for length in range(3, n + 1): # loop by substring length so dp[i+1][j-1] is ready
            for i in range(0, n - length + 1): # start index
                j = i + length - 1 # end index
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if length > longest:
                        start = i
                        longest = length
        return s[start:start + longest]







if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)