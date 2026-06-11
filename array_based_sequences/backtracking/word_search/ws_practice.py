from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def search(row, col, index):
            pass

        







if __name__ == "__main__":r
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)
