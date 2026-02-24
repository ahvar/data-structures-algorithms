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
            aval = int(a[aptr]) if aptr >= 0 else 0
            bval = int(b[bptr]) if bptr >= 0 else 0
            total = aval + bval + carry
            digit = total % 2
            carry = total // 2
            result.append(str(digit))
            aptr -= 1
            bptr -= 1
        return "".join(reversed(result))


class TestAddBinary:

    def test_add_binary(self):
        a = "11"
        b = "1"
        s = Solution()
        assert s.addBinary(a, b) == "100"
