"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the
stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None or len(prices) == 0:
            return 0

        hold = [0 for _ in range(len(prices) + 1)]
        hold[0] = -prices[0]
        sell = [0 for _ in range(len(prices) + 1)]

        for i in range(1, len(prices) + 1):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i - 1])
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i - 1])
        return sell[len(prices)]


if __name__ == "__main__":

    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    solution.maxProfit(prices)
