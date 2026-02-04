import pprint

pp = pprint.PrettyPrinter(indent=4)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        rows = [""] * numRows
        curr_row = 0
        going_down = False
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
