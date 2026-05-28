from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box_idx = (row // 3) * 3 + (col // 3)
                if val in rows[row] or val in cols[col] or val in boxes[box_idx]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                boxes[box_idx].add(val)
        return True
