"""
Given a string s, return the longest palindromic substring in s.
 
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        if not s:
            return ""
        i = 1
        while i < len(s) - 1 and s[0] == s[i]:
            i += 1
        if i == len(s) - 1:
            return s
        left = 0
        while left < len(s):
            for right in range(len(s)):
                sub = s[left : right + 1]
                if sub in s and sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
            left += 1
        return longest


if __name__ == "__main__":
    input = "babad"
    s = Solution()
    print(s.longestPalindrome(input))
    input = "cbbd"
    print(s.longestPalindrome(input))
