"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, 
replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

import unittest

class Solution:
    def isHappy(self, n: int) -> bool:
        count = 1000

        while count > 0:

            normalized_n = [int(char)*int(char) for char in str(n)]
            n = sum(normalized_n)

            if n == 1:
                return True

            count -= 1

        return False
        


class TestSolution(unittest.TestCase):
    def test_is_happy(self):
        s = Solution()

        n = 19
        expected = True
        actual = s.isHappy(n)
        self.assertEqual(actual, expected)

        n = 2
        expected = False
        actual = s.isHappy(n)
        self.assertEqual(actual, expected)


unittest.main()