from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                maxx += prices[i] - prices[i - 1]
        return maxx
