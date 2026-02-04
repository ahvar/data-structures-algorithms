from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def to_pos(label: int) -> tuple[int, int]:
            r = (label - 1) // n
            c = (label - 1) % n
            row = n - 1 - r
            if r % 2 == 1:
                c = n - 1 - c
            return row, c

        target = n * n
        q = deque([(1, 0)])
        visited = {1}

        while q:
            label, moves = q.popleft()
            if label == target:
                return moves
            for nxt in range(label + 1, min(label + 6, target) + 1):
                r, c = to_pos(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dest not in visited:
                    visited.add(dest)
                    q.append((dest, moves + 1))
        return -1
