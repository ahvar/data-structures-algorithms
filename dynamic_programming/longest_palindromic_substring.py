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

    def _brute_force(self, s: str) -> str:
        subs = []
        # get all substrings
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                subs.append(s[i:j])
        sub_no_blank = [subs.remove(sub) for sub in subs if not sub]
        sub_no_blank.sort()
        for sub in sub_no_blank:
            if sub == sub[::-1]:
                return sub

        

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        # -------------------------------------
        # setup
        # -------------------------------------
        n = len(s) # length of s
        dp = [[False] * n for i in range(n)] # dp table

        # ------------------------------------
        # base case: all single-char substrings
        # are palindromes
        # ------------------------------------
        for i in range(n):
            dp[i][i] = True
        
        start = 0
        max_len = 1
        # all equivalent length 2 substrings are palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                max_len = 2
                start = i
        
        for length in range(3,n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]  and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start: start+max_len]
    
if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    pp.pprint(solution.longestPalindrome(s))