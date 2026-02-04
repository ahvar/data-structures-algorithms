from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []

        def _backtrack(permutation):
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for n in nums:
                if n not in permutation:
                    permutation.append(n)
                    _backtrack(permutation)
                    permutation.pop()

        _backtrack([])
        return result
