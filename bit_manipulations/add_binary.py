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
        if not a:
            return b
        if not b:
            return a
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        result = []
        while i >= 0 or j >= 0 or carry:
            aval = int(a[i]) if i >= 0 else 0
            bval = int(b[j]) if i >= 0 else 0
            total = aval + bval + carry
            digit = total % 2
            carry = total // 2
            result.append(str(digit))
            i -= 1
            j -= 1
        return "".join(reversed(result))


if __name__ == "__main__":
    solution = Solution()
