"""
Given two binary strings a and b, return their sum as a binary string.
"""

import unittest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_a_b = int(a, 2) + int(b, 2)
        return "{0:b}".format(sum_a_b)


class TestSolution(unittest.TestCase):
    def testAddBinary(self):
        s = Solution()

        a = "11"
        b = "1"
        expected = "100"
        actual = s.addBinary(a, b)
        self.assertEqual(actual, expected)
        
        a = "1010"
        b = "1011"
        expected = "10101"
        actual = s.addBinary(a, b)
        self.assertEqual(actual, expected)


unittest.main()