"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == None or len(board) == 0 or word == None or word == "":
            return False
        m, n, l = len(board), len(board[0]), len(word)
        visited = [[False] * n for _ in range(m)]

        def search(row, col, index) -> bool:
            if index == l:
                return True
            if (
                row < 0
                or row >= m
                or col < 0
                or col >= n
                or visited[row][col]
                or board[row][col] != word[index]
            ):
                return False

            visited[row][col] = True

            if search(row + 1, col, index + 1):  # down
                return True
            if search(row - 1, col, index + 1):  # up
                return True
            if search(row, col + 1, index + 1):  # right
                return True
            if search(row, col - 1, index + 1):  # left
                return True

            visited[row][col] = False
            return False

        for row in range(m):
            for col in range(n):
                if search(row, col, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)
