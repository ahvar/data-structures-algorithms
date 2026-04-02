from typing import List, Tuple
from decimal import Decimal


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # the diff between the two strings is more than 1 character
        if abs(len(s) - len(t)) > 1:
            return False
        # they're already identical
        if s == t:
            return False
        rightt = len(t) - 1
        rights = len(s) - 1
        left = 0
        while left < rightt and left < rights and s[left] == t[left]:
            left += 1
        while left < rightt and left < rights and t[rightt] == s[rights]:
            rightt -= 1
            rights -= 1
        if len(s) == len(t):
            return rightt - left == 0 and rights - left == 0

        if len(s) < len(t):
            return rightt - left == 0 and rights - left == -1

        if len(s) > len(t):
            return rightt - left == -1 and rights - left == 0


class TestOneEdit:
    def setup_method(self):
        self.solution = Solution()

    def test_simple(self):
        s = "abcdfg"
        t = "adcrfg"
        assert self.solution.isOneEditDistance(s, t) == False


if __name__ == "__main__":
    solution = Solution()
