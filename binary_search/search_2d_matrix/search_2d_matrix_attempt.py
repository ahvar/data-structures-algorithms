from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        left = 0
        right = n * m - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1
        return False
