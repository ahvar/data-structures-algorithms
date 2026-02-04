class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        a_ptr = len(a) - 1
        b_ptr = len(b) - 1
        carry = 0
        result = []
        while a_ptr >= 0 or b_ptr >= 0 or carry:
            a_val = int(a[a_ptr]) if a_ptr >= 0 else 0
            b_val = int(b[b_ptr]) if b_ptr >= 0 else 0
            total = a_val + b_val + carry
            carry = total // 2
            digit = total % 2
            result.append(str(digit))
            a_ptr -= 1
            b_ptr -= 1
        return "".join(reversed(result))
