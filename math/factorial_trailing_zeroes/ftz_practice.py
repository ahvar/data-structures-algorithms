class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeroes = 0
        factor_five = 0
        while factor_five <= n:
            count += n // factor_five
            factor_five *= 5
        return count
