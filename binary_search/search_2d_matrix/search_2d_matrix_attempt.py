from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            if mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class TestSolution:

    def test_search_matrix(self):
        matrix = [[2, 3, 4], [5, 6, 7]]
        target = 5
        s = Solution()
        assert s.searchMatrix(matrix, target)
