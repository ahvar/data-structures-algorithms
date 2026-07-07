class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for sc, tc in zip(s, t):
            if sc in s2t and s2t[sc] != tc or tc in t2s and t2s[tc] != sc:
                return False
            s2t[sc] = tc
            t2s[tc] = sc
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.isIsomorphic(s="egg", t="add") == True
