"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).

dp[i][j] means s[i..j]

"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str: 
        # edge cases
        if s == None or len(s) == 0:
            return ""
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
        
        maxx = 0 # max length palindromic substring
        start = 0 # starting index of ^
        dp = [[False] * len(s) for _ in range(len(s))]

        # base case 1: single chars are palindromic substrings of length == 1
        for i in range(len(s)):
            dp[i][i] = True

        # base case 2: length == 2 substrings of identical chars are palindromes
        for i in range(len(s)):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxx = 2
                start = i
        # general case: walk rightward from index == 3; increasing the length
        for length in range(3,len(s) + 1):
            # walk the length of the current substring
            for i in range(len(s) - length + 1):
                j = i + length - 1 # end of the current substring
                # check ends and then inner chars to confirm palindrome
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    maxx = length
                    start = i
        # return longest palindromic substring
        return s[start:start + maxx]
        







           
           








       








if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)