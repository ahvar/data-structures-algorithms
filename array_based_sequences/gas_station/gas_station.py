from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0  # gas in the tank
        total = 0  # total $ left ?
        n = len(gas)  # length of one loop in circular gas station track
        start = 0  # starting index
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


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert (
            self.solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
            == 3
        )
