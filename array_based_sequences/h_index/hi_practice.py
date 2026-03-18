from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = sorted(citations, reverse=True)
        h = 0
        for i, cite in enumerate(c):
            if cite >= i + 1:
                h = i + 1
            else:
                break
        return h
