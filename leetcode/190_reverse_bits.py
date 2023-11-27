"""
Reverse bits of a given 32 bits unsigned integer.
"""

import unittest

class Solution:
    def reverseBitsString(self, n: str) -> str:
        final = ""
        for char in n:
            final = char + final

        return final
    
    def reverseBits(self, n: int) -> int:
        stringified = str(n)
        if len(stringified) < 32:
            zeros = (32 - len(stringified)) * "0"
            stringified = zeros + stringified

        stringified = stringified[::-1]
        return int(stringified, 2)



class TestSolution(unittest.TestCase):
    def testReverseBits(self):
        s = Solution()

        n = "00000010100101000001111010011100"
        expected = "00111001011110000010100101000000"
        actual = s.reverseBitsString(n)
        self.assertEqual(actual, expected)

        n = "11111111111111111111111111111101"
        expected = "10111111111111111111111111111111"
        actual = s.reverseBitsString(n)
        self.assertEqual(actual, expected)

        n = 10100101000001111010011100
        expected = 964176192
        actual = s.reverseBits(n)
        self.assertEqual(actual, expected)

        n = 11111111111111111111111111111101
        expected = 3221225471
        actual = s.reverseBits(n)
        self.assertEqual(actual, expected)

        n = 10100101000001111010011100
        expected = 964176192
        actual = s.reverseBits(n)
        self.assertEqual(actual, expected)


unittest.main()
