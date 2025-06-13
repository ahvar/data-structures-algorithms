"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
import pprint
pp = pprint.PrettyPrinter(indent=4)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        cols = int(n / 2)
        table = [[' '] * cols for _ in range(numRows)]  
        k = 0
        j = 0
        while k < len(s) - numRows:
            for i in range(numRows): # move vertical (rows)
                table[i][j] = s[k]
                k += 1
            if k > len(s) - 1:
                break
            for i in range(numRows - 2, -1, -1): # move horizontal (cols)
                j += 1
                table[i][j] = s[k]
                k += 1
        output = ""
        for i in range(cols):
            for j in range(numRows):
                if table[i][j] != ' ':
                    output += table[i][j].upper()

        
            
    


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    pp.pprint(solution.convert(s,numRows))