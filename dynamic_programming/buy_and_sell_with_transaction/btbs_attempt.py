from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if prices == None or len(prices) == 0:
            return 0
        n = len(prices)
        hold = [0 for _ in range(n + 1)]
        sell = [0 for _ in range(n + 1)]
        hold[0] = -prices[0]
        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(hold[i - 1], sell[i - 1] + prices[i] - fee)
        return sell[n]
