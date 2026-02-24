from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = [0 for _ in range(n + 1)]
        hold[0] = -prices[0]
        sell = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i - 1])
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i - 1] - fee)
        return sell[n]


class TestSolution:

    def setup_method(self):
        self.prices = [1, 3, 2, 8, 4, 9]
        self.fee = 2

    def test_max_profit(self):
        s = Solution()
        assert s.maxProfit(self.prices, self.fee) == 8
