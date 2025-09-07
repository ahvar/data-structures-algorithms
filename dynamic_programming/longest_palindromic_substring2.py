"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).

dp[i][j] means s[i..j]

"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) == 0:
            return ""
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
    
        dp = [[False] * len(s) for _ in range(len(s))]
        maxx = 1
        start = 0
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxx = 2
                start = 0

        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    maxx = length
                    start = i

        return s[start:start + maxx]
            

        

        


        
             
        
        







           
           








       








if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)