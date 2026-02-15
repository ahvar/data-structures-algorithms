from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(row, col, index):
            if index == len(word):
                return True
            if (
                row >= m  # went past last row
                or row < 0  # went past first row
                or col >= n  # went past last column
                or col < 0  # went past first column
                or board[row][col] != word[index]  # char mismatch
                or visited[row][col]  # already looked here
            ):
                return False

            visited[row][col] = True

            if search(row + 1, col, index + 1):
                return True
            if search(row - 1, col, index + 1):
                return True
            if search(row, col + 1, index + 1):
                return True
            if search(row, col - 1, index + 1):
                return True

            visited[row][col] = False
            return False

        if not board or not word:
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
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
