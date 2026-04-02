from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                box_idx = (row // 3) * 3 + (col % 3)
                if val in rows[row] or val in cols[col] or val in boxes[box_idx]:
                    return False

                rows.add(val)
                cols.add(val)
                boxes.add(val)
        return True
