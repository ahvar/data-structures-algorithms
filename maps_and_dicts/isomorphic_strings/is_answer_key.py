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


if __name__ == "__main__":
    s = "egg"
    t = "add"
    solution = Solution()
    print(solution.isIsomorphic(s, t))
