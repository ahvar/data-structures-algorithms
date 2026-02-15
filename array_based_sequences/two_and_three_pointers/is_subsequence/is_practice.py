class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  # Empty string is always a subsequence
            return True
        if len(s) > len(t):
            return False
        if s == t:
            return True
        i = 0
        j = 0
        while i <= len(s) - 1 and j <= len(t) - 1:
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    return True
            j += 1
        return False
