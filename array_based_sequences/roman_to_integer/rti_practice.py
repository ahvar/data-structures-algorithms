class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = []
        total = 0
        prev = 0
        for c in s:
            curr = nums[c]
            if curr < prev:
                total -= curr
            else:
                total += curr
        return total
