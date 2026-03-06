from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_profit(self):
        assert self.solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
