from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(s) and i < len(prefix) and prefix[i] == s[i]:
                i += 1
            prefix = prefix[:i]
            if not prefix:
                break

        return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))
