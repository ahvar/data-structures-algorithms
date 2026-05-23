from typing import List, Tuple
from decimal import Decimal


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        left = 0
        rightt = len(t) - 1
        rights = len(s) - 1
        while left < len(t) and left < len(s) and s[left] == t[left]:
            left += 1
        while left <= rightt and left <= rights and s[rights] == t[rightt]:
            rightt -= 1
            rights -= 1

        if len(s) == len(t):
            return rightt - left == 0 and rights - left == 0
        if len(s) < len(t):
            return rightt - left == 0 and rights - left == -1
        if len(s) > len(t):
            return rightt - left == -1 and rights - left == 0


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_one(self):
        assert self.solution.isOneEditDistance("abcd", "abrd") == True
