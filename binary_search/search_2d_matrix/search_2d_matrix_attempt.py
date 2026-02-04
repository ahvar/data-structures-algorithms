from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
