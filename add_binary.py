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
    def trim(self, s):
        first_one = s.find("1")
        return s[first_one:] if first_one != -1 else "0"
    
    def addBinary(self, a: str, b: str) -> str:

        a = self.trim(a)
        b = self.trim(b)

        n = len(a)
        m = len(b)

        if n < m:
            a, b = b, a
            n, m = m, n

        j = m - 1
        carry = 0
        result = []
        for i in range(n-1,-1,-1):
            bit1 = int(a[i])
            bit_sum = bit1 + carry

            if bit_sum == 0:
                if carry:
                    result.append("1")
                    carry -= 1
                else:
                    result.append("0")
            if bit_sum == 1:
                if carry:
                    result.append('0')
                else:
                    result.append('1')
            if bit_sum == 2:
                if carry:
                    result.append("1")
                else:
                    result.append("0")
                    carry += 1
            if bit_sum == 3:
                if carry:
                    result.append("11")
                else:
                    result.apppend("10")
        return ''.join(result[::-1])



                



if __name__ == "__main__":
    solution = Solution()
