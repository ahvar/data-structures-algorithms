from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        total = 0
        n = len(gas)
        for i in range(n):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff

            if tank < 0:
                start = i + 1
                tank = 0

            if total < 0:
                return -1
        return start


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution(gas, cost)
