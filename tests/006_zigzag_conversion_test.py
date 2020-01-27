from problems.zigzag_conversion import Solution

subject = Solution()

def test_1():
    s = "PAYPALISHIRING"
    numRows = 3
    result = subject.convert(s, numRows)

    assert result == "PAHNAPLSIIGYIR"

def test_2():
    s = "PAYPALISHIRING"
    numRows = 4
    result = subject.convert(s, numRows)

    assert result == "PINALSIGYAHRPI"
