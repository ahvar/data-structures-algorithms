import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row_count = 0
        going_down = False
        for c in s:
            rows[row_count] += c

            if row_count == 0 or row_count == numRows - 1:
                going_down = not going_down
            row_count += 1 if going_down else -1
        return "".join(rows)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    pp.pprint(solution.convert(s, numRows))
