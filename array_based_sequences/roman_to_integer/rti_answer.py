class Solution:
    def romanToInt(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0
        for char in s:
            curr = symbols[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
        return total


if __name__ == "__main__":
    solution = Solution()
    solution.romanToInt()
