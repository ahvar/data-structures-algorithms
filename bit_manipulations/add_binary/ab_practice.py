class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        carry = 0
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        result = []
        while a_idx >= 0 or b_idx >= 0 or carry:
            a_int = int(a[a_idx]) if a_idx >= 0 else 0
            b_int = int(b[b_idx]) if b_idx >= 0 else 0
            total = a_int + b_int + carry
            digit = total % 2
            carry = total // 2
            result.append(str(digit))
            a_idx -= 1
            b_idx -= 1
        return "".join(result)


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        self.solution.addBinary(a="11", b="1") == "100"
        self.solution.addBinary(a="1010", b="1011") == "10101"
