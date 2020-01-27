"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

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
"""


"""
P    I    N
A  L S  I G
Y A  H R
P    I

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        length = len(s)

        rows = []
        for index in range(min(length, numRows)):
            rows.append("")

        currentRow = 0 
        goingDown = False
        for pos in range(len(s)):
            rows[currentRow] = rows[currentRow] + s[pos]

            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currentRow = currentRow + 1
            else:
                currentRow = currentRow - 1
        
        return ''.join(rows)
