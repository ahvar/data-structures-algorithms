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
        q = deque([1, 0])
        visited = {1}

        while q:
            label, moves = q.popleft()
