from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins == None or len(coins) == 0:
            return -1

        n = len(coins)
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
