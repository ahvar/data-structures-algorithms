class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}

        for cs, ct in zip(s, t):
            if (cs in s2t and s2t[cs] != ct) or (ct in t2s and t2s[ct] != cs):
                return False
            s2t[cs] = ct
            t2s[ct] = cs
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_is_iso(self):
        assert self.solution.isIsomorphic("egg", "add") == True
