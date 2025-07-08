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
        n = len(prices)
        holding = [0] * n
        holding[0] = -prices[0]
        cash = [0] * n
        cash[0] = prices[0]
        for i in range(1,n):
            # end day still holding share: hold from yesterday or in cash yesterday and bought today
            holding[i] = max(holding[i-1], cash[i-1] - prices[i])
            # end day in cash: already in cash vs. holding yesterday and sell today
            cash[i] = max(cash[i-1], holding[i-1] + prices[i])
        return cash[n-1]



if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    solution.maxProfit(prices)
