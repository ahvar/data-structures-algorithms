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
        if strs == None or len(strs) == 0:
            return ""
        pre = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(pre) and i < len(s) and pre[i] == s[i]:
                i += 1
            pre = pre[:i]
            if not pre:
                break
        return pre


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))
