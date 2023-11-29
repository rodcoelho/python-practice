"""
Given an integer n, return the number of trailing zeroes in n!.
"""

import unittest


class Solution:
    def trailingZeroes(self, n: int) -> int:
        product = 1
        for i in range(1, n+1):
            product *= i
        
        zeros = 0
        stringified_product = str(product)
        for char in stringified_product:
            if char == "0":
                zeros += 1
            else:
                zeros = 0
        
        return zeros
    

class TestSolution(unittest.TestCase):
    def testTrailingZeros(self):
        s = Solution()

        n = 3
        expected = 0
        actual = s.trailingZeroes(n)
        self.assertEqual(actual, expected)

        n = 5
        expected = 1
        actual = s.trailingZeroes(n)
        self.assertEqual(actual, expected)

        n = 0
        expected = 0
        actual = s.trailingZeroes(n)
        self.assertEqual(actual, expected)

unittest.main()
