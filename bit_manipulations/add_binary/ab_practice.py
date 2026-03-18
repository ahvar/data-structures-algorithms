class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        result = []
        while i >= 0 or j >= 0 or carry:
            a_val = int(a[i]) if i >= 0 else 0
            b_val = int(b[j]) if j >= 0 else 0

            total = a_val + b_val + carry
            digit = total % 2
            carry = total // 2
            result.append(str(digit))

            i -= 1
            j -= 1
        return "".join(reversed(result))


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_add_binary(self):
        assert self.solution.addBinary("11", "1") == "100"
