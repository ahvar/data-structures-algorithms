class Solution:
    def isValid(self, s: str) -> bool:
        chars = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
                continue
            else:
                if not stack or stack[-1] != chars.get(c):
                    return False
                stack.pop()

        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.isValid(s="()[]{}") == True
