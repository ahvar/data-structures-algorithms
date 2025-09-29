"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def _search(row, col, index):
            if index == l:
                return True
            # the current row or col is out of bounds for word
            # we already visited the location in the current search
            # the board and word characters don't match
            if row < 0 or row >= n or col < 0 or col >= m or visited[row][col] or board[row][col] != word[index]:
                return False
            
            visited[row][col] = True # record that we've already matched the char at this position
            
            if _search(row+1, col, index + 1):
                return True
            if _search(row-1, col, index + 1):
                return True
            if _search(row, col+1, index + 1):
                return True
            if _search(row, col-1, index + 1):
                return True
            
            visited[row][col] = False # toggle the location back false so we can use it in another search
            return False

        if board == None or word == None or word == "":
            return False
        # get the dimensions of the board and the length of word
        n = len(board)
        m = len(board[0])
        l = len(word)
        # 2D array same dimensions as board so we can track where we've been
        visited = [ [False] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if _search(row, col, 0): # each board position is a potential starting point for word
                    return True
        return False



        

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)