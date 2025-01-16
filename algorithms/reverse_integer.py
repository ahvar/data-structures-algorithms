"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing
x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        rx = strx[::-1]
        if "-" in rx and math.pow(-2, 31) < x < 0:
            pass
        elif math.pow(-2, 31) <= x <= math.pow(2, 31):
            return float(rx)
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-123))
