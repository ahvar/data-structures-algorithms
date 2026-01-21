from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        hold = [-prices[0]]
        sell = [0]
        for i in range(1, n):
            new_hold = max(hold[i - 1], sell[i - 1] - prices[i])
            new_sell = max(sell[i - 1], hold[i - 1] + prices[i])
            hold.append(new_hold)
            sell.append(new_sell)
        return sell[n - 1]
