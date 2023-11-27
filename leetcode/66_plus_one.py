"""
You are given a large integer represented as an integer array digits, 

where each digits[i] is the ith digit of the integer.

The digits are ordered from most significant to least significant in left-to-right order. 

The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = str(int("".join([str(digit) for digit in digits])) + 1)
        return [int(char) for char in digits]


class TestSolution(unittest.TestCase):
    def testPlusOne(self):
        s = Solution()

        digits = [1,2,3]
        expected = [1,2,4]
        actual = s.plusOne(digits)
        self.assertEqual(actual, expected)

        digits = [4,3,2,1]
        expected = [4,3,2,2]
        actual = s.plusOne(digits)
        self.assertEqual(actual, expected)

        digits = [9]
        expected = [1,0]
        actual = s.plusOne(digits)
        self.assertEqual(actual, expected)
        

unittest.main()