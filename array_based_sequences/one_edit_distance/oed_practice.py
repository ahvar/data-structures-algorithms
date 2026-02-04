from typing import List, Tuple
from decimal import Decimal


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        left = 0
        rightt = len(t) - 1
        rights = len(s) - 1
        while left <= rightt and left <= rights and s[left] == t[left]:
            left += 1

        while rightt >= left and rights >= left and s[rights] == t[rightt]:
            rightt -= 1
            rights -= 1

        if len(s) == len(t):
            return rights - left == 0 and rightt - left == 0

        if len(s) < len(t):
            return rights - left == -1 and rightt - left == 0

        if len(s) > len(t):
            return rights - left == 0 and rightt - left == -1


if __name__ == "__main__":
    solution = Solution()
