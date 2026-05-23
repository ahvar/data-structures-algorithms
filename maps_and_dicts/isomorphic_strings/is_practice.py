class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for s_char, t_char in zip(s, t):
            if s_char in s2t:
                if s2t[s_char] != t_char:
                    return False
            elif t_char in t2s:
                if t2s[t_char] != s_char:
                    return False
                return False
            s2t[s_char] = t_char
            t2s[t_char] = s_char
        return True


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.isIsomorphic(s="paper", t="title") == True
