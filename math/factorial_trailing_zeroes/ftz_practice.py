class Solution:
    def trailingZeroes(self, n: int) -> int:
        # trailing zeroes come from factors of 10; 2 and 5
        # there are always more 2's than 5's
        count = 0
        power_of_5 = 5
        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5
        return count
