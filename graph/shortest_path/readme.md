# Shortest Path Visiting All Nodes

## Problem Context

You are given an undirected, connected graph with `n` nodes labeled from `0` to `n - 1`.
The graph is represented as an adjacency list named `graph`, where:

- `graph[i]` is the list of all nodes directly connected to node `i`.

### What this means

1. Undirected graph:
If node `a` is connected to node `b`, then `b` is also connected to `a`.

2. Connected graph:
Every node is reachable from every other node (no isolated components).

3. Node labels:
If `n = 5`, valid node IDs are `0, 1, 2, 3, 4`.

4. Adjacency list:
If `graph[0] = [1, 2, 3]`, then node `0` has edges to nodes `1`, `2`, and `3`.

The goal is to return the length of the shortest path that visits every node at least once.
You may:

- start at any node,
- stop at any node,
- revisit nodes,
- reuse edges.

## Core Idea

Use BFS on states, not just nodes.

Each BFS state is:

- current node,
- visited-node mask (bitmask),
- distance (number of edges traveled).

Why this works:

- BFS explores in increasing path length order.
- The first time we reach a state where all nodes are visited, that distance is guaranteed to be minimal.

## Step-by-Step Solution

1. Let `n = len(graph)`.
2. Build the target mask:
   - `target = (1 << n) - 1`
   - This is a bitmask with `n` bits set to `1` (all nodes visited).
3. Multi-source BFS initialization:
   - Start from every node `i` simultaneously.
   - Initial state for node `i`: `(i, 1 << i, 0)`.
   - Add each state to a queue and mark it as seen.
4. BFS loop:
   - Pop `(node, mask, dist)`.
   - If `mask == target`, return `dist`.
   - For each neighbor `nxt` in `graph[node]`:
	 - `next_mask = mask | (1 << nxt)`
	 - If `(nxt, next_mask)` is unseen, add it with distance `dist + 1`.
5. In a connected graph, BFS will always find a valid answer.

## Reference Implementation (Python)

```python
from collections import deque
from typing import List


class Solution:
	def shortestPathLength(self, graph: List[List[int]]) -> int:
		n = len(graph)

		# Single node is already fully visited.
		if n == 1:
			return 0

		target = (1 << n) - 1

		# Multi-source BFS over (node, visited_mask, distance)
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
					queue.append((nxt, next_mask, dist + 1))

		# Should not happen for connected graphs.
		return -1
```

## Quick Trace (Sample 1)

Input:

```python
graph = [[1, 2, 3], [0], [0], [0]]
```

One shortest valid path:

```text
1 -> 0 -> 2 -> 0 -> 3
```

Edges traveled: `4`, so output is `4`.

## Complexity

- Number of states: up to `n * 2^n`
- Time complexity: `O((n + m) * 2^n)` (often simplified to `O(n * 2^n)`)
- Space complexity: `O(n * 2^n)`

Given `n <= 12`, this approach is efficient and standard for this problem.
