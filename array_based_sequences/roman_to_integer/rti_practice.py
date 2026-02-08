class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        result = 0
        rn = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = 0
        for ch in s:
            curr = rn[ch]
            if curr > prev:

                result += curr - 2 * prev

            else:
                result += curr
            prev = curr
        return result
