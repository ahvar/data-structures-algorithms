from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxx = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                maxx += prices[i] - prices[i - 1]
        return maxx
