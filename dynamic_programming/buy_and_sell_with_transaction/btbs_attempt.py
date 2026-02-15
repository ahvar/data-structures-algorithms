from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold = [0 for _ in range(n + 1)]
        hold[0] = -prices[0]
        sell = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i - 1])
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i - 1] - fee)
        return sell[n]
