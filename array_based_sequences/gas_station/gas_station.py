from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        



class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_circuit(self):
        assert (
            self.solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])
            == 3
        )
