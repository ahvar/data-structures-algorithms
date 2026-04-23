from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c = sorted(citations, reverse=True)
        hindex = 0
        for idx, cite in enumerate(c):
            if cite >= idx + 1:
                hindex = idx + 1
            else:
                break
        return hindex
