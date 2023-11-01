"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])

        palindrome = True
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i - 1]:
                palindrome = False
            
        return palindrome


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()

        s = "racecar"
        expected = True
        actual = solution.isPalindrome(s)
        self.assertEqual(actual, expected)

        s = "A man, a plan, a canal: Panama"
        expected = True
        actual = solution.isPalindrome(s)
        self.assertEqual(actual, expected)

        s = "race a car"
        expected = False
        actual = solution.isPalindrome(s)
        self.assertEqual(actual, expected)
        
        s = " "
        expected = True
        actual = solution.isPalindrome(s)
        self.assertEqual(actual, expected)

unittest.main()