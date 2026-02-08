"""
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        for right in range(len(haystack)):
            if haystack[right] == needle[0]:
                left = right + 1
                for i in range(1, len(needle)):
                    if left <= len(haystack) - 1:
                        if needle[i] != haystack[left]:
                            break
                        left += 1
                    else:
                        break
                if left - right == len(needle):
                    return right
        return -1


if __name__ == "__main__":
    haystack = "paiwoehiwoewlq"
    needle = "woew"
    solution = Solution()
    print(solution.strStr(haystack, needle))
