"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def _search(row, col, index):
            if index == len(word):
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

            if _search(row + 1, col, index + 1):
                return True
            if _search(row - 1, col, index + 1):
                return True
            if _search(row, col + 1, index + 1):
                return True
            if _search(row, col - 1, index + 1):
                return True

            visited[row][col] = False
            return False

        if board == None or len(board) == 0:
            return False
        if word == None or len(word) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if _search(row, col, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)
