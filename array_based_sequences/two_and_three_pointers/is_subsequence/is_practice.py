class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = 0
        j = 0
        while i < len(t) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_ss(self):
        assert self.solution.isSubsequence(s="abc", t="ahbgdc") == True
