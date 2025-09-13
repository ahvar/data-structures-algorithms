"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).

dp[i][j] means s[i..j]

"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or s == "" or len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxx = 0
        start = 0
        for i in range(n):
            dp[i][i] = True # because single characters are length == 1 palindromic substrings
        
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxx = 2
                start = i
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    maxx = length
                    start = i
        return s[start: start + maxx]



        

        


        
             
        
        







           
           








       








if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)