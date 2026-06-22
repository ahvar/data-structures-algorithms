from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            tank += diff
            total += diff

            if tank < 0:
                tank = 0
                start = i + 1

        if total < 0:
            return -1
        return start


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_circuit(self):
        assert (
            self.solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
            == 3
        )
