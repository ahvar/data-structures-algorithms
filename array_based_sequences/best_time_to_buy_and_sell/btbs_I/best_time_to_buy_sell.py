from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max_profit(self):
        assert self.solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
