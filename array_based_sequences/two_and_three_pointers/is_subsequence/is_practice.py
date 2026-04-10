class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        sl = 0
        tl = 0
        while sl < len(s) and tl < len(t):
            if s[sl] == t[tl]:
                sl += 1
            tl += 1
        return sl == len(s)


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_ss(self):
        assert self.solution.isSubsequence(s="abc", t="ahbgdc") == True
