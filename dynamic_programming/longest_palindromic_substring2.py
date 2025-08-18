"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).

dp[i][j] means s[i..j]

"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str: 
        if s == None or s == "":
            return ""
       
        if len(s) == 1:
            return s
       
        if len(s) == 2 and s[0] == s[1]:
            return s
       
        dp = [ [False] * len(s) for _ in range(len(s))]
        start = 0
        maxx = 1
        # all single char substrings are palindromes of length 1
        for i in range(len(s)):
            dp[i][i] = True

        # all substrings of length == 2 with identical chars are palindromes
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxx = 2

        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i-1][j-1]:
                    dp[i][j] = True
                    start = i
                    maxx = length

        return s[start:start + maxx]

           
           








       








if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)