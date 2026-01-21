import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        going_down = False
        curr_row = 0
        for c in s:
            rows[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1
        return "".join(rows)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    pp.pprint(solution.convert(s, numRows))
