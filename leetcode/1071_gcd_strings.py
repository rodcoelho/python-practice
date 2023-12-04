"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 

(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

import unittest


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller = str2 if len(str2) < len(str1) else str1
        bigger = str2 if smaller == str1 else str1
        smaller_len = len(smaller)
        smaller_copy = smaller
        bigger_copy = bigger
        index_error_count = 0

        while len(bigger_copy) > 0 or len(smaller) % len(smaller_copy) != 0:

            if index_error_count == len(smaller):
                return ""

            try:
                index = bigger_copy.index(smaller_copy)
            except ValueError:
                index_error_count += 1
                smaller_len -= 1
                
                smaller_copy = smaller[:smaller_len]
                bigger_copy = bigger
                continue

            bigger_copy = bigger_copy[smaller_len:]

        smaller_check = False
        bigger_check = False
        if smaller_copy * (len(smaller) // len(smaller_copy)) == smaller:
            smaller_check = True
        if smaller_copy * (len(bigger) // len(smaller_copy)) == bigger:
            bigger_check = True

        if bigger_check and smaller_check:
            return smaller_copy
        return ""
    
    
class TestSolution(unittest.TestCase):
    def testGCDStrings(self):
        s = Solution()

        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        actual = s.gcdOfStrings(str1, str2)
        self.assertEqual(actual, expected)

        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        actual = s.gcdOfStrings(str1, str2)
        self.assertEqual(actual, expected)

        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        actual = s.gcdOfStrings(str1, str2)
        self.assertEqual(actual, expected)

        str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
        str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
        expected = "TAUXX"
        actual = s.gcdOfStrings(str1, str2)
        self.assertEqual(actual, expected)

        str1 = "EFGABC"
        str2 = "ABC"
        expected = ""
        actual = s.gcdOfStrings(str1, str2)
        self.assertEqual(actual, expected)
        

unittest.main()