from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0
        maxx = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxx += prices[i] - prices[i - 1]
        return maxx
