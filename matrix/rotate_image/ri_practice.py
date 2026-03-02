from typing import List
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        for i in range(m):
            n = len(matrix[i])
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pp.pprint(matrix)
    print("--------------")
    pp.pprint(solution.rotate(matrix))
