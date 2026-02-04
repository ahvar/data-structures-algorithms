from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(row, col, index):
            if index == len(word):
                return True
            if (
                row < 0
                or row >= n
                or col < 0
                or col >= m
                or visited[row][col]
                or board[row][col] != word[index]
            ):
                False

            visited[row][col] = True

            if search(row + 1, col, index + 1):
                return True
            if search(row, col + 1, index + 1):
                return True
            if search(row - 1, col, index + 1):
                return True
            if search(row, col - 1, index + 1):
                return True

            visited[row][col] = False
            return False

        if not board or not word:
            return False

        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if search(row, col, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)
