"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is
less than 150 combinations for the given input.

candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Notes:
1. a list of integers all > than the target cannot sum to the target
2. one list of one integer all == to the target are among the unique combinations of candidate integers

"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.candidates.sort()
        i = len(self.candidates) - 1
        while i >= 0 and self.candidates[i] > target:
            i -= 1
        if i < 0:
            return []
        self.max_i = i
        self.results: List[List[int]] = []
        self._dfs(start=0, remain=target, path=[])
        return self.results

    def _dfs(self, start, remain, path):
        if remain == 0:
            self.results.append(path.copy())
            return
        if start > self.max_i:
            return
        
        ub = self.max_i
        while ub >= start and self.candidates[ub] > remain:
            ub -= 1

        if ub < start:
            return
        
        for i in range(start, ub + 1):
            val = self.candidates[i]
            path.append(val)
            self._dfs(start=i, remain=remain-val, path=path)
            path.pop()

if __name__ == "__main__":
    candidates = [2,3]
    target = 6
    solution = Solution()
    solution.combinationSum(candidates, target)