from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        holding = [0 for _ in range(n + 1)]
        holding[0] = -prices[0]
        selling = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            holding[i] = max(holding[i - 1], selling[i - 1] - prices[i - 1])
            selling[i] = max(selling[i - 1], holding[i - 1] + prices[i - 1] - fee)
        return selling[n]


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example(self):
        assert self.solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2) == 8
        assert self.solution.maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3) == 6
