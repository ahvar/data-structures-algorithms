from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = sorted(citations, reverse=True)
        hindex = 0
        for i, cite in enumerate(c):
            if cite >= i + 1:
                hindex = i + 1
            else:
                break
        return hindex
