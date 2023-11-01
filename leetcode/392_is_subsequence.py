"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

import unittest

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        count = 0
        for char in t:
            if char == s[count]:
                count += 1

                if count == len(s):
                    return True

        return False
        

class TestSolution(unittest.TestCase):
    def test_isSubsequence(self):
        solution = Solution()

        s = "abc"
        t = "ahbgdc"
        expected = True 
        actual = solution.isSubsequence(s, t)
        self.assertEqual(actual, expected)

        s = "b"
        t = "abc"
        expected = True 
        actual = solution.isSubsequence(s, t)
        self.assertEqual(actual, expected)

        s = "axc"
        t = "ahbgdc"
        expected = False
        actual = solution.isSubsequence(s, t)
        self.assertEqual(actual, expected)

        s = ""
        t = "ahbgdc"
        expected = True
        actual = solution.isSubsequence(s, t)
        self.assertEqual(actual, expected)

unittest.main()