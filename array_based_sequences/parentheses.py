"""
Given n pairs of parentheses, write a function to
generate all combinations of well-formed parentheses.
"""
from typing import List
class Solution:
    def _helper(self, curr, opencount, closecount, n, results):
        if len(curr) == 2 * n:
            results.append(curr)
            return
        if opencount < n:
            self._helper(curr + "(", opencount+1, closecount, n, results)
        if closecount < opencount:
            self._helper(curr + ")", opencount, closecount + 1, n, results)

        return results

    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        curr = ""
        results = self._helper(curr, 0, 0, n, results)
        return results
        





if __name__ == "__main__":
    n = 3
    solution = Solution()
    solution = solution.generateParenthesis(n)
