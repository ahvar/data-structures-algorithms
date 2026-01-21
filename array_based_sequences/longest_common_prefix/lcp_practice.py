from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            i = 0
            while i < len(word) and i < len(prefix) and prefix[i] == word[i]:
                i += 1
            prefix = word[:i]
            if not prefix:
                break
        return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))
