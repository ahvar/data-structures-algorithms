from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = [0 for _ in range(len(prices) + 1)]
        hold[0] = -prices[0]
        sell = [0 for _ in range(len(prices) + 1)]
        for i in range(1, len(prices) + 1):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i - 1])
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i - 1] - fee)
        return sell[len(prices)]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_max(self):
        assert self.solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2) == 8
