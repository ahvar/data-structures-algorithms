class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if s == t:
            return True
        left_s = 0
        left_t = 0

        while left_t < len(t):
            if s[left_s] == t[left_t]:
                left_s += 1
                if left_s == len(s):
                    return True
            left_t += 1
        return False


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_subsequence(self):
        assert self.solution.isSubsequence("abc", "ahbgdc") == True
