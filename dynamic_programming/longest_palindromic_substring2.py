"""
Given a string, find the longest substring that is a palindrome
(reads the same backward as forward).

dp[i][j] means s[i..j]

"aabcdcbefg"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return ""
        dp = [[False] * n for _ in range(n)]
        if n == 1: return s
        # 1 base case: all single characters are palindromes of length 1
        for i in range(n): dp[i][i] = True
        start, max_len = 0, 1
        # 2 base case: all substrings of length == 2 where characters are equivalent
        for i in range(1, n):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start, max_len = i, 2
        
        for length in range(3, n + 1):
            for i in range(0, n-(length+1)):
                j = i + length - 1
                # recurrence; char check first; only if ends match do we consult inner substring
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        start, max_len = i, length

        return s[start:start+max_len]






if __name__ == "__main__":
    example_string = "aabcdcbefg"
    solution = Solution()
    solution.longestPalindrome(example_string)