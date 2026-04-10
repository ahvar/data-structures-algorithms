from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_profit(self):
        assert self.solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
