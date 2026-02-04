from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        n = len(matrix)
        for i in range(n):
            m = len(matrix[i])
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
