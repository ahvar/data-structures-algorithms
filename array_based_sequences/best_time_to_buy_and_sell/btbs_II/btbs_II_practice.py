from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        prices1 = [7, 1, 9, 1]

        assert self.solution.maxProfit(prices) == 7
        assert self.solution.maxProfit(prices1) == 8
