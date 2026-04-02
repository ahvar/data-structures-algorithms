class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sptr = 0
        tptr = 0
        while sptr < len(s) and tptr < len(t):
            if s[sptr] == t[tptr]:
                sptr += 1
            if sptr >= len(s):
                break
            tptr += 1
        if sptr == len(s):
            return True
        return False


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.isSubsequence("abc", "ahbgdc") == True
