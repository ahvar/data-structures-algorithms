"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

"""
from typing import List, Tuple
from decimal import Decimal
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False
        
        left = 0
        right_t = len(t) - 1
        right_s = len(s) - 1
        while left <= right_t and left <= right_s and s[left] == t[left]:
            left += 1
        while right_t >= left and right_s >= left and t[right_t] == s[right_s]:
            right_t -= 1
            right_s -= 1
        
        if len(s) == len(t):
            return right_s - left == 0 and right_t - left == 0
        
        if len(s) < len(t):
            return right_t - left == 0 and right_s - left == -1
        
        if len(s) > len(t):
            return right_s - left == 0 and right_t - left == -1
            


        




    


        

        

if __name__ == "__main__":
    solution = Solution()
