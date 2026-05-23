from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        grid = [[False] * n for _ in range(m)]

        def _search(row, col, index):
            if index >= len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index] or grid[row][col]:
                return False
            
            grid[row][col] = True

            if _search(row + 1, col):
                return True
            if _search(row - 1, col):
                return True
            if _search(row, col + 1):
                return True
            if _search(row, col - 1):
                return True
            
            grid[row][col] = False
            return False

        for r in range(m):
            for c in range(n):
                if _search(r, c, 0):
                    return True
        return False






if __name__ == "__main__":r
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)
