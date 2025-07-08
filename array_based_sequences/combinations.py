"""
Given two integers n and k, return all possible combinations of k numbers chosen from the
range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered
to be the same combination.
"""
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k > n:
            return []
        if k == n:
            return [ [i for i in range(1,n+1) ]]
        if k == 1:
            return [ [i] for i in range(1,n+1) ]
        results = []
        if k == 2:
            for i in range(1, n):
                for j in range(i+1, n+1):
                    results.append([i, j])
            return results
        for left in range(1,n+1):
            j = left + 1
            while j < n+1:
                partial = [right for right in range(j, j + (k-1)) if right <= n]
                partial.append(left)
                results.append(partial)
                j += 1
        return results
            
                


if __name__ == "__main__":
    n = 2
    k = 2
    solution = Solution()
    combos = solution.combine(n, k)
    print(combos)