"""
Given a string s, return the longest palindromic substring in s.

babad

b
ba
bab
baba
a
ab
aba
abad
b
ba
bad
 
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        subs = []
        for i in range(n):
            j = n
            for j in range(i + 1, n + 1):
                subs.append(s[i:j])
        longest = ""
        for sub in subs:
            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub
        return longest


if __name__ == "__main__":
    input = "jlimmiqalil"
    s = Solution()
    print(s.longestPalindrome(input))
