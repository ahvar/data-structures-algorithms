class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        i, j = len(s), len(t)
        while i < len(s) and j < len(t):
            if s[i] == s[t]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_iss(self):

        assert self.solution.isSubsequence(s="abc", t="ahbgdc") == True
