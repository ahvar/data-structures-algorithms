from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)

        if n == 1:
            return 0

        target = (1 << n) - 1

        queue = deque()
        seen = set()

        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            seen.add((i, mask))
        while queue:
            node, mask, dist = queue.popleft()

            if mask == target:
                return dist

            for nxt in graph[node]:
                next_mask = mask | (1 << nxt)
                state = (nxt, next_mask)

                if state not in seen:
                    seen.add(state)
                    queue.append(nxt, next_mask, dist + 1)
        return -1
