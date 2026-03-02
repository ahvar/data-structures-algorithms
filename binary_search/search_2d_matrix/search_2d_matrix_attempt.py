from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = (right + left) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
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
