from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        flat = [num for row in matrix for num in row]
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (right + left) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] < target:
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
