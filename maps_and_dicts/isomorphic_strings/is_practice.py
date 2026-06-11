class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}

        for sc, tc in zip(s, t):
            if (
                s2t.get(sc, None)
                and s2t.get(sc) != tc
                or t2s.get(tc, None)
                and t2s[tc].get(tc) != sc
            ):
                return False
            s2t[sc] = tc
            t2s[tc] = sc
        return True
