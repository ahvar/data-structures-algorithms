from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        n = len(gas)
        m = len(cost)
        tank = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            tank += 1

            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1
        return start
