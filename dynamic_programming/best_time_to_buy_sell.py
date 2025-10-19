"""
You are given an array prices where prices[i] is the price of a given stock on the ith day,
and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like,
but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
    
Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


notes:

"""
 
from typing import List
class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if prices == None or len(prices) == 0:
            return 0
        profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy_price + fee:
                profit += prices[i] - buy_price - 1
                buy_price = prices[i] - fee
            elif prices[i] < buy_price:
                buy_price = prices[i]
        return profit



if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    #prices = [1,3]
    fee = 2
    solution = Solution()
    #solution.maxProfit(prices, fee)
    print(solution.maxProfit(prices, fee))