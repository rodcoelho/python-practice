
import unittest

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        listified = [[] for d in range(numRows + 1)]

        count = 0
        tmp = 0
        fwd = True
        while count < len(s):
            
            listified[tmp].append(s[count])

            if tmp == 0:
                fwd = True
            elif tmp == numRows -1:
                fwd = False

            if fwd is True:
                tmp += 1
            else:
                tmp -= 1

            count += 1

        final = ""
        for l in listified:
            for element in l:
                final += element
        return final


class TestSolution(unittest.TestCase):
    def test_convert(self):
        solution = Solution()

        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        actual = solution.convert(s, numRows)
        self.assertEqual(actual, expected)

        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        actual = solution.convert(s, numRows)
        self.assertEqual(actual, expected)

        s = "A"
        numRows = 1
        expected = "A"
        actual = solution.convert(s, numRows)
        self.assertEqual(actual, expected)

unittest.main()