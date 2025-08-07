"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List
class Solution:
    def _search(self, r, c, index):
        if index == len(self.word): return True
        if r < 0 or r >= self.m or c < 0 or c >= self.n or self.visited[r][c] or self.board[r][c] != word[index]:
            return False
        self.visited[r][c] = True
        
        if self.search(r+1, c, index+1): return True
        if self.search(r-1,c, index+1): return True
        if self._search(r,c+1,index+1): return True
        if self._search(r, c - 1, index + 1): return True

        self.visited[r][c] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [ [False] * self.n for _ in range(self.m)]
        # try each cell as a starting point
        for i in range(self.m):
            for j in range(self.n):
                if self._search(i, j, 0): return True
        return False
        

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)