from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        if prices == None or len(prices) == 0:
            return 0
        n = len(prices)
        hold = [0 for _ in range(n + 1)]
        hold[0] = -prices[0]
        sell = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], (sell[i - 1] - prices[i - 1]))
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i - 1] - fee)
        return sell[n]


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    # prices = [1,3]
    fee = 2
    solution = Solution()
    # solution.maxProfit(prices, fee)
    print(solution.maxProfit(prices, fee))
