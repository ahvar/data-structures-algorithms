"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""

import math


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = None
        if "+" in s or "-" in s:
            sign = s[0]
            s = s[1:]
        j = 0
        k = 0
        while j < len(s):
            if s[j] == "0":
                k = j
                j += 1
            elif s[j].isdigit():
                j += 1
            elif s[j].isalpha():
                j -= 1
                break
        if k > 0:
            value = s[k + 1 : j + 1]
        else:
            value = s[k : j + 1]
        if not value:
            return 0
        if sign == "-":
            value = 0 - int(value)
        else:
            value = int(value)
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        if not INT_MIN <= value <= INT_MAX:
            value = max(INT_MIN, min(value, INT_MAX))
        return value


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("0-1"))
