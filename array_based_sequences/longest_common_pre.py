"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"    

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1,len(strs)):
            string = strs[i]
            j = 0
            while j < min(len(prefix), len(string)) and prefix[j] == string[j]:
                j += 1
            prefix = prefix[:j]
            if not prefix:
                return ""
        return prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))