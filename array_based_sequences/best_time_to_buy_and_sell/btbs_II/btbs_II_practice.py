from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            # if the price today > price yesterday
            # then you would have sold today for the max profit
            # you can make until now
            if prices[i] > prices[i - 1]:
                # if you sold for profit then you bought yesterday
                max_profit += prices[i] - prices[i - 1]
        return max_profit


class TestMaxProfit:
    def setup_method(self):
        self.solution = Solution()

    def test_nominal(self):
        assert self.solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
