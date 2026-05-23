class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        power_of_five = 5
        while power_of_five <= n:
            zeroes += n // power_of_five
            power_of_five *= 5
        return zeroes
