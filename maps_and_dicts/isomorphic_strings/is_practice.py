class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}

        for s_char, t_char in zip(s, t):
            if (
                s_char in s2t
                and s2t.get(s_char) != t2s[t_char]
                or t_char in t2s
                and t2s.get(t_char) != s2t(s_char)
            ):
                return False
            s2t[s_char] = t_char
            t2s[t_char] = s_char
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.isIsomorphic(s="egg", t="add") == True
