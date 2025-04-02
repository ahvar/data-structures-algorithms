"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(t), len(s)
        if n < m:
            return False
        elif not s or not s and not t:
            return True
        elif not t:
            return False
        i = j = 0
        while i < n and j < m:
            if s[j] == t[i]:
                j += 1
            i += 1
        if j == m:
            return True
        return False


if __name__ == "__main__":
    sstring = "abc"
    tstring = "ahbgdc"
    s = Solution()
    print(s.isSubsequence(sstring, tstring))
