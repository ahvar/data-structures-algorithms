from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - min_price > maxx:
                maxx = price - min_price
        return maxx


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_maxx(self):
        assert self.solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
