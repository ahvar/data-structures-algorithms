class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        aptr = len(a) - 1
        bptr = len(b) - 1
        carry = 0
        result = []
        while aptr >= 0 or bptr >= 0 or carry:
            aint = int(a[aptr]) if aptr >= 0 else 0
            bint = int(b[bptr]) if bptr >= 0 else 0
            total = aint + bint + carry
            carry = total // 2
            digit = total % 2
            result.append(str(digit))
            aptr -= 1
            bptr -= 1
        return "".join(reversed(result))


if __name__ == "__main__":
    solution = Solution()
