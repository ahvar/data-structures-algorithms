This solution is called "Greedy BFS" because it combines two algorithmic concepts:

BFS (Breadth-First Search) aspect:

It processes indices in "levels" or "waves" - all positions reachable with 1 jump, then all positions reachable with 2 jumps, etc.
current_end marks the boundary of the current level
When i == current_end, you've exhausted all positions in the current level and must move to the next level (increment jumps)
Greedy aspect:

Instead of exploring every position in a level (like true BFS), it greedily tracks only the farthest position reachable
It doesn't need a queue because it only cares about the maximum reach, not which specific positions are visited