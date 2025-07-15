"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List
class Solution:

    def search_matrix_alt(self, matrix, target):
        if not matrix: return False
        n = len(matrix)
        m = len(matrix[0])
        all_vals = []
        for m in matrix:
            all_vals += m
        left, right = 0, len(all_vals) - 1
        while left <= right:
            mid = ((right - left) // 2) + left
            guess = all_vals[mid]
            if guess == target:
                return True
            if guess < target:
                left = mid + 1
            if guess > target:
                right = mid
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        left_row = 0
        left_col = 0
        right_row = n - 1
        right_col = m - 1
        while left_row < right_row and left_col < right_col:
            mid_row = ((right_row - left_row) // 2 ) + left_row
            mid_col = ((right_col - left_col) // 2) + left_col
            guess = matrix[mid_row][mid_col]
            if guess == target:
                return True
            if guess < target:
                left_row = mid_row + 1
                left_col = 0
            if guess > target:
                right_row = mid_row
                right_col = m - 1
        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    solution = Solution()
    solution.searchMatrix(matrix,target)
