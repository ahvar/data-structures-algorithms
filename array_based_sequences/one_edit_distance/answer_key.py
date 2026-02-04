class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) > len(t)) > 1:
            return False
        if s == t:
            return False
        left = 0
        right_s = len(s) - 1
        right_t = len(t) - 1
        while left < len(s) and left < len(t) and s[left] == t[left]:
            left += 1
        while right_s >= left and right_t >= left and s[right_s] == t[right_t]:
            right_s -= 1
            right_t -= 1
        # sample length strings - replace one char
        if len(s) == len(t):
            return right_s - left == 0 and right_t - left == 0
        # s shorter - insert one char
        if len(s) < len(t):
            return right_s - left == -1 and right_t - left == 0
        # s is longer - delete one char
        if len(s) > len(t):
            return right_s - left == 0 and right_t - left == -1
