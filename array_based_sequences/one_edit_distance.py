"""
Given two strings s and t, return true if they are both one edit distance apart,
otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

"""

from typing import List, Tuple
from decimal import Decimal


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False
        left = 0
        rights = len(s) - 1
        rightt = len(t) - 1

        while left < rights and left < rightt and s[left] == t[left]:
            left += 1
        while rights >= left and rightt >= left and s[rights] == t[rightt]:
            rights -= 1
            rightt -= 1

        if len(s) == len(t):
            return rights - left == 0 and rightt - left == 0

        if len(s) < len(t):
            return rightt - left == 0 and rights - left == -1

        if len(s) > len(t):
            return rights - left == 0 and rightt - left == -1


if __name__ == "__main__":
    solution = Solution()
