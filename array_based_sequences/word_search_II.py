"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
from typing import List
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        def _search(j, k, i, word_len):
            if i == word_len - 1: return True

            if j < 0 or j >= m or k < 0 or k >= n or board[j][k] != word[i] or visited[j][k]: return False
            visited[j][k] = True
            if board[j][k] != word[i+1]:
                return False
            
            if _search(j,k+1,i) == word[i+1]:
                visited[j][k+1] == True
                return True
            
            if _search(j+1,k,i) == word[i+1]:
                visited[j+1][k] = True
                return True
            
            if _search(j-1,k,i) == word[i+1]:
                visited[j-1][k] = True
                return True
            
            if _search(j,k-1,i) == word[i+1]:
                visited[j][k-1] = True
                return True
            
            visited[j][k] = False
            return False
            

        m = len(board)
        n = len(board[0])
        if len(board) == 0:
            if len(word) != 0:
                return False
            else:
                return True

        visited = [[False] * n for _ in range(m)]
        for j in range(m):
            for k in range(n):
                _search(j, k, 0, len(word))
        return False





if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    solution = Solution()
    solution.exist(board, word)