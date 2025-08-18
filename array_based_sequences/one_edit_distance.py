"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        left = 0
        right_s = len(s) - 1
        right_t = len(s) - 1


        # find first mismatch from left
        while left < len(s) and left < len(t) and s[left] == t[left]:
            left += 1
        # find first mismatch from right
        while right_s >= left and right_t >= left and s[right_s] == t[right_t]:
            right_s -= 1
            right_t -= 1

        # case 1: replace operation
        if len(s) == len(t):
            return right_s - left == 0 and right_t - left == 0
        
        # case 2: insert operation
        elif len(s) < len(t):
            return right_s - left == -1 and right_t - left == 0

        # case 3: delete operation
        elif len(t) > len(s):
            return right_s - left == 0 and right_t - left == -1




if __name__ == "__main__":
    solution = Solution()
        
        
        
        


        
            


