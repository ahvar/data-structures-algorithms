from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] <= amount else -1


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_coin_change(self):
        assert self.solution.coinChange([1, 2, 5], 11) == 3
