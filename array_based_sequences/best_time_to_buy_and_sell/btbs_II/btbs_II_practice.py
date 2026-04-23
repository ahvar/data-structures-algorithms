from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        for i in range(1, len(prices)):
            # calculate the max profit until the current day
            # if today's price is greater than yesterday
            # then we should buy yesterday and sell at today's price
            # for the max profit available so far
            if prices[i] > prices[i - 1]:
                maxx += prices[i] - prices[i - 1]
        return maxx
