"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing
x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        sign = ""
        strx = str(x)
        if "-" in strx or "+" in strx:
            sign = strx.pop(0)
        rx = strx[::-1]
        if int(rx) > math.pow(2, 31) or (int(rx) - math.pow(-2, 31)):
            return 0
        return int(rx)


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-123))
