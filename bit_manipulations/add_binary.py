"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        digits = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry
            current_digit = total % 2
            carry = total // 2

            digits.append(str(current_digit))
            i -= 1
            j -= 1
        return "".join(reversed(digits))


if __name__ == "__main__":
    solution = Solution()
