"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        flat = [num for row in matrix for num in row]
        left, right = 0, len(flat) - 1
        while left <= right:
            mid = (left + right) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    solution = Solution()
    solution.searchMatrix(matrix, target)
