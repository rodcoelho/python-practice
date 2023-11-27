"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)[::-1]
        return palindrome == str(x)

class TestSolution(unittest.TestCase):
    def testIsPalindrome(self):
        s = Solution()

        x = 121
        expected = True
        actual = s.isPalindrome(x)
        self.assertEqual(actual, expected)

        x = -121
        expected = False
        actual = s.isPalindrome(x)
        self.assertEqual(actual, expected)

        x = 10
        expected = False
        actual = s.isPalindrome(x)
        self.assertEqual(actual, expected)

unittest.main()